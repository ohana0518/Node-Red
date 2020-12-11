[
    {
        "id": "a0328995.71a608",
        "type": "tab",
        "label": "流程1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cf85a98b.b2b768",
        "type": "inject",
        "z": "a0328995.71a608",
        "name": "on ",
        "topic": "1",
        "payload": "1",
        "payloadType": "num",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130,
        "y": 340,
        "wires": [
            [
                "2be83e07.8ffe02",
                "90c33aa6.94ce58"
            ]
        ]
    },
    {
        "id": "831d89ce.593498",
        "type": "inject",
        "z": "a0328995.71a608",
        "name": "off",
        "topic": "",
        "payload": "0",
        "payloadType": "num",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130,
        "y": 520,
        "wires": [
            [
                "2be83e07.8ffe02",
                "90c33aa6.94ce58"
            ]
        ]
    },
    {
        "id": "2be83e07.8ffe02",
        "type": "rpi-gpio out",
        "z": "a0328995.71a608",
        "name": "green led",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 560,
        "y": 380,
        "wires": []
    },
    {
        "id": "90c33aa6.94ce58",
        "type": "debug",
        "z": "a0328995.71a608",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 550,
        "y": 480,
        "wires": []
    },
    {
        "id": "5ea43ad7.dba644",
        "type": "rpi-gpio in",
        "z": "a0328995.71a608",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 70,
        "y": 640,
        "wires": [
            [
                "90c33aa6.94ce58",
                "e99af136.7412b"
            ]
        ]
    },
    {
        "id": "e99af136.7412b",
        "type": "switch",
        "z": "a0328995.71a608",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 170,
        "y": 720,
        "wires": [
            [
                "5df2e81f.25e538"
            ],
            [
                "57f6884b.8d7c78"
            ]
        ]
    },
    {
        "id": "5df2e81f.25e538",
        "type": "change",
        "z": "a0328995.71a608",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 390,
        "y": 620,
        "wires": [
            [
                "2be83e07.8ffe02"
            ]
        ]
    },
    {
        "id": "57f6884b.8d7c78",
        "type": "change",
        "z": "a0328995.71a608",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 370,
        "y": 700,
        "wires": [
            [
                "2be83e07.8ffe02"
            ]
        ]
    }
]
