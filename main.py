from call_api import call_api
from check_status import check_job_status

thing_name = 'KEN0362216'
resources = [
    {
        'resource_id': 'x57edx',
        'path_with_query_string': f'/jobs/meter/{thing_name}/openMeterValve',
        'payload': {"meterType": "P4-MQTT"}
    },
    {
        'resource_id': 'lellvt',
        'path_with_query_string': f'/jobs/meter/{thing_name}/openMeterLock',
        'payload': {"meterType": "P4-MQTT"}
    },
    {
        'resource_id': 'vctj1u',
        'path_with_query_string': f'/jobs/meter/{thing_name}/adjustData',
        'payload': {
            "meterType": "P4-MQTT",
            "customerId": "1191522",
            "creditRemaining": 20,
            "gasRemaining": 12,
            "unitPrice": 290,
            "cylinderSerial": "12",
            "meterChangeDate": 1719924942
        }
    },
    {
        'resource_id': 'h9h3hd',
        'path_with_query_string': f'/jobs/meter/{thing_name}/changeBattery',
        'payload': {
            "meterType": "P4-MQTT",
            "batteryModel": "EEDSGGT",
            "batteryQuantity": 19000,
            "batterySerialNumberList": "2"
        }
    },
    {
        'resource_id': '9lxr6h',
        'path_with_query_string': f'/jobs/meter/{thing_name}/getMeterStatus',
        'payload': {"meterType": "P4-MQTT"}
    }
]

def automate_job_status_check(resource):
    job_id = call_api(resource, thing_name)

    if job_id:
        check_job_status(job_id, thing_name)
    else:
        print("Failed to retrieve Job ID. Exiting...")

if __name__ == "__main__":
    for resource in resources:
        automate_job_status_check(resource)
