# SCHEMAS

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
    'location': location,
}

