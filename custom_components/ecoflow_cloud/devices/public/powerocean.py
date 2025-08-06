from ...api import EcoflowApiClient
from ...entities import (
    BaseNumberEntity,
    BaseSelectEntity,
    BaseSensorEntity,
    BaseSwitchEntity,
    BaseButtonEntity,
)
from ...number import ChargingPowerEntity
from ...sensor import (
    CapacitySensorEntity,
    InWattsSensorEntity,
    LevelSensorEntity,
    WattsSensorEntity,
    OutWattsSensorEntity,
    TempSensorEntity,
    InWattsBatterySensorEntity,
    InWattsHouseSensorEntity,
    InRawWattsSolarSensorEntity,
    VoltAmpSensorEntity,
    VoltAmpReactSensorEntity,
    VoltSensorEntity,
    AmpSensorEntity,
    StatusSensorEntity,
)
from .. import BaseDevice, const
from .data_bridge import to_plain

import logging
from typing import Any
from pprint import pformat
import re

_PREFIX_PAT = re.compile(r'^\d{2}\_\d\.')

_LOGGER = logging.getLogger(__name__)


class PowerOcean(BaseDevice):

    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:

        return [
            # Battery
            LevelSensorEntity(client, self, "bpSoc", const.BATTERY_LEVEL_SOC),
            InWattsBatterySensorEntity(
                client, self, "bpPwr", const.POWEROCEAN_BATTERY_IN_POWER
            ),
            # Solar / Inverter
            # InWattsSolarSensorEntity(
            #     client, self, "pvInvPwr", const.POWEROCEAN_PV_INV_POWER
            # ),
            InRawWattsSolarSensorEntity(client, self, "mpptPwr", const.SOLAR_IN_POWER),
            # Load
            InWattsHouseSensorEntity(
                client, self, "sysLoadPwr", const.POWEROCEAN_HOME_IN_POWER
            ),
            # Grid
            OutWattsSensorEntity(
                client, self, "sysGridPwr", const.POWEROCEAN_GRID_OUT_POWER
            ),
            # Phase A
            WattsSensorEntity(
                client, self, "pcsAPhase.actPwr", const.POWEROCEAN_ACTIVE_POWER_L1
            ),
            VoltAmpSensorEntity(
                client,
                self,
                "pcsAPhase.apparentPwr",
                const.POWEROCEAN_APPARENT_POWER_L1,
            ),
            VoltAmpReactSensorEntity(
                client, self, "pcsAPhase.reactPwr", const.POWEROCEAN_REACTIVE_POWER_L1
            ),
            VoltSensorEntity(client, self, "pcsAPhase.vol",
                             const.POWEROCEAN_VOLT_L1),
            AmpSensorEntity(client, self, "pcsAPhase.amp", const.POWEROCEAN_AMP_L1),
            # Phase B
            WattsSensorEntity(
                client, self, "pcsBPhase.actPwr", const.POWEROCEAN_ACTIVE_POWER_L2
            ),
            VoltAmpSensorEntity(
                client,
                self,
                "pcsBPhase.apparentPwr",
                const.POWEROCEAN_APPARENT_POWER_L2,
            ),
            VoltAmpReactSensorEntity(
                client, self, "pcsBPhase.reactPwr", const.POWEROCEAN_REACTIVE_POWER_L2
            ),
            VoltSensorEntity(client, self, "pcsBPhase.vol", const.POWEROCEAN_VOLT_L2),
            AmpSensorEntity(client, self, "pcsBPhase.amp", const.POWEROCEAN_AMP_L2),
            # Grid Phase C
            WattsSensorEntity(
                client, self, "pcsCPhase.actPwr", const.POWEROCEAN_ACTIVE_POWER_L3
            ),
            VoltAmpSensorEntity(
                client,
                self,
                "pcsCPhase.apparentPwr",
                const.POWEROCEAN_APPARENT_POWER_L3,
            ),
            VoltAmpReactSensorEntity(
                client, self, "pcsCPhase.reactPwr", const.POWEROCEAN_REACTIVE_POWER_L3
            ),
            VoltSensorEntity(client, self, "pcsCPhase.vol", const.POWEROCEAN_VOLT_L3),
            AmpSensorEntity(client, self, "pcsCPhase.amp", const.POWEROCEAN_AMP_L3),


            # String 1
            InRawWattsSolarSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.0.pwr", const.POWEROCEAN_POWER_MPPT1
            ),
            AmpSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.0.amp", const.POWEROCEAN_AMP_MPPT1
            ),
            VoltSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.0.vol", const.POWEROCEAN_VOLT_MPPT1
            ),
            # String 2
            InRawWattsSolarSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.1.pwr", const.POWEROCEAN_POWER_MPPT2
            ),
            AmpSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.1.amp", const.POWEROCEAN_AMP_MPPT2
            ),
            VoltSensorEntity(
                client, self, "mpptHeartBeat.0.mpptPv.1.vol", const.POWEROCEAN_VOLT_MPPT2
            ),

            StatusSensorEntity(client, self),

        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []

    def buttons(self, client: EcoflowApiClient) -> list[BaseButtonEntity]:
        return []

    def _prepare_data(self, raw_data) -> dict[str, "Any"]:
        res = super()._prepare_data(raw_data)
        # _LOGGER.info(f"_prepare_data {raw_data}")
        res = to_plain(res)

        # remove the prefix in the params dict to make mqtt resuslt  refernces
        # similar to the API result
        for paramkye in ('param', 'params'):
            update_dict = {}
            params = res.get(paramkye)
            if params:
                for k, v in params.items():
                    if _PREFIX_PAT.match(k):
                        update_dict['.'.join(k.split('.')[1:])] = v
                        # del params[k]

                params.update(update_dict)

        # _LOGGER.info("_prepare_data result")
        # _LOGGER.info(pformat(res))

        return res

    def _status_sensor(self, client: EcoflowApiClient) -> StatusSensorEntity:
        return StatusSensorEntity(client, self)
