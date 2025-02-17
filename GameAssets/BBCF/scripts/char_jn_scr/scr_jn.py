@Subroutine
def OverDrivePowerUpSkill():
    if SLOT_OverdriveTimer:
        CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    AddActionMark(0)


@Subroutine
def PreInit():
    CharacterID('jn')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(5900)
    WalkBSpeed(4800)
    DashFInitialVelocity(16000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(41000)
    Gravity(1850)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(1)
    CreateDecalOn(1)
    if SLOT_116:
        Health(15000)
        WalkFSpeed(8850)
        WalkBSpeed(7200)
        DashFInitialVelocity(21000)
        DashFMaxVelocity(33000)
        OverdriveDuration(780, 780, 780, 780, 780, 780, 780, 780, 780, 780)
    Move_Register('ShortDash', 0x1)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -100000, 200000, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    SkillEstimateRange(0, 200000, -100000, 50000, 250, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -100000, 200000, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    MoveCancellableFrames(29, 30)
    AirborneOpponentPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 230000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveCancellableFrames(100, 100)
    DamageStunPriority(1200)
    GuardStunPriority(1200)
    SkillEstimateRange(50000, 400000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(-50000, 450000, -150000, 150000, 1000, 10)
    if SLOT_100:
        StateCall('NanDato')
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveComboPriority(1)
    DamageStunPriority(2000)
    AirborneOpponentPriority(2000)
    MoveCancellableFrames(15, 17)
    MoveHeatValuePriority(490, 500, 0, 1000)
    SkillEstimateRange(0, 500000, -200000, 200000, 250, 0)
    if SLOT_100:
        StateCall('NanDato')
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    AirborneOpponentPriority(4000)
    SkillEstimateRange(50000, 300000, 150000, 700000, 250, 5)
    if SLOT_100:
        StateCall('NanDato')
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    AirborneOpponentPriority(1)
    SkillEstimateRange(350000, 600000, -150000, 150000, 500, 1)
    if SLOT_100:
        StateCall('StoryYowai5D')
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    Unknown15027(3500)
    SkillEstimateRange(50000, 300000, -200000, 200000, 100, 0)
    if SLOT_100:
        StateCall('StoryYowai5D')
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    Unknown15027(1)
    DamageStunPriority(1)
    SkillEstimateRange(550000, 750000, 0, 300000, 1000, 50)
    if SLOT_100:
        StateCall('StoryYowai5D')
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(1)
    SkillEstimateRange(100000, 300000, -200000, 0, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(0, 300000, -300000, 0, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    MoveMaxChainRepeat(1)
    DamageStunPriority(4000)
    SkillEstimateRange(100000, 550000, -100000, 300000, 1000, 10)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    MoveMaxChainRepeat(1)
    DamageStunPriority(3000)
    SkillEstimateRange(-100000, 250000, -400000, -100000, 1000, 10)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    MovePriority(1)
    MoveCancellableFrames(30, 32)
    SkillEstimateRange(-300000, 300000, -300000, 300000, 1000, 50)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(100000, 250000, 0, 200000, 1000, 50)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_Condition(0x3008)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(1)
    AirborneOpponentPriority(1)
    JumpAvoidPriority(10000)
    SkillEstimateRange(800000, 2000000, -100000, 200000, 500, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Shot_DWeak', INPUT_SPECIALMOVE)
    Move_Condition(0x3008)
    StateCall('Shot')
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Shot_D', INPUT_SPECIALMOVE)
    Move_Condition(0x3009)
    Move_Condition(0x2004)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    OpponentAttackPriority(1)
    SkillEstimateRange(0, 500000, -200000, 150000, 200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AirShot', INPUT_SPECIALMOVE)
    Move_Condition(0x3008)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(0)
    GuardStunPriority(1000)
    SkillEstimateRange(500000, 1000000, -200000, 300000, 250, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AirShot_DWeak', INPUT_SPECIALMOVE)
    Move_Condition(0x3008)
    StateCall('AirShot')
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AirShot_D', INPUT_SPECIALMOVE)
    Move_Condition(0x3009)
    Move_Condition(0x2001)
    Move_Condition(0x2004)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    OpponentAttackPriority(1)
    SkillEstimateRange(0, 350000, -250000, 200000, 200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AntiAir_Fast', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    GuardStunPriority(1)
    AirborneOpponentPriority(3000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(100000, 500000, 200000, 500000, 350, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AntiAir_Slow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(1)
    DamageStunPriority(0)
    MoveComboPriority(1)
    OpponentAttackPriority(4000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-150000, 150000, -100000, 300000, 250, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AntiAir_DWeak', INPUT_SPECIALMOVE)
    StateCall('AntiAir_Slow')
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AntiAir_D', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x2004)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveComboPriority(1)
    OpponentAttackPriority(4000)
    MoveCPULevel(500, 1000, 10, 1000)
    MoveButtonHoldTime(3, 44, 45)
    SkillEstimateRange(-250000, 250000, -50000, 300000, 200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Shot_D_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x3009)
    Move_Condition(0x2004)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    StateCall('Shot_D')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    MoveLow()
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1500)
    MoveButtonHoldTime(2, 17, 20)
    SkillEstimateRange(0, 2500000, -200000, 100000, 1000, 50)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Assault_2nd', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_HOLD_C)
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('Assault_DWeak', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    StateCall('Assault')
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Assault_D', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x2004)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    MoveLow()
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    AirborneOpponentPriority(1)
    DamageStunPriority(50000)
    Unknown15026(2, 43, 45)
    SkillEstimateRange(0, 1000000, -150000, 150000, 250, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('Assault_D_2nd', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_HOLD_C)
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(1200)
    SkillEstimateRange(100000, 450000, -500000, 100000, 100, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AirAssault_DWeak', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    StateCall('AirAssault')
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('AirAssault_D', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Condition(0x2004)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 300000, -350000, 300000, 100, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('RushAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0xdf)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 200000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('RushAssaultFinish', INPUT_SPECIALMOVE)
    Move_Condition(0x2004)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(2000)
    Move_EndRegister()
    Move_Register('UltimateAtemi', INPUT_DISTORTION)
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(2000)
    DamageStunPriority(1)
    MoveComboPriority(1)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-100000, 350000, -100000, 500000, 200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAtemi_OD', INPUT_DISTORTION)
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(2000)
    DamageStunPriority(1)
    MoveComboPriority(1)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-100000, 350000, -100000, 500000, 200, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('UltimateShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3072)
    OpponentAttackPriority(5000)
    DamageStunPriority(5000)
    MoveCPULevel(500, 1000, 10, 1000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(500000, 1500000, -200000, 200000, 200, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    Move_Condition(0x3072)
    OpponentAttackPriority(5000)
    DamageStunPriority(5000)
    MoveCPULevel(500, 1000, 10, 1000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(500000, 1500000, -200000, 200000, 200, 10)
    Move_EndRegister()
    Move_Register('UltimateAntiAirShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    GuardStunPriority(1)
    SkillEstimateRange(0, 500000, 100000, 500000, 500, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAntiAirShot_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    GuardStunPriority(1)
    SkillEstimateRange(0, 500000, 100000, 500000, 500, 0)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAirShot', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 350000, -600000, -100000, 500, 1)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAirShot_OD', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    SkillEstimateRange(0, 350000, -600000, -100000, 500, 1)
    Move_Condition(0x3072)
    Move_EndRegister()
    Move_Register('astral', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_2HOLD8)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(-500000, 1500000, -250000, 200000, 300, 1)
    Move_Condition(0x3072)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'Assault_D', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Assault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'RushAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'UltimateAntiAirShot', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2C', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2C', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5D', 'AirAssault', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5D', 'AirAssault_D', 10000000)
    TempPriorityMultiplier('RushAssault', 'RushAssaultFinish', 5000000)
    StylishModeSpecialButton('AntiAir_Slow', 0x4, 0xea)
    StylishModeSpecialButton('AntiAir_D', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0x79)
    StylishModeSpecialButton('Assault_D', 0x4, 0x79)
    StylishModeSpecialButton('UltimateShot', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateShot_OD', 0x4, 0x5f)
    StylishModeSpecialButton('Shot', 0x4, 0x45)
    StylishModeSpecialButton('Shot_D', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault', 0x4, 0xea)
    StylishModeSpecialButton('AirAssault_D', 0x4, 0xea)
    StylishModeSpecialButton('UltimateAirShot', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAirShot_OD', 0x4, 0x5f)
    StylishModeSpecialButton('AirShot', 0x4, 0x45)
    StylishModeSpecialButton('AirShot_D', 0x4, 0x45)
    StylishModeSpecialButton('RushAssaultFinish', 0x4, 0xea)
    StylishModeSpecialButton('Assault_D_2nd', 0x4, 0xea)
    StylishModeSpecialButton('Assault_2nd', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 1, 150000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 1, 300000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 3, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 7, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk5D', 'ShortDash', 0, 0)
    StylishModeCancels('NmlAtk5D', 'RushAssault', 1, 230000)
    StylishModeCancels('NmlAtk5D', 'UltimateShot', 6, 50)
    StylishModeCancels('NmlAtk5D', 'UltimateShot_OD', 6, 50)
    StylishModeCancels('NmlAtk5D', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk6B', 'AirAssault', 6, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk6D', 10, 700000)
    StylishModeCancels('NmlAtk6C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk6C', 'Shot_D', 13, 0)
    StylishModeCancels('RushAssault', 'RushAssaultFinish', 0, 0)
    StylishModeCancels('Assault', 'Assault_2nd', 0, 0)
    StylishModeCancels('Assault_D', 'Assault_D_2nd', 0, 0)
    StylishModeCancels('ThrowExe', 'ShortDash', 0, 0)
    StylishModeCancels('ThrowExe', 'astral', 6, 0)
    StylishModeCancels('BackThrowExe', 'ShortDash', 0, 0)
    StylishModeCancels('BackThrowExe', 'astral', 6, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk6A', 1, 150000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 1, 200000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 12, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 7, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk2C', 'FHighJump', 3, 0)
    StylishModeCancels('NmlAtk2D', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk2D', 'astral', 6, 0)
    StylishModeCancels('NmlAtk2D', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk3C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk3C', 'AntiAir_Slow', 1, 250000)
    StylishModeCancels('NmlAtk3C', 'UltimateShot', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateShot_OD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'Assault_D', 10, 1200000)
    StylishModeCancels('NmlAtk3C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirAssault', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirAssault_D', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR2C', 2, 100000)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR2C', 13, 0)
    StylishModeCancels('NmlAtkAIR2C', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR2C', 'AirAssault', 3, 0)
    StylishModeCancels('NmlAtkAIR2C', 'AirAssault_D', 3, 0)
    StylishModeCancels('NmlAtkAIR5D', 'AirAssault', 0, 0)
    HitSprites(0, 'jn062_01')
    HitSprites(1, 'jn062_03')
    HitSprites(2, 'jn062_04')
    HitSprites(3, 'jn062_05')
    HitSprites(4, 'jn062_06')
    HitSprites(5, 'jn062_06')
    HitSprites(6, 'jn062_07')
    HitSprites(7, 'jn041_02')
    HitSprites(8, 'jn040_02')
    HitSprites(9, 'jn045_02')
    HitSprites(10, 'jn060_00')
    HitSprites(11, 'jn060_01')
    HitSprites(12, 'jn060_02')
    HitSprites(13, 'jn060_03')
    HitSprites(14, 'jn060_04')
    HitSprites(15, 'jn060_12')
    HitSprites(16, 'jn050_00')
    HitSprites(17, 'jn052_00')
    HitSprites(18, 'jn054_00')
    HitSprites(19, 'jn000_00')
    HitSprites(20, 'jn000_00')
    HitSprites(25, 'jn063_00')
    HitSprites(26, 'jn063_01')
    HitSprites(27, 'jn063_02')
    HitSprites(28, 'jn063_03')
    HitSprites(29, 'jn063_09')
    HitSprites(30, 'jn077_90')
    HitSprites(31, 'jn077_91')
    HitSprites(32, 'jn077_90ex01')
    HitSprites(33, 'jn077_91ex01')
    HitSprites(34, 'jn077_90ex02')
    HitSprites(35, 'jn077_91ex02')
    HitSprites(36, 'jn077_90ex03')
    HitSprites(37, 'jn077_91ex03')
    HitSprites(24, 'jn073_01')
    CommonVoicelines(0, 'jn000')
    CommonVoicelines(1, 'jn001')
    CommonVoicelines(2, 'jn002')
    CommonVoicelines(3, 'jn003')
    CommonVoicelines(4, 'jn004')
    CommonVoicelines(5, 'jn005')
    CommonVoicelines(6, 'jn006')
    CommonVoicelines(7, 'jn007')
    CommonVoicelines(8, 'jn008')
    CommonVoicelines(9, 'jn009')
    CommonVoicelines(10, 'jn010')
    CommonVoicelines(11, 'jn011')
    CommonVoicelines(12, 'jn012')
    CommonVoicelines(13, 'jn013')
    CommonVoicelines(14, 'jn014')
    CommonVoicelines(15, 'jn015')
    CommonVoicelines(16, 'jn016')
    CommonVoicelines(17, 'jn017')
    CommonVoicelines(18, 'jn018')
    CommonVoicelines(19, 'jn019')
    CommonVoicelines(20, 'jn020')
    CommonVoicelines(21, 'jn021')
    CommonVoicelines(22, 'jn022')
    CommonVoicelines(23, 'jn023')
    CommonVoicelines(24, 'jn024')
    CommonVoicelines(25, 'jn025')
    CommonVoicelines(26, 'jn026')
    CommonVoicelines(27, 'jn027')
    CommonVoicelines(28, 'jn028')
    CommonVoicelines(29, 'jn029')
    CommonVoicelines(30, 'jn030')
    CommonVoicelines(31, 'jn031')
    CommonVoicelines(32, 'jn032')
    CommonVoicelines(33, 'jn033')
    CommonVoicelines(34, 'jn034')
    CommonVoicelines(35, 'jn035')
    CommonVoicelines(36, 'jn036')
    CommonVoicelines(37, 'jn037')
    CommonVoicelines(38, 'jn038')
    CommonVoicelines(39, 'jn039')
    CommonVoicelines(40, 'jn040')
    CommonVoicelines(41, 'jn041')
    CommonVoicelines(42, 'jn042')
    CommonVoicelines(43, 'jn043')
    CommonVoicelines(44, 'jn044')
    CommonVoicelines(45, 'jn045')
    CommonVoicelines(46, 'jn046')
    CommonVoicelines(47, 'jn047')
    CommonVoicelines(48, 'jn048')
    CommonVoicelines(49, 'jn049')
    CommonVoicelines(50, 'jn050')
    CommonVoicelines(51, 'jn051')
    CommonVoicelines(52, 'jn052')
    CommonVoicelines(53, 'jn053')
    CommonVoicelines(54, 'jn100')
    CommonVoicelines(55, 'jn101')
    CommonVoicelines(56, 'jn102')
    CommonVoicelines(57, 'jn103')
    CommonVoicelines(58, 'jn104')
    CommonVoicelines(59, 'jn105')
    CommonVoicelines(60, 'jn106')
    CommonVoicelines(61, 'jn107')
    CommonVoicelines(62, 'jn108')
    CommonVoicelines(63, 'jn109')
    CommonVoicelines(64, 'jn150')
    CommonVoicelines(65, 'jn151')
    CommonVoicelines(66, 'jn152')
    CommonVoicelines(67, 'jn153')
    CommonVoicelines(68, 'jn154')
    CommonVoicelines(69, 'jn155')
    CommonVoicelines(70, 'jn156')
    CommonVoicelines(71, 'jn157')
    CommonVoicelines(72, 'jn158')
    CommonVoicelines(75, 'jn160')
    CommonVoicelines(73, 'jn402')
    CommonVoicelines(74, 'jn403')
    if CharacterIDCheck('rg'):
        if SLOT_43:
            CommonVoicelines(73, 'jn403')
            CommonVoicelines(74, 'jn403')
        else:
            CommonVoicelines(73, 'jn402')
            CommonVoicelines(74, 'jn402')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def CheckOverDriveNormal():
    callSubroutine('OverDrivePowerUpSkill')
    if SLOT_OverdriveTimer:
        FreezeCount(3)
        FreezeTime(30)

    def upon_OPPONENT_HIT():
        if SLOT_OverdriveTimer:
            if not CheckCondition(12400):
                AirPushbackX(500)
                AirPushbackY(-5000)


@Subroutine
def CheckOverDriveFreeze():
    if SLOT_OverdriveTimer:
        ResetAttackP2()
        EnemyHitstopAddition(6, 0, 5)
        FreezeCount(3)

        def upon_OPPONENT_HIT():
            ScreenShake(20000, 20000)


@Subroutine
def CheckOverDriveSpecial():
    SLOT_58 = 0
    if SLOT_OverdriveTimer:
        SLOT_58 = 1
        HeatCooldown(0)


@Subroutine
def CheckDriveFlash():

    def upon_16():
        if SLOT_56:
            SLOT_56 = SLOT_56 + 1


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_21:
            if SLOT_116:
                SLOT_DamageMultiplier = 110
                HeatChange(3)


@State
def CmnActStand():
    label(0)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 80):
        gotoLabel(0)
    sprite('jn001_00', 8)
    sprite('jn001_01', 8)
    sprite('jn001_02', 10)
    SLOT_88 = 960
    Voiceline('jn000')
    sprite('jn001_03', 8)
    sprite('jn001_04', 8)
    sprite('jn001_05', 8)
    sprite('jn001_06', 10)
    sprite('jn001_07', 8)
    sprite('jn001_08', 8)
    sprite('jn001_09', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('jn003_01', 4)
    sprite('jn003_00', 4)


@State
def CmnActStand2Crouch():
    sprite('jn010_00', 3)
    sprite('jn010_01', 3)


@State
def CmnActCrouch():
    label(0)
    sprite('jn010_02', 8)
    sprite('jn010_03', 8)
    sprite('jn010_04', 8)
    sprite('jn010_05', 8)
    sprite('jn010_06', 8)
    sprite('jn010_07', 8)
    sprite('jn010_08', 8)
    sprite('jn010_09', 8)
    sprite('jn010_10', 8)
    sprite('jn010_11', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('jn013_01', 4)
    sprite('jn013_00', 4)


@State
def CmnActCrouch2Stand():
    sprite('jn010_01', 4)
    sprite('jn010_00', 4)


@State
def CmnActJumpPre():
    sprite('jn020_00', 2)
    sprite('jn020_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('jn020_02', 3)
    sprite('jn020_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('jn020_04', 3)
    sprite('jn020_05', 3)


@State
def CmnActJumpDown():
    sprite('jn020_05', 3)
    sprite('jn020_06', 3)
    sprite('jn020_07', 3)
    label(0)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('jn020_10', 3)
    sprite('jn020_11', 3)
    sprite('jn020_12', 3)
    sprite('jn020_13', 3)
    sprite('jn020_14', 3)


@State
def CmnActLandingStiffLoop():
    sprite('jn020_10', 2)
    sprite('jn020_11', 2)
    sprite('jn020_12', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('jn020_13', 3)
    sprite('jn020_14', 3)


@State
def CmnActFWalk():
    sprite('jn030_00', 6)
    label(0)
    sprite('jn030_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)
    sprite('jn030_03', 6)
    sprite('jn030_04', 6)
    sprite('jn030_05', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)
    sprite('jn030_07', 6)
    sprite('jn030_08', 6)
    sprite('jn030_09', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('jn031_00', 6)
    label(0)
    sprite('jn031_01', 6)
    sprite('jn031_02', 6)
    sprite('jn031_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn031_04', 6)
    sprite('jn031_05', 6)
    sprite('jn031_06', 6)
    sprite('jn031_07', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn031_08', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    label(0)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('jn032_11', 8)
    sprite('jn032_12', 4)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('jn033_00', 2)
    sprite('jn033_01', 3)
    physicsXImpulse(-24000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('jn033_02', 3)
    setInvincible(0)
    sprite('jn033_03', 3)
    sprite('jn033_04', 32767)
    loopRest()
    label(1)
    sprite('jn033_05', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('jn033_06', 1)
    sprite('jn033_07', 1)
    sprite('jn033_08', 1)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('jn035_00', 5)
    label(0)
    sprite('jn035_01', 3)
    sprite('jn035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('jn036_00', 5)
    label(0)
    sprite('jn036_01', 3)
    sprite('jn036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('jn050_00', 1)
    sprite('jn050_01', 1)
    sprite('jn050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('jn050_01', 1)
    sprite('jn050_02', 1)
    sprite('jn050_01', 2)
    sprite('jn050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('jn050_02', 1)
    sprite('jn050_03', 1)
    sprite('jn050_02', 2)
    sprite('jn050_01', 2)
    sprite('jn050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('jn050_03', 1)
    sprite('jn050_04', 1)
    sprite('jn050_03', 2)
    sprite('jn050_02', 2)
    sprite('jn050_01', 2)
    sprite('jn050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('jn050_04', 1)
    sprite('jn050_05', 1)
    sprite('jn050_04', 2)
    sprite('jn050_03', 2)
    sprite('jn050_02', 2)
    sprite('jn050_01', 2)
    sprite('jn050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('jn052_00', 1)
    sprite('jn052_01', 1)
    sprite('jn052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('jn052_01', 1)
    sprite('jn052_02', 1)
    sprite('jn052_01', 2)
    sprite('jn052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('jn052_02', 1)
    sprite('jn052_03', 1)
    sprite('jn052_02', 2)
    sprite('jn052_01', 2)
    sprite('jn052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('jn052_03', 1)
    sprite('jn052_04', 1)
    sprite('jn052_03', 2)
    sprite('jn052_02', 2)
    sprite('jn052_01', 2)
    sprite('jn052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('jn052_04', 1)
    sprite('jn052_05', 1)
    sprite('jn052_04', 2)
    sprite('jn052_03', 2)
    sprite('jn052_02', 2)
    sprite('jn052_01', 2)
    sprite('jn052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('jn054_00', 1)
    sprite('jn054_01', 1)
    sprite('jn054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('jn054_01', 1)
    sprite('jn054_02', 1)
    sprite('jn054_01', 2)
    sprite('jn054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('jn054_02', 1)
    sprite('jn054_03', 1)
    sprite('jn054_02', 2)
    sprite('jn054_01', 2)
    sprite('jn054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('jn054_03', 1)
    sprite('jn054_04', 1)
    sprite('jn054_03', 2)
    sprite('jn054_02', 2)
    sprite('jn054_01', 2)
    sprite('jn054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('jn054_04', 1)
    sprite('jn054_05', 1)
    sprite('jn054_04', 2)
    sprite('jn054_03', 2)
    sprite('jn054_02', 2)
    sprite('jn054_01', 2)
    sprite('jn054_00', 2)


@State
def CmnActBDownUpper():
    sprite('jn060_00', 6)
    label(0)
    sprite('jn060_01', 4)
    sprite('jn060_01add', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('jn060_02', 4)


@State
def CmnActBDownDown():
    label(0)
    sprite('jn060_03', 4)
    sprite('jn060_03add', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('jn060_04', 3)


@State
def CmnActBDownBound():
    sprite('jn060_05', 3)
    sprite('jn060_06', 3)
    sprite('jn060_07', 3)
    sprite('jn060_08', 3)
    sprite('jn060_09', 3)
    sprite('jn060_10', 3)
    sprite('jn060_11', 3)


@State
def CmnActBDownLoop():
    label(0)
    sprite('jn060_12', 1)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDown2Stand():
    sprite('jn061_00', 3)
    sprite('jn061_01', 3)
    sprite('jn061_02', 3)
    sprite('jn061_03', 3)
    sprite('jn061_04', 3)
    sprite('jn061_05', 3)
    sprite('jn061_06', 3)
    sprite('jn061_07', 3)
    sprite('jn061_08', 3)


@State
def CmnActFDownUpper():
    sprite('jn063_00', 3)
    sprite('jn063_01', 3)


@State
def CmnActFDownUpperEnd():
    sprite('jn063_01', 3)


@State
def CmnActFDownDown():
    sprite('jn063_01', 3)
    label(0)
    sprite('jn063_02', 3)
    sprite('jn063_02add', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('jn063_03', 3)


@State
def CmnActFDownBound():
    sprite('jn063_04', 3)
    sprite('jn063_05', 3)
    sprite('jn063_06', 3)
    sprite('jn063_07', 3)
    sprite('jn063_08', 3)


@State
def CmnActFDownLoop():
    sprite('jn063_09', 3)


@State
def CmnActFDown2Stand():
    sprite('jn064_00', 3)
    sprite('jn064_01', 3)
    sprite('jn064_02', 3)
    sprite('jn064_03', 3)
    sprite('jn064_04', 3)
    sprite('jn064_05', 3)
    sprite('jn064_06', 3)
    sprite('jn064_07', 3)
    sprite('jn064_08', 3)
    sprite('jn064_09', 3)
    sprite('jn064_10', 3)
    sprite('jn064_11', 3)
    sprite('jn064_12', 3)


@State
def CmnActVDownUpper():
    sprite('jn062_00', 4)
    label(0)
    sprite('jn062_01', 4)
    sprite('jn062_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('jn062_03', 3)
    sprite('jn062_04', 3)


@State
def CmnActVDownDown():
    sprite('jn062_05', 4)
    sprite('jn062_06', 4)
    label(0)
    sprite('jn062_07', 4)
    sprite('jn062_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('jn062_09', 2)
    sprite('jn062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('jn062_09', 2)
    sprite('jn062_10', 2)


@State
def CmnActBlowoff():
    sprite('jn072_00', 3)
    label(0)
    sprite('jn072_01', 3)
    sprite('jn072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('jn074_00', 3)
    sprite('jn074_01', 3)
    sprite('jn074_02', 3)
    sprite('jn074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('jn082_00', 2)
    sprite('jn082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('jn071_03', 1)


@State
def CmnActWallBound():
    sprite('jn073_00', 3)
    sprite('jn073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('jn073_02', 3)
    label(0)
    sprite('jn073_03', 3)
    sprite('jn073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('jn070_00', 2)
    sprite('jn070_01', 2)
    sprite('jn070_02', 2)
    sprite('jn070_03', 2)


@State
def CmnActStaggerDown():
    sprite('jn070_08', 6)
    sprite('jn070_09', 6)
    sprite('jn070_10', 6)
    sprite('jn070_11', 6)


@State
def CmnActUkemiStagger():
    sprite('jn070_12', 2)
    sprite('jn070_13', 3)
    sprite('jn070_14', 3)


@State
def CmnActUkemiAirF():
    sprite('jn113_00', 2)
    sprite('jn113_01', 2)
    sprite('jn113_02', 2)


@State
def CmnActUkemiAirB():
    sprite('jn113_00', 2)
    sprite('jn113_01', 2)
    sprite('jn113_02', 2)


@State
def CmnActUkemiAirN():
    sprite('jn113_00', 2)
    sprite('jn113_01', 2)
    sprite('jn113_02', 2)


@State
def CmnActUkemiLandF():
    sprite('jn110_00', 3)
    sprite('jn110_01', 3)
    sprite('jn110_02', 3)
    sprite('jn110_03', 3)
    sprite('jn110_04', 3)
    sprite('jn110_05', 3)
    sprite('jn110_06', 3)
    sprite('jn110_07', 200)
    sprite('jn110_08', 6)


@State
def CmnActUkemiLandB():
    sprite('jn111_00', 3)
    sprite('jn111_01', 3)
    sprite('jn111_02', 3)
    sprite('jn111_03', 3)
    sprite('jn111_04', 3)
    sprite('jn111_05', 3)
    sprite('jn111_06', 200)
    sprite('jn111_07', 6)


@State
def CmnActUkemiLandN():
    sprite('jn112_00', 3)
    sprite('jn112_01', 3)
    sprite('jn112_02', 3)
    sprite('jn112_03', 3)
    sprite('jn112_04', 3)
    sprite('jn112_05', 3)
    sprite('jn112_06', 3)
    sprite('jn112_07', 3)
    sprite('jn112_08', 3)


@State
def CmnActUkemiLandNLanding():
    sprite('jn020_11', 3)
    sprite('jn020_12', 3)
    sprite('jn020_13', 3)
    sprite('jn020_14', 3)


@State
def CmnActMidGuardPre():
    sprite('jn040_00', 3)
    sprite('jn040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('jn040_02', 5)
    sprite('jn040_03', 5)
    sprite('jn040_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('jn040_01', 3)
    sprite('jn040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('jn040_05', 3)
    label(0)
    sprite('jn040_02', 5)
    sprite('jn040_03', 5)
    sprite('jn040_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('jn040_01', 3)
    sprite('jn040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('jn041_00', 3)
    sprite('jn041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('jn041_02', 5)
    sprite('jn041_03', 5)
    sprite('jn041_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('jn041_01', 3)
    sprite('jn041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('jn041_05', 3)
    label(0)
    sprite('jn041_02', 5)
    sprite('jn041_03', 5)
    sprite('jn041_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('jn041_01', 3)
    sprite('jn041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('jn043_00', 3)
    sprite('jn043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('jn043_02', 5)
    sprite('jn043_03', 5)
    sprite('jn043_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('jn043_01', 3)
    sprite('jn043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('jn043_05', 3)
    label(0)
    sprite('jn043_02', 5)
    sprite('jn043_03', 5)
    sprite('jn043_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('jn043_01', 3)
    sprite('jn043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('jn045_00', 3)
    sprite('jn045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('jn045_02', 5)
    sprite('jn045_03', 5)
    sprite('jn045_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('jn045_01', 3)
    sprite('jn045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('jn045_05', 3)
    label(0)
    sprite('jn045_02', 5)
    sprite('jn045_03', 5)
    sprite('jn045_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('jn045_01', 3)
    sprite('jn045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('jn090_00', 2)
    sprite('jn090_01', 2)
    sprite('jn090_02', 1)
    SetCommonActionMark(1)
    sprite('jn090_03', 6)
    sprite('jn090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('jn091_00', 2)
    sprite('jn091_01', 2)
    sprite('jn091_02', 1)
    SetCommonActionMark(1)
    sprite('jn091_03', 6)
    sprite('jn091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('jn092_00', 2)
    sprite('jn092_01', 2)
    sprite('jn092_02', 1)
    SetCommonActionMark(1)
    sprite('jn092_03', 6)
    sprite('jn092_04', 6)


@State
def CmnActAirTurn():
    sprite('jn025_00', 4)
    sprite('jn025_01', 4)
    sprite('jn025_02', 4)


@State
def CmnActLockWait():
    sprite('________', 10)
    sprite('________', 10)
    sprite('jn040_01', 3)
    sprite('jn040_00', 3)


@State
def CmnActLockReject():
    sprite('jn312_00', 4)
    sprite('jn312_01', 4)
    sprite('jn312_02', 2)
    sprite('jn312_03', 3)
    sprite('jn312_04', 5)
    sprite('jn312_05', 5)
    sprite('jn312_06', 5)
    sprite('jn312_07', 5)
    sprite('jn312_08', 5)
    sprite('jn312_09', 5)
    sprite('jn312_10', 5)


@State
def CmnActAirLockWait():
    sprite('jn045_02', 1)
    sprite('jn045_01', 3)
    sprite('jn045_00', 3)


@State
def CmnActAirLockReject():
    sprite('jn322_00', 5)
    sprite('jn322_01', 2)
    sprite('jn322_02', 1)
    sprite('jn322_03', 3)
    sprite('jn322_04', 4)
    sprite('jn322_05', 4)
    sprite('jn322_06', 4)
    sprite('jn322_07', 4)
    sprite('jn322_08', 4)
    sprite('jn322_09', 4)


@State
def CmnActLandSpin():
    sprite('jn071_00', 4)
    sprite('jn071_01', 4)
    label(0)
    sprite('jn071_02', 4)
    sprite('jn071_03', 4)
    sprite('jn071_04', 4)
    sprite('jn071_05', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('jn071_06', 6)
    sprite('jn071_07', 6)
    sprite('jn071_08', 4)


@State
def CmnActVertSpin():
    label(0)
    sprite('jn071_02', 4)
    sprite('jn071_03', 4)
    sprite('jn071_04', 4)
    sprite('jn071_05', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('jn077_90', 2)
    sprite('jn077_91', 2)
    sprite('jn077_90ex01', 2)
    sprite('jn077_91ex01', 2)
    sprite('jn077_90ex02', 2)
    sprite('jn077_91ex02', 2)
    sprite('jn077_90ex03', 2)
    sprite('jn077_91ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('jn077_00', 3)
    label(0)
    sprite('jn077_01', 3)
    sprite('jn077_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('jn077_03', 3)
    sprite('jn077_04', 3)
    sprite('jn077_05', 3)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('jn060_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('jn060_10', 5)
    sprite('jn060_11', 4)


@State
def CmnActBurstBegin():
    sprite('jn331_00', 2)
    label(0)
    sprite('jn331_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('jn331_02', 3)
    label(0)
    sprite('jn331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('jn331_04', 2)
    sprite('jn331_05', 2)
    sprite('jn331_06', 2)


@State
def CmnActAirBurstBegin():
    sprite('jn332_00', 2)
    label(0)
    sprite('jn332_01', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('jn332_02', 3)
    sprite('jn332_03', 3)
    label(0)
    sprite('jn332_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('jn332_05', 3)
    sprite('jn332_06', 3)
    sprite('jn020_05', 3)
    sprite('jn020_06', 3)
    sprite('jn020_07', 3)
    label(0)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('jn333_00', 3)
    sprite('jn333_01', 3)
    sprite('jn333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('jn333_03', 32767)
    CreateObject('EMB_JN_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('jn333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)
    sprite('jn333_06', 3)
    sprite('jn333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('jn333_08', 4)
    sprite('jn333_09', 4)
    sprite('jn333_10', 4)


@State
def CmnActAirOverDriveBegin():
    sprite('jn333_11', 3)
    sprite('jn333_12', 3)
    sprite('jn333_13', 3)
    CharacterFlash(16639, 20, 1)
    sprite('jn333_14', 32767)
    CreateObject('EMB_JN_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('jn333_15', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)
    sprite('jn333_06', 3)
    sprite('jn333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('jn333_16', 4)
    sprite('jn333_17', 4)
    sprite('jn333_18', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        WhiffCancel('NmlAtk5A')
    sprite('jn200_00', 1)
    PerInertia(60)
    sprite('jn200_01', 3)
    sprite('jn200_02', 1)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jn200_03', 3)
    sprite('jn200_03', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('jn200_04', 4)
    sprite('jn200_05', 4)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(400)
        SingleProration(1)
        PushbackX(-5000)
        AirPushbackY(10000)
        AirPushbackX(-3000)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitJumpCancel(1)
    sprite('jn201_00', 2)
    sprite('jn201_01', 2)
    sprite('jn201_02', 2)
    RandomCommonVoiceline(1)
    sprite('jn201_03', 1)
    StartMultihit()
    sprite('jn201_03', 2)
    CommonSE('003_swing_grap_0_1')
    sprite('jn201_04', 2)
    sprite('jn201_05', 1)
    sprite('jn201_06', 1)
    sprite('jn201_07', 1)
    RefreshMultihit()
    PushbackX(-10000)
    AirPushbackX(-2600)
    AirPushbackY(18000)
    sprite('jn201_08', 4)
    Recovery()
    Unknown2063()
    sprite('jn201_09', 4)
    sprite('jn201_10', 4)
    sprite('jn201_11', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        UseSlashHitspark(1)
        AirUntechableTime(20)
        callSubroutine('CheckOverDriveNormal')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('jn202_00', 2)
    sprite('jn202_01', 2)
    RandomCommonVoiceline(2)
    sprite('jn202_02', 2)
    sprite('jn202_03', 3)
    sprite('jn202_04', 2)
    CreateObject('zan_b0', -1)
    CommonSE('009_swing_rapier_1')
    sprite('jn202_05', 2)
    sprite('jn202_05', 5)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn202_06', 2)
    sprite('jn202_08', 3)
    sprite('jn202_09', 3)
    sprite('jn202_10', 2)
    sprite('jn202_11', 1)
    sprite('jn202_12', 1)
    sprite('jn202_14', 1)
    CreateObject('EffNoutou', 0)
    sprite('jn202_16', 1)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(960)
        AttackP2(79)
        AirPushbackY(10000)
        AirPushbackX(18000)
        FreezeCount(1)
        FreezeTime(26)
        PushbackX(30400)
        HitAirUnblockable(0)
        ProjectileLevel(1)
        UseSlashHitspark(1)
        UseFreezeHitspark(1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveFreeze')
        if SLOT_OverdriveTimer:
            FreezeTime(36)
        HitOrBlockCancel('ShortDash')
    sprite('jn203_00', 2)
    XImpulseAcceleration(25)
    sprite('jn203_01', 1)
    RandomCommonVoiceline(3)
    sprite('jn203_02', 2)
    CreateObject('ModelMagicCircle1', 0)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn203_03', 2)
    sprite('jn203_04', 2)
    sprite('jn203_05', 2)
    sprite('jn203_06', 2)
    sprite('jn203_07', 3)
    CreateObject('EffAtk5D', 0)
    ScreenShake(0, 5000)
    sprite('jn203_08', 8)
    sprite('jn203_09', 4)
    Recovery()
    Unknown2063()
    sprite('jn203_10', 4)
    sprite('jn203_11', 4)
    sprite('jn203_12', 4)
    sprite('jn203_13', 4)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('jn230_00', 3)
    PerInertia(60)
    sprite('jn230_01', 3)
    RandomCommonVoiceline(0)
    sprite('jn230_02', 4)
    CommonSE('003_swing_grap_0_0')
    sprite('jn230_03', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('jn230_04', 5)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(600)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('jn231_00', 2)
    sprite('jn231_01', 2)
    sprite('jn231_02', 1)
    sprite('jn231_03', 1)
    RandomCommonVoiceline(1)
    sprite('jn231_04', 1)
    sprite('jn231_05', 1)
    CommonSE('003_swing_grap_0_1')
    sprite('jn231_06', 2)
    sprite('jn231_07', 2)
    Recovery()
    Unknown2063()
    sprite('jn231_08', 2)
    sprite('jn231_09', 2)
    sprite('jn231_10', 2)
    sprite('jn231_11', 2)
    sprite('jn231_12', 2)
    sprite('jn231_13', 2)
    sprite('jn231_14', 1)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(930)
        AttackP1(90)
        UseSlashHitspark(1)
        AirUntechableTime(24)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        callSubroutine('CheckOverDriveNormal')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('jn232_00', 4)
    sprite('jn232_01', 4)
    sprite('jn232_02', 5)
    RandomCommonVoiceline(2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('jn232_03', 1)
    CommonSE('009_swing_rapier_2')
    sprite('jn232_04', 1)
    CreateObject('zan_d0', -1)
    sprite('jn232_06', 1)
    sprite('jn232_07', 3)
    sprite('jn232_07', 6)
    setInvincible(0)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn232_09', 3)
    sprite('jn232_11', 3)
    sprite('jn232_13', 3)
    sprite('jn232_14', 3)
    sprite('jn232_15', 3)
    WhiffCancelEnable(1)
    sprite('jn232_16', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn232_17', 5)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(16000)
        AirUntechableTime(26)
        CHHardKnockdown(1)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        callSubroutine('OverDrivePowerUpSkill')
        if SLOT_OverdriveTimer:
            FreezeCount(3)
            FreezeTime(30)
    sprite('jn235_00', 2)
    sprite('jn235_01', 2)
    sprite('jn235_02', 2)
    CommonSE('009_swing_rapier_1')
    SmartVoiceline('jn108')
    sprite('jn235_03', 4)
    sprite('jn235_04', 2)
    SetXCollisionFromOrigin(150)
    sprite('jn235_05', 4)
    CreateObject('zan235', -1)
    sprite('jn235_06', 4)
    Recovery()
    Unknown2063()
    SetXCollisionFromOrigin(-1)
    sprite('jn235_07', 4)
    sprite('jn235_08', 4)
    sprite('jn235_09', 4)
    sprite('jn235_10', 4)
    CreateObject('EffNoutou', 0)
    sprite('jn235_11', 4)
    sprite('jn235_12', 4)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        SpecialCancel(0)
        callSubroutine('CheckDriveFlash')
    sprite('jn233_00', 3)
    sprite('jn233_01', 3)
    RandomCommonVoiceline(3)
    sprite('jn233_02', 2)
    sprite('jn233_03', 2)
    sprite('jn233_04', 2)
    CreateObject('IcicleSub', 0)
    CreateObject('ModelMagicCircle4', 1)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn233_05', 2)
    CreateObject('IcicleAttack', 0)
    sprite('jn233_06', 2)
    sprite('jn233_07', 4)
    sprite('jn233_08', 4)
    sprite('jn233_09', 4)
    Recovery()
    Unknown2063()
    sprite('jn233_10', 4)
    sprite('jn233_11', 3)
    sprite('jn233_12', 3)
    CreateObject('EffNoutou', 1)
    sprite('jn233_13', 3)
    SpecialCancel(1)
    HitJumpCancel(1)
    sprite('jn233_14', 4)
    sprite('jn233_15', 4)
    sprite('jn233_16', 4)
    sprite('jn233_17', 4)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
    sprite('jn250_00', 2)
    sprite('jn250_01', 2)
    sprite('jn250_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jn250_03', 3)
    sprite('jn250_03', 1)
    AttackOff()
    sprite('jn250_04', 4)
    Recovery()
    Unknown2063()
    sprite('jn250_05', 4)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AirPushbackX(3000)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('jn251_00', 2)
    sprite('jn251_01', 3)
    sprite('jn251_02', 3)
    RandomCommonVoiceline(1)
    sprite('jn251_03', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn251_04', 3)
    sprite('jn251_05', 1)
    sprite('jn251_05', 2)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn251_06', 4)
    sprite('jn251_07', 4)
    sprite('jn251_08', 4)
    sprite('jn251_09', 4)
    sprite('jn251_10', 4)
    sprite('jn251_11', 4)
    sprite('jn251_12', 4)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        AirPushbackX(8000)
        AirPushbackY(23000)
        AirUntechableTime(19)
        UseSlashHitspark(1)
        callSubroutine('CheckOverDriveNormal')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('jn252_00', 2)
    sprite('jn252_01', 2)
    sprite('jn252_01', 2)
    RandomCommonVoiceline(2)
    sprite('jn252_02', 4)
    sprite('jn252_03', 2)
    sprite('jn252_04', 2)
    CreateObject('zan_e0', -1)
    CommonSE('009_swing_rapier_1')
    sprite('jn252_05', 3)
    sprite('jn252_06', 3)
    Recovery()
    Unknown2063()
    sprite('jn252_07', 3)
    sprite('jn252_08', 3)
    sprite('jn252_09', 3)
    sprite('jn252_10', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn252_11', 3)
    sprite('jn252_12', 3)
    sprite('jn252_13', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        AirPushbackX(8000)
        AirPushbackY(23000)
        AirUntechableTime(19)
        callSubroutine('CheckOverDriveNormal')
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitJumpCancel(1)
    sprite('jn412_00', 5)
    sprite('jn412_01', 2)
    ForcedLandingRecovery(5, 1)
    SmartVoiceline('jn110')
    sprite('jn412_02', 2)
    CreateObject('zan412', 0)
    sprite('jn412_03', 1)
    CommonSE('009_swing_rapier_1')
    sprite('jn412_03', 2)
    sprite('jn412_04', 6)
    EndYPhysicsImpulse()
    Recovery()
    Unknown2063()
    sprite('jn412_05', 2)
    sprite('jn412_06', 2)
    sprite('jn412_07', 4)
    CreateObject('EffNoutou', 0)
    sprite('jn412_08', 3)
    sprite('jn412_09', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(970)
        AttackP1(80)
        AttackP2(82)
        UseSlashHitspark(1)
        HitOverhead(0)
        AirPushbackY(12000)
        YImpulseBeforeWallbounce(1600)
        FreezeCount(1)
        FreezeTime(50)
        StrikeProjectileLevel(1)
        ProjectileLevel(1)
        MoveAttributes(1, 0, 0, 0, 0)
        UseFreezeHitspark(1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveFreeze')
        if SLOT_OverdriveTimer:
            FreezeTime(60)
    sprite('jn253_00', 3)
    sprite('jn253_01', 3)
    RandomCommonVoiceline(3)
    sprite('jn253_02', 3)
    sprite('jn253_03', 3)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    CreateObject('ModelMagicCircle3', 1)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    ForcedLandingRecovery(6, 1)
    sprite('jn253_04', 3)
    CreateObject('EffAtk8D', 0)
    sprite('jn253_05', 3)
    CreateObject('EffNoutou', 1)
    sprite('jn253_06', 3)
    Recovery()
    Unknown2063()
    sprite('jn253_07', 3)
    sprite('jn253_08', 3)
    sprite('jn253_09', 5)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(60)
    YAccel(30)
    EndYPhysicsImpulse()
    sprite('jn253_10', 5)
    sprite('jn253_11', 5)
    sprite('jn253_12', 5)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(640)
        AttackP1(80)
        BonusProration(110)
        HitOverhead(2)
        PushbackX(14000)
        AirPushbackY(-30000)
        Hitstun(24)
        GroundedHitstunAnimation(3)
        HardKnockdown(10)
        StarterRating(2)
        SpecialCancel(0)
    sprite('jn210_00', 3)
    sprite('jn210_01', 3)
    RandomCommonVoiceline(1)
    sprite('jn210_02', 3)
    CommonSE('008_swing_pole_0')
    sprite('jn210_03', 3)
    sprite('jn210_04', 3)
    CommonSE('008_swing_pole_0')
    sprite('jn210_05', 3)
    sprite('jn210_06', 3)
    CommonSE('008_swing_pole_0')
    sprite('jn210_07', 2)
    Recovery()
    Unknown2063()
    sprite('jn210_08', 2)
    sprite('jn210_09', 2)
    sprite('jn210_10', 2)
    sprite('jn210_11', 2)
    sprite('jn210_12', 2)
    sprite('jn210_13', 2)
    sprite('jn210_14', 2)
    sprite('jn210_15', 2)
    sprite('jn210_16', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(840)
        AttackP1(90)
        Hitstun(26)
        AirUntechableTime(26)
        AirPushbackX(10000)
        AirPushbackY(13000)
        MoveAttributes(1, 0, 0, 0, 0)
        HitAirUnblockable(0)
        uponSendToLabel(LANDING, 1)
    sprite('jn211_00', 1)
    PerInertia(60)
    sprite('jn211_01', 1)
    sprite('jn211_02', 1)
    sprite('jn211_03', 3)
    PreDashEffects(0, 0, 1)
    physicsXImpulse(16000)
    physicsYImpulse(20000)
    setGravity(2000)
    RandomCommonVoiceline(1)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    sprite('jn211_04', 3)
    sprite('jn211_05', 2)
    sprite('jn211_06', 2)
    sprite('jn211_07', 3)
    sprite('jn211_08', 2)
    sprite('jn211_09', 4)
    CommonSE('004_swing_grap_1_1')
    sprite('jn211_10', 2)
    setInvincible(0)
    Recovery()
    sprite('jn211_11', 32767)
    label(1)
    sprite('jn211_12', 3)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    sprite('jn020_11', 3)
    sprite('jn020_12', 3)
    sprite('jn020_13', 3)
    sprite('jn020_14', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1060)
        AttackP2(84)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(18000)
        AirPushbackY(28000)
        AirUntechableTime(36)
        PushbackX(22000)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        callSubroutine('OverDrivePowerUpSkill')
        if SLOT_OverdriveTimer:
            FreezeCount(3)
            FreezeTime(45)
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        StayAfterMovement(1, 0)
        SetXCollisionFromOrigin(120)
    sprite('jn212_00', 2)
    sprite('jn212_01', 2)
    sprite('jn212_02', 2)
    sprite('jn212_03', 3)
    SmartVoiceline('jn109')
    sprite('jn212_04', 3)
    sprite('jn212_05', 3)
    sprite('jn212_06', 3)
    sprite('jn212_07', 3)
    CreateObject('zan_a0', -1)
    CommonSE('009_swing_rapier_2')
    sprite('jn212_08', 3)
    Recovery()
    Unknown2063()
    sprite('jn212_09', 3)
    sprite('jn212_10', 3)
    sprite('jn212_11', 3)
    sprite('jn212_12', 3)
    sprite('jn212_13', 3)
    sprite('jn212_14', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn212_15', 5)
    sprite('jn212_16', 5)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        NoAttackDuringAction(1)
        StayAfterMovement(1, 0)
        callSubroutine('CheckDriveFlash')
    sprite('jn213_00', 4)
    sprite('jn213_01', 4)
    RandomCommonVoiceline(3)
    sprite('jn213_02', 4)
    SetXCollisionFromOrigin(120)
    sprite('jn213_03', 4)
    CreateObject('ModelMagicCircle2', 1)
    AltKnockdownEffects(100, 0, 1)
    ScreenShake(0, 5000)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn213_04', 4)
    SetXCollisionFromOrigin(150)
    sprite('jn213_05', 4)
    sprite('jn213_06', 4)
    CreateObject('EffAtk6D', 0)
    sprite('jn213_07', 4)
    sprite('jn213_08', 7)
    sprite('jn213_09', 4)
    SetXCollisionFromOrigin(120)
    Recovery()
    Unknown2063()
    sprite('jn213_10', 4)
    SetXCollisionFromOrigin(-1)
    sprite('jn213_11', 3)
    sprite('jn213_12', 3)
    sprite('jn213_13', 3)
    sprite('jn213_14', 3)
    sprite('jn213_15', 3)
    sprite('jn213_16', 3)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 20)
    if random_(2, 0, 50):
        Voiceline('jn404')
    else:
        Voiceline('jn405')
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 8)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    loopRest()
    ExitState()


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        UseSlashHitspark(1)
    sprite('jn202_00', 3)
    sprite('jn202_01', 3)
    sprite('jn202_02', 3)
    sprite('jn202_03', 3)
    sprite('jn202_04', 2)
    CreateObject('zan_b0', -1)
    CommonSE('009_swing_rapier_1')
    sprite('jn202_05', 3)
    sprite('jn202_06', 3)
    sprite('jn202_07', 3)
    sprite('jn202_08', 3)
    sprite('jn202_09', 3)
    sprite('jn202_10', 4)
    sprite('jn202_11', 4)
    sprite('jn202_12', 4)
    sprite('jn202_13', 4)
    sprite('jn202_14', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn202_15', 3)
    sprite('jn202_16', 3)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(11)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(60)
        HardKnockdown(1)
        GroundBounce(1)
        BouncePercentage(30)
        PushbackX(8000)
        UseSlashHitspark(1)
        Blockstun(24)
        HitBackReturnIgnore(1)
        StarterRating(2)
        callSubroutine('CheckOverDriveNormal')
        FreezeTime(60)

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
    sprite('jn414_00', 3)
    sprite('jn414_01', 1)
    E0EAEffect('GuardCrushWind', 0)
    Voiceline('jn159')
    HeatChange(-2500)
    sprite('jn414_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('jn414_02', 2)
    label(100)
    sprite('jn414_03', 3)
    sprite('jn414_04', 3)
    sprite('jn414_05', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('jn414_06', 2)
    CommonSE('009_swing_rapier_1')
    sprite('jn414_07', 2)
    sprite('jn414_08', 2)
    CommonSE('009_swing_rapier_2')
    CreateObject('zan414', -1)
    sprite('jn414_09', 2)
    StartMultihit()
    sprite('jn414_09', 1)
    sprite('jn414_10', 6)
    EnableAfterimage(0)
    sprite('jn414_11', 6)
    CreateObject('EffNoutou', 0)
    sprite('jn414_12', 6)
    sprite('jn414_13', 4)
    sprite('jn414_14', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('jn310_00', 3)
    sprite('jn310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('jn310_02', 3)
    sprite('jn310_02', 3)
    AttackOff()
    sprite('jn310_03', 6)
    SmartVoiceline('jn155')
    sprite('jn310_04', 8)
    sprite('jn310_05', 6)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        SetZLine(0, 50)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        StarterRating(2)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Crumple(28)
        Stagger(28)
        PushbackX(6000)
        Hitstop(0)
        SpecialCancel(0)
    sprite('jn310_02', 2)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('jn311_00', 5)
    CreateObject('jnef311', 1)
    CreateObject('ModelMagicCircle2', 1)
    Voiceline('jn153')
    sprite('jn311_01', 4)
    sprite('jn311_02', 4)
    sprite('jn311_03', 4)
    sprite('jn311_04', 4)
    sprite('jn311_05', 4)
    sprite('jn311_06', 4)
    sprite('jn311_07', 5)
    RefreshMultihit()
    Damage(1500)
    AttackP2(50)
    AirPushbackX(12000)
    YImpulseBeforeWallbounce(1400)
    Hitstop(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    FreezeCount(3)
    FreezeTime(55)

    def upon_OPPONENT_HIT():
        SpecialCancel(1)
        HitOrBlockCancel('ShortDash')
    sprite('jn311_08', 4)
    sprite('jn311_09', 4)
    sprite('jn311_10', 4)
    sprite('jn311_11', 4)
    sprite('jn311_12', 4)
    sprite('jn311_13', 4)
    sprite('jn311_14', 4)
    sprite('jn311_15', 4)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('jn310_00', 3)
    sprite('jn310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('jn310_02', 3)
    sprite('jn310_02', 3)
    AttackOff()
    sprite('jn310_03', 6)
    SmartVoiceline('jn155')
    sprite('jn310_04', 8)
    sprite('jn310_05', 6)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        FreezeCount(3)
        FreezeTime(55)
        AirPushbackX(12000)
        YImpulseBeforeWallbounce(1400)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        StayAfterMovement(1, 0)
        SetZLine(0, 50)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        AttackDirection(1)
        HitOrBlockCancel('ShortDash')
    sprite('jn310_02', 2)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('jn313_00', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn313_01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn313_02', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('jn313_03', 5)
    SmartVoiceline('jn153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn313_04', 5)
    CreateObject('jnef311', 1)
    CreateObject('ModelMagicCircle2', 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn313_05', 30)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn313_06', 5)
    sprite('jn313_07', 5)
    sprite('jn313_08', 5)
    sprite('jn313_09', 5)
    sprite('jn313_10', 5)
    sprite('jn313_11', 5)
    sprite('jn313_12', 5)
    sprite('jn313_13', 5)
    sprite('jn313_14', 5)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('jn320_00', 3)
    sprite('jn320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('jn320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('jn320_03', 3)
    sprite('jn320_04', 3)
    SmartVoiceline('jn155')
    sprite('jn320_05', 3)
    sprite('jn320_06', 6)
    sprite('jn320_07', 4)
    sprite('jn320_08', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(0)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        FreezeCount(3)
        FreezeTime(65)
        AirPushbackX(5000)
        AirPushbackY(30000)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        ForcedLandingRecovery(0, 0)
    sprite('jn321_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    ThrowLock(1)
    sprite('jn321_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SmartVoiceline('jn154')
    sprite('jn321_02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('jn321_03', 3)
    CreateObject('jnef321top', 1)
    CreateObject('jnef321bottom', 2)
    CreateObject('ModelMagicCircle3', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(3, 0, 0, 0, 0)
    sprite('jn321_04', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn321_05', 30)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jn321_06', 2)
    sprite('jn321_07', 2)
    ScreenShake(50000, 0)
    sprite('jn321_08', 4)
    sprite('jn321_09', 4)
    sprite('jn321_10', 4)
    sprite('jn321_11', 4)
    sprite('jn321_12', 4)
    EndYPhysicsImpulse()
    sprite('jn321_13', 4)
    sprite('jn321_14', 4)
    sprite('jn321_15', 4)


@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('jn032_00', 3)
    sprite('jn032_01', 3)
    sprite('jn032_02', 4)
    AirDashEffects(0)
    physicsXImpulse(30000)
    AddInertia(50000)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    sprite('jn032_11', 2)
    XImpulseAcceleration(50)
    sprite('jn032_12', 2)


@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckDriveFlash')
        callSubroutine('OverDrivePowerUpSkill')
        SLOT_58 = SLOT_OverdriveTimer
    sprite('jn400_00', 1)
    sprite('jn400_01', 1)
    Voiceline('jn200')
    sprite('jn400_02', 1)
    sprite('jn400_02', 4)
    CreateObject('ice_shot', 0)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
    sprite('jn400_03', 3)
    sprite('jn400_04', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn400_05', 3)
    sprite('jn400_06', 3)
    sprite('jn400_07', 3)
    sprite('jn400_08', 3)
    sprite('jn400_09', 3)
    sprite('jn400_10', 3)
    sprite('jn400_11', 3)
    sprite('jn400_12', 3)
    Recovery()
    sprite('jn400_13', 3)
    sprite('jn400_14', 2)
    sprite('jn400_15', 2)


@State
def Shot_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        HeatChange(-2500)
        CreateObject('jnef_25percent', -1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
    sprite('jn400_00', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    PrivateSE('jnse_22')
    sprite('jn400_01', 3)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    Voiceline('jn202')
    sprite('jn400_02', 9)
    CreateObject('ice_shot_ex2', 0)
    RegisterObject(7, 1)
    sprite('jn400_03', 3)
    sprite('jn400_04', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn400_05', 3)
    sprite('jn400_06', 3)
    sprite('jn400_07', 3)
    sprite('jn400_08', 3)
    sprite('jn400_09', 3)
    sprite('jn400_10', 3)
    sprite('jn400_11', 3)
    sprite('jn400_12', 3)
    Recovery()
    sprite('jn400_13', 3)
    sprite('jn400_14', 2)
    sprite('jn400_15', 2)
    EnableAfterimage(0)


@State
def AirShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        EndMomentum(1)
        ForcedLandingRecovery(9, 1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('OverDrivePowerUpSkill')
        SLOT_58 = SLOT_OverdriveTimer
    sprite('jn402_00', 1)
    physicsXImpulse(-8000)
    SetAcceleration(100)
    physicsYImpulse(27000)
    setGravity(1500)
    sprite('jn402_00', 2)
    Voiceline('jn203')
    sprite('jn402_01', 3)
    CreateObject('air_ice_shot', 1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
    sprite('jn402_02', 3)
    sprite('jn402_03', 3)
    sprite('jn402_04', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn402_05', 2)
    sprite('jn402_06', 20)
    EndYPhysicsImpulse()
    sprite('jn402_07', 6)
    sprite('jn402_08', 6)


@State
def AirShot_D():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        HeatChange(-2500)
        CreateObject('jnef_25percent', -1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
    sprite('jn402_00', 3)
    EndMomentum(1)
    physicsXImpulse(-2000)
    physicsYImpulse(2000)
    sprite('jn402_00', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    PrivateSE('jnse_22')
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    ForcedLandingRecovery(9, 1)
    sprite('jn402_01', 3)
    Voiceline('jn205')
    sprite('jn402_02', 3)
    sprite('jn402_03', 3)
    CreateObject('air_ice_shot_ex2', 1)
    RegisterObject(7, 1)
    sprite('jn402_04', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn402_05', 2)
    sprite('jn402_06', 12)
    physicsXImpulse(-2000)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    sprite('jn402_07', 4)
    EnableAfterimage(0)
    sprite('jn402_08', 4)


@State
def RushAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(385)
        SingleProration(1)
        GroundedHitstunAnimation(4)
        AirPushbackX(2500)
        AirPushbackY(2500)
        PushbackX(3000)
        Hitstop(0)
        UseSlashHitspark(1)
        FatalCounter(1)
        if SLOT_OverdriveTimer:
            UseFreezeHitspark(1)
            SLOT_58 = 1

        def upon_OPPONENT_HIT():
            if SLOT_StateDuration >= 50:
                UseFreezeHitspark(1)
                SLOT_52 = 1
            AddActionMark(1)
            if SLOT_2 == 4:
                ResetPushback()
                ResetVerticalDrag()
                AirUntechableTime(40)
                AirHitstunAnimation(10)
                GroundedHitstunAnimation(2)
                Stagger(39)
                Crumple(29)
                PushbackX(12000)
                if SLOT_52:
                    FreezeCount(3)
                    FreezeTime(50)
                    GotoState('RushAssault_Freeze')
                if SLOT_58:
                    FreezeCount(5)
                    FreezeTime(50)
                BufferedOrPressedGoto('RushAssaultFinish')
        BlendMode_Normal()

        def upon_STATE_END():
            AlphaValue(255)
        callSubroutine('CheckDriveFlash')
    sprite('jn410_00', 5)
    HitBackReturnIgnore(1)
    loopRest()
    SLOT_51 = SLOT_51 + SLOT_29
    if not SLOT_51 < 300000:
        notConditionalSendToLabel(1)
    sprite('jn410_01', 1)
    HitBackReturnIgnore(0)
    sprite('jn410_02', 1)
    callSubroutine('OverDrivePowerUpSkill')
    Voiceline('jn213')
    sprite('jn410_03ex01', 2)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    BeginBuffer('RushAssaultFinish')
    sprite('jn410_04', 1)
    sprite('jn410_05', 1)
    AlphaValue(0)
    sprite('jn410_06', 1)
    LandingEffects(100, 1, 1)
    sprite('jn410_07ex01', 2)
    AlphaValue(255)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_08', 1)
    sprite('jn410_09', 1)
    AlphaValue(0)
    sprite('jn410_10', 1)
    AlphaValue(255)
    LandingEffects(100, 1, 1)
    sprite('jn410_11ex01', 2)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_12', 1)
    sprite('jn410_13', 1)
    AlphaValue(0)
    sprite('jn410_14', 1)
    AlphaValue(255)
    LandingEffects(100, 1, 1)
    sprite('jn410_15ex01', 2)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_16', 2)
    Recovery()
    sprite('jn410_17', 2)
    sprite('jn410_18', 4)
    sprite('jn410_19', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn410_19', 10)
    DisallowGoto('RushAssaultFinish')
    sprite('jn410_20', 5)
    loopRest()
    ExitState()
    label(1)
    sprite('jn430_25', 3)
    HitBackReturnIgnore(0)
    sprite('jn430_24', 5)
    sprite('jn430_23', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 15)
    Voiceline('jn039')
    sprite('jn430_25', 3)
    sprite('jn430_26', 3)


@State
def RushAssaultFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(400)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirPushbackY(10000)
        AirPushbackX(-5000)
        AirUntechableTime(40)
        PushbackX(-19800)
        FreezeCount(10)
        FreezeTime(70)
        Hitstop(0)
        UseSlashHitspark(1)
        IgnoreComboTime(1)
        AttackDirection(0)
        HeatChange(-2500)
        callSubroutine('CheckOverDriveSpecial')
        if SLOT_58:
            Damage(200)
            SingleProration(1)
            FreezeCountReset()
            FreezeTimeReset()
            UseFreezeHitspark(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SetActionMark(1)

        def upon_STATE_END():
            Visibility(0)
        CreateObject('jnef_25percent', -1)
        callSubroutine('CheckDriveFlash')
    sprite('jn433_01', 4)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    PrivateSE('jnse_21')
    sprite('jn433_02', 4)
    sprite('jn433_03', 4)
    sprite('jn433_04', 4)
    sprite('jn433_05', 4)
    sprite('jn433_07', 1)
    sprite('jn433_09', 1)
    sprite('jn433_11', 1)
    sprite('jn433_13', 1)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('jn433_14', 2)
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    TeleportToObject(22)
    AddX(200000)
    AbsoluteY(0)
    SetXCollisionFromOrigin(20)
    Visibility(1)
    if not SLOT_58:
        notConditionalSendToLabel(0)
    sprite('jn433_14', 2)
    RefreshMultihit()
    if SLOT_58:
        AirPushbackX(-1000)
        PushbackX(-1000)
    sprite('jn433_14', 2)
    RefreshMultihit()
    sprite('jn433_14', 2)
    RefreshMultihit()
    sprite('jn433_14', 2)
    RefreshMultihit()
    label(0)
    sprite('jn433_14', 2)
    SetXCollisionFromOrigin(-1)
    SetInertia(20000)
    Visibility(0)
    if SLOT_58:
        RefreshMultihit()
        FreezeCount(10)
        FreezeTime(70)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
    sprite('jn433_15', 3)
    physicsXImpulse(0)
    SetXCollisionFromOrigin(-1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('jn433_16', 3)
    sprite('jn433_17', 4)
    sprite('jn433_18', 4)
    sprite('jn433_19', 4)
    SetInertia(0)
    sprite('jn433_20', 4)
    sprite('jn433_21', 4)
    sprite('jn433_22', 4)
    sprite('jn433_23', 4)
    sprite('jn433_24', 4)
    sprite('jn433_25', 3)
    sprite('jn433_27', 2)
    sprite('jn433_28', 1)
    CreateObject('EffNoutou', 0)
    Voiceline('jn214')
    sprite('jn433_28', 1)
    if not SLOT_51 < 300000:
        if not SLOT_2:
            sendToLabel(9)
    sprite('jn433_30', 4)
    CreateObject('RushAssaultFinishAtkObj', -1)
    Recovery()
    sprite('jn433_31', 4)
    sprite('jn433_32', 4)
    sprite('jn433_33', 4)
    label(9)
    sprite('jn433_34', 4)
    sprite('jn433_35', 4)
    sprite('jn433_36', 4)
    sprite('jn000_00', 1)
    Flip()


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(640)
        AttackP1(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirUntechableTime(26)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        UseSlashHitspark(1)
        StarterRating(2)
        if SLOT_OverdriveTimer:
            FreezeCount(5)
            FreezeTime(45)
        HitOrBlockCancel('Assault_2nd')
        WhiffCancel('Assault_2nd')
        callSubroutine('CheckDriveFlash')
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 0)

        def upon_STATE_END():
            CreateObject('IceBoard_koware', -1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn408_00', 3)
    callSubroutine('OverDrivePowerUpSkill')
    CreateObject('IceBoard', -1)
    RegisterObject(4, 1)
    Voiceline('jn210')
    sprite('jn408_01', 3)
    physicsXImpulse(-3000)
    physicsYImpulse(4000)
    EndYPhysicsImpulse()
    sprite('jn408_02', 3)
    sprite('jn408_03', 2)
    sprite('jn408_04', 2)
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)
    CommonSE('000_airdash_0')
    physicsXImpulse(35000)
    SetYCollisionFromOrigin(60)
    SetXCollisionFromOrigin(150)
    ObjectUpon(FALLING, 32)
    sprite('jn408_06ex', 1)
    sprite('jn408_06ex', 1)
    WhiffCancelEnable(1)
    sprite('jn408_07ex', 2)
    sprite('jn408_06ex', 2)
    sprite('jn408_07ex', 2)
    label(0)
    sprite('jn408_08', 5)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(STATE_END)
    uponSendToLabel(LANDING, 100)
    DeleteObject(4)
    CreateObject('IceBoard_koware', -1)
    Recovery()
    SetYCollisionFromOrigin(-1)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(25)
    PerAcceleration(0)
    physicsYImpulse(14000)
    EndYPhysicsImpulse()
    ChainCancel(0)
    WhiffCancelEnable(0)
    label(9)
    sprite('jn408_09', 3)
    sprite('jn408_10', 3)
    loopRest()
    gotoLabel(9)
    label(100)
    EndMomentum(1)
    sprite('jn020_10', 2)
    sprite('jn020_11', 2)
    sprite('jn020_13', 3)


@State
def Assault_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(30)
        AirPushbackY(-28000)
        YImpulseBeforeWallbounce(1000)
        HardKnockdown(1)
        Hitstop(8)
        CHStateIfCHStart(3)
        MoveAttributes(1, 0, 0, 0, 0)
        UseSlashHitspark(1)
        if SLOT_OverdriveTimer:
            FreezeCount(5)
            FreezeTime(45)
        PushCollisionHeightLow(120000)
        uponSendToLabel(LANDING, 3)
    sprite('jn408_11', 1)
    physicsXImpulse(20000)
    physicsYImpulse(25000)
    setGravity(2500)
    sprite('jn408_12', 3)
    sprite('jn408_13', 3)
    sprite('jn408_14', 3)
    Voiceline('jn211')
    sprite('jn408_15', 3)
    XImpulseAcceleration(80)
    sprite('jn408_16ex01', 2)
    CreateObject('zan408', 0)
    CommonSE('009_swing_rapier_1')
    XImpulseAcceleration(80)
    sprite('jn408_17', 2)
    sprite('jn408_18', 2)
    Recovery()
    sprite('jn408_19', 32767)
    label(3)
    sprite('jn408_20', 3)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    PushCollisionHeightLow(-1)
    sprite('jn408_21', 3)
    sprite('jn408_22', 2)
    sprite('jn408_23', 2)
    sprite('jn408_24', 2)
    sprite('jn408_25', 2)
    sprite('jn408_26', 2)
    CreateObject('EffNoutou', 0)
    sprite('jn408_27', 2)
    sprite('jn408_28', 2)


@State
def Assault_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(640)
        AttackP1(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        Hitstun(26)
        AirUntechableTime(40)
        NonCornerWallbounce(1)
        Wallbounce(1)
        WallbounceReboundTime(5)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        UseSlashHitspark(1)
        StarterRating(2)
        FreezeCount(10)
        FreezeTime(45)
        HitOrBlockCancel('Assault_D_2nd')
        WhiffCancel('Assault_D_2nd')
        HeatChange(-2500)
        CreateObject('jnef_25percent', -1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 0)

        def upon_STATE_END():
            CreateObject('IceBoard_koware', -1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn408_00', 3)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    CreateObject('IceBoard', -1)
    RegisterObject(4, 1)
    Voiceline('jn210')
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    PrivateSE('jnse_22')
    sprite('jn408_01', 3)
    physicsXImpulse(-5000)
    physicsYImpulse(4000)
    EndYPhysicsImpulse()
    sprite('jn408_02', 3)
    sprite('jn408_03', 2)
    sprite('jn408_04', 2)
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)
    CommonSE('000_airdash_0')
    physicsXImpulse(50000)
    SetAcceleration(3000)
    SetYCollisionFromOrigin(60)
    SetXCollisionFromOrigin(150)
    ObjectUpon(FALLING, 32)
    sprite('jn408_06ex', 1)
    sprite('jn408_06ex', 1)
    WhiffCancelEnable(1)
    sprite('jn408_07ex', 2)
    sprite('jn408_06ex', 2)
    sprite('jn408_07ex', 2)
    sprite('jn408_06ex', 2)
    label(0)
    sprite('jn408_08', 5)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(STATE_END)
    uponSendToLabel(LANDING, 100)
    DeleteObject(4)
    CreateObject('IceBoard_koware', -1)
    EnableAfterimage(1)
    Recovery()
    SetYCollisionFromOrigin(-1)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(25)
    PerAcceleration(0)
    physicsYImpulse(14000)
    EndYPhysicsImpulse()
    ChainCancel(0)
    WhiffCancelEnable(0)
    label(9)
    sprite('jn408_09', 3)
    sprite('jn408_10', 3)
    loopRest()
    gotoLabel(9)
    label(100)
    EndMomentum(1)
    sprite('jn020_10', 2)
    sprite('jn020_11', 2)
    sprite('jn020_13', 3)


@State
def Assault_D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackY(12000)
        AirPushbackX(48000)
        Floorslide(15)
        AirUntechableTime(50)
        CHStateIfCHStart(3)
        MoveAttributes(1, 0, 0, 0, 0)
        UseSlashHitspark(1)
        callSubroutine('CheckOverDriveSpecial')
        if SLOT_58:
            AirPushbackY(20000)
            Wallbounce(1)
            WallbounceReboundTime(10)
            AirHitstunAfterWallbounce(40)
            WallstickDuration(40)
            Wallstick(1)
        EnableAfterimage(1)
        PushCollisionHeightLow(120000)
        uponSendToLabel(LANDING, 3)
    sprite('jn409_00', 1)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    physicsXImpulse(24000)
    sprite('jn409_00', 1)
    ObjectUpon(STATE_END, 33)
    sprite('jn409_01', 2)
    physicsYImpulse(15000)
    setGravity(1500)
    sprite('jn409_02', 2)
    Voiceline('jn212')
    sprite('jn409_03', 3)
    sprite('jn409_04', 2)
    sprite('jn409_05', 2)
    sprite('jn409_06ex01', 3)
    CreateObject('zan409', 0)
    CommonSE('009_swing_rapier_0')
    XImpulseAcceleration(70)
    sprite('jn409_07', 3)
    Recovery()
    sprite('jn409_08', 3)
    sprite('jn409_09', 32767)
    label(3)
    sprite('jn409_10', 3)
    CreateObject('EffNoutou', 0)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    PushCollisionHeightLow(-1)
    EnableAfterimage(0)
    sprite('jn409_11', 3)
    sprite('jn409_12', 3)
    sprite('jn409_13', 3)
    sprite('jn409_14', 3)
    sprite('jn409_15', 3)


@State
def AirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(90)
        AttackP2(82)
        GroundedHitstunAnimation(2)
        Stagger(8)
        Crumple(99)
        AirHitstunAnimation(17)
        AirPushbackX(24000)
        AirPushbackY(-36000)
        MoveAttributes(1, 0, 0, 0, 0)
        AirUntechableTime(36)
        PushbackX(19800)
        HardKnockdown(1)
        UseSlashHitspark(1)
        StarterRating(2)
        if SLOT_OverdriveTimer:
            FreezeCount(5)
            FreezeTime(55)
        callSubroutine('CheckDriveFlash')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn413_00', 2)
    callSubroutine('OverDrivePowerUpSkill')
    XImpulseAcceleration(20)
    PerInertia(0)
    YAccel(0)
    PerGravity(-20)
    sprite('jn413_01', 2)
    sprite('jn413_02', 2)
    sprite('jn413_05', 3)
    Voiceline('jn215')
    sprite('jn413_06', 3)
    EndMomentum(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(1800)
    CommonSE('009_swing_rapier_2')
    PrivateSE('jnse_21')
    CreateObject('EFF413C', -1)
    sprite('jn413_07', 3)
    ForcedLandingRecovery(8, 1)
    sprite('jn413_08', 3)
    Recovery()
    XImpulseAcceleration(50)
    sprite('jn413_09', 3)
    sprite('jn413_10', 6)
    CreateObject('EffNoutou', 0)
    XImpulseAcceleration(50)
    sprite('jn413_11', 5)
    XImpulseAcceleration(50)
    sprite('jn413_12', 5)
    sprite('jn020_05', 3)
    sprite('jn020_06', 3)
    sprite('jn020_07', 3)
    label(0)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    gotoLabel(0)


@State
def AirAssault_D():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(600)
        AttackP1(90)
        AttackP2(100)
        AirPushbackY(10000)
        AirPushbackX(-3000)
        MoveAttributes(1, 0, 0, 0, 0)
        FreezeCount(10)
        FreezeTime(80)
        Hitstop(6)
        PreventGroundedHit(1)
        UseSlashHitspark(1)
        StarterRating(2)
        HeatChange(-2500)
        CreateObject('jnef_25percent', -1)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn413_00', 2)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    PrivateSE('jnse_22')
    XImpulseAcceleration(20)
    PerInertia(0)
    YAccel(0)
    PerGravity(-20)
    sprite('jn413_01', 2)
    Voiceline('jn216')
    sprite('jn413_02', 2)
    CommonSE('009_swing_rapier_1')
    sprite('jn413_03', 2)
    CreateObject('EFF413D', -1)
    StartMultihit()
    sprite('jn413_03', 1)
    EndMomentum(1)
    sprite('jn413_04', 3)
    sprite('jn413_05', 3)
    sprite('jn413_06', 3)
    EndMomentum(1)
    physicsXImpulse(-6000)
    physicsYImpulse(18000)
    setGravity(2000)
    CommonSE('009_swing_rapier_2')
    PrivateSE('jnse_21')
    CreateObject('EFF413C', -1)
    sprite('jn413_07', 3)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1200)
    GroundedHitstunAnimation(2)
    Stagger(10)
    Crumple(99)
    AirHitstunAnimation(17)
    AirPushbackX(24000)
    AirPushbackY(-36000)
    AirUntechableTime(42)
    HardKnockdown(1)
    FreezeCountReset()
    AttackP2(82)
    HitOverhead(2)
    Hitstop(12)
    PreventGroundedHit(0)
    if SLOT_58:
        AirPushbackX(5000)
        AirPushbackY(-80000)
        GroundBounce(1)
        BouncePercentage(45)
        AirUntechableTime(90)
        HardKnockdownReset()
    ForcedLandingRecovery(6, 1)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('jn413_08', 3)
    XImpulseAcceleration(80)
    Recovery()
    sprite('jn413_09', 3)
    sprite('jn413_10', 6)
    XImpulseAcceleration(80)
    CreateObject('EffNoutou', 0)
    sprite('jn413_11', 5)
    XImpulseAcceleration(80)
    sprite('jn413_12', 5)


@State
def AntiAir_Fast():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(950)
        AttackP1(80)
        AttackP2(82)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(18000)
        CHAirPushbackX(16000)
        AirPushbackY(52000)
        AirUntechableTime(45)
        EnemyHitstopAddition(0, 5, 5)
        PushbackX(12000)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        StarterRating(2)
        if SLOT_OverdriveTimer:
            FreezeCount(5)
            FreezeTime(55)
        callSubroutine('CheckDriveFlash')
    sprite('jn405_00', 2)
    callSubroutine('OverDrivePowerUpSkill')
    sprite('jn405_01', 2)
    sprite('jn405_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('jn405_03', 1)
    CreateObject('EFF28AtkA', 0)
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    Voiceline('jn206')
    sprite('jn405_04', 3)
    PrivateSE('jnse_21')
    sprite('jn405_05', 3)
    setInvincible(0)
    Recovery()
    sprite('jn405_06', 3)
    sprite('jn405_07', 2)
    sprite('jn405_07ex', 2)
    sprite('jn405_08', 2)
    sprite('jn405_08ex', 2)
    sprite('jn405_09', 2)
    sprite('jn405_09ex', 2)
    sprite('jn405_10', 2)
    sprite('jn405_11', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn405_12', 2)
    sprite('jn405_13', 2)
    sprite('jn405_14', 2)
    sprite('jn405_15', 2)
    sprite('jn405_16', 2)


@State
def AntiAir_Slow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(60)
        AttackP2(92)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        CHAirHitstunAnimation(18)
        CHGroundedHitstunAnimation(18)
        AirPushbackY(37000)
        CHAirPushbackX(2000)
        CHAirPushbackY(43000)
        AirUntechableTime(56)
        Hitstop(10)
        EnemyHitstopAddition(0, 8, 8)
        StarterRating(0)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        if SLOT_OverdriveTimer:
            FreezeCount(5)
            FreezeTime(70)
        setInvincible(1)
        callSubroutine('CheckDriveFlash')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn406_00', 2)
    callSubroutine('OverDrivePowerUpSkill')
    sprite('jn406_01', 2)
    sprite('jn406_02', 2)
    sprite('jn406_03', 2)
    CrouchState(1)
    sprite('jn406_04', 2)
    sprite('jn406_05', 1)
    sprite('jn406_06', 1)
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    Voiceline('jn207')
    sprite('jn406_07', 3)
    PrivateSE('jnse_21')
    CreateObject('EFF28AtkC', 0)
    sprite('jn406_08', 3)
    setInvincible(0)
    sprite('jn406_09', 3)
    sprite('jn406_10', 3)
    sprite('jn406_11', 3)
    sprite('jn406_12', 3)
    sprite('jn406_13', 4)
    sprite('jn406_14', 4)
    sprite('jn406_15', 4)
    sprite('jn406_16', 4)
    sprite('jn406_17', 4)
    CreateObject('EffNoutou', 1)
    sprite('jn406_18', 4)
    sprite('jn406_19', 4)
    sprite('jn406_20', 3)
    sprite('jn406_21', 3)
    CrouchState(0)


@State
def AntiAir_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(900)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10000)
        AirUntechableTime(44)
        Hitstop(1)
        FreezeCount(10)
        FreezeTime(50)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        AttackDirection(0)
        StarterRating(0)
        HeatChange(-2500)
        CreateObject('jnef_25percent', -1)
        setInvincible(1)
        StayAfterMovement(1, 0)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('jn407_00', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    PrivateSE('jnse_22')
    sprite('jn407_01', 3)
    sprite('jn407_02', 3)
    sprite('jn407_03', 3)
    sprite('jn407_04', 3)
    PrivateSE('jnse_21')
    CreateObject('zan407', 0)
    CommonSE('009_swing_rapier_0')
    Voiceline('jn208')
    sprite('jn407_05', 3)
    sprite('jn407_06', 3)
    sprite('jn407_07', 3)
    setInvincible(0)
    sprite('jn407_08', 3)
    sprite('jn407_26', 3)
    sprite('jn407_26', 54)
    uponSendToLabel(RELEASE_D, 0)
    sprite('jn407_26', 1)
    AltKnockdownEffects(100, 1, 1)
    HitOverhead(4)
    HitLow(4)
    HitAirUnblockable(4)
    FatalCounter(1)
    loopRest()
    label(0)
    clearUponHandler(RELEASE_D)
    sprite('jn407_09', 3)
    sprite('jn407_10', 2)
    sprite('jn407_11', 2)
    PrivateSE('jnse_21')
    CreateObject('EFF28AtkD', 0)
    sprite('jn407_12', 2)
    StartMultihit()
    sprite('jn407_12', 1)
    RefreshMultihit()
    Damage(1200)
    if SLOT_137:
        DamageMultiplier(80)
    Hitstop(20)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(48000)
    AirPushbackY(12000)
    WallbounceReboundTime(5)
    AirHitstunAfterWallbounce(44)
    Wallstick(1)
    WallstickDuration(30)
    HardKnockdown(1)
    Floorslide(30)
    FreezeCountReset()
    HitAirUnblockable(0)
    StarterRating(3)
    if SLOT_58:
        WallbounceReboundTimeReset()
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    Voiceline('jn209')
    sprite('jn407_13', 3)
    sprite('jn407_14', 3)
    sprite('jn407_15', 3)
    sprite('jn407_16', 3)
    sprite('jn407_17', 3)
    sprite('jn407_18', 3)
    sprite('jn407_19', 3)
    sprite('jn407_20', 3)
    sprite('jn407_21', 5)
    sprite('jn407_22', 4)
    EnableAfterimage(0)
    sprite('jn407_23', 3)
    sprite('jn407_24', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn407_25', 3)


@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        NoAttackDuringAction(1)
        setInvincible(1)
    sprite('jn430_00', 1)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn250')
    sprite('jn430_00', 1)
    sprite('jn430_01', 2)
    sprite('jn430_02', 2)
    sprite('jn430_03', 2)
    sprite('jn430_04', 2)
    sprite('jn430_05', 2)
    sprite('jn430_06', 2)
    sprite('jn430_07', 3)
    sprite('jn430_08', 3)
    sprite('jn430_09', 3)
    sprite('jn430_10', 3)
    CommonSE('009_swing_rapier_1')
    sprite('jn430_11', 3)
    sprite('jn430_12', 3)
    sprite('jn430_13', 3)
    setInvincible(0)
    sprite('jn430_14', 3)
    CommonSE('006_swing_blade_1')
    sprite('jn430_15', 3)
    CreateObject('UltimateSlashShotObj', 0)
    CommonSE('000_airdash_0')
    sprite('jn430_16', 3)
    sprite('jn430_17', 3)
    sprite('jn430_18', 3)
    sprite('jn430_19', 3)
    sprite('jn430_20', 3)
    sprite('jn430_21', 3)
    sprite('jn430_22', 3)
    sprite('jn430_23', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 3)
    sprite('jn430_25', 3)
    sprite('jn430_26', 3)


@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)

        def upon_32():
            setInvincible(1)
            SetActionMark(1)
        AttackType(4)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
    sprite('jn430_00', 1)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn250')
    sprite('jn430_00', 1)
    sprite('jn430_01', 2)
    sprite('jn430_02', 2)
    sprite('jn430_03', 2)
    sprite('jn430_04', 2)
    sprite('jn430_05', 2)
    sprite('jn430_06', 2)
    sprite('jn430_07', 3)
    sprite('jn430_08', 3)
    sprite('jn430_09', 3)
    sprite('jn430_10', 3)
    CommonSE('009_swing_rapier_1')
    sprite('jn430_11', 3)
    sprite('jn430_12', 3)
    sprite('jn430_13', 3)
    setInvincible(0)
    sprite('jn430_14', 3)
    CommonSE('006_swing_blade_1')
    sprite('jn430_15', 3)
    CreateObject('OverDriveSlashShotObj', 0)
    CommonSE('000_airdash_0')
    sprite('jn430_16', 3)
    sprite('jn430_17', 3)
    sprite('jn430_18', 3)
    sprite('jn430_19', 3)
    sprite('jn430_20', 3)
    sprite('jn430_21', 3)
    if SLOT_2:
        enterState('UltimateShotAddAttack')
    clearUponHandler(32)
    sprite('jn430_22', 3)
    sprite('jn430_23', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 3)
    sprite('jn430_25', 3)
    sprite('jn430_26', 3)


@State
def UltimateShotAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackType(4)
        StayAfterMovement(1, 0)
        setInvincible(1)
        AttackOff()

        def upon_32():
            AddActionMark(1)
    sprite('jn330_03', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_04', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_05', 3)
    Voiceline('jn251')
    sprite('jn330_06', 12)
    sprite('jn330_06', 12)
    SetBackground(2)
    sprite('jn330_07', 3)
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    sprite('jn330_08', 5)
    CreateParticle('jnef_ast_attack', 0)
    CreateObject('AstralStartPtc', -1)
    PrivateSE('jnse_22')
    CreateObject('UltimateShotOverDrive', -1)
    ObjectUpon(STATE_END, 32)
    sprite('jn330_09', 5)
    sprite('jn330_10', 5)
    sprite('jn330_11', 5)
    CreateObject('UltimateShotOverDrive', -1)
    ObjectUpon(STATE_END, 33)
    sprite('jn330_11', 15)
    sprite('jn330_11', 10)
    CreateObject('UltimateShotOverDrive', -1)
    ObjectUpon(STATE_END, 34)
    sprite('jn330_11', 20)
    sprite('jn330_12', 5)
    sprite('jn330_13', 5)
    sprite('jn330_14', 5)
    sprite('jn330_15', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_16', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_17', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_18', 4)
    CommonSE('008_swing_pole_0')
    sprite('jn330_19', 4)
    Voiceline('jn255')
    sprite('jn330_20', 4)
    sprite('jn330_21', 4)
    CreateObject('EffNoutou', 0)
    sprite('jn330_22', 4)
    if SLOT_2:
        CreateObject('OverDriveSlashShotFinish', -1)
        ScreenShake(40000, 40000)
        TriggerUponForState('UltimateShotOverDrive', 41)
    sprite('jn330_23', 4)
    sprite('jn330_24', 55)
    sprite('jn330_25', 8)
    sprite('jn330_26', 8)


@State
def UltimateAntiAirShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        NoAttackDuringAction(1)
        setInvincible(1)

        def upon_32():
            clearUponHandler(32)
            SLOT_51 = 1
        callSubroutine('CheckDriveFlash')

        def upon_STATE_END():
            ExtendCollisionX(0)
    sprite('jn431_00', 2)
    sprite('jn431_01', 2)
    sprite('jn431_02', 2)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn252')
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    ExtendCollisionX(50)
    sprite('jn431_03', 2)
    sprite('jn431_04', 2)
    sprite('jn431_05', 2)
    sprite('jn431_06', 2)
    sprite('jn431_07', 3)
    sprite('jn431_08', 3)
    ExtendCollisionX(100)
    sprite('jn431_09', 3)
    CreateObject('IceBow', 0)
    CreateObject('IceArrow', 1)
    ObjectUpon(STATE_END, 32)
    CommonSE('018_ice_break_0')
    CommonSE('008_swing_pole_0')
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_09', 3)
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_09', 3)
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_13', 1)
    setInvincible(0)
    CreateObject('IceCircleA', 2)
    sprite('jn431_13', 1)
    CreateObject('IceCircleB', 3)
    sprite('jn431_13', 1)
    CreateObject('IceCircleC', 3)
    sprite('jn431_14', 3)
    CommonSE('009_swing_rapier_2')
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    EndMomentum(1)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    if not SLOT_51:
        sendToLabel(1)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    label(1)
    sprite('jn431_17', 3)
    sprite('jn431_18', 3)
    sprite('jn431_19', 3)
    sprite('jn431_20', 3)
    ExtendCollisionX(50)
    sprite('jn431_21', 3)
    ExtendCollisionX(0)
    sprite('jn431_22', 3)


@State
def UltimateAntiAirShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        NoAttackDuringAction(1)
        setInvincible(1)
        AttackType(4)

        def upon_32():
            clearUponHandler(32)
            SLOT_51 = 1
        callSubroutine('CheckDriveFlash')

        def upon_STATE_END():
            ExtendCollisionX(0)
    sprite('jn431_00', 2)
    sprite('jn431_01', 2)
    sprite('jn431_02', 2)
    DistortionSettings(45, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn252')
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    ExtendCollisionX(50)
    sprite('jn431_03', 2)
    sprite('jn431_04', 2)
    sprite('jn431_05', 2)
    sprite('jn431_06', 2)
    sprite('jn431_07', 3)
    sprite('jn431_08', 3)
    ExtendCollisionX(100)
    sprite('jn431_09', 3)
    CreateObject('IceBow', 0)
    CreateObject('IceArrow_OD', 1)
    ObjectUpon(STATE_END, 32)
    CommonSE('018_ice_break_0')
    CommonSE('008_swing_pole_0')
    PrivateSE('jnse_22')
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_09', 3)
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_09', 3)
    sprite('jn431_10', 3)
    sprite('jn431_11', 3)
    sprite('jn431_12', 3)
    sprite('jn431_13', 1)
    setInvincible(0)
    CreateObject('IceCircleA', 2)
    sprite('jn431_13', 1)
    CreateObject('IceCircleB', 3)
    sprite('jn431_13', 1)
    CreateObject('IceCircleC', 3)
    sprite('jn431_14', 3)
    CommonSE('009_swing_rapier_2')
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    loopRest()
    if not SLOT_51:
        sendToLabel(1)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    sprite('jn431_13', 3)
    sprite('jn431_14', 3)
    sprite('jn431_15', 3)
    sprite('jn431_16', 3)
    label(1)
    sprite('jn431_17', 3)
    sprite('jn431_18', 3)
    sprite('jn431_19', 3)
    sprite('jn431_20', 3)
    ExtendCollisionX(50)
    sprite('jn431_21', 3)
    ExtendCollisionX(0)
    sprite('jn431_22', 3)


@State
def UltimateAirShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        callSubroutine('CheckDriveFlash')
        EndMomentum(1)

        def upon_32():
            clearUponHandler(32)
            XImpulseAcceleration(80)
            PerGravity(50)
    sprite('jn253_00', 2)
    sprite('jn253_01', 2)
    sprite('jn253_01', 3)
    DistortionSettings(32, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn252')
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn253_02', 18)
    CreateObject('IceBow', 0)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceArrow', 1)
    ObjectUpon(STATE_END, 33)
    sprite('jn253_03', 3)
    sprite('jn402_00', 1)
    sprite('jn402_00', 2)
    sprite('jn402_01', 3)
    sprite('jn402_02', 3)
    SetInertia(0)
    physicsXImpulse(-10000)
    physicsYImpulse(36000)
    EndYPhysicsImpulse()
    ForcedLandingRecovery(16, 1)
    sprite('jn402_03', 3)
    sprite('jn402_04', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('jn402_05', 2)
    sprite('jn402_06', 16)
    setInvincible(0)
    CreateObject('IceCircleA', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceCircleB', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceCircleC', -1)
    ObjectUpon(STATE_END, 33)
    sprite('jn402_07', 4)
    sprite('jn402_08', 4)
    sprite('jn020_05', 3)
    sprite('jn020_06', 3)
    sprite('jn020_07', 3)

    def upon_LANDING():
        EndMomentum(1)
    label(0)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    gotoLabel(0)


@State
def UltimateAirShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        AttackType(4)
        callSubroutine('CheckDriveFlash')
        setGravity(0)
        EndMomentum(1)

        def upon_32():
            clearUponHandler(32)
            XImpulseAcceleration(80)
            PerGravity(50)
    sprite('jn253_00', 2)
    sprite('jn253_01', 2)
    sprite('jn253_01', 3)
    DistortionSettings(32, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    Voiceline('jn252')
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn253_02', 18)
    CreateObject('IceBow', 0)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceArrow_OD', 1)
    ObjectUpon(STATE_END, 33)
    sprite('jn253_03', 3)
    sprite('jn402_00', 1)
    sprite('jn402_00', 2)
    sprite('jn402_01', 3)
    sprite('jn402_02', 3)
    SetInertia(0)
    physicsXImpulse(-10000)
    physicsYImpulse(36000)
    EndYPhysicsImpulse()
    ForcedLandingRecovery(11, 1)
    sprite('jn402_03', 3)
    sprite('jn402_04', 3)
    CommonSE('003_swing_grap_0_1')
    PrivateSE('jnse_22')
    sprite('jn402_05', 2)
    sprite('jn402_06', 16)
    setInvincible(0)
    CreateObject('IceCircleA', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceCircleB', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('IceCircleC', -1)
    ObjectUpon(STATE_END, 33)
    sprite('jn402_07', 4)
    sprite('jn402_08', 4)
    sprite('jn020_05', 3)
    sprite('jn020_06', 3)
    sprite('jn020_07', 3)

    def upon_LANDING():
        EndMomentum(1)
    label(0)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    gotoLabel(0)


@State
def UltimateAtemi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        UseSlashHitspark(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        DefeatOpponentBehavior(1)
        IgnoreComboTime(1)
        MoveAttributes(0, 1, 0, 0, 0)
        FreezeCount(60)
        FreezeTime(180)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        PassByArmor(1)
        FatalCounter(1)
        AttackP2(100)
        OnlyHitPlayer(1)
        StarterRating(2)
        SetZLine(0, 50)

        def upon_OPPONENT_HIT():
            AttackOff()
            SetActionMark(1)

        def upon_GUARDPOINT_ACTIVATION():
            clearUponHandler(GUARDPOINT_ACTIVATION)
            NoDamageAction(1)
            sendToLabel(111)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)
        GuardpointBlockUnblockable(0)
        BurstInvincibility(1)
        GuardpointHitstop(5, 73)
    sprite('jn432_00', 1)
    DistortionSettings(36, -1, 0)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_JN', -1)
    Voiceline('jn253')
    CreateObject('jn_DD_2_ex', -1)
    HeatChange(-5000)
    sprite('jn432_01', 40)
    sprite('jn432_02', 9)
    sprite('jn432_03', 4)
    setInvincible(0)
    sprite('jn432_04', 4)
    sprite('jn432_05', 4)
    sprite('jn432_06', 4)
    sprite('jn432_07', 4)
    loopRest()
    ExitState()
    label(111)
    sprite('jn433_00', 4)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('jn433_01', 4)
    sprite('jn433_02', 4)
    sprite('jn433_03', 4)
    sprite('jn433_04', 4)
    sprite('jn433_05', 4)
    sprite('jn433_06', 4)
    sprite('jn433_07', 4)
    sprite('jn433_08', 4)
    sprite('jn433_09', 4)
    sprite('jn433_10', 4)
    sprite('jn433_11', 4)
    sprite('jn433_12', 4)
    sprite('jn433_13', 4)
    sprite('jn433_14', 3)
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_DD', 0)
    ScreenShake(0, 16000)
    AddX(1696000)
    sprite('jn433_15', 3)
    sprite('jn433_16', 3)
    sprite('jn433_15', 3)
    sprite('jn433_16', 3)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(444)
    sprite('jn433_17', 4)
    sprite('jn433_18', 4)
    sprite('jn433_19', 4)
    sprite('jn433_20', 4)
    sprite('jn433_21', 4)
    sprite('jn433_22', 4)
    sprite('jn433_23', 4)
    sprite('jn433_24', 4)
    sprite('jn433_25', 4)
    sprite('jn433_26', 4)
    sprite('jn433_27', 4)
    sprite('jn433_28', 4)
    sprite('jn433_30', 4)
    sprite('jn433_31', 4)
    sprite('jn433_32', 4)
    sprite('jn433_33', 4)
    sprite('jn433_34', 4)
    sprite('jn433_35', 4)
    sprite('jn433_36', 4)
    sprite('jn000_00', 1)
    Flip()
    loopRest()
    ExitState()
    label(444)
    sprite('jn433_17', 4)
    sprite('jn433_18', 4)
    sprite('jn433_19', 4)
    sprite('jn433_20', 4)
    Voiceline('jn254')
    sprite('jn433_21', 4)
    sprite('jn433_22', 4)
    sprite('jn433_23', 4)
    sprite('jn433_24', 4)
    sprite('jn433_25', 4)
    sprite('jn433_26', 4)
    sprite('jn433_27', 30)
    sprite('jn433_28', 40)
    CreateObject('EffNoutou', 0)
    sprite('jn433_29', 5)
    ScreenShake(26000, 0)
    CreateObject('Yukikazedmy', -1)
    sprite('jn433_30', 5)
    sprite('jn433_31', 5)
    sprite('jn433_32', 5)
    sprite('jn433_33', 5)
    sprite('jn433_28', 34)
    sprite('jn433_34', 5)
    sprite('jn433_35', 5)
    sprite('jn433_36', 5)
    sprite('jn000_00', 1)
    Flip()
    loopRest()
    ExitState()


@State
def UltimateAtemi_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        UseSlashHitspark(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        DefeatOpponentBehavior(1)
        IgnoreComboTime(1)
        MoveAttributes(0, 1, 0, 0, 0)
        FreezeCount(60)
        FreezeTime(180)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        PassByArmor(1)
        FatalCounter(1)
        AttackP2(100)
        OnlyHitPlayer(1)
        Hitstop(1)
        AttackType(4)
        StarterRating(2)
        SetZLine(0, 50)

        def upon_OPPONENT_HIT():
            EndAttack()
            SetActionMark(1)

        def upon_GUARDPOINT_ACTIVATION():
            clearUponHandler(GUARDPOINT_ACTIVATION)
            NoDamageAction(1)
            sendToLabel(111)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)
        GuardpointBlockUnblockable(0)
        BurstInvincibility(1)
        GuardpointHitstop(5, 73)
    sprite('jn432_00', 1)
    DistortionSettings(36, -1, 0)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_JN', -1)
    Voiceline('jn253')
    CreateObject('jn_DD_2_ex', -1)
    HeatChange(-5000)
    sprite('jn432_01', 40)
    sprite('jn432_02', 9)
    sprite('jn432_03', 4)
    setInvincible(0)
    sprite('jn432_04', 4)
    sprite('jn432_05', 4)
    sprite('jn432_06', 4)
    sprite('jn432_07', 4)
    loopRest()
    ExitState()
    label(111)
    sprite('jn433_00', 4)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('jn433_01', 4)
    sprite('jn433_02', 4)
    sprite('jn433_03', 4)
    sprite('jn433_04', 4)
    sprite('jn433_05', 4)
    sprite('jn433_06', 4)
    sprite('jn433_07', 4)
    sprite('jn433_08', 4)
    sprite('jn433_09', 4)
    sprite('jn433_10', 4)
    sprite('jn433_11', 4)
    sprite('jn433_12', 4)
    sprite('jn433_13', 4)
    sprite('jn433_14', 3)
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_DD', 0)
    ScreenShake(0, 16000)
    AddX(1696000)
    sprite('jn433_15', 3)
    RefreshMultihit()
    sprite('jn433_16', 3)
    RefreshMultihit()
    sprite('jn433_15', 3)
    RefreshMultihit()
    sprite('jn433_16', 3)
    RefreshMultihit()
    loopRest()
    if SLOT_2:
        enterState('UltimateAtemiAddAttack')
    sprite('jn433_17', 4)
    sprite('jn433_18', 4)
    sprite('jn433_19', 4)
    sprite('jn433_20', 4)
    sprite('jn433_21', 4)
    sprite('jn433_22', 4)
    sprite('jn433_23', 4)
    sprite('jn433_24', 4)
    sprite('jn433_25', 4)
    sprite('jn433_26', 4)
    sprite('jn433_27', 4)
    sprite('jn433_28', 4)
    sprite('jn433_30', 4)
    sprite('jn433_31', 4)
    sprite('jn433_32', 4)
    sprite('jn433_33', 4)
    sprite('jn433_34', 4)
    sprite('jn433_35', 4)
    sprite('jn433_36', 4)
    sprite('jn000_00', 1)
    Flip()


@State
def UltimateAtemiAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackType(4)
        NoAttackDuringAction(0)
        DefeatOpponentBehavior(1)
        Hitstop(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackY(-10000)
        FreezeCount(20)
        FreezeTime(100)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        setInvincible(1)
        SetBackground(2)
    sprite('jn433_01', 4)
    ForceFaceSprite()
    CallPrivateFunction('jn_drive_flash', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn433_02', 4)
    sprite('jn433_03', 4)
    sprite('jn433_04', 4)
    sprite('jn433_05', 4)
    sprite('jn433_07', 1)
    sprite('jn433_09', 1)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('jn433_14', 3)
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    TeleportToObject(22)
    AddX(500000)
    AbsoluteY(0)
    SetXCollisionFromOrigin(20)
    CreateObject('AstralStartPtc', -1)
    sprite('jn433_15', 3)
    SetXCollisionFromOrigin(-1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('jn433_16', 3)
    loopRest()
    sprite('jn433_01', 1)
    ForceFaceSprite()
    sprite('jn433_02', 1)
    sprite('jn433_03', 1)
    sprite('jn433_04', 1)
    sprite('jn433_05', 1)
    sprite('jn433_07', 1)
    sprite('jn433_09', 1)
    sprite('jn433_14', 2)
    RefreshMultihit()
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    TeleportToObject(22)
    AddX(400000)
    AbsoluteY(0)
    SetXCollisionFromOrigin(20)
    sprite('jn433_15', 1)
    SetXCollisionFromOrigin(-1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('jn433_16', 1)
    loopRest()
    sprite('jn433_01', 1)
    ForceFaceSprite()
    sprite('jn433_02', 1)
    sprite('jn433_03', 1)
    sprite('jn433_04', 1)
    sprite('jn433_05', 1)
    sprite('jn433_07', 1)
    sprite('jn433_09', 1)
    sprite('jn433_14', 1)
    RefreshMultihit()
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    TeleportToObject(22)
    AddX(300000)
    AbsoluteY(0)
    SetXCollisionFromOrigin(20)
    sprite('jn433_15', 1)
    SetXCollisionFromOrigin(-1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('jn433_16', 1)
    loopRest()
    sprite('jn433_01', 1)
    ForceFaceSprite()
    sprite('jn433_02', 1)
    sprite('jn433_03', 1)
    sprite('jn433_04', 1)
    sprite('jn433_05', 1)
    sprite('jn433_07', 1)
    sprite('jn433_09', 1)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('jn433_14', 3)
    RefreshMultihit()
    Visibility(1)
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    CreateParticle('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    TeleportToObject(22)
    AddX(275000)
    AbsoluteY(0)
    SetXCollisionFromOrigin(20)
    sprite('jn414_09', 1)
    Flip()
    Visibility(0)
    SetInertia(-10000)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('jn414_09', 2)
    StartMultihit()
    sprite('jn414_10', 20)
    sprite('jn414_10', 20)
    Voiceline('jn254')
    sprite('jn414_11', 6)
    CreateObject('EffNoutou', 0)
    sprite('jn414_12', 70)
    ScreenShake(40000, 40000)
    CreateObject('YukikazedmyOD', -1)
    sprite('jn414_13', 5)
    sprite('jn414_14', 5)
    ExitState()


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(58000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 350000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            SetXCollisionFromOrigin(550)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('jn202_00ex01', 4)
    E0EAEffect('BurstDDeff', 103)
    sprite('jn202_01ex01', 7)
    sprite('jn410_13ex01', 4)
    Voiceline('jn280')
    CommonSE('006_swing_blade_1')
    CommonSE('009_swing_rapier_2')
    sprite('jn410_14ex01', 4)
    sprite('jn410_15ex02', 3)
    sprite('jn410_15ex02', 2)
    AttackOff()
    setInvincible(0)
    sprite('jn410_16ex01', 5)
    sprite('jn410_17ex01', 5)
    sprite('jn410_18ex01', 5)
    sprite('jn410_19ex01', 12)
    CreateObject('EffNoutou', 0)
    sprite('jn410_20ex01', 5)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(58000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 350000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            SetXCollisionFromOrigin(550)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('jn202_00ex01', 3)
    E0EAEffect('BurstDDeff', 103)
    sprite('jn202_01ex01', 2)
    Voiceline('jn280')
    sprite('jn410_13ex01', 2)
    CommonSE('006_swing_blade_1')
    CommonSE('009_swing_rapier_2')
    sprite('jn410_14ex01', 2)
    sprite('jn410_15ex02', 3)
    sprite('jn410_15ex02', 2)
    AttackOff()
    setInvincible(0)
    sprite('jn410_16ex01', 5)
    sprite('jn410_17ex01', 5)
    sprite('jn410_18ex01', 5)
    sprite('jn410_19ex01', 12)
    CreateObject('EffNoutou', 0)
    sprite('jn410_20ex01', 5)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(300)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(0)
        HardKnockdown(1)
        Hitstop(0)
        AirUntechableTime(200)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        if SLOT_51:
            Damage(400)
            SetActionMark(1)
        CreateObject('BurstDD_Camera', -1)
        SetBackground(1)
        clearUponHandler(LANDING)

        def upon_LANDING():
            DespawnEAEffect('BurstDD_Camera')
            sendToLabel(100)
    sprite('jn410_15ex02', 3)
    StartMultihit()
    sprite('jn410_16ex01', 3)
    sprite('jn410_17ex01', 3)
    sprite('jn410_18ex01', 3)
    sprite('jn410_19ex01', 6)
    CreateObject('EffNoutou', 0)
    sprite('jn410_20ex01', 3)
    sprite('jn330_03ex01', 4)
    CommonSE('009_swing_rapier_1')
    sprite('jn330_04ex01', 4)
    sprite('jn330_05ex01', 4)
    sprite('jn330_06ex01', 2)
    TriggerUponForState('BurstDD_Camera', 32)
    sprite('jn330_06ex01', 2)
    sprite('jn330_06ex01', 2)
    sprite('jn330_06ex01', 2)
    sprite('jn330_07ex01', 2)
    sprite('jn330_08ex01', 4)
    StartMultihit()
    CreateObject('BurstDD_IceNew', -1)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_1')
    PrivateSE('jnse_22')
    sprite('jn330_09ex01', 4)
    sprite('jn330_10ex01', 4)
    sprite('jn330_11ex01', 8)
    sprite('jn330_12ex01', 3)
    sprite('jn330_13ex01', 3)
    sprite('jn330_14ex01', 3)
    sprite('jn330_15ex01', 3)
    CreateObject('BurstDD_Sword', 0)
    sprite('jn330_16ex01', 3)
    sprite('jn440_00', 3)
    sprite('jn440_01', 3)
    sprite('jn440_02', 2)
    physicsYImpulse(36000)
    JumpEffects(0, 0)
    sprite('jn440_03', 2)
    TriggerUponForState('BurstDD_Camera', 33)
    sprite('jn440_02', 2)
    sprite('jn440_03', 2)
    sprite('jn440_02', 2)
    sprite('jn440_03', 2)
    sprite('jn440_02', 2)
    sprite('jn440_03', 2)
    sprite('jn440_04', 2)
    loopRest()
    sprite('jn408_14ex01', 2)
    DespawnEAEffect('BurstDD_Sword')
    physicsYImpulse(-1000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    UseSlashHitspark(1)
    Hitstop(8)
    YAccel(-100)
    sprite('jn413_06ex01', 2)
    CommonSE('006_swing_blade_0')
    if SLOT_51:
        Voiceline('jn281')
    elif SLOT_43:
        Voiceline('jn281')
    else:
        Voiceline('jn282')
    sprite('jn413_07ex01', 2)
    RefreshMultihit()
    sprite('jn413_08ex01', 2)
    sprite('jn412_01ex01', 2)
    sprite('jn412_02ex01', 2)
    CommonSE('006_swing_blade_0')
    sprite('jn412_03ex01', 2)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    sprite('jn412_04ex01', 2)
    sprite('jn252_02ex01', 2)
    sprite('jn252_03ex01', 2)
    CommonSE('006_swing_blade_0')
    sprite('jn252_04ex01', 2)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    sprite('jn252_05ex01', 2)
    if not SLOT_51:
        notConditionalSendToLabel(9)
    label(0)
    Hitstop(2)
    sprite('null', 2)
    YAccel(-100)
    sprite('jn413_06ex01', 1)
    CommonSE('006_swing_blade_0')
    sprite('jn413_07ex01', 1)
    RefreshMultihit()
    sprite('jn413_08ex01', 1)
    sprite('null', 2)
    sprite('jn412_02ex01', 1)
    CommonSE('006_swing_blade_0')
    sprite('jn412_03ex01', 1)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    sprite('jn412_04ex01', 1)
    sprite('null', 2)
    sprite('jn252_03ex01', 1)
    CommonSE('006_swing_blade_0')
    sprite('jn252_04ex01', 1)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    sprite('jn252_05ex01', 1)
    if SLOT_2:
        sendToLabel(0)
        AddActionMark(-1)
    loopRest()
    label(9)
    sprite('jn408_14ex01', 6)
    physicsYImpulse(6000)
    setGravity(1000)
    sprite('jn408_15ex01', 6)
    sprite('jn408_16ex01', 2)
    StartMultihit()
    if SLOT_51:
        Voiceline('jn282')
    CommonSE('006_swing_blade_2')
    sprite('jn408_16ex01', 3)
    RefreshMultihit()
    Damage(1250)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-100000)
    Hitstop(30)
    DefeatOpponentBehavior(0)
    TriggerUponForState('BurstDD_IceNew', 32)
    if SLOT_51:
        CreateObject('BurstDD_SlashEX', -1)
    else:
        CreateObject('BurstDD_Slash', -1)
    sprite('jn408_17ex01', 4)
    TriggerUponForState('BurstDD_Camera', 34)
    sprite('jn408_18ex01', 4)
    sprite('jn408_19ex01', 4)
    sprite('jn020_06', 3)
    EndYPhysicsImpulse()
    sprite('jn020_07', 3)
    label(99)
    sprite('jn020_08', 3)
    sprite('jn020_09', 3)
    loopRest()
    gotoLabel(99)
    label(100)
    sprite('jn020_10', 3)
    sprite('jn020_11', 3)
    sprite('jn020_12', 3)


@State
def astral():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Hitstop(0)
        PushbackX(0)
        AirUntechableTime(200)
        Damage(0)
        MinimumDamage(100)
        AirPushbackX(0)
        AirPushbackY(-100000)
        PassByArmor(1)
        FreezeCount(360)
        FreezeTime(380)
        HitLow(2)
        ProjectileLevel(3)
        MoveAttributes(0, 0, 1, 0, 0)
        StayAfterMovement(1, 0)
        EnterStateIfEventID(12, 'astral2')
        setInvincible(1)
    sprite('jn450_00', 5)
    sprite('jn450_01', 5)
    DistortionSettings(60, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_JN_AH', -1)
    Voiceline('jn290')
    sprite('jn450_02', 5)
    sprite('jn450_03', 5)
    sprite('jn450_04', 5)
    sprite('jn450_05', 5)
    sprite('jn450_06', 5)
    sprite('jn450_07', 5)
    sprite('jn450_08', 5)
    sprite('jn450_09', 5)
    sprite('jn450_10', 5)
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    sprite('jn450_11', 5)
    sprite('jn450_12', 5)
    sprite('jn450_13', 5)
    sprite('jn450_14', 5)
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    sprite('jn450_15', 5)
    sprite('jn450_16', 5)
    sprite('jn450_17', 5)
    sprite('jn450_18', 10)
    CreateObject('JNEF_ast_attack', 0)
    PrivateSE('jnse_22')
    setInvincible(0)
    sprite('jn450_19', 5)
    sprite('jn450_20', 5)
    sprite('jn450_21', 5)
    sprite('jn450_22', 5)
    sprite('jn450_23', 5)
    sprite('jn450_24', 5)
    sprite('jn450_25', 5)
    sprite('jn450_26', 5)
    sprite('jn450_27', 5)
    sprite('jn450_28', 5)
    NoAttackDuringAction(1)
    sprite('jn450_29', 5)
    CreateObject('EffNoutou', 0)
    SetBackground(0)
    sprite('jn450_30', 5)
    sprite('jn450_31', 5)
    sprite('jn450_32', 5)
    sprite('jn450_33', 5)
    sprite('jn450_34', 5)
    sprite('jn450_35', 5)
    sprite('jn450_36', 5)
    sprite('jn450_37', 5)


@State
def astral2():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        StayAfterMovement(1, 0)
        SetBackground(3)
        setInvincible(1)
        HUDVisibillity(1)
        NoAttackDuringAction(1)
        AstralHeatCleanup(1, 1)
        PlayPlayAstralBGM(1)
        CreateObject('LookAtMe', -1)
        RegisterObject(8, 1)
        KeepBackground(1)
        DisableOppPushCollision(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
    sprite('jn450_19', 3)
    CreateObject('AstralStartPtc', -1)
    CreateObject('ef_jnah_A', 101)
    CreateObject('ef_jnah_B', 101)
    CreateParticle('jnef_ast_icewind', 101)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_19', 3)
    sprite('jn450_20', 3)
    sprite('jn450_21', 3)
    sprite('jn450_22', 5)
    sprite('jn450_23', 5)
    sprite('jn450_24', 5)
    sprite('jn450_25', 5)
    sprite('jn450_26', 5)
    Voiceline('jn291')
    sprite('jn450_27', 5)
    sprite('jn450_28', 5)
    CreateObject('AstralFinishPtc', -1)
    CreateObject('EffNoutou', 0)
    sprite('jn450_29', 5)
    NoAttackDuringAction(0)
    HitAnywhere(1)
    DefeatOpponentBehavior(3)
    UseSlashHitspark(1)
    MinimumDamage(100)
    Damage(27315)
    Hitstop(0)
    RefreshMultihit()
    CommonSE('018_ice_break_1')
    SetBackground(2)
    sprite('jn450_29add01', 7)
    sprite('jn450_29add02', 7)
    sprite('jn450_29add03', 7)
    sprite('jn450_29add04', 70)
    sprite('jn450_29add04', 70)
    CameraControlEnable(1)
    CameraWinnerControlStop(1)
    DeleteObject(8)
    sprite('jn450_30', 7)
    sprite('jn450_31', 7)
    sprite('jn450_32', 7)
    sprite('jn450_33', 7)
    sprite('jn450_34', 7)
    sprite('jn450_35', 7)
    EndAttack()
    sprite('jn450_36', 7)
    sprite('jn450_37', 7)
    sprite('jn000_00', 7)
    AddX(128000)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    WinAction()
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn407')
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 150)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    EndDemo()
    loopRest()
    ExitState()


@State
def NanDato():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('jn430_26', 3)
    sprite('jn430_25', 4)
    sprite('jn430_24', 10)
    sprite('jn430_23', 1)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 1)
    sprite('jn430_23', 1)
    sprite('jn430_24', 10)
    CommonSE('014_electric_m')
    ScreenShake(12000, 0)
    sprite('jn430_24', 30)
    Voiceline('jn039')
    sprite('jn430_25', 5)
    sprite('jn430_26', 4)


@State
def StoryYowai5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(100)
        AttackP2(80)
        AirPushbackY(10000)
        AirPushbackX(24000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        HitOrBlockCancel('ShortDash')
        SpecialCancel(0)
        AttackOff()
    sprite('jn203_00', 2)
    XImpulseAcceleration(25)
    sprite('jn203_01', 2)
    RandomCommonVoiceline(1)
    sprite('jn203_02', 2)
    sprite('jn203_03', 2)
    AddInertia(8333)
    sprite('jn203_04', 2)
    sprite('jn203_05', 1)
    sprite('jn203_06', 1)
    sprite('jn203_07ex01', 4)
    RefreshMultihit()
    ScreenShake(0, 5000)
    sprite('jn203_08', 8)
    AttackOff()
    sprite('jn203_09', 4)
    sprite('jn203_10', 4)
    sprite('jn203_11', 4)
    sprite('jn203_12', 4)
    sprite('jn203_13', 4)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('jn054')
    sprite('jn900_00', 32767)
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
        AbsoluteY(200000)
    sprite('jn901_00', 50)
    physicsYImpulse(-150)
    sprite('jn901_00', 50)
    physicsYImpulse(150)
    Voiceline('jn055')
    label(0)
    sprite('jn901_00', 50)
    physicsYImpulse(-150)
    sprite('jn901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('jn000', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('jn055', 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn400', 12641, 25392, 12337, 12641, 25392, 12337, 12641, 
        25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn401', 12641, 25392, 12337, 12641, 25392, 12337, 14433, 
        14435, 12641, 25392, 12337, 12641, 25392, 12337, 12897, 25392, 
        12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('jn404', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn405', 12641, 25392, 12341, 14433, 14435, 14433, 14435, 
        14433, 14435, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn406', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 24880, 25400, 24888, 25400, 24888, 25400, 
        24888, 12337, 12643, 24880, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn407', 13411, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12849, 13923, 24880, 12337, 12643, 24880, 25400, 24888, 
        25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('jn408', 14435, 24888, 25400, 24888, 12337, 12643, 24882, 
        25400, 24888, 12337, 12643, 24880, 25400, 24888, 12337, 12643, 48, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn412', 14433, 14435, 14433, 14435, 14433, 14435, 13921, 
        13923, 13921, 13923, 14433, 14435, 13921, 13923, 13921, 13923, 
        13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('jn413', 12641, 25392, 12337, 12641, 25392, 12337, 13921, 
        13923, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn414', 12641, 25392, 24888, 25400, 24888, 25400, 24888, 
        25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn415', 12641, 25392, 12337, 12641, 25392, 12337, 12641, 
        25392, 12337, 12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn416', 12641, 25392, 12337, 12641, 25392, 12337, 12641, 
        25392, 12337, 12641, 25392, 12337, 12641, 25392, 12337, 12641, 
        25392, 12337, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jn417', 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('jn000', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn400', 12641, 25392, 12337, 12641, 25392, 12337, 
            13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn401', 14433, 14435, 14433, 14435, 12641, 25392, 
            12337, 14433, 14435, 12641, 25392, 12337, 12641, 25392, 12337, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
            14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn405', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn406', 12641, 25392, 12337, 12641, 25392, 12337, 
            12641, 25392, 12337, 12641, 25392, 12337, 14433, 14435, 12641, 
            25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn407', 12641, 25392, 12337, 12641, 25392, 12337, 
            14433, 14435, 14433, 14435, 12641, 25394, 12337, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('jn408', 14691, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 24880, 25400, 24888, 12849, 14435, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn412', 14433, 14435, 14433, 14435, 12641, 25392, 
            12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn413', 12641, 25392, 12337, 12641, 25392, 12337, 
            12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jn414', 12641, 25392, 12337, 12641, 25392, 12337, 
            14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn415', 12641, 25392, 12337, 12641, 25392, 12337, 
            12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jn416', 12641, 25392, 12337, 12641, 25392, 12337, 
            12641, 25392, 12337, 12641, 25392, 13617, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jn417', 14433, 14435, 14433, 14435, 12641, 25392, 
            12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            if CharacterIDCheck('rg'):
                Unknown18011('jn000', 13923, 14177, 14179, 14177, 14179, 
                    14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('jn000', 13923, 14177, 14179, 14177, 14179, 
                    14177, 14179, 14177, 14691, 24880, 25399, 24887, 25399,
                    55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn400', 14177, 13411, 14177, 14179, 14177, 
                    14179, 12641, 25397, 12340, 14177, 14179, 14177, 14179,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn401', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('jn000', 13923, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('jn400', 13923, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn401', 14179, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('jn000', 13923, 14177, 14179, 14177, 14179, 14177,
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn400', 13923, 14177, 14179, 14177, 13923, 24880,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn401', 14179, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 12641, 25396, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('jn000', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn400', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('iz'):
            Unknown18011('jn000', 13923, 13921, 13923, 13921, 13923, 13921,
                13411, 24885, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn400', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 24880, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('jn401', 13921, 13923, 13921, 13923, 13921, 14179,
                24885, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25400, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('jn000', 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn401', 14177, 14179, 14177, 14435, 24885, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            if SLOT_138:
                Unknown18011('jn500', 12643, 12337, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641,
                    25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn501', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('jn500', 14433, 14435, 14433, 14435, 14433, 
                    12643, 12336, 14433, 14179, 14433, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn501', 14177, 14179, 14177, 13923, 13921, 
                    13923, 13921, 14691, 24880, 13617, 14179, 14177, 14179,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('jn504', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn505', 12641, 25392, 12337, 12641, 25392, 12343,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('jn504', 14433, 13667, 14433, 13667, 14433, 
                    14435, 14433, 13667, 14433, 13667, 12641, 25392, 12339,
                    12641, 25398, 24885, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn505', 14433, 14435, 13153, 25392, 12341, 
                    12641, 25392, 24886, 25400, 24885, 25397, 24885, 12337,
                    14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('jn506', 12641, 25394, 24887, 12849, 14179, 12641,
                25392, 24887, 12337, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('jn507', 14177, 14179, 14177, 14179, 14177, 13923,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('jn521', 14177, 14179, 14177, 14435, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('jn524', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13411, 24885, 25398, 24886, 25398, 12593, 24880, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn525', 13923, 14177, 14179, 14177, 14179, 13921,
                14179, 24880, 25400, 24885, 25400, 24885, 25400, 24885, 
                25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('jn524', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13411, 24885,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn525', 14177, 14179, 13153, 25392, 12340, 
                    14433, 13667, 14433, 13667, 13665, 13667, 13665, 13667,
                    14177, 14179, 14433, 13667, 14433, 13667, 12897, 25392,
                    53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mu'):
            if SLOT_140:
                Unknown18011('jn528', 14177, 14179, 12641, 25396, 24887, 
                    25399, 24887, 25398, 24886, 25398, 24886, 25399, 24887,
                    13361, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('jn529', 13155, 24880, 12337, 13667, 24886, 
                    25400, 24885, 25400, 24885, 25400, 24885, 25400, 24885,
                    25400, 24885, 25400, 24885, 13361, 13667, 14433, 13667,
                    12897, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('pt'):
            Unknown18011('jn535', 12643, 12338, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('iz'):
            Unknown18011('jn538', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13923, 24880, 25398, 24884, 25398, 
                24884, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn539', 14177, 14179, 14177, 12643, 12338, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('jn546', 12641, 25392, 24887, 12337, 13923, 12641,
                25392, 24886, 12337, 13923, 12641, 25392, 24886, 12337, 
                13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn547', 13921, 13923, 13921, 13923, 14177, 14179,
                13921, 13923, 13665, 13667, 14177, 12643, 12336, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            if SLOT_140:
                Unknown18011('jn546', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 12641, 25392, 13620,
                    13921, 13411, 13921, 13411, 13921, 13923, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown18011('jn547', 14433, 13667, 13923, 14433, 13667, 
                    14433, 13667, 14433, 13667, 14433, 13667, 14433, 13667,
                    14433, 13667, 12641, 25396, 12341, 14433, 13667, 14433,
                    13667, 13665, 13667, 12897, 25392, 53, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('jn550', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 14435, 24880, 25398, 24886, 25398, 12593, 24880, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn551', 14177, 14179, 14177, 13923, 24880, 25400,
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('jn552', 13923, 24880, 25399, 24887, 25398, 24886,
                25398, 12849, 24880, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn553', 12641, 25392, 24887, 12337, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 14691, 24880, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('nt'):
            Unknown18011('jn560', 14177, 14179, 13921, 13923, 13921, 14691,
                24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn561', 14177, 14691, 24880, 12337, 13923, 12641,
                25392, 24886, 12337, 13923, 12641, 25392, 24886, 12337, 
                13923, 12641, 25392, 24886, 12337, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('jn558', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn559', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 24880, 25400, 
                24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('jn562', 14177, 14179, 14177, 14179, 14177, 14435,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn563', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 24882, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('jn564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn565', 14177, 14179, 14177, 14179, 14177, 13923,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ma'):
            Unknown18011('jn568', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                24880, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn569', 13921, 13923, 13921, 13923, 13921, 14179,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 12337, 24880, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('jn570', 14177, 14179, 14177, 14179, 14177, 14435,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jn571', 12643, 12336, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jb'):
        SyncEntry()
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('jb'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('rc'):
        SyncEntry()
        gotoLabel(130)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('tb'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2220)
        else:
            gotoLabel(220)
    if CharacterIDCheck('mu'):
        if SLOT_140:
            conditionalSendToLabel(2240)
    if CharacterIDCheck('pt'):
        SyncEntry()
        gotoLabel(270)
    if CharacterIDCheck('iz'):
        SyncEntry()
        gotoLabel(290)
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
        gotoLabel(360)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('nt'):
        SyncEntry()
        gotoLabel(400)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(410)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    if CharacterIDCheck('ma'):
        SyncEntry()
        gotoLabel(430)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    if CharacterIDCheck('hz'):
        gotoLabel(3)
    if CharacterIDCheck('vh'):
        gotoLabel(3)
    label(482)
    if random_(2, 0, 20):
        conditionalSendToLabel(3)
    if random_(2, 0, 50):
        conditionalSendToLabel(2)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    label(0)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('jn600_00', 6)
    Voiceline('jn412')
    CreateObject('jnef600iceSword', -1)
    RegisterObject(4, 1)
    label(12)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_4():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    Voiceline('jn413')
    DemoTimer(80)
    loopRest()
    ExitState()
    label(1)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('jn600_00', 6)
    Voiceline('jn414')
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    Voiceline('jn415')
    DemoTimer(120)
    loopRest()
    ExitState()
    label(2)
    sprite('jn601_00', 3)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    if SLOT_43:
        Voiceline('jn416')
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 125)
    if SLOT_44:
        Voiceline('jn416')
    sprite('jn601_12', 30)
    if SLOT_44:
        Voiceline('jn417')
    sprite('jn601_12', 30)
    if SLOT_43:
        Voiceline('jn417')
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(3)
    sprite('jn601_00', 3)
    CreateObject('ptPhantom_NoSound', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(-500)
    label(4)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(4)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    if SLOT_43:
        Voiceline('jn416')
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 125)
    if SLOT_44:
        Voiceline('jn416')
    sprite('jn601_12', 30)
    if SLOT_44:
        Voiceline('jn417')
    sprite('jn601_12', 30)
    if SLOT_43:
        Voiceline('jn417')
    sprite('jn601_13', 6)
    ObjectUpon(FALLING, 32)
    sprite('jn601_14', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(100)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(100)
    uponSendToLabel(32, 102)
    label(101)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    Voiceline('jn500')
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(1100)
    sprite('null', 1)
    XPositionRelativeFacing(-1000000)
    ScreenCollision(0)
    EnableCollision(0)
    uponSendToLabel(32, 1102)
    loopRest()
    label(1101)
    sprite('null', 32767)
    loopRest()
    label(1102)
    sprite('null', 10)
    AttackDefaults_StandingSpecial()
    StayAfterMovement(1, 0)
    SetXCollisionFromOrigin(120)
    sprite('jn032_00', 2)
    physicsXImpulse(40000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 2)
    label(0)
    sprite('jn032_11', 3)
    sprite('jn032_12', 3)
    DashEffects(100, 1, 1)
    sprite('jn212_00', 1)
    EndMomentum(1)
    sprite('jn212_01', 1)
    physicsXImpulse(10000)
    sprite('jn212_02', 1)
    sprite('jn212_03', 2)
    sprite('jn212_04', 2)
    DashEffects(100, 1, 1)
    sprite('jn212_05', 2)
    sprite('jn212_06', 2)
    XImpulseAcceleration(50)
    sprite('jn212_07', 3)
    EndMomentum(1)
    CreateObject('zan_a0', -1)
    CommonSE('009_swing_rapier_2')
    sprite('jn212_08', 3)
    sprite('jn212_09', 3)
    sprite('jn212_10', 2)
    sprite('jn212_11', 2)
    sprite('jn212_12', 2)
    sprite('jn212_13', 2)
    AddX(-40000)
    sprite('jn212_14', 2)
    AddX(-50000)

    def upon_OPPONENT_HIT_OR_BLOCK():
        ScreenShake(30000, 30000)
        AddInertia(-2000)
    sprite('jn407_00', 3)
    XPositionRelativeFacing(-260000)
    PrivateSE('jnse_22')
    sprite('jn407_01', 3)
    sprite('jn407_02', 3)
    sprite('jn407_03', 3)
    sprite('jn407_04', 3)
    RefreshMultihit()
    PrivateSE('jnse_21')
    CreateObject('zan407', 0)
    CommonSE('009_swing_rapier_0')
    sprite('jn407_05', 3)
    sprite('jn407_06', 2)
    sprite('jn407_07', 2)
    sprite('jn407_08', 3)
    sprite('jn407_09', 2)
    sprite('jn407_10', 2)
    DashEffects(100, 1, 1)
    sprite('jn407_11', 2)
    PrivateSE('jnse_21')
    CreateObject('EFF28AtkD', 0)
    sprite('jn407_12', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    sprite('jn407_13', 3)
    sprite('jn407_14', 3)
    sprite('jn407_15', 3)
    sprite('jn407_16', 3)
    sprite('jn407_17', 3)
    sprite('jn407_18', 3)
    sprite('jn407_19', 3)
    sprite('jn407_20', 3)
    sprite('jn407_21', 5)
    sprite('jn407_22', 4)
    AddX(60000)
    sprite('jn407_23', 3)
    sprite('jn407_24', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn410_01', 1)
    sprite('jn410_02', 1)
    sprite('jn410_03ex01', 1)
    RefreshMultihit()
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)

    def upon_OPPONENT_HIT_OR_BLOCK():
        ScreenShake(30000, 30000)
        AddInertia(-1000)
    sprite('jn410_04', 1)
    sprite('jn410_06', 1)
    LandingEffects(100, 1, 1)
    sprite('jn410_07ex01', 1)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    RefreshMultihit()
    sprite('jn410_08', 1)
    sprite('jn410_10', 1)
    LandingEffects(100, 1, 1)
    sprite('jn410_11ex01', 1)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    RefreshMultihit()
    sprite('jn410_12', 1)
    sprite('jn410_14', 1)
    LandingEffects(100, 1, 1)
    sprite('jn410_15ex01', 1)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    CreateObject('EventIceMakePtc', 0)
    RefreshMultihit()
    CommonSE('009_swing_rapier_0')
    sprite('jn410_16', 2)
    sprite('jn410_17', 2)
    sprite('jn410_18', 4)
    sprite('jn410_19', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn410_19', 30)
    sprite('jn410_20', 6)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    Voiceline('jn500')
    DemoEndOnVoiceEnd(1)
    sprite('jn300_03', 6)
    sprite('jn300_04', 200)
    sprite('jn300_03', 8)
    sprite('jn300_02', 6)
    sprite('jn300_01', 6)
    sprite('jn300_00', 6)
    loopRest()
    ExitState()
    label(120)
    uponSendToLabel(32, 122)
    label(121)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(121)
    label(122)
    clearUponHandler(32)
    sprite('jn600_00', 6)
    Voiceline('jn504')
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    loopRest()
    ExitState()
    label(2120)

    def upon_EVERY_FRAME():
        if not SLOT_17:
            AddActionMark(1)
        if SLOT_2 >= 20:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2122)
    label(2121)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(2121)
    label(2122)
    sprite('jn430_26', 4)
    sprite('jn430_25', 4)
    sprite('jn430_24', 5)
    sprite('jn430_23', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn430_23', 180)
    Voiceline('jn504')
    sprite('jn430_23', 5)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(130)
    uponSendToLabel(32, 132)
    label(131)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('jn600_00', 6)
    Voiceline('jn506')
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    clearUponHandler(32)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    loopRest()
    ExitState()
    label(200)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(200)
    sprite('jn601_00', 20)
    CreateObject('ptPhantom', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(500)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 30)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    ObjectUpon(FALLING, 32)
    loopRest()
    uponSendToLabel(32, 202)
    label(201)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('jn430_26', 7)
    sprite('jn430_25', 7)
    Voiceline('jn520')
    DemoTimer(180)
    sprite('jn430_24', 7)
    sprite('jn430_23', 120)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    loopRest()
    ExitState()
    label(220)
    sprite('jn601_00', 3)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(220)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 60)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    uponSendToLabel(32, 222)
    label(221)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(221)
    label(222)
    sprite('jn300_00', 6)
    Voiceline('jn524')
    DemoTimer(400)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 30)
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 8)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    loopRest()
    ExitState()
    label(2220)

    def upon_EVERY_FRAME():
        if not SLOT_17:
            AddActionMark(1)
        if SLOT_2 >= 20:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2221)
    sprite('jn601_00', 32767)
    label(2221)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 120)
    Voiceline('jn524')
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2240)
    sprite('jn300_04', 2)
    uponSendToLabel(32, 2241)
    sprite('jn300_04', 32767)
    label(2241)
    sprite('jn300_04', 80)
    sprite('jn300_04', 8)
    Voiceline('jn528')
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 8)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn430_26', 4)
    sprite('jn430_25', 4)
    sprite('jn430_24', 5)
    sprite('jn430_23', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn430_23', 250)
    sprite('jn430_23', 5)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(270)
    sprite('jn601_00', 3)
    CreateObject('ptPhantom_NoSound', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(-500)
    label(271)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(271)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 125)
    Voiceline('jn534')
    sprite('jn601_12', 30)
    sprite('jn601_12', 30)
    sprite('jn601_13', 6)
    ObjectUpon(22, 32)
    ObjectUpon(FALLING, 32)
    sprite('jn601_14', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(290)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(290)
    uponSendToLabel(32, 292)
    label(291)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(291)
    label(292)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    Voiceline('jn538')
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    DemoTimer(20)
    loopRest()
    ExitState()
    label(330)
    uponSendToLabel(32, 332)
    label(331)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('jn600_00', 6)
    Voiceline('jn546')
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    clearUponHandler(32)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    loopRest()
    ExitState()
    label(2330)
    sprite('null', 1)
    ScreenCollision(0)
    XPositionRelativeFacing(-960000)
    SetZVal(-750)
    AttackDefaults_StandingSpecial()
    uponSendToLabel(32, 2332)

    def upon_STATE_END():
        SetZVal(0)
    label(2331)
    sprite('null', 32767)
    label(2332)
    sprite('jn408_00', 3)
    CreateObject('IceBoard', -1)
    RegisterObject(4, 1)
    sprite('jn408_01', 3)
    physicsXImpulse(-3000)
    physicsYImpulse(4000)
    EndYPhysicsImpulse()
    sprite('jn408_02', 3)
    sprite('jn408_03', 2)
    sprite('jn408_04', 2)
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)
    CommonSE('000_airdash_0')
    physicsXImpulse(32000)
    SetAcceleration(1000)
    ObjectUpon(FALLING, 32)
    sprite('jn408_06ex', 2)
    sprite('jn408_07ex', 2)
    sprite('jn408_06ex', 2)
    sprite('jn408_11', 2)

    def upon_OPPONENT_HIT_OR_BLOCK():
        ScreenShake(3000, 50000)
        CommonSE('105_guard_slash_2')
        XImpulseAcceleration(50)
    uponSendToLabel(LANDING, 2333)
    DeleteObject(4)
    CreateObject('IceBoard_koware', -1)
    physicsXImpulse(16000)
    physicsYImpulse(25000)
    setGravity(2500)
    sprite('jn408_12', 3)
    sprite('jn408_13', 3)
    sprite('jn408_14', 3)
    sprite('jn408_15', 2)
    XImpulseAcceleration(80)
    sprite('jn408_16ex01', 3)
    CreateObject('zan408', 0)
    CommonSE('slash_rapier_middle')
    XImpulseAcceleration(80)
    sprite('jn408_17', 2)
    sprite('jn408_18', 2)
    sprite('jn408_19', 32767)
    label(2333)
    sprite('jn408_20', 4)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    PushCollisionHeightLow(-1)
    sprite('jn408_21', 4)
    sprite('jn408_22', 6)
    sprite('jn408_23', 5)
    sprite('jn408_24', 4)
    sprite('jn408_25', 4)
    sprite('jn408_26', 4)
    CreateObject('EffNoutou', 0)
    sprite('jn408_27', 4)
    sprite('jn408_28', 4)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn300_00', 6)
    Voiceline('jn546')
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 150)
    sprite('jn300_05', 8)
    ObjectUpon(22, 32)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 8)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    loopRest()
    ExitState()
    label(350)
    uponSendToLabel(32, 352)
    label(351)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(351)
    label(352)
    clearUponHandler(32)
    sprite('jn600_00', 6)
    Voiceline('jn550')
    DemoTimer(360)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    CreateObject('ptPhantom', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(500)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    ObjectUpon(FALLING, 32)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    loopRest()
    ExitState()
    label(360)
    sprite('jn601_00', 3)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(360)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    CreateObject('ptPhantom', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(500)
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 240)
    Voiceline('jn552')
    sprite('jn601_12', 30)
    sprite('jn601_12', 30)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    ObjectUpon(22, 32)
    ObjectUpon(FALLING, 32)
    loopRest()
    ExitState()
    label(390)
    sprite('jn601_00', 3)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(390)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    CreateObject('ptPhantom', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-100000)
        SetZVal(500)
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 240)
    Voiceline('jn558')
    sprite('jn601_12', 40)
    ObjectUpon(22, 32)
    ObjectUpon(FALLING, 32)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    loopRest()
    ExitState()
    label(400)
    sprite('jn601_00', 3)
    sprite('jn601_00', 3)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(400)
    sprite('jn601_00', 6)
    CreateObject('jnef601makeSword', 0)
    RegisterObject(6, 1)
    PrivateSE('jnse_22')
    sprite('jn601_01', 6)
    sprite('jn601_02', 6)
    sprite('jn601_03', 6)

    def RunOnObject_6():
        sendToLabel(1)
    sprite('jn601_04', 6)
    sprite('jn601_05', 6)
    sprite('jn601_06', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_07', 6)
    sprite('jn601_08', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    CommonSE('008_swing_pole_1')
    sprite('jn601_11', 6)
    sprite('jn601_12', 200)
    Voiceline('jn560')
    sprite('jn601_12', 40)
    ObjectUpon(22, 32)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    loopRest()
    ExitState()
    label(410)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(410)
    label(411)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    Voiceline('jn562')
    DemoEndOnVoiceEnd(1)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    loopRest()
    ExitState()
    label(420)
    sprite('jn600_00', 1)

    def upon_32():
        SetActionMark(1)
    label(421)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(421)
    label(422)
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(4, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    Voiceline('jn564')
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_4():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(430)
    sprite('jn600_00', 1)

    def upon_32():
        SetActionMark(1)
    label(431)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(431)
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(4, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    Voiceline('jn568')
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_4():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    DemoTimer(170)
    loopRest()
    ExitState()
    label(440)
    sprite('jn600_00', 1)

    def upon_32():
        SetActionMark(1)
    label(441)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(441)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(4, 1)
    Voiceline('jn570')
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_4():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    DemoTimer(170)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 30)
    Voiceline('jn400')
    DemoEndOnVoiceEnd(1)
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 32767)
    loopRest()
    ExitState()
    label(20)
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 30)
    Voiceline('jn401')
    DemoEndOnVoiceEnd(1)
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 8)
    sprite('jn300_08', 32767)
    loopRest()
    ExitState()


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('no'):
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('rc'):
        conditionalSendToLabel(130)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('tb'):
        if SLOT_140:
            gotoLabel(2220)
        else:
            gotoLabel(220)
    if CharacterIDCheck('mu'):
        if SLOT_140:
            conditionalSendToLabel(2240)
    if CharacterIDCheck('pt'):
        conditionalSendToLabel(270)
    if CharacterIDCheck('iz'):
        conditionalSendToLabel(290)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ce'):
        conditionalSendToLabel(360)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('nt'):
        conditionalSendToLabel(400)
    if CharacterIDCheck('mi'):
        if SLOT_138:
            gotoLabel(410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('ma'):
        conditionalSendToLabel(430)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn407')
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    if SLOT_43:
        DemoTimer(120)
    else:
        DemoTimer(10)
    loopRest()
    ExitState()
    label(0)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn408')
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 70)
    sprite('jn611_13', 32767)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(1)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn406')
    sprite('jn610_08', 32767)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(100)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn501')
    sprite('jn610_08', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(1100)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn501')
    sprite('jn610_08', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(120)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn505')
    DemoTimer(300)
    sprite('jn610_08', 32767)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(2120)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    Voiceline('jn505')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(130)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn507')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(200)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn521')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(220)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn525')
    DemoEndOnVoiceEnd(1)
    sprite('jn610_08', 32767)
    loopRest()
    ExitState()
    label(2220)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    Voiceline('jn525')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(2240)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn529')
    DemoEndOnVoiceEnd(1)
    sprite('jn610_08', 32767)
    loopRest()
    ExitState()
    label(270)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn535')
    DemoEndOnVoiceEnd(1)
    sprite('jn610_08', 32767)
    loopRest()
    ExitState()
    label(290)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn539')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(330)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn547')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 70)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(2330)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn547')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(350)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn551')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(360)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 140)
    Voiceline('jn553')
    DemoEndOnVoiceEnd(1)
    sprite('jn610_08', 32767)
    loopRest()
    ExitState()
    label(390)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn559')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(400)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn561')
    DemoTimer(260)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 70)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(410)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn563')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(1410)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn563')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(420)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn565')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    ExitState()
    label(430)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn569')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()
    label(440)
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    Voiceline('jn571')
    DemoEndOnVoiceEnd(1)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()


@State
def CmnActLose():
    sprite('jn620_00', 6)
    Voiceline('jn411')
    sprite('jn620_01', 6)
    sprite('jn620_02', 6)
    sprite('jn620_03', 6)
    sprite('jn620_04', 6)
    sprite('jn620_05', 6)
    sprite('jn620_06', 6)
    sprite('jn620_07', 6)
    sprite('jn620_08', 32767)
    DemoTimer(20)
    loopRest()


@State
def EventDefEntryWait():
    label(0)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
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
    sprite('jn620_08', 32767)


@State
def EventDefLose01():
    sprite('jn620_08', 7)
    sprite('jn064_03', 7)
    sprite('jn064_02', 7)
    sprite('jn064_01', 7)
    sprite('jn064_00', 7)
    sprite('jn063_09', 32767)


@State
def EventEntryRunWait():
    sprite('null', 32767)
    AddX(-700000)
    ScreenCollision(0)


@State
def EventEntryRun():
    sprite('jn032_00', 4)
    ScreenCollision(0)
    DashEffects(100, 1, 1)
    physicsXImpulse(15000)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    XImpulseAcceleration(90)
    sprite('jn032_11', 4)
    sprite('jn032_12', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventChouhatsu():
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 32767)


@State
def EventChouhatsuEnd():
    sprite('jn300_04', 6)
    sprite('jn300_05', 6)
    sprite('jn300_06', 6)
    sprite('jn300_07', 6)
    sprite('jn300_08', 6)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventYoroke():
    sprite('jn070_00', 4)
    sprite('jn070_01', 4)
    sprite('jn070_02', 4)
    sprite('jn070_03', 32767)
    loopRest()


@State
def EventAZYorokeLoop():
    sprite('jn070_03', 32767)


@State
def EventAZYoroke2Down():
    sprite('jn070_03', 2)
    sprite('jn070_08', 6)
    sprite('jn070_09', 6)
    sprite('jn070_10', 6)
    sprite('jn070_11', 6)
    sprite('jn064_03', 6)
    sprite('jn064_02', 6)
    sprite('jn064_01', 6)
    sprite('jn063_09', 32767)
    loopRest()


@State
def EventAZDown():
    sprite('jn061_00', 32767)


@State
def EventAZDownToStand():
    sprite('jn061_00', 6)
    sprite('jn061_01', 6)
    sprite('jn061_02', 6)
    sprite('jn061_03', 6)
    sprite('jn061_04', 6)
    sprite('jn061_05', 6)
    sprite('jn061_06', 6)
    sprite('jn061_07', 6)
    sprite('jn061_08', 6)
    Flip()
    sprite('jn620_00', 6)
    sprite('jn620_01', 6)
    sprite('jn620_02', 6)
    sprite('jn620_03', 6)
    sprite('jn620_04', 6)
    sprite('jn620_05', 6)
    sprite('jn620_06', 6)
    sprite('jn620_07', 6)
    sprite('jn620_08', 32767)


@State
def EventVSAM1():
    sprite('jn430_26', 4)
    sprite('jn430_25', 4)
    sprite('jn430_24', 5)
    sprite('jn430_23', 32767)
    CreateObject('EffNoutou', 0)


@State
def EventVSAM2():
    sprite('jn430_23', 5)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventVSRG1():
    setInvincible(1)
    AttackDefaults_StandingNormal()
    sprite('jn202_00', 2)
    sprite('jn202_01', 2)
    sprite('jn202_02', 2)
    sprite('jn202_03', 3)
    sprite('jn202_04', 2)
    CreateObject('zan_b0', -1)
    CommonSE('009_swing_rapier_1')
    sprite('jn202_05', 2)
    sprite('jn202_05', 12)
    StartMultihit()
    sprite('jn202_06', 2)
    sprite('jn202_08', 3)
    sprite('jn202_09', 3)
    sprite('jn202_10', 2)
    sprite('jn202_11', 1)
    sprite('jn202_12', 1)
    sprite('jn202_14', 1)
    CreateObject('EffNoutou', 0)
    sprite('jn202_16', 1)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventVSTB1():
    sprite('jn300_04', 32767)


@State
def EventVSTB2():
    sprite('jn300_04', 8)
    sprite('jn300_05', 6)
    sprite('jn300_06', 6)
    sprite('jn300_07', 6)
    sprite('jn300_08', 6)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventJNDamage():
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_02', 15)
    sprite('jn620_01', 7)
    sprite('jn620_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventJNDamage2():
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_02', 30)
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 100)
    sprite('jn300_05', 8)
    sprite('jn300_06', 8)
    sprite('jn300_07', 6)
    sprite('jn300_08', 6)
    sprite('jn300_09', 8)
    sprite('jn300_10', 8)
    loopRest()
    enterState('CmnActStand')


@State
def EventJNvsHZWin():
    sprite('jn033_00', 2)
    ScreenCollision(0)
    sprite('jn033_01', 3)
    physicsXImpulse(-48000)
    physicsYImpulse(30000)
    setGravity(1550)
    JumpSoundEffects()
    CommonSE('000_airdash_2')
    sprite('jn033_02', 3)
    sprite('jn033_03', 3)
    sprite('jn033_04', 3)
    sprite('jn033_05', 2)
    sprite('jn033_06', 1)
    sprite('jn033_07', 1)
    sprite('jn033_08', 1)
    sprite('null', 1)


@State
def EventJNYoroke():
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_02', 5)
    sprite('jn620_03', 5)
    sprite('jn620_04', 5)
    sprite('jn620_05', 5)
    sprite('jn620_06', 5)
    sprite('jn620_07', 5)
    sprite('jn620_08', 32767)


@State
def EventJNYorokeReverse():
    sprite('jn620_08', 8)
    sprite('jn620_07', 8)
    sprite('jn620_06', 8)
    sprite('jn620_05', 8)
    sprite('jn620_04', 12)
    sprite('jn620_03', 4)
    sprite('jn620_02', 4)
    sprite('jn620_01', 4)
    sprite('jn620_00', 3)
    enterState('CmnActStand')


@State
def EventJNvsNOEntry02():
    label(0)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def EventJNTimeupLoop():
    sprite('jn620_08', 32767)


@State
def EventJNvsNOWin01():
    EnableCollision(0)
    ScreenCollision(0)
    sprite('jn620_08', 6)
    sprite('jn620_07', 6)
    sprite('jn620_06', 6)
    sprite('jn620_05', 6)
    sprite('jn620_04', 6)
    sprite('jn620_03', 6)
    sprite('jn620_02', 6)
    sprite('jn620_01', 6)
    sprite('jn620_00', 6)
    loopRest()
    sprite('jn032_00', 4)
    physicsXImpulse(24000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)


@State
def EventKubifuri():
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 60)
    sprite('jn300_05', 6)
    sprite('jn300_06', 6)
    sprite('jn300_07', 6)
    sprite('jn300_08', 6)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    enterState('CmnActStand')


@State
def EventKubifuriShort():
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 10)
    sprite('jn300_05', 6)
    sprite('jn300_06', 6)
    sprite('jn300_07', 6)
    sprite('jn300_08', 6)
    sprite('jn300_09', 6)
    sprite('jn300_10', 6)
    enterState('CmnActStand')


@State
def EventJNYorokeSummon():
    sprite('jn620_08', 32767)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)


@State
def EventJNYorokeDelObj():
    sprite('jn620_08', 32767)
    DeleteObject(5)


@State
def EventHazamaAttack():
    sprite('jn000_00', 7)
    CreateObject('EventEffSpKensei', -1)
    sprite('jn000_01', 5)
    sprite('jn000_01ex01', 2)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitlz', 108)
    CommonSE('101_hit_slash_2')
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventRGAntiAirEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(8)
        UseSlashHitspark(1)
        setInvincible(1)
    sprite('jn000_00', 7)
    sprite('jn407_00', 3)
    sprite('jn407_01', 3)
    sprite('jn407_02', 3)
    sprite('jn407_03', 3)
    sprite('jn407_04', 3)
    PrivateSE('jnse_21')
    CreateObject('zan407', 0)
    CommonSE('009_swing_rapier_0')
    sprite('jn407_05', 3)
    sprite('jn407_06', 3)
    sprite('jn407_07', 3)
    sprite('jn407_08', 3)
    sprite('jn407_26', 10)
    sprite('jn407_09', 2)
    sprite('jn407_10', 3)
    sprite('jn407_11', 3)
    PrivateSE('jnse_21')
    CreateObject('EFF28AtkD', 0)
    sprite('jn407_12ex', 3)
    RefreshMultihit()
    Hitstop(20)
    CommonSE('010_swing_sword_0')
    sprite('jn407_13ex', 3)
    sprite('jn407_14', 3)
    sprite('jn407_15', 3)
    sprite('jn407_16', 3)
    sprite('jn407_17', 3)
    sprite('jn407_18', 3)
    sprite('jn407_19', 3)
    sprite('jn407_20', 3)
    sprite('jn407_21', 5)
    sprite('jn407_22', 4)
    sprite('jn407_23', 3)
    sprite('jn407_24', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn407_25', 3)
    XPositionRelativeFacing(-260000)
    loopRest()


@State
def EventRGWin1():
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 5)
    loopRest()


@State
def EventRGYorokeLoop():
    sprite('jn070_02', 32767)


@State
def EventRGYoroke2Down():
    sprite('jn070_03', 2)
    sprite('jn070_08', 6)
    sprite('jn070_09', 6)
    sprite('jn070_10', 6)
    sprite('jn070_11', 6)
    sprite('jn064_03', 6)
    sprite('jn064_02', 6)
    sprite('jn064_01', 6)
    sprite('jn063_09', 32767)
    loopRest()


@State
def EventJNReAction():
    sprite('jn001_00', 8)
    sprite('jn001_01', 8)
    sprite('jn001_02', 10)
    sprite('jn001_03', 8)
    sprite('jn001_04', 8)
    sprite('jn001_05', 8)
    sprite('jn001_06', 10)
    sprite('jn001_07', 8)
    sprite('jn001_08', 8)
    sprite('jn001_09', 8)
    enterState('CmnActStand')


@State
def EventJNVsRCDownLoop():
    sprite('jn063_09', 32767)
    XPositionRelativeFacing(-40000)
    loopRest()


@State
def EventTBDown01():
    sprite('jn061_00', 32767)
    XPositionRelativeFacing(-50000)


@State
def EventMUYoroke():
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_02', 5)
    sprite('jn620_03', 5)
    sprite('jn620_04', 5)
    sprite('jn620_05', 5)
    sprite('jn620_06', 5)
    sprite('jn620_07', 5)
    sprite('jn620_08', 32767)


@State
def EventMUUdekumiloop():
    label(0)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(0)


@State
def EventMUSummonSword():
    sprite('jn600_00', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(4, 1)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    sprite('jn600_04', 6)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_4():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    sprite('jn000_00', 1)
    enterState('CmnActStand')


@State
def EventHZVsJN_Dash5C():
    ScreenCollision(0)
    XPositionRelativeFacing(-1350000)
    Visibility(0)

    def upon_EVERY_FRAME():
        if SLOT_29 < 700000:
            sendToLabel(1)
    sprite('jn032_00', 4)
    CommonSE('000_airdash_0')
    physicsXImpulse(10000)
    SetAcceleration(1000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    label(0)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    sprite('jn032_11', 2)
    ObjectUpon(22, 32)
    SetAcceleration(0)
    XImpulseAcceleration(60)
    sprite('jn032_11', 2)
    sprite('jn032_12', 2)
    XImpulseAcceleration(60)
    sprite('jn202_03', 3)
    sprite('jn202_04', 2)
    CreateObject('zan_b0', -1)
    CommonSE('009_swing_rapier_1')
    XImpulseAcceleration(60)
    sprite('jn202_05', 2)
    sprite('jn202_05', 5)
    StartMultihit()
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('jn202_06', 4)
    sprite('jn202_07', 3)
    sprite('jn202_08', 4)
    sprite('jn202_09', 4)
    sprite('jn202_10', 3)
    sprite('jn202_11', 3)
    sprite('jn202_12', 3)
    sprite('jn202_13', 2)
    sprite('jn202_14', 2)
    CreateObject('EffNoutou', 0)
    sprite('jn202_15', 2)
    sprite('jn202_16', 2)
    enterState('CmnActStand')


@State
def EventGuardUe():
    sprite('jn040_00', 6)
    sprite('jn040_01', 6)
    label(0)
    sprite('jn040_02', 6)
    sprite('jn040_03', 6)
    sprite('jn040_04', 6)
    gotoLabel(0)


@State
def EventGuardUeEnd():
    sprite('jn040_00', 6)
    sprite('jn040_01', 6)
    enterState('CmnActStand')


@State
def EventWin2():
    sprite('jn611_00', 5)
    sprite('jn611_01', 5)
    sprite('jn611_02', 5)
    sprite('jn611_03', 5)
    sprite('jn611_04', 5)
    sprite('jn611_05', 5)
    CreateObject('jnef611icewing', 0)
    PrivateSE('jnse_02')
    sprite('jn611_06', 5)
    sprite('jn611_07', 5)
    sprite('jn611_08', 5)
    sprite('jn611_09', 5)
    sprite('jn611_10', 5)
    sprite('jn611_11', 5)
    sprite('jn611_12', 5)
    sprite('jn611_13', 60)
    sprite('jn611_13', 5)
    sprite('jn611_13', 32767)
    loopRest()


@State
def EventTBDown02():
    sprite('jn620_08', 30)
    ParticleSize(1200)
    CreateObject('EventTBHitEff', 0)
    RegisterObject(4, 1)

    def RunOnObject_4():
        SetZVal(-4000)
    sprite('jn620_08', 32767)


@State
def EventJNYorokeEnd():
    sprite('jn620_08', 5)
    sprite('jn620_07', 5)
    sprite('jn620_06', 5)
    sprite('jn620_05', 5)
    sprite('jn620_04', 5)
    sprite('jn620_03', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventDashLeaveOpposite():
    sprite('jn032_00', 4)
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(24000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    ObjectUpon(22, 32)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)


@State
def EventJNvsTBAction01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-100000)
    label(0)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def EventJNvsTBAction02():
    sprite('jn003_00', 3)
    sprite('jn003_01', 3)
    Flip()
    label(1)
    sprite('jn000_00', 7)
    physicsXImpulse(0)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(1)


@State
def EventCrouch():
    label(0)
    sprite('jn010_02', 6)
    sprite('jn010_03', 6)
    sprite('jn010_04', 6)
    sprite('jn010_05', 6)
    sprite('jn010_06', 6)
    sprite('jn010_07', 6)
    sprite('jn010_08', 6)
    sprite('jn010_09', 6)
    sprite('jn010_10', 6)
    sprite('jn010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def EventCrouchToStand():
    sprite('jn010_01', 4)
    sprite('jn010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventSummonPtPhantom():
    sprite('keep', 2)
    CreateObject('ptPhantom', -1)

    def RunOnObject_1():
        AddX(-50000)
        SetZVal(-500)
    loopRest()
    enterState('CmnActStand')


@State
def EventSummonPtPhantomEnd():
    sprite('keep', 2)
    TriggerUponForState('ptPhantom', 32)
    enterState('CmnActStand')


@State
def EventShake():
    sprite('keep', 2)
    CreateObject('EventShakeObj', -1)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalkFrameIn():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('jn030_00', 6)
    physicsXImpulse(4650)
    label(0)
    sprite('jn030_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)
    sprite('jn030_03', 6)
    sprite('jn030_04', 6)
    sprite('jn030_05', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)
    sprite('jn030_07', 6)
    sprite('jn030_08', 6)
    sprite('jn030_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventUltimateShot():
    sprite('jn430_00', 1)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    HeatChange(-5000)
    CreateObject('EMB_JN', -1)
    sprite('jn430_00', 1)
    sprite('jn430_01', 2)
    sprite('jn430_02', 2)
    sprite('jn430_03', 2)
    sprite('jn430_04', 2)
    sprite('jn430_05', 2)
    sprite('jn430_06', 2)
    sprite('jn430_07', 3)
    sprite('jn430_08', 3)
    sprite('jn430_09', 3)
    sprite('jn430_10', 3)
    CommonSE('009_swing_rapier_1')
    sprite('jn430_11', 3)
    sprite('jn430_12', 3)
    sprite('jn430_13', 3)
    sprite('jn430_14', 3)
    CommonSE('006_swing_blade_1')
    sprite('jn430_15', 3)
    CreateObject('Event_UltimateSlashShotObj', 0)
    CommonSE('000_airdash_0')
    ObjectUpon(22, 32)
    sprite('jn430_16', 3)
    sprite('jn430_17', 3)
    sprite('jn430_18', 3)
    sprite('jn430_19', 3)
    sprite('jn430_20', 3)
    sprite('jn430_21', 3)
    sprite('jn430_22', 3)
    sprite('jn430_23', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn430_24', 3)
    sprite('jn430_25', 3)
    sprite('jn430_26', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventDashLeaveOppositeReverse():
    sprite('jn032_00', 4)
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(-24000)
    DashEffects(100, 1, 1)
    Flip()
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    ObjectUpon(22, 32)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Entry1():
    label(0)
    sprite('jn600_00', 6)
    sprite('jn600_01', 6)
    sprite('jn600_02', 6)
    sprite('jn600_03', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Entry1End():
    sprite('keep', 2)
    sprite('jn600_04', 6)
    CreateObject('jnef600iceSword', -1)
    RegisterObject(5, 1)
    sprite('jn600_05', 6)
    sprite('jn600_06', 6)
    sprite('jn600_07', 6)
    sprite('jn600_08', 6)
    sprite('jn600_09', 6)
    sprite('jn600_10', 6)
    sprite('jn600_11', 6)

    def RunOnObject_5():
        sendToLabel(1)
    sprite('jn600_12', 6)
    sprite('jn600_13', 6)
    sprite('jn600_14', 6)
    sprite('jn600_15', 6)
    sprite('jn600_16', 6)
    sprite('jn600_17', 6)
    sprite('jn600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Kenchira():
    sprite('jn430_26', 4)
    sprite('jn430_25', 4)
    sprite('jn430_24', 5)
    sprite('jn430_23', 5)
    CreateObject('EffNoutou', 0)
    sprite('jn430_23', 32767)
    loopRest()


@State
def Act2Event_KenchiraEnd():
    sprite('jn430_23', 5)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_SummonTrinity():
    sprite('keep', 2)
    CreateObject('ptPhantom', -1)

    def RunOnObject_1():
        AddX(-50000)
        SetZVal(-500)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_bnvsjn_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('jn003_01', 4)
    Flip()
    sprite('jn003_00', 4)
    sprite('jn030_00', 6)
    physicsXImpulse(4650)
    sprite('jn030_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)
    sprite('jn030_03', 6)
    sprite('jn030_04', 6)
    sprite('jn030_05', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)
    sprite('jn030_07', 6)
    sprite('jn030_08', 6)
    sprite('jn030_09', 6)
    sprite('jn030_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)
    sprite('jn030_03', 6)
    sprite('jn030_04', 6)
    sprite('jn030_05', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)
    sprite('jn030_07', 6)
    sprite('jn030_08', 6)
    sprite('jn030_09', 6)
    sprite('null', 32767)
    EndMomentum(1)


@State
def Act2Event_cevsjn_00():
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_01', 7)
    sprite('jn620_00', 7)
    sprite('jn000_00', 7)
    sprite('jn001_00', 8)
    sprite('jn001_01', 8)
    sprite('jn001_02', 10)
    sprite('jn001_03', 8)
    sprite('jn001_04', 8)
    sprite('jn001_05', 8)
    sprite('jn001_06', 10)
    sprite('jn001_07', 8)
    sprite('jn001_08', 8)
    sprite('jn001_09', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvstb_00():
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 32767)
    loopRest()


@State
def Act3Event_jnvstb_01():
    sprite('jn300_05', 7)
    sprite('jn300_06', 7)
    sprite('jn300_07', 7)
    sprite('jn300_08', 7)
    sprite('jn300_09', 7)
    sprite('jn300_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvstb_02():
    sprite('jn001_00', 8)
    sprite('jn001_01', 8)
    sprite('jn001_02', 10)
    sprite('jn001_03', 8)
    sprite('jn001_04', 8)
    sprite('jn001_05', 8)
    sprite('jn001_06', 10)
    sprite('jn001_07', 8)
    sprite('jn001_08', 8)
    sprite('jn001_09', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvstb_03():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('jn414_06', 1)
    CommonSE('009_swing_rapier_1')
    sprite('jn414_07', 2)
    sprite('jn414_08', 2)
    CommonSE('009_swing_rapier_2')
    CreateObject('zan414', -1)
    sprite('jn414_09', 2)
    sprite('jn414_09', 16)
    sprite('jn414_10', 6)
    sprite('jn414_11', 6)
    CreateObject('EffNoutou', 0)
    sprite('jn414_12', 24)
    sprite('jn414_13', 5)
    sprite('jn414_14', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvstb_04():
    sprite('jn601_14', 6)
    sprite('jn600_18', 6)
    sprite('jn601_09', 6)
    sprite('jn601_10', 6)
    sprite('jn601_11', 6)
    sprite('jn601_12', 32767)
    loopRest()


@State
def Act3Event_jnvstb_05():
    sprite('keep', 30)
    CameraControlEnable(1)
    CameraControlInfinity(1)
    sprite('keep', 10)
    CreateObject('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)
    loopRest()


@State
def Act3Event_jnvstb_06():
    sprite('keep', 2)
    sprite('jn601_13', 6)
    sprite('jn601_14', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvsrc_00():
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 32767)
    loopRest()


@State
def Act3Event_jnvsrc_01():
    sprite('keep', 2)
    sprite('jn610_00', 7)
    loopRest()
    enterState('Act3Event_jnvstb_00')


@State
def Act3Event_jnvsrc_02():
    sprite('keep', 2)
    CreateObject('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)
    loopRest()


@State
def Act3Event_jnvsno_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-960000)
        NoAttackDuringAction(1)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 300000:
                    clearUponHandler(EVERY_FRAME)
                    ObjectUpon(22, 32)
                    uponSendToLabel(LANDING, 100)
                    sendToLabel(0)
            elif SLOT_XDistanceFromCenterOfStage > -300000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(22, 32)
                uponSendToLabel(LANDING, 100)
                sendToLabel(0)
    sprite('jn408_00', 3)
    CreateObject('Act3Event_IceBoard', -1)
    RegisterObject(4, 1)
    sprite('jn408_01', 3)
    physicsXImpulse(-3000)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    sprite('jn408_02', 3)
    sprite('jn408_03', 2)
    sprite('jn408_04', 2)
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)
    CommonSE('000_airdash_0')
    physicsXImpulse(42000)
    SetAcceleration(1000)
    ObjectUpon(FALLING, 32)
    label(1)
    sprite('jn408_06ex', 2)
    sprite('jn408_07ex', 2)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 3)
    sprite('keep', 7)
    SetAcceleration(0)
    XImpulseAcceleration(0)
    sprite('jn408_08', 5)
    DeleteObject(4)
    CreateObject('Act3Event_IceBoard_koware', -1)
    physicsXImpulse(-10000)
    physicsYImpulse(14000)
    EndYPhysicsImpulse()
    label(9)
    sprite('jn408_09', 3)
    sprite('jn408_10', 3)
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('jn020_10', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('jn020_11', 5)
    sprite('jn020_12', 6)
    sprite('jn020_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvsno_01():
    sprite('jn430_00', 3)
    CommonSE('009_swing_rapier_2')
    sprite('jn430_04', 4)
    sprite('jn430_03', 4)
    sprite('jn430_02', 4)
    sprite('jn430_01', 32767)
    loopRest()


@State
def Act3Event_jnvsno_02():
    sprite('jn410_14', 2)
    CommonSE('009_swing_rapier_1')
    sprite('jn410_15', 3)
    sprite('jn410_16', 4)
    sprite('jn410_17', 4)
    sprite('jn410_18', 4)
    sprite('jn410_19', 15)
    CreateObject('EffNoutou', 0)
    sprite('jn410_20', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvsno_03():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-900000)
        ScreenCollision(0)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 360000:
                sendToLabel(0)
                clearUponHandler(EVERY_FRAME)
        elif SLOT_XDistanceFromCenterOfStage > -360000:
            sendToLabel(0)
            clearUponHandler(EVERY_FRAME)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    physicsXImpulse(24000)
    sprite('jn032_01', 4)
    label(9)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('jn032_11', 6)
    physicsXImpulse(0)
    SetInertia(10000)
    sprite('jn032_12', 6)
    loopRest()
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act3Event_jnvskg_00():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('jn407_09', 1)
    sprite('jn407_10', 2)
    sprite('jn407_11', 2)
    PrivateSE('jnse_21')
    CreateObject('EFF28AtkD', 0)
    sprite('jn407_12', 24)
    CreateObject('Act3Event_Offset', 0)
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    sprite('jn407_13', 3)
    sprite('jn407_14', 3)
    sprite('jn407_15', 3)
    sprite('jn407_16', 3)
    sprite('jn407_17', 3)
    sprite('jn407_18', 3)
    sprite('jn407_19', 3)
    sprite('jn407_20', 3)
    sprite('jn407_21', 5)
    sprite('jn407_22', 4)
    sprite('jn407_23', 3)
    sprite('jn407_24', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn407_25', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_arvsjn_00():

    def upon_IMMEDIATE():
        AddX(180000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn620_00', 2)
    clearUponHandler(32)
    CommonSE('100_hit_grap_2')
    ScreenShake(3000, 18000)
    CallCustomizableParticle('ef_hitmd', 103)
    sprite('jn620_01', 2)
    sprite('jn620_02', 2)
    sprite('jn620_03', 2)
    sprite('jn620_04', 2)
    sprite('jn620_05', 16)
    AddInertia(-29000)
    sprite('jn620_06', 5)
    sprite('jn620_07', 5)
    sprite('jn620_08', 32767)
    EndMomentum(1)
    loopRest()


@State
def Act3Event_arvsjn_01():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('jn620_08', 3)
    sprite('jn620_07', 3)
    sprite('jn620_06', 3)
    sprite('jn620_05', 3)
    sprite('jn620_04', 5)
    sprite('jn620_03', 2)
    sprite('jn620_02', 2)
    sprite('jn620_01', 2)
    sprite('jn620_00', 2)
    sprite('jn000_00', 5)
    sprite('jn405_00', 2)
    sprite('jn405_01', 2)
    sprite('jn405_02', 2)
    sprite('jn405_03', 1)
    CreateObject('EFF28AtkA', 0)
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    sprite('jn405_04', 16)
    PrivateSE('jnse_21')
    ObjectUpon(22, 32)
    sprite('jn405_05', 3)
    sprite('jn405_06', 3)
    sprite('jn405_07', 2)
    sprite('jn405_07ex', 2)
    sprite('jn405_08', 2)
    sprite('jn405_08ex', 2)
    sprite('jn405_09', 2)
    sprite('jn405_09ex', 2)
    sprite('jn405_10', 2)
    sprite('jn405_11', 3)
    CreateObject('EffNoutou', 0)
    sprite('jn405_12', 2)
    sprite('jn405_13', 2)
    sprite('jn405_14', 2)
    sprite('jn405_15', 2)
    sprite('jn405_16', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_DashOut():
    sprite('jn003_01', 4)
    Flip()
    sprite('jn003_00', 4)
    sprite('jn032_00', 4)
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(24000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    ObjectUpon(22, 32)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('null', 32767)


@State
def Act3Event_ptvsjn_00():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('jn414_06', 1)
    CommonSE('009_swing_rapier_1')
    sprite('jn414_07', 2)
    sprite('jn414_08', 2)
    CommonSE('009_swing_rapier_2')
    CreateObject('zan414', -1)
    sprite('jn414_09', 2)
    sprite('jn414_09', 16)
    ObjectUpon(22, 32)
    sprite('jn414_10', 6)
    sprite('jn414_11', 6)
    CreateObject('EffNoutou', 0)
    sprite('jn414_12', 24)
    sprite('jn414_13', 5)
    sprite('jn414_14', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_izvsjn_00():
    sprite('jn110_05', 3)
    AddX(230000)
    sprite('jn110_06', 8)
    CreateParticle('caef_guardcrash', 0)
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)
    AddInertia(-50000)
    sprite('jn110_07', 10)
    PerInertia(30)
    KnockdownEffects(100, 1, 1)
    sprite('jn110_07', 5)
    KnockdownEffects(100, 1, 0)
    EndMomentum(1)
    sprite('jn110_08', 7)
    sprite('jn010_00', 6)
    sprite('jn000_00', 6)
    sprite('jn000_00', 6)
    sprite('jn610_00', 5)
    sprite('jn610_01', 5)
    sprite('jn610_02', 5)
    sprite('jn610_03', 5)
    sprite('jn610_04', 5)
    sprite('jn610_05', 5)
    sprite('jn610_06', 5)
    sprite('jn610_07', 5)
    sprite('jn610_08', 5)
    sprite('jn610_00', 7)
    loopRest()
    enterState('CmnActStand')
    loopRest()


@State
def Act3Event_tmvsjn_00():
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 32767)
    loopRest()


@State
def Act3Event_tmvsjn_01():
    sprite('jn300_05', 7)
    TriggerUponForState('Act3Event_ptPhantom_Renew', 32)
    sprite('jn300_06', 7)
    sprite('jn300_07', 7)
    sprite('jn300_08', 7)
    sprite('jn300_09', 7)
    sprite('jn300_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tmvsjn_02():
    sprite('jn110_05', 3)
    AddX(230000)
    sprite('jn110_06', 8)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('106_guard_crush')
    CommonSE('101_hit_slash_3')
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)
    AddInertia(-50000)
    sprite('jn110_07', 10)
    PerInertia(30)
    KnockdownEffects(100, 1, 1)
    sprite('jn110_07', 5)
    KnockdownEffects(100, 1, 0)
    EndMomentum(1)
    sprite('jn110_08', 7)
    sprite('jn000_00', 6)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 3:
            if SLOT_52 % 2:
                AddX(1000)
            else:
                AddX(-1000)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1
    sprite('jn620_00', 5)
    sprite('jn620_01', 5)
    sprite('jn620_02', 5)
    sprite('jn620_03', 5)
    sprite('jn620_04', 5)
    sprite('jn620_05', 5)
    sprite('jn620_06', 5)
    sprite('jn620_07', 5)
    sprite('jn620_08', 32767)
    clearUponHandler(EVERY_FRAME)
    loopRest()


@State
def Act3Event_tmvsjn_03():
    sprite('keep', 2)
    CreateObject('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)
    loopRest()


@State
def Act3Event_tmvsjn_04():
    sprite('jn430_23', 5)
    CreateObject('Act3Event_ptPhantom_Renew', -1)
    sprite('jn430_24', 6)
    sprite('jn430_25', 6)
    sprite('jn430_26', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tmvsjn_05():
    sprite('jn620_08', 6)
    TriggerUponForState('Act3Event_ptPhantom_Renew', 32)
    sprite('jn620_07', 6)
    sprite('jn620_06', 6)
    sprite('jn620_05', 6)
    sprite('jn620_04', 5)
    sprite('jn620_03', 2)
    sprite('jn620_02', 2)
    sprite('jn620_01', 2)
    sprite('jn620_00', 2)
    sprite('jn000_00', 4)
    sprite('jn003_01', 4)
    Flip()
    sprite('jn003_00', 4)
    sprite('jn032_00', 4)
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(24000)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    ObjectUpon(22, 32)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_00', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('null', 32767)


@State
def Act3Event_phvsjn_00():
    sprite('jn110_05', 3)
    AddX(230000)
    sprite('jn110_06', 8)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('106_guard_crush')
    CommonSE('101_hit_slash_3')
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)
    AddInertia(-50000)
    sprite('jn110_07', 10)
    PerInertia(30)
    KnockdownEffects(100, 1, 1)
    sprite('jn110_07', 5)
    KnockdownEffects(100, 1, 0)
    EndMomentum(1)
    sprite('jn110_08', 7)
    sprite('jn000_00', 6)
    loopRest()
    sprite('jn300_00', 6)
    sprite('jn300_01', 6)
    sprite('jn300_02', 6)
    sprite('jn300_03', 6)
    sprite('jn300_04', 30)
    sprite('jn300_05', 7)
    sprite('jn300_06', 7)
    sprite('jn300_07', 7)
    sprite('jn300_08', 7)
    sprite('jn300_09', 7)
    sprite('jn300_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsjn_01():
    sprite('jn033_00', 2)
    ScreenCollision(0)
    sprite('jn033_01', 3)
    physicsXImpulse(-48000)
    physicsYImpulse(30000)
    setGravity(1550)
    JumpSoundEffects()
    CommonSE('000_airdash_2')
    sprite('jn033_02', 3)
    sprite('jn033_03', 3)
    sprite('jn033_04', 3)
    sprite('jn033_05', 2)
    sprite('jn033_06', 1)
    sprite('jn033_07', 1)
    sprite('jn033_08', 1)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_phvsjn_02():
    sprite('keep', 2)
    CreateObject('Act3Event_ptPhantom_Renew', -1)
    loopRest()
    enterState('CmnActStand')
