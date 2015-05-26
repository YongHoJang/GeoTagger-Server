import json
import random
from flask import current_app, url_for



class SurveyFormItem:
    '''
    Survey Form Item Basic Class
    '''
    def __init__(self, item_num, item_type, question,note=None):
        self.item_num = item_num
        self.item_type = item_type
        self.question = question # string
        self.note = note # string
    
        

class SurveyFormCheckboxe(SurveyFormItem):
    '''
    Survey Form Item for checkboxes
    '''
    def __init__(self, item_num, question, choices, note=None):
        SurveyFormItem.__init__(self, item_num, "checkbox", question, note)
        self.choices = choices
    
    def to_html(self):
        result_str = '<br/>'
        label_template = '<span class="form_question"><label>%s</label></span><br/>'
        note_template = '<span class="form_note"><label>%s</label></span><br/>'
        choice_template = '<input type="checkbox" name="%s" value="%s">%s</input><br/> '
        
        result_str = result_str + (label_template % self.question)
        
        if self.note is not None:
            note_str = note_template % self.note
            result_str = result_str + note_str
         
        for choice in self.choices:
            group_name = self.item_num + 'group' 
            line_str = choice_template % (group_name, choice, choice) 
            resutl_str = result_str + template
        
        return result_str
        
    
    
class SurveyFormRadio(SurveyFormItem):
    '''
    Survey Form Item for radio buttons
    '''
    def __init__(self, item_num, question, choices, note=None):    
        SurveyFormItem.__init__(self, item_num, "radio", question, note)
        self.choices = choices
    
    def to_html(self):
        result_str = '<br/>'
        label_template = '<span class="form_question"><label>%s</label></span><br/>'
        note_template = '<span class="form_note"><label>%s</label></span><br/>'
        choice_template = '<input type="radio" name="%s" value="%s">%s</input><br/> '
        
        result_str = result_str + (label_template % self.question)
        
        if self.note is not None:
            note_str = note_template % self.note
            result_str = result_str + note_str
         
        for choice in self.choices:
            group_name = self.item_num + 'group' 
            line_str = choice_template % (group_name, choice, choice) 
            resutl_str = result_str + template
        
        return result_str
        
    
class SurveyFormFreetext(SurveyFormItem):
    '''
    Survey Form Item for textarea
    '''
    def __init__(self, item_num, question, choices, note=None):    
        SurveyFormItem.__init__(self, item_num, "textarea", question, note)
        self.choices = choices
        
        
    def to_html(self):
        result_str = '<br/>'
        label_template = '<span class="form_question"><label>%s</label></span><br/>'
        note_template = '<span class="form_note"><label>%s</label></span><br/>'
        textarea_template = '<textarea name="%s"></textarea><br/> '
        
        result_str = result_str + (label_template % self.question)
        
        if self.note is not None:
            note_str = note_template % self.note
            result_str = result_str + note_str
         
        resutl_str = result_str + (textarea_template % item_num)
        
        return result_str


class SurveyForm:
    '''
    SurveyForm holds information about how to generate a survey form by reading
    json-based form structure data.
    '''

    def __init__(self, form_name, form_json, form_id=None):
        if (form_id is None):
           form_id = SurveyForm.generate_form_id() 
        # Set attributes
        self.form_name = form_name
        self.form_id = form_id
        self.questions = []
        self.form_json = None


    def save(self):
        pass
    
    
    def load_json(self, form_json):
        self.form_json = form_json
        
             
    def to_json(self):
        return self.form_json
    
              
    def to_html(self, dest_url):
        json_data = '''
        { "form_id":1234567890,
            "items":[
                        {"type":"radio", "question":"is boolean?", "note":"This is a boolian note.","choices":["Yes", "No"]},
                        {"type":"checkbox", "question":"Check as many as you wont.", "note":"This is a checkbox note.",
                            "choices":["Evangelism", "Mercy", "Training"]},
                        {"type":"freetext", "question":"Type what you want", "note":"This is a freetext note."}
                    ]
        }         
        '''
        json_obj = json.loads(json_data)
        html_str = '''<form action="%s">''' % dest_url
        html_end= '</form>'
        items = json_obj['items']
        item_num = 0
        
        for item in items:
            item_type = item['type']
            question = item['question']
            
            note = None
            if ( 'note' in item):
                note = item['note']
            
            choices = None 
            if ('choices' in item):
                choices = item['choices']
                           
            converted_html_str = SurveyForm.convert_to_form_html(item_num, 
                item_type, question, note, choices)
                
            html_str = html_str + converted_html_str
        
        html_str = html_str + html_end
            
        return html_str
        
        
    @staticmethod
    def generate_form_id():
        '''
        Generates a form id
        '''
        r_num = 10 # the length of form_id
        char_range = string.ascii_lowercase + string.digits
        mongo = current_app._get_current_object().data.driver
        form_id = ''.join(random.choice(char_range) for x in range(r_num))
        # Check if form_id is unique. If not, generate it again.
        while True: 
            surveyform = mongo.db.surveyforms.find_one({'form_id': form_id})
            if surveyform is None:
                break
            form_id = ''.join(random.choice(char_range) for x in range(r_num))
        
        return form_id
    
    
    @staticmethod
    def create():
        pass
        
    @staticmethod
    def fetch(form_id):
        pass
    
    @staticmethod
    def convert_to_form_html(item_num, item_type, question, note, choices):
        if (item_type == 'checkbox'):

            result_str = '<br/>'
            label_template = '<span class="form_question"><label>%s</label></span><br/>'
            note_template = '<span class="form_note"><label>%s</label></span><br/>'
            choice_template = '<input type="checkbox" name="%s" value="%s">%s</input><br/> '
        
            result_str = result_str + (label_template % question)
        
            if note is not None:
                note_str = note_template % note
                result_str = result_str + note_str
         
            for choice in choices:
                group_name = str(item_num) + 'group' 
                line_str = choice_template % (group_name, choice, choice) 
                result_str = result_str + line_str
        
            return result_str

        elif (item_type == 'radio'):

            result_str = '<br/>'
            label_template = '<span class="form_question"><label>%s</label></span><br/>'
            note_template = '<span class="form_note"><label>%s</label></span><br/>'
            choice_template = '<input type="radio" name="%s" value="%s">%s</input><br/> '
        
            result_str = result_str + (label_template % question)
        
            if note is not None:
                note_str = note_template % note
                result_str = result_str + note_str
         
            for choice in choices:
                group_name = str(item_num) + 'group' 
                line_str = choice_template % (group_name, choice, choice) 
                result_str = result_str + line_str
        
            return result_str            
            
        elif (item_type == 'freetext'):

            result_str = '<br/>'
            label_template = '<span class="form_question"><label>%s</label></span><br/>'
            note_template = '<span class="form_note"><label>%s</label></span><br/>'
            textarea_template = '<textarea name="%s"></textarea><br/> '
        
            result_str = result_str + (label_template % question)
        
            if note is not None:
                note_str = note_template % note
                result_str = result_str + note_str
         
            result_str = result_str + (textarea_template % item_num)
        
            return result_str

        else:
            return ''
        
    
    
    
    
    

