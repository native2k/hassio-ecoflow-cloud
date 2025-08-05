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
)
from .. import BaseDevice, const


class PowerOcean(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        """
        {'code': '0',
        'data': {'bpPwr': 0.0,
                'bpSoc': 100,
                'bp_addr.': '{\n  "bpTemp": [],\n  "bpCellVol": []\n}',
                'bp_addr.HJ3AZD1AZH4F0216': '{\n'
                                            '  "bpPwr": 0.1491534,\n'
                                            '  "bpSoc": 100,\n'
                                            '  "bpSoh": 100,\n'
                                            '  "bpTemp": [24.0, 25.0, 24.0, 24.0, '
                                            '25.0, 24.0, 24.0, 24.0, 24.0],\n'
                                            '  "bpCellMaxVol": 3348.0,\n'
                                            '  "bpCellMinVol": 3341.0,\n'
                                            '  "bpRunSta": "RUNSTA_RUN",\n'
                                            '  "bpVol": 53.46,\n'
                                            '  "bpAmp": 0.00279,\n'
                                            '  "bpBusVol": 833.7848,\n'
                                            '  "bpErrCode": 2,\n'
                                            '  "bpCellVol": [3343.0, 3346.0, 3345.0, '
                                            '3344.0, 3346.0, 3348.0, 3343.0, 3346.0, '
                                            '3347.0, 3346.0, 3345.0, 3345.0, 3345.0, '
                                            '3345.0, 3341.0, 3346.0],\n'
                                            '  "bpDsrc": 2,\n'
                                            '  "bpSn": "SEozQVpEMUFaSDRGMDIxNg==",\n'
                                            '  "bpCycles": 1,\n'
                                            '  "bpBalanceState": 0,\n'
                                            '  "bpHvMosTemp": 24.0,\n'
                                            '  "bpLvMosTemp": 24.0,\n'
                                            '  "bpPtcTemp": 24.0,\n'
                                            '  "bpHtsTemp": 26.0,\n'
                                            '  "bpBusNegTemp": 25.0,\n'
                                            '  "bpBusPosTemp": 26.0,\n'
                                            '  "bpEnvTemp": 24.0,\n'
                                            '  "bpAccuChgCap": 154010,\n'
                                            '  "bpAccuDsgCap": 84461,\n'
                                            '  "bpDesignCap": 100000,\n'
                                            '  "bpFullCap": 100000,\n'
                                            '  "bpMaxCellTemp": 25.0,\n'
                                            '  "bpMinCellTemp": 24.0,\n'
                                            '  "bpMaxMosTemp": 24.0,\n'
                                            '  "bpMinMosTemp": 24.0,\n'
                                            '  "bpBmsFault": 0,\n'
                                            '  "bpEcloundSoc": 65535,\n'
                                            '  "bpHeartbeatVer": 33,\n'
                                            '  "bpTimestamp": 1754309777,\n'
                                            '  "bpRealSoc": 99.0,\n'
                                            '  "bpRealSoh": 100.0,\n'
                                            '  "bpGlobalProtect": 0,\n'
                                            '  "bpDownLimitSoc": 24,\n'
                                            '  "bpUpLimitSoc": 100,\n'
                                            '  "bpActiveCalReqStat": 0,\n'
                                            '  "bpActiveCalRunStat": 0,\n'
                                            '  "moduleProductInfo": 21251,\n'
                                            '  "moduleProgramSta": 1,\n'
                                            '  "moduleAplSwVer": 67177217,\n'
                                            '  "moduleLoaderSwVer": 67174401,\n'
                                            '  "bmsRunSta": '
                                            '"PB_BMS_STATE_DISCHARGEABLE",\n'
                                            '  "bmsChgDsgSta": "PB_STANDBY_STATE",\n'
                                            '  "dabModSta": "PB_MOD_STA_WARNNING",\n'
                                            '  "bpChgSop": 37,\n'
                                            '  "bpDsgSop": 80,\n'
                                            '  "bpRemainWatth": 5120.0,\n'
                                            '  "bpTargetSoc": 99.999985,\n'
                                            '  "bpDiffSoc": 2.5,\n'
                                            '  "bpMaxSoc": 99.99983,\n'
                                            '  "bpMinSoc": 97.499985,\n'
                                            '  "bpLimitSoc": 0.5,\n'
                                            '  "bpCalendarSoh": 100.0,\n'
                                            '  "bpCycleSoh": 100.0,\n'
                                            '  "bpAcRechargeFlag": false,\n'
                                            '  "bpPtcHeatFlag": false,\n'
                                            '  "bpPtcExitEvent": "PB_PTC_OT_STATE",\n'
                                            '  "bpAccuChgEnergy": 8323,\n'
                                            '  "bpAccuDsgEnergy": 4446,\n'
                                            '  "bpPtcTemp2": 24.0,\n'
                                            '  "bpSysState": "NORMAL_STATE",\n'
                                            '  "bpAuxCellVol01": 3342.0\n'
                                            '}',
                'bp_addr.HJ3AZDHAZH3V0305': '{\n'
                                            '  "bpPwr": -0.17789592,\n'
                                            '  "bpSoc": 100,\n'
                                            '  "bpSoh": 100,\n'
                                            '  "bpTemp": [24.0, 25.0, 24.0, 24.0, '
                                            '25.0, 24.0, 24.0, 24.0, 24.0],\n'
                                            '  "bpCellMaxVol": 3329.0,\n'
                                            '  "bpCellMinVol": 3329.0,\n'
                                            '  "bpRunSta": "RUNSTA_RUN",\n'
                                            '  "bpVol": 53.213,\n'
                                            '  "bpAmp": -0.0033430913,\n'
                                            '  "bpBusVol": 833.5702,\n'
                                            '  "bpErrCode": 2,\n'
                                            '  "bpCellVol": [3329.0, 3329.0, 3329.0, '
                                            '3329.0, 3329.0, 3329.0, 3329.0, 3329.0, '
                                            '3329.0, 3329.0, 3329.0, 3329.0, 3329.0, '
                                            '3329.0, 3329.0, 3329.0],\n'
                                            '  "bpDsrc": 1,\n'
                                            '  "bpSn": "SEozQVpESEFaSDNWMDMwNQ==",\n'
                                            '  "bpCycles": 0,\n'
                                            '  "bpBalanceState": 0,\n'
                                            '  "bpHvMosTemp": 25.0,\n'
                                            '  "bpLvMosTemp": 25.0,\n'
                                            '  "bpPtcTemp": 23.0,\n'
                                            '  "bpHtsTemp": 26.0,\n'
                                            '  "bpBusNegTemp": 25.0,\n'
                                            '  "bpBusPosTemp": 26.0,\n'
                                            '  "bpEnvTemp": 24.0,\n'
                                            '  "bpAccuChgCap": 81378,\n'
                                            '  "bpAccuDsgCap": 11384,\n'
                                            '  "bpDesignCap": 100000,\n'
                                            '  "bpFullCap": 100000,\n'
                                            '  "bpMaxCellTemp": 25.0,\n'
                                            '  "bpMinCellTemp": 24.0,\n'
                                            '  "bpMaxMosTemp": 25.0,\n'
                                            '  "bpMinMosTemp": 25.0,\n'
                                            '  "bpBmsFault": 0,\n'
                                            '  "bpEcloundSoc": 65535,\n'
                                            '  "bpHeartbeatVer": 33,\n'
                                            '  "bpTimestamp": 1754309771,\n'
                                            '  "bpRealSoc": 100.0,\n'
                                            '  "bpRealSoh": 100.0,\n'
                                            '  "bpGlobalProtect": 0,\n'
                                            '  "bpDownLimitSoc": 24,\n'
                                            '  "bpUpLimitSoc": 100,\n'
                                            '  "bpActiveCalReqStat": 0,\n'
                                            '  "bpActiveCalRunStat": 0,\n'
                                            '  "moduleProductInfo": 21251,\n'
                                            '  "moduleProgramSta": 1,\n'
                                            '  "moduleAplSwVer": 67177217,\n'
                                            '  "moduleLoaderSwVer": 67174401,\n'
                                            '  "bmsRunSta": '
                                            '"PB_BMS_STATE_DISCHARGEABLE",\n'
                                            '  "bmsChgDsgSta": "PB_STANDBY_STATE",\n'
                                            '  "dabModSta": "PB_MOD_STA_WARNNING",\n'
                                            '  "bpChgSop": 49,\n'
                                            '  "bpDsgSop": 80,\n'
                                            '  "bpRemainWatth": 5120.0,\n'
                                            '  "bpTargetSoc": 99.98685,\n'
                                            '  "bpDiffSoc": 0.5,\n'
                                            '  "bpMaxSoc": 99.98678,\n'
                                            '  "bpMinSoc": 99.48698,\n'
                                            '  "bpLimitSoc": 0.5,\n'
                                            '  "bpCalendarSoh": 100.0,\n'
                                            '  "bpCycleSoh": 100.0,\n'
                                            '  "bpAcRechargeFlag": false,\n'
                                            '  "bpPtcHeatFlag": false,\n'
                                            '  "bpPtcExitEvent": "PB_PTC_OT_STATE",\n'
                                            '  "bpAccuChgEnergy": 4391,\n'
                                            '  "bpAccuDsgEnergy": 573,\n'
                                            '  "bpPtcTemp2": 24.0,\n'
                                            '  "bpSysState": "NORMAL_STATE",\n'
                                            '  "bpAuxCellVol01": 3328.0\n'
                                            '}',
                'bp_addr.HJ3AZDHAZH3V0669': '{\n'
                                            '  "bpPwr": -0.33270356,\n'
                                            '  "bpSoc": 100,\n'
                                            '  "bpSoh": 100,\n'
                                            '  "bpTemp": [23.0, 24.0, 24.0, 24.0, '
                                            '24.0, 23.0, 23.0, 23.0, 23.0],\n'
                                            '  "bpCellMaxVol": 3365.0,\n'
                                            '  "bpCellMinVol": 3343.0,\n'
                                            '  "bpRunSta": "RUNSTA_RUN",\n'
                                            '  "bpVol": 53.597,\n'
                                            '  "bpAmp": -0.0062075034,\n'
                                            '  "bpBusVol": 833.084,\n'
                                            '  "bpErrCode": 2,\n'
                                            '  "bpCellVol": [3357.0, 3343.0, 3361.0, '
                                            '3349.0, 3351.0, 3365.0, 3344.0, 3348.0, '
                                            '3349.0, 3352.0, 3364.0, 3360.0, 3351.0, '
                                            '3348.0, 3344.0, 3348.0],\n'
                                            '  "bpDsrc": 3,\n'
                                            '  "bpSn": "SEozQVpESEFaSDNWMDY2OQ==",\n'
                                            '  "bpCycles": 1,\n'
                                            '  "bpBalanceState": 0,\n'
                                            '  "bpHvMosTemp": 23.0,\n'
                                            '  "bpLvMosTemp": 23.0,\n'
                                            '  "bpPtcTemp": 22.0,\n'
                                            '  "bpHtsTemp": 25.0,\n'
                                            '  "bpBusNegTemp": 24.0,\n'
                                            '  "bpBusPosTemp": 26.0,\n'
                                            '  "bpEnvTemp": 23.0,\n'
                                            '  "bpAccuChgCap": 153911,\n'
                                            '  "bpAccuDsgCap": 82622,\n'
                                            '  "bpDesignCap": 100000,\n'
                                            '  "bpFullCap": 100000,\n'
                                            '  "bpMaxCellTemp": 24.0,\n'
                                            '  "bpMinCellTemp": 23.0,\n'
                                            '  "bpMaxMosTemp": 23.0,\n'
                                            '  "bpMinMosTemp": 23.0,\n'
                                            '  "bpBmsFault": 0,\n'
                                            '  "bpEcloundSoc": 65535,\n'
                                            '  "bpHeartbeatVer": 33,\n'
                                            '  "bpTimestamp": 1754309770,\n'
                                            '  "bpRealSoc": 100.0,\n'
                                            '  "bpRealSoh": 100.0,\n'
                                            '  "bpGlobalProtect": 0,\n'
                                            '  "bpDownLimitSoc": 24,\n'
                                            '  "bpUpLimitSoc": 100,\n'
                                            '  "bpActiveCalReqStat": 0,\n'
                                            '  "bpActiveCalRunStat": 0,\n'
                                            '  "moduleProductInfo": 21251,\n'
                                            '  "moduleProgramSta": 1,\n'
                                            '  "moduleAplSwVer": 67177217,\n'
                                            '  "moduleLoaderSwVer": 67174401,\n'
                                            '  "bmsRunSta": '
                                            '"PB_BMS_STATE_DISCHARGEABLE",\n'
                                            '  "bmsChgDsgSta": "PB_STANDBY_STATE",\n'
                                            '  "dabModSta": "PB_MOD_STA_WARNNING",\n'
                                            '  "bpChgSop": 33,\n'
                                            '  "bpDsgSop": 80,\n'
                                            '  "bpRemainWatth": 5120.0,\n'
                                            '  "bpTargetSoc": 99.98764,\n'
                                            '  "bpDiffSoc": 0.5,\n'
                                            '  "bpMaxSoc": 99.98762,\n'
                                            '  "bpMinSoc": 99.48777,\n'
                                            '  "bpLimitSoc": 0.5,\n'
                                            '  "bpCalendarSoh": 100.0,\n'
                                            '  "bpCycleSoh": 100.0,\n'
                                            '  "bpAcRechargeFlag": false,\n'
                                            '  "bpPtcHeatFlag": false,\n'
                                            '  "bpPtcExitEvent": "PB_PTC_OT_STATE",\n'
                                            '  "bpAccuChgEnergy": 8320,\n'
                                            '  "bpAccuDsgEnergy": 4345,\n'
                                            '  "bpPtcTemp2": 24.0,\n'
                                            '  "bpSysState": "NORMAL_STATE",\n'
                                            '  "bpAuxCellVol01": 3356.0\n'
                                            '}',
                'bp_addr.updateTime': '2025-08-04 20:16:21',
                'ems.0026PVYPM1H0UMB2': '{\n'
                                        '  "devInfo": {\n'
                                        '    "devAddr": 214,\n'
                                        '    "devSn": "0026PVYPM1H0UMB2",\n'
                                        '    "subAddr": 1\n'
                                        '  },\n'
                                        '  "thirdPlugParamReport": {\n'
                                        '    "householdPwr": 0.0,\n'
                                        '    "maxPwr": 0.0,\n'
                                        '    "switchStat": 0,\n'
                                        '    "subIdx": 0,\n'
                                        '    "socketNum": 0,\n'
                                        '    "socketInfo": [],\n'
                                        '    "errorCode": ""\n'
                                        '  }\n'
                                        '}',
                'ems.updateTime': '2025-07-30 19:12:30',
                'emsBpAliveNum': 3,
                'emsErrCode.errCode': [523],
                'ems_change_report.afciEn': 0,
                'ems_change_report.afciEnSet': 0,
                'ems_change_report.afciEnableCmdState': 0,
                'ems_change_report.afciFaultClearState': 0,
                'ems_change_report.afciFaultCntCh1': 0,
                'ems_change_report.afciFaultCntCh2': 0,
                'ems_change_report.afciFaultFlagCh1': 0,
                'ems_change_report.afciFaultFlagCh2': 0,
                'ems_change_report.afciFaultMaxValueCh1': 0.0,
                'ems_change_report.afciFaultMaxValueCh2': 0.0,
                'ems_change_report.afciFaultValueCh1': 0.0,
                'ems_change_report.afciFaultValueCh2': 0.0,
                'ems_change_report.afciIsExist': 0,
                'ems_change_report.afciProtectValueCh1': 0.0,
                'ems_change_report.afciProtectValueCh2': 0.0,
                'ems_change_report.afciSelfTestCmdState': 0,
                'ems_change_report.afciSellfTestResult': 0,
                'ems_change_report.afciSwitchFreqCh1': 0,
                'ems_change_report.afciSwitchFreqCh2': 0,
                'ems_change_report.batRealyStatus': 2,
                'ems_change_report.batRelayCloseFailFlag': 0,
                'ems_change_report.batSoftRelayStatus': 0,
                'ems_change_report.bpChgDsgSta': 2,
                'ems_change_report.bpLineOffFlag': 0,
                'ems_change_report.bpOnlineSum': 3,
                'ems_change_report.bpRestartFlag': 1,
                'ems_change_report.bpReverseFlag': 0,
                'ems_change_report.bpSoc': 100,
                'ems_change_report.bpTotalChgEnergy': 20528,
                'ems_change_report.bpTotalDsgEnergy': 8859,
                'ems_change_report.chgDsgMode': 0,
                'ems_change_report.chgDsgPwr': 700.0,
                'ems_change_report.devMaxPower': 0,
                'ems_change_report.duration': 0,
                'ems_change_report.emsAcmakeStat': False,
                'ems_change_report.emsBackupEvent': 0,
                'ems_change_report.emsCtrlLedBright': 40,
                'ems_change_report.emsCtrlLedType': 1,
                'ems_change_report.emsFeedMode': 1,
                'ems_change_report.emsFeedPwr': 10000,
                'ems_change_report.emsFeedRatio': 100,
                'ems_change_report.emsSgReady.emsSgParam': [],
                'ems_change_report.emsSgReadyEn': False,
                'ems_change_report.emsSgRunStat': 0,
                'ems_change_report.emsStopAll': 0,
                'ems_change_report.emsWordMode': 'WORKMODE_SELFUSE',
                'ems_change_report.emsWorkState': 0,
                'ems_change_report.endTimestamp': 0,
                'ems_change_report.ethWanStat': 32,
                'ems_change_report.evBindList.evSn': [],
                'ems_change_report.iot4gErr': 7,
                'ems_change_report.iot4gOn': 1,
                'ems_change_report.iot4gPdp': -1,
                'ems_change_report.iot4gSta': 0,
                'ems_change_report.meterCheckState': 0,
                'ems_change_report.mppt1FaultCode': 0,
                'ems_change_report.mppt1WarningCode': 0,
                'ems_change_report.mppt2FaultCode': 0,
                'ems_change_report.mppt2WarningCode': 0,
                'ems_change_report.parallelAllowState': False,
                'ems_change_report.parallelType': 0,
                'ems_change_report.parallelTypeCur': 0,
                'ems_change_report.parallelTypeSet': 0,
                'ems_change_report.pcs10minOverVol': 253.0,
                'ems_change_report.pcs10minOverVolSwitch': 1,
                'ems_change_report.pcs10minOverVolTime': 100,
                'ems_change_report.pcsAcErrCode': 0,
                'ems_change_report.pcsAcWarningCode': 0,
                'ems_change_report.pcsActivePowerDeratingPercent': 1.0,
                'ems_change_report.pcsActivePowerDeratingSwitch': 0,
                'ems_change_report.pcsActivePowerGradient': 0.0033,
                'ems_change_report.pcsActivePowerNormalRampUpRate': 60.0,
                'ems_change_report.pcsActivePowerSoftStartRate': 0.1,
                'ems_change_report.pcsActivePowerSoftstartSwitch': 1,
                'ems_change_report.pcsActivePowerSoftstartTime': 666,
                'ems_change_report.pcsAntiBackFlowSwitch': 1,
                'ems_change_report.pcsAutoTestFlag': 0,
                'ems_change_report.pcsAutoTestPercent': 0,
                'ems_change_report.pcsAutoTestState': 0,
                'ems_change_report.pcsAvgOvpProtectCnt': 0,
                'ems_change_report.pcsAvgOvpProtectValue': 0.0,
                'ems_change_report.pcsCospP1': 0.1,
                'ems_change_report.pcsCospP2': 0.5,
                'ems_change_report.pcsCospP3': 1.0,
                'ems_change_report.pcsCospP4': 0.0,
                'ems_change_report.pcsCospPf1': -1.0,
                'ems_change_report.pcsCospPf2': -1.0,
                'ems_change_report.pcsCospPf3': -0.9,
                'ems_change_report.pcsCospPf4': 0.0,
                'ems_change_report.pcsDcErrCode': 0,
                'ems_change_report.pcsFastCheck': 0,
                'ems_change_report.pcsFaultRecoverHighFreqOnGrid': 50.1,
                'ems_change_report.pcsFaultRecoverHighVolOnGrid': 253.0,
                'ems_change_report.pcsFaultRecoverLowFreqOnGrid': 47.53,
                'ems_change_report.pcsFaultRecoverLowVolOnGrid': 195.5,
                'ems_change_report.pcsFaultRecoverOnGridWaitTime': 60000,
                'ems_change_report.pcsFreqExternalSignal': 0,
                'ems_change_report.pcsFreqLocalCommand': 1,
                'ems_change_report.pcsFreqRecoverTime': 1000,
                'ems_change_report.pcsFunctionEnable': 0,
                'ems_change_report.pcsHighFreqOnGrid': 50.1,
                'ems_change_report.pcsHighVolOnGrid': 253.0,
                'ems_change_report.pcsHighVolRideThroughRecover': 253.0,
                'ems_change_report.pcsHvrtLvrtSwitch': 1,
                'ems_change_report.pcsIslandDetectSwitch': 1,
                'ems_change_report.pcsLowFreq1': 47.5,
                'ems_change_report.pcsLowFreq2': 47.5,
                'ems_change_report.pcsLowFreqOnGrid': 47.53,
                'ems_change_report.pcsLowFreqRecover': 47.53,
                'ems_change_report.pcsLowFreqTime1': 100,
                'ems_change_report.pcsLowFreqTime2': 100,
                'ems_change_report.pcsLowVol1': 184.0,
                'ems_change_report.pcsLowVol2': 103.5,
                'ems_change_report.pcsLowVol3': 57.5,
                'ems_change_report.pcsLowVolOnGrid': 195.5,
                'ems_change_report.pcsLowVolRecover': 195.5,
                'ems_change_report.pcsLowVolRideThroughProtectTime1': 5200,
                'ems_change_report.pcsLowVolRideThroughProtectTime2': 3000,
                'ems_change_report.pcsLowVolRideThroughProtectTime3': 1000,
                'ems_change_report.pcsLowVolRideThroughRecover': 195.5,
                'ems_change_report.pcsLowVolRideThroughStart1': 184.0,
                'ems_change_report.pcsLowVolRideThroughStart2': 103.5,
                'ems_change_report.pcsLowVolRideThroughStart3': 34.5,
                'ems_change_report.pcsLowVolTime1': 3000,
                'ems_change_report.pcsLowVolTime2': 300,
                'ems_change_report.pcsLowVolTime3': 240,
                'ems_change_report.pcsOfpProtectCnt': 0,
                'ems_change_report.pcsOfpProtectValue': 0.0,
                'ems_change_report.pcsOnGridWaitTime': 60000,
                'ems_change_report.pcsOngridReconnectFlag': 1,
                'ems_change_report.pcsOverFreq1': 51.5,
                'ems_change_report.pcsOverFreq2': 51.5,
                'ems_change_report.pcsOverFreqDeratingCutoffPower': 0.0,
                'ems_change_report.pcsOverFreqDeratingEnd': 50.2,
                'ems_change_report.pcsOverFreqDeratingEndDelay': 0.0,
                'ems_change_report.pcsOverFreqDeratingFrozeSwitch': 0,
                'ems_change_report.pcsOverFreqDeratingPowerBased': 2.0,
                'ems_change_report.pcsOverFreqDeratingRecoverSlope': 0.09,
                'ems_change_report.pcsOverFreqDeratingRecoverSlopeSwitch': 1,
                'ems_change_report.pcsOverFreqDeratingSlope': 0.4,
                'ems_change_report.pcsOverFreqDeratingStart': 50.2,
                'ems_change_report.pcsOverFreqDeratingStartDelay': 0.0,
                'ems_change_report.pcsOverFreqDeratingSwitch': 0,
                'ems_change_report.pcsOverFreqRecover': 50.1,
                'ems_change_report.pcsOverFreqTime1': 100,
                'ems_change_report.pcsOverFreqTime2': 100,
                'ems_change_report.pcsOverVol1': 287.5,
                'ems_change_report.pcsOverVol2': 287.5,
                'ems_change_report.pcsOverVol3': 0.0,
                'ems_change_report.pcsOverVolDeratingDaleyTime': 0.0,
                'ems_change_report.pcsOverVolDeratingEnd': 257.6,
                'ems_change_report.pcsOverVolDeratingEndPower': 0.0,
                'ems_change_report.pcsOverVolDeratingStart': 253.0,
                'ems_change_report.pcsOverVolDeratingStartingPower': 1.0,
                'ems_change_report.pcsOverVolDeratingSwitch': 0,
                'ems_change_report.pcsOverVolDeratingTimeConst': 10.0,
                'ems_change_report.pcsOverVolRecover': 253.0,
                'ems_change_report.pcsOverVolRideThroughProtectTime1': 5500,
                'ems_change_report.pcsOverVolRideThroughProtectTime2': 1000,
                'ems_change_report.pcsOverVolRideThroughStart1': 265.65,
                'ems_change_report.pcsOverVolRideThroughStart2': 287.5,
                'ems_change_report.pcsOverVolTime1': 100,
                'ems_change_report.pcsOverVolTime2': 100,
                'ems_change_report.pcsOverVolTime3': 0,
                'ems_change_report.pcsOvpProtectCnt': 0,
                'ems_change_report.pcsOvpProtectValue': 0.0,
                'ems_change_report.pcsPfValue': 1.0,
                'ems_change_report.pcsPowerDeratingFlag': 5,
                'ems_change_report.pcsPowerDeratingSet': 200,
                'ems_change_report.pcsQuLockinPower': 0.0,
                'ems_change_report.pcsQuLockoutPower': 0.0,
                'ems_change_report.pcsQuMinimumCosphi': 0.4,
                'ems_change_report.pcsQuQ1': 0.6,
                'ems_change_report.pcsQuQ2': 0.0,
                'ems_change_report.pcsQuQ3': 0.0,
                'ems_change_report.pcsQuQ4': -0.6,
                'ems_change_report.pcsQuTimeConst': 10.0,
                'ems_change_report.pcsQuV1': 213.90001,
                'ems_change_report.pcsQuV2': 223.1,
                'ems_change_report.pcsQuV3': 236.9,
                'ems_change_report.pcsQuV4': 246.1,
                'ems_change_report.pcsQuickSelfcheckEn': 0,
                'ems_change_report.pcsReactPwrCompensation': 0.0062,
                'ems_change_report.pcsReactPwrModeSelect': 0,
                'ems_change_report.pcsReactPwrPercent': 0.0,
                'ems_change_report.pcsReconnectGridDetectSwitch': 1,
                'ems_change_report.pcsRelaySelfCheckSta': 10,
                'ems_change_report.pcsRelayStateShow': 676432975,
                'ems_change_report.pcsRunFsmState': 2541889614,
                'ems_change_report.pcsRunSta': 'RUNSTA_RUN',
                'ems_change_report.pcsSafetyCountryCodeSelection': 4,
                'ems_change_report.pcsSendEnd': 0,
                'ems_change_report.pcsUfpProtectCnt': 0,
                'ems_change_report.pcsUfpProtectValue': 0.0,
                'ems_change_report.pcsUnderFreqIncrementEnd': 49.8,
                'ems_change_report.pcsUnderFreqIncrementEndDelay': 0.0,
                'ems_change_report.pcsUnderFreqIncrementFrozeSwitch': 0,
                'ems_change_report.pcsUnderFreqIncrementRecoverSlope': 0.09,
                'ems_change_report.pcsUnderFreqIncrementRecoverSlopeSwitch': 1,
                'ems_change_report.pcsUnderFreqIncrementSlope': 0.4,
                'ems_change_report.pcsUnderFreqIncrementStart': 49.8,
                'ems_change_report.pcsUnderFreqIncrementStartDelay': 0.0,
                'ems_change_report.pcsUnderFreqIncrementSwitch': 0,
                'ems_change_report.pcsUvp1ProtectCnt': 0,
                'ems_change_report.pcsUvp1ProtectValue': 0.0,
                'ems_change_report.pcsUvp2ProtectCnt': 0,
                'ems_change_report.pcsUvp2ProtectValue': 0.0,
                'ems_change_report.pcsVolRecoverTime': 1000,
                'ems_change_report.poAiSchedule.bpChgDownLimit': 20.0,
                'ems_change_report.poAiSchedule.bpChgEffic': 0.9999,
                'ems_change_report.poAiSchedule.bpChgPwrMax': 7500.0,
                'ems_change_report.poAiSchedule.bpChgUpLimit': 100.0,
                'ems_change_report.poAiSchedule.bpCrrentSoc': 100.0,
                'ems_change_report.poAiSchedule.bpDsgEffic': 0.99,
                'ems_change_report.poAiSchedule.bpDsgPwrMax': 9900.0,
                'ems_change_report.poAiSchedule.bpFullCap': 15360.0,
                'ems_change_report.poAiSchedule.gridGetMaxPwr': 400.0,
                'ems_change_report.poAiSchedule.maxFeedPwr': 10000.0,
                'ems_change_report.poAiSchedule.pcsMaxInPwr': 10000.0,
                'ems_change_report.poAiSchedule.pcsMaxOutPwr': 10000.0,
                'ems_change_report.rateCtrlSwtich': True,
                'ems_change_report.rcrReport.activeState': 0,
                'ems_change_report.rcrReport.enable': 0,
                'ems_change_report.relay14a': 0,
                'ems_change_report.roleEffectState': 0,
                'ems_change_report.safetyEffectState': 0,
                'ems_change_report.sys14aEnable': False,
                'ems_change_report.sys14aType': 1,
                'ems_change_report.sysBatBackupRatio': 0,
                'ems_change_report.sysBatDsgDownLimit': 20,
                'ems_change_report.sysCalStat': 0,
                'ems_change_report.sysGridSta': 0,
                'ems_change_report.sysHeatStat': 0,
                'ems_change_report.sysMeterCfg': 0,
                'ems_change_report.sysMulPeakSwitch': False,
                'ems_change_report.sysMulPeakTime': 1200,
                'ems_change_report.sysOnOffMachineStat': 0,
                'ems_change_report.sysRateCtrlTime': 60,
                'ems_change_report.sysStateBit': 0,
                'ems_change_report.sysTypeCfg': 0,
                'ems_change_report.updateTime': '2025-08-04 20:18:07',
                'ems_change_report.userRole': 0,
                'ems_change_report.virtualHardEdition': 1,
                'ems_change_report.wifiStaStat': 0,
                'ems_change_report.wireless4gIccid': '',
                'ems_eco_logy_dev.HPReport.devSn': '',
                'ems_eco_logy_dev.HPReport.errorCode': '',
                'ems_eco_logy_dev.HPReport.online': 0,
                'ems_eco_logy_dev.updateTime': '2025-08-04 20:18:06',
                'ems_edev_sys.devFirstInfo': 31,
                'ems_edev_sys.devInfoFix.devSubInfoFix': [],
                'ems_edev_sys.devInfoVar.devSubInfoVar': [],
                'ems_edev_sys.devLastInfo': 31,
                'ems_edev_sys.devLastMinInfo': 31,
                'ems_edev_sys.dispatchType': 1,
                'ems_edev_sys.feedPwrCap': 10000.0,
                'ems_edev_sys.freeNum': 36,
                'ems_edev_sys.pclPwrBase': 0.0,
                'ems_edev_sys.socCur': 99.99148,
                'ems_edev_sys.socDev': 100,
                'ems_edev_sys.solarFlag': 9177,
                'ems_edev_sys.startState': 0,
                'ems_edev_sys.stratType': 0,
                'ems_edev_sys.sysFlag': 67,
                'ems_edev_sys.updateTime': '2025-08-04 20:04:56',
                'ems_edev_sys.usedNum': 0,
                'ems_logy_dev.devItem': [],
                'ems_logy_dev.updateTime': '2025-08-04 16:34:57',
                'ems_param_change_report.bpBurst': False,
                'ems_param_change_report.breakerCapacityMax': 400,
                'ems_param_change_report.breakerEnableState': False,
                'ems_param_change_report.devSoc': 100,
                'ems_param_change_report.emsAllPeakTaskReport.peakTaskCfg': [],
                'ems_param_change_report.emsPeakShavingReport.peakShavingControlEnergy': 0.0,
                'ems_param_change_report.emsPeakShavingReport.peakShavingEnergy': 0.0,
                'ems_param_change_report.emsPeakShavingReport.peakShavingMaxPower': 0.0,
                'ems_param_change_report.emsPeakShavingReport.peakShavingSoc': 0.0,
                'ems_param_change_report.emsPeakShavingReport.peakShavingStatus': 'NO_PEAK_SHAVING_TASK',
                'ems_param_change_report.emsPeakShavingReport.peakShavingTimes': 0.0,
                'ems_param_change_report.energyEfficientEnable': False,
                'ems_param_change_report.lowerPowerStat': False,
                'ems_param_change_report.smartCtrl': False,
                'ems_param_change_report.sysSwitchBit': 0,
                'ems_param_change_report.sysTimeTab': 0,
                'ems_param_change_report.sysZone': 0,
                'ems_param_change_report.touOffset': 0.0,
                'ems_param_change_report.updateTime': '2025-08-04 20:18:06',
                'ems_priority.devPrioReport': [],
                'ems_priority.updateTime': '2025-08-04 16:34:57',
                'ems_tou_task.pouTaskCfg': [],
                'ems_tou_task.touTaskCfg': [],
                'ems_tou_task.updateTime': '2025-08-04 16:34:56',
                'error_code.bpErrCode': [{'errCode': [],
                                            'moduleSn': 'SEozQVpESEFaSDNWMDMwNQ=='},
                                        {'errCode': [],
                                            'moduleSn': 'SEozQVpEMUFaSDRGMDIxNg=='},
                                        {'errCode': [],
                                            'moduleSn': 'SEozQVpESEFaSDNWMDY2OQ=='}],
                'error_code.emsErrCode.errCode': [523],
                'error_code.emsErrCode.moduleSn': 'SEozMVpEMUFaSDNVMDE0MA==',
                'error_code.pcsErrCode.errCode': [],
                'error_code.pcsErrCode.moduleSn': 'SEozMTIxMDJCRzNBMDQzNw==',
                'error_code.updateTime': '2025-08-04 20:18:08',
                'error_code_mark_report.errorCode': [0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0],
                'error_code_mark_report.updateTime': '2025-08-04 16:34:57',
                'mpptHeartBeat': [{'mpptPv': [{'amp': 2.0649018,
                                                'pwr': 870.3428,
                                                'vol': 421.49353},
                                                {'amp': 2.930396,
                                                'pwr': 635.6013,
                                                'vol': 216.89946}]}],
                'mpptPwr': 3080.0,
                'pcsAPhase.actPwr': -410.43326,
                'pcsAPhase.amp': 1.7866042,
                'pcsAPhase.apparentPwr': 432.09467,
                'pcsAPhase.reactPwr': 135.09384,
                'pcsAPhase.vol': 241.8525,
                'pcsBPhase.actPwr': -412.5142,
                'pcsBPhase.amp': 1.7850913,
                'pcsBPhase.apparentPwr': 435.90646,
                'pcsBPhase.reactPwr': 140.87755,
                'pcsBPhase.vol': 244.19281,
                'pcsCPhase.actPwr': -407.78058,
                'pcsCPhase.amp': 1.8013728,
                'pcsCPhase.apparentPwr': 431.87854,
                'pcsCPhase.reactPwr': 142.24654,
                'pcsCPhase.vol': 239.74968,
                'pvInvPwr': 0.0,
                'sysGridPwr': -2780.0,
                'sysLoadPwr': 300.0},
        'eagleEyeTraceId': 'ea1a2a350917543098960671802d0007',
        'message': 'Success',
        'tid': ''}
        """

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
            VoltSensorEntity(client, self, "pcsAPhase.vol", const.POWEROCEAN_VOLT_L1),
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
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []
        # return [
        #     ChargingPowerEntity(
        #         client,
        #         self,
        #         "cfgPlugInInfoAcInChgPowMax",
        #         const.AC_CHARGING_POWER,
        #         400,
        #         2900,
        #         lambda value: {
        #             "sn": self.device_info.sn,
        #             "cmdId": 17,
        #             "dirDest": 1,
        #             "dirSrc": 1,
        #             "cmdFunc": 254,
        #             "dest": 2,
        #             "params": {"cfgPlugInInfoAcInChgPowMax": value},
        #         },
        #     ),
        # ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []

    def buttons(self, client: EcoflowApiClient) -> list[BaseButtonEntity]:
        return []
