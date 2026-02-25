{
    'name': 'Restrict Debug Mode Access',
    'version': '19.0.1.0.0',
    'category': 'Security',
    'summary': 'Restrict Debug Mode access for unauthorized users in Odoo backend',
    'description': """
Restrict Debug Mode Access for Odoo 19
=======================================

This module provides a security enhancement to control access to Odoo's
Developer Mode (Debug Mode) in the backend interface.

🎯 KEY FEATURES
===============

🔒 GROUP-BASED ACCESS CONTROL
------------------------------
• Control Debug Mode access by assigning users to a dedicated security group
• Only authorized personnel can enable Developer Mode
• Simple toggle via user settings

🚫 ACCESS DENIED SCREEN
------------------------
• Full-screen "ACCESS DENIED" message for unauthorized attempts
• Automatic 5-second countdown with page refresh
• Visual overlay prevents interaction during countdown

🛡️ ENHANCED SECURITY
---------------------
• Prevents non-technical users from using Debug Mode
• Safeguards Odoo instance integrity
• No modifications to core files

⚡ SEAMLESS INTEGRATION
-----------------------
• Integrates with Odoo's core session management
• Works with standard web assets pipeline
• Zero configuration needed after installation

💼 PERFECT FOR
-------------
• System Administrators - Control who can access developer tools
• Business Owners - Protect production environments
• IT Managers - Enforce security policies
• Consultants - Secure client instances

🚀 WHY CHOOSE THIS MODULE?
==========================
✅ No configuration needed - works out of the box
✅ Group-based access control
✅ Visual "Access Denied" feedback
✅ Automatic page refresh enforcement
✅ Compatible with Community and Enterprise editions

⭐ If you like this module, please rate us on Odoo App Store!
    """,
    'author': 'Sheikh Muhammad Saad, OdooElevate',
    'website': 'https://odooelevate.odoo.com/',
    'support': 'info.odooelevate@gmail.com',
    'license': 'AGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/restrict_debug_security.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'oe_restrict_debug_mode/static/src/core/debug/restrict_debug.js',
            'oe_restrict_debug_mode/static/src/core/debug/restrict_debug_view.xml',
            'oe_restrict_debug_mode/static/src/core/debug/restrict_debug.scss',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'sequence': 1,
}
