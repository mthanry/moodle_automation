import requests
from bs4 import BeautifulSoup as bs
from requests import post
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Constant for the Moodle api
KEY      = '8cc87cf406775101c2df87b07b3a170d'
URL      = 'https://034f8a1dcb5c.eu.ngrok.io'
ENDPOINT ='/webservice/rest/server.php'
courseid = 5

VIDEO_REPOSITORY = 'https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX'


################################################
# Rest-Api functions and classes
# https://github.com/corvus-albus/corvus-albus-moodle-local_wsmanagesections-script-example
################################################

def rest_api_parameters(in_args, prefix='', out_dict=None):
    """Transform dictionary/array structure to a flat dictionary, with key names
    defining the structure.
    Example usage:
    >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
    {'courses[0][id]':1,
     'courses[0][name]':'course1'}
    """
    if out_dict==None:
        out_dict = {}
    if not type(in_args) in (list,dict):
        out_dict[prefix] = in_args
        return out_dict
    if prefix == '':
        prefix = prefix + '{0}'
    else:
        prefix = prefix + '[{0}]'
    if type(in_args)==list:
        for idx, item in enumerate(in_args):
            rest_api_parameters(item, prefix.format(idx), out_dict)
    elif type(in_args)==dict:
        for key, item in in_args.items():
            rest_api_parameters(item, prefix.format(key), out_dict)
    return out_dict

def call(fname, **kwargs):
    """Calls moodle API function with function name fname and keyword arguments.
    Example:
    >>> call_mdl_function('core_course_update_courses',
                           courses = [{'id': 1, 'fullname': 'My favorite course'}])
    """
    parameters = rest_api_parameters(kwargs)
    parameters.update({"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
    #print(parameters)
    response = post(URL+ENDPOINT, data=parameters).json()
    if type(response) == dict and response.get('exception'):
        raise SystemError("Error calling Moodle API\n", response)
    return response

class LocalGetSections(object):
    """Get settings of sections. Requires courseid. Optional you can specify sections via number or id."""
    def __init__(self, cid, secnums = [], secids = []):
        self.getsections = call('local_wsmanagesections_get_sections', courseid = cid, sectionnumbers = secnums, sectionids = secids)

class LocalUpdateSections(object):
    """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""
    def __init__(self, cid, sectionsdata):
        self.updatesections = call('local_wsmanagesections_update_sections', courseid = cid, sections = sectionsdata)

################################################
# Helper functions
################################################

# Get list of google videos
def get_gvideos(g_drive_folder, video_url_base = 'https://drive.google.com/file/d/', vid_tag_class = 'Q5txwe'):

    req = requests.get(g_drive_folder)
    soup = bs(req.text, 'html.parser')

    videos = soup.find_all('div',class_ = vid_tag_class)
    videos_details = []
    
    for video in videos:
        video_title = video.text
        video_date = re.search(r'(\d{4}-\d{2}-\d{2})',video_title)
        video_id = video.parent.parent.parent.parent.attrs['data-id']   

        video_detail = {
            'id': video_id,
            'url': video_url_base + video_id,
            'title': video_title,
            'date': datetime.strptime(video_date.group(), '%Y-%m-%d')
        }
    
        videos_details.append(video_detail)
        
    return videos_details

def missing_gvideo(video, section):
    if video['date'] > section['start'] and video['date'] <= section['end']:
        #the dates match. Is the video id found in section summary?
        summary = bs(section['summary'], 'html.parser')
        if summary.find(string=video['title']):
            return False
        else:
            return True
    return False

# Get date object based on day month closest from now
def closest_date(day_month, format = '%d %B'):
    '''
        Assumes and returns a date based on how close it is from now

        Parameters:
            day: day of the month
            month: name of the month
            format: specify the format of the day and month. Default is %d %B (4 January)

        Returns:
            date: datetime object representing the closest day month
        
    '''
    now = datetime.today()
    curr_date = datetime.strptime(day_month + ' ' + str(now.year), format + ' %Y')
    last_date = curr_date - relativedelta(years=1)
    next_date = curr_date + relativedelta(years=1)
    
    return min([curr_date,last_date,next_date], key=lambda x: abs(x - now))




all_gvideos = get_gvideos(VIDEO_REPOSITORY)



# Get all sections details as an iterable
sec = LocalGetSections(courseid)
all_sections = []

for section in sec.getsections:
    dates = re.findall(r'(\d{1,2} \w{3,})',section['name'])
    
    if len(dates) == 2:
        start   = closest_date(dates[0])
        end     = closest_date(dates[1])
    else:
        start   = None
        end     = None

    section_details = {
        'num'   : section['sectionnum'],
        'start'         : start,
        'end'           : end,
        'name'  :section['name'],
        'summary': section['summary']
    }

    all_sections.append(section_details)


updates = []

for section in all_sections:
    
    # Are there google videos for the sections?
    if section['start'] == None or section['end'] == None:
        continue
    else:
        missing_gvideos = list(filter(lambda gvideo: missing_gvideo(gvideo, section), all_gvideos))
        
        # Amend summaries with unpublished videos
        for missing_video in missing_gvideos:
            summary = bs(section['summary'], 'html.parser')
            new_link = summary.new_tag('a', href=missing_video['url'])
            new_link.string = missing_video['title']

            section['summary'] += '<p>' + str(new_link) + '</p>'


        # Add the modified summaries to pending updates
        updates.append(
            {
                'section': section['num'],
                'summary': section['summary']
            }
        )
        
data = [{
    'section': 1,
    'summary': ''
}] 
sec = LocalUpdateSections(courseid, data)
print(sec.updatesections)












class Moodle_section():
    def __init__(self, section):
        self.num        = section['num']
        self.name       = section['name']
        self.summary    = section['summary']

        dates = re.findall(r'(\d{1,2} \w{3,})',self.name)
    
        if len(dates) == 2:
            self.start  = closest_date(dates[0])
            self.end    = closest_date(dates[1])
        else:
            self.start  = None
            self.end    = None

        self.published_links = []
        self.new_links = []








################################################
# Examples
################################################

# # Get all sections of the course.
# sec = LocalGetSections(courseid)
# # Get sections ids of the course with the given numbers.
# #sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6])
# # Get sections ids of the course with the given ids.
# #sec = LocalGetSections(courseid, [], [7186, 7187, 7188, 7189])
# # Get sections ids of the course with the given numbers and given ids.
# #sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6], [7186, 7187, 7188, 7189])
# print(sec.getsections)


# Update sections. Example for onetopic format.
# data = [{   'type': 'num', 
#             'section': 4, 
#             'name': 'Four§', 
#             'summary': '<p>section FOUR</p>', 
#             'summaryformat': 1, 
#             'visible': 1 , 
#             'highlight': 0, 
#             'sectionformatoptions': [{'name': 'level', 'value': '1'}]},\
#         {   'type': 'num', 
#             'section': 3, 
#             'name': '3', 
#             'summary': '<p>section THREE</p>', 
#             'summaryformat': 1, 
#             'visible': 0 , 
#             'highlight': 0, 
#             'sectionformatoptions': [{'name': 'level', 'value': '0'}]}
# ]

# sec = LocalUpdateSections(courseid, data)
# print(sec.updatesections)


# Get sections ids of the course with the given numbers.
sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6])


# Get sections ids of the course with the given ids.
#sec = LocalGetSections(courseid, [], [7186, 7187, 7188, 7189])
# Get sections ids of the course with the given numbers and given ids.
#sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6], [7186, 7187, 7188, 7189])

