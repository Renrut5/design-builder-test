from nautobot.apps.jobs import IntegerVar, ObjectVar, register_jobs, StringVar

from nautobot.dcim.models import Location
from nautobot.tenancy.models import Tenant
from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.design_job import DesignJob
from .context import NonNetworkDesignContext

class TestDesignJob(DesignJob):
    """"""
    site_name = StringVar(
        label="Site Name",
        regex=r"\w{3}\d+",
        description="Unique name for the site.",
    )

    class Meta:
        name = "Test Design"
        design_mode = DesignModeChoices.DEPLOYMENT
        has_sensitive_variables = False
        dryrun_default = True
        design_file = "designs/0001_design.yaml.j2"
        context_class = NonNetworkDesignContext


name = "Test Design"
register_jobs(TestDesignJob)
