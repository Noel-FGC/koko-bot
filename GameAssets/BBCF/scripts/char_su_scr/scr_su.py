@Subroutine
def GetUnLockPower():
    if SLOT_4 == 8191:
        pass
    else:
        SLOT_5 = SLOT_5 + 1
        if SLOT_5 == 9:
            SLOT_5 = 1


@Subroutine
def GetUnLockPowerRep():
    SLOT_4 and 4
    if not SLOT_0 == 4:
        SLOT_5 = 1
    else:
        SLOT_4 and 8
        if not SLOT_0 == 8:
            SLOT_5 = 2
        else:
            SLOT_4 and 512
            if not SLOT_0 == 512:
                SLOT_5 = 3
            else:
                SLOT_4 and 2048
                if not SLOT_0 == 2048:
                    SLOT_5 = 4
                else:
                    SLOT_4 and 4096
                    if not SLOT_0 == 4096:
                        SLOT_5 = 5
                    else:
                        SLOT_4 and 64
                        if not SLOT_0 == 64:
                            SLOT_5 = 6
                        else:
                            SLOT_4 and 32
                            if not SLOT_0 == 32:
                                SLOT_5 = 7
                            else:
                                SLOT_4 and 16
                                if not SLOT_0 == 16:
                                    SLOT_5 = 8


@Subroutine
def UseUnLockPowerForce():
    if SLOT_5 == 1:
        SLOT_4 and 4
        if SLOT_0 == 4:
            callSubroutine('GetUnLockPower')
        else:
            SLOT_4 and 2
            if SLOT_0 == 2:
                ModifyVar_(8, 2, 4, 0, 4)
                SLOT_5 = 0
                callSubroutine('EmissionStart')
                Unknown30016(255)
                CreateObject('suef_unlock1st', 103)
                callSubroutine('UseUnLockPowerSE')
                Voiceline('su300')
            else:
                SLOT_4 and 1
                if SLOT_0 == 1:
                    ModifyVar_(8, 2, 4, 0, 2)
                    SLOT_5 = 0
                    callSubroutine('EmissionStart')
                    Unknown30016(255)
                    CreateObject('suef_unlock1st', 103)
                    callSubroutine('UseUnLockPowerSE')
                    Voiceline('su300')
                else:
                    ModifyVar_(8, 2, 4, 0, 1)
                    SLOT_5 = 0
                    callSubroutine('EmissionStart')
                    Unknown30016(255)
                    CreateObject('suef_unlock1st', 103)
                    callSubroutine('UseUnLockPowerSE')
                    Voiceline('su300')
    elif SLOT_5 == 2:
        SLOT_4 and 8
        if SLOT_0 == 8:
            callSubroutine('GetUnLockPower')
        else:
            ModifyVar_(8, 2, 4, 0, 8)
            SLOT_5 = 0
            callSubroutine('EmissionStart')
            Unknown30016(255)
            CreateObject('suef_unlock2nd', 103)
            callSubroutine('UseUnLockPowerSE')
            Voiceline('su301')
    elif SLOT_5 == 3:
        SLOT_4 and 512
        if SLOT_0 == 512:
            callSubroutine('GetUnLockPower')
        else:
            SLOT_4 and 256
            if SLOT_0 == 256:
                ModifyVar_(8, 2, 4, 0, 512)
                SLOT_5 = 0
                callSubroutine('EmissionStart')
                Unknown30016(255)
                CreateObject('suef_unlock3rd', 103)
                callSubroutine('UseUnLockPowerSE')
                Voiceline('su302')
            else:
                SLOT_4 and 128
                if SLOT_0 == 128:
                    ModifyVar_(8, 2, 4, 0, 256)
                    SLOT_5 = 0
                    callSubroutine('EmissionStart')
                    Unknown30016(255)
                    CreateObject('suef_unlock3rd', 103)
                    callSubroutine('UseUnLockPowerSE')
                    Voiceline('su302')
                else:
                    ModifyVar_(8, 2, 4, 0, 128)
                    SLOT_5 = 0
                    callSubroutine('EmissionStart')
                    Unknown30016(255)
                    CreateObject('suef_unlock3rd', 103)
                    callSubroutine('UseUnLockPowerSE')
                    Voiceline('su302')
    elif SLOT_5 == 4:
        SLOT_4 and 2048
        if SLOT_0 == 2048:
            callSubroutine('GetUnLockPower')
        else:
            SLOT_4 and 1024
            if SLOT_0 == 1024:
                ModifyVar_(8, 2, 4, 0, 2048)
                SLOT_5 = 0
                callSubroutine('EmissionStart')
                Unknown30016(255)
                CreateObject('suef_unlock4th', 103)
                callSubroutine('UseUnLockPowerSE')
                Voiceline('su303')
            else:
                ModifyVar_(8, 2, 4, 0, 1024)
                SLOT_5 = 0
                callSubroutine('EmissionStart')
                Unknown30016(255)
                CreateObject('suef_unlock4th', 103)
                callSubroutine('UseUnLockPowerSE')
                Voiceline('su303')
    elif SLOT_5 == 5:
        SLOT_4 and 4096
        if SLOT_0 == 4096:
            callSubroutine('GetUnLockPower')
        else:
            ModifyVar_(8, 2, 4, 0, 4096)
            SLOT_5 = 0
            callSubroutine('EmissionStart')
            Unknown30016(255)
            CreateObject('suef_unlock5th', 103)
            callSubroutine('UseUnLockPowerSE')
            Voiceline('su304')
    elif SLOT_5 == 6:
        SLOT_4 and 64
        if SLOT_0 == 64:
            callSubroutine('GetUnLockPower')
        else:
            ModifyVar_(8, 2, 4, 0, 64)
            SLOT_5 = 0
            callSubroutine('EmissionStart')
            Unknown30016(255)
            CreateObject('suef_unlock6th', 103)
            callSubroutine('UseUnLockPowerSE')
            Voiceline('su305')
    elif SLOT_5 == 7:
        SLOT_4 and 32
        if SLOT_0 == 32:
            callSubroutine('GetUnLockPower')
        else:
            ModifyVar_(8, 2, 4, 0, 32)
            SLOT_5 = 0
            callSubroutine('EmissionStart')
            Unknown30016(255)
            CreateObject('suef_unlock7th', 103)
            callSubroutine('UseUnLockPowerSE')
            Voiceline('su306')
    elif SLOT_5 == 8:
        SLOT_4 and 16
        if SLOT_0 == 16:
            callSubroutine('GetUnLockPower')
        else:
            ModifyVar_(8, 2, 4, 0, 16)
            SLOT_5 = 0
            callSubroutine('EmissionStart')
            Unknown30016(255)
            CreateObject('suef_unlock8th', 103)
            callSubroutine('UseUnLockPowerSE')
            Voiceline('su307')
    elif SLOT_5 == 0:
        callSubroutine('GetUnLockPower')


@Subroutine
def UseUnLockPowerSE():
    PrivateSE('suse_01')
    PrivateSE('suse_01')
    Hitstop(20)


@Subroutine
def PreInit():
    CharacterID('su')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(12500)
    WalkFSpeed(7000)
    WalkBSpeed(4800)
    DashFInitialVelocity(11000)
    DashFAccel(200)
    DashFMaxVelocity(33000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(42000)
    Gravity(1650)
    AirFDashDuration(16)
    ExtendCollisionX(25)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(4)
    FootstepSE(0)
    CreateDecalOn(1)
    CPUJumpPriority(2000)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(1)
    DamageStunPriority(4000)
    SkillEstimateRange(0, 250000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    JumpAvoidPriority(10000)
    SkillEstimateRange(750000, 1200000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(4000)
    SkillEstimateRange(0, 300000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    SkillEstimateRange(-50000, 550000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveCancellableFrames(58, 60)
    GuardStunPriority(2000)
    SkillEstimateRange(200000, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    DamageStunPriority(2000)
    AirborneOpponentPriority(500)
    SkillEstimateRange(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 550000, -200000, 150000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveMaxChainRepeat(1)
    MoveMid()
    SkillEstimateRange(0, 400000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    MoveCancellableFrames(28, 30)
    AirborneOpponentPriority(4000)
    SkillEstimateRange(-100000, 350000, 200000, 550000, 500, 5)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    MoveCancellableFrames(38, 40)
    SkillEstimateRange(0, 450000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    AirborneOpponentPriority(0)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 500000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    MoveMid()
    DamageStunPriority(500)
    SkillEstimateRange(-250000, 400000, -200000, 400000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4D', INPUT_4D)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(0)
    SkillEstimateRange(1100000, 1500000, -200000, 100000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    MoveLow()
    AirborneOpponentPriority(0)
    SkillEstimateRange(0, 500000, -100000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(500)
    SkillEstimateRange(-200000, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 450000, -300000, 300000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SkillEstimateRange(0, 500000, -400000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    SkillEstimateRange(-300000, 300000, -300000, 300000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    DamageStunPriority(0)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 400000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('RushAssault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('RushAssault')
    CallSkillConditions('CheckEnableRushAssault_OneButto')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('LongAssault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('LongAssault')
    CallSkillConditions('CheckEnableLongAssault_OneButto')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Assault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('Assault')
    CallSkillConditions('CheckEnableAssault_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('LowAssault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('LowAssault')
    CallSkillConditions('CheckEnableLowAssault_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Shot_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('Shot')
    CallSkillConditions('CheckEnableShot_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('MidAssault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('MidAssault')
    CallSkillConditions('CheckEnableMidAssault_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AirMidAssault_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AirMidAssault')
    CallSkillConditions('CheckEnableMidAssault_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AntiAir_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AntiAir')
    CallSkillConditions('CheckEnableAntiAir_OneButton')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AssaultThrow_OneButton', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AssaultThrow')
    CallSkillConditions('CheckEnableAssaultThrow_OneButt')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('RushAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0xc6)
    CallSkillConditions('CheckEnableRushAssault')
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 400000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('LongAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckEnableLongAssault')
    SkillEstimateRange(0, 1000000, -200000, 200000, 150, 10)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    CallSkillConditions('CheckEnableAssault')
    SkillEstimateRange(350000, 750000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('LowAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    CallSkillConditions('CheckEnableLowAssault')
    MoveLow()
    SkillEstimateRange(350000, 750000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    CallSkillConditions('CheckEnableShot')
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 550000, -200000, 300000, 500, 10)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    CallSkillConditions('CheckEnableMidAssault')
    MoveMid()
    AirborneOpponentPriority(0)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AirMidAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    CallSkillConditions('CheckEnableMidAssault')
    SkillEstimateRange(0, 400000, -400000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    CallSkillConditions('CheckEnableAntiAir')
    OpponentAttackPriority(4000)
    AirborneOpponentPriority(0)
    SkillEstimateRange(-300000, 350000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('AssaultThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_C)
    CallSkillConditions('CheckEnableAssaultThrow')
    MoveThrow()
    AirborneOpponentPriority(0)
    SkillEstimateRange(0, 600000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateLongAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckEnableUltimateLongAssault')
    DamageStunPriority(1)
    OpponentAttackPriority(4000)
    SkillEstimateRange(650000, 1500000, -200000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateLongAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    CallSkillConditions('CheckEnableUltimateLongAssault')
    DamageStunPriority(1)
    OpponentAttackPriority(4000)
    SkillEstimateRange(650000, 1500000, -200000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateRushAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateRushAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateCommand', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_2HOLD8)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    MovePriority(5000)
    OpponentAttackPriority(0)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    Unknown15027(0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_2141236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(8000)
    SkillEstimateRange(-300000, 300000, -200000, 300000, 500, 10)
    Move_EndRegister()
    Move_Register('BurstDD_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    Move_Input_(INPUT_HOLD_B)
    Move_Input_(INPUT_HOLD_C)
    Move_Input_(INPUT_HOLD_D)
    Move_Condition(0x3081)
    CallSkillConditions('Func_BurstDD_Easy')
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('BurstDD_Cancel', INPUT_SPECIALMOVE)
    StateCall('BurstDD_Easy')
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('BurstDD', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    NeutralOnly(1)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 1)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'FHighJump', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'UltimateLongAssault', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'UltimateLongAssaultOD', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'FHighJump', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk2D', 'Assault', 10000000)
    TempPriorityMultiplier('NmlAtk2D', 'LowAssault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Assault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'LowAssault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk4D', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk4D', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk6D', 'LowAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6D', 'LongAssault', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('LowAssault', 'FHighJump', 10000000)
    StylishModeSpecialButton('Assault', 0x4, 0xea)
    StylishModeSpecialButton('AntiAir', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0x79)
    StylishModeSpecialButton('Assault', 0x4, 0x45)
    StylishModeSpecialButton('Shot', 0x4, 0x45)
    StylishModeSpecialButton('Assault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateRushAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateRushAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('AirMidAssault', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk2C', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 8, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk5C', 'FJump', 3, 0)
    StylishModeCancels('NmlAtk5C', 'FHighJump', 3, 130000)
    StylishModeCancels('NmlAtk5D', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk5D', 'NmlAtk6D', 13, 0)
    StylishModeCancels('NmlAtk5D', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk5D', 'RushAssault', 13, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk4D', 6, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk6D', 3, 0)
    StylishModeCancels('NmlAtk6D', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk6D', 'RushAssault', 10, 350000)
    StylishModeCancels('NmlAtk6D', 'MidAssault', 6, 0)
    StylishModeCancels('NmlAtk6D', 'LowAssault', 6, 0)
    StylishModeCancels('NmlAtk6D', 'LongAssault', 10, 800000)
    StylishModeCancels('LowAssault', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2C', 3, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk2C', 3, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 3, 0)
    StylishModeCancels('NmlAtk2C', 'FHighJump', 3, 130000)
    StylishModeCancels('NmlAtk2D', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk2D', 'RushAssault', 10, 350000)
    StylishModeCancels('NmlAtk2D', 'LowAssault', 6, 0)
    StylishModeCancels('NmlAtk2D', 'LongAssault', 10, 800000)
    StylishModeCancels('NmlAtk2D', 'UltimateRushAssault', 6, 0)
    StylishModeCancels('NmlAtk2D', 'UltimateRushAssaultOD', 6, 0)
    StylishModeCancels('NmlAtk2D', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk3C', 'RushAssault', 10, 350000)
    StylishModeCancels('NmlAtk3C', 'LowAssault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'LongAssault', 10, 800000)
    StylishModeCancels('NmlAtk3C', 'UltimateRushAssault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateRushAssaultOD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk3C', 'RushAssault', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirMidAssault', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 13, 0)
    HitSprites(0, 'su062_01')
    HitSprites(1, 'su062_03')
    HitSprites(2, 'su062_04')
    HitSprites(3, 'su062_05')
    HitSprites(4, 'su062_05')
    HitSprites(5, 'su062_06')
    HitSprites(6, 'su062_07')
    HitSprites(7, 'su041_02')
    HitSprites(8, 'su040_02')
    HitSprites(9, 'su045_02')
    HitSprites(10, 'su060_00')
    HitSprites(11, 'su060_01')
    HitSprites(12, 'su060_03')
    HitSprites(13, 'su060_05')
    HitSprites(14, 'su060_07')
    HitSprites(15, 'su060_14')
    HitSprites(16, 'su050_00')
    HitSprites(17, 'su052_00')
    HitSprites(18, 'su054_00')
    HitSprites(19, 'su000_00')
    HitSprites(20, 'su000_00')
    HitSprites(25, 'su063_00')
    HitSprites(26, 'su063_01')
    HitSprites(27, 'su063_02')
    HitSprites(28, 'su063_04')
    HitSprites(29, 'su063_10')
    HitSprites(30, 'su077_00')
    HitSprites(31, 'su077_01')
    HitSprites(32, 'su077_00ex00')
    HitSprites(33, 'su077_01ex00')
    HitSprites(34, 'su077_00ex01')
    HitSprites(35, 'su077_01ex01')
    HitSprites(36, 'su077_00ex02')
    HitSprites(37, 'su077_01ex02')
    HitSprites(24, 'su073_01')
    CommonVoicelines(0, 'su000')
    CommonVoicelines(1, 'su001')
    CommonVoicelines(2, 'su002')
    CommonVoicelines(3, 'su003')
    CommonVoicelines(4, 'su004')
    CommonVoicelines(5, 'su005')
    CommonVoicelines(6, 'su006')
    CommonVoicelines(7, 'su007')
    CommonVoicelines(8, 'su008')
    CommonVoicelines(9, 'su009')
    CommonVoicelines(10, 'su010')
    CommonVoicelines(11, 'su011')
    CommonVoicelines(12, 'su012')
    CommonVoicelines(13, 'su013')
    CommonVoicelines(14, 'su014')
    CommonVoicelines(15, 'su015')
    CommonVoicelines(16, 'su016')
    CommonVoicelines(17, 'su017')
    CommonVoicelines(18, 'su018')
    CommonVoicelines(19, 'su019')
    CommonVoicelines(20, 'su020')
    CommonVoicelines(21, 'su021')
    CommonVoicelines(22, 'su022')
    CommonVoicelines(23, 'su023')
    CommonVoicelines(24, 'su024')
    CommonVoicelines(25, 'su025')
    CommonVoicelines(26, 'su026')
    CommonVoicelines(27, 'su027')
    CommonVoicelines(28, 'su028')
    CommonVoicelines(29, 'su029')
    CommonVoicelines(30, 'su030')
    CommonVoicelines(31, 'su031')
    CommonVoicelines(32, 'su032')
    CommonVoicelines(33, 'su033')
    CommonVoicelines(34, 'su034')
    CommonVoicelines(35, 'su035')
    CommonVoicelines(36, 'su036')
    CommonVoicelines(37, 'su037')
    CommonVoicelines(38, 'su038')
    CommonVoicelines(39, 'su039')
    CommonVoicelines(40, 'su040')
    CommonVoicelines(41, 'su041')
    CommonVoicelines(42, 'su042')
    CommonVoicelines(43, 'su043')
    CommonVoicelines(44, 'su044')
    CommonVoicelines(45, 'su045')
    CommonVoicelines(46, 'su046')
    CommonVoicelines(47, 'su047')
    CommonVoicelines(48, 'su048')
    CommonVoicelines(49, 'su049')
    CommonVoicelines(50, 'su050')
    CommonVoicelines(51, 'su051')
    CommonVoicelines(52, 'su052')
    CommonVoicelines(53, 'su053')
    CommonVoicelines(54, 'su100')
    CommonVoicelines(55, 'su101')
    CommonVoicelines(56, 'su102')
    CommonVoicelines(57, 'su103')
    CommonVoicelines(58, 'su104')
    CommonVoicelines(59, 'su105')
    CommonVoicelines(60, 'su106')
    CommonVoicelines(61, 'su107')
    CommonVoicelines(62, 'su108')
    CommonVoicelines(63, 'su109')
    CommonVoicelines(64, 'su150')
    CommonVoicelines(65, 'su151')
    CommonVoicelines(66, 'su152')
    CommonVoicelines(67, 'su153')
    CommonVoicelines(68, 'su154')
    CommonVoicelines(69, 'su155')
    CommonVoicelines(70, 'su156')
    CommonVoicelines(71, 'su157')
    CommonVoicelines(72, 'su158')
    CommonVoicelines(75, 'su160')
    CommonVoicelines(73, 'su402')
    CommonVoicelines(74, 'su403')
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(5)
    Unknown30009(11)


@Subroutine
def MatchInit2():
    Unknown30007(0)
    Unknown30011('')
    SLOT_4 = 1


@Subroutine
def CheckEnableAssault():
    SLOT_47 = 0
    SLOT_4 and 1
    if SLOT_0 == 1:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableAntiAir():
    SLOT_47 = 0
    SLOT_4 and 8
    if SLOT_0 == 8:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableLongAssault():
    SLOT_47 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableAssaultThrow():
    SLOT_47 = 0
    SLOT_4 and 32
    if SLOT_0 == 32:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableRushAssault():
    SLOT_47 = 0
    SLOT_4 and 64
    if SLOT_0 == 64:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableShot():
    SLOT_47 = 0
    SLOT_4 and 128
    if SLOT_0 == 128:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableMidAssault():
    SLOT_47 = 0
    SLOT_4 and 1024
    if SLOT_0 == 1024:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableLowAssault():
    SLOT_47 = 0
    SLOT_4 and 4096
    if SLOT_0 == 4096:
        SLOT_47 = 1
    elif SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckEnableUltimateLongAssault():
    SLOT_47 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SLOT_47 = 1


@Subroutine
def CheckEnableAssault_OneButton():
    SLOT_47 = 0
    if SLOT_56 == 1:
        SLOT_47 = 1


@Subroutine
def CheckEnableAntiAir_OneButton():
    SLOT_47 = 0
    if SLOT_56 == 2:
        SLOT_47 = 1


@Subroutine
def CheckEnableShot_OneButton():
    SLOT_47 = 0
    if SLOT_56 == 3:
        SLOT_47 = 1


@Subroutine
def CheckEnableMidAssault_OneButton():
    SLOT_47 = 0
    if SLOT_56 == 4:
        SLOT_47 = 1


@Subroutine
def CheckEnableLowAssault_OneButton():
    SLOT_47 = 0
    if SLOT_56 == 5:
        SLOT_47 = 1


@Subroutine
def CheckEnableRushAssault_OneButto():
    SLOT_47 = 0
    if SLOT_56 == 6:
        SLOT_47 = 1


@Subroutine
def CheckEnableAssaultThrow_OneButt():
    SLOT_47 = 0
    if SLOT_56 == 7:
        SLOT_47 = 1


@Subroutine
def CheckEnableLongAssault_OneButto():
    SLOT_47 = 0
    if SLOT_56 == 8:
        SLOT_47 = 1


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_InNeutral:
            if SLOT_4 == 8191:
                SLOT_5 = 0
            TrainingModeSLOT('TRI_SusanooUnlock1', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 1)
                ModifyVar_(8, 2, 4, 0, 2)
            if SLOT_67 == 2:
                ModifyVar_(8, 2, 4, 0, 1)
                ModifyVar_(8, 2, 4, 0, 2)
                ModifyVar_(8, 2, 4, 0, 4)
            TrainingModeSLOT('TRI_SusanooUnlock2', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 8)
            TrainingModeSLOT('TRI_SusanooUnlock3', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 128)
            if SLOT_67 == 2:
                ModifyVar_(8, 2, 4, 0, 128)
                ModifyVar_(8, 2, 4, 0, 256)
            if SLOT_67 == 3:
                ModifyVar_(8, 2, 4, 0, 128)
                ModifyVar_(8, 2, 4, 0, 256)
                ModifyVar_(8, 2, 4, 0, 512)
            TrainingModeSLOT('TRI_SusanooUnlock4', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 1024)
            if SLOT_67 == 2:
                ModifyVar_(8, 2, 4, 0, 1024)
                ModifyVar_(8, 2, 4, 0, 2048)
            TrainingModeSLOT('TRI_SusanooUnlock5', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 4096)
            TrainingModeSLOT('TRI_SusanooUnlock6', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 64)
            TrainingModeSLOT('TRI_SusanooUnlock7', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 32)
            TrainingModeSLOT('TRI_SusanooUnlock8', 2, 67)
            if SLOT_67 == 1:
                ModifyVar_(8, 2, 4, 0, 16)
        if SLOT_7:
            if not CurrentStateCheck('UltimateLongAssault'):
                if not CurrentStateCheck('UltimateLongAssaultOD'):
                    SLOT_7 = 0
    if SLOT_CurrentHealth:
        if not SLOT_IsInHitstun:
            if not SLOT_6:
                CreateObject('suef_aura', 103)


@Subroutine
def EmissionStart():
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(5)
    Unknown30016(0)
    Unknown30017(0)
    if not SLOT_57:
        Unknown30009(11)


@Subroutine
def OnFinalize():
    Unknown30007(0)
    Unknown30011('')
    Unknown30016(255)
    Unknown30017(0)
    SLOT_7 = 0


@Subroutine
def OnPreDraw():
    CallPrivateFunction('SU_Light', 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActStand():
    label(0)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(0, 2, 123):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('su001_00', 6)
    SLOT_88 = 960

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    callSubroutine('EmissionStart')
    Unknown30017(17)
    CreateObject('suef_001', -1)
    CreateObject('suef_001_blm_2d', -1)
    CommonSE('022_magiccircle_b')
    SmartVoiceline('su000')
    sprite('su001_01', 6)
    sprite('su001_02', 7)
    sprite('su001_03', 8)
    sprite('su001_04', 9)
    sprite('su001_05', 9)
    sprite('su001_06', 9)
    sprite('su001_07', 8)
    sprite('su001_08', 7)
    Unknown30017(-12)
    sprite('su001_09', 6)
    sprite('su001_10', 6)
    SLOT_57 = 0
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(STATE_END)
    SLOT_6 = 0
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('su003_00', 3)
    sprite('su003_01', 3)
    sprite('su003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('su010_00', 4)
    sprite('su010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('su010_02', 6)
    sprite('su010_03', 6)
    sprite('su010_04', 6)
    sprite('su010_05', 6)
    sprite('su010_06', 6)
    sprite('su010_07', 6)
    sprite('su010_08', 6)
    sprite('su010_09', 6)
    sprite('su010_10', 6)
    sprite('su010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('su013_00', 3)
    sprite('su013_01', 3)
    sprite('su013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('su010_01', 4)
    sprite('su010_00', 4)


@State
def CmnActJumpPre():
    sprite('su023_00', 2)
    sprite('su023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('su020_00', 4)
    sprite('su020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('su020_02', 3)
    sprite('su020_03', 3)
    sprite('su020_04', 3)


@State
def CmnActJumpDown():
    sprite('su020_05', 3)
    sprite('su020_06', 3)
    label(0)
    sprite('su020_07', 4)
    sprite('su020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    LandingEffects(100, 1, 0)
    sprite('su024_00', 3)
    sprite('su024_01', 3)
    sprite('su024_02', 3)
    sprite('su024_03', 3)
    sprite('su024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('su024_00', 2)
    sprite('su024_01', 2)
    sprite('su024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('su024_03', 3)
    sprite('su024_04', 3)


@State
def CmnActFWalk():
    sprite('su030_00', 7)
    label(0)
    sprite('su030_01', 7)
    sprite('su030_02', 7)
    sprite('su030_03', 7)
    sprite('su030_04', 7)
    sprite('su030_05', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su030_06', 7)
    sprite('su030_07', 7)
    sprite('su030_08', 7)
    sprite('su030_09', 7)
    sprite('su030_10', 7)
    sprite('su030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su030_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('su031_00', 7)
    label(0)
    sprite('su031_01', 7)
    sprite('su031_02', 7)
    sprite('su031_03', 7)
    sprite('su031_04', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su031_05', 7)
    sprite('su031_06', 7)
    sprite('su031_07', 7)
    sprite('su031_08', 7)
    sprite('su031_09', 7)
    sprite('su031_10', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su031_11', 7)
    sprite('su031_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('su032_15', 3)
    EndMomentum(1)
    sprite('su032_14', 3)
    sprite('su032_13', 3)
    sprite('su032_12', 3)
    sprite('su032_11', 3)
    sprite('su032_00', 3)
    XSpeed(31000)
    label(0)
    sprite('su032_01', 4)
    sprite('su032_02', 4)
    sprite('su032_03', 4)
    sprite('su032_04', 4)
    DashEffects(100, 1, 1)
    sprite('su032_05', 4)
    sprite('su032_06', 4)
    sprite('su032_07', 4)
    sprite('su032_08', 4)
    DashEffects(100, 1, 1)
    sprite('su032_09', 4)
    sprite('su032_10', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('su032_11', 3)
    sprite('su032_12', 3)
    sprite('su032_13', 3)
    sprite('su032_14', 3)
    sprite('su032_15', 3)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()

        def upon_STATE_END():
            physicsYImpulse(0)
            setGravity(0)
    sprite('su033_00', 1)
    sprite('su033_01', 3)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('su033_02', 1)
    sprite('su033_02', 2)
    setInvincible(0)
    loopRest()
    label(0)
    sprite('su033_01', 3)
    sprite('su033_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su033_03', 3)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('su033_04', 3)
    sprite('su033_05', 3)
    WhiffFWalkCancel(1)
    WhiffFDashCancel(1)
    WhiffBWalkCancel(1)
    WhiffBDashCancel(1)
    WhiffJumpCancel(1)
    WhiffBlockCancel(1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    sprite('su033_06', 3)
    sprite('su033_07', 3)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('su035_00', 3)
    label(0)
    sprite('su035_01', 3)
    sprite('su035_02', 3)
    sprite('su035_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('su036_00', 3)
    label(0)
    sprite('su036_01', 3)
    sprite('su036_02', 3)
    sprite('su036_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('su050_00', 1)
    sprite('su050_01', 1)
    sprite('su050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('su050_01', 1)
    sprite('su050_02', 1)
    sprite('su050_01', 2)
    sprite('su050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('su050_02', 1)
    sprite('su050_03', 1)
    sprite('su050_02', 2)
    sprite('su050_01', 2)
    sprite('su050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('su050_03', 1)
    sprite('su050_04', 1)
    sprite('su050_03', 2)
    sprite('su050_02', 2)
    sprite('su050_01', 2)
    sprite('su050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('su050_04', 1)
    sprite('su050_04', 1)
    sprite('su050_04', 2)
    sprite('su050_03', 2)
    sprite('su050_02', 2)
    sprite('su050_01', 2)
    sprite('su050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('su052_00', 1)
    sprite('su052_01', 1)
    sprite('su052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('su052_01', 1)
    sprite('su052_02', 1)
    sprite('su052_01', 2)
    sprite('su052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('su052_02', 1)
    sprite('su052_03', 1)
    sprite('su052_02', 2)
    sprite('su052_01', 2)
    sprite('su052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('su052_03', 1)
    sprite('su052_04', 1)
    sprite('su052_03', 2)
    sprite('su052_02', 2)
    sprite('su052_01', 2)
    sprite('su052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('su052_04', 1)
    sprite('su052_04', 1)
    sprite('su052_04', 2)
    sprite('su052_03', 2)
    sprite('su052_02', 2)
    sprite('su052_01', 2)
    sprite('su052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('su054_00', 1)
    sprite('su054_01', 1)
    sprite('su054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('su054_01', 1)
    sprite('su054_02', 1)
    sprite('su054_01', 2)
    sprite('su054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('su054_02', 1)
    sprite('su054_03', 1)
    sprite('su054_02', 2)
    sprite('su054_01', 2)
    sprite('su054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('su054_03', 1)
    sprite('su054_04', 1)
    sprite('su054_03', 2)
    sprite('su054_02', 2)
    sprite('su054_01', 2)
    sprite('su054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('su054_04', 1)
    sprite('su054_04', 1)
    sprite('su054_04', 2)
    sprite('su054_03', 2)
    sprite('su054_02', 2)
    sprite('su054_01', 2)
    sprite('su054_00', 2)


@State
def CmnActBDownUpper():
    sprite('su060_00', 4)
    label(0)
    sprite('su060_01', 4)
    sprite('su060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('su060_03', 4)


@State
def CmnActBDownDown():
    sprite('su060_04', 4)
    label(0)
    sprite('su060_05', 4)
    sprite('su060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('su060_07', 2)
    sprite('su060_08', 2)


@State
def CmnActBDownBound():
    sprite('su060_09', 3)
    sprite('su060_10', 3)
    sprite('su060_11', 3)
    sprite('su060_12', 3)
    sprite('su060_13', 3)


@State
def CmnActBDownLoop():
    sprite('su060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('su061_00', 3)
    sprite('su061_01', 3)
    sprite('su061_02', 3)
    sprite('su061_03', 3)
    sprite('su061_04', 3)
    sprite('su061_05', 3)
    sprite('su061_06', 2)
    sprite('su061_07', 2)
    sprite('su061_08', 3)
    sprite('su061_09', 3)


@State
def CmnActFDownUpper():
    sprite('su063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('su063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('su063_02', 3)
    sprite('su063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('su063_04', 3)
    sprite('su063_05', 3)


@State
def CmnActFDownBound():
    sprite('su063_06', 2)
    sprite('su063_07', 2)
    sprite('su063_08', 3)
    sprite('su063_09', 3)
    sprite('su063_10', 3)


@State
def CmnActFDownLoop():
    sprite('su063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('su064_00', 2)
    sprite('su064_01', 2)
    sprite('su064_02', 2)
    sprite('su064_03', 2)
    sprite('su064_04', 2)
    sprite('su064_05', 2)
    sprite('su064_06', 2)
    sprite('su064_07', 2)
    sprite('su064_08', 3)
    sprite('su064_09', 3)


@State
def CmnActVDownUpper():
    sprite('su062_00', 3)
    label(0)
    sprite('su062_01', 3)
    sprite('su062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('su062_03', 3)
    sprite('su062_04', 3)


@State
def CmnActVDownDown():
    sprite('su062_05', 3)
    sprite('su062_06', 3)
    label(0)
    sprite('su062_07', 3)
    sprite('su062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('su062_09', 2)
    sprite('su062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('su062_09', 2)
    sprite('su062_10', 2)


@State
def CmnActBlowoff():
    sprite('su072_00', 3)
    sprite('su072_01', 3)
    sprite('su072_02', 3)
    label(0)
    sprite('su072_01', 3)
    sprite('su072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('su074_00', 3)
    sprite('su074_01', 3)
    sprite('su074_02', 3)
    sprite('su074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('su082_00', 2)
    sprite('su082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('su071_04', 1)


@State
def CmnActWallBound():
    sprite('su073_00', 3)
    sprite('su073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('su073_02', 3)
    label(0)
    sprite('su073_03', 3)
    sprite('su073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('su070_00', 2)
    sprite('su070_01', 2)
    label(0)
    sprite('su070_02', 5)
    sprite('su070_03', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('su070_04', 4)
    sprite('su070_05', 4)
    sprite('su070_06', 4)
    sprite('su070_07', 4)
    sprite('su070_08', 4)
    sprite('su070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('su070_11', 2)
    sprite('su070_12', 3)
    sprite('su070_13', 3)


@State
def CmnActUkemiAirF():
    sprite('su113_00', 3)
    sprite('su113_01', 3)
    sprite('su113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('su113_00', 3)
    sprite('su113_01', 3)
    sprite('su113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('su113_00', 3)
    sprite('su113_01', 3)
    sprite('su113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('su110_00', 2)
    sprite('su110_01', 2)
    sprite('su110_02', 2)
    sprite('su110_03', 2)
    sprite('su110_04', 3)
    sprite('su110_05', 3)
    sprite('su110_06', 200)
    sprite('su110_07', 3)
    sprite('su110_08', 3)


@State
def CmnActUkemiLandB():
    sprite('su111_00', 3)
    sprite('su111_01', 3)
    sprite('su111_02', 3)
    sprite('su111_03', 3)
    sprite('su111_04', 3)
    sprite('su111_05', 3)
    sprite('su111_06', 200)
    sprite('su111_07', 3)
    sprite('su111_08', 3)


@State
def CmnActUkemiLandN():
    sprite('su112_00', 2)
    sprite('su112_01', 2)
    sprite('su112_02', 2)
    sprite('su112_03', 2)
    sprite('su112_04', 2)
    sprite('su112_05', 2)
    sprite('su112_06', 2)
    sprite('su112_07', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('su024_00', 3)
    sprite('su024_01', 3)
    sprite('su024_02', 3)
    sprite('su024_03', 3)
    sprite('su024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('su040_00', 3)
    sprite('su040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('su040_02', 4)
    sprite('su040_03', 4)
    sprite('su040_04', 4)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('su040_01', 3)
    sprite('su040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('su040_05', 3)
    label(0)
    sprite('su040_02', 3)
    sprite('su040_03', 3)
    sprite('su040_04', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('su040_01', 3)
    sprite('su040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('su041_00', 3)
    sprite('su041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('su041_02', 4)
    sprite('su041_03', 4)
    sprite('su041_04', 4)
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('su041_01', 3)
    sprite('su041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('su041_05', 3)
    label(0)
    sprite('su041_02', 4)
    sprite('su041_03', 4)
    sprite('su041_04', 4)
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('su041_01', 3)
    sprite('su041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('su043_00', 3)
    sprite('su043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('su043_02', 4)
    sprite('su043_03', 4)
    sprite('su043_04', 4)
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('su043_01', 3)
    sprite('su043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('su043_05', 3)
    label(0)
    sprite('su043_02', 4)
    sprite('su043_03', 4)
    sprite('su043_04', 4)
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('su043_01', 3)
    sprite('su043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('su045_00', 3)
    sprite('su045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('su045_02', 4)
    sprite('su045_03', 4)
    sprite('su045_04', 4)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('su045_01', 3)
    sprite('su045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('su045_05', 3)
    label(0)
    sprite('su045_02', 4)
    sprite('su045_03', 4)
    sprite('su045_04', 4)
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('su045_01', 3)
    sprite('su045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('su090_00', 2)
    sprite('su090_01', 2)
    sprite('su090_02', 1)
    SetCommonActionMark(1)
    sprite('su090_03', 6)
    sprite('su090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('su091_00', 2)
    sprite('su091_01', 2)
    sprite('su091_02', 1)
    SetCommonActionMark(1)
    sprite('su091_03', 6)
    sprite('su091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('su092_00', 2)
    sprite('su092_01', 2)
    sprite('su092_02', 1)
    SetCommonActionMark(1)
    sprite('su092_03', 6)
    sprite('su092_04', 6)


@State
def CmnActAirTurn():
    sprite('su025_00', 4)
    sprite('su025_01', 4)
    sprite('su025_02', 4)


@State
def CmnActLockWait():
    sprite('su040_02', 1)
    sprite('su040_01', 3)
    sprite('su040_00', 3)


@State
def CmnActLockReject():
    sprite('su312_00', 2)
    sprite('su312_01', 2)
    sprite('su312_02', 2)
    sprite('su312_03', 5)
    CreateObject('suef_312', -1)
    sprite('su312_04', 3)
    sprite('su312_05', 3)
    sprite('su312_06', 3)
    sprite('su312_07', 3)
    sprite('su312_08', 3)
    sprite('su312_09', 3)


@State
def CmnActAirLockWait():
    sprite('su045_02', 1)
    sprite('su045_01', 3)
    sprite('su045_00', 3)


@State
def CmnActAirLockReject():
    sprite('su322_00', 3)
    sprite('su322_01', 3)
    sprite('su322_02', 6)
    sprite('su322_03', 8)
    CreateObject('suef_312', -1)

    def RunOnObject_1():
        AddX(-48000)
    sprite('su322_04', 3)
    sprite('su322_05', 3)
    sprite('su322_06', 3)


@State
def CmnActLandSpin():
    sprite('su071_00', 4)
    sprite('su071_01', 4)
    label(0)
    sprite('su071_02', 2)
    sprite('su071_03', 2)
    sprite('su071_04', 2)
    sprite('su071_05', 2)
    sprite('su071_06', 2)
    sprite('su071_07', 2)
    sprite('su071_08', 2)
    sprite('su071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('su071_10', 6)
    sprite('su071_11', 5)
    sprite('su071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('su071_02', 2)
    sprite('su071_03', 2)
    sprite('su071_04', 2)
    sprite('su071_05', 2)
    sprite('su071_06', 2)
    sprite('su071_07', 2)
    sprite('su071_08', 2)
    sprite('su071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('su077_00', 2)
    sprite('su077_01', 2)
    sprite('su077_00ex00', 2)
    sprite('su077_01ex00', 2)
    sprite('su077_00ex01', 2)
    sprite('su077_01ex01', 2)
    sprite('su077_00ex02', 2)
    sprite('su077_01ex02', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('su077_02', 4)
    label(0)
    sprite('su077_03', 3)
    sprite('su077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('su077_05', 5)
    sprite('su077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('su060_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('su060_11', 4)
    sprite('su060_13', 5)


@State
def CmnActBurstBegin():
    sprite('su331_00', 2)
    CreateObject('suef_331', 103)
    sprite('su331_01', 2)
    label(0)
    sprite('su331_02', 3)
    sprite('su331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('su331_04', 2)
    sprite('su331_05', 2)
    SLOT_57 = 1
    callSubroutine('EmissionStart')
    Unknown30016(255)
    label(0)
    sprite('su331_06', 3)
    sprite('su331_07', 3)
    sprite('su331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('su331_09', 3)
    SLOT_57 = 1
    callSubroutine('EmissionStart')
    Unknown30016(255)
    Unknown30017(-42)
    sprite('su331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('su331_11', 2)
    CreateObject('suef_331', 103)
    sprite('su331_12', 2)
    label(0)
    sprite('su331_02', 3)
    sprite('su331_03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('su331_04', 2)
    sprite('su331_05', 2)
    SLOT_57 = 1
    callSubroutine('EmissionStart')
    Unknown30016(255)
    label(0)
    sprite('su331_06', 2)
    sprite('su331_07', 2)
    sprite('su331_08', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('su331_13', 2)
    SLOT_57 = 1
    callSubroutine('EmissionStart')
    Unknown30016(255)
    Unknown30017(-42)
    sprite('su331_14', 2)
    sprite('su020_05', 3)
    sprite('su020_06', 3)
    label(0)
    sprite('su020_07', 4)
    sprite('su020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('su333_00', 3)
    sprite('su333_01', 3)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    sprite('su333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('su333_03', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('su333_04', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    label(0)
    sprite('su333_05', 3)
    sprite('su333_06', 3)
    sprite('su333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('su333_08', 6)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    Unknown30017(-21)
    sprite('su333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('su333_10', 3)
    sprite('su333_11', 3)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    sprite('su333_12', 3)
    CharacterFlash(16639, 20, 1)
    ParticleLayer(11)
    sprite('su333_13', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('su333_14', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    label(0)
    sprite('su333_05', 3)
    sprite('su333_06', 3)
    sprite('su333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('su333_15', 6)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    Unknown30017(-21)
    sprite('su333_16', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(450)
        PushbackX(12000)
        AirPushbackY(20000)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su200_00', 2)
    PerInertia(60)
    sprite('su200_01', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('su200_02', 2)
    RandomCommonVoiceline(0)
    sprite('su200_03', 5)
    CreateObject('suef_200', -1)
    sprite('su200_04', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('su200_05', 1)
    sprite('su200_06', 1)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(770)
        AirUntechableTime(19)
        AirPushbackY(20000)
        AirPushbackX(10000)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')
        HitJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
    sprite('su201_00', 2)
    sprite('su201_01', 3)
    CommonSE('005_swing_grap_2_1')
    sprite('su201_02', 3)
    RandomCommonVoiceline(1)
    sprite('su201_03', 2)
    sprite('su201_04', 4)
    sprite('su201_05', 2)
    Recovery()
    Unknown2063()
    sprite('su201_06', 2)
    sprite('su201_07', 3)
    sprite('su201_08', 3)
    sprite('su201_09', 3)
    sprite('su201_10', 3)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1000)
        Hitstop(15)
        PushbackX(39900)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
        if SLOT_93:
            WhiffCancel('RushAssault')
            WhiffCancelEnable(1)
    sprite('su202_00', 4)
    sprite('su202_01', 4)
    SetXCollisionFromOrigin(150)
    sprite('su202_02', 6)
    sprite('su202_03', 2)
    CommonSE('005_swing_grap_2_2')
    RandomCommonVoiceline(2)
    sprite('su202_04', 2)
    WhiffCancelEnable(0)
    sprite('su202_05', 4)
    sprite('su202_06', 4)
    Recovery()
    Unknown2063()
    sprite('su202_07', 4)
    sprite('su202_08', 2)
    SetXCollisionFromOrigin(-1)
    sprite('su202_09', 2)
    sprite('su202_10', 2)
    sprite('su202_11', 2)
    sprite('su202_12', 2)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1100)
        AttackP2(84)
        AirUntechableTime(45)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(10000)
        Wallbounce(1)
        NonCornerWallbounce(0)
        WallbounceReboundTime(0)
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('UseUnLockPowerForce')
        StayAfterMovement(1, 0)
    sprite('su203_00', 2)
    sprite('su203_01', 2)
    sprite('su203_02', 2)
    CreateObject('suef_203', -1)
    PrivateSE('suse_00')
    sprite('su203_03', 4)
    sprite('su203_04', 3)
    SetXCollisionFromOrigin(200)
    sprite('su203_05', 3)
    CommonSE('005_swing_grap_2_2')
    RandomCommonVoiceline(3)
    sprite('su203_06', 3)
    CreateObject('suef_203_atk', -1)
    SetXCollisionFromOrigin(250)
    ScreenShake(15000, 15000)
    sprite('su203_07', 3)
    Recovery()
    Unknown2063()
    sprite('su203_08', 4)
    sprite('su203_09', 4)
    sprite('su203_10', 4)
    sprite('su203_11', 4)
    SetXCollisionFromOrigin(-1)
    sprite('su203_12', 3)
    sprite('su203_13', 3)
    sprite('su203_14', 3)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su230_00', 2)
    PerInertia(60)
    sprite('su230_01', 2)
    sprite('su230_02', 2)
    CommonSE('005_swing_grap_2_0')
    RandomCommonVoiceline(0)
    sprite('su230_03', 2)
    CreateObject('suef_230', -1)
    sprite('su230_04', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('su230_05', 3)
    sprite('su230_06', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(720)
        AttackP1(90)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su231_00', 2)
    sprite('su231_01', 2)
    sprite('su231_01', 2)
    sprite('su231_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('006_swing_blade_1')
    sprite('su231_03', 3)
    CreateObject('suef_231', -1)
    sprite('su231_04', 4)
    Recovery()
    Unknown2063()
    sprite('su231_05', 4)
    sprite('su231_06', 4)
    sprite('su231_07', 4)
    sprite('su231_08', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AirUntechableTime(22)
        PushbackX(9900)
        MoveAttributes(0, 1, 0, 0, 0)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
        if SLOT_94:
            ChainCancel(0)
            SpecialCancel(0)
    sprite('su232_00', 3)
    sprite('su232_01', 3)
    SetAcceleration(10000)
    sprite('su232_02', 3)
    RandomCommonVoiceline(2)
    CommonSE('005_swing_grap_2_2')
    sprite('su232_03', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    CreateObject('suef_232', -1)
    EndMomentum(1)
    sprite('su232_03', 2)
    AttackOff()
    sprite('su232_04', 1)
    PushbackX(30400)
    RefreshMultihit()

    def upon_OPPONENT_HIT_OR_BLOCK():
        HitOrBlockJumpCancel(1)
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            ChainCancel(1)
            SpecialCancel(1)
    sprite('su232_04', 4)
    HitOrBlockJumpCancel(1)
    setInvincible(0)
    sprite('su232_06', 4)
    Recovery()
    Unknown2063()
    sprite('su232_07', 5)
    sprite('su232_08', 5)
    sprite('su232_09', 5)
    sprite('su232_10', 3)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        AirPushbackX(3000)
        AirPushbackY(8000)
        CHHardKnockdown(10)
        HitLow(2)
        AttackP2(82)
        HitOrBlockCancel('NmlAtk4D')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
        if SLOT_94:
            SpecialCancel(0)
    sprite('su235_00', 2)
    sprite('su235_01', 3)
    SetXCollisionFromOrigin(200)
    sprite('su235_02', 3)
    CommonSE('005_swing_grap_2_2')
    sprite('su235_03', 3)
    CreateObject('suef_235', -1)
    RandomCommonVoiceline(2)
    sprite('su235_04', 2)
    sprite('su235_05', 2)
    sprite('su235_06', 2)
    sprite('su235_07', 2)
    sprite('su235_08', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('su235_09', 2)
    CreateObject('suef_235_2', -1)
    sprite('su235_10', 4)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(18000)
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            SpecialCancel(1)
    sprite('su235_11', 4)
    Recovery()
    Unknown2063()
    sprite('su235_12', 4)
    sprite('su235_13', 4)
    sprite('su235_14', 4)
    SetXCollisionFromOrigin(-1)
    sprite('su235_15', 4)
    sprite('su235_16', 3)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1080)
        AttackP1(90)
        AttackP2(79)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        HitLow(2)
        UseSlashHitspark(1)
        HardKnockdown(1)
        SpecialCancel(0)
        SpecialCancelOnHit(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('UseUnLockPowerForce')
        StayAfterMovement(1, 0)
    sprite('su233_00', 3)
    sprite('su233_01', 6)
    sprite('su233_02', 3)
    sprite('su233_03', 3)
    physicsXImpulse(45000)
    SetXCollisionFromOrigin(200)
    CreateObject('suef_233_claw2_3d', -1)
    CommonSE('006_swing_blade_2')
    PrivateSE('suse_00')
    RandomCommonVoiceline(3)
    sprite('su233_04', 3)
    ScreenShake(5000, 5000)
    CreateObject('suef_233_claw_3d', -1)
    XImpulseAcceleration(50)
    sprite('su233_04', 2)
    XImpulseAcceleration(50)
    sprite('su233_05', 2)
    Recovery()
    Unknown2063()
    XImpulseAcceleration(50)
    sprite('su233_06', 2)
    sprite('su233_07', 3)
    sprite('su233_08', 3)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(0)
    sprite('su233_09', 3)
    sprite('su233_10', 3)
    sprite('su233_11', 3)
    sprite('su233_12', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(450)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su250_00', 2)
    sprite('su250_01', 2)
    sprite('su250_02', 3)
    CommonSE('005_swing_grap_2_0')
    RandomCommonVoiceline(0)
    sprite('su250_03', 5)
    CreateObject('suef_250', -1)
    sprite('su250_04', 3)
    Recovery()
    Unknown2063()
    sprite('su250_05', 3)
    sprite('su250_06', 3)
    sprite('su250_07', 3)
    sprite('su250_08', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(740)
        AttackP1(80)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su251_00', 3)
    sprite('su251_01', 2)
    sprite('su251_02', 2)
    CreateObject('suef_251', -1)
    sprite('su251_03', 2)
    CommonSE('006_swing_blade_1')
    RandomCommonVoiceline(1)
    sprite('su251_04', 4)
    CreateObject('suef_251_3d', -1)
    sprite('su251_05', 4)
    Recovery()
    Unknown2063()
    sprite('su251_06', 4)
    sprite('su251_07', 4)
    sprite('su251_08', 4)
    sprite('su251_09', 3)
    sprite('su251_10', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(770)
        AttackP1(80)
        AirHitstunAnimation(10)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
            SLOT_52 = 1

        def upon_EVERY_FRAME():
            if SLOT_52:
                clearUponHandler(EVERY_FRAME)
                HitOverhead(0)
        if SLOT_94:
            ChainCancel(0)
    sprite('su252_00', 3)
    sprite('su252_01', 3)
    CreateObject('suef_252', -1)
    sprite('su252_02', 3)
    CommonSE('005_swing_grap_2_2')
    RandomCommonVoiceline(2)
    sprite('su252_03', 2)
    sprite('su252_04', 2)
    sprite('su252_04', 2)
    AttackOff()
    sprite('su252_05', 3)
    RefreshMultihit()
    AirUntechableTime(30)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            ChainCancel(1)
    sprite('su252_06', 4)
    Recovery()
    Unknown2063()
    sprite('su252_07', 4)
    sprite('su252_08', 4)
    sprite('su252_09', 4)
    sprite('su252_10', 4)
    sprite('su252_11', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        AttackP2(82)
        AirUntechableTime(30)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(-60000)
        HitOverhead(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('UseUnLockPowerForce')
    sprite('su253_00', 2)
    sprite('su253_01', 3)
    ForcedLandingRecovery(9, 1)
    sprite('su253_02', 3)
    CreateObject('suef_253_3d', 103)
    PrivateSE('suse_00')
    sprite('su253_03', 3)
    sprite('su253_04', 3)
    RandomCommonVoiceline(3)
    sprite('su253_05', 3)
    sprite('su253_06', 3)
    sprite('su253_07', 3)
    Recovery()
    Unknown2063()
    sprite('su253_08', 6)
    sprite('su253_09', 6)
    sprite('su253_10', 6)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)

        def upon_33():
            BeginBuffer('NmlAtk4D')
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
    sprite('su210_00', 3)
    PerInertia(60)
    sprite('su210_01', 5)
    RandomCommonVoiceline(1)
    sprite('su210_02', 3)
    SetXCollisionFromOrigin(200)
    sprite('su210_03', 2)
    sprite('su210_04', 2)
    CreateObject('suef_210_Atk', 0)
    PrivateSE('suse_02')
    sprite('su210_04', 4)
    CreateObject('suef_210_shot', 0)
    ScreenShake(10000, 10000)
    sprite('su210_05', 6)
    sprite('su210_06', 6)
    BufferedOrPressedGoto('NmlAtk4D')
    sprite('su210_07', 6)
    sprite('su210_08', 5)
    DisallowGoto2('NmlAtk4D')
    sprite('su210_09', 5)
    SetXCollisionFromOrigin(-1)
    sprite('su210_10', 5)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AirUntechableTime(27)
        AirPushbackX(9000)
        AirPushbackY(18000)
        PushbackX(12000)
        FatalCounter(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtk6D')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        StayAfterMovement(1, 0)
        if SLOT_94:
            ChainCancel(0)
    sprite('su211_00', 3)
    sprite('su211_01', 8)
    SetXCollisionFromOrigin(200)
    sprite('su211_02', 3)
    physicsXImpulse(40000)
    CommonSE('005_swing_grap_2_1')
    sprite('su211_03', 3)
    XImpulseAcceleration(20)
    CreateObject('suef_211', -1)
    RandomCommonVoiceline(1)
    sprite('su211_04', 4)
    ScreenShake(0, 3000)
    CreateObject('suef_211_foot', 0)
    CreateObject('suef_211_foot', 1)
    physicsXImpulse(0)
    CommonSE('213_bound_0')
    sprite('su211_05', 5)
    ChainCancel(0)
    sprite('su211_06', 4)
    sprite('su211_07', 2)
    physicsXImpulse(80000)
    SetXCollisionFromOrigin(-1)
    CommonSE('005_swing_grap_2_1')
    sprite('su211_08', 5)
    AirPushbackY(20000)
    RefreshMultihit()
    ScreenShake(0, 9000)
    CreateObject('suef_211_2', -1)
    CreateObject('suef_211_foot2', 0)
    CreateObject('suef_211_foot2', 1)
    physicsXImpulse(0)
    SetAcceleration(0)
    CommonSE('213_bound_0')

    def upon_OPPONENT_HIT_OR_BLOCK():
        ChainCancel(1)
    sprite('su211_09', 2)
    Recovery()
    Unknown2063()
    sprite('su211_10', 2)
    sprite('su211_11', 2)
    sprite('su211_12', 2)
    sprite('su211_13', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1120)
        AttackP1(90)
        Hitstop(15)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        HardKnockdown(12)
        PushbackX(19800)
        HitOverhead(2)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
        if SLOT_93:
            WhiffCancel('RushAssault')
            WhiffCancelEnable(1)
    sprite('su212_00', 3)
    sprite('su212_01', 3)
    RandomCommonVoiceline(2)
    sprite('su212_02', 3)
    sprite('su212_03', 3)
    sprite('su212_04', 3)
    CreateObject('suef_212', -1)
    sprite('su212_05', 6)
    CommonSE('005_swing_grap_2_2')
    sprite('su212_06', 3)
    physicsXImpulse(35000)
    sprite('su212_07', 4)
    physicsXImpulse(0)
    ScreenShake(0, 7500)
    WhiffCancelEnable(0)
    sprite('su212_08', 5)
    Recovery()
    Unknown2063()
    sprite('su212_09', 4)
    sprite('su212_10', 4)
    sprite('su212_11', 4)
    sprite('su212_12', 3)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1150)
        AttackP1(90)
        AttackP2(82)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(17)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(25)
        Stagger(5)
        Crumple(40)
        Floorslide(15)
        HitOverhead(2)
        StarterRating(2)
        PushbackX(8000)
        SpecialCancel(0)
        SpecialCancelOnHit(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            XImpulseAcceleration(30)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('UseUnLockPowerForce')
        StayAfterMovement(1, 0)
    sprite('su213_00', 5)
    sprite('su213_01', 5)
    RandomCommonVoiceline(3)
    sprite('su213_02', 3)
    CreateObject('suef_213', -1)
    SetXCollisionFromOrigin(200)
    sprite('su213_03', 2)
    sprite('su213_04', 2)
    PrivateSE('suse_00')
    sprite('su213_05', 2)
    CreateObject('suef_213_2', -1)
    physicsXImpulse(10000)
    CommonSE('005_swing_grap_2_2')
    sprite('su213_06', 3)
    ScreenShake(10000, 20000)
    XImpulseAcceleration(200)
    sprite('su213_07', 2)
    sprite('su213_08', 1)
    StartMultihit()
    sprite('su213_08', 1)
    physicsXImpulse(0)
    CreateObject('suef_213_3d', 0)
    GroundedHitstunAnimation(17)
    AirPushbackX(12000)
    FloorslideReset()
    HardKnockdown(1)
    sprite('su213_08', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('su213_09', 4)
    sprite('su213_10', 4)
    sprite('su213_11', 4)
    sprite('su213_12', 4)
    SetXCollisionFromOrigin(-1)
    sprite('su213_13', 4)
    sprite('su213_14', 3)


@State
def NmlAtk4D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('su214_00', 3)
    sprite('su214_01', 3)
    sprite('su214_02', 3)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su214_03', 3)
    sprite('su214_07', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    CreateParticle('suef_214b', 0)
    CreateObject('suef_214ground', 1)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    PrivateSE('suse_03')
    callSubroutine('UseUnLockPowerForce')
    Voiceline('su108')
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateParticle('suef_214', 0)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_11', 3)
    Unknown30017(-25)
    sprite('su214_12', 3)
    sprite('su214_13', 3)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)

        def upon_EVERY_FRAME():
            SLOT_6 = 1

        def upon_STATE_END():
            clearUponHandler(EVERY_FRAME)
            SLOT_6 = 0
    sprite('su300_00', 7)
    sprite('su300_01', 7)
    CreateObject('suef_300', -1)
    CommonSE('022_magiccircle_b')
    sprite('su300_02', 7)
    sprite('su300_03', 40)
    RandomVoiceline('su404', 100, 'su405', 100, '', 0, '', 0)
    sprite('su300_03', 20)
    sprite('su300_04', 7)
    sprite('su300_05', 7)
    sprite('su300_06', 7)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        StayAfterMovement(1, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su203_00', 2)
    sprite('su203_01', 2)
    PrivateSE('suse_00')
    sprite('su203_02', 2)
    CreateObject('suef_203', -1)
    sprite('su203_03', 2)
    sprite('su203_04', 2)
    SetXCollisionFromOrigin(200)
    sprite('su203_05', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('su203_06', 3)
    CreateObject('suef_203_atk', -1)
    SetXCollisionFromOrigin(250)
    sprite('su203_07', 4)
    sprite('su203_08', 4)
    sprite('su203_09', 4)
    sprite('su203_10', 4)
    sprite('su203_11', 4)
    SetXCollisionFromOrigin(-1)
    sprite('su203_12', 4)
    sprite('su203_13', 4)
    sprite('su203_14', 3)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(2500)
        AirPushbackY(-45000)
        PushbackX(8000)
        YImpulseBeforeWallbounce(0)
        Blockstun(24)
        AirUntechableTime(60)
        Stagger(60)
        Crumple(50)
        GroundBounce(1)
        BouncePercentage(30)
        HardKnockdown(10)
        HitBackReturnIgnore(1)
        StarterRating(2)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 10:
                SetActionMark(481)
                GuardCrushHitstun(32)
                AttackP2(60)
                if CheckInput(0x5):
                    sendToLabel(0)
                elif CheckInput(0xe):
                    sendToLabel(0)
            if SLOT_StateDuration >= 20:
                clearUponHandler(OPPONENT_BLOCKS)
                SetActionMark(0)
                GuardCrushHitstun(60)
                AttackP2(100)
                StarterRating(3)
                if CheckInput(0x5):
                    sendToLabel(0)
                elif CheckInput(0xe):
                    sendToLabel(0)
                EnableAfterimage(1)
                AfterimageBlendMode(2)
                AfterimageColor_1(160, 0, 0, 0)
                AfterimageColor_2(96, 0, 0, 0)
                AfterimageMask_1(0, 8, 48, 192)
                AfterimageMask_2(0, 8, 48, 255)
                AfterimageSize_1(1010)
                AfterimageSize_2(900)
            if SLOT_StateDuration >= 50:
                sendToLabel(0)
    sprite('su340_00', 3)
    sprite('su340_01', 1)
    E0EAEffect('GuardCrushWind', 0)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    CreateObject('suef_340_hold', -1)
    Voiceline('su159')
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su340_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('su340_02', 3)
    ParticleColorFromPalette(224, 224, 224)
    sprite('su340_03', 3)
    label(100)
    sprite('su340_01', 3)
    sprite('su340_02', 3)
    sprite('su340_03', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('su340_04', 2)
    clearUponHandler(EVERY_FRAME)
    DespawnEAEffect('suef_340_hold')
    CreateObject('suef_340', -1)
    sprite('su340_05', 2)
    sprite('su340_06', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('su340_07', 3)
    physicsXImpulse(30000)
    sprite('su340_08', 1)
    physicsXImpulse(0)
    CreateParticle('suef_340foot', 0)
    CreateObject('suef_340_rock', 0)
    CreateObject('suef_406_crack', 0)
    ScreenShake(15000, 25000)
    CommonSE('209_down_normal_1')
    sprite('su340_08', 2)
    AttackOff()
    EnableAfterimage(0)
    sprite('su340_09', 3)
    sprite('su340_10', 3)
    sprite('su340_11', 3)
    sprite('su340_12', 3)
    Unknown30017(-25)
    sprite('su340_13', 2)
    sprite('su340_14', 3)
    sprite('su340_15', 3)
    sprite('su340_16', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('su310_00', 3)
    sprite('su310_01', 3)
    sprite('su310_02', 3)
    sprite('su310_03', 3)
    CommonSE('010_swing_sword_1')
    sprite('su310_04', 3)
    Voiceline('su155')
    sprite('su310_05', 3)
    sprite('su310_06', 8)
    sprite('su310_07', 3)
    sprite('su310_08', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(6500)
        AirPushbackY(12000)
        YImpulseBeforeWallbounce(1500)
        AirUntechableTime(60)
        Hitstop(0)
        EnemyHitstopAddition(-1, -1, -1)
        HardKnockdown(10)
        StarterRating(2)
        OppPositionOnHit(1, 150000, 150000)
        SpecialCancel(0)
        EnableRapidCancel(0)
        ShutUp(1)
        DamageEffect(5, '')
        DamageFromStateOnly('ThrowExe')
        StayAfterMovement(1, 0)
    sprite('su310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    AttackOff()
    ThrowLock(1)
    sprite('su311_00', 4)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_01', 20)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    AddCombo(1)
    ScreenShake(5000, 10000)
    CreateParticle('ef_hitmd', 0)

    def RunOnObject_22():
        AltKnockdownEffects(104, 1, 1)
        KnockdownEffects(104, 1, 1)
    sprite('su311_02', 6)
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_03', 6)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_04', 6)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_05', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_06', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_07', 10)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su311_07', 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    RefreshMultihit()
    sprite('su311_08', 6)
    sprite('su311_09', 10)
    Voiceline('su153')
    sprite('su311_10', 4)
    CommonSE('005_swing_grap_2_2')
    sprite('su311_11', 4)
    CreateObject('suef_311', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1500)
    AttackP2(50)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackX(2000)
    AirPushbackY(39000)
    ResetGravity()
    Hitstop(15)
    EnemyHitstopAddition(0, 0, 5)
    HardKnockdownReset()
    OppPositionOnHit(0, 0, 0)
    ShutUp(0)
    DamageEffect(0, '')
    DamageFromStateOnly('')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockJumpCancel(1)
        SpecialCancel(1)
        EnableRapidCancel(1)
        callSubroutine('GetUnLockPower')
    ScreenShake(15000, 30000)
    sprite('su311_12', 4)
    sprite('su311_13', 4)
    sprite('su311_14', 5)
    sprite('su311_15', 5)
    sprite('su311_16', 5)
    sprite('su311_17', 4)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('su310_00', 3)
    sprite('su310_01', 3)
    sprite('su310_02', 3)
    sprite('su310_03', 3)
    CommonSE('010_swing_sword_1')
    sprite('su310_04', 3)
    Voiceline('su155')
    sprite('su310_05', 3)
    sprite('su310_06', 8)
    sprite('su310_07', 3)
    sprite('su310_08', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-6500)
        AirPushbackY(12000)
        YImpulseBeforeWallbounce(1500)
        AirUntechableTime(60)
        Hitstop(0)
        StarterRating(2)
        OppPositionOnHit(1, -110000, 120000)
        SpecialCancel(0)
        EnableRapidCancel(0)
        ShutUp(1)
        DamageEffect(5, '')
        DamageFromStateOnly('BackThrowExe')
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
    sprite('su310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    AttackOff()
    ThrowLock(1)
    sprite('su313_00', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su313_01', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su313_02', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su313_03', 15)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su313_04', 17)
    RefreshMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su313_05', 6)
    sprite('su313_06', 3)
    Voiceline('su153')
    ScreenShake(15000, 0)
    RefreshMultihit()
    CreateObject('suef_313', 0)
    CreateObject('suef_313_smoke', -1)
    PrivateSE('suse_02')
    AttackLevel_(5)
    Damage(1500)
    AttackP2(50)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(120000)
    AirPushbackY(8000)
    FlipOnHit(1)
    Wallbounce(1)
    WallbounceReboundTime(20)
    AirHitstunAfterWallbounce(60)
    Wallstick(1)
    WallstickDuration(40)
    Hitstop(13)
    OppPositionOnHit(0, 0, 0)
    ShutUp(0)
    DamageEffect(0, '')
    DamageFromStateOnly('')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk4D')
        SpecialCancel(1)
        EnableRapidCancel(1)
        callSubroutine('GetUnLockPower')
    sprite('su313_07', 3)
    sprite('su313_08', 3)
    sprite('su313_09', 3)
    sprite('su313_07', 3)
    sprite('su313_08', 3)
    sprite('su313_10', 2)
    sprite('su313_11', 2)
    sprite('su313_12', 2)
    sprite('su313_13', 2)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('su320_00', 3)
    sprite('su320_01', 3)
    sprite('su320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('su320_03', 3)
    CommonSE('010_swing_sword_1')
    sprite('su320_04', 3)
    Voiceline('su155')
    sprite('su320_05', 3)
    sprite('su320_06', 8)
    sprite('su320_07', 3)
    sprite('su320_08', 3)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        Hitstop(15)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(40000)
        AirUntechableTime(100)
        UseSlashHitspark(1)
        StarterRating(2)
        SetZLine(0, 50)
        EndMomentum(1)
        ForcedLandingRecovery(0, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            callSubroutine('GetUnLockPower')
    sprite('su320_02', 5)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    AttackOff()
    sprite('su321_00', 5)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    YSpeed(8000)
    setGravity(400)
    sprite('su321_01', 5)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su321_02', 5)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('su321_03', 15)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('su321_04', 4)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('su154')
    sprite('su321_05', 3)
    CreateObject('suef_321', -1)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    RefreshMultihit()
    CommonSE('006_swing_blade_2')
    sprite('su321_06', 3)
    sprite('su321_07', 3)
    sprite('su321_08', 3)
    sprite('su321_09', 3)
    sprite('su321_10', 3)


@Subroutine
def CheckAssaultLv():
    SLOT_51 = 0
    SLOT_4 and 1
    if SLOT_0 == 1:
        SLOT_51 = 1
    SLOT_4 and 2
    if SLOT_0 == 2:
        SLOT_51 = 2
    SLOT_4 and 4
    if SLOT_0 == 4:
        SLOT_51 = 3
    if SLOT_OverdriveTimer:
        SLOT_51 = 3


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckAssaultLv')
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AttackP2(79)
        Hitstun(23)
        AirUntechableTime(30)
        AirPushbackX(24000)
        AirPushbackY(18000)
        AttackDirection(0)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 1
            sendToLabel(1)
        if SLOT_51 == 2:
            AirPushbackY(22000)
            GotoState('Assault_Lv2')
        if SLOT_51 == 3:
            SingleProration(1)
            AirPushbackY(16000)
            GotoState('Assault_Lv3')

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT_OR_BLOCK)
                clearUponHandler(OPPONENT_HIT)
                SLOT_7 = 1
                sendToLabel(10)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su400_00', 3)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    DespawnEAEffect('suef_aura')
    Voiceline('su200')
    sprite('su400_01', 3)
    sprite('su400_02', 3)
    sprite('su400_03', 3)
    AltKnockdownEffects(100, 1, 1)
    CreateObject('suef_400_particle2', -1)
    sprite('su400_04', 2)
    physicsXImpulse(50000)
    SetXCollisionFromOrigin(250)
    CommonSE('000_airdash_1')
    CreateObject('suef_400_aura3', 0)
    sprite('su400_05', 3)
    DashEffects(100, 1, 0)
    CreateObject('suef_400', -1)
    sprite('su400_06', 2)
    sprite('su400_06', 1)
    if SLOT_51 == 1:
        sendToLabel(1)
    sprite('su400_05', 3)
    DashEffects(100, 1, 0)
    sprite('su400_06', 3)
    label(1)
    sprite('su400_07', 4)
    DespawnEAEffect('suef_400')
    CreateObject('suef_400_aura2', 0)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(OPPONENT_HIT)
    DashEffects(100, 1, 0)
    Recovery()
    sprite('su400_21', 3)
    DespawnEAEffect('suef_400_particle2')
    XImpulseAcceleration(60)
    SetXCollisionFromOrigin(-1)
    DashEffects(100, 1, 0)
    sprite('su032_11', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 1)
    Unknown30017(-25)
    sprite('su032_12', 3)
    EndMomentum(1)
    SkidEffects(100, 1, 1)
    sprite('su032_13', 2)
    sprite('su032_14', 2)
    sprite('su032_15', 2)
    ExitState()
    label(10)
    sprite('su400_07', 2)
    DespawnEAEffect('suef_400')
    CreateObject('suef_400_aura2', 0)
    DespawnEAEffect('suef_400_particle2')
    XImpulseAcceleration(80)
    DashEffects(100, 1, 0)
    uponSendToLabel(LANDING, 11)
    sprite('su400_08', 2)
    DespawnEAEffect('suef_400_aura2')
    SetXCollisionFromOrigin(-1)
    DashEffects(100, 1, 0)
    sprite('su400_09', 2)
    XImpulseAcceleration(80)
    sprite('su400_10', 2)
    sprite('su400_11', 2)
    XImpulseAcceleration(60)
    CommonSE('005_swing_grap_2_2')
    sprite('su400_12', 4)
    physicsYImpulse(8000)
    EndYPhysicsImpulse()
    Voiceline('su201')
    RefreshMultihit()
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(48)
    ResetPushback()
    AirPushbackY(32000)
    UseSlashHitspark(1)
    CreateObject('suef_400_claw', -1)
    CreateObject('suef_400_claw2', -1)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SLOT_7 = 1
    sprite('su400_13', 4)
    XImpulseAcceleration(60)
    Recovery()
    sprite('su400_14', 32767)
    XImpulseAcceleration(60)
    label(11)
    sprite('su400_15', 3)
    EndMomentum(1)
    AltKnockdownEffects(100, 1, 1)
    Unknown30017(-17)
    sprite('su400_16', 3)
    sprite('su400_17', 3)
    sprite('su400_18', 3)
    sprite('su400_19', 2)
    sprite('su400_20', 2)


@Subroutine
def CheckAntiAirLv():
    SLOT_51 = 0
    SLOT_4 and 8
    if SLOT_0 == 8:
        SLOT_51 = 1


@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckAntiAirLv')
        NoAttackDuringAction(1)
        SLOT_7 = 0

        def upon_32():
            SLOT_7 = 2
    sprite('su401_00', 2)
    setInvincible(1)
    CreateObject('suef_401handaura', -1)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    Voiceline('su202')
    sprite('su401_01', 2)
    sprite('su401_02', 2)
    sprite('su401_03', 4)
    sprite('su401_04', 1)
    sprite('su401_05', 3)
    ScreenShake(10000, 25000)
    CreateObject('suef_401', -1)
    CommonSE('016_explode_1')
    CommonSE('209_down_normal_1')
    sprite('su401_06', 3)
    sprite('su401_07', 3)
    sprite('su401_08', 3)
    setInvincible(0)
    sprite('su401_06', 3)
    sprite('su401_07', 3)
    sprite('su401_08', 3)
    sprite('su401_06', 3)
    sprite('su401_07', 3)
    sprite('su401_08', 3)
    sprite('su401_09', 3)
    sprite('su401_10', 3)
    sprite('su401_11', 3)
    SetXCollisionFromOrigin(-1)
    sprite('su401_12', 4)
    sprite('su401_13', 4)
    Unknown30017(-25)
    sprite('su401_14', 4)
    sprite('su401_15', 4)
    sprite('su401_16', 4)


@Subroutine
def CheckLongAssaultLv():
    SLOT_51 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SLOT_51 = 1


@State
def LongAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckLongAssaultLv')
        AttackLevel_(5)
        Damage(1650)
        AttackP1(80)
        Hitstop(15)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(45)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackDirection(0)
        CHAirPushbackX(60000)
        CHAirPushbackY(30000)
        CHWallbounce(1)
        NonCornerWallbounce(0)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 8
        StayAfterMovement(1, 0)
    sprite('su402_00', 3)
    CreateObject('suef_402', -1)
    sprite('su402_01', 3)
    sprite('su402_02', 3)
    sprite('su402_03', 2)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    Voiceline('su203')
    sprite('su402_04', 2)
    SetXCollisionFromOrigin(200)
    PrivateSE('suse_05')
    PrivateSE('suse_02')
    CommonSE('006_swing_blade_2')
    sprite('su402_05', 2)
    sprite('su402_06', 3)
    KnockdownEffects(100, 1, 0)
    AttackOff()
    sprite('su402_07', 3)
    RefreshMultihit()
    sprite('su402_08', 3)
    Recovery()
    sprite('su402_09', 3)
    sprite('su402_10', 3)
    sprite('su402_11', 4)
    Unknown30017(-25)
    sprite('su402_12', 4)
    SetXCollisionFromOrigin(-1)
    sprite('su402_13', 4)
    sprite('su402_14', 3)


@Subroutine
def CheckAssaultThrowLv():
    SLOT_51 = 0
    SLOT_4 and 32
    if SLOT_0 == 32:
        SLOT_51 = 1


@State
def AssaultThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AssaultThrowExe', 2, 0, 0)
        callSubroutine('CheckAssaultThrowLv')
        DistanceCheck(-1, -1, 130000, 0)
        RangeCheck(70000)
        ThrowTechWindow(-1)

        def upon_EVERY_FRAME():
            SLOT_19 < 300000
            if not SLOT_0 and not SLOT_52:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(1)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 7
        StayAfterMovement(1, 0)
    sprite('su403_00', 2)
    Voiceline('su204')
    sprite('su403_01', 3)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    EnableAfterimage(1)
    AfterimageInterval(1)
    AfterimageCount(7)
    AfterimageColor_1(128, 0, 0, 0)
    AfterimageColor_2(0, 0, 0, 0)
    sprite('su403_02', 3)
    sprite('su403_03', 3)
    sprite('su403_01', 3)
    sprite('su403_02', 3)
    sprite('su403_03', 3)
    sprite('su403_01', 3)
    sprite('su403_02', 3)
    sprite('su403_04', 3)
    physicsXImpulse(50000)
    SetXCollisionFromOrigin(200)
    CommonSE('000_airdash_2')
    sprite('su403_05', 4)
    CreateParticle('suef_403dash', -1)
    sprite('su403_06', 4)
    SLOT_52 = 1
    sprite('su403_05', 4)
    sprite('su403_06', 4)
    CommonSE('010_swing_sword_1')
    label(1)
    sprite('su403_29', 4)
    clearUponHandler(EVERY_FRAME)
    XImpulseAcceleration(60)
    Voiceline('su155')
    sprite('su403_30', 4)
    XImpulseAcceleration(60)
    sprite('su233_05', 4)
    XImpulseAcceleration(60)
    CrouchState(1)
    Unknown30017(-12)
    KnockdownEffects(100, 1, 1)
    sprite('su233_06', 4)
    XImpulseAcceleration(60)
    EnableAfterimage(0)
    sprite('su233_07', 4)
    XImpulseAcceleration(60)
    sprite('su233_08', 4)
    XImpulseAcceleration(60)
    sprite('su233_09', 4)
    XImpulseAcceleration(0)
    sprite('su233_10', 3)
    sprite('su233_11', 3)
    sprite('su233_12', 3)


@State
def AssaultThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        DamageFromStateOnly('AssaultThrowExe')
        AttackLevel_(4)
        Damage(1800)
        MinimumDamage(30)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        AirPushbackX(50000)
        AirPushbackY(40000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        AirHitstunAfterWallbounce(30)
        Wallstick(1)
        WallstickDuration(30)
        HardKnockdown(15)
        Unknown11102(1)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        CHStateIfCHStart(3)
        EnableRapidCancel(0)
        callSubroutine('EmissionStart')
        Unknown30016(255)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_XDistanceFromFowardCorner <= 250000:
                    clearUponHandler(EVERY_FRAME)
                    SetActionMark(0)
                    sendToLabel(2)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 7
        CameraControlEnable(1)
        StayAfterMovement(1, 0)
    sprite('su403_06', 1)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    AttackOff()
    SetXCollisionFromOrigin(400)
    physicsXImpulse(20000)
    CreateObject('suef_403_aura', 103)
    EnableAfterimage(1)
    AfterimageInterval(0)
    AfterimageCount(10)
    AfterimageColor_1(128, 0, 0, 0)
    AfterimageColor_2(0, 0, 0, 0)
    CreateObject('suef_403_camera', 100)
    sprite('su403_07', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    TriggerUponForState('suef_403_camera', 32)
    sprite('su403_08', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(50000)
    SetActionMark(20)
    label(1)
    sprite('su403_09', 2)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('015_blaze_0')
    sprite('su403_10', 2)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    loopRest()
    AddActionMark(-1)
    if SLOT_2:
        conditionalSendToLabel(1)
    label(2)
    sprite('su403_10', 2)
    CameraControlEnable(0)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su403_11', 2)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(0)
    SetAcceleration(0)
    DespawnEAEffect('suef_403_aura')
    sprite('su403_12', 12)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    WallbounceEffects(0, 0, 0)
    SetXCollisionFromOrigin(550)
    RefreshMultihit()
    ScreenShake(10000, 5000)
    Voiceline('su205')
    sprite('su403_13', 4)
    CreateObject('suef_403_hand', -1)
    sprite('su403_14', 4)
    sprite('su403_15', 5)
    SetXCollisionFromOrigin(650)
    DespawnEAEffect('suef_403_hand')
    CreateObject('suef_403_smash', -1)
    sprite('su403_16', 4)
    CreateObject('suef_403_smoke', -1)
    WallbounceEffects(0, 0, 0)
    RefreshMultihit()
    AttackP2(60)
    DamageFromStateOnly('')
    DefeatOpponentBehavior(0)
    BurstInvincibility(0)

    def upon_OPPONENT_HIT():
        EnableRapidCancel(1)
    ScreenShake(20000, 10000)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('su403_17', 4)
    sprite('su403_18', 4)
    sprite('su403_19', 4)
    sprite('su403_20', 4)
    EnableAfterimage(0)
    sprite('su403_21', 4)
    sprite('su403_22', 4)
    sprite('su403_23', 4)
    sprite('su403_24', 4)
    sprite('su403_25', 6)
    Unknown30017(-12)
    sprite('su403_26', 6)
    sprite('su403_27', 6)
    sprite('su403_28', 6)


@Subroutine
def CheckRushAssaultLv():
    SLOT_51 = 0
    SLOT_4 and 64
    if SLOT_0 == 64:
        SLOT_51 = 1


@State
def RushAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckRushAssaultLv')
        AttackLevel_(3)
        Damage(570)
        ChipPercentage(15)
        Hitstop(3)
        EnemyHitstopAddition(-1, -1, 2)
        AirUntechableTime(35)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(12000)
        PushbackX(30400)
        Crumple(22)
        CHStagger(47)
        CHCrumple(42)
        NonCornerWallbounce(1)
        WallbounceReboundTime(0)
        Unknown11102(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(2)
        MoveAttributes(0, 0, 0, 1, 0)
        HitsparkSize(600)

        def upon_EVERY_FRAME():
            if SLOT_54:
                if CheckInput(0x14):
                    SetActionMark(1)
                elif CheckInput(INPUT_RELEASE_C):
                    SetActionMark(1)
                SLOT_52 = SLOT_52 + 1
                if SLOT_52 >= 3:
                    HitBackReturnIgnore(0)
                    RefreshMultihit()
                else:
                    HitBackReturnIgnore(1)
                if SLOT_53 >= 12:
                    sendToLabel(2)
            if SLOT_55:
                if not SLOT_94:
                    if CheckInput(INPUT_HOLD_B):
                        if CheckInput(INPUT_HOLD_C):
                            if CheckInput(INPUT_HOLD_D):
                                sendToLabel(2)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_52 = 0
            SLOT_53 = SLOT_53 + 1
            SLOT_7 = 6
        StayAfterMovement(1, 0)
    sprite('su404_00', 1)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    SmartVoiceline('su206')
    sprite('su404_01', 2)
    SetXCollisionFromOrigin(200)
    sprite('su404_02', 1)
    sprite('su404_03', 1)
    SLOT_54 = 1
    sprite('su404_04', 3)
    CreateObject('suef_404', 0)
    SLOT_55 = 1
    ScreenShake(1500, 1500)
    sprite('su404_05', 3)
    sprite('su404_06', 3)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2)
    label(1)
    sprite('su404_04', 3)
    SetActionMark(0)
    ScreenShake(1500, 1500)
    sprite('su404_05', 3)
    sprite('su404_06', 3)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2)
    SLOT_55 = SLOT_55 + 1
    if not SLOT_55 >= 10:
        notConditionalSendToLabel(1)
    label(2)
    sprite('su404_07', 3)
    clearUponHandler(EVERY_FRAME)
    DespawnEAEffect('suef_404')
    HitBackReturnIgnore(0)
    Unknown30017(-12)
    Recovery()
    sprite('su404_08', 3)
    sprite('su404_09', 3)
    sprite('su404_10', 2)
    sprite('su404_11', 2)
    SetXCollisionFromOrigin(-1)
    sprite('su404_12', 2)
    sprite('su404_13', 2)
    sprite('su404_14', 3)


@Subroutine
def CheckShotLv():
    SLOT_51 = 0
    SLOT_4 and 128
    if SLOT_0 == 128:
        SLOT_51 = 1
    SLOT_4 and 256
    if SLOT_0 == 256:
        SLOT_51 = 2
        SLOT_53 = 1
    SLOT_4 and 512
    if SLOT_0 == 512:
        SLOT_51 = 3
        SLOT_54 = 1
    if SLOT_OverdriveTimer:
        SLOT_51 = 3
        SLOT_54 = 1


@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckShotLv')
        NoAttackDuringAction(1)
        callSubroutine('EmissionStart')
        Unknown30017(25)
        SLOT_7 = 0

        def upon_32():
            SLOT_7 = 3
    if SLOT_54:
        conditionalSendToLabel(3)
    if SLOT_53:
        conditionalSendToLabel(2)
    sprite('su405_00', 2)
    sprite('su405_01', 2)
    sprite('su405_02', 3)
    ScreenShake(2000, 2000)
    sprite('su405_03', 3)
    CreateObject('suef_405', 0)
    CreateObject('suef_405_crack', 0)
    sprite('su405_06', 3)
    sprite('su405_07', 3)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_405')
    CreateObject('suef_405kick', -1)
    ObjectUpon(STATE_END, 33)
    PrivateSE('suse_04')
    CommonSE('209_down_normal_0')
    Voiceline('su207')
    sprite('su405_08', 3)
    sprite('su405_09', 3)
    sprite('su405_10', 3)
    sprite('su405_11', 3)
    sprite('su405_12', 3)
    sprite('su405_13', 4)
    Recovery()
    Unknown30017(-25)
    sprite('su405_14', 4)
    sprite('su405_15', 2)
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('su405_00', 2)
    sprite('su405_01', 3)
    sprite('su405_02', 3)
    ScreenShake(2000, 2000)
    CommonSE('019_quake_1')
    sprite('su405_03', 3)
    CreateObject('suef_405', 0)
    CreateObject('suef_405_crack', 0)
    sprite('su405_04', 3)
    sprite('su405_05', 3)
    ScreenShake(2000, 2000)
    sprite('su405_03', 3)
    sprite('su405_06', 3)
    sprite('su405_07', 3)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_405')
    CreateObject('suef_405kick', -1)
    ObjectUpon(STATE_END, 34)
    PrivateSE('suse_04')
    CommonSE('209_down_normal_1')
    Voiceline('su207')
    sprite('su405_08', 3)
    sprite('su405_09', 3)
    sprite('su405_10', 3)
    sprite('su405_11', 3)
    sprite('su405_12', 3)
    sprite('su405_13', 4)
    Recovery()
    Unknown30017(-25)
    sprite('su405_14', 4)
    sprite('su405_15', 2)
    loopRest()
    gotoLabel(9)
    label(3)
    sprite('su405_00', 2)
    sprite('su405_01', 3)
    sprite('su405_02', 3)
    ScreenShake(2000, 2000)
    CommonSE('019_quake_1')
    sprite('su405_03', 3)
    CreateObject('suef_405', 0)
    CreateObject('suef_405_crack', 0)
    sprite('su405_04', 3)
    sprite('su405_05', 3)
    ScreenShake(2000, 2000)
    sprite('su405_03', 3)
    sprite('su405_06', 3)
    sprite('su405_07', 3)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_405')
    CreateObject('suef_405kick', -1)
    ObjectUpon(STATE_END, 35)
    PrivateSE('suse_04')
    CommonSE('209_down_normal_1')
    Voiceline('su207')
    sprite('su405_08', 3)
    sprite('su405_09', 3)
    sprite('su405_10', 3)
    sprite('su405_11', 3)
    sprite('su405_12', 3)
    sprite('su405_13', 4)
    Recovery()
    Unknown30017(-25)
    sprite('su405_14', 4)
    sprite('su405_15', 2)
    label(9)
    sprite('su405_15', 1)


@Subroutine
def CheckMidAssaultLv():
    SLOT_51 = 0
    SLOT_4 and 1024
    if SLOT_0 == 1024:
        SLOT_51 = 1
    SLOT_4 and 2048
    if SLOT_0 == 2048:
        SLOT_51 = 2
    if SLOT_OverdriveTimer:
        SLOT_51 = 2


@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckMidAssaultLv')
        AttackLevel_(3)
        Damage(840)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(45)
        AirPushbackY(-55000)
        HitOverhead(2)
        Hitstop(8)
        StarterRating(2)
        BouncePercentage(50)
        GroundBounce(1)
        MoveAttributes(1, 0, 0, 0, 0)
        if SLOT_51 == 2:
            GotoState('MidAssault_Lv2')

        def upon_LANDING():
            sendToLabel(2)
            EndMomentum(1)
            KnockdownEffects(100, 1, 1)
            DespawnEAEffect('suef_406_roll_3d')
            RefreshMultihit()
            Hitstop(11)
            HitOverhead(0)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 4

        def upon_32():
            SLOT_7 = 4
        if SLOT_137:
            DamageMultiplier(80)
        StayAfterMovement(1, 0)
    sprite('su023_00', 2)
    CommonSE('002_highjump_1')
    Voiceline('su208')
    sprite('su023_01', 2)
    sprite('su406_00', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    EndMomentum(1)
    physicsXImpulse(30000)
    physicsYImpulse(20000)
    setGravity(2000)
    callSubroutine('EmissionStart')
    Unknown30017(12)
    sprite('su406_01', 3)
    sprite('su406_02', 3)
    XImpulseAcceleration(80)
    sprite('su406_03', 3)
    XImpulseAcceleration(80)
    sprite('su406_04', 3)
    XImpulseAcceleration(80)
    sprite('su406_05', 3)
    XImpulseAcceleration(0)
    loopRest()
    CreateObject('suef_406_roll_3d', 103)
    PrivateSE('suse_02')
    label(1)
    sprite('su406_06', 2)
    sprite('su406_07', 2)
    sprite('su406_08', 2)
    sprite('su406_09', 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('su406_10', 3)
    if SLOT_51 == 2:
        CreateObject('suef_406_OD', 0)
        CommonSE('016_explode_2')
    else:
        CreateObject('suef_406', 0)
    sprite('su406_11', 4)
    setInvincible(0)
    Recovery()
    sprite('su406_12', 4)
    sprite('su406_13', 4)
    sprite('su406_14', 3)
    Unknown30017(-25)
    sprite('su406_15', 3)
    sprite('su406_16', 3)
    sprite('su406_17', 3)


@State
def AirMidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('CheckMidAssaultLv')
        AttackLevel_(3)
        Damage(660)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(11)
        AirUntechableTime(45)
        HardKnockdown(1)
        AirPushbackY(-44000)
        Hitstop(2)
        EnemyHitstopAddition(0, -1, 2)
        MoveAttributes(1, 0, 0, 0, 0)
        AttackOff()
        clearUponHandler(LANDING)

        def upon_LANDING():
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2)
            EndMomentum(1)
            KnockdownEffects(100, 1, 1)
            DespawnEAEffect('suef_406_roll_3d')
            RefreshMultihit()
            GroundedHitstunAnimation(11)
            Hitstop(11)

        def upon_EVERY_FRAME():
            if SLOT_2:
                SLOT_52 = SLOT_52 + -1
                if not SLOT_52:
                    RefreshMultihit()
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_52 = 5
            SLOT_7 = 4

        def upon_32():
            SLOT_7 = 4
        if SLOT_137:
            DamageMultiplier(80)
        StayAfterMovement(1, 0)
    sprite('su406_02', 2)
    PerInertia(0)
    XSpeed(15000)
    YAccel(20)
    YSpeed(25000)
    setGravity(3000)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su406_03', 2)
    XImpulseAcceleration(80)
    sprite('su406_04', 2)
    XImpulseAcceleration(80)
    sprite('su406_05', 2)
    XImpulseAcceleration(80)
    sprite('su406_06ex01', 2)
    XImpulseAcceleration(80)
    CreateObject('suef_406_roll_3d', 103)
    PrivateSE('suse_02')
    CommonSE('006_swing_blade_2')
    Voiceline('su208')
    sprite('su406_07ex01', 2)
    sprite('su406_08ex01', 2)
    SetActionMark(1)
    RefreshMultihit()
    CommonSE('006_swing_blade_2')
    sprite('su406_09ex01', 2)
    label(1)
    sprite('su406_06ex01', 2)
    XImpulseAcceleration(80)
    CommonSE('006_swing_blade_2')
    sprite('su406_07ex01', 2)
    sprite('su406_08ex01', 2)
    sprite('su406_09ex01', 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('su406_10', 3)
    if SLOT_51 == 2:
        CreateObject('suef_406_OD', 0)
        ObjectUpon(STATE_END, 32)
        CommonSE('016_explode_2')
    else:
        CreateObject('suef_406', 0)
    sprite('su406_11', 4)
    Recovery()
    sprite('su406_12', 4)
    sprite('su406_13', 4)
    sprite('su406_14', 3)
    Unknown30017(-25)
    sprite('su406_15', 3)
    sprite('su406_16', 3)
    sprite('su406_17', 3)


@Subroutine
def CheckLowAssaultLv():
    SLOT_51 = 0
    SLOT_4 and 4096
    if SLOT_0 == 4096:
        SLOT_51 = 1


@State
def LowAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckLowAssaultLv')
        AttackLevel_(4)
        Damage(390)
        AttackP1(80)
        AttackP2(94)
        AirPushbackY(-4000)
        AirUntechableTime(36)
        Hitstun(24)
        Hitstop(4)
        HardKnockdown(1)
        HitLow(2)
        StarterRating(2)
        MoveAttributes(0, 0, 1, 0, 0)

        def upon_EVERY_FRAME():
            SLOT_19 < 200000
            if not SLOT_0 and not SLOT_2:
                sendToLabel(1)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(EVERY_FRAME)
            SLOT_7 = 5
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su407_00', 3)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su407_01', 4)
    sprite('su407_02', 4)
    sprite('su407_03', 3)
    physicsXImpulse(3000)
    SetXCollisionFromOrigin(250)
    sprite('su407_03', 3)
    XImpulseAcceleration(200)
    CommonSE('000_airdash_2')
    sprite('su407_04', 2)
    XImpulseAcceleration(1000)
    CreateObject('suef_407_jiware', -1)
    ScreenShake(13000, 13000)
    RefreshMultihit()
    CommonSE('209_down_normal_1')
    sprite('su407_05', 2)
    SetActionMark(1)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    loopRest()
    gotoLabel(1)
    sprite('su407_03', 3)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    Unknown30017(-25)
    DespawnEAEffect('suef_407_jiware')
    Recovery()
    XImpulseAcceleration(50)
    sprite('su407_02', 3)
    XImpulseAcceleration(50)
    sprite('su407_01', 3)
    XImpulseAcceleration(50)
    sprite('su407_00', 3)
    XImpulseAcceleration(0)
    ExitState()
    label(1)
    sprite('su407_06', 2)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    SetAcceleration(-5000)
    sprite('su407_07', 2)
    sprite('su407_08', 2)
    sprite('su407_09', 3)
    SetXCollisionFromOrigin(-1)
    sprite('su407_10', 3)
    DespawnEAEffect('suef_407_jiware')
    SetAcceleration(0)
    sprite('su407_11', 3)
    sprite('su407_12', 3)
    Voiceline('su209')
    sprite('su407_13', 4)
    KnockdownEffects(100, 1, 1)
    CreateObject('suef_407_kick', -1)
    XImpulseAcceleration(0)
    RefreshMultihit()
    Damage(780)
    Hitstop(15)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(8000)
    AirPushbackY(50000)
    HitLow(0)
    HardKnockdown(0)
    MoveAttributes(0, 1, 0, 0, 0)

    def upon_OPPONENT_HIT_OR_BLOCK():
        HitJumpCancel(1)
        SLOT_7 = 5
    uponSendToLabel(LANDING, 2)
    sprite('su407_14', 4)
    Recovery()
    physicsYImpulse(12000)
    setGravity(1500)
    sprite('su407_15', 4)
    sprite('su407_16', 4)
    sprite('su407_17', 4)
    sprite('su407_18', 32767)
    label(2)
    sprite('su407_19', 3)
    EndMomentum(1)
    HitJumpCancel(0)
    Unknown30017(-25)
    LandingEffects(100, 1, 1)
    sprite('su407_20', 2)
    sprite('su407_21', 2)
    sprite('su407_22', 2)
    sprite('su407_23', 2)


@State
def UltimateLongAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(2800)
        AttackP1(70)
        MinimumDamage(40)
        AirUntechableTime(80)
        Hitstop(0)
        EnemyHitstopAddition(20, 20, 28)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(15000)
        WallbounceReboundTime(0)
        Floorslide(20)
        StarterRating(0)
        UseSlashHitspark(1)
        AttackDirection(0)
        AirPushbackX(150000)
        CHHardKnockdown(10)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 8
        StayAfterMovement(1, 0)
    sprite('su430_00', 3)
    setInvincible(1)
    CreateObject('suef_430_sword', -1)
    sprite('su430_01', 3)
    CameraControlEnable(1)
    CameraPosition(900)
    callSubroutine('EmissionStart')
    Unknown30017(12)
    sprite('su430_02', 3)
    DistortionSettings(75, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    Voiceline('su250')
    sprite('su430_03', 3)
    sprite('su430_04', 3)
    ParticleColorFromPalette(128, 128, 128)
    CallCustomizableParticle('suef_430sword', 103)
    sprite('su430_05', 3)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    CameraControlEnable(0)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_08', 6)
    TriggerUponForState('suef_430_sword', 32)
    sprite('su430_09', 6)
    sprite('su430_10', 6)
    sprite('su430_11', 6)
    sprite('su430_12', 6)
    sprite('su430_13', 6)
    sprite('su430_14', 1)
    sprite('su430_15', 1)
    Voiceline('su251')
    sprite('su430_16', 6)
    CreateObject('suef_430_slash', -1)
    PrivateSE('suse_02')
    PrivateSE('suse_06')
    PrivateSE('suse_06')

    def upon_OPPONENT_HIT():
        CommonSE('025_cleanhit_slash')
    sprite('su430_17', 3)
    setInvincible(0)
    sprite('su430_18', 3)
    sprite('su430_19', 3)
    sprite('su430_20', 3)
    sprite('su430_17', 3)
    sprite('su430_18', 3)
    sprite('su430_19', 3)
    sprite('su430_20', 3)
    sprite('su430_17', 3)
    sprite('su430_21', 5)
    sprite('su430_22', 5)
    sprite('su402_11ex01', 5)
    SetXCollisionFromOrigin(-1)
    Unknown30017(-25)
    sprite('su402_12ex01', 5)
    sprite('su402_13ex01', 4)
    sprite('su402_14ex01', 4)


@State
def UltimateLongAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(3500)
        AttackP1(70)
        MinimumDamage(40)
        AirUntechableTime(80)
        Hitstop(0)
        EnemyHitstopAddition(20, 20, 28)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(15000)
        WallbounceReboundTime(0)
        Floorslide(20)
        UseSlashHitspark(1)
        StarterRating(0)
        AttackType(4)
        AttackDirection(0)
        AirPushbackX(150000)
        CHHardKnockdown(10)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 8
        StayAfterMovement(1, 0)
    sprite('su430_00', 3)
    setInvincible(1)
    CreateObject('suef_430_sword', -1)
    sprite('su430_01', 3)
    CameraControlEnable(1)
    CameraPosition(900)
    callSubroutine('EmissionStart')
    Unknown30017(12)
    sprite('su430_02', 3)
    DistortionSettings(75, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    Voiceline('su250')
    sprite('su430_03', 3)
    sprite('su430_04', 3)
    sprite('su430_05', 3)
    ScreenShake(4000, 4000)
    CommonSE('019_quake_1')
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    ScreenShake(4000, 4000)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    ScreenShake(4000, 4000)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    ScreenShake(4000, 4000)
    CommonSE('019_quake_1')
    CameraControlEnable(0)
    sprite('su430_06', 3)
    ScreenShake(4000, 4000)
    CommonSE('019_quake_1')
    sprite('su430_07', 3)
    ScreenShake(4000, 4000)
    sprite('su430_08', 6)
    TriggerUponForState('suef_430_sword', 32)
    ScreenShake(6000, 6000)
    CommonSE('019_quake_1')
    sprite('su430_09', 6)
    ScreenShake(6000, 6000)
    sprite('su430_10', 6)
    ScreenShake(8000, 8000)
    sprite('su430_11', 6)
    ScreenShake(8000, 8000)
    sprite('su430_12', 6)
    ScreenShake(10000, 10000)
    sprite('su430_13', 6)
    ScreenShake(10000, 10000)
    CommonSE('019_quake_1')
    sprite('su430_14', 1)
    sprite('su430_15', 1)
    Voiceline('su251')
    sprite('su430_16', 6)
    CreateObject('suef_430_slash', -1)
    PrivateSE('suse_02')
    PrivateSE('suse_06')
    PrivateSE('suse_06')

    def upon_OPPONENT_HIT():
        CommonSE('025_cleanhit_slash')
    sprite('su430_17', 3)
    setInvincible(0)
    sprite('su430_18', 3)
    sprite('su430_19', 3)
    sprite('su430_20', 3)
    sprite('su430_17', 3)
    sprite('su430_18', 3)
    sprite('su430_19', 3)
    sprite('su430_20', 3)
    sprite('su430_17', 3)
    sprite('su430_21', 5)
    TriggerUponForState('suef_430_sword', 33)
    sprite('su430_22', 5)
    sprite('su402_11ex01', 5)
    SetXCollisionFromOrigin(-1)
    Unknown30017(-25)
    sprite('su402_12ex01', 5)
    sprite('su402_13ex01', 4)
    sprite('su402_14ex01', 4)


@State
def UltimateRushAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        MinimumDamage(10)
        AttackP2(60)
        PushbackX(30400)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        OppPositionOnHit(1, 200000, 0)
        EnemyHitstopAddition(0, 0, 0)
        Crumple(100)
        Stagger(120)
        Hitstop(7)
        AttackDirection(0)
        SLOT_65 = 0
        SLOT_62 = 0
        SLOT_64 = SLOT_4
        callSubroutine('UltimateRush_Program')
        if SLOT_63 == 2:
            GroundedHitstunAnimation(11)
            AirHitstunAnimation(11)
            AirPushbackY(60000)
            AirPushbackX(-1000)
            AirUntechableTime(100)
        if SLOT_63 == 3:
            PushbackX(0)
        if SLOT_63 == 6:
            PushbackX(0)
        callSubroutine('UltimateRush_Next')
        StayAfterMovement(1, 0)

        def upon_EVERY_FRAME():
            if not SLOT_21:
                CameraControlEnable(0)

        def upon_OPPONENT_HIT():
            CameraControlEnable(1)
            SetActionMark(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su431_00', 4)
    setInvincible(1)
    sprite('su431_01', 6)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('su431_02', 30)
    SetXCollisionFromOrigin(200)
    callSubroutine('EmissionStart')
    Unknown30017(12)
    Voiceline('su252')
    sprite('su431_03', 3)
    CreateObject('suef_431_punch', -1)
    sprite('su431_04', 3)
    sprite('su431_05', 3)
    sprite('su431_06', 3)
    sprite('su431_07', 3)
    sprite('su431_08', 4)
    KnockdownEffects(100, 1, 1)
    ScreenShake(20000, 20000)
    SetXCollisionFromOrigin(-1)
    sprite('su431_09', 4)
    if not SLOT_2:
        setInvincible(0)
    sprite('su431_10', 12)
    Unknown30017(-12)
    sprite('su431_11', 6)
    sprite('su213_12ex00', 6)
    SetXCollisionFromOrigin(-1)
    sprite('su213_13ex00', 6)
    sprite('su213_14ex00', 6)


@State
def UltimateRushAssault_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(190)
        MinimumDamage(10)
        AttackP2(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(500)
        AirUntechableTime(60)
        HardKnockdown(1)
        Hitstop(0)
        WallbounceReboundTime(0)
        ReduceHitEffects(1)
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        DefeatOpponentBehavior(1)
        EnableRapidCancel(0)
        SLOT_51 = 3
        SLOT_52 = 20

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_52 = SLOT_52 + -1
            ScreenShake(5000, 5000)
            XImpulseAcceleration(95)
            DashEffects(100, 1, 1)
        setInvincible(1)
        CameraControlEnable(1)

        def upon_45():
            SLOT_106 = SLOT_106 + -2
            if SLOT_106 <= 850:
                clearUponHandler(45)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su000_00', 1)
    sprite('su431_12', 5)
    sprite('su431_13', 5)
    DistortionSettings(60, -1, 0)
    CameraPosition(975)
    sprite('su431_14', 5)
    sprite('su431_15', 5)
    sprite('su431_16', 5)
    sprite('su431_17', 5)
    Voiceline('su256')
    SetBackground(2)
    callSubroutine('EmissionStart')
    Unknown30017(8)
    sprite('su431_18', 5)
    sprite('su431_19', 3)
    CreateObject('suef_431_charge', -1)
    ScreenShake(2500, 2500)

    def upon_EVERY_FRAME():
        if not SLOT_51:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(1)
    label(0)
    sprite('su431_20', 3)
    ScreenShake(2500, 2500)
    SLOT_51 = SLOT_51 + -1
    sprite('su431_21', 3)
    ScreenShake(2500, 2500)
    sprite('su431_22', 3)
    ScreenShake(2500, 2500)
    sprite('su431_19', 3)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su431_23', 6)
    SetBackground(1)
    ScreenShake(5000, 5000)
    CreateObject('suef_431_ring', -1)
    CameraControlEnable(0)
    CameraPosition(1000)
    sprite('su431_24', 6)
    ScreenShake(5000, 5000)
    sprite('su431_25', 2)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_431_charge')
    CreateObject('suef_431_beam', -1)
    physicsXImpulse(-40000)
    PrivateSE('suse_07')
    sprite('su431_26', 2)

    def upon_EVERY_FRAME():
        if not SLOT_52:
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            EnableRapidCancel(1)
            sendToLabel(9)
    label(2)
    sprite('su431_27', 2)
    RefreshMultihit()
    XImpulseAcceleration(75)
    sprite('su431_28', 2)
    RefreshMultihit()
    sprite('su431_29', 2)
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('su431_27', 3)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    XImpulseAcceleration(70)
    sprite('su431_28', 3)
    sprite('su431_29', 3)
    sprite('su431_27', 4)
    XImpulseAcceleration(70)
    DespawnEAEffect('suef_431_beam')
    sprite('su431_28', 4)
    sprite('su431_29', 4)
    sprite('su431_30', 4)
    sprite('su431_31', 4)
    sprite('su431_32', 4)
    sprite('su431_33', 6)
    EndMomentum(1)
    SetXCollisionFromOrigin(-1)
    sprite('su431_34', 6)
    sprite('su431_35', 6)
    sprite('su431_36', 6)


@State
def UltimateRushAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        MinimumDamage(10)
        AttackP2(60)
        PushbackX(30400)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        OppPositionOnHit(1, 200000, 0)
        EnemyHitstopAddition(0, 0, 0)
        Crumple(100)
        Stagger(120)
        Hitstop(7)
        AttackType(4)
        AttackDirection(0)
        SLOT_65 = 0
        SLOT_62 = 1
        SLOT_64 = SLOT_4
        callSubroutine('UltimateRush_Program')
        if SLOT_63 == 2:
            GroundedHitstunAnimation(11)
            AirHitstunAnimation(11)
            AirPushbackY(60000)
            AirPushbackX(-1000)
            AirUntechableTime(100)
        if SLOT_63 == 3:
            PushbackX(0)
        if SLOT_63 == 6:
            PushbackX(0)
        callSubroutine('UltimateRush_Next')
        StayAfterMovement(1, 0)

        def upon_EVERY_FRAME():
            if not SLOT_21:
                CameraControlEnable(0)

        def upon_OPPONENT_HIT():
            CameraControlEnable(1)
            SetActionMark(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su431_00', 4)
    setInvincible(1)
    sprite('su431_01', 6)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('su431_02', 30)
    SetXCollisionFromOrigin(200)
    callSubroutine('EmissionStart')
    Unknown30017(12)
    Voiceline('su257')
    sprite('su431_03', 3)
    CreateObject('suef_431_punch', -1)
    sprite('su431_04', 3)
    sprite('su431_05', 3)
    sprite('su431_06', 3)
    sprite('su431_07', 3)
    sprite('su431_08', 4)
    KnockdownEffects(100, 1, 1)
    ScreenShake(20000, 20000)
    SetXCollisionFromOrigin(-1)
    sprite('su431_09', 4)
    if not SLOT_2:
        setInvincible(0)
    sprite('su431_10', 12)
    Unknown30017(-12)
    sprite('su431_11', 6)
    sprite('su213_12ex00', 6)
    SetXCollisionFromOrigin(-1)
    sprite('su213_13ex00', 6)
    sprite('su213_14ex00', 6)


@State
def UltimateRushAssault_FinishOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(190)
        MinimumDamage(10)
        AttackP2(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(500)
        AirUntechableTime(60)
        HardKnockdown(1)
        Hitstop(0)
        WallbounceReboundTime(0)
        ReduceHitEffects(1)
        OnlyHitPlayer(1)
        PassByArmor(1)
        AttackType(4)
        CHStateIfCHStart(3)
        DefeatOpponentBehavior(1)
        EnableRapidCancel(0)
        SLOT_51 = 3
        SLOT_52 = 34

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_52 = SLOT_52 + -1
            ScreenShake(5000, 5000)
            XImpulseAcceleration(95)
            DashEffects(100, 1, 1)
        setInvincible(1)
        CameraControlEnable(1)

        def upon_45():
            SLOT_106 = SLOT_106 + -2
            if SLOT_106 <= 850:
                clearUponHandler(45)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su000_00', 1)
    sprite('su431_12', 5)
    sprite('su431_13', 5)
    DistortionSettings(60, -1, 0)
    CameraPosition(975)
    sprite('su431_14', 5)
    sprite('su431_15', 5)
    sprite('su431_16', 5)
    sprite('su431_17', 5)
    Voiceline('su261')
    SetBackground(2)
    callSubroutine('EmissionStart')
    Unknown30017(8)
    sprite('su431_18', 5)
    sprite('su431_19', 3)
    CreateObject('suef_431_charge', -1)
    ScreenShake(2500, 2500)

    def upon_EVERY_FRAME():
        if not SLOT_51:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(1)
    label(0)
    sprite('su431_20', 3)
    ScreenShake(2500, 2500)
    SLOT_51 = SLOT_51 + -1
    sprite('su431_21', 3)
    ScreenShake(2500, 2500)
    sprite('su431_22', 3)
    ScreenShake(2500, 2500)
    sprite('su431_19', 3)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su431_23', 6)
    SetBackground(1)
    ScreenShake(5000, 5000)
    CreateObject('suef_431_ring', -1)
    CameraControlEnable(0)
    CameraPosition(1000)
    sprite('su431_24', 6)
    ScreenShake(5000, 5000)
    sprite('su431_25', 2)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_431_charge')
    CreateObject('suef_431_beam', -1)
    physicsXImpulse(-40000)
    PrivateSE('suse_07')
    sprite('su431_26', 2)

    def upon_EVERY_FRAME():
        if not SLOT_52:
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            EnableRapidCancel(1)
            sendToLabel(9)
    label(2)
    sprite('su431_27', 2)
    RefreshMultihit()
    XImpulseAcceleration(75)
    sprite('su431_28', 2)
    RefreshMultihit()
    sprite('su431_29', 2)
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('su431_27', 3)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    XImpulseAcceleration(70)
    sprite('su431_28', 3)
    sprite('su431_29', 3)
    sprite('su431_27', 4)
    XImpulseAcceleration(70)
    DespawnEAEffect('suef_431_beam')
    sprite('su431_28', 4)
    sprite('su431_29', 4)
    sprite('su431_30', 4)
    sprite('su431_31', 4)
    sprite('su431_32', 4)
    sprite('su431_33', 6)
    EndMomentum(1)
    SetXCollisionFromOrigin(-1)
    sprite('su431_34', 6)
    sprite('su431_35', 6)
    sprite('su431_36', 6)


@Subroutine
def UltimateRush_NextAtk():
    AttackLevel_(4)
    Damage(500)
    MinimumDamage(15)
    AttackP2(95)
    SingleProration(1)
    Hitstun(100)
    AirUntechableTime(100)
    HardKnockdown(1)
    PushbackX(19800)
    OnlyHitPlayer(1)
    PassByArmor(1)
    CHStateIfCHStart(3)
    callSubroutine('UltimateRush_Next')
    callSubroutine('UltimateRush_Program')
    DefeatOpponentBehavior(1)
    EnableRapidCancel(0)
    if PreviousStateCheck('UltimateRushAssault'):
        SLOT_52 = 1
    elif PreviousStateCheck('UltimateRushAssaultOD'):
        SLOT_52 = 1
    setInvincible(1)
    callSubroutine('EmissionStart')
    Unknown30016(255)
    CameraControlEnable(1)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 150000:
            XImpulseAcceleration(20)


@Subroutine
def UltimateRush_Program():
    SLOT_63 = 0
    SLOT_64 and 2
    if SLOT_0 == 2:
        SLOT_63 = 1
        ModifyVar_(14, 2, 64, 0, 2)
    else:
        SLOT_64 and 8
        if SLOT_0 == 8:
            SLOT_63 = 2
            ModifyVar_(14, 2, 64, 0, 8)
        else:
            SLOT_64 and 128
            if SLOT_0 == 128:
                SLOT_63 = 3
                ModifyVar_(14, 2, 64, 0, 128)
            else:
                SLOT_64 and 1024
                if SLOT_0 == 1024:
                    SLOT_63 = 4
                    ModifyVar_(14, 2, 64, 0, 1024)
                else:
                    SLOT_64 and 4096
                    if SLOT_0 == 4096:
                        SLOT_63 = 5
                        ModifyVar_(14, 2, 64, 0, 4096)
                    else:
                        SLOT_64 and 64
                        if SLOT_0 == 64:
                            SLOT_63 = 6
                            ModifyVar_(14, 2, 64, 0, 64)
                        else:
                            SLOT_64 and 32
                            if SLOT_0 == 32:
                                SLOT_63 = 7
                                ModifyVar_(14, 2, 64, 0, 32)
                            else:
                                SLOT_64 and 16
                                if SLOT_0 == 16:
                                    SLOT_63 = 8
                                    ModifyVar_(14, 2, 64, 0, 16)


@Subroutine
def UltimateRush_Next():

    def upon_OPPONENT_HIT():
        SetActionMark(1)
        AlphaValue(255)
        setInvincible(1)

    def upon_8():
        if SLOT_21:
            if SLOT_2:
                if SLOT_63 == 0:
                    if SLOT_62:
                        enterState('UltimateRushAssault_FinishOD')
                    else:
                        enterState('UltimateRushAssault_Finish')
                else:
                    SLOT_65 = SLOT_65 + 1
                    if SLOT_62:
                        if SLOT_65 == 1:
                            Voiceline('su258')
                        if SLOT_65 == 4:
                            Voiceline('su259')
                        if SLOT_65 == 7:
                            Voiceline('su260')
                    else:
                        if SLOT_65 == 1:
                            Voiceline('su253')
                        if SLOT_65 == 4:
                            Voiceline('su254')
                        if SLOT_65 == 7:
                            Voiceline('su255')
                if SLOT_63 == 1:
                    enterState('UltimateRush_Exe1')
                if SLOT_63 == 2:
                    enterState('UltimateRush_Exe2')
                if SLOT_63 == 3:
                    enterState('UltimateRush_Exe3')
                if SLOT_63 == 4:
                    enterState('UltimateRush_Exe4')
                if SLOT_63 == 5:
                    enterState('UltimateRush_Exe5')
                if SLOT_63 == 6:
                    enterState('UltimateRush_Exe6')
                if SLOT_63 == 7:
                    enterState('UltimateRush_Exe7')
                if SLOT_63 == 8:
                    if SLOT_62:
                        enterState('UltimateRush_Exe8SP')
                    else:
                        enterState('UltimateRush_Exe8')


@State
def UltimateRush_Exe1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        OppPositionOnHit(1, 200000, 0)
        if not SLOT_63:
            GroundedHitstunAnimation(1)
            AirPushbackX(24000)
            AirPushbackY(36000)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 1
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su400_00', 3)
    sprite('su400_01', 3)
    sprite('su400_03', 3)
    AltKnockdownEffects(100, 1, 1)
    sprite('su400_04', 2)
    physicsXImpulse(60000)
    CommonSE('000_airdash_1')
    sprite('su400_05', 2)
    XImpulseAcceleration(200)
    DashEffects(100, 1, 0)
    CreateObject('suef_400', -1)
    loopRest()
    if SLOT_51 == 3:
        sendToLabel(1)
    sprite('su400_07', 3)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 0)
    DespawnEAEffect('suef_400')
    sprite('su400_21', 3)
    XImpulseAcceleration(60)
    DashEffects(100, 1, 0)
    loopRest()
    if SLOT_63:
        conditionalSendToLabel(9)
    sprite('su032_11', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 1)
    sprite('su032_12', 3)
    EndMomentum(1)
    SkidEffects(100, 1, 1)
    sprite('su032_13', 3)
    sprite('su032_14', 3)
    sprite('su032_15', 1)
    loopRest()
    ExitState()
    label(1)
    sprite('su400_07', 2)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 0)
    DespawnEAEffect('suef_400')
    SetXCollisionFromOrigin(-1)
    DashEffects(100, 1, 0)
    sprite('su400_09', 1)
    XImpulseAcceleration(60)
    sprite('su400_10', 1)
    sprite('su400_11', 1)
    XImpulseAcceleration(60)
    sprite('su400_12', 2)
    RefreshMultihit()
    CreateObject('suef_400_claw', -1)
    CreateObject('suef_400_claw2', -1)
    sprite('su400_13', 2)
    XImpulseAcceleration(60)
    sprite('su400_14', 2)
    XImpulseAcceleration(60)
    if SLOT_63:
        conditionalSendToLabel(9)
    sprite('su400_15', 3)
    EndMomentum(1)
    AltKnockdownEffects(100, 1, 1)
    sprite('su400_16', 3)
    sprite('su400_17', 3)
    sprite('su400_18', 3)
    sprite('su400_19', 3)
    sprite('su400_20', 2)
    label(9)
    sprite('keep', 1)


@State
def UltimateRush_Exe2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckAntiAirLv')
        callSubroutine('UltimateRush_NextAtk')
        OppPositionOnHit(1, 200000, 50000)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        if not SLOT_63:
            GroundedHitstunAnimation(10)
            AirHitstunAnimation(10)
            AirPushbackX(8000)
            AirPushbackY(54000)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 2
        if SLOT_137:
            DamageMultiplier(80)
    if not SLOT_52:
        notConditionalSendToLabel(0)
    sprite('su401_00', 4)
    sprite('su401_01', 4)
    sprite('su401_02', 4)
    sprite('su401_03', 4)
    label(0)
    sprite('su401_04', 1)
    sprite('su401_05', 3)
    CreateObject('suef_401_SP', -1)
    ScreenShake(10000, 25000)
    if SLOT_63:
        conditionalSendToLabel(1)
    CommonSE('016_explode_1')
    CommonSE('209_down_normal_1')
    sprite('su401_06', 3)
    sprite('su401_07', 3)
    sprite('su401_05', 3)
    sprite('su401_06', 3)
    sprite('su401_07', 3)
    sprite('su401_08', 2)
    sprite('su401_09', 2)
    sprite('su401_10', 2)
    sprite('su401_11', 2)
    sprite('su401_12', 3)
    sprite('su401_13', 3)
    sprite('su401_14', 3)
    sprite('su401_15', 3)
    sprite('su401_16', 3)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('su401_08', 2)
    sprite('su401_09', 2)
    label(9)
    sprite('keep', 1)


@State
def UltimateRush_Exe3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckShotLv')
        callSubroutine('UltimateRush_NextAtk')
        if SLOT_53:
            Damage(600)
        if SLOT_54:
            Damage(700)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(100)
        OppPositionOnHit(1, 200000, 0)
        if not SLOT_63:
            GroundedHitstunAnimation(13)
            AirHitstunAnimation(13)
            AirPushbackX(16000)
            AirPushbackY(32000)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 3
        if SLOT_137:
            DamageMultiplier(80)
    if not SLOT_52:
        notConditionalSendToLabel(0)
    sprite('su405_00', 2)
    sprite('su405_01', 2)
    sprite('su405_02', 3)
    ScreenShake(2000, 2000)
    sprite('su405_03', 3)
    CreateObject('suef_405', 0)
    CreateObject('suef_405_crack', 0)
    sprite('su405_04', 3)
    sprite('su405_05', 3)
    ScreenShake(2000, 2000)
    label(0)
    sprite('su405_03', 3)
    CreateObject('suef_405', 0)
    CreateObject('suef_405_crack', 0)
    sprite('su405_06', 3)
    sprite('su405_07', 3)
    ScreenShake(5000, 5000)
    DespawnEAEffect('suef_405')
    CreateObject('suef_405kick_SP', -1)
    if SLOT_52:
        physicsXImpulse(45000)
    PrivateSE('suse_04')
    CommonSE('209_down_normal_0')
    sprite('su405_08', 3)
    physicsXImpulse(0)
    sprite('su405_09', 3)
    loopRest()
    if SLOT_63:
        conditionalSendToLabel(9)
    sprite('su405_10', 3)
    sprite('su405_11', 3)
    sprite('su405_12', 3)
    label(9)
    sprite('su405_13', 3)
    sprite('su405_14', 3)
    sprite('su405_15', 2)


@State
def UltimateRush_Exe4():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckMidAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        Damage(100)
        AirPushbackX(-1000)
        AirPushbackY(-10000)
        GroundBounce(1)
        Hitstop(2)
        OppPositionOnHit(1, 120000, 0)
        if SLOT_51 == 2:
            SLOT_53 = 1
        uponSendToLabel(LANDING, 2)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 4
        if SLOT_137:
            DamageMultiplier(80)
    if not SLOT_52:
        notConditionalSendToLabel(0)
    sprite('su023_00', 3)
    CommonSE('002_highjump_1')
    sprite('su023_01', 3)
    label(0)
    sprite('su406_00', 2)
    physicsXImpulse(40000)
    physicsYImpulse(16000)
    setGravity(1600)
    CreateParticle('ef_smokej', -1)
    sprite('su406_01', 2)
    sprite('su406_02', 2)
    sprite('su406_03', 1)
    sprite('su406_04', 1)
    sprite('su406_05', 1)
    sprite('su406_06ex00', 3)
    CreateObject('suef_406_roll_3d', 103)
    RefreshMultihit()
    label(1)
    sprite('su406_07ex00', 3)
    RefreshMultihit()
    sprite('su406_08ex00', 3)
    RefreshMultihit()
    sprite('su406_09ex00', 3)
    RefreshMultihit()
    sprite('su406_06ex00', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('su406_10', 2)
    EndMomentum(1)
    DespawnEAEffect('suef_406_roll_3d')
    CreateObject('suef_406', 0)
    CommonSE('016_explode_2')
    ScreenShake(8000, 8000)
    RefreshMultihit()
    Damage(300)
    AirPushbackX(15000)
    AirPushbackY(20000)
    Hitstop(6)
    GroundBounce(0)
    if SLOT_53:
        CreateObject('suef_406_SP', 0)
        Damage(900)
        if SLOT_137:
            DamageMultiplier(80)
    if not SLOT_63:
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackY(40000)
    sprite('su406_11', 2)
    if SLOT_63:
        conditionalSendToLabel(9)
    sprite('su406_12', 4)
    sprite('su406_13', 4)
    sprite('su406_14', 3)
    sprite('su406_15', 3)
    sprite('su406_16', 3)
    sprite('su406_17', 2)
    label(9)
    sprite('keep', 1)


@State
def UltimateRush_Exe5():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckLowAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        Damage(200)
        PushbackX(4000)
        AirPushbackX(-1000)
        AirPushbackY(-10000)
        Hitstop(3)
        OppPositionOnHit(1, 110000, 0)
        clearUponHandler(EVERY_FRAME)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            XImpulseAcceleration(80)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 5
        if SLOT_137:
            DamageMultiplier(80)
    if not SLOT_52:
        notConditionalSendToLabel(0)
    sprite('su407_00', 2)
    sprite('su407_01', 3)
    label(0)
    sprite('su407_02', 3)
    sprite('su407_03', 3)
    physicsXImpulse(100000)
    CommonSE('000_airdash_2')
    sprite('su407_04', 2)
    CreateObject('suef_407_jiware', -1)
    ScreenShake(13000, 13000)
    RefreshMultihit()
    CommonSE('209_down_normal_1')
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    PerAcceleration(0)
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_04', 2)
    RefreshMultihit()
    sprite('su407_05', 2)
    sprite('su407_06', 1)
    XImpulseAcceleration(50)
    sprite('su407_07', 1)
    XImpulseAcceleration(50)
    sprite('su407_08', 1)
    EndMomentum(1)
    sprite('su407_09', 2)
    sprite('su407_10', 2)
    DespawnEAEffect('suef_407_jiware')
    sprite('su407_11', 2)
    sprite('su407_12', 3)
    sprite('su407_13', 3)
    KnockdownEffects(100, 1, 1)
    CreateObject('suef_407_kick', -1)
    XImpulseAcceleration(0)
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(4000)
    AirPushbackY(50000)
    CameraControlEnable(1)
    sprite('su407_14', 3)
    sprite('su407_15', 3)
    sprite('su407_16', 3)
    sprite('su407_17', 3)
    sprite('su407_18', 3)
    sprite('su407_19', 3)
    sprite('su407_20', 4)
    KnockdownEffects(100, 1, 0)
    sprite('su407_21', 4)
    sprite('su407_22', 3)
    sprite('su407_23', 3)


@State
def UltimateRush_Exe6():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckRushAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        Damage(350)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackY(3000)
        YImpulseBeforeWallbounce(1000)
        Hitstop(2)
        OppPositionOnHit(1, 150000, 100000)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 6
        if SLOT_137:
            DamageMultiplier(80)
        StayAfterMovement(1, 0)
    sprite('su404_00', 2)
    sprite('su404_01', 3)
    sprite('su404_02', 3)
    sprite('su404_03', 3)
    sprite('su404_04', 2)
    CreateObject('suef_404', 0)
    physicsXImpulse(20000)
    sprite('su404_05', 2)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('su404_06', 2)
    RefreshMultihit()
    sprite('su404_04', 2)
    RefreshMultihit()
    sprite('su404_05', 2)
    RefreshMultihit()
    sprite('su404_06', 2)
    RefreshMultihit()
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(20000)
    AirPushbackY(13000)
    sprite('su404_07', 1)
    sprite('su404_08', 1)
    sprite('su404_09', 1)
    sprite('su404_10', 1)
    DespawnEAEffect('suef_404')
    sprite('su404_11', 1)
    sprite('su404_12', 1)
    sprite('su404_13', 1)
    sprite('su404_14', 2)


@State
def UltimateRush_Exe7():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckRushAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        AttackOff()
        AirPushbackX(80000)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(1000)
        OppPositionOnHit(1, 150000, 50000)
        Hitstop(7)
        EnemyHitstopAddition(0, 15, 15)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 7
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su403_00', 4)
    sprite('su403_01', 4)
    sprite('su403_04', 4)
    physicsXImpulse(20000)
    sprite('su403_09', 2)
    XImpulseAcceleration(400)
    sprite('su403_10', 2)
    sprite('su403_11', 2)
    XImpulseAcceleration(30)
    sprite('su403_12', 3)
    RefreshMultihit()
    ScreenShake(15000, 15000)
    EndMomentum(1)
    sprite('su403_13', 3)
    CreateObject('suef_403_hand', -1)
    sprite('su403_14', 3)
    sprite('su403_15', 3)
    DespawnEAEffect('suef_403_hand')
    CreateObject('suef_403_smash', -1)
    ObjectUpon(STATE_END, 33)
    sprite('su403_16', 3)
    WallbounceEffects(0, 0, 1)
    RefreshMultihit()
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    WallbounceReboundTime(-10)
    Wallstick(1)
    WallstickDuration(100)
    AirHitstunAfterWallbounce(100)
    HardKnockdown(1)
    OppPositionOnHit(1, 250000, 100000)
    EnemyHitstopAddition(0, 0, 0)
    sprite('su403_17', 3)
    sprite('su403_18', 3)
    sprite('su403_19', 3)
    CameraControlEnable(1)
    sprite('su403_20', 3)
    sprite('su403_21', 3)
    sprite('su010_00', 2)


@State
def UltimateRush_Exe8():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckLongAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        Damage(1500)
        Hitstop(12)
        GroundedHitstunAnimation(9)
        AirPushbackX(4000)
        AirPushbackY(2000)
        YImpulseBeforeWallbounce(60)
        UseSlashHitspark(1)
        CameraControlEnable(1)
        StayAfterMovement(1, 0)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 8
        if SLOT_137:
            DamageMultiplier(80)
        HitAnywhere(1)
    sprite('su402_00', 3)
    CreateObject('suef_402', -1)
    sprite('su402_01', 3)
    sprite('su402_02', 3)
    sprite('su402_03', 2)
    sprite('su402_04', 2)
    PrivateSE('suse_05')
    PrivateSE('suse_02')
    CommonSE('006_swing_blade_2')
    sprite('su402_05', 2)
    sprite('su402_06', 3)
    KnockdownEffects(100, 1, 0)
    AttackOff()
    sprite('su402_07ex01', 3)
    RefreshMultihit()
    sprite('su402_08', 3)
    sprite('su402_09', 3)
    sprite('su402_10', 3)
    sprite('su402_08', 3)
    sprite('su402_09', 3)
    sprite('su402_10', 3)
    sprite('su402_11', 3)
    sprite('su402_12', 3)
    sprite('su402_13', 3)
    sprite('su402_14', 1)


@State
def UltimateRush_Exe8SP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('CheckLongAssaultLv')
        callSubroutine('UltimateRush_NextAtk')
        Damage(2000)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirPushbackX(4000)
        AirPushbackY(2000)
        YImpulseBeforeWallbounce(60)
        UseSlashHitspark(1)
        CameraControlEnable(1)
        StayAfterMovement(1, 0)
        SLOT_7 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_7 = 8
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su430_00', 3)
    CreateObject('suef_430_sword', -1)
    sprite('su430_01', 3)
    sprite('su430_02', 3)
    DistortionSettings(53, -1, 0)
    sprite('su430_03', 3)
    SetBackground(2)
    sprite('su430_04', 3)
    ParticleColorFromPalette(128, 128, 128)
    CallCustomizableParticle('suef_430sword', 103)
    sprite('su430_05', 3)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_05', 3)
    sprite('su430_06', 3)
    sprite('su430_07', 3)
    sprite('su430_08', 6)
    TriggerUponForState('suef_430_sword', 32)
    sprite('su430_09', 6)
    sprite('su430_10', 6)
    sprite('su430_11', 6)
    sprite('su430_12', 6)
    sprite('su430_13', 6)
    sprite('su430_14', 1)
    sprite('su430_15', 1)
    sprite('su430_16', 6)
    CreateObject('suef_430_slash', -1)
    PrivateSE('suse_02')
    PrivateSE('suse_06')
    PrivateSE('suse_06')
    CommonSE('025_cleanhit_slash')
    sprite('su430_17', 3)
    sprite('su430_18', 3)
    sprite('su430_19', 3)
    sprite('su430_20', 3)
    sprite('su430_21', 5)
    sprite('su430_22', 5)
    sprite('su402_11ex01', 5)
    sprite('su402_12ex01', 5)
    sprite('su402_13ex01', 4)
    sprite('su402_14ex01', 4)


@State
def UltimateCommand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        setInvincible(1)
        GuardPoint_(1)
        GuardpointHitstop(-2, -1)
        SpecificInvincibility(0, 1, 0, 1, 0)
    sprite('su214_00', 3)
    sprite('su214_01', 3)
    sprite('su214_02', 3)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su214_03', 3)
    DistortionSettings(60, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('su214_04', 3)
    sprite('su214_05', 3)
    sprite('su214_06', 3)
    sprite('su214_04', 3)
    sprite('su214_05', 3)
    sprite('su214_06', 3)
    sprite('su214_04', 3)
    CreateObject('suef_432_auradust', 103)
    Voiceline('su262')
    sprite('su214_05', 3)
    sprite('su214_06', 3)
    sprite('su214_04', 3)
    sprite('su214_05', 3)
    sprite('su214_06', 3)
    sprite('su214_07', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    CreateObject('suef_214ground', 1)
    CreateObject('suef_432_aura', -1)
    CreateObject('suef_432_aura2', -1)
    SLOT_5 = 0
    SLOT_4 and 8
    if not SLOT_0 == 8:
        ModifyVar_(8, 2, 4, 0, 8)
        AddActionMark(1)
    SLOT_4 and 128
    if not SLOT_0 == 128:
        ModifyVar_(8, 2, 4, 0, 128)
        AddActionMark(1)
    SLOT_4 and 1024
    if not SLOT_0 == 1024:
        ModifyVar_(8, 2, 4, 0, 1024)
        AddActionMark(1)
    SLOT_4 and 4096
    if not SLOT_0 == 4096:
        ModifyVar_(8, 2, 4, 0, 4096)
        AddActionMark(1)
    SLOT_4 and 64
    if not SLOT_0 == 64:
        ModifyVar_(8, 2, 4, 0, 64)
        AddActionMark(1)
    SLOT_4 and 32
    if not SLOT_0 == 32:
        ModifyVar_(8, 2, 4, 0, 32)
        AddActionMark(1)
    SLOT_4 and 16
    if not SLOT_0 == 16:
        ModifyVar_(8, 2, 4, 0, 16)
        AddActionMark(1)
    if SLOT_2:
        PrivateSE('suse_11')
        PrivateSE('suse_11')
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    setInvincible(0)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_11', 3)
    Unknown30017(-25)
    sprite('su214_12', 3)
    sprite('su214_13', 3)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DamageFromStateOnly('AstralHeat')
        AttackLevel_(5)
        Damage(0)
        MinimumDamage(100)
        AirUntechableTime(300)
        AirPushbackX(0)
        AirPushbackY(-100000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HardKnockdown(999)
        OppPositionOnHit(1, 0, 0)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        DefeatOpponentBehavior(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            Hitstop(0)
            EnemyHitstopAddition(0, -1, -1)
            PushbackX(0)
            SetZVal(500)
            AstralHeatCleanup(1, 1)
            PlayPlayAstralBGM(1)
            DisableOppPushCollision(1)
            EnableCollision(0)
            WallCollisionDetection(0)
            ScreenCollision(0)
            sendToLabel(1)

            def upon_45():
                SLOT_6 = 1

            def upon_STATE_END():
                clearUponHandler(45)
                SLOT_6 = 0
        StayAfterMovement(1, 0)
    sprite('su450_00', 3)
    setInvincible(1)
    EndMomentum(1)
    CreateObject('suef_450_hand', -1)
    DespawnEAEffect('suef_aura')
    sprite('su450_01', 3)
    DistortionSettings(50, -1, 2)
    EmptyHeat()
    CreateObject('EMB_SU_AH', -1)
    Voiceline('su290')
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_02', 3)
    sprite('su450_03', 3)
    sprite('su450_04', 3)
    sprite('su450_05', 3)
    DespawnEAEffect('suef_450_hand')
    CreateObject('suef_450_atk1', -1)
    PrivateSE('suse_04')
    CommonSE('005_swing_grap_2_2')
    sprite('su450_06', 3)
    sprite('su450_07', 4)
    setInvincible(0)
    sprite('su450_08', 4)
    sprite('su450_09', 4)
    sprite('su450_07', 4)
    sprite('su450_08', 4)
    sprite('su450_09', 4)
    sprite('su450_33', 4)
    sprite('su450_34', 4)
    sprite('su450_35', 4)
    ExitState()
    label(1)
    sprite('su450_07', 3)
    sprite('su450_08', 3)
    sprite('su450_09', 3)
    sprite('su450_07', 3)
    sprite('su450_08', 3)
    sprite('su450_09', 3)
    sprite('su450_07', 3)
    sprite('su450_08', 3)
    sprite('su450_09', 3)
    sprite('su450_07', 3)
    sprite('su450_08', 3)
    sprite('su450_09', 3)
    sprite('su450_07', 3)
    sprite('su450_08', 3)
    sprite('su450_09', 3)
    HUDVisibillity(1)
    sprite('su450_10', 6)
    CreateObject('suef_450_atk2', 0)
    Voiceline('su291')
    RefreshMultihit()
    Damage(3000)
    HitAnywhere(1)
    Hitstop(6)
    EnemyHitstopAddition(0, 0, 0)
    OppPositionOnHit(0, 0, 0)
    AirUntechableTime(999)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(80000)
    AirPushbackY(40000)
    YImpulseBeforeWallbounce(0)
    CreateObject('AstralHeat_Camera', -1)
    PrivateSE('suse_00')
    sprite('su450_11', 3)
    CreateObject('suef_450_bg', -1)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_11', 3)
    sprite('su450_12', 3)
    sprite('su450_13', 3)
    sprite('su450_14', 6)
    CreateObject('suef_450_shake', -1)
    sprite('su450_15', 6)
    CreateObject('suef_450_sword', -1)
    PrivateSE('suse_05')
    PrivateSE('suse_05')
    Voiceline('su292')
    sprite('su450_16', 8)
    sprite('su450_17', 8)
    sprite('su450_18', 8)
    sprite('su450_19', 8)
    sprite('su450_20', 6)
    sprite('su450_21', 6)
    sprite('su450_22', 6)
    TriggerUponForState('suef_450_shake', 32)
    PrivateSE('suse_05')
    PrivateSE('suse_05')
    sprite('su450_23', 6)
    sprite('su450_24', 3)
    CreateObject('suef_450_swordaura', -1)
    CreateObject('suef_450_storm_group', -1)
    PrivateSE('suse_07')
    SetActionMark(12)

    def upon_EVERY_FRAME():
        if SLOT_2 >= 12:
            RefreshMultihit()
            Damage(1498)
            UseSlashHitspark(1)
            HitsparkSize(0)
            Hitstop(0)
            SetActionMark(0)
            AddCombo(1)
            CreateObject('suef_450_HitEff', 100)
        else:
            AddActionMark(1)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    Voiceline('su293')
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_24', 3)
    sprite('su450_25', 3)
    sprite('su450_26', 3)
    sprite('su450_27', 3)
    TriggerUponForState('suef_450_sword', 32)
    PrivateSE('suse_06')
    PrivateSE('suse_06')
    SetActionMark(8)

    def upon_EVERY_FRAME():
        if SLOT_2 >= 8:
            Damage(1498)
            RefreshMultihit()
            SetActionMark(0)
            AddCombo(1)
            CreateObject('suef_450_HitEff', 100)
        else:
            AddActionMark(1)
    sprite('su450_28', 3)
    TriggerUponForState('suef_450_swordaura', 32)
    sprite('su450_29', 3)
    TriggerUponForState('AstralHeat_Camera', 33)
    DespawnEAEffect('suef_450_storm_group')
    sprite('su450_30', 3)
    CreateObject('suef_450_swordaura2', -1)
    CreateObject('suef_450_storm2_group', -1)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    PrivateSE('suse_10')
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    TriggerUponForState('suef_450_shake', 33)
    TriggerUponForState('suef_450_storm2_group', 32)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    TriggerUponForState('suef_450_shake', 34)
    TriggerUponForState('suef_450_storm2_group', 33)
    PrivateSE('suse_10')
    SetActionMark(4)

    def upon_EVERY_FRAME():
        if SLOT_2 >= 4:
            RefreshMultihit()
            Damage(1997)
            SetActionMark(0)
            AddCombo(1)
            CreateObject('suef_450_HitEff', 100)
            CreateObject('suef_450_HitEff', 100)
        else:
            AddActionMark(1)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    Voiceline('su294')
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    CreateObject('suef_450_storm3_group', -1)
    sprite('su450_30', 3)
    SetActionMark(2)

    def upon_EVERY_FRAME():
        if SLOT_2 >= 2:
            RefreshMultihit()
            SetActionMark(0)
            AddCombo(1)
            CreateObject('suef_450_HitEff', 100)
            CreateObject('suef_450_HitEff', 100)
        else:
            AddActionMark(1)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('su450_31', 3)
    sprite('su450_32', 3)
    sprite('su450_30', 3)
    sprite('null', 10)
    clearUponHandler(EVERY_FRAME)
    DespawnEAEffect('suef_450_sword')
    DespawnEAEffect('suef_450_swordaura2')
    DespawnEAEffect('suef_450_storm2_group')
    DespawnEAEffect('suef_450_storm3_group')
    DespawnEAEffect('suef_450_shake')
    DespawnEAEffect('suef_450_bg')
    CreateObject('suef_450_HitEff', 100)
    CreateObject('suef_450_HitEff', 100)
    CreateObject('suef_450_HitEff', 100)
    CreateObject('suef_450_HitEff', 100)
    CreateObject('suef_450_HitEff', 100)
    sprite('su450_29', 80)
    TriggerUponForState('AstralHeat_Camera', 41)
    Visibility(1)
    SetBackground(2)
    CameraControlEnable(1)
    CameraFast(1)
    RefreshMultihit()
    Damage(14119)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackY(30000)
    AirPushbackX(100000)
    ResetGravity()
    OppPositionOnHit(2, 0, 0)
    DefeatOpponentBehavior(3)
    DamageEffect(5, '')
    HitsparkSize(1000)
    AddCombo(4)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():

        def RunOnObject_22():
            AlphaValue(0)
    sprite('su450_29', 20)
    SetBackground(3)
    sprite('su611_09', 6)
    XPositionRelativeFacing(260000)
    Visibility(0)
    CreateObject('suef_450_end', -1)
    CreateObject('suef_611_ah', -1)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    WinAction()
    DemoTimer(150)
    sprite('su611_12', 6)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    Voiceline('su295')
    label(3)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(3)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        DespawnEAEffect('suef_aura')

        def upon_14():
            Voiceline('su054')
    sprite('su900_00', 32767)
    EnableCollision(0)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraFast(1)
    CameraControlEnable(1)
    CameraControlInfinity(1)
    FaceLeft()
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    EndMomentum(1)
    CreateObject('suef_900_circle', 0)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(220000)
    sprite('su901_00', 6)
    physicsYImpulse(-180)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    physicsYImpulse(180)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    sprite('su901_00', 6)
    sprite('su901_01', 6)
    loopRest()
    if random_(2, 0, 30):
        conditionalSendToLabel(0)
    sprite('su901_02', 6)
    physicsYImpulse(-180)
    sprite('su901_03', 6)
    Voiceline('su055')
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('su901_02', 6)
    physicsYImpulse(-180)
    Voiceline('su318')
    sprite('su901_03', 3)
    sprite('su901_02', 3)
    sprite('su901_01', 3)
    sprite('su901_02', 3)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    label(9)
    sprite('su901_04', 6)
    YAccel(-100)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    sprite('su901_03', 6)
    sprite('su901_04', 6)
    loopRest()
    gotoLabel(9)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        PushbackX(0)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            if SLOT_XDistanceFromFowardCorner <= 200000:
                SLOT_XDistanceFromCenterOfStage = 1665000

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        StayAfterMovement(1, 0)
    sprite('su203_00ex00', 3)
    E0EAEffect('BurstDDeff', 103)
    sprite('su203_01ex00', 4)
    sprite('su203_02ex00', 4)
    sprite('su203_03ex00', 4)
    sprite('su203_04ex00', 4)
    SetXCollisionFromOrigin(200)
    Voiceline('su280')
    sprite('su313_06ex00', 3)
    CreateObject('suef_440', 0)
    CreateObject('suef_440_smoke', -1)
    PrivateSE('suse_02')
    sprite('su313_07ex00', 5)
    setInvincible(0)
    sprite('su313_08ex00', 5)
    sprite('su313_09ex00', 5)
    sprite('su313_10ex00', 5)
    sprite('su313_11ex00', 5)
    SetXCollisionFromOrigin(-1)
    sprite('su313_12ex00', 5)
    sprite('su313_13ex00', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        PushbackX(0)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            if SLOT_XDistanceFromFowardCorner <= 200000:
                SLOT_XDistanceFromCenterOfStage = 1665000

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        StayAfterMovement(1, 0)
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('su203_00ex00', 1)
    E0EAEffect('BurstDDeff', 103)
    sprite('su203_01ex00', 2)
    sprite('su203_02ex00', 2)
    sprite('su203_03ex00', 2)
    sprite('su203_04ex00', 2)
    SetXCollisionFromOrigin(200)
    Voiceline('su280')
    sprite('su313_06ex00', 3)
    CreateObject('suef_440', 0)
    CreateObject('suef_440_smoke', -1)
    PrivateSE('suse_02')
    sprite('su313_07ex00', 5)
    setInvincible(0)
    sprite('su313_08ex00', 5)
    sprite('su313_09ex00', 5)
    sprite('su313_10ex00', 5)
    sprite('su313_11ex00', 5)
    SetXCollisionFromOrigin(-1)
    sprite('su313_12ex00', 5)
    sprite('su313_13ex00', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        HardKnockdown(10)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        DamageFromStateOnly('BurstDDAdd')
        DefeatOpponentBehavior(1)
        AttackDirection(0)
        HitAnywhere(1)
        MinimumDamage(10)
        if SLOT_51:
            AirPushbackX(4500)
            AirPushbackY(105000)
        else:
            AirPushbackX(3000)
            AirPushbackY(70000)
        StayAfterMovement(1, 0)
        SetBackground(1)
        CHStateIfCHStart(3)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 2)

        def upon_STATE_END():
            EnableCollision(1)
            CameraControlEnable(0)
            CameraNoScreenCollision(0)
            CameraNoCeiling(0)
    sprite('su313_06ex00', 3)
    setInvincible(1)
    AddX(-110000)
    StartMultihit()
    EnableCollision(0)
    DespawnEAEffect('suef_aura')
    sprite('su313_07ex00', 3)
    sprite('su313_08ex00', 3)
    sprite('su313_09ex00', 3)
    sprite('su313_10ex00', 3)
    sprite('su313_11ex00', 3)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraNoCeiling(1)
    sprite('su313_12ex00', 3)
    sprite('su313_13ex00', 3)
    sprite('su000_00', 2)
    CreateObject('suef_440_fireaura', 103)
    sprite('su023_00ex00', 4)
    sprite('su023_01ex00', 4)
    physicsXImpulse(15000)
    sprite('su406_00ex00', 3)
    CreateObject('suef_440_kick', -1)
    CommonSE('016_explode_2')
    PrivateSE('suse_00')
    JumpEffects(1, 1)
    physicsYImpulse(60000)
    setGravity(2000)
    if SLOT_51:
        YSpeed(35000)
    sprite('su406_01ex00', 3)
    sprite('keep', 1)
    if SLOT_51:
        conditionalSendToLabel(100)
    loopRest()
    sprite('su406_06ex00', 2)
    Damage(210)
    Hitstop(5)
    AirPushbackX(3000)
    ResetVerticalDrag()
    CreateObject('suef_440_rolling', 103)
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    Voiceline('su281')
    sprite('su406_09ex00', 2)
    sprite('su406_06ex00', 2)
    RefreshMultihit()
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    sprite('su406_09ex00', 2)
    sprite('su406_06ex00', 2)
    RefreshMultihit()
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    sprite('su406_09ex00', 2)
    loopRest()
    gotoLabel(1)
    label(100)
    sprite('su406_06ex00', 2)
    Damage(210)
    Hitstop(5)
    EnemyHitstopAddition(0, -2, -2)
    AirPushbackX(7000)
    AirPushbackY(60000)
    CreateObject('suef_440_rolling', 103)
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    Voiceline('su281')
    sprite('su406_09ex00', 2)
    sprite('su406_06ex00', 2)
    RefreshMultihit()
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    sprite('su406_09ex00', 2)
    RefreshMultihit()
    sprite('su406_06ex00', 2)
    RefreshMultihit()
    Hitstop(4)
    EnemyHitstopAddition(0, 0, 0)
    sprite('su406_07ex00', 2)
    RefreshMultihit()
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    sprite('su406_09ex00', 2)
    RefreshMultihit()
    sprite('su406_06ex00', 2)
    Hitstop(3)
    RefreshMultihit()
    sprite('su406_07ex00', 2)
    RefreshMultihit()
    sprite('su406_08ex00', 2)
    RefreshMultihit()
    ResetPushback()
    ResetVerticalDrag()
    sprite('su406_09ex00', 2)
    RefreshMultihit()
    sprite('su406_06ex00', 2)
    RefreshMultihit()
    sprite('su406_07ex00', 2)
    sprite('su406_08ex00', 2)
    sprite('su406_09ex00', 2)
    loopRest()
    label(1)
    sprite('su440_00', 3)
    TriggerUponForState('suef_440_rolling', 32)
    sprite('su440_00', 1)
    RefreshMultihit()
    sprite('su440_00', 3)
    if SLOT_51:
        AttackDefaults_Throw('BurstDDFinishSP', 3, 1, 0)
    else:
        AttackDefaults_Throw('BurstDDFinish', 3, 1, 0)
    DistanceCheck(-1, -1, -1, -1)
    RangeCheck(1000000)
    ThrowTechWindow(-1)
    PreventAirborneHit(0)
    RefreshMultihit()
    XImpulseAcceleration(0)
    sprite('su440_01', 3)
    sprite('su440_02', 3)
    PerGravity(250)
    sprite('su440_03', 3)
    PerGravity(250)
    sprite('su440_04', 3)
    PerGravity(250)
    sprite('su440_05', 3)
    PerGravity(250)
    sprite('su440_05', 3)
    PerGravity(250)
    sprite('su440_05', 3)
    PerGravity(250)
    sprite('su440_05', 3)
    PerGravity(250)
    sprite('su440_05', 3)
    PerGravity(250)
    label(2)
    sprite('su401_05ex00', 3)
    clearUponHandler(LANDING)
    AttackOff()
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_09ex00', 3)
    sprite('su401_10ex00', 3)
    sprite('su403_26ex00', 6)
    sprite('su403_27ex00', 6)
    sprite('su403_28ex00', 6)


@State
def BurstDDFinish():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 1, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirUntechableTime(200)
        AirPushbackX(9000)
        AirPushbackY(75000)
        YImpulseBeforeWallbounce(3000)
        HardKnockdown(10)
        ThrowTechWindow(-1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        DefeatOpponentBehavior(0)
        AttackType(4)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDFinish')
        CHStateIfCHStart(3)
        MinimumDamage(10)
        AttackOff()
        setInvincible(1)
        Unknown2066(1)
        EnableRapidCancel(0)
        EnableCollision(0)
        EndMomentum(1)
        EndYPhysicsImpulse()
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        CameraFast(1)
        clearUponHandler(LANDING)

        def upon_LANDING():
            ScreenShake(4000, 20000)
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            CameraControlEnable(0)
            CameraFast(0)
            CameraNoScreenCollision(0)
            CameraNoCeiling(0)
        StayAfterMovement(1, 0)
    sprite('su440_00', 3)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    sprite('su440_01', 3)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    EnableAfterimage(1)
    sprite('su440_02', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_03', 3)
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_04', 3)
    OppThrowAnimation(5, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_05', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_05', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PerGravity(200)
    sprite('su440_05', 300)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    label(1)
    sprite('su401_05ex00', 3)
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    clearUponHandler(LANDING)
    AbsoluteY(0)
    EndMomentum(1)
    RefreshMultihit()
    ScreenShake(4000, 20000)
    CreateObject('suef_440_finish', -1)
    PrivateSE('suse_04')
    CommonSE('016_explode_2')
    CommonSE('209_down_normal_1')
    Voiceline('su282')
    sprite('su401_05ex00', 3)
    sprite('su401_06ex00', 3)
    EnableCollision(1)
    EnableAfterimage(0)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    CameraControlEnable(0)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_09ex00', 3)
    sprite('su401_10ex00', 3)
    sprite('su403_26ex00', 4)
    sprite('su403_27ex00', 4)
    sprite('su403_28ex00', 4)


@State
def BurstDDFinishSP():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 1, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(100)
        Hitstop(0)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirUntechableTime(200)
        AirPushbackY(75000)
        YImpulseBeforeWallbounce(3000)
        GroundBounce(1)
        BouncePercentage(45)
        HardKnockdown(10)
        ThrowTechWindow(-1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        DefeatOpponentBehavior(0)
        AttackType(4)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDFinishSP')
        CHStateIfCHStart(3)
        MinimumDamage(10)
        AttackOff()
        setInvincible(1)
        Unknown2066(1)
        EnableRapidCancel(0)
        EnableCollision(0)
        EndMomentum(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        CameraFast(1)
        clearUponHandler(LANDING)

        def upon_LANDING():
            ScreenShake(8000, 40000)
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            CameraControlEnable(0)
            CameraFast(0)
            CameraNoScreenCollision(0)
            CameraNoCeiling(0)
        StayAfterMovement(1, 0)
    sprite('su440_00', 6)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    sprite('su440_01', 6)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    EnableAfterimage(1)
    sprite('su440_02', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_02', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    EndYPhysicsImpulse()
    sprite('su440_03', 6)
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_04', 6)
    OppThrowAnimation(5, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_05', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('su440_05', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PerGravity(150)
    sprite('su440_05', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PerGravity(200)
    sprite('su440_05', 300)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PerGravity(300)
    label(1)
    sprite('su401_05ex00', 3)
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    clearUponHandler(LANDING)
    AbsoluteY(0)
    EndMomentum(1)
    RefreshMultihit()
    ScreenShake(8000, 40000)
    CreateObject('suef_440_finish_sp', -1)
    PrivateSE('suse_04')
    CommonSE('016_explode_2')
    CommonSE('209_down_normal_1')
    CommonSE('025_cleanhit_grap')
    Voiceline('su282')
    sprite('su401_05ex00', 3)
    sprite('su401_06ex00', 3)
    EnableCollision(1)
    EnableAfterimage(0)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_06ex00', 3)
    CameraControlEnable(0)
    sprite('su401_07ex00', 3)
    sprite('su401_08ex00', 3)
    sprite('su401_09ex00', 3)
    sprite('su401_10ex00', 3)
    sprite('su403_26ex00', 4)
    sprite('su403_27ex00', 4)
    sprite('su403_28ex00', 4)


@Subroutine
def MouthTableInit():
    Unknown18011('su000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('su412', 13921, 13667, 24886, 25399, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('su000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('su412', 12641, 25392, 24886, 25398, 24886, 25398, 
            24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
            25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            Unknown18011('su5000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('su5020', 14433, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14433, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('su5040', 12641, 25394, 12343, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('su5060', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hz'):
            Unknown18011('su5260', 12641, 25392, 24887, 25399, 14388, 14177,
                14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('su5320', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('su5360', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('az'):
            Unknown18011('su5440', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25397, 13362, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('su5480', 12641, 25400, 24887, 25399, 14130, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('su5520', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 13155, 24886, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('su5580', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 12899, 24885, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('su5620', 12641, 25398, 24887, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('su5700', 14177, 13411, 24880, 25399, 24885, 25399,
                24885, 25399, 24887, 12337, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(100)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(120)
    if CharacterIDCheck('rc'):
        SyncEntry()
        gotoLabel(130)
    if CharacterIDCheck('hz'):
        SyncEntry()
        gotoLabel(230)
    if CharacterIDCheck('vh'):
        SyncEntry()
        gotoLabel(260)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('az'):
        SyncEntry()
        gotoLabel(320)
    if CharacterIDCheck('kk'):
        SyncEntry()
        gotoLabel(340)
    if CharacterIDCheck('ce'):
        SyncEntry()
        gotoLabel(360)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(410)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if CharacterIDCheck('su'):
        if SLOT_43:
            gotoLabel(0)
        else:
            gotoLabel(10)
    if random_(2, 0, 67):
        conditionalSendToLabel(10)
    label(0)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(1)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su412')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(2)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su413')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(10)
    sprite('null', 1)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    if random_(2, 0, 50):
        SetActionMark(1)
    label(11)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(11)
    sprite('null', 20)
    sprite('su020_00', 4)
    ColorForTransition(4283453520)
    CreateObject('suef_601', -1)
    CommonSE('016_explode_2')
    CommonSE('209_down_normal_1')
    CreateObject('suef_601_bloom', -1)
    CreateObject('suef_601_bloom_add', -1)
    physicsYImpulse(70000)
    ScreenShake(0, 30000)
    EndYPhysicsImpulse()
    uponSendToLabel(FALLING, 13)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 15)
    sprite('su020_01', 4)
    label(12)
    sprite('su020_00', 4)
    sprite('su020_01', 4)
    loopRest()
    gotoLabel(12)
    label(13)
    sprite('su020_07', 5)
    DespawnEAEffect('suef_601_bloom')
    CreateObject('suef_601_bloom2', -1)
    clearUponHandler(FALLING)
    if SLOT_2:
        Voiceline('su414')
    else:
        Voiceline('su416')
    sprite('su020_08', 5)
    label(14)
    sprite('su020_07', 5)
    clearUponHandler(FALLING)
    sprite('su020_08', 5)
    loopRest()
    gotoLabel(14)
    label(15)
    sprite('su024_00', 7)
    DespawnEAEffect('suef_601_bloom2')
    ColorTransition(4294967295, 30)
    clearUponHandler(LANDING)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    sprite('su601_00', 7)
    sprite('su601_01', 7)
    CreateObject('suef_aura', 103)
    sprite('su601_02', 7)
    sprite('su601_03', 7)
    sprite('su601_04', 7)
    sprite('su601_05', 7)
    sprite('su601_06', 7)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    if SLOT_2:
        Voiceline('su415')
        DemoTimer(120)
    else:
        Voiceline('su417')
        DemoTimer(150)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    ExitState()
    label(100)
    sprite('su600_tm610', 1)
    uponSendToLabel(32, 101)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su600_tm610', 32767)
    loopRest()
    label(101)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5000')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(102)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(102)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5001')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(110)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(111)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(111)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5020')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(112)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(112)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5021')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(120)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(121)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(121)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 170)
    Voiceline('su5040')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(122)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(122)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5041')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(130)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(131)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(131)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5060')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(132)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(132)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5061')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(230)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(231)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(231)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5260')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(232)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(232)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5261')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(260)
    sprite('su600_tm610', 1)
    uponSendToLabel(32, 261)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su600_tm610', 32767)
    loopRest()
    label(261)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 80)
    Voiceline('su5320')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(262)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(262)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5321')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    DemoTimer(100)
    loopRest()
    ExitState()
    label(280)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(281)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(281)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5360')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    ObjectUpon(22, 32)
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(282)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(282)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5361')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    ExitState()
    label(320)
    sprite('su600_tm610', 1)
    uponSendToLabel(32, 321)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su600_tm610', 32767)
    loopRest()
    label(321)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 170)
    Voiceline('su5440')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(322)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(322)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5441')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(340)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(341)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(341)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 130)
    Voiceline('su5480')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(342)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(342)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5481')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(360)
    sprite('su600_tm610', 1)
    uponSendToLabel(32, 361)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su600_tm610', 32767)
    loopRest()
    label(361)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 170)
    Voiceline('su5520')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(362)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(362)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5521')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(390)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(391)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(391)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 130)
    Voiceline('su5580')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(392)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(392)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5581')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(410)
    sprite('su600_tm610', 1)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    label(411)
    sprite('su600_tm610', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(411)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 130)
    Voiceline('su5620')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(412)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(412)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5621')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(440)
    sprite('su600_tm610', 1)
    uponSendToLabel(32, 441)
    CreateObject('su600_ha', -1)
    CreateObject('su600_tm', -1)
    PaletteIndex(5)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su600_tm610', 32767)
    loopRest()
    label(441)
    sprite('su600_tm610', 20)
    sprite('su600_tm610', 120)
    Voiceline('su5700')
    sprite('null', 30)
    TriggerUponForState('su600_ha', 32)
    CommonSE('015_blaze_2')
    sprite('null', 8)
    PaletteIndex(0)
    TriggerUponForState('su600_tm', 32)
    PrivateSE('suse_08')
    sprite('null', 8)
    sprite('null', 8)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 4)
    sprite('su600_00', 6)
    Size(1000)
    CreateObject('suef_600_bloom', -1)
    BlendMode_Normal()
    ForceBloomMaskOn(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    SetActionMark(5)
    label(442)
    sprite('su600_00', 6)
    AddActionMark(-1)
    sprite('su600_01', 6)
    sprite('su600_02', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(442)
    sprite('su600_03', 10)
    TriggerUponForState('suef_600_bloom', 32)
    PrivateSE('suse_02')
    PrivateSE('suse_04')
    sprite('su600_04', 8)
    ScreenShake(1000, 10000)
    CreateObject('suef_600_splash', 103)
    CreateParticle('suef_600ground2', -1)
    ForceBloomMaskOn(1)
    ForceShadowOn(1)
    ColorTransition(4294967295, 30)
    sprite('su600_05', 6)
    Voiceline('su5701')
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_05', 6)
    sprite('su600_06', 6)
    sprite('su600_07', 6)
    sprite('su600_08', 9)
    sprite('su600_09', 9)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    DemoTimer(100)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('su615_00', 6)
    StayAfterMovement(1, 0)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su615_01', 6)
    sprite('su615_02', 6)
    sprite('su615_03', 6)
    RandomVoiceline('su400', 100, 'su401', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    label(1)
    sprite('su615_04', 6)
    sprite('su615_05', 6)
    sprite('su615_06', 6)
    sprite('su615_07', 6)
    sprite('su615_08', 6)
    sprite('su615_09', 6)
    gotoLabel(1)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if SLOT_109:
        conditionalSendToLabel(50)
    if CharacterIDCheck('rg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('no'):
        conditionalSendToLabel(120)
    if CharacterIDCheck('rc'):
        conditionalSendToLabel(130)
    if CharacterIDCheck('hz'):
        conditionalSendToLabel(230)
    if CharacterIDCheck('vh'):
        conditionalSendToLabel(260)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(280)
    if CharacterIDCheck('az'):
        conditionalSendToLabel(320)
    if CharacterIDCheck('kk'):
        conditionalSendToLabel(340)
    if CharacterIDCheck('ce'):
        conditionalSendToLabel(360)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('mi'):
        conditionalSendToLabel(410)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    label(482)
    SLOT_4 and 16
    if SLOT_0 == 16:
        gotoLabel(30)
    elif random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(10)
    sprite('su610_00', 8)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su610_01', 8)
    sprite('su610_02', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    if SLOT_19 >= 640000:
        CameraLookAtEnemy(1)
    sprite('su610_03', 8)
    CreateObject('suef_610_soul', -1)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_06', 8)
    TriggerUponForState('suef_610_soul', 32)
    CameraLookAtEnemy(0)
    CameraControlEnable(1)
    sprite('su610_07', 6)
    CreateObject('suef_610_soul2', -1)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    Voiceline('su406')
    DemoEndOnVoiceEnd(1)
    sprite('su610_08', 7)
    sprite('su610_09', 7)
    sprite('su610_10', 20)
    sprite('su610_11', 6)
    sprite('su610_12', 6)
    sprite('su610_13', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_17', 6)
    TriggerUponForState('suef_610_soul2', 32)
    PrivateSE('suse_02')
    sprite('su610_18', 6)
    sprite('su610_19', 6)
    ScreenShake(0, 10000)
    label(11)
    sprite('su610_20', 7)
    sprite('su610_21', 7)
    sprite('su610_22', 7)
    sprite('su610_23', 7)
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su611_01', 6)
    Voiceline('su407')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(21)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(21)
    label(30)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su611_01', 6)
    CreateObject('suef_611', -1)
    PrivateSE('suse_00')
    Voiceline('su408')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 7)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    CreateObject('suef_611_b', -1)
    ScreenShake(0, 10000)
    PrivateSE('suse_05')
    PrivateSE('suse_02')
    label(31)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(31)
    label(50)
    sprite('su615_00', 6)
    StayAfterMovement(1, 0)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su615_01', 6)
    sprite('su615_02', 6)
    sprite('su615_03', 6)
    Voiceline('su406')
    DemoEndOnVoiceEnd(1)
    label(51)
    sprite('su615_04', 6)
    sprite('su615_05', 6)
    sprite('su615_06', 6)
    sprite('su615_07', 6)
    sprite('su615_08', 6)
    sprite('su615_09', 6)
    loopRest()
    gotoLabel(51)
    label(100)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su501')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(101)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(101)
    label(110)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su503')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(111)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(111)
    label(120)
    sprite('su610_00', 8)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su610_01', 8)
    sprite('su610_02', 8)
    sprite('su610_03', 8)
    Voiceline('su505')
    DemoEndOnVoiceEnd(1)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    if SLOT_19 >= 640000:
        CameraLookAtEnemy(1)
    sprite('su610_03', 8)
    CreateObject('suef_610_soul', -1)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_06', 8)
    TriggerUponForState('suef_610_soul', 32)
    CameraLookAtEnemy(0)
    CameraControlEnable(1)
    sprite('su610_07', 6)
    CreateObject('suef_610_soul2', -1)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    sprite('su610_08', 7)
    sprite('su610_09', 7)
    sprite('su610_10', 20)
    sprite('su610_11', 6)
    sprite('su610_12', 6)
    sprite('su610_13', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_17', 6)
    TriggerUponForState('suef_610_soul2', 32)
    PrivateSE('suse_02')
    sprite('su610_18', 6)
    sprite('su610_19', 6)
    ScreenShake(0, 10000)
    label(121)
    sprite('su610_20', 7)
    sprite('su610_21', 7)
    sprite('su610_22', 7)
    sprite('su610_23', 7)
    loopRest()
    gotoLabel(121)
    label(130)
    sprite('su610_00', 8)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su610_01', 8)
    sprite('su610_02', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    if SLOT_19 >= 640000:
        CameraLookAtEnemy(1)
    sprite('su610_03', 8)
    CreateObject('suef_610_soul', -1)
    sprite('su610_04', 8)
    Voiceline('su507')
    DemoEndOnVoiceEnd(1)
    sprite('su610_05', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_06', 8)
    TriggerUponForState('suef_610_soul', 32)
    CameraLookAtEnemy(0)
    CameraControlEnable(1)
    sprite('su610_07', 6)
    CreateObject('suef_610_soul2', -1)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    sprite('su610_08', 7)
    sprite('su610_09', 7)
    sprite('su610_10', 20)
    sprite('su610_11', 6)
    sprite('su610_12', 6)
    sprite('su610_13', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_17', 6)
    TriggerUponForState('suef_610_soul2', 32)
    PrivateSE('suse_02')
    sprite('su610_18', 6)
    sprite('su610_19', 6)
    ScreenShake(0, 10000)
    label(131)
    sprite('su610_20', 7)
    sprite('su610_21', 7)
    sprite('su610_22', 7)
    sprite('su610_23', 7)
    loopRest()
    gotoLabel(131)
    label(230)
    sprite('su610_00', 8)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su610_01', 8)
    sprite('su610_02', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    if SLOT_19 >= 640000:
        CameraLookAtEnemy(1)
    sprite('su610_03', 8)
    CreateObject('suef_610_soul', -1)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_06', 8)
    TriggerUponForState('suef_610_soul', 32)
    CameraLookAtEnemy(0)
    CameraControlEnable(1)
    sprite('su610_07', 6)
    CreateObject('suef_610_soul2', -1)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    Voiceline('su527')
    DemoEndOnVoiceEnd(1)
    sprite('su610_08', 7)
    sprite('su610_09', 7)
    sprite('su610_10', 20)
    sprite('su610_11', 6)
    sprite('su610_12', 6)
    sprite('su610_13', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_17', 6)
    TriggerUponForState('suef_610_soul2', 32)
    PrivateSE('suse_02')
    sprite('su610_18', 6)
    sprite('su610_19', 6)
    ScreenShake(0, 10000)
    label(231)
    sprite('su610_20', 7)
    sprite('su610_21', 7)
    sprite('su610_22', 7)
    sprite('su610_23', 7)
    loopRest()
    gotoLabel(231)
    label(260)
    sprite('su610_00', 8)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    sprite('su610_01', 8)
    sprite('su610_02', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    if SLOT_19 >= 640000:
        CameraLookAtEnemy(1)
    sprite('su610_03', 8)
    CreateObject('suef_610_soul', -1)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    sprite('su610_06', 8)
    TriggerUponForState('suef_610_soul', 32)
    CameraLookAtEnemy(0)
    CameraControlEnable(1)
    sprite('su610_07', 6)
    CreateObject('suef_610_soul2', -1)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    Voiceline('su533')
    DemoEndOnVoiceEnd(1)
    sprite('su610_08', 7)
    sprite('su610_09', 7)
    sprite('su610_10', 20)
    sprite('su610_11', 6)
    sprite('su610_12', 6)
    sprite('su610_13', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_14', 6)
    sprite('su610_15', 6)
    sprite('su610_16', 6)
    sprite('su610_17', 6)
    TriggerUponForState('suef_610_soul2', 32)
    PrivateSE('suse_02')
    sprite('su610_18', 6)
    sprite('su610_19', 6)
    ScreenShake(0, 10000)
    label(261)
    sprite('su610_20', 7)
    sprite('su610_21', 7)
    sprite('su610_22', 7)
    sprite('su610_23', 7)
    loopRest()
    gotoLabel(261)
    label(280)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su537')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(281)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(281)
    label(320)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su545')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(321)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(321)
    label(340)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su549')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(341)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(341)
    label(360)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su553')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(361)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(361)
    label(390)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su559')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(391)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(391)
    label(410)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su563')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(411)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(411)
    label(440)
    sprite('su611_00', 6)

    def upon_EVERY_FRAME():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        SLOT_6 = 0
    SLOT_4 and 16
    if SLOT_0 == 16:
        SetActionMark(1)
    sprite('su611_01', 6)
    if SLOT_2:
        CreateObject('suef_611', -1)
        PrivateSE('suse_00')
    Voiceline('su571')
    DemoEndOnVoiceEnd(1)
    sprite('su611_02', 6)
    sprite('su611_03', 6)
    sprite('su611_04', 6)
    sprite('su611_05', 7)
    sprite('su611_06', 7)
    sprite('su611_07', 5)
    sprite('su611_08', 6)
    if SLOT_2:
        CreateObject('suef_611_b', -1)
        PrivateSE('suse_05')
    ScreenShake(0, 10000)
    PrivateSE('suse_02')
    label(441)
    sprite('su611_09', 6)
    sprite('su611_10', 6)
    sprite('su611_11', 6)
    sprite('su611_12', 6)
    loopRest()
    gotoLabel(441)


@State
def CmnActLose():
    sprite('su620_00', 6)
    StayAfterMovement(1, 0)
    sprite('su620_01', 6)
    Voiceline('su411')
    DemoEndOnVoiceEnd(1)
    sprite('su620_02', 6)
    sprite('su620_03', 6)
    sprite('su620_04', 6)
    sprite('su620_05', 6)
    sprite('su620_06', 32767)


@State
def Act3Event_StandLoop():
    label(0)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_Reaction():
    sprite('su001_00', 6)
    callSubroutine('EmissionStart')
    Unknown30017(17)
    CreateObject('suef_001', -1)
    CreateObject('suef_001_blm_2d', -1)
    CommonSE('022_magiccircle_b')
    sprite('su001_01', 6)
    sprite('su001_02', 7)
    sprite('su001_03', 8)
    sprite('su001_04', 9)
    sprite('su001_05', 9)
    sprite('su001_06', 9)
    sprite('su001_07', 8)
    sprite('su001_08', 7)
    Unknown30017(-12)
    sprite('su001_09', 6)
    sprite('su001_10', 6)
    SLOT_57 = 0
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Chouhatsu():
    sprite('su300_00', 7)
    sprite('su300_01', 7)
    sprite('su300_02', 7)
    sprite('su300_03', 32767)
    loopRest()


@State
def Act3Event_ChouhatsuEnd():
    sprite('su300_04', 7)
    sprite('su300_05', 7)
    sprite('su300_06', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Win():
    sprite('su610_00', 9)
    sprite('su610_01', 6)
    sprite('su610_02', 3)
    label(0)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_WinEnd():
    sprite('su610_02', 6)
    sprite('su610_01', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Houkou():
    sprite('su214_00', 6)
    sprite('su214_01', 6)
    sprite('su214_02', 6)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su214_03', 6)
    sprite('su214_07', 6)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    CreateParticle('suef_214b', 0)
    CreateObject('suef_214ground', 1)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    PrivateSE('suse_03')
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateParticle('suef_214', 0)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_08', 3)
    ScreenShake(0, 6000)
    CreateParticle('suef_214', 0)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_11', 3)
    Unknown30017(-51)
    sprite('su214_12', 6)
    sprite('su214_13', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_HoukouLoop():
    sprite('su214_00', 6)
    sprite('su214_01', 6)
    sprite('su214_02', 6)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su214_03', 6)
    sprite('su214_07', 6)
    loopRest()
    label(0)
    sprite('su214_08', 6)
    ScreenShake(0, 6000)
    CreateObject('suef_214', 0)
    CreateParticle('suef_214b', 0)
    CreateObject('suef_214ground', 1)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    PrivateSE('suse_03')
    sprite('su214_09', 6)
    sprite('su214_10', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_HoukouLoopEnd():
    sprite('su214_08', 6)
    ScreenShake(0, 6000)
    CreateParticle('suef_214', 0)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    sprite('su214_09', 3)
    sprite('su214_10', 3)
    sprite('su214_11', 3)
    Unknown30017(-51)
    sprite('su214_12', 2)
    sprite('su214_13', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_RoundWin():
    sprite('su615_00', 6)
    sprite('su615_01', 6)
    sprite('su615_02', 6)
    sprite('su615_03', 6)
    label(0)
    sprite('su615_04', 6)
    sprite('su615_05', 6)
    sprite('su615_06', 6)
    sprite('su615_07', 6)
    sprite('su615_08', 6)
    sprite('su615_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_RoundWinEnd():
    sprite('su615_03', 6)
    sprite('su615_02', 6)
    sprite('su615_01', 6)
    sprite('su615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_suvsvh_00():
    sprite('su615_00', 6)
    CameraControlEnable(1)
    sprite('su615_01', 6)
    sprite('su615_02', 6)
    sprite('su615_03', 6)
    label(0)
    sprite('su615_04', 6)
    sprite('su615_05', 6)
    sprite('su615_06', 6)
    sprite('su615_07', 6)
    sprite('su615_08', 6)
    sprite('su615_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsvh_01():
    sprite('su615_03', 6)
    CameraControlEnable(1)
    sprite('su615_02', 6)
    sprite('su615_01', 6)
    sprite('su615_00', 6)
    loopRest()
    label(0)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsvh_02():
    sprite('su610_00', 9)
    CameraControlEnable(1)
    sprite('su610_01', 6)
    sprite('su610_02', 3)
    CommonSE('005_swing_grap_2_0')
    label(0)
    sprite('su610_03', 8)
    sprite('su610_04', 8)
    sprite('su610_05', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsvh_03():
    sprite('su610_02', 3)
    CameraControlEnable(1)
    sprite('su610_01', 6)
    sprite('su610_00', 9)
    loopRest()
    label(0)
    sprite('su000_00', 7)
    sprite('su000_01', 7)
    sprite('su000_02', 7)
    sprite('su000_03', 7)
    sprite('su000_04', 7)
    sprite('su000_05', 7)
    sprite('su000_06', 7)
    sprite('su000_07', 7)
    sprite('su000_08', 7)
    sprite('su000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsvh_04():
    sprite('su300_00', 7)
    CameraControlEnable(1)
    sprite('su300_01', 7)
    sprite('su300_02', 7)
    sprite('su300_03', 32767)
    loopRest()


@State
def Act3Event_suvsvh_05():
    sprite('su300_04', 7)
    CameraControlEnable(1)
    sprite('su300_05', 7)
    sprite('su300_06', 7)
    sprite('su615_00', 6)
    sprite('su615_01', 6)
    sprite('su615_02', 6)
    sprite('su615_03', 6)
    label(0)
    sprite('su615_04', 6)
    sprite('su615_05', 6)
    sprite('su615_06', 6)
    sprite('su615_07', 6)
    sprite('su615_08', 6)
    sprite('su615_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsph_00():
    uponSendToLabel(32, 5)
    sprite('su333_00', 5)
    sprite('su333_01', 5)
    sprite('su333_02', 5)
    sprite('su333_02', 40)
    sprite('su333_02', 110)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_0')
    sprite('su333_02', 130)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_0')
    sprite('su333_02', 80)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_0')
    SetActionMark(4)
    label(1)
    sprite('su333_02', 10)
    ScreenShake(0, 1000)
    CommonSE('019_quake_0')
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1)
    SetActionMark(4)
    label(2)
    sprite('su333_02', 10)
    ScreenShake(0, 1000)
    CommonSE('019_quake_0')
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2)
    SetActionMark(4)
    label(3)
    sprite('su333_03', 10)
    ScreenShake(0, 4000)
    CommonSE('019_quake_0')
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(3)
    SetActionMark(13)
    label(4)
    sprite('su333_03', 10)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(4)
    label(5)
    sprite('su333_02', 3)
    clearUponHandler(32)
    callSubroutine('EmissionStart')
    Unknown30017(25)
    sprite('su214_03', 3)
    CommonSE('209_down_normal_0')
    sprite('su214_06', 3)
    sprite('su214_07', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('su214_08', 6)
    CreateObject('suef_214', 0)
    CreateParticle('suef_214b', 0)
    CreateObject('suef_214ground', 1)
    CreateObject('suef_214ground2', 2)
    CreateObject('suef_214ground2', 3)
    PrivateSE('suse_03')
    PrivateSE('suse_08')
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('su214_09', 6)
    CommonSE('019_cloth_a')
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('su214_10', 6)
    CommonSE('019_cloth_a')
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('su214_08', 6)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('su214_09', 6)
    ScreenShake(0, 60000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('su214_10', 6)
    sprite('su214_08', 6)
    sprite('su214_09', 6)
    sprite('su214_10', 6)
    sprite('su214_08', 6)
    sprite('su214_09', 6)
    sprite('su214_10', 6)
    sprite('su214_08', 6)
    sprite('su214_09', 6)
    sprite('su214_10', 6)
    sprite('su214_08', 6)
    sprite('su214_09', 6)
    sprite('su214_10', 6)
    sprite('su214_11', 6)
    Unknown30017(-21)
    sprite('su214_12', 6)
    sprite('su214_13', 6)
    loopRest()
    enterState('CmnActStand')
