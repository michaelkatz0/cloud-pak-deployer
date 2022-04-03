from generatorPreProcessor import GeneratorPreProcessor
import sys

# Validating:
# ---
# cp4d_role:
# - project: zen-40
#   openshift_cluster_name: {{ env_id }}
#   name: My Test Role
#   description: My Test Role Description
#   state: installed|removed
#   permissions:
#     - manage_catalog
#     - monitor_project
#     - manage_groups

def preprocessor(attributes=None, fullConfig=None):
    g = GeneratorPreProcessor(attributes,fullConfig)

    g('openshift_cluster_name').isRequired()
    g('project').isRequired()
    g('name').isRequired()
    g('state').isRequired()
    g('description').isRequired()
    g('permissions').isRequired()

    # Now that we have reached this point, we can check the attribute details if the previous checks passed
    if len(g.getErrors()) == 0:
        fc = g.getFullConfig()
        ge=g.getExpandedAttributes()

        if ge['state'] not in ['installed','removed']:
            g.appendError(msg='cp4d_role state must be "installed" or "removed"')

    result = {
        'attributes_updated': g.getExpandedAttributes(),
        'errors': g.getErrors()
    }
    return result