from mycroft import MycroftSkill, intent_file_handler


class Whyclassification(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('whyclassification.intent')
    def handle_whyclassification(self, message):
        self.speak_dialog('whyclassification')


def create_skill():
    return Whyclassification()

