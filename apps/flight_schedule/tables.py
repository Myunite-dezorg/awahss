import django_tables2 as tables
from .models import FlightTask
 
 
 
class TasksTable(tables.Table):
    
     
    user = tables.Column(accessor="user")
    technology = tables.Column(attrs={"tf": {"bgcolor": "red"}})
    airline = tables.Column(attrs={"tf": {"bgcolor": "red"}})
    flight = tables.Column()
    sched_time = tables.Column(verbose_name="Sch_t",)
    registration = tables.Column(verbose_name="Reg",)
    route = tables.Column(attrs={"tf": {"bgcolor": "red"}})
    payload = tables.Column(verbose_name="Cargo",)
    status = tables.Column(attrs={"tf": {"bgcolor": "red"}})
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    class Meta:
        ATTRIBUTES = {
            "th" : {
                "_ordering": {
                    "orderable": "sortable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        
        model = FlightTask
        sequence = ('selection', 'task_date',)
        template_name = "django_tables2/bootstrap.html"
        fields = (
            'task_date',
            # 'airline',
            # 'flight',
            # 'sched_time',
            # 'route',
            # 'status',
            
        )
        task_date = tables.Column(attrs=ATTRIBUTES) 
     
 