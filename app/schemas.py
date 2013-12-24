# SCHEMAS
schema_people = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}


people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema_people
}


schema_location = {
    'desc': {
        'type': 'string',
        'minlength': 0,
        'maxlength': 800,
    },
    'tags': {
        'type': 'string',
        'minlength': 0,
        'maxlength': 200,
    },
    'lat': {
        'type':'float',
        'required': True,
    },
    'lon': {
        'type':'float',
        'required': True,
    },
    'timestamp': {
        'type': 'datetime',
        #'required': True,

    },
    'photoId': {
        'type': 'string',
    },

    'evanType': {
        'type': 'boolean',
    },
    'trainType': {
        'type': 'boolean',
    },
    'mercyType': {
        'type': 'boolean',
    },
    'artsType': {
        'type': 'boolean',
    },
    'bibleStudyType': {
        'type': 'boolean',
    },
    'campusType': {
        'type': 'boolean',
    },
    'churchPlantingType': {
        'type': 'boolean',
    },
    'communityDevType': {
        'type': 'boolean',
    },
    'constructionType': {
        'type': 'boolean',
    },
    'counselingType': {
        'type': 'boolean',
    },
    'healthcareType': {
        'type': 'boolean',
    },
    'hospitalType': {
        'type': 'boolean',
    },
    'indigenousType': {
        'type': 'boolean',
    },
    'mediaType': {
        'type': 'boolean',
    },
    'orphansType': {
        'type': 'boolean',
    },
    'prisonType': {
        'type': 'boolean',
    },
    'prostitutesType': {
        'type': 'boolean',
    },
    'researchType': {
        'type': 'boolean',
    },
    'urbanType': {
        'type': 'boolean',
    },
    'womenType': {
        'type': 'boolean',
    },
    'youthType': {
        'type': 'boolean',
    },

    'contactConfirmed': {
        'type': 'boolean',
    },

    'contactEmail': {
        'type': 'string'
    },
    'contactPhone': {
        'type': 'string'
    },    
    'contactWebsite': {
        'type': 'string',
    },

    'dataId': {
        'type': 'string',
    },

    'owner': {
        'type': 'objectid',
        #'required': True,
        'data_relation': {
            'resource': 'user',
        }
    },
    'project': {
        'type': 'objectid',
        #'required': True,
        'data_relation': {
            'resource': 'project',
        }
    },
    'ozwid': {
        'type': 'string',
    }
}


location = {

    'item_title': 'location',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema_location
}

domain = {
    'people': people,
    'location': location,
}

