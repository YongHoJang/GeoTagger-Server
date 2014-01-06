schema_user = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
        'unique': True,
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 200,
        'required': True,
    },
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True
    },
    'middlename': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,        
    },        
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,        
    },
    'email': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100
    },
    'is_active': {
        'type': 'boolean',
    },
    # If a system uses email validation process.
    'is_validated': {
        'type': 'boolean',
    },
    'last_login': {
        'type': 'datetime',
    },
    'app_key': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    }

}

user = {
    'item_title': 'user',
    # Additional lookup with username
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },    
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    'schema': schema_user,
}