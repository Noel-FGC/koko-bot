@Subroutine
def PreInit():
    CharacterID('nt')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11500)
    WalkFSpeed(5700)
    WalkBSpeed(4300)
    DashFInitialVelocity(18000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(42000)
    AirDashFSpeed(27900)
    AirFDashDuration(16)
    AirDashBSpeed(24000)
    AirBDashDuration(10)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5A_2', 0x1)
    Move_Input_(0x6c)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    DamageStunPriority(10000)
    GuardStunPriority(10000)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    DamageStunPriority(1)
    SkillEstimateRange(0, 400000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    MoveLow()
    DamageStunPriority(2000)
    SkillEstimateRange(0, 250000, -100000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(1500)
    SkillEstimateRange(0, 250000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMaxChainRepeat(1)
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    AirborneOpponentPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(1)
    SkillEstimateRange(50000, 400000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(400000, 700000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    AirborneOpponentPriority(2000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(-50000, 250000, -100000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    SkillEstimateRange(0, 400000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    MoveMaxChainRepeat(2)
    MoveButtonHoldTime(3, 2, 20)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(500)
    SkillEstimateRange(450000, 800000, -200000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    MoveButtonHoldTime(3, 2, 20)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(500)
    SkillEstimateRange(450000, 800000, -200000, 800000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    SharedGatling('NmlAtk5D')
    MoveLow()
    MoveButtonHoldTime(3, 2, 20)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(500)
    SkillEstimateRange(450000, 800000, -100000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(500)
    SkillEstimateRange(0, 250000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    DamageStunPriority(2000)
    SkillEstimateRange(-50000, 350000, -250000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SkillEstimateRange(-50000, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    MoveButtonHoldTime(3, 2, 20)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(400000, 850000, -500000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    AddChain(1)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 250000, -200000, 200000, 500, 0)
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
    SkillEstimateRange(0, 200000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('DodgeThrow', INPUT_SPECIALMOVE)
    Move_Input_(0x93)
    Move_Input_(0x8d)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    MoveThrow()
    AirborneOpponentPriority(4000)
    OpponentAttackPriority(2000)
    SkillEstimateRange(-250000, 250000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    MoveCancellableFrames(27, 29)
    OpponentAttackPriority(1)
    DamageStunPriority(500)
    SkillEstimateRange(-50000, 400000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_2nd', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    MoveCancellableFrames(20, 21)
    OpponentAttackPriority(1)
    DamageStunPriority(10000)
    GuardStunPriority(3000)
    SkillEstimateRange(-50000, 300000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdYoko', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    OpponentAttackPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(10000)
    SkillEstimateRange(-50000, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdTate', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    AirborneOpponentPriority(3000)
    Unknown15027(5000)
    GuardStunPriority(1)
    SkillEstimateRange(-50000, 300000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('AntiAirC', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(500)
    MoveCancellableFrames(30, 35)
    AirborneOpponentPriority(2000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveComboPriority(1)
    MoveCPULevel(50, 100, 100, 1000)
    SkillEstimateRange(-50000, 300000, 50000, 400000, 250, 0)
    Move_EndRegister()
    Move_Register('AntiAirD', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(3500)
    MoveCancellableFrames(45, 49)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveCPULevel(50, 100, 100, 1000)
    SkillEstimateRange(-50000, 300000, -200000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('AntiAirC_Air', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(100)
    MoveCancellableFrames(30, 35)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 300000, 150, 0)
    Move_EndRegister()
    Move_Register('AntiAirD_Air', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(1500)
    MoveCancellableFrames(45, 49)
    DamageStunPriority(500)
    GuardStunPriority(0)
    MoveCPULevel(50, 100, 100, 1000)
    SkillEstimateRange(-50000, 300000, -200000, 300000, 150, 0)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    DamageStunPriority(10000)
    Move_EndRegister()
    Move_Register('Dodge', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(2000)
    DamageStunPriority(2500)
    MoveCPULevel(50, 100, 100, 1000)
    SkillEstimateRange(-50000, 350000, -200000, 300000, 400, 0)
    Move_EndRegister()
    Move_Register('EdgeAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(1)
    SkillEstimateRange(300000, 550000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(350000, 800000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(350000, 800000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(350000, 800000, -600000, -300000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(350000, 800000, -600000, -300000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveCPULevel(50, 100, 1, 1000)
    SkillEstimateRange(-100000, 350000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveCPULevel(50, 100, 1, 1000)
    SkillEstimateRange(-100000, 350000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_2141236)
    Move_Input_(0x5)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(50000, 450000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('BurstDD_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    Move_Input_(INPUT_HOLD_B)
    Move_Input_(INPUT_HOLD_C)
    Move_Input_(INPUT_HOLD_D)
    Move_Condition(0x3081)
    CallSkillConditions('Func_BurstDD_Easy')
    OpponentAttackPriority(3000)
    DamageStunPriority(7000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('BurstDD_Cancel', INPUT_SPECIALMOVE)
    StateCall('BurstDD_Easy')
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(3000)
    DamageStunPriority(7000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('BurstDD', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    NeutralOnly(1)
    OpponentAttackPriority(3000)
    DamageStunPriority(7000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5A_2', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Assault', 50000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'AntiAirD', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Assault', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AntiAirD_Air', 10000000)
    TempPriorityMultiplier('Assault_3rdTate', 'FJump', 10000000)
    StylishModeSpecialButton('AntiAirD', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('Dodge', 0x4, 0x45)
    StylishModeSpecialButton('AntiAirD_Air', 0x4, 0xea)
    StylishModeSpecialButton('UltimateAirAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAirAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('AntiAir2nd', 0x4, 0xea)
    StylishModeSpecialButton('Assault_2nd', 0x4, 0xea)
    StylishModeSpecialButton('Assault_3rdYoko', 0x4, 0xea)
    StylishModeSpecialButton('DodgeThrow', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5A_2', 0, 0)
    StylishModeCancels('NmlAtk5A_2', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A_2', 'AstralHeat', 5, 100)
    StylishModeCancels('NmlAtk5A_2', 'NmlAtk6A', 13, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'FHighJump', 12, 0)
    StylishModeCancels('NmlAtk5C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 1, 250000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D', 8, 0)
    StylishModeCancels('NmlAtk5C', 'FHighJump', 12, 0)
    StylishModeCancels('NmlAtk5C', 'EdgeAssault', 13, 0)
    StylishModeCancels('NmlAtk5D', 'EdgeAssault', 0, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('NmlAtk5D', 'NmlAtk2D', 8, 0)
    StylishModeCancels('NmlAtk6A', 'AstralHeat', 5, 100)
    StylishModeCancels('NmlAtk6A', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5C', 13, 0)
    StylishModeCancels('NmlAtk6B', 'UltimateAirAssault', 5, 50)
    StylishModeCancels('NmlAtk6B', 'UltimateAirAssaultOD', 5, 50)
    StylishModeCancels('NmlAtk6B', 'Assault', 8, 0)
    StylishModeCancels('NmlAtk6C', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk6D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk6D', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('ThrowExe', 'Assault', 0, 0)
    StylishModeCancels('BackThrowExe', 'Assault', 0, 0)
    StylishModeCancels('BackThrowExe', 'UltimateEdgeAssault', 5, 0)
    StylishModeCancels('BackThrowExe', 'UltimateEdgeAssaultOD', 5, 0)
    StylishModeCancels('Assault', 'Assault_2nd', 0, 0)
    StylishModeCancels('Assault_2nd', 'Assault_3rdYoko', 6, 0)
    StylishModeCancels('Assault_3rdTate', 'VHighJump', 6, 0)
    StylishModeCancels('AntiAirC', 'AntiAir2nd', 0, 0)
    StylishModeCancels('AntiAirD', 'AntiAir2nd', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 3, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2A', 13, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk3C', 1, 250000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 3, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'FHighJump', 12, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 5, 100)
    StylishModeCancels('NmlAtk3C', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'EdgeAssault', 13, 0)
    StylishModeCancels('NmlAtk2D', 'EdgeAssault', 0, 0)
    StylishModeCancels('NmlAtk2D', 'NmlAtk5D', 1, 300000)
    StylishModeCancels('NmlAtk2D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk2D', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AntiAirD_Air', 6, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 13, 0)
    StylishModeCancels('AntiAirC_Air', 'AntiAir2nd', 0, 0)
    StylishModeCancels('AntiAirD_Air', 'AntiAir2nd', 0, 0)
    HitSprites(0, 'nt062_01')
    HitSprites(1, 'nt062_03')
    HitSprites(2, 'nt062_04')
    HitSprites(3, 'nt062_05')
    HitSprites(4, 'nt062_05')
    HitSprites(5, 'nt062_06')
    HitSprites(6, 'nt062_07')
    HitSprites(7, 'nt041_02')
    HitSprites(8, 'nt040_02')
    HitSprites(9, 'nt045_02')
    HitSprites(10, 'nt060_00')
    HitSprites(11, 'nt060_01')
    HitSprites(12, 'nt060_03')
    HitSprites(13, 'nt060_05')
    HitSprites(14, 'nt060_07')
    HitSprites(15, 'nt060_14')
    HitSprites(16, 'nt050_00')
    HitSprites(17, 'nt052_00')
    HitSprites(18, 'nt054_00')
    HitSprites(19, 'nt000_00')
    HitSprites(20, 'nt000_00')
    HitSprites(25, 'nt063_00')
    HitSprites(26, 'nt063_01')
    HitSprites(27, 'nt063_02')
    HitSprites(28, 'nt063_04')
    HitSprites(29, 'nt063_10')
    HitSprites(30, 'nt077_00')
    HitSprites(31, 'nt077_01')
    HitSprites(32, 'nt077_00ex01')
    HitSprites(33, 'nt077_01ex01')
    HitSprites(34, 'nt077_00ex02')
    HitSprites(35, 'nt077_01ex02')
    HitSprites(36, 'nt077_00ex03')
    HitSprites(37, 'nt077_01ex03')
    HitSprites(24, 'nt073_01')
    CommonVoicelines(0, 'nt000')
    CommonVoicelines(1, 'nt001')
    CommonVoicelines(2, 'nt002')
    CommonVoicelines(3, 'nt003')
    CommonVoicelines(4, 'nt004')
    CommonVoicelines(5, 'nt005')
    CommonVoicelines(6, 'nt006')
    CommonVoicelines(7, 'nt007')
    CommonVoicelines(8, 'nt008')
    CommonVoicelines(9, 'nt009')
    CommonVoicelines(10, 'nt010')
    CommonVoicelines(11, 'nt011')
    CommonVoicelines(12, 'nt012')
    CommonVoicelines(13, 'nt013')
    CommonVoicelines(14, 'nt014')
    CommonVoicelines(15, 'nt015')
    CommonVoicelines(16, 'nt016')
    CommonVoicelines(17, 'nt017')
    CommonVoicelines(18, 'nt018')
    CommonVoicelines(19, 'nt019')
    CommonVoicelines(20, 'nt020')
    CommonVoicelines(21, 'nt021')
    CommonVoicelines(22, 'nt022')
    CommonVoicelines(23, 'nt023')
    CommonVoicelines(24, 'nt024')
    CommonVoicelines(25, 'nt025')
    CommonVoicelines(26, 'nt026')
    CommonVoicelines(27, 'nt027')
    CommonVoicelines(28, 'nt028')
    CommonVoicelines(29, 'nt029')
    CommonVoicelines(30, 'nt030')
    CommonVoicelines(31, 'nt031')
    CommonVoicelines(32, 'nt032')
    CommonVoicelines(33, 'nt033')
    CommonVoicelines(34, 'nt034')
    CommonVoicelines(35, 'nt035')
    CommonVoicelines(36, 'nt036')
    CommonVoicelines(37, 'nt037')
    CommonVoicelines(38, 'nt038')
    CommonVoicelines(39, 'nt039')
    CommonVoicelines(40, 'nt040')
    CommonVoicelines(41, 'nt041')
    CommonVoicelines(42, 'nt042')
    CommonVoicelines(43, 'nt043')
    CommonVoicelines(44, 'nt044')
    CommonVoicelines(45, 'nt045')
    CommonVoicelines(46, 'nt046')
    CommonVoicelines(47, 'nt047')
    CommonVoicelines(48, 'nt048')
    CommonVoicelines(49, 'nt049')
    CommonVoicelines(50, 'nt050')
    CommonVoicelines(51, 'nt051')
    CommonVoicelines(52, 'nt052')
    CommonVoicelines(53, 'nt053')
    CommonVoicelines(54, 'nt100')
    CommonVoicelines(55, 'nt101')
    CommonVoicelines(56, 'nt102')
    CommonVoicelines(57, 'nt103')
    CommonVoicelines(58, 'nt104')
    CommonVoicelines(59, 'nt105')
    CommonVoicelines(60, 'nt106')
    CommonVoicelines(61, 'nt107')
    CommonVoicelines(62, 'nt108')
    CommonVoicelines(63, 'nt109')
    CommonVoicelines(64, 'nt150')
    CommonVoicelines(65, 'nt151')
    CommonVoicelines(66, 'nt152')
    CommonVoicelines(67, 'nt153')
    CommonVoicelines(68, 'nt154')
    CommonVoicelines(69, 'nt155')
    CommonVoicelines(70, 'nt156')
    CommonVoicelines(71, 'nt157')
    CommonVoicelines(72, 'nt158')
    CommonVoicelines(75, 'nt160')
    CommonVoicelines(73, 'nt402')
    CommonVoicelines(74, 'nt403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnFrameStep():
    if SLOT_OverdriveTimer:
        SLOT_66 = 1
    elif not SLOT_65:
        if SLOT_21:
            SLOT_66 = 0
    if not SLOT_81:
        if SLOT_4:
            if not SLOT_OverdriveTimer:
                SLOT_4 = SLOT_4 + -2
            else:
                SLOT_4 = SLOT_4 + -1
        if SLOT_4 <= -1:
            SLOT_4 = 0


@Subroutine
def OnPreDraw():
    CallPrivateFunction('NT_RagnaSwitch', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def Drive_Zanzou():
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(4)
    AfterimageInterval(0)
    AfterimageColor_1(255, 255, 0, 0)
    AfterimageColor_2(51, 255, 0, 0)
    AfterimageMask_1(0, 0, 0, 0)
    AfterimageMask_2(0, 0, 0, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)


@State
def CmnActStand():
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(0, 2, 123):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('nt001_00', 7)
    SLOT_88 = 960
    Voiceline('nt000')
    sprite('nt001_01', 7)
    sprite('nt001_02', 7)
    sprite('nt001_03', 7)
    sprite('nt001_04', 7)
    sprite('nt001_05', 7)
    sprite('nt001_06', 7)
    sprite('nt001_07', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('nt003_00', 3)
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)


@State
def CmnActStand2Crouch():
    sprite('nt010_00', 4)
    sprite('nt010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('nt010_02', 6)
    sprite('nt010_03', 6)
    sprite('nt010_04', 6)
    sprite('nt010_05', 6)
    sprite('nt010_06', 6)
    sprite('nt010_07', 6)
    sprite('nt010_08', 6)
    sprite('nt010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('nt013_00', 3)
    sprite('nt013_01', 3)
    sprite('nt013_00ex01', 3)


@State
def CmnActCrouch2Stand():
    sprite('nt010_01', 4)
    sprite('nt010_00', 4)


@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        SLOT_4 = 0
    sprite('nt023_00', 2)
    sprite('nt023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('nt020_00', 4)
    sprite('nt020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('nt020_02', 3)
    sprite('nt020_03', 3)
    sprite('nt020_04', 3)


@State
def CmnActJumpDown():
    sprite('nt020_05', 3)
    sprite('nt020_06', 3)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('nt024_00', 3)
    sprite('nt024_01', 3)
    sprite('nt024_02', 3)
    sprite('nt024_03', 3)
    sprite('nt024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('nt024_00', 2)
    sprite('nt024_01', 2)
    sprite('nt024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('nt024_03', 3)
    sprite('nt024_04', 3)


@State
def CmnActFWalk():
    sprite('nt030_00', 8)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('nt031_00', 8)
    label(0)
    sprite('nt031_01', 8)
    sprite('nt031_02', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt031_03', 8)
    sprite('nt031_04', 8)
    sprite('nt031_05', 8)
    sprite('nt031_06', 8)
    sprite('nt031_07', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt031_08', 8)
    sprite('nt031_09', 8)
    sprite('nt031_10', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_EVERY_FRAME():
        SLOT_4 = 26
    sprite('nt032_00', 2)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():

    def upon_8():
        SLOT_4 = 0
    sprite('nt032_09', 3)
    sprite('nt032_10', 3)
    sprite('nt032_11', 3)
    sprite('nt032_12', 3)


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
    sprite('nt033_00', 1)
    sprite('nt033_01', 3)
    SmartVoiceline('nt005')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    setInvincible(0)
    loopRest()
    label(0)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt033_03', 1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():

    def upon_EVERY_FRAME():
        if SLOT_OverdriveTimer:
            SLOT_4 = 26
        else:
            SLOT_4 = 0
    sprite('nt035_00', 3)
    label(0)
    sprite('nt035_01', 3)
    sprite('nt035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('nt036_00', 3)
    label(0)
    sprite('nt036_01', 3)
    sprite('nt036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('nt050_00', 1)
    sprite('nt050_01', 1)
    sprite('nt050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('nt050_01', 1)
    sprite('nt050_02', 1)
    sprite('nt050_01', 2)
    sprite('nt050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('nt050_02', 1)
    sprite('nt050_03', 1)
    sprite('nt050_02', 2)
    sprite('nt050_01', 2)
    sprite('nt050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('nt050_03', 1)
    sprite('nt050_04', 1)
    sprite('nt050_03', 2)
    sprite('nt050_02', 2)
    sprite('nt050_01', 2)
    sprite('nt050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('nt050_04', 1)
    sprite('nt050_04', 1)
    sprite('nt050_04', 2)
    sprite('nt050_03', 2)
    sprite('nt050_02', 2)
    sprite('nt050_01', 2)
    sprite('nt050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('nt052_00', 1)
    sprite('nt052_01', 1)
    sprite('nt052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('nt052_01', 1)
    sprite('nt052_02', 1)
    sprite('nt052_01', 2)
    sprite('nt052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('nt052_02', 1)
    sprite('nt052_03', 1)
    sprite('nt052_02', 2)
    sprite('nt052_01', 2)
    sprite('nt052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('nt052_03', 1)
    sprite('nt052_04', 1)
    sprite('nt052_03', 2)
    sprite('nt052_02', 2)
    sprite('nt052_01', 2)
    sprite('nt052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('nt052_04', 1)
    sprite('nt052_04', 1)
    sprite('nt052_04', 2)
    sprite('nt052_03', 2)
    sprite('nt052_02', 2)
    sprite('nt052_01', 2)
    sprite('nt052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('nt054_00', 1)
    sprite('nt054_01', 1)
    sprite('nt054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('nt054_01', 1)
    sprite('nt054_02', 1)
    sprite('nt054_01', 2)
    sprite('nt054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('nt054_02', 1)
    sprite('nt054_03', 1)
    sprite('nt054_02', 2)
    sprite('nt054_01', 2)
    sprite('nt054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('nt054_03', 1)
    sprite('nt054_04', 1)
    sprite('nt054_03', 2)
    sprite('nt054_02', 2)
    sprite('nt054_01', 2)
    sprite('nt054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('nt054_04', 1)
    sprite('nt054_04', 1)
    sprite('nt054_04', 2)
    sprite('nt054_03', 2)
    sprite('nt054_02', 2)
    sprite('nt054_01', 2)
    sprite('nt054_00', 2)


@State
def CmnActBDownUpper():
    sprite('nt060_00', 4)
    label(0)
    sprite('nt060_01', 4)
    sprite('nt060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('nt060_03', 4)


@State
def CmnActBDownDown():
    sprite('nt060_04', 4)
    label(0)
    sprite('nt060_05', 4)
    sprite('nt060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('nt060_07', 2)
    sprite('nt060_08', 2)


@State
def CmnActBDownBound():
    sprite('nt060_09', 3)
    sprite('nt060_10', 3)
    sprite('nt060_11', 3)
    sprite('nt060_12', 3)
    sprite('nt060_13', 3)


@State
def CmnActBDownLoop():
    sprite('nt060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('nt061_00', 4)
    sprite('nt061_01', 3)
    sprite('nt061_02', 3)
    sprite('nt061_03', 3)
    sprite('nt061_04', 3)
    sprite('nt061_05', 3)
    sprite('nt061_06', 3)
    sprite('nt061_07', 3)
    sprite('nt061_08', 3)


@State
def CmnActFDownUpper():
    sprite('nt063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('nt063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('nt063_02', 3)
    sprite('nt063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('nt063_04', 3)
    sprite('nt063_05', 3)


@State
def CmnActFDownBound():
    sprite('nt063_06', 2)
    sprite('nt063_07', 2)
    sprite('nt063_08', 3)
    sprite('nt063_09', 3)
    sprite('nt063_10', 3)


@State
def CmnActFDownLoop():
    sprite('nt063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('nt064_00', 2)
    sprite('nt064_01', 2)
    sprite('nt064_02', 2)
    sprite('nt064_03', 2)
    sprite('nt064_04', 2)
    sprite('nt064_05', 2)
    sprite('nt064_06', 2)
    sprite('nt064_07', 2)
    sprite('nt064_08', 2)
    sprite('nt064_09', 2)
    sprite('nt064_10', 2)
    sprite('nt064_11', 2)


@State
def CmnActVDownUpper():
    sprite('nt062_00', 3)
    label(0)
    sprite('nt062_01', 3)
    sprite('nt062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('nt062_03', 3)
    sprite('nt062_04', 3)


@State
def CmnActVDownDown():
    sprite('nt062_05', 3)
    sprite('nt062_06', 3)
    label(0)
    sprite('nt062_07', 3)
    sprite('nt062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('nt062_09', 2)
    sprite('nt062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('nt062_09', 2)
    sprite('nt062_10', 2)


@State
def CmnActBlowoff():
    sprite('nt072_00', 3)
    sprite('nt072_01', 3)
    sprite('nt072_02', 3)
    label(0)
    sprite('nt072_01', 3)
    sprite('nt072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('nt074_00', 3)
    sprite('nt074_01', 3)
    sprite('nt074_02', 3)
    sprite('nt074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('nt082_00', 2)
    sprite('nt082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('nt070_01', 1)


@State
def CmnActWallBound():
    sprite('nt073_00', 3)
    sprite('nt073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('nt073_02', 3)
    label(0)
    sprite('nt073_03', 3)
    sprite('nt073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('nt070_00', 2)
    sprite('nt070_01', 2)
    label(0)
    sprite('nt070_02', 5)
    sprite('nt070_03', 5)
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('nt070_04', 4)
    sprite('nt070_05', 4)
    sprite('nt070_06', 4)
    sprite('nt070_07', 4)
    sprite('nt070_08', 4)
    sprite('nt070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('nt070_10', 2)
    sprite('nt070_11', 2)
    sprite('nt070_12', 2)
    sprite('nt070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('nt113_00', 3)
    sprite('nt113_01', 3)
    sprite('nt113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('nt113_00', 3)
    sprite('nt113_01', 3)
    sprite('nt113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('nt113_00', 3)
    sprite('nt113_01', 3)
    sprite('nt113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('nt110_00', 2)
    sprite('nt110_01', 2)
    sprite('nt110_02', 2)
    sprite('nt110_03', 2)
    sprite('nt110_04', 2)
    sprite('nt110_05', 2)
    sprite('nt110_06', 2)
    sprite('nt110_07', 200)
    sprite('nt110_08', 3)
    sprite('nt110_09', 3)


@State
def CmnActUkemiLandB():
    sprite('nt111_00', 2)
    sprite('nt111_01', 2)
    sprite('nt111_02', 2)
    sprite('nt111_03', 2)
    sprite('nt111_04', 2)
    sprite('nt111_05', 2)
    sprite('nt111_06', 2)
    sprite('nt111_07', 200)
    sprite('nt111_08', 3)
    sprite('nt111_09', 3)


@State
def CmnActUkemiLandN():
    sprite('nt112_00', 2)
    sprite('nt112_01', 2)
    sprite('nt112_02', 2)
    sprite('nt112_03', 2)
    sprite('nt112_04', 2)
    sprite('nt112_05', 2)
    sprite('nt112_06', 3)
    sprite('nt112_07', 3)
    sprite('nt112_08', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('nt024_00', 3)
    sprite('nt024_01', 3)
    sprite('nt024_02', 3)
    sprite('nt024_03', 3)
    sprite('nt024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('nt040_00', 3)
    sprite('nt040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('nt040_02', 4)
    sprite('nt040_03', 4)
    sprite('nt040_04', 4)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('nt040_01', 3)
    sprite('nt040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('nt040_05', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('nt040_01', 3)
    sprite('nt040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('nt041_00', 3)
    sprite('nt041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('nt041_02', 4)
    sprite('nt041_03', 4)
    sprite('nt041_04', 4)
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('nt041_01', 3)
    sprite('nt041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('nt041_05', 3)


@State
def CmnActHighHeavyGuardEnd():
    sprite('nt041_01', 3)
    sprite('nt041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('nt043_00', 3)
    sprite('nt043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('nt043_02', 3)
    sprite('nt043_03', 3)
    sprite('nt043_04', 3)
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('nt043_01', 3)
    sprite('nt043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('nt043_05', 3)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('nt043_01', 3)
    sprite('nt043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('nt045_00', 3)
    sprite('nt045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('nt045_02', 3)
    sprite('nt045_03', 3)
    sprite('nt045_04', 3)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('nt045_01', 3)
    sprite('nt045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('nt045_05', 3)


@State
def CmnActAirHeavyGuardEnd():
    sprite('nt045_01', 3)
    sprite('nt045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('nt090_00', 2)
    sprite('nt090_01', 2)
    sprite('nt090_02', 1)
    SetCommonActionMark(1)
    sprite('nt090_03', 6)
    sprite('nt090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('nt091_00', 2)
    sprite('nt091_01', 2)
    sprite('nt091_02', 1)
    SetCommonActionMark(1)
    sprite('nt091_03', 6)
    sprite('nt091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('nt092_00', 2)
    sprite('nt092_01', 2)
    sprite('nt092_02', 1)
    SetCommonActionMark(1)
    sprite('nt092_03', 6)
    sprite('nt092_04', 6)


@State
def CmnActAirTurn():
    sprite('nt025_00', 4)
    sprite('nt025_01', 4)
    sprite('nt025_00ex01', 4)


@State
def CmnActLockWait():
    sprite('nt040_02', 1)
    sprite('nt040_01', 3)
    sprite('nt040_00', 3)


@State
def CmnActLockReject():
    sprite('nt312_00', 2)
    sprite('nt312_01', 2)
    sprite('nt312_02', 2)
    sprite('nt312_03', 8)
    sprite('nt312_04', 4)
    sprite('nt312_05', 3)
    sprite('nt312_06', 4)


@State
def CmnActAirLockWait():
    sprite('nt045_02', 1)
    sprite('nt045_01', 3)
    sprite('nt045_00', 3)


@State
def CmnActAirLockReject():
    sprite('nt322_00', 2)
    sprite('nt322_01', 2)
    sprite('nt322_02', 8)
    sprite('nt322_03', 2)
    sprite('nt322_04', 3)
    sprite('nt322_05', 3)
    sprite('nt322_06', 3)


@State
def CmnActLandSpin():
    sprite('nt071_00', 4)
    sprite('nt071_01', 4)
    label(0)
    sprite('nt071_02', 2)
    sprite('nt071_03', 2)
    sprite('nt071_04', 2)
    sprite('nt071_05', 2)
    sprite('nt071_06', 2)
    sprite('nt071_07', 2)
    sprite('nt071_08', 2)
    sprite('nt071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('nt071_10', 6)
    sprite('nt071_11', 5)
    sprite('nt071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('nt071_02', 2)
    sprite('nt071_03', 2)
    sprite('nt071_04', 2)
    sprite('nt071_05', 2)
    sprite('nt071_06', 2)
    sprite('nt071_07', 2)
    sprite('nt071_08', 2)
    sprite('nt071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('nt077_00', 2)
    sprite('nt077_01', 2)
    sprite('nt077_00ex01', 2)
    sprite('nt077_01ex01', 2)
    sprite('nt077_00ex02', 2)
    sprite('nt077_01ex02', 2)
    sprite('nt077_00ex03', 2)
    sprite('nt077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('nt077_02', 4)
    label(0)
    sprite('nt077_03', 3)
    sprite('nt077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('nt077_05', 5)
    sprite('nt077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('nt060_07', 3)
    sprite('nt060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('nt060_11', 4)
    sprite('nt060_13', 5)


@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    sprite('nt331_00', 2)
    sprite('nt331_01', 2)
    label(0)
    sprite('nt331_02', 3)
    sprite('nt331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('nt331_04', 2)
    sprite('nt331_05', 2)
    label(0)
    sprite('nt331_06', 3)
    sprite('nt331_07', 3)
    sprite('nt331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('nt331_09', 3)
    sprite('nt331_10', 3)


@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    sprite('nt331_11', 2)
    sprite('nt331_12', 2)
    label(0)
    sprite('nt331_02', 3)
    sprite('nt331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('nt331_04', 2)
    sprite('nt331_05', 2)
    label(0)
    sprite('nt331_06', 3)
    sprite('nt331_07', 3)
    sprite('nt331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('nt331_13', 3)
    sprite('nt331_14', 3)
    sprite('nt020_05', 3)
    sprite('nt020_06', 3)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('nt333_00', 3)
    sprite('nt333_01', 3)
    sprite('nt333_02', 3)
    CharacterFlash(16639, 20, 1)
    ParticleLayer(11)
    CreateParticle('ntef_333_kyushu', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    sprite('nt333_03', 32767)
    CreateObject('EMB_NT_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('nt333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('nt333_05', 3)
    CreateObject('ntef_OverDrive', 0)
    CreateParticle('ntef_333_kaiho', 0)
    CreateParticle('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)
    sprite('nt333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('nt333_08', 6)
    sprite('nt333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('nt333_10', 3)
    sprite('nt333_11', 3)
    sprite('nt333_12', 3)
    CharacterFlash(16639, 20, 1)
    ParticleLayer(11)
    CreateParticle('ntef_333_kyushu', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    sprite('nt333_13', 32767)
    CreateObject('EMB_NT_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('nt333_14', 3)
    label(0)
    sprite('nt333_05', 3)
    CreateObject('ntef_OverDrive', 0)
    CreateParticle('ntef_333_kaiho', 0)
    CreateParticle('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)
    sprite('nt333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('nt333_15', 6)
    sprite('nt333_16', 6)


@Subroutine
def Drive_Func():

    def upon_RELEASE_D():
        SLOT_51 = 1
        clearUponHandler(RELEASE_D)
    if SLOT_OverdriveTimer:
        SLOT_58 = 1
        HitOrBlockCancel('ShortDash')

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            BufferedOrPressedGoto('ShortDash')


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(300)
        AttackP2(80)
        AirPushbackY(12000)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A_2')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('nt200_00', 2)
    PerInertia(60)
    sprite('nt200_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('nt200_02', 1)
    sprite('nt200_03', 3)
    sprite('nt200_04', 3)
    Recovery()
    Unknown2063()
    sprite('nt200_05', 3)
    sprite('nt200_06', 3)
    sprite('nt200_07', 3)


@State
def NmlAtk5A_2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        AirPushbackY(18000)
        CHGroundedHitstunAnimation(2)
        CHStagger(37)
        CHCrumple(35)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('nt200_06', 2)
    sprite('nt200_08', 2)
    physicsXImpulse(3000)
    DashEffects(100, 1, 1)
    sprite('nt200_09', 3)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    physicsXImpulse(55000)
    SetAcceleration(-5000)
    sprite('nt200_10', 4)
    EndMomentum(1)
    sprite('nt200_11', 3)
    Recovery()
    Unknown2063()
    sprite('nt200_12', 4)
    sprite('nt200_13', 4)
    sprite('nt200_14', 3)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(550)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockJumpCancel(1)
        StayAfterMovement(1, 0)
    sprite('nt201_00', 3)
    sprite('nt201_01', 2)
    physicsXImpulse(8000)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_1')
    sprite('nt201_02', 2)
    StartMultihit()
    XImpulseAcceleration(150)
    sprite('nt201_03', 3)
    XImpulseAcceleration(80)
    sprite('nt201_04', 4)
    XImpulseAcceleration(0)
    Recovery()
    Unknown2063()
    sprite('nt201_05', 3)
    sprite('nt201_06', 4)
    sprite('nt201_07', 4)
    sprite('nt201_08', 3)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
    sprite('nt202_00', 2)
    sprite('nt202_01', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('nt202_02', 3)
    RandomCommonVoiceline(2)
    physicsXImpulse(4000)
    sprite('nt202_03', 3)
    XImpulseAcceleration(600)
    sprite('nt202_04', 4)
    XImpulseAcceleration(20)
    sprite('nt202_05', 4)
    XImpulseAcceleration(0)
    Recovery()
    Unknown2063()
    sprite('nt202_06', 4)
    sprite('nt202_07', 4)
    sprite('nt202_08', 3)
    sprite('nt202_09', 3)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(900)
        AttackP2(89)
        AirPushbackX(28000)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Floorslide(10)
        PushbackX(24800)
        Hitstop(15)
        UseSlashHitspark(1)
        callSubroutine('Drive_Func')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('nt203_00', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('nt203_01', 3)
    SpriteIfNot0(2, 2, 58)
    BeginBuffer('ShortDash')
    sprite('nt203_02', 3)
    CreateObject('ntef_D_bodyaura', 1)
    CreateObject('ntef_D_handaura_3D', 0)
    CreateObject('ntef_D_handaura', 0)
    CreateParticle('ntef_D_aura', 2)
    sprite('nt203_03', 3)
    BufferedOrPressedGoto('ShortDash')
    sprite('nt203_04', 3)
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('nt203_02ex01', 3)
    CreateParticle('ntef_D_aura', 2)
    SLOT_51 = 0
    ScreenShake(3000, 9000)
    LandingEffects(-1, 1, 0)
    sprite('nt203_03ex01', 2)
    if SLOT_58:
        conditionalSendToLabel(0)
    sprite('nt203_03ex01', 1)
    sprite('nt203_04ex01', 3)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt203_02ex01', 3)
    sprite('nt203_03ex01', 3)
    loopRest()
    label(0)
    sprite('nt203_05ex01', 3)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt203_06ex01', 3)
    sprite('nt203_07ex01', 3)
    if SLOT_OverdriveTimer:
        SmartRandomVoiceline('nt106', 100, 'nt301', 100, '', 0, '', 0)
    else:
        SmartRandomVoiceline('nt106', 100, 'nt300', 100, '', 0, '', 0)
    PrivateSE('ntse_04')
    CreateParticle('ntef_D_aura', 0)
    sprite('nt203_08ex01', 3)
    DisallowGoto2('ShortDash')
    CallCustomizableParticle('ntef_D_aura', 0)
    CallCustomizableParticle('ntef_D_aura', 1)
    CallCustomizableParticle('ntef_D_aura', 2)
    CallCustomizableParticle('ntef_D_aura', 3)
    Damage(1350)
    ChipPercentage(20)
    AttackP2(94)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(19)
    AirPushbackX(42000)
    AirPushbackY(15000)
    Stagger(35)
    Crumple(25)
    AirUntechableTime(40)
    Floorslide(20)
    Hitstop(20)
    HitAirUnblockable(3)
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(24)
    if SLOT_58:
        Stagger(45)
        Crumple(35)
        GuardCrushHitstun(34)
    sprite('nt203_09ex01', 2)
    CallCustomizableParticle('ntef_D_aura', 0)
    CallCustomizableParticle('ntef_D_aura', 1)
    CallCustomizableParticle('ntef_D_aura', 2)
    CallCustomizableParticle('ntef_D_aura', 3)
    sprite('nt203_10ex01', 3)
    ParticleSize(750)
    CallCustomizableParticle('ntef_D_aura', 0)
    ParticleSize(750)
    CallCustomizableParticle('ntef_D_aura', 1)
    ParticleSize(750)
    CallCustomizableParticle('ntef_D_aura', 2)
    Recovery()
    Unknown2063()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt203_05', 2)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    sprite('nt203_06', 1)
    sprite('nt203_07', 1)
    SmartRandomVoiceline('nt104', 100, 'nt105', 100, 'nt107', 100, '', 0)
    PrivateSE('ntse_05')
    sprite('nt203_08', 3)
    DisallowGoto2('ShortDash')
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt203_09', 2)
    sprite('nt203_10', 3)
    Recovery()
    Unknown2063()
    label(9)
    sprite('nt203_11', 3)
    sprite('nt203_12', 4)
    sprite('nt203_13', 4)
    sprite('nt203_14', 4)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(90)
        PushbackX(12000)
        HitLow(2)
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
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    if PreviousStateCheck('NmlAtk2A'):
        conditionalSendToLabel(1)
    sprite('nt230_00', 2)
    PerInertia(60)
    sprite('nt230_01', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('nt230_02', 2)
    RandomCommonVoiceline(0)
    sprite('nt230_03', 2)
    gotoLabel(9)
    label(1)
    sprite('nt230_01', 3)
    sprite('nt230_02', 3)
    CommonSE('004_swing_grap_1_0')
    RandomCommonVoiceline(0)
    sprite('nt230_03', 2)
    label(9)
    sprite('nt230_04', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('nt230_02', 3)
    sprite('nt230_01', 3)
    sprite('nt230_00', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        Damage(480)
        HitLow(2)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('nt231_00', 3)
    sprite('nt231_01', 2)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_1')
    sprite('nt231_02', 2)
    sprite('nt231_03', 3)
    sprite('nt231_04', 3)
    Recovery()
    Unknown2063()
    sprite('nt231_05', 3)
    sprite('nt231_06', 2)
    sprite('nt231_07', 2)
    sprite('nt231_08', 2)
    sprite('nt231_09', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Damage(850)
        AirUntechableTime(23)
        AirPushbackX(3000)
        AirPushbackY(27000)
        AirHitstunAnimation(10)
        MoveAttributes(0, 1, 0, 0, 0)
        CHGroundedHitstunAnimation(10)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('nt232_00', 3)
    sprite('nt232_01', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('nt232_02', 2)
    RandomCommonVoiceline(2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('nt232_03', 2)
    sprite('nt232_04', 3)
    sprite('nt232_04', 3)
    setInvincible(0)
    sprite('nt232_05', 4)
    Recovery()
    Unknown2063()
    sprite('nt232_06', 5)
    sprite('nt232_07', 5)
    sprite('nt232_08', 5)
    sprite('nt232_09', 3)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(780)
        AttackP2(79)
        AirUntechableTime(40)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(13000)
        CHHardKnockdown(1)
        HitLow(2)
        StayAfterMovement(1, 0)
    sprite('nt234_00', 2)
    sprite('nt234_01', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('nt234_02', 2)
    RandomCommonVoiceline(2)
    sprite('nt234_03', 3)
    sprite('nt234_04', 2)
    sprite('nt234_05', 2)
    sprite('nt234_06', 3)
    Recovery()
    Unknown2063()
    sprite('nt234_07', 3)
    sprite('nt234_08', 3)
    sprite('nt234_09', 2)
    sprite('nt234_10', 3)
    sprite('nt234_11', 3)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(5)
        Damage(900)
        AttackP1(90)
        AttackP2(89)
        AirPushbackX(28000)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Floorslide(10)
        PushbackX(24800)
        Hitstop(15)
        UseSlashHitspark(1)
        HitLow(2)
        callSubroutine('Drive_Func')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        StayAfterMovement(1, 0)
    sprite('nt233_00', 3)
    sprite('nt233_01', 3)
    SpriteIfNot0(1, 2, 58)
    CreateObject('ntef_D_bodyaura', 1)

    def RunOnObject_1():
        AlphaValue(200)
        Size(900)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    BeginBuffer('ShortDash')
    sprite('nt233_02', 3)
    sprite('nt233_03', 3)
    BufferedOrPressedGoto('ShortDash')
    sprite('nt233_01', 3)
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('nt233_02', 3)
    SLOT_51 = 0
    sprite('nt233_03', 3)
    ScreenShake(3000, 9000)
    LandingEffects(0, 1, 0)
    sprite('nt233_01', 1)
    if SLOT_58:
        conditionalSendToLabel(0)
    sprite('nt233_01', 2)
    sprite('nt233_02', 3)
    sprite('nt233_03', 3)
    sprite('nt233_01', 3)
    loopRest()
    label(0)
    sprite('nt233_04ex01', 3)
    sprite('nt233_05ex01', 3)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    sprite('nt233_06ex01', 4)
    if SLOT_OverdriveTimer:
        SmartRandomVoiceline('nt106', 100, 'nt301', 100, '', 0, '', 0)
    else:
        SmartRandomVoiceline('nt106', 100, 'nt300', 100, '', 0, '', 0)
    PrivateSE('ntse_04')
    sprite('nt233_07ex01', 3)
    DisallowGoto2('ShortDash')
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    CreateParticle('ntef_D_aura', 6)
    Damage(1350)
    ChipPercentage(20)
    AttackP2(94)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(19)
    AirPushbackX(42000)
    AirPushbackY(15000)
    Stagger(35)
    Crumple(25)
    AirUntechableTime(40)
    Floorslide(20)
    Hitstop(20)
    Wallbounce(1)
    NonCornerWallbounce(1)
    Wallstick(1)
    WallstickDuration(31)
    AirHitstunAfterWallbounce(20)
    HitAirUnblockable(3)
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(24)
    if SLOT_58:
        Stagger(45)
        Crumple(35)
        GuardCrushHitstun(34)
    sprite('nt233_08ex01', 2)
    sprite('nt233_09ex01', 3)
    Recovery()
    Unknown2063()
    EnableAfterimage(0)
    sprite('nt233_10ex01', 3)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt233_04', 3)
    sprite('nt233_05', 2)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    sprite('nt233_06', 1)
    SmartRandomVoiceline('nt104', 100, 'nt105', 100, 'nt107', 100, '', 0)
    PrivateSE('ntse_05')
    sprite('nt233_07', 3)
    DisallowGoto2('ShortDash')
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt233_08', 2)
    sprite('nt233_09', 3)
    Recovery()
    Unknown2063()
    EnableAfterimage(0)
    sprite('nt233_10', 3)
    label(9)
    sprite('nt233_11', 3)
    sprite('nt233_12', 3)
    sprite('nt233_13', 3)
    sprite('nt233_14', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        Damage(300)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    if PreviousStateCheck('NmlAtk2A'):
        conditionalSendToLabel(1)
    sprite('nt250_00', 2)
    sprite('nt250_01', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('nt250_02', 2)
    RandomCommonVoiceline(0)
    sprite('nt250_03', 3)
    gotoLabel(9)
    label(1)
    sprite('nt250_01', 3)
    sprite('nt250_02', 3)
    CommonSE('004_swing_grap_1_0')
    RandomCommonVoiceline(0)
    sprite('nt250_03', 3)
    label(9)
    sprite('nt250_04', 3)
    Recovery()
    Unknown2063()
    sprite('nt250_01', 3)
    sprite('nt250_00', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AttackP1(80)
        Damage(580)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('nt251_00', 3)
    sprite('nt251_01', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('nt251_02', 2)
    RandomCommonVoiceline(1)
    sprite('nt251_03', 4)
    sprite('nt251_04', 2)
    sprite('nt251_05', 2)
    Recovery()
    Unknown2063()
    sprite('nt251_06', 4)
    sprite('nt251_07', 4)
    sprite('nt251_08', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        Damage(900)
        AirUntechableTime(20)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('nt252_00', 2)
    sprite('nt252_01', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('nt252_02', 2)
    RandomCommonVoiceline(2)
    sprite('nt252_03', 2)
    sprite('nt252_04', 3)
    sprite('nt252_05', 3)
    sprite('nt252_06', 3)
    Recovery()
    Unknown2063()
    sprite('nt252_07', 3)
    sprite('nt252_08', 3)
    sprite('nt252_09', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        Damage(900)
        AttackP2(79)
        BonusProration(110)
        AirPushbackX(12000)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        Hitstop(15)
        UseSlashHitspark(1)
        HitOverhead(0)
        callSubroutine('Drive_Func')
    sprite('nt253_00', 3)
    sprite('nt253_01', 3)
    SpriteIfNot0(1, 2, 58)
    CreateObject('ntef_D_bodyaura', 1)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    ForcedLandingRecovery(6, 1)
    sprite('nt253_02', 3)
    sprite('nt253_03', 3)
    sprite('nt253_01', 3)
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('nt253_02', 3)
    SLOT_51 = 0
    sprite('nt253_03', 3)
    ScreenShake(5000, 5000)
    XImpulseAcceleration(20)
    YAccel(0)
    PerGravity(0)
    PerAcceleration(0)
    PerInertia(0)
    if SLOT_58:
        conditionalSendToLabel(0)
    sprite('nt253_01', 3)
    loopRest()
    label(0)
    sprite('nt253_04', 3)
    setGravity(-200)
    SpriteIfNot0(2, 2, 58)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt253_05ex01', 3)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    SpriteIfNot0(2, 2, 58)
    CreateParticle('ntef_D_aura', 0)
    PrivateSE('ntse_04')
    sprite('nt253_06ex01', 6)
    EndYPhysicsImpulse()
    SpriteIfNot0(2, 2, 58)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt253_07ex01', 3)
    if SLOT_OverdriveTimer:
        SmartRandomVoiceline('nt106', 100, 'nt301', 100, '', 0, '', 0)
    else:
        SmartRandomVoiceline('nt106', 100, 'nt300', 100, '', 0, '', 0)
    SpriteIfNot0(2, 2, 58)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt253_08ex01', 3)
    AttackLevel_(5)
    Damage(1350)
    ChipPercentage(20)
    AttackP2(84)
    GroundedHitstunAnimation(1)
    AirPushbackY(-82000)
    YImpulseBeforeWallbounce(0)
    AirUntechableTime(60)
    Hitstop(20)
    GroundBounce(1)
    BouncePercentage(35)
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(24)
    ForcedLandingRecovery(12, 1)
    if SLOT_58:
        GuardCrushHitstun(34)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    CreateParticle('ntef_D_aura', 6)
    CreateParticle('ntef_D_aura', 7)
    sprite('nt253_09ex01', 2)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    sprite('nt253_10', 3)
    CreateObject('ntef_253_b', -1)
    Recovery()
    Unknown2063()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt253_04', 1)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt253_05', 1)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt253_06', 1)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    SmartRandomVoiceline('nt104', 100, 'nt105', 100, 'nt108', 100, '', 0)
    PrivateSE('ntse_05')
    sprite('nt253_07', 1)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt253_08', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    sprite('nt253_09', 2)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt253_10', 3)
    CreateObject('ntef_253_a', -1)
    Recovery()
    Unknown2063()
    label(9)
    sprite('nt253_11', 3)
    sprite('nt253_12', 4)
    sprite('nt253_13', 4)
    sprite('nt253_14', 4)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(80)
        BonusProration(110)
        Damage(700)
        GroundedHitstunAnimation(3)
        AirPushbackY(-30000)
        HardKnockdown(1)
        HitOverhead(2)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('nt210_00', 3)
    sprite('nt210_01', 5)
    Voiceline('nt104')
    sprite('nt210_02', 3)
    sprite('nt210_03', 3)
    PreDashEffects(100, 1, 1)
    physicsXImpulse(18000)
    sprite('nt210_04', 3)
    sprite('nt210_05', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('nt210_06', 3)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(30)
    sprite('nt210_07', 3)
    sprite('nt210_08', 4)
    EndMomentum(1)
    Recovery()
    Unknown2063()
    sprite('nt210_09', 4)
    sprite('nt210_10', 4)
    sprite('nt210_11', 4)
    sprite('nt210_12', 4)
    sprite('nt210_13', 4)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(80)
        Damage(750)
        AirHitstunAnimation(13)
        AirUntechableTime(30)
        AirPushbackX(12000)
        AirPushbackY(20000)
        PushbackX(19800)
        MoveAttributes(1, 0, 0, 0, 0)
        HitAirUnblockable(0)
        uponSendToLabel(LANDING, 9)
    sprite('nt211_00', 2)
    sprite('nt211_01', 2)
    sprite('nt211_02', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    physicsXImpulse(15000)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    PerInertia(50)
    JumpEffects(0, 0)
    sprite('nt211_03', 3)
    Voiceline('nt103')
    CommonSE('004_swing_grap_1_2')
    sprite('nt211_04', 3)
    sprite('nt211_05', 3)
    XImpulseAcceleration(80)
    sprite('nt211_06', 4)
    XImpulseAcceleration(50)
    sprite('nt211_07', 2)
    Recovery()
    Unknown2063()
    sprite('nt211_08', 32767)
    loopRest()
    label(9)
    sprite('nt211_09', 2)
    setInvincible(0)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(50)
    sprite('nt211_10', 2)
    XImpulseAcceleration(50)
    sprite('nt211_11', 2)
    XImpulseAcceleration(0)
    sprite('nt211_12', 2)
    sprite('nt211_13', 2)
    sprite('nt211_14', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(80)
        Damage(800)
        AirUntechableTime(30)
        Hitstun(25)
        PushbackX(12000)
        MoveAttributes(1, 0, 0, 0, 0)
        CrouchWhiff(1)
        HitAirUnblockable(0)
        SpecialCancel(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        uponSendToLabel(LANDING, 9)
    sprite('nt212_00', 2)
    sprite('nt212_01', 2)
    Voiceline('nt109')
    sprite('nt212_02', 2)
    sprite('nt212_03', 8)
    EnableCollision(0)
    EndMomentum(1)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    setGravity(1600)
    JumpEffects(0, 0)
    CommonSE('000_airdash_1')
    sprite('nt212_04', 8)
    sprite('nt212_05', 3)
    CommonSE('004_swing_grap_1_2')
    XImpulseAcceleration(70)
    sprite('nt212_05', 3)
    XImpulseAcceleration(70)
    sprite('nt212_06', 3)
    XImpulseAcceleration(70)
    sprite('nt212_06', 3)
    EnableCollision(1)
    sprite('nt212_07', 2)
    sprite('nt212_08', 2)
    sprite('nt212_09', 2)
    XImpulseAcceleration(30)
    Recovery()
    Unknown2063()
    sprite('nt212_10', 2)
    sprite('nt212_11', 2)
    sprite('nt212_12', 32767)
    label(9)
    sprite('nt212_13', 2)
    EndMomentum(1)
    EnableAfterimage(0)
    LandingEffects(100, 1, 1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    sprite('nt212_14', 2)
    sprite('nt212_15', 2)
    sprite('nt212_16', 2)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1000)
        AttackP2(89)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(40)
        AirPushbackX(24000)
        Hitstop(15)
        UseSlashHitspark(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk6C')
        callSubroutine('Drive_Func')
    sprite('nt213_00', 3)
    sprite('nt213_01', 3)
    SpriteIfNot0(1, 2, 58)
    BeginBuffer('ShortDash')
    CreateObject('ntef_D_bodyaura', 1)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    sprite('nt213_02', 3)
    sprite('nt213_03', 3)
    BufferedOrPressedGoto('ShortDash')
    sprite('nt213_01', 3)
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('nt213_02ex01', 3)
    SLOT_51 = 0
    sprite('nt213_03ex01', 3)
    ScreenShake(3000, 9000)
    LandingEffects(-1, 1, 0)
    sprite('nt213_01ex01', 3)
    if SLOT_58:
        conditionalSendToLabel(0)
    sprite('nt213_02ex01', 3)
    sprite('nt213_03ex01', 3)
    sprite('nt213_01ex01', 3)
    sprite('nt213_02ex01', 3)
    loopRest()
    label(0)
    sprite('nt213_04ex01', 3)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    sprite('nt213_05ex01', 4)
    sprite('nt213_06ex01', 4)
    if SLOT_OverdriveTimer:
        SmartRandomVoiceline('nt106', 100, 'nt301', 100, '', 0, '', 0)
    else:
        SmartRandomVoiceline('nt106', 100, 'nt300', 100, '', 0, '', 0)
    PrivateSE('ntse_04')
    sprite('nt213_07ex01', 3)
    DisallowGoto2('ShortDash')
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    CreateParticle('ntef_D_aura', 6)
    CreateParticle('ntef_D_aura', 7)
    CreateParticle('ntef_D_aura', 8)
    CreateParticle('ntef_D_aura', 9)
    CreateParticle('ntef_D_aura', 10)
    Damage(1500)
    ChipPercentage(20)
    AttackP2(94)
    AirPushbackX(42000)
    AirPushbackY(36000)
    AirUntechableTime(60)
    Wallbounce(1)
    WallbounceReboundTime(5)
    Hitstop(20)
    HitAirUnblockable(3)
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(24)
    FatalCounter(1)
    if SLOT_58:
        GuardCrushHitstun(34)
    sprite('nt213_08ex01', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    sprite('nt213_09ex01', 3)
    Recovery()
    Unknown2063()
    sprite('nt213_10ex01', 3)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt213_04', 3)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    TriggerUponForState('ntef_D_bodyaura', 32)
    sprite('nt213_05', 3)
    sprite('nt213_06', 2)
    SmartRandomVoiceline('nt104', 100, 'nt105', 100, 'nt108', 100, '', 0)
    PrivateSE('ntse_05')
    sprite('nt213_07', 3)
    DisallowGoto2('ShortDash')
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    sprite('nt213_08', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    sprite('nt213_09', 3)
    Recovery()
    Unknown2063()
    sprite('nt213_10', 3)
    label(9)
    sprite('nt213_11', 3)
    sprite('nt213_12', 4)
    sprite('nt213_13', 4)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('nt300_00', 5)
    sprite('nt300_01', 5)
    sprite('nt300_02', 5)
    sprite('nt300_03', 5)
    SmartRandomVoiceline('nt404', 100, 'nt405', 100, '', 0, '', 0)
    sprite('nt300_04', 6)
    sprite('nt300_03', 5)
    sprite('nt300_02', 5)
    sprite('nt300_03', 5)
    sprite('nt300_04', 6)
    sprite('nt300_03', 5)
    sprite('nt300_02', 5)
    sprite('nt300_05', 6)
    sprite('nt300_06', 6)
    sprite('nt300_07', 5)
    sprite('nt300_08', 5)
    sprite('nt300_09', 6)
    sprite('nt300_08', 5)
    sprite('nt300_07', 5)
    sprite('nt300_08', 5)
    sprite('nt300_09', 6)
    sprite('nt300_08', 5)
    sprite('nt300_07', 5)
    sprite('nt300_10', 7)
    sprite('nt300_11', 4)
    sprite('nt300_12', 4)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('nt202_00', 3)
    sprite('nt202_01', 3)
    sprite('nt202_02', 3)
    physicsXImpulse(4000)
    sprite('nt202_03', 3)
    XImpulseAcceleration(600)
    CommonSE('004_swing_grap_1_2')
    sprite('nt202_04', 3)
    XImpulseAcceleration(20)
    sprite('nt202_04', 5)
    sprite('nt202_05', 6)
    XImpulseAcceleration(0)
    sprite('nt202_06', 6)
    sprite('nt202_07', 6)
    sprite('nt202_08', 6)
    sprite('nt202_09', 6)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(12)
        AirPushbackX(45000)
        AirPushbackY(18000)
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
        StayAfterMovement(1, 0)
        SLOT_2 = SLOT_4
        if SLOT_2:
            AddInertia(10000)

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
    sprite('nt340_00', 3)
    sprite('nt340_01', 1)
    E0EAEffect('GuardCrushWind', 0)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    sprite('nt340_01', 1)
    CharacterFlash(16763080, 8, 2)
    sprite('nt340_02', 3)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('rgef_413_hensin01', 0)
    loopRest()
    label(100)
    sprite('nt340_03', 3)
    sprite('nt340_04', 3)
    sprite('nt340_05', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('nt340_06', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('nt340_07', 3)
    Voiceline('nt159')
    SetXCollisionFromOrigin(200)
    sprite('nt340_08', 3)
    physicsXImpulse(24000)
    ScreenShake(8000, 0)
    KnockdownEffects(100, 1, 1)
    sprite('nt340_09', 1)
    CreateObject('ntef_340', -1)
    SetXCollisionFromOrigin(-1)
    sprite('nt340_09', 2)
    XImpulseAcceleration(0)
    AttackOff()
    EnableAfterimage(0)
    sprite('nt340_10', 3)
    sprite('nt340_11', 3)
    sprite('nt340_12', 3)
    AddX(10000)
    sprite('nt340_13', 3)
    AddX(5000)
    sprite('nt340_14', 3)
    AddX(5000)
    sprite('nt340_15', 3)
    AddX(5000)
    sprite('nt340_16', 3)
    AddX(10000)
    sprite('nt340_17', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('nt310_00', 3)
    sprite('nt310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('nt310_02', 3)
    sprite('nt310_03', 3)
    SmartVoiceline('nt155')
    sprite('nt310_04', 3)
    sprite('nt310_05', 11)
    sprite('nt310_06', 3)
    sprite('nt310_07', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirUntechableTime(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Wallbounce(1)
        AirHitstunAfterWallbounce(60)
        Wallstick(1)
        WallstickDuration(30)
        AirPushbackY(40000)
        AirPushbackX(10000)
        StarterRating(2)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 0)
    sprite('nt310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('nt311_00', 3)
    SmartVoiceline('nt153')
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('nt311_01', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('nt311_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('nt311_03', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('nt311_04', 4)
    AddX(60000)
    physicsXImpulse(12000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    EnableCollision(1)
    JumpEffects(0, 0)
    sprite('nt311_05', 4)
    sprite('nt311_06', 4)
    sprite('nt311_07', 4)
    sprite('nt311_08', 32767)
    label(0)
    sprite('nt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt024_01', 2)
    WhiffNormalCancel(1)
    WhiffFDashCancel(1)
    sprite('nt024_02', 2)
    sprite('nt024_03', 2)
    sprite('nt024_04', 2)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('nt310_00', 3)
    CommonSE('010_swing_sword_0')
    sprite('nt310_01', 3)
    sprite('nt310_02', 3)
    sprite('nt310_03', 3)
    SmartVoiceline('nt155')
    sprite('nt310_04', 3)
    sprite('nt310_05', 11)
    sprite('nt310_06', 3)
    sprite('nt310_07', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(50)
        SingleProration(1)
        AirHitstunAnimation(6)
        GroundedHitstunAnimation(6)
        Hitstun(25)
        PushbackX(-4000)
        Hitstop(0)
        DamageFromStateOnly('BackThrowExe')
        StarterRating(2)
        SpecialCancel(0)
        EnableRapidCancel(0)
    sprite('nt310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('nt313_00', 1)
    SmartVoiceline('nt153')
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    sprite('nt313_00', 4)
    physicsXImpulse(60000)
    PreDashEffects(100, 1, 1)
    sprite('nt313_01', 4)
    XImpulseAcceleration(50)
    sprite('nt313_02', 4)
    XImpulseAcceleration(50)
    CreateObject('BackThrow_DashStop', 0)
    sprite('nt313_03', 4)
    EnableCollision(1)
    XImpulseAcceleration(50)
    sprite('nt313_03', 4)
    EndMomentum(1)
    sprite('nt313_04', 3)
    physicsXImpulse(-50000)
    sprite('nt313_05', 2)
    Flip()
    XImpulseAcceleration(50)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Crumple(30)
    ResetPushbackX()
    Hitstop(20)
    DamageEffect(0, '')
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        ScreenShake(8000, 0)
        SpecialCancel(1)
        EnableRapidCancel(1)
    sprite('nt313_06', 2)
    EndMomentum(1)
    sprite('nt313_07', 2)
    sprite('nt313_08', 3)
    sprite('nt313_09', 3)
    sprite('nt340_16', 3)
    sprite('nt340_17', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('nt320_00', 3)
    sprite('nt320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('nt320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('nt320_03', 3)
    SmartVoiceline('nt155')
    sprite('nt320_04', 8)
    sprite('nt320_02', 4)
    StartMultihit()
    sprite('nt320_01', 4)
    sprite('nt320_00', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(-20000)
        Floorslide(1)
        HardKnockdown(40)
        Hitstop(0)
        StarterRating(2)
        SpecialCancel(0)
        EndMomentum(1)
        ForcedLandingRecovery(0, 0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)
    sprite('nt320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('nt321_00', 3)
    SmartVoiceline('nt154')
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SetZLine(1, 50)
    sprite('nt321_01', 5)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    sprite('nt321_02', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    sprite('nt321_03', 3)
    setGravity(3000)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    sprite('nt321_04', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    label(1)
    sprite('nt321_05', 4)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    sprite('nt321_06', 4)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('nt321_07', 2)
    KnockdownEffects(100, 1, 1)
    sprite('nt321_08', 8)
    sprite('nt033_01', 3)
    uponSendToLabel(LANDING, 2)
    physicsXImpulse(-15000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    loopRest()
    label(0)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('nt033_03', 1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 4)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)


@Subroutine
def Dash_AfterImage():
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageColor_1(255, 0, 0, 255)
    AfterimageInterval(3)
    AfterimageCount(5)


@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)

        def upon_EVERY_FRAME():
            SLOT_4 = 2
        physicsXImpulse(30000)
        AddInertia(50000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AirDashEffects(0)
        WhiffSpecialCancel(1)
    sprite('nt032_02', 4)
    sprite('nt032_03', 4)
    sprite('nt032_04', 4)
    sprite('nt032_10', 4)
    XImpulseAcceleration(50)
    sprite('nt032_11', 4)


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(14000)
        Hitstop(15)
        PushbackX(24800)
        AttackDirection(0)
        WhiffCancel('Assault_2nd')
        HitOrBlockCancel('Assault_2nd')
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('Assault_En')
            Hitstop(15)
            GroundedHitstunAnimation(3)
            physicsXImpulse(40000)
            callSubroutine('Dash_AfterImage')
            if not PreviousStateCheck('ShortDash'):
                AirDashEffects(0)
        else:
            physicsXImpulse(20000)
    sprite('nt400_00', 3)
    Voiceline('nt200')
    PreDashEffects(100, 1, 1)
    sprite('nt400_01', 3)
    sprite('nt400_02', 3)
    SetYCollisionFromOrigin(250)
    CommonSE('004_swing_grap_1_1')
    sprite('nt400_03', 3)
    CreateObject('ntef_400_aura', -1)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('nt400_04', 3)
    SetYCollisionFromOrigin(-1)
    sprite('nt400_05', 2)
    WhiffCancelEnable(1)
    Recovery()
    XImpulseAcceleration(10)
    sprite('nt400_06', 3)
    EnableAfterimage(0)
    sprite('nt400_07', 3)
    sprite('nt400_08', 3)
    XImpulseAcceleration(0)
    SkidEffects(100, 1, 1)
    sprite('nt400_09', 3)
    sprite('nt400_10', 3)
    WhiffCancelEnable(0)
    ChainCancel(0)


@State
def Assault_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AirPushbackX(28000)
        AirPushbackY(14000)
        AirUntechableTime(28)
        Hitstop(15)
        AttackDirection(0)
        FatalCounter(1)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        WhiffCancel('Assault_3rdYoko')
        WhiffCancel('Assault_3rdTate')
        HitOrBlockCancel('Assault_3rdYoko')
        HitOrBlockCancel('Assault_3rdTate')
    sprite('nt400_07', 1)
    physicsXImpulse(50000)
    SetYCollisionFromOrigin(250)
    PreDashEffects(100, 1, 1)
    sprite('nt400_08', 1)
    sprite('nt401_00', 2)
    XImpulseAcceleration(50)
    sprite('nt401_01', 2)
    Voiceline('nt201')
    PrivateSE('ntse_02')
    CreateObject('ntef_401_aura1', -1)
    XImpulseAcceleration(50)
    sprite('nt401_01', 2)
    XImpulseAcceleration(50)
    sprite('nt401_02', 3)
    DespawnEAEffect('ntef_401_aura1')
    CreateObject('ntef_401_aura2', -1)
    SetXCollisionFromOrigin(150)
    SetYCollisionFromOrigin(-1)
    AddX(100000)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt401_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    EnableAfterimage(0)
    sprite('nt401_04', 5)
    sprite('nt401_05', 4)
    sprite('nt401_06', 5)
    sprite('nt401_07', 4)
    WhiffCancelEnable(0)
    ChainCancel(0)


@State
def Assault_3rdYoko():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AirUntechableTime(40)
        GroundedHitstunAnimation(1)
        AirPushbackX(44000)
        CHAirPushbackX(88000)
        AirPushbackY(16000)
        CHWallbounce(1)
        AttackDirection(0)
        FatalCounter(1)
        if SLOT_59:
            GroundedHitstunAnimation(19)
            AirHitstunAnimation(19)

            def upon_OPPONENT_HIT():
                BeginBuffer('ShortDash')
            callSubroutine('Dash_AfterImage')
    sprite('nt402_00', 2)
    sprite('nt402_01', 2)
    sprite('nt402_02', 3)
    physicsXImpulse(4000)
    if SLOT_59:
        XSpeed(1000)
    sprite('nt402_03', 3)
    XImpulseAcceleration(200)
    DashEffects(100, 1, 1)
    sprite('nt402_04', 3)
    PrivateSE('ntse_03')
    CreateObject('ntef_402', -1)
    XImpulseAcceleration(300)
    SetXCollisionFromOrigin(150)
    DashEffects(100, 1, 1)
    sprite('nt402_05', 3)
    Voiceline('nt202')
    XImpulseAcceleration(150)
    SetXCollisionFromOrigin(200)
    PreDashEffects(100, 1, 1)
    sprite('nt402_06', 4)
    sprite('nt402_07', 3)
    SetXCollisionFromOrigin(-1)
    Recovery()
    loopRest()
    label(9)
    sprite('nt402_08', 4)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(50)
    BufferedOrPressedGoto('ShortDash')
    EnableAfterimage(0)
    sprite('nt402_09', 4)
    EndMomentum(1)
    sprite('nt402_10', 7)
    sprite('nt402_11', 4)
    DisallowGoto2('ShortDash')


@State
def Assault_3rdTate():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(60)
        AirUntechableTime(30)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(18)
        CHAirHitstunAnimation(18)
        AirPushbackX(1000)
        AirPushbackY(42000)
        Hitstop(18)
        HitJumpCancel(1)
        StayAfterMovement(1, 0)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
    sprite('keep', 1)
    StartMultihit()
    sprite('nt403_00', 2)
    physicsXImpulse(2000)
    if SLOT_59:
        XImpulseAcceleration(200)
    sprite('nt403_01', 2)
    XImpulseAcceleration(200)
    PreDashEffects(100, 1, 1)
    sprite('nt403_01', 2)
    XImpulseAcceleration(300)
    PreDashEffects(100, 1, 1)
    sprite('nt403_01', 2)
    XImpulseAcceleration(400)
    sprite('nt403_02', 2)
    Voiceline('nt203')
    XImpulseAcceleration(50)
    sprite('nt403_02', 2)
    PrivateSE('ntse_03')
    SkidEffects(100, 1, 1)
    XImpulseAcceleration(50)
    sprite('nt403_03', 2)
    CreateObject('ntef_403', -1)
    XImpulseAcceleration(20)
    sprite('nt403_04ex01', 2)
    KnockdownEffects(100, 1, 1)
    ScreenShake(5000, 10000)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('nt403_04', 6)
    AirPushbackY(36000)
    sprite('nt403_05', 3)
    Recovery()
    sprite('nt403_06', 7)
    sprite('nt403_07', 4)
    sprite('nt403_08', 4)
    sprite('nt403_09', 4)
    sprite('nt403_10', 4)
    sprite('nt403_11', 4)


@State
def EdgeAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        CHGroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackY(33000)
        AirPushbackX(12000)
        AirUntechableTime(38)
        Hitstop(7)
        UseSlashHitspark(1)
        SLOT_59 = 0
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('EdgeAssault_En')
            AttackLevel_(4)
            GroundedHitstunAnimation(2)
            Crumple(32)
            PushbackX(12000)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                if SLOT_51:
                    Damage(1200)
                    AirHitstunAnimation(2)
                    CHGroundedHitstunAnimation(2)
                    Stagger(14)
                    Crumple(99)
                    EnableEmergencyTechAirHit(1)
                    SetXCollisionFromOrigin(40)
                    EnableCollision(0)
                    ScreenShake(5000, 5000)
                    SLOT_52 = 1
            callSubroutine('Dash_AfterImage')
    if SLOT_2:
        conditionalSendToLabel(10)
    sprite('nt404_00', 4)
    CreateParticle('ntef_D_aura', 0)
    sprite('nt404_01', 6)
    CreateParticle('ntef_D_aura', 0)
    PrivateSE('ntse_04')
    sprite('nt404_02', 2)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    Voiceline('nt204')
    sprite('nt404_03', 2)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    sprite('nt404_04', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    sprite('nt404_05', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 3)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('nt404_00', 4)
    physicsXImpulse(4000)
    CreateParticle('ntef_D_aura', 0)
    SkidEffects(100, 1, 0)
    sprite('nt404_01', 4)
    PrivateSE('ntse_04')
    CreateParticle('ntef_D_aura', 0)
    sprite('nt404_02', 2)
    Voiceline('nt204')
    XImpulseAcceleration(300)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    PreDashEffects(100, 1, 1)
    sprite('nt404_03', 2)
    XImpulseAcceleration(400)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    AirDashEffects(0)
    sprite('nt404_04', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    CreateParticle('ntef_D_aura', 5)
    if SLOT_19 <= 200000:
        CopyFromRightToLeft(23, 2, 51, 22, 2, 37)
    sprite('nt404_05', 3)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 3)
    XImpulseAcceleration(50)
    EnableAfterimage(0)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(9)
    sprite('nt404_10', 2)
    SetXCollisionFromOrigin(-1)
    EnableCollision(1)
    Flip()
    XImpulseAcceleration(80)
    sprite('nt404_11', 3)
    EnableAfterimage(0)
    LandingEffects(100, 1, 0)
    XImpulseAcceleration(60)
    sprite('nt404_11', 4)
    SkidEffects(0, 1, 1)
    sprite('nt404_12', 3)
    XImpulseAcceleration(60)
    SkidEffects(0, 1, 0)
    sprite('nt404_12', 4)
    SkidEffects(0, 1, 0)
    sprite('nt210_11ex01', 2)
    XImpulseAcceleration(0)
    sprite('nt210_12ex01', 2)
    XImpulseAcceleration(0)
    sprite('nt210_13ex01', 3)
    ExitState()
    label(9)
    sprite('nt404_07', 4)
    XImpulseAcceleration(30)
    EnableCollision(1)
    sprite('nt404_08', 4)
    XImpulseAcceleration(30)
    sprite('nt404_09', 4)
    EnableAfterimage(0)
    XImpulseAcceleration(30)
    sprite('nt402_10', 3)
    XImpulseAcceleration(30)
    sprite('nt402_11', 2)
    XImpulseAcceleration(0)


@State
def AntiAirC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(44000)
        HitAirUnblockable(3)
        uponSendToLabel(LANDING, 9)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('AntiAirC_En')
            AirPushbackX(14000)
            physicsXImpulse(40000)
            callSubroutine('Dash_AfterImage')
        else:
            physicsXImpulse(20000)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            BeginBuffer('AntiAir2nd')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                HitAirUnblockable(0)
    sprite('nt405_00', 1)
    Voiceline('nt205')
    sprite('nt405_01', 2)
    XImpulseAcceleration(50)
    PreDashEffects(100, 1, 1)
    sprite('nt405_02', 1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('nt405_03', 1)
    CommonSE('004_swing_grap_1_2')
    XImpulseAcceleration(50)
    sprite('nt405_04', 3)
    CreateObject('ntef_405Weak', -1)
    JumpEffects(3, 100)
    sprite('nt405_05', 3)
    AirPushbackY(38000)
    XImpulseAcceleration(50)
    physicsYImpulse(26000)
    EndYPhysicsImpulse()
    TriggerUponForState('ntef_405Weak', 32)
    if SLOT_2:
        XImpulseAcceleration(300)
    sprite('nt405_06', 3)
    setInvincible(0)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_07', 3)
    TriggerUponForState('ntef_405Weak', 33)
    sprite('nt405_08', 3)
    sprite('nt405_09', 2)
    BufferedOrPressedGoto('AntiAir2nd')
    sprite('nt405_10', 2)
    sprite('nt405_11', 2)
    sprite('nt405_12', 3)
    sprite('nt405_13', 2)
    DisallowGoto2('AntiAir2nd')
    sprite('nt405_14', 3)
    EnableAfterimage(0)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt024_01', 3)
    sprite('nt024_02', 2)
    sprite('nt024_03', 2)
    sprite('nt024_04', 2)


@State
def AntiAirD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(60)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(44000)
        HitAirUnblockable(3)
        StarterRating(0)
        setInvincible(1)
        uponSendToLabel(LANDING, 9)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('AntiAirD_En')
            AirPushbackX(15000)
            physicsXImpulse(40000)
            callSubroutine('Dash_AfterImage')
        else:
            physicsXImpulse(20000)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            BeginBuffer('AntiAir2nd')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                HitAirUnblockable(0)
    sprite('nt405_00', 2)
    Voiceline('nt207')
    sprite('nt405_01', 2)
    XImpulseAcceleration(50)
    PreDashEffects(100, 1, 1)
    sprite('nt405_02', 2)
    sprite('nt405_03', 2)
    PrivateSE('ntse_00')
    XImpulseAcceleration(50)
    sprite('nt405_04ex', 3)
    CreateObject('ntef_405Test', 0)
    JumpEffects(3, 100)
    sprite('nt405_05ex', 3)
    XImpulseAcceleration(50)
    physicsYImpulse(40000)
    EndYPhysicsImpulse()
    if SLOT_2:
        Damage(450)
        if SLOT_137:
            DamageMultiplier(80)
        Hitstop(3)
        XImpulseAcceleration(300)
        YAccel(80)
    else:
        HitAirUnblockable(0)
    RefreshMultihit()
    sprite('nt405_06ex', 3)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_05ex', 2)
    setInvincible(0)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_06ex', 2)
    if SLOT_2:
        AirPushbackY(32000)
        RefreshMultihit()
    label(2)
    sprite('nt405_07', 2)
    TriggerUponForState('ntef_405Test', 32)
    sprite('nt405_08', 3)
    BufferedOrPressedGoto('AntiAir2nd')
    sprite('nt405_09', 2)
    sprite('nt405_10', 2)
    sprite('nt405_11', 2)
    sprite('nt405_12', 3)
    sprite('nt405_13', 2)
    DisallowGoto2('AntiAir2nd')
    sprite('nt405_14', 3)
    EnableAfterimage(0)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    EnableAfterimage(0)
    sprite('nt024_01', 8)
    sprite('nt024_02', 2)
    sprite('nt024_03', 2)
    sprite('nt024_04', 2)


@State
def AntiAirC_Air():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(44000)
        setInvincible(1)
        SpecificInvincibility(1, 0, 0, 0, 0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)
        AddY(80000)
        XImpulseAcceleration(0)
        YAccel(0)
        PerGravity(0)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            callSubroutine('Dash_AfterImage')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            BeginBuffer('AntiAir2nd')
    sprite('nt405_01', 1)
    Voiceline('nt205')
    sprite('nt405_02', 2)
    if SLOT_2:
        physicsXImpulse(20000)
    else:
        physicsXImpulse(10000)
    sprite('nt405_03', 2)
    CommonSE('004_swing_grap_1_2')
    XImpulseAcceleration(50)
    sprite('nt405_04', 2)
    XImpulseAcceleration(50)
    physicsYImpulse(26000)
    EndYPhysicsImpulse()
    CreateObject('ntef_405WeakAir', -1)
    sprite('nt405_05', 3)
    setInvincible(0)
    TriggerUponForState('ntef_405WeakAir', 32)
    sprite('nt405_06', 3)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_07', 3)
    TriggerUponForState('ntef_405WeakAir', 33)
    sprite('nt405_08', 3)
    sprite('nt405_09', 2)
    BufferedOrPressedGoto('AntiAir2nd')
    sprite('nt405_10', 2)
    sprite('nt405_11', 2)
    sprite('nt405_12', 3)
    sprite('nt405_13', 2)
    DisallowGoto2('AntiAir2nd')
    sprite('nt405_14', 3)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt024_01', 3)
    sprite('nt024_02', 2)
    sprite('nt024_03', 2)
    sprite('nt024_04', 2)


@State
def AntiAirD_Air():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(800)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(60)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(44000)
        StarterRating(0)
        setInvincible(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)
        AddY(80000)
        XImpulseAcceleration(0)
        YAccel(0)
        PerGravity(0)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            AirPushbackX(20000)
            AirPushbackY(48000)
            callSubroutine('Dash_AfterImage')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            BeginBuffer('AntiAir2nd')
    sprite('nt405_01', 2)
    Voiceline('nt207')
    sprite('nt405_02', 2)
    if SLOT_2:
        physicsXImpulse(30000)
    else:
        physicsXImpulse(20000)
    sprite('nt405_03', 2)
    PrivateSE('ntse_00')
    XImpulseAcceleration(50)
    sprite('nt405_04ex', 2)
    CreateObject('ntef_405AirTest', 0)
    XImpulseAcceleration(50)
    physicsYImpulse(40000)
    EndYPhysicsImpulse()
    sprite('nt405_05ex', 2)
    if SLOT_2:
        if SLOT_IsGrounded:
            Damage(400)
            if SLOT_137:
                DamageMultiplier(80)
        else:
            Damage(600)
            if SLOT_137:
                DamageMultiplier(80)
        Hitstop(3)
        XImpulseAcceleration(300)
        YAccel(80)
        RefreshMultihit()
    sprite('nt405_06ex', 2)
    RefreshMultihit()
    sprite('nt405_05ex', 2)
    setInvincible(0)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_06ex', 2)
    if SLOT_2:
        RefreshMultihit()
    sprite('nt405_07', 2)
    TriggerUponForState('ntef_405AirTest', 32)
    sprite('nt405_08', 3)
    BufferedOrPressedGoto('AntiAir2nd')
    sprite('nt405_09', 2)
    sprite('nt405_10', 2)
    sprite('nt405_11', 2)
    sprite('nt405_12', 3)
    sprite('nt405_13', 2)
    DisallowGoto2('AntiAir2nd')
    sprite('nt405_14', 3)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt024_01', 8)
    sprite('nt024_02', 2)
    sprite('nt024_03', 2)
    sprite('nt024_04', 2)


@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1000)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirUntechableTime(40)
        AirPushbackY(-40000)
        SetInertia(0)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            XSpeed(3000)
            SetAcceleration(-400)
            YSpeed(12000)
            setGravity(1800)
            AirPushbackX(15000)
        else:
            XSpeed(8000)
            SetAcceleration(-400)
            physicsYImpulse(22000)
            setGravity(1800)
    sprite('nt406_00', 2)
    sprite('nt406_01', 2)
    sprite('nt406_02', 2)
    sprite('nt406_03', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('nt406_04', 2)
    sprite('nt406_05', 3)
    if not PreviousStateCheck('AntiAirD'):
        if not PreviousStateCheck('AntiAirD_Air'):
            Voiceline('nt206')
    sprite('nt406_06', 3)
    sprite('nt406_07', 3)
    SetAcceleration(0)
    Recovery()
    sprite('nt406_08', 3)
    sprite('nt406_09', 3)
    sprite('nt406_10', 3)
    EnableAfterimage(0)
    label(0)
    sprite('nt020_07', 3)
    sprite('nt020_08', 3)
    loopRest()
    gotoLabel(0)


@State
def Dodge():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        setInvincible(1)
        SpecificInvincibility(1, 1, 0, 1, 0)
        SetZLine(0, 30)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:

            def upon_STATE_END():
                Flip()
                AlphaValue(255)
                ConstantAlphaModifier(0)
        BeginBuffer('ShortDash')

        def upon_EVERY_FRAME():
            if SLOT_41 <= 150000:
                if SLOT_IsFacingRight:
                    if SLOT_40 >= 0:
                        clearUponHandler(EVERY_FRAME)
                        XImpulseAcceleration(40)
                elif SLOT_40 <= 0:
                    clearUponHandler(EVERY_FRAME)
                    XImpulseAcceleration(40)
    if SLOT_2:
        conditionalSendToLabel(10)
    sprite('nt407_00', 4)
    Voiceline('nt208')
    EndMomentum(1)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    sprite('nt407_01', 4)
    BeginBuffer('DodgeThrow')
    sprite('nt407_02', 4)
    BufferedOrPressedGoto('ShortDash')
    BufferedOrPressedGoto('DodgeThrow')
    sprite('nt407_03', 18)
    EnableCollision(0)
    sprite('nt407_02', 3)
    setInvincible(0)
    SetZLine(1, 30)
    EnableCollision(1)
    EnableAfterimage(0)
    sprite('nt407_04', 3)
    sprite('nt407_05', 2)
    DisallowGoto2('ShortDash')
    DisallowGoto2('DodgeThrow')
    loopRest()
    gotoLabel(9)
    label(10)
    Voiceline('nt210')
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(5000)
    callSubroutine('Dash_AfterImage')
    sprite('nt408_00', 4)
    XImpulseAcceleration(200)
    PrivateSE('ntse_12')
    sprite('nt408_01', 4)
    BeginBuffer('DodgeThrow')
    sprite('nt408_02', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    sprite('nt408_02', 4)
    XImpulseAcceleration(600)
    sprite('nt408_03', 4)
    XImpulseAcceleration(50)
    BufferedOrPressedGoto('DodgeThrow')
    sprite('nt408_04', 3)
    XImpulseAcceleration(50)
    sprite('nt408_05', 3)
    XImpulseAcceleration(50)
    AlphaValue(160)
    ConstantAlphaModifier(20)
    sprite('nt408_06', 3)
    setInvincible(0)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    EndMomentum(1)
    SetZLine(1, 30)
    EnableAfterimage(0)
    sprite('nt408_07', 4)
    DisallowGoto2('DodgeThrow')
    sprite('nt408_08', 3)
    label(9)
    sprite('keep', 1)


@State
def DodgeThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('DodgeThrowExe', 2, 0, 0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(120000)
        ThrowTechWindow(-1)
        AttackP1(90)
        PreventAirborneHit(0)
        LockOpponentState(1)
        CrouchWhiff(1)
        setInvincible(1)
        SpecificInvincibility(1, 1, 0, 0, 0)
        if SLOT_59:
            ForceFaceSprite()
    if SLOT_59:
        conditionalSendToLabel(0)
    sprite('nt409_00', 2)
    sprite('nt409_01', 2)
    sprite('nt409_02', 3)
    physicsXImpulse(30000)
    DashEffects(100, 1, 1)
    sprite('nt409_03', 3)
    XImpulseAcceleration(20)
    loopRest()
    label(0)
    sprite('nt409_04', 2)
    PreDashEffects(100, 1, 1)
    XImpulseAcceleration(0)
    sprite('nt409_05', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('nt409_06', 5)
    CreateObject('ntef_409', -1)
    EnableAfterimage(0)
    sprite('nt409_17', 5)
    Voiceline('nt155')
    setInvincible(0)
    sprite('nt409_18', 5)
    sprite('nt409_19', 5)
    sprite('nt402_10', 8)
    sprite('nt402_11', 5)


@State
def DodgeThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(1426)
        AttackP2(82)
        MinimumDamage(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(9000)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        PassByArmor(1)
        StarterRating(2)
        CHStateIfCHStart(3)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 0)
        NoDamageAction(1)
    sprite('nt409_06', 1)
    if SLOT_59:
        Voiceline('nt211')
    else:
        Voiceline('nt209')
    CreateObject('ntef_409', -1)
    OppThrowAnimation(25, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    StartMultihit()
    sprite('nt409_07', 3)
    OppThrowAnimation(25, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    sprite('nt409_08', 3)
    sprite('nt409_09', 3)
    physicsXImpulse(12000)
    physicsYImpulse(24000)
    EndYPhysicsImpulse()
    JumpEffects(0, 0)
    sprite('nt409_10', 3)
    sprite('nt409_11', 3)
    CreateObject('ntef_410', -1)
    RefreshMultihit()
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackY(32000)
    IgnoreComboTime(0)
    EnemyHitstopAddition(0, 1, 1)
    XImpulseAcceleration(50)
    sprite('nt409_12', 3)
    sprite('nt409_13', 3)
    sprite('nt409_14', 3)
    sprite('nt409_15', 3)
    sprite('nt409_16', 32767)
    loopRest()
    label(0)
    sprite('nt033_03', 1)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(2000)
        MinimumDamage(40)
        AttackP2(75)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        CHAirPushbackX(55000)
        AirUntechableTime(80)
        Hitstop(20)
        AttackDirection(0)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        SLOT_59 = 0
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('UltimateAssault_En')
            Damage(2400)
            callSubroutine('Dash_AfterImage')
        if SLOT_137:
            DamageMultiplier(80)

        def upon_OPPONENT_HIT():
            SpecificInvincibility(1, 1, 1, 1, 1)
            EnableCollision(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            sendToLabel(1)
    sprite('nt430_00', 2)
    sprite('nt430_01', 2)
    sprite('nt430_02', 2)
    Voiceline('nt250')
    CreateObject('ntef_430atk', -1)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    EndMomentum(1)
    sprite('nt430_03', 3)
    sprite('nt430_04', 3)
    sprite('nt430_05', 3)
    CreateObject('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)
    sprite('nt430_04', 3)
    sprite('nt430_05', 3)
    sprite('nt430_06', 4)
    EnableAfterimage(1)
    TriggerUponForState('ntef_430atk', 32)
    sprite('nt430_07', 4)
    sprite('nt430_08', 4)
    sprite('nt430_09', 4)
    sprite('nt430_10', 4)
    sprite('nt430_11', 6)
    sprite('nt430_12', 3)
    sprite('nt430_13', 3)
    physicsXImpulse(5000)
    PreDashEffects(100, 1, 0)
    Voiceline('nt251')
    PrivateSE('ntse_06')
    PrivateSE('ntse_07')
    sprite('nt430_14_2', 2)
    SpecificInvincibility(0, 0, 0, 1, 0)
    XImpulseAcceleration(800)
    SetAcceleration(7000)
    if SLOT_2:
        XImpulseAcceleration(120)
        PerAcceleration(150)
        JumpEffects(3, 100)
    DashEffects(100, 1, 0)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    AttackOff()
    physicsXImpulse(50000)
    SetAcceleration(7000)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    label(2)
    sprite('nt430_16', 3)
    EnableCollision(1)
    setInvincible(0)
    XImpulseAcceleration(30)
    PerAcceleration(0)
    SkidEffects(100, 1, 0)
    TriggerUponForState('ntef_430atk', 33)
    sprite('nt430_17', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 0)
    sprite('nt430_18', 3)
    SkidEffects(100, 1, 0)
    sprite('nt430_19', 3)
    SkidEffects(100, 1, 0)
    CrouchState(1)
    sprite('nt430_20', 8)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('nt430_21', 3)
    EnableAfterimage(0)


@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1800)
        MinimumDamage(30)
        AttackP2(75)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        CHAirPushbackX(55000)
        AirUntechableTime(80)
        Hitstop(20)
        EnemyHitstopAddition(0, 0, 0)
        AttackDirection(0)
        PassByArmor(1)
        AttackType(4)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            GotoState('UltimateAssaultOD_En')
            Damage(2160)
            callSubroutine('Dash_AfterImage')
        if SLOT_137:
            DamageMultiplier(80)

        def upon_OPPONENT_HIT():
            SpecificInvincibility(1, 1, 1, 1, 1)
            EnableCollision(0)
            SLOT_51 = 1

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            sendToLabel(1)

        def upon_EVERY_FRAME():
            if SLOT_19 <= 170000:
                if SLOT_52:
                    sendToLabel(2)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('nt430_00', 2)
    sprite('nt430_01', 2)
    sprite('nt430_02', 2)
    Voiceline('nt250')
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('ntef_430atk', -1)
    sprite('nt430_03', 3)
    sprite('nt430_04', 3)
    sprite('nt430_05', 3)
    CreateObject('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)
    sprite('nt430_04', 3)
    sprite('nt430_05', 3)
    sprite('nt430_06', 4)
    EnableAfterimage(1)
    TriggerUponForState('ntef_430atk', 32)
    sprite('nt430_07', 4)
    sprite('nt430_08', 4)
    sprite('nt430_09', 4)
    sprite('nt430_10', 4)
    sprite('nt430_11', 6)
    sprite('nt430_12', 3)
    sprite('nt430_13', 3)
    physicsXImpulse(5000)
    PreDashEffects(100, 1, 0)
    Voiceline('nt251')
    PrivateSE('ntse_06')
    PrivateSE('ntse_07')
    sprite('nt430_14_2', 2)
    SpecificInvincibility(0, 0, 0, 1, 0)
    XImpulseAcceleration(800)
    SetAcceleration(7000)
    if SLOT_2:
        XImpulseAcceleration(120)
        PerAcceleration(150)
        JumpEffects(3, 100)
    DashEffects(100, 1, 0)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    AttackOff()
    physicsXImpulse(50000)
    SetAcceleration(7000)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    sprite('nt430_14', 1)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(90)
    sprite('nt430_14', 1)
    SLOT_52 = 1
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_15', 2)
    DashEffects(100, 1, 0)
    sprite('nt430_14', 2)
    DashEffects(100, 1, 0)
    label(2)
    sprite('nt430_16', 3)
    clearUponHandler(EVERY_FRAME)
    EnableCollision(1)
    if not SLOT_51:
        setInvincible(0)
    XImpulseAcceleration(30)
    PerAcceleration(0)
    SkidEffects(100, 1, 0)
    TriggerUponForState('ntef_430atk', 33)
    sprite('nt430_17', 3)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 0)
    if SLOT_51:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_18', 3)
    SkidEffects(100, 1, 0)
    sprite('nt430_19', 3)
    SkidEffects(100, 1, 0)
    CrouchState(1)
    sprite('nt430_20', 8)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('nt430_21', 3)
    EnableAfterimage(0)


@State
def UltimateAssaultOD_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1800)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP2(100)
        MinimumDamage(30)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackY(55000)
        YImpulseBeforeWallbounce(2500)
        AirUntechableTime(80)
        Hitstop(20)
        AttackDirection(0)
        AttackType(4)
        CHStateIfCHStart(3)
        setInvincible(1)
        uponSendToLabel(LANDING, 9)

        def upon_STATE_END():
            SLOT_59 = 0
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        else:
            EnableAfterimage(1)
            AfterimageBlendMode(1)
            AfterimageInterval(3)
            AfterimageCount(5)
        if SLOT_XDistanceFromFowardCorner <= 250000:
            XPositionRelativeFacing(1615000)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
        if PreviousStateCheck('UltimateAirAssaultOD'):
            SLOT_51 = 1
    sprite('nt430_17', 3)
    if SLOT_51:
        ForceFaceSprite()
        physicsXImpulse(30000)
    CreateObject('ntef_430_moya', -1)
    SkidEffects(100, 1, 0)
    sprite('nt430_31', 3)

    def RunOnObject_22():
        XImpulseAcceleration(20)
        YAccel(20)
        PerGravity(20)
    SkidEffects(100, 1, 0)
    DistortionSettings(35, -1, 0)
    E0EAEffect('aura', 65535)
    sprite('nt430_32', 25)
    EndMomentum(1)
    CrouchState(1)
    SetBackground(2)
    if SLOT_21:
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('nt430_33', 8)
    physicsXImpulse(5000)
    sprite('nt430_34', 4)
    Voiceline('nt254')
    XImpulseAcceleration(200)
    sprite('nt430_34', 4)
    sprite('nt430_35', 6)
    PrivateSE('ntse_07')
    XImpulseAcceleration(200)
    physicsYImpulse(16000)
    setGravity(1000)
    CrouchState(0)
    JumpEffects(3, 100)
    sprite('nt430_36', 3)
    RefreshMultihit()
    XImpulseAcceleration(50)
    CreateObject('ntef_430atkOD', -1)
    CommonSE('025_cleanhit_grap')
    TriggerUponForState('ntef_430_moya', 32)
    sprite('nt430_37', 4)
    XImpulseAcceleration(50)
    sprite('nt430_38', 4)
    XImpulseAcceleration(50)
    sprite('nt430_39', 4)
    XImpulseAcceleration(50)
    sprite('nt430_40', 4)
    label(0)
    sprite('nt020_07', 4)
    sprite('nt020_08', 4)
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt024_01', 12)
    sprite('nt024_02', 3)
    sprite('nt024_03', 3)
    sprite('nt024_04', 3)


@State
def UltimateAirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        Damage(1800)
        if SLOT_137:
            DamageMultiplier(80)
        MinimumDamage(40)
        AttackP2(75)
        Hitstop(20)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Floorslide(20)
        AttackDirection(0)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)

        def upon_OPPONENT_HIT():
            SpecificInvincibility(1, 1, 1, 1, 1)
            EnableCollision(0)
    sprite('nt430_22', 2)
    sprite('nt430_23', 2)
    sprite('nt430_24', 3)
    Voiceline('nt252')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)
    CreateObject('ntef_Air430atk', -1)
    sprite('nt430_23', 3)
    sprite('nt430_24', 3)
    sprite('nt430_22', 3)
    sprite('nt430_23', 3)
    sprite('nt430_24', 3)
    sprite('nt430_25', 3)
    EnableAfterimage(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    TriggerUponForState('ntef_Air430atk', 32)
    sprite('nt430_25', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_26', 8)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_27', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_27', 3)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('nt430_28', 3)
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    sprite('nt430_28', 3)
    Voiceline('nt253')
    PrivateSE('ntse_06')
    PrivateSE('ntse_07')
    XImpulseAcceleration(300)
    YAccel(300)
    sprite('nt430_29_2', 2)
    SpecificInvincibility(0, 0, 0, 1, 0)
    XImpulseAcceleration(300)
    YAccel(300)
    SetAcceleration(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)
    label(0)
    sprite('nt430_29', 2)
    sprite('nt430_30', 2)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)
    setInvincible(0)
    XImpulseAcceleration(60)
    YAccel(0)
    PerAcceleration(0)
    PerGravity(0)
    SkidEffects(100, 1, 0)
    TriggerUponForState('ntef_Air430atk', 33)
    sprite('nt430_17', 2)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 0)
    sprite('nt430_18', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_18', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_19', 2)
    SkidEffects(100, 1, 0)
    CrouchState(1)
    sprite('nt430_19', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_20', 10)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('nt430_21', 3)
    EnableAfterimage(0)


@State
def UltimateAirAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        Damage(1700)
        if SLOT_137:
            DamageMultiplier(80)
        MinimumDamage(30)
        AttackP2(75)
        Hitstop(20)
        EnemyHitstopAddition(0, -2, -2)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Floorslide(22)
        AttackDirection(0)
        PassByArmor(1)
        AttackType(4)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)

        def upon_OPPONENT_HIT():
            AttackOff()
            SpecificInvincibility(1, 1, 1, 1, 1)
            EnableCollision(0)
            SLOT_51 = 1
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('nt430_22', 2)
    sprite('nt430_23', 2)
    sprite('nt430_24', 3)
    Voiceline('nt252')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)
    CreateObject('ntef_Air430atk', -1)
    sprite('nt430_23', 3)
    sprite('nt430_24', 3)
    sprite('nt430_22', 3)
    sprite('nt430_23', 3)
    sprite('nt430_24', 3)
    sprite('nt430_25', 3)
    EnableAfterimage(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    TriggerUponForState('ntef_Air430atk', 32)
    sprite('nt430_25', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_26', 8)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_27', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('nt430_27', 3)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('nt430_28', 3)
    physicsXImpulse(6000)
    physicsYImpulse(-6000)
    sprite('nt430_28', 3)
    Voiceline('nt253')
    PrivateSE('ntse_06')
    PrivateSE('ntse_07')
    XImpulseAcceleration(300)
    YAccel(300)
    sprite('nt430_29_2', 2)
    SpecificInvincibility(0, 0, 0, 1, 0)
    XImpulseAcceleration(300)
    YAccel(300)
    SetAcceleration(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)
    label(0)
    sprite('nt430_29', 2)
    sprite('nt430_30', 2)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)
    EnableCollision(1)
    setInvincible(0)
    TriggerUponForState('ntef_Air430atk', 33)
    XImpulseAcceleration(60)
    YAccel(0)
    PerAcceleration(0)
    PerGravity(0)
    SkidEffects(100, 1, 0)
    if SLOT_51:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_17', 2)
    XImpulseAcceleration(60)
    SkidEffects(100, 1, 0)
    sprite('nt430_18', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_18', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_19', 2)
    SkidEffects(100, 1, 0)
    CrouchState(1)
    sprite('nt430_19', 2)
    SkidEffects(100, 1, 0)
    sprite('nt430_20', 10)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('nt430_21', 3)
    EnableAfterimage(0)


@State
def UltimateEdgeAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(1300)
        MinimumDamage(25)
        Hitstop(3)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        CHAirPushbackX(5500)
        AirPushbackY(58000)
        AirUntechableTime(300)
        AttackDirection(0)
        PassByArmor(1)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        SLOT_2 = SLOT_4
        if SLOT_2:
            callSubroutine('Dash_AfterImage')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            Hitstop(20)
            EnemyHitstopAddition(0, 0, 0)
            enterState('UltimateEdgeAssault_Exe')
            TriggerUponForState('ntef_431', 33)
            CameraControlEnable(1)
    sprite('nt431_00', 3)
    sprite('nt431_01', 3)
    Voiceline('nt255')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('ntef_430_bloodMatome', -1)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)

    def RunOnObject_1():
        Size(3000)
    sprite('nt431_02', 3)
    sprite('nt431_03', 3)
    sprite('nt431_01', 3)
    sprite('nt431_02', 3)
    sprite('nt431_03', 3)
    sprite('nt431_01', 3)
    sprite('nt431_02', 3)
    sprite('nt431_04', 5)
    sprite('nt431_05', 5)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    sprite('nt431_06', 5)
    if SLOT_2:
        physicsXImpulse(3000)
    sprite('nt431_07', 5)
    if SLOT_2:
        XImpulseAcceleration(200)
        PreDashEffects(100, 1, 1)
    sprite('nt431_08', 5)
    if SLOT_2:
        XImpulseAcceleration(400)
    CreateObject('ntef_431', -1)
    PrivateSE('ntse_07')
    PrivateSE('ntse_07')
    sprite('nt431_09', 1)
    XImpulseAcceleration(0)
    sprite('nt431_09', 5)
    clearUponHandler(OPPONENT_HIT)
    AttackOff()
    sprite('nt431_09', 9)
    PrivateSE('ntse_08')
    sprite('nt431_10', 7)
    setInvincible(0)
    EnableAfterimage(0)
    sprite('nt431_11', 9)
    sprite('nt431_12', 9)
    sprite('nt203_14', 9)


@State
def UltimateEdgeAssault_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(2719)
        AttackP2(75)
        MinimumDamage(25)
        GroundedHitstunAnimation(19)
        AirHitstunAnimation(19)
        AirPushbackX(160000)
        AirPushbackY(15000)
        AirUntechableTime(100)
        Floorslide(30)
        HardKnockdown(25)
        HitsparkSize(0)
        EnableRapidCancel(0)
        HitBackReturnIgnore(1)
        CHStateIfCHStart(3)
        PassByArmor(1)
        StarterRating(2)
        NoDamageAction(1)
        CameraControlEnable(1)
        EnableCollision(0)

        def upon_STATE_END():
            ExtendCollisionX(0)
    sprite('nt431_09', 5)
    StartMultihit()
    sprite('nt431_10', 6)
    sprite('nt431_11', 6)
    sprite('nt431_12', 6)
    loopRest()
    sprite('nt203_14', 3)
    SetBackground(2)

    def RunOnObject_22():
        TeleportToObject(22)
        AddX(-250000)
        AbsoluteY(2100000)
        physicsYImpulse(-50000)
        setGravity(0)
    sprite('nt340_01', 5)
    Voiceline('nt256')
    sprite('nt340_02', 5)
    sprite('nt340_03', 2)
    sprite('nt340_04', 2)
    sprite('nt340_05', 2)
    sprite('nt340_03', 2)
    sprite('nt340_04', 2)
    sprite('nt340_05', 2)
    sprite('nt340_03', 2)
    sprite('nt340_04', 2)
    sprite('nt340_05', 2)
    sprite('nt340_06', 5)
    sprite('nt340_07', 2)
    ExtendCollisionX(200)
    sprite('nt340_08', 2)
    physicsXImpulse(100000)
    KnockdownEffects(100, 1, 1)
    sprite('nt340_09', 6)
    EndMomentum(1)
    ScreenShake(20000, 4000)
    CreateObject('ntef_431AddAtk', -1)
    CommonSE('025_cleanhit_grap')
    CommonSE('025_cleanhit_grap')
    sprite('nt340_10', 3)
    ExtendCollisionX(0)
    EnableCollision(1)
    CameraControlEnable(0)
    sprite('nt340_11', 3)
    sprite('nt340_12', 3)
    sprite('nt340_13', 3)
    EnableRapidCancel(1)
    sprite('nt340_14', 3)
    sprite('nt340_15', 3)
    sprite('nt340_16', 3)
    sprite('nt340_17', 3)
    sprite('nt615_00', 5)
    sprite('nt615_01', 5)
    sprite('nt615_02', 5)
    sprite('nt615_03', 10)
    sprite('nt615_04', 3)
    Voiceline('nt257')
    sprite('nt615_05', 10)
    sprite('nt615_05', 10)
    SetBackground(0)
    sprite('nt615_04', 3)
    sprite('nt615_03', 3)
    sprite('nt615_02', 3)
    sprite('nt615_01', 3)
    sprite('nt615_00', 3)


@State
def UltimateEdgeAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(1300)
        Hitstop(3)
        MinimumDamage(25)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        CHAirPushbackX(5500)
        AirPushbackY(58000)
        AirUntechableTime(300)
        AttackType(4)
        AttackDirection(0)
        PassByArmor(1)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        setInvincible(1)
        EndMomentum(1)
        SLOT_2 = SLOT_4
        if SLOT_2:
            callSubroutine('Dash_AfterImage')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            Hitstop(20)
            EnemyHitstopAddition(0, 0, 0)
            enterState('UltimateEdgeAssault_Exe_OD')
            TriggerUponForState('ntef_431_OD', 33)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('nt431_00', 3)
    sprite('nt431_01', 3)
    Voiceline('nt255')
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    CreateObject('ntef_430_bloodMatome', -1)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)

    def RunOnObject_1():
        Size(3000)
    sprite('nt431_02', 3)
    sprite('nt431_03', 3)
    sprite('nt431_01', 3)
    sprite('nt431_02', 3)
    sprite('nt431_03', 3)
    sprite('nt431_01', 3)
    sprite('nt431_02', 3)
    sprite('nt431_04', 5)
    sprite('nt431_05', 5)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    sprite('nt431_06', 5)
    if SLOT_2:
        physicsXImpulse(3000)
    sprite('nt431_07', 5)
    if SLOT_2:
        XImpulseAcceleration(200)
        PreDashEffects(100, 1, 1)
    sprite('nt431_08', 5)
    if SLOT_2:
        XImpulseAcceleration(400)
    CreateObject('ntef_431_OD', -1)
    PrivateSE('ntse_07')
    PrivateSE('ntse_07')
    sprite('nt431_09', 1)
    XImpulseAcceleration(0)
    sprite('nt431_09', 5)
    clearUponHandler(OPPONENT_HIT)
    AttackOff()
    sprite('nt431_09', 9)
    PrivateSE('ntse_08')
    sprite('nt431_10', 7)
    setInvincible(0)
    EnableAfterimage(0)
    sprite('nt431_11', 9)
    sprite('nt431_12', 9)
    sprite('nt203_14', 9)


@State
def UltimateEdgeAssault_Exe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1900)
        MinimumDamage(25)
        Hitstop(45)
        GroundedHitstunAnimation(1)
        AirPushbackX(2000)
        AirPushbackY(54000)
        AirUntechableTime(100)
        UseSlashHitspark(1)
        AttackType(4)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        NoDamageAction(1)
        EnableCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        WallCollisionDetection(0)
        ScreenCollision(0)
        EnableRapidCancel(0)

        def upon_32():
            EnableRapidCancel(1)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
            ExtendCollisionX(0)
    sprite('nt431_09', 5)
    StartMultihit()
    sprite('nt431_10', 6)
    sprite('nt431_11', 6)
    sprite('nt431_12', 6)
    ExtendCollisionX(250)
    sprite('nt431_13', 4)

    def RunOnObject_22():
        TeleportToObject(22)
        AddX(-300000)
        AbsoluteY(1750000)
        physicsYImpulse(-50000)
        setGravity(0)
    SetBackground(2)
    sprite('nt431_14', 4)
    sprite('nt431_15', 4)
    CreateObject('ntef_431OD', -1)
    sprite('nt431_16', 4)
    sprite('nt431_17', 4)
    PrivateSE('ntse_04')
    sprite('nt431_18', 4)
    sprite('nt431_19', 4)
    sprite('nt431_20', 2)
    Voiceline('nt258')
    sprite('nt431_21', 2)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    WallCollisionDetection(1)
    ScreenCollision(1)
    StayAfterMovement(1, 0)
    sprite('nt431_22', 2)
    RefreshMultihit()
    Hitstop(45)
    CommonSE('025_cleanhit_slash')
    sprite('nt431_23', 5)
    CreateObject('ntef_431OdLastSubMato', -1)
    ExtendCollisionX(0)
    CommonSE('025_cleanhit_slash')
    sprite('nt431_24', 5)
    sprite('nt431_25', 5)
    sprite('nt431_26', 5)
    sprite('nt431_27', 5)
    sprite('nt431_28', 35)
    sprite('nt431_28', 10)
    SetBackground(0)
    sprite('nt431_29', 6)
    sprite('nt431_30', 6)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        Blockstun(26)
        Hitstop(20)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 150000, 0)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(20000)
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)
            if SLOT_XDistanceFromFowardCorner <= 200000:
                SLOT_XDistanceFromCenterOfStage = 1665000

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('nt440_00', 5)
    Voiceline('nt280')
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('nt312_01ex01', 6)
    sprite('nt440_01', 5)
    sprite('nt200_09', 3)
    CommonSE('004_swing_grap_1_2')
    physicsXImpulse(45000)
    SetAcceleration(-5000)
    DashEffects(100, 1, 1)
    sprite('nt440_02', 3)
    EndMomentum(1)
    sprite('nt440_02', 6)
    AttackOff()
    setInvincible(0)
    sprite('nt440_03', 9)
    sprite('nt200_12ex01', 7)
    sprite('nt200_13ex01', 7)
    sprite('nt200_14ex01', 5)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        Blockstun(26)
        Hitstop(20)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 150000, 0)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(20000)
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)
            if SLOT_XDistanceFromFowardCorner <= 200000:
                SLOT_XDistanceFromCenterOfStage = 1665000

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('nt440_00', 2)
    Voiceline('nt280')
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('nt312_01ex01', 2)
    sprite('nt440_01', 2)
    sprite('nt200_09', 3)
    CommonSE('004_swing_grap_1_2')
    physicsXImpulse(45000)
    SetAcceleration(-5000)
    DashEffects(100, 1, 1)
    sprite('nt440_02', 3)
    EndMomentum(1)
    sprite('nt440_02', 6)
    AttackOff()
    setInvincible(0)
    sprite('nt440_03', 9)
    sprite('nt200_12ex01', 7)
    sprite('nt200_13ex01', 7)
    sprite('nt200_14ex01', 5)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(500)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(28000)
        AirUntechableTime(100)
        HardKnockdown(20)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        StayAfterMovement(1, 0)
        SetBackground(1)
        SLOT_65 = 1

        def upon_STATE_END():
            SLOT_65 = 0
            ExtendCollisionX(0)
            DespawnEAEffect('BurstDD_Camera')
    sprite('nt440_02', 5)
    StartMultihit()
    CreateObject('BurstDD_Camera', -1)
    sprite('nt440_03', 3)
    sprite('nt200_12ex01', 3)
    sprite('nt440_04', 3)
    physicsXImpulse(4000)
    sprite('nt440_05', 3)
    XImpulseAcceleration(200)
    sprite('nt440_06', 3)
    sprite('nt440_07', 3)
    Voiceline('nt281')
    XImpulseAcceleration(200)
    JumpEffects(3, 100)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('nt440_08', 1)
    ExtendCollisionX(10)
    sprite('nt440_08', 1)
    ExtendCollisionX(20)
    sprite('nt440_09', 1)
    ExtendCollisionX(30)
    sprite('nt440_09', 1)
    ExtendCollisionX(40)
    sprite('nt440_09', 1)
    ExtendCollisionX(50)
    sprite('nt440_10', 1)
    ExtendCollisionX(60)
    sprite('nt440_10', 1)
    ExtendCollisionX(70)
    sprite('nt440_10', 1)
    ExtendCollisionX(80)
    sprite('nt440_11', 1)
    ExtendCollisionX(90)
    sprite('nt440_11', 1)
    ExtendCollisionX(100)
    sprite('nt440_11', 1)
    sprite('nt440_12', 3)
    CreateParticle('ntef_611_end', 0)
    CreateParticle('ntef_611_end', 1)
    PrivateSE('ntse_09')
    sprite('nt440_13', 3)
    sprite('nt440_14', 3)
    YAccel(150)
    PrivateSE('ntse_04')
    sprite('nt440_15', 3)
    YAccel(150)
    sprite('nt440_16', 3)
    YAccel(150)
    if SLOT_51:
        uponSendToLabel(LANDING, 100)
    else:
        uponSendToLabel(LANDING, 1)
    sprite('nt440_16', 30)
    XImpulseAcceleration(150)
    YAccel(200)
    label(1)
    sprite('nt440_17', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    Damage(1400)
    Hitstop(8)
    EnemyHitstopAddition(-5, -5, -5)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    OppPositionOnHit(1, 350000, 0)
    UseSlashHitspark(1)
    RefreshMultihit()
    sprite('nt440_18', 3)
    CreateObject('ntef_440Axe', -1)
    LandingEffects(100, 1, 1)
    ExtendCollisionX(0)
    Damage(550)
    Hitstop(9)
    EnemyHitstopAddition(-1, -1, -1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    OppPositionOnHit(0, 0, 0)
    DefeatOpponentBehavior(0)
    HardKnockdown(10)
    HitBackReturnIgnore(1)
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('nt440_17', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    Damage(1700)
    Hitstop(13)
    EnemyHitstopAddition(-10, -10, -10)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    OppPositionOnHit(1, 300000, 0)
    UseSlashHitspark(1)
    RefreshMultihit()
    sprite('nt440_18', 3)
    CreateObject('ntef_440Axe', -1)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    Damage(610)
    Hitstop(1)
    EnemyHitstopAddition(4, 4, 4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(70000)
    AirPushbackY(30000)
    OppPositionOnHit(0, 0, 0)
    ReduceHitEffects(1)
    HitsparkSize(700)
    HitBackReturnIgnore(1)
    RefreshMultihit()
    CreateObject('ntef_440LastEx', -1)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    RefreshMultihit()
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    RefreshMultihit()
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    RefreshMultihit()
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    ExtendCollisionX(0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    Hitstop(0)
    EnemyHitstopAddition(20, 20, 20)
    HardKnockdown(10)
    HitsparkSize(1000)
    DefeatOpponentBehavior(0)
    RefreshMultihit()
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    label(9)
    sprite('nt440_19', 3)
    AttackOff()
    ExtendCollisionX(0)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    sprite('nt440_20', 3)
    sprite('nt440_19', 3)
    DespawnEAEffect('BurstDD_Camera')
    sprite('nt440_20', 3)
    sprite('nt440_21', 4)
    sprite('nt440_22', 4)
    sprite('nt440_23', 4)
    sprite('nt440_24', 4)
    sprite('nt403_09ex01', 4)
    sprite('nt403_10ex01', 4)
    sprite('nt403_11ex01', 4)
    sprite('nt601_06ex01', 5)
    sprite('nt601_07ex01', 5)
    sprite('nt601_08ex01', 8)
    CommonSE('019_cloth_a')
    sprite('nt601_09ex01', 5)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DamageFromStateOnly('AstralHeat')
        AttackLevel_(5)
        DefeatOpponentBehavior(1)
        Damage(0)
        Hitstun(20)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(220)
        Crumple(200)
        Hitstun(200)
        HitsparkSize(1500)
        PassByArmor(1)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        MinimumDamage(100)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            Hitstop(0)
            EnableAfterimage(0)
            sendToLabel(0)
            AstralHeatCleanup(1, 1)
            PlayPlayAstralBGM(1)
            HitAnywhere(1)
            WallCollisionDetection(0)
            ScreenCollision(0)
            ForceFaceSprite()
            EndMomentum(1)
            PushbackX(19800)
            CameraControlEnable(1)
            CameraNoScreenCollision(1)
            CameraControlInfinity(1)
            HUDVisibillity(1)
            StayAfterMovement(1, 0)

            def RunOnObject_22():
                WallCollisionDetection(0)
                ScreenCollision(0)
        setInvincible(1)
        SLOT_65 = 1
        SLOT_66 = 1

        def upon_STATE_END():
            SLOT_65 = 0
        SLOT_59 = 0
        SLOT_59 = SLOT_4
        SLOT_2 = SLOT_4
        if SLOT_2:
            callSubroutine('Dash_AfterImage')
    sprite('nt451_00', 3)
    sprite('nt451_01', 3)
    Voiceline('nt290')
    DistortionSettings(54, -1, 1)
    EmptyHeat()
    CreateObject('EMB_NT_AH', -1)
    CreateObject('ntef_D_handaura', 0)
    CreateObject('ntef_D_handaura_3D', 0)
    CreateObject('ntef_451aura', -1)
    CreateObject('ntef_430_aura00', -1)

    def RunOnObject_1():
        AddY(200000)
        AddScale(-600)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    CreateObject('ntef_451aura', -1)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    CreateObject('ntef_451aura', -1)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    CreateObject('ntef_451aura', -1)
    CreateObject('ntef_430_aura00', -1)

    def RunOnObject_1():
        AddY(200000)
        AddScale(-600)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    ParticleLayer(11)
    CreateObject('ntef_451aura', -1)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    CreateObject('ntef_451aura', -1)
    CreateObject('ntef_430_aura00', -1)

    def RunOnObject_1():
        AddY(200000)
        AddScale(-600)
    sprite('nt451_02', 3)
    sprite('nt451_03', 3)
    sprite('nt451_01', 3)
    sprite('nt451_04', 4)
    TriggerUponForState('ntef_D_handaura_3D', 32)
    TriggerUponForState('ntef_D_handaura', 32)
    sprite('nt451_05', 4)
    PrivateSE('ntse_04')
    sprite('nt451_06', 6)
    sprite('nt451_07', 15)
    CreateObject('ntef_451', -1)
    setInvincible(0)
    sprite('nt451_50', 4)
    sprite('nt203_12', 3)
    sprite('nt203_13', 3)
    sprite('nt203_14', 3)
    loopRest()
    ExitState()
    label(0)
    sprite('nt451_07', 4)
    CreateObject('ntef_451_hit', -1)
    clearUponHandler(STATE_END)
    CreateObject('ntef_451_BG', -1)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(300)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(350)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(400)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(450)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(500)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(550)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(600)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(650)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(700)
    sprite('nt451_07', 2)
    SetXCollisionFromOrigin(750)
    sprite('nt451_07', 5)
    SetXCollisionFromOrigin(800)
    sprite('nt451_08', 6)
    SetXCollisionFromOrigin(-1)
    sprite('nt451_09', 4)
    CameraPosition(800)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    Voiceline('nt291')
    CreateObject('ntef_451_2', -1)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    if SLOT_43:
        conditionalSendToLabel(1)
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    sprite('nt451_10', 3)
    sprite('nt451_11', 3)
    sprite('nt451_12', 3)
    PrivateSE('ntse_01')
    label(1)
    sprite('nt451_13', 4)
    CameraPosition(1000)
    TriggerUponForState('ntef_451_2', 34)
    sprite('nt451_14', 5)
    sprite('nt451_15', 6)
    PrivateSE('ntse_04')
    sprite('nt451_16', 5)
    sprite('nt451_17', 5)
    RefreshMultihit()
    Damage(2100)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    Hitstun(300)
    Hitstop(1)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(10000, 10000)
    sprite('nt451_18', 8)
    sprite('nt451_19', 4)
    PrivateSE('ntse_04')
    sprite('nt451_20', 6)
    sprite('nt451_21', 3)
    CreateObject('ntef_451slash2', 0)
    RefreshMultihit()
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_22', 6)
    sprite('nt451_23', 6)
    sprite('nt451_24', 4)
    PrivateSE('ntse_04')
    sprite('nt451_25', 4)
    sprite('nt451_26', 3)
    CreateObject('ntef_451slash', 0)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(10000)
    ScreenShake(0, 5000)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_27', 7)
    sprite('nt451_51', 4)
    sprite('nt451_52', 4)
    sprite('nt451_16', 5)
    Voiceline('nt292')
    PrivateSE('ntse_04')
    sprite('nt451_17', 5)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(5000)
    Hitstun(300)
    Hitstop(1)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_18', 8)
    sprite('nt451_19', 4)
    PrivateSE('ntse_04')
    sprite('nt451_20', 6)
    sprite('nt451_21', 3)
    CreateObject('ntef_451slash2', 0)
    RefreshMultihit()
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_22', 6)
    sprite('nt451_23', 6)
    sprite('nt451_24', 4)
    PrivateSE('ntse_04')
    sprite('nt451_25', 4)
    sprite('nt451_26', 3)
    CreateObject('ntef_451slash', 0)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    ScreenShake(0, 5000)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_27', 7)
    sprite('nt451_28', 4)
    sprite('nt451_29', 5)
    PrivateSE('ntse_04')
    sprite('nt451_30', 4)
    sprite('nt451_31', 5)
    RefreshMultihit()
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    PushbackX(0)
    OppPositionOnHit(1, 400000, 0)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddX(350000)
    CommonSE('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_32', 3)
    sprite('nt451_33', 3)
    sprite('nt451_34', 4)
    sprite('nt451_35', 4)
    sprite('nt451_36', 3)
    TriggerUponForState('ntef_451_2', 32)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    if SLOT_43:
        conditionalSendToLabel(2)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    sprite('nt451_36', 3)
    sprite('nt451_37', 3)
    sprite('nt451_38', 3)
    PrivateSE('ntse_04')
    label(2)
    sprite('nt451_39', 3)
    Voiceline('nt293')
    TriggerUponForState('ntef_451slash_kyushu', 32)
    CreateObject('ntef_451_BG', -1)
    sprite('nt451_40', 10)
    TriggerUponForState('ntef_451_2', 33)
    RefreshMultihit()
    Damage(5300)
    PushbackX(0)
    Hitstop(20)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    OppPositionOnHit(0, 0, 0)
    CommonSE('025_cleanhit_slash')
    sprite('nt451_40', 10)
    CreateParticle('tef_451_end', -1)
    sprite('nt451_40', 1)
    RefreshMultihit()
    Damage(10000)
    DefeatOpponentBehavior(3)
    AirPushbackY(30000)
    AirPushbackX(100000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Hitstop(0)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():

        def RunOnObject_22():
            AlphaValue(0)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    CreateObject('ntef_451SubMato', -1)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_41', 3)
    sprite('nt451_42', 3)
    sprite('nt451_43', 3)
    sprite('nt451_44', 5)
    sprite('nt451_45', 5)
    sprite('nt451_46', 5)
    sprite('nt451_47', 65)
    XPositionRelativeFacing(260000)
    SLOT_64 = 1
    DespawnEAEffect('ntef_451_BG')
    sprite('nt451_48', 8)
    sprite('nt451_49', 8)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('nt054')
    sprite('nt900_00', 32767)
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
        AbsoluteY(230000)
    sprite('nt901_00', 50)
    physicsYImpulse(-150)
    sprite('nt901_00', 50)
    physicsYImpulse(150)
    Voiceline('nt055')
    label(0)
    sprite('nt901_00', 50)
    physicsYImpulse(-150)
    sprite('nt901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('nt055', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
        14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('nt000', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt400', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt401', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt404', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt405', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        12643, 24880, 25400, 24888, 25400, 24888, 56, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt406', 12897, 25397, 13623, 14433, 14435, 14433, 14435, 
        14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt407', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14691, 24885, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt408', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14691, 24885, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
        24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('nt411', 13921, 14435, 12897, 25397, 13619, 14433, 14435, 
        14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt412', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt414', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt415', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt416', 12897, 25394, 12593, 14433, 14435, 14433, 14435, 
        14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt417', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('nt418', 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('nt000', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt400', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt401', 12641, 25396, 24888, 25398, 24888, 25400, 
            12343, 14433, 14435, 14433, 14435, 14433, 12643, 24880, 12849, 
            14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt404', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('nt405', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('nt406', 12897, 25397, 12342, 14433, 14435, 14433, 
            14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt407', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 24885, 25400, 24888, 25400, 24888, 25400, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('nt408', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14691, 24883, 25400, 24888, 25400, 24888, 25400, 24888, 
            25400, 24888, 12337, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt411', 12641, 25392, 24888, 25398, 24888, 25400, 
            24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('nt412', 14433, 14435, 14433, 14691, 24880, 25400, 
            24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('nt414', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt415', 12641, 25392, 24886, 25400, 24888, 25400, 
            24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('nt416', 14433, 14435, 14433, 14435, 14433, 14435, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt417', 14433, 14435, 14433, 14435, 14433, 14435, 
            12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('nt418', 14433, 14435, 14433, 13923, 14433, 13923, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            Unknown18011('nt000', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('nt400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 13923, 12641, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('nt401', 14177, 14179, 14433, 13667, 24880, 25400,
                24885, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('nt000', 12641, 25392, 24886, 25400, 24888, 25400,
                24888, 25400, 24888, 25398, 24886, 25398, 24886, 25398, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt400', 12641, 25396, 24886, 25400, 12342, 14433,
                14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
                14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 13923, 24880, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('ny'):
            Unknown18011('nt000', 14433, 14435, 14433, 13667, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('nt400', 14433, 14435, 14433, 14179, 24885, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('nt401', 13921, 13923, 13921, 13923, 24880, 25400,
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('nt000', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('nt000', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('nt400', 14433, 14435, 14433, 13667, 24885, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt401', 13921, 12643, 24880, 25400, 24886, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rm'):
            Unknown18011('nt000', 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt400', 14177, 14179, 14177, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('nt401', 14177, 14179, 14177, 14179, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            Unknown18011('nt500', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 24880, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('nt501', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 13923, 24880, 25400, 
                24888, 25400, 24888, 25400, 12339, 14433, 14435, 14433, 
                14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('nt502', 14433, 14435, 14433, 14691, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt503', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14691, 24880, 25400, 
                24888, 25400, 24888, 25400, 12338, 14433, 14435, 14433, 
                14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('nt506', 13921, 13923, 13921, 13923, 13921, 14179,
                24880, 25398, 24886, 25398, 12339, 13921, 13923, 13921, 
                13923, 13921, 14435, 24880, 25398, 12337, 13921, 13411, 
                13921, 13411, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt507', 14433, 12643, 24880, 25400, 24888, 25400,
                24888, 25400, 24888, 25400, 12342, 14433, 13667, 24880, 
                25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 
                25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('nt506', 13921, 13923, 13921, 13923, 13921, 
                    13411, 24884, 25398, 24886, 25398, 24886, 25398, 24884,
                    25398, 24884, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('nt507', 14433, 12643, 24880, 25400, 24888, 
                    25400, 12340, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('ny'):
            Unknown18011('nt522', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14435, 24880, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt523', 14433, 14435, 14433, 14179, 24885, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('nt522', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14179,
                    24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399,
                    24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('nt532', 14433, 14435, 14433, 14435, 14177, 14435,
                14177, 12899, 24885, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('nt533', 14433, 13411, 24880, 25400, 24888, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('nt536', 14433, 14435, 14433, 14435, 14433, 13667,
                24880, 25400, 12340, 14433, 14435, 14433, 14435, 14433, 
                14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt537', 14433, 14435, 13921, 13923, 13921, 13923,
                13921, 14435, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rm'):
            Unknown18011('nt554', 14433, 14435, 14433, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('nt555', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 13923, 24880, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('nt562', 14433, 14435, 14433, 13411, 24888, 25398,
                24886, 25400, 24888, 25400, 24888, 25400, 14388, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('nt563', 14689, 14179, 14177, 14179, 12641, 25392,
                12341, 12641, 25392, 12849, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 14433, 14435, 14177, 14179, 
                14177, 14179, 12641, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(100)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('rc'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2130)
        else:
            gotoLabel(130)
    if CharacterIDCheck('ny'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2210)
        else:
            gotoLabel(210)
    if CharacterIDCheck('vh'):
        SyncEntry()
        gotoLabel(260)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('rm'):
        SyncEntry()
        gotoLabel(370)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(410)
    label(482)
    if random_(2, 0, 25):
        conditionalSendToLabel(20)
    if random_(2, 0, 33):
        conditionalSendToLabel(30)
    if random_(2, 0, 50):
        conditionalSendToLabel(40)
    label(10)
    if random_(2, 0, 33):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    gotoLabel(2)
    label(20)
    gotoLabel(4)
    label(30)
    if CharacterIDCheck('nt'):
        SyncEntry()
        gotoLabel(10)
    else:
        gotoLabel(6)
    label(40)
    gotoLabel(5)
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('nt600_00', 6)
    sprite('nt600_01', 7)
    sprite('nt600_02', 7)
    sprite('nt600_03', 7)
    sprite('nt600_04', 7)
    sprite('nt600_03', 7)
    sprite('nt600_02', 7)
    sprite('nt600_01', 7)
    sprite('nt600_02', 7)
    sprite('nt600_03', 7)
    sprite('nt600_04', 14)
    sprite('nt600_03', 7)
    sprite('nt600_02', 7)
    sprite('nt600_01', 7)
    sprite('nt600_05', 7)
    sprite('nt600_06', 7)
    sprite('nt600_07', 7)
    sprite('nt600_06', 7)
    sprite('nt600_05', 7)
    sprite('nt600_06', 7)
    sprite('nt600_07', 14)
    sprite('nt600_06', 7)
    sprite('nt600_05', 7)
    sprite('nt600_01', 6)
    sprite('nt600_00', 8)
    sprite('nt600_08', 8)
    sprite('nt600_09', 8)
    sprite('nt600_10', 8)
    Voiceline('nt418')
    sprite('nt600_11', 8)
    sprite('nt600_12', 8)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(1)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('nt600_00', 6)
    sprite('nt600_01', 6)
    sprite('nt600_13', 6)
    sprite('nt600_14', 6)
    sprite('nt600_15', 20)
    sprite('nt600_01', 6)
    sprite('nt600_16', 6)
    sprite('nt600_17', 6)
    sprite('nt600_18', 20)
    sprite('nt600_01', 6)
    sprite('nt600_00', 8)
    sprite('nt600_08', 8)
    sprite('nt600_09', 8)
    sprite('nt600_10', 8)
    Voiceline('nt418')
    sprite('nt600_11', 8)
    sprite('nt600_12', 8)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2)
    sprite('nt300_00', 7)
    sprite('nt300_01', 7)
    sprite('nt300_02', 7)
    sprite('nt300_03', 7)
    sprite('nt300_04', 8)
    sprite('nt300_03', 7)
    sprite('nt300_02', 7)
    sprite('nt300_03', 7)
    sprite('nt300_04', 8)
    sprite('nt300_03', 7)
    sprite('nt300_02', 7)
    sprite('nt300_05', 7)
    sprite('nt300_06', 7)
    sprite('nt300_07', 6)
    sprite('nt300_08', 6)
    sprite('nt300_09', 7)
    sprite('nt300_08', 6)
    sprite('nt300_07', 6)
    sprite('nt300_08', 6)
    sprite('nt300_09', 7)
    sprite('nt300_08', 6)
    sprite('nt300_07', 6)
    sprite('nt300_10', 7)
    Voiceline('nt418')
    sprite('nt300_11', 6)
    sprite('nt300_12', 6)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(3)
    sprite('nt601_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(3)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 80)
    Voiceline('nt414')
    sprite('nt601_05', 70)
    Voiceline('nt415')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(4)
    sprite('nt601_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(4)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 110)
    Voiceline('nt416')
    sprite('nt601_05', 50)
    Voiceline('nt417')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(5)
    sprite('nt601_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(5)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 110)
    SpriteIfNot0(130, 2, 44)
    Voiceline('nt412')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(6)
    sprite('nt601_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(6)
    sprite('nt601_00', 8)
    if CharacterIDCheck('nt'):
        conditionalSendToLabel(6)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 120)
    CreateObject('ntef_601', -1)
    sprite('nt601_05', 120)
    Voiceline('nt414')
    sprite('nt601_05', 70)
    Voiceline('nt415')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    DemoTimer(45)
    loopRest()
    ExitState()
    label(100)
    sprite('nt602_00', 3)
    XPositionRelativeFacing(-48000)
    SetZVal(-1000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(100)
    sprite('nt602_00', 300)
    Voiceline('nt500')
    sprite('nt602_00', 240)
    sprite('nt033_00', 3)
    sprite('nt033_00', 3)
    sprite('nt033_01', 3)
    physicsXImpulse(-14000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    uponSendToLabel(LANDING, 102)
    label(101)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('nt033_03', 2)
    EndMomentum(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)
    XPositionRelativeFacing(-260000)
    SetZVal(0)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(110)
    uponSendToLabel(32, 112)
    label(111)
    sprite('nt601_00', 8)
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 110)
    Voiceline('nt502')
    DemoTimer(250)
    sprite('nt601_05', 50)
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    loopRest()
    ExitState()
    label(130)
    sprite('nt603_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(130)
    sprite('nt603_00', 20)
    sprite('nt603_00', 6)
    sprite('nt603_01', 6)
    sprite('nt603_02', 6)
    sprite('nt603_03', 6)
    sprite('nt603_04ex01', 80)
    Voiceline('nt506')
    sprite('nt603_05', 6)
    sprite('nt603_06', 12)
    sprite('nt603_05', 6)
    sprite('nt603_04', 6)
    sprite('nt603_07', 6)
    sprite('nt603_08', 12)
    sprite('nt603_07', 6)
    sprite('nt603_04ex01', 150)
    sprite('nt603_09', 6)
    sprite('nt603_10', 6)
    physicsXImpulse(5700)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 310000:
            clearUponHandler(EVERY_FRAME)
            ObjectUpon(22, 32)
            XPositionRelativeFacing(-50000)
            EndMomentum(1)
            sendToLabel(132)
    label(131)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('nt033_00', 3)
    sprite('nt033_01', 3)
    SmartVoiceline('nt015')
    physicsXImpulse(-14000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    uponSendToLabel(LANDING, 134)
    label(133)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(133)
    label(134)
    sprite('nt033_03', 2)
    EndMomentum(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)
    XPositionRelativeFacing(-260000)
    SetZVal(0)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(2130)
    sprite('nt603_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2130)
    sprite('nt603_00', 20)
    sprite('nt603_00', 6)
    sprite('nt603_01', 6)
    sprite('nt603_02', 6)
    sprite('nt603_03', 6)
    sprite('nt603_04ex01', 200)
    Voiceline('nt506')
    sprite('nt603_09', 6)
    sprite('nt603_10', 6)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 310000:
            clearUponHandler(EVERY_FRAME)
            ObjectUpon(22, 32)
            XPositionRelativeFacing(-50000)
            EndMomentum(1)
            sendToLabel(2132)
    sprite('nt030_01', 1)
    physicsXImpulse(5700)
    label(2131)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(2131)
    label(2132)
    sprite('nt033_00', 3)
    sprite('nt033_01', 3)
    SmartVoiceline('nt015')
    physicsXImpulse(-14000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    uponSendToLabel(LANDING, 2134)
    label(2133)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(2133)
    label(2134)
    sprite('nt033_03', 2)
    EndMomentum(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)
    XPositionRelativeFacing(-260000)
    SetZVal(0)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(210)
    sprite('nt601_00', 20)

    def upon_32():
        SetActionMark(1)
    sprite('nt601_01', 8)
    sprite('nt601_02', 20)
    sprite('nt601_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(210)
    sprite('nt601_00', 20)
    sprite('nt601_01', 8)
    sprite('nt601_02', 20)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 150)
    sprite('nt601_05', 100)
    Voiceline('nt522')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    DemoTimer(20)
    loopRest()
    ExitState()
    label(2210)
    sprite('nt601_00', 20)

    def upon_32():
        SetActionMark(1)
    sprite('nt601_01', 8)
    sprite('nt601_02', 20)
    sprite('nt601_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2210)
    sprite('nt601_00', 20)
    sprite('nt601_01', 8)
    sprite('nt601_02', 20)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 220)
    sprite('nt601_05', 200)
    Voiceline('nt522')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(260)
    sprite('nt601_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(260)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 80)
    Voiceline('nt532')
    sprite('nt601_05', 70)
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    uponSendToLabel(32, 282)
    label(281)
    sprite('nt601_00', 8)
    loopRest()
    gotoLabel(281)
    label(282)
    sprite('nt601_01', 8)
    clearUponHandler(32)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 140)
    Voiceline('nt536')
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    loopRest()
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    ObjectUpon(22, 32)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    ExitState()
    label(370)
    uponSendToLabel(32, 372)
    label(371)
    sprite('nt601_00', 8)
    loopRest()
    gotoLabel(371)
    label(372)
    sprite('nt601_01', 8)
    sprite('nt601_02', 8)
    sprite('nt601_01', 8)
    sprite('nt601_00', 8)
    sprite('nt601_01', 8)
    sprite('nt601_02', 14)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 110)
    Voiceline('nt554')
    DemoTimer(250)
    sprite('nt601_05', 50)
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    ObjectUpon(22, 32)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    loopRest()
    ExitState()
    label(410)
    sprite('nt603_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(410)
    sprite('nt603_00', 20)
    sprite('nt603_00', 6)
    sprite('nt603_01', 6)
    sprite('nt603_02', 6)
    sprite('nt603_03', 6)
    sprite('nt603_04ex01', 60)
    Voiceline('nt562')
    sprite('nt603_05', 5)
    sprite('nt603_06', 5)
    sprite('nt603_05', 5)
    sprite('nt603_04', 5)
    sprite('nt603_07', 5)
    sprite('nt603_08', 5)
    sprite('nt603_07', 5)
    sprite('nt603_04ex01', 120)
    sprite('nt603_09', 6)
    sprite('nt603_10', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    SmartRandomVoiceline('nt400', 100, 'nt401', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    loopRest()


@State
def CmnActMatchWin():
    if SLOT_64:
        conditionalSendToLabel(2)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('rc'):
        if SLOT_140:
            gotoLabel(2130)
        else:
            gotoLabel(130)
    if CharacterIDCheck('ny'):
        conditionalSendToLabel(210)
    if CharacterIDCheck('vh'):
        conditionalSendToLabel(260)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(280)
    if CharacterIDCheck('rm'):
        conditionalSendToLabel(370)
    if CharacterIDCheck('mi'):
        if SLOT_138:
            gotoLabel(410)
        else:
            gotoLabel(1410)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(2)
    label(1)
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 55)
    Voiceline('nt406')
    CreateParticle('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)
    sprite('nt610_07', 8)
    sprite('nt610_08', 8)
    sprite('nt610_09', 32767)
    DemoEndOnVoiceEnd(1)
    label(2)
    sprite('nt611_00', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    SmartRandomVoiceline('nt407', 100, 'nt408', 100, '', 0, '', 0)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    sprite('nt611_01', 4)
    sprite('nt611_04', 4)
    CreateObject('ntef_611', -1)
    PrivateSE('ntse_11')
    sprite('nt611_05', 4)
    sprite('nt611_06', 4)
    sprite('nt611_07', 4)
    sprite('nt611_08', 4)
    sprite('nt611_09', 32767)
    DemoEndOnVoiceEnd(1)
    label(100)
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 180)
    Voiceline('nt501')
    DemoEndOnVoiceEnd(1)
    sprite('nt610_06', 8)
    sprite('nt610_07', 8)
    sprite('nt610_08', 8)
    sprite('nt610_09', 32767)
    loopRest()
    label(110)
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 55)
    Voiceline('nt503')
    CreateParticle('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)
    sprite('nt610_07', 8)
    sprite('nt610_08', 8)
    sprite('nt610_09', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(130)
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 55)
    Voiceline('nt507')
    DemoEndOnVoiceEnd(1)
    CreateParticle('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)
    sprite('nt610_07', 8)
    sprite('nt610_08', 8)
    sprite('nt610_09', 32767)
    loopRest()
    label(2130)
    sprite('nt611_00', 4)
    sprite('nt611_01', 4)
    sprite('nt611_02', 4)
    Voiceline('nt507')
    DemoEndOnVoiceEnd(1)
    sprite('nt611_03', 4)
    SetActionMark(3)
    label(2131)
    sprite('nt611_01', 4)
    AddActionMark(-1)
    sprite('nt611_02', 4)
    sprite('nt611_03', 4)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2131)
    sprite('nt611_04', 4)
    CreateObject('ntef_611', -1)
    PrivateSE('ntse_11')
    sprite('nt611_05', 3)
    sprite('nt611_06', 3)
    sprite('nt611_07', 3)
    sprite('nt611_08', 3)
    sprite('nt611_09', 32767)
    label(210)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    Voiceline('nt523')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(260)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    Voiceline('nt533')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(280)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    Voiceline('nt537')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(370)
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 55)
    Voiceline('nt555')
    CreateParticle('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)
    sprite('nt610_07', 8)
    sprite('nt610_08', 8)
    sprite('nt610_09', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(410)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    Voiceline('nt563')
    DemoEndOnVoiceEnd(1)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 50)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    loopRest()
    label(1410)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    Voiceline('nt563')
    DemoEndOnVoiceEnd(1)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 50)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    loopRest()


@State
def CmnActLose():
    sprite('nt620_00', 8)
    sprite('nt620_01', 8)
    sprite('nt620_02', 8)
    LandingEffects(100, 1, 1)
    sprite('nt620_03', 8)
    sprite('nt620_04', 8)
    sprite('nt620_05', 8)
    sprite('nt620_06', 8)
    sprite('nt620_07', 8)
    sprite('nt620_08', 8)
    sprite('nt620_09', 8)
    sprite('nt620_10', 32767)
    Voiceline('nt411')
    DemoEndOnVoiceEnd(1)
    CreateParticle('ntef_620_tameiki', 0)


@State
def EventDefEntryWait():
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventStandToReverse():
    sprite('nt003_00', 6)
    Flip()
    sprite('nt003_01', 6)
    sprite('nt003_00ex01', 6)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    enterState('CmnActStand')


@State
def EventStandReverse():
    sprite('nt003_00', 6)
    Flip()
    sprite('nt003_01', 6)
    sprite('nt003_00ex01', 6)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    sprite('nt407_00', 4)
    sprite('nt407_01', 4)
    sprite('nt407_02', 4)
    sprite('nt407_03', 10)
    sprite('nt407_02', 8)
    sprite('nt407_04', 6)
    sprite('nt407_05', 5)
    enterState('CmnActStand')


@State
def EventReverse():
    XPositionRelativeFacing(-350000)
    sprite('nt000_00', 7)
    Flip()
    label(0)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    sprite('nt000_00', 7)
    loopRest()
    gotoLabel(0)


@State
def EventSake():
    sprite('nt407_00', 4)
    sprite('nt407_01', 4)
    sprite('nt407_02', 4)
    sprite('nt407_03', 10)
    sprite('nt407_02', 8)
    sprite('nt407_04', 6)
    sprite('nt407_05', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventRCExcite():
    sprite('nt300_00', 5)
    sprite('nt300_01', 5)
    sprite('nt300_02', 5)
    sprite('nt300_03', 5)
    sprite('nt300_04', 6)
    sprite('nt300_03', 5)
    sprite('nt300_02', 5)
    sprite('nt300_03', 5)
    sprite('nt300_04', 6)
    sprite('nt300_03', 5)
    sprite('nt300_02', 5)
    sprite('nt300_05', 6)
    sprite('nt300_06', 6)
    sprite('nt300_07', 5)
    sprite('nt300_08', 5)
    sprite('nt300_09', 6)
    sprite('nt300_08', 5)
    sprite('nt300_07', 5)
    sprite('nt300_08', 5)
    sprite('nt300_09', 6)
    sprite('nt300_08', 5)
    sprite('nt300_07', 5)
    sprite('nt300_10', 7)
    sprite('nt300_11', 4)
    sprite('nt300_12', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventRCVSNT():
    sprite('nt312_00', 4)
    sprite('nt312_01', 4)
    sprite('nt312_02', 4)
    sprite('nt312_03', 4)
    sprite('nt312_04', 40)
    sprite('nt312_05', 6)
    sprite('nt312_06', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventRCVSNTWalk():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('nt030_00', 8)
    physicsXImpulse(1800)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventNTWalkNear():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 0:
                SetActionMark(0)
                sendToLabel(1)
    sprite('nt030_00', 8)
    physicsXImpulse(1600)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    enterState('CmnActStand')


@State
def EventUkemiLandB():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 2)
        ScreenCollision(0)
        SetActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 520000:
                    SetActionMark(0)
                    sendToLabel(1)
    sprite('nt030_00', 8)
    physicsXImpulse(4650)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt000_01', 7)
    EndMomentum(1)
    setInvincible(1)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    sprite('nt000_00', 7)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('nt111_00', 2)
    physicsXImpulse(-20000)
    sprite('nt111_01', 2)
    sprite('nt111_02', 2)
    sprite('nt111_03', 2)
    sprite('nt111_04', 2)
    sprite('nt111_05', 2)
    sprite('nt111_06', 2)
    sprite('nt111_07', 3)
    XImpulseAcceleration(40)
    sprite('nt111_08', 3)
    XImpulseAcceleration(40)
    sprite('nt111_08', 3)
    XImpulseAcceleration(40)
    sprite('nt111_09', 3)
    XImpulseAcceleration(0)
    sprite('nt010_01', 3)
    EndMomentum(1)
    sprite('nt010_00', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventRunFlameIn():
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
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventNYvsNTRun():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventCreateLifeLink():
    sprite('keep', 7)
    CreateObject('Fade1', -1)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsRCEntryWaitCameraON():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-750000)
        CameraControlEnable(1)
        ScreenCollision(0)
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventRCVSNTWalk2():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('nt030_00', 8)
    physicsXImpulse(4350)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventAction01():
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 8)
    sprite('nt615_07', 32767)
    loopRest()


@State
def EventAction01End():
    sprite('nt615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventActionKubiKokiKoki():
    sprite('nt603_00', 6)
    sprite('nt603_01', 6)
    sprite('nt603_02', 6)
    sprite('nt603_03', 6)
    sprite('nt603_04', 6)
    sprite('nt603_05', 6)
    sprite('nt603_06', 6)
    sprite('nt603_07', 6)
    sprite('nt603_08', 6)
    sprite('nt603_07', 6)
    sprite('nt603_06', 6)
    sprite('nt603_05', 6)
    sprite('nt603_04', 6)
    sprite('nt603_03', 6)
    sprite('nt603_02', 6)
    sprite('nt603_01', 6)
    sprite('nt603_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsCEWalkAndBDash():

    def upon_EVERY_FRAME():
        uponSendToLabel(32, 10)
        ScreenCollision(0)
    sprite('nt030_00', 8)
    physicsXImpulse(4350)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    EndMomentum(1)
    loopRest()
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('nt033_00', 1)
    sprite('nt033_01', 3)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    setInvincible(1)
    sprite('nt033_02', 3)
    uponSendToLabel(LANDING, 20)
    label(3)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(3)
    label(20)
    sprite('nt033_03', 1)
    EndMomentum(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)
    XPositionRelativeFacing(-260000)
    setInvincible(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSVHWalk():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-900000)
        CameraControlEnable(1)
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('nt030_00', 8)
    physicsXImpulse(4350)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    label(3)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(3)


@State
def EventVSVHEntry01():
    label(0)
    sprite('nt601_00', 12)
    sprite('nt601_01', 8)
    sprite('nt601_02', 12)
    sprite('nt601_01', 8)
    loopRest()
    gotoLabel(0)


@State
def EventVSVHEntry02():
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 32767)


@State
def EventVSVHEntryEnd():
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsVHEntryWaitCameraON():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-900000)
        CameraControlEnable(1)
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_ntvsmk_00():
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_ntvsmk_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-1500000)
        CameraControlEnable(1)
        uponSendToLabel(32, 3)
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('nt030_00', 9)
    physicsXImpulse(3000)
    label(0)
    sprite('nt030_01', 9)
    sprite('nt030_02', 9)
    sprite('nt030_03', 9)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 9)
    sprite('nt030_05', 9)
    sprite('nt030_06', 9)
    sprite('nt030_07', 9)
    sprite('nt030_08', 9)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 9)
    sprite('nt030_10', 9)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    CameraControlEnable(0)
    ScreenCollision(1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('nt407_00', 4)
    EndMomentum(1)
    SetZVal(500)
    sprite('nt407_01', 4)
    sprite('nt407_02', 4)
    sprite('nt407_03', 18)
    CreateParticle('ef_kaihi', 103)
    sprite('nt407_02', 8)
    sprite('nt407_04', 6)
    sprite('nt407_05', 5)
    loopRest()
    SetZVal(0)
    enterState('CmnActStand')


@State
def Act2Event_ntvsmk_02():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
    sprite('nt603_04ex01', 32767)
    loopRest()
    label(0)
    sprite('nt603_04ex01', 4)
    sprite('nt603_09', 6)
    sprite('nt603_10', 6)
    physicsXImpulse(4000)
    sprite('nt030_01', 7)
    sprite('nt030_02', 7)
    sprite('nt030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt000_00', 7)
    EndMomentum(1)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ntvsrm_01():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
    sprite('nt603_04ex01', 32767)
    loopRest()
    label(0)
    sprite('nt603_04ex01', 4)
    sprite('nt603_09', 6)
    sprite('nt603_10', 6)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ntvsrm_02():
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    sprite('nt001_00', 7)
    sprite('nt001_01', 7)
    sprite('nt001_02', 7)
    sprite('nt001_03', 7)
    sprite('nt001_04', 7)
    sprite('nt001_05', 7)
    sprite('nt001_06', 7)
    sprite('nt001_07', 7)
    enterState('CmnActStand')


@State
def Act2Event_ntvsrm_04_stop():
    sprite('nt610_03', 32767)
    loopRest()


@State
def Act2Event_ntvsrm_04_toStand():
    sprite('keep', 120)
    sprite('nt610_01', 5)
    sprite('nt610_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ntvsrm_05():
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    loopRest()


@State
def Act2Event_ntvsrg_00():
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_ntvsrg_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-2100000)
        CameraControlEnable(1)
        uponSendToLabel(32, 3)
    ScreenCollision(0)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 720000:
                SetActionMark(1)
        elif SLOT_XDistanceFromCenterOfStage > -720000:
            SetActionMark(1)
    sprite('nt030_00', 9)
    physicsXImpulse(3000)
    label(0)
    sprite('nt030_01', 9)
    sprite('nt030_02', 9)
    sprite('nt030_03', 9)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 9)
    sprite('nt030_05', 9)
    sprite('nt030_06', 9)
    sprite('nt030_07', 9)
    sprite('nt030_08', 9)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 9)
    sprite('nt030_10', 9)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(0)
    sprite('nt030_01', 9)
    sprite('nt030_02', 9)
    sprite('nt030_03', 9)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 9)
    sprite('nt603_10', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-380000)
    sprite('nt603_09', 6)
    sprite('nt603_08', 6)
    sprite('nt603_07', 6)
    sprite('nt603_04ex02', 32767)
    loopRest()


@State
def Act2Event_ntvsrg_02():
    sprite('nt603_04ex02', 32767)
    CameraControlEnable(0)
    loopRest()


@State
def Act2Event_ntvsrg_03():
    sprite('nt603_04ex02', 60)
    sprite('nt603_04ex01', 180)
    sprite('nt603_04ex01', 4)
    sprite('nt603_09', 4)
    sprite('nt603_10', 4)
    sprite('nt032_00', 3)
    physicsXImpulse(15000)
    sprite('nt032_01', 3)
    sprite('nt032_09', 3)
    physicsXImpulse(0)
    AddInertia(3000)
    sprite('nt032_10', 3)
    sprite('nt032_11', 3)
    sprite('nt032_12', 3)
    sprite('nt000_00', 7)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ntvsrg_04():
    sprite('nt603_04ex01', 32767)
    loopRest()


@State
def Act2Event_ntvsrg_05():
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventBGBlack():
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    CreateObject('Fade2', 0)
    ObjectUpon(22, 32)

    def RunOnObject_1():
        RegisterObject(4, 1)
        SetZVal(-2000)
    loopRest()
    sprite('keep', 1)
    CommonSE('022_magiccircle_b')
    SetZVal(-2000)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Nirami():
    sprite('nt003_00', 6)
    Flip()
    sprite('nt603_02', 6)
    Flip()
    sprite('nt603_03', 6)
    sprite('nt603_04ex01', 32767)
    loopRest()


@State
def Act2Event_NiramiEnd():
    sprite('nt603_03', 6)
    sprite('nt603_02', 6)
    sprite('nt003_00', 6)
    Flip()
    loopRest()
    Flip()
    enterState('CmnActStand')


@State
def Act2Event_Swing():
    sprite('nt611_00', 3)
    sprite('nt611_01', 3)
    sprite('nt611_05', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('nt611_06', 3)
    sprite('nt611_07', 5)
    sprite('nt611_08', 5)
    sprite('nt611_09', 24)
    sprite('nt611_08', 4)
    sprite('nt611_07', 4)
    sprite('nt404_00ex01', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RoundWin():
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 6)
    sprite('nt615_07', 32767)
    loopRest()


@State
def Act2Event_RoundWinEnd():
    sprite('nt615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_vhvsnt_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-120000)

        def upon_LANDING():
            sendToLabel(0)
            EndMomentum(1)
            LandingEffects(100, 1, 1)
    sprite('nt033_00', 3)
    sprite('nt033_01', 3)
    physicsXImpulse(-10000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    loopRest()
    label(9)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('nt033_03', 4)
    sprite('nt620_01', 6)
    Flip()
    sprite('nt620_02', 6)
    sprite('nt620_03', 7)
    sprite('nt620_04', 7)
    sprite('nt620_05', 7)
    sprite('nt620_06', 7)
    sprite('nt620_07', 7)
    sprite('nt620_08', 7)
    sprite('nt620_09', 7)
    sprite('nt620_10', 32767)
    CreateParticle('ntef_620_tameiki', 0)
    loopRest()


@State
def Act2Event_vhvsnt_01():
    sprite('keep', 2)
    sprite('nt620_09', 5)
    sprite('nt620_08', 5)
    sprite('nt620_07', 5)
    sprite('nt620_06', 5)
    sprite('nt620_05', 32767)
    loopRest()


@State
def Act2Event_ntvsmi_00():
    sprite('nt402_08', 7)
    LandingEffects(100, 1, 1)
    sprite('nt402_09', 7)
    sprite('nt402_10', 12)
    sprite('nt402_11', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_kubi():
    sprite('nt603_00', 6)
    sprite('nt603_01', 6)
    sprite('nt603_02', 6)
    sprite('nt603_03', 6)
    sprite('nt603_04', 6)
    sprite('nt603_05', 6)
    sprite('nt603_06', 6)
    sprite('nt603_07', 6)
    sprite('nt603_08', 6)
    sprite('nt603_07', 6)
    sprite('nt603_06', 6)
    sprite('nt603_05', 6)
    sprite('nt603_04', 6)
    sprite('nt603_03', 6)
    sprite('nt603_02', 6)
    sprite('nt603_01', 6)
    sprite('nt603_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_hitoiki_00():
    sprite('nt610_00', 6)
    sprite('nt610_01', 6)
    sprite('nt610_02', 6)
    sprite('nt610_03', 6)
    sprite('nt610_04', 6)
    sprite('nt610_05', 32767)
    CreateParticle('ntef_610_tameiki', 0)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_hitoiki_01():
    sprite('nt610_06', 6)
    sprite('nt610_03', 6)
    sprite('nt610_02', 6)
    sprite('nt610_01', 6)
    sprite('nt610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventAct2_TKvsNT00():
    sprite('keep', 2)
    XPositionRelativeFacing(320000)
    loopRest()
    enterState('CmnActStand')


@State
def EventAct2_TKvsNT01():
    sprite('nt090_00', 2)
    physicsXImpulse(-20000)
    sprite('nt090_00', 4)
    physicsXImpulse(0)
    SetInertia(-8000)
    CommonSE('208_brake_normal')
    sprite('nt090_01', 4)
    CommonSE('208_brake_normal')
    sprite('nt090_02', 60)
    CommonSE('208_brake_normal')
    sprite('nt090_03', 6)
    CommonSE('208_brake_normal')
    sprite('nt090_04', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Entry_ClosedEye():
    sprite('nt603_04ex02', 32767)
    CameraControlEnable(0)
    loopRest()


@State
def Act3Event_Entry_OpenedEye():
    sprite('nt603_04ex01', 32767)
    CameraControlEnable(0)
    loopRest()


@State
def Act3Event_mivsnt_00():
    sprite('nt611_00', 3)
    sprite('nt611_01', 3)
    sprite('nt611_05', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('nt611_06', 3)
    sprite('nt611_07', 5)
    sprite('nt611_08', 5)
    sprite('nt611_09', 32767)


@State
def Act3Event_mivsnt_01():
    sprite('nt611_08', 3)
    sprite('nt611_07', 3)
    sprite('nt404_00ex01', 3)
    CreateObject('Act3Event_Black', -1)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 2)
    sprite('nt040_00', 3)
    sprite('nt040_01', 3)
    label(0)
    sprite('nt040_02', 4)
    sprite('nt040_03', 4)
    sprite('nt040_04', 4)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mivsnt_02():

    def upon_IMMEDIATE():
        ForceFaceSprite()
    sprite('nt062_01', 32767)
    TriggerUponForState('Act3Event_Black', 32)
    CreateObject('Act3Event_mivsnt_01', -1)
    CreateObject('Act3Event_mivsnt_02_rl', -1)
    setGravity(0)
    AddX(320000)
    AddY(160000)
    Flip()
    loopRest()


@State
def Act3Event_ntvshz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-2200000)
        CameraControlEnable(1)
        ScreenCollision(0)
        SetActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 1750000:
                    SetActionMark(0)
                    sendToLabel(1)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
    sprite('nt030_00', 8)
    physicsXImpulse(4800)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    EndMomentum(1)
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('nt615_00', 6)
    sprite('nt615_01', 6)
    sprite('nt615_02', 6)
    sprite('nt615_03', 12)
    sprite('nt615_04', 6)
    PrivateSE('ntse_10')
    sprite('nt615_05', 20)
    sprite('nt615_06', 6)
    sprite('nt615_07', 32767)
    label(4)
    sprite('nt615_00', 6)
    loopRest()
    gotoLabel(2)
    label(5)
    sprite('nt030_00', 8)
    physicsXImpulse(4800)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    DashEffects(100, 1, 1)
    sprite('nt030_04', 8)
    CameraControlEnable(0)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    EndMomentum(1)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_ntvshz_01():

    def upon_IMMEDIATE():
        AddX(-150000)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt402_00', 2)
    ObjectUpon(22, 32)
    sprite('nt402_00', 2)
    sprite('nt402_01', 2)
    sprite('nt402_02', 3)
    physicsXImpulse(2500)
    sprite('nt402_03', 3)
    XImpulseAcceleration(120)
    DashEffects(100, 1, 1)
    sprite('nt402_04', 3)
    PrivateSE('ntse_03')
    CreateObject('ntef_402', -1)
    XImpulseAcceleration(200)
    SetXCollisionFromOrigin(150)
    DashEffects(100, 1, 1)
    sprite('nt402_05', 15)
    XImpulseAcceleration(120)
    SetXCollisionFromOrigin(200)
    PreDashEffects(100, 1, 1)
    sprite('nt402_06', 3)
    sprite('nt402_07', 3)
    SetXCollisionFromOrigin(-1)
    sprite('nt402_08', 3)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(50)
    sprite('nt402_09', 3)
    EndMomentum(1)
    sprite('nt402_10', 3)
    sprite('nt402_11', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvshz_02():
    sprite('nt032_00', 2)
    physicsXImpulse(12000)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('keep', 1)
    sprite('nt032_09', 3)
    EndMomentum(1)
    AddInertia(9000)
    sprite('nt032_10', 3)
    sprite('nt032_11', 3)
    sprite('nt032_12', 2)
    sprite('nt032_12', 1)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsha_00():

    def upon_IMMEDIATE():
        AddX(130000)
        uponSendToLabel(33, 1)
    label(0)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt040_05', 10)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('104_guard_grap_1')
    ScreenShake(2000, 5000)
    sprite('nt040_01', 3)
    AddInertia(-21000)
    sprite('nt040_02', 3)
    sprite('nt040_03', 3)
    sprite('nt040_01', 3)
    sprite('nt040_00', 2)
    sprite('nt040_00', 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsha_01():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        NoDamageAction(1)
    sprite('nt603_04ex01', 32767)
    loopRest()
    label(0)
    sprite('nt603_03', 4)
    sprite('nt603_02', 4)
    sprite('nt003_00', 4)
    Flip()
    sprite('nt407_00', 4)
    Flip()
    EndMomentum(1)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    sprite('nt407_01', 4)
    sprite('nt407_02', 4)
    sprite('nt407_03', 18)
    sprite('nt407_02', 8)
    SetZLine(1, 30)
    EnableCollision(1)
    EnableAfterimage(0)
    sprite('nt407_04', 6)
    sprite('nt407_05', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsha_02():

    def upon_IMMEDIATE():
        ObjectUpon(22, 32)
    sprite('nt611_00', 3)
    sprite('nt611_01', 3)
    sprite('nt611_05', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('nt611_06', 3)
    sprite('nt611_07', 5)
    sprite('nt611_08', 5)
    sprite('nt611_09', 24)
    sprite('nt611_08', 4)
    sprite('nt611_07', 4)
    sprite('nt404_00ex01', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsrl_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-2200000)
        CameraControlEnable(1)
        ScreenCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_19 < 1750000:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(1)

        def upon_32():
            CameraControlEnable(0)
    sprite('nt030_00', 8)
    physicsXImpulse(4800)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    EndMomentum(1)
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(2)


@State
def Act3Event_ntvsrl_01():

    def upon_IMMEDIATE():
        AddX(250000)
        uponSendToLabel(32, 40)
    sprite('nt000_00', 7)
    sprite('nt033_00', 1)
    sprite('nt033_01', 3)
    physicsXImpulse(-15000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    setInvincible(1)
    sprite('nt033_02', 3)
    uponSendToLabel(LANDING, 20)
    label(3)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(3)
    label(20)
    sprite('nt033_03', 1)
    EndMomentum(1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 2)
    sprite('nt033_05', 2)
    sprite('nt033_06', 2)
    sprite('nt033_07', 2)
    setInvincible(0)
    label(30)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(30)
    label(40)
    sprite('nt040_05', 10)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')
    ScreenShake(2000, 5000)
    sprite('nt040_01', 3)
    AddInertia(-21000)
    sprite('nt040_02', 3)
    sprite('nt040_03', 3)
    sprite('nt040_01', 3)
    sprite('nt040_00', 2)
    sprite('nt040_00', 1)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsrl_02():
    ScreenCollision(0)
    EnableCollision(0)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 640000:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(1)
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('nt032_09', 3)
    EndMomentum(1)
    AddInertia(9000)
    sprite('nt032_10', 3)
    sprite('nt032_11', 3)
    sprite('nt032_12', 2)
    sprite('nt032_12', 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('Act2Event_Swing')


@State
def Act3Event_ntvsrl_03():

    def upon_IMMEDIATE():
        AlphaValue(0)
        Visibility(1)
    sprite('null', 1)
    PrivateSE('ntse_14')
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_ntvsrl_04():

    def upon_IMMEDIATE():
        AlphaValue(0)
        Visibility(1)
    sprite('null', 1)
    CommonSE('000_airdash_1')
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_ntvsrc_00():

    def upon_IMMEDIATE():
        ObjectUpon(22, 32)
        XPositionRelativeFacing(-900000)
        AbsoluteY(12000)
        Flip()
        AttackDefaults_StandingDD()
    sprite('nt060_05', 4)
    physicsXImpulse(-22000)
    physicsYImpulse(16000)
    setGravity(1200)
    ScreenCollision(0)
    uponSendToLabel(LANDING, 1)
    sprite('nt060_06', 4)
    label(0)
    sprite('nt072_01', 3)
    sprite('nt072_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt060_07', 3)
    clearUponHandler(LANDING)
    XImpulseAcceleration(0)
    AltKnockdownEffects(100, 1, 1)
    sprite('nt060_08', 3)
    sprite('nt060_14', 40)
    AltKnockdownEffects(100, 1, 1)
    sprite('nt061_00', 4)
    sprite('nt061_01', 3)
    sprite('nt061_02', 3)
    sprite('nt061_03', 3)
    sprite('nt061_04', 3)
    sprite('nt061_05', 3)
    sprite('nt061_06', 3)
    sprite('nt061_07', 3)
    sprite('nt061_08', 3)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ntvsrc_01():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_19 < 140000:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(1)
            EnableCollision(1)
        AttackDefaults_StandingDD()
        uponSendToLabel(32, 5)
    sprite('nt603_03', 6)
    sprite('nt603_02', 6)
    sprite('nt003_00', 6)
    Flip()
    sprite('keep', 1)
    Flip()
    sprite('nt030_00', 8)
    physicsXImpulse(4800)
    label(0)
    sprite('nt030_01', 8)
    sprite('nt030_02', 8)
    sprite('nt030_03', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)
    sprite('nt030_05', 8)
    sprite('nt030_06', 8)
    sprite('nt030_07', 8)
    sprite('nt030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)
    sprite('nt030_10', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    EndMomentum(1)
    label(2)
    sprite('nt000_00', 7)
    sprite('nt000_01', 7)
    sprite('nt000_02', 7)
    sprite('nt000_03', 7)
    sprite('nt000_04', 7)
    sprite('nt000_05', 7)
    sprite('nt000_06', 7)
    sprite('nt000_07', 7)
    sprite('nt000_08', 7)
    loopRest()
    gotoLabel(2)
    label(5)
    sprite('nt072_00', 1)
    clearUponHandler(EVERY_FRAME)
    AddX(3000)
    sprite('nt072_00', 1)
    AddX(-3000)
    sprite('nt072_00', 1)
    AddX(3000)
    sprite('nt072_00', 1)
    AddX(-3000)
    sprite('nt072_00', 1)
    AddX(3000)
    sprite('nt072_00', 1)
    AddX(-3000)
    sprite('nt072_00', 1)
    AddX(3000)
    sprite('nt072_00', 1)
    AddX(-3000)
    sprite('nt072_00', 1)
    AddX(3000)
    sprite('nt072_00', 1)
    AddX(-3000)
    sprite('nt072_00', 3)
    physicsXImpulse(-32000)
    physicsYImpulse(12000)
    setGravity(2500)
    uponSendToLabel(LANDING, 7)
    label(6)
    sprite('nt072_01', 3)
    sprite('nt072_02', 3)
    loopRest()
    gotoLabel(6)
    label(7)
    sprite('nt060_07', 3)
    clearUponHandler(LANDING)
    XImpulseAcceleration(0)
    XPositionRelativeFacing(-260000)
    AltKnockdownEffects(100, 1, 1)
    sprite('nt060_08', 3)
    sprite('nt060_14', 40)
    AltKnockdownEffects(100, 1, 1)
    sprite('nt061_00', 4)
    sprite('nt061_01', 3)
    sprite('nt061_02', 3)
    sprite('nt061_03', 3)
    sprite('nt061_04', 3)
    sprite('nt061_05', 3)
    sprite('nt061_06', 3)
    sprite('nt061_07', 3)
    sprite('nt061_08', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_NiramiClose():
    sprite('nt003_00', 6)
    Flip()
    sprite('nt603_02', 6)
    Flip()
    sprite('nt603_03', 6)
    sprite('nt603_04ex02', 32767)
    loopRest()


@State
def Act3Event_DashIn():
    ScreenCollision(0)
    EnableCollision(0)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 640000:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(1)
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('nt032_09', 3)
    EndMomentum(1)
    AddInertia(9000)
    sprite('nt032_10', 3)
    sprite('nt032_11', 3)
    sprite('nt032_12', 2)
    sprite('nt032_12', 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_DashOut():
    ScreenCollision(0)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    sprite('nt032_01', 3)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    sprite('nt032_06', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    sprite('null', 32767)
    Visibility(1)
    AlphaValue(0)
    loopRest()


@State
def Act3Event_esvsnt_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-1220000)

        def RunOnObject_22():
            CameraControlEnable(0)
        CameraControlEnable(1)

        def upon_32():
            CameraControlEnable(0)
            clearUponHandler(32)

        def upon_STATE_END():
            CameraControlEnable(0)
    label(0)
    sprite('nt620_09', 8)
    sprite('nt620_08', 8)
    sprite('nt620_07', 8)
    sprite('nt620_06', 20)
    sprite('nt620_07', 8)
    sprite('nt620_08', 8)
    sprite('nt620_09', 8)
    sprite('nt620_10', 240)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_esvsnt_01():
    XPositionRelativeFacing(200000)
    sprite('nt111_00', 3)
    AddInertia(-60000)
    sprite('nt111_01', 3)
    sprite('nt111_02', 3)
    sprite('nt111_03', 3)
    sprite('nt111_04', 3)
    sprite('nt111_05', 3)
    LandingEffects(100, 1, 1)
    sprite('nt111_06', 3)
    sprite('nt111_07', 3)
    sprite('nt111_08', 3)
    sprite('nt111_08', 6)
    EndMomentum(1)
    sprite('nt111_09', 6)
    sprite('nt010_01', 6)
    sprite('nt010_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_esvsnt_02():
    ScreenCollision(0)
    sprite('nt603_03', 3)
    sprite('nt603_02', 3)
    sprite('nt003_00', 3)
    Flip()
    sprite('nt003_01', 3)
    sprite('nt003_00ex01', 3)
    sprite('nt032_00', 2)
    physicsXImpulse(20000)
    label(0)
    sprite('nt032_01', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_06', 3)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    loopRest()
    sprite('nt032_01', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_06', 3)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    sprite('nt032_01', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_02', 3)
    sprite('nt032_03', 4)
    sprite('nt032_04', 3)
    sprite('nt032_05', 3)
    DashEffects(100, 1, 1)
    sprite('nt032_06', 3)
    sprite('nt032_07', 4)
    sprite('nt032_08', 3)
    sprite('null', 32767)
    Visibility(1)
    AlphaValue(0)
    loopRest()


@State
def Act3Event_esvsnt_90():
    label(0)
    sprite('nt601_00', 40)
    sprite('nt601_01', 8)
    sprite('nt601_02', 20)
    sprite('nt601_01', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_esvsnt_91():
    sprite('keep', 2)
    sprite('nt601_03', 7)
    sprite('nt601_04', 7)
    sprite('nt601_05', 32767)
    loopRest()


@State
def Act3Event_esvsnt_92():
    sprite('nt601_05', 2)
    CreateObject('ntef_601', -1)
    sprite('nt601_05', 32767)
    loopRest()


@State
def Act3Event_esvsnt_93():
    sprite('nt601_06', 9)
    sprite('nt601_07', 9)
    sprite('nt601_08', 9)
    CommonSE('019_cloth_a')
    sprite('nt601_09', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_esvsnt_94():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(50000)
        uponSendToLabel(LANDING, 1)
    sprite('nt041_00', 3)
    sprite('nt041_01', 3)
    sprite('nt041_02', 4)
    sprite('nt041_03', 4)
    sprite('nt033_00', 3)
    sprite('nt033_01', 3)
    physicsXImpulse(-20000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('nt033_02', 3)
    label(0)
    sprite('nt033_01', 3)
    sprite('nt033_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt033_03', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('nt033_04', 4)
    sprite('nt033_05', 4)
    sprite('nt033_06', 4)
    sprite('nt033_07', 4)
    loopRest()
    enterState('CmnActStand')
