import os
import ldclient
from ldclient.config import Config

ldclient.set_config(Config(os.environ.get("LD_SDK_KEY")))
ld_client = ldclient.get()

tenants = ['ACME', 'BCDR', 'GFLM']
    
for tenant in tenants:
    ctx = {
    "key": tenant
    }
    
    should_deploy = ld_client.variation("auto-deploy", ctx, False)
    
    if should_deploy:
        print(f"DEPLOYING: {tenant}")
    else:
        print(f"NOT DEPLOYING: {tenant}")
