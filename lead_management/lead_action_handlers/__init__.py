from lead_management.lead_action_handlers.add_reminder_handler import AddReminderActionHandler
from lead_management.lead_action_handlers.log_call_handler import LogCallActionHandler
from lead_management.lead_action_handlers.send_profile_handler import SendProfileActionHandler


class Types(object):
    LOG_CALL = 'log_call'
    SEND_PROFILE = 'send_profile'
    ADD_REMINDER = 'add_reminder'


HANDLER_MAP = {
    Types.LOG_CALL: LogCallActionHandler,
    Types.SEND_PROFILE: SendProfileActionHandler,
    Types.ADD_REMINDER: AddReminderActionHandler,
}


def get_handler(action_type):
    try:
        return HANDLER_MAP[action_type]
    except KeyError:
        raise RuntimeError('Handler for action: {a} not defined'.format(a=action_type))
