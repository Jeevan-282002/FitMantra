import logging
from rest_framework.response import Response
from rest_framework import status
from FitJeeva import error_messege_conf


logger = logging.getLogger("rvsf")
logger_excp = logging.getLogger('rvsf_excp')
cron_logger = logging.getLogger('rvsf_cron')
cron_logger_excp = logging.getLogger('rvsf_cron_excp')


def main_exception(view, exception=None, function_name=None, user=None, error_message=None):
    logger.error(exception)
    logger.exception("Exception raised in {} as {}".format(view, str(exception)))
    logger_excp.error(exception)
    logger_excp.exception(
        "Exception raised in {} as {}".format(view, str(exception)))
    if error_message:
        return Response(error_message, status=status.HTTP_412_PRECONDITION_FAILED)



def start_logger_info(view, request,source=None):
    if source =='cron':
        cron_logger.info("{} started....".format(view))
        cron_logger.info(request)
        return True
    else:
        logger.info("{} started....".format(view))
        logger.info(request)
        return True


def end_logger_info(view, response, desc=None,source=None):
    if source =='cron':
        cron_logger.info("{} DESC = {} ended....".format(view, desc))
        cron_logger.info(response)
        return True
    else:
        logger.info("{} DESC = {} ended....".format(view, desc))
        logger.info(response)
        return True


def basic_response(message, status, view=None, desc=None):
    end_logger_info(view, message, desc)
    return Response(message, status=status)


def helper_error(view, exception, function_name=None, user=None,source=None):
    if source =='cron':
        cron_logger.error(view)
        cron_logger_excp.exception("Exception raised in {},function_name={} as {}".format(view, function_name, str(exception)))
        cron_logger_excp.error(exception)
        return False
    else:
        logger.error(view)
        logger.exception("Exception raised in {},function_name={} as {}".format(view, function_name, str(exception)))
        logger_excp.error(exception)
        logger_excp.exception(
            "Exception raised in {} as {}".format(view, str(exception)))
        error_shared_request = {
            "user": user,
            "function_name": function_name,
            "error": str(exception)
        }
        shared.error_log(error_shared_request)
        return False


def logger_info(str):
    logger.info(str)
    logger_excp.info(str)

def cron_logger_info(str):
    cron_logger.info(str)
