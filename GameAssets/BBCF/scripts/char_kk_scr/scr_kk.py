@Subroutine
def PreInit():
    CharacterID('kk')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(10500)
    WalkFSpeed(4800)
    WalkBSpeed(4800)
    DashFInitialVelocity(18000)
    DashFAccel(400)
    DashFMaxVelocity(28000)
    JumpYVelocity(32000)
    SuperJumpYVelocity(42000)
    AirDashCount(1)
    AirDashBSpeed(22000)
    AirBDashDuration(22)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    if SLOT_116:
        Health(13500)
        DashFInitialVelocity(27000)
        DashFMaxVelocity(42000)
        AirDashCount(2)
        AirDashFSpeed(46500)
        AirFDashDuration(15)
        AirDashBSpeed(33000)
        AirBDashDuration(16)
        OverdriveDuration(780, 780, 780, 780, 780, 780, 780, 780, 780, 780)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    ResourceGauge(0, 1, 48, 1, 9, 9, -16711681, -16711681)
    NumberGauge(0, 1)
    ResourceGauge(1, 1, 46, 1, 1, 1, -65536, -65536)
    ResourceGaugeFlash(1, 1)
    DisableResourceGaugeBar(1, 1)
    ResourceGauge(2, 1, 47, 1, 1, 1, -65536, -65536)
    ResourceGaugeFlash(2, 1)
    DisableResourceGaugeBar(2, 1)
    ResourceGauge(3, 0, 48, 1, 240, 0, -1, -1)
    ResourceGaugeFlash(0, 1)
    CPUJumpPriority(500)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    Unknown15027(5000)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMaxChainRepeat(1)
    AirborneOpponentPriority(3500)
    SkillEstimateRange(-100000, 250000, -50000, 400000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    MoveLow()
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMaxChainRepeat(2)
    MoveMid()
    DamageStunPriority(1)
    MoveCancellableFrames(48, 50)
    SkillEstimateRange(50000, 350000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    MoveCancellableFrames(21, 23)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    SkillEstimateRange(150000, 350000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    AirborneOpponentPriority(100)
    SkillEstimateRange(0, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    GuardStunPriority(1)
    DamageStunPriority(500)
    MoveComboPriority(1500)
    MoveCancellableFrames(35, 38)
    SkillEstimateRange(250000, 600000, -100000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(-50000, 300000, -150000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    MoveCancellableFrames(28, 30)
    DamageStunPriority(3000)
    SkillEstimateRange(50000, 400000, -150000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    DamageStunPriority(100)
    SkillEstimateRange(200000, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    DamageStunPriority(100)
    SkillEstimateRange(100000, 500000, -250000, 250000, 400, 50)
    Move_EndRegister()
    Move_Register('StandDrive', 0x1)
    CallSkillConditions('FuncAtkDrive')
    Move_Condition(0x304d)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(300000, 1500000, -200000, 300000, 250, 10)
    Move_EndRegister()
    Move_Register('StandDrive_UP', INPUT_SPECIALMOVE)
    CallSkillConditions('FuncAtkDrive')
    Move_Condition(0x304d)
    Move_Condition(0x2000)
    Move_Input_(0x93)
    Move_Input_(INPUT_PRESS_D)
    StateCall('StandDrive')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('CrouchDrive', 0x1)
    CallSkillConditions('FuncAtkDrive')
    Move_Condition(0x304d)
    Move_Condition(0x2000)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(300000, 1500000, -200000, 300000, 250, 10)
    Move_EndRegister()
    Move_Register('AirDrive', 0x1)
    CallSkillConditions('FuncAtkDrive')
    Move_Condition(0x304d)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(0, 300000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('AtkDrive_2nd', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckAtkDrive_2ndAvailable')
    Move_Condition(0x304d)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AtkDrive_2ndAir', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckAtkDrive_2ndAvailable')
    Move_Condition(0x304d)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AtkDrive_2nd_ChainOnly', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckAtkDrive_2ndAvailable')
    Move_Condition(0x304d)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    CallFunction('Drive_2ndCall')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Drive_Stop', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckDrive_StopAvailable')
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Drive_StopAir', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckDrive_StopAvailable')
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Shot_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(300000, 600000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('Shot_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(600000, 800000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('Shot_C', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(600000, 1000000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AirShot_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 350000, -400000, -100000, 100, 10)
    Move_EndRegister()
    Move_Register('AirShot_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(800000, 1000000, -400000, -100000, 100, 10)
    Move_EndRegister()
    Move_Register('AirShot_C', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(1000000, 1200000, -400000, -100000, 100, 10)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 300000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    CPUUsable(0)
    PlayerUsable(0)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 300000, -200000, 200000, 200, 25)
    Move_EndRegister()
    Move_Register('SpinAssault', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    CallSkillConditions('Func_SpinAssault')
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(350000, 1000000, -800000, 800000, 10, 200)
    Move_EndRegister()
    Move_Register('Freeze_Shot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15027(5000)
    SkillEstimateRange(0, 350000, -200000, 200000, 150, 10)
    Move_EndRegister()
    Move_Register('Lightning_Shot_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304f)
    DamageStunPriority(3000)
    SkillEstimateRange(-100000, 300000, -200000, 1500000, 100, 0)
    Move_EndRegister()
    Move_Register('Lightning_Shot_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x304f)
    DamageStunPriority(3000)
    SkillEstimateRange(-100000, 400000, 100000, 1500000, 100, 0)
    Move_EndRegister()
    Move_Register('Warp', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    MoveComboPriority(0)
    OpponentAttackPriority(3000)
    SkillEstimateRange(0, 350000, -200000, 300000, 300, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_A', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304e)
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 350000, -200000, 600000, 250, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_B', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(700000, 1200000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_C', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x304e)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(1000000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateAirShot_A', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304e)
    SkillEstimateRange(1000000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateAirShot_B', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateAirShot_C', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateShotOD_A', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 350000, -200000, 600000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateShotOD_B', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateShotOD_C', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateAirShotOD_A', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    SkillEstimateRange(1000000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateAirShotOD_B', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateAirShotOD_C', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    Move_Condition(0x304e)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('UltimateBlackhole', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    GuardStunPriority(4000)
    DamageStunPriority(5000)
    SkillEstimateRange(800000, 1200000, -200000, 250000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateBlackhole_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    GuardStunPriority(4000)
    DamageStunPriority(5000)
    SkillEstimateRange(800000, 1200000, -200000, 250000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateLaser', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2003)
    Move_Input_(INPUT_64641236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(8000)
    GuardStunPriority(5000)
    SkillEstimateRange(500000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateLaser_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2003)
    Move_Input_(INPUT_64641236)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    OpponentAttackPriority(8000)
    GuardStunPriority(5000)
    SkillEstimateRange(500000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateAirLaser', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2003)
    Move_Input_(INPUT_64641236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(8000)
    GuardStunPriority(5000)
    SkillEstimateRange(150000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('UltimateAirLaser_OD', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2003)
    Move_Input_(INPUT_64641236)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    OpponentAttackPriority(8000)
    GuardStunPriority(5000)
    SkillEstimateRange(150000, 1500000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_D)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 5000, 50)
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
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk6A', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Assault_A', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Assault_A', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'SpinAssault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'UltimateShot_A', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'UltimateShotOD_A', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'SpinAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'Lightning_Shot_A', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'UltimateShot_A', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'UltimateShotOD_A', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2C', 'AirShot_A', 10000000)
    StylishModeSpecialButton('SpinAssault', 0x4, 0xea)
    StylishModeSpecialButton('Assault_A', 0x4, 0x79)
    StylishModeSpecialButton('UltimateShot_A', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateShotOD_A', 0x4, 0x5f)
    StylishModeSpecialButton('Freeze_Shot', 0x4, 0x45)
    StylishModeSpecialButton('AirShot_C', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAirShot_A', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAirShotOD_A', 0x4, 0x5f)
    StylishModeSpecialButton('AirShot_A', 0x4, 0x45)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6A', 3, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 1, 250000)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk6A', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk6B', 'Lightning_Shot_A', 12, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtkAIR2C', 0, 0)
    StylishModeCancels('ThrowExe', 'Assault_A', 0, 0)
    StylishModeCancels('ThrowExe', 'Freeze_Shot', 10, 300000)
    StylishModeCancels('BackThrowExe', 'UltimateLaser', 0, 0)
    StylishModeCancels('BackThrowExe', 'UltimateLaser_OD', 0, 0)
    StylishModeCancels('AirThrowExe', 'UltimateAirLaser', 0, 0)
    StylishModeCancels('AirThrowExe', 'UltimateAirLaser_OD', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 1, 300000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk2C', 'Freeze_Shot', 13, 0)
    StylishModeCancels('NmlAtk3C', 'Assault_A', 0, 0)
    StylishModeCancels('NmlAtk3C', 'Freeze_Shot', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 3, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR2C', 10, 300000)
    HitSprites(0, 'kk062_01')
    HitSprites(1, 'kk062_03')
    HitSprites(2, 'kk062_04')
    HitSprites(3, 'kk062_05')
    HitSprites(4, 'kk062_05')
    HitSprites(5, 'kk062_06')
    HitSprites(6, 'kk062_07')
    HitSprites(7, 'kk041_02')
    HitSprites(8, 'kk040_02')
    HitSprites(9, 'kk045_02')
    HitSprites(10, 'kk060_00')
    HitSprites(11, 'kk060_01')
    HitSprites(12, 'kk060_03')
    HitSprites(13, 'kk060_05')
    HitSprites(14, 'kk060_07')
    HitSprites(15, 'kk060_14')
    HitSprites(16, 'kk050_00')
    HitSprites(17, 'kk052_00')
    HitSprites(18, 'kk054_00')
    HitSprites(19, 'kk000_00')
    HitSprites(20, 'kk000_00')
    HitSprites(25, 'kk063_00')
    HitSprites(26, 'kk063_01')
    HitSprites(27, 'kk063_02')
    HitSprites(28, 'kk063_04')
    HitSprites(29, 'kk063_10')
    HitSprites(30, 'kk077_00')
    HitSprites(31, 'kk077_01')
    HitSprites(32, 'kk077_00ex01')
    HitSprites(33, 'kk077_01ex01')
    HitSprites(34, 'kk077_00ex02')
    HitSprites(35, 'kk077_01ex02')
    HitSprites(36, 'kk077_00ex03')
    HitSprites(37, 'kk077_01ex03')
    HitSprites(24, 'kk073_01')
    CommonVoicelines(0, 'kk000')
    CommonVoicelines(1, 'kk001')
    CommonVoicelines(2, 'kk002')
    CommonVoicelines(3, 'kk003')
    CommonVoicelines(4, 'kk004')
    CommonVoicelines(5, 'kk005')
    CommonVoicelines(6, 'kk006')
    CommonVoicelines(7, 'kk007')
    CommonVoicelines(8, 'kk008')
    CommonVoicelines(9, 'kk009')
    CommonVoicelines(10, 'kk010')
    CommonVoicelines(11, 'kk011')
    CommonVoicelines(12, 'kk012')
    CommonVoicelines(13, 'kk013')
    CommonVoicelines(14, 'kk014')
    CommonVoicelines(15, 'kk015')
    CommonVoicelines(16, 'kk016')
    CommonVoicelines(17, 'kk017')
    CommonVoicelines(18, 'kk018')
    CommonVoicelines(19, 'kk019')
    CommonVoicelines(20, 'kk020')
    CommonVoicelines(21, 'kk021')
    CommonVoicelines(22, 'kk022')
    CommonVoicelines(23, 'kk023')
    CommonVoicelines(24, 'kk024')
    CommonVoicelines(25, 'kk025')
    CommonVoicelines(26, 'kk026')
    CommonVoicelines(27, 'kk027')
    CommonVoicelines(28, 'kk028')
    CommonVoicelines(29, 'kk029')
    CommonVoicelines(30, 'kk030')
    CommonVoicelines(31, 'kk031')
    CommonVoicelines(32, 'kk032')
    CommonVoicelines(33, 'kk033')
    CommonVoicelines(34, 'kk034')
    CommonVoicelines(35, 'kk035')
    CommonVoicelines(36, 'kk036')
    CommonVoicelines(37, 'kk037')
    CommonVoicelines(38, 'kk038')
    CommonVoicelines(39, 'kk039')
    CommonVoicelines(40, 'kk040')
    CommonVoicelines(41, 'kk041')
    CommonVoicelines(42, 'kk042')
    CommonVoicelines(43, 'kk043')
    CommonVoicelines(44, 'kk044')
    CommonVoicelines(45, 'kk045')
    CommonVoicelines(46, 'kk046')
    CommonVoicelines(47, 'kk047')
    CommonVoicelines(48, 'kk048')
    CommonVoicelines(49, 'kk049')
    CommonVoicelines(50, 'kk050')
    CommonVoicelines(51, 'kk051')
    CommonVoicelines(52, 'kk052')
    CommonVoicelines(53, 'kk053')
    CommonVoicelines(54, 'kk100')
    CommonVoicelines(55, 'kk101')
    CommonVoicelines(56, 'kk102')
    CommonVoicelines(57, 'kk103')
    CommonVoicelines(58, 'kk104')
    CommonVoicelines(59, 'kk105')
    CommonVoicelines(60, 'kk106')
    CommonVoicelines(61, 'kk107')
    CommonVoicelines(62, 'kk108')
    CommonVoicelines(63, 'kk109')
    CommonVoicelines(64, 'kk150')
    CommonVoicelines(65, 'kk151')
    CommonVoicelines(66, 'kk152')
    CommonVoicelines(67, 'kk153')
    CommonVoicelines(68, 'kk154')
    CommonVoicelines(69, 'kk155')
    CommonVoicelines(70, 'kk156')
    CommonVoicelines(71, 'kk157')
    CommonVoicelines(72, 'kk158')
    CommonVoicelines(75, 'kk160')
    CommonVoicelines(73, 'kk402')
    CommonVoicelines(74, 'kk403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def MatchInit2():
    SLOT_64 = 600
    SLOT_65 = 100
    SLOT_66 = 100


@Subroutine
def FuncAtkDrive():
    SLOT_4 = 0
    SLOT_47 = 0
    if not SLOT_5 == 2:
        callSubroutine('FuncAtkDrive_Set')


@Subroutine
def FuncAtkDrive_Set():
    if CheckInput(0x1d):
        if not CurrentStateCheck('StandDrive'):
            if not CurrentStateCheck('CrouchDrive'):
                if not CurrentStateCheck('AirDrive'):
                    if CheckInput(0x37):
                        SLOT_59 = 1
                        SLOT_47 = SLOT_0
                    if CheckInput(0x44):
                        SLOT_59 = 2
                        SLOT_47 = SLOT_0
                    if CheckInput(0x51):
                        SLOT_59 = 3
                        SLOT_47 = SLOT_0
                    if CheckInput(0x5e):
                        SLOT_59 = 4
                        SLOT_47 = SLOT_0
                    if CheckInput(0x6b):
                        SLOT_59 = 5
                        SLOT_47 = SLOT_0
                    if CheckInput(0x78):
                        SLOT_59 = 6
                        SLOT_47 = SLOT_0
                    if CheckInput(0x85):
                        SLOT_59 = 7
                        SLOT_47 = SLOT_0
                    if CheckInput(0x92):
                        SLOT_59 = 8
                        SLOT_47 = SLOT_0
                    if CheckInput(0x9f):
                        SLOT_59 = 9
                        SLOT_47 = SLOT_0
    elif SLOT_113:
        if not CurrentStateCheck('StandDrive'):
            if not CurrentStateCheck('CrouchDrive'):
                if not CurrentStateCheck('AirDrive'):
                    if SLOT_IsAirborne:
                        Unknown61(0, 1, 0, 3, 0, 9999, 0, 9999, 0, 9999, 0,
                            9999)
                        SLOT_59 = SLOT_0
                        SLOT_47 = SLOT_0
                    else:
                        Unknown61(0, 4, 0, 6, 0, 9999, 0, 9999, 0, 9999, 0,
                            9999)
                        SLOT_59 = SLOT_0
                        SLOT_47 = SLOT_0


@Subroutine
def DriveSet():
    if SLOT_58:
        CreateObject('efkk_Drive_OD', -1)
    else:
        CreateObject('efkk_Drive', -1)
    RegisterObject(5, 1)
    SLOT_31 = SLOT_31 + -1
    if not SLOT_OverdriveTimer:
        SLOT_34 = 0
    if SLOT_59 == 1:
        ObjectUpon(5, 33)
    if SLOT_59 == 2:
        ObjectUpon(5, 34)
    if SLOT_59 == 3:
        ObjectUpon(5, 35)
    if SLOT_59 == 4:
        ObjectUpon(5, 36)
    if SLOT_59 == 5:
        pass
    if SLOT_59 == 6:
        ObjectUpon(5, 38)
    if SLOT_59 == 7:
        ObjectUpon(5, 39)
    if SLOT_59 == 8:
        ObjectUpon(5, 40)
    if SLOT_59 == 9:
        ObjectUpon(5, 41)


@Subroutine
def CheckAtkDrive_2ndAvailable():
    SLOT_47 = 0
    if SLOT_5 == 1:
        SLOT_47 = 1


@Subroutine
def CheckDrive_StopAvailable():
    SLOT_47 = 0
    if SLOT_5:
        if not SLOT_5 == 3:
            SLOT_47 = 1


@Subroutine
def Drive_2ndCall():
    SLOT_5 = 3


@Subroutine
def Delete_hole():
    DespawnEAEffect('efkk_202_hole')
    DespawnEAEffect('efkk_212_hole')
    DespawnEAEffect('efkk_212_hole_out')
    DespawnEAEffect('efkk_232_hole')
    DespawnEAEffect('efkk_232_hole_out')
    DespawnEAEffect('efkk_235_hole')
    DespawnEAEffect('efkk_252_hole')
    DespawnEAEffect('efkk_253_hole')
    DespawnEAEffect('efkk_340_hole')


@Subroutine
def Func_SpinAssault():
    if not SLOT_60:
        SLOT_47 = 1
    else:
        SLOT_47 = 0


@Subroutine
def OnFrameStep():
    if SLOT_32:
        ResourceBarIcon(1, 46)
    else:
        ResourceBarIcon(1, 49)
    if SLOT_33:
        ResourceBarIcon(2, 47)
    else:
        ResourceBarIcon(2, 50)
    if not SLOT_81:
        if not SLOT_5:
            if not SLOT_7:
                SLOT_63 = SLOT_63 + 1
                if SLOT_63 > 30:
                    if SLOT_34 < 240:
                        if SLOT_31 < 9:
                            if SLOT_OverdriveTimer:
                                SLOT_34 = SLOT_34 + 5
                            else:
                                SLOT_34 = SLOT_34 + 1
                    else:
                        SLOT_31 = SLOT_31 + 1
                        SLOT_34 = 0
        else:
            if SLOT_OverdriveTimer:
                if not SLOT_7:
                    if SLOT_31 < 9:
                        if SLOT_34 < 240:
                            if SLOT_OverdriveTimer:
                                SLOT_34 = SLOT_34 + 2
                        else:
                            SLOT_31 = SLOT_31 + 1
                            SLOT_34 = 0
            if SLOT_5 == 1:
                pass
            if SLOT_5 >= 2:
                pass
    if SLOT_21:
        if SLOT_116:
            HeatChange(3)

    def upon_53():
        DespawnEAEffect('efkk_fireball_Hontai')
        DespawnEAEffect('efkk_UltraSokidan_Hontai')
        DespawnEAEffect('efkk_UltraSokidan_Hontai_OD')
    if not SLOT_81:
        TrainingModeSLOT('TRI_KokonoeGravity', 2, 67)
        if SLOT_67:
            if not SLOT_5:
                if SLOT_InNeutral:
                    SLOT_31 = 1200


@Subroutine
def OnLanding():
    SLOT_60 = 0


@Subroutine
def OnDamage():
    if SLOT_IsGrounded:
        SLOT_60 = 0


@State
def CmnActStand():
    label(0)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('kk001_00', 6)
    SLOT_88 = 960
    Voiceline('kk000')
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 6)
    sprite('kk001_06', 6)
    sprite('kk001_07', 6)
    sprite('kk001_08', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('kk003_00', 3)
    SmartVoiceline('kk001')
    sprite('kk003_01', 3)
    sprite('kk003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('kk010_00', 4)
    sprite('kk010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('kk010_02', 6)
    sprite('kk010_03', 6)
    sprite('kk010_04', 6)
    sprite('kk010_05', 6)
    sprite('kk010_06', 6)
    sprite('kk010_07', 6)
    sprite('kk010_08', 6)
    sprite('kk010_09', 6)
    sprite('kk010_10', 6)
    sprite('kk010_11', 6)
    sprite('kk010_12', 6)
    sprite('kk010_13', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('kk013_00', 3)
    sprite('kk013_01', 3)
    sprite('kk013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('kk010_01', 4)
    sprite('kk010_00', 4)


@State
def CmnActJumpPre():
    sprite('kk023_00', 2)
    sprite('kk023_01', 2)
    if SLOT_IsMovingForward:
        RandomVoiceline('kk003', 75, '', 100, '', 100, '', 100)
    else:
        RandomVoiceline('kk002', 75, '', 100, '', 100, '', 100)


@State
def CmnActJumpUpper():
    callSubroutine('Delete_hole')
    label(0)
    sprite('kk020_00', 4)
    sprite('kk020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('kk020_02', 3)
    sprite('kk020_03', 3)
    sprite('kk020_04', 3)


@State
def CmnActJumpDown():
    sprite('kk020_05', 3)
    sprite('kk020_06', 3)
    label(0)
    sprite('kk020_07', 4)
    sprite('kk020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('kk024_00', 3)
    sprite('kk024_01', 3)
    sprite('kk024_02', 3)
    sprite('kk024_03', 3)
    sprite('kk024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('kk024_00', 2)
    sprite('kk024_01', 2)
    sprite('kk024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('kk024_03', 3)
    sprite('kk024_04', 3)


@State
def CmnActFWalk():
    sprite('kk030_00', 7)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(0)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('kk031_00', 7)
    sprite('kk031_01', 7)
    sprite('kk031_02', 7)
    sprite('kk031_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk031_04', 7)
    sprite('kk031_05', 7)
    sprite('kk031_06', 7)
    sprite('kk031_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk031_08', 7)
    sprite('kk031_09', 7)
    sprite('kk031_10', 7)
    label(0)
    sprite('kk031_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk031_12', 7)
    sprite('kk031_13', 7)
    sprite('kk031_14', 7)
    sprite('kk031_15', 7)
    sprite('kk031_16', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk031_17', 7)
    sprite('kk031_18', 7)
    sprite('kk031_19', 7)
    sprite('kk031_20', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('kk032_00', 2)
    label(0)
    sprite('kk032_01', 3)
    CreateParticle('kkef_dash', 0)
    CreateParticle('kkef_dash_smoke', 0)
    PrivateSE('kkse_28')
    sprite('kk032_02', 3)
    PrivateSE('kkse_28')
    CreateParticle('kkef_dash_smoke', 0)
    sprite('kk032_03', 3)
    CreateParticle('kkef_dash_smoke', 0)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('kk032_05', 3)
    sprite('kk032_06', 3)
    sprite('kk032_07', 3)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('kk033_00', 1)
    sprite('kk033_01', 2)
    physicsXImpulse(-19000)
    physicsYImpulse(7300)
    setGravity(1550)
    JumpSoundEffects()
    sprite('kk033_02', 3)
    SmartVoiceline('kk005')
    sprite('kk033_03', 1)
    sprite('kk033_03', 2)
    setInvincible(0)
    loopRest()
    label(0)
    sprite('kk033_02', 3)
    sprite('kk033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('kk033_04', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('kk033_05', 2)
    sprite('kk033_06', 2)
    sprite('kk033_07', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('kk035_00', 3)
    label(0)
    sprite('kk035_01', 3)
    CreateObject('efkk_airdash', 0)
    CreateObject('efkk_airdash_back', 1)
    CreateParticle('kkef_airdash_smoke', 0)
    sprite('kk035_02', 3)
    SmartVoiceline('kk004')
    CreateObject('efkk_airdash', 0)
    CreateObject('efkk_airdash_back', 1)
    CreateParticle('kkef_airdash_smoke', 0)
    sprite('kk035_03', 3)
    CreateObject('efkk_airdash', 0)
    CreateObject('efkk_airdash_back', 1)
    CreateParticle('kkef_airdash_smoke', 0)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('kk036_00', 3)
    label(0)
    sprite('kk036_01', 3)
    CreateObject('efkk_airbackdash', 0)
    CreateObject('efkk_airbackdash_back', 1)
    CreateParticle('kkef_airbackdash_smoke', 0)
    sprite('kk036_02', 3)
    CreateObject('efkk_airbackdash', 0)
    CreateObject('efkk_airbackdash_back', 1)
    CreateParticle('kkef_airbackdash_smoke', 0)
    sprite('kk036_03', 3)
    CreateObject('efkk_airbackdash', 0)
    CreateObject('efkk_airbackdash_back', 1)
    CreateParticle('kkef_airbackdash_smoke', 0)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('kk050_00', 1)
    sprite('kk050_01', 1)
    sprite('kk050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('kk050_01', 1)
    sprite('kk050_02', 1)
    sprite('kk050_01', 2)
    sprite('kk050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('kk050_02', 1)
    sprite('kk050_03', 1)
    sprite('kk050_02', 2)
    sprite('kk050_01', 2)
    sprite('kk050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('kk050_03', 1)
    sprite('kk050_04', 1)
    sprite('kk050_03', 2)
    sprite('kk050_02', 2)
    sprite('kk050_01', 2)
    sprite('kk050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('kk050_04', 1)
    sprite('kk050_04', 1)
    sprite('kk050_04', 2)
    sprite('kk050_03', 2)
    sprite('kk050_02', 2)
    sprite('kk050_01', 2)
    sprite('kk050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('kk052_00', 1)
    sprite('kk052_01', 1)
    sprite('kk052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('kk052_01', 1)
    sprite('kk052_02', 1)
    sprite('kk052_01', 2)
    sprite('kk052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('kk052_02', 1)
    sprite('kk052_03', 1)
    sprite('kk052_02', 2)
    sprite('kk052_01', 2)
    sprite('kk052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('kk052_03', 1)
    sprite('kk052_04', 1)
    sprite('kk052_03', 2)
    sprite('kk052_02', 2)
    sprite('kk052_01', 2)
    sprite('kk052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('kk052_04', 1)
    sprite('kk052_04', 1)
    sprite('kk052_04', 2)
    sprite('kk052_03', 2)
    sprite('kk052_02', 2)
    sprite('kk052_01', 2)
    sprite('kk052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('kk054_00', 1)
    sprite('kk054_01', 1)
    sprite('kk054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('kk054_01', 1)
    sprite('kk054_02', 1)
    sprite('kk054_01', 2)
    sprite('kk054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('kk054_02', 1)
    sprite('kk054_03', 1)
    sprite('kk054_02', 2)
    sprite('kk054_01', 2)
    sprite('kk054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('kk054_03', 1)
    sprite('kk054_04', 1)
    sprite('kk054_03', 2)
    sprite('kk054_02', 2)
    sprite('kk054_01', 2)
    sprite('kk054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('kk054_04', 1)
    sprite('kk054_04', 1)
    sprite('kk054_04', 2)
    sprite('kk054_03', 2)
    sprite('kk054_02', 2)
    sprite('kk054_01', 2)
    sprite('kk054_00', 2)


@State
def CmnActBDownUpper():
    sprite('kk060_00', 4)
    label(0)
    sprite('kk060_01', 4)
    sprite('kk060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('kk060_03', 4)


@State
def CmnActBDownDown():
    sprite('kk060_04', 4)
    label(0)
    sprite('kk060_05', 4)
    sprite('kk060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('kk060_07', 2)
    sprite('kk060_08', 2)


@State
def CmnActBDownBound():
    sprite('kk060_09', 3)
    sprite('kk060_10', 3)
    sprite('kk060_11', 3)
    sprite('kk060_12', 3)
    sprite('kk060_13', 3)


@State
def CmnActBDownLoop():
    sprite('kk060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('kk061_00', 3)
    sprite('kk061_01', 3)
    sprite('kk061_02', 3)
    sprite('kk061_03', 3)
    sprite('kk061_04', 3)
    sprite('kk061_05', 3)
    sprite('kk061_06', 2)
    sprite('kk061_07', 2)
    sprite('kk061_08', 2)
    sprite('kk061_09', 2)
    sprite('kk061_10', 2)


@State
def CmnActFDownUpper():
    sprite('kk063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('kk063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('kk063_02', 3)
    sprite('kk063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('kk063_04', 3)
    sprite('kk063_05', 3)
    sprite('kk063_06', 2)


@State
def CmnActFDownBound():
    sprite('kk063_07', 2)
    sprite('kk063_08', 3)
    sprite('kk063_09', 3)
    sprite('kk063_10', 3)


@State
def CmnActFDownLoop():
    sprite('kk063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('kk064_00', 2)
    sprite('kk064_01', 2)
    sprite('kk064_02', 2)
    sprite('kk064_03', 2)
    sprite('kk064_04', 2)
    sprite('kk064_05', 2)
    sprite('kk064_06', 2)
    sprite('kk064_07', 2)
    sprite('kk064_08', 2)
    sprite('kk064_09', 2)
    sprite('kk064_10', 2)
    sprite('kk064_11', 2)


@State
def CmnActVDownUpper():
    sprite('kk062_00', 3)
    label(0)
    sprite('kk062_01', 3)
    sprite('kk062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('kk062_03', 3)
    sprite('kk062_04', 3)


@State
def CmnActVDownDown():
    sprite('kk062_05', 3)
    sprite('kk062_06', 3)
    label(0)
    sprite('kk062_07', 3)
    sprite('kk062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('kk062_09', 2)
    sprite('kk062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('kk062_09', 2)
    sprite('kk062_10', 2)


@State
def CmnActBlowoff():
    sprite('kk072_00', 3)
    sprite('kk072_01', 3)
    sprite('kk072_02', 3)
    label(0)
    sprite('kk072_01', 3)
    sprite('kk072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('kk074_00', 3)
    sprite('kk074_01', 3)
    sprite('kk074_02', 3)
    sprite('kk074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('kk082_00', 2)
    sprite('kk082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('kk062_01', 1)


@State
def CmnActWallBound():
    sprite('kk073_00', 3)
    sprite('kk073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('kk073_02', 3)
    label(0)
    sprite('kk073_03', 3)
    sprite('kk073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('kk070_00', 2)
    sprite('kk070_01', 2)
    sprite('kk070_02', 2)
    sprite('kk070_03', 2)


@State
def CmnActStaggerDown():
    sprite('kk070_04', 4)
    sprite('kk070_05', 4)
    sprite('kk070_06', 4)
    sprite('kk070_07', 4)
    sprite('kk070_08', 4)
    sprite('kk070_09', 3)


@State
def CmnActUkemiStagger():
    sprite('kk070_10', 2)
    sprite('kk070_11', 2)
    sprite('kk070_12', 2)
    sprite('kk070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('kk113_00', 3)
    sprite('kk113_01', 3)
    sprite('kk113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('kk113_00', 3)
    sprite('kk113_01', 3)
    sprite('kk113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('kk113_00', 3)
    sprite('kk113_01', 3)
    sprite('kk113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('kk110_00', 2)
    sprite('kk110_01', 2)
    sprite('kk110_02', 2)
    sprite('kk110_03', 2)
    sprite('kk110_04', 2)
    sprite('kk110_05', 2)
    sprite('kk110_06', 2)
    sprite('kk110_07', 200)
    sprite('kk110_08', 2)
    sprite('kk110_09', 2)
    sprite('kk110_10', 1)
    sprite('kk110_11', 1)


@State
def CmnActUkemiLandB():
    sprite('kk111_00', 3)
    sprite('kk111_01', 3)
    sprite('kk111_02', 3)
    sprite('kk111_03', 3)
    sprite('kk111_04', 3)
    sprite('kk111_05', 3)
    sprite('kk111_06', 3)
    sprite('kk111_07', 200)
    sprite('kk111_08', 2)
    sprite('kk111_09', 2)
    sprite('kk111_10', 1)
    sprite('kk111_11', 1)


@State
def CmnActUkemiLandN():
    sprite('kk112_00', 2)
    sprite('kk112_01', 2)
    sprite('kk112_02', 2)
    sprite('kk112_03', 2)
    sprite('kk112_04', 2)
    sprite('kk112_05', 2)
    sprite('kk112_06', 2)
    sprite('kk112_07', 2)
    sprite('kk112_08', 2)
    sprite('kk112_09', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('kk024_00', 3)
    sprite('kk024_01', 3)
    sprite('kk024_02', 3)
    sprite('kk024_03', 3)
    sprite('kk024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('kk040_00', 3)
    sprite('kk040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('kk040_02', 3)
    sprite('kk040_03', 3)
    sprite('kk040_04', 3)
    sprite('kk040_05', 3)
    sprite('kk040_06', 3)
    sprite('kk040_07', 3)
    sprite('kk040_08', 3)
    sprite('kk040_09', 3)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('kk040_01', 3)
    sprite('kk040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('kk040_10', 3)


@State
def CmnActMidHeavyGuardEnd():
    sprite('kk040_01', 3)
    sprite('kk040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('kk041_00', 3)
    sprite('kk041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('kk041_02', 3)
    sprite('kk041_03', 3)
    sprite('kk041_04', 3)
    sprite('kk041_05', 3)
    sprite('kk041_06', 3)
    sprite('kk041_07', 3)
    sprite('kk041_08', 3)
    sprite('kk041_09', 3)
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('kk041_01', 3)
    sprite('kk041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('kk041_10', 3)


@State
def CmnActHighHeavyGuardEnd():
    sprite('kk041_01', 3)
    sprite('kk041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('kk043_00', 3)
    sprite('kk043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('kk043_02', 3)
    sprite('kk043_03', 3)
    sprite('kk043_04', 3)
    sprite('kk043_05', 3)
    sprite('kk043_06', 3)
    sprite('kk043_07', 3)
    sprite('kk043_08', 3)
    sprite('kk043_09', 3)
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('kk043_01', 3)
    sprite('kk043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('kk043_10', 3)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('kk043_01', 3)
    sprite('kk043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('kk045_00', 3)
    sprite('kk045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('kk045_02', 3)
    sprite('kk045_03', 3)
    sprite('kk045_04', 3)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('kk045_01', 3)
    sprite('kk045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('kk045_05', 3)


@State
def CmnActAirHeavyGuardEnd():
    sprite('kk045_01', 3)
    sprite('kk045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('kk090_00', 2)
    sprite('kk090_01', 2)
    sprite('kk090_02', 1)
    SetCommonActionMark(1)
    sprite('kk090_03', 6)
    sprite('kk090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('kk091_00', 2)
    sprite('kk091_01', 2)
    sprite('kk091_02', 1)
    SetCommonActionMark(1)
    sprite('kk091_03', 6)
    sprite('kk091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('kk092_00', 2)
    sprite('kk092_01', 2)
    sprite('kk092_02', 1)
    SetCommonActionMark(1)
    sprite('kk092_03', 6)
    sprite('kk092_04', 6)


@State
def CmnActAirTurn():
    sprite('kk025_00', 4)
    sprite('kk025_01', 4)
    sprite('kk025_02', 4)


@State
def CmnActLockWait():
    sprite('kk040_02', 3)
    sprite('kk040_01', 3)
    sprite('kk040_00', 3)


@State
def CmnActLockReject():
    sprite('kk312_00', 2)
    sprite('kk312_01', 2)
    sprite('kk312_02', 2)
    sprite('kk312_03', 8)
    sprite('kk312_04', 4)
    sprite('kk312_05', 3)
    sprite('kk312_06', 2)
    sprite('kk312_07', 2)
    sprite('kk312_08', 2)


@State
def CmnActAirLockWait():
    sprite('kk045_02', 1)
    sprite('kk045_01', 3)
    sprite('kk045_00', 3)


@State
def CmnActAirLockReject():
    sprite('kk322_00', 2)
    sprite('kk322_01', 2)
    sprite('kk322_02', 8)
    sprite('kk322_03', 2)
    sprite('kk322_04', 3)
    sprite('kk322_05', 3)
    sprite('kk322_06', 3)
    sprite('kk322_07', 3)
    sprite('kk322_08', 3)


@State
def CmnActLandSpin():
    sprite('kk071_00', 4)
    sprite('kk071_01', 4)
    label(0)
    sprite('kk071_02', 2)
    sprite('kk071_03', 2)
    sprite('kk071_04', 2)
    sprite('kk071_05', 2)
    sprite('kk071_06', 2)
    sprite('kk071_07', 2)
    sprite('kk071_08', 2)
    sprite('kk071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('kk071_10', 6)
    sprite('kk071_11', 5)
    sprite('kk071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('kk071_02', 2)
    sprite('kk071_03', 2)
    sprite('kk071_04', 2)
    sprite('kk071_05', 2)
    sprite('kk071_06', 2)
    sprite('kk071_07', 2)
    sprite('kk071_08', 2)
    sprite('kk071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('kk077_00', 2)
    sprite('kk077_01', 2)
    sprite('kk077_00ex01', 2)
    sprite('kk077_01ex01', 2)
    sprite('kk077_00ex02', 2)
    sprite('kk077_01ex02', 2)
    sprite('kk077_00ex03', 2)
    sprite('kk077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('kk077_02', 4)
    label(0)
    sprite('kk077_03', 3)
    sprite('kk077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('kk077_05', 5)
    sprite('kk077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('kk060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('kk060_11', 4)
    sprite('kk060_13', 5)


@State
def CmnActBurstBegin():
    sprite('kk331_00', 2)
    sprite('kk331_01', 2)
    label(0)
    sprite('kk331_02', 3)
    sprite('kk331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('kk331_04', 2)
    sprite('kk331_05', 2)
    label(0)
    sprite('kk331_06', 3)
    sprite('kk331_07', 3)
    sprite('kk331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('kk331_09', 3)
    sprite('kk331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('kk331_11', 2)
    sprite('kk331_12', 2)
    label(0)
    sprite('kk331_02', 3)
    sprite('kk331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('kk331_04', 2)
    sprite('kk331_05', 2)
    label(0)
    sprite('kk331_06', 2)
    sprite('kk331_07', 2)
    sprite('kk331_08', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('kk331_13', 4)
    sprite('kk331_14', 4)
    sprite('kk020_05', 3)
    sprite('kk020_06', 3)
    label(0)
    sprite('kk020_07', 4)
    sprite('kk020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('kk333_00', 3)
    sprite('kk333_01', 3)
    sprite('kk333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('kk333_03', 32767)
    CreateObject('EMB_KK_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('kk333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('kk333_05', 3)
    sprite('kk333_06', 3)
    sprite('kk333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('kk333_08', 6)
    sprite('kk333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('kk333_10', 3)
    sprite('kk333_11', 3)
    sprite('kk333_12', 3)
    CharacterFlash(16639, 20, 1)
    sprite('kk333_13', 32767)
    CreateObject('EMB_KK_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('kk333_14', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('kk333_05', 3)
    sprite('kk333_06', 3)
    sprite('kk333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('kk333_15', 6)
    sprite('kk333_16', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        HitAirUnblockable(0)
        StarterRating(2)
        AirPushbackY(20000)
        PushbackX(12000)
        WhiffCancel('NmlAtk5A')
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
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk200_00', 2)
    PerInertia(60)
    sprite('kk200_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('kk200_02', 1)
    sprite('kk200_03', 3)
    sprite('kk200_04', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('kk200_02', 3)
    sprite('kk200_01', 3)
    sprite('kk200_00', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        PushbackX(15300)
        AirPushbackX(3000)
        AirPushbackY(-15000)
        GroundBounce(1)
        UsePunchHitspark(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk201_00', 4)
    sprite('kk201_01', 1)
    SetInertia(0)
    physicsXImpulse(26000)
    sprite('kk201_02', 1)
    sprite('kk201_03', 1)
    RandomCommonVoiceline(1)
    sprite('kk201_04', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('kk201_05', 3)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(20)
    sprite('kk201_06', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    EndMomentum(1)
    sprite('kk201_07', 4)
    sprite('kk201_08', 4)
    sprite('kk201_09', 4)
    sprite('kk201_10', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileLevel(1)
        Damage(800)
        Hitstop(7)
        AirHitstunAnimation(17)
        AirUntechableTime(36)
        AirHitstunAfterWallbounce(30)
        AirPushbackX(28000)
        AirPushbackY(8000)
        CHGroundedHitstunAnimation(2)
        CHWallbounce(1)
        CHAirPushbackY(12000)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        callSubroutine('Delete_hole')
        StayAfterMovement(1, 0)
    sprite('kk202_00', 2)
    CreateObject('efkk_202_hole', -1)
    sprite('kk202_01', 2)
    sprite('kk202_02', 2)
    sprite('kk202_03', 3)
    CommonSE('004_swing_grap_1_2')
    RandomCommonVoiceline(2)
    sprite('kk202_04', 2)
    sprite('kk202_05', 2)
    CreateObject('efkk_202_smoke', 0)
    PrivateSE('kkse_23')
    StartMultihit()
    sprite('kk202_06', 2)
    CreateObject('efkk202_BLT', 0)
    sprite('kk202_06', 2)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('kk202_07', 4)
    sprite('kk202_08', 4)
    sprite('kk202_09', 4)
    CreateObject('efkk_202_weapon', -1)
    sprite('kk202_10', 3)
    sprite('kk202_11', 3)
    sprite('kk202_12', 3)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        HitAirUnblockable(0)
        PushbackX(12000)
        StarterRating(2)
        UsePunchHitspark(1)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk230_00', 2)
    PerInertia(60)
    sprite('kk230_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('kk230_02', 2)
    StartMultihit()
    sprite('kk230_03', 3)
    sprite('kk230_04', 4)
    NoAttackDuringAction(1)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('kk230_05', 4)
    sprite('kk230_06', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(400)
        Hitstop(9)
        AttackP1(90)
        AirPushbackY(6000)
        AirPushbackX(1000)
        HitLow(2)
        UsePunchHitspark(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        callSubroutine('Delete_hole')
    sprite('kk231_00', 2)
    sprite('kk231_01', 2)
    sprite('kk231_02', 3)
    sprite('kk231_03', 2)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_1')
    sprite('kk231_04', 3)
    sprite('kk231_05', 3)
    sprite('kk231_06', 3)
    CommonSE('008_swing_pole_1')
    sprite('kk231_07', 3)
    RefreshMultihit()
    AirPushbackY(13000)
    ResetPushback()
    sprite('kk231_08', 2)
    Recovery()
    Unknown2063()
    sprite('kk231_09', 2)
    sprite('kk231_10', 3)
    sprite('kk231_11', 3)
    sprite('kk231_12', 2)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1080)
        AttackP2(82)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(28000)
        AirUntechableTime(33)
        Hitstun(20)
        Hitstop(15)
        PushbackX(24800)
        FatalCounter(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            ScreenShake(4000, 1000)
            CommonSE('016_explode_1')
            CommonSE('016_explode_1')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        HitJumpCancel(1)
        callSubroutine('Delete_hole')
    sprite('kk232_00', 3)
    sprite('kk232_00', 2)
    CreateObject('efkk_232_hole', -1)
    sprite('kk232_01', 3)
    sprite('kk232_02', 3)
    sprite('kk232_03', 3)
    sprite('kk232_04', 3)
    RandomCommonVoiceline(2)
    sprite('kk232_05', 1)
    CommonSE('005_swing_grap_2_1')
    PrivateSE('kkse_22')
    sprite('kk232_06', 3)
    CreateObject('efkk_232_burner', -1)
    sprite('kk232_07', 3)
    CreateObject('efkk_232_hole_out', -1)
    Recovery()
    Unknown2063()
    sprite('kk232_08', 3)
    sprite('kk232_09', 3)
    sprite('kk232_10', 2)
    sprite('kk232_11', 2)
    sprite('kk232_12', 2)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(460)
        AttackP1(90)
        AttackP2(89)
        HitLow(2)
        AirHitstunAnimation(11)
        PushbackX(-8000)
        Hitstun(10)
        AirUntechableTime(34)
        AirPushbackX(-8000)
        AirPushbackY(18000)
        CHHardKnockdown(10)
        Hitstop(6)
        EnemyHitstopAddition(7, 7, 9)
        if not SLOT_94:
            SpecialCancelOnHit(1)
            HitOrBlockCancel('StandDrive')
            HitOrBlockCancel('CrouchDrive')
        if SLOT_94:
            SpecialCancelOnHit(0)
            SpecialCancel(0)
    sprite('kk235_00', 3)
    sprite('kk235_01', 2)
    CreateObject('efkk_235_hole', -1)
    sprite('kk235_02', 2)
    sprite('kk235_03', 2)
    PrivateSE('kkse_01')
    sprite('kk235_04', 4)
    sprite('kk235_05', 3)
    CommonSE('010_swing_sword_0')
    CreateParticle('kkef_235_2', 0)
    sprite('kk235_06', 2)
    CreateParticle('kkef_235', 0)
    sprite('kk235_07', 2)
    sprite('kk235_08', 2)
    RandomCommonVoiceline(2)
    sprite('kk235_09', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    HitLow(0)
    Hitstop(11)
    EnemyHitstopAddition(0, 0, 2)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SpecialCancel(1)
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk235_10', 3)
    Recovery()
    Unknown2063()
    sprite('kk235_11', 3)
    sprite('kk235_12', 3)
    sprite('kk235_13', 2)
    sprite('kk235_14', 2)
    sprite('kk235_15', 2)
    CreateObject('efkk_235_weapon', -1)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(660)
        AttackP1(90)
        CHGroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        HitAirUnblockable(3)
        AirPushbackX(3000)
        AirPushbackY(32000)
        AirUntechableTime(24)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        HitOrBlockJumpCancel(1)
        StayAfterMovement(1, 0)
        callSubroutine('Delete_hole')
    sprite('kk210_00', 1)
    sprite('kk210_01', 2)
    sprite('kk210_02', 3)
    SetInertia(6000)
    sprite('kk210_02ex01', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('kk210_02ex02', 3)

    def upon_RELEASE_A():
        sendToLabel(0)
    if SLOT_94:
        sendToLabel(0)
    sprite('kk210_02', 3)
    sprite('kk210_02ex01', 3)
    sprite('kk210_02ex02', 1)
    sprite('kk210_02ex02', 1)
    Damage(770)
    BonusProration(110)
    GroundedHitstunAnimation(18)
    CHGroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    Hitstop(16)
    AirUntechableTime(40)
    GotoState('NmlAtk6A_Hold')
    label(0)
    sprite('kk210_03', 1)
    SmartVoiceline('kk109')
    clearUponHandler(RELEASE_A)
    sprite('kk210_04', 1)
    CommonSE('004_swing_grap_1_0')
    PerInertia(30)
    sprite('kk210_05', 4)
    CreateObject('efkk_210', 0)
    XImpulseAcceleration(0)
    sprite('kk210_06', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('kk210_07', 3)
    sprite('kk210_08', 3)
    sprite('kk210_09', 3)
    sprite('kk210_10', 3)
    sprite('kk210_11', 3)
    sprite('kk210_12', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(500)
        AttackP1(90)
        StarterRating(2)
        AirUntechableTime(35)
        AirPushbackY(-40000)
        PushbackX(12000)
        GroundBounce(1)
        BouncePercentage(50)
        HitOverhead(2)
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk211_00', 3)
    sprite('kk211_01', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('kk211_02', 3)
    sprite('kk211_03', 2)
    CommonSE('003_swing_grap_0_2')
    sprite('kk211_03', 1)

    def upon_RELEASE_B():
        sendToLabel(10)
        clearUponHandler(RELEASE_B)
    sprite('kk211_01', 3)
    sprite('kk211_02', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('kk211_03', 3)
    sprite('kk211_01', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('kk211_02', 3)
    sprite('kk211_03', 3)
    CommonSE('003_swing_grap_0_2')
    loopRest()
    enterState('NmlAtk6B_Hold')
    TurnLimitByInitialize(1)
    label(10)
    sprite('kk211_04', 3)
    sprite('kk211_05', 3)
    sprite('kk211_06', 2)
    sprite('kk211_07', 2)
    sprite('kk211_08', 2)
    RandomCommonVoiceline(0)
    CommonSE('008_swing_pole_1')
    sprite('kk211_09', 2)
    sprite('kk211_10', 3)
    sprite('kk211_11', 4)
    physicsXImpulse(16000)
    physicsYImpulse(10000)
    setGravity(4000)
    SpecialCancel(0)
    sprite('kk211_11', 32767)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_1')
    uponSendToLabel(LANDING, 11)
    label(11)
    sprite('kk211_12', 2)
    XImpulseAcceleration(30)
    RefreshMultihit()
    GroundedHitstunAnimation(3)

    def upon_OPPONENT_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        SpecialCancel(1)
    sprite('kk211_13', 4)
    XImpulseAcceleration(50)
    Recovery()
    Unknown2063()
    sprite('kk211_14', 4)
    XImpulseAcceleration(50)
    sprite('kk211_15', 4)
    XImpulseAcceleration(0)
    sprite('kk211_16', 4)
    sprite('kk211_17', 4)
    sprite('kk211_18', 3)
    sprite('kk211_19', 3)


@State
def NmlAtk6B_Hold():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(550)
        AttackP1(80)
        BonusProration(110)
        AirUntechableTime(42)
        AirPushbackY(-40000)
        PushbackX(12000)
        HardKnockdown(1)
        HitOverhead(2)
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk211_04', 3)
    sprite('kk211_05', 3)
    sprite('kk211_06', 2)
    sprite('kk211_07', 2)
    sprite('kk211_08', 2)
    RandomCommonVoiceline(0)
    CommonSE('008_swing_pole_1')
    sprite('kk211_09', 2)
    sprite('kk211_10', 3)
    sprite('kk211_11', 4)
    physicsXImpulse(16000)
    physicsYImpulse(18000)
    setGravity(4000)
    SpecialCancel(0)
    sprite('kk211_11', 32767)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_1')
    uponSendToLabel(LANDING, 1)
    label(1)
    sprite('kk211_12', 2)
    XImpulseAcceleration(30)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    GroundBounce(1)
    BouncePercentage(60)
    HardKnockdown(-1)
    PushbackX(24000)

    def upon_OPPONENT_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        SpecialCancel(1)
    sprite('kk211_13', 2)
    XImpulseAcceleration(50)
    Recovery()
    Unknown2063()
    sprite('kk211_14', 2)
    XImpulseAcceleration(50)
    sprite('kk211_15', 2)
    XImpulseAcceleration(0)
    sprite('kk211_16', 2)
    sprite('kk211_17', 2)
    sprite('kk211_18', 2)
    sprite('kk211_19', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1250)
        AttackP1(90)
        AttackP2(82)
        AirUntechableTime(40)
        Hitstop(15)
        AirPushbackY(30000)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        MoveAttributes(1, 0, 0, 0, 0)
        HitAirUnblockable(3)
        FatalCounter(1)
        HitAirUnblockable(0)
        uponSendToLabel(LANDING, 0)
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            ScreenShake(1000, 4000)
            CommonSE('016_explode_1')
            CommonSE('016_explode_1')
            HitOrBlockCancel('AirDrive')
        callSubroutine('Delete_hole')
    sprite('kk212_00', 3)
    CreateObject('efkk_212_hole', -1)
    sprite('kk212_01', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('kk212_02', 3)
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    setGravity(1600)
    sprite('kk212_03', 4)
    XImpulseAcceleration(200)
    sprite('kk212_04', 4)
    CreateObject('efkk_212_burner', -1)
    XImpulseAcceleration(200)
    sprite('kk212_05', 4)
    RandomCommonVoiceline(2)
    PrivateSE('kkse_22')
    CommonSE('005_swing_grap_2_1')
    XImpulseAcceleration(200)
    YAccel(150)
    sprite('kk212_06', 3)
    XImpulseAcceleration(30)
    YAccel(-200)
    sprite('kk212_07', 3)
    setInvincible(0)
    XImpulseAcceleration(80)
    YAccel(50)
    Recovery()
    Unknown2063()
    sprite('kk212_08', 3)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('kk212_09', 3)
    XImpulseAcceleration(80)
    label(1)
    sprite('kk212_10', 2)
    sprite('kk212_11', 2)
    gotoLabel(1)
    label(0)
    sprite('kk212_12', 2)
    CreateObject('efkk_212_hole_out', -1)
    EndMomentum(1)
    sprite('kk212_13', 2)
    sprite('kk212_14', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(220)
        Hitstop(5)
        AttackP1(80)
        SingleProration(1)
        StarterRating(2)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_52 = 1
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        HitOrBlockJumpCancel(1)

        def upon_EVERY_FRAME():
            if SLOT_52:
                HitOverhead(0)
                Damage(110)
    sprite('kk250_00', 2)
    sprite('kk250_01', 3)
    SmartVoiceline('kk108')
    sprite('kk250_02', 1)
    StartMultihit()
    sprite('kk250_02', 3)
    CommonSE('003_swing_grap_0_0')
    RefreshMultihit()
    sprite('kk250_03', 3)
    RefreshMultihit()
    sprite('kk250_04', 3)
    RefreshMultihit()
    sprite('kk250_02', 3)
    CommonSE('003_swing_grap_0_0')
    RefreshMultihit()
    sprite('kk250_03', 3)
    RefreshMultihit()
    sprite('kk250_04', 3)
    RefreshMultihit()
    sprite('kk250_05', 4)
    Recovery()
    Unknown2063()
    sprite('kk250_06', 4)
    sprite('kk250_07', 4)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(500)
        AttackP1(80)
        AirUntechableTime(19)
        PushbackX(15000)
        AirHitstunAnimation(10)
        AirPushbackY(22000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('AirDrive')
        HitOrBlockJumpCancel(1)
    sprite('kk251_00', 3)
    sprite('kk251_01', 3)
    sprite('kk251_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_1')
    sprite('kk251_03', 4)
    sprite('kk251_04', 3)
    sprite('kk251_05', 4)
    RefreshMultihit()
    CommonSE('008_swing_pole_1')
    sprite('kk251_06', 2)
    Recovery()
    Unknown2063()
    sprite('kk251_07', 3)
    sprite('kk251_08', 3)
    sprite('kk251_09', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        ProjectileLevel(1)
        Damage(750)
        AttackP1(80)
        PushbackX(30400)
        Hitstop(7)
        AirHitstunAnimation(17)
        AirUntechableTime(40)
        AirPushbackX(44000)
        AirPushbackY(22000)
        YImpulseBeforeWallbounce(1500)
        CHGroundedHitstunAnimation(2)
        Wallbounce(1)
        WallbounceReboundTime(7)
        CHAirPushbackY(12000)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR2C')
        HitCancel('AirDrive')
        callSubroutine('Delete_hole')
    sprite('kk252_00', 3)
    CreateObject('efkk_252_hole', -1)
    sprite('kk252_01', 2)
    EndMomentum(1)
    sprite('kk252_02', 2)
    sprite('kk252_03', 3)
    RandomCommonVoiceline(2)
    CommonSE('004_swing_grap_1_2')
    sprite('kk252_04', 2)
    CreateObject('efkk_202_smoke', 0)
    CreateObject('efkk202_BLT', 1)
    StartMultihit()
    PrivateSE('kkse_23')
    sprite('kk252_04', 3)
    physicsXImpulse(-6000)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    sprite('kk252_05', 3)
    Recovery()
    Unknown2063()
    sprite('kk252_06', 3)
    sprite('kk252_07', 3)
    sprite('kk252_08', 3)
    sprite('kk252_09', 3)
    CreateObject('efkk_252_weapon', -1)
    sprite('kk252_10', 3)
    sprite('kk252_11', 3)
    sprite('kk252_12', 3)
    sprite('kk252_13', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(90)
        AttackP2(82)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(-60000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(30)
        PushbackX(36000)
        AirUntechableTime(30)
        AirHitstunAfterWallbounce(30)
        Hitstop(15)
        FatalCounter(1)
        StarterRating(2)
        HitOrBlockCancel('AirDrive')

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            ScreenShake(1000, 4000)
            CommonSE('016_explode_1')
            CommonSE('016_explode_1')
        IgnoreInertia(1)
        SetInertia(0)
        callSubroutine('Delete_hole')
    sprite('kk253_00', 2)
    CreateObject('efkk_253_hole', -1)
    sprite('kk253_01', 2)
    sprite('kk253_02', 2)
    EndMomentum(1)
    sprite('kk253_03', 2)
    sprite('kk253_04', 2)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    EndYPhysicsImpulse()
    sprite('kk253_05', 3)
    CreateObject('efkk_253_burner', -1)
    sprite('kk253_05', 3)
    RandomCommonVoiceline(2)
    PrivateSE('kkse_22')
    CommonSE('005_swing_grap_2_1')
    sprite('kk253_06', 3)
    ForcedLandingRecovery(10, 1)
    sprite('kk253_07', 1)
    sprite('kk253_07', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('kk253_08', 3)
    CreateObject('efkk_253_weapon', -1)
    sprite('kk253_09', 3)
    sprite('kk253_10', 3)
    DespawnEAEffect('efkk_253_burner')
    sprite('kk253_11', 4)
    sprite('kk253_12', 4)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    if random_(2, 0, 50):
        Voiceline('kk404')
    else:
        Voiceline('kk405')
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('kk201_00', 8)
    sprite('kk201_01', 1)
    SetInertia(0)
    physicsXImpulse(26000)
    sprite('kk201_02', 1)
    sprite('kk201_03', 1)
    sprite('kk201_04', 3)
    CommonSE('004_swing_grap_1_2')
    RandomCommonVoiceline(1)
    sprite('kk201_05', 3)
    XImpulseAcceleration(20)
    sprite('kk201_06', 9)
    StartMultihit()
    EndMomentum(1)
    sprite('kk201_07', 6)
    sprite('kk201_08', 6)
    sprite('kk201_09', 6)
    sprite('kk201_10', 6)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(50000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Floorslide(15)
        Wallbounce(1)
        WallbounceReboundTime(30)
        Wallstick(1)
        WallstickDuration(35)
        AirHitstunAfterWallbounce(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        StarterRating(2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            PrivateSE('kkse_07')

        def upon_OPPONENT_HIT():
            PrivateSE('kkse_06')

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
    sprite('kk340_00', 3)
    CreateObject('efkk_340_hole', -1)
    sprite('kk340_01', 3)
    Voiceline('kk159')
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    sprite('kk340_02', 4)
    sprite('kk340_03', 4)
    sprite('kk340_04', 4)
    label(100)
    sprite('kk340_05', 3)
    sprite('kk340_06', 3)
    sprite('kk340_07', 3)
    gotoLabel(100)
    label(0)
    sprite('keep', 2)
    clearUponHandler(EVERY_FRAME)
    sprite('kk340_08', 3)
    CreateObject('efkk_340', -1)
    PrivateSE('kkse_22')
    sprite('kk340_09', 3)
    StartMultihit()
    CommonSE('005_swing_grap_2_2')
    sprite('kk340_10', 1)
    StartMultihit()
    sprite('kk340_10', 1)
    sprite('kk340_11', 3)
    EnableAfterimage(0)
    sprite('kk340_12', 4)
    sprite('kk340_13', 4)
    CreateObject('efkk_340_hole_out', -1)
    sprite('kk340_14', 4)
    sprite('kk340_15', 4)
    sprite('kk340_16', 3)
    sprite('kk340_17', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
        callSubroutine('Delete_hole')
    sprite('kk310_00', 3)
    sprite('kk310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kk310_02', 3)
    sprite('kk310_03', 3)
    SmartVoiceline('kk155')
    sprite('kk310_04', 12)
    sprite('kk310_05', 3)
    sprite('kk310_01', 3)
    sprite('kk310_00', 2)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(5)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(90)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(60)
        Hitstop(0)
        DamageFromStateOnly('ThrowExe')
        SpecialCancel(0)
        StarterRating(2)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
    sprite('kk310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('kk311_00', 3)
    sprite('kk311_01', 3)
    Voiceline('kk153')
    sprite('kk311_02', 3)
    sprite('kk311_03', 5)
    AltKnockdownEffects(100, 1, 1)
    sprite('kk311_04', 5)
    CreateParticle('kkef311_flash', 1)
    sprite('kk311_05', 12)
    sprite('kk311_06', 2)
    sprite('kk311_07', 2)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('kkef311_linework', 1)
    sprite('kk311_08', 2)
    sprite('kk311_09', 8)
    RefreshMultihit()
    Damage(1500)
    AttackP2(50)
    Hitstop(25)
    WallbounceReboundTime(5)
    Floorslide(20)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    UseSlashHitspark(1)
    AirPushbackX(60000)
    AirPushbackY(1000)
    YImpulseBeforeWallbounce(100)
    DamageFromStateOnly('')
    OppMovementUnlock(0)
    AltKnockdownEffects(100, 1, 1)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('kkef311_hit', 0)

    def upon_OPPONENT_HIT():
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
        SpecialCancel(1)
        ScreenShake(60000, 5000)
        PrivateSE('kkse_11')
        EnableRapidCancel(1)
    sprite('kk311_10', 7)
    sprite('kk311_11', 6)
    sprite('kk311_12', 6)
    sprite('kk311_13', 5)
    sprite('kk311_14', 4)
    sprite('kk311_15', 3)
    sprite('kk311_16', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
        callSubroutine('Delete_hole')
    sprite('kk310_00', 3)
    sprite('kk310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kk310_02', 3)
    sprite('kk310_03', 3)
    SmartVoiceline('kk155')
    sprite('kk310_04', 12)
    sprite('kk310_05', 3)
    sprite('kk310_01', 3)
    sprite('kk310_00', 2)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(5)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        FlipOnHit(1)
        AirPushbackX(15000)
        AirPushbackY(48000)
        AirUntechableTime(90)
        Hitstop(25)
        Wallbounce(1)
        WallbounceReboundTime(1)
        AttackDirection(0)
        StarterRating(2)
        OppMovementUnlock(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        ForceFaceSprite()
        HitOrBlockCancel('StandDrive')
        HitOrBlockCancel('CrouchDrive')
    sprite('kk310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('kk313_00', 3)
    ClipThroughOpp()
    ConstantAlphaModifier(-15)
    SetXCollisionFromOrigin(40)
    EnableCollision(0)
    SetZLine(0, 50)
    OppThrowAnimation(8, 0)
    sprite('kk313_01', 1)
    Voiceline('kk153')
    OppThrowAnimation(8, 0)
    physicsXImpulse(60000)
    OppThrowAnimation(8, 0)
    sprite('kk313_01', 1)
    OppThrowAnimation(8, 0)
    XImpulseAcceleration(80)
    sprite('kk313_01', 1)
    OppThrowAnimation(8, 0)
    XImpulseAcceleration(60)
    sprite('kk313_02', 1)
    OppThrowAnimation(8, 0)
    XImpulseAcceleration(40)
    ConstantAlphaModifier(15)
    sprite('kk313_02', 1)
    OppThrowAnimation(8, 0)
    XImpulseAcceleration(20)
    sprite('kk313_02', 1)
    OppThrowAnimation(8, 0)
    XImpulseAcceleration(10)
    sprite('kk313_03', 3)
    EndMomentum(1)
    SetZLine(1, 50)
    OppThrowAnimation(8, 0)
    sprite('kk313_04', 1)
    OppThrowAnimation(8, 0)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('kk313_04', 4)
    sprite('kk313_05', 5)
    OppThrowAnimation(8, 0)
    CreateParticle('kkef311_flash', 1)
    sprite('kk313_06', 5)
    OppThrowAnimation(8, 0)
    sprite('kk313_07', 2)
    OppThrowAnimation(8, 0)
    sprite('kk313_08', 2)
    OppThrowAnimation(8, 0)
    sprite('kk313_09', 2)
    OppThrowAnimation(8, 0)
    ParticleRotationAngle(-30000)
    CallCustomizableParticle('kkef311_linework', 1)
    EnableCollision(1)
    SetXCollisionFromOrigin(30)
    sprite('kk313_10', 5)
    PrivateSE('kkse_11')
    ScreenShake(5000, 60000)
    AltKnockdownEffects(100, 1, 1)
    ParticleRotationAngle(-30000)
    CallCustomizableParticle('kkef311_hit', 0)
    sprite('kk313_11', 5)
    sprite('kk313_12', 5)
    sprite('kk313_13', 6)
    sprite('kk313_14', 5)
    sprite('kk313_15', 4)
    sprite('kk313_16', 3)
    sprite('kk313_17', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
        callSubroutine('Delete_hole')
    sprite('kk320_00', 3)
    sprite('kk320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kk320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('kk320_03', 3)
    Voiceline('kk155')
    sprite('kk320_04', 5)
    sprite('kk320_05', 5)
    sprite('kk320_01', 5)
    sprite('kk320_00', 5)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(5)
        Damage(1500)
        AttackP1(100)
        AttackP2(50)
        AirUntechableTime(100)
        Hitstop(25)
        OppMovementUnlock(0)
        StarterRating(2)
        AirPushbackX(30000)
        AirPushbackY(48000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Wallbounce(1)
        WallbounceReboundTime(10)
        OppPositionOnHit(3, 50000, 150000)
        HitOrBlockCancel('AirDrive')
    sprite('kk320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('kk321_00', 3)
    OppThrowAnimation(9, 0)
    sprite('kk321_01', 3)
    OppThrowAnimation(9, 0)
    sprite('kk321_02', 3)
    Voiceline('kk154')
    OppThrowAnimation(9, 0)
    sprite('kk321_03', 4)
    OppThrowAnimation(9, 0)
    sprite('kk321_04', 4)
    OppThrowAnimation(9, 0)
    CreateParticle('kkef311_flash', 1)
    sprite('kk321_05', 9)
    OppThrowAnimation(9, 0)
    sprite('kk321_06', 2)
    OppThrowAnimation(9, 0)
    sprite('kk321_07', 2)
    OppThrowAnimation(9, 0)
    ParticleRotationAngle(30000)
    CallCustomizableParticle('kkef311_linework', 1)
    sprite('kk321_08', 2)
    SetZLine(1, 50)
    sprite('kk321_09', 5)
    PrivateSE('kkse_11')
    ScreenShake(5000, 60000)
    ParticleRotationAngle(30000)
    CallCustomizableParticle('kkef311_hit', 0)
    sprite('kk321_10', 5)
    sprite('kk321_11', 5)
    sprite('kk321_12', 6)
    sprite('kk321_13', 5)
    sprite('kk321_14', 4)
    EndYPhysicsImpulse()
    sprite('kk321_15', 3)
    sprite('kk321_16', 3)


@State
def StandDrive():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
        callSubroutine('Delete_hole')
    sprite('kk203_00', 3)
    sprite('kk203_01', 3)
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    sprite('kk203_02', 4)
    sprite('kk203_03', 3)
    SmartVoiceline('kk107')
    sprite('kk203_03', 1)
    DespawnEAEffect('efkk_Drive')
    DespawnEAEffect('efkk_Drive_OD')
    sprite('kk203_04', 3)
    SpriteIfNot0(2, 2, 110)
    CreateObject('efkk_denpa2', 0)
    callSubroutine('DriveSet')
    sprite('kk203_05', 3)
    SpriteIfNot0(2, 2, 110)
    Recovery()
    Unknown2063()
    sprite('kk203_06', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk203_07', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk203_08', 3)
    sprite('kk203_09', 3)


@State
def CrouchDrive():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        SpecialCancel(0)
        CrouchState(1)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
        callSubroutine('Delete_hole')
    sprite('kk233_00', 3)
    sprite('kk233_01', 3)
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    sprite('kk233_02', 4)
    sprite('kk233_03', 3)
    SmartVoiceline('kk107')
    sprite('kk233_03', 1)
    DespawnEAEffect('efkk_Drive')
    DespawnEAEffect('efkk_Drive_OD')
    sprite('kk233_04', 3)
    SpriteIfNot0(2, 2, 110)
    CreateObject('efkk_denpa', 0)
    callSubroutine('DriveSet')
    sprite('kk233_05', 3)
    SpriteIfNot0(2, 2, 110)
    Recovery()
    Unknown2063()
    sprite('kk233_06', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk233_07', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk233_08', 3)
    sprite('kk233_09', 3)


@State
def AirDrive():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
        callSubroutine('Delete_hole')
    sprite('kk254_00', 3)
    sprite('kk254_01', 3)
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    sprite('kk254_02', 4)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk254_03', 3)
    SmartVoiceline('kk107')
    sprite('kk254_03', 1)
    DespawnEAEffect('efkk_Drive')
    DespawnEAEffect('efkk_Drive_OD')
    sprite('kk254_04', 3)
    SpriteIfNot0(2, 2, 110)
    CreateObject('efkk_denpa', 0)
    callSubroutine('DriveSet')
    sprite('kk254_05', 3)
    SpriteIfNot0(2, 2, 110)
    Recovery()
    Unknown2063()
    sprite('kk254_06', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk254_07', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    EndYPhysicsImpulse()
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(70)
    sprite('kk254_08', 3)
    sprite('kk254_09', 3)


@State
def AtkDrive_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        SLOT_5 = 2
        callSubroutine('Delete_hole')
    sprite('kk203_00', 2)
    sprite('kk203_01', 1)
    sprite('kk203_02', 3)
    sprite('kk203_03', 2)
    SmartVoiceline('kk106')
    sprite('kk203_04', 3)
    CreateObject('efkk_denpa2', 0)
    ObjectUpon(5, 32)
    sprite('kk203_05', 3)
    sprite('kk203_06', 2)
    sprite('kk203_07', 2)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk203_08', 3)
    sprite('kk203_09', 2)


@State
def AtkDrive_2ndAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        SLOT_5 = 2
        callSubroutine('Delete_hole')
    sprite('kk254_00', 2)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk254_01', 1)
    sprite('kk254_02', 3)
    sprite('kk254_03', 2)
    SmartVoiceline('kk106')
    sprite('kk254_04', 3)
    CreateObject('efkk_denpa', 0)
    SLOT_5 = 2
    ObjectUpon(5, 32)
    sprite('kk254_05', 3)
    EndYPhysicsImpulse()
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(70)
    sprite('kk254_06', 2)
    sprite('kk254_07', 2)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk254_08', 3)
    sprite('kk254_09', 2)


@State
def Drive_Stop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        callSubroutine('Delete_hole')
    sprite('kk203_00', 3)
    sprite('kk203_01', 3)
    sprite('kk203_02', 4)
    sprite('kk203_03', 4)
    sprite('kk203_04', 3)
    CreateObject('efkk_denpa2', 0)
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    SLOT_34 = SLOT_34 + 120
    sprite('kk203_05', 3)
    SpriteIfNot0(2, 2, 110)
    Recovery()
    Unknown2063()
    sprite('kk203_06', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk203_07', 3)
    SpriteIfNot0(2, 2, 110)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk203_08', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk203_09', 3)
    SpriteIfNot0(2, 2, 110)


@State
def Drive_StopAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        callSubroutine('Delete_hole')
    sprite('kk254_00', 3)
    sprite('kk254_01', 3)
    sprite('kk254_02', 4)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk254_03', 4)
    sprite('kk254_04', 3)
    CreateObject('efkk_denpa', 0)
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    SLOT_34 = SLOT_34 + 120
    sprite('kk254_05', 3)
    SpriteIfNot0(2, 2, 110)
    Recovery()
    Unknown2063()
    EndYPhysicsImpulse()
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(70)
    sprite('kk254_06', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk254_07', 3)
    SpriteIfNot0(2, 2, 110)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffJumpCancel(1)
    sprite('kk254_08', 3)
    SpriteIfNot0(2, 2, 110)
    sprite('kk254_09', 3)
    SpriteIfNot0(2, 2, 110)


@Subroutine
def ShottoAtkDrive_2nd():

    def upon_EVERY_FRAME():
        if SLOT_StateDuration >= 20:
            WhiffCancelEnable(1)
            WhiffCancel('AtkDrive_2nd_ChainOnly')
        if SLOT_StateDuration >= 35:
            WhiffCancelEnable(0)
            clearUponHandler(EVERY_FRAME)


@Subroutine
def AirShottoAtkDrive_2nd():

    def upon_EVERY_FRAME():
        if SLOT_StateDuration >= 17:
            WhiffCancelEnable(1)
            WhiffCancel('AtkDrive_2nd_ChainOnly')
        if SLOT_StateDuration >= 32:
            WhiffCancelEnable(0)
            clearUponHandler(EVERY_FRAME)


@State
def Shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('ShottoAtkDrive_2nd')
    sprite('kk402_00', 3)
    sprite('kk402_01', 3)
    sprite('kk402_02', 3)
    sprite('kk402_03', 3)
    sprite('kk402_04', 3)
    Voiceline('kk204')
    sprite('kk402_05', 3)
    sprite('kk402_06', 3)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 33)
    sprite('kk402_07', 3)
    sprite('kk402_08', 3)
    sprite('kk402_09', 3)
    sprite('kk402_10', 3)
    CreateObject('efkk402_BLT', 0)
    sprite('kk402_11', 3)
    sprite('kk402_12', 3)
    sprite('kk402_13', 3)
    Recovery()


@State
def Shot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('ShottoAtkDrive_2nd')
    sprite('kk402_00', 3)
    sprite('kk402_01', 3)
    sprite('kk402_02', 3)
    sprite('kk402_03', 3)
    sprite('kk402_04', 3)
    Voiceline('kk204')
    sprite('kk402_05', 3)
    sprite('kk402_06', 3)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 34)
    sprite('kk402_07', 3)
    sprite('kk402_08', 3)
    sprite('kk402_09', 3)
    sprite('kk402_10', 3)
    CreateObject('efkk402_BLT', 0)
    sprite('kk402_11', 3)
    sprite('kk402_12', 3)
    sprite('kk402_13', 3)
    Recovery()


@State
def Shot_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('ShottoAtkDrive_2nd')
    sprite('kk402_00', 3)
    sprite('kk402_01', 3)
    sprite('kk402_02', 3)
    sprite('kk402_03', 3)
    sprite('kk402_04', 3)
    Voiceline('kk204')
    sprite('kk402_05', 3)
    sprite('kk402_06', 3)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 35)
    sprite('kk402_07', 3)
    sprite('kk402_08', 3)
    sprite('kk402_09', 3)
    sprite('kk402_10', 3)
    CreateObject('efkk402_BLT', 0)
    sprite('kk402_11', 3)
    sprite('kk402_12', 3)
    sprite('kk402_13', 3)
    Recovery()


@State
def AirShot_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('AirShottoAtkDrive_2nd')
    sprite('kk402_14', 3)
    sprite('kk402_15', 2)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk402_16', 2)
    sprite('kk402_17', 2)
    Voiceline('kk204')
    sprite('kk402_18', 3)
    sprite('kk402_19', 3)
    sprite('kk402_06', 5)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 33)
    ForcedLandingRecovery(6, 1)
    sprite('kk402_07', 3)
    sprite('kk402_08', 2)
    sprite('kk402_09', 2)
    sprite('kk402_20', 5)
    CreateObject('efkk402_BLT', 0)
    PopSpeedX()
    XImpulseAcceleration(60)
    EndYPhysicsImpulse()
    sprite('kk402_21', 5)
    sprite('kk402_22', 5)
    sprite('kk402_23', 5)
    Recovery()


@State
def AirShot_B():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('AirShottoAtkDrive_2nd')
    sprite('kk402_14', 3)
    sprite('kk402_15', 2)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk402_16', 2)
    sprite('kk402_17', 2)
    Voiceline('kk204')
    sprite('kk402_18', 3)
    sprite('kk402_19', 3)
    sprite('kk402_06', 5)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 34)
    ForcedLandingRecovery(6, 1)
    sprite('kk402_07', 3)
    sprite('kk402_08', 2)
    sprite('kk402_09', 2)
    sprite('kk402_20', 5)
    CreateObject('efkk402_BLT', 0)
    PopSpeedX()
    XImpulseAcceleration(60)
    EndYPhysicsImpulse()
    sprite('kk402_21', 5)
    sprite('kk402_22', 5)
    sprite('kk402_23', 5)
    Recovery()


@State
def AirShot_C():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Delete_hole')
        callSubroutine('AirShottoAtkDrive_2nd')
    sprite('kk402_14', 3)
    sprite('kk402_15', 2)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    sprite('kk402_16', 2)
    sprite('kk402_17', 2)
    Voiceline('kk204')
    sprite('kk402_18', 3)
    sprite('kk402_19', 3)
    sprite('kk402_06', 5)
    PrivateSE('kkse_12')
    CreateObject('efkk_fireball_Hontai', 0)
    ObjectUpon(STATE_END, 35)
    ForcedLandingRecovery(6, 1)
    sprite('kk402_07', 3)
    sprite('kk402_08', 2)
    sprite('kk402_09', 2)
    sprite('kk402_20', 5)
    CreateObject('efkk402_BLT', 0)
    PopSpeedX()
    XImpulseAcceleration(60)
    EndYPhysicsImpulse()
    sprite('kk402_21', 5)
    sprite('kk402_22', 5)
    sprite('kk402_23', 5)
    Recovery()


@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        CHCrumple(39)
        AirUntechableTime(36)
        AirPushbackX(0)
        AirPushbackY(-28000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        OppMovementUnlock(1)
        DistanceCheck(400000, -1, -1, -1)
        OppPositionOnHit(1, 150000, 0)

        def upon_EVERY_FRAME():
            SLOT_19 < 200000
            if not SLOT_0 and not SLOT_51:
                sendToLabel(0)

        def upon_OPPONENT_HIT():
            CreateObject('efkk400_Hand002nd', -1)
            RegisterObject(4, 1)
            PushbackX(0)
            ScreenShake(5000, 10000)
            if SLOT_2:
                enterState('Assault_A_2nd')

        def upon_RELEASE_A():
            SetActionMark(1)
        callSubroutine('Delete_hole')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('kk400_00', 1)
    CreateObject('efkk400A_fire00', -1)
    PrivateSE('kkse_01')
    sprite('kk400_01', 1)
    Voiceline('kk200')
    sprite('kk400_02', 1)
    sprite('kk400_03', 1)
    sprite('kk400_04', 3)
    PrivateSE('kkse_22')
    sprite('kk400_05', 3)
    physicsXImpulse(45000)
    SetXCollisionFromOrigin(150)
    CommonSE('000_airdash_1')
    PreDashEffects(100, 1, 0)
    EnableAfterimage(1)
    sprite('kk400_06', 3)
    sprite('kk400_07', 3)
    SLOT_51 = 1
    sprite('kk400_05', 3)
    sprite('kk400_06', 3)
    sprite('kk400_07', 3)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('kk400_08', 1)
    TriggerUponForState('efkk400A_fire00', 32)
    XImpulseAcceleration(50)
    sprite('kk400_09', 1)
    XImpulseAcceleration(50)
    CommonSE('005_swing_grap_2_0')
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk400_10', 3)
    EnableAfterimage(0)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('kk400_10', 1)
    Recovery()
    StartMultihit()
    CallCustomizableParticle('kkef400kowarearm_01', 0)
    CallCustomizableParticle('kkef400kowarearm_01', 1)
    WhiffCancelEnable(0)
    sprite('kk400_33', 3)
    sprite('kk400_34', 3)
    sprite('kk400_35', 3)
    SetXCollisionFromOrigin(-1)
    sprite('kk400_36', 4)
    sprite('kk400_37', 4)
    sprite('kk400_38', 4)
    ParticleSize(800)
    CallCustomizableParticle('kkef403koware_05', 0)
    CommonSE('016_explode_0')
    ParticleSize(800)
    CallCustomizableParticle('kkef403koware_05', 1)


@State
def Assault_A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        NonCornerWallbounce(1)
        WallbounceReboundTime(5)
        AirUntechableTime(60)
        AirPushbackX(75000)
        AirPushbackY(10000)
        CHStateIfCHStart(3)
        HitBackReturnIgnore(1)
        SetXCollisionFromOrigin(200)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('kk400_11', 2)
    sprite('kk400_12', 2)
    sprite('kk400_13', 2)
    CreateObject('efkk400_Hand00', -1)
    sprite('kk400_14', 2)
    sprite('kk400_15', 2)
    sprite('kk400_16', 2)
    if SLOT_44:
        Voiceline('kk201')
    TriggerUponForState('efkk400A_fire00', 33)
    sprite('kk400_17', 2)
    sprite('kk400_18', 1)
    sprite('kk400_19', 4)
    sprite('kk400_20', 1)
    sprite('kk400_21', 2)
    sprite('kk400_22', 1)
    TriggerUponForState('efkk400A_fire00', 34)
    sprite('kk400_23', 2)
    CommonSE('005_swing_grap_2_0')
    sprite('kk400_24', 1)
    if SLOT_43:
        Voiceline('kk201')
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk400_25', 3)
    PrivateSE('kkse_25')
    RefreshMultihit()
    CreateObject('efkk400_Hand01', -1)
    CreateObject('efkk400_CircleRenzok', -1)
    TriggerUponForState('efkk400_Hand00', 32)

    def upon_OPPONENT_HIT():
        ObjectUpon(FALLING, 34)
    sprite('kk400_26', 3)
    Recovery()
    WhiffCancelEnable(0)
    sprite('kk400_27', 3)
    sprite('kk400_28', 3)
    sprite('kk400_26', 3)
    sprite('kk400_27', 3)
    sprite('kk400_28', 3)
    sprite('kk400_26', 3)
    sprite('kk400_29', 3)
    sprite('kk400_30', 3)
    sprite('kk400_31', 3)
    sprite('kk400_32', 3)


@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(40)
        Crumple(35)
        IgnoreComboTime(1)
        OppMovementUnlock(1)
        DistanceCheck(400000, -1, -1, -1)
        OppPositionOnHit(1, 150000, 0)

        def upon_OPPONENT_HIT():
            PushbackX(0)
            enterState('Assault_B_2nd')

        def upon_EVERY_FRAME():
            if SLOT_19 < 300000:
                if SLOT_51:
                    sendToLabel(1)
        callSubroutine('Delete_hole')
    sprite('kk400_00', 1)
    PrivateSE('kkse_01')
    sprite('kk400_01', 1)
    Voiceline('kk200')
    CreateObject('efkk400A_fire00', -1)
    ScreenShake(4000, 2000)
    LandingEffects(100, 1, 0)
    sprite('kk400_02', 2)
    sprite('kk400_03', 2)
    sprite('kk400_04', 8)
    PrivateSE('kkse_22')
    sprite('kk400_05', 2)
    physicsXImpulse(67500)
    SetXCollisionFromOrigin(150)
    CommonSE('000_airdash_1')
    PreDashEffects(100, 1, 0)
    sprite('kk400_06', 2)
    DashEffects(100, 1, 0)
    sprite('kk400_07', 2)
    SLOT_51 = 1
    sprite('kk400_05', 2)
    sprite('kk400_06', 2)
    DashEffects(100, 1, 0)
    sprite('kk400_07', 2)
    label(1)
    sprite('kk400_08', 2)
    TriggerUponForState('efkk400A_fire00', 32)
    clearUponHandler(EVERY_FRAME)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(80)
    DashEffects(100, 1, 0)
    sprite('kk400_09', 2)
    XImpulseAcceleration(80)
    CommonSE('005_swing_grap_2_0')
    sprite('kk400_10', 3)
    EndMomentum(1)
    SkidEffects(100, 1, 0)
    sprite('kk400_10', 3)
    Recovery()
    StartMultihit()
    CallCustomizableParticle('kkef400kowarearm_01', 0)
    CallCustomizableParticle('kkef400kowarearm_01', 1)
    sprite('kk400_33', 4)
    sprite('kk400_34', 4)
    sprite('kk400_35', 4)
    sprite('kk400_36', 4)
    sprite('kk400_37', 4)
    sprite('kk400_38', 4)
    ParticleSize(800)
    CallCustomizableParticle('kkef403koware_05', 0)
    CommonSE('016_explode_0')
    ParticleSize(800)
    CallCustomizableParticle('kkef403koware_05', 1)
    sprite('kk400_38', 2)


@State
def Assault_B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        NonCornerWallbounce(1)
        WallbounceReboundTime(5)
        AirUntechableTime(60)
        AirPushbackX(75000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(100)
        CHStateIfCHStart(3)
        HitBackReturnIgnore(1)
        SetXCollisionFromOrigin(200)
    sprite('kk400_11', 2)
    sprite('kk400_12', 2)
    sprite('kk400_13', 2)
    CreateObject('efkk400_Hand00', -1)
    sprite('kk400_14', 2)
    sprite('kk400_15', 2)
    sprite('kk400_16', 2)
    if SLOT_44:
        Voiceline('kk201')
    TriggerUponForState('efkk400A_fire00', 33)
    sprite('kk400_17', 2)
    sprite('kk400_18', 2)
    sprite('kk400_19', 6)
    sprite('kk400_20', 2)
    sprite('kk400_21', 2)
    sprite('kk400_22', 2)
    TriggerUponForState('efkk400A_fire00', 34)
    sprite('kk400_23', 2)
    CommonSE('005_swing_grap_2_0')
    sprite('kk400_24', 2)
    if SLOT_43:
        Voiceline('kk201')
    sprite('kk400_25', 3)
    PrivateSE('kkse_25')
    RefreshMultihit()
    CreateObject('efkk400_Hand01', -1)
    CreateObject('efkk400_CircleRenzok', -1)
    TriggerUponForState('efkk400_Hand00', 32)

    def upon_OPPONENT_HIT():
        CreateObject('efkk400_Hand002nd', -1)
        ObjectUpon(STATE_END, 33)
    sprite('kk400_26', 3)
    Recovery()
    sprite('kk400_29', 3)
    sprite('kk400_30', 3)
    sprite('kk400_31', 3)
    sprite('kk400_32', 3)


@State
def Freeze_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        ProjectileLevel(2)
        StrikeProjectileLevel(0)
        Damage(600)
        Hitstop(2)
        FreezeCount(5)
        FreezeTime(120)
        ChipPercentage(10)
        PushbackX(19800)
        MoveAttributes(0, 0, 0, 1, 0)
        DamageEffect(4, 'ef_gird_damage')
        SLOT_57 = 1

        def upon_OPPONENT_HIT_OR_BLOCK():
            CommonSE('017_freeze_1')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            clearUponHandler(17)
            sendToLabel(1)
        RunLoopUpon(17, 90)
        uponSendToLabel(17, 100)
        callSubroutine('Delete_hole')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('kk401_00', 2)
    sprite('kk401_01', 2)
    Voiceline('kk202')
    sprite('kk401_02', 3)
    sprite('kk401_03', 3)
    sprite('kk401_04', 3)
    sprite('kk401_05', 3)
    sprite('kk401_03', 3)
    sprite('kk401_04', 3)
    sprite('kk401_05', 3)
    sprite('kk401_06', 3)
    StartMultihit()
    CreateParticle('kkef401icewind_00', 106)
    CreateParticle('kkef401icewind_00', 106)
    CreateParticle('kkef401icewind_00', 106)
    CreateParticle('kkef401icewind_00', 106)
    CreateObject('efkk_freezwind00', 0)
    PrivateSE('kkse_04')
    PrivateSE('kkse_05')
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    label(0)
    sprite('kk401_07', 2)
    RefreshMultihit()
    sprite('kk401_08', 2)
    RefreshMultihit()
    sprite('kk401_09', 2)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('kk401_32', 3)
    TriggerUponForState('efkk_freezwind00', 32)
    Recovery()
    WhiffCancelEnable(0)
    sprite('kk401_33', 3)
    sprite('kk401_34', 3)
    sprite('kk401_35', 3)
    ExitState()
    label(1)
    sprite('kk401_07', 3)
    WhiffCancelEnable(0)
    sprite('kk401_08', 3)
    sprite('kk401_09', 3)
    sprite('kk401_07', 3)
    sprite('kk401_08', 3)
    sprite('kk401_09', 3)
    TriggerUponForState('efkk_freezwind00', 32)
    sprite('kk401_10', 4)
    sprite('kk401_11', 4)
    CreateObject('efkk_401_hole', -1)
    CreateObject('efkk401_reitouhou', 0)
    Voiceline('kk203')
    sprite('kk401_12', 4)
    sprite('kk401_13', 3)
    CreateObject('efkk_401weapon', -1)
    CreateObject('efkk_401weapon2', -1)
    PrivateSE('kkse_01')
    PrivateSE('kkse_03')
    PrivateSE('kkse_03')
    sprite('kk401_14', 3)
    PrivateSE('kkse_02')
    SetXCollisionFromOrigin(200)
    sprite('kk401_15', 3)
    SetXCollisionFromOrigin(250)
    sprite('kk401_16', 3)
    SetXCollisionFromOrigin(300)
    sprite('kk401_17', 3)
    RefreshMultihit()
    Damage(0)
    SetXCollisionFromOrigin(350)
    ScreenShake(3000, 0)
    physicsXImpulse(-3000)
    Hitstop(0)
    AirPushbackX(30000)
    AirPushbackY(-10000)
    PushbackX(39600)
    FreezeCount(-1)
    IgnoreComboTime(1)
    AttackP2(100)
    sprite('kk401_18', 1)
    NoAttackDuringAction(1)
    CreateObject('efkk_BLTtakusan', 2)
    CreateObject('efkk_Mazleflash', 0)
    CreateObject('efkk_Mazleflash', 1)
    SLOT_51 = 4
    SLOT_52 = 2
    label(2)
    sprite('kk401_18', 3)
    XImpulseAcceleration(90)
    ScreenShake(3000, 0)
    SLOT_52 = SLOT_52 + -1

    def upon_32():
        SLOT_52 = SLOT_52 + 1
    sprite('kk401_19', 3)
    ScreenShake(1500, 1500)
    sprite('kk401_20', 3)
    ScreenShake(3000, 0)
    SLOT_51 = SLOT_51 + -1
    if not SLOT_51:
        notConditionalSendToLabel(3)
    if not SLOT_52:
        notConditionalSendToLabel(3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('kk401_18', 3)
    NoAttackDuringAction(1)
    TriggerUponForState('efkk_Mazleflash', 32)
    TriggerUponForState('efkk_BLTtakusan', 32)
    sprite('kk401_19', 3)
    sprite('kk401_20', 3)
    EnableRapidCancel(0)
    if SLOT_52:
        if SLOT_Meter >= 5000:
            CreateObject('efkk401_MisileAtk', -1)

            def upon_35():
                clearUponHandler(35)
                if not SLOT_IsFacingRight:
                    if SLOT_40 > 0:
                        if SLOT_OverdriveTimer:
                            enterState('Freeze_Shot_Finish_OD')
                        else:
                            enterState('Freeze_Shot_Finish')
                elif SLOT_40 < 0:
                    if SLOT_OverdriveTimer:
                        enterState('Freeze_Shot_Finish_OD')
                    else:
                        enterState('Freeze_Shot_Finish')
    sprite('kk401_36', 5)
    EnableRapidCancel(1)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(0)
    CreateObject('efkk401_minigunbrake', -1)
    TriggerUponForState('efkk_Mazleflash', 32)
    TriggerUponForState('efkk_BLTtakusan', 32)
    IgnoreTurn(1)
    WhiffCrouchBlockCancel(1)
    Recovery()
    sprite('kk404_06ex01', 4)
    sprite('kk404_07ex01', 4)
    sprite('kk404_08ex01', 4)
    sprite('kk404_09ex01', 4)


@State
def Freeze_Shot_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
    sprite('kk401_21', 4)
    CreateObject('efkk401_minigunbrake', -1)
    DistortionSettings(26, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    setInvincible(1)
    sprite('kk401_22', 4)
    sprite('kk401_23', 12)
    sprite('kk401_24', 3)
    setInvincible(0)
    sprite('kk401_25', 3)
    Voiceline('kk252')
    sprite('kk401_26', 3)
    sprite('kk401_26', 3)
    CreateObject('efkk401_micile', -1)
    sprite('kk401_27', 6)
    Recovery()
    sprite('kk401_28', 6)
    sprite('kk401_29', 6)
    sprite('kk401_30', 3)
    sprite('kk401_31', 3)
    sprite('kk001_00', 6)
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 3)
    sprite('kk001_06', 3)
    sprite('kk001_07', 3)
    sprite('kk001_08', 3)


@State
def Freeze_Shot_Finish_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        AttackType(4)
    sprite('kk401_21', 4)
    CreateObject('efkk401_minigunbrake', -1)
    DistortionSettings(28, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    setInvincible(1)
    sprite('kk401_22', 4)
    sprite('kk401_23', 12)
    sprite('kk401_24', 3)
    setInvincible(0)
    sprite('kk401_25', 3)
    Voiceline('kk252')
    sprite('kk401_26', 3)
    sprite('kk401_26', 3)
    CreateObject('efkk401_micile_OD', -1)
    sprite('kk401_27', 6)
    Recovery()
    sprite('kk401_28', 6)
    sprite('kk401_29', 6)
    sprite('kk401_30', 3)
    sprite('kk401_31', 3)
    sprite('kk001_00', 6)
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 3)
    sprite('kk001_06', 3)
    sprite('kk001_07', 3)
    sprite('kk001_08', 3)


@State
def Lightning_Shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Delete_hole')
    sprite('kk403_00', 2)
    sprite('kk403_01', 2)
    sprite('kk403_02', 2)
    Voiceline('kk205')
    sprite('kk403_03', 2)
    sprite('kk403_04', 3)
    CreateObject('efkk_403_TrapA', -1)
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk403_05', 3)
    sprite('kk403_06', 3)
    sprite('kk403_07', 5)
    sprite('kk403_08', 5)
    sprite('kk403_09', 5)
    WhiffCancelEnable(0)
    sprite('kk403_10', 5)
    Recovery()
    sprite('kk403_11', 5)


@State
def Lightning_Shot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        callSubroutine('Delete_hole')
    sprite('kk403_00', 3)
    sprite('kk403_01', 3)
    sprite('kk403_02', 3)
    Voiceline('kk205')
    sprite('kk403_03', 3)
    sprite('kk403_04', 3)
    CreateObject('efkk_403_TrapB', -1)
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk403_05', 3)
    sprite('kk403_06', 3)
    sprite('kk403_07', 3)
    sprite('kk403_08', 2)
    sprite('kk403_09', 2)
    WhiffCancelEnable(0)
    sprite('kk403_10', 2)
    Recovery()
    sprite('kk403_11', 3)


@State
def Warp():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        EndMomentum(1)
        callSubroutine('Delete_hole')
    sprite('kk404_00ex00', 4)
    sprite('kk404_00ex02', 1)
    if SLOT_5:
        CopyFromRightToLeft(3, 2, 51, 5, 2, 22)
        if not SLOT_IsFacingRight:
            PrivateFunction(1, 2, 51, 2, 22, 2, 52)
        else:
            PrivateFunction(1, 2, 22, 2, 51, 2, 52)
        SLOT_XVelocity = SLOT_52
        XImpulseAcceleration(100)
        XSpeed(-200000)
        if SLOT_52 < 270000:
            XSpeed(270000)
    else:
        physicsXImpulse(-270000)
        XImpulseAcceleration(-100)
    setInvincible(1)
    EnableCollision(0)
    ForceFaceSprite()
    PrivateSE('kkse_19')
    CreateObject('Warp01', -1)
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk404_00ex02', 1)
    EndMomentum(1)
    sprite('kk404_01ex02', 3)
    sprite('kk404_02ex02', 3)
    Voiceline('kk206')
    sprite('kk404_03ex02', 3)
    sprite('kk404_04ex02', 3)
    WhiffCancelEnable(0)
    sprite('kk404_05ex02', 3)
    sprite('kk404_06ex02', 3)
    sprite('kk404_07ex02', 3)
    setInvincible(0)
    EnableCollision(1)
    sprite('kk404_08ex02', 3)
    sprite('kk404_09ex02', 3)


@State
def SpinAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(300)
        AttackP1(90)
        AttackP2(82)
        SingleProration(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        Hitstop(5)
        UseFireHitspark(1)
        MoveAttributes(1, 0, 0, 0, 0)
        SLOT_60 = 1
        EndMomentum(1)
        SLOT_6 = 0

        def upon_STATE_END():
            SLOT_6 = 0
            ResetExternalForces()

        def upon_32():
            SLOT_51 = 1

        def upon_EVERY_FRAME():
            if SLOT_6:
                if SLOT_5 == 1:
                    AirPushbackX(8000)
                    AirPushbackY(8000)
                    YImpulseBeforeWallbounce(1800)
                    PushbackX(8000)
                    Blockstun(20)
                    if SLOT_51:
                        ExternalForcesRate(10, 40)
                        ObjectUpon26(5, 0, -250000, 40000, 1)
                    elif SLOT_StateDuration <= 25:
                        ExternalForcesRate(10, 40)
                        ObjectUpon26(5, 0, -250000, 10000, 1)
                    else:
                        ExternalForcesRate(10, 40)
                        ObjectUpon26(5, 0, -250000, 30000, 1)
                    if SLOT_YDistanceFromFloor <= 16000:
                        SLOT_YDistanceFromFloor = 16000
                    if SLOT_YVelocity >= 4000:
                        SLOT_YVelocity = 4000
                elif SLOT_5 >= 2:
                    ExternalForcesRate(50, 50)
                else:
                    ExternalForcesRate(0, 0)
                    setGravity(1800)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 8)
        if SLOT_137:
            DamageMultiplier(80)
    if SLOT_IsAirborne:
        conditionalSendToLabel(0)
    sprite('kk405_00', 3)
    sprite('kk405_01', 3)
    sprite('kk405_02', 3)
    sprite('kk405_03', 3)
    sprite('kk405_04', 3)
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk405_05', 3)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('kk405_15', 2)
    sprite('kk405_16', 2)
    sprite('kk405_17', 2)
    sprite('kk405_03ex01', 2)
    sprite('kk405_04ex01', 3)
    WhiffCancelEnable(1)
    WhiffCancel('AtkDrive_2nd_ChainOnly')
    sprite('kk405_05ex01', 3)
    loopRest()
    label(1)
    sprite('kk405_06', 3)
    RefreshMultihit()
    CreateObject('efkk405_Fire00', -1)
    Voiceline('kk207')
    CommonSE('005_swing_grap_2_2')
    PrivateSE('kkse_12')
    if not SLOT_5 == 1:
        physicsXImpulse(12000)
        physicsYImpulse(36000)
        setGravity(1800)
    AddY(30000)
    SLOT_6 = 1
    sprite('kk405_07', 3)
    sprite('kk405_08', 3)
    RefreshMultihit()
    sprite('kk405_09', 3)
    sprite('kk405_10', 3)
    RefreshMultihit()
    sprite('kk405_06', 3)
    CreateObject('efkk405_Fire00', -1)
    CommonSE('015_blaze_0')
    sprite('kk405_07', 3)
    RefreshMultihit()
    sprite('kk405_08', 3)
    sprite('kk405_09', 3)
    RefreshMultihit()
    sprite('kk405_10', 3)
    sprite('kk405_06', 3)
    CreateObject('efkk405_Fire00', -1)
    CommonSE('015_blaze_0')
    RefreshMultihit()
    sprite('kk405_07', 3)
    sprite('kk405_08', 3)
    RefreshMultihit()
    sprite('kk405_09', 3)
    sprite('kk405_10', 3)
    RefreshMultihit()
    sprite('kk405_06', 3)
    CreateObject('efkk405_Fire00', -1)
    CommonSE('015_blaze_0')
    sprite('kk405_07', 3)
    RefreshMultihit()
    sprite('kk405_08', 3)
    sprite('kk405_09', 3)
    RefreshMultihit()
    sprite('kk405_10', 3)
    sprite('kk405_06', 3)
    CreateObject('efkk405_Fire00', -1)
    CommonSE('015_blaze_0')
    RefreshMultihit()
    sprite('kk405_07', 3)
    sprite('kk405_08', 3)
    RefreshMultihit()
    sprite('kk405_09', 3)
    sprite('kk405_10', 3)
    RefreshMultihit()
    label(8)
    sprite('kk405_11', 3)
    TriggerUponForState('efkk405_Fire00', 32)
    ResetExternalForces()
    SLOT_6 = 0
    clearUponHandler(LANDING)
    clearUponHandler(EVERY_FRAME)
    ForceFaceSprite()
    Recovery()
    WhiffCancelEnable(0)
    physicsXImpulse(1500)
    physicsYImpulse(6000)
    EndYPhysicsImpulse()
    sprite('kk405_12', 3)
    CreateObject('efkk405_PartsA', 0)
    CreateObject('efkk405_PartsB', 1)
    sprite('kk405_13', 3)
    sprite('kk405_14', 3)


@State
def UltimateShot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(3000)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 3)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    sprite('kk430_09', 3)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 3)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 33)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateShot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(4500)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 4)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    PreDashEffects(100, 1, 1)
    sprite('kk430_09', 4)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 4)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 34)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateShot_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(7500)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 5)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    PreDashEffects(100, 1, 1)
    sprite('kk430_09', 5)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 5)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 35)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateAirShot_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 33)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateAirShot_B():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 34)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateAirShot_C():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        MinimumDamage(15)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShot')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai', 0)
    ObjectUpon(STATE_END, 35)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateShotOD_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(3000)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 3)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    sprite('kk430_09', 3)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 3)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 33)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateShotOD_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(4500)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 4)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    PreDashEffects(100, 1, 1)
    sprite('kk430_09', 4)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 4)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 34)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateShotOD_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        GotoState('UltimateShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_00', 4)
    sprite('kk430_01', 4)
    DistortionSettings(40, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_02', 6)
    Voiceline('kk250')
    sprite('kk430_03', 6)
    sprite('kk430_04', 6)
    sprite('kk430_05', 6)
    sprite('kk430_06', 4)
    sprite('kk430_07', 4)
    physicsXImpulse(7500)
    PreDashEffects(100, 1, 1)
    sprite('kk430_08', 5)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 1)
    PrivateSE('kkse_01')
    PreDashEffects(100, 1, 1)
    sprite('kk430_09', 5)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_10', 5)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('kk430_11', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    LandingEffects(100, 1, 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 35)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15', 3)
    sprite('kk430_16', 3)
    sprite('kk430_17', 3)
    sprite('kk430_18', 3)
    sprite('kk430_19', 3)
    sprite('kk430_20', 3)
    sprite('kk430_21', 3)
    sprite('kk430_22', 3)


@State
def UltimateAirShotOD_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(10000, 40000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 33)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateAirShotOD_B():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(10000, 40000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 34)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateAirShotOD_C():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1250)
        AttackP1(60)
        AirUntechableTime(90)
        AirPushbackY(45000)
        CHAirPushbackY(90000)
        AirPushbackX(1000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AttackDirection(0)
        UseFireHitspark(1)
        AttackType(4)
        StarterRating(0)
        setInvincible(1)
        EndMomentum(1)
        ForcedLandingRecovery(6, 1)
        GotoState('UltimateAirShotOD')
        callSubroutine('Delete_hole')
        Unknown23170('UltimateShot')
    sprite('kk430_23', 2)
    sprite('kk430_24', 2)
    sprite('kk430_02ex', 5)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk430_03ex', 5)
    Voiceline('kk250')
    sprite('kk430_04ex', 5)
    sprite('kk430_05ex', 11)
    sprite('kk430_06ex', 4)
    sprite('kk430_07ex', 4)
    sprite('kk430_08ex', 4)
    PrivateSE('kkse_01')
    sprite('kk430_09', 4)
    sprite('kk430_10', 4)
    sprite('kk430_11', 3)
    CreateObject('efkk401_Kakyufire', 1)
    PrivateSE('kkse_14')
    PrivateSE('kkse_14')
    ScreenShake(8000, 36000)
    sprite('kk430_11', 3)
    StartMultihit()
    CreateObject('efkk_UltraSokidan_Hontai_OD', 0)
    ObjectUpon(STATE_END, 35)
    setInvincible(0)
    sprite('kk430_12', 3)
    sprite('kk430_13', 3)
    sprite('kk430_14', 3)
    sprite('kk430_15ex', 3)
    TriggerUponForState('efkk401_Kakyufire', 32)
    sprite('kk430_25', 3)
    setGravity(2000)
    sprite('kk430_26', 3)
    sprite('kk430_27', 3)


@State
def UltimateBlackhole():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        PreventBlocking(1)
        EndMomentum(1)
        EnableRapidCancel(0)
        setInvincible(1)
        ExternalForcesRate(0, 0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 0)

        def upon_41():
            clearUponHandler(41)
            clearUponHandler(17)
            SetActionMark(1)
            SLOT_7 = 2
            setInvincible(1)
        uponSendToLabel(35, 10)
        RunLoopUpon(17, 267)

        def upon_17():
            clearUponHandler(17)
            clearUponHandler(41)
            TriggerUponForState('efkk_GravityBall', 33)
            TriggerUponForState('efkk_AtkGravityBall', 34)
            sendToLabel(10)
        SLOT_7 = 2
        SLOT_63 = 0

        def upon_14():
            clearUponHandler(41)
            TriggerUponForState('efkk_GravityBall', 33)
            TriggerUponForState('efkk_AtkGravityBall', 34)

        def upon_STATE_END():
            SLOT_7 = 0
        callSubroutine('Delete_hole')
    sprite('kk431_00', 4)
    sprite('kk431_01', 4)
    sprite('kk431_02', 4)
    sprite('kk431_03', 40)
    CreateObject('efkk_GravityBall', -1)
    Voiceline('kk251')
    sprite('kk431_04', 5)
    DistortionSettings(56, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk431_05', 5)
    sprite('kk431_06', 5)
    sprite('kk431_07', 5)
    sprite('kk431_08', 5)
    sprite('kk431_09', 5)
    sprite('kk431_10', 5)
    sprite('kk431_11', 3)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    setGravity(-100)
    TriggerUponForState('efkk_GravityBall', 32)
    CreateObject('efkk_AtkGravityBall', -1)
    SLOT_7 = 1
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    sprite('kk431_12', 3)
    sprite('kk431_13', 3)
    sprite('kk431_14', 3)
    sprite('kk431_15', 3)
    EndMomentum(1)
    physicsYImpulse(1200)
    label(1)
    sprite('kk431_12', 3)
    sprite('kk431_13', 3)
    sprite('kk431_14', 3)
    sprite('kk431_15', 3)
    YAccel(-100)
    if not SLOT_2:
        setInvincible(0)
    gotoLabel(1)
    label(10)
    sprite('keep', 3)
    clearUponHandler(17)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(41)
    SLOT_7 = 2
    TriggerUponForState('efkk_GravityBall', 33)
    TriggerUponForState('efkk_AtkGravityBall', 34)
    sprite('kk431_16', 4)
    sprite('kk431_17', 4)
    physicsYImpulse(4000)
    setGravity(200)
    sprite('kk431_18', 3)
    sprite('kk431_19', 3)
    sprite('kk431_20', 3)
    sprite('kk431_18', 3)
    sprite('kk431_19', 3)
    sprite('kk431_20', 3)
    sprite('kk431_21', 3)
    sprite('kk020_06', 3)
    PerGravity(1000)
    label(13)
    sprite('kk020_07', 3)
    sprite('kk020_08', 3)
    loopRest()
    gotoLabel(13)
    label(0)
    sprite('kk024_00', 2)
    sprite('kk024_01', 2)
    sprite('kk024_02', 4)
    sprite('kk024_03', 2)
    sprite('kk024_04', 2)


@State
def UltimateBlackhole_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        PreventBlocking(1)
        EndMomentum(1)
        EnableRapidCancel(0)
        setInvincible(1)
        ExternalForcesRate(0, 0)
        AttackType(4)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 0)

        def upon_41():
            clearUponHandler(41)
            clearUponHandler(17)
            SLOT_7 = 2
            SetActionMark(1)
            setInvincible(1)
        uponSendToLabel(35, 10)
        RunLoopUpon(17, 267)

        def upon_17():
            clearUponHandler(17)
            clearUponHandler(41)
            TriggerUponForState('efkk_GravityBall', 33)
            TriggerUponForState('efkk_AtkGravityBall_OD', 34)
            sendToLabel(10)
        SLOT_7 = 2
        SLOT_63 = 0

        def upon_14():
            clearUponHandler(41)
            TriggerUponForState('efkk_GravityBall', 33)
            TriggerUponForState('efkk_AtkGravityBall_OD', 34)

        def upon_STATE_END():
            SLOT_7 = 0
        callSubroutine('Delete_hole')
    sprite('kk431_00', 4)
    sprite('kk431_01', 4)
    sprite('kk431_02', 4)
    sprite('kk431_03', 40)
    Voiceline('kk251')
    CreateObject('efkk_GravityBall', -1)
    sprite('kk431_04', 5)
    DistortionSettings(56, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)
    sprite('kk431_05', 5)
    sprite('kk431_06', 5)
    sprite('kk431_07', 5)
    sprite('kk431_08', 5)
    sprite('kk431_09', 5)
    sprite('kk431_10', 5)
    sprite('kk431_11', 3)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    setGravity(-100)
    TriggerUponForState('efkk_GravityBall', 32)
    CreateObject('efkk_AtkGravityBall_OD', -1)
    SLOT_7 = 1
    TriggerUponForState('efkk_Drive', 37)
    TriggerUponForState('efkk_Drive_OD', 37)
    sprite('kk431_12', 3)
    sprite('kk431_13', 3)
    sprite('kk431_14', 3)
    sprite('kk431_15', 3)
    EndMomentum(1)
    physicsYImpulse(1200)
    sprite('kk431_12', 3)
    sprite('kk431_13', 3)
    sprite('kk431_14', 3)
    sprite('kk431_15', 3)
    YAccel(-100)
    if not SLOT_2:
        setInvincible(0)
    label(1)
    sprite('kk431_12', 2)
    sprite('kk431_13', 2)
    sprite('kk431_14', 2)
    sprite('kk431_15', 2)
    YAccel(-100)
    gotoLabel(1)
    label(10)
    sprite('keep', 3)
    clearUponHandler(17)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(41)
    SLOT_7 = 2
    TriggerUponForState('efkk_GravityBall', 33)
    TriggerUponForState('efkk_AtkGravityBall_OD', 34)
    sprite('kk431_16', 4)
    sprite('kk431_17', 4)
    physicsYImpulse(4000)
    setGravity(200)
    if not SLOT_2:
        setInvincible(0)
    sprite('kk431_18', 3)
    sprite('kk431_19', 3)
    sprite('kk431_20', 3)
    sprite('kk431_18', 3)
    sprite('kk431_19', 3)
    sprite('kk431_20', 3)
    sprite('kk431_21', 3)
    sprite('kk020_06', 3)
    PerGravity(1000)
    label(13)
    sprite('kk020_07', 3)
    sprite('kk020_08', 3)
    loopRest()
    gotoLabel(13)
    label(0)
    sprite('kk024_00', 2)
    sprite('kk024_01', 2)
    sprite('kk024_02', 4)
    sprite('kk024_03', 2)
    sprite('kk024_04', 2)


@State
def UltimateLaser():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(1)
        setInvincible(1)
        PreventSelfPush(1)
        EnableRapidCancel(0)
        callSubroutine('Delete_hole')
    sprite('kk432_00', 2)
    sprite('kk432_01', 2)
    sprite('kk432_02', 3)
    Voiceline('kk253')
    DistortionSettings(60, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    CreateObject('vrkkef432_Land', -1)
    CreateObject('efkk_BigTager', -1)
    ObjectUpon(STATE_END, 41)
    sprite('kk432_03', 3)
    SetBackground(2)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_02', 3)
    sprite('kk432_03', 3)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_02', 3)
    sprite('kk432_03', 3)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_06', 3)
    setInvincible(0)
    sprite('kk432_07', 3)
    sprite('kk432_08', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    RunLoopUpon(17, 180)

    def upon_17():
        sendToLabel(2)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    uponSendToLabel(RELEASE_C, 2)
    SLOT_51 = 6
    label(1)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    SLOT_51 = SLOT_51 + 1

    def upon_EVERY_FRAME():
        if CheckInput(0xca):
            SLOT_52 = SLOT_52 + 1
    gotoLabel(1)
    label(2)
    clearUponHandler(17)
    clearUponHandler(RELEASE_C)
    clearUponHandler(EVERY_FRAME)
    SLOT_52 = SLOT_52 / 6
    SLOT_51 = SLOT_51 + SLOT_52
    sprite('kk432_09', 3)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    setInvincible(1)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_13', 3)
    sprite('kk432_14', 3)
    sprite('kk432_15', 3)
    Voiceline('kk254')
    TriggerUponForState('vrkkef432_Land', 32)
    sprite('kk432_16', 3)
    sprite('kk432_17', 3)
    sprite('kk432_18', 3)
    TriggerUponForState('efkk_BigTager', 32)
    sprite('kk432_19', 3)
    CreateObject('efkk_BigTagerAtk', -1)
    label(10)
    sprite('kk432_20', 2)
    sprite('kk432_21', 2)
    sprite('kk432_22', 2)
    sprite('kk432_23', 1)
    sprite('kk432_23', 1)
    SLOT_51 = SLOT_51 + -1
    if SLOT_51:
        conditionalSendToLabel(10)
    sprite('kk432_20', 3)
    setInvincible(0)
    TriggerUponForState('efkk_BigTagerAtk', 32)
    TriggerUponForState('efkk_Beam00', 32)
    sprite('kk432_21', 3)
    sprite('kk432_22', 3)
    sprite('kk432_23', 3)
    sprite('kk432_20', 4)
    sprite('kk432_21', 4)
    sprite('kk432_22', 4)
    sprite('kk432_23', 4)
    sprite('kk432_20', 5)
    sprite('kk432_21', 5)
    sprite('kk432_22', 5)
    sprite('kk432_23', 5)
    sprite('kk432_20', 6)
    TriggerUponForState('efkk_BigTager', 33)
    sprite('kk432_21', 6)
    sprite('kk432_22', 6)
    sprite('kk432_23', 6)
    TriggerUponForState('vrkkef432_Land', 33)
    sprite('kk432_24', 6)
    sprite('kk432_25', 6)
    sprite('kk432_26', 6)


@State
def UltimateLaser_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(1)
        setInvincible(1)
        PreventSelfPush(1)
        EnableRapidCancel(0)
        callSubroutine('Delete_hole')
        AttackType(4)
    sprite('kk432_00', 2)
    sprite('kk432_01', 2)
    sprite('kk432_02', 3)
    Voiceline('kk255')
    DistortionSettings(72, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    CreateObject('vrkkef432_Land', -1)
    CreateObject('efkk_ODBigTager', -1)
    ObjectUpon(STATE_END, 41)
    sprite('kk432_03', 3)
    SetBackground(2)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_02', 3)
    sprite('kk432_03', 3)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_02', 3)
    sprite('kk432_03', 3)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_02', 3)
    sprite('kk432_03', 3)
    sprite('kk432_04', 3)
    sprite('kk432_05', 3)
    sprite('kk432_06', 3)
    setInvincible(0)
    sprite('kk432_07', 3)
    sprite('kk432_08', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    RunLoopUpon(17, 216)

    def upon_17():
        sendToLabel(2)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    uponSendToLabel(RELEASE_C, 2)
    SLOT_51 = 6
    label(1)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    SLOT_51 = SLOT_51 + 1

    def upon_EVERY_FRAME():
        if CheckInput(0xca):
            SLOT_52 = SLOT_52 + 1
    gotoLabel(1)
    label(2)
    clearUponHandler(17)
    clearUponHandler(RELEASE_C)
    clearUponHandler(EVERY_FRAME)
    SLOT_52 = SLOT_52 / 6
    SLOT_51 = SLOT_51 + SLOT_52
    sprite('kk432_09', 3)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    setInvincible(1)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_13', 3)
    sprite('kk432_14', 3)
    sprite('kk432_15', 3)
    Voiceline('kk256')
    TriggerUponForState('vrkkef432_Land', 32)
    sprite('kk432_16', 3)
    sprite('kk432_17', 3)
    sprite('kk432_18', 3)
    TriggerUponForState('efkk_ODBigTager', 32)
    sprite('kk432_19', 3)
    CreateObject('efkk_BigTagerAtk_OD', -1)
    label(10)
    sprite('kk432_20', 2)
    sprite('kk432_21', 2)
    sprite('kk432_22', 2)
    sprite('kk432_23', 1)
    sprite('kk432_23', 1)
    SLOT_51 = SLOT_51 + -1
    if SLOT_51:
        conditionalSendToLabel(10)
    sprite('kk432_20', 3)
    setInvincible(0)
    TriggerUponForState('efkk_BigTagerAtk_OD', 32)
    TriggerUponForState('efkk_ODBeam00', 32)
    sprite('kk432_21', 3)
    sprite('kk432_22', 3)
    sprite('kk432_23', 3)
    sprite('kk432_20', 4)
    sprite('kk432_21', 4)
    sprite('kk432_22', 4)
    sprite('kk432_23', 4)
    sprite('kk432_20', 5)
    sprite('kk432_21', 5)
    sprite('kk432_22', 5)
    sprite('kk432_23', 5)
    sprite('kk432_20', 6)
    TriggerUponForState('efkk_ODBigTager', 33)
    sprite('kk432_21', 6)
    sprite('kk432_22', 6)
    sprite('kk432_23', 6)
    TriggerUponForState('vrkkef432_Land', 33)
    sprite('kk432_24', 6)
    sprite('kk432_25', 6)
    sprite('kk432_26', 6)


@State
def UltimateAirLaser():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        EndMomentum(1)
        ForcedLandingRecovery(0, 1)
        PreventSelfPush(1)
        EnableRapidCancel(0)
        callSubroutine('Delete_hole')
    sprite('kk432_27', 2)
    sprite('kk432_28', 2)
    sprite('kk432_29', 3)
    Voiceline('kk253')
    DistortionSettings(60, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    CreateObject('efkk_BigTager', -1)
    setInvincible(1)
    sprite('kk432_30', 3)
    SetBackground(2)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    sprite('kk432_29', 3)
    sprite('kk432_30', 3)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    setInvincible(0)
    sprite('kk432_29', 3)
    CreateObject('vrkkef432_Air', -1)
    setInvincible(1)
    sprite('kk432_30', 3)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    sprite('kk432_33', 3)
    sprite('kk432_34', 3)
    sprite('kk432_35', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_13', 3)
    sprite('kk432_14', 3)
    sprite('kk432_15', 3)
    TriggerUponForState('vrkkef432_Air', 32)
    sprite('kk432_16', 3)
    sprite('kk432_17', 3)
    sprite('kk432_18', 3)
    TriggerUponForState('efkk_BigTager', 32)
    sprite('kk432_19', 3)
    CreateObject('efkk_BigTagerAtk', -1)
    ObjectUpon(STATE_END, 33)
    label(10)
    sprite('kk432_20', 2)
    sprite('kk432_21', 2)
    sprite('kk432_22', 2)
    sprite('kk432_23', 1)
    sprite('kk432_23', 1)
    AddActionMark(1)
    if not SLOT_2 >= 8:
        sendToLabel(10)
    sprite('kk432_20', 3)
    setInvincible(0)
    TriggerUponForState('efkk_BigTagerAtk', 32)
    TriggerUponForState('efkk_Beam00', 32)
    sprite('kk432_21', 3)
    sprite('kk432_22', 3)
    sprite('kk432_23', 3)
    sprite('kk432_20', 4)
    sprite('kk432_21', 4)
    sprite('kk432_22', 4)
    sprite('kk432_23', 4)
    sprite('kk432_20', 5)
    sprite('kk432_21', 5)
    sprite('kk432_22', 5)
    sprite('kk432_23', 5)
    sprite('kk432_20', 6)
    TriggerUponForState('efkk_BigTager', 33)
    TriggerUponForState('vrkkef432_Air', 33)
    sprite('kk432_21', 6)
    sprite('kk432_22', 6)
    sprite('kk432_36', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(12000)
    setGravity(1000)
    sprite('kk432_37', 4)
    sprite('kk020_06', 4)
    label(13)
    sprite('kk020_07', 4)
    XImpulseAcceleration(80)
    sprite('kk020_08', 4)
    loopRest()
    gotoLabel(13)


@State
def UltimateAirLaser_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        EndMomentum(1)
        ForcedLandingRecovery(0, 1)
        PreventSelfPush(1)
        EnableRapidCancel(0)
        callSubroutine('Delete_hole')
        AttackType(4)
    sprite('kk432_27', 2)
    sprite('kk432_28', 2)
    sprite('kk432_29', 3)
    Voiceline('kk255')
    DistortionSettings(60, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    HeatChange(-5000)
    CreateObject('EMB_KK', -1)

    def RunOnObject_1():
        RenderLayer(2)
    CreateObject('efkk_ODBigTager', -1)
    setInvincible(1)
    sprite('kk432_30', 3)
    SetBackground(2)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    sprite('kk432_29', 3)
    sprite('kk432_30', 3)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    sprite('kk432_29', 3)
    sprite('kk432_30', 3)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    setInvincible(0)
    sprite('kk432_29', 3)
    CreateObject('vrkkef432_Air', -1)
    setInvincible(1)
    sprite('kk432_30', 3)
    sprite('kk432_31', 3)
    sprite('kk432_32', 3)
    sprite('kk432_33', 3)
    sprite('kk432_34', 3)
    sprite('kk432_35', 3)
    sprite('kk432_09', 3)
    sprite('kk432_10', 3)
    sprite('kk432_11', 3)
    sprite('kk432_12', 3)
    sprite('kk432_13', 3)
    sprite('kk432_14', 3)
    sprite('kk432_15', 3)
    TriggerUponForState('vrkkef432_Air', 32)
    sprite('kk432_16', 3)
    sprite('kk432_17', 3)
    sprite('kk432_18', 3)
    TriggerUponForState('efkk_ODBigTager', 32)
    sprite('kk432_19', 3)
    CreateObject('efkk_BigTagerAtk_OD', -1)
    ObjectUpon(STATE_END, 33)
    sprite('kk432_16', 3)
    sprite('kk432_17', 3)
    sprite('kk432_18', 3)
    label(10)
    sprite('kk432_20', 2)
    sprite('kk432_21', 2)
    sprite('kk432_22', 2)
    sprite('kk432_23', 1)
    sprite('kk432_23', 1)
    AddActionMark(1)
    if not SLOT_2 >= 8:
        sendToLabel(10)
    sprite('kk432_20', 3)
    setInvincible(0)
    TriggerUponForState('efkk_BigTagerAtk_OD', 32)
    TriggerUponForState('efkk_ODBeam00', 32)
    AddCombo(5)
    sprite('kk432_21', 3)
    sprite('kk432_22', 3)
    sprite('kk432_23', 3)
    sprite('kk432_20', 4)
    sprite('kk432_21', 4)
    sprite('kk432_22', 4)
    sprite('kk432_23', 4)
    sprite('kk432_20', 5)
    sprite('kk432_21', 5)
    sprite('kk432_22', 5)
    sprite('kk432_23', 5)
    sprite('kk432_20', 6)
    TriggerUponForState('efkk_ODBigTager', 33)
    TriggerUponForState('vrkkef432_Air', 33)
    sprite('kk432_21', 6)
    sprite('kk432_22', 6)
    sprite('kk432_36', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(12000)
    setGravity(1000)
    sprite('kk432_37', 4)
    sprite('kk020_06', 4)
    label(13)
    sprite('kk020_07', 4)
    XImpulseAcceleration(80)
    sprite('kk020_08', 4)
    loopRest()
    gotoLabel(13)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(9999)
        Crumple(200)
        DamageFromStateOnly('BurstDD_missile')
        Blockstun(26)
        Hitstop(20)
        OppMovementUnlock(1)
        OppPositionOnHit(1, 180000, 0)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            PushbackX(100000)
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('kk440_00', 3)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('kk280')
    sprite('kk440_01', 3)
    sprite('kk440_02', 7)
    sprite('kk440_03', 2)
    physicsXImpulse(5000)
    sprite('kk440_04', 2)
    XImpulseAcceleration(200)
    CommonSE('004_swing_grap_1_2')
    sprite('kk440_05', 2)
    XImpulseAcceleration(600)
    sprite('kk400_25ex01', 3)
    CreateParticle('kkef440_shotei', 0)
    XImpulseAcceleration(30)
    sprite('kk400_26ex01', 6)
    XImpulseAcceleration(0)
    setInvincible(0)
    sprite('kk400_27ex01', 6)
    sprite('kk400_28ex01', 6)
    sprite('kk400_29ex01', 4)
    sprite('kk400_30ex01', 4)
    sprite('kk400_31ex01', 4)
    sprite('kk400_32ex01', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(9999)
        Crumple(200)
        DamageFromStateOnly('BurstDD_missile')
        Blockstun(26)
        Hitstop(20)
        OppMovementUnlock(1)
        OppPositionOnHit(1, 180000, 0)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            PushbackX(100000)
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('kk440_00', 1)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('kk280')
    sprite('kk440_01', 1)
    sprite('kk440_02', 1)
    sprite('kk440_03', 2)
    physicsXImpulse(5000)
    sprite('kk440_04', 2)
    XImpulseAcceleration(200)
    CommonSE('004_swing_grap_1_2')
    sprite('kk440_05', 2)
    XImpulseAcceleration(600)
    sprite('kk400_25ex01', 3)
    CreateParticle('kkef440_shotei', 0)
    XImpulseAcceleration(30)
    sprite('kk400_26ex01', 6)
    XImpulseAcceleration(0)
    setInvincible(0)
    sprite('kk400_27ex01', 6)
    sprite('kk400_28ex01', 6)
    sprite('kk400_29ex01', 4)
    sprite('kk400_30ex01', 4)
    sprite('kk400_31ex01', 4)
    sprite('kk400_32ex01', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(60)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(200)
        Wallbounce(1)
        WallbounceReboundTime(5)
        HardKnockdown(1)
        Hitstop(1)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDAdd')
        OppMovementUnlock(1)
        MinimumDamage(10)
        SetXCollisionFromOrigin(200)
        StayAfterMovement(1, 0)
        SetBackground(1)
    sprite('kk400_25ex01', 3)
    StartMultihit()
    SetXCollisionFromOrigin(250)
    sprite('kk400_26ex01', 3)
    SetXCollisionFromOrigin(300)
    sprite('kk400_27ex01', 3)
    SetXCollisionFromOrigin(350)
    sprite('kk400_28ex01', 3)
    SetXCollisionFromOrigin(400)
    sprite('kk400_29ex01', 3)
    sprite('kk400_30ex01', 3)
    sprite('kk400_31ex01', 3)
    sprite('kk400_32ex01', 3)
    sprite('kk333_00ex01', 4)
    sprite('kk333_01ex01', 4)
    Voiceline('kk281')
    sprite('kk333_02ex01', 4)
    sprite('kk333_03ex01', 4)
    sprite('kk333_04ex01', 4)
    sprite('kk440_06', 6)
    CommonSE('024_getset_b')
    sprite('kk440_07', 6)
    CreateParticle('kkef440_kira', 0)
    AltKnockdownEffects(100, 1, 0)
    sprite('kk440_08', 40)
    PrivateSE('kkse_20')
    sprite('kk440_09', 3)
    sprite('kk440_10', 3)
    if SLOT_51:
        SetActionMark(8)
    else:
        SetActionMark(4)
    CreateObject('efkk440_MissileFire', 0)

    def RunOnObject_1():
        Rotation(1000)
        AddY(7000)
    CreateObject('efkk440_MissileFire', 1)

    def RunOnObject_1():
        Rotation(-8000)
        AddX(-10000)
        AddY(10000)
    CreateObject('efkk440_MissileFire', 2)

    def RunOnObject_1():
        Size(600)
        Rotation(-12000)
    CreateObject('efkk440_MissileFire', 3)

    def RunOnObject_1():
        Size(800)
        Rotation(45000)
        AddY(10000)
    label(1)
    sprite('kk440_11', 4)
    CreateObject('BurstDD_missile', 0)
    PrivateSE('kkse_24')
    sprite('kk440_12', 4)
    CreateObject('BurstDD_missile', 5)
    sprite('kk440_13', 4)
    CreateObject('BurstDD_missile', 11)
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1)
    sprite('kk440_11', 4)
    CreateObject('BurstDD_missile', -1)
    ObjectUpon(STATE_END, 32)

    def RunOnObject_1():
        AddY(300000)
        DeviationY(-25000, 25000)
    sprite('kk440_12', 4)
    CreateObject('BurstDD_missile2', -1)

    def RunOnObject_1():
        AddY(200000)
        DeviationY(-25000, 25000)
    sprite('kk440_13', 4)
    physicsXImpulse(0)
    sprite('kk440_11', 3)
    TriggerUponForState('efkk440_MissileFire', 32)
    DespawnEAEffect('BurstDD_AtkMatome')
    sprite('kk440_12', 3)
    sprite('kk440_13', 3)
    sprite('kk440_14', 3)
    sprite('kk440_15', 3)
    sprite('kk440_16', 3)
    Voiceline('kk282')
    CreateObject('efkk440_PartsA', 0)
    CreateObject('efkk440_PartsB', 1)
    CreateObject('efkk440_PartsC', 2)
    CreateObject('efkk440_PartsD', 3)
    CreateObject('efkk440_ThunderTame', 4)
    CreateObject('efkk440_ThunderTame', 5)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_16', 3)
    sprite('kk440_17', 3)
    sprite('kk440_18', 3)
    sprite('kk440_19', 3)
    TriggerUponForState('efkk440_ThunderTame', 32)
    sprite('kk440_20', 3)
    Voiceline('kk283')
    if SLOT_51:
        SetActionMark(15)
    else:
        SetActionMark(5)
    CreateObject('BurstDD_thunderball', -1)
    DespawnEAEffect('efkk440_ThunderTame')
    label(2)
    sprite('kk440_21', 2)
    RefreshMultihit()
    HitsparkSize(0)
    sprite('kk440_22', 2)
    RefreshMultihit()
    sprite('kk440_23', 2)
    RefreshMultihit()
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2)
    sprite('keep', 1)
    OppPositionOnHit(0, 0, 0)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackX(8000)
    UseFireHitspark(1)
    DefeatOpponentBehavior(0)
    if not SLOT_51:
        notConditionalSendToLabel(3)
    sprite('kk440_21', 4)
    CreateObject('BurstDDEx_SmokeBody', -1)
    DespawnEAEffect('BurstDD_thunderball')
    TriggerUponForState('BurstDD_Camera', 32)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    Visibility(1)
    sprite('kk440_21', 30)
    RefreshMultihit()
    Damage(1000)
    AirPushbackY(68000)
    Hitstop(0)
    HardKnockdown(30)
    sprite('kk400_37ex01', 30)
    Visibility(0)
    CreateObject('efkk440_Koge', -1)
    AddX(-110000)
    sprite('kk400_37ex01', 60)
    Voiceline('kk285')
    sprite('kk400_38ex01', 6)
    loopRest()
    ExitState()
    label(3)
    sprite('kk440_21', 4)
    RefreshMultihit()
    Damage(600)
    AirPushbackY(40000)
    Hitstop(8)
    HardKnockdown(1)
    TriggerUponForState('BurstDD_thunderball', 32)
    sprite('kk440_22', 4)
    sprite('kk440_23', 4)
    sprite('kk440_21', 4)
    if CharacterIDCheck('ph'):
        Voiceline('kk284')
    sprite('kk440_21', 6)
    sprite('kk440_22', 4)
    sprite('kk440_23', 4)
    sprite('kk440_21', 6)
    sprite('kk440_22', 6)
    sprite('kk440_23', 6)
    if not CharacterIDCheck('ph'):
        Voiceline('kk284')
    sprite('kk401_36ex01', 6)
    CreateObject('efkk440_Parts2A', 0)
    CreateObject('efkk440_Parts2B', 1)
    CreateObject('efkk440_Parts2D', 2)
    CreateObject('efkk440_Parts2C', 3)
    sprite('kk404_06ex03', 6)
    sprite('kk404_07ex03', 6)
    sprite('kk404_08ex03', 6)
    sprite('kk404_09ex03', 12)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AstralHeat_2nd', 5, 0, 0)
        RangeCheck(90000)
        DistanceCheck(250000, 1, -1, -1)

        def upon_EVERY_FRAME():
            if SLOT_2 > 3:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(0)
        DefeatOpponentBehavior(1)
        callSubroutine('Delete_hole')
    sprite('kk450_00', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 0, 0)
    sprite('kk450_01', 3)
    sprite('kk450_02', 3)
    Voiceline('kk290')
    sprite('kk450_03', 3)
    DistortionSettings(55, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KK_AH', -1)
    label(1)
    sprite('kk450_04', 3)
    sprite('kk450_01', 3)
    sprite('kk450_02', 3)
    sprite('kk450_03', 3)
    AddActionMark(1)
    gotoLabel(1)
    label(0)
    sprite('kk450_04', 3)
    sprite('kk450_05', 3)
    StartMultihit()
    CommonSE('010_swing_sword_0')
    sprite('kk450_06', 12)
    sprite('kk450_05', 3)
    setInvincible(0)
    sprite('kk450_04', 3)
    sprite('kk450_03', 3)
    sprite('kk450_02', 3)
    sprite('kk450_01', 3)
    sprite('kk450_00', 3)


@State
def AstralHeat_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(5, 0, 0)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Hitstop(1)
        EnemyHitstopAddition(1000, 1000, 1000)
        Hitstun(1000)
        DamageFromStateOnly('AstralHeat_3rd')
        DefeatOpponentBehavior(1)
        Damage(0)
        DamageEffect(5, '')
        TriggerUponForState('efkk_Drive', 37)
        TriggerUponForState('efkk_Drive_OD', 37)
        TriggerUponForState('efkk_403_TrapA', 41)
        TriggerUponForState('efkk_403_TrapB', 41)
        TriggerUponForState('efkk_fireball_Hontai', 41)
        TriggerUponForState('efkk_UltraSokidan_Hontai', 41)
        TriggerUponForState('efkk_UltraSokidan_Hontai_OD', 41)
    sprite('kk450_06', 25)
    AttackOff()
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('kk450_06', 2)
    PlayPlayAstralBGM(0)
    RefreshMultihit()
    sprite('kk450_06', 1)
    enterState('AstralHeat_3rd')


@State
def AstralHeat_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(5, 0, 0)
        Hitstun(1000)
        AirUntechableTime(1000)
        Hitstop(0)
        PushbackX(0)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        NoDamageAction(1)
        ScreenCollision(1)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeat_3rd')
        AstralHeatCleanup(1, 1)
        HitAnywhere(1)
        ForceFaceSprite()
        HUDVisibillity(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        AttackLevel_(3)
        Damage(150)
        HitsparkSize(700)
    sprite('kk450_07', 3)
    Voiceline('kk291')
    sprite('kk450_08', 2)
    RefreshMultihit()
    sprite('kk450_09', 2)
    sprite('kk450_10', 2)
    RefreshMultihit()
    sprite('kk450_11', 2)
    RefreshMultihit()
    sprite('kk450_12', 2)
    sprite('kk450_13', 2)
    RefreshMultihit()
    sprite('kk450_14', 2)
    RefreshMultihit()
    sprite('kk450_15', 2)
    sprite('kk450_16', 2)
    RefreshMultihit()
    sprite('kk450_08', 2)
    RefreshMultihit()
    sprite('kk450_09', 2)
    sprite('kk450_10', 2)
    RefreshMultihit()
    sprite('kk450_11', 2)
    RefreshMultihit()
    sprite('kk450_12', 2)
    sprite('kk450_13', 2)
    RefreshMultihit()
    sprite('kk450_14', 2)
    RefreshMultihit()
    sprite('kk450_15', 2)
    sprite('kk450_16', 2)
    RefreshMultihit()
    sprite('kk450_08', 2)
    RefreshMultihit()
    sprite('kk450_09', 2)
    sprite('kk450_10', 2)
    RefreshMultihit()
    sprite('kk450_11', 2)
    RefreshMultihit()
    sprite('kk450_12', 2)
    sprite('kk450_13', 2)
    RefreshMultihit()
    sprite('kk450_14', 2)
    RefreshMultihit()
    sprite('kk450_15', 2)
    sprite('kk450_16', 2)
    RefreshMultihit()
    sprite('kk450_08', 2)
    RefreshMultihit()
    sprite('kk450_09', 2)
    sprite('kk450_10', 2)
    RefreshMultihit()
    sprite('kk450_11', 2)
    RefreshMultihit()
    sprite('kk450_12', 2)
    sprite('kk450_13', 2)
    RefreshMultihit()
    sprite('kk450_14', 2)
    RefreshMultihit()
    sprite('kk450_15', 2)
    sprite('kk450_16', 2)
    RefreshMultihit()
    sprite('kk450_17', 5)
    physicsXImpulse(-5000)
    sprite('kk450_18', 5)
    sprite('kk450_19', 5)
    sprite('kk450_20', 5)
    sprite('kk450_21', 5)
    XImpulseAcceleration(0)
    sprite('kk450_22', 2)
    physicsXImpulse(25000)
    sprite('kk450_23', 2)
    sprite('kk450_24', 3)
    XImpulseAcceleration(0)
    AttackLevel_(5)
    Damage(500)
    RefreshMultihit()
    PushbackX(120000)
    ScreenShake(50000, 50000)

    def RunOnObject_22():
        EnableCollision(0)
    sprite('kk450_24', 30)
    sprite('kk450_25', 5)

    def RunOnObject_22():
        physicsYImpulse(35000)
    sprite('kk450_26', 5)
    sprite('kk450_27', 5)

    def RunOnObject_22():
        physicsYImpulse(0)
        physicsXImpulse(0)
    sprite('kk450_28', 5)
    sprite('kk450_29', 3)
    CreateObject('efkk_AHJishaku00', -1)
    CameraControlEnable(0)
    CreateObject('450Cam', -1)
    sprite('kk450_30', 3)
    CommonSE('014_electric_m')
    CommonSE('014_electric_sl')
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_s')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    CommonSE('014_electric_m')
    sprite('kk450_29', 3)
    CommonSE('014_electric_sl')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    Voiceline('kk292')
    sprite('kk450_29', 3)
    CommonSE('014_electric_l')
    sprite('kk450_30', 3)
    CommonSE('014_electric_m')
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_ll')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_m')
    sprite('kk450_30', 3)
    CreateObject('efkk_Whiteout', -1)
    sprite('kk450_31', 3)
    CommonSE('014_electric_ml')
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    CommonSE('014_electric_m')
    sprite('kk450_31', 3)
    CommonSE('014_electric_s')
    sprite('kk450_29', 3)
    CommonSE('014_electric_m')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    CommonSE('014_electric_sl')
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    CommonSE('014_electric_l')
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_ll')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    CommonSE('014_electric_m')
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    CommonSE('014_electric_ml')
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_s')
    sprite('kk450_30', 3)
    CommonSE('014_electric_m')
    sprite('kk450_31', 3)
    CommonSE('014_electric_sl')
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    CommonSE('014_electric_l')
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    CommonSE('014_electric_ll')
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    sprite('kk450_31', 3)
    sprite('kk450_29', 3)
    sprite('kk450_30', 3)
    DespawnEAEffect('efkk_AHJishaku00')
    sprite('kk450cutin_00', 4)
    FaceRight()
    TriggerUponForState('450Cam', 33)

    def RunOnObject_22():
        Visibility(1)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    CreateObject('efkk_InsekiEff', -1)
    CommonSE('022_magiccircle_b')
    sprite('kk450cutin_00', 4)
    SetBackground(3)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    Voiceline('kk293')
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    physicsXImpulse(-750)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    if SLOT_44:
        Voiceline('kk294')
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('kk450cutin_00', 4)
    BlendMode_Normal()
    ConstantAlphaModifier(-26)
    sprite('kk450cutin_01', 4)
    sprite('kk450cutin_02', 4)
    sprite('kk450cutin_03', 4)
    sprite('null', 32)
    sprite('null', 144)
    if SLOT_43:
        Voiceline('kk294')
    sprite('kk450cutin_01', 20)
    Visibility(1)
    physicsXImpulse(0)
    Unknown20010(-5000, 0, 0)
    CreateParticle('kkef450kirikae_01', -1)
    TriggerUponForState('450Cam', 32)

    def RunOnObject_22():
        AlphaValue(0)
    sprite('kk450cutin_01', 60)
    if SLOT_43:
        Voiceline('kk295')
    CreateParticle('kkef450planetend_00', -1)
    sprite('kk450cutin_01', 60)
    if SLOT_44:
        Voiceline('kk295')
    sprite('kk450cutin_00', 1)
    RefreshMultihit()
    Damage(33000)
    DefeatOpponentBehavior(3)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    OppPositionOnHit(2, 0, 1000)
    Hitstop(0)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpulseBeforeWallbounce(0)
    HitAnywhere(1)
    DespawnEAEffect('450Cam')
    SetBackground(2)
    TriggerUponForState('450Shake2', 32)
    PrivateSE('kkse_30')
    PrivateSE('kkse_30')
    sprite('kk450cutin_00', 99)
    XPositionRelativeFacing(0)
    sprite('kk333_05', 4)
    CameraControlEnable(1)
    CameraFast(1)
    CameraPosition(1000)
    CreateObject('efkk_WinBG', -1)
    Visibility(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    sprite('kk333_05', 4)
    WinAction()
    DemoTimer(150)
    Voiceline('kk300')
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    label(0)
    sprite('kk333_05', 4)
    sprite('kk333_06', 4)
    sprite('kk333_07', 4)
    loopRest()
    gotoLabel(0)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('kk054')
    sprite('kk900_00', 32767)
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
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(220000)
    sprite('kk901_00', 50)
    physicsYImpulse(-150)
    sprite('kk901_00', 50)
    physicsYImpulse(150)
    Voiceline('kk055')
    label(0)
    sprite('kk901_00', 50)
    physicsYImpulse(-150)
    sprite('kk901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk055', 13921, 13923, 13921, 13923, 13665, 13667, 13665, 
        13667, 13921, 13923, 13921, 13923, 14177, 14179, 14177, 13155, 
        24880, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0)
    Unknown18011('kk300', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk400', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('kk401', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('kk404', 13921, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('kk405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk406', 13921, 13923, 13921, 13411, 24884, 25397, 24885, 
        25398, 24887, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk407', 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk408', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 55, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk411', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk412', 13921, 13923, 13921, 13923, 13921, 12899, 24880, 
        25398, 24886, 25398, 24886, 25398, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk413', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk414', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13665, 13667, 13665, 13667, 13665, 13923, 
        13921, 13923, 13921, 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk415', 14179, 14177, 12899, 24880, 25398, 24886, 25398, 
        24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kk416', 13409, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('kk417', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk300', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk400', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk401', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk404', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('kk405', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('kk406', 14177, 13155, 24888, 25399, 24887, 25398, 
            24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk407', 14177, 14179, 14177, 14179, 14177, 14179, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk408', 12641, 25392, 24888, 12337, 14435, 12641, 
            25394, 24888, 12849, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk411', 14177, 14179, 14177, 12899, 24888, 25399, 
            24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk412', 12641, 25394, 12849, 13921, 13923, 13921, 
            13923, 13921, 12899, 24880, 25398, 24886, 25398, 24886, 25398, 
            24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk413', 14177, 14179, 14177, 14179, 14177, 14179, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('kk414', 12643, 24880, 12849, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 
            13923, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk415', 13921, 13923, 13921, 12643, 24885, 25399, 
            24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk416', 12641, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kk417', 14177, 14179, 14177, 13155, 24880, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('tg'):
            Unknown18011('kk000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kk400', 13921, 13155, 24880, 25398, 24886, 25398,
                24886, 25398, 24886, 25398, 24886, 24886, 25398, 24886, 
                25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ar'):
            Unknown18011('kk000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kk400', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('lc'):
            Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('kk400', 13921, 13923, 13921, 13155, 24880, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13411, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('kk400', 12641, 25394, 24886, 12849, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13411,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk400', 13921, 13923, 13921, 13923, 13921, 13923,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13667,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('kk000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('kk400', 12641, 25394, 24886, 12849, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 13921, 13923, 13921, 13923, 13921, 13411,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tg'):
            if SLOT_138:
                Unknown18011('kk510', 14177, 14179, 14177, 14179, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 24880, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown18011('kk511', 12641, 25392, 13620, 13921, 13923, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
            else:
                Unknown18011('kk510', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13155, 24880, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk511', 12897, 25392, 13620, 12641, 25394, 
                    24886, 25398, 24886, 25398, 24886, 25400, 24888, 25400,
                    24888, 25400, 24888, 25400, 24888, 12338, 14435, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('lc'):
            if SLOT_138:
                Unknown18011('kk512', 14177, 14179, 14177, 14179, 13665, 
                    13667, 13665, 13667, 13665, 13667, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13155, 25392, 24886, 25398,
                    24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk513', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13667, 24880, 25398, 24886,
                    25398, 24886, 25397, 24885, 25397, 24885, 25397, 24885,
                    53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('kk512', 14177, 14179, 14177, 14179, 14177, 
                    13411, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk5130', 14433, 13923, 12641, 25397, 13618, 
                    12641, 25392, 24886, 25398, 24886, 25399, 12337, 14177,
                    14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk5131', 14433, 14435, 14433, 14435, 14433, 
                    14435, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ar'):
            Unknown18011('kk514', 12641, 25392, 24886, 12337, 13923, 12641,
                25392, 24886, 12337, 13923, 12641, 25392, 24886, 12337, 
                13923, 12641, 25392, 24886, 12337, 13923, 12641, 25392, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk515', 13921, 13923, 13921, 13923, 13921, 13923,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('kk536', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13667, 24880, 25398, 
                24886, 25398, 12338, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk537', 13921, 13923, 13921, 13923, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk536', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13667, 24880,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk537', 13923, 24880, 25398, 24886, 25398, 
                    24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398,
                    24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398,
                    24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('bl'):
            Unknown18011('kk542', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk543', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13667, 14433, 13667, 14433, 13411, 
                24885, 25400, 24888, 25400, 24886, 25400, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk542', 14177, 14179, 14177, 14179, 14177, 
                    13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk543', 14177, 14179, 14177, 14179, 14177, 
                    13155, 24885, 25400, 24888, 25400, 24886, 25400, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('az'):
            Unknown18011('kk544', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 
                12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk545', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk544', 14177, 14179, 14177, 14179, 14177, 
                    14179, 24880, 25399, 24887, 25399, 12339, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk545', 14177, 14179, 14177, 13411, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('kk546', 14689, 14179, 14689, 14179, 14689, 14179,
                14689, 14179, 14689, 14179, 14689, 14179, 14689, 14179, 
                14689, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk547', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk546', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338,
                    14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
                Unknown18011('kk547', 13921, 13923, 13921, 13923, 13921, 
                    13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('kk550', 12641, 25394, 12341, 14689, 14179, 14689,
                14179, 14689, 14179, 14689, 14179, 14689, 13667, 24885, 
                25401, 24887, 25401, 24887, 25401, 24887, 25399, 24887, 
                25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('kk551', 14177, 14179, 14177, 13923, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 
                25399, 13618, 14177, 14179, 14177, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('kk552', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 14435, 24880, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk553', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                25392, 24886, 25400, 24886, 25400, 24886, 25400, 24886, 
                25400, 24886, 25400, 24886, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk552', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 24885,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk553', 13921, 14691, 48, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rm'):
            Unknown18011('kk554', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk555', 13921, 13923, 13921, 13667, 24880, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk555', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    13923, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('kk558', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 24880, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk559', 13921, 13923, 13921, 13923, 13921, 14179,
                24880, 25401, 24886, 25401, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kk558', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 13411, 24885, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk559', 13921, 13923, 13921, 13923, 13921, 
                    13667, 24885, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            if SLOT_138:
                pass
            else:
                Unknown18011('kk562', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 13923, 24880, 25398, 24886, 25398, 24886, 25398,
                    24886, 25398, 24886, 25398, 24886, 25398, 12338, 13921,
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kk563', 14433, 14435, 14433, 14435, 12641, 
                    25398, 12341, 14177, 14179, 14177, 14179, 13921, 13923,
                    14433, 14435, 12641, 25394, 24887, 25399, 12337, 12641,
                    25392, 12339, 12641, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_140:
                    Unknown18011('kk562', 14177, 14179, 14177, 14179, 14177,
                        14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                        14177, 14179, 13923, 24880, 25398, 24886, 25398, 
                        24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                        25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0)
                    Unknown18011('kk563', 14177, 14179, 14177, 14179, 14177,
                        14179, 14177, 14179, 14177, 14179, 24880, 25399, 
                        24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                        25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                        24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('kk564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 12643, 12336, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk565', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('kk000', 13923, 24884, 25399, 24887, 25399, 24887,
                25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('kk400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk570', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kk571', 14177, 14179, 14177, 14179, 14177, 13923,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        if SLOT_138:
            gotoLabel(150)
        else:
            gotoLabel(1150)
    if CharacterIDCheck('lc'):
        if SLOT_138:
            gotoLabel(160)
        else:
            gotoLabel(1160)
    if CharacterIDCheck('ar'):
        SyncEntry()
        gotoLabel(170)
    if CharacterIDCheck('rl'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2280)
        else:
            gotoLabel(280)
    if CharacterIDCheck('bl'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2310)
        else:
            gotoLabel(310)
    if CharacterIDCheck('az'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2320)
        else:
            gotoLabel(320)
    if CharacterIDCheck('kg'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ce'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    if CharacterIDCheck('rm'):
        SyncEntry()
        gotoLabel(370)
    if CharacterIDCheck('ph'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2390)
        else:
            gotoLabel(390)
    if CharacterIDCheck('mi'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2410)
        else:
            gotoLabel(410)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(20)
    if random_(2, 0, 50):
        conditionalSendToLabel(30)
    label(0)
    sprite('kk600_00', 6)
    sprite('kk600_01', 6)
    sprite('kk600_00ex1a', 6)
    sprite('kk600_01ex1a', 6)
    sprite('kk600_00ex2a', 6)
    sprite('kk600_01ex2a', 6)
    sprite('kk600_00ex3a', 6)
    sprite('kk600_01ex3a', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('kk600_00', 6)
    PrivateSE('kkse_32')
    sprite('kk600_01', 6)
    sprite('kk600_00ex1a', 6)
    Voiceline('kk412')
    sprite('kk600_01ex1a', 6)
    sprite('kk600_00ex2a', 6)
    sprite('kk600_01ex2a', 6)
    sprite('kk600_00ex3a', 6)
    sprite('kk600_01ex3a', 6)
    label(1)
    sprite('kk600_00', 6)
    sprite('kk600_01', 6)
    sprite('kk600_00ex1a', 6)
    sprite('kk600_01ex1a', 6)
    sprite('kk600_00ex2a', 6)
    sprite('kk600_01ex2a', 6)
    sprite('kk600_00ex3a', 6)
    sprite('kk600_01ex3a', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(1)
    sprite('kk600_00', 6)
    sprite('kk600_01', 6)
    sprite('kk600_00ex1a', 6)
    sprite('kk600_01ex1a', 6)
    sprite('kk600_00ex2a', 6)
    sprite('kk600_01ex2a', 6)
    sprite('kk600_00ex3a', 6)
    sprite('kk600_01ex3a', 6)
    sprite('kk600_02', 8)
    sprite('kk600_03', 8)
    sprite('kk600_04', 6)
    sprite('kk600_05', 6)
    sprite('kk600_06', 6)
    Voiceline('kk413')
    sprite('kk600_07', 6)
    sprite('kk600_08', 6)
    sprite('kk600_09', 6)
    if SLOT_43:
        DemoTimer(60)
    else:
        DemoTimer(120)
    loopRest()
    ExitState()
    label(20)
    sprite('kk600_00b', 6)
    sprite('kk600_01b', 6)
    sprite('kk600_00ex1b', 6)
    sprite('kk600_01ex1b', 6)
    sprite('kk600_00ex2b', 6)
    sprite('kk600_01ex2b', 6)
    sprite('kk600_00ex3b', 6)
    sprite('kk600_01ex3b', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('kk600_00b', 6)
    PrivateSE('kkse_32')
    Voiceline('kk414')
    sprite('kk600_01b', 6)
    sprite('kk600_00ex1b', 6)
    sprite('kk600_01ex1b', 6)
    sprite('kk600_00ex2b', 6)
    sprite('kk600_01ex2b', 6)
    sprite('kk600_00ex3b', 6)
    sprite('kk600_01ex3b', 6)
    label(21)
    sprite('kk600_00b', 6)
    sprite('kk600_01b', 6)
    sprite('kk600_00ex1b', 6)
    sprite('kk600_01ex1b', 6)
    sprite('kk600_00ex2b', 6)
    sprite('kk600_01ex2b', 6)
    sprite('kk600_00ex3b', 6)
    sprite('kk600_01ex3b', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(21)
    sprite('kk600_02b', 8)
    sprite('kk600_03b', 8)
    sprite('kk600_04b', 6)
    sprite('kk600_05', 6)
    sprite('kk600_06', 6)
    Voiceline('kk415')
    sprite('kk600_07', 6)
    sprite('kk600_08', 6)
    sprite('kk600_09', 6)
    if SLOT_43:
        DemoTimer(90)
    else:
        DemoTimer(90)
    loopRest()
    ExitState()
    label(30)
    sprite('kk601_00', 6)
    CreateObject('kkef_601', -1)
    label(31)
    sprite('kk601_00ex1', 6)
    sprite('kk601_00ex2', 6)
    sprite('kk601_00ex3', 6)
    sprite('kk601_00ex4', 6)
    sprite('kk601_00ex5', 6)
    sprite('kk601_00ex6', 6)
    sprite('kk601_00ex7', 6)
    sprite('kk601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(31)
    sprite('kk601_00ex1', 6)
    PrivateSE('kkse_33')
    sprite('kk601_00ex2', 6)
    sprite('kk601_00ex3', 6)
    sprite('kk601_00ex4', 6)
    sprite('kk601_00ex5', 6)
    sprite('kk601_00ex6', 6)
    sprite('kk601_00ex7', 6)
    sprite('kk601_00', 6)
    sprite('kk601_00ex1', 6)
    Voiceline('kk416')
    DespawnEAEffect('kkef_601')
    sprite('kk601_01', 8)
    sprite('kk601_02', 8)
    sprite('kk601_03', 26)
    sprite('kk601_04', 8)
    sprite('kk601_05', 8)
    sprite('kk601_06', 8)
    sprite('kk601_07', 6)
    CreateObject('efkk_610_hole_out', -1)
    sprite('kk601_08', 6)
    sprite('kk601_09', 6)
    Voiceline('kk417')
    sprite('kk601_10', 6)
    sprite('kk601_11', 6)
    sprite('kk601_12', 6)
    sprite('kk601_13', 6)
    if SLOT_43:
        DemoTimer(110)
    else:
        DemoTimer(120)
    loopRest()
    ExitState()
    label(150)
    uponSendToLabel(32, 152)
    label(151)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(151)
    label(152)
    sprite('kk001_00', 6)
    clearUponHandler(32)
    SLOT_88 = 960
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 6)
    sprite('kk001_06', 6)
    sprite('kk001_07', 6)
    sprite('kk001_08', 6)
    loopRest()
    sprite('kk000_00', 7)
    Voiceline('kk510')
    DemoTimer(300)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(1150)
    sprite('kk001_02', 7)
    sprite('kk001_03', 7)
    sprite('kk001_04', 7)
    sprite('kk001_03', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1150)
    sprite('kk001_02', 7)
    sprite('kk001_03', 7)
    sprite('kk001_04', 7)
    sprite('kk001_03', 7)
    Voiceline('kk510')
    DemoTimer(300)
    sprite('kk001_02', 7)
    sprite('kk001_03', 7)
    sprite('kk001_04', 7)
    sprite('kk001_05', 7)
    sprite('kk001_06', 7)
    sprite('kk001_07', 7)
    sprite('kk001_08', 7)
    sprite('kk000_00', 7)
    sprite('kk300_00', 6)
    sprite('kk300_01', 6)
    sprite('kk300_02', 6)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 7)
    sprite('kk300_09', 7)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    ObjectUpon(22, 32)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    ExitState()
    label(160)
    uponSendToLabel(32, 162)
    label(161)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(161)
    label(162)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    Voiceline('kk512')
    DemoTimer(220)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(1160)
    sprite('null', 1)
    uponSendToLabel(32, 1161)
    sprite('null', 32767)
    loopRest()
    label(1161)
    sprite('null', 4)
    sprite('kk404_00ex02', 4)
    PrivateSE('kkse_19')
    sprite('kk404_01ex02', 4)
    sprite('kk404_02ex02', 4)
    sprite('kk404_03ex02', 4)
    sprite('kk404_04ex02', 4)
    sprite('kk404_05ex02', 4)
    sprite('kk404_06ex02', 4)
    sprite('kk404_07ex02', 4)
    sprite('kk404_08ex02', 4)
    sprite('kk404_09ex02', 4)
    sprite('keep', 1)
    uponSendToLabel(33, 1163)
    label(1162)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    gotoLabel(1162)
    label(1163)
    sprite('kk300_00', 4)
    Voiceline('kk512')
    DemoTimer(220)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(170)
    uponSendToLabel(32, 172)
    label(171)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(171)
    label(172)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    Voiceline('kk514')
    DemoTimer(220)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(280)
    uponSendToLabel(32, 282)
    label(281)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(281)
    label(282)
    sprite('kk620_00', 6)
    clearUponHandler(32)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk536')
    DemoTimer(250)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    ExitState()
    label(2280)
    sprite('kk333_05', 6)
    sprite('kk333_06', 6)
    sprite('kk333_07', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2280)
    sprite('kk333_05', 6)
    sprite('kk333_06', 6)
    sprite('kk333_07', 6)
    Voiceline('kk536')
    SetActionMark(13)
    label(2281)
    sprite('kk333_05', 6)
    AddActionMark(-1)
    sprite('kk333_06', 6)
    sprite('kk333_07', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2281)
    sprite('kk333_08', 6)
    sprite('kk333_09', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(310)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    if SLOT_17:
        conditionalSendToLabel(310)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk542')
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2310)
    sprite('keep', 1)
    uponSendToLabel(32, 2312)
    label(2311)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    gotoLabel(2311)
    label(2312)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    Voiceline('kk542')
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    DemoTimer(140)
    loopRest()
    ExitState()
    label(320)
    uponSendToLabel(32, 322)
    label(321)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(321)
    label(322)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    Voiceline('kk544')
    DemoTimer(200)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(2320)
    sprite('keep', 2)
    uponSendToLabel(32, 2322)
    label(2321)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(2321)
    label(2322)
    sprite('kk620_00', 6)
    clearUponHandler(32)
    sprite('kk620_01', 6)
    Voiceline('kk544')
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    SetActionMark(4)
    label(2323)
    sprite('kk620_06', 6)
    AddActionMark(-1)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2323)
    sprite('kk620_06', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    ObjectUpon(22, 32)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(330)
    uponSendToLabel(32, 332)
    label(331)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(331)
    label(332)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    Voiceline('kk546')
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    ExitState()
    label(2330)
    sprite('keep', 2)

    def upon_32():
        Voiceline('kk546')
        SetActionMark(1)
        DemoTimer(340)
    label(2331)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2331)
    sprite('kk620_06', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    ExitState()
    label(350)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    if SLOT_17:
        conditionalSendToLabel(350)
    sprite('kk620_06', 6)
    Voiceline('kk550')
    DemoTimer(300)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(360)
    uponSendToLabel(32, 362)
    label(361)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(361)
    label(362)
    sprite('kk300_00', 4)
    clearUponHandler(32)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    Voiceline('kk552')
    DemoTimer(200)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    ExitState()
    label(2360)
    sprite('keep', 1)
    uponSendToLabel(32, 2362)
    label(2361)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(2361)
    label(2362)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    Voiceline('kk552')
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    SetActionMark(4)
    label(2363)
    sprite('kk620_06', 6)
    AddActionMark(-1)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2363)
    sprite('kk620_06', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(370)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    if SLOT_17:
        conditionalSendToLabel(370)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk554')
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(390)
    uponSendToLabel(32, 392)
    label(391)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    gotoLabel(391)
    label(392)
    sprite('kk620_06', 6)
    Voiceline('kk558')
    DemoTimer(250)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    ExitState()
    label(2390)
    sprite('keep', 1)

    def upon_32():
        Voiceline('kk558')
        DemoTimer(230)
        SetActionMark(1)
    label(2391)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2391)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    ExitState()
    label(410)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    if SLOT_17:
        conditionalSendToLabel(410)
    sprite('kk620_06', 6)
    Voiceline('kk562')
    DemoTimer(300)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2410)
    sprite('kk602_00', 20)
    uponSendToLabel(32, 2411)
    sprite('kk602_00', 32767)
    loopRest()
    label(2411)
    sprite('kk602_00', 150)
    Voiceline('kk562')
    sprite('kk602_01', 7)
    sprite('kk602_02', 6)
    sprite('kk602_03', 6)
    sprite('kk602_04', 6)
    SetActionMark(3)
    label(2412)
    sprite('kk602_05', 6)
    AddActionMark(-1)
    sprite('kk602_06', 6)
    sprite('kk602_07', 6)
    sprite('kk602_08', 6)
    sprite('kk602_09', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2412)
    sprite('kk602_10', 7)
    sprite('kk602_11', 7)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(420)
    sprite('kk620_06', 6)

    def upon_32():
        SetActionMark(1)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    label(421)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(421)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    Voiceline('kk564')
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(440)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(440)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    Voiceline('kk570')
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    SetActionMark(3)
    label(441)
    sprite('kk620_06', 6)
    AddActionMark(-1)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(441)
    sprite('kk620_04', 6)
    sprite('kk620_03', 10)
    ObjectUpon(22, 32)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    DemoTimer(30)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('ar'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('lc'):
        conditionalSendToLabel(300)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(100)
    label(482)
    sprite('kk615_00', 8)
    sprite('kk615_01', 7)
    sprite('kk615_02', 7)
    sprite('kk615_01', 6)
    sprite('kk615_02', 6)
    CommonSE('019_cloth_b')
    sprite('kk615_03', 7)
    sprite('kk615_04', 7)
    sprite('kk615_05', 7)
    CommonSE('205_runjump_garden_1')
    sprite('kk615_06', 10)
    sprite('kk615_07', 6)
    sprite('kk615_08', 6)
    if random_(2, 0, 50):
        Voiceline('kk400')
    else:
        Voiceline('kk401')
    DemoEndOnVoiceEnd(1)
    sprite('kk615_09', 7)
    sprite('kk615_10', 7)
    CommonSE('205_runjump_garden_0')
    sprite('kk615_06', 12)
    label(1)
    sprite('kk615_07', 6)
    sprite('kk615_08', 6)
    sprite('kk615_09', 7)
    sprite('kk615_10', 7)
    CommonSE('205_runjump_garden_0')
    sprite('kk615_06', 20)
    loopRest()
    gotoLabel(1)
    label(100)
    sprite('keep', 1)
    CameraControlEnable(1)
    physicsXImpulse(4800)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 370000:
                SetActionMark(0)
                sendToLabel(102)
    sprite('kk030_00', 7)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(101)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('kk010_00', 7)
    EndMomentum(1)
    sprite('kk010_01', 7)
    if random_(2, 0, 50):
        Voiceline('kk400')
    else:
        Voiceline('kk401')
    DemoEndOnVoiceEnd(1)
    label(103)
    sprite('kk010_02', 7)
    sprite('kk010_03', 7)
    sprite('kk010_04', 7)
    sprite('kk010_05', 7)
    sprite('kk010_06', 7)
    sprite('kk010_07', 7)
    sprite('kk010_08', 7)
    sprite('kk010_09', 7)
    sprite('kk010_10', 7)
    sprite('kk010_11', 7)
    sprite('kk010_12', 7)
    sprite('kk010_13', 7)
    loopRest()
    gotoLabel(103)
    label(200)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    if random_(2, 0, 50):
        Voiceline('kk400')
    else:
        Voiceline('kk401')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(201)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(201)
    label(300)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    if random_(2, 0, 50):
        Voiceline('kk400')
    else:
        Voiceline('kk401')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        if SLOT_138:
            gotoLabel(150)
        else:
            gotoLabel(1150)
    if CharacterIDCheck('lc'):
        if SLOT_138:
            gotoLabel(160)
        else:
            gotoLabel(1160)
    if CharacterIDCheck('ar'):
        conditionalSendToLabel(170)
    if CharacterIDCheck('rl'):
        if SLOT_140:
            gotoLabel(2280)
        else:
            gotoLabel(280)
    if CharacterIDCheck('bl'):
        if SLOT_140:
            gotoLabel(2310)
        else:
            gotoLabel(310)
    if CharacterIDCheck('az'):
        if SLOT_140:
            gotoLabel(2320)
        else:
            gotoLabel(320)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ce'):
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    if CharacterIDCheck('rm'):
        if SLOT_140:
            gotoLabel(2370)
        else:
            gotoLabel(370)
    if CharacterIDCheck('ph'):
        if SLOT_140:
            gotoLabel(2390)
        else:
            gotoLabel(390)
    if CharacterIDCheck('mi'):
        if SLOT_140:
            gotoLabel(2410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    sprite('keep', 1)
    if SLOT_109:
        sendToLabel(10)
    if SLOT_123:
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(10)
    sprite('kk610_00', 7)
    sprite('kk610_01', 7)
    sprite('kk610_02', 7)
    sprite('kk610_03', 7)
    sprite('kk610_04', 150)
    Voiceline('kk406')
    sprite('kk610_05', 7)
    sprite('kk610_06', 7)
    sprite('kk610_07', 7)
    sprite('kk610_08', 7)
    sprite('kk610_09', 7)
    sprite('kk610_09', 32767)
    Voiceline('kk407')
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(20)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraNoScreenCollision(1)
    sprite('kk611_00', 6)
    sprite('kk611_01', 6)
    if SLOT_43:
        Voiceline('kk408')
        DemoEndOnVoiceEnd(1)
    sprite('kk611_02', 6)
    sprite('kk611_03', 6)
    sprite('kk611_04', 6)
    sprite('kk611_05', 6)
    ParticleSize(575)
    CallCustomizableParticle('ef_smokes', 0)
    CommonSE('201_walk_garden_2')
    sprite('kk611_06', 6)
    sprite('kk611_06ex01', 2)
    sprite('kk611_06ex02', 2)
    sprite('kk611_06ex03', 2)
    sprite('kk611_06ex04', 4)
    sprite('kk611_06ex05', 4)
    sprite('kk611_06ex06', 4)
    sprite('kk611_07', 6)
    sprite('kk611_08', 6)
    sprite('kk611_09', 6)
    sprite('kk611_10', 6)
    sprite('kk611_11', 6)
    sprite('kk611_12', 6)
    sprite('kk611_13', 13)
    CreateObject('efkk_611', -1)
    sprite('kk611_14', 6)
    CreateObject('efkk_611b', -1)
    sprite('kk611_15', 6)
    physicsXImpulse(4000)
    CreateParticle('kkef_dash', 0)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_16', 3)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_16', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_17', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_17', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    if SLOT_44:
        Voiceline('kk408')
        DemoEndOnVoiceEnd(1)
    sprite('kk611_18', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_18', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    sprite('kk611_16', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    sprite('kk611_17', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    sprite('kk611_18', 3)
    XSpeed(500)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 3)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    PrivateSE('kkse_28')
    label(16)
    sprite('kk611_16', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    sprite('kk611_17', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    sprite('kk611_18', 6)
    CreateParticle('kkef_dash_smoke', 1)
    CreateParticle('kkef_dash', 1)
    loopRest()
    gotoLabel(16)
    ExitState()
    label(150)
    sprite('keep', 1)
    CameraControlEnable(1)
    physicsXImpulse(4800)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 370000:
                SetActionMark(0)
                sendToLabel(152)
    sprite('kk030_00', 7)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(151)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('kk010_00', 7)
    EndMomentum(1)
    sprite('kk010_01', 7)
    Voiceline('kk511')
    DemoEndOnVoiceEnd(1)
    label(153)
    sprite('kk010_02', 7)
    sprite('kk010_03', 7)
    sprite('kk010_04', 7)
    sprite('kk010_05', 7)
    sprite('kk010_06', 7)
    sprite('kk010_07', 7)
    sprite('kk010_08', 7)
    sprite('kk010_09', 7)
    sprite('kk010_10', 7)
    sprite('kk010_11', 7)
    sprite('kk010_12', 7)
    sprite('kk010_13', 7)
    loopRest()
    gotoLabel(153)
    label(1150)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk511')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(1151)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(1151)
    label(160)
    sprite('keep', 1)
    CameraControlEnable(1)
    physicsXImpulse(4800)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 370000:
                SetActionMark(0)
                sendToLabel(162)
    sprite('kk030_00', 7)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(161)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('kk010_00', 7)
    EndMomentum(1)
    sprite('kk010_01', 7)
    Voiceline('kk513')
    DemoEndOnVoiceEnd(1)
    label(163)
    sprite('kk010_02', 7)
    sprite('kk010_03', 7)
    sprite('kk010_04', 7)
    sprite('kk010_05', 7)
    sprite('kk010_06', 7)
    sprite('kk010_07', 7)
    sprite('kk010_08', 7)
    sprite('kk010_09', 7)
    sprite('kk010_10', 7)
    sprite('kk010_11', 7)
    sprite('kk010_12', 7)
    sprite('kk010_13', 7)
    loopRest()
    gotoLabel(163)
    label(1160)
    sprite('keep', 1)
    CameraControlEnable(1)
    physicsXImpulse(4800)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 370000:
                SetActionMark(0)
                sendToLabel(1162)
    sprite('kk030_00', 7)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(1161)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(1161)
    label(1162)
    sprite('kk610_00', 8)
    EndMomentum(1)
    sprite('kk610_01', 7)
    sprite('kk610_02', 6)
    sprite('kk610_03', 7)
    sprite('kk610_04', 10)
    sprite('kk610_04', 250)
    Voiceline('kk5130')
    sprite('kk610_05', 7)
    sprite('kk610_06', 7)
    sprite('kk610_07', 7)
    sprite('kk610_08', 7)
    sprite('kk610_09', 7)
    sprite('kk610_09', 32767)
    Voiceline('kk5131')
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(170)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk515')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)
    loopRest()
    label(280)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk537')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)
    loopRest()
    label(2280)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk537')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(2281)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 7)
    sprite('kk620_06ex02', 7)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(2281)
    label(310)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk543')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)
    loopRest()
    label(2310)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk543')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(2311)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 7)
    sprite('kk620_06ex02', 7)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(2311)
    label(320)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk545')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(321)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(321)
    label(2320)
    sprite('keep', 1)
    if SLOT_109:
        sendToLabel(10)
    sprite('keep', 1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraControlEnable(1)
    SetZVal(750)

    def upon_EVERY_FRAME():
        if SLOT_29 < 320000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2322)
    sprite('kk030_00', 7)
    physicsXImpulse(5000)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(2321)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(2321)
    label(2322)
    sprite('kk010_00', 7)
    sprite('kk010_01', 7)
    Voiceline('kk545')
    DemoEndOnVoiceEnd(1)
    label(2323)
    sprite('kk010_02', 7)
    sprite('kk010_03', 7)
    sprite('kk010_04', 7)
    sprite('kk010_05', 7)
    sprite('kk010_06', 7)
    sprite('kk010_07', 7)
    sprite('kk010_08', 7)
    sprite('kk010_09', 7)
    sprite('kk010_10', 7)
    sprite('kk010_11', 7)
    sprite('kk010_12', 7)
    sprite('kk010_13', 7)
    loopRest()
    gotoLabel(2323)
    label(330)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk547')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(331)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(331)
    label(2330)
    sprite('kk001_00', 7)
    Voiceline('kk547')
    DemoEndOnVoiceEnd(1)
    sprite('kk001_01', 7)
    label(2331)
    sprite('kk001_02', 7)
    sprite('kk001_03', 7)
    sprite('kk001_04', 7)
    sprite('kk001_03', 7)
    loopRest()
    gotoLabel(2331)
    label(350)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk551')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)
    loopRest()
    label(360)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk553')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 20)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(361)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(361)
    label(2360)
    sprite('kk001_00', 7)
    Voiceline('kk553')
    DemoEndOnVoiceEnd(1)
    sprite('kk001_01', 7)
    label(2361)
    sprite('kk001_02', 7)
    sprite('kk001_03', 7)
    sprite('kk001_04', 7)
    sprite('kk001_03', 7)
    loopRest()
    gotoLabel(2361)
    label(370)
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    Voiceline('kk555')
    DemoEndOnVoiceEnd(1)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 32767)
    loopRest()
    label(2370)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk555')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(2371)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 7)
    sprite('kk620_06ex02', 7)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(2371)
    label(390)
    sprite('kk620_00', 6)
    Voiceline('kk559')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(361)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(361)
    label(2390)
    sprite('kk620_00', 6)
    Voiceline('kk559')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(2391)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(2391)
    label(410)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk563')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(411)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(411)
    label(1410)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk563')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(1411)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(1411)
    label(2410)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk563')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(2411)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(2411)
    label(420)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk565')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(421)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    loopRest()
    gotoLabel(421)
    label(440)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 10)
    Voiceline('kk571')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 6)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(441)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 8)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 7)
    sprite('kk620_06ex07', 8)
    loopRest()
    gotoLabel(441)
    label(666)
    sprite('kk610_00', 7)
    sprite('kk610_01', 7)
    sprite('kk610_02', 7)
    sprite('kk610_03', 7)
    sprite('kk610_04', 150)
    Voiceline('kk406')
    sprite('kk610_05', 7)
    sprite('kk610_06', 7)
    sprite('kk610_07', 7)
    sprite('kk610_08', 7)
    sprite('kk610_09', 7)
    sprite('kk610_09', 32767)
    Voiceline('kk407')
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()


@State
def CmnActLose():
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    Voiceline('kk411')
    DemoEndOnVoiceEnd(1)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(0)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWait():
    label(0)
    sprite('rg000_00', 7)
    sprite('rg000_01', 7)
    sprite('rg000_02', 7)
    sprite('rg000_03', 7)
    sprite('rg000_04', 7)
    sprite('rg000_05', 7)
    sprite('rg000_06', 7)
    sprite('rg000_05', 7)
    sprite('rg000_04', 7)
    sprite('rg000_03', 7)
    sprite('rg000_02', 7)
    sprite('rg000_01', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryStand():
    sprite('keep', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefWin():
    sprite('keep', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefLose():
    sprite('rg620_05', 32767)


@State
def EventWinKKSpecial():
    sprite('kk602_00', 32767)


@State
def EventKKPhone():
    sprite('kk610_00', 7)
    sprite('kk610_01', 7)
    sprite('kk610_02', 7)
    sprite('kk610_03', 7)
    sprite('kk610_04', 32767)
    loopRest()


@State
def EventKKGlasses():
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(0)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(0)


@State
def EventKKGlassesEnd():
    sprite('kk620_05', 6)
    sprite('kk620_04ex02', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04', 7)
    sprite('kk620_03', 6)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKKReaction():
    sprite('kk001_00', 6)
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 6)
    sprite('kk001_06', 6)
    sprite('kk001_07', 6)
    sprite('kk001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKKChouhatsu():
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    enterState('CmnActStand')


@State
def EventKKNabiki():
    sprite('kk430_00', 6)
    sprite('kk430_01', 6)
    sprite('kk430_02', 6)
    label(1)
    sprite('kk430_03', 5)
    sprite('kk430_04', 5)
    sprite('kk430_05', 5)
    loopRest()
    gotoLabel(1)


@State
def EventKKNabikiEnd():
    sprite('kk430_02', 6)
    sprite('kk430_01', 6)
    sprite('kk430_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKKWalkEntryWait():
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 1)
    AddX(-770000)
    sprite('null', 32767)
    loopRest()


@State
def EventKKWalkEntry():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventWarpOut():
    ScreenCollision(0)
    sprite('kk620_05', 6)
    EndYPhysicsImpulse()
    sprite('kk620_04ex02', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_04ex01', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_04', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_03', 8)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('kk620_02', 8)
    CommonSE('014_electric_sl')
    CreateParticle('haef_event_lose_end', 103)
    sprite('kk620_01', 8)
    sprite('kk620_00', 6)
    XPositionRelativeFacing(-500000)
    AlphaValue(0)
    sprite('null', 6)
    loopRest()


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)


@State
def EventVsRCWait():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-210000)
    sprite('kk602_00', 32767)


@State
def EventVsRCWait2():
    sprite('kk620_00', 6)
    XPositionRelativeFacing(-260000)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    label(0)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 7)
    sprite('kk620_06ex05', 6)
    sprite('kk620_06ex06', 6)
    sprite('kk620_06ex07', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_kkvskg_01():
    sprite('kk404_00ex02', 2)
    PrivateSE('kkse_19')
    ObjectUpon(22, 32)
    sprite('kk404_00ex02', 1)
    sprite('kk404_01ex02', 6)
    sprite('kk404_02ex02', 6)
    sprite('kk404_03ex02', 6)
    sprite('kk404_04ex02', 6)
    sprite('kk404_05ex02', 6)
    sprite('kk404_06ex02', 6)
    sprite('kk404_07ex02', 6)
    sprite('kk404_08ex02', 6)
    sprite('kk404_09ex02', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_phvskk_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-245000)

        def upon_32():
            sendToLabel(1)

        def upon_STATE_END():
            EndMomentum(1)
            XPositionRelativeFacing(-260000)
    label(0)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('kk040_00', 4)
    sprite('kk040_01', 4)
    sprite('kk040_02', 5)
    sprite('kk040_10', 13)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('104_guard_grap_1')
    ScreenShake(3000, 18000)
    sprite('kk040_10', 17)
    AddInertia(-2000)
    sprite('kk040_01', 5)
    sprite('kk040_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_phvskk_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('kk040_10', 10)
    sprite('kk090_00', 18)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('104_guard_grap_2')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('kk090_01', 5)
    sprite('kk090_02', 15)
    sprite('kk090_03', 6)
    sprite('kk090_04', 6)
    sprite('kk061_10', 6)
    sprite('kk061_06', 6)
    sprite('kk061_05', 32767)
    loopRest()


@State
def Act2Event_phvskk_02():
    sprite('keep', 2)
    sprite('kk061_06', 6)
    sprite('kk061_07', 6)
    sprite('kk061_08', 6)
    sprite('kk061_09', 6)
    sprite('kk061_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_rmvskk_00():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_19 <= 70000:
                sendToLabel(1)
    label(0)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('kk003_00', 3)
    sprite('kk003_01', 3)
    sprite('kk003_02', 3)
    Flip()
    loopRest()
    enterState('CmnActStand')


@State
def Act2EventEntryWait_kkvsrl():
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 1)
    XPositionRelativeFacing(-2100000)
    sprite('null', 32767)
    loopRest()


@State
def Act2EventEntry_kkvsrl():

    def upon_32():
        CameraControlEnable(0)
    CameraControlEnable(1)
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act2EventChouhatsu():
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    enterState('CmnActStand')


@State
def Act2EventNabiki():
    sprite('kk430_00', 6)
    sprite('kk430_01', 6)
    sprite('kk430_02', 6)
    label(1)
    sprite('kk430_03', 5)
    sprite('kk430_04', 5)
    sprite('kk430_05', 5)
    loopRest()
    gotoLabel(1)


@State
def Act2EventNabikiEnd():
    sprite('kk430_02', 6)
    sprite('kk430_01', 6)
    sprite('kk430_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Megane():
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 32767)
    loopRest()


@State
def Act2Event_MeganeEnd():
    sprite('keep', 2)
    sprite('kk620_04', 7)
    sprite('kk620_03', 6)
    sprite('kk620_02', 6)
    sprite('kk620_01', 6)
    sprite('kk620_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_OverDrive():
    sprite('kk333_00', 6)
    sprite('kk333_01', 6)
    sprite('kk333_02', 6)
    sprite('kk333_03', 6)
    sprite('kk333_04', 4)
    label(0)
    sprite('kk333_05', 5)
    sprite('kk333_06', 5)
    sprite('kk333_07', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_OverDriveEnd():
    sprite('keep', 2)
    sprite('kk333_08', 6)
    sprite('kk333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cavskk_00():
    sprite('kk070_00', 6)
    CreateObject('Act2Event_Yure', -1)
    sprite('kk070_01', 6)
    sprite('kk070_02', 6)
    sprite('kk070_03', 6)
    sprite('kk070_02', 6)
    sprite('kk070_03', 6)
    sprite('kk070_10', 6)
    sprite('kk070_11', 12)
    sprite('kk070_12', 8)
    sprite('kk070_13', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_WarpIn():
    sprite('kk404_01ex02', 6)
    PrivateSE('kkse_19')
    sprite('kk404_02ex02', 4)
    sprite('kk404_03ex02', 4)
    sprite('kk404_04ex02', 4)
    sprite('kk404_05ex02', 4)
    sprite('kk404_06ex02', 4)
    sprite('kk404_07ex02', 4)
    sprite('kk404_08ex02', 4)
    sprite('kk404_09ex02', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Chouhatsu():
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 9)
    sprite('kk300_09', 9)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvskk_00():
    sprite('keep', 1)
    CreateObject('Act2Event_Yure', -1)
    sprite('keep', 32767)
    loopRest()


@State
def Act2EventCamerayose_tgvskk():
    sprite('keep', 1)
    CameraControlEnable(1)
    RunLoopUpon(17, 90)
    uponSendToLabel(17, 1)
    label(0)
    sprite('kk000_00', 7)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    gotoLabel(0)
    label(1)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 32767)


@State
def Act2EventWalkEntryWait():
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 1)
    AddX(-770000)
    sprite('null', 32767)
    loopRest()


@State
def Act2EventWalkEntry():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act2EventWalkEntry_kkvskg():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    physicsXImpulse(0)
    ObjectUpon(22, 32)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvskk_00():
    sprite('kk620_06ex04', 32767)


@State
def Act3Event_hzvskk_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-190000)
    sprite('kk000_00', 7)
    sprite('kk070_00', 3)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitmz', 103)
    CommonSE('101_hit_slash_1')
    ScreenShake(1000, 20000)
    AddInertia(-5000)
    sprite('kk070_00', 3)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitmz', 103)
    CommonSE('101_hit_slash_1')
    ScreenShake(1000, 20000)
    AddInertia(-5000)
    sprite('kk070_00', 3)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitmz', 103)
    CommonSE('101_hit_slash_1')
    ScreenShake(1000, 20000)
    AddInertia(-5000)
    sprite('kk070_00', 4)
    sprite('kk070_01', 4)
    sprite('kk070_02', 4)
    sprite('kk070_03', 40)
    loopRest()
    sprite('kk070_04', 5)
    sprite('kk070_05', 5)
    sprite('kk070_06', 5)
    sprite('kk070_07', 4)
    sprite('kk070_08', 4)
    sprite('kk070_09', 4)
    sprite('kk063_11', 32767)
    LandingEffects(100, 1, 0)
    CommonSE('209_down_normal_0')
    AddX(180000)


@State
def Act3Event_hzvskk_02():

    def upon_IMMEDIATE():

        def upon_LANDING():
            sendToLabel(0)
            EndMomentum(1)
            LandingEffects(100, 1, 1)
    sprite('kk112_00', 3)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    sprite('kk112_01', 3)
    sprite('kk112_02', 3)
    sprite('kk112_03', 3)
    sprite('kk112_04', 3)
    sprite('kk112_05', 3)
    sprite('kk112_06', 3)
    sprite('kk112_07', 3)
    sprite('kk112_08', 3)
    sprite('kk112_09', 32767)
    label(0)
    sprite('kk024_00', 4)
    sprite('kk024_01', 4)
    sprite('kk024_02', 4)
    sprite('kk024_03', 4)
    sprite('kk024_04', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvskk_00():
    sprite('kk001_00', 6)
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 6)
    sprite('kk001_06', 6)
    sprite('kk001_07', 6)
    sprite('kk001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvskk_01():
    sprite('kk300_00', 4)
    sprite('kk300_01', 4)
    sprite('kk300_02', 4)
    sprite('kk300_03', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_04', 6)
    sprite('kk300_05', 6)
    sprite('kk300_06', 6)
    sprite('kk300_07', 6)
    sprite('kk300_08', 7)
    sprite('kk300_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvskk_02():
    sprite('kk210_12', 6)
    sprite('kk211_00', 5)
    label(0)
    sprite('kk211_01', 4)
    CommonSE('003_swing_grap_0_2')
    sprite('kk211_02', 4)
    sprite('kk211_03', 4)
    sprite('kk211_01', 4)
    sprite('kk211_02', 4)
    sprite('kk211_03', 4)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mkvskk_03():
    sprite('kk211_00', 5)
    sprite('kk210_12', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hbvskk_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-720000)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    clearUponHandler(EVERY_FRAME)
                    XPositionRelativeFacing(-260000)
                    EndMomentum(1)
                    sendToLabel(0)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                clearUponHandler(EVERY_FRAME)
                XPositionRelativeFacing(-260000)
                EndMomentum(1)
                sendToLabel(0)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(9)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('kk000_00', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kkvsar_00():

    def upon_IMMEDIATE():
        AddX(-120000)
        uponSendToLabel(LANDING, 0)
        callSubroutine('Delete_hole')
    sprite('kk212_00', 3)
    CreateObject('efkk_212_hole', -1)
    sprite('kk212_01', 3)
    sprite('kk212_02', 3)
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    setGravity(1600)
    sprite('kk212_03', 4)
    XImpulseAcceleration(200)
    sprite('kk212_04', 4)
    CreateObject('efkk_212_burner', -1)
    XImpulseAcceleration(200)
    sprite('kk212_05', 4)
    PrivateSE('kkse_22')
    CommonSE('005_swing_grap_2_1')
    XImpulseAcceleration(200)
    YAccel(150)
    sprite('kk212_06', 14)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    ScreenShake(1000, 4000)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    ObjectUpon(22, 32)
    EndMomentum(1)
    setGravity(0)
    sprite('kk212_06', 1)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(30)
    YAccel(-200)
    sprite('kk212_07', 3)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('kk212_08', 3)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('kk212_09', 3)
    XImpulseAcceleration(80)
    label(1)
    sprite('kk212_10', 2)
    sprite('kk212_11', 2)
    gotoLabel(1)
    label(0)
    sprite('kk212_12', 2)
    CreateObject('efkk_212_hole_out', -1)
    EndMomentum(1)
    sprite('kk212_13', 2)
    sprite('kk212_14', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kkvsar_01():
    sprite('kk000_00', 7)
    CameraControlEnable(1)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk620_00', 6)
    sprite('kk620_01', 6)
    sprite('kk620_02', 6)
    sprite('kk620_03', 6)
    sprite('kk620_04', 7)
    sprite('kk620_04ex01', 7)
    sprite('kk620_04ex02', 7)
    sprite('kk620_05', 6)
    sprite('kk620_06', 6)
    sprite('kk620_06ex01', 6)
    sprite('kk620_06ex02', 6)
    sprite('kk620_06ex03', 7)
    sprite('kk620_06ex04', 32767)


@State
def Act3Event_arvskk_00():

    def upon_IMMEDIATE():
        AddX(-80000)
        uponSendToLabel(LANDING, 0)
        callSubroutine('Delete_hole')
    sprite('keep', 5)
    sprite('kk212_00', 3)
    CreateObject('efkk_212_hole', -1)
    sprite('kk212_01', 3)
    sprite('kk212_02', 3)
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    setGravity(1600)
    sprite('kk212_03', 4)
    XImpulseAcceleration(200)
    sprite('kk212_04', 4)
    CreateObject('efkk_212_burner', -1)
    XImpulseAcceleration(200)
    sprite('kk212_05', 4)
    PrivateSE('kkse_22')
    CommonSE('005_swing_grap_2_1')
    XImpulseAcceleration(200)
    YAccel(150)
    sprite('kk212_06', 12)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    setGravity(0)
    CreateObject('Eventoffset_Sosai_arvskk', 0)
    sprite('kk212_06', 1)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(30)
    YAccel(-200)
    sprite('kk212_07', 3)
    XImpulseAcceleration(-80)
    YAccel(50)
    sprite('kk212_08', 3)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('kk212_09', 3)
    XImpulseAcceleration(80)
    label(1)
    sprite('kk212_10', 2)
    sprite('kk212_11', 2)
    gotoLabel(1)
    label(0)
    sprite('kk212_12', 2)
    CreateObject('efkk_212_hole_out', -1)
    EndMomentum(1)
    sprite('kk212_13', 2)
    sprite('kk212_14', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kkvsph_00():
    sprite('keep', 1)
    CreateObject('Act3Event_kkvsph_no', 100)
    RegisterObject(4, 1)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kkvsph_01():
    sprite('kk430_02', 6)
    ObjectUpon(FALLING, 32)
    sprite('kk430_01', 6)
    sprite('kk430_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvskk_00():
    sprite('keep', 2)
    CreateObject('Act3Event_kgvskk_mu', -1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvskk_01():
    sprite('kk001_00', 6)
    TriggerUponForState('Act3Event_kgvskk_mu', 32)
    sprite('kk001_01', 6)
    sprite('kk001_02', 6)
    sprite('kk001_03', 6)
    sprite('kk001_04', 6)
    sprite('kk001_05', 6)
    sprite('kk001_06', 6)
    sprite('kk001_07', 6)
    sprite('kk001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_CrouchLoop():
    label(0)
    sprite('kk010_02', 6)
    sprite('kk010_03', 6)
    sprite('kk010_04', 6)
    sprite('kk010_05', 6)
    sprite('kk010_06', 6)
    sprite('kk010_07', 6)
    sprite('kk010_08', 6)
    sprite('kk010_09', 6)
    sprite('kk010_10', 6)
    sprite('kk010_11', 6)
    sprite('kk010_12', 6)
    sprite('kk010_13', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CrouchToStand():
    sprite('kk010_01', 7)
    sprite('kk010_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tmvskk_00():
    ScreenCollision(0)
    EnableCollision(0)
    sprite('kk620_05', 6)
    EndYPhysicsImpulse()
    sprite('kk620_04ex02', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_04ex01', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_04', 7)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    sprite('kk620_03', 8)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('kk620_02', 8)
    CommonSE('014_electric_sl')
    CreateParticle('haef_event_lose_end', 103)
    sprite('kk620_01', 8)
    sprite('kk620_00', 6)
    XPositionRelativeFacing(-500000)
    AlphaValue(0)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_jbvskk_00():
    sprite('kk070_03', 10)
    sprite('kk070_04', 6)
    sprite('kk070_05', 6)
    sprite('kk070_06', 6)
    sprite('kk070_07', 6)
    sprite('kk070_08', 6)
    sprite('kk070_09', 6)
    sprite('kk063_11', 60)
    LandingEffects(100, 1, 0)
    CommonSE('209_down_normal_0')
    AddX(180000)
    sprite('kk063_11', 30)
    ConstantAlphaModifier(-8)
    CommonSE('000_airdash_0')
    sprite('kk063_11', 32767)
    AlphaValue(0)
    Visibility(1)
    loopRest()


@State
def Act3Event_jbvskk_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-720000)
        AlphaValue(255)
        Visibility(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    clearUponHandler(EVERY_FRAME)
                    XPositionRelativeFacing(-260000)
                    EndMomentum(1)
                    sendToLabel(0)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                clearUponHandler(EVERY_FRAME)
                XPositionRelativeFacing(-260000)
                EndMomentum(1)
                sendToLabel(0)
    sprite('kk030_00', 7)
    physicsXImpulse(4800)
    sprite('kk030_01', 7)
    sprite('kk030_02', 7)
    sprite('kk030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_04', 7)
    sprite('kk030_05', 7)
    sprite('kk030_06', 7)
    sprite('kk030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_08', 7)
    sprite('kk030_09', 7)
    sprite('kk030_10', 7)
    label(9)
    sprite('kk030_11', 7)
    sprite('kk030_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_13', 7)
    sprite('kk030_14', 7)
    sprite('kk030_15', 7)
    sprite('kk030_16', 7)
    sprite('kk030_17', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kk030_18', 7)
    sprite('kk030_19', 7)
    sprite('kk030_20', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('kk000_00', 1)
    loopRest()
    enterState('CmnActStand')
