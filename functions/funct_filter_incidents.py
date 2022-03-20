# -*- coding: utf-8 -*-

"""AppFunction implementation"""
import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient import SimpleHTTPException



PACKAGE_NAME = "filterincidents"
FN_NAME = "filter_incidents"

INCIDENT_QUERY_PAGED = "/incidents/query_paged"
QUERY_PAGED_RETURN_LEVEL = "?return_level=normal"

LOG = logging.getLogger(__name__)
class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'filter_incidents'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.param1
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        yield StatusMessage("Searching...")
        try:

            filter = {
                "filters": [
                    {
                        "conditions": [
                            {
                            "field_name": "create_date",
                            "method": "gte",
                            "value": 1645603140
                            }
                        ]
                    }
                ],
                "sorts":[],
                "start":10,
                "length":100
            }
            url = "{}{}".format(INCIDENT_QUERY_PAGED, QUERY_PAGED_RETURN_LEVEL)
            search_results = self.rest_client().post(url, filter)
            totalresults=search_results['recordsTotal']
            data=search_results['data']
            print("Total %s records found!" % str(totalresults))
            for row in data:
                print("Incident name is %s, owner id is %s, creator: %s" % (str(row['name']),str(row['owner_id']),str(row['creator']['email'])))
            reason = None
        except SimpleHTTPException as err:
            search_results = None
            reason = "Check input fields: {}".format(str(err))
            LOG.error(reason)


        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implemtation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()
        #
        # yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        #
        # yield FunctionResult(results)
        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        results = {"mock_key": "Mock Value!"}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
