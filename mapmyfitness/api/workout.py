from .base import BaseAPI
from ..inflators import WorkoutInflator
from ..validators import WorkoutValidator
from ..serializers import WorkoutSerializer

aggregate_values = ['active_time_total', 'distance_total', 'speed_max',
                    'speed_min', 'heartrate_min', 'power_min', 'speed_avg',
                    'power_avg', 'heartrate_max', 'power_max',
                    'elapsed_time_total', 'heartrate_avg',
                    'metabolic_energy_total'
                    ]

time_series_values = ['heartrate', 'speed', 'cadence', 'power', 'torque',
                      'distance', 'steps', 'position', 'timer_stop'
                      ]


class Workout(BaseAPI):
    path = '/workout'
    validator_class = WorkoutValidator
    inflator_class = WorkoutInflator
    serializer_class = WorkoutSerializer
    embedded_name = 'workouts'
