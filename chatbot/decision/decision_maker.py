from chatbot.common.chat_share_data import ShareData
from chatbot.story.story_board_manager import StoryBoardManager
from chatbot.services.service_provider import ServiceProvider
from chatbot.common.chat_story_conf_data import ChatStoryConfData


class DecisionMaker(ShareData):
    """
    (1) check intend is clear , if not return intend select list
    (2) check intend service type (story board, ontology and etc)
    """
    def __init__(self, dict_conf):
        self.dict_conf = dict_conf

    def run(self, share_data):
        """

        :param share_data:
        :return:
        """
        try :
            if(len(share_data.get_intent_id()) == 0):
                pass
            else:
                intent_conf = ChatStoryConfData(share_data.get_intent_id()[0])
                if(len(share_data.get_intent_id()) > 1 or len(intent_conf.get_intent_story()) == 0):
                    share_data.set_output_data("Story not Set")
                    pass
                elif(len(share_data.get_intent_id()) == 1):
                    if (not self._check_essential_entity(share_data.get_story_slot_entity().keys(), share_data)):
                        pass
                    elif(intent_conf.get_intent_story()[0]['fields']['story_type'] == 'response'):
                        response_story = intent_conf.get_story_response(intent_conf.get_intent_story()[0]['pk'])
                        share_data = StoryBoardManager(response_story).run(share_data)
                    elif(intent_conf.get_intent_story()[0]['fields']['story_type'] == 'service'):
                        service_story = intent_conf.get_story_service(intent_conf.get_intent_story()[0]['pk'])
                        share_data = ServiceProvider(service_story).run(share_data)
                    else:
                        share_data.set_output_data("무슨말인지 모르겠어요")
                        #share_data.initialize_story()
                else: #intent 3개 이상
                    share_data.set_output_data("무슨말인지 모르겠어요")
            return share_data
        except Exception as e:
            raise Exception(e)

    def _check_essential_entity(self, entity_list, share_data):
        check_value = True
        for entity in self.dict_conf.get_entity_key(share_data.get_intent_id()[0]):
            if (entity in entity_list):
                pass
            else:
                share_data.set_output_data(entity + " 값을 입력해 주세요")
                #Story상 필수 Slot값이 없을 경우 필요한 Slot 값을 출력
                key_slot = self.dict_conf.get_entity_key(share_data.get_intent_id()[0])
                input_slot = list(share_data.get_story_slot_entity().keys())
                need_slot = [x for x in key_slot if x not in input_slot]
                share_data.set_output_data(' '.join(need_slot) + " 값을 입력해 주세요")
                check_value = False
                break
        return check_value