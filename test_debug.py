from testrail_api import TestRailAPI

from configz.testrail import TESTRAIL_DOMAIN_URL, TESTRAIL_USERNAME, TESTRAIL_PASSWORD

api = TestRailAPI(TESTRAIL_DOMAIN_URL, TESTRAIL_USERNAME, TESTRAIL_PASSWORD)


def test_compare_status():
    last_two_results = api.results.get_results(test_id=980542)[0:2]
    if last_two_results[0].get('status_id') != last_two_results[1].get('status_id'):
        if last_two_results[0].get('status_id') == 1:
            print(f"The test for case is now Pass")
        elif last_two_results[0].get('status_id') == 5:
            print(f"The test for case is now Failed")
    else:
        pass


def test_get_cases_from_run():
    list_of_tests = api.tests.get_tests(run_id=4237)
    list_of_test_id = []
    for each_test in list_of_tests:
        list_of_test_id.append(each_test.get('id'))
    print(list_of_test_id)
    print(list_of_test_id.__len__())


def test_get_run_name():
    api.runs.get_run(run_id=4237).get('name')











