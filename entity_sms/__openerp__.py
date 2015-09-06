{
    'name': "Entity SMS V2 (Multi Gateway)",
    'version': "2.5",
    'author': "Sythil",
    'category': "Tools",
    'summary': "Send/Receive sms to leads and partners using Twilio",
    'data': [
        'ir.cron.csv',
        'esms_core.xml',
        'res_partner.xml',
        'esms_accounts.xml',
        'esms_templates.xml',
        'esms_import.xml',
        'esms_compose.xml',
        'esms_compose_multi.xml',
        'esms_autoresponse.xml',
        'esms_history.xml',
        'esms.gateways.csv',
	'security/ir.model.access.csv',
        'smsgateway/gateway_config.xml',
        'smsglobal/gateway_config.xml',
        'twilio/gateway_config.xml',
    ],
    'demo': [],
    'depends': ['web', 'crm'],
    'installable': True,
}