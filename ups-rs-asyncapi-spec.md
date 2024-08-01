# DICOM UPS-RS WebSocket API 1.0.0 documentation

* Specification ID: `urn:com:example:dicom:ups-rs:api`
* License: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
* Default content type: [application/json](https://www.iana.org/assignments/media-types/application/json)
* Support: [API Support](https://www.example.com/support)
* Email support: [support@example.com](mailto:support@example.com)

AsyncAPI 2.6.0 specification for UPS-RS WebSocket-based subscription and notification
##### Specification tags

| Name | Description | Documentation |
|---|---|---|
| UPS | Unified Procedure Step | - |
| DICOM | Digital Imaging and Communications in Medicine | - |


## Table of Contents

* [Servers](#servers)
  * [production](#production-server)
* [Operations](#operations)
  * [PUB /workitems/subscription](#pub-workitemssubscription-operation)
  * [SUB /workitems/subscription](#sub-workitemssubscription-operation)
  * [PUB /workitems/subscription/{subscriptionUID}](#pub-workitemssubscriptionsubscriptionuid-operation)
  * [SUB /workitems/subscription/{subscriptionUID}](#sub-workitemssubscriptionsubscriptionuid-operation)

## Servers

### `production` Server

* URL: `example.com/ups-rs`
* Protocol: `wss`

Production UPS-RS WebSocket server


## Operations

### PUB `/workitems/subscription` Operation

*Receive UPS Workitem event notifications*

* Operation ID: `receiveWorkitemNotifications`

#### Message General UPS Workitem Event Notification `ups.workitem.event.notification.general`

##### Payload

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| (root) | object | - | - | - | **additional properties are allowed** |
| eventType | string | - | allowed (`"CREATED"`, `"UPDATED"`, `"STATE_REPORT"`, `"CANCELED"`, `"COMPLETED"`) | - | **required** |
| workitemUID | string | - | - | - | **required** |
| subscriptionUID | string | - | - | - | - |
| procedureStepState | string | - | allowed (`"SCHEDULED"`, `"IN PROGRESS"`, `"COMPLETED"`, `"CANCELED"`) | - | - |
| progressInformation | object | - | - | - | **additional properties are allowed** |
| progressInformation.numberOfCompletedSuboperations | integer | - | - | - | - |
| progressInformation.numberOfFailedSuboperations | integer | - | - | - | - |
| progressInformation.numberOfWarningSuboperations | integer | - | - | - | - |
| progressInformation.numberOfRemainingSuboperations | integer | - | - | - | - |
| cancellationReason | string | - | - | - | - |
| workitem | object | - | - | - | **additional properties are allowed** |
| workitem.workitemUID | string | - | - | - | **required** |
| workitem.procedureStepState | string | - | allowed (`"SCHEDULED"`, `"IN PROGRESS"`, `"COMPLETED"`, `"CANCELED"`) | - | **required** |
| workitem.scheduledProcedureStepStartDateTime | string | - | - | format (`date-time`) | **required** |
| workitem.scheduledWorkitemCodeSequence | object | - | - | - | **required**, **additional properties are allowed** |
| workitem.scheduledWorkitemCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledWorkitemCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledWorkitemCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.inputInformationSequence | array<object> | - | - | - | **required** |
| workitem.inputInformationSequence.studyInstanceUID | string | - | - | - | - |
| workitem.inputInformationSequence.seriesInstanceUID | string | - | - | - | - |
| workitem.scheduledStationNameCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationNameCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationNameCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationNameCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationClassCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationGeographicLocationCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence | array<object> | - | - | - | - |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerName | string | - | - | - | - |
| workitem.scheduledProcedureStepDescription | string | - | - | - | - |
| workitem.scheduledProtocolCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledProtocolCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledProtocolCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledProtocolCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.referencedRequestSequence | array<object> | - | - | - | - |
| workitem.referencedRequestSequence.studyInstanceUID | string | - | - | - | - |
| workitem.referencedRequestSequence.accessionNumber | string | - | - | - | - |
| workitem.referencedRequestSequence.requestedProcedureID | string | - | - | - | - |
| workitem.referencedRequestSequence.requestedProcedureDescription | string | - | - | - | - |

> Examples of payload _(generated)_

```json
{
  "eventType": "CREATED",
  "workitemUID": "string",
  "subscriptionUID": "string",
  "procedureStepState": "SCHEDULED",
  "progressInformation": {
    "numberOfCompletedSuboperations": 0,
    "numberOfFailedSuboperations": 0,
    "numberOfWarningSuboperations": 0,
    "numberOfRemainingSuboperations": 0
  },
  "cancellationReason": "string",
  "workitem": {
    "workitemUID": "string",
    "procedureStepState": "SCHEDULED",
    "scheduledProcedureStepStartDateTime": "2019-08-24T14:15:22Z",
    "scheduledWorkitemCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "inputInformationSequence": [
      {
        "studyInstanceUID": "string",
        "seriesInstanceUID": "string"
      }
    ],
    "scheduledStationNameCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledStationClassCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledStationGeographicLocationCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledHumanPerformersSequence": [
      {
        "humanPerformerCodeSequence": {
          "codeValue": "string",
          "codingSchemeDesignator": "string",
          "codeMeaning": "string"
        },
        "humanPerformerName": "string"
      }
    ],
    "scheduledProcedureStepDescription": "string",
    "scheduledProtocolCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "referencedRequestSequence": [
      {
        "studyInstanceUID": "string",
        "accessionNumber": "string",
        "requestedProcedureID": "string",
        "requestedProcedureDescription": "string"
      }
    ]
  }
}
```



### SUB `/workitems/subscription` Operation

*Subscribe to UPS Workitem events*

* Operation ID: `subscribeToWorkitems`

#### Message UPS Workitem Subscription Request `ups.workitem.subscription.request`

##### Payload

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| (root) | object | - | - | - | **additional properties are allowed** |
| filter | object | - | - | - | **required**, **additional properties are allowed** |
| filter.worklistLabel | string | - | - | - | - |
| filter.procedureStepState | string | - | allowed (`"SCHEDULED"`, `"IN PROGRESS"`, `"COMPLETED"`, `"CANCELED"`) | - | - |
| filter.scheduledStationAETitle | string | - | - | - | - |
| filter.performerAETitle | string | - | - | - | - |
| deleteSubscription | boolean | If true, delete any existing subscriptions matching the filter | - | - | - |

> Examples of payload _(generated)_

```json
{
  "filter": {
    "worklistLabel": "string",
    "procedureStepState": "SCHEDULED",
    "scheduledStationAETitle": "string",
    "performerAETitle": "string"
  },
  "deleteSubscription": true
}
```



### PUB `/workitems/subscription/{subscriptionUID}` Operation

*Receive UPS Workitem event notifications for a specific subscription*

* Operation ID: `receiveSpecificSubscriptionNotifications`

#### Parameters

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| subscriptionUID | string | Unique identifier for the subscription | - | - | **required** |


#### Message Specific UPS Workitem Event Notification `ups.workitem.event.notification.specific`

##### Payload

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| (root) | object | - | - | - | **additional properties are allowed** |
| eventType | string | - | allowed (`"CREATED"`, `"UPDATED"`, `"STATE_REPORT"`, `"CANCELED"`, `"COMPLETED"`) | - | **required** |
| workitemUID | string | - | - | - | **required** |
| subscriptionUID | string | - | - | - | - |
| procedureStepState | string | - | allowed (`"SCHEDULED"`, `"IN PROGRESS"`, `"COMPLETED"`, `"CANCELED"`) | - | - |
| progressInformation | object | - | - | - | **additional properties are allowed** |
| progressInformation.numberOfCompletedSuboperations | integer | - | - | - | - |
| progressInformation.numberOfFailedSuboperations | integer | - | - | - | - |
| progressInformation.numberOfWarningSuboperations | integer | - | - | - | - |
| progressInformation.numberOfRemainingSuboperations | integer | - | - | - | - |
| cancellationReason | string | - | - | - | - |
| workitem | object | - | - | - | **additional properties are allowed** |
| workitem.workitemUID | string | - | - | - | **required** |
| workitem.procedureStepState | string | - | allowed (`"SCHEDULED"`, `"IN PROGRESS"`, `"COMPLETED"`, `"CANCELED"`) | - | **required** |
| workitem.scheduledProcedureStepStartDateTime | string | - | - | format (`date-time`) | **required** |
| workitem.scheduledWorkitemCodeSequence | object | - | - | - | **required**, **additional properties are allowed** |
| workitem.scheduledWorkitemCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledWorkitemCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledWorkitemCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.inputInformationSequence | array<object> | - | - | - | **required** |
| workitem.inputInformationSequence.studyInstanceUID | string | - | - | - | - |
| workitem.inputInformationSequence.seriesInstanceUID | string | - | - | - | - |
| workitem.scheduledStationNameCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationNameCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationNameCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationNameCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationClassCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationClassCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledStationGeographicLocationCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledStationGeographicLocationCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence | array<object> | - | - | - | - |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.scheduledHumanPerformersSequence.humanPerformerName | string | - | - | - | - |
| workitem.scheduledProcedureStepDescription | string | - | - | - | - |
| workitem.scheduledProtocolCodeSequence | object | - | - | - | **additional properties are allowed** |
| workitem.scheduledProtocolCodeSequence.codeValue | string | - | - | - | **required** |
| workitem.scheduledProtocolCodeSequence.codingSchemeDesignator | string | - | - | - | **required** |
| workitem.scheduledProtocolCodeSequence.codeMeaning | string | - | - | - | **required** |
| workitem.referencedRequestSequence | array<object> | - | - | - | - |
| workitem.referencedRequestSequence.studyInstanceUID | string | - | - | - | - |
| workitem.referencedRequestSequence.accessionNumber | string | - | - | - | - |
| workitem.referencedRequestSequence.requestedProcedureID | string | - | - | - | - |
| workitem.referencedRequestSequence.requestedProcedureDescription | string | - | - | - | - |

> Examples of payload _(generated)_

```json
{
  "eventType": "CREATED",
  "workitemUID": "string",
  "subscriptionUID": "string",
  "procedureStepState": "SCHEDULED",
  "progressInformation": {
    "numberOfCompletedSuboperations": 0,
    "numberOfFailedSuboperations": 0,
    "numberOfWarningSuboperations": 0,
    "numberOfRemainingSuboperations": 0
  },
  "cancellationReason": "string",
  "workitem": {
    "workitemUID": "string",
    "procedureStepState": "SCHEDULED",
    "scheduledProcedureStepStartDateTime": "2019-08-24T14:15:22Z",
    "scheduledWorkitemCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "inputInformationSequence": [
      {
        "studyInstanceUID": "string",
        "seriesInstanceUID": "string"
      }
    ],
    "scheduledStationNameCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledStationClassCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledStationGeographicLocationCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "scheduledHumanPerformersSequence": [
      {
        "humanPerformerCodeSequence": {
          "codeValue": "string",
          "codingSchemeDesignator": "string",
          "codeMeaning": "string"
        },
        "humanPerformerName": "string"
      }
    ],
    "scheduledProcedureStepDescription": "string",
    "scheduledProtocolCodeSequence": {
      "codeValue": "string",
      "codingSchemeDesignator": "string",
      "codeMeaning": "string"
    },
    "referencedRequestSequence": [
      {
        "studyInstanceUID": "string",
        "accessionNumber": "string",
        "requestedProcedureID": "string",
        "requestedProcedureDescription": "string"
      }
    ]
  }
}
```



### SUB `/workitems/subscription/{subscriptionUID}` Operation

*Unsubscribe from UPS Workitem events*

* Operation ID: `unsubscribeFromWorkitems`

#### Parameters

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| subscriptionUID | string | Unique identifier for the subscription | - | - | **required** |


#### Message UPS Workitem Unsubscription Request `ups.workitem.unsubscription.request`

##### Payload

| Name | Type | Description | Value | Constraints | Notes |
|---|---|---|---|---|---|
| (root) | object | - | - | - | **additional properties are allowed** |
| reason | string | - | allowed (`"USER_REQUEST"`, `"CONNECTION_CLOSURE"`) | - | **required** |
| subscriptionUID | string | - | - | - | - |

> Examples of payload _(generated)_

```json
{
  "reason": "USER_REQUEST",
  "subscriptionUID": "string"
}
```



