@Subroutine
def PreInit():
    CharacterID('am')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(10500)
    DashFInitialVelocity(13000)
    DashFMaxVelocity(15000)
    JumpYVelocity(31200)
    SuperJumpYVelocity(33000)
    Gravity(1170)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    ResourceGauge(0, 1, 38, 1, 6000, 0, -14663425, -14663425)
    ResourceGaugeFlash(0, 1)
    CPURetreatPriority(5000)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    Unknown15027(5000)
    SkillEstimateRange(0, 250000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    AirborneOpponentPriority(4000)
    SkillEstimateRange(-100000, 300000, -100000, 400000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 250000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2A2nd', INPUT_2A)
    MoveMaxChainRepeat(3)
    FollowupOnly(1)
    Move_Input_(0x2)
    SharedGatling('NmlAtk2A')
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('Atk2A3rd', INPUT_2A)
    MoveMaxChainRepeat(3)
    FollowupOnly(1)
    Move_Input_(0x2)
    SharedGatling('NmlAtk2A')
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    MoveCancellableFrames(23, 25)
    GuardStunPriority(4000)
    SkillEstimateRange(0, 450000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 350000, -100000, 250000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    SkillEstimateRange(0, 450000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4C', INPUT_4C)
    MoveMaxChainRepeat(1)
    OpponentAttackPriority(250)
    DamageStunPriority(1)
    SkillEstimateRange(450000, 800000, -100000, 350000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(1)
    Move_Input_(0x66)
    OpponentAttackPriority(250)
    DamageStunPriority(1)
    MoveCancellableFrames(40, 42)
    SkillEstimateRange(650000, 1000000, -100000, 450000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveMaxChainRepeat(1)
    MoveCancellableFrames(50, 52)
    AirborneOpponentPriority(4000)
    SkillEstimateRange(700000, 1100000, 200000, 650000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk1C', INPUT_1C)
    MoveMaxChainRepeat(1)
    MoveLow()
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(500000, 800000, -100000, 250000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    MoveMaxChainRepeat(1)
    Move_Input_(0x3f)
    MoveLow()
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    MoveCancellableFrames(40, 42)
    SkillEstimateRange(700000, 1000000, -100000, 250000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(0)
    MoveComboPriority(3000)
    SkillEstimateRange(0, 500000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    CallSkillConditions('IsDRILLReady')
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(4000)
    GuardStunPriority(2000)
    MoveCancellableFrames(50, 60)
    MoveButtonHoldTime(3, 50, 60)
    SkillEstimateRange(0, 450000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    CallSkillConditions('IsDRILLReady')
    MoveButtonHoldTime(3, 88, 90)
    DamageStunPriority(5000)
    GuardStunPriority(3000)
    SkillEstimateRange(600000, 900000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    CallSkillConditions('IsDRILLReady')
    MoveButtonHoldTime(3, 30, 40)
    MoveCancellableFrames(38, 40)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(-50000, 250000, 150000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AtkAIR5A2nd', INPUT_J5A)
    FollowupOnly(1)
    Move_Input_(0x2)
    SharedGatling('NmlAtkAIR5A')
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    MoveCancellableFrames(28, 29)
    SkillEstimateRange(0, 550000, -450000, 100000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    MoveMaxChainRepeat(1)
    MoveCancellableFrames(40, 42)
    SkillEstimateRange(600000, 1100000, -350000, 0, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6C', INPUT_J6C)
    Move_Input_(0x59)
    MoveMaxChainRepeat(1)
    AirborneOpponentPriority(5000)
    MoveCancellableFrames(42, 43)
    SkillEstimateRange(600000, 1100000, -50000, 400000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR4C', INPUT_J4C)
    Move_Input_(0x8d)
    MoveMaxChainRepeat(1)
    GuardStunPriority(0)
    AirborneOpponentPriority(5000)
    MoveCancellableFrames(30, 32)
    SkillEstimateRange(200000, 550000, -600000, -200000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    Move_Input_(0x59)
    SharedGatling('NmlAtkAIR4C')
    StateCall('NmlAtkAIR4C')
    MovePriority(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    CallSkillConditions('IsDRILLReady')
    DamageStunPriority(4000)
    GuardStunPriority(4000)
    MoveCancellableFrames(38, 40)
    MoveButtonHoldTime(3, 48, 50)
    SkillEstimateRange(0, 350000, -450000, -100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B', INPUT_J2B)
    SkillEstimateRange(-200000, 200000, -400000, -100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6D', INPUT_J6D)
    CallSkillConditions('IsDRILLReady')
    Move_Input_(0x59)
    GuardStunPriority(3000)
    MoveCancellableFrames(60, 65)
    MoveButtonHoldTime(3, 60, 65)
    SkillEstimateRange(-50000, 450000, -150000, 500000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(0)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
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
    SkillEstimateRange(100000, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Kamae', INPUT_SPECIALMOVE)
    CallSkillConditions('IsDRILLReady')
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x300a)
    OpponentAttackPriority(1)
    DamageStunPriority(5000)
    GuardStunPriority(5000)
    SkillEstimateRange(650000, 1450000, -250000, 450000, 150, 0)
    Move_EndRegister()
    Move_Register('GroundDrill_A', INPUT_SPECIALMOVE)
    CallSkillConditions('IsDRILLReady')
    FollowupOnly(1)
    Move_Input_(0x2)
    SharedGatling('Kamae')
    SkillEstimateRange(350000, 650000, -200000, 1200000, 10000, 100)
    Move_EndRegister()
    Move_Register('GroundDrill_B', INPUT_SPECIALMOVE)
    CallSkillConditions('IsDRILLReady')
    FollowupOnly(1)
    Move_Input_(0xb)
    SharedGatling('Kamae')
    SkillEstimateRange(650000, 950000, -200000, 1200000, 10000, 100)
    Move_EndRegister()
    Move_Register('GroundDrill_C', INPUT_SPECIALMOVE)
    CallSkillConditions('IsDRILLReady')
    FollowupOnly(1)
    Move_Input_(0x14)
    SharedGatling('Kamae')
    SkillEstimateRange(1050000, 1350000, -200000, 1200000, 10000, 100)
    Move_EndRegister()
    Move_Register('MultiStrike', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(-50000, 400000, -200000, 250000, 500, 10)
    Move_EndRegister()
    Move_Register('Ginga', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(350000, 700000, -200000, 250000, 500, 10)
    Move_EndRegister()
    Move_Register('Anti_Air', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    Unknown15027(2500)
    AirborneOpponentPriority(4000)
    OpponentAttackPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(300000, 800000, 150000, 600000, 0, 100)
    Move_EndRegister()
    Move_Register('MultiStrike_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_C)
    StateCall('MultiStrike')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AirMultiStrike', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(0)
    SkillEstimateRange(0, 500000, -450000, -100000, 250, 50)
    Move_EndRegister()
    Move_Register('FrontJumpA', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(500000, 750000, -100000, 250000, 250, 50)
    Move_EndRegister()
    Move_Register('FrontJumpB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    SkillEstimateRange(500000, 750000, -100000, 250000, 250, 50)
    Move_EndRegister()
    Move_Register('BackJumpA', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    GuardStunPriority(3000)
    MoveCancellableFrames(28, 30)
    SkillEstimateRange(0, 900000, -100000, 250000, 300, 50)
    Move_EndRegister()
    Move_Register('BackJumpB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    GuardStunPriority(3000)
    DamageStunPriority(1)
    MoveCancellableFrames(28, 30)
    SkillEstimateRange(0, 900000, -100000, 250000, 300, 50)
    Move_EndRegister()
    Move_Register('AirFrontJumpA', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3009)
    MovePriority(100)
    DamageStunPriority(1)
    GuardStunPriority(3000)
    Move_EndRegister()
    Move_Register('AirFrontJumpB', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3009)
    MovePriority(100)
    DamageStunPriority(1)
    Move_EndRegister()
    Move_Register('AirBackJumpA', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3009)
    MovePriority(100)
    DamageStunPriority(1)
    MoveCancellableFrames(28, 30)
    Move_EndRegister()
    Move_Register('AirBackJumpB', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3009)
    MovePriority(100)
    DamageStunPriority(1)
    MoveCancellableFrames(38, 40)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_222)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1500)
    DamageStunPriority(3000)
    SkillEstimateRange(200000, 600000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    CallSkillConditions('IsDRILLReady')
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(8000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    CallSkillConditions('IsDRILLReady')
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(8000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('ImperialDrill', INPUT_DISTORTION)
    CallSkillConditions('IsDRILLReady')
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Unknown15027(1)
    GuardStunPriority(5000)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('ImperialDrill_OD', INPUT_DISTORTION)
    CallSkillConditions('IsDRILLReady')
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    Unknown15027(1)
    GuardStunPriority(5000)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
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
    SkillEstimateRange(0, 600000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 600000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 600000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk4C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk1C', 10000000)
    TempPriorityMultiplier('NmlAtk4C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk4C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Ginga', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'MultiStrike', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'FrontJumpA', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'Kamae', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk2B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk1C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk1C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'Ginga', 10000000)
    TempPriorityMultiplier('NmlAtk2D', 'BackJumpA', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'MultiStrike', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtkAIR4C', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'ImperialDrill', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'UltimateAssault', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2B', 'AirBackJumpB', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR4C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR6C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirFrontJumpB', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5D', 'AirMultiStrike', 10000000)
    TempPriorityMultiplier('NmlAtkAIR6C', 'NmlAtkAIR4C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR6D', 'AirBackJumpB', 10000000)
    TempPriorityMultiplier('NmlAtkAIR4C', 'AirMultiStrike', 10000000)
    TempPriorityMultiplier('NmlAtkAIR4C', 'AirBackJumpA', 10000000)
    StylishModeSpecialButton('MultiStrike', 0x4, 0xea)
    StylishModeSpecialButton('Ginga', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('Kamae', 0x4, 0x45)
    StylishModeSpecialButton('AirMultiStrike', 0x4, 0xea)
    StylishModeSpecialButton('AirFrontJumpA', 0x4, 0x79)
    StylishModeSpecialButton('AirBackJumpA', 0x4, 0x5f)
    StylishModeSpecialButton('GroundDrill_A', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk6A', 'FJump', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk3C', 6, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk4C', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk1C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D', 1, 700000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtkAIR4C', 1, 250000)
    StylishModeCancels('NmlAtk6C', 'NmlAtk6A', 0, 0)
    StylishModeCancels('NmlAtk6C', 'Ginga', 13, 0)
    StylishModeCancels('NmlAtk4C', 'NmlAtk3C', 6, 0)
    StylishModeCancels('NmlAtk4C', 'NmlAtk5D', 13, 0)
    StylishModeCancels('NmlAtk4C', 'NmlAtk6C', 12, 0)
    StylishModeCancels('NmlAtk5D', 'Ginga', 0, 0)
    StylishModeCancels('NmlAtk5D', 'MultiStrike', 6, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('ThrowExe', 'Anti_Air', 0, 0)
    StylishModeCancels('BackThrowExe', 'Anti_Air', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk2D', 3, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 13, 0)
    StylishModeCancels('NmlAtk3C', 'MultiStrike', 0, 0)
    StylishModeCancels('NmlAtk3C', 'Ginga', 13, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'MultiStrike', 10, 650000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 1, 700000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk1C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2D', 'FrontJumpA', 0, 0)
    StylishModeCancels('NmlAtk2D', 'Anti_Air', 10, 400000)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'AirFrontJumpA', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'AirMultiStrike', 3, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5D', 13, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirMultiStrike', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR6C', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirBackJumpA', 13, 0)
    StylishModeCancels('NmlAtkAIR2B', 'AirMultiStrike', 0, 0)
    StylishModeCancels('NmlAtkAIR2B', 'AirBackJumpA', 13, 0)
    StylishModeCancels('NmlAtkAIR6C', 'NmlAtkAIR4C', 0, 0)
    StylishModeCancels('NmlAtkAIR6C', 'AirBackJumpA', 13, 0)
    StylishModeCancels('NmlAtkAIR4C', 'AirMultiStrike', 0, 0)
    StylishModeCancels('NmlAtkAIR4C', 'AirBackJumpA', 13, 0)
    HitSprites(0, 'am062_01')
    HitSprites(1, 'am062_03')
    HitSprites(2, 'am062_04')
    HitSprites(3, 'am062_05')
    HitSprites(4, 'am062_05')
    HitSprites(5, 'am062_06')
    HitSprites(6, 'am062_07')
    HitSprites(7, 'am041_02')
    HitSprites(8, 'am040_02')
    HitSprites(9, 'am045_02')
    HitSprites(10, 'am060_00')
    HitSprites(11, 'am060_01')
    HitSprites(12, 'am060_03')
    HitSprites(13, 'am060_05')
    HitSprites(14, 'am060_07')
    HitSprites(15, 'am060_14')
    HitSprites(16, 'am050_00')
    HitSprites(17, 'am052_00')
    HitSprites(18, 'am054_00')
    HitSprites(19, 'am000_00')
    HitSprites(20, 'am000_00')
    HitSprites(25, 'am063_00')
    HitSprites(26, 'am063_01')
    HitSprites(27, 'am063_02')
    HitSprites(28, 'am063_04')
    HitSprites(29, 'am063_10')
    HitSprites(30, 'am077_00')
    HitSprites(31, 'am077_01')
    HitSprites(32, 'am077_00ex01')
    HitSprites(33, 'am077_01ex01')
    HitSprites(34, 'am077_00ex02')
    HitSprites(35, 'am077_01ex02')
    HitSprites(36, 'am077_00ex03')
    HitSprites(37, 'am077_01ex03')
    HitSprites(24, 'am073_01')
    CommonVoicelines(0, 'am000')
    CommonVoicelines(1, 'am001')
    CommonVoicelines(2, 'am002')
    CommonVoicelines(3, 'am003')
    CommonVoicelines(4, 'am004')
    CommonVoicelines(5, 'am005')
    CommonVoicelines(6, 'am006')
    CommonVoicelines(7, 'am007')
    CommonVoicelines(8, 'am008')
    CommonVoicelines(9, 'am009')
    CommonVoicelines(10, 'am010')
    CommonVoicelines(11, 'am011')
    CommonVoicelines(12, 'am012')
    CommonVoicelines(13, 'am013')
    CommonVoicelines(14, 'am014')
    CommonVoicelines(15, 'am015')
    CommonVoicelines(16, 'am016')
    CommonVoicelines(17, 'am017')
    CommonVoicelines(18, 'am018')
    CommonVoicelines(19, 'am019')
    CommonVoicelines(20, 'am020')
    CommonVoicelines(21, 'am021')
    CommonVoicelines(22, 'am022')
    CommonVoicelines(23, 'am023')
    CommonVoicelines(24, 'am024')
    CommonVoicelines(25, 'am025')
    CommonVoicelines(26, 'am026')
    CommonVoicelines(27, 'am027')
    CommonVoicelines(28, 'am028')
    CommonVoicelines(29, 'am029')
    CommonVoicelines(30, 'am030')
    CommonVoicelines(31, 'am031')
    CommonVoicelines(32, 'am032')
    CommonVoicelines(33, 'am033')
    CommonVoicelines(34, 'am034')
    CommonVoicelines(35, 'am035')
    CommonVoicelines(36, 'am036')
    CommonVoicelines(37, 'am037')
    CommonVoicelines(38, 'am038')
    CommonVoicelines(39, 'am039')
    CommonVoicelines(40, 'am040')
    CommonVoicelines(41, 'am041')
    CommonVoicelines(42, 'am042')
    CommonVoicelines(43, 'am043')
    CommonVoicelines(44, 'am044')
    CommonVoicelines(45, 'am045')
    CommonVoicelines(46, 'am046')
    CommonVoicelines(47, 'am047')
    CommonVoicelines(48, 'am048')
    CommonVoicelines(49, 'am049')
    CommonVoicelines(50, 'am050')
    CommonVoicelines(51, 'am051')
    CommonVoicelines(52, 'am052')
    CommonVoicelines(53, 'am053')
    CommonVoicelines(54, 'am100')
    CommonVoicelines(55, 'am101')
    CommonVoicelines(56, 'am102')
    CommonVoicelines(57, 'am103')
    CommonVoicelines(58, 'am104')
    CommonVoicelines(59, 'am105')
    CommonVoicelines(60, 'am106')
    CommonVoicelines(61, 'am107')
    CommonVoicelines(62, 'am108')
    CommonVoicelines(63, 'am109')
    CommonVoicelines(64, 'am150')
    CommonVoicelines(65, 'am151')
    CommonVoicelines(66, 'am152')
    CommonVoicelines(67, 'am153')
    CommonVoicelines(68, 'am154')
    CommonVoicelines(69, 'am155')
    CommonVoicelines(70, 'am156')
    CommonVoicelines(71, 'am157')
    CommonVoicelines(72, 'am158')
    CommonVoicelines(75, 'am160')
    CommonVoicelines(73, 'am402')
    CommonVoicelines(74, 'am403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def IsDRILLReady():
    SLOT_47 = 0
    if op(15, 2, 59, 0, 0):
        SLOT_47 = 1


@Subroutine
def DrillLevelUp():
    if SLOT_59 == 1:
        SLOT_31 = 0
        SLOT_59 = 2
    elif SLOT_59 == 2:
        SLOT_31 = 0
        SLOT_59 = 3
    elif SLOT_59 == 3:
        SLOT_31 = 6000
        SLOT_59 = 0
        SLOT_60 = 0
    callSubroutine('ExGageUpDate')
    if not CurrentStateCheck('Kamae'):
        callSubroutine('DrillActionJump')


@Subroutine
def DrillLevelDown():
    if not SLOT_31:
        if SLOT_59 == 0:
            SLOT_31 = 0
            SLOT_59 = 1
        elif SLOT_59 == 2:
            SLOT_31 = 6000
            SLOT_59 = 1
        elif SLOT_59 == 3:
            SLOT_31 = 6000
            SLOT_59 = 2
    TrainingModeSLOT('TRI_AmaneDrill', 2, 67)
    if SLOT_67:
        if op(15, 2, 59, 0, 0):
            SLOT_67 = SLOT_67 + 1
            if SLOT_59 < SLOT_67:
                SLOT_59 = SLOT_67
                SLOT_31 = 0
    callSubroutine('ExGageUpDate')


@Subroutine
def ExGageUpDate():
    if SLOT_59 == 0:
        ResourceBarIcon(0, 73)
        ResourceBarColor(0, 4294901760)
        ResourceBarFullColor(0, 4294901760)
        ResourceGaugeX(0, 1)
    if SLOT_59 == 1:
        ResourceBarIcon(0, 38)
        ResourceBarColor(0, 4280303871)
        ResourceBarFullColor(0, 4280303871)
        ResourceGaugeX(0, 0)
    if SLOT_59 == 2:
        ResourceBarIcon(0, 39)
        ResourceBarColor(0, 4282417407)
        ResourceBarFullColor(0, 4282417407)
        ResourceGaugeX(0, 0)
    if SLOT_59 == 3:
        ResourceBarIcon(0, 40)
        ResourceBarColor(0, 4284547071)
        ResourceBarFullColor(0, 4284547071)
        ResourceGaugeX(0, 0)


@Subroutine
def DrillAttackData1():
    AttackLevel_(3)
    AttackP1(80)
    AttackP2(99)
    ChipPercentage(30)
    Hitstop(2)
    HitsparkSize(800)
    ReduceHitEffects(1)
    Unknown12052(1)
    StarterRating(2)


@Subroutine
def DrillAttackData2():
    AttackLevel_(4)
    AttackP1(80)
    AttackP2(99)
    ChipPercentage(60)
    Hitstop(1)
    HitsparkSize(600)
    ReduceHitEffects(1)
    Unknown12052(1)
    StarterRating(2)


@Subroutine
def DrillAttackData3():
    AttackLevel_(5)
    AttackP1(80)
    AttackP2(99)
    ChipPercentage(90)
    MinimumDamage(5)
    Hitstop(0)
    PushbackX(30400)
    HitsparkSize(400)
    ReduceHitEffects(1)
    Unknown12052(1)
    StarterRating(2)


@Subroutine
def DrillActionJump():
    if SLOT_59 == 0:
        sendToLabel(1)
    SetActionMark(30)
    if SLOT_59 == 1:
        sendToLabel(100)
        callSubroutine('DrillAttackData1')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_53 = 3
            SLOT_31 = SLOT_31 + 70
            ScreenShake(500, 500)
            if CurrentStateCheck('NmlAtkAIR5D'):
                YAccel(90)

        def upon_OPPONENT_HIT():
            SLOT_31 = SLOT_31 - 20
    if SLOT_59 == 2:
        sendToLabel(200)
        callSubroutine('DrillAttackData2')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_53 = 2
            SLOT_31 = SLOT_31 + 70
            ScreenShake(1000, 1000)
            if CurrentStateCheck('NmlAtkAIR5D'):
                YAccel(90)
            SLOT_54 = SLOT_54 + -1
            if SLOT_54 <= 0:
                DamageEffect(0, '')
                GuardEffect(0, '')
                SLOT_54 = 2
            else:
                DamageEffect(8, '')
                GuardEffect(8, '')

        def upon_OPPONENT_HIT():
            SLOT_31 = SLOT_31 - 20
    if SLOT_59 == 3:
        sendToLabel(300)
        callSubroutine('DrillAttackData3')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_53 = 1
            SLOT_31 = SLOT_31 + 70
            ScreenShake(1500, 1500)
            if CurrentStateCheck('NmlAtkAIR5D'):
                YAccel(90)
            SLOT_54 = SLOT_54 + -1
            if SLOT_54 <= 0:
                DamageEffect(0, '')
                GuardEffect(0, '')
                SLOT_54 = 3
            else:
                DamageEffect(8, '')
                GuardEffect(8, '')

        def upon_OPPONENT_HIT():
            SLOT_31 = SLOT_31 - 20


@Subroutine
def DrillCheck():
    if SLOT_57:
        if op(15, 2, 59, 0, 0):
            SLOT_60 = 67
            SLOT_31 = SLOT_31 + SLOT_2
        if SLOT_31 >= 6000:
            callSubroutine('DrillLevelUp')
        if SLOT_52 >= 3:

            def upon_RELEASE_D():
                sendToLabel(1)
            SpecialCancel(1)
        if SLOT_52 == 15:
            sendToLabel(1)


@Subroutine
def AtkC_Damage2nd():

    def upon_OPPONENT_HIT():
        AddActionMark(1)

    def upon_EVERY_FRAME():
        if not SLOT_81:
            if SLOT_2 >= 1:
                clearUponHandler(EVERY_FRAME)
                DamageMultiplier(30)


@Subroutine
def MatchInit2():
    SLOT_59 = 1


@Subroutine
def OnFrameStep():
    if SLOT_21:
        if not SLOT_81:
            if SLOT_60 < 62:
                if not SLOT_6:
                    if not SLOT_57:
                        if not SLOT_61:
                            if SLOT_59:
                                if SLOT_60:
                                    SLOT_60 = SLOT_60 + -1
                                    if SLOT_59 == 3:
                                        SLOT_31 = SLOT_31 + -10
                                elif SLOT_59 == 3:
                                    SLOT_31 = SLOT_31 + -20
                                else:
                                    SLOT_31 = SLOT_31 + -5
                            elif SLOT_59 == 0:
                                SLOT_31 = SLOT_31 + -50
                            callSubroutine('DrillLevelDown')
            else:
                SLOT_60 = SLOT_60 + -1
            if SLOT_OverdriveTimer:
                if not SLOT_57:
                    if not SLOT_61:
                        if op(15, 2, 59, 0, 0):
                            SLOT_60 = 67
                            if not CurrentStateCheck('NmlAtkGuardCrush'):
                                SLOT_31 = SLOT_31 + SLOT_2
                        if SLOT_31 >= 6000:
                            if SLOT_59 == 1:
                                SLOT_31 = 0
                                SLOT_59 = 2
                            elif SLOT_59 == 2:
                                SLOT_31 = 0
                                SLOT_59 = 3
                            elif SLOT_59 == 3:
                                SLOT_31 = 6000
                                SLOT_59 = 0
                                SLOT_60 = 0
                            callSubroutine('ExGageUpDate')
                        if op(15, 2, 59, 0, 0):
                            if not SLOT_59 == 3:
                                SLOT_31 = SLOT_31 + 50
                            else:
                                SLOT_31 = SLOT_31 + -30
    if not SLOT_81:
        callSubroutine('DrillCheck')


@Subroutine
def OnFinalize():
    ExtendCollisionX(0)


@Subroutine
def OnLanding():
    SLOT_5 = 0


@Subroutine
def OnDamage():
    if SLOT_IsGrounded:
        SLOT_5 = 0


@State
def CmnActStand():
    label(0)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('am001_00', 6)
    SLOT_88 = 960
    SmartVoiceline('am000')
    sprite('am001_01', 7)
    sprite('am001_02', 7)
    sprite('am001_03', 7)
    sprite('am001_04', 27)
    sprite('am001_05', 7)
    sprite('am001_06', 7)
    sprite('am001_07', 7)
    sprite('am001_08', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('am003_01ex', 3)
    SmartVoiceline('am001')
    sprite('am003_00', 3)
    sprite('am003_01', 3)


@State
def CmnActStand2Crouch():
    sprite('am010_00', 4)
    sprite('am010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('am010_02', 8)
    sprite('am010_03', 8)
    sprite('am010_04', 8)
    sprite('am010_05', 8)
    sprite('am010_06', 8)
    sprite('am010_07', 8)
    sprite('am010_08', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('am013_01ex', 3)
    sprite('am013_00', 3)
    sprite('am013_01', 3)


@State
def CmnActCrouch2Stand():
    sprite('am010_01', 4)
    sprite('am010_00', 4)


@State
def CmnActJumpPre():
    sprite('am023_00', 2)
    sprite('am023_01', 2)


@State
def CmnActJumpUpper():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('am020_00', 4)
    sprite('am020_01', 4)
    SmartVoiceline('am002')
    gotoLabel(0)
    label(1)
    sprite('am020_00', 4)
    sprite('am020_01', 4)
    SmartVoiceline('am002')
    gotoLabel(0)
    label(2)
    sprite('am020_00', 4)
    sprite('am020_01', 4)
    SmartVoiceline('am003')
    gotoLabel(0)
    label(0)
    sprite('am020_00', 4)
    sprite('am020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('am020_02', 3)
    sprite('am020_03', 3)
    sprite('am020_04', 3)


@State
def CmnActJumpDown():
    sprite('am020_05', 3)
    sprite('am020_06', 3)
    label(0)
    sprite('am020_07', 4)
    sprite('am020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('am024_00', 3)
    sprite('am024_01', 3)
    sprite('am024_02', 3)
    sprite('am024_03', 3)
    sprite('am024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('am024_00', 2)
    sprite('am024_01', 2)
    sprite('am024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('am024_03', 3)
    sprite('am024_04', 3)


@State
def CmnActFWalk():
    sprite('am030_00', 7)
    label(0)
    sprite('am030_01', 7)
    sprite('am030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('am031_00', 7)
    label(0)
    sprite('am031_01', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am031_02', 7)
    sprite('am031_03', 7)
    sprite('am031_04', 7)
    sprite('am031_05', 7)
    sprite('am031_06', 7)
    sprite('am031_07', 7)
    sprite('am031_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am031_09', 7)
    sprite('am031_10', 7)
    sprite('am031_11', 7)
    sprite('am031_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('am032_00', 2)
    label(0)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('am032_08', 3)
    sprite('am032_09', 3)
    sprite('am032_10', 3)
    sprite('am032_11', 3)


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
    sprite('am033_00', 1)
    sprite('am033_01', 3)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1200)
    JumpSoundEffects()
    SmartVoiceline('am005')
    sprite('am033_02', 3)
    sprite('am033_03', 3)
    setInvincible(0)
    label(0)
    sprite('am033_04', 3)
    sprite('am033_02', 3)
    sprite('am033_03', 3)
    sprite('am033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('am033_05', 3)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('am033_06', 3)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('am035_00', 3)
    label(0)
    sprite('am035_01', 3)
    sprite('am035_02', 3)
    sprite('am035_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('am036_00', 3)
    label(0)
    sprite('am036_01', 3)
    sprite('am036_02', 3)
    sprite('am036_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('am050_00', 1)
    sprite('am050_01', 1)
    sprite('am050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('am050_01', 1)
    sprite('am050_02', 1)
    sprite('am050_01', 2)
    sprite('am050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('am050_02', 1)
    sprite('am050_03', 1)
    sprite('am050_02', 2)
    sprite('am050_01', 2)
    sprite('am050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('am050_03', 1)
    sprite('am050_04', 1)
    sprite('am050_03', 2)
    sprite('am050_02', 2)
    sprite('am050_01', 2)
    sprite('am050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('am050_04', 1)
    sprite('am050_04', 1)
    sprite('am050_04', 2)
    sprite('am050_03', 2)
    sprite('am050_02', 2)
    sprite('am050_01', 2)
    sprite('am050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('am052_00', 1)
    sprite('am052_01', 1)
    sprite('am052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('am052_01', 1)
    sprite('am052_02', 1)
    sprite('am052_01', 2)
    sprite('am052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('am052_02', 1)
    sprite('am052_03', 1)
    sprite('am052_02', 2)
    sprite('am052_01', 2)
    sprite('am052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('am052_03', 1)
    sprite('am052_04', 1)
    sprite('am052_03', 2)
    sprite('am052_02', 2)
    sprite('am052_01', 2)
    sprite('am052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('am052_04', 1)
    sprite('am052_04', 1)
    sprite('am052_04', 2)
    sprite('am052_03', 2)
    sprite('am052_02', 2)
    sprite('am052_01', 2)
    sprite('am052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('am054_00', 1)
    sprite('am054_01', 1)
    sprite('am054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('am054_01', 1)
    sprite('am054_02', 1)
    sprite('am054_01', 2)
    sprite('am054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('am054_02', 1)
    sprite('am054_03', 1)
    sprite('am054_02', 2)
    sprite('am054_01', 2)
    sprite('am054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('am054_03', 1)
    sprite('am054_04', 1)
    sprite('am054_03', 2)
    sprite('am054_02', 2)
    sprite('am054_01', 2)
    sprite('am054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('am054_04', 1)
    sprite('am054_04', 1)
    sprite('am054_04', 2)
    sprite('am054_03', 2)
    sprite('am054_02', 2)
    sprite('am054_01', 2)
    sprite('am054_00', 2)


@State
def CmnActBDownUpper():
    sprite('am060_00', 4)
    label(0)
    sprite('am060_01', 4)
    sprite('am060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('am060_03', 4)


@State
def CmnActBDownDown():
    sprite('am060_04', 4)
    label(0)
    sprite('am060_05', 4)
    sprite('am060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('am060_07', 2)
    sprite('am060_08', 2)


@State
def CmnActBDownBound():
    sprite('am060_09', 3)
    sprite('am060_10', 3)
    sprite('am060_11', 3)
    sprite('am060_12', 3)
    sprite('am060_13', 3)


@State
def CmnActBDownLoop():
    sprite('am060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('am061_00', 3)
    sprite('am061_01', 3)
    sprite('am061_02', 3)
    sprite('am061_03', 3)
    sprite('am061_04', 3)
    sprite('am061_05', 3)
    sprite('am061_06', 2)
    sprite('am061_07', 2)
    sprite('am061_08', 2)


@State
def CmnActFDownUpper():
    sprite('am063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('am063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('am063_02', 3)
    sprite('am063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('am063_04', 3)
    sprite('am063_05', 3)


@State
def CmnActFDownBound():
    sprite('am063_06', 2)
    sprite('am063_07', 2)
    sprite('am063_08', 3)
    sprite('am063_09', 3)
    sprite('am063_10', 3)


@State
def CmnActFDownLoop():
    sprite('am063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('am064_00', 2)
    sprite('am064_01', 2)
    sprite('am064_02', 2)
    sprite('am064_03', 2)
    sprite('am064_04', 2)
    sprite('am064_05', 2)
    sprite('am064_06', 2)
    sprite('am064_07', 2)


@State
def CmnActVDownUpper():
    sprite('am062_00', 3)
    label(0)
    sprite('am062_01', 3)
    sprite('am062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('am062_03', 3)
    sprite('am062_04', 3)


@State
def CmnActVDownDown():
    sprite('am062_05', 3)
    sprite('am062_06', 3)
    label(0)
    sprite('am062_07', 3)
    sprite('am062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('am062_09', 2)
    sprite('am062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('am062_09', 2)
    sprite('am062_10', 2)


@State
def CmnActBlowoff():
    sprite('am072_00', 3)
    sprite('am072_01', 3)
    sprite('am072_02', 3)
    label(0)
    sprite('am072_01', 3)
    sprite('am072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('am074_00', 3)
    sprite('am074_01', 3)
    sprite('am074_02', 3)
    sprite('am074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('am082_00', 2)
    sprite('am082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('am071_04', 1)


@State
def CmnActWallBound():
    sprite('am073_00', 3)
    sprite('am073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('am073_02', 3)
    label(0)
    sprite('am073_03', 3)
    sprite('am073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('am070_00', 4)
    sprite('am070_01', 3)
    sprite('am070_02', 3)
    sprite('am070_03', 3)


@State
def CmnActStaggerDown():
    sprite('am070_04', 4)
    sprite('am070_05', 4)
    sprite('am070_06', 4)
    sprite('am070_07', 4)
    sprite('am070_08', 4)
    sprite('am070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('am070_11', 2)
    sprite('am070_12', 3)
    sprite('am070_13', 3)


@State
def CmnActUkemiAirF():
    sprite('am113_00', 3)
    sprite('am113_01', 3)
    sprite('am113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('am113_00', 3)
    sprite('am113_01', 3)
    sprite('am113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('am113_00', 3)
    sprite('am113_01', 3)
    sprite('am113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('am110_00', 2)
    sprite('am110_01', 2)
    sprite('am110_02', 2)
    sprite('am110_03', 2)
    sprite('am110_04', 2)
    sprite('am110_06', 2)
    sprite('am110_07', 2)
    sprite('am110_08', 200)
    sprite('am110_09', 3)
    sprite('am110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('am111_00', 3)
    sprite('am111_01', 3)
    sprite('am111_02', 3)
    sprite('am111_03', 3)
    sprite('am111_04', 3)
    sprite('am111_06', 3)
    sprite('am111_07', 200)
    sprite('am111_08', 2)
    sprite('am111_09', 2)
    sprite('am111_10', 2)


@State
def CmnActUkemiLandN():
    sprite('am112_00', 2)
    sprite('am112_01', 2)
    sprite('am112_02', 2)
    sprite('am112_03', 2)
    sprite('am112_04', 2)
    sprite('am112_05', 2)
    sprite('am112_06', 2)
    sprite('am112_07', 2)
    sprite('am112_08', 2)
    sprite('am112_09', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('am024_00', 3)
    sprite('am024_01', 3)
    sprite('am024_02', 3)
    sprite('am024_03', 3)
    sprite('am024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('am040_00', 3)
    sprite('am040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('am040_02', 3)
    sprite('am040_03', 3)
    sprite('am040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('am040_01', 3)
    sprite('am040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('am040_05', 3)
    label(0)
    sprite('am040_02', 3)
    sprite('am040_03', 3)
    sprite('am040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('am040_01', 3)
    sprite('am040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('am041_00', 3)
    sprite('am041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('am041_02', 3)
    sprite('am041_03', 3)
    sprite('am041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('am041_01', 3)
    sprite('am041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('am041_05', 3)
    label(0)
    sprite('am041_02', 3)
    sprite('am041_03', 3)
    sprite('am041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('am041_01', 3)
    sprite('am041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('am043_00', 3)
    sprite('am043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('am043_02', 3)
    sprite('am043_03', 3)
    sprite('am043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('am043_01', 3)
    sprite('am043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('am043_05', 3)
    label(0)
    sprite('am043_02', 3)
    sprite('am043_03', 3)
    sprite('am043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('am043_01', 3)
    sprite('am043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('am045_00', 3)
    sprite('am045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('am045_02', 3)
    sprite('am045_03', 3)
    sprite('am045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('am045_01', 3)
    sprite('am045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('am045_05', 3)
    label(0)
    sprite('am045_02', 3)
    sprite('am045_03', 3)
    sprite('am045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('am045_01', 3)
    sprite('am045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('am090_00', 2)
    sprite('am090_01', 2)
    sprite('am090_02', 1)
    SetCommonActionMark(1)
    sprite('am090_03', 6)
    sprite('am090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('am091_00', 2)
    sprite('am091_01', 2)
    sprite('am091_02', 1)
    SetCommonActionMark(1)
    sprite('am091_03', 6)
    sprite('am091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('am092_00', 2)
    sprite('am092_01', 2)
    sprite('am092_02', 1)
    SetCommonActionMark(1)
    sprite('am092_03', 6)
    sprite('am092_04', 6)


@State
def CmnActAirTurn():
    sprite('am025_01ex', 4)
    sprite('am025_00', 4)
    sprite('am025_01', 4)


@State
def CmnActLockWait():
    sprite('am040_02', 1)
    sprite('am040_01', 3)
    sprite('am040_00', 3)


@State
def CmnActLockReject():
    sprite('am312_00', 3)
    sprite('am312_01', 3)
    sprite('am312_02', 3)
    sprite('am312_03', 3)
    sprite('am312_04', 3)
    sprite('am312_05', 3)
    sprite('am312_06', 3)
    sprite('am312_07', 3)
    sprite('am312_08', 3)
    sprite('am312_09', 3)


@State
def CmnActAirLockWait():
    sprite('am045_02', 1)
    sprite('am045_01', 3)
    sprite('am045_00', 3)


@State
def CmnActAirLockReject():
    sprite('am322_00', 3)
    sprite('am322_01', 3)
    sprite('am322_02', 3)
    sprite('am322_03', 3)
    sprite('am322_04', 3)
    sprite('am322_05', 3)
    sprite('am322_06', 3)
    sprite('am322_07', 3)
    sprite('am322_08', 3)
    sprite('am322_09', 3)


@State
def CmnActLandSpin():
    sprite('am071_00', 4)
    sprite('am071_01', 4)
    label(0)
    sprite('am071_02', 2)
    sprite('am071_03', 2)
    sprite('am071_04', 2)
    sprite('am071_05', 2)
    sprite('am071_06', 2)
    sprite('am071_07', 2)
    sprite('am071_08', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('am071_09', 4)
    sprite('am071_10', 4)
    sprite('am071_11', 4)
    sprite('am071_12', 4)


@State
def CmnActVertSpin():
    label(0)
    sprite('am071_02', 2)
    sprite('am071_03', 2)
    sprite('am071_04', 2)
    sprite('am071_05', 2)
    sprite('am071_06', 2)
    sprite('am071_07', 2)
    sprite('am071_08', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('am077_00', 2)
    sprite('am077_01', 2)
    sprite('am077_00ex01', 2)
    sprite('am077_01ex01', 2)
    sprite('am077_00ex02', 2)
    sprite('am077_01ex02', 2)
    sprite('am077_00ex03', 2)
    sprite('am077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('am077_02', 4)
    label(0)
    sprite('am077_03', 3)
    sprite('am077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('am077_05', 5)
    sprite('am077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('am060_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('am060_11', 4)
    sprite('am060_13', 5)


@State
def CmnActBurstBegin():
    sprite('am331_00', 2)
    sprite('am331_01', 2)
    label(0)
    sprite('am331_02', 3)
    sprite('am331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('am331_04', 2)
    sprite('am331_05', 2)
    label(0)
    sprite('am331_06', 3)
    sprite('am331_07', 3)
    sprite('am331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('am331_09', 3)
    sprite('am331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('am331_11', 2)
    sprite('am331_12', 2)
    label(0)
    sprite('am331_02', 3)
    sprite('am331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('am331_04', 2)
    sprite('am331_05', 2)
    label(0)
    sprite('am331_06', 3)
    sprite('am331_07', 3)
    sprite('am331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('am331_13', 3)
    sprite('am331_14', 3)
    label(0)
    sprite('am020_07', 4)
    sprite('am020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('am333_00', 3)
    sprite('am333_01', 3)
    sprite('am333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('am333_03', 32767)
    CreateObject('EMB_AM_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('am333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('am333_05', 3)
    sprite('am333_06', 3)
    sprite('am333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('am333_08', 3)
    sprite('am333_09', 3)
    sprite('am333_10', 3)
    sprite('am333_11', 3)


@State
def CmnActAirOverDriveBegin():
    sprite('am333_12', 3)
    sprite('am333_13', 3)
    sprite('am333_14', 3)
    CharacterFlash(16639, 20, 1)
    sprite('am333_15', 32767)
    CreateObject('EMB_AM_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('am333_16', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('am333_05', 3)
    sprite('am333_06', 3)
    sprite('am333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('am333_08', 3)
    sprite('am333_09', 3)
    sprite('am333_17', 3)
    sprite('am333_18', 3)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        SingleProration(1)
        StarterRating(2)
        WhiffCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
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
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('am200_00', 2)
    PerInertia(60)
    sprite('am200_01', 1)
    sprite('am200_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am200_03', 3)
    sprite('am200_04', 2)
    sprite('am200_05', 2)
    CommonSE('003_swing_grap_0_0')
    sprite('am200_06', 1)
    RefreshMultihit()

    def upon_45():
        HitOrBlockCancel('NmlAtk5A')
    sprite('am200_06', 2)
    WhiffCancelEnable(1)
    sprite('am200_01', 5)
    Recovery()
    Unknown2063()
    sprite('am200_00', 4)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(280)
        Hitstop(3)
        PushbackX(26000)
        AirPushbackY(16000)
        AirPushbackX(26000)
        AirUntechableTime(23)
        SingleProration(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4C')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk1C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('am201_00', 2)
    sprite('am201_01', 2)
    sprite('am201_02', 2)
    sprite('am201_03', 2)
    sprite('am201_04', 2)
    CommonSE('004_swing_grap_1_0')
    RandomCommonVoiceline(1)
    sprite('am201_05', 2)
    sprite('am201_06', 2)
    RefreshMultihit()
    sprite('am201_07', 2)
    RefreshMultihit()
    Hitstop(7)
    sprite('am201_08', 2)
    Recovery()
    Unknown2063()
    sprite('am201_09', 3)
    sprite('am201_10', 3)
    sprite('am201_11', 3)
    sprite('am201_12', 3)
    sprite('am201_13', 3)
    sprite('am201_14', 3)
    sprite('am201_15', 3)
    sprite('am201_16', 2)


@State
def NmlAtk4C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AirHitstunAnimation(11)
        AirUntechableTime(28)
        PushbackX(-19800)
        AirPushbackX(-2000)
        HitAirUnblockable(0)
        CrouchWhiff(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk1C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am202_00', 1)
    sprite('am202_01', 1)
    sprite('am202_02', 2)
    sprite('am202_03', 2)
    sprite('am202_04', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am106', 100, '', 0)
    sprite('am202_05', 2)
    CommonSE('010_swing_sword_2')
    sprite('am202_06', 2)
    CreateObject('202_Particle', 0)
    sprite('am202_07', 2)
    CreateObject('202_Particle', 0)
    CreateObject('202_Particle', 1)
    sprite('am202_08ex01', 2)
    sprite('am202_09ex01', 2)
    sprite('am202_10ex01', 4)
    sprite('am202_11ex01', 2)
    AttackOff()
    sprite('am202_12', 3)
    Recovery()
    Unknown2063()
    sprite('am202_13', 3)
    sprite('am202_14', 3)
    sprite('am202_15', 3)
    sprite('am202_16', 3)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirHitstunAnimation(11)
        AirUntechableTime(28)
        PushbackX(-28000)
        AirPushbackX(-5500)
        HitAirUnblockable(0)
        SingleProration(1)
        CrouchWhiff(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk1C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        if SLOT_94:
            SpecialCancel(0)
        callSubroutine('AtkC_Damage2nd')
    sprite('am202_00', 2)
    sprite('am202_01', 2)
    sprite('am202_02', 2)
    sprite('am202_03', 2)
    sprite('am202_04', 3)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am106', 100, '', 0)
    sprite('am202_05', 2)
    CommonSE('010_swing_sword_2')
    sprite('am202_06', 2)
    CreateObject('202_Particle', 0)
    sprite('am202_07', 2)
    CreateObject('202_Particle', 0)
    CreateObject('202_Particle', 1)
    sprite('am202_08', 2)
    CreateObject('202_Particle', 0)
    sprite('am202_09', 2)
    sprite('am202_10', 4)
    sprite('am202_11', 2)
    GroundedHitstunAnimation(2)
    Stagger(45)
    RefreshMultihit()

    def upon_OPPONENT_HIT_OR_BLOCK():
        if SLOT_94:
            SpecialCancel(1)
    sprite('am202_12', 3)
    Recovery()
    Unknown2063()
    sprite('am202_13', 3)
    sprite('am202_14', 3)
    sprite('am202_15', 3)
    sprite('am202_16', 3)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Damage(120)
        AirHitstunAnimation(19)
        CHCrumple(24)
        AirPushbackX(30000)
        AirPushbackY(6000)
        AirUntechableTime(24)
        HitAirUnblockable(0)
        EnemyHitstopAddition(1, 1, 0)
        UseSlashHitspark(1)
        AttackDirection(2)
        SpecialCancel(0)
        ParticleColorFromPalette(226, 226, 226)
        FatalCounter(1)

        def upon_EVERY_FRAME():
            SLOT_53 = SLOT_53 + -1
            if not SLOT_53:
                RefreshMultihit()
    sprite('am203_00', 2)
    physicsXImpulse(5000)
    sprite('am203_01', 2)
    sprite('am203_02', 2)
    sprite('am203_03', 2)
    sprite('am203_04', 2)
    SmartRandomVoiceline('am108', 100, 'am109', 100, '', 0, '', 0)
    sprite('am203_05', 2)
    SetXCollisionFromOrigin(200)
    AddX(100000)
    physicsXImpulse(29500)
    sprite('am203_07', 1)
    sprite('am203_07', 1)
    callSubroutine('DrillActionJump')
    CHGroundedHitstunAnimation(2)
    CHCrumple(40)
    CreateObject('203_drill', 0)
    SLOT_57 = 1
    label(100)
    TriggerUponForState('203_drill', 33)
    sprite('am203_08', 2)
    XImpulseAcceleration(30)
    CreateObject('D_tornado', 0)
    CreateObject('D_tornado2', 1)
    CreateObject('D_tornado3', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    label(101)
    sprite('am203_09', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_10', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_08', 2)
    XImpulseAcceleration(30)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(101)
    label(200)
    TriggerUponForState('203_drill', 34)
    AirPushbackX(33000)
    AirUntechableTime(26)
    sprite('am203_08', 2)
    XImpulseAcceleration(40)
    CreateObject('D_lv2_tornado', 0)
    CreateObject('D_lv2_tornado2', 1)
    CreateObject('D_lv2_tornado3', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    label(201)
    sprite('am203_09', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_10', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_08', 2)
    XImpulseAcceleration(40)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(201)
    label(300)
    TriggerUponForState('203_drill', 35)
    AirPushbackX(36000)
    AirUntechableTime(28)
    sprite('am203_08', 2)
    XImpulseAcceleration(50)
    CreateObject('D_lv3_tornado', 0)
    CreateObject('D_lv3_tornado2', 1)
    CreateObject('D_lv3_tornado3', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    label(301)
    sprite('am203_09', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_10', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am203_08', 2)
    XImpulseAcceleration(50)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(301)
    label(1)
    sprite('keep', 1)
    SLOT_57 = 0
    RefreshMultihit()
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    DespawnEAEffect('D_tornado')
    DespawnEAEffect('D_tornado2')
    DespawnEAEffect('D_tornado3')
    DespawnEAEffect('D_lv2_tornado')
    DespawnEAEffect('D_lv2_tornado2')
    DespawnEAEffect('D_lv2_tornado3')
    DespawnEAEffect('D_lv3_tornado')
    DespawnEAEffect('D_lv3_tornado2')
    DespawnEAEffect('D_lv3_tornado3')
    sprite('am203_11', 3)
    SetXCollisionFromOrigin(-1)
    physicsXImpulse(0)
    SetActionMark(0)
    Recovery()
    AttackOff()
    Unknown2063()
    CreateParticle('amef_5D_end', 0)
    TriggerUponForState('203_drill', 32)
    sprite('am203_12', 3)
    sprite('am203_13', 3)
    sprite('am203_14', 3)
    CommonSE('019_cloth_a')
    sprite('am203_15', 3)
    sprite('am203_16', 3)
    sprite('am203_17', 3)
    sprite('am203_18', 2)
    sprite('am203_19', 2)
    loopRest()


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Damage(300)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('Atk2A2nd')
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
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('am230_00', 2)
    PerInertia(60)
    sprite('am230_01', 2)
    sprite('am230_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am230_03', 1)
    sprite('am230_03', 2)
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A2nd')
    sprite('am230_04', 4)
    Recovery()
    Unknown2063()
    sprite('am230_07', 5)
    WhiffCancelEnable(0)


@State
def Atk2A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Damage(300)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('Atk2A3rd')
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
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('am230_04', 2)
    sprite('am230_05', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am230_06', 1)
    sprite('am230_06', 2)
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A3rd')
    sprite('am230_01', 4)
    Recovery()
    Unknown2063()
    sprite('am230_00', 5)
    WhiffCancelEnable(0)


@State
def Atk2A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Damage(300)
        SingleProration(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
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
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('am230_01', 2)
    sprite('am230_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am230_03', 3)
    sprite('am230_04', 2)
    sprite('am230_05', 2)
    CommonSE('003_swing_grap_0_0')
    sprite('am230_06', 3)
    RefreshMultihit()
    sprite('am230_06', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('am230_01', 3)
    sprite('am230_00', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(540)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4C')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk1C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('am235_00', 2)
    sprite('am235_01', 2)
    RandomCommonVoiceline(1)
    sprite('am235_02', 2)
    sprite('am235_03', 1)
    sprite('am235_04', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('am235_05', 3)
    sprite('am235_06', 3)
    Recovery()
    Unknown2063()
    sprite('am235_07', 2)
    sprite('am235_08', 2)
    sprite('am235_09', 2)
    sprite('am235_10', 2)
    sprite('am235_11', 2)
    sprite('am235_12', 2)
    sprite('am235_13', 2)
    sprite('am235_14', 2)


@State
def NmlAtk1C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(90)
        HitLow(2)
        HitAirUnblockable(0)
        AirHitstunAnimation(10)
        AirUntechableTime(28)
        PushbackX(-19800)
        AirPushbackX(-2000)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk4C')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am232_00', 2)
    sprite('am232_01', 2)
    sprite('am232_02', 2)
    sprite('am232_03', 2)
    sprite('am232_04', 1)
    sprite('am232_05', 1)
    sprite('am232_06', 1)
    CreateObject('232_Particle', 0)
    sprite('am232_07', 1)
    CreateObject('232_Particle', 0)
    sprite('am232_08ex01', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am106', 100, 'am107', 100
        )
    sprite('am232_09ex01', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('232_Particle', 0)
    sprite('am232_10ex01', 2)
    sprite('am232_11ex01', 4)
    sprite('am232_12ex01', 2)
    AttackOff()
    sprite('am232_13', 3)
    Recovery()
    Unknown2063()
    sprite('am232_14', 4)
    sprite('am232_15', 4)
    sprite('am232_16', 4)
    sprite('am232_17', 4)
    sprite('am232_18', 4)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        HitLow(2)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(10)
        AirUntechableTime(28)
        PushbackX(-24800)
        AirPushbackX(-2000)
        AirPushbackY(36000)
        HitAirUnblockable(0)
        SingleProration(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk4C')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        if SLOT_94:
            AttackOffOrBlockCancel('NmlAtk6A')
            AttackOffOrBlockCancel('NmlAtk4C')
            AttackOffOrBlockCancel('NmlAtk5C')
            AttackOffOrBlockCancel('NmlAtk3C')
            AttackOffOrBlockCancel('NmlAtk5D')
            AttackOffOrBlockCancel('NmlAtk2D')
            AttackOffOrBlockCancel('NmlAtk6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am232_00', 2)
    sprite('am232_01', 2)
    sprite('am232_02', 2)
    sprite('am232_03', 2)
    sprite('am232_04', 2)
    sprite('am232_05', 2)
    sprite('am232_06', 2)
    CreateObject('232_Particle', 0)
    sprite('am232_07', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am106', 100, 'am107', 100
        )
    CreateObject('232_Particle', 0)
    sprite('am232_08', 2)
    CreateObject('232_Particle', 0)
    sprite('am232_09', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('232_Particle', 0)
    sprite('am232_10', 2)
    sprite('am232_11', 4)
    sprite('am232_12', 1)
    PushbackX(-14800)
    AirPushbackX(-2000)
    AirPushbackY(36000)
    RefreshMultihit()
    HitLow(0)
    sprite('am232_12', 1)
    if SLOT_94:
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk4C')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('am232_13', 3)
    Recovery()
    Unknown2063()
    sprite('am232_14', 4)
    sprite('am232_15', 4)
    sprite('am232_16', 4)
    sprite('am232_17', 4)
    sprite('am232_18', 4)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP2(82)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(16000)
        AirUntechableTime(40)
        CHHardKnockdown(1)
        StayAfterMovement(1, 0)
    sprite('am231_00', 1)
    sprite('am231_01', 2)
    sprite('am231_02', 2)
    sprite('am231_03', 2)
    sprite('am231_04', 2)
    physicsXImpulse(3000)
    AddInertia(5000)
    sprite('am231_05', 2)
    XImpulseAcceleration(200)
    RandomCommonVoiceline(1)
    sprite('am231_06', 2)
    XImpulseAcceleration(200)
    CommonSE('003_swing_grap_0_1')
    sprite('am231_07', 4)
    sprite('am231_08', 3)
    Recovery()
    Unknown2063()
    XImpulseAcceleration(80)
    sprite('am231_09', 3)
    XImpulseAcceleration(80)
    sprite('am231_10', 3)
    XImpulseAcceleration(80)
    sprite('am231_11', 3)
    XImpulseAcceleration(0)
    sprite('am231_12', 3)
    sprite('am231_13', 3)
    sprite('am231_14', 3)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Damage(140)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(27000)
        AirUntechableTime(30)
        HitAirUnblockable(0)
        EnemyHitstopAddition(1, 1, 0)
        UseSlashHitspark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        AttackDirection(2)
        Wallbounce(1)
        WallbounceReboundTime(10)
        NonCornerWallbounce(1)
        SpecialCancel(0)
        ParticleColorFromPalette(226, 226, 226)

        def upon_EVERY_FRAME():
            SLOT_53 = SLOT_53 + -1
            if not SLOT_53:
                RefreshMultihit()
    sprite('am233_00', 1)
    sprite('am233_01', 1)
    sprite('am233_02', 2)
    sprite('am233_03', 2)
    sprite('am233_04', 2)
    SmartRandomVoiceline('am108', 100, 'am109', 100, '', 0, '', 0)
    sprite('am233_05', 2)
    sprite('am233_06', 1)
    sprite('am233_06', 1)
    callSubroutine('DrillActionJump')
    CreateObject('233_drill', 0)
    SLOT_57 = 1
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    label(100)
    TriggerUponForState('233_drill', 33)
    sprite('am233_07', 2)
    CreateObject('2D_tornado', 0)
    CreateObject('2D_tornado2', 1)
    CreateObject('2D_tornado3', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    label(101)
    sprite('am233_08', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_09', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_07', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(101)
    label(200)
    TriggerUponForState('233_drill', 34)
    AirUntechableTime(34)
    AirPushbackX(9600)
    AirPushbackY(32400)
    sprite('am233_07', 2)
    CreateObject('2D_lv2_tornado', 0)
    CreateObject('2D_lv2_tornado2', 1)
    CreateObject('2D_lv2_tornado3', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    label(201)
    sprite('am233_08', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_09', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_07', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(201)
    label(300)
    TriggerUponForState('233_drill', 35)
    AirUntechableTime(38)
    AirPushbackX(12000)
    AirPushbackY(40500)
    sprite('am233_07', 2)
    CreateObject('2D_lv3_tornado', 0)
    CreateObject('2D_lv3_tornado2', 1)
    CreateObject('2D_lv3_tornado3', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    label(301)
    sprite('am233_08', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_09', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am233_07', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(301)
    label(1)
    sprite('keep', 1)
    SLOT_57 = 0
    RefreshMultihit()
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    DespawnEAEffect('2D_tornado')
    DespawnEAEffect('2D_tornado2')
    DespawnEAEffect('2D_tornado3')
    DespawnEAEffect('2D_lv2_tornado')
    DespawnEAEffect('2D_lv2_tornado2')
    DespawnEAEffect('2D_lv2_tornado3')
    DespawnEAEffect('2D_lv3_tornado')
    DespawnEAEffect('2D_lv3_tornado2')
    DespawnEAEffect('2D_lv3_tornado3')
    sprite('am233_10', 3)
    setInvincible(0)
    SetActionMark(0)
    Recovery()
    Unknown2063()
    ParticleRotationAngle(25000)
    CallCustomizableParticle('amef_2D_end', 0)
    TriggerUponForState('233_drill', 32)
    sprite('am233_11', 3)
    sprite('am233_12', 4)
    CommonSE('019_cloth_a')
    sprite('am233_13', 3)
    sprite('am233_14', 3)
    sprite('am233_15', 3)
    sprite('am233_16', 3)
    sprite('am233_17', 3)
    sprite('am233_18', 3)
    loopRest()


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AirUntechableTime(16)
        AirPushbackY(16000)
        SingleProration(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('am250_00', 1)
    sprite('am250_01', 2)
    sprite('am250_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am250_03', 3)
    sprite('am250_04', 2)
    sprite('am250_05', 2)
    CommonSE('003_swing_grap_0_0')
    sprite('am250_06', 1)
    RefreshMultihit()

    def upon_45():
        HitOrBlockCancel('NmlAtkAIR5A')
    sprite('am250_06', 2)
    sprite('am250_01', 5)
    Recovery()
    Unknown2063()
    sprite('am250_00', 4)


@State
def AtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('am250_05', 5)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('am250_06', 3)
    sprite('am250_06', 1)
    sprite('am250_01', 5)
    Recovery()
    Unknown2063()
    sprite('am250_00', 4)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(280)
        AttackP1(80)
        Hitstop(3)
        AirUntechableTime(20)
        AirPushbackY(18000)
        HitOverhead(0)
        SingleProration(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockJumpCancel(1)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        if SLOT_94:
            HitOrBlockJumpCancel(0)
            SpecialCancelOnHit(0)
            ChainCancel(0)
    sprite('am251_00', 2)
    sprite('am251_01', 2)
    sprite('am251_02', 2)
    sprite('am251_03', 2)
    sprite('am251_04', 2)
    RandomCommonVoiceline(0)
    sprite('am251_05', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('am251_06', 2)
    sprite('am251_06', 2)
    RefreshMultihit()
    sprite('am251_07', 3)
    Hitstop(7)
    RefreshMultihit()
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            HitOrBlockJumpCancel(1)
            SpecialCancelOnHit(1)
            ChainCancel(1)
    sprite('am251_08', 4)
    Recovery()
    Unknown2063()
    sprite('am251_09', 4)
    sprite('am251_10', 4)
    sprite('am251_11', 4)
    sprite('am251_12', 4)


@State
def NmlAtkAIR2B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirUntechableTime(36)
        AirPushbackX(2000)
        AirPushbackY(-60000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(40)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        UseSlashHitspark(1)
        HitOverhead(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_51 = 1
            YAccel(50)
    sprite('am254_00', 3)
    sprite('am254_01', 3)
    EndMomentum(1)
    physicsXImpulse(0)
    physicsYImpulse(9000)
    setGravity(900)
    sprite('am254_02', 3)
    sprite('am254_03', 3)
    RandomCommonVoiceline(0)
    sprite('am254_04', 3)
    CommonSE('006_swing_blade_1')
    sprite('am254_05', 3)
    CreateParticle('amef_j2c_skr', 0)
    physicsYImpulse(-28000)
    setGravity(1400)
    sprite('am254_06', 3)
    sprite('am254_07', 3)
    sprite('am254_08', 3)
    if SLOT_51:
        physicsYImpulse(18000)
    Recovery()
    Unknown2063()
    sprite('am254_09', 3)
    sprite('am254_10', 3)
    sprite('am254_11', 3)
    sprite('am254_12', 3)
    sprite('am254_13', 3)
    sprite('am254_14', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        HitOverhead(0)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(11)
        CHGroundedHitstunAnimation(11)
        AirUntechableTime(28)
        PushbackX(-16000)
        SingleProration(1)
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am252_00', 2)
    sprite('am252_01', 1)
    sprite('am252_01', 1)
    XSpeed(-30000)
    YSpeed(20000)
    XImpulseAcceleration(20)
    YAccel(20)
    sprite('am252_02', 2)
    sprite('am252_03', 2)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am252_04', 2)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am252_05', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am107', 100, '', 0)
    EndMomentum(1)
    XImpulseAcceleration(0)
    YAccel(0)
    CreateObject('252_Particle', 0)
    CreateObject('252_Particle', 1)
    sprite('am252_06', 2)
    CreateObject('252_Particle', 0)
    CreateObject('252_Particle', 1)
    sprite('am252_07', 3)
    CommonSE('010_swing_sword_2')
    CreateObject('252_Particle', 0)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setGravity(900)
    sprite('am252_08', 2)
    ForcedLandingRecovery(6, 0)
    AirPushbackX(-8000)
    AirPushbackY(40000)
    sprite('am252_09', 4)
    sprite('am252_10', 2)
    AirPushbackX(-8000)
    AirPushbackY(36000)
    RefreshMultihit()
    sprite('am252_11', 5)
    Recovery()
    Unknown2063()
    GravityDefault()
    sprite('am252_12', 4)
    sprite('am252_13', 4)
    sprite('am252_14', 5)
    sprite('am252_15', 5)
    sprite('am252_16', 5)


@State
def NmlAtkAIR6C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(780)
        AttackP1(80)
        HitOverhead(0)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(19)
        CHGroundedHitstunAnimation(19)
        AirUntechableTime(28)
        PushbackX(-16000)
        SingleProration(1)
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am255_00', 2)
    sprite('am255_01', 1)
    sprite('am255_01', 1)
    XSpeed(-30000)
    YSpeed(20000)
    XImpulseAcceleration(20)
    YAccel(20)
    sprite('am255_02', 2)
    sprite('am255_03', 2)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am255_04', 2)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am255_05', 2)
    XImpulseAcceleration(0)
    YAccel(0)
    CreateObject('255_Particle', 0)
    sprite('am255_06', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am107', 100, '', 0)
    CreateObject('255_Particle', 0)
    sprite('am255_07', 2)
    CreateObject('255_Particle', 0)
    sprite('am255_08', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('255_Particle', 0)
    physicsXImpulse(-15000)
    physicsYImpulse(15000)
    setGravity(900)
    sprite('am255_09', 2)
    ForcedLandingRecovery(6, 0)
    AirPushbackX(-30000)
    AirPushbackY(10000)
    sprite('am255_10', 2)
    XImpulseAcceleration(120)
    GravityDefault()
    sprite('am255_11', 2)
    sprite('am255_12', 2)
    AirPushbackX(-30000)
    AirPushbackY(0)
    RefreshMultihit()
    sprite('am255_13', 4)
    XImpulseAcceleration(50)
    YAccel(125)
    Recovery()
    Unknown2063()
    sprite('am255_14', 4)
    XImpulseAcceleration(50)
    YAccel(125)
    sprite('am255_15', 4)
    YAccel(125)
    sprite('am255_16', 4)
    YAccel(125)
    sprite('am255_17', 4)
    sprite('am255_18', 4)


@State
def NmlAtkAIR4C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        HitOverhead(0)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(10)
        AirUntechableTime(28)
        PushbackX(-16000)
        SingleProration(1)
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR6D')
        callSubroutine('AtkC_Damage2nd')
    sprite('am256_00', 2)
    sprite('am256_01', 1)
    sprite('am256_01', 1)
    XSpeed(-30000)
    YSpeed(40000)
    XImpulseAcceleration(20)
    YAccel(20)
    sprite('am256_02', 2)
    sprite('am256_03', 2)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am256_04', 2)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am107', 100, '', 0)
    XImpulseAcceleration(80)
    YAccel(80)
    sprite('am256_05', 2)
    XImpulseAcceleration(0)
    YAccel(0)
    CreateObject('256_Particle', 0)
    CreateObject('256_Particle', 1)
    sprite('am256_06', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('256_Particle', 0)
    sprite('am256_07', 3)
    CreateObject('256_Particle', 0)
    physicsXImpulse(-3000)
    physicsYImpulse(18000)
    setGravity(900)
    sprite('am256_08', 2)
    ForcedLandingRecovery(6, 0)
    AirPushbackX(-10000)
    AirPushbackY(30000)
    sprite('am256_09', 4)
    YAccel(120)
    sprite('am256_10', 2)
    AirPushbackX(-6000)
    AirPushbackY(40000)
    RefreshMultihit()
    sprite('am256_11', 5)
    GravityDefault()
    Recovery()
    Unknown2063()
    sprite('am256_12', 5)
    sprite('am256_13', 5)
    sprite('am256_14', 5)
    sprite('am256_15', 5)
    sprite('am256_16', 5)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(100)
        AirPushbackX(6000)
        AirPushbackY(-6000)
        HitOverhead(0)
        EnemyHitstopAddition(1, 1, 0)
        UseSlashHitspark(1)
        SpecialCancel(0)
        ParticleColorFromPalette(226, 226, 226)

        def upon_EVERY_FRAME():
            SLOT_53 = SLOT_53 + -1
            if not SLOT_53:
                RefreshMultihit()
    sprite('am253_00', 3)
    sprite('am253_01', 3)
    SmartRandomVoiceline('am108', 100, 'am109', 100, '', 0, '', 0)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('am253_02', 3)
    sprite('am253_03', 2)
    sprite('am253_03', 1)
    callSubroutine('DrillActionJump')
    CHGroundedHitstunAnimation(2)
    CHCrumple(40)
    CreateObject('253_drill', 0)
    ForcedLandingRecovery(10, 1)
    PushCollisionHeightLow(20000)
    SLOT_57 = 1
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(80)
    PerGravity(150)
    label(100)
    TriggerUponForState('253_drill', 33)
    sprite('am253_04', 2)
    CreateObject('amef_airD', 0)
    CreateObject('amef_airD2', 0)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    label(101)
    sprite('am253_05', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_06', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_04', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(101)
    label(200)
    TriggerUponForState('253_drill', 34)
    sprite('am253_04', 2)
    CreateObject('amef_airD', 0)
    CreateObject('amef_airD2', 0)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    label(201)
    sprite('am253_05', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_06', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_04', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(201)
    label(300)
    TriggerUponForState('253_drill', 35)
    sprite('am253_04', 2)
    CreateObject('amef_airD', 0)
    CreateObject('amef_airD2', 0)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    label(301)
    sprite('am253_05', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_06', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am253_04', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(301)
    label(1)
    sprite('keep', 1)
    SLOT_57 = 0
    RefreshMultihit()
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    sprite('am253_07', 3)
    PushCollisionHeightLow(-1)
    SetActionMark(0)
    TriggerUponForState('253_drill', 32)
    DespawnEAEffect('amef_airD')
    DespawnEAEffect('amef_airD2')
    Recovery()
    Unknown2063()
    sprite('am253_08', 3)
    CommonSE('019_cloth_a')
    sprite('am253_09', 3)
    sprite('am253_10', 3)
    sprite('am253_11', 3)
    sprite('am253_12', 3)
    sprite('am253_13', 3)
    sprite('am253_14', 3)
    loopRest()


@State
def NmlAtkAIR6D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Damage(150)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Wallbounce(1)
        AirPushbackX(28000)
        AirPushbackY(32000)
        AirUntechableTime(36)
        EnemyHitstopAddition(1, 1, 0)
        UseSlashHitspark(1)
        AttackDirection(2)
        HitOverhead(0)
        SpecialCancel(0)
        ParticleColorFromPalette(226, 226, 226)

        def upon_EVERY_FRAME():
            SLOT_53 = SLOT_53 + -1
            if not SLOT_53:
                RefreshMultihit()
    sprite('am257_00', 3)
    sprite('am257_01', 3)
    EndMomentum(1)
    SmartRandomVoiceline('am108', 100, 'am109', 100, '', 0, '', 0)
    sprite('am257_02', 2)
    sprite('am257_03', 2)
    sprite('am257_04', 3)
    physicsXImpulse(40000)
    SetXCollisionFromOrigin(200)
    sprite('am257_05', 2)
    physicsXImpulse(30000)
    sprite('am257_05', 1)
    physicsXImpulse(20000)
    callSubroutine('DrillActionJump')
    CreateObject('203_drill', 0)
    SLOT_57 = 1
    label(100)
    TriggerUponForState('203_drill', 33)
    sprite('am257_06', 2)
    XImpulseAcceleration(30)
    CreateObject('Air6D_tornado', 0)
    CreateObject('Air6D_tornado2', 1)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    label(101)
    sprite('am257_07', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_08', 2)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_06', 2)
    XImpulseAcceleration(30)
    PrivateSE('amse_01_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(101)
    label(200)
    TriggerUponForState('203_drill', 34)
    AirPushbackX(30800)
    AirPushbackY(35200)
    Blockstun(20)
    AirUntechableTime(40)
    sprite('am257_06', 2)
    XImpulseAcceleration(40)
    CreateObject('Air6D_lv2_tornado', 0)
    CreateObject('Air6D_lv2_tornado2', 1)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    label(201)
    sprite('am257_07', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_08', 2)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_06', 2)
    XImpulseAcceleration(40)
    PrivateSE('amse_02_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(201)
    label(300)
    TriggerUponForState('203_drill', 35)
    AirPushbackX(33600)
    AirPushbackY(38400)
    Blockstun(22)
    AirUntechableTime(44)
    sprite('am257_06', 2)
    XImpulseAcceleration(50)
    CreateObject('Air6D_lv3_tornado', 0)
    CreateObject('Air6D_lv3_tornado2', 1)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    label(301)
    sprite('am257_07', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_08', 2)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    sprite('am257_06', 2)
    XImpulseAcceleration(50)
    PrivateSE('amse_03_loop')
    SLOT_52 = SLOT_52 + 1
    loopRest()
    gotoLabel(301)
    label(1)
    sprite('keep', 1)
    SLOT_57 = 0
    RefreshMultihit()
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    DespawnEAEffect('Air6D_tornado')
    DespawnEAEffect('Air6D_tornado2')
    DespawnEAEffect('Air6D_lv2_tornado')
    DespawnEAEffect('Air6D_lv2_tornado2')
    DespawnEAEffect('Air6D_lv3_tornado')
    DespawnEAEffect('Air6D_lv3_tornado2')
    sprite('am257_09', 3)
    physicsXImpulse(0)
    physicsYImpulse(6000)
    GravityDefault()
    SetActionMark(0)
    Recovery()
    Unknown2063()
    TriggerUponForState('203_drill', 32)
    CreateParticle('amef_air6D_end', 1)
    SetXCollisionFromOrigin(-1)
    sprite('am257_10', 3)
    sprite('am257_11', 3)
    CommonSE('019_cloth_a')
    sprite('am257_12', 3)
    sprite('am257_13', 3)
    sprite('am257_14', 3)
    sprite('am257_15', 3)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        HitAirUnblockable(3)
        AirPushbackY(36000)
        AirUntechableTime(28)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(10)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
    sprite('am210_00', 2)
    sprite('am210_01', 2)
    sprite('am210_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('am210_03', 2)
    RandomCommonVoiceline(1)
    sprite('am210_04', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('am210_05', 4)
    sprite('am210_06', 3)
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('am210_07', 3)
    sprite('am210_08', 3)
    sprite('am210_09', 3)
    sprite('am210_10', 3)
    sprite('am210_11', 3)
    sprite('am210_12', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(800)
        AttackP1(80)
        BonusProration(110)
        AirPushbackX(36000)
        AirPushbackY(18000)
        Floorslide(15)
        AirUntechableTime(40)
        FatalCounter(1)
        CHAirPushbackX(48000)
        CHAirPushbackY(36000)
        CHWallbounce(1)
        HitAirUnblockable(0)
        MoveAttributes(1, 0, 0, 0, 0)
        SpecialCancel(0)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR6C')
        HitOrBlockCancel('NmlAtkAIR4C')
        HitOrBlockCancel('NmlAtkAIR2C')
    sprite('am211_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 0, 1)
    physicsXImpulse(1000)
    sprite('am211_01', 2)
    sprite('am211_02', 2)
    PerInertia(50)
    physicsYImpulse(7500)
    setGravity(600)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('am211_03', 2)
    sprite('am211_04', 2)
    sprite('am211_05', 2)
    RandomCommonVoiceline(1)
    sprite('am211_06', 2)
    CommonSE('004_swing_grap_1_1')
    CommonSE('019_cloth_a')
    sprite('am211_07', 3)
    sprite('am211_08', 3)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setInvincible(0)
    Recovery()
    sprite('am211_09', 3)
    physicsXImpulse(-12000)
    sprite('am211_10', 3)
    physicsXImpulse(-24000)
    sprite('am211_11', 3)
    Unknown2063()
    XImpulseAcceleration(80)
    sprite('am211_12', 3)
    XImpulseAcceleration(80)
    sprite('am211_13', 3)
    XImpulseAcceleration(60)
    sprite('am211_14', 2)
    XImpulseAcceleration(60)
    sprite('am020_04', 1)
    XImpulseAcceleration(60)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirUntechableTime(35)
        Floorslide(35)
        SingleProration(1)
        PreventGroundedHit(1)
        FatalCounter(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        if SLOT_94:
            ChainCancel(0)
        callSubroutine('AtkC_Damage2nd')
    sprite('am212_00', 2)
    sprite('am212_01', 1)
    sprite('am212_01', 1)
    SmartRandomVoiceline('am104', 100, 'am105', 100, 'am107', 100, '', 0)
    sprite('am212_02', 3)
    sprite('am212_03', 3)
    sprite('am212_04', 2)
    sprite('am212_05', 2)
    sprite('am212_06', 2)
    sprite('am212_07', 2)
    CreateObject('212_Particle', 0)
    sprite('am212_08', 2)
    CreateObject('212_Particle', 0)
    sprite('am212_09', 2)
    CommonSE('006_swing_blade_2')
    CreateObject('212_Particle', 0)
    CreateObject('212_Particle', 1)
    sprite('am212_10', 2)
    AirPushbackX(-20000)
    AirPushbackY(3000)
    sprite('am212_11', 3)
    sprite('am212_12', 3)
    CommonSE('006_swing_blade_2')
    sprite('am212_13', 1)
    AirUntechableTime(38)
    AirPushbackX(-33000)
    RefreshMultihit()
    sprite('am212_13', 3)
    if SLOT_94:
        ChainCancel(1)
    sprite('am212_14', 4)
    Recovery()
    Unknown2063()
    sprite('am212_15', 4)
    sprite('am212_16', 4)
    sprite('am212_17', 4)
    sprite('am212_18', 4)
    sprite('am212_19', 4)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        if SLOT_59 == 0:
            sendToLabel(1)

        def upon_STATE_END():
            TriggerUponForState('6DTop', 35)

        def upon_32():
            clearUponHandler(32)
            SLOT_57 = 1
            callSubroutine('DrillActionJump')
            SetActionMark(60)
            if SLOT_OverdriveTimer:
                SetActionMark(50)

        def upon_34():
            SetActionMark(200)
            if SLOT_OverdriveTimer:
                SetActionMark(50)

        def upon_33():
            sendToLabel(1)
        RunLoopUpon(17, 240)

        def upon_17():
            sendToLabel(1)
    sprite('am213_00', 2)
    sprite('am213_01', 2)
    sprite('am213_02', 3)
    sprite('am213_03', 3)
    sprite('am213_04', 3)
    SmartRandomVoiceline('am108', 100, 'am109', 100, '', 0, '', 0)
    sprite('am213_05', 3)
    sprite('am213_06', 3)
    CreateParticle('amef_6D', 0)
    CreateParticle('amef_6D', 1)
    CommonSE('006_swing_blade_1')
    sprite('am213_07', 3)
    CreateParticle('amef_6D', 0)
    sprite('am213_08', 3)
    sprite('am213_09', 3)
    sprite('am213_10', 3)
    CreateObject('6DTop', 0)
    RegisterObject(4, 1)
    sprite('am213_11', 3)
    sprite('am213_12', 3)
    sprite('am213_13', 3)
    sprite('am213_14', 30)
    label(100)
    sprite('am213_14', 1)
    ObjectUpon(FALLING, 32)
    gotoLabel(100)
    label(200)
    sprite('am213_14', 1)
    ObjectUpon(FALLING, 33)
    gotoLabel(200)
    label(300)
    sprite('am213_14', 1)
    ObjectUpon(FALLING, 34)
    gotoLabel(300)
    label(1)
    sprite('am213_15', 4)
    SLOT_57 = 0
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(34)
    clearUponHandler(17)
    SetActionMark(0)
    ObjectUpon(FALLING, 35)
    sprite('am213_16', 3)
    sprite('am213_17', 3)
    sprite('am213_18', 3)
    sprite('am213_19', 3)
    sprite('am213_20', 3)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('am300_00', 6)
    sprite('am300_01', 6)
    if random_(2, 0, 50):
        Voiceline('am404')
    else:
        Voiceline('am405')
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    sprite('am300_09', 6)
    sprite('am300_10', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('am201_00', 2)
    sprite('am201_01', 2)
    sprite('am201_02', 3)
    sprite('am201_03', 3)
    sprite('am201_04', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('am201_05', 2)
    sprite('am201_06', 2)
    sprite('am201_07', 2)
    sprite('am201_08', 2)
    sprite('am201_09', 3)
    sprite('am201_10', 3)
    sprite('am201_11', 3)
    sprite('am201_12', 3)
    sprite('am201_13', 3)
    sprite('am201_14', 3)
    sprite('am201_15', 3)
    sprite('am201_16', 2)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(18)
        AirPushbackY(38000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(60)
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
    sprite('am402_00', 2)
    sprite('am402_01', 1)
    sprite('am402_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    Voiceline('am159')
    HeatChange(-2500)
    sprite('am402_02', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('am402_03', 2)
    sprite('am402_04', 4)
    label(100)
    sprite('am340_00', 4)
    sprite('am340_01', 4)
    sprite('am402_04', 4)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('am402_06', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('am402_07', 3)
    sprite('am402_08', 3)
    CommonSE('010_swing_sword_2')
    sprite('am340_02', 1)
    sprite('am340_02', 1)
    AttackOff()
    EnableAfterimage(0)
    sprite('am402_10', 2)
    sprite('am402_11', 2)
    sprite('am402_12', 2)
    sprite('am402_13', 2)
    sprite('am402_14', 3)
    CommonSE('019_cloth_b')
    sprite('am402_15', 3)
    sprite('am402_16', 2)
    sprite('am402_17', 2)
    sprite('am402_18', 2)
    sprite('am402_19', 2)
    sprite('am402_20', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('am310_00', 2)
    CommonSE('010_swing_sword_0')
    sprite('am310_01', 4)
    sprite('am310_02', 3)
    sprite('am310_03', 3)
    SmartVoiceline('am155')
    sprite('am310_04', 3)
    sprite('am310_05', 6)
    sprite('am310_06', 4)
    sprite('am310_07', 4)
    sprite('am310_08', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(24000)
        AirPushbackY(40000)
        NonCornerWallbounce(1)
        Wallbounce(1)
        Wallstick(1)
        AirUntechableTime(50)
        Hitstop(3)
        StayAfterMovement(1, 0)
        StarterRating(2)
    sprite('am310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('am311_00', 3)
    SmartVoiceline('am153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_02', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_03', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_04', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_05', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_06', 6)
    OppThrowAnimation(0, 0)
    CreateParticle('amef_throw', 1)
    sprite('am311_07', 5)
    OppThrowAnimation(0, 0)
    sprite('am311_08', 5)
    sprite('am311_09', 6)
    CreateObject('Throw_windmill', 0)
    sprite('am311_10', 5)
    sprite('am311_11', 5)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('am310_00', 2)
    CommonSE('010_swing_sword_0')
    sprite('am310_01', 4)
    sprite('am310_02', 3)
    sprite('am310_03', 3)
    SmartVoiceline('am155')
    sprite('am310_04', 3)
    sprite('am310_05', 6)
    sprite('am310_06', 4)
    sprite('am310_07', 4)
    sprite('am310_08', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(24000)
        AirPushbackY(40000)
        NonCornerWallbounce(1)
        Wallbounce(1)
        Wallstick(1)
        AirUntechableTime(50)
        Hitstop(3)
        StayAfterMovement(1, 0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        SetZLine(1, 50)
        StarterRating(2)
    sprite('am310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('am313_00', 3)
    SmartVoiceline('am153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am313_01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am313_02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 1)
    sprite('am313_03', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am310_02ex01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    Flip()
    sprite('am311_00', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_02', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_04', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_05', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am311_06', 6)
    OppThrowAnimation(0, 0)
    CreateParticle('amef_throw', 1)
    sprite('am311_07', 5)
    OppThrowAnimation(0, 0)
    sprite('am311_08', 5)
    sprite('am311_09', 6)
    CreateObject('Throw_windmill', 0)
    sprite('am311_10', 5)
    sprite('am311_11', 5)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('am320_00', 3)
    sprite('am320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('am320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('am320_03', 4)
    sprite('am320_04', 5)
    SmartVoiceline('am155')
    sprite('am320_05', 5)
    sprite('am320_06', 5)
    sprite('am320_07', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SetZLine(0, 50)
        AttackLevel_(4)
        Damage(750)
        AttackP1(100)
        AttackP2(50)
        SingleProration(1)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(2400)
        AirPushbackY(34000)
        YImpulseBeforeWallbounce(1800)
        Hitstop(0)
        AirUntechableTime(80)
        GroundBounce(1)
        BouncePercentage(50)
        OppMovementUnlock(1)
        StarterRating(2)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        ForcedLandingRecovery(0, 0)
    sprite('am320_02', 5)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('am321_00', 4)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SmartVoiceline('am154')
    sprite('am321_01', 4)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('004_swing_grap_1_1')
    physicsYImpulse(10000)
    sprite('am321_02', 4)
    YAccel(80)
    sprite('am321_03', 4)
    YAccel(50)
    SetZLine(1, 50)
    sprite('am321_04', 4)
    YAccel(0)
    sprite('am321_05', 4)
    sprite('am321_06', 4)
    sprite('am321_07', 4)
    sprite('am321_08', 4)
    sprite('am321_09', 16)
    sprite('am321_10', 2)
    sprite('am321_11', 4)
    RefreshMultihit()
    Hitstop(16)
    AirPushbackY(-45000)
    AirPushbackX(45000)
    Wallbounce(1)
    WallbounceReboundTime(50)
    BouncePercentageReset()
    sprite('am321_12', 4)
    sprite('am321_13', 3)
    sprite('am321_14', 3)
    sprite('am321_15', 3)
    sprite('am321_16', 3)
    sprite('am321_17', 3)
    GravityDefault()
    sprite('am321_18', 3)


@State
def Kamae():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        EndMomentum(1)

        def upon_EVERY_FRAME():
            if op(15, 2, 59, 0, 0):
                SLOT_60 = 67
                SLOT_31 = SLOT_31 + SLOT_2
            if SLOT_31 >= 6000:
                callSubroutine('DrillLevelUp')
            if not SLOT_59:
                sendToLabel(1)
            if SLOT_51:
                if CheckInput(INPUT_PRESS_D):
                    Unknown23170('KamaeStop')
                    sendToLabel(1)
                if SLOT_94:
                    if CheckInput(0x31):
                        Unknown23170('KamaeStop')
                        sendToLabel(1)
        if SLOT_59 == 0:
            sendToLabel(1)
    sprite('am400_00', 2)
    BeginBuffer('GroundDrill_A')
    BeginBuffer('GroundDrill_B')
    BeginBuffer('GroundDrill_C')
    sprite('am400_01', 2)
    Voiceline('am200')
    CallCustomizableParticle('amef_401_charge_start', 0)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    if SLOT_OverdriveTimer:
        SetActionMark(10)
    else:
        SetActionMark(80)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardPoint_(1)
    sprite('am400_02', 1)
    SLOT_51 = 5
    BufferedOrPressedGoto('GroundDrill_A')
    BufferedOrPressedGoto('GroundDrill_B')
    BufferedOrPressedGoto('GroundDrill_C')
    label(0)
    sprite('am400_03', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    CommonSE('019_cloth_b')
    sprite('am400_04', 4)
    sprite('am400_05', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_06', 4)
    sprite('am400_07', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_08', 3)
    sprite('am400_08', 1)
    SLOT_51 = SLOT_51 + -1
    if not SLOT_51:
        notConditionalSendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('am400_02', 4)
    clearUponHandler(EVERY_FRAME)
    setInvincible(0)
    SetActionMark(0)
    DisallowGoto('GroundDrill_A')
    DisallowGoto('GroundDrill_B')
    DisallowGoto('GroundDrill_C')
    Recovery()
    sprite('am400_01', 4)
    sprite('am400_00', 4)


@State
def GroundDrill_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        Floorslide(10)
        AirPushbackX(18000)
        AirPushbackY(-24000)
        GroundBounce(1)
        MoveAttributes(0, 0, 1, 0, 0)
        if SLOT_59 == 0:
            sendToLabel(1)
        SetActionMark(0)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        GuardPoint_(1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('am401_00', 2)
    CallCustomizableParticle('amef_401add2_add2', 0)
    ParticleColorFromPalette(226, 226, 226)
    sprite('am401_01', 1)
    sprite('am401_02', 2)
    sprite('am401_03', 1)
    sprite('am401_04', 1)
    sprite('am401_05', 1)
    sprite('am401_06', 2)
    sprite('am401_07', 1)
    sprite('am401_08', 2)
    setInvincible(0)
    sprite('am401_09', 2)
    sprite('am401_10', 2)
    sprite('am401_11', 2)
    ExtendCollisionX(100)
    sprite('am401_12', 2)
    Voiceline('am201')
    ExtendCollisionX(150)
    clearUponHandler(STATE_END)
    CommonSE('213_bound_0')
    CreateObject('GroundDrill', 0)
    RegisterObject(4, 1)
    if SLOT_59 == 1:
        ObjectUpon(FALLING, 32)
    if SLOT_59 == 2:
        ObjectUpon(FALLING, 33)
    if SLOT_59 == 3:
        ObjectUpon(FALLING, 34)
    label(1)
    sprite('am401_13', 2)
    sprite('am401_14', 3)
    sprite('am401_15', 2)
    sprite('am401_16', 3)
    sprite('am401_17', 3)
    ExtendCollisionX(150)
    sprite('am401_18', 2)
    ExtendCollisionX(100)
    sprite('am401_19', 3)
    ExtendCollisionX(50)
    sprite('am401_20', 2)
    ExtendCollisionX(0)
    sprite('am401_21', 3)
    sprite('am401_22', 2)
    sprite('am401_23', 3)
    sprite('am401_24', 3)


@State
def GroundDrill_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        Floorslide(10)
        AirPushbackX(24000)
        AirPushbackY(-24000)
        GroundBounce(1)
        MoveAttributes(0, 0, 1, 0, 0)
        if SLOT_59 == 0:
            sendToLabel(1)
        SetActionMark(0)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        GuardPoint_(1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('am401_00', 2)
    CallCustomizableParticle('amef_401add2_add2', 0)
    ParticleColorFromPalette(226, 226, 226)
    sprite('am401_01', 1)
    sprite('am401_02', 2)
    sprite('am401_03', 1)
    sprite('am401_04', 1)
    sprite('am401_05', 1)
    sprite('am401_06', 2)
    sprite('am401_07', 1)
    sprite('am401_08', 2)
    setInvincible(0)
    sprite('am401_09', 2)
    sprite('am401_10', 2)
    sprite('am401_11', 2)
    ExtendCollisionX(100)
    sprite('am401_12', 2)
    Voiceline('am201')
    ExtendCollisionX(150)
    clearUponHandler(STATE_END)
    CommonSE('213_bound_0')
    CreateObject('GroundDrill', 1)
    RegisterObject(4, 1)
    if SLOT_59 == 1:
        ObjectUpon(FALLING, 32)
    if SLOT_59 == 2:
        ObjectUpon(FALLING, 33)
    if SLOT_59 == 3:
        ObjectUpon(FALLING, 34)
    label(1)
    sprite('am401_13', 2)
    sprite('am401_14', 3)
    sprite('am401_15', 2)
    sprite('am401_16', 3)
    sprite('am401_17', 3)
    ExtendCollisionX(150)
    sprite('am401_18', 2)
    ExtendCollisionX(100)
    sprite('am401_19', 3)
    ExtendCollisionX(50)
    sprite('am401_20', 2)
    ExtendCollisionX(0)
    sprite('am401_21', 3)
    sprite('am401_22', 2)
    sprite('am401_23', 3)
    sprite('am401_24', 3)


@State
def GroundDrill_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        Floorslide(10)
        AirPushbackX(30000)
        AirPushbackY(-24000)
        GroundBounce(1)
        MoveAttributes(0, 0, 1, 0, 0)
        if SLOT_59 == 0:
            sendToLabel(1)
        SetActionMark(0)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        GuardPoint_(1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('am401_00', 2)
    CallCustomizableParticle('amef_401add2_add2', 0)
    ParticleColorFromPalette(226, 226, 226)
    sprite('am401_01', 1)
    sprite('am401_02', 2)
    sprite('am401_03', 1)
    sprite('am401_04', 1)
    sprite('am401_05', 1)
    sprite('am401_06', 2)
    sprite('am401_07', 1)
    sprite('am401_08', 2)
    setInvincible(0)
    sprite('am401_09', 2)
    sprite('am401_10', 2)
    sprite('am401_11', 2)
    ExtendCollisionX(100)
    sprite('am401_12', 2)
    Voiceline('am201')
    clearUponHandler(STATE_END)
    ExtendCollisionX(150)
    CommonSE('213_bound_0')
    CreateObject('GroundDrill', 2)
    RegisterObject(4, 1)
    if SLOT_59 == 1:
        ObjectUpon(FALLING, 32)
    if SLOT_59 == 2:
        ObjectUpon(FALLING, 33)
    if SLOT_59 == 3:
        ObjectUpon(FALLING, 34)
    label(1)
    sprite('am401_13', 2)
    sprite('am401_14', 3)
    sprite('am401_15', 2)
    sprite('am401_16', 3)
    sprite('am401_17', 3)
    ExtendCollisionX(150)
    sprite('am401_18', 2)
    ExtendCollisionX(100)
    sprite('am401_19', 3)
    ExtendCollisionX(50)
    sprite('am401_20', 2)
    ExtendCollisionX(0)
    sprite('am401_21', 3)
    sprite('am401_22', 2)
    sprite('am401_23', 3)
    sprite('am401_24', 3)


@State
def Anti_Air():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EnableRapidCancel(0)

        def upon_14():
            TriggerUponForState('402_punch', 32)
    sprite('am402_00', 2)
    sprite('am402_01', 2)
    sprite('am402_02', 2)
    sprite('am402_03', 2)
    sprite('am402_04', 2)
    Voiceline('am202')
    sprite('am402_05', 3)
    sprite('am402_06', 2)
    sprite('am402_07', 3)
    CreateObject('402_punch', 100)
    sprite('am402_08', 3)
    CommonSE('010_swing_sword_2')
    sprite('am402_09', 3)
    CreateParticle('amef_402', 0)
    sprite('am402_10', 3)
    sprite('am402_11', 3)
    sprite('am402_12', 3)
    sprite('am402_13', 3)
    sprite('am402_14', 3)
    CommonSE('019_cloth_b')
    sprite('am402_15', 6)
    EnableRapidCancel(1)
    sprite('am402_16', 3)
    sprite('am402_17', 3)
    sprite('am402_18', 3)
    sprite('am402_19', 3)
    sprite('am402_20', 3)


@State
def MultiStrike():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(2)
        Damage(200)
        AttackP2(75)
        AirUntechableTime(30)
        Hitstop(3)
        SingleProration(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('am403_00', 2)
    Voiceline('am203')
    XSpeed(6000)
    sprite('am403_01', 2)
    XImpulseAcceleration(120)
    sprite('am403_02', 2)
    CommonSE('019_cloth_a')
    sprite('am403_03', 3)
    XImpulseAcceleration(150)
    sprite('am403_04', 2)
    XImpulseAcceleration(180)
    sprite('am403_05', 3)
    AirPushbackX(8000)
    AirPushbackY(20000)
    CreateParticle('amef_airmove_skr', 0)
    CommonSE('019_cloth_c')
    sprite('am403_06', 3)
    AirPushbackX(8000)
    AirPushbackY(15000)
    CreateParticle('amef_airmove_skr', 0)
    RefreshMultihit()
    sprite('am403_07', 3)
    AirPushbackX(16000)
    AirPushbackY(10000)
    CreateParticle('amef_airmove_skr', 0)
    RefreshMultihit()
    sprite('am403_08', 3)
    AirPushbackX(12000)
    AirPushbackY(5000)
    CreateParticle('amef_airmove_skr', 0)
    RefreshMultihit()
    sprite('am403_09', 3)
    AirPushbackX(12000)
    AirPushbackY(0)
    RefreshMultihit()
    sprite('am403_10', 3)
    AirPushbackX(12000)
    AirPushbackY(0)
    RefreshMultihit()
    sprite('am403_11', 4)
    sprite('am403_12', 3)
    physicsXImpulse(0)
    ScreenShake(8000, 6000)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(750)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(30000)
    AirPushbackY(16000)
    Hitstop(15)
    Wallbounce(1)
    NonCornerWallbounce(1)
    AirHitstunAfterWallbounce(20)
    Wallstick(1)
    WallstickDuration(17)
    if SLOT_137:
        DamageMultiplier(80)
    AltKnockdownEffects(100, 1, 1)
    sprite('am403_13', 2)
    Recovery()
    sprite('am403_14', 2)
    sprite('am403_15', 2)
    sprite('am403_16', 3)
    sprite('am403_17', 3)
    sprite('am403_18', 3)
    sprite('am403_19', 3)
    sprite('am403_20', 3)


@State
def Ginga():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('am406_00', 3)
    sprite('am406_01', 3)
    sprite('am406_02', 3)
    sprite('am406_03', 2)
    Voiceline('am207')
    physicsXImpulse(5000)
    sprite('am406_04', 3)
    XImpulseAcceleration(150)
    CreateObject('amef_408', -1)
    CommonSE('006_swing_blade_2')
    sprite('am406_05', 3)
    XImpulseAcceleration(150)
    sprite('am406_06', 3)
    XImpulseAcceleration(60)
    sprite('am406_07', 4)
    XImpulseAcceleration(60)
    sprite('am406_08', 4)
    XImpulseAcceleration(0)
    sprite('am406_09', 4)
    sprite('am406_10', 3)
    Recovery()
    sprite('am406_11', 3)
    sprite('am406_12', 3)
    sprite('am406_13', 3)
    sprite('am406_14', 3)
    sprite('am406_15', 3)


@State
def AirMultiStrike():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(200)
        AttackP1(80)
        AttackP2(89)
        SingleProration(1)
        Hitstop(2)
        EnemyHitstopAddition(-1, -1, -1)
        Hitstun(25)
        AirUntechableTime(25)
        HardKnockdown(25)
        AirPushbackX(27000)
        AirPushbackY(-54000)
        YImpulseBeforeWallbounce(0)
        PushbackX(22000)
        AttackDirection(2)
        HitsparkSize(800)
        EnableAfterimage(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('am404_00', 2)
    Voiceline('am100')
    EndMomentum(1)
    sprite('am404_01', 2)
    sprite('am404_02', 2)
    sprite('am404_03', 2)
    sprite('am404_04', 2)
    sprite('am404_05', 2)
    PrivateSE('amse_05')
    CreateParticle('amef_airmove_skr', 0)
    CreateObject('403_tossinaura', 0)
    physicsXImpulse(30000)
    physicsYImpulse(-48000)
    setGravity(0)
    loopRest()
    label(0)
    sprite('am404_06', 4)
    CreateParticle('amef_airmove_skr', 0)
    RefreshMultihit()
    sprite('am404_07', 4)
    CreateParticle('amef_airmove_skr', 0)
    RefreshMultihit()
    sprite('am404_05', 4)
    CreateParticle('amef_airmove_skr', 0)
    CreateObject('403_tossinaura', 0)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('am404_08', 4)
    ScreenShake(2000, 10000)
    YAccel(0)
    XImpulseAcceleration(80)
    TriggerUponForState('403_tossinaura', 32)
    LandingEffects(100, 1, 1)
    EnableAfterimage(0)
    ForceFaceSprite()
    CrouchState(1)
    sprite('am404_09', 4)
    XImpulseAcceleration(80)
    sprite('am404_10', 4)
    Voiceline('am204')
    XImpulseAcceleration(60)
    sprite('am404_11', 3)
    XImpulseAcceleration(0)
    RefreshMultihit()
    Damage(900)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(30000)
    AirPushbackY(6000)
    ResetGravity()
    AirUntechableTime(30)
    Floorslide(5)
    HardKnockdown(0)
    Hitstop(11)
    EnemyHitstopAddition(0, 0, 2)
    MoveAttributes(0, 0, 1, 0, 0)
    HitsparkSize(1000)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('am404_12', 3)
    AttackOff()
    Recovery()
    sprite('am404_13', 3)
    sprite('am404_14', 3)
    sprite('am404_15', 3)
    sprite('am404_16', 3)
    sprite('am404_17', 3)
    CrouchState(0)
    sprite('am404_18', 3)
    sprite('am404_19', 3)


@State
def FrontJumpA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        ForcedLandingRecovery(4, 1)
    sprite('am023_00', 2)
    sprite('am023_01', 2)
    SmartVoiceline('am205')
    sprite('am405_00', 3)
    Recovery()
    PrivateSE('amse_05')
    JumpEffects(0, 0)
    physicsYImpulse(24000)
    physicsXImpulse(18000)
    setGravity(1600)
    CreateParticle('amef_airmove_skr', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    label(0)
    sprite('am405_00', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_04', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_05', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def FrontJumpB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        ForcedLandingRecovery(4, 1)
    sprite('am023_00', 3)
    sprite('am023_01', 3)
    SmartVoiceline('am205')
    sprite('am405_00', 3)
    Recovery()
    PrivateSE('amse_05')
    JumpEffects(1, 0)
    physicsYImpulse(30000)
    physicsXImpulse(20000)
    setGravity(1800)
    CreateParticle('amef_airmove_skr', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    label(0)
    sprite('am405_00', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_04', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_05', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def BackJumpA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        ForcedLandingRecovery(4, 1)
    sprite('am023_00', 2)
    sprite('am023_01', 2)
    sprite('am405_06', 3)
    Recovery()
    PrivateSE('amse_05')
    SmartVoiceline('am206')
    JumpEffects(0, 0)
    physicsYImpulse(24000)
    physicsXImpulse(-16000)
    setGravity(1600)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def BackJumpB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        ForcedLandingRecovery(4, 1)
    sprite('am023_00', 3)
    sprite('am023_01', 3)
    sprite('am405_06', 3)
    Recovery()
    PrivateSE('amse_05')
    SmartVoiceline('am206')
    JumpEffects(1, 0)
    physicsYImpulse(32000)
    physicsXImpulse(-14000)
    setGravity(1800)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def AirFrontJumpA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        SLOT_5 = 1
        ForcedLandingRecovery(4, 1)
        Recovery()
    sprite('am405_00', 3)
    PrivateSE('amse_05')
    SmartVoiceline('am205')
    JumpEffects(0, 0)
    physicsYImpulse(20000)
    physicsXImpulse(16000)
    setGravity(1400)
    CreateParticle('amef_airmove_skr', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_00', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_04', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_05', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def AirFrontJumpB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        SLOT_5 = 1
        ForcedLandingRecovery(4, 1)
        Recovery()
    sprite('am405_00', 3)
    PrivateSE('amse_05')
    SmartVoiceline('am205')
    JumpEffects(1, 0)
    physicsYImpulse(30000)
    physicsXImpulse(16000)
    setGravity(1400)
    CreateParticle('amef_airmove_skr', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_00', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_01', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_02', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_03', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_04', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_05', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def AirBackJumpA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        SLOT_5 = 1
        ForcedLandingRecovery(4, 1)
        Recovery()
    sprite('am405_06', 3)
    PrivateSE('amse_05')
    SmartVoiceline('am206')
    JumpEffects(0, 0)
    physicsYImpulse(24000)
    physicsXImpulse(-12000)
    setGravity(1400)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def AirBackJumpB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        uponSendToLabel(FALLING, 9)
        SLOT_5 = 1
        ForcedLandingRecovery(4, 1)
        Recovery()
    sprite('am405_06', 3)
    PrivateSE('amse_05')
    SmartVoiceline('am206')
    JumpEffects(1, 0)
    physicsYImpulse(36000)
    physicsXImpulse(-12000)
    setGravity(1400)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    EndIfChangeFacing(1)
    WhiffOverdriveCancel(1)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@Subroutine
def UltimateAssault_SE():
    if SLOT_59 == 1:
        PrivateSE('amse_01_loop')
    if SLOT_59 == 2:
        PrivateSE('amse_02_loop')
    if SLOT_59 == 3:
        PrivateSE('amse_03_loop')


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(82)
        PushbackX(-1000)
        AirUntechableTime(60)
        Hitstop(3)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(98)
        Crumple(98)
        CHStagger(98)
        CHCrumple(98)
        ChipPercentage(10)
        StarterRating(2)
        if SLOT_59 == 2:
            ChipPercentage(15)
        if SLOT_59 == 3:
            ChipPercentage(20)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            AlphaValue(198)
            ConstantAlphaModifier(-6)
            EnableCollision(0)
            setInvincible(1)
            EnableRapidCancel(0)
            EffectPosition(22, 104)
            AddX(-100000)
            sendToLabel(9)

        def upon_32():
            EnableRapidCancel(1)
            clearUponHandler(32)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_61 = 0
        setInvincible(1)
        SLOT_61 = 1
        if SLOT_137:
            DamageMultiplier(80)
    sprite('am430_00', 4)
    Voiceline('am250')
    AddX(-80000)
    sprite('am430_01', 3)
    AddX(-60000)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('am430_02', 3)
    AddX(-40000)
    sprite('am430_03', 3)
    AddX(-20000)
    sprite('am430_04', 3)
    sprite('am430_05', 18)
    sprite('am430_05', 2)
    EndMomentum(1)
    sprite('am430_06', 3)
    CreateObject('430_tossindril', 0)
    CreateObject('430_roop', 1)
    PreDashEffects(100, 1, 1)
    sprite('am430_07', 1)
    AbsoluteY(1)
    physicsXImpulse(80000)
    AirDashEffects(1)
    RefreshMultihit()
    sprite('am430_07', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    AirDashEffects(1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    setInvincible(0)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    RefreshMultihit()
    TriggerUponForState('430_tossindril', 32)
    TriggerUponForState('430_roop', 32)
    callSubroutine('UltimateAssault_SE')
    sprite('am430_10', 6)
    AbsoluteY(0)
    XImpulseAcceleration(60)
    sprite('am430_27', 3)
    XImpulseAcceleration(50)
    DashEffects(100, 1, 1)
    sprite('am430_28', 3)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 1)
    sprite('am430_29', 3)
    DashEffects(100, 1, 1)
    sprite('am430_30', 3)
    physicsXImpulse(0)
    sprite('am430_30', 3)
    sprite('am430_31', 4)
    sprite('am430_32', 4)
    sprite('am430_33', 4)
    sprite('am430_34', 4)
    sprite('am430_35', 4)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 6)
    physicsXImpulse(35000)
    TriggerUponForState('430_tossindril', 32)
    sprite('am430_10', 6)
    AbsoluteY(0)
    CreateObject('430_slash', -1)
    TriggerUponForState('430_roop', 32)
    XImpulseAcceleration(70)
    sprite('am430_10', 6)
    XImpulseAcceleration(70)
    sprite('am430_11', 8)
    XImpulseAcceleration(70)
    AlphaValue(80)
    ConstantAlphaModifier(10)
    LandingEffects(100, 1, 1)
    sprite('am430_12', 10)
    XImpulseAcceleration(30)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('am430_13', 4)
    TriggerUponForState('430_slash', 32)
    physicsXImpulse(0)
    sprite('am430_14', 4)
    EnableCollision(1)
    sprite('am430_15', 4)
    sprite('am430_16', 4)
    sprite('am430_17', 30)
    Voiceline('am251')
    sprite('am430_18', 4)
    sprite('am430_19', 4)
    PrivateSE('amse_06')
    PrivateSE('amse_07')
    sprite('am430_20', 2)
    SLOT_57 = 0
    callSubroutine('DrillActionJump')
    CreateObject('UltimateAssaultExplosion', -1)
    DamageFromStateOnly('UltimateAssaultExplosion')
    label(1)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosion', 32)
    gotoLabel(2)
    label(100)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosion', 32)
    gotoLabel(2)
    label(200)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosion', 33)
    gotoLabel(2)
    label(300)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosion', 34)
    gotoLabel(2)
    label(2)
    sprite('am430_20', 3)
    SLOT_61 = 0
    SLOT_59 = 0
    SLOT_31 = 6000
    callSubroutine('DrillLevelDown')
    sprite('am430_21', 3)
    sprite('am430_22', 3)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_23', 4)
    sprite('am430_24', 4)
    sprite('am430_25', 4)
    sprite('am430_26', 4)
    sprite('am000_00', 3)
    setInvincible(0)
    ForceFaceSprite()


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(82)
        PushbackX(-1000)
        AirUntechableTime(60)
        Hitstop(3)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(98)
        Crumple(98)
        CHStagger(98)
        CHCrumple(98)
        ChipPercentage(10)
        AttackType(4)
        StarterRating(2)
        if SLOT_59 == 2:
            ChipPercentage(15)
        if SLOT_59 == 3:
            ChipPercentage(20)
            GotoState('UltimateAssaultOD_Lv3')

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            AlphaValue(198)
            ConstantAlphaModifier(-6)
            EnableCollision(0)
            setInvincible(1)
            EnableRapidCancel(0)
            EffectPosition(22, 104)
            AddX(-100000)
            sendToLabel(9)

        def upon_32():
            EnableRapidCancel(1)
            clearUponHandler(32)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_61 = 0
        setInvincible(1)
        SLOT_61 = 1
        if SLOT_137:
            DamageMultiplier(80)
    sprite('am430_00', 4)
    Voiceline('am250')
    AddX(-80000)
    sprite('am430_01', 3)
    AddX(-60000)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('am430_02', 3)
    AddX(-40000)
    sprite('am430_03', 3)
    AddX(-20000)
    sprite('am430_04', 3)
    sprite('am430_05', 18)
    sprite('am430_05', 2)
    EndMomentum(1)
    sprite('am430_06', 3)
    CreateObject('430_tossindril', 0)
    CreateObject('430_roop', 1)
    PreDashEffects(100, 1, 1)
    sprite('am430_07', 1)
    AbsoluteY(1)
    physicsXImpulse(80000)
    AirDashEffects(1)
    RefreshMultihit()
    sprite('am430_07', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    AirDashEffects(1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_08', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    setInvincible(0)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    RefreshMultihit()
    callSubroutine('UltimateAssault_SE')
    sprite('am430_09', 1)
    RefreshMultihit()
    TriggerUponForState('430_tossindril', 32)
    TriggerUponForState('430_roop', 32)
    callSubroutine('UltimateAssault_SE')
    sprite('am430_10', 6)
    AbsoluteY(0)
    XImpulseAcceleration(60)
    sprite('am430_27', 3)
    XImpulseAcceleration(50)
    DashEffects(100, 1, 1)
    sprite('am430_28', 3)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 1)
    sprite('am430_29', 3)
    DashEffects(100, 1, 1)
    sprite('am430_30', 3)
    physicsXImpulse(0)
    sprite('am430_30', 3)
    sprite('am430_31', 4)
    sprite('am430_32', 4)
    sprite('am430_33', 4)
    sprite('am430_34', 4)
    sprite('am430_35', 4)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 6)
    physicsXImpulse(35000)
    TriggerUponForState('430_tossindril', 32)
    sprite('am430_10', 6)
    AbsoluteY(0)
    CreateObject('430_slash', -1)
    TriggerUponForState('430_roop', 32)
    XImpulseAcceleration(70)
    sprite('am430_10', 6)
    XImpulseAcceleration(70)
    sprite('am430_11', 8)
    XImpulseAcceleration(70)
    AlphaValue(80)
    ConstantAlphaModifier(10)
    LandingEffects(100, 1, 1)
    sprite('am430_12', 10)
    XImpulseAcceleration(30)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('am430_13', 4)
    TriggerUponForState('430_slash', 32)
    physicsXImpulse(0)
    sprite('am430_14', 4)
    EnableCollision(1)
    sprite('am430_15', 4)
    sprite('am430_16', 4)
    sprite('am430_17', 30)
    Voiceline('am251')
    sprite('am430_18', 4)
    sprite('am430_19', 4)
    PrivateSE('amse_06')
    PrivateSE('amse_07')
    sprite('am430_20', 2)
    SLOT_57 = 0
    callSubroutine('DrillActionJump')
    CreateObject('UltimateAssaultExplosionOD', -1)
    DamageFromStateOnly('UltimateAssaultExplosionOD')
    label(1)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosionOD', 32)
    gotoLabel(2)
    label(100)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosionOD', 32)
    gotoLabel(2)
    label(200)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosionOD', 33)
    gotoLabel(2)
    label(300)
    sprite('am430_20', 2)
    TriggerUponForState('UltimateAssaultExplosionOD', 34)
    gotoLabel(2)
    label(2)
    sprite('am430_20', 3)
    SLOT_61 = 0
    SLOT_59 = 0
    SLOT_31 = 6000
    callSubroutine('DrillLevelDown')
    sprite('am430_21', 3)
    sprite('am430_22', 3)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_20', 4)
    sprite('am430_21', 4)
    sprite('am430_22', 4)
    sprite('am430_23', 4)
    sprite('am430_24', 4)
    sprite('am430_25', 4)
    sprite('am430_26', 4)
    sprite('am000_00', 3)
    setInvincible(0)
    ForceFaceSprite()


@State
def ImperialDrill():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(1)
        SLOT_4 = SLOT_59
        SLOT_61 = 1

        def upon_STATE_END():
            SLOT_61 = 0
    sprite('am431_00', 4)
    Voiceline('am252')
    sprite('am431_01', 4)
    sprite('am431_02', 4)
    DistortionSettings(36, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('am431_03', 4)
    sprite('am431_04', 4)
    sprite('am431_05', 4)
    sprite('am431_06', 4)
    sprite('am431_07', 10)
    sprite('am431_08', 4)
    setInvincible(0)
    sprite('am431_09', 4)
    sprite('am431_10', 2)
    CreateObject('ContinuationDrillCreater', -1)
    SLOT_61 = 0
    SLOT_59 = 0
    SLOT_31 = 6000
    callSubroutine('DrillLevelDown')
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_14', 3)
    sprite('am431_15', 3)
    sprite('am431_16', 3)
    sprite('am431_17', 3)
    sprite('am431_18', 4)
    sprite('am431_19', 4)
    sprite('am431_20', 4)


@State
def ImperialDrill_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(1)
        SLOT_4 = SLOT_59
        AttackType(4)
        SLOT_61 = 1

        def upon_STATE_END():
            SLOT_61 = 0
    sprite('am431_00', 4)
    Voiceline('am252')
    sprite('am431_01', 4)
    sprite('am431_02', 4)
    DistortionSettings(36, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('am431_03', 4)
    sprite('am431_04', 4)
    sprite('am431_05', 4)
    sprite('am431_06', 4)
    sprite('am431_07', 10)
    sprite('am431_08', 4)
    setInvincible(0)
    sprite('am431_09', 4)
    sprite('am431_10', 2)
    CreateObject('ContinuationDrillCreaterOD', -1)
    SLOT_61 = 0
    SLOT_59 = 0
    SLOT_31 = 6000
    callSubroutine('DrillLevelDown')
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_10', 2)
    sprite('am431_11', 2)
    sprite('am431_12', 2)
    sprite('am431_13', 2)
    sprite('am431_14', 3)
    sprite('am431_15', 3)
    sprite('am431_16', 3)
    sprite('am431_17', 3)
    sprite('am431_18', 4)
    sprite('am431_19', 4)
    sprite('am431_20', 4)


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
        OppPositionOnHit(1, 450000, 0)
        DamageFromStateOnly('BurstDDCatch')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            enterState('BurstDDCatch')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('am040_00ex01', 4)
    Voiceline('am280')
    setInvincible(1)
    EndMomentum(1)
    E0EAEffect('BurstDDeff', 103)
    sprite('am312_02ex01', 4)
    CommonSE('019_cloth_a')
    sprite('am312_03ex01', 4)
    sprite('am312_04ex01', 4)
    sprite('am312_05ex01', 3)
    CommonSE('006_swing_blade_2')
    sprite('am312_06ex01', 3)
    sprite('am312_06ex01', 6)
    AttackOff()
    setInvincible(0)
    sprite('am312_07ex01', 10)
    sprite('am312_08ex01', 10)
    sprite('am312_09ex01', 8)


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
        OppPositionOnHit(1, 450000, 0)
        DamageFromStateOnly('BurstDDCatch')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            enterState('BurstDDCatch')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('am040_00ex01', 1)
    Voiceline('am280')
    setInvincible(1)
    EndMomentum(1)
    E0EAEffect('BurstDDeff', 103)
    sprite('am312_02ex01', 2)
    CommonSE('019_cloth_a')
    sprite('am312_03ex01', 2)
    sprite('am312_04ex01', 2)
    sprite('am312_05ex01', 2)
    CommonSE('006_swing_blade_2')
    sprite('am312_06ex01', 3)
    sprite('am312_06ex01', 6)
    AttackOff()
    setInvincible(0)
    sprite('am312_07ex01', 10)
    sprite('am312_08ex01', 10)
    sprite('am312_09ex01', 8)


@State
def BurstDDCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BurstDDExe', 3, 0, 0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        MinimumDamage(10)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        AttackP2(100)
        SameMoveProration(-1)
        IgnoreComboTime(1)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        DamageFromStateOnly('BurstDDExe')
        SetBackground(1)
        Unknown2066(1)
    sprite('am312_06ex01', 3)
    setInvincible(1)
    sprite('am312_07ex01', 6)
    sprite('am312_08ex01', 6)
    sprite('am312_09ex01', 8)


@State
def BurstDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(4)
        Damage(800)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        AttackP2(100)
        SameMoveProration(-1)
        AirUntechableTime(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(48000)
        IgnoreComboTime(1)
        OnlyHitPlayer(1)
        HitAnywhere(1)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        EnableRapidCancel(0)
        MinimumDamage(10)
        DamageFromStateOnly('BurstDDExe2')

        def upon_OPPONENT_HIT():
            AddActionMark(1)

        def upon_STATE_END():
            ExtendCollisionX(0)
        SetBackground(1)
        Unknown2066(1)
    sprite('am312_06ex01', 10)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    AttackOff()
    sprite('am312_07ex01', 5)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am312_08ex01', 5)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am312_09ex01', 5)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CreateObject('BurstDDCamera', -1)
    sprite('am210_00ex01', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('am210_01ex01', 1)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ExtendCollisionX(500)
    sprite('am210_01ex01', 1)
    ExtendCollisionX(520)
    sprite('am210_02ex01', 1)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ExtendCollisionX(540)
    sprite('am210_02ex01', 1)
    ExtendCollisionX(560)
    sprite('am210_03ex01', 1)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ExtendCollisionX(580)
    sprite('am210_03ex01', 1)
    ExtendCollisionX(600)
    sprite('am210_04ex01', 1)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ExtendCollisionX(650)
    sprite('am210_04ex01', 1)
    ExtendCollisionX(700)
    sprite('am210_05ex01', 2)
    Voiceline('am281')
    RefreshMultihit()
    sprite('am210_06ex01', 2)
    sprite('am210_07ex01', 3)
    sprite('am210_08ex01', 3)
    sprite('am210_09ex01', 3)
    sprite('am210_10ex01', 3)
    if SLOT_2:
        enterState('BurstDDExe2')
    sprite('am210_11', 2)
    sprite('am210_12', 2)
    DespawnEAEffect('BurstDDCamera')


@State
def BurstDDExe2():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BurstDDFinish', 3, 1, 0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        Damage(500)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        AttackP2(100)
        SameMoveProration(-1)
        IgnoreComboTime(1)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDFinish')
        MinimumDamage(10)
        EnableRapidCancel(0)
        SetBackground(1)
        Unknown2066(1)
    sprite('am212_00ex01', 3)
    setInvincible(1)
    sprite('am212_01ex01', 3)
    sprite('am212_02ex01', 3)
    sprite('am212_03ex01', 3)
    sprite('am212_04ex01', 3)
    sprite('am212_05ex01', 3)
    sprite('am212_06ex01', 3)
    CommonSE('006_swing_blade_1')
    sprite('am212_07ex01', 2)
    CommonSE('006_swing_blade_1')
    sprite('am440_00', 2)
    sprite('am440_01', 2)
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('am440_02ex00', 3)
    loopRest()
    DespawnEAEffect('BurstDDCamera')
    label(1)
    sprite('am440_02ex01', 3)
    loopRest()
    DespawnEAEffect('BurstDDCamera')


@State
def BurstDDFinish():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackType(4)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(0)
        AttackP2(100)
        SameMoveProration(-1)
        Hitstop(25)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(-5500)
        AirPushbackY(-30000)
        HardKnockdown(15)
        IgnoreComboTime(1)
        OnlyHitPlayer(1)
        HitAnywhere(1)
        CHStateIfCHStart(3)
        DamageFromStateOnly('BurstDDFinish')
        MinimumDamage(10)
        EnableRapidCancel(0)
        SetBackground(1)

        def upon_STATE_END():
            Flip()
            DespawnEAEffect('BurstDDCamera')
        AttackOff()
    if SLOT_51:
        conditionalSendToLabel(100)
    sprite('am440_02ex00', 20)
    OppThrowAnimation(24, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    CreateParticle('amef_440a', 1)
    sprite('am440_03', 4)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_04', 4)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_05', 3)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_06', 3)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_07', 2)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    TriggerUponForState('BurstDDCamera', 32)
    sprite('am440_08', 2)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('am282')
    sprite('am440_09', 6)
    CreateObject('amef_440finish_a', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    ScreenShake(50000, 50000)
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('am440_02ex01', 20)
    OppThrowAnimation(24, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    CreateParticle('amef_440b', 1)
    sprite('am440_03ex01', 4)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_04ex01', 4)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_05ex01', 3)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_06ex01', 3)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('am440_07ex01', 2)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    TriggerUponForState('BurstDDCamera', 32)
    sprite('am440_08ex01', 2)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('am282')
    sprite('am440_09ex01', 6)
    DamageEffect(2, 'Ameff_BurstDDHit')
    CommonSE('025_cleanhit_grap')
    CreateObject('amef_440finish_b', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Damage(3750)
    ScreenShake(120000, 120000)
    RefreshMultihit()
    label(9)
    sprite('am440_09', 4)
    DespawnEAEffect('BurstDDCamera')
    sprite('am440_10', 4)
    sprite('am440_11', 4)
    sprite('am440_12', 4)
    sprite('am440_13', 4)
    sprite('am440_14', 4)
    sprite('am440_15', 4)
    KeepBackground(0)
    sprite('am213_19ex01', 4)
    sprite('am213_20ex01', 4)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        EndMomentum(0)
        AttackLevel_(0)
        Hitstun(40)
        Damage(300)
        DefeatOpponentBehavior(1)
        StayAfterMovement(1, 0)
        AttackOff()

        def upon_32():
            setInvincible(1)
            AstralHeatCleanup(1, 1)
            PlayPlayAstralBGM(1)
            CreateObject('450_renge', -1)
            sendToLabel(0)
            clearUponHandler(32)
            TriggerUponForState('GroundDrill', 35)

            def RunOnObject_22():
                WallCollisionDetection(0)
    sprite('am450_00', 6)
    setInvincible(1)
    Voiceline('am290')
    DistortionSettings(60, -1, 2)
    CreateObject('EMB_AM_AH', -1)
    EmptyHeat()
    sprite('am450_01', 6)
    E0EAEffect('aura', 65535)
    sprite('am450_02', 6)
    sprite('am450_03', 6)
    sprite('am450_04', 6)
    sprite('am450_05', 6)
    sprite('am450_06', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    CreateObject('450_Hokaku', -1)
    CreateObject('450_HokakuCircle', -1)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    setInvincible(0)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_25', 6)
    SetBackground(0)
    TriggerUponForState('450_HokakuCircle', 32)
    TriggerUponForState('450_Hokaku', 32)
    sprite('am450_26', 6)
    loopRest()
    ExitState()
    label(0)
    sprite('am450_07', 6)
    RenderLayer(4)
    SetBackground(3)
    HUDVisibillity(1)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    TriggerUponForState('450_HokakuCircle', 32)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    Voiceline('am291')
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_07', 6)
    sprite('am450_08', 6)
    sprite('am450_09', 6)
    sprite('am450_10', 6)
    RenderLayer(0)
    sprite('am450_11', 6)
    sprite('am450_12', 6)
    sprite('am450_13', 6)
    PrivateSE('amse_07')
    sprite('am450_14', 6)
    sprite('am450_15', 15)
    sprite('am450_15', 15)
    sprite('am450_16', 8)
    sprite('am450_17', 8)
    sprite('am450_18', 8)
    sprite('am450_19', 8)
    sprite('am450_20', 8)
    sprite('am450_21', 8)
    sprite('am450_22', 8)
    sprite('am450_23', 8)
    sprite('am450_24', 120)
    sprite('am450_24', 10)
    PrivateSE('amse_08')
    CreateObject('450_maku', -1)
    sprite('am450_24', 110)
    Voiceline('am292')
    sprite('am450_24', 90)
    WinAction()
    CameraControlInfinity(1)
    CameraWinnerControlStop(1)
    sprite('am450_24', 32767)
    DemoTimer(150)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('am054')
    sprite('am900_00', 32767)
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
        AbsoluteY(150000)
    sprite('am901_00', 50)
    physicsYImpulse(-150)
    sprite('am901_00', 50)
    physicsYImpulse(150)
    Voiceline('am055')
    label(0)
    sprite('am901_00', 32767)
    physicsYImpulse(-150)
    sprite('am901_00', 32767)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('am000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14433, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am055', 12641, 25392, 12337, 14177, 13155, 24886, 25399, 
        24887, 25399, 24887, 25399, 24887, 25399, 24884, 25399, 24887, 
        25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am290', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
        13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('am291', 13921, 13923, 13921, 13923, 13921, 13411, 24885, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
        24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('am292', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am400', 14433, 14435, 14433, 14435, 14433, 14435, 13921, 
        13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am401', 14433, 14435, 12641, 25394, 24886, 25399, 24887, 
        25399, 24887, 25399, 24887, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am404', 14177, 13411, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 
        24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am406', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
        14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('am407', 14177, 14179, 14177, 13411, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
        13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am408', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        13411, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am411', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am412', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14177, 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am413', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am414', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('am415', 12641, 25394, 24887, 25399, 24887, 25398, 24886, 
        25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('am416', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('am417', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 12643, 24880, 24888, 25400, 24888, 25400, 24888, 
        25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('am000', 14177, 14179, 14177, 14179, 14177, 14179, 
            14433, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am290', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am291', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('am292', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am400', 14177, 14179, 14177, 14179, 14177, 14179, 
            13921, 13923, 13921, 13411, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('am401', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am404', 13409, 12643, 24888, 25399, 24887, 25398, 
            24886, 25398, 24886, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am405', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
            14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am406', 13923, 14177, 14179, 14177, 14179, 14177, 
            12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am407', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 
            25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 
            25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am408', 14433, 14435, 14433, 14435, 14433, 12643, 
            24880, 25399, 24887, 25398, 24886, 25398, 24886, 25399, 24887, 
            25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
            55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am411', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am412', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am413', 14177, 14179, 14177, 14179, 13921, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am414', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am415', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('am416', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('am417', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('ca'):
            Unknown18011('am000', 14177, 14179, 14177, 13155, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('am400', 14177, 13411, 24880, 25399, 24887, 25398,
                24886, 25398, 24887, 25399, 24887, 25399, 24887, 12849, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('am401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 12641, 25398, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('am506', 14177, 13923, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('am507', 12641, 25392, 24887, 12337, 14179, 12641,
                25392, 24887, 25399, 12344, 12641, 25392, 24887, 12337, 
                14179, 12641, 25392, 24887, 12337, 14179, 12641, 25392, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('am546', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('am547', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ca'):
            Unknown18011('am518', 14177, 14179, 14177, 12899, 24880, 25399,
                24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('am519', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('am518', 12643, 12340, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('am519', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('am558', 14177, 14179, 14177, 13923, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('am559', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 
                24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            if SLOT_138:
                pass
            else:
                Unknown18011('am562', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('am563', 14177, 14179, 14177, 14179, 12641, 
                    25392, 24887, 25399, 24887, 25399, 24887, 12338, 14179,
                    14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hb'):
            if SLOT_140:
                Unknown18011('am556', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 12641, 25392, 12342,
                    14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399,
                    24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
                Unknown18011('am557', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887,
                    25399, 24887, 25401, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rc'):
        SyncEntry()
        gotoLabel(130)
    if CharacterIDCheck('ca'):
        if SLOT_140:
            gotoLabel(2190)
        else:
            gotoLabel(190)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('hb'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2380)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(400)
    label(482)
    if random_(2, 0, 34):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('am600_00', 6)
    CreateObject('600_kamuro', -1)
    CreateObject('600_ichiza', -1)
    loopRest()
    label(1)
    sprite('am600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('am600_00', 120)
    Voiceline('am412')
    sprite('am600_00', 6)
    TriggerUponForState('600_kamuro', 32)
    TriggerUponForState('600_ichiza', 32)
    sprite('am600_01', 6)
    Voiceline('am413')
    PrivateSE('amse_07')
    CommonSE('019_cloth_c')
    sprite('am600_02', 6)
    sprite('am600_03', 6)
    sprite('am600_04', 6)
    sprite('am600_05', 6)
    sprite('am600_06', 6)
    sprite('am600_07', 6)
    sprite('am600_08', 6)
    sprite('am600_09', 6)
    loopRest()
    DemoTimer(80)
    ExitState()
    label(10)
    sprite('am601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('am601_00', 100)
    Voiceline('am414')
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    Voiceline('am415')
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    if SLOT_43:
        DemoTimer(65)
    else:
        DemoTimer(105)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    ExitState()
    label(20)
    sprite('am601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('am601_00', 180)
    Voiceline('am416')
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    Voiceline('am417')
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    if SLOT_43:
        DemoTimer(200)
    else:
        DemoTimer(40)
    loopRest()
    ExitState()
    label(130)
    uponSendToLabel(32, 132)
    label(131)
    sprite('am601_00', 6)
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('am601_00', 120)
    clearUponHandler(32)
    Voiceline('am506')
    DemoTimer(300)
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    ExitState()
    label(190)
    sprite('am600_00', 6)
    CreateObject('600_kamuro', -1)
    CreateObject('600_ichiza', -1)
    loopRest()
    label(191)
    sprite('am600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(191)
    sprite('am600_00', 120)
    clearUponHandler(32)
    Voiceline('am518')
    DemoTimer(300)
    sprite('am600_00', 6)
    TriggerUponForState('600_kamuro', 32)
    TriggerUponForState('600_ichiza', 32)
    sprite('am600_01', 6)
    PrivateSE('amse_07')
    CommonSE('019_cloth_c')
    sprite('am600_02', 6)
    sprite('am600_03', 6)
    sprite('am600_04', 6)
    sprite('am600_05', 6)
    sprite('am600_06', 6)
    sprite('am600_07', 6)
    sprite('am600_08', 6)
    sprite('am600_09', 6)
    loopRest()
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    ObjectUpon(22, 32)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    ExitState()
    label(2190)
    sprite('am601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2190)
    sprite('am601_00', 10)
    sprite('am601_00', 120)
    Voiceline('am518')
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    ObjectUpon(22, 32)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    uponSendToLabel(32, 332)
    label(331)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    gotoLabel(331)
    label(332)
    sprite('am000_00', 3)
    sprite('am300_00', 6)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    Voiceline('am546')
    label(333)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(333)
    sprite('am300_09', 6)
    sprite('am300_10', 6)
    loopRest()
    DemoTimer(30)
    loopRest()
    ExitState()
    label(2380)
    sprite('am600_00', 6)
    CreateObject('600_kamuro', -1)
    CreateObject('600_ichiza', -1)
    label(2381)
    sprite('am600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2381)
    sprite('am600_00', 20)
    sprite('am600_00', 180)
    Voiceline('am556')
    sprite('am600_00', 6)
    TriggerUponForState('600_kamuro', 32)
    TriggerUponForState('600_ichiza', 32)
    sprite('am600_01', 6)
    PrivateSE('amse_07')
    CommonSE('019_cloth_c')
    sprite('am600_02', 6)
    sprite('am600_03', 6)
    sprite('am600_04', 6)
    sprite('am600_05', 6)
    sprite('am600_06', 6)
    sprite('am600_07', 6)
    sprite('am600_08', 6)
    sprite('am600_09', 6)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    ObjectUpon(22, 32)
    sprite('am000_15', 7)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(390)
    uponSendToLabel(32, 392)
    label(391)
    sprite('am601_00', 6)
    loopRest()
    gotoLabel(391)
    label(392)
    sprite('am601_00', 100)
    clearUponHandler(32)
    Voiceline('am558')
    DemoTimer(200)
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    loopRest()
    ExitState()
    label(400)
    uponSendToLabel(32, 402)
    label(401)
    sprite('am601_00', 6)
    loopRest()
    gotoLabel(401)
    label(402)
    sprite('am601_00', 110)
    clearUponHandler(32)
    Voiceline('am562')
    DemoTimer(240)
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    if random_(2, 0, 50):
        Voiceline('am400')
    else:
        Voiceline('am401')
    DemoEndOnVoiceEnd(1)
    sprite('am615_07', 32767)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rc'):
        conditionalSendToLabel(130)
    if CharacterIDCheck('ca'):
        conditionalSendToLabel(190)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('hb'):
        if SLOT_140:
            conditionalSendToLabel(2380)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('mi'):
        if SLOT_138:
            gotoLabel(410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('am610_00', 6)
    CreateObject('610_spot', -1)
    sprite('am610_01', 6)
    sprite('am610_02', 6)
    sprite('am610_03', 6)
    CommonSE('019_cloth_c')
    sprite('am610_04', 6)
    sprite('am610_05', 6)
    Voiceline('am406')
    sprite('am610_06', 6)
    sprite('am610_07', 6)
    CreateObject('610_ichiza', -1)
    sprite('am610_08', 6)
    sprite('am610_09', 6)
    sprite('am610_10', 6)
    sprite('am610_11', 6)
    sprite('am610_12', 6)
    sprite('am610_13', 6)
    CommonSE('019_cloth_a')
    sprite('am610_14', 6)
    sprite('am610_15', 32767)
    if SLOT_43:
        DemoTimer(130)
    else:
        DemoTimer(160)
    loopRest()
    ExitState()
    label(10)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am407')
    if SLOT_43:
        DemoTimer(200)
    else:
        DemoTimer(310)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(20)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am408')
    if SLOT_43:
        DemoTimer(130)
    else:
        DemoTimer(250)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(130)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am507')
    DemoEndOnVoiceEnd(1)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(190)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am519')
    DemoEndOnVoiceEnd(1)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(330)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am547')
    DemoEndOnVoiceEnd(1)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(2380)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    Voiceline('am557')
    DemoEndOnVoiceEnd(1)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()
    label(390)
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    Voiceline('am559')
    DemoEndOnVoiceEnd(1)
    sprite('am615_07', 32767)
    label(410)
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    Voiceline('am563')
    DemoEndOnVoiceEnd(1)
    sprite('am615_07', 32767)
    label(1410)
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    Voiceline('am563')
    DemoEndOnVoiceEnd(1)
    sprite('am615_07', 32767)
    label(666)
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    if random_(2, 0, 50):
        Voiceline('am407')
    else:
        Voiceline('am408')
    DemoEndOnVoiceEnd(1)
    sprite('am611_06', 32767)
    loopRest()
    ExitState()


@State
def CmnActLose():
    sprite('am620_00', 6)
    sprite('am620_01', 6)
    Voiceline('am411')
    sprite('am620_02', 6)
    sprite('am620_03', 6)
    sprite('am620_04', 6)
    sprite('am620_05', 6)
    sprite('am620_06', 6)
    sprite('am620_07', 6)
    sprite('am620_08', 32767)
    DemoTimer(150)
    loopRest()


@State
def EventDefEntryWait():
    label(0)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
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
def EventDefChouhatsu():
    sprite('am300_00', 6)
    label(0)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDefChouhatsuEnd():
    sprite('am300_09', 6)
    sprite('am300_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventFDashOutOpposite():
    EnableCollision(0)
    ScreenCollision(0)
    ForceFaceSprite()
    Flip()
    sprite('am003_01ex', 3)
    sprite('am003_00', 3)
    sprite('am003_01', 3)
    sprite('am032_00', 2)
    SLOT_51 = 0
    sprite('am032_01', 1)
    physicsXImpulse(21000)
    SetAcceleration(200)
    label(0)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    if SLOT_51 <= 4:
        DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    if SLOT_51 <= 4:
        DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    loopRest()
    SLOT_51 = SLOT_51 + 1
    gotoLabel(0)


@State
def EventVSBN1():
    sprite('am601_00', 32767)


@State
def EventVSBN2():
    sprite('am601_00', 6)
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSBN3():
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    sprite('am615_07', 32767)


@State
def EventVSJN1():
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    sprite('am611_06', 32767)


@State
def EventVSCA1():
    sprite('keep', 32767)
    XPositionRelativeFacing(-960000)
    ScreenCollision(0)
    Visibility(1)


@State
def EventVSCA2():
    ScreenCollision(0)
    sprite('am032_00', 2)
    physicsXImpulse(15000)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    XImpulseAcceleration(70)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    sprite('am032_01', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSCA3():
    ScreenCollision(0)
    sprite('am032_00', 2)
    physicsXImpulse(12000)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    DashEffects(100, 1, 1)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    DashEffects(100, 1, 1)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    label(0)
    sprite('am032_01', 2)
    sprite('am032_02', 4)
    sprite('am032_03', 4)
    sprite('am032_04', 4)
    sprite('am032_05', 4)
    sprite('am032_06', 4)
    sprite('am032_07', 4)
    sprite('am032_08', 4)
    sprite('am032_09', 4)
    sprite('am032_10', 4)
    sprite('am032_11', 4)
    sprite('am032_12', 4)
    loopRest()
    gotoLabel(0)


@State
def EventVSRC1():
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 32767)


@State
def EventVSRC2():
    sprite('am611_05', 7)
    sprite('am611_04', 7)
    sprite('am611_03', 7)
    sprite('am611_02', 7)
    sprite('am611_01', 7)
    sprite('am611_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSRC3():
    label(0)
    sprite('am010_02', 8)
    sprite('am010_03', 8)
    sprite('am010_04', 8)
    sprite('am010_05', 8)
    sprite('am010_06', 8)
    sprite('am010_07', 8)
    sprite('am010_08', 8)
    loopRest()
    gotoLabel(0)


@State
def EventVSRC4():
    sprite('am010_01', 4)
    sprite('am010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventReactionStart():
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    sprite('am611_06', 32767)


@State
def EventReactionEnd():
    sprite('am611_06', 6)
    sprite('am611_05', 6)
    sprite('am611_04', 6)
    sprite('am611_03', 6)
    sprite('am611_02', 6)
    sprite('am611_01', 6)
    sprite('am611_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventYoroke():
    sprite('am070_01', 32767)
    loopRest()


@State
def EventDown():
    StayAfterMovement(1, 0)
    sprite('am070_00', 4)
    sprite('am070_01', 3)
    sprite('am070_02', 3)
    sprite('am070_03', 3)
    sprite('am070_04', 4)
    sprite('am070_05', 4)
    sprite('am070_06', 4)
    sprite('am070_07', 4)
    sprite('am070_08', 4)
    sprite('am070_09', 4)
    Unknown1004()
    sprite('am063_11', 32767)
    StayAfterMovement(0, 0)
    Unknown1005()
    loopRest()


@State
def EventActionStrike():
    sprite('am403_00', 6)
    sprite('am403_01', 6)
    sprite('am403_02', 6)
    sprite('am403_03', 6)
    sprite('am403_04', 6)
    sprite('am403_05', 6)
    sprite('am403_06', 6)
    sprite('am403_07', 6)
    sprite('am403_08', 6)
    sprite('am403_09', 6)
    sprite('am403_10', 6)
    sprite('am403_11', 6)
    sprite('am403_12', 6)
    sprite('am403_13', 6)
    sprite('am403_14', 6)
    sprite('am403_15', 6)
    sprite('am403_16', 6)
    sprite('am403_17', 6)
    sprite('am403_18', 6)
    sprite('am403_19', 6)
    sprite('am403_20', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKamae():
    sprite('am400_00', 4)
    sprite('am400_01', 4)
    CallCustomizableParticle('amef_401_charge_start', 0)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    label(0)
    sprite('am400_03', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_04', 4)
    sprite('am400_05', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_06', 4)
    sprite('am400_07', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_08', 3)
    sprite('am400_08', 1)
    loopRest()
    gotoLabel(0)


@State
def EventKamaeEnd():
    sprite('am400_02', 2)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    CallCustomizableParticle('amef_401_charge_start', 0)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_01', 4)
    sprite('am400_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalkEntry():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('am030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('am030_01', 7)
    sprite('am030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    CameraControlEnable(0)
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('keep', 32767)
    Visibility(1)


@State
def EventBackJumpB():

    def upon_IMMEDIATE():
        uponSendToLabel(FALLING, 9)
        EnableCollision(0)
        ScreenCollision(0)
    sprite('am023_00', 3)
    sprite('am023_01', 3)
    sprite('am405_06', 3)
    PrivateSE('amse_05')
    JumpEffects(1, 0)
    physicsYImpulse(23000)
    physicsXImpulse(-22000)
    setGravity(900)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def EventFWalkOutOpposite():
    EnableCollision(0)
    ScreenCollision(0)
    ForceFaceSprite()
    Flip()
    sprite('am003_01ex', 3)
    sprite('am003_00', 3)
    sprite('am003_01', 3)
    sprite('am032_00', 2)
    SLOT_51 = 0
    sprite('am032_01', 1)
    physicsXImpulse(4800)
    label(0)
    sprite('am030_01', 7)
    sprite('am030_02', 7)
    if SLOT_51 <= 2:
        SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    if SLOT_51 <= 2:
        SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    SLOT_51 = SLOT_51 + 1
    gotoLabel(0)


@State
def Act2Event_Smile():
    sprite('am611_00', 6)
    sprite('am611_01', 6)
    sprite('am611_02', 6)
    sprite('am611_03', 6)
    sprite('am611_04', 6)
    sprite('am611_05', 6)
    sprite('am611_06', 32767)
    loopRest()


@State
def Act2Event_SmileEnd():
    sprite('keep', 2)
    sprite('am611_06', 6)
    sprite('am611_05', 6)
    sprite('am611_04', 6)
    sprite('am611_03', 6)
    sprite('am611_02', 6)
    sprite('am611_01', 6)
    sprite('am611_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Hand():
    sprite('am310_00', 7)
    sprite('am310_01', 7)
    sprite('am310_02', 32767)
    loopRest()


@State
def Act2Event_HandEnd():
    sprite('keep', 2)
    sprite('am611_01', 8)
    sprite('am611_00', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Entry1():
    sprite('am601_00', 32767)
    loopRest()


@State
def Act2Event_Entry1End():
    sprite('am601_00', 6)
    sprite('am601_00', 6)
    sprite('am601_01', 6)
    sprite('am601_02', 6)
    sprite('am601_03', 6)
    sprite('am601_04', 6)
    sprite('am601_05', 6)
    sprite('am601_06', 6)
    ParticleColorFromPalette(20, 20, 20)
    CallCustomizableParticle('amef_601_add', 0)
    CommonSE('019_cloth_c')
    sprite('am601_07', 6)
    sprite('am601_08', 6)
    sprite('am601_09', 6)
    sprite('am601_10', 6)
    sprite('am601_11', 4)
    sprite('am601_12', 4)
    sprite('am601_13', 4)
    sprite('am601_14', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_TimeUp():
    sprite('am620_00', 6)
    sprite('am620_01', 6)
    LandingEffects(100, 1, 1)
    sprite('am620_02', 6)
    sprite('am620_03', 6)
    sprite('am620_04', 6)
    sprite('am620_05', 6)
    sprite('am620_06', 6)
    sprite('am620_07', 12)
    sprite('am620_08', 32767)
    loopRest()


@State
def Act2Event_TimeUpEnd():
    sprite('keep', 2)
    sprite('am620_06', 6)
    sprite('am620_05', 6)
    sprite('am620_04', 6)
    sprite('am061_05', 5)
    sprite('am061_06', 5)
    sprite('am061_07', 5)
    sprite('am061_08', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_mkvsam_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('keep', 2)
    sprite('am611_06', 6)
    sprite('am611_05', 6)
    sprite('am611_04', 6)
    sprite('am611_03', 6)
    sprite('am611_02', 6)
    sprite('am611_01', 6)
    sprite('am611_00', 6)
    sprite('keep', 2)
    sprite('am003_01ex', 3)
    Flip()
    sprite('am003_00', 3)
    sprite('am003_01', 3)
    sprite('am030_00', 7)
    physicsXImpulse(4650)
    SetActionMark(3)
    label(0)
    sprite('am030_01', 7)
    AddActionMark(-1)
    sprite('am030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)
    loopRest()


@State
def Act2Event_WalkEntry():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 620000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('am030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('am030_01', 7)
    sprite('am030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    CameraControlEnable(0)
    enterState('CmnActStand')


@State
def Act2Event_backstep():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()

        def upon_8():
            setInvincible(0)
    sprite('am033_00', 1)
    sprite('am033_01', 3)
    physicsXImpulse(-12000)
    physicsYImpulse(5800)
    setGravity(1200)
    JumpSoundEffects()
    sprite('am033_02', 3)
    sprite('am033_03', 3)
    label(0)
    sprite('am033_04', 3)
    sprite('am033_02', 3)
    sprite('am033_03', 3)
    sprite('am033_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('am033_05', 3)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('am033_06', 3)


@State
def Act2Event_sensuOpen():
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    sprite('am615_07', 32767)
    loopRest()


@State
def Act2Event_sensuClose():
    sprite('am615_04', 6)
    sprite('am615_03', 6)
    sprite('am615_02', 6)
    sprite('am615_01', 6)
    sprite('am615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Kamae():
    sprite('am400_00', 4)
    sprite('am400_01', 4)
    CallCustomizableParticle('amef_401_charge_start', 0)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    label(0)
    sprite('am400_03', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    CommonSE('019_cloth_b')
    sprite('am400_04', 4)
    sprite('am400_05', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_06', 4)
    sprite('am400_07', 4)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_08', 3)
    sprite('am400_08', 1)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_KamaeEnd():
    sprite('am400_02', 2)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_02', 2)
    CallCustomizableParticle('amef_401_charge_start', 0)
    CreateParticle('amef_401_charge_sakura', 0)
    ParticleColorFromPalette(25, 25, 25)
    CallCustomizableParticle('amef_401_charge', 0)
    sprite('am400_01', 4)
    sprite('am400_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_BackJumpB():

    def upon_IMMEDIATE():
        uponSendToLabel(FALLING, 9)
        EnableCollision(0)
        ScreenCollision(0)
    sprite('am023_00', 3)
    sprite('am023_01', 3)
    sprite('am405_06', 3)
    PrivateSE('amse_05')
    JumpEffects(1, 0)
    physicsYImpulse(23000)
    physicsXImpulse(-22000)
    setGravity(900)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageMask_2(0, 255, 140, 215)
    AfterimageCount(5)
    AfterimageInterval(2)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    label(0)
    sprite('am405_06', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_07', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_08', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_09', 3)
    CreateParticle('amef_airmove_skr', 0)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(FALLING)
    sprite('am405_10', 3)
    CreateParticle('amef_airmove_skr', 0)
    sprite('am405_11', 3)
    CreateParticle('amef_airmove_skr', 0)


@State
def Act2Event_WalkEntry_amvsce():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('am030_00', 7)
    physicsXImpulse(4800)
    label(0)
    sprite('am030_01', 7)
    sprite('am030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_03', 7)
    sprite('am030_04', 7)
    sprite('am030_05', 7)
    sprite('am030_06', 7)
    sprite('am030_07', 7)
    sprite('am030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('am030_09', 7)
    sprite('am030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    CameraControlEnable(0)
    enterState('Act2EventChouhatsu')


@State
def Act2EventChouhatsu():
    sprite('am300_00', 6)
    label(0)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2EventChouhatsu_Camera():
    sprite('am000_00', 7)
    CameraControlEnable(1)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am300_00', 6)
    label(0)
    sprite('am300_01', 6)
    sprite('am300_02', 6)
    sprite('am300_03', 6)
    sprite('am300_04', 6)
    sprite('am300_05', 6)
    sprite('am300_06', 6)
    sprite('am300_07', 6)
    sprite('am300_08', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2EventChouhatsuEnd():
    sprite('am300_09', 6)
    sprite('am300_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_YureMotion():
    sprite('am050_00', 4)
    CreateObject('Act2Event_Yure', -1)
    sprite('am050_01', 6)
    sprite('am050_02', 8)
    sprite('am050_01', 8)
    sprite('am050_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_novsam_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('am040_03', 5)
    sprite('am090_00', 12)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('am090_01', 7)
    AddInertia(-11000)
    sprite('am090_02', 7)
    sprite('am090_03', 7)
    sprite('am090_04', 7)
    sprite('am620_00', 6)
    sprite('am620_01', 6)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('am620_02', 6)
    sprite('am620_03', 6)
    sprite('am620_04', 6)
    sprite('am620_05', 6)
    sprite('am620_06', 6)
    sprite('am620_07', 12)
    sprite('am620_08', 32767)
    loopRest()


@State
def Act3Event_vhvsam_00():
    sprite('am333_00', 5)
    sprite('am333_01', 5)
    sprite('am333_02', 5)
    sprite('am333_03', 32767)


@State
def Act3Event_vhvsam_01():
    sprite('am333_04', 3)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(3000, 60000)
    SetActionMark(5)
    label(9)
    sprite('am333_05', 3)
    AddActionMark(-1)
    sprite('am333_06', 3)
    sprite('am333_07', 3)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(9)
    sprite('am333_08', 5)
    sprite('am333_09', 5)
    sprite('am333_10', 5)
    sprite('am333_11', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsph_00_Loop():
    sprite('am001_00', 6)
    sprite('am001_01', 7)
    sprite('am001_02', 7)
    sprite('am001_03', 7)
    sprite('am001_04', 32767)


@State
def Act3Event_amvsph_00_LoopEnd():
    sprite('am001_05', 7)
    sprite('am001_06', 7)
    sprite('am001_07', 7)
    sprite('am001_08', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsph_01():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        EnableCollision(0)
        ScreenCollision(0)
    sprite('am430_00', 4)
    AddX(-80000)
    sprite('am430_01', 3)
    AddX(-60000)
    DistortionSettings(30, -1, 0)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('am430_02', 3)
    AddX(-40000)
    sprite('am430_03', 3)
    AddX(-20000)
    sprite('am430_04', 3)
    sprite('am430_05', 18)
    sprite('am430_05', 2)
    EndMomentum(1)
    sprite('am430_06', 3)
    CreateObject('430_tossindril', 0)
    CreateObject('430_roop', 1)
    PreDashEffects(100, 1, 1)
    sprite('am430_07', 1)
    ObjectUpon(22, 32)
    AbsoluteY(1)
    physicsXImpulse(80000)
    AirDashEffects(1)
    sprite('am430_07', 1)
    CreateObject('Act3Event_vsphCamera', -1)
    sprite('am430_08', 1)
    AirDashEffects(1)
    sprite('am430_08', 1)
    sprite('am430_08', 1)
    sprite('am430_09', 1)
    setInvincible(0)
    sprite('am430_09', 1)
    sprite('am430_09', 1)
    TriggerUponForState('430_tossindril', 32)
    TriggerUponForState('430_roop', 32)
    sprite('am430_10', 6)
    AbsoluteY(0)
    XImpulseAcceleration(60)
    sprite('am430_27', 6)
    XImpulseAcceleration(50)
    DashEffects(100, 1, 1)
    sprite('am430_28', 6)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 1)
    sprite('am430_29', 6)
    DashEffects(100, 1, 1)
    sprite('am430_30', 6)
    physicsXImpulse(0)
    SetBackground(0)
    sprite('am430_30', 3)
    sprite('am430_31', 4)
    sprite('am430_32', 4)
    sprite('am430_33', 4)
    sprite('am430_34', 4)
    sprite('am430_35', 4)
    loopRest()
    sprite('am003_01ex', 3)
    Flip()
    sprite('am003_00', 3)
    sprite('am003_01', 3)
    label(0)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    gotoLabel(0)


@State
def Act3Event_amvsph_02():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
    sprite('am615_00', 6)
    sprite('am615_01', 6)
    sprite('am615_02', 6)
    sprite('am615_03', 6)
    sprite('am615_04', 6)
    CommonSE('019_cloth_a')
    sprite('am615_05', 6)
    sprite('am615_06', 6)
    sprite('am615_07', 32767)
    loopRest()


@State
def Act3Event_amvsiz_00_Loop():
    sprite('am450_00', 6)
    sprite('am450_01', 6)
    sprite('am450_02', 6)
    sprite('am450_03', 6)
    sprite('am450_04', 6)
    sprite('am450_05', 6)
    sprite('am450_06', 6)
    label(0)
    sprite('am450_07', 7)
    sprite('am450_08', 7)
    sprite('am450_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_amvsiz_00_LoopEnd():
    sprite('am450_25', 6)
    sprite('am450_26', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsiz_01():
    sprite('am213_15', 32767)


@State
def Act3Event_amvsiz_02():
    sprite('am213_16', 5)
    sprite('am213_17', 5)
    sprite('am213_18', 5)
    sprite('am213_19', 5)
    sprite('am213_20', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsiz_03():

    def upon_IMMEDIATE():

        def upon_32():
            CreateObject('Act3Event_vsizCamera', -1)
    sprite('am003_01ex', 3)
    Flip()
    CreateObject('Act3Event_CreateKK', -1)
    sprite('am003_00', 3)
    sprite('am003_01', 3)
    label(0)
    sprite('am000_00', 7)
    sprite('am000_01', 7)
    sprite('am000_02', 7)
    sprite('am000_03', 7)
    sprite('am000_04', 7)
    sprite('am000_05', 7)
    sprite('am000_06', 7)
    sprite('am000_07', 7)
    sprite('am000_08', 7)
    sprite('am000_09', 7)
    sprite('am000_10', 7)
    sprite('am000_11', 7)
    sprite('am000_12', 7)
    sprite('am000_13', 7)
    sprite('am000_14', 7)
    sprite('am000_15', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_amvsiz_04():
    sprite('keep', 1)
    CreateObject('Act3Event_vsizCamera', -1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsha_00():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
    sprite('am000_00', 5)
    sprite('am000_01', 5)
    sprite('am201_00', 2)
    sprite('am201_01', 2)
    sprite('am201_02', 2)
    sprite('am201_03', 2)
    sprite('am201_04', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('am201_05', 16)
    CreateObject('Eventoffset_Sosai', -1)
    sprite('am201_06', 2)
    RefreshMultihit()
    sprite('am201_07', 2)
    RefreshMultihit()
    sprite('am235_00', 2)
    sprite('am235_01', 2)
    sprite('am235_02', 2)
    sprite('am235_03', 2)
    sprite('am235_04', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('am235_05', 12)
    CreateObject('Eventoffset_Sosai2', -1)
    sprite('am312_00', 3)
    sprite('am312_01', 3)
    sprite('am312_02', 3)
    sprite('am312_03', 3)
    sprite('am312_04', 3)
    sprite('am312_05', 3)
    sprite('am312_06', 3)
    CreateObject('Act3Event_NagenukeEff', -1)
    CommonSE('107_throw_comeout')
    ObjectUpon(22, 32)
    sprite('am312_07', 3)
    sprite('am312_08', 3)
    sprite('am312_09', 3)
    loopRest()
    enterState('CmnActStand')
