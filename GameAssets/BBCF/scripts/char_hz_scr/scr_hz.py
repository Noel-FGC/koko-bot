@Subroutine
def PreInit():
    CharacterID('hz')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(6200)
    WalkBSpeed(4800)
    DashFInitialVelocity(18000)
    JumpYVelocity(31000)
    SuperJumpYVelocity(38000)
    Gravity(1500)
    AirDashFSpeed(24000)
    AirFDashDuration(16)
    AirDashBSpeed(18000)
    AirBDashDuration(14)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    if SLOT_116:
        Health(14000)
        WalkFSpeed(9300)
        WalkBSpeed(7200)
        OverdriveDuration(780, 780, 780, 780, 780, 780, 780, 780, 780, 780)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    ResourceGauge(0, 1, 15, 1, 2, 2, -1, -1)
    NumberGauge(0, 1)
    ResourceGauge(1, 0, 7, 1, 1500, 1500, -1, -1)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 200000, 100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    MoveHeatValuePriority(500, 1000, 10, 1000)
    SkillEstimateRange(0, 280000, -200000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(3000)
    OpponentAttackPriority(1)
    SkillEstimateRange(0, 250000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 320000, -200000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveLow()
    MoveHeatValuePriority(500, 1000, 10, 1000)
    SkillEstimateRange(0, 250000, -120000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    DamageStunPriority(1500)
    SkillEstimateRange(0, 280000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    MoveCancellableFrames(20, 22)
    AirborneOpponentPriority(3000)
    SkillEstimateRange(0, 300000, 50000, 350000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    GuardStunPriority(1000)
    DamageStunPriority(4000)
    SkillEstimateRange(-50000, 150000, 100000, 550000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    MoveCancellableFrames(14, 15)
    SkillEstimateRange(-50000, 320000, 200000, 500000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(0)
    SkillEstimateRange(50000, 550000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    MoveCancellableFrames(30, 40)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1400000, 0, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Easy', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('NmlAtk5D')
    Move_EndRegister()
    Move_Register('NmlAtk5DStop', 0x1)
    Move_Condition(0x304d)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    AirborneOpponentPriority(50000)
    SkillEstimateRange(-150000, 250000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4D', INPUT_4D)
    MoveCancellableFrames(34, 35)
    GuardStunPriority(1)
    SkillEstimateRange(100000, 400000, 250000, 1000000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4D_Easy', 0x1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('NmlAtk4D')
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    SkillEstimateRange(450000, 1000000, 250000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6D_Easy', 0x1)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('NmlAtk6D')
    Move_EndRegister()
    Move_Register('NmlAtk6DStop', 0x1)
    Move_Condition(0x304d)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    SkillEstimateRange(-150000, 1300000, -200000, 50000, 50000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    MoveCancellableFrames(20, 25)
    SkillEstimateRange(-100000, 10000, 700000, 2000000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2D_Easy', 0x1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('NmlAtk2D')
    Move_EndRegister()
    Move_Register('NmlAtk2DStop', 0x1)
    Move_Condition(0x304d)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    SkillEstimateRange(-150000, 1300000, -200000, 50000, 50000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(1)
    SkillEstimateRange(50000, 200000, -100000, 130000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(0, 350000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    DamageStunPriority(10000)
    SkillEstimateRange(0, 300000, -250000, 110000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_2', 0x1)
    FollowupOnly(1)
    Move_Input_(0x14)
    MoveComboPriority(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_3', 0x1)
    FollowupOnly(1)
    Move_Input_(0x14)
    MoveComboPriority(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_4', 0x1)
    FollowupOnly(1)
    Move_Input_(0x14)
    MoveComboPriority(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_5', 0x1)
    FollowupOnly(1)
    Move_Input_(0x14)
    MoveComboPriority(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    DamageStunPriority(10000)
    MoveCancellableFrames(100, 100)
    SkillEstimateRange(-150000, 300000, -350000, -100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    AirborneOpponentPriority(1)
    MoveComboPriority(0)
    DamageStunPriority(1)
    SkillEstimateRange(600000, 1000000, 0, 100000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2D', INPUT_J2D)
    AirborneOpponentPriority(1)
    MoveComboPriority(0)
    DamageStunPriority(1)
    SkillEstimateRange(-70000, 70000, -800000, -500000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR4D', INPUT_J4D)
    AirborneOpponentPriority(1)
    MoveComboPriority(0)
    DamageStunPriority(1)
    SkillEstimateRange(300000, 600000, -800000, -450000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6D', INPUT_J6D)
    AirborneOpponentPriority(1)
    MoveComboPriority(0)
    DamageStunPriority(1)
    SkillEstimateRange(600000, 1100000, -500000, -100000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR8D', INPUT_J8D)
    AirborneOpponentPriority(1)
    MoveComboPriority(0)
    DamageStunPriority(1)
    SkillEstimateRange(450000, 1000000, 250000, 600000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5DStop', 0x1)
    Move_Condition(0x304d)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    SkillEstimateRange(-150000, 250000, -200000, 300000, 100000, 50)
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
    SkillEstimateRange(100000, 250000, -20000, 50000, 1000, 50)
    Move_EndRegister()
    Move_Register('DriveJump8', INPUT_SPECIALMOVE)
    Move_Condition(0x304d)
    Move_Input_(0x8d)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    OpponentAttackPriority(100000)
    SkillEstimateRange(400000, 1200000, -600000, 1000000, 1000, 50)
    Move_EndRegister()
    Move_Register('DriveJump6', INPUT_SPECIALMOVE)
    Move_Condition(0x304d)
    Move_Input_(0x8d)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    DamageStunPriority(10000)
    GuardStunPriority(10000)
    SkillEstimateRange(-200000, 1200000, -600000, 1000000, 1000, 50)
    Move_EndRegister()
    Move_Register('DriveJump4', INPUT_SPECIALMOVE)
    Move_Condition(0x304d)
    Move_Input_(0x8d)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    GuardStunPriority(100000)
    SkillEstimateRange(400000, 1200000, -600000, 1000000, 1000, 50)
    Move_EndRegister()
    Move_Register('Kamae', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    Unknown15027(1)
    DamageStunPriority(1)
    GuardStunPriority(3000)
    SkillEstimateRange(0, 500000, -150000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('KamaeA', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    MoveMid()
    DamageStunPriority(2000)
    GuardStunPriority(5000)
    SkillEstimateRange(50000, 550000, 0, 350000, 750, 50)
    Move_EndRegister()
    Move_Register('KamaeB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(4000)
    SkillEstimateRange(-200000, 350000, 0, 450000, 1000, 50)
    Move_EndRegister()
    Move_Register('KamaeC', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    MoveLow()
    SkillEstimateRange(-50000, 450000, -250000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('KamaeD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    GuardStunPriority(10000)
    SkillEstimateRange(0, 400000, -200000, 180000, 50, 1000)
    Move_EndRegister()
    Move_Register('KamaeDashF', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_66)
    AddChain(1)
    SkillEstimateRange(0, 500000, -200000, 200000, 50, 1500)
    Move_EndRegister()
    Move_Register('KamaeDashB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_44)
    AddChain(1)
    OpponentAttackPriority(2000)
    SkillEstimateRange(0, 300000, -200000, 200000, 50, 1000)
    Move_EndRegister()
    Move_Register('SpecialShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    GuardStunPriority(2000)
    SkillEstimateRange(350000, 600000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('SpecialAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(1)
    SkillEstimateRange(-50000, 400000, -200000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(2500)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(300000, 800000, 650000, 1100000, 200, 0)
    Move_EndRegister()
    Move_Register('SpecialShot_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    StateCall('SpecialShot')
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('SPThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    MoveThrow()
    DamageStunPriority(1)
    JumpAvoidPriority(10000)
    SkillEstimateRange(0, 200000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AirAssault2', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    MovePriority(1)
    SkillEstimateRange(0, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 1500000, -200000, 0, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateShot_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    DamageStunPriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 1500000, -200000, 0, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow_OD', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(0xf7)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(20000)
    SkillEstimateRange(-300000, 300000, -200000, 1000000, 500, 1)
    Move_EndRegister()
    Move_Register('BurstDD_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    Move_Input_(INPUT_HOLD_B)
    Move_Input_(INPUT_HOLD_C)
    Move_Input_(INPUT_HOLD_D)
    Move_Condition(0x3081)
    CallSkillConditions('Func_BurstDD_Easy')
    OpponentAttackPriority(8000)
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
    OpponentAttackPriority(8000)
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
    OpponentAttackPriority(8000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk4D', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'SpecialShot', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'SpecialAssault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'UltimateShot', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'UltimateShot_OD', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'AirAssault2', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C_5', 'AirAssault2', 10000000)
    TempPriorityMultiplier('NmlAtk4D', 'DriveJump6', 10000000)
    TempPriorityMultiplier('NmlAtk4D', 'AntiAir', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2D', 'DriveJump6', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'AstralHeat', 10000000)
    StylishModeSpecialButton('UltimateShot', 0x4, 0xea)
    StylishModeSpecialButton('UltimateShot_OD', 0x4, 0xea)
    StylishModeSpecialButton('SpecialAssault', 0x4, 0xea)
    StylishModeSpecialButton('SPThrow', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('SpecialShot', 0x4, 0x45)
    StylishModeSpecialButton('KamaeA', 0x4, 0xea)
    StylishModeSpecialButton('UltimateThrow', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateThrow_OD', 0x4, 0x5f)
    StylishModeSpecialButton('AirAssault2', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5C', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 1, 200000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 3, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 1, 180000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 12, 0)
    StylishModeCancels('NmlAtk6A', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk6A', 'UltimateAssault_OD', 7, 0)
    StylishModeCancels('NmlAtk6A', 'AstralHeat', 10, 300000)
    StylishModeCancels('NmlAtk6B', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk6B', 'UltimateAssault_OD', 7, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk5D', 0, 0)
    StylishModeCancels('AntiAir', 'UltimateShot', 6, 0)
    StylishModeCancels('AntiAir', 'UltimateShot_OD', 6, 0)
    StylishModeCancels('ThrowExe', 'AntiAir', 6, 0)
    StylishModeCancels('ThrowExe', 'AstralHeat', 10, 400000)
    StylishModeCancels('BackThrowExe', 'Kamae', 6, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 1, 200000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 12, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'FHighJump', 12, 0)
    StylishModeCancels('NmlAtk3C', 'SpecialShot', 0, 0)
    StylishModeCancels('NmlAtk3C', 'SpecialAssault', 1, 300000)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault_OD', 7, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'AirAssault2', 3, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5C_2', 0, 0)
    StylishModeCancels('NmlAtkAIR5C_2', 'AirAssault2', 0, 0)
    StylishModeCancels('NmlAtkAIR5C_2', 'NmlAtkAIR5C_3', 2, 100000)
    StylishModeCancels('NmlAtkAIR5C_2', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C_2', 'NmlAtkAIR5C_3', 13, 0)
    StylishModeCancels('NmlAtkAIR5C_3', 'NmlAtkAIR5C_4', 0, 0)
    StylishModeCancels('NmlAtkAIR5C_4', 'NmlAtkAIR5C_5', 0, 0)
    StylishModeCancels('NmlAtkAIR5C_5', 'AirAssault2', 0, 0)
    StylishModeCancels('NmlAtkAIR2C', 'AirAssault2', 3, 0)
    StylishModeCancels('NmlAtkAIR2C', 'FJump', 12, 0)
    HitSprites(0, 'hz062_01')
    HitSprites(1, 'hz062_03')
    HitSprites(2, 'hz062_04')
    HitSprites(3, 'hz062_05')
    HitSprites(4, 'hz062_05')
    HitSprites(5, 'hz062_06')
    HitSprites(6, 'hz062_07')
    HitSprites(7, 'hz041_02')
    HitSprites(8, 'hz040_02')
    HitSprites(9, 'hz045_02')
    HitSprites(10, 'hz060_00')
    HitSprites(11, 'hz060_01')
    HitSprites(12, 'hz060_03')
    HitSprites(13, 'hz060_05')
    HitSprites(14, 'hz060_07')
    HitSprites(15, 'hz060_14')
    HitSprites(16, 'hz050_00')
    HitSprites(17, 'hz052_00')
    HitSprites(18, 'hz054_00')
    HitSprites(19, 'hz000_00')
    HitSprites(20, 'hz000_00')
    HitSprites(25, 'hz063_00')
    HitSprites(26, 'hz063_01')
    HitSprites(27, 'hz063_02')
    HitSprites(28, 'hz063_04')
    HitSprites(29, 'hz063_11')
    HitSprites(30, 'hz077_00')
    HitSprites(31, 'hz077_01')
    HitSprites(32, 'hz077_00ex01')
    HitSprites(33, 'hz077_01ex01')
    HitSprites(34, 'hz077_00ex02')
    HitSprites(35, 'hz077_01ex02')
    HitSprites(36, 'hz077_00ex03')
    HitSprites(37, 'hz077_01ex03')
    HitSprites(24, 'hz073_01')
    CommonVoicelines(0, 'hz000')
    CommonVoicelines(1, 'hz001')
    CommonVoicelines(2, 'hz002')
    CommonVoicelines(3, 'hz003')
    CommonVoicelines(4, 'hz004')
    CommonVoicelines(5, 'hz005')
    CommonVoicelines(6, 'hz006')
    CommonVoicelines(7, 'hz007')
    CommonVoicelines(8, 'hz008')
    CommonVoicelines(9, 'hz009')
    CommonVoicelines(10, 'hz010')
    CommonVoicelines(11, 'hz011')
    CommonVoicelines(12, 'hz012')
    CommonVoicelines(13, 'hz013')
    CommonVoicelines(14, 'hz014')
    CommonVoicelines(15, 'hz015')
    CommonVoicelines(16, 'hz016')
    CommonVoicelines(17, 'hz017')
    CommonVoicelines(18, 'hz018')
    CommonVoicelines(19, 'hz019')
    CommonVoicelines(20, 'hz020')
    CommonVoicelines(21, 'hz021')
    CommonVoicelines(22, 'hz022')
    CommonVoicelines(23, 'hz023')
    CommonVoicelines(24, 'hz024')
    CommonVoicelines(25, 'hz025')
    CommonVoicelines(26, 'hz026')
    CommonVoicelines(27, 'hz027')
    CommonVoicelines(28, 'hz028')
    CommonVoicelines(29, 'hz029')
    CommonVoicelines(30, 'hz030')
    CommonVoicelines(31, 'hz031')
    CommonVoicelines(32, 'hz032')
    CommonVoicelines(33, 'hz033')
    CommonVoicelines(34, 'hz034')
    CommonVoicelines(35, 'hz035')
    CommonVoicelines(36, 'hz036')
    CommonVoicelines(37, 'hz037')
    CommonVoicelines(38, 'hz038')
    CommonVoicelines(39, 'hz039')
    CommonVoicelines(40, 'hz040')
    CommonVoicelines(41, 'hz041')
    CommonVoicelines(42, 'hz042')
    CommonVoicelines(43, 'hz043')
    CommonVoicelines(44, 'hz044')
    CommonVoicelines(45, 'hz045')
    CommonVoicelines(46, 'hz046')
    CommonVoicelines(47, 'hz047')
    CommonVoicelines(48, 'hz048')
    CommonVoicelines(49, 'hz049')
    CommonVoicelines(50, 'hz050')
    CommonVoicelines(51, 'hz051')
    CommonVoicelines(52, 'hz052')
    CommonVoicelines(53, 'hz053')
    CommonVoicelines(54, 'hz100')
    CommonVoicelines(55, 'hz101')
    CommonVoicelines(56, 'hz102')
    CommonVoicelines(57, 'hz103')
    CommonVoicelines(58, 'hz104')
    CommonVoicelines(59, 'hz105')
    CommonVoicelines(60, 'hz106')
    CommonVoicelines(61, 'hz107')
    CommonVoicelines(62, 'hz108')
    CommonVoicelines(63, 'hz109')
    CommonVoicelines(64, 'hz150')
    CommonVoicelines(65, 'hz151')
    CommonVoicelines(66, 'hz152')
    CommonVoicelines(67, 'hz153')
    CommonVoicelines(68, 'hz154')
    CommonVoicelines(69, 'hz155')
    CommonVoicelines(70, 'hz156')
    CommonVoicelines(71, 'hz157')
    CommonVoicelines(72, 'hz158')
    CommonVoicelines(75, 'hz160')
    CommonVoicelines(73, 'hz402')
    CommonVoicelines(74, 'hz403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_OverdriveTimer:
            SLOT_32 = SLOT_32 + 30
        elif SLOT_IsGrounded:
            SLOT_32 = SLOT_32 + 10
        elif SLOT_32 <= 900:
            SLOT_32 = SLOT_32 + 5
        if SLOT_32 >= 1500:
            SLOT_31 = 2
        if SLOT_InNeutral:
            TrainingModeSLOT('TRI_HazamaUroboros', 2, 67)
            if SLOT_67:
                SLOT_31 = 1500
    if not SLOT_IsInHitstun:
        if SLOT_21:
            if SLOT_IsUnlimited:
                if not CheckObjectPresence(5):
                    if not SLOT_66:
                        CreateObject('HZEF_DrainField', -1)
                        RegisterObject(5, 1)
            elif SLOT_21:
                if SLOT_OverdriveTimer:
                    if not CheckObjectPresence(5):
                        if not SLOT_66:
                            CreateObject('HZEF_DrainField', -1)
                            RegisterObject(5, 1)
                if not SLOT_OverdriveTimer:
                    if not SLOT_64:
                        TriggerUponForState('HZEF_DrainField', 32)
        else:
            TriggerUponForState('HZEF_DrainField', 32)


@Subroutine
def OnActionBegin():
    TriggerUponForState('EffKamaeLand', 32)


@State
def CmnActStand():
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('hz001_00', 7)
    SLOT_88 = 960
    SmartVoiceline('hz000')
    sprite('hz001_01', 5)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_06', 5)
    sprite('hz001_07', 5)
    sprite('hz001_08', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('hz003_00', 3)
    SmartVoiceline('hz001')
    sprite('hz003_01', 3)
    sprite('hz003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('hz010_00', 4)
    sprite('hz010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('hz010_02', 8)
    sprite('hz010_03', 8)
    sprite('hz010_04', 8)
    sprite('hz010_05', 8)
    sprite('hz010_06', 8)
    sprite('hz010_07', 8)
    sprite('hz010_08', 8)
    sprite('hz010_09', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('hz013_00', 3)
    sprite('hz013_01', 3)
    sprite('hz013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('hz010_01', 4)
    sprite('hz010_00', 4)


@State
def CmnActJumpPre():
    sprite('hz023_00', 2)
    sprite('hz023_01', 1)
    sprite('hz023_02', 1)


@State
def CmnActJumpUpper():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('hz020_00', 3)
    sprite('hz020_01', 3)
    SmartVoiceline('hz002')
    label(10)
    sprite('hz020_00', 3)
    sprite('hz020_01', 3)
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('hz021_00', 3)
    sprite('hz021_01', 3)
    SmartVoiceline('hz002')
    label(11)
    sprite('hz021_00', 3)
    sprite('hz021_01', 3)
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('hz022_00', 3)
    sprite('hz022_01', 3)
    SmartVoiceline('hz003')
    label(22)
    sprite('hz022_00', 3)
    sprite('hz022_01', 3)
    loopRest()
    gotoLabel(22)


@State
def CmnActJumpUpperEnd():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('hz020_02', 3)
    sprite('hz020_03', 3)
    sprite('hz020_04', 3)
    loopRest()
    ExitState()
    label(1)
    sprite('hz021_02', 3)
    sprite('hz021_03', 2)
    sprite('hz021_04', 2)
    loopRest()
    ExitState()
    label(2)
    sprite('hz022_02', 3)
    sprite('hz022_03', 3)
    sprite('hz022_04', 3)
    loopRest()
    ExitState()


@State
def CmnActJumpDown():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('hz020_05', 3)
    sprite('hz020_06', 3)
    label(0)
    sprite('hz020_07', 3)
    sprite('hz020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz021_05', 2)
    sprite('hz021_06', 3)
    label(11)
    sprite('hz021_07', 3)
    sprite('hz021_08', 3)
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('hz022_05', 3)
    label(22)
    sprite('hz022_06', 3)
    sprite('hz022_07', 3)
    loopRest()
    gotoLabel(22)


@State
def CmnActJumpLanding():
    sprite('hz024_00', 3)
    sprite('hz024_01', 3)
    sprite('hz024_02', 3)
    sprite('hz024_03', 3)
    sprite('hz024_04', 3)
    sprite('hz024_05', 3)


@State
def CmnActLandingStiffLoop():
    sprite('hz024_00', 2)
    sprite('hz024_01', 2)
    sprite('hz024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('hz024_03', 3)
    sprite('hz024_04', 3)
    sprite('hz024_05', 3)


@State
def CmnActFWalk():
    sprite('hz030_00', 7)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('hz031_00', 7)
    sprite('hz031_01', 7)
    label(0)
    sprite('hz031_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz031_03', 7)
    sprite('hz031_04', 7)
    sprite('hz031_05', 7)
    sprite('hz031_06', 7)
    sprite('hz031_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz031_08', 7)
    sprite('hz031_09', 7)
    sprite('hz031_10', 7)
    sprite('hz031_11', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        EndMomentum(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffBarrierCancel2(1)
        WhiffOverdriveCancel(1)
        AddInertia(25000)
    sprite('hz032_00', 1)
    physicsXImpulse(5000)
    sprite('hz032_01', 1)
    physicsXImpulse(10000)
    sprite('hz032_02', 2)
    DashEffects(100, 1, 1)
    physicsXImpulse(24000)
    sprite('hz032_03', 2)
    sprite('hz032_02', 1)
    sprite('hz032_04', 2)
    XImpulseAcceleration(80)
    SkidEffects(100, 1, 1)
    sprite('hz032_04ex01', 2)
    XImpulseAcceleration(60)
    sprite('hz032_04ex02', 2)
    sprite('hz032_05', 2)
    XImpulseAcceleration(40)
    sprite('hz032_06', 2)
    sprite('hz032_07', 1)
    loopRest()


@State
def CmnActFDashStop():
    pass


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        InvincibilityDuration(7)
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('hz033_00', 1)
    sprite('hz033_01', 2)
    SmartVoiceline('hz005')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1200)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('hz033_05', 2)
    sprite('hz033_06', 2)
    sprite('hz033_07', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('hz035_00', 2)
    SmartVoiceline('hz004')
    sprite('hz035_01', 3)
    sprite('hz035_02', 3)
    sprite('hz035_03', 3)
    sprite('hz035_00', 3)
    sprite('hz020_04', 3)


@State
def CmnActAirBDash():
    sprite('hz036_00', 2)
    SmartVoiceline('hz006')
    sprite('hz036_01', 2)
    sprite('hz036_02', 2)
    sprite('hz036_03', 2)
    sprite('hz036_01', 2)
    sprite('hz036_00', 2)
    sprite('hz020_04', 2)


@State
def CmnActHitStandLv1():
    sprite('hz050_00', 1)
    sprite('hz050_01', 1)
    sprite('hz050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('hz050_01', 1)
    sprite('hz050_02', 1)
    sprite('hz050_01', 2)
    sprite('hz050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('hz050_02', 1)
    sprite('hz050_03', 1)
    sprite('hz050_02', 2)
    sprite('hz050_01', 2)
    sprite('hz050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('hz050_03', 1)
    sprite('hz050_04', 1)
    sprite('hz050_03', 2)
    sprite('hz050_02', 2)
    sprite('hz050_01', 2)
    sprite('hz050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('hz050_04', 1)
    sprite('hz050_04', 1)
    sprite('hz050_04', 2)
    sprite('hz050_03', 2)
    sprite('hz050_02', 2)
    sprite('hz050_01', 2)
    sprite('hz050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('hz052_00', 1)
    sprite('hz052_01', 1)
    sprite('hz052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('hz052_01', 1)
    sprite('hz052_02', 1)
    sprite('hz052_01', 2)
    sprite('hz052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('hz052_02', 1)
    sprite('hz052_03', 1)
    sprite('hz052_02', 2)
    sprite('hz052_01', 2)
    sprite('hz052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('hz052_03', 1)
    sprite('hz052_04', 1)
    sprite('hz052_03', 2)
    sprite('hz052_02', 2)
    sprite('hz052_01', 2)
    sprite('hz052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('hz052_04', 1)
    sprite('hz052_04', 1)
    sprite('hz052_04', 2)
    sprite('hz052_03', 2)
    sprite('hz052_02', 2)
    sprite('hz052_01', 2)
    sprite('hz052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('hz054_00', 1)
    sprite('hz054_01', 1)
    sprite('hz054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('hz054_01', 1)
    sprite('hz054_02', 1)
    sprite('hz054_01', 2)
    sprite('hz054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('hz054_02', 1)
    sprite('hz054_03', 1)
    sprite('hz054_02', 2)
    sprite('hz054_01', 2)
    sprite('hz054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('hz054_03', 1)
    sprite('hz054_04', 1)
    sprite('hz054_03', 2)
    sprite('hz054_02', 2)
    sprite('hz054_01', 2)
    sprite('hz054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('hz054_04', 1)
    sprite('hz054_04', 1)
    sprite('hz054_04', 2)
    sprite('hz054_03', 2)
    sprite('hz054_02', 2)
    sprite('hz054_01', 2)
    sprite('hz054_00', 2)


@State
def CmnActBDownUpper():
    sprite('hz060_00', 4)
    label(0)
    sprite('hz060_01', 4)
    sprite('hz060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('hz060_03', 4)


@State
def CmnActBDownDown():
    sprite('hz060_04', 4)
    label(0)
    sprite('hz060_05', 4)
    sprite('hz060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('hz060_07', 2)
    sprite('hz060_08', 2)


@State
def CmnActBDownBound():
    sprite('hz060_09', 3)
    sprite('hz060_10', 3)
    sprite('hz060_11', 3)
    sprite('hz060_12', 3)
    sprite('hz060_13', 3)


@State
def CmnActBDownLoop():
    sprite('hz060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('hz061_00', 3)
    sprite('hz061_01', 3)
    sprite('hz061_02', 3)
    sprite('hz061_03', 3)
    sprite('hz061_04', 3)
    sprite('hz061_05', 3)
    sprite('hz061_06', 2)
    sprite('hz061_07', 2)
    sprite('hz061_08', 2)
    sprite('hz061_09', 2)
    sprite('hz061_10', 3)
    sprite('hz061_11', 3)
    sprite('hz061_12', 3)
    sprite('hz061_13', 3)


@State
def CmnActFDownUpper():
    sprite('hz063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('hz063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('hz063_02', 3)
    sprite('hz063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('hz063_04', 3)
    sprite('hz063_05', 3)


@State
def CmnActFDownBound():
    sprite('hz063_06', 3)
    sprite('hz063_07', 3)
    sprite('hz063_08', 3)
    sprite('hz063_09', 3)
    sprite('hz063_10', 3)
    sprite('hz063_11', 3)


@State
def CmnActFDownLoop():
    sprite('hz063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('hz064_00', 3)
    sprite('hz064_01', 3)
    sprite('hz064_02', 3)
    sprite('hz064_03', 3)
    sprite('hz064_04', 3)
    sprite('hz064_05', 3)
    sprite('hz064_06', 3)
    sprite('hz064_07', 3)
    sprite('hz064_08', 3)
    sprite('hz064_09', 3)
    sprite('hz064_10', 3)
    sprite('hz064_11', 3)


@State
def CmnActVDownUpper():
    sprite('hz062_00', 3)
    label(0)
    sprite('hz062_01', 3)
    sprite('hz062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('hz062_03', 3)
    sprite('hz062_04', 3)


@State
def CmnActVDownDown():
    sprite('hz062_05', 3)
    sprite('hz062_06', 3)
    label(0)
    sprite('hz062_07', 3)
    sprite('hz062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('hz062_09', 2)
    sprite('hz062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('hz062_09', 2)
    sprite('hz062_10', 2)


@State
def CmnActBlowoff():
    sprite('hz072_00', 3)
    sprite('hz072_01', 3)
    sprite('hz072_02', 3)
    label(0)
    sprite('hz072_01', 3)
    sprite('hz072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('hz074_00', 3)
    sprite('hz074_01', 3)
    sprite('hz074_02', 3)
    sprite('hz074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('hz082_00', 2)
    sprite('hz082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('hz071_04', 1)


@State
def CmnActWallBound():
    sprite('hz073_00', 3)
    sprite('hz073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('hz073_02', 3)
    label(0)
    sprite('hz073_03', 3)
    sprite('hz073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('hz070_00', 4)
    sprite('hz070_01', 3)
    sprite('hz070_02', 3)
    sprite('hz070_03', 3)
    sprite('hz070_02', 4)
    sprite('hz070_03', 4)
    sprite('hz070_02', 5)
    sprite('hz070_03', 5)
    label(0)
    sprite('hz070_02', 6)
    sprite('hz070_03', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('hz070_04', 4)
    sprite('hz070_05', 4)
    sprite('hz070_06', 4)
    sprite('hz070_07', 4)
    sprite('hz070_08', 4)
    sprite('hz070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('hz070_10', 2)
    sprite('hz070_11', 2)
    sprite('hz070_12', 2)
    sprite('hz070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('hz113_00', 3)
    sprite('hz113_01', 3)
    sprite('hz113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('hz113_00', 3)
    sprite('hz113_01', 3)
    sprite('hz113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('hz113_00', 3)
    sprite('hz113_01', 3)
    sprite('hz113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('hz110_00', 2)
    sprite('hz110_01', 2)
    sprite('hz110_02', 2)
    sprite('hz110_03', 3)
    sprite('hz110_04', 3)
    sprite('hz110_06', 3)
    sprite('hz110_07', 3)
    sprite('hz110_08', 200)
    sprite('hz110_09', 3)
    sprite('hz110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('hz111_00', 2)
    sprite('hz111_01', 2)
    sprite('hz111_02', 2)
    sprite('hz111_03', 3)
    sprite('hz111_04', 3)
    sprite('hz111_06', 3)
    sprite('hz111_07', 3)
    sprite('hz111_08', 200)
    sprite('hz111_09', 3)
    sprite('hz111_10', 3)


@State
def CmnActUkemiLandN():
    sprite('hz112_00', 2)
    sprite('hz112_01', 2)
    sprite('hz112_02', 2)
    sprite('hz112_03', 2)
    sprite('hz112_04', 2)
    sprite('hz112_05', 2)
    sprite('hz112_06', 2)
    sprite('hz112_07', 2)
    sprite('hz112_08', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('hz024_00', 3)
    sprite('hz024_01', 3)
    sprite('hz024_02', 3)
    sprite('hz024_03', 3)
    sprite('hz024_04', 3)
    sprite('hz024_05', 3)


@State
def CmnActMidGuardPre():
    sprite('hz040_00', 3)
    sprite('hz040_01', 3)


@State
def CmnActMidGuardLoop():
    sprite('hz040_04', 3)
    sprite('hz040_03', 3)
    CreateObject('HZEF_GuardLoop', 0)
    sprite('hz040_02', 3)
    loopRest()
    label(0)
    sprite('hz040_04', 3)
    sprite('hz040_03', 3)
    sprite('hz040_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('hz040_01', 3)
    sprite('hz040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('hz040_05', 3)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz040_04', 3)
    sprite('hz040_03', 3)
    sprite('hz040_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('hz040_01', 3)
    sprite('hz040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('hz041_00', 3)
    sprite('hz041_01', 3)


@State
def CmnActHighGuardLoop():
    sprite('hz041_04', 3)
    sprite('hz041_03', 3)
    CreateObject('HZEF_GuardLoop', 0)
    sprite('hz041_02', 3)
    loopRest()
    label(0)
    sprite('hz041_04', 3)
    sprite('hz041_03', 3)
    sprite('hz041_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('hz041_01', 3)
    sprite('hz041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('hz041_05', 3)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz041_04', 3)
    sprite('hz041_03', 3)
    sprite('hz041_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('hz041_01', 3)
    sprite('hz041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('hz043_00', 3)
    sprite('hz043_01', 3)


@State
def CmnActCrouchGuardLoop():
    sprite('hz043_04', 3)
    sprite('hz043_03', 3)
    CreateObject('HZEF_GuardLoop', 0)
    sprite('hz043_02', 3)
    loopRest()
    label(0)
    sprite('hz043_04', 3)
    sprite('hz043_03', 3)
    sprite('hz043_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('hz043_01', 3)
    sprite('hz043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('hz043_05', 3)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz043_04', 3)
    sprite('hz043_03', 3)
    sprite('hz043_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('hz043_01', 3)
    sprite('hz043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('hz045_00', 3)
    sprite('hz045_01', 3)


@State
def CmnActAirGuardLoop():
    sprite('hz045_04', 3)
    sprite('hz045_03', 3)
    CreateObject('HZEF_GuardLoop', 0)
    sprite('hz045_02', 3)
    loopRest()
    label(0)
    sprite('hz045_04', 3)
    sprite('hz045_03', 3)
    sprite('hz045_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('hz045_01', 3)
    sprite('hz045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('hz045_05', 3)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz045_04', 3)
    sprite('hz045_03', 3)
    sprite('hz045_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('hz045_01', 3)
    sprite('hz045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('hz090_00', 2)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    sprite('hz090_01', 2)
    sprite('hz090_02', 1)
    SetCommonActionMark(1)
    sprite('hz090_03', 6)
    sprite('hz090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('hz091_00', 2)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    sprite('hz091_01', 2)
    sprite('hz091_02', 1)
    SetCommonActionMark(1)
    sprite('hz091_03', 6)
    sprite('hz091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('hz092_00', 2)
    CreateObject('HZEF_HeavyGuardLoop', 0)
    sprite('hz092_01', 2)
    sprite('hz092_02', 1)
    SetCommonActionMark(1)
    sprite('hz092_03', 6)
    sprite('hz092_04', 6)


@State
def CmnActAirTurn():
    sprite('hz025_00', 3)
    sprite('hz025_01', 3)
    sprite('hz025_02', 3)


@State
def CmnActLockWait():
    sprite('hz040_02', 1)
    sprite('hz040_01', 3)
    sprite('hz040_00', 3)


@State
def CmnActLockReject():
    sprite('hz312_00', 2)
    sprite('hz312_01', 3)
    sprite('hz312_02', 3)
    sprite('hz312_03', 5)
    sprite('hz312_04', 5)
    sprite('hz312_05', 3)
    sprite('hz312_06', 4)
    sprite('hz312_07', 4)
    sprite('hz312_08', 3)
    sprite('hz312_09', 3)


@State
def CmnActAirLockWait():
    sprite('hz045_02', 1)
    sprite('hz045_01', 3)
    sprite('hz045_00', 3)


@State
def CmnActAirLockReject():
    sprite('hz322_01', 3)
    sprite('hz322_02', 3)
    sprite('hz322_03', 3)
    sprite('hz322_04', 5)
    sprite('hz322_05', 5)
    sprite('hz322_05', 4)
    sprite('hz322_06', 4)
    sprite('hz322_07', 3)
    sprite('hz322_08', 3)


@State
def CmnActLandSpin():
    sprite('hz071_00', 4)
    sprite('hz071_01', 4)
    label(0)
    sprite('hz071_02', 2)
    sprite('hz071_03', 2)
    sprite('hz071_04', 2)
    sprite('hz071_05', 2)
    sprite('hz071_06', 2)
    sprite('hz071_07', 2)
    sprite('hz071_08', 2)
    sprite('hz071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('hz071_10', 6)
    sprite('hz071_11', 5)
    sprite('hz071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('hz071_02', 2)
    sprite('hz071_03', 2)
    sprite('hz071_04', 2)
    sprite('hz071_05', 2)
    sprite('hz071_06', 2)
    sprite('hz071_07', 2)
    sprite('hz071_08', 2)
    sprite('hz071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('hz077_00', 2)
    sprite('hz077_01', 2)
    sprite('hz077_00ex01', 2)
    sprite('hz077_01ex01', 2)
    sprite('hz077_00ex02', 2)
    sprite('hz077_01ex02', 2)
    sprite('hz077_00ex03', 2)
    sprite('hz077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('hz077_02', 4)
    label(0)
    sprite('hz077_03', 3)
    sprite('hz077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('hz077_05', 5)
    sprite('hz077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('hz060_07', 4)
    sprite('hz060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('hz060_11', 5)
    sprite('hz060_12', 4)


@State
def CmnActBurstBegin():
    sprite('hz331_00', 2)
    sprite('hz331_01', 2)
    label(0)
    sprite('hz331_02', 3)
    sprite('hz331_03', 3)
    sprite('hz331_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('hz331_05', 2)
    label(0)
    sprite('hz331_06', 3)
    sprite('hz331_07', 3)
    sprite('hz331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('hz331_09', 3)
    sprite('hz331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('hz331_11', 2)
    sprite('hz331_12', 2)
    label(0)
    sprite('hz331_02', 3)
    sprite('hz331_03', 2)
    sprite('hz331_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('hz331_05', 2)
    label(0)
    sprite('hz331_06', 2)
    sprite('hz331_07', 2)
    sprite('hz331_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('hz331_13', 3)
    sprite('hz331_14', 3)
    label(0)
    sprite('hz020_07', 4)
    sprite('hz020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('hz333_00', 3)
    sprite('hz333_01', 3)
    sprite('hz333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('hz333_03', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('hz333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('hz333_05', 3)
    sprite('hz333_06', 3)
    sprite('hz333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('hz333_08', 4)
    sprite('hz333_09', 4)
    sprite('hz333_10', 4)


@State
def CmnActAirOverDriveBegin():
    sprite('hz333_11', 3)
    sprite('hz333_12', 3)
    sprite('hz333_13', 3)
    CharacterFlash(16639, 20, 1)
    sprite('hz333_14', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('hz333_15', 3)
    label(0)
    sprite('hz333_05', 3)
    sprite('hz333_06', 3)
    sprite('hz333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('hz333_16', 4)
    sprite('hz333_17', 4)
    sprite('hz333_18', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockJumpCancel(1)
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
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('hz200_00', 1)
    PerInertia(60)
    sprite('hz200_01', 1)
    sprite('hz200_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('hz200_03', 3)
    sprite('hz200_04', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('hz200_05', 3)
    sprite('hz200_06', 3)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(550)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
    sprite('hz201_00', 3)
    sprite('hz201_01', 2)
    sprite('hz201_02', 2)
    sprite('hz201_03', 3)
    CommonSE('003_swing_grap_0_2')
    RandomCommonVoiceline(1)
    sprite('hz201_04', 3)
    Recovery()
    Unknown2063()
    sprite('hz201_05', 3)
    sprite('hz201_06', 3)
    sprite('hz201_07', 3)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(450)
        SingleProration(1)
        UseSlashHitspark(1)
        AirPushbackX(4000)
        AirPushbackY(22000)
        PushbackX(12000)
        StayAfterMovement(1, 0)
        HitJumpCancel(1)
        Hitstop(5)
        AirUntechableTime(21)
        HitAirUnblockable(3)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
    sprite('hz202_00', 2)
    sprite('hz202_01', 2)
    sprite('hz202_02', 1)
    CreateObject('EffKnifeSignal', 0)
    CreateObject('EffKnifeSignal', 1)
    sprite('hz202_03', 2)
    sprite('hz202_04', 2)
    sprite('hz202_05', 1)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    RandomCommonVoiceline(2)
    CreateObject('Eff5CZanzo', -1)
    sprite('hz202_05', 1)
    StartMultihit()
    sprite('hz202_06', 6)
    RefreshMultihit()
    sprite('hz202_07', 4)
    Recovery()
    Unknown2063()
    sprite('hz202_08', 4)
    sprite('hz202_09', 4)
    sprite('hz202_10', 4)
    sprite('hz202_11', 3)
    sprite('hz202_12', 4)
    sprite('hz202_13', 5)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('hz230_00', 1)
    PerInertia(60)
    sprite('hz230_01', 2)
    sprite('hz230_02', 2)
    sprite('hz230_03', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('hz230_04', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('hz230_05', 4)
    sprite('hz230_06', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(550)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
    sprite('hz231_00', 3)
    sprite('hz231_01', 3)
    sprite('hz231_02', 3)
    sprite('hz231_03', 2)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_2')
    sprite('hz231_04', 2)
    Recovery()
    Unknown2063()
    sprite('hz231_05', 2)
    sprite('hz231_06', 3)
    sprite('hz231_07', 3)
    sprite('hz231_08', 3)
    sprite('hz231_09', 4)
    WhiffFWalkCancel(1)
    WhiffFDashCancel(1)
    WhiffBWalkCancel(1)
    WhiffBDashCancel(1)
    WhiffJumpCancel(1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchingTurnCancel(1)
    WhiffCrouchBlockCancel(1)
    WhiffBlockCancel(1)
    WhiffBarrierCancel2(1)
    EnablePreGuard(1)
    WhiffOverdriveCancel(1)
    sprite('hz231_10', 3)
    sprite('hz231_11', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        AirUntechableTime(25)
        AirPushbackX(9000)
        AirPushbackY(36000)
        CHAirUntechableTime(48)
        CHGroundedHitstunAnimation(1)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockJumpCancel(1)
    sprite('hz232_00', 5)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz232_01', 2)
    sprite('hz232_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('hz232_03', 2)
    RandomCommonVoiceline(2)
    sprite('hz232_04', 1)
    StartMultihit()
    sprite('hz232_04', 3)
    CreateObject('Eff2CZanzo', -1)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    sprite('hz232_04', 1)
    setInvincible(0)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('hz232_05', 4)
    sprite('hz232_06', 4)
    sprite('hz232_07', 4)
    sprite('hz232_08', 4)
    sprite('hz232_09', 4)
    sprite('hz232_10', 4)
    sprite('hz232_11', 4)
    WhiffFWalkCancel(1)
    WhiffFDashCancel(1)
    WhiffBWalkCancel(1)
    WhiffBDashCancel(1)
    WhiffJumpCancel(1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchingTurnCancel(1)
    WhiffCrouchBlockCancel(1)
    WhiffBlockCancel(1)
    WhiffBarrierCancel2(1)
    EnablePreGuard(1)
    WhiffOverdriveCancel(1)
    sprite('hz232_12', 4)
    sprite('hz232_13', 4)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(840)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        UseSlashHitspark(1)
        AirPushbackY(18000)
        AttackP1(90)
        AirUntechableTime(40)
        CHHardKnockdown(1)
        EnableEmergencyTechAirHit(1)
    sprite('hz240_00', 3)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz240_01', 3)
    sprite('hz240_02', 3)
    sprite('hz240_03', 3)
    sprite('hz240_04', 1)
    StartMultihit()
    RandomCommonVoiceline(2)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    sprite('hz240_04', 4)
    CreateObject('Eff3CZanzo', -1)
    sprite('hz240_05', 2)
    Recovery()
    Unknown2063()
    sprite('hz240_06', 2)
    sprite('hz240_07', 2)
    sprite('hz240_08', 3)
    sprite('hz240_09', 3)
    sprite('hz240_10', 3)
    sprite('hz240_11', 3)
    sprite('hz240_12', 3)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        BonusProration(110)
        HitOverhead(2)
        AirPushbackY(-20000)
        HardKnockdown(1)
        GroundedHitstunAnimation(3)
        PushbackX(12000)
        StarterRating(2)
        HitOrBlockCancel('UltimateAssault')
        HitOrBlockCancel('UltimateAssault_OD')
        HitOrBlockCancel('UltimateShot')
        HitOrBlockCancel('UltimateShot_OD')
        HitOrBlockCancel('AstralHeat')
        SpecialCancel(0)
    sprite('hz210_00', 4)
    sprite('hz210_01', 3)
    sprite('hz210_02', 3)
    sprite('hz210_03', 4)
    sprite('hz210_04', 5)
    sprite('hz210_05', 1)
    SmartVoiceline('hz108')
    sprite('hz210_06', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('hz210_07', 3)
    sprite('hz210_08', 3)
    Recovery()
    Unknown2063()
    sprite('hz210_09', 3)
    sprite('hz210_10', 3)
    sprite('hz210_11', 2)
    sprite('hz210_12', 2)
    sprite('hz210_13', 2)
    sprite('hz210_14', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        AirHitstunAnimation(11)
        AirPushbackY(-20000)
        HardKnockdown(1)
        CHGroundedHitstunAnimation(2)
        FatalCounter(1)
        HitLow(2)
        PushbackX(12000)
        MoveAttributes(0, 0, 1, 0, 0)
        HitOrBlockCancel('UltimateAssault')
        HitOrBlockCancel('UltimateAssault_OD')
        HitOrBlockCancel('UltimateShot')
        HitOrBlockCancel('UltimateShot_OD')
        HitOrBlockCancel('AstralHeat')
        SpecialCancel(0)
    sprite('hz211_00', 3)
    sprite('hz211_01', 3)
    sprite('hz211_02', 4)
    sprite('hz211_03', 5)
    sprite('hz211_04', 2)
    sprite('hz211_05', 2)
    SmartVoiceline('hz109')
    sprite('hz211_06', 2)
    physicsXImpulse(15000)
    sprite('hz211_07', 3)
    CommonSE('004_swing_grap_1_1')
    physicsXImpulse(10000)
    sprite('hz211_08', 3)
    physicsXImpulse(0)
    sprite('hz211_09', 3)
    Recovery()
    Unknown2063()
    sprite('hz211_10', 3)
    sprite('hz211_11', 3)
    sprite('hz211_12', 2)
    sprite('hz211_13', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(510)
        AttackP2(84)
        SingleProration(1)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        HardKnockdown(1)
        Hitstop(0)
        PushbackX(12000)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 0, 0, 1, 0)
        HitAirUnblockable(0)
        UseSlashHitspark(1)
        HitsparkSize(600)
        AttackOff()
        SpecialCancel(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            BeginBuffer('NmlAtk5D_Easy')
            BeginBuffer('NmlAtk4D_Easy')
            BeginBuffer('NmlAtk6D_Easy')
            BeginBuffer('NmlAtk2D_Easy')
    sprite('hz212_00', 2)
    sprite('hz212_01', 2)
    sprite('hz212_02', 2)
    sprite('hz212_03', 3)
    sprite('hz212_04', 4)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz212_05', 3)
    sprite('hz212_06', 3)
    EndMomentum(1)
    physicsYImpulse(13000)
    physicsXImpulse(-20000)
    SetAcceleration(400)
    EndYPhysicsImpulse()
    RandomCommonVoiceline(2)
    uponSendToLabel(LANDING, 1)
    sprite('hz212_07', 3)
    CreateObject('ShotKnifeObj', 0)
    ObjectHitbox(1)
    CreateObject('ShotKnife', 0)
    CommonSE('007_swing_knife_0')
    CommonSE('004_swing_grap_1_0')
    RefreshMultihit()
    sprite('hz212_08', 3)
    sprite('hz212_09', 3)
    RefreshMultihit()
    sprite('hz212_10', 3)
    sprite('hz212_11', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    AirPushbackX(8000)
    HardKnockdown(0)
    GroundBounce(1)
    sprite('hz212_11', 32767)
    label(1)
    sprite('hz212_12', 2)
    AttackOff()
    EndMomentum(1)
    Recovery()
    Unknown2063()
    BufferedOrPressedGoto('NmlAtk5D_Easy')
    BufferedOrPressedGoto('NmlAtk4D_Easy')
    BufferedOrPressedGoto('NmlAtk6D_Easy')
    BufferedOrPressedGoto('NmlAtk2D_Easy')
    sprite('hz212_13', 2)
    sprite('hz212_14', 2)
    sprite('hz212_15', 2)
    sprite('hz212_16', 2)
    DisallowGoto('NmlAtk5D_Easy')
    DisallowGoto('NmlAtk4D_Easy')
    DisallowGoto('NmlAtk6D_Easy')
    DisallowGoto('NmlAtk2D_Easy')
    sprite('hz212_17', 2)
    sprite('hz212_18', 2)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAirThrow')
    sprite('hz250_00', 2)
    sprite('hz250_01', 2)
    sprite('hz250_02', 2)
    sprite('hz250_03', 3)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('hz250_04', 3)
    Recovery()
    Unknown2063()
    sprite('hz250_05', 3)
    sprite('hz250_06', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        AirUntechableTime(16)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
    sprite('hz251_00', 3)
    sprite('hz251_01', 3)
    sprite('hz251_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_1')
    sprite('hz251_03', 4)
    sprite('hz251_03', 2)
    StartMultihit()
    sprite('hz251_04', 2)
    sprite('hz251_05', 4)
    Recovery()
    Unknown2063()
    sprite('hz251_06', 4)
    sprite('hz251_07', 3)
    sprite('hz251_08', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        UseSlashHitspark(1)
        Hitstop(5)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C_2')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')
        PushGravity()
    sprite('hz252_00', 1)
    sprite('hz252_01', 1)
    sprite('hz252_02', 2)
    BeginBuffer('NmlAtkAIR5C_2')
    sprite('hz252_03', 2)
    CreateObject('EffKnifeSignal', 0)
    CreateObject('EffKnifeSignal', 1)
    sprite('hz252_04', 2)
    RandomCommonVoiceline(2)
    sprite('hz252_05', 1)
    StartMultihit()
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz252_05', 2)
    CreateObject('Eff8CZanzo', 0)
    sprite('hz252_06', 2)
    BufferedOrPressedGoto('NmlAtkAIR5C_2')
    Recovery()
    Unknown2063()
    sprite('hz252_36', 2)
    DisallowGoto('NmlAtkAIR5C_2')
    sprite('hz252_29', 3)
    sprite('hz252_30', 2)
    sprite('hz252_31', 2)
    sprite('hz252_32', 3)
    sprite('hz252_33', 3)
    sprite('hz252_34', 3)
    sprite('hz252_35', 3)


@State
def NmlAtkAIR5C_2():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(400)
        AttackP1(80)
        AttackP2(90)
        AirHitstunAnimation(10)
        Hitstop(5)
        EnemyHitstopAddition(0, 5, 5)
        UseSlashHitspark(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C_3')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            YAccel(50)
            PerGravity(50)
    sprite('hz252_07', 2)
    sprite('hz252_08', 1)
    BeginBuffer('NmlAtkAIR5C_3')
    RandomCommonVoiceline(2)
    sprite('hz252_09', 1)
    StartMultihit()
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz252_09', 2)
    CreateObject('Eff8CZanzo_2', 0)
    sprite('hz252_10', 2)
    Recovery()
    Unknown2063()
    sprite('hz252_37', 2)
    BufferedOrPressedGoto('NmlAtkAIR5C_3')
    sprite('hz252_29', 3)
    DisallowGoto('NmlAtkAIR5C_3')
    sprite('hz252_30', 2)
    PopGravity()
    sprite('hz252_31', 2)
    sprite('hz252_32', 3)
    sprite('hz252_33', 3)
    sprite('hz252_34', 3)
    sprite('hz252_35', 3)


@State
def NmlAtkAIR5C_3():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(400)
        AttackP1(80)
        AttackP2(90)
        AirPushbackY(20000)
        Hitstop(5)
        EnemyHitstopAddition(0, 5, 5)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5C_4')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            XImpulseAcceleration(80)
            YAccel(50)
            PerGravity(50)
    sprite('hz252_11', 1)
    sprite('hz252_12', 1)
    sprite('hz252_13', 1)
    BeginBuffer('NmlAtkAIR5C_4')
    RandomCommonVoiceline(2)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz252_14', 2)
    CreateObject('Eff8CZanzo_3', 0)
    sprite('hz252_15', 2)
    BufferedOrPressedGoto('NmlAtkAIR5C_4')
    Recovery()
    Unknown2063()
    sprite('hz252_38', 2)
    DisallowGoto('NmlAtkAIR5C_4')
    sprite('hz252_29', 3)
    PopGravity()
    sprite('hz252_30', 2)
    sprite('hz252_31', 2)
    sprite('hz252_32', 3)
    sprite('hz252_33', 3)
    sprite('hz252_34', 3)
    sprite('hz252_35', 3)


@State
def NmlAtkAIR5C_4():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(400)
        AttackP1(80)
        AttackP2(90)
        AirPushbackY(20000)
        Hitstop(5)
        EnemyHitstopAddition(0, 5, 5)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5C_5')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            XImpulseAcceleration(80)
            YAccel(50)
            PerGravity(50)
    sprite('hz252_16', 1)
    sprite('hz252_17', 1)
    sprite('hz252_18', 1)
    BeginBuffer('NmlAtkAIR5C_5')
    sprite('hz252_19', 1)
    RandomCommonVoiceline(2)
    sprite('hz252_20', 1)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz252_21', 3)
    CreateObject('Eff8CZanzo_4', 0)
    sprite('hz252_39', 2)
    BufferedOrPressedGoto('NmlAtkAIR5C_5')
    Recovery()
    Unknown2063()
    sprite('hz252_29', 3)
    DisallowGoto('NmlAtkAIR5C_5')
    sprite('hz252_30', 2)
    PopGravity()
    sprite('hz252_31', 2)
    sprite('hz252_32', 3)
    sprite('hz252_33', 3)
    sprite('hz252_34', 3)
    sprite('hz252_35', 3)


@State
def NmlAtkAIR5C_5():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AttackP2(94)
        AirHitstunAnimation(10)
        UseSlashHitspark(1)
        EnemyHitstopAddition(0, 5, 5)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')
        PopGravity()
    sprite('hz252_22', 1)
    sprite('hz252_23', 1)
    sprite('hz252_24', 1)
    sprite('hz252_25', 1)
    StartMultihit()
    RandomCommonVoiceline(2)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz252_25', 2)
    CreateObject('Eff8CZanzo_5', 0)
    sprite('hz252_26', 2)
    Recovery()
    Unknown2063()
    sprite('hz252_27', 3)
    sprite('hz252_28', 2)
    sprite('hz252_29', 3)
    sprite('hz252_30', 2)
    sprite('hz252_31', 2)
    sprite('hz252_32', 3)
    sprite('hz252_33', 3)
    sprite('hz252_34', 3)
    sprite('hz252_35', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(780)
        AttackP1(80)
        UseSlashHitspark(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAIR4D')
        HitOrBlockCancel('NmlAtkAIR8D')
    sprite('hz253_00', 3)
    sprite('hz253_01', 2)
    sprite('hz253_02', 2)
    sprite('hz253_03', 2)
    sprite('hz253_04', 2)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    sprite('hz253_05', 1)
    RandomCommonVoiceline(2)
    sprite('hz253_06', 1)
    StartMultihit()
    CreateObject('EffAir2CZanzo', 0)
    sprite('hz253_06', 4)
    sprite('hz253_07', 3)
    Recovery()
    Unknown2063()
    sprite('hz253_08', 3)
    sprite('hz253_09', 3)
    sprite('hz253_10', 3)
    sprite('hz253_11', 3)
    sprite('hz253_12', 4)
    sprite('hz253_13', 3)


@Subroutine
def UroborosInit():
    AttackLevel_(1)
    AttackP1(80)
    AttackP2(92)
    PushbackX(8000)
    Blockstun(9)
    Hitstop(3)
    AirPushbackX(6000)
    StrikeProjectileLevel(0)
    ProjectileLevel(1)
    UseSlashHitspark(1)
    HitOverhead(0)
    HitLow(0)
    HitAirUnblockable(0)
    StarterRating(2)
    Unknown12052(1)
    AttackOff()
    MoveAttributes(0, 0, 0, 1, 0)
    if SLOT_OverdriveTimer:
        AttackLevel_(5)
        DamageMultiplier(200)
        Blockstun(9)
        Hitstop(8)
        EnemyHitstopAddition(15, 20, 20)
        AirUntechableTime(28)
        Hitstun(14)
        SLOT_51 = 1

    def upon_OPPONENT_HIT():
        SLOT_31 = 2
        SLOT_32 = 0

    def upon_OPPONENT_HIT_OR_BLOCK():
        clearUponHandler(39)
        clearUponHandler(OPPONENT_HIT_OR_BLOCK)
        ObjectUpon(FALLING, 38)
        AttackOff()
        SetActionMark(1)

    def upon_39():
        clearUponHandler(39)
        clearUponHandler(OPPONENT_HIT_OR_BLOCK)
        ObjectUpon(FALLING, 38)
        AttackOff()
        SetActionMark(1)
    SetActionMark(0)

    def upon_EVERY_FRAME():
        if SLOT_2:
            SetActionMark(0)
            clearUponHandler(EVERY_FRAME)
            sendToLabel(0)
        if SLOT_YDistanceFromFloor >= 3000000:
            SLOT_YDistanceFromFloor = 3000000
    WhiffCancel('DriveJump6')
    WhiffCancel('DriveJump4')
    WhiffCancel('DriveJump8')


@Subroutine
def UroborosPowerUp():
    if not SLOT_51:
        AttackLevel_(5)
        DamageMultiplier(200)
        Blockstun(9)
        Hitstop(8)
        EnemyHitstopAddition(0, 20, 20)
        AirUntechableTime(28)
        Hitstun(14)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Damage(250)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtk5DStop')
        HitOrBlockCancel('NmlAtk5DStop')
    sprite('hz203_00', 3)
    sprite('hz203_01', 3)
    sprite('hz203_02', 3)
    RandomCommonVoiceline(3)
    sprite('hz203_03', 3)
    sprite('hz203_04', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 109)
    RegisterObject(4, 1)
    ObjectUpon2(4, 0, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    CommonSE('004_swing_grap_1_0')
    sprite('hz203_05', 3)
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz203_06', 2)
    sprite('hz203_07', 2)
    callSubroutine('UroborosPowerUp')
    sprite('hz203_08', 2)
    sprite('hz203_06', 2)
    sprite('hz203_07', 2)
    sprite('hz203_08', 2)
    label(0)
    sprite('hz203_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtk5DStop')
    sprite('hz203_07', 3)
    sprite('hz203_08', 3)
    AttackOff()
    Recovery()
    sprite('hz203_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtk5DEnd')


@State
def NmlAtk5DEnd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
    sprite('hz203_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz203_10', 5)
    sprite('hz203_11', 3)
    sprite('hz203_12', 3)
    sprite('hz203_13', 3)


@State
def NmlAtk5DStop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
    sprite('hz203_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz203_10', 5)
    sprite('hz203_11', 3)
    sprite('hz203_12', 3)
    sprite('hz203_13', 3)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Damage(400)
        BonusProration(110)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtk2DStop')
        HitOrBlockCancel('NmlAtk2DStop')
    sprite('hz233_00', 2)
    sprite('hz233_01', 2)
    sprite('hz233_02', 2)
    RandomCommonVoiceline(3)
    sprite('hz233_03', 2)
    sprite('hz233_04', 2)
    CommonSE('004_swing_grap_1_0')
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 109)
    RegisterObject(4, 1)
    ObjectUpon2(4, 3, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)

    def RunOnObject_1():
        AddX(-80000)
        AddY(-160000)
    sprite('hz233_05', 2)
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz233_06', 2)
    callSubroutine('UroborosPowerUp')
    sprite('hz233_07', 2)
    sprite('hz233_08', 2)
    sprite('hz233_06', 2)
    sprite('hz233_07', 2)
    sprite('hz233_08', 2)
    label(0)
    sprite('hz233_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtk2DStop')
    sprite('hz233_07', 3)
    sprite('hz233_08', 3)
    sprite('hz233_06', 3)
    AttackOff()
    Recovery()
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtk2DEnd')


@State
def NmlAtk2DEnd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
    sprite('hz233_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz233_10', 3)
    sprite('hz233_11', 3)
    sprite('hz233_12', 3)
    sprite('hz233_13', 3)


@State
def NmlAtk2DStop():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
    sprite('hz233_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz233_10', 3)
    sprite('hz233_11', 3)
    sprite('hz233_12', 3)
    sprite('hz233_13', 3)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Damage(300)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtk6DStop')
        HitOrBlockCancel('NmlAtk6DStop')
    sprite('hz213_00', 3)
    sprite('hz213_01', 3)
    sprite('hz213_02', 3)
    RandomCommonVoiceline(3)
    sprite('hz213_03', 3)
    sprite('hz213_04', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 109)
    RegisterObject(4, 1)
    ObjectUpon2(4, 1, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    sprite('hz213_05', 3)
    CommonSE('004_swing_grap_1_0')
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz213_06', 2)
    sprite('hz213_07', 2)
    callSubroutine('UroborosPowerUp')
    sprite('hz213_08', 2)
    sprite('hz213_06', 3)
    sprite('hz213_07', 3)
    sprite('hz213_08', 3)
    label(0)
    sprite('hz213_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtk6DStop')
    sprite('hz213_07', 3)
    sprite('hz213_08', 3)
    AttackOff()
    Recovery()
    sprite('hz213_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtk6DEnd')


@State
def NmlAtk4D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Damage(300)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtk6DStop')
        HitOrBlockCancel('NmlAtk6DStop')
    sprite('hz213_00', 2)
    sprite('hz213_01', 2)
    sprite('hz213_02', 2)
    RandomCommonVoiceline(3)
    sprite('hz213_03', 3)
    sprite('hz213_04', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 109)
    RegisterObject(4, 1)
    ObjectUpon2(4, 2, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    sprite('hz213_05', 3)
    CommonSE('004_swing_grap_1_0')
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz213_06', 2)
    callSubroutine('UroborosPowerUp')
    sprite('hz213_07', 2)
    sprite('hz213_08', 2)
    sprite('hz213_06', 3)
    sprite('hz213_07', 3)
    sprite('hz213_08', 3)
    label(0)
    sprite('hz213_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtk6DStop')
    sprite('hz213_07', 3)
    sprite('hz213_08', 3)
    AttackOff()
    Recovery()
    sprite('hz213_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtk6DEnd')


@State
def NmlAtk6DEnd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
    sprite('hz213_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz213_10', 3)
    sprite('hz213_11', 3)
    sprite('hz213_12', 3)
    sprite('hz213_13', 3)


@State
def NmlAtk6DStop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
    sprite('hz213_09', 3)
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz213_10', 3)
    sprite('hz213_11', 3)
    sprite('hz213_12', 3)
    sprite('hz213_13', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(250)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtkAIR5DStop')
        HitOrBlockCancel('NmlAtkAIR5DStop')
    sprite('hz254_00', 3)
    sprite('hz254_01', 3)
    RandomCommonVoiceline(3)
    sprite('hz254_02', 3)
    sprite('hz254_03', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 0)
    RegisterObject(4, 1)
    ObjectUpon2(4, 4, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(100)
    sprite('hz254_04', 3)
    CommonSE('004_swing_grap_1_0')
    PerGravity(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)
    PerGravity(90)
    callSubroutine('UroborosPowerUp')
    sprite('hz254_06', 2)
    PerGravity(90)
    sprite('hz254_07', 2)
    EndMomentum(1)
    sprite('hz254_08', 2)
    sprite('hz254_06', 2)
    sprite('hz254_07', 2)
    sprite('hz254_08', 2)
    loopRest()
    label(0)
    sprite('hz254_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtkAIR5DStop')
    sprite('hz254_07', 3)
    sprite('hz254_08', 3)
    AttackOff()
    Recovery()
    sprite('hz254_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtkAIR5DEnd')


@State
def NmlAtkAIR2D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(250)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtkAIR5DStop')
        HitOrBlockCancel('NmlAtkAIR5DStop')
    sprite('hz254_00', 3)
    sprite('hz254_01', 3)
    RandomCommonVoiceline(3)
    sprite('hz254_02', 3)
    sprite('hz254_03', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 4)
    RegisterObject(4, 1)
    ObjectUpon2(4, 8, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(100)
    sprite('hz254_04', 3)
    CommonSE('004_swing_grap_1_0')
    PerGravity(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)
    PerGravity(90)
    callSubroutine('UroborosPowerUp')
    sprite('hz254_06', 2)
    PerGravity(90)
    sprite('hz254_07', 2)
    EndMomentum(1)
    sprite('hz254_08', 2)
    sprite('hz254_06', 2)
    sprite('hz254_07', 2)
    sprite('hz254_08', 2)
    loopRest()
    label(0)
    sprite('hz254_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtkAIR5DStop')
    sprite('hz254_07', 3)
    sprite('hz254_08', 3)
    AttackOff()
    Recovery()
    sprite('hz254_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtkAIR5DEnd')


@State
def NmlAtkAIR4D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(250)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtkAIR5DStop')
        HitOrBlockCancel('NmlAtkAIR5DStop')
    sprite('hz254_00', 3)
    sprite('hz254_01', 3)
    RandomCommonVoiceline(3)
    sprite('hz254_02', 3)
    sprite('hz254_03', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 3)
    RegisterObject(4, 1)
    ObjectUpon2(4, 7, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(100)
    sprite('hz254_04', 3)
    CommonSE('004_swing_grap_1_0')
    PerGravity(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)
    PerGravity(90)
    callSubroutine('UroborosPowerUp')
    sprite('hz254_06', 2)
    PerGravity(90)
    sprite('hz254_07', 2)
    EndMomentum(1)
    sprite('hz254_08', 2)
    sprite('hz254_06', 2)
    sprite('hz254_07', 2)
    sprite('hz254_08', 2)
    loopRest()
    label(0)
    sprite('hz254_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtkAIR5DStop')
    sprite('hz254_07', 3)
    sprite('hz254_08', 3)
    AttackOff()
    Recovery()
    sprite('hz254_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtkAIR5DEnd')


@State
def NmlAtkAIR6D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(250)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtkAIR5DStop')
        HitOrBlockCancel('NmlAtkAIR5DStop')
    sprite('hz254_00', 3)
    sprite('hz254_01', 3)
    RandomCommonVoiceline(3)
    sprite('hz254_02', 3)
    sprite('hz254_03', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 2)
    RegisterObject(4, 1)
    ObjectUpon2(4, 6, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(100)
    sprite('hz254_04', 3)
    CommonSE('004_swing_grap_1_0')
    PerGravity(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)
    PerGravity(90)
    callSubroutine('UroborosPowerUp')
    sprite('hz254_06', 2)
    PerGravity(90)
    sprite('hz254_07', 2)
    EndMomentum(1)
    sprite('hz254_08', 2)
    sprite('hz254_06', 2)
    sprite('hz254_07', 2)
    sprite('hz254_08', 2)
    loopRest()
    label(0)
    sprite('hz254_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtkAIR5DStop')
    sprite('hz254_07', 3)
    sprite('hz254_08', 3)
    AttackOff()
    Recovery()
    sprite('hz254_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtkAIR5DEnd')


@State
def NmlAtkAIR8D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(400)
        callSubroutine('UroborosInit')
        WhiffCancel('NmlAtkAIR5DStop')
        HitOrBlockCancel('NmlAtkAIR5DStop')
    sprite('hz254_00', 3)
    sprite('hz254_01', 3)
    RandomCommonVoiceline(3)
    sprite('hz254_02', 3)
    sprite('hz254_03', 3)
    SLOT_54 = 1
    DeleteObject(4)
    CreateObject('Kusari', 1)
    RegisterObject(4, 1)
    ObjectUpon2(4, 5, 0)
    ObjectHitbox(4)
    CreateObject('ExBodyAura', -1)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(100)
    sprite('hz254_04', 3)
    CommonSE('004_swing_grap_1_0')
    PerGravity(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)
    PerGravity(90)
    callSubroutine('UroborosPowerUp')
    sprite('hz254_06', 1)
    PerGravity(90)
    sprite('hz254_06', 1)
    sprite('hz254_07', 2)
    EndMomentum(1)
    sprite('hz254_08', 2)
    sprite('hz254_06', 2)
    sprite('hz254_07', 2)
    sprite('hz254_08', 2)
    loopRest()
    label(0)
    sprite('hz254_06', 3)
    clearUponHandler(39)
    ObjectUpon(FALLING, 40)
    EndMomentum(1)
    PreventWhiffCancel('NmlAtkAIR5DStop')
    sprite('hz254_07', 3)
    sprite('hz254_08', 3)
    AttackOff()
    Recovery()
    sprite('hz254_06', 3)
    loopRest()
    label(1)
    sprite('keep', 1)
    PopSpeedX()
    PopSpeedY()
    EndYPhysicsImpulse()
    WhiffCancelEnable(0)
    AttackOff()
    enterState('NmlAtkAIR5DEnd')


@State
def NmlAtkAIR5DEnd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
    sprite('hz254_09', 6)
    EndYPhysicsImpulse()
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz254_10', 6)
    sprite('hz254_11', 6)
    sprite('hz254_12', 5)
    sprite('hz254_13', 5)


@State
def NmlAtkAIR5DStop():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        EndMomentum(1)
        AttackOff()
        Recovery()
        SLOT_54 = 1
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
    sprite('hz254_09', 4)
    EndYPhysicsImpulse()
    ObjectUpon(FALLING, 32)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz254_10', 4)
    sprite('hz254_11', 4)
    sprite('hz254_12', 3)
    sprite('hz254_13', 3)


@State
def DriveJump6():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(40)
                YAccel(60)
                setGravity(2000)

        def upon_EVERY_FRAME():
            CallPrivateFunction('KusariJumpIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
        SLOT_52 = 12
        SLOT_53 = 16
        ObjectUpon(FALLING, 33)
        ObjectUpon(FALLING, 39)
        SLOT_54 = 1
        TriggerUponForState('ExPortal', 32)
    EndMomentum(1)
    if PreviousStateCheck('NmlAtk6D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk4D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk5D'):
        conditionalSendToLabel(1)
    if PreviousStateCheck('NmlAtk2D'):
        conditionalSendToLabel(2)
    gotoLabel(3)
    label(0)
    Unknown23130(25650, 8, 2)
    sprite('hz408_30', 2)
    SmartVoiceline('hz209')
    sprite('hz408_31', 2)
    sprite('hz408_02', 2)
    loopRest()
    gotoLabel(10)
    label(1)
    Unknown23130(25650, 8, 2)
    sprite('hz408_32', 2)
    SmartVoiceline('hz209')
    sprite('hz408_33', 2)
    CommonSE('011_spin_0')
    sprite('hz408_02', 2)
    loopRest()
    gotoLabel(10)
    label(2)
    Unknown23130(25650, 8, 2)
    sprite('hz408_34', 2)
    SmartVoiceline('hz209')
    sprite('hz408_35', 2)
    sprite('hz408_02', 2)
    loopRest()
    gotoLabel(10)
    label(3)
    Unknown23130(25650, 8, 2)
    sprite('hz408_00', 2)
    SmartVoiceline('hz209')
    sprite('hz408_01', 2)
    sprite('hz408_02', 2)
    loopRest()
    gotoLabel(10)
    label(10)
    sprite('keep', 1)
    CallPrivateFunction('KusariJumpSpeed6', 0, 600, 0, 100, 0, 0, 0, 0)
    EnableAfterimage(1)
    SetActionMark(1)
    TriggerUponForState('ExBodyAura', 32)
    ConstantAlphaModifier(20)
    label(108)
    sprite('hz408_05', 3)
    sprite('hz408_06', 3)
    sprite('hz408_07', 3)
    loopRest()
    gotoLabel(108)
    label(109)
    sprite('hz408_10', 3)
    sprite('hz408_11', 3)
    sprite('hz408_12', 3)
    loopRest()
    gotoLabel(109)
    label(106)
    sprite('hz408_15', 3)
    sprite('hz408_16', 3)
    sprite('hz408_17', 3)
    loopRest()
    gotoLabel(106)
    label(103)
    sprite('hz408_20', 3)
    sprite('hz408_21', 3)
    sprite('hz408_22', 3)
    loopRest()
    gotoLabel(103)
    label(102)
    sprite('hz408_25', 3)
    sprite('hz408_26', 3)
    sprite('hz408_27', 3)
    loopRest()
    gotoLabel(102)
    label(208)
    sprite('hz408_08', 3)
    sprite('hz408_09', 3)
    loopRest()
    ExitState()
    label(209)
    sprite('hz408_13', 3)
    sprite('hz408_14', 3)
    loopRest()
    ExitState()
    label(206)
    sprite('hz408_18', 3)
    sprite('hz408_19', 3)
    loopRest()
    ExitState()
    label(203)
    sprite('hz408_23', 3)
    sprite('hz408_24', 3)
    loopRest()
    ExitState()
    label(202)
    sprite('hz408_28', 3)
    sprite('hz408_29', 3)
    loopRest()
    ExitState()


@State
def DriveJump4():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()

        def upon_EVERY_FRAME():
            CallPrivateFunction('KusariJumpIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
        SLOT_52 = 27
        SLOT_53 = 23
        EnableAfterimage(1)
        ObjectUpon(FALLING, 33)
        ObjectUpon(FALLING, 39)
        SetXCollisionFromOrigin(20)
        SLOT_54 = 1
        TriggerUponForState('ExPortal', 32)
    EndMomentum(1)
    if PreviousStateCheck('NmlAtk6D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk4D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk5D'):
        conditionalSendToLabel(1)
    if PreviousStateCheck('NmlAtk2D'):
        conditionalSendToLabel(2)
    gotoLabel(3)
    label(0)
    Unknown23130(25650, 16, 2)
    sprite('hz408_30', 2)
    SmartVoiceline('hz211')
    sprite('hz408_31', 2)
    sprite('hz408_02', 2)
    physicsXImpulse(-1250)
    physicsYImpulse(2500)
    setGravity(-600)
    sprite('hz408_03', 2)
    sprite('hz408_04', 8)
    loopRest()
    gotoLabel(10)
    label(1)
    Unknown23130(25650, 16, 2)
    sprite('hz408_32', 2)
    SmartVoiceline('hz211')
    sprite('hz408_33', 2)
    CommonSE('011_spin_0')
    sprite('hz408_02', 2)
    physicsXImpulse(-1250)
    physicsYImpulse(2500)
    setGravity(-600)
    sprite('hz408_03', 2)
    sprite('hz408_04', 8)
    loopRest()
    gotoLabel(10)
    label(2)
    Unknown23130(25650, 16, 2)
    sprite('hz408_34', 2)
    SmartVoiceline('hz211')
    sprite('hz408_35', 2)
    sprite('hz408_02', 2)
    physicsXImpulse(-1250)
    physicsYImpulse(2500)
    setGravity(-600)
    sprite('hz408_03', 2)
    sprite('hz408_04', 8)
    loopRest()
    gotoLabel(10)
    label(3)
    Unknown23130(25650, 16, 2)
    sprite('hz408_00', 2)
    SmartVoiceline('hz211')
    sprite('hz408_01', 2)
    sprite('hz408_02', 2)
    physicsXImpulse(-1250)
    physicsYImpulse(2500)
    setGravity(-600)
    sprite('hz408_03', 2)
    sprite('hz408_04', 8)
    loopRest()
    gotoLabel(10)
    label(10)
    sprite('keep', 1)
    CallPrivateFunction('KusariJumpSpeed4', 0, 7, 0, 0, 0, 0, 0, 0)
    EnableAfterimage(1)
    EnableCollision(0)
    SetActionMark(1)
    TriggerUponForState('ExBodyAura', 32)
    setGravity(2500)
    label(108)
    sprite('hz408_05', 3)
    sprite('hz408_06', 3)
    sprite('hz408_07', 3)
    loopRest()
    gotoLabel(108)
    label(109)
    sprite('hz408_10', 3)
    sprite('hz408_11', 3)
    sprite('hz408_12', 3)
    loopRest()
    gotoLabel(109)
    label(106)
    sprite('hz408_15', 3)
    sprite('hz408_16', 3)
    sprite('hz408_17', 3)
    loopRest()
    gotoLabel(106)
    label(103)
    sprite('hz408_20', 3)
    sprite('hz408_21', 3)
    sprite('hz408_22', 3)
    loopRest()
    gotoLabel(103)
    label(102)
    sprite('hz408_25', 3)
    sprite('hz408_26', 3)
    sprite('hz408_27', 3)
    loopRest()
    gotoLabel(102)
    label(208)
    sprite('hz408_08', 1)
    ForceFaceSprite()
    setGravity(1500)
    XImpulseAcceleration(0)
    YAccel(10)
    sprite('hz408_08', 1)
    ForceFaceSprite()
    sprite('hz408_08', 1)
    ForceFaceSprite()
    sprite('hz408_09', 3)
    loopRest()
    ExitState()
    label(209)
    sprite('hz408_13', 1)
    ForceFaceSprite()
    setGravity(1500)
    XImpulseAcceleration(3)
    YAccel(15)
    sprite('hz408_13', 1)
    ForceFaceSprite()
    sprite('hz408_13', 1)
    ForceFaceSprite()
    sprite('hz408_14', 3)
    loopRest()
    ExitState()
    label(206)
    sprite('hz408_18', 1)
    ForceFaceSprite()
    setGravity(1200)
    XImpulseAcceleration(3)
    YAccel(10)
    sprite('hz408_18', 1)
    ForceFaceSprite()
    sprite('hz408_18', 1)
    ForceFaceSprite()
    sprite('hz408_19', 3)
    loopRest()
    ExitState()
    label(203)
    sprite('hz408_23', 1)
    ForceFaceSprite()
    setGravity(2000)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('hz408_23', 1)
    ForceFaceSprite()
    sprite('hz408_23', 1)
    ForceFaceSprite()
    sprite('hz408_24', 3)
    loopRest()
    ExitState()
    label(202)
    sprite('hz408_28', 1)
    ForceFaceSprite()
    setGravity(2000)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('hz408_28', 1)
    ForceFaceSprite()
    sprite('hz408_28', 1)
    ForceFaceSprite()
    sprite('hz408_29', 3)
    loopRest()
    ExitState()


@State
def DriveJump8():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(50)
                YAccel(50)
                setGravity(2000)

        def upon_EVERY_FRAME():
            CallPrivateFunction('KusariJumpIdling', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_XVelocity <= 1000:
                PerAcceleration(0)
        SLOT_31 = SLOT_31 + -1
        SLOT_32 = 0
        SLOT_52 = 30
        SLOT_53 = 64
        ObjectUpon(FALLING, 33)
        ObjectUpon(FALLING, 39)
        SLOT_54 = 1
        TriggerUponForState('ExPortal', 32)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
    EndMomentum(1)
    if PreviousStateCheck('NmlAtk6D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk4D'):
        conditionalSendToLabel(0)
    if PreviousStateCheck('NmlAtk5D'):
        conditionalSendToLabel(1)
    if PreviousStateCheck('NmlAtk2D'):
        conditionalSendToLabel(2)
    gotoLabel(3)
    label(0)
    Unknown23130(25650, 8, 2)
    sprite('hz408_30', 3)
    SmartVoiceline('hz210')
    sprite('hz408_31', 3)
    loopRest()
    gotoLabel(10)
    label(1)
    Unknown23130(25650, 8, 2)
    sprite('hz408_32', 3)
    SmartVoiceline('hz210')
    sprite('hz408_33', 3)
    CommonSE('011_spin_0')
    loopRest()
    gotoLabel(10)
    label(2)
    Unknown23130(25650, 8, 2)
    sprite('hz408_34', 3)
    SmartVoiceline('hz210')
    sprite('hz408_35', 3)
    loopRest()
    gotoLabel(10)
    label(3)
    Unknown23130(25650, 8, 2)
    sprite('hz408_00', 3)
    SmartVoiceline('hz210')
    sprite('hz408_01', 3)
    loopRest()
    gotoLabel(10)
    label(10)
    sprite('hz408_02', 4)
    EndMomentum(1)
    AddY(10000)
    physicsXImpulse(-40000)
    physicsYImpulse(0)
    setGravity(-5000)
    SetAcceleration(3000)
    TriggerUponForState('ExBodyAura', 32)
    sprite('hz408_03', 4)
    sprite('hz408_04', 2)
    sprite('hz408_04', 1)
    setGravity(0)
    SetAcceleration(0)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('hz408_04', 1)
    SetActionMark(1)
    EndMomentum(1)
    CallPrivateFunction('KusariJumpSpeed6', 0, 750, 0, 100, 0, 0, 0, 1)
    SetAcceleration(-500)
    EnableAfterimage(1)
    setInvincible(0)
    label(108)
    sprite('hz408_36', 3)
    sprite('hz408_37', 3)
    sprite('hz408_38', 3)
    loopRest()
    gotoLabel(108)
    label(109)
    sprite('hz408_41', 3)
    sprite('hz408_42', 3)
    sprite('hz408_43', 3)
    loopRest()
    gotoLabel(109)
    label(106)
    sprite('hz408_46', 3)
    sprite('hz408_47', 3)
    sprite('hz408_48', 3)
    loopRest()
    gotoLabel(106)
    label(103)
    sprite('hz408_51', 3)
    sprite('hz408_52', 3)
    sprite('hz408_53', 3)
    loopRest()
    gotoLabel(103)
    label(102)
    sprite('hz408_56', 3)
    sprite('hz408_57', 3)
    sprite('hz408_58', 3)
    loopRest()
    gotoLabel(102)
    label(208)
    sprite('hz408_39', 3)
    sprite('hz408_40', 3)
    loopRest()
    ExitState()
    label(209)
    sprite('hz408_44', 3)
    sprite('hz408_45', 3)
    loopRest()
    ExitState()
    label(206)
    sprite('hz408_49', 3)
    sprite('hz408_50', 3)
    loopRest()
    ExitState()
    label(203)
    sprite('hz408_54', 3)
    sprite('hz408_55', 3)
    loopRest()
    ExitState()
    label(202)
    sprite('hz408_59', 3)
    sprite('hz408_60', 3)
    loopRest()
    ExitState()


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    if SLOT_45:
        conditionalSendToLabel(1)
    sprite('hz300_00', 3)
    sprite('hz300_00', 3)
    if random_(2, 0, 50):
        Voiceline('hz404')
    else:
        Voiceline('hz405')
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    label(3)
    sprite('hz300_06', 6)
    if SLOT_97:
        conditionalSendToLabel(3)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('hz301_00', 6)
    SmartVoiceline('hz200')
    sprite('hz301_01', 6)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    sprite('hz301_04', 6)
    sprite('hz301_05', 6)
    sprite('hz301_06', 6)
    sprite('hz301_07', 6)
    label(2)
    loopRest()


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('hz201_00', 4)
    sprite('hz201_01', 4)
    sprite('hz201_02', 4)
    sprite('hz201_03', 4)
    CommonSE('003_swing_grap_0_2')
    sprite('hz201_04', 15)
    AttackOff()
    sprite('hz201_05', 6)
    sprite('hz201_06', 6)
    sprite('hz201_07', 6)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        UseSlashHitspark(1)
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
        Blockstun(24)
        HitBackReturnIgnore(1)
        StarterRating(2)

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
    sprite('hz410_00', 3)
    sprite('hz410_00', 1)
    E0EAEffect('GuardCrushWind', 1)
    Voiceline('hz159')
    HeatChange(-2500)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz410_01', 4)
    CharacterFlash(16763080, 8, 2)
    loopRest()
    label(100)
    sprite('hz410_02', 3)
    sprite('hz410_03', 3)
    sprite('hz410_04', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('hz410_05', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('hz410_06', 2)
    sprite('hz410_06', 4)
    CreateObject('Eff410', -1)
    PrivateSE('hzse_08')
    sprite('hz410_07', 1)
    CommonSE('007_swing_knife_0')
    CommonSE('004_swing_grap_1_0')
    sprite('hz410_07', 2)
    StartMultihit()
    EnableAfterimage(0)
    sprite('hz410_08', 3)
    sprite('hz410_09', 3)
    sprite('hz410_10', 3)
    sprite('hz410_11', 3)
    sprite('hz410_12', 3)
    sprite('hz410_13', 3)
    sprite('hz410_14', 3)
    sprite('hz410_15', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('hz310_00', 2)
    CommonSE('010_swing_sword_0')
    sprite('hz310_01', 4)
    sprite('hz310_02', 3)
    sprite('hz310_03', 4)
    sprite('hz310_04', 4)
    SmartVoiceline('hz155')
    sprite('hz310_05', 7)
    sprite('hz310_06', 4)
    sprite('hz310_07', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(9000)
        AirPushbackY(45000)
        AirUntechableTime(70)
        StayAfterMovement(1, 0)
        Hitstop(3)
        SpecialCancel(1)
        StarterRating(2)
    sprite('hz310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('hz311_00', 5)
    SmartVoiceline('hz153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_01', 8)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_02', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_04', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_05', 2)
    CommonSE('006_swing_blade_1')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz311_06', 3)
    sprite('hz311_07', 3)
    sprite('hz311_08', 3)
    sprite('hz311_09', 3)
    sprite('hz311_11', 3)
    sprite('hz311_12', 3)
    sprite('hz311_13', 3)
    sprite('hz311_14', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('hz310_00', 2)
    CommonSE('010_swing_sword_0')
    sprite('hz310_01', 4)
    sprite('hz310_02', 3)
    sprite('hz310_03', 4)
    sprite('hz310_04', 4)
    SmartVoiceline('hz155')
    sprite('hz310_05', 7)
    sprite('hz310_06', 4)
    sprite('hz310_07', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(20000)
        Hitstop(15)
        AirUntechableTime(60)
        Floorslide(20)
        StarterRating(2)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        FlipOnHit(1)
        SpecialCancel(1)
    sprite('hz310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('hz313_00', 4)
    SmartVoiceline('hz153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('hz313_01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('hz313_02', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 1)
    sprite('hz313_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('hz313_04', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('hz313_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('hz313_06', 6)
    sprite('hz313_07', 6)
    sprite('hz313_08', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('hz313_09', 1)
    CommonSE('100_hit_grap_3')
    sprite('hz313_10', 6)
    sprite('hz313_11', 6)
    sprite('hz313_12', 5)
    sprite('hz313_13', 5)
    sprite('hz313_14', 4)
    sprite('hz313_15', 4)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('hz320_00', 3)
    sprite('hz320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('hz320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('hz320_03', 5)
    sprite('hz320_04', 8)
    SmartVoiceline('hz155')
    sprite('hz320_05', 5)
    sprite('hz320_06', 5)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SetZLine(0, 50)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        Hitstop(0)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(500)
        AirPushbackY(-70000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(65)
        AirUntechableTime(65)
        StarterRating(2)
        ForcedLandingRecovery(0, 0)
    sprite('hz320_02', 5)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('hz321_00', 3)
    sprite('hz321_01', 3)
    SmartVoiceline('hz154')
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz321_02', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('hz321_03', 3)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('hz321_04', 6)
    SetZLine(1, 50)
    sprite('hz321_05', 3)
    sprite('hz321_06', 2)
    physicsXImpulse(-2000)
    physicsYImpulse(15000)
    GravityDefault()
    sprite('hz321_07', 2)
    sprite('hz321_08', 2)
    sprite('hz321_09', 2)
    sprite('hz321_10', 2)
    sprite('hz321_11', 2)
    sprite('hz321_12', 2)
    sprite('hz321_13', 2)


@Subroutine
def Kamae_Zanzou():
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(6)
    AfterimageInterval(2)
    AfterimageColor_1(240, 0, 128, 0)
    AfterimageColor_2(60, 0, 128, 0)
    AfterimageMask_1(0, 0, 64, 0)
    AfterimageMask_2(0, 0, 0, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)


@State
def Kamae():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        WhiffCancel('KamaeD')
        WhiffCancel('UltimateThrow')
        WhiffCancel('UltimateThrow_OD')
        AttackOff()
        if not PreviousStateCheck('KamaeDashF'):
            SLOT_65 = 0

        def upon_14():
            SLOT_65 = 0

        def upon_EVERY_FRAME():
            SLOT_65 = SLOT_65 + 1
            if SLOT_65 > 6:
                WhiffCancelEnable(1)
                BeginBuffer('KamaeA')
                BeginBuffer('KamaeB')
                BeginBuffer('KamaeC')
                BeginBuffer('KamaeDashB')
                BeginBuffer('KamaeDashF')
            if SLOT_65 > 22:
                callSubroutine('Kamae_Zanzou')
                BufferedOrPressedGoto('KamaeA')
                BufferedOrPressedGoto('KamaeB')
                BufferedOrPressedGoto('KamaeC')
                BufferedOrPressedGoto('KamaeDashB')
                BufferedOrPressedGoto('KamaeDashF')
    sprite('hz400_00', 3)
    sprite('hz400_01', 2)
    sprite('hz400_01', 1)
    CreateObject('EffKamae', 0)
    CreateObject('EffKamaeLand', -1)
    sprite('hz400_02', 5)
    SmartVoiceline('hz200')
    PrivateSE('hzse_05')
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 5)
    sprite('hz400_02', 5)
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 4)
    sprite('hz400_09', 1)
    enterState('KamaeD')


@State
def SpecialAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP2(79)
        AirUntechableTime(40)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(17)
        PushbackX(2000)
        AirPushbackY(-34000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(50)
        SLOT_65 = 0
        WhiffCancel('KamaeD')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz411_00', 3)
    CreateObject('EffLandAura', -1)
    Voiceline('hz214')
    sprite('hz411_01', 3)
    sprite('hz411_02', 3)
    sprite('hz411_03', 3)
    CreateObject('Eff411', -1)
    CommonSE('006_swing_blade_1')
    PrivateSE('hzse_06')
    sprite('hz411_04', 2)
    sprite('hz411_05', 2)
    sprite('hz411_06', 2)
    BeginBuffer('KamaeA')
    BeginBuffer('KamaeB')
    BeginBuffer('KamaeC')
    BeginBuffer('KamaeDashB')
    BeginBuffer('KamaeDashF')
    BeginBuffer('UltimateThrow')
    BeginBuffer('UltimateThrow_OD')
    sprite('hz411_07', 1)
    sprite('hz411_08', 1)
    sprite('hz411_09', 1)
    CreateObject('EffKamaeLand', -1)
    sprite('hz411_10', 3)
    PreventBlocking(1)
    CreateObject('EffKamae', 0)

    def upon_EVERY_FRAME():
        SLOT_65 = SLOT_65 + 1
        if SLOT_65 > 22:
            callSubroutine('Kamae_Zanzou')
    PrivateSE('hzse_05')
    WhiffCancelEnable(1)
    BufferedOrPressedGoto('KamaeA')
    BufferedOrPressedGoto('KamaeB')
    BufferedOrPressedGoto('KamaeC')
    BufferedOrPressedGoto('KamaeDashB')
    BufferedOrPressedGoto('KamaeDashF')
    BufferedOrPressedGoto('UltimateThrow')
    BufferedOrPressedGoto('UltimateThrow_OD')
    sprite('hz400_02', 5)
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 5)
    sprite('hz400_02', 5)
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 4)
    sprite('hz400_09', 1)
    enterState('KamaeD')


@State
def KamaeA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(80)
        AirHitstunAnimation(11)
        AirPushbackY(-60000)
        AirUntechableTime(40)
        PushbackX(15300)
        MoveAttributes(1, 0, 0, 0, 0)
        HitOverhead(2)
        StarterRating(2)
        AttackLevel_(3)
        Damage(700)
        AttackP2(79)
        Hitstun(19)
        if SLOT_65 > 22:
            AttackLevel_(4)
            Damage(840)
            AttackP2(82)
            GroundedHitstunAnimation(11)
            HardKnockdown(15)
            callSubroutine('Kamae_Zanzou')
            GotoState('KamaeATame')
            SLOT_51 = 1
            PerInertia(30)
        SLOT_65 = 0
        setInvincible(1)
        SpecificInvincibility(0, 0, 1, 0, 0)
        AddX(50000)
        EnableAfterimage(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz402_00', 1)
    CreateObject('EffLandAura', -1)
    sprite('hz402_01', 2)
    DespawnEAEffect('EffKamaeLand')
    DespawnEAEffect('EffKamae')
    AddX(50000)
    sprite('hz402_02', 2)
    SmartVoiceline('hz202')
    CommonSE('019_cloth_c')
    physicsXImpulse(8000)
    physicsYImpulse(18000)
    setGravity(2250)
    if SLOT_51:
        XImpulseAcceleration(150)
        CharacterFlash(32768, 12, 2)
    if PreviousStateCheck('KamaeDashF'):
        XImpulseAcceleration(125)
    if PreviousStateCheck('KamaeDashB'):
        XImpulseAcceleration(150)
    uponSendToLabel(LANDING, 1)
    sprite('hz402_03', 2)
    sprite('hz402_04', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('hz402_05', 2)
    CreateObject('EffChudan', -1)
    sprite('hz402_06', 3)
    PrivateSE('hzse_06')
    sprite('hz402_07', 3)
    sprite('hz402_08', 2)
    sprite('hz402_09', 2)
    sprite('hz402_10', 32767)
    Recovery()
    label(1)
    sprite('hz402_11', 3)
    setInvincible(0)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz402_12', 2)
    sprite('hz402_13', 2)
    sprite('hz402_14', 2)
    sprite('hz402_15', 2)


@State
def KamaeB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(90)
        HitAirUnblockable(3)
        PushbackX(19800)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackLevel_(4)
        Damage(900)
        AttackP2(82)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(40000)
        CHAirPushbackX(4000)
        CHAirPushbackY(48000)
        if SLOT_65 > 22:
            AttackLevel_(5)
            Damage(1080)
            AttackP2(84)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirPushbackX(10000)
            AirPushbackY(46000)
            CHAirPushbackX(10000)
            CHAirPushbackY(46000)
            AirUntechableTime(55)
            YImpulseBeforeWallbounce(1600)
            EnemyHitstopAddition(0, 10, 18)
            SLOT_52 = 1
            callSubroutine('Kamae_Zanzou')
            GotoState('KamaeBTame')
        SLOT_65 = 0
        uponSendToLabel(LANDING, 1)
        PerInertia(80)
        setInvincible(1)
        EnableAfterimage(1)
        AddX(10000)
    sprite('hz401_00', 1)
    PrivateSE('hzse_07')
    CommonSE('006_swing_blade_2')
    SmartVoiceline('hz201')
    CreateObject('EffSamaso', -1)
    CreateObject('EffLandAura', -1)
    sprite('hz401_00', 1)
    DespawnEAEffect('EffKamaeLand')
    DespawnEAEffect('EffKamae')
    sprite('hz401_01', 3)
    physicsYImpulse(28000)
    physicsXImpulse(-4000)
    setGravity(2400)
    CommonSE('004_swing_grap_1_1')
    if SLOT_52:
        CharacterFlash(32768, 10, 2)
    sprite('hz401_02', 3)
    sprite('hz401_03', 2)
    sprite('hz401_03', 2)
    sprite('hz401_04', 4)
    setInvincible(0)
    sprite('hz401_05', 4)
    label(0)
    sprite('hz401_06', 3)
    sprite('hz401_07', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz401_08', 3)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz401_09', 2)
    sprite('hz401_10', 2)
    sprite('hz401_11', 2)
    sprite('hz401_12', 2)
    sprite('hz401_13', 2)
    sprite('hz401_14', 2)


@State
def KamaeC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(80)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        Hitstop(16)
        MoveAttributes(0, 0, 1, 0, 0)
        UseSlashHitspark(1)
        HitLow(2)
        AttackLevel_(4)
        Damage(900)
        AirUntechableTime(40)
        AirPushbackX(3000)
        AirPushbackY(22000)
        CHAirPushbackX(-2000)
        CHAirPushbackY(27000)
        if SLOT_65 > 22:
            SLOT_52 = 1
            AttackLevel_(5)
            Damage(1080)
            AirUntechableTime(60)
            AirPushbackX(-2000)
            AirPushbackY(32000)
            CHAirPushbackX(-2000)
            CHAirPushbackY(32000)
            YImpulseBeforeWallbounce(1600)
            HitAirUnblockable(3)
            callSubroutine('Kamae_Zanzou')
            GotoState('KamaeCTame')
        SLOT_65 = 0
        StayAfterMovement(1, 0)
        physicsXImpulse(2000)
        if PreviousStateCheck('KamaeDashB'):
            physicsXImpulse(3000)
        PerInertia(80)
        setInvincible(1)
        SpecificInvincibility(0, 1, 0, 0, 0)
        EnableAfterimage(1)
    sprite('hz403_00', 1)
    CreateObject('EffLandAura', -1)
    sprite('hz403_00', 1)
    DespawnEAEffect('EffKamaeLand')
    DespawnEAEffect('EffKamae')
    sprite('hz403_01', 2)
    CommonSE('007_swing_knife_1')
    XImpulseAcceleration(200)
    sprite('hz403_02', 2)
    XImpulseAcceleration(200)
    sprite('hz403_03', 2)
    SmartVoiceline('hz203')
    CommonSE('007_swing_knife_1')
    sprite('hz403_04', 2)
    XImpulseAcceleration(30)
    CreateObject('EffGedan', -1)
    sprite('hz403_05', 2)
    XImpulseAcceleration(50)
    CommonSE('007_swing_knife_1')
    if SLOT_52:
        CharacterFlash(32768, 9, 2)
    sprite('hz403_06', 1)
    PrivateSE('hzse_06')
    sprite('hz403_07', 2)
    sprite('hz403_08', 4)
    XImpulseAcceleration(0)
    PerInertia(0)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    sprite('hz403_09', 4)
    setInvincible(0)
    Recovery()
    sprite('hz403_10', 3)
    sprite('hz403_11', 3)
    sprite('hz403_12', 3)
    sprite('hz403_13', 3)
    EnableAfterimage(0)
    sprite('hz403_14', 2)
    sprite('hz403_15', 2)


@State
def KamaeD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EnableAfterimage(1)
        AttackOff()
        Recovery()
        SLOT_65 = 0
    sprite('hz400_01', 6)
    CreateObject('EffLandAura', -1)
    TriggerUponForState('EffKamae', 32)
    sprite('hz400_10', 6)
    sprite('hz400_11', 6)


@State
def KamaeDashF():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        WhiffCancel('KamaeA')
        WhiffCancel('KamaeB')
        WhiffCancel('KamaeC')
        WhiffCancel('UltimateThrow')
        WhiffCancel('UltimateThrow_OD')

        def upon_EVERY_FRAME():
            SLOT_65 = SLOT_65 + 1
            if SLOT_65 > 22:
                callSubroutine('Kamae_Zanzou')

        def upon_STATE_END():
            ForceFaceSprite()
    sprite('hz032_00', 3)
    CreateObject('EffLandAura', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageInterval(1)
    AddX(50000)
    physicsXImpulse(5333)
    AddInertia(30000)
    sprite('hz032_01', 3)
    XImpulseAcceleration(150)
    WhiffCancelEnable(1)
    sprite('hz032_02', 3)
    DespawnEAEffect('EffKamae')
    CreateObject('EffKamae', 0)
    SmartVoiceline('hz212')
    DashEffects(100, 1, 1)
    XImpulseAcceleration(200)
    sprite('hz032_03', 3)
    XImpulseAcceleration(200)
    sprite('hz032_04', 3)
    SkidEffects(100, 1, 1)
    XImpulseAcceleration(60)
    sprite('hz032_04ex01', 3)
    XImpulseAcceleration(60)
    sprite('hz032_04ex02', 3)
    XImpulseAcceleration(60)
    sprite('hz032_05', 3)
    XImpulseAcceleration(60)
    sprite('hz032_06', 3)
    XImpulseAcceleration(0)
    sprite('hz032_07', 3)
    sprite('hz032_07', 1)
    if CheckInput(INPUT_HOLD_D):
        enterState('KamaeD')
    else:
        enterState('Kamae')


@State
def KamaeDashB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        WhiffCancel('KamaeA')
        WhiffCancel('KamaeB')
        WhiffCancel('KamaeC')
        WhiffCancel('UltimateThrow')
        WhiffCancel('UltimateThrow_OD')

        def upon_EVERY_FRAME():
            SLOT_65 = SLOT_65 + 1
            if SLOT_65 > 22:
                callSubroutine('Kamae_Zanzou')
        AddX(-80000)

        def upon_14():
            SLOT_65 = 0

        def upon_STATE_END():
            SetInertia(0)
            ForceFaceSprite()
    sprite('hz409_00', 3)
    CreateObject('EffLandAura', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageInterval(1)
    physicsXImpulse(-30000)
    SetInertia(-10000)
    sprite('hz409_01', 3)
    SmartVoiceline('hz213')
    DespawnEAEffect('EffKamae')
    CreateObject('EffKamae', 0)
    WhiffCancelEnable(1)
    DashEffects(100, 1, 1)
    sprite('hz409_02', 3)
    XImpulseAcceleration(60)
    sprite('hz409_01', 3)
    DashEffects(100, 1, 1)
    sprite('hz409_02', 3)
    XImpulseAcceleration(60)
    sprite('hz409_01', 3)
    DashEffects(100, 1, 1)
    sprite('hz409_02', 3)
    XImpulseAcceleration(60)
    sprite('hz409_01', 3)
    sprite('hz409_03', 4)
    SkidEffects(100, 1, 1)
    XImpulseAcceleration(60)
    sprite('hz409_04', 4)
    XImpulseAcceleration(0)
    WhiffCancelEnable(0)
    clearUponHandler(EVERY_FRAME)
    SLOT_65 = 0
    TriggerUponForState('EffKamae', 32)


@State
def SpecialShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(680)
        AttackP2(79)
        CHGroundedHitstunAnimation(19)
        AirHitstunAnimation(19)
        AirPushbackX(24000)
        AirPushbackY(8000)
        AirUntechableTime(35)
        Floorslide(25)
        Hitstop(9)
        EnemyHitstopAddition(5, 5, 7)
        StrikeProjectileLevel(1)
        ProjectileLevel(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz407_00', 3)
    SmartVoiceline('hz208')
    CreateObject('EffLandAura', -1)
    sprite('hz407_01', 3)
    PrivateSE('hzse_08')
    CreateObject('EffSpKensei', -1)
    sprite('hz407_02', 4)
    sprite('hz407_03', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz407_04', 2)
    sprite('hz407_05', 3)
    Recovery()
    sprite('hz407_06', 3)
    sprite('hz407_07', 3)
    sprite('hz407_08', 2)
    sprite('hz407_09', 2)
    sprite('hz407_10', 2)
    sprite('hz407_11', 2)
    sprite('hz407_12', 2)
    sprite('hz407_13', 2)


@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        PreventGroundedHit(1)
        EnemyHitstopAddition(7, 30, 30)
        HitAirUnblockable(3)
        AttackDirection(0)
        UseSlashHitspark(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(2)
        AirPushbackX(0)
        IgnoreComboTime(1)
        Unknown12052(2)
        FatalCounter(1)
        MoveAttributes(0, 0, 0, 1, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_65 > 22:
                    CopyFromRightToLeft(22, 2, 83, 4, 2, 83)
                    CopyFromRightToLeft(23, 2, 51, 4, 2, 23)
                    SLOT_51 = SLOT_51 + -300000
                    CopyFromRightToLeft(22, 2, 23, 23, 2, 51)
        uponSendToLabel(OPPONENT_HIT, 0)
        AttackOff()
    sprite('hz405_00', 2)
    sprite('hz405_01', 2)
    SmartVoiceline('hz205')
    CreateObject('AntiAirWindSmoke', -1)
    CreateObject('ExBodyAuraAntiAir', -1)

    def RunOnObject_1():
        AddY(-80000)
    sprite('hz405_02', 2)
    sprite('hz405_03', 2)
    sprite('hz405_04', 2)
    sprite('hz405_05', 3)
    PrivateSE('hzse_02')
    PrivateSE('hzse_04')
    CreateObject('KusariAntiAir', 109)
    RegisterObject(4, 1)
    ObjectHitbox(4)
    TriggerUponForState('AntiAirWindSmoke', 32)
    sprite('hz405_06', 3)
    RefreshMultihit()
    sprite('hz405_06', 7)
    SLOT_51 = 1
    sprite('hz405_20', 2)
    AttackOff()
    TriggerUponForState('AntiAirWindSmoke', 33)
    Recovery()
    sprite('hz405_21', 2)
    sprite('hz405_22', 2)
    sprite('hz405_23', 2)
    sprite('hz405_24', 2)
    sprite('hz405_25', 2)
    sprite('hz405_26', 2)
    CommonSE('006_swing_blade_0')
    sprite('hz405_27', 3)
    sprite('hz405_28', 3)
    sprite('hz405_29', 3)
    sprite('hz405_30', 3)
    sprite('hz405_31', 3)
    sprite('hz405_32', 3)
    ExitState()
    label(0)
    clearUponHandler(OPPONENT_HIT)
    SetActionMark(1)
    ObjectUpon(FALLING, 32)
    SetXCollisionFromOrigin(150)
    sprite('hz405_07', 6)
    sprite('hz405_08', 6)
    sprite('hz405_09', 2)
    sprite('hz405_10', 2)
    SmartVoiceline('hz206')
    TriggerUponForState('AntiAirWindSmoke', 33)
    sprite('hz405_11', 2)
    CommonSE('011_spin_0')
    sprite('hz405_12', 2)
    SetActionMark(0)
    RefreshMultihit()
    Damage(2000)
    AttackP2(82)
    AirPushbackX(-48000)
    AirPushbackY(6000)
    AirUntechableTime(120)
    EnemyHitstopAddition(0, 0, 0)
    Hitstop(0)
    Floorslide(25)
    IgnoreComboTime(0)
    Wallbounce(1)
    WallbounceReboundTime(0)
    NonCornerWallbounce(1)
    NonCornerCHWallbounce(0)
    HardKnockdown(20)
    sprite('hz405_13', 5)
    AttackOff()
    sprite('hz405_14', 5)
    sprite('hz405_15', 20)
    sprite('hz405_15', 7)
    CtrlDirectionVsTarget()
    HitOrBlockCancel('UltimateShot')
    HitOrBlockCancel('UltimateShot_OD')
    sprite('hz405_16', 5)
    sprite('hz405_17', 5)
    sprite('hz405_18', 5)
    sprite('hz405_19', 5)


@State
def AirAssault2():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(900)
        GroundedHitstunAnimation(1)
        AttackP1(80)
        AirPushbackY(-68000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(50)
        HardKnockdown(1)
        CHHardKnockdown(-1)
        EnableEmergencyTechAirHit(1)
        CHGroundBounce(1)
        CHBouncePercentage(50)
        UseSlashHitspark(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz412_00', 3)
    EndMomentum(1)
    physicsYImpulse(12000)
    setGravity(2400)
    physicsXImpulse(4000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageMask_1(0, 171, 57, 171)
    AfterimageMask_2(0, 0, 0, 0)
    sprite('hz412_01', 3)
    sprite('hz412_02', 3)
    Voiceline('hz215')
    sprite('hz412_03', 2)
    XImpulseAcceleration(50)
    YAccel(120)
    PerGravity(150)
    ParticleSize(1440)
    ParticleRandomRotation()
    CallCustomizableParticle('hzef_412flash', 0)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    sprite('hz412_04', 3)
    CreateObject('Eff412Zanzo', -1)
    label(0)
    sprite('hz412_05', 3)
    sprite('hz412_04', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('hz412_06', 4)
    Recovery()
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('hz412_07', 4)
    EnableAfterimage(0)
    if not SLOT_2:
        WhiffCrouchBlockCancel(1)
        WhiffStandingTurnCancel(1)
        WhiffCrouchingTurnCancel(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffFDashCancel(1)
        WhiffFWalkCancel(1)
    sprite('hz412_08', 4)
    sprite('hz412_09', 4)


@State
def SPThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('SPThrowExe', 2, 0, 0)
        RangeCheck(90000)
        DistanceCheck(250000, 1, -1, -1)
        PushbackX(0)
        DamageFromStateOnly('SPThrowExe')
        UseSlashHitspark(1)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 0, 1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(10)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('hz406_00', 3)
    PrivateSE('hzse_09')
    SmartVoiceline('hz207')
    CreateObject('EffLandAura', -1)
    CreateObject('EffCommandThrowAura', -1)
    sprite('hz406_01', 2)
    PrivateSE('hzse_09')
    sprite('hz406_01', 2)
    sprite('hz406_02', 2)
    CreateObject('EffCommandThrowWind', 0)
    CommonSE('004_swing_grap_1_0')
    sprite('hz406_03', 2)
    PrivateSE('hzse_09')
    CreateObject('EffCommandThrowWind', 0)
    sprite('hz406_04', 1)
    CreateObject('EffCommandThrowWind', 1)
    CommonSE('004_swing_grap_1_0')
    sprite('hz406_04', 1)
    setInvincible(0)
    sprite('hz406_05', 2)
    EnableAfterimage(0)
    sprite('hz406_06', 2)
    sprite('hz406_07', 3)
    sprite('hz406_08', 3)
    sprite('hz406_09', 3)
    sprite('hz406_10', 3)
    sprite('hz406_11', 3)
    sprite('hz406_12', 3)
    sprite('hz406_13', 3)
    sprite('hz406_14', 3)
    sprite('hz406_15', 3)


@State
def SPThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(3)
        Damage(600)
        AttackP2(60)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)
        AirPushbackY(42000)
        AirPushbackX(3000)
        Hitstop(6)
        UseSlashHitspark(1)
        StarterRating(2)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(10)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz406_04', 12)
    PrivateSE('hzse_09')
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    EnableCollision(0)
    ThrowLock(1)
    sprite('hz406_16', 3)
    PrivateSE('hzse_09')
    sprite('hz406_17', 3)
    PrivateSE('hzse_09')
    CommonSE('100_hit_grap_3')
    sprite('hz406_18', 1)
    PrivateSE('hzse_09')
    sprite('hz406_19', 6)
    EnableAfterimage(0)
    sprite('hz406_20', 4)
    CommonSE('007_swing_knife_2')
    sprite('hz406_21', 3)
    sprite('hz406_22', 3)
    sprite('hz406_23', 3)
    sprite('hz406_24', 3)
    sprite('hz406_25', 3)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(0)
        AttackLevel_(5)
        Damage(1950)
        Hitstop(30)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(90000)
        AirPushbackX(3000)
        YImpulseBeforeWallbounce(1600)
        AttackP1(50)
        AirUntechableTime(120)
        AttackDirection(0)
        StarterRating(2)
        FatalCounter(1)
        uponSendToLabel(LANDING, 1)
        StayAfterMovement(1, 0)

        def upon_STATE_END():
            AlphaValue(255)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz430_00', 2)
    sprite('hz430_00', 30)
    setInvincible(1)
    SmartVoiceline('hz250')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('EffUltimateAssaultBunshinA', -1)
    CreateObject('EffUltimateAssaultBunshinB', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-10)
    sprite('hz430_01', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(40000)
    ConstantAlphaModifier(150)
    sprite('hz430_02', 3)
    XImpulseAcceleration(25)
    sprite('hz430_03', 3)
    setInvincible(0)
    XImpulseAcceleration(25)
    sprite('hz430_04', 2)
    XImpulseAcceleration(25)
    CommonSE('004_swing_grap_1_2')
    AltKnockdownEffects(100, 1, 1)
    CreateObject('HZEF_UltimateAssault', -1)
    sprite('hz430_05', 3)
    PrivateSE('hzse_14')
    SmartVoiceline('hz251')
    ScreenShake(10000, 10000)
    sprite('hz430_06', 5)
    physicsYImpulse(8000)
    sprite('hz430_07', 5)
    GravityDefault()
    sprite('hz430_08', 5)
    label(0)
    sprite('hz430_09', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz430_10', 3)
    XImpulseAcceleration(0)
    sprite('hz430_11', 3)
    sprite('hz430_12', 3)
    sprite('hz430_13', 3)
    sprite('hz430_14', 3)
    sprite('hz430_15', 4)
    sprite('hz430_16', 4)
    sprite('hz430_17', 4)
    sprite('hz430_18', 4)


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(0)
        AttackLevel_(5)
        Damage(2100)
        Hitstop(30)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(90000)
        AirPushbackX(3000)
        YImpulseBeforeWallbounce(1600)
        AttackP1(50)
        AirUntechableTime(120)
        AttackDirection(0)
        AttackType(4)
        StarterRating(2)
        FatalCounter(1)
        uponSendToLabel(LANDING, 1)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            ScreenShake(40000, 40000)

        def upon_STATE_END():
            AlphaValue(255)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hz430_00', 2)
    setInvincible(1)
    sprite('hz430_00', 30)
    SmartVoiceline('hz250')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('EffUltimateAssaultBunshinA', -1)
    CreateObject('EffUltimateAssaultBunshinB', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-10)
    sprite('hz430_01', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(50000)
    ConstantAlphaModifier(150)
    sprite('hz430_02', 3)
    XImpulseAcceleration(25)
    sprite('hz430_03', 3)
    XImpulseAcceleration(25)
    PrivateSE('hzse_07')
    sprite('hz430_04', 2)
    XImpulseAcceleration(25)
    CommonSE('004_swing_grap_1_2')
    AltKnockdownEffects(100, 1, 1)
    CreateObject('HZEF_UltimateAssault', -1)
    CreateObject('HZEF_UltimateAssaultOD', -1)
    sprite('hz430_05', 3)
    PrivateSE('hzse_14')
    SmartVoiceline('hz251')
    ScreenShake(10000, 10000)
    setInvincible(0)
    sprite('hz430_06', 5)
    physicsYImpulse(8000)
    sprite('hz430_07', 5)
    GravityDefault()
    sprite('hz430_08', 5)
    label(0)
    sprite('hz430_09', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz430_10', 3)
    XImpulseAcceleration(0)
    sprite('hz430_11', 3)
    sprite('hz430_12', 3)
    sprite('hz430_13', 3)
    sprite('hz430_14', 3)
    sprite('hz430_15', 4)
    sprite('hz430_16', 4)
    sprite('hz430_17', 4)
    sprite('hz430_18', 4)


@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(1)
        Damage(200)
        AttackP1(80)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(1)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        AttackOff()
        EndMomentum(1)
        uponSendToLabel(32, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_65 > 22:
                    CopyFromRightToLeft(22, 2, 83, 4, 2, 83)
                    CopyFromRightToLeft(23, 2, 51, 4, 2, 23)
                    SLOT_51 = SLOT_51 + -300000
                    CopyFromRightToLeft(22, 2, 23, 23, 2, 51)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(3)
    sprite('hz431_00', 4)
    setInvincible(1)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('UltimateLockMagic', -1)
    CreateObject('DDLockAura', -1)
    sprite('hz431_01', 2)
    PrivateSE('hzse_05')
    sprite('hz431_02', 20)
    SmartVoiceline('hz252')
    sprite('hz431_02', 11)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('hz431_03', 4)
    TriggerUponForState('UltimateLockMagic', 32)
    sprite('hz431_04', 4)
    sprite('hz431_05', 4)
    CreateObject('UltimateLockObj', -1)
    TriggerUponForState('UltimateLockMagic', 33)
    CreateObject('EffUltimateLockSignal', -1)
    sprite('hz431_06', 3)
    setInvincible(0)
    TriggerUponForState('UltimateLockObjCenter', 32)
    TriggerUponForState('UltimateLockObjTop', 32)
    TriggerUponForState('UltimateLockObjBottom', 32)
    TriggerUponForState('DDLockAura', 32)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_56', 3)
    sprite('hz431_57', 3)
    sprite('hz431_58', 3)
    sprite('hz431_59', 3)
    sprite('hz431_60', 3)
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(32)
    TriggerUponForState('DDLockAura', 32)
    sprite('hz431_06', 4)
    ForceFaceSprite()
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('hz431_07', 4)
    sprite('hz431_08', 4)
    sprite('hz431_06', 5)
    sprite('hz431_07', 5)
    sprite('hz431_08', 5)
    sprite('hz431_09', 3)
    AttackOff()
    sprite('hz431_10', 3)
    sprite('hz431_11', 3)
    CreateObject('UltimateKusari', 109)
    uponSendToLabel(33, 22)
    sprite('hz431_12', 3)
    TriggerUponForState('UltimateLockObjCenter', 32)
    TriggerUponForState('UltimateLockObjTop', 32)
    TriggerUponForState('UltimateLockObjBottom', 32)
    SLOT_52 = 10
    loopRest()
    label(1)
    sprite('hz431_13', 3)
    sprite('hz431_14', 3)
    sprite('hz431_15', 2)
    sprite('hz431_15', 1)
    SLOT_52 = SLOT_52 + -1
    if SLOT_52:
        conditionalSendToLabel(1)
    label(22)
    clearUponHandler(33)
    sprite('hz431_16', 4)
    sprite('hz431_17', 4)
    CommonSE('011_spin_0')
    sprite('hz431_18', 4)
    sprite('hz431_19', 8)
    sprite('hz431_20', 28)
    sprite('hz431_21', 5)
    loopRest()
    EnableCollision(0)
    CreateObject('UltimateWindSmoke', -1)
    CreateParticle('hzef_ultimateauraopt', -1)
    CreateObject('DDBodyAura', -1)
    SmartVoiceline('hz253')
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    sprite('hz431_23', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    sprite('hz431_25', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    sprite('hz431_27', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    sprite('hz431_23', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    sprite('hz431_25', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    sprite('hz431_27', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpulseBeforeWallbounce(700)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    sprite('hz431_30', 3)
    CreateObject('HZEF_DDBackAura', -1)
    TriggerUponForState('UltimateWindSmoke', 32)
    TriggerUponForState('DDBodyAura', 32)
    sprite('hz431_31', 3)
    sprite('hz431_32', 3)
    sprite('hz431_33', 3)
    sprite('hz431_34', 3)
    sprite('hz431_35', 3)
    PrivateSE('hzse_08')
    PrivateSE('hzse_05')
    sprite('hz431_36', 3)
    sprite('hz431_37', 2)
    sprite('hz431_38', 3)
    CreateObject('EffDDSnakeFang', -1)
    ScreenShake(0, 10000)
    sprite('hz431_39', 3)
    ScreenShake(0, 8000)
    sprite('hz431_38', 3)
    ScreenShake(0, 6000)
    sprite('hz431_39', 3)
    ScreenShake(0, 4000)
    sprite('hz431_38', 3)
    ScreenShake(0, 2000)
    sprite('hz431_39', 3)
    sprite('hz431_38', 3)
    sprite('hz431_39', 3)
    sprite('hz431_38', 3)
    sprite('hz431_39', 3)
    sprite('hz431_40', 2)
    CameraControlEnable(1)
    TriggerUponForState('UltimateWindSmoke', 33)
    sprite('hz431_41', 1)
    CommonSE('009_swing_rapier_1')
    sprite('hz431_42', 3)
    PrivateSE('hzse_14')
    PrivateSE('hzse_03')
    ScreenShake(15000, 15000)
    DefeatOpponentBehavior(0)
    AttackLevel_(4)
    Damage(2000)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackY(30000)
    AirPushbackX(50000)
    YImpulseBeforeWallbounce(1300)
    HardKnockdown(22)
    Hitstop(12)
    RefreshMultihit()
    CameraControlEnable(0)
    setInvincible(0)
    IgnoreComboTime(1)
    SingleComboCorrection(1)
    GotoState('UltimateShotFinish')
    sprite('hz431_43', 5)
    EnableCollision(1)
    TriggerUponForState('HZEF_DDBackAura', 32)
    TriggerUponForState('DDBodyAura', 33)
    sprite('hz431_44', 5)
    sprite('hz431_45', 5)
    sprite('hz431_43', 5)
    sprite('hz431_44', 5)
    sprite('hz431_45', 5)
    sprite('hz431_43', 5)
    sprite('hz431_44', 5)
    sprite('hz431_45', 5)
    sprite('hz431_46', 5)
    sprite('hz431_47', 5)
    sprite('hz431_48', 5)
    sprite('hz431_49', 5)
    PrivateSE('hzse_09')
    sprite('hz431_50', 4)
    PrivateSE('hzse_09')
    sprite('hz431_51', 4)
    PrivateSE('hzse_09')
    sprite('hz431_52', 3)
    CommonSE('007_swing_knife_2')
    sprite('hz431_53', 12)
    sprite('hz431_55', 4)


@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(1)
        Damage(90)
        AttackP1(80)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(2)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        AttackType(4)
        StayAfterMovement(1, 0)
        AttackOff()
        SLOT_64 = 1

        def upon_STATE_END():
            SLOT_64 = 0

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(100)
        uponSendToLabel(32, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_65 > 22:
                    CopyFromRightToLeft(22, 2, 83, 4, 2, 83)
                    CopyFromRightToLeft(23, 2, 51, 4, 2, 23)
                    SLOT_51 = SLOT_51 + -300000
                    CopyFromRightToLeft(22, 2, 23, 23, 2, 51)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(3)
    sprite('hz431_00', 4)
    setInvincible(1)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('UltimateLockMagic', -1)
    CreateObject('DDLockAura', -1)
    sprite('hz431_01', 2)
    PrivateSE('hzse_05')
    sprite('hz431_02', 20)
    SmartVoiceline('hz252')
    sprite('hz431_02', 11)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('hz431_03', 4)
    TriggerUponForState('UltimateLockMagic', 32)
    sprite('hz431_04', 4)
    sprite('hz431_05', 4)
    CreateObject('UltimateLockObj', -1)
    TriggerUponForState('UltimateLockMagic', 33)
    CreateObject('EffUltimateLockSignal', -1)
    sprite('hz431_06', 3)
    setInvincible(0)
    TriggerUponForState('UltimateLockObjCenter', 32)
    TriggerUponForState('UltimateLockObjTop', 32)
    TriggerUponForState('UltimateLockObjBottom', 32)
    TriggerUponForState('DDLockAura', 32)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_06', 3)
    sprite('hz431_07', 3)
    sprite('hz431_08', 3)
    sprite('hz431_56', 3)
    sprite('hz431_57', 3)
    sprite('hz431_58', 3)
    sprite('hz431_59', 3)
    sprite('hz431_60', 3)
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(32)
    TriggerUponForState('DDLockAura', 32)
    sprite('hz431_06', 4)
    ForceFaceSprite()
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('hz431_07', 4)
    sprite('hz431_08', 4)
    sprite('hz431_06', 5)
    sprite('hz431_07', 5)
    sprite('hz431_08', 5)
    sprite('hz431_09', 3)
    AttackOff()
    sprite('hz431_10', 3)
    sprite('hz431_11', 3)
    CreateObject('UltimateKusari', 109)
    uponSendToLabel(33, 22)
    sprite('hz431_12', 3)
    TriggerUponForState('UltimateLockObjCenter', 32)
    TriggerUponForState('UltimateLockObjTop', 32)
    TriggerUponForState('UltimateLockObjBottom', 32)
    SLOT_52 = 10
    loopRest()
    label(1)
    sprite('hz431_13', 3)
    sprite('hz431_14', 3)
    sprite('hz431_15', 2)
    sprite('hz431_15', 1)
    SLOT_52 = SLOT_52 + -1
    if SLOT_52:
        conditionalSendToLabel(1)
    label(22)
    clearUponHandler(33)
    sprite('hz431_16', 4)
    sprite('hz431_17', 4)
    CommonSE('011_spin_0')
    sprite('hz431_18', 4)
    sprite('hz431_19', 8)
    sprite('hz431_20', 28)
    sprite('hz431_21', 5)
    loopRest()
    EnableCollision(0)
    CreateObject('UltimateWindSmoke', -1)
    CreateParticle('hzef_ultimateauraopt', -1)
    CreateObject('DDBodyAura', -1)
    SmartVoiceline('hz253')
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    sprite('hz431_23', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    sprite('hz431_25', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    sprite('hz431_27', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    sprite('hz431_23', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    sprite('hz431_25', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    sprite('hz431_27', 1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    Hitstop(1)
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_22', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoA', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_24', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoB', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_26', 1)
    RefreshMultihit()
    CreateObject('EffDDZanzoC', -1)
    CommonSE('009_swing_rapier_0')
    sprite('null', 1)
    sprite('hz431_28', 1)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpulseBeforeWallbounce(700)
    OppPositionOnHit(1, 200000, 40000)
    RefreshMultihit()
    CreateObject('EffDDZanzoD', -1)
    sprite('hz431_29', 1)
    CommonSE('009_swing_rapier_0')
    sprite('hz431_30', 3)
    sprite('hz431_31', 3)
    sprite('hz431_32', 3)
    sprite('hz431_33', 3)
    TriggerUponForState('UltimateWindSmoke', 33)
    CreateObject('hzef432_bind', -1)
    CommonSE('022_magiccircle_c')
    sprite('hz432_10', 3)
    CreateObject('HZEF_DDBackAura', -1)
    sprite('hz432_11', 3)
    sprite('hz432_12', 3)
    TriggerUponForState('DDBodyAura', 33)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    sprite('hz432_15', 3)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    SmartVoiceline('hz254')
    CreateObject('EffDDSnakeFangOD', -1)
    sprite('hz432_15', 3)
    sprite('hz432_16', 3)
    sprite('hz432_17', 3)
    sprite('hz432_18', 4)
    TriggerUponForState('HZEF_DDBackAura', 32)
    sprite('hz432_19', 2)
    SetYCollisionFromOrigin(360)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    setGravity(1500)
    sprite('hz432_20', 2)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1000)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(5000)
    AirPushbackY(17000)
    ResetGravity()
    UseSlashHitspark(0)
    UsePunchHitspark(1)
    Hitstop(13)
    HardKnockdown(1)
    DamageEffect(0, '')
    OppPositionOnHit(0, 0, 0)
    TriggerUponForState('hzef432_bind', 32)
    sprite('hz432_21', 3)
    sprite('hz432_22', 3)
    sprite('hz432_47', 3)
    PrivateSE('hzse_11')
    sprite('hz432_48', 32767)
    PrivateSE('hzse_12')
    label(100)
    sprite('hz432_49', 3)
    RefreshMultihit()
    AirHitstunAnimation(19)
    GroundedHitstunAnimation(19)
    Wallbounce(1)
    WallbounceReboundTime(0)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Hitstop(20)
    HardKnockdown(60)
    DefeatOpponentBehavior(0)
    EndMomentum(1)
    ScreenShake(50000, 50000)
    CommonSE('005_swing_grap_2_0')
    CommonSE('025_cleanhit_grap')
    CommonSE('025_cleanhit_grap')
    CommonSE('213_bound_1')
    PrivateSE('hzse_12')
    GotoState('UltimateShot_ODFinish')
    sprite('hz432_50', 5)
    sprite('hz432_51', 5)
    sprite('hz432_52', 5)
    sprite('hz432_53', 5)
    sprite('hz432_53ex', 5)
    clearUponHandler(EVERY_FRAME)
    sprite('hz432_57', 5)
    sprite('hz432_58', 5)
    sprite('hz432_59', 5)
    sprite('hz601_17', 5)
    CommonSE('019_cloth_a')
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    sprite('hz301_00', 5)
    sprite('hz301_01', 5)
    sprite('hz301_02', 5)
    sprite('hz301_03', 5)
    sprite('hz301_02', 5)
    sprite('hz301_03', 5)
    sprite('hz301_02', 5)
    sprite('hz301_03', 5)
    sprite('hz301_04', 5)
    sprite('hz301_05', 5)
    sprite('hz301_06', 5)
    sprite('hz301_07', 5)


@State
def UltimateThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateThrowExe', 3, 0, 0)
        RangeCheck(80000)
        DistanceCheck(250000, 1, -1, -1)
        setInvincible(1)
        if SLOT_65 > 22:
            SLOT_51 = 1
            callSubroutine('Kamae_Zanzou')

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('hz032_00', 1)
    CreateObject('EffLandAura', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageInterval(1)
    physicsXImpulse(3000)
    sprite('hz032_01', 2)
    physicsXImpulse(5000)
    sprite('hz032_02', 2)
    CreateObject('EffKamae', 0)
    DashEffects(100, 1, 1)
    physicsXImpulse(15000)
    if SLOT_51:
        CharacterFlash(32768, 24, 2)
        XSpeed(10000)
    sprite('hz032_03', 3)
    sprite('hz032_04', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 1)
    sprite('hz032_04ex01', 4)
    XImpulseAcceleration(60)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('hz032_04ex02', 4)
    XImpulseAcceleration(60)
    SmartVoiceline('hz255')
    sprite('hz432_00', 3)
    CreateObject('EffKamae', 0)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz432_01', 19)
    CommonSE('010_swing_sword_0')
    sprite('hz432_02', 3)
    CommonSE('010_swing_sword_0')
    sprite('hz432_03', 8)
    setInvincible(0)
    EnableAfterimage(0)
    sprite('hz432_04', 8)
    DespawnEAEffect('EffKamae')
    sprite('hz432_05', 8)
    sprite('hz432_06', 8)
    sprite('hz432_07', 8)


@State
def UltimateThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(200)
        AirUntechableTime(120)
        Hitstop(0)
        AttackP2(70)
        DefeatOpponentBehavior(1)
        OppPositionOnHit(1, 250000, 100000)
        DamageEffect(5, '')
        SetZLine(1, 50)
        StayAfterMovement(1, 0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('hz432_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    StartMultihit()
    ThrowLock(1)
    DespawnEAEffect('EffKamae')
    sprite('hz432_02', 3)
    CreateObject('hzef432_bind', -1)
    sprite('hz432_08', 3)
    sprite('hz432_09', 3)
    CommonSE('022_magiccircle_c')
    sprite('hz432_10', 3)
    sprite('hz432_11', 3)
    sprite('hz432_12', 3)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    sprite('hz432_15', 3)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    sprite('hz432_15', 3)
    sprite('hz432_16', 3)
    sprite('hz432_17', 3)
    SmartVoiceline('hz256')
    sprite('hz432_18', 3)
    sprite('hz432_19', 2)
    SetYCollisionFromOrigin(360)
    SetXCollisionFromOrigin(300)
    physicsXImpulse(15000)
    physicsYImpulse(30000)
    setGravity(2500)
    sprite('hz432_20', 2)
    RefreshMultihit()
    AttackLevel_(4)
    ResetAttackP2()
    Damage(280)
    AirPushbackY(3000)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    ResetPushback()
    ResetVerticalDrag()
    ResetGravity()
    Hitstop(7)
    HardKnockdown(1)
    DamageEffect(0, '')
    TriggerUponForState('hzef432_bind', 32)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_21', 4)
    sprite('hz432_22', 4)
    sprite('hz432_23', 4)
    sprite('hz432_24', 2)
    sprite('hz432_25', 2)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-50000)
    YImpulseBeforeWallbounce(0)
    GroundBounce(1)
    BouncePercentage(40)
    sprite('hz432_26', 2)
    sprite('hz432_27', 32767)
    label(1)
    sprite('hz432_28', 3)
    EndMomentum(1)
    SetXCollisionFromOrigin(550)
    CreateObject('UltimateThrowCamera', -1)
    sprite('hz432_29', 3)
    sprite('hz432_30', 3)
    sprite('hz432_31', 3)
    sprite('hz432_32', 3)
    sprite('hz432_33', 3)
    sprite('hz432_34', 2)
    RefreshMultihit()
    AirPushbackY(-50000)
    ResetGravity()
    GroundBounceReset()
    HardKnockdown(1)
    Hitstop(0)
    sprite('hz432_34', 3)
    sprite('hz432_35', 3)
    sprite('hz432_36', 3)
    sprite('hz432_37', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 4)
    sprite('hz432_39', 12)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(57)
    AirPushbackX(300)
    HitsparkSize(500)
    ScreenShake(0, 1000)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_37', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 3)
    sprite('hz432_39', 8)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_37', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 3)
    sprite('hz432_39', 4)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    SLOT_52 = 4
    label(10)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 2)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    SLOT_52 = SLOT_52 + -1
    if not SLOT_52:
        notConditionalSendToLabel(11)
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 2)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 3)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_44', 3)
    CreateObject('hzef432', -1)
    sprite('hz432_45', 3)
    DespawnEAEffect('UltimateThrowCamera')
    CommonSE('005_swing_grap_2_0')
    CommonSE('213_bound_1')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(400)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(7500)
    AirPushbackY(20000)
    Hitstop(8)
    HitsparkSize(1000)
    physicsXImpulse(10000)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()

    def upon_LANDING():
        clearUponHandler(LANDING)
        sendToLabel(2)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_46', 3)
    PrivateSE('hzse_11')
    sprite('hz432_47', 3)
    PrivateSE('hzse_11')
    sprite('hz432_48', 32767)
    PrivateSE('hzse_12')
    label(2)
    sprite('hz432_49', 3)
    CommonSE('005_swing_grap_2_0')
    CommonSE('213_bound_1')
    PrivateSE('hzse_12')
    EndMomentum(1)
    RefreshMultihit()
    Damage(800)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Wallstick(1)
    WallstickDuration(30)
    AirHitstunAfterWallbounce(100)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Hitstop(16)
    HardKnockdown(40)
    DefeatOpponentBehavior(0)
    ScreenShake(50000, 50000)
    GotoState('UltimateThrow_Finish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_50', 6)
    SetXCollisionFromOrigin(150)
    sprite('hz432_51', 6)
    sprite('hz432_52', 6)
    sprite('hz432_53', 6)
    sprite('hz432_53ex', 6)
    sprite('hz432_54', 6)
    sprite('hz432_55', 15)
    clearUponHandler(EVERY_FRAME)
    sprite('hz432_56', 7)
    sprite('hz432_57', 7)
    sprite('hz432_58', 7)
    sprite('hz432_59', 7)
    sprite('hz601_17', 7)
    CommonSE('019_cloth_a')
    sprite('hz601_18', 7)
    sprite('hz601_19', 7)


@State
def UltimateThrow_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateThrowExe_OD', 3, 0, 0)
        RangeCheck(80000)
        DistanceCheck(250000, 1, -1, -1)
        AttackType(4)
        setInvincible(1)
        if SLOT_65 > 22:
            SLOT_51 = 1
            callSubroutine('Kamae_Zanzou')

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('hz032_00', 1)
    CreateObject('EffLandAura', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageInterval(1)
    physicsXImpulse(3000)
    sprite('hz032_01', 2)
    physicsXImpulse(5000)
    sprite('hz032_02', 2)
    CreateObject('EffKamae', 0)
    DashEffects(100, 1, 1)
    physicsXImpulse(15000)
    if SLOT_51:
        CharacterFlash(32768, 24, 2)
        XSpeed(10000)
    sprite('hz032_03', 3)
    sprite('hz032_04', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 1)
    sprite('hz032_04ex01', 4)
    XImpulseAcceleration(60)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('hz032_04ex02', 4)
    XImpulseAcceleration(60)
    SmartVoiceline('hz255')
    sprite('hz432_00', 3)
    CreateObject('EffKamae', 0)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz432_01', 19)
    CommonSE('010_swing_sword_0')
    sprite('hz432_02', 3)
    CommonSE('010_swing_sword_0')
    sprite('hz432_03', 8)
    setInvincible(0)
    EnableAfterimage(0)
    sprite('hz432_04', 8)
    DespawnEAEffect('EffKamae')
    sprite('hz432_05', 8)
    sprite('hz432_06', 8)
    sprite('hz432_07', 8)


@State
def UltimateThrowExe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(200)
        AirUntechableTime(120)
        Hitstop(0)
        AttackP2(70)
        DefeatOpponentBehavior(1)
        AttackType(4)
        OppPositionOnHit(1, 250000, 100000)
        DamageEffect(5, '')
        SetZLine(1, 50)
        StayAfterMovement(1, 0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
        SLOT_64 = 1

        def upon_STATE_END():
            SLOT_64 = 0
        if not CheckObjectPresence(5):
            CreateObject('HZEF_DrainField', -1)
            RegisterObject(5, 1)
    sprite('hz432_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    StartMultihit()
    ThrowLock(1)
    DespawnEAEffect('EffKamae')
    sprite('hz432_02', 3)
    CreateObject('hzef432_bind', -1)
    sprite('hz432_08', 3)
    sprite('hz432_09', 3)
    CommonSE('022_magiccircle_c')
    sprite('hz432_10', 3)
    sprite('hz432_11', 3)
    sprite('hz432_12', 3)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    sprite('hz432_15', 3)
    sprite('hz432_13', 3)
    sprite('hz432_14', 3)
    sprite('hz432_15', 3)
    sprite('hz432_16', 3)
    sprite('hz432_17', 3)
    SmartVoiceline('hz256')
    sprite('hz432_18', 3)
    sprite('hz432_19', 2)
    SetYCollisionFromOrigin(360)
    SetXCollisionFromOrigin(300)
    physicsXImpulse(15000)
    physicsYImpulse(30000)
    setGravity(2500)
    sprite('hz432_20', 2)
    RefreshMultihit()
    AttackLevel_(4)
    ResetAttackP2()
    Damage(280)
    AirPushbackY(3000)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    ResetPushback()
    ResetVerticalDrag()
    ResetGravity()
    Hitstop(7)
    HardKnockdown(1)
    DamageEffect(0, '')
    TriggerUponForState('hzef432_bind', 32)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_21', 4)
    sprite('hz432_22', 4)
    sprite('hz432_23', 4)
    sprite('hz432_24', 2)
    sprite('hz432_25', 2)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-50000)
    YImpulseBeforeWallbounce(0)
    GroundBounce(1)
    BouncePercentage(40)
    sprite('hz432_26', 2)
    sprite('hz432_27', 32767)
    label(1)
    sprite('hz432_28', 3)
    EndMomentum(1)
    SetXCollisionFromOrigin(550)
    CreateObject('UltimateThrowCamera', -1)
    sprite('hz432_29', 3)
    sprite('hz432_30', 3)
    sprite('hz432_31', 3)
    sprite('hz432_32', 3)
    sprite('hz432_33', 3)
    sprite('hz432_34', 2)
    RefreshMultihit()
    AirPushbackY(-50000)
    ResetGravity()
    GroundBounceReset()
    HardKnockdown(1)
    Hitstop(0)
    sprite('hz432_34', 3)
    sprite('hz432_35', 3)
    sprite('hz432_36', 3)
    sprite('hz432_37', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 4)
    sprite('hz432_39', 12)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(57)
    AirPushbackX(300)
    HitsparkSize(500)
    ScreenShake(0, 1000)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_37', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 3)
    sprite('hz432_39', 8)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_37', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 3)
    sprite('hz432_39', 4)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    SLOT_52 = 8
    label(10)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 2)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    SLOT_52 = SLOT_52 + -1
    if not SLOT_52:
        notConditionalSendToLabel(11)
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 2)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_39', 1)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 3)
    RefreshMultihit()
    ScreenShake(0, 1000)
    sprite('hz432_37', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 2)
    sprite('hz432_39', 6)
    RefreshMultihit()
    ScreenShake(1000, 20000)
    sprite('hz432_39', 1)
    sprite('hz432_37', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 4)
    sprite('hz432_39', 12)
    RefreshMultihit()
    ScreenShake(1000, 40000)
    sprite('hz432_37', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 6)
    sprite('hz432_39', 12)
    RefreshMultihit()
    sprite('hz432_37', 5)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_38', 8)
    sprite('hz432_39', 23)
    RefreshMultihit()
    HardKnockdown(180)
    ScreenShake(1000, 80000)
    EnableRapidCancel(0)
    sprite('hz432_39', 1)
    sprite('hz432_40', 6)
    sprite('hz432_41', 8)
    Voiceline('hz257')
    sprite('hz432_42', 8)
    sprite('hz432_43', 8)
    CommonSE('021_bonecleak_1')
    sprite('hz432_41', 8)
    sprite('hz432_42', 8)
    sprite('hz432_43', 8)
    sprite('hz432_41', 8)
    sprite('hz432_42', 8)
    sprite('hz432_43', 8)
    CommonSE('021_bonecleak_1')
    sprite('hz432_41', 8)
    sprite('hz432_42', 8)
    sprite('hz432_43', 8)
    sprite('hz432_41', 8)
    sprite('hz432_42', 8)
    sprite('hz432_43', 8)
    CommonSE('021_bonecleak_1')
    sprite('hz432_41', 16)
    sprite('hz432_41', 8)
    EnableRapidCancel(1)
    sprite('hz432_44', 3)
    CreateObject('hzef432', -1)
    sprite('hz432_45', 3)
    DespawnEAEffect('UltimateThrowCamera')
    CommonSE('005_swing_grap_2_0')
    CommonSE('213_bound_1')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(400)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(7500)
    AirPushbackY(20000)
    HardKnockdown(10)
    Hitstop(8)
    HitsparkSize(1000)
    physicsXImpulse(10000)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()

    def upon_LANDING():
        clearUponHandler(LANDING)
        sendToLabel(2)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_46', 3)
    PrivateSE('hzse_11')
    sprite('hz432_47', 3)
    PrivateSE('hzse_11')
    sprite('hz432_48', 32767)
    PrivateSE('hzse_12')
    label(2)
    sprite('hz432_49', 3)
    CommonSE('005_swing_grap_2_0')
    CommonSE('025_cleanhit_grap')
    CommonSE('025_cleanhit_grap')
    CommonSE('213_bound_1')
    PrivateSE('hzse_12')
    EndMomentum(1)
    RefreshMultihit()
    Damage(800)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Wallstick(1)
    WallstickDuration(30)
    AirHitstunAfterWallbounce(100)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Hitstop(16)
    HardKnockdown(40)
    DefeatOpponentBehavior(0)
    ScreenShake(50000, 50000)
    GotoState('UltimateThrowOD_Finish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('hz432_50', 6)
    SetXCollisionFromOrigin(150)
    sprite('hz432_51', 6)
    sprite('hz432_52', 6)
    sprite('hz432_53', 6)
    sprite('hz432_53ex', 6)
    sprite('hz432_54', 6)
    sprite('hz432_55', 15)
    clearUponHandler(EVERY_FRAME)
    sprite('hz432_56', 7)
    sprite('hz432_57', 7)
    sprite('hz432_58', 7)
    sprite('hz432_59', 7)
    sprite('hz601_17', 7)
    CommonSE('019_cloth_a')
    sprite('hz601_18', 7)
    sprite('hz601_19', 7)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        AirPushbackY(15000)
        AirUntechableTime(60)
        HardKnockdown(60)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
            SLOT_64 = 0
        SLOT_64 = 1
    sprite('hz041_00ex01', 8)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('hz280')
    sprite('hz312_00ex01', 4)
    sprite('hz312_01ex01', 4)
    sprite('hz440_00', 3)
    CreateObject('EffKnifeSignal', 0)
    CommonSE('007_swing_knife_2')
    sprite('hz440_01', 3)
    CreateObject('Eff440Zanzo', -1)
    sprite('hz440_02', 5)
    setInvincible(0)
    sprite('hz440_03', 5)
    sprite('hz440_04', 5)
    sprite('hz312_07ex01', 5)
    sprite('hz440_05', 5)
    sprite('hz440_06', 5)
    sprite('hz000_00', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        AirPushbackY(15000)
        AirUntechableTime(60)
        HardKnockdown(60)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
            SLOT_64 = 0
        SLOT_64 = 1
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('hz041_00ex01', 2)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('hz280')
    sprite('hz312_00ex01', 2)
    sprite('hz312_01ex01', 2)
    sprite('hz440_00', 3)
    CreateObject('EffKnifeSignal', 0)
    CommonSE('007_swing_knife_2')
    sprite('hz440_01', 3)
    CreateObject('Eff440Zanzo', -1)
    sprite('hz440_02', 5)
    setInvincible(0)
    sprite('hz440_03', 5)
    sprite('hz440_04', 5)
    sprite('hz312_07ex01', 5)
    sprite('hz440_05', 5)
    sprite('hz440_06', 5)
    sprite('hz000_00', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(400)
        AirUntechableTime(120)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        CameraNoScreenCollision(1)
        CameraControlEnable(1)
        SetBackground(1)
        uponSendToLabel(LANDING, 2)
        SLOT_64 = 1

        def upon_STATE_END():
            SLOT_64 = 0
    sprite('hz440_02ex01', 5)
    SetXCollisionFromOrigin(300)
    sprite('keep', 1)
    if SLOT_51:
        sendToLabel(100)
    sprite('hz440_07', 8)
    physicsXImpulse(30000)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('hz440_08', 3)
    sprite('hz440_09', 3)
    physicsXImpulse(20000)
    AddX(50000)
    Voiceline('hz281')
    sprite('hz440_10', 3)
    sprite('hz440_11', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(-6000)
    AirPushbackY(8000)
    XImpulseAcceleration(50)
    sprite('hz440_12', 3)
    sprite('hz440_13', 3)
    CreateObject('EffKnifeSignal', 0)
    RefreshMultihit()
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(2000)
    AirPushbackY(30000)
    UseSlashHitspark(1)
    XImpulseAcceleration(0)
    sprite('hz440_14', 3)
    sprite('hz440_15', 3)
    sprite('hz440_16', 3)
    sprite('hz311_10ex01', 3)
    label(0)
    sprite('hz401_00ex01', 3)
    physicsXImpulse(5000)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz401_01ex01', 3)
    physicsYImpulse(20000)
    setGravity(2400)
    CreateObject('Eff440Zanzo_b', -1)
    CommonSE('004_swing_grap_1_2')
    sprite('hz401_02ex01', 3)
    sprite('hz401_03ex01', 3)
    CreateObject('Eff440Zanzo_b2', -1)
    RefreshMultihit()
    AirPushbackY(60000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(8)
    UseSlashHitspark(1)
    sprite('hz401_04ex01', 3)
    sprite('hz401_05ex01', 3)
    XImpulseAcceleration(50)
    SetXCollisionFromOrigin(-1)
    label(1)
    sprite('hz401_06ex01', 2)
    sprite('hz401_07ex01', 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('hz401_08ex01', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('hz401_09ex01', 3)
    sprite('hz405_03ex01', 3)
    sprite('hz440_17', 3)
    sprite('hz440_18', 3)
    CreateObject('KusariBurstDD', 109)
    RegisterObject(4, 1)
    ObjectHitbox(4)
    PrivateSE('hzse_02')
    sprite('hz440_20', 6)
    RefreshMultihit()
    Hitstop(0)
    EnemyHitstopAddition(7, 30, 30)
    sprite('hz440_21', 3)
    ObjectUpon(FALLING, 32)
    sprite('hz440_22', 3)
    sprite('hz405_10ex01', 3)
    sprite('hz405_11ex01', 3)
    sprite('hz405_12ex01', 2)
    AttackOff()
    sprite('hz405_12ex01', 1)
    RefreshMultihit()
    AirPushbackX(-14000)
    AirPushbackY(-60000)
    OppPositionOnHit(3, -300000, 0)
    EnemyHitstopAddition(0, 0, 0)
    HardKnockdown(25)
    AttackDirection(0)
    HitAnywhere(1)
    EnableCollision(0)
    sprite('hz405_13ex01', 5)
    sprite('hz405_14ex01', 5)
    sprite('hz405_15ex01', 5)
    sprite('hz405_15ex02', 20)
    ScreenShake(3000, 15000)
    sprite('hz405_16ex01', 3)
    sprite('hz440_23', 3)
    if SLOT_44:
        if SLOT_51:
            Voiceline('hz282')
        else:
            Voiceline('hz281')
    else:
        Voiceline('hz282')
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(3)
    sprite('hz440_24', 4)
    CreateObject('Eff440snake', -1)
    PrivateSE('hzse_08')
    CommonSE('006_swing_blade_2')
    CommonSE('103_hit_counter_slash_0')
    RefreshMultihit()
    Damage(1000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(16000)
    AirPushbackY(55000)
    YImpulseBeforeWallbounce(2400)
    Hitstop(7)
    HardKnockdown(-1)
    OppPositionOnHit(0, 0, 0)
    AttackDirection(1)
    DefeatOpponentBehavior(0)
    EnableCollision(1)

    def upon_OPPONENT_HIT():
        ScreenShake(2000, 10000)
    sprite('hz440_25', 2)
    sprite('hz440_25ex01', 2)
    sprite('hz440_25ex02', 2)
    sprite('hz440_25', 3)
    sprite('hz440_25ex01', 3)
    sprite('hz440_25ex02', 3)
    sprite('hz440_25', 3)
    sprite('hz440_25ex01', 3)
    sprite('hz440_25ex02', 3)
    loopRest()
    gotoLabel(9)
    label(3)
    sprite('hz440_24', 1)
    PrivateSE('hzse_08')
    CommonSE('006_swing_blade_2')
    CommonSE('103_hit_counter_slash_2')
    RefreshMultihit()
    Damage(700)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackX(4000)
    AirPushbackY(55000)
    YImpulseBeforeWallbounce(2400)
    Hitstop(7)
    HardKnockdown(-1)
    OppPositionOnHit(0, 0, 0)
    AttackDirection(1)
    EnemyHitstopAddition(-2, -2, -2)
    EnableCollision(1)

    def upon_OPPONENT_HIT():
        ScreenShake(2000, 10000)
    CreateObject('HZEF_UltimateAssault', -1)

    def RunOnObject_1():
        AddX(-390000)
    CreateObject('HZEF_UltimateAssaultOD', -1)

    def RunOnObject_1():
        AddX(-390000)
    sprite('hz440_25', 2)
    RefreshMultihit()
    sprite('hz440_25ex01', 2)
    RefreshMultihit()
    sprite('hz440_25ex02', 2)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    sprite('hz440_25', 3)
    sprite('hz440_25ex01', 3)
    sprite('hz440_25ex02', 3)
    sprite('hz440_25', 3)
    sprite('hz440_25ex01', 3)
    sprite('hz440_25ex02', 3)
    sprite('hz440_25', 3)
    sprite('hz440_25ex01', 3)
    sprite('hz440_25ex02', 3)
    label(9)
    sprite('hz440_26', 4)
    sprite('hz440_27', 4)
    sprite('hz440_28', 4)
    sprite('hz440_29', 4)
    sprite('hz440_30', 4)
    sprite('hz440_31', 4)
    sprite('hz440_32', 4)
    sprite('hz440_33', 4)
    sprite('hz000_00', 1)
    Flip()


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_AirAstral()
        DamageFromStateOnly('AstralHeat')
        AttackLevel_(3)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        MinimumDamage(100)
        setInvincible(1)
        EndMomentum(1)

        def upon_32():
            PlayPlayAstralBGM(0)
            SetActionMark(1)
    sprite('hz450_00', 4)
    SmartVoiceline('hz290')
    DistortionSettings(46, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_AST', -1)
    SetBackground(2)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    sprite('hz450_01', 6)
    sprite('hz450_02', 6)
    sprite('hz450_03', 25)
    sprite('hz450_04', 6)
    sprite('hz450_05', 6)
    sprite('hz450_06', 3)
    sprite('hz450_07', 3)
    sprite('hz450_08', 3)
    CreateObject('HZEF_ASTBACK', -1)
    CreateObject('HZEF_ASTMagicCircle', -1)
    CommonSE('015_blaze_1')
    sprite('hz450_09', 3)
    CreateObject('KusariAstral', 0)
    ObjectUpon(STATE_END, 32)
    CommonSE('019_quake_0')
    PrivateSE('hzse_06')
    sprite('hz450_10', 3)
    CreateObject('KusariAstral', 1)
    ObjectUpon(STATE_END, 33)
    sprite('hz450_11', 3)
    CreateObject('KusariAstral', 2)
    ObjectUpon(STATE_END, 34)
    sprite('hz450_12', 3)
    CreateObject('KusariAstral', 3)
    ObjectUpon(STATE_END, 35)
    PrivateSE('hzse_06')
    sprite('hz450_13', 3)
    CreateObject('KusariAstral', 4)
    ObjectUpon(STATE_END, 36)
    sprite('hz450_09', 3)
    CreateObject('KusariAstral', 5)
    ObjectUpon(STATE_END, 37)
    sprite('hz450_10', 3)
    CreateObject('KusariAstral', 6)
    ObjectUpon(STATE_END, 38)
    sprite('hz450_11', 3)
    CreateObject('KusariAstral', 7)
    ObjectUpon(STATE_END, 39)
    sprite('hz450_12', 3)
    sprite('hz450_13', 3)
    sprite('hz450_09', 3)
    CommonSE('019_quake_0')
    sprite('hz450_10', 3)
    sprite('hz450_11', 3)
    sprite('hz450_12', 3)
    sprite('hz450_13', 3)
    sprite('hz450_09', 3)
    sprite('hz450_10', 3)
    sprite('hz450_11', 3)
    sprite('hz450_12', 3)
    sprite('hz450_13', 3)
    sprite('hz450_09', 3)
    sprite('hz450_10', 3)
    sprite('hz450_11', 3)
    sprite('hz450_12', 3)
    sprite('hz450_13', 3)
    TriggerUponForState('KusariAstral', 41)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('hz450_23', 4)
    setInvincible(0)
    TriggerUponForState('KusariAstral', 40)
    sprite('hz450_24', 4)
    sprite('hz450_25', 4)
    sprite('hz450_26', 4)
    sprite('hz450_27', 4)
    sprite('hz450_28', 4)
    loopRest()
    ExitState()
    label(0)
    HUDVisibillity(1)
    CameraControlInfinity(1)
    CameraWinnerControlStop(1)
    SetBackground(3)
    TriggerUponForState('HZEF_ASTBACK', 32)
    sprite('hz450_14', 3)
    random_(2, 0, 50)
    SLOT_55 = SLOT_0
    if SLOT_55:
        Voiceline('hz291')
    else:
        Voiceline('hz293')
    CommonSE('019_quake_0')
    sprite('hz450_15', 3)
    AstralHeatCleanup(1, 1)
    SLOT_66 = 1
    ObjectUpon(5, 32)
    sprite('hz450_16', 3)
    CreateObject('HZEF_ASTSIGNAL', -1)
    sprite('hz450_17', 3)
    TriggerUponForState('KusariAstral', 40)
    loopRest()
    RunLoopUpon(17, 350)
    uponSendToLabel(17, 2)
    sprite('hz450_18', 6)
    PrivateSE('hzse_00')
    PrivateSE('hzse_05')
    CreateObject('AST_Enshutsu', -1)
    sprite('hz450_19', 6)
    sprite('hz450_20', 6)
    sprite('hz450_21', 6)
    sprite('hz450_22', 6)
    BlendMode_Normal()
    ConstantAlphaModifier(-1)
    loopRest()
    sprite('hz450_18', 6)
    sprite('hz450_19', 6)
    sprite('hz450_20', 6)
    PrivateSE('hzse_08')
    CommonSE('015_blaze_0')
    CommonSE('019_quake_0')
    sprite('hz450_21', 6)
    CommonSE('019_quake_1')
    PrivateSE('hzse_08')
    sprite('hz450_22', 6)
    CommonSE('019_quake_0')
    loopRest()
    label(1)
    sprite('hz450_18', 6)
    CommonSE('019_quake_1')
    sprite('hz450_19', 6)
    CommonSE('019_quake_0')
    sprite('hz450_20', 6)
    CommonSE('019_quake_1')
    sprite('hz450_21', 6)
    CommonSE('019_quake_0')
    sprite('hz450_22', 6)
    CommonSE('019_quake_1')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('null', 40)
    ConstantAlphaModifier(0)
    CommonSE('019_quake_0')
    sprite('null', 40)
    CommonSE('019_quake_0')
    sprite('null', 40)
    if SLOT_55:
        Voiceline('hz292')
    else:
        Voiceline('hz294')
    CommonSE('019_quake_0')
    sprite('null', 40)
    CommonSE('019_quake_0')
    sprite('null', 40)
    PrivateSE('hzse_07')
    CommonSE('019_quake_0')
    sprite('null', 40)
    CommonSE('019_quake_0')
    sprite('null', 35)
    PrivateSE('hzse_03')
    PrivateSE('hzse_06')
    PrivateSE('hzse_08')
    label(99)
    DefeatOpponentBehavior(3)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(100000)
    AirPushbackX(0)
    AirUntechableTime(666)
    Damage(30000)
    Hitstop(10)
    PushbackX(0)
    HitAnywhere(1)
    sprite('hz450_lastatk', 10)
    sprite('hz620_00', 20)
    CreateObject('HZAST_BlackOut', -1)
    SetBackground(0)
    sprite('hz620_00', 40)
    CameraFast(1)
    loopRest()
    WinAction()
    DemoTimer(320)
    BlendMode_Off()
    AlphaValue(255)
    XPositionRelativeFacing(0)
    SetZVal(500)

    def RunOnObject_22():
        Flip()
        EndMomentum(1)
        XPositionRelativeFacing(0)
        AddX(280000)
        AbsoluteY(2560000)
        physicsXImpulse(1000)
        GravityDefault()
    sprite('hz001_00', 6)
    sprite('hz001_01', 6)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz611_00', 4)
    sprite('hz611_01', 10)
    sprite('hz611_02', 4)
    CommonSE('019_cloth_a')
    sprite('hz611_03', 4)
    sprite('hz611_04', 4)
    sprite('hz611_05', 4)
    sprite('hz611_06', 4)
    sprite('hz611_07', 4)
    sprite('hz611_08', 6)
    Voiceline('hz408')
    DemoTimer(200)
    loopRest()
    label(100)
    sprite('hz611_09', 6)
    sprite('hz611_10', 6)
    sprite('hz611_11', 6)
    loopRest()
    gotoLabel(100)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('hz054')
    sprite('hz900_00', 32767)
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
    CreateObject('RLAstLockmc', 0)
    CreateObject('RLAstLockAura', 0)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(250000)
    sprite('hz901_00', 50)
    physicsYImpulse(-150)
    sprite('hz901_00', 50)
    physicsYImpulse(150)
    Voiceline('hz055')
    Mouth(13665, 13667, 13665, 13155, 24880, 25397, 24885, 25397, 24885, 
        25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('hz901_00', 50)
    physicsYImpulse(-150)
    sprite('hz901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('hz000', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 24880, 12337, 12643, 24880, 12337, 12643, 48, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz257', 13923, 12641, 25400, 12849, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
        13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('hz261', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz307', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz400', 12643, 24880, 12339, 12643, 24886, 12337, 12643, 
        24880, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz401', 13411, 12641, 25392, 12337, 14433, 14435, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14435, 
        14433, 14435, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz404', 14177, 14179, 14177, 14179, 13921, 13923, 13921, 
        13923, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz405', 14177, 14179, 14177, 14179, 13921, 13923, 13921, 
        13923, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz406', 12643, 24880, 12338, 12643, 24880, 12337, 12643, 
        24880, 12337, 12899, 24880, 13617, 13667, 12641, 25397, 24885, 
        12338, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('hz407', 13667, 13665, 13667, 12897, 25392, 12337, 12641, 
        25392, 12337, 12641, 25392, 12337, 12641, 25392, 12337, 12641, 
        25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz408', 14435, 12641, 25392, 24888, 25400, 24888, 25400, 
        24888, 12337, 14435, 12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz411', 14689, 14691, 14689, 13155, 24885, 25400, 24888, 
        25400, 24888, 12337, 12643, 24880, 12849, 14435, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz412', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 24880, 12337, 13923, 12641, 25392, 12337, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz414', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 25398, 24884, 25400, 24888, 25400, 24888, 12337, 12643, 
        12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('hz415', 13411, 13665, 13667, 12641, 25394, 13873, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 14435, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('hz416', 14691, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('hz417', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('hz000', 13411, 12641, 25392, 12337, 12641, 25392, 
            12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz257', 13923, 12641, 25400, 12849, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz261', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz307', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz400', 12899, 12641, 25392, 12337, 14433, 14435, 
            13921, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz401', 12643, 24880, 12337, 12643, 24880, 12337, 
            13667, 12641, 25392, 24886, 13873, 12643, 48, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('hz404', 12641, 25398, 24888, 25400, 24888, 25400, 
            24888, 12337, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz405', 12641, 25392, 12337, 12641, 25392, 12337, 
            14433, 14435, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz406', 13923, 12641, 25392, 12337, 12641, 25392, 
            12339, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz407', 12641, 25392, 12337, 14433, 12643, 24880, 
            12337, 13923, 12641, 25392, 24886, 12337, 13923, 12641, 25392, 
            24886, 13361, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz408', 14433, 14435, 14433, 14435, 14433, 12899, 
            24887, 25400, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 
            25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz411', 12899, 24880, 13873, 12643, 24880, 25400, 
            13875, 12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('hz412', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 13873, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz414', 12641, 25394, 24888, 12849, 14435, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 12899, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz415', 12643, 24880, 12337, 12643, 24880, 12337, 
            13411, 24880, 12337, 12643, 24880, 12337, 13411, 24880, 25400, 
            56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz416', 14691, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz417', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 12641, 25394, 12337, 12641, 25394, 12337, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
    if SLOT_45:
        Unknown18011('hz000', 14177, 14179, 14689, 12643, 24880, 12337, 
            14435, 12641, 25394, 14388, 12641, 25392, 12337, 12641, 25392, 
            12337, 12641, 25396, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz257', 13923, 13921, 13923, 13921, 12643, 24882, 
            25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
            24886, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz261', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz307', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz400', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 12641, 25395, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz406', 13921, 13411, 12641, 25392, 24886, 25398, 
            13875, 13921, 13923, 13921, 13923, 13921, 14435, 12641, 25394, 
            24886, 12337, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz407', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 12899, 24887, 12337, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz408', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 12641, 25394, 12850, 14433, 
            12899, 24883, 25398, 24884, 25398, 24884, 25398, 24884, 25398, 
            24884, 12337, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )
        Unknown18011('hz411', 12641, 25392, 24886, 25398, 24886, 12337, 
            13923, 13921, 13923, 13409, 13411, 13409, 13411, 12641, 25400, 
            54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz412', 12643, 24880, 12337, 12643, 24880, 12337, 
            13411, 12641, 25392, 24884, 12337, 13411, 12641, 25392, 24884, 
            12337, 13411, 12641, 25392, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz414', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 12897, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('hz416', 12643, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('hz417', 12641, 25392, 24888, 12337, 14435, 12641, 
            25392, 24888, 12337, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('tm'):
            Unknown18011('hz000', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 12897, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('hz400', 13921, 13923, 13921, 13155, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz401', 12641, 25392, 12339, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 
                12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('hz000', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 12897, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('hz400', 14433, 13923, 14433, 13155, 24880, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('hz401', 13923, 13921, 13923, 13921, 13923, 13921,
                13411, 24880, 12337, 13923, 12641, 25392, 24886, 12337, 
                13923, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('hz000', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 12897, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('hz400', 13921, 13923, 13921, 13155, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz401', 12641, 25392, 12339, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 
                12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('hz504', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('hz505', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13155, 24885, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('hz504', 14177, 14179, 14177, 13411, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('hz505', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 12899, 24884,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('hz524', 13921, 13923, 13921, 13155, 24880, 25398,
                24886, 25398, 12343, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('hz525', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('hz524', 14177, 14179, 14177, 14179, 14177, 
                    13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('hz525', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 12641, 25394, 12341,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('hz530', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('hz531', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 
                24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('hz530', 12643, 12340, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('hz531', 14177, 14179, 14177, 14179, 14177, 
                    13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('hz536', 14179, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz537', 12641, 25392, 24887, 12337, 14179, 14177,
                14179, 14177, 13155, 24880, 12337, 14179, 12641, 25392, 
                24887, 12337, 14179, 12641, 25392, 24887, 12337, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('hz546', 14179, 14177, 14179, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz547', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14177, 14179, 14177, 14179, 
                14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('tm'):
            if SLOT_138:
                Unknown18011('hz550', 13921, 13923, 13921, 13923, 24880, 
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 13617, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('hz551', 12641, 25392, 24887, 12337, 14179, 
                    12641, 25392, 24887, 12337, 14179, 12641, 25392, 24887,
                    12337, 14179, 12641, 25392, 24887, 12337, 14179, 12641,
                    25392, 24887, 12337, 14179, 12641, 25392, 12342, 12641,
                    25392, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0)
            else:
                Unknown18011('hz550', 12897, 25392, 13617, 14177, 13667, 
                    24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398,
                    24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398,
                    24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('hz551', 13665, 13667, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14433, 14435, 12641, 25396, 14386,
                    14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396,
                    24886, 13361, 13923, 14177, 14179, 12641, 25396, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_140:
                    Unknown18011('hz550', 14177, 14179, 14177, 14179, 14177,
                        14179, 14177, 14179, 14177, 13923, 24880, 25399, 
                        24887, 25399, 24887, 25399, 12338, 14177, 14179, 
                        14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                        )
                    Unknown18011('hz551', 14177, 14179, 14177, 14179, 14177,
                        13667, 24880, 25399, 24887, 25399, 24887, 25399, 
                        24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                        25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hb'):
            Unknown18011('hz556', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 13923, 24880, 25400, 24886, 25400, 24886, 
                25400, 24886, 25400, 24886, 25400, 24886, 25400, 24886, 
                25400, 24886, 25400, 24886, 25400, 24886, 13617, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz557', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('hz558', 14433, 13923, 14433, 13923, 14433, 13923,
                24880, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('hz559', 12641, 25397, 13617, 12641, 25392, 13620,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('hz562', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 12641, 25397, 12341, 14177, 14179, 14177, 
                14179, 14177, 14179, 13921, 13923, 13921, 13923, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz563', 14433, 14435, 14433, 13667, 13665, 13411,
                13665, 13411, 13665, 13667, 12641, 25394, 24887, 25399, 
                24887, 25398, 24886, 25399, 24887, 12338, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('hz564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                12641, 25394, 13619, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('hz565', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if SLOT_IsUnlimited:
        conditionalSendToLabel(99)
    if CharacterIDCheck('su'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('tb'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2220)
        else:
            gotoLabel(220)
    if CharacterIDCheck('mk'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2250)
        else:
            gotoLabel(250)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('tm'):
        if SLOT_138:
            gotoLabel(350)
        elif SLOT_139:
            gotoLabel(1350)
        else:
            gotoLabel(2350)
    if CharacterIDCheck('hb'):
        SyncEntry()
        gotoLabel(380)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(410)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(1)
    if random_(2, 0, 50):
        conditionalSendToLabel(5)
    label(0)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('hz600_00', 20)
    Voiceline('hz412')
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(1)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('hz601_00', 5)
    Voiceline('hz414')
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    label(2)
    sprite('hz601_12', 5)
    if SLOT_97:
        conditionalSendToLabel(2)
    sprite('hz601_12', 16)
    if SLOT_45:
        conditionalSendToLabel(4)
    sprite('hz601_12', 1)
    Voiceline('hz415')
    label(3)
    sprite('hz601_12', 5)
    if SLOT_97:
        conditionalSendToLabel(3)
    label(4)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(5)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(5)
    sprite('hz600_00', 1)
    Voiceline('hz416')
    label(6)
    sprite('hz600_00', 5)
    if SLOT_97:
        conditionalSendToLabel(6)
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    Voiceline('hz417')
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(99)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(99)
    sprite('hz213_00', 8)
    sprite('hz213_01', 8)
    sprite('hz213_02', 8)
    Voiceline('hz302')
    CreateObject('ModelMagicCircle1', -1)
    sprite('hz213_03', 8)
    ParticleColor(4278255360, 4278255360, 4278255360)
    ParticleSize(1500)
    CallCustomizableParticle('rgef431handpow', 0)
    DistortionSettings(1, -1, 0)
    E0EAEffect('aura', 65535)
    SetBackground(1)
    KeepBackground(1)
    label(199)
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    if SLOT_97:
        conditionalSendToLabel(199)
    sprite('hz213_03', 15)
    Voiceline('hz303')
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_03', 15)
    ScreenShake(0, 8000)
    CommonSE('019_quake_0')
    sprite('hz213_04', 2)
    ScreenShake(20000, 20000)
    sprite('hz213_04', 3)
    PrivateSE('hzse_rg01')
    PrivateSE('hzse_rg02')
    PrivateSE('hzse_rg03')
    sprite('hz213_05', 5)
    CreateParticle('rgef_bkkakusan', -1)
    CreateObject('HZEF_BBStart', -1)
    if SLOT_IsUnlimited:
        if not CheckObjectPresence(5):
            CreateObject('HZEF_DrainField', -1)
            RegisterObject(5, 1)
    sprite('hz213_06', 5)
    sprite('hz213_07', 5)
    sprite('hz213_08', 5)
    sprite('hz213_06', 5)
    sprite('hz213_07', 5)
    sprite('hz213_08', 5)
    sprite('hz213_09', 5)
    sprite('hz213_10', 5)
    sprite('hz213_11', 5)
    sprite('hz213_12', 5)
    sprite('hz213_13', 5)
    SetBackground(0)
    KeepBackground(0)
    loopRest()
    ExitState()
    label(120)
    sprite('hz602_00', 5)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(120)
    sprite('hz602_00', 360)
    Voiceline('hz504')
    label(121)
    sprite('hz602_00', 8)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(121)
    sprite('hz602_01', 8)
    sprite('hz602_02', 8)
    sprite('hz602_03', 8)
    sprite('hz602_04', 8)
    sprite('hz602_05', 8)
    sprite('hz602_06', 8)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(2120)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2120)
    label(2121)
    sprite('hz600_00', 20)
    sprite('hz600_00', 200)
    Voiceline('hz504')
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(220)
    uponSendToLabel(32, 222)
    label(221)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(221)
    label(222)
    sprite('hz300_00', 6)
    clearUponHandler(32)
    Voiceline('hz524')
    DemoTimer(350)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 45)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    sprite('hz601_00', 5)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 60)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    loopRest()
    ExitState()
    label(2220)
    sprite('keep', 2)
    uponSendToLabel(32, 2222)
    label(2221)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(2221)
    label(2222)
    sprite('hz610_00', 7)
    sprite('hz610_01', 7)
    Voiceline('hz524')
    sprite('hz610_06', 7)
    sprite('hz610_07', 7)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 180)
    sprite('hz610_08', 6)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(250)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(250)
    sprite('hz300_00', 6)
    Voiceline('hz530')
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 180)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2250)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2250)
    sprite('hz600_00', 150)
    Voiceline('hz530')
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    DemoTimer(30)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    uponSendToLabel(32, 282)
    label(281)
    sprite('hz600_00', 6)
    loopRest()
    gotoLabel(281)
    label(282)
    sprite('hz600_00', 80)
    clearUponHandler(32)
    Voiceline('hz536')
    DemoTimer(300)
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    loopRest()
    ExitState()
    label(330)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(330)
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    Voiceline('hz546')
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    loopRest()
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz300_00', 6)
    Voiceline('hz530')
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 100)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(350)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(350)
    sprite('hz300_00', 6)
    Voiceline('hz550')
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 120)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(1350)
    sprite('hz000_00', 8)
    uponSendToLabel(32, 1351)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(1350)
    label(1351)
    sprite('hz601_00', 5)
    Voiceline('hz550')
    clearUponHandler(32)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 180)
    sprite('hz601_13', 6)
    ObjectUpon(22, 32)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    loopRest()
    ExitState()
    label(2350)
    sprite('hz000_00', 8)
    uponSendToLabel(32, 2351)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(2350)
    label(2351)
    sprite('hz601_00', 5)
    Voiceline('hz550')
    clearUponHandler(32)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 180)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(380)
    uponSendToLabel(32, 382)
    label(381)
    sprite('hz600_00', 6)
    loopRest()
    gotoLabel(381)
    label(382)
    sprite('hz600_00', 6)
    clearUponHandler(32)
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    Voiceline('hz556')
    DemoTimer(300)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    loopRest()
    sprite('hz300_00', 6)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 100)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(390)
    sprite('hz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(390)
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    uponSendToLabel(32, 392)
    loopRest()
    label(391)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(391)
    label(392)
    sprite('hz300_00', 6)
    Voiceline('hz558')
    DemoTimer(300)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 200)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    ExitState()
    label(410)
    sprite('null', 1)
    AddX(-700000)
    ScreenCollision(0)
    EnableCollision(0)
    uponSendToLabel(32, 414)
    label(411)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(411)
    sprite('hz030_00', 7)
    physicsXImpulse(5600)
    sprite('hz030_01', 7)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 780000:
            ObjectUpon(22, 32)
        if SLOT_19 <= 520000:
            clearUponHandler(EVERY_FRAME)
            XPositionRelativeFacing(-260000)
            EndMomentum(1)
            sendToLabel(413)
    label(412)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(412)
    label(413)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(413)
    label(414)
    sprite('hz601_00', 5)
    Voiceline('hz562')
    clearUponHandler(32)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 210)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    loopRest()
    ExitState()
    label(420)
    sprite('hz600_00', 6)
    uponSendToLabel(32, 421)
    sprite('hz600_00', 32767)
    loopRest()
    label(421)
    sprite('hz600_00', 50)
    sprite('hz600_00', 20)
    Voiceline('hz564')
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    DemoTimer(45)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    ExitState()


@State
def EntrySeqVsRg():
    AttackDefaults_StandingNormal()
    XPositionRelativeFacing(-1200000)
    ScreenCollision(0)
    AttackLevel_(4)
    setInvincible(1)
    clearUponHandler(32)
    uponSendToLabel(32, 22)
    label(20)
    sprite('null', 1)
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('hz030_00', 7)
    physicsXImpulse(6200)
    sprite('hz030_01', 7)
    label(21)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(21)
    label(22)
    clearUponHandler(32)
    uponSendToLabel(LANDING, 24)
    sprite('hz033_00', 2)
    EndMomentum(1)
    sprite('hz033_01', 2)
    SmartVoiceline('hz005')
    physicsXImpulse(-14000)
    physicsYImpulse(8800)
    setGravity(2200)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(23)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(23)
    label(24)
    physicsXImpulse(0)
    physicsYImpulse(0)
    uponSendToLabel(32, 26)
    label(25)
    sprite('hz000_00', 1)
    loopRest()
    gotoLabel(25)
    label(26)
    clearUponHandler(32)
    sprite('hz202_00', 1)
    sprite('hz202_01', 1)
    sprite('hz202_02', 2)
    CreateObject('EffKnifeSignal', 0)
    CreateObject('EffKnifeSignal', 1)
    sprite('hz202_03', 2)
    sprite('hz202_04', 3)
    RefreshMultihit()
    sprite('hz202_05', 1)
    CommonSE('007_swing_knife_2')
    CommonSE('004_swing_grap_1_0')
    CreateObject('Eff5CZanzo', -1)
    sprite('hz202_05', 1)
    StartMultihit()
    sprite('hz202_06', 2)
    physicsXImpulse(-15000)
    SetAcceleration(800)
    sprite('hz202_07', 2)
    sprite('hz202_08', 1)
    sprite('hz202_09', 1)
    sprite('hz202_10', 1)
    sprite('hz202_11', 1)
    sprite('hz202_12', 1)
    sprite('hz202_13', 1)
    physicsXImpulse(0)
    SetAcceleration(0)
    loopRest()
    uponSendToLabel(32, 28)
    label(27)
    sprite('hz000_00', 1)
    loopRest()
    gotoLabel(27)
    label(28)
    clearUponHandler(32)
    sprite('hz232_03', 2)
    CreateObject('EffKnifeSignal', 0)
    sprite('hz232_04', 1)
    sprite('hz232_04', 3)
    RefreshMultihit()
    CreateObject('Eff2CZanzo', -1)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    physicsXImpulse(-15000)
    SetAcceleration(800)
    sprite('hz232_04', 2)
    sprite('hz232_05', 2)
    sprite('hz232_06', 2)
    sprite('hz232_07', 2)
    sprite('hz232_08', 2)
    sprite('hz232_09', 2)
    sprite('hz232_10', 2)
    sprite('hz232_11', 2)
    sprite('hz232_12', 2)
    physicsXImpulse(0)
    SetAcceleration(0)
    sprite('hz232_13', 2)
    loopRest()
    uponSendToLabel(32, 1030)
    label(29)
    sprite('hz010_02', 1)
    gotoLabel(29)
    label(1030)
    clearUponHandler(32)
    uponSendToLabel(LANDING, 1032)
    sprite('hz430_00', 5)
    sprite('hz430_00', 35)
    DistortionSettings(40, -1, 4)
    HeatChange(-5000)
    HeatCooldown(420)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('EffUltimateAssaultBunshinA', -1)
    CreateObject('EffUltimateAssaultBunshinB', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-10)
    sprite('hz430_01', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(50000)
    ConstantAlphaModifier(150)
    sprite('hz430_02', 3)
    XImpulseAcceleration(25)
    sprite('hz430_03', 3)
    XImpulseAcceleration(25)
    sprite('hz430_04', 3)
    RefreshMultihit()
    XImpulseAcceleration(25)
    CommonSE('004_swing_grap_1_2')
    AltKnockdownEffects(100, 1, 1)
    CreateObject('HZEF_UltimateAssault', -1)
    sprite('hz430_05', 10)
    PrivateSE('hzse_14')
    sprite('hz430_06', 5)
    physicsYImpulse(8000)
    sprite('hz430_07', 5)
    GravityDefault()
    sprite('hz430_08', 5)
    label(1031)
    sprite('hz430_09', 5)
    loopRest()
    gotoLabel(1031)
    label(1032)
    sprite('hz430_10', 3)
    XImpulseAcceleration(0)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('hz430_11', 3)
    sprite('hz430_12', 3)
    sprite('hz430_13', 3)
    sprite('hz430_14', 3)
    sprite('hz430_15', 4)
    sprite('hz430_16', 4)
    sprite('hz430_17', 4)
    sprite('hz430_18', 4)
    EndAttack()
    if SLOT_45:
        uponSendToLabel(32, 1034)
    else:
        gotoLabel(1034)
    sprite('hz000_00', 1)
    ObjectUpon(22, 32)
    loopRest()
    label(1033)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(1033)
    label(1034)
    clearUponHandler(32)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz300_00', 6)
    if SLOT_45:
        Voiceline('hz700')
        DemoTimer(140)
    else:
        Voiceline('hz500')
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    label(1035)
    sprite('hz300_06', 6)
    if SLOT_97:
        conditionalSendToLabel(1035)
    sprite('hz300_07', 6)
    ObjectUpon(22, 32)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()


@State
def CmnActRoundWin():
    sprite('hz615_00', 6)
    sprite('hz615_01', 6)
    sprite('hz615_02', 6)
    sprite('hz615_03', 6)
    loopRest()
    if SLOT_45:
        Voiceline('hz400')
        gotoLabel(1)
    if random_(2, 0, 50):
        Voiceline('hz400')
    else:
        Voiceline('hz401')
    label(1)
    sprite('hz615_04', 8)
    DemoEndOnVoiceEnd(1)
    sprite('hz615_05', 20)
    sprite('hz615_05', 32767)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('no'):
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('tb'):
        if SLOT_140:
            gotoLabel(2220)
        else:
            gotoLabel(220)
    if CharacterIDCheck('mk'):
        if SLOT_140:
            gotoLabel(2250)
        else:
            gotoLabel(250)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(280)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('tm'):
        if SLOT_138:
            gotoLabel(350)
        elif SLOT_139:
            gotoLabel(1350)
        else:
            gotoLabel(2350)
    if CharacterIDCheck('hb'):
        conditionalSendToLabel(380)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('mi'):
        if SLOT_138:
            gotoLabel(410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if SLOT_109:
        conditionalSendToLabel(1)
    if random_(2, 0, 33):
        conditionalSendToLabel(1)
    if random_(2, 0, 50):
        conditionalSendToLabel(3)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz407')
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    DemoTimer(120)
    label(1)
    sprite('hz001_00', 6)
    sprite('hz001_01', 6)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz611_00', 4)
    sprite('hz611_01', 10)
    sprite('hz611_02', 4)
    CommonSE('019_cloth_a')
    sprite('hz611_03', 4)
    sprite('hz611_04', 4)
    sprite('hz611_05', 4)
    sprite('hz611_06', 4)
    sprite('hz611_07', 4)
    sprite('hz611_08', 6)
    Voiceline('hz408')
    DemoEndOnVoiceEnd(1)
    label(2)
    sprite('hz611_09', 6)
    sprite('hz611_10', 6)
    sprite('hz611_11', 6)
    loopRest()
    gotoLabel(2)
    label(3)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(5)
    sprite('hz030_00', 7)
    sprite('hz030_01', 7)
    label(4)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(4)
    label(5)
    physicsXImpulse(0)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz406')
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(6)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(6)
    sprite('hz612_06', 1)
    DemoTimer(30)
    label(7)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(7)
    label(120)
    sprite('hz001_00', 6)
    sprite('hz001_01', 6)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz611_00', 4)
    sprite('hz611_01', 10)
    sprite('hz611_02', 4)
    CommonSE('019_cloth_a')
    sprite('hz611_03', 4)
    sprite('hz611_04', 4)
    sprite('hz611_05', 4)
    sprite('hz611_06', 4)
    sprite('hz611_07', 4)
    sprite('hz611_08', 6)
    Voiceline('hz505')
    DemoEndOnVoiceEnd(1)
    label(121)
    sprite('hz611_09', 6)
    sprite('hz611_10', 6)
    sprite('hz611_11', 6)
    loopRest()
    gotoLabel(121)
    label(2120)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2122)
    sprite('hz030_00', 7)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    sprite('hz030_01', 7)
    label(2121)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(2121)
    label(2122)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz505')
    DemoEndOnVoiceEnd(1)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(2124)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(2124)
    label(220)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz525')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(2220)
    sprite('keep', 1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2222)
    sprite('hz030_00', 7)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    sprite('hz030_01', 7)
    label(2221)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(2221)
    label(2222)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz525')
    DemoEndOnVoiceEnd(1)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(2223)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(2223)
    label(250)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz531')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(2250)
    sprite('hz610_00', 6)
    sprite('hz610_06', 7)
    sprite('hz610_07', 7)
    Voiceline('hz531')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 32767)
    loopRest()
    label(280)
    if SLOT_109:
        conditionalSendToLabel(482)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(282)
    sprite('hz030_00', 7)
    sprite('hz030_01', 7)
    label(281)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(281)
    label(282)
    physicsXImpulse(0)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz537')
    DemoEndOnVoiceEnd(1)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(283)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(283)
    label(330)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz547')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(350)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz551')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(1350)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz551')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(2350)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz551')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(380)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz557')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(390)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    Voiceline('hz559')
    DemoEndOnVoiceEnd(1)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    sprite('hz610_10', 32767)
    loopRest()
    label(410)
    if SLOT_109:
        conditionalSendToLabel(482)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(412)
    sprite('hz030_00', 7)
    sprite('hz030_01', 7)
    label(411)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(411)
    label(412)
    physicsXImpulse(0)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz563')
    DemoEndOnVoiceEnd(1)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(413)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(413)
    label(1410)
    if SLOT_109:
        conditionalSendToLabel(482)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(1412)
    sprite('hz030_00', 7)
    sprite('hz030_01', 7)
    label(1411)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(1411)
    label(1412)
    physicsXImpulse(0)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    Voiceline('hz563')
    DemoEndOnVoiceEnd(1)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    label(1413)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(1413)
    label(420)
    sprite('hz001_00', 6)
    sprite('hz001_01', 6)
    sprite('hz001_02', 8)
    Voiceline('hz565')
    DemoEndOnVoiceEnd(1)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz611_00', 4)
    sprite('hz611_01', 10)
    sprite('hz611_02', 4)
    CommonSE('019_cloth_a')
    sprite('hz611_03', 4)
    sprite('hz611_04', 4)
    sprite('hz611_05', 4)
    sprite('hz611_06', 4)
    sprite('hz611_07', 4)
    sprite('hz611_08', 6)
    label(421)
    sprite('hz611_09', 6)
    sprite('hz611_10', 6)
    sprite('hz611_11', 6)
    loopRest()
    gotoLabel(421)


@State
def CmnActLose():
    sprite('hz620_00', 7)
    Voiceline('hz411')
    sprite('hz620_01', 7)
    sprite('hz620_02', 7)
    sprite('hz620_03', 4)
    sprite('hz620_04', 4)
    sprite('hz620_05', 4)
    sprite('hz620_06', 7)
    sprite('hz620_07', 7)
    sprite('hz620_08', 7)
    DemoTimer(90)
    label(0)
    sprite('hz620_02', 7)
    sprite('hz620_03', 4)
    sprite('hz620_04', 4)
    sprite('hz620_05', 4)
    sprite('hz620_06', 7)
    sprite('hz620_07', 7)
    sprite('hz620_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWait():
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
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
    sprite('hz620_05', 32767)


@State
def EventDefDown():
    sprite('hz060_14', 32767)


@State
def EventHZCenterWait():
    sprite('keep', 2)
    XPositionRelativeFacing(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventAdjustTie():
    sprite('hz001_00', 6)
    sprite('hz001_01', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_06', 6)
    sprite('hz001_07', 6)
    sprite('hz001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefEntryWalkIn():
    EnableCollision(0)
    ScreenCollision(0)
    XPositionRelativeFacing(-1280000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 265000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -265000:
            sendToLabel(1)
    sprite('hz030_00', 7)
    physicsXImpulse(6200)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventDefWalkOutOpposite():
    EnableCollision(0)
    ScreenCollision(0)
    sprite('hz003_00', 3)
    ForceFaceSprite()
    Flip()
    sprite('hz003_01', 3)
    sprite('hz003_02', 3)
    sprite('hz030_00', 7)
    physicsXImpulse(6200)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventPale():
    sprite('hz301_02', 32767)


@State
def EventPaleToStand():
    sprite('hz301_02', 7)
    sprite('hz301_04', 7)
    sprite('hz301_05', 7)
    sprite('hz301_06', 7)
    sprite('hz301_07', 7)
    enterState('CmnActStand')


@State
def EventWarp():
    sprite('keep', 2)
    ConstantAlphaModifier(-10)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')


@State
def EventWarp2():
    EnableCollision(0)
    ScreenCollision(0)
    AlphaValue(255)
    XPositionRelativeFacing(-1280000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 265000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -265000:
            sendToLabel(1)
    sprite('hz030_00', 7)
    physicsXImpulse(6200)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventBow():
    sprite('hz432_59', 6)
    sprite('hz432_58', 6)
    sprite('hz432_57', 6)
    sprite('hz432_56', 6)
    sprite('hz432_55', 32767)


@State
def EventHZVsJN_EntryWaitJNsAttack():
    XPositionRelativeFacing(0)
    uponSendToLabel(32, 1)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    uponSendToLabel(LANDING, 3)
    sprite('hz033_00', 2)
    EndMomentum(1)
    sprite('hz033_01', 2)
    physicsXImpulse(-20000)
    physicsYImpulse(8800)
    setGravity(2200)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(2)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)
    sprite('hz033_05', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('hz033_06', 4)
    sprite('hz033_07', 4)
    enterState('CmnActStand')


@State
def EventHZVsRG_KickAndStomp0():
    XPositionRelativeFacing(-170000)
    EnableCollision(0)
    SetZLine(1, 100)
    SLOT_52 = 4
    label(1)
    Unknown61(0, 2, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_51 = SLOT_0
    label(2)
    sprite('hz432_37', 1)
    SLOT_51 = SLOT_51 - 1
    loopRest()
    if SLOT_51 > 0:
        conditionalSendToLabel(2)
    if random_(2, 0, 50):
        conditionalSendToLabel(3)
    sprite('hz432_38', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_36', 2)
    sprite('hz432_34', 5)
    CommonSE('100_hit_grap_1')
    ObjectUpon(22, 33)
    ScreenShake(4000, 12000)
    sprite('hz432_35', 5)
    sprite('hz432_36', 5)
    loopRest()
    SLOT_52 = SLOT_52 - 1
    if SLOT_52 <= 0:
        conditionalSendToLabel(4)
    gotoLabel(1)
    label(3)
    sprite('hz432_38', 5)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_39', 5)
    CommonSE('100_hit_grap_2')
    ObjectUpon(22, 32)
    ScreenShake(0, 8000)
    loopRest()
    SLOT_52 = SLOT_52 - 1
    if SLOT_52 <= 0:
        conditionalSendToLabel(4)
    gotoLabel(1)
    label(4)
    sprite('hz432_37', 6)
    sprite('hz432_38', 5)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_39', 5)
    CommonSE('100_hit_grap_2')
    ObjectUpon(22, 32)
    ScreenShake(0, 8000)
    loopRest()
    sprite('hz432_40', 32767)
    loopRest()


@State
def EventHZVsRG_KickAndStomp1():
    XPositionRelativeFacing(-170000)
    EnableCollision(0)
    SetZLine(1, 100)
    sprite('hz432_40', 110)
    sprite('hz432_37', 10)
    sprite('hz432_38', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_36', 2)
    sprite('hz432_34', 5)
    CommonSE('100_hit_grap_1')
    ObjectUpon(22, 33)
    ScreenShake(4000, 12000)
    sprite('hz432_35', 5)
    sprite('hz432_36', 5)
    loopRest()
    sprite('hz432_37', 20)
    sprite('hz432_38', 5)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_39', 5)
    CommonSE('100_hit_grap_2')
    ObjectUpon(22, 32)
    ScreenShake(0, 8000)
    loopRest()
    sprite('hz432_40', 6)
    label(0)
    sprite('hz432_41', 20)
    sprite('hz432_42', 6)
    sprite('hz432_43', 6)
    sprite('hz432_41', 6)
    sprite('hz432_42', 6)
    sprite('hz432_43', 6)
    sprite('hz432_41', 6)
    sprite('hz432_42', 14)
    sprite('hz432_43', 6)
    sprite('hz432_41', 50)
    sprite('hz432_42', 6)
    sprite('hz432_43', 6)
    sprite('hz432_41', 6)
    sprite('hz432_42', 6)
    sprite('hz432_43', 6)
    loopRest()
    gotoLabel(0)


@State
def EventHZVsRG_KickAndStomp2():
    XPositionRelativeFacing(-170000)
    EnableCollision(0)
    SetZLine(1, 100)
    sprite('hz432_40', 6)
    loopRest()
    label(1)
    Unknown61(0, 2, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_51 = SLOT_0
    label(2)
    sprite('hz432_37', 1)
    SLOT_51 = SLOT_51 - 1
    loopRest()
    if SLOT_51 > 0:
        conditionalSendToLabel(2)
    if random_(2, 0, 50):
        conditionalSendToLabel(3)
    sprite('hz432_38', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_36', 2)
    sprite('hz432_34', 5)
    CommonSE('100_hit_grap_1')
    ObjectUpon(22, 33)
    ScreenShake(4000, 12000)
    sprite('hz432_35', 5)
    sprite('hz432_36', 5)
    loopRest()
    gotoLabel(1)
    label(3)
    sprite('hz432_38', 5)
    CommonSE('004_swing_grap_1_0')
    sprite('hz432_39', 5)
    CommonSE('100_hit_grap_2')
    ObjectUpon(22, 32)
    ScreenShake(0, 8000)
    loopRest()
    if random_(2, 0, 10):
        conditionalSendToLabel(4)
    gotoLabel(1)
    label(4)
    sprite('hz432_40', 6)
    sprite('hz432_41', 6)
    sprite('hz432_42', 6)
    sprite('hz432_43', 6)
    sprite('hz432_40', 8)
    loopRest()
    gotoLabel(1)


@State
def EventHZBackStepShort1():
    setInvincible(1)
    uponSendToLabel(LANDING, 1)
    ExternalForcesRate(100, 0)
    sprite('hz033_00', 1)
    sprite('hz033_01', 2)
    physicsXImpulse(-6000)
    physicsYImpulse(14000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('hz033_05', 3)
    sprite('hz033_06', 3)
    sprite('hz033_07', 3)
    enterState('CmnActStand')


@State
def EventHZBackStepShort2():
    setInvincible(1)
    uponSendToLabel(LANDING, 1)
    ExternalForcesRate(100, 0)
    sprite('hz033_00', 1)
    sprite('hz033_01', 2)
    physicsXImpulse(-6000)
    physicsYImpulse(14000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    XPositionRelativeFacing(-260000)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('hz033_05', 3)
    sprite('hz033_06', 3)
    sprite('hz033_07', 3)
    enterState('CmnActStand')


@State
def EventHZBackStep():
    setInvincible(1)
    uponSendToLabel(LANDING, 1)
    ExternalForcesRate(100, 0)
    sprite('hz033_00', 1)
    sprite('hz033_01', 2)
    physicsXImpulse(-12000)
    physicsYImpulse(14000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    sprite('hz033_05', 3)
    sprite('hz033_06', 3)
    sprite('hz033_07', 3)
    enterState('CmnActStand')


@State
def EventHZBackStep02():
    setInvincible(1)
    uponSendToLabel(LANDING, 1)
    ExternalForcesRate(100, 0)
    sprite('hz033_00', 1)
    sprite('hz033_01', 2)
    physicsXImpulse(-12000)
    physicsYImpulse(14000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    setInvincible(0)
    clearUponHandler(LANDING)
    ExternalForcesRate(100, 0)
    sprite('hz033_00', 1)
    physicsXImpulse(0)
    XPositionRelativeFacing(0)
    LandingEffects(100, 1, 1)
    sprite('hz033_01', 2)
    setInvincible(1)
    physicsXImpulse(-12000)
    physicsYImpulse(14000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    uponSendToLabel(LANDING, 3)
    sprite('hz033_03', 3)
    loopRest()
    label(2)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    sprite('hz033_05', 3)
    sprite('hz033_06', 3)
    sprite('hz033_07', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventFWalk():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('hz030_00', 7)
    physicsXImpulse(5000)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventHZStandTurn():
    Flip()
    sprite('hz003_00', 5)
    sprite('hz003_01', 5)
    sprite('hz003_02', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZStartAction01Start():
    sprite('hz600_00', 32767)
    loopRest()


@State
def EventHZStartAction01Stop():
    sprite('hz600_01', 6)
    sprite('hz600_02', 6)
    sprite('hz600_03', 6)
    sprite('hz600_04', 6)
    sprite('hz600_05', 6)
    sprite('hz600_06', 6)
    sprite('hz600_07', 6)
    sprite('hz600_08', 6)
    sprite('hz600_09', 6)
    sprite('hz600_10', 6)
    sprite('hz600_11', 6)
    sprite('hz600_12', 6)
    CommonSE('019_cloth_c')
    sprite('hz600_13', 6)
    sprite('hz600_14', 6)
    sprite('hz600_15', 6)
    sprite('hz600_16', 6)
    sprite('hz600_17', 6)
    sprite('hz600_18', 6)
    sprite('hz600_19', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZStartAction02Start():
    sprite('hz601_00', 5)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 15)
    sprite('hz601_12', 32767)
    loopRest()


@State
def EventHZStartAction02Stop():
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventTimeUpLose():
    sprite('hz620_00', 7)
    sprite('hz620_01', 7)
    label(0)
    sprite('hz620_02', 7)
    sprite('hz620_03', 4)
    sprite('hz620_04', 4)
    sprite('hz620_05', 4)
    sprite('hz620_06', 7)
    sprite('hz620_07', 7)
    sprite('hz620_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventHZPowerUpSet():
    sprite('hz213_00', 8)
    sprite('hz213_01', 8)
    sprite('hz213_02', 8)
    CreateObject('ModelMagicCircle1', -1)
    sprite('hz213_03', 8)
    ParticleColor(4278255360, 4278255360, 4278255360)
    ParticleSize(1500)
    CallCustomizableParticle('rgef431handpow', 0)
    DistortionSettings(1, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    SetBackground(1)
    KeepBackground(1)
    label(1)
    ScreenShake(0, 8000)
    sprite('hz213_03', 15)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(1)


@State
def EventHZPowerUpGo():
    sprite('hz213_04', 2)
    ScreenShake(20000, 20000)
    sprite('hz213_04', 3)
    PrivateSE('hzse_rg01')
    PrivateSE('hzse_rg02')
    PrivateSE('hzse_rg03')
    sprite('hz213_05', 5)
    CreateParticle('rgef_bkkakusan', -1)
    CreateObject('HZEF_BBStart', -1)
    if SLOT_IsUnlimited:
        if not CheckObjectPresence(5):
            CreateObject('HZEF_DrainField', -1)
            RegisterObject(5, 1)
    sprite('hz213_06', 5)
    sprite('hz213_07', 5)
    sprite('hz213_08', 5)
    sprite('hz213_06', 5)
    sprite('hz213_07', 5)
    sprite('hz213_08', 5)
    sprite('hz213_09', 5)
    sprite('hz213_10', 5)
    sprite('hz213_11', 5)
    sprite('hz213_12', 5)
    sprite('hz213_13', 5)
    SetBackground(0)
    KeepBackground(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZPowerDown():
    sprite('hz000_00', 1)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZExcite01Start():
    sprite('hz300_00', 6)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    label(0)
    sprite('hz300_06', 6)
    loopRest()
    gotoLabel(0)


@State
def EventHZExcite01Stop():
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZExcite02Start():
    sprite('hz301_00', 6)
    sprite('hz301_01', 6)
    label(0)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(0)


@State
def EventHZExcite02Loop():
    label(0)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(0)


@State
def EventHZExcite02Stop():
    sprite('hz301_04', 6)
    sprite('hz301_05', 6)
    sprite('hz301_06', 6)
    sprite('hz301_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZWinActionStart():
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    label(0)
    sprite('hz610_03', 7)
    sprite('hz610_04', 7)
    sprite('hz610_05', 7)
    loopRest()
    gotoLabel(0)


@State
def EventHZWinActionStop():
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 5)
    sprite('hz610_09', 5)
    label(0)
    sprite('hz610_10', 1)
    loopRest()
    gotoLabel(0)


@State
def EventHZWinActionToStand():
    sprite('hz610_08', 5)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventShot():
    sprite('hz407_00', 4)
    PrivateSE('hzse_05')
    CreateObject('EffLandAura', -1)
    sprite('hz407_01', 4)
    PrivateSE('hzse_08')
    CreateObject('EffSpKensei', -1)
    sprite('hz407_02', 4)
    sprite('hz407_03', 4)
    CommonSE('004_swing_grap_1_0')
    sprite('hz407_04', 2)
    sprite('hz407_05', 3)
    sprite('hz407_06', 3)
    sprite('hz407_07', 3)
    sprite('hz407_08', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('hz407_09', 3)
    sprite('hz407_10', 3)
    sprite('hz407_11', 3)
    sprite('hz407_12', 3)
    sprite('hz407_13', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventRGvsHZEntry00():
    Flip()
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def EventHZvsRGEntry00():
    XPositionRelativeFacing(0)
    enterState('CmnActStand')


@State
def EventJNvsHZWin01():
    sprite('hz301_02', 32767)


@State
def EventNOvsHZEntry00():
    XPositionRelativeFacing(-500000)
    enterState('EventTimeUpLose')


@State
def EventRCvsHZEntry00():
    XPositionRelativeFacing(-900000)
    ScreenCollision(0)
    Visibility(1)
    sprite('hz000_00', 1)
    CreateObject('NoelTimeUpLose', -1)
    sprite('hz000_00', 32767)


@State
def Event5D():
    sprite('hz203_00', 3)
    sprite('hz203_01', 3)
    sprite('hz203_02', 3)
    sprite('hz203_03', 3)
    sprite('hz203_04', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('hz203_05', 3)
    PrivateSE('hzse_04')
    sprite('hz203_06', 2)
    sprite('hz203_07', 2)
    sprite('hz203_08', 2)
    loopRest()


@State
def EventNoelCatchSet():
    sprite('hz310_02', 1)
    CreateObject('NoelDownUpperSet', -1)
    sprite('hz310_02', 32767)
    loopRest()


@State
def EventNoelCatchGo():
    sprite('hz310_02', 3)
    CreateObject('NoelDownUpperGo', -1)
    sprite('hz313_00', 4)
    sprite('hz313_01', 4)
    sprite('hz313_02', 4)
    sprite('hz313_03', 4)
    sprite('hz313_04', 4)
    sprite('hz313_05', 4)
    sprite('hz313_06', 6)
    sprite('hz313_07', 6)
    sprite('hz313_08', 1)
    sprite('hz313_09', 1)
    sprite('hz313_09', 5)
    CommonSE('100_hit_grap_3')
    sprite('hz313_10', 6)
    sprite('hz313_11', 6)
    sprite('hz313_12', 4)
    sprite('hz313_13', 4)
    sprite('hz313_14', 4)
    sprite('hz313_15', 4)
    sprite('hz000_00', 8)
    Flip()
    sprite('hz000_01', 8)
    loopRest()
    enterState('EventHZStandTurn')


@State
def NoelCollectEntrySet():
    ScreenCollision(0)
    XPositionRelativeFacing(-900000)
    Visibility(1)
    sprite('hz000_00', 1)
    CreateObject('NoelEntry', -1)
    sprite('hz000_00', 32767)


@State
def NoelCollectEntryGo():
    sprite('keep', 1)
    CreateObject('NoelWarp', -1)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZvsHAEntry():
    XPositionRelativeFacing(260000)
    enterState('CmnActStand')


@State
def EventHZvsRGGoBackStep():
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    enterState('EventHZBackStep')


@State
def EventVHvsHZEntry00():
    XPositionRelativeFacing(-900000)
    ScreenCollision(0)
    Visibility(1)
    sprite('hz000_00', 1)
    sprite('hz000_00', 32767)


@State
def EventRlvsHzEntry01():
    sprite('hz060_14', 32767)


@State
def EventRlvsHzEntry02():
    sprite('hz061_00', 7)
    sprite('hz061_01', 7)
    sprite('hz061_02', 7)
    sprite('hz061_03', 7)
    sprite('hz061_04', 7)
    sprite('hz061_05', 7)
    sprite('hz061_06', 7)
    sprite('hz061_07', 32767)


@State
def EventRlvsHzEntry03():
    sprite('hz061_08', 5)
    sprite('hz061_09', 5)
    sprite('hz061_10', 5)
    sprite('hz061_11', 5)
    sprite('hz061_12', 5)
    sprite('hz061_13', 5)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def EventTimeUpLoseEnd():
    sprite('hz620_00', 7)
    sprite('hz620_01', 7)
    enterState('CmnActStand')


@State
def EventHZWalkIn():
    ScreenCollision(0)
    XPositionRelativeFacing(-900000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('hz030_00', 7)
    physicsXImpulse(4650)
    label(0)
    sprite('hz030_01', 7)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_07', 7)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventVsVHAction1():

    def upon_IMMEDIATE():
        callSubroutine('Kamae_Zanzou')
        uponSendToLabel(32, 10)
    sprite('hz400_00', 3)
    sprite('hz400_01', 2)
    sprite('hz400_01', 1)
    CreateObject('EffKamae', 0)
    CreateObject('EffKamaeLand', -1)
    sprite('hz400_02', 5)
    PrivateSE('hzse_05')
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 5)
    label(0)
    sprite('hz400_02', 5)
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 4)
    sprite('hz400_09', 1)
    gotoLabel(0)
    label(10)
    sprite('hz400_02', 1)
    loopRest()
    enterState('EventVsVHAction2')


@State
def EventVsVHAction2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        AttackP2(82)
        AirUntechableTime(48)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        PushbackX(9800)
        AirPushbackY(40000)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        StarterRating(2)
        HardKnockdown(999)
        if SLOT_65 > 22:
            AttackLevel_(5)
            Damage(1080)
            AttackP2(84)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirPushbackX(10000)
            AirPushbackY(46000)
            CHAirPushbackX(10000)
            CHAirPushbackY(46000)
            YImpulseBeforeWallbounce(1600)
            AirUntechableTime(55)
            EnemyHitstopAddition(0, 10, 18)
            SLOT_52 = 1
            callSubroutine('Kamae_Zanzou')
        uponSendToLabel(LANDING, 1)
        PerInertia(80)
        setInvincible(1)
        EnableAfterimage(1)
        AddX(10000)
    sprite('hz401_00', 1)
    PrivateSE('hzse_07')
    CreateObject('EffSamaso', -1)
    CreateObject('EffLandAura', -1)
    sprite('hz401_00', 1)
    DespawnEAEffect('EffKamaeLand')
    sprite('hz401_01', 3)
    physicsYImpulse(28000)
    physicsXImpulse(-4000)
    setGravity(2400)
    CommonSE('004_swing_grap_1_2')
    if SLOT_52:
        CharacterFlash(32768, 10, 2)
    sprite('hz401_02', 3)
    sprite('hz401_03', 2)
    sprite('hz401_03', 2)
    sprite('hz401_04', 4)
    sprite('hz401_05', 4)
    label(0)
    sprite('hz401_06', 3)
    sprite('hz401_07', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz401_08', 3)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz401_09', 3)
    sprite('hz401_10', 3)
    sprite('hz401_11', 2)
    sprite('hz401_12', 2)
    sprite('hz401_13', 2)
    sprite('hz401_14', 2)
    setInvincible(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventHZvsVHEntry():
    XPositionRelativeFacing(-160000)
    enterState('CmnActStand')


@State
def EventvsHBEntry():
    sprite('hz602_00', 32767)
    loopRest()


@State
def EventvsHBEntryCameraON():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
    sprite('hz602_00', 32767)
    loopRest()


@State
def EventvsHBEntryEnd():
    sprite('hz602_01', 5)
    sprite('hz602_02', 5)
    sprite('hz602_03', 5)
    sprite('hz602_04', 5)
    sprite('hz602_05', 5)
    CameraControlEnable(0)
    sprite('hz602_06', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Bow():
    sprite('hz601_00', 5)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 40)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Chouhatsu():
    sprite('hz300_00', 6)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 45)
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ChouhatsuStop():
    sprite('hz300_00', 6)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    label(0)
    sprite('hz300_06', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Warai():
    sprite('hz301_00', 6)
    sprite('hz301_01', 6)
    label(0)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_WaraiEnd():
    sprite('hz301_04', 6)
    sprite('hz301_05', 6)
    sprite('hz301_06', 6)
    sprite('hz301_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Down():
    sprite('hz060_14', 32767)
    loopRest()


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_DownEnd():
    sprite('keep', 2)
    sprite('hz061_00', 5)
    sprite('hz061_01', 5)
    sprite('hz061_02', 5)
    sprite('hz061_03', 5)
    sprite('hz061_04', 5)
    sprite('hz061_05', 5)
    sprite('hz061_06', 4)
    sprite('hz061_07', 4)
    sprite('hz061_08', 4)
    sprite('hz061_09', 4)
    sprite('hz061_10', 5)
    sprite('hz061_11', 5)
    sprite('hz061_12', 5)
    sprite('hz061_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yareyare():
    sprite('keep', 2)
    sprite('hz610_00', 7)
    sprite('hz610_01', 7)
    sprite('hz610_06', 7)
    sprite('hz610_07', 7)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 32767)


@State
def Act2Event_YareyareEnd():
    sprite('keep', 2)
    sprite('hz610_08', 6)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Why():
    sprite('keep', 2)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_06', 6)
    sprite('hz610_07', 6)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 12)
    sprite('hz610_08', 6)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_WalkIn():

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
    sprite('keep', 2)
    sprite('hz030_00', 7)
    physicsXImpulse(4650)
    sprite('hz030_01', 7)
    label(9)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hz000_00', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Laugh():
    sprite('hz301_00', 6)
    sprite('hz301_01', 6)
    loopRest()
    enterState('Act2Event_Laughing')


@State
def Act2Event_Laughing():
    label(9)
    Unknown61(0, 10, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_2 = SLOT_0
    label(0)
    sprite('hz301_02', 1)
    AddActionMark(-1)
    loopRest()
    if SLOT_2 > 0:
        conditionalSendToLabel(0)
    loopRest()
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(9)


@State
def Act2Event_LaughEnd():
    sprite('keep', 2)
    sprite('hz301_04', 6)
    sprite('hz301_05', 6)
    sprite('hz301_06', 6)
    sprite('hz301_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_hzvsrg_00():

    def upon_IMMEDIATE():

        def upon_32():
            CreateObject('Act2Event_Yure', -1)
    sprite('keep', 2)
    sprite('hz301_04', 6)
    sprite('hz301_05', 6)
    sprite('hz301_06', 6)
    sprite('hz301_07', 6)
    loopRest()
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_tmvshz_00():
    sprite('keep', 2)
    sprite('hz610_00', 7)
    sprite('hz610_01', 7)
    sprite('hz610_06', 7)
    sprite('hz610_07', 7)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 32767)


@State
def Act2Event_tmvshz_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
    sprite('keep', 2)
    sprite('hz610_08', 6)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz003_00', 3)
    Flip()
    sprite('hz003_01', 3)
    sprite('hz003_02', 3)
    sprite('hz030_00', 7)
    physicsXImpulse(4650)
    sprite('hz030_01', 7)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    sprite('null', 32767)
    Visibility(1)
    EndMomentum(1)
    loopRest()


@State
def Act2Event_hzvshb_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
    sprite('keep', 2)
    sprite('hz003_00', 4)
    Flip()
    sprite('hz003_01', 4)
    sprite('hz003_02', 4)
    sprite('hz030_00', 7)
    physicsXImpulse(4650)
    sprite('hz030_01', 7)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    sprite('null', 32767)
    Visibility(1)
    EndMomentum(1)
    loopRest()


@State
def Act2Event_tbvshz_00():

    def upon_IMMEDIATE():
        Visibility(0)
    sprite('hz000_00', 1)
    ObjectUpon(22, 32)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Tokei_Pause():
    sprite('hz615_00', 6)
    sprite('hz615_01', 6)
    sprite('hz615_02', 6)
    sprite('hz615_03', 6)
    sprite('hz615_04', 8)
    sprite('hz615_05', 32767)


@State
def Act2Event_Tokei_PauseEnd():
    sprite('hz615_04', 4)
    sprite('hz615_03', 4)
    sprite('hz615_02', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_BDash():

    def upon_IMMEDIATE():

        def upon_LANDING():
            sendToLabel(1)
            EndMomentum(1)
        ScreenCollision(0)
        EnableCollision(0)
    sprite('hz033_00', 3)
    sprite('hz033_01', 4)
    physicsXImpulse(-28000)
    physicsYImpulse(18000)
    setGravity(1800)
    JumpSoundEffects()
    JumpEffects(3, 100)
    sprite('hz033_02', 4)
    sprite('hz033_03', 4)
    loopRest()
    label(0)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz033_05', 3)
    sprite('hz033_06', 3)
    sprite('hz033_07', 3)


@State
def Act2Event_izvshz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('hz070_00', 15)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitmz', 103)
    CommonSE('101_hit_slash_1')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('hz070_01', 4)
    sprite('hz070_02', 4)
    sprite('hz070_03', 32767)
    loopRest()


@State
def Act2Event_izvshz_01():
    sprite('hz070_10', 5)
    sprite('hz070_11', 5)
    sprite('hz070_12', 5)
    sprite('hz070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_izvshz_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-1500000)
        EnableCollision(0)
        ScreenCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('hz000_00', 7)
    sprite('hz000_01', 7)
    sprite('hz000_02', 7)
    sprite('hz610_00', 7)
    sprite('hz610_01', 7)
    sprite('hz610_06', 7)
    sprite('hz610_07', 7)
    sprite('hz610_08', 6)
    sprite('hz610_09', 6)
    sprite('hz610_10', 32767)
    loopRest()


@State
def Act2Event_izvshz_03():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('keep', 2)
    sprite('hz610_08', 6)
    sprite('hz610_07', 6)
    sprite('hz610_06', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_izvshz_04():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('hz301_00', 6)
    sprite('hz301_01', 6)
    loopRest()
    enterState('Act2Event_izvshz_05')


@State
def Act2Event_izvshz_05():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    label(9)
    Unknown61(0, 10, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_2 = SLOT_0
    label(0)
    sprite('hz301_02', 1)
    AddActionMark(-1)
    loopRest()
    if SLOT_2 > 0:
        conditionalSendToLabel(0)
    loopRest()
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(9)


@State
def Act3Event_tkvshz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('hz410_00', 3)
    CreateObject('Act3Event_Ragna', -1)
    RegisterObject(4, 1)
    sprite('hz410_00', 3)
    sprite('hz410_01', 4)
    label(9)
    sprite('hz410_02', 6)
    sprite('hz410_03', 6)
    sprite('hz410_04', 6)
    loopRest()
    gotoLabel(9)


@State
def Act3Event_tkvshz_01():

    def upon_IMMEDIATE():

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(0)
            EndMomentum(1)
            XPositionRelativeFacing(-260000)
            LandingEffects(100, 1, 1)
    sprite('keep', 2)
    sprite('hz410_01', 5)
    sprite('hz410_00', 5)
    sprite('hz033_00', 3)
    sprite('hz033_01', 3)
    physicsXImpulse(-8000)
    physicsYImpulse(10000)
    setGravity(1800)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(9)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hz033_05', 4)
    sprite('hz033_06', 4)
    sprite('hz033_07', 4)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz050_00', 6)
    sprite('hz050_01', 10)
    sprite('hz052_00', 2)
    ScreenShake(0, 8000)
    sprite('hz052_01', 2)
    sprite('hz052_02', 2)
    sprite('hz052_03', 6)
    sprite('hz052_02', 4)
    sprite('hz052_01', 5)
    sprite('hz052_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tkvshz_02():
    sprite('keep', 1)
    ObjectUpon(FALLING, 32)
    sprite('keep', 1)
    enterState('CmnActStand')


@State
def Act3Event_tkvshz_03():
    sprite('keep', 1)
    ObjectUpon(FALLING, 33)
    ObjectUpon(22, 32)
    sprite('keep', 1)
    enterState('CmnActStand')


@State
def Act3Event_tkvshz_04():
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    label(0)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_tkvshz_05():
    sprite('keep', 2)
    sprite('hz610_02', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tkvshz_06():

    def upon_IMMEDIATE():
        ObjectUpon(22, 33)
    sprite('hz050_00', 6)
    sprite('hz050_01', 10)
    sprite('hz052_00', 2)
    ScreenShake(0, 8000)
    sprite('hz052_01', 2)
    sprite('hz052_02', 2)
    sprite('hz052_03', 6)
    sprite('hz052_02', 4)
    sprite('hz052_01', 5)
    sprite('hz052_00', 6)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    loopRest()
    enterState('Act2Event_Yareyare')


@State
def Act3Event_tkvshz_07():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(0)
            EndMomentum(1)
            LandingEffects(100, 1, 1)
    sprite('hz000_00', 8)
    sprite('hz033_00', 3)
    sprite('hz033_01', 3)
    physicsXImpulse(-10000)
    physicsYImpulse(10000)
    setGravity(1800)
    JumpSoundEffects()
    sprite('hz033_02', 3)
    sprite('hz033_03', 3)
    loopRest()
    label(9)
    sprite('hz033_03', 3)
    sprite('hz033_04', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hz033_05', 4)
    sprite('hz033_06', 4)
    sprite('hz033_07', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tkvshz_08():

    def upon_IMMEDIATE():
        SetActionMark(30)
        SLOT_58 = 3

        def upon_EVERY_FRAME():
            if SLOT_2:
                AddActionMark(-1)
                if SLOT_2 <= 0:
                    SLOT_58 = SLOT_58 + -1
                    Unknown61(0, 60, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0)
                    SLOT_2 = SLOT_0
                    sendToLabel(1)
            if SLOT_58 <= 0:
                clearUponHandler(EVERY_FRAME)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz050_00', 6)
    sprite('hz050_01', 10)
    sprite('hz052_00', 2)
    sprite('hz052_01', 2)
    sprite('hz052_02', 2)
    ScreenShake(0, 8000)
    sprite('hz052_03', 6)
    sprite('hz052_02', 4)
    sprite('hz052_01', 5)
    sprite('hz052_00', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_hzvsmk_00():
    sprite('hz300_00', 6)
    sprite('hz300_01', 6)
    sprite('hz300_02', 6)
    sprite('hz300_03', 6)
    sprite('hz300_04', 6)
    sprite('hz300_05', 6)
    sprite('hz300_06', 32767)


@State
def Act3Event_hzvsmk_01():
    sprite('hz300_07', 6)
    sprite('hz300_08', 6)
    sprite('hz300_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvsmk_02():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('hz403_04', 2)
    CreateObject('Act3Event_EffGedan', -1)
    sprite('hz403_05', 2)
    CommonSE('007_swing_knife_1')
    sprite('hz403_06', 1)
    PrivateSE('hzse_06')
    sprite('hz403_07', 2)
    sprite('hz403_08', 18)
    CommonSE('009_swing_rapier_1')
    CommonSE('004_swing_grap_1_0')
    sprite('hz403_09', 4)
    sprite('hz403_10', 4)
    sprite('hz403_11', 4)
    sprite('hz403_12', 4)
    sprite('hz403_13', 4)
    sprite('hz403_14', 4)
    sprite('hz403_15', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvskk_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        NoAttackDuringAction(1)

        def upon_LANDING():
            sendToLabel(0)
            EndMomentum(1)
    sprite('hz212_05', 3)
    sprite('hz212_06', 3)
    EndMomentum(1)
    physicsYImpulse(13000)
    physicsXImpulse(-16500)
    SetAcceleration(400)
    EndYPhysicsImpulse()
    sprite('hz212_07', 3)
    CreateObject('ShotKnifeObj', 0)
    ObjectHitbox(1)
    CreateObject('ShotKnife', 0)
    CommonSE('007_swing_knife_0')
    CommonSE('004_swing_grap_1_0')
    sprite('hz212_08', 3)
    sprite('hz212_09', 3)
    sprite('hz212_10', 3)
    sprite('hz212_11', 3)
    sprite('hz212_11', 32767)
    label(0)
    sprite('hz212_12', 4)
    sprite('hz212_13', 4)
    sprite('hz212_14', 4)
    sprite('hz212_15', 4)
    sprite('hz212_16', 4)
    sprite('hz212_17', 4)
    sprite('hz212_18', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvskk_01():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
        SetZVal(750)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 120000:
                    clearUponHandler(EVERY_FRAME)
                    EndMomentum(1)
                    sendToLabel(0)
            elif SLOT_XDistanceFromCenterOfStage > -120000:
                clearUponHandler(EVERY_FRAME)
                EndMomentum(1)
                sendToLabel(0)
    sprite('keep', 2)
    sprite('hz030_00', 7)
    physicsXImpulse(4650)
    sprite('hz030_01', 7)
    label(9)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hz612_00', 6)
    sprite('hz612_01', 6)
    sprite('hz612_02', 6)
    sprite('hz612_03', 6)
    sprite('hz612_04', 8)
    sprite('hz612_05', 8)
    label(1)
    sprite('hz612_06', 4)
    sprite('hz612_07', 6)
    sprite('hz612_08', 6)
    sprite('hz612_09', 6)
    sprite('hz612_10', 6)
    sprite('hz612_11', 5)
    sprite('hz612_12', 4)
    loopRest()
    gotoLabel(1)


@State
def Act3Event_hzvskk_02():
    sprite('hz612_05', 6)
    sprite('hz612_04', 6)
    sprite('hz612_03', 6)
    sprite('hz612_02', 6)
    sprite('hz612_01', 7)
    sprite('hz612_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvsrl_00():
    sprite('hz001_00', 6)
    sprite('hz001_01', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_03', 8)
    sprite('hz001_04', 8)
    sprite('hz001_05', 8)
    sprite('hz001_04', 8)
    sprite('hz001_03', 8)
    sprite('hz001_02', 8)
    sprite('hz001_06', 6)
    sprite('hz001_07', 6)
    sprite('hz001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvsrl_01():
    sprite('hz620_00', 7)
    sprite('hz620_01', 7)
    label(0)
    sprite('hz620_02', 7)
    sprite('hz620_03', 4)
    sprite('hz620_04', 4)
    sprite('hz620_05', 4)
    sprite('hz620_06', 7)
    sprite('hz620_07', 7)
    sprite('hz620_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_hzvsrl_02():
    sprite('hz620_01', 7)
    sprite('hz620_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_hzvstm_00():
    sprite('hz431_00', 5)
    sprite('hz431_01', 5)
    sprite('hz410_00', 5)
    sprite('hz410_01', 5)
    PrivateSE('hzse_09')
    label(9)
    sprite('hz410_02', 5)
    sprite('hz410_03', 5)
    sprite('hz410_04', 5)
    loopRest()
    gotoLabel(9)


@State
def Act3Event_hzvstm_01():
    sprite('keep', 2)
    sprite('hz406_16', 4)
    PrivateSE('hzse_09')
    AddX(120000)
    sprite('hz406_17', 4)
    PrivateSE('hzse_09')
    AddX(-60000)
    sprite('hz406_18', 4)
    PrivateSE('hzse_09')
    AddX(-60000)
    sprite('hz406_19', 4)
    sprite('hz406_20', 2)
    CommonSE('007_swing_knife_2')
    sprite('hz406_21', 3)
    sprite('hz406_22', 4)
    sprite('hz406_23', 5)
    sprite('hz406_24', 6)
    sprite('hz406_25', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_vhvshz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('hz040_00', 2)
    sprite('hz040_01', 2)
    sprite('hz040_02', 3)
    sprite('hz040_05', 15)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('hz090_00', 1)
    AddInertia(-11000)
    sprite('hz090_01', 2)
    sprite('hz090_02', 16)
    sprite('hz090_03', 4)
    sprite('hz090_04', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Ac32Event_ntvshz_00():

    def upon_IMMEDIATE():
        Visibility(0)
    sprite('hz000_00', 1)
    ObjectUpon(22, 35)
    loopRest()
    enterState('CmnActStand')


@State
def Ac32Event_ntvshz_01():

    def upon_IMMEDIATE():
        Visibility(0)
    sprite('hz000_00', 1)
    ObjectUpon(22, 36)
    loopRest()
    enterState('CmnActStand')


@State
def Ac32Event_ntvshz_02():

    def upon_IMMEDIATE():
        Visibility(0)
    sprite('hz000_00', 1)
    ObjectUpon(22, 37)
    loopRest()
    enterState('CmnActStand')


@State
def Ac32Event_ntvshz_03():

    def upon_IMMEDIATE():
        AddX(120000)

        def upon_32():
            sendToLabel(1)
    sprite('hz400_01', 1)
    CreateObject('EffKamae', 0)
    CreateObject('EffKamaeLand', -1)
    label(0)
    sprite('hz400_02', 5)
    PrivateSE('hzse_05')
    sprite('hz400_03', 5)
    sprite('hz400_04', 5)
    sprite('hz400_05', 5)
    sprite('hz400_06', 5)
    sprite('hz400_07', 5)
    sprite('hz400_08', 5)
    sprite('hz400_09', 5)
    gotoLabel(0)
    label(1)
    sprite('hz401_00', 1)
    uponSendToLabel(LANDING, 3)
    PrivateSE('hzse_07')
    CommonSE('006_swing_blade_2')
    CreateObject('EffSamaso', -1)
    CreateObject('EffLandAura', -1)
    sprite('hz401_00', 1)
    DespawnEAEffect('EffKamaeLand')
    sprite('hz401_01', 3)
    physicsYImpulse(28000)
    physicsXImpulse(-4000)
    setGravity(2400)
    CommonSE('004_swing_grap_1_1')
    CharacterFlash(32768, 10, 2)
    sprite('hz401_02', 3)
    sprite('hz401_03', 14)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    CreateObject('Eventoffset_Sosai_ntvshz', 103)
    EndMomentum(1)
    setGravity(0)
    sprite('hz401_04', 4)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    sprite('hz401_05', 4)
    label(2)
    sprite('hz401_06', 3)
    sprite('hz401_07', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('hz401_08', 3)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('hz401_09', 3)
    sprite('hz401_10', 3)
    sprite('hz401_11', 2)
    sprite('hz401_12', 2)
    sprite('hz401_13', 2)
    sprite('hz401_14', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_CAvsHZ00():
    sprite('hz001_00', 6)
    ObjectUpon(22, 32)
    sprite('hz001_01', 6)
    sprite('hz001_02', 6)
    sprite('hz001_03', 6)
    sprite('hz001_05', 6)
    ObjectUpon(22, 35)
    sprite('hz001_04', 6)
    sprite('hz001_03', 6)
    sprite('hz001_02', 6)
    sprite('hz001_06', 6)
    sprite('hz001_07', 6)
    sprite('hz001_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_CAvsHZ01():
    sprite('hz040_00', 4)
    ObjectUpon(22, 34)
    sprite('hz040_01', 4)
    label(0)
    sprite('hz040_02', 8)
    sprite('hz040_03', 8)
    sprite('hz040_04', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CAvsHZ02():
    sprite('hz602_04', 4)
    sprite('hz602_03', 4)
    sprite('hz602_02', 4)
    sprite('hz602_01', 4)
    sprite('hz602_00', 32767)


@State
def Act3Event_tbvshz_00():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 100)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        XPositionRelativeFacing(-50000)
    sprite('hz040_00', 4)
    SetInertia(-20000)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('104_guard_grap_1')
    ScreenShake(5000, 20000)
    sprite('hz040_01', 4)
    LandingEffects(100, 1, 1)
    label(0)
    sprite('hz040_02', 8)
    sprite('hz040_03', 8)
    sprite('hz040_04', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz040_01', 4)
    sprite('hz040_00', 4)
    loopRest()
    enterState('CmnActStand')
