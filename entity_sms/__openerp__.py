{
    'name': "Entity SMS (SMSGATEWAY,CLICKATELL,SMSGLOBAL)",
    'version': "1.3",
    'author': "Sythil",
    'category': "Tools",
    'summary': "Allows you send smses from any model",
    'data': [
        'views/qweb.xml',
        'esms.xml',
        'esms.gateways.csv',
	'security/ir.model.access.csv',
        'smsgateway/gateway_config.xml',
        'clickatell/gateway_config.xml',
        'smsglobal/gateway_config.xml',
    ],
    'qweb': ['static/src/xml/esms_widget.xml'],
    'demo': [],
    'depends': ['web'],
    'installable': True,
}