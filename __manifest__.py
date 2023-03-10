{
    'name': 'Common RESTful API Interface Architecture',
    'version': '13.0.1.0',
    'summary': 'This module provides common RESTful API Architecture.',
    'description': """
        The Common RESTful Connector API Architecture module is a powerful tool for Odoo developers who need to integrate their applications with other API servers. This module offers a range of features to simplify the process of connecting to external APIs, including standardized API endpoints, customizable response formats, and an intuitive configuration interface.

        With the The Common RESTful Connector API Architecture module, developers can quickly and easily create new API connections without needing to write custom code for each individual server. This saves time and reduces the risk of errors, while also making it easier to modify and maintain the application over time.

        Overall, the The Common RESTful Connector API Architecture module is an essential add-on for any Odoo developer who needs to integrate their application with external APIs. Its intuitive design and powerful features make it a valuable asset for streamlining development workflows and improving the quality and reliability of your applications.
        
        In addition to simplifying the process of connecting to external APIs, the Common API Architecture module also offers advanced logging and error-handling features. Specifically, the module can automatically generate logs of all API requests and responses, allowing developers to track the progress of their application's interactions with external servers.

        Moreover, the Common API Architecture module can also be configured to send automatic email notifications in the event of an error. This feature is incredibly useful for ensuring that developers are quickly made aware of any problems with their application's API connections, allowing them to address issues promptly and minimize the risk of downtime or data loss.
        
        Overall, the logging and error-handling features of the Common API Architecture module make it a powerful tool for developers who need to ensure the reliability and security of their Odoo applications. By providing detailed logs and automated error notifications, this module helps to streamline development workflows and ensure that applications continue to run smoothly even in the face of unexpected issues.
    """,
    'category': 'Services/Connector',
    'support': 'odoo.tangerine@gmail.com',
    'author': 'Tangerine',
    'maintainer': 'Tangerine',
    'license': 'OPL-1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/api_request_header_data.xml',
        'views/instances_api_server_views.xml',
        'views/instances_api_server_header_views.xml',
        'views/instances_api_server_endpoint_views.xml',
        'views/api_request_header_views.xml',
        'views/api_connection_histories_views.xml',
        'views/menus.xml'
    ],
    'images': ['static/description/thumbnail.gif'],
    'currency': 'USD',
    'price': 21.00,
    'installable': True,
    'application': True
}