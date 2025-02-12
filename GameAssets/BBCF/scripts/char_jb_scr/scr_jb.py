@Subroutine
def PreInit():
    CharacterID('jb')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(4200)
    WalkBSpeed(3300)
    DashFInitialVelocity(17500)
    DashFAccel(2500)
    DashFMaxVelocity(30000)
    JumpYVelocity(40000)
    SuperJumpYVelocity(50000)
    ForwardJumpVelocity(10000)
    ForwardSuperJumpVelocity(15000)
    BackwardJumpVelocity(10000)
    BackwardSuperJumpVelocity(15000)
    Gravity(2000)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(0)
    FootstepSE(1)
    CreateDecalOn(1)
    ResourceGauge(0, 1, 75, 1, 1, 0, 0, 0)
    HideResourceGauge(0, 1)
    DisableResourceGaugeBar(0, 1)
    ResourceGauge(1, 0, 0, 1, 600, 0, 0, 0)
    CPUJumpPriority(2000)
    CPURetreatPriority(500)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('FDash_Turn', 0x1)
    Move_Input_(0x78)
    Move_Input_(0xa7)
    Move_Input_(0x59)
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('BDash2FDash', 0x1)
    Move_Input_(0x79)
    FollowupOnly(1)
    SkillEstimateRange(600000, 1500000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(750)
    SkillEstimateRange(0, 250000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x1)
    SharedGatling('NmlAtk5A')
    Move_Input_(0x6c)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 275000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x1)
    SharedGatling('NmlAtk5A')
    Move_Input_(0x6c)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 300000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    DamageStunPriority(1)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(2500)
    MoveComboPriority(0)
    DamageStunPriority(0)
    SkillEstimateRange(-100000, 400000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2A_2nd', 0x1)
    SharedGatling('NmlAtk2A')
    Move_Input_(0x45)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2A_3rd', 0x1)
    SharedGatling('NmlAtk2A')
    Move_Input_(0x45)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 370000, -200000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMaxChainRepeat(1)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(2500)
    DamageStunPriority(0)
    MoveComboPriority(0)
    SkillEstimateRange(-100000, 300000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    AirborneOpponentPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 450000, -100000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    DamageStunPriority(500)
    SkillEstimateRange(200000, 450000, -200000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveMid()
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 450000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    AirborneOpponentPriority(6000)
    SkillEstimateRange(-100000, 350000, 100000, 450000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    DamageStunPriority(750)
    SkillEstimateRange(0, 400000, -100000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5D', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303c)
    OpponentAttackPriority(1)
    DamageStunPriority(250)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(250)
    SkillEstimateRange(-50000, 300000, -350000, 50000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(-100000, 400000, -150000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    AirborneOpponentPriority(1)
    SkillEstimateRange(-100000, 350000, -400000, -200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x303c)
    GuardStunPriority(0)
    DamageStunPriority(250)
    SkillEstimateRange(-100000, 300000, -500000, -300000, 500, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR6D', 0x1)
    Move_Condition(0x2001)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303c)
    OpponentAttackPriority(5000)
    GuardStunPriority(0)
    DamageStunPriority(250)
    SkillEstimateRange(250000, 600000, -500000, -300000, 100, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5D_SP', 0x1)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x304d)
    CallSkillConditions('NmlAtk5D_SP_Check')
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(500000, 1500000, -400000, 400000, 250, 10)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    AddChain(1)
    Move_EndRegister()
    Move_Register('ShortBackDash', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_44)
    FollowupOnly(1)
    AddChain(1)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(300000, 800000, -200000, 800000, 1, 1000)
    Move_EndRegister()
    Move_Register('AirShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Condition(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveComboPriority(0)
    SkillEstimateRange(800000, 1500000, -500000, -200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x303c)
    OpponentAttackPriority(1)
    GuardStunPriority(3000)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x303c)
    OpponentAttackPriority(1)
    GuardStunPriority(0)
    SkillEstimateRange(-600000, 425000, -200000, 500000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_1', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x304d)
    CallSkillConditions('HexaEdge_1_Check')
    OpponentAttackPriority(1)
    GuardStunPriority(3000)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 1000, 1)
    Move_EndRegister()
    Move_Register('HexaEdge_2', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    Move_Condition(0x304d)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_3', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    Move_Condition(0x304d)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_4', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    Move_Condition(0x304d)
    AirborneOpponentPriority(2000)
    GuardStunPriority(1)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_Blow', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    Move_Condition(0x304d)
    GuardStunPriority(1)
    SkillEstimateRange(-50000, 400000, -200000, 50000, 500, 500)
    Move_EndRegister()
    Move_Register('HexaEdge_Upper', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    Move_Condition(0x304d)
    SkillEstimateRange(-400000, 400000, -200000, 350000, 1000, 10)
    Move_EndRegister()
    Move_Register('HexaEdge_Low', INPUT_SPECIALMOVE)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    Move_Condition(0x304d)
    MoveLow()
    AirborneOpponentPriority(1)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_Mid', INPUT_SPECIALMOVE)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    Move_Condition(0x304d)
    MoveMid()
    GuardStunPriority(2000)
    SkillEstimateRange(-400000, 350000, -200000, 50000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_Multi', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    Move_Condition(0x304d)
    GuardStunPriority(1)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 1)
    Move_EndRegister()
    Move_Register('HexaEdge_Chage', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_646)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    Move_Condition(0x304d)
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(-400000, 400000, -200000, 150000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_FrontDash', INPUT_SPECIALMOVE)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    Move_Condition(0x304d)
    GuardStunPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(-700000, 700000, -300000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('HexaEdge_BackDash', INPUT_SPECIALMOVE)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    Move_Condition(0x304d)
    GuardStunPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(-700000, 700000, -300000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('Assault_Low', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    MoveLow()
    GuardStunPriority(4000)
    SkillEstimateRange(-600000, 450000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Assault_Mid', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(1)
    GuardStunPriority(4000)
    SkillEstimateRange(-600000, 450000, -100000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirAssault_Mid', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    CallSkillConditions('AirAssault_Mid_Check')
    AirborneOpponentPriority(5000)
    GuardStunPriority(0)
    SkillEstimateRange(-50000, 300000, -50000, 200000, 50, 1)
    Move_EndRegister()
    Move_Register('Assault_Multi', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AirAssault_Multi', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    SkillEstimateRange(-50000, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Assault_ChageAttack', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    MoveButtonHoldTime(2, 1, 30)
    GuardStunPriority(6000)
    SkillEstimateRange(-50000, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirMoveFront', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('AirMove_Check')
    GuardStunPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(-150000, 350000, -400000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('AirMoveBack', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('AirMove_Check')
    GuardStunPriority(6000)
    DamageStunPriority(1)
    SkillEstimateRange(-150000, 350000, -400000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(5000)
    DamageStunPriority(1)
    GuardStunPriority(0)
    TempPriorityMultiplierInterval(1, 0, 1, 0, 4000)
    SkillEstimateRange(0, 500000, -200000, 200000, 1, 100)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Condition(0x3081)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(5000)
    DamageStunPriority(1)
    GuardStunPriority(0)
    TempPriorityMultiplierInterval(1, 0, 1, 0, 4000)
    SkillEstimateRange(0, 500000, -200000, 200000, 1, 100)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(3000)
    GuardStunPriority(0)
    DamageStunPriority(0)
    SkillEstimateRange(50000, 350000, -600000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateAirAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Condition(0x3081)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(3000)
    GuardStunPriority(0)
    DamageStunPriority(0)
    SkillEstimateRange(50000, 350000, -600000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateChage', INPUT_DISTORTION)
    Move_Condition(0x303c)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xca)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    Move_EndRegister()
    Move_Register('UltimateChageEX', INPUT_DISTORTION)
    Move_Condition(0x304d)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xca)
    Move_Input_(INPUT_PRESS_A)
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_6321463214)
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
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'Assault_B', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'Assault_Low', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'UltimateAssault', 50000000)
    TempPriorityMultiplier('NmlAtk5D', 'UltimateAssault_OD', 50000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Assault_A', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'HexaEdge_1', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'AirAssault_Mid', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'HexaEdge_1', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AN_NmlAtkAIR6D', 50000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirAssault_Mid', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'HexaEdge_1', 10000000)
    TempPriorityMultiplier('AN_NmlAtkAIR6D', 'Assault_B', 10000000)
    TempPriorityMultiplier('AN_NmlAtkAIR6D', 'Assault_Low', 10000000)
    TempPriorityMultiplier('AN_NmlAtkAIR6D', 'UltimateAssault', 50000000)
    TempPriorityMultiplier('AN_NmlAtkAIR6D', 'UltimateAssault_OD', 50000000)
    TempPriorityMultiplier('HexaEdge_1', 'HexaEdge_2', 10000000)
    TempPriorityMultiplier('HexaEdge_2', 'HexaEdge_3', 10000000)
    TempPriorityMultiplier('HexaEdge_3', 'HexaEdge_4', 10000)
    TempPriorityMultiplier('HexaEdge_3', 'HexaEdge_Upper', 10000)
    TempPriorityMultiplier('HexaEdge_4', 'HexaEdge_Blow', 10000)
    TempPriorityMultiplier('HexaEdge_4', 'HexaEdge_Low', 10000)
    TempPriorityMultiplier('HexaEdge_Upper', 'HexaEdge_Blow', 10000)
    TempPriorityMultiplier('HexaEdge_Upper', 'HexaEdge_Multi', 10000)
    TempPriorityMultiplier('HexaEdge_Upper', 'HexaEdge_Mid', 10000)
    TempPriorityMultiplier('HexaEdge_Upper', 'HexaEdge_Chage', 10000)
    TempPriorityMultiplier('Assault_Low', 'Shot', 10000000)
    TempPriorityMultiplier('HexaEdge_Low', 'Shot', 10000000)
    StylishModeSpecialButton('Assault_A', 0x4, 0xea)
    StylishModeSpecialButton('HexaEdge_1', 0x4, 0xea)
    StylishModeSpecialButton('Assault_Low', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('Shot', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault_Multi', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAirAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAirAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('AirShot', 0x4, 0x45)
    StylishModeSpecialButton('HexaEdge_2', 0x4, 0xea)
    StylishModeSpecialButton('HexaEdge_3', 0x4, 0xea)
    StylishModeSpecialButton('HexaEdge_4', 0x4, 0xea)
    StylishModeSpecialButton('HexaEdge_Blow', 0x4, 0xea)
    StylishModeSpecialButton('HexaEdge_Low', 0x4, 0x79)
    StylishModeSpecialButton('HexaEdge_Mid', 0x4, 0x5f)
    StylishModeCancels('NmlAtk5A', 'NmlAtk2B', 13, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 2, 120000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk3C', 3, 0)
    StylishModeCancels('NmlAtk5B', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk5C', 'Assault_Mid', 13, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 3, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D', 6, 0)
    StylishModeCancels('NmlAtk5C', 'HexaEdge_1', 6, 0)
    StylishModeCancels('NmlAtk5C', 'Assault_ChageAttack', 8, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 10, 1200000)
    StylishModeCancels('NmlAtk6C', 'Assault_Mid', 13, 0)
    StylishModeCancels('NmlAtk6C', 'UltimateChage', 13, 0)
    StylishModeCancels('NmlAtk6C', 'HexaEdge_1', 13, 0)
    StylishModeCancels('NmlAtk6C', 'Assault_ChageAttack', 6, 0)
    StylishModeCancels('NmlAtk6C', 'UltimateChage', 6, 0)
    StylishModeCancels('NmlAtk5D', 'Assault_B', 6, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk5D', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 2, 120000)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 13, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 1, 150000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 6, 0)
    StylishModeCancels('NmlAtk2C', 'AirAssault_Mid', 13, 0)
    StylishModeCancels('NmlAtk2C', 'HexaEdge_1', 0, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk3C', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk3C', 'Assault_Mid', 13, 0)
    StylishModeCancels('NmlAtk3C', 'Assault_A', 2, 150000)
    StylishModeCancels('NmlAtk3C', 'HexaEdge_1', 2, 150000)
    StylishModeCancels('NmlAtkAIR5A', 'Assault_A', 0, 0)
    StylishModeCancels('NmlAtkAIR5A', 'HexaEdge_1', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'AirAssault_Multi', 6, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR2C', 'AirAssault_Multi', 3, 0)
    StylishModeCancels('NmlAtkAIR5D', 'Assault_B', 6, 0)
    StylishModeCancels('NmlAtkAIR5D', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtkAIR5D', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('AN_NmlAtkAIR6D', 'Assault_B', 6, 0)
    StylishModeCancels('AN_NmlAtkAIR6D', 'UltimateAssault', 6, 0)
    StylishModeCancels('AN_NmlAtkAIR6D', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('NmlAtk5D_SP', 'UltimateAirAssault_OD', 6, 0)
    StylishModeCancels('Atk6AExe', 'Assault_B', 6, 0)
    StylishModeCancels('Atk6AExe', 'HexaEdge_1', 6, 0)
    StylishModeCancels('Atk6AExe', 'AstralHeat', 6, 0)
    StylishModeCancels('Atk6BExe', 'Assault_ChageAttack', 6, 0)
    StylishModeCancels('Atk6BExe', 'AstralHeat', 6, 0)
    StylishModeCancels('ThrowExe', 'Assault_B', 0, 0)
    StylishModeCancels('ThrowExe', 'HexaEdge_1', 0, 0)
    StylishModeCancels('ThrowExe', 'UltimateChage', 0, 0)
    StylishModeCancels('ThrowExe', 'Assault_A', 10, 800000)
    StylishModeCancels('BackThrowExe', 'Assault_B', 0, 0)
    StylishModeCancels('BackThrowExe', 'HexaEdge_1', 0, 0)
    StylishModeCancels('BackThrowExe', 'UltimateChage', 0, 0)
    StylishModeCancels('BackThrowExe', 'Assault_A', 10, 800000)
    StylishModeCancels('AirThrowExe', 'Assault_B', 0, 0)
    StylishModeCancels('AirThrowExe', 'HexaEdge_1', 0, 0)
    StylishModeCancels('AirThrowExe', 'Assault_A', 10, 800000)
    StylishModeCancels('HexaEdge_1', 'HexaEdge_Upper', 0, 0)
    StylishModeCancels('HexaEdge_1', 'HexaEdge_2', 2, 250000)
    StylishModeCancels('HexaEdge_2', 'HexaEdge_Upper', 0, 0)
    StylishModeCancels('HexaEdge_2', 'HexaEdge_3', 2, 250000)
    StylishModeCancels('HexaEdge_3', 'HexaEdge_Upper', 6, 0)
    StylishModeCancels('HexaEdge_3', 'HexaEdge_4', 13, 0)
    StylishModeCancels('HexaEdge_4', 'HexaEdge_Blow', 0, 0)
    StylishModeCancels('HexaEdge_4', 'HexaEdge_Mid', 13, 0)
    StylishModeCancels('HexaEdge_Upper', 'HexaEdge_Multi', 0, 0)
    StylishModeCancels('HexaEdge_Upper', 'HexaEdge_Blow', 10, 1000000)
    StylishModeCancels('Assault_Low', 'Shot', 6, 0)
    StylishModeCancels('Assault_Low', 'UltimateChage', 6, 0)
    StylishModeCancels('Assault_Low', 'UltimateChage', 13, 0)
    StylishModeCancels('Assault_Multi', 'UltimateChage', 0, 0)
    StylishModeCancels('AirAssault_Multi', 'UltimateChage', 0, 0)
    HitSprites(0, 'jb062_01')
    HitSprites(1, 'jb062_03')
    HitSprites(2, 'jb062_04')
    HitSprites(3, 'jb062_05')
    HitSprites(4, 'jb062_05')
    HitSprites(5, 'jb062_06')
    HitSprites(6, 'jb062_07')
    HitSprites(7, 'jb041_02')
    HitSprites(8, 'jb040_02')
    HitSprites(9, 'jb045_02')
    HitSprites(10, 'jb060_00')
    HitSprites(11, 'jb060_01')
    HitSprites(12, 'jb060_03')
    HitSprites(13, 'jb060_05')
    HitSprites(14, 'jb060_07')
    HitSprites(15, 'jb060_14')
    HitSprites(16, 'jb050_00')
    HitSprites(17, 'jb052_00')
    HitSprites(18, 'jb054_00')
    HitSprites(19, 'jb000_00')
    HitSprites(20, 'jb000_00')
    HitSprites(25, 'jb063_00')
    HitSprites(26, 'jb063_01')
    HitSprites(27, 'jb063_02')
    HitSprites(28, 'jb063_04')
    HitSprites(29, 'jb063_10')
    HitSprites(30, 'jb077_00')
    HitSprites(31, 'jb077_01')
    HitSprites(32, 'jb077_00ex00')
    HitSprites(33, 'jb077_01ex00')
    HitSprites(34, 'jb077_00ex01')
    HitSprites(35, 'jb077_01ex01')
    HitSprites(36, 'jb077_00ex02')
    HitSprites(37, 'jb077_01ex02')
    HitSprites(24, 'jb073_01')
    CommonVoicelines(0, 'jb000')
    CommonVoicelines(1, 'jb001')
    CommonVoicelines(2, 'jb002')
    CommonVoicelines(3, 'jb003')
    CommonVoicelines(4, 'jb004')
    CommonVoicelines(5, 'jb005')
    CommonVoicelines(6, 'jb006')
    CommonVoicelines(7, 'jb007')
    CommonVoicelines(8, 'jb008')
    CommonVoicelines(9, 'jb009')
    CommonVoicelines(10, 'jb010')
    CommonVoicelines(11, 'jb011')
    CommonVoicelines(12, 'jb012')
    CommonVoicelines(13, 'jb013')
    CommonVoicelines(14, 'jb014')
    CommonVoicelines(15, 'jb015')
    CommonVoicelines(16, 'jb016')
    CommonVoicelines(17, 'jb017')
    CommonVoicelines(18, 'jb018')
    CommonVoicelines(19, 'jb019')
    CommonVoicelines(20, 'jb020')
    CommonVoicelines(21, 'jb021')
    CommonVoicelines(22, 'jb022')
    CommonVoicelines(23, 'jb023')
    CommonVoicelines(24, 'jb024')
    CommonVoicelines(25, 'jb025')
    CommonVoicelines(26, 'jb026')
    CommonVoicelines(27, 'jb027')
    CommonVoicelines(28, 'jb028')
    CommonVoicelines(29, 'jb029')
    CommonVoicelines(30, 'jb030')
    CommonVoicelines(31, 'jb031')
    CommonVoicelines(32, 'jb032')
    CommonVoicelines(33, 'jb033')
    CommonVoicelines(34, 'jb034')
    CommonVoicelines(35, 'jb035')
    CommonVoicelines(36, 'jb036')
    CommonVoicelines(37, 'jb037')
    CommonVoicelines(38, 'jb038')
    CommonVoicelines(39, 'jb039')
    CommonVoicelines(40, 'jb040')
    CommonVoicelines(41, 'jb041')
    CommonVoicelines(42, 'jb042')
    CommonVoicelines(43, 'jb043')
    CommonVoicelines(44, 'jb044')
    CommonVoicelines(45, 'jb045')
    CommonVoicelines(46, 'jb046')
    CommonVoicelines(47, 'jb047')
    CommonVoicelines(48, 'jb048')
    CommonVoicelines(49, 'jb049')
    CommonVoicelines(50, 'jb050')
    CommonVoicelines(51, 'jb051')
    CommonVoicelines(52, 'jb052')
    CommonVoicelines(53, 'jb053')
    CommonVoicelines(54, 'jb100')
    CommonVoicelines(55, 'jb101')
    CommonVoicelines(56, 'jb102')
    CommonVoicelines(57, 'jb103')
    CommonVoicelines(58, 'jb104')
    CommonVoicelines(59, 'jb105')
    CommonVoicelines(60, 'jb106')
    CommonVoicelines(61, 'jb107')
    CommonVoicelines(62, 'jb108')
    CommonVoicelines(63, 'jb109')
    CommonVoicelines(64, 'jb150')
    CommonVoicelines(65, 'jb151')
    CommonVoicelines(66, 'jb152')
    CommonVoicelines(67, 'jb153')
    CommonVoicelines(68, 'jb154')
    CommonVoicelines(69, 'jb155')
    CommonVoicelines(70, 'jb156')
    CommonVoicelines(71, 'jb157')
    CommonVoicelines(72, 'jb158')
    CommonVoicelines(75, 'jb160')
    CommonVoicelines(73, 'jb402')
    CommonVoicelines(74, 'jb403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def HexaEdge_1_Check():
    SLOT_47 = 0
    if not SLOT_59:
        SLOT_47 = 1


@Subroutine
def AirMove_Check():
    SLOT_47 = 0
    if not SLOT_60:
        SLOT_47 = 1


@Subroutine
def AirAssault_Mid_Check():
    SLOT_47 = 0
    if not SLOT_61:
        SLOT_47 = 1


@Subroutine
def NmlAtk5D_SP_Check():
    SLOT_47 = 0
    if not SLOT_63:
        SLOT_47 = 1


@Subroutine
def OnDamage():
    if SLOT_IsGrounded:
        SLOT_59 = 0
        SLOT_60 = 0
        SLOT_61 = 0
        SLOT_62 = 0
        SLOT_63 = 0


@Subroutine
def OnLanding():
    SLOT_59 = 0
    SLOT_60 = 0
    SLOT_61 = 0
    SLOT_62 = 0
    SLOT_63 = 0


@Subroutine
def OnFrameStep():
    if not SLOT_21:
        SLOT_32 = 0
        if CheckObjectPresence(7):
            DeleteObject(7)
    if SLOT_32:
        if not SLOT_81:
            SLOT_32 = SLOT_32 + -1
        if not CheckObjectPresence(6):
            CreateObject('MarkingPoint', -1)
            RegisterObject(6, 1)
    else:
        SLOT_32 = 0
        if CheckObjectPresence(6):
            ObjectUpon(6, 32)
    if SLOT_31:
        if not CheckObjectPresence(7):
            CreateObject('ChageAuraGenerator', -1)
            RegisterObject(7, 1)
    TrainingModeSLOT('TRI_JubeiPowerUp', 2, 67)
    if SLOT_67:
        if SLOT_67 == 1:
            if SLOT_21:
                SLOT_31 = 1
                if not CheckObjectPresence(7):
                    CreateObject('ChageAuraGenerator', -1)
                    RegisterObject(7, 1)


@Subroutine
def OnFinalize():
    pass


@Subroutine
def OnPreDraw():
    pass


@Subroutine
def MatchInit():
    pass


@Subroutine
def AddChainD():
    HitOrBlockCancel('NmlAtk5D')
    HitOrBlockCancel('NmlAtkAIR5D')
    HitOrBlockCancel('AN_NmlAtkAIR6D')
    HitOrBlockCancel('NmlAtk5D_SP')


@Subroutine
def __5A_AtkData():
    AttackDefaults_StandingNormal()
    AttackLevel_(1)
    Damage(300)
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
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')
    callSubroutine('AddChainD')


@Subroutine
def __2A_AtkData():
    AttackDefaults_CrouchingNormal()
    AttackLevel_(1)
    Damage(300)
    AirPushbackY(13000)
    PushbackX(12000)
    HitAirUnblockable(0)
    StarterRating(2)
    HitOrBlockCancel('NmlAtk5A')
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
    callSubroutine('AddChainD')


@Subroutine
def HexaEdge_Atk():
    AttackLevel_(3)
    Damage(600)
    AttackP1(80)
    AttackP2(94)
    AirPushbackX(24000)
    AirPushbackY(14000)
    Hitstun(19)
    AirUntechableTime(21)
    Hitstop(7)
    UseSlashHitspark(1)
    if SLOT_137:
        DamageMultiplier(80)
    HitOrBlockCancel('UltimateChage')


@Subroutine
def AssaultUpper_Atk():
    Damage(600)
    ResetPushback()
    AirPushbackY(30000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirUntechableTime(40)
    if SLOT_137:
        DamageMultiplier(80)
    HitOrBlockCancel('UltimateChage')


@Subroutine
def AssaultFinish_Atk():
    Damage(900)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(30000)
    AirPushbackY(18000)
    AirUntechableTime(40)
    Hitstop(11)
    EnemyHitstopAddition(0, 2, 4)
    MoveAttributes(1, 0, 0, 0, 0)
    if SLOT_137:
        DamageMultiplier(80)


@Subroutine
def Assault_Low_Atk():
    AttackLevel_(4)
    Damage(950)
    AttackP1(90)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(5000)
    AirPushbackX(20000)
    CHAirPushbackY(20000)
    CHAirPushbackX(-1000)
    YImpulseBeforeWallbounce(3000)
    HardKnockdown(1)
    AirUntechableTime(30)
    HitLow(2)
    UseSlashHitspark(1)
    FatalCounter(1)
    MoveAttributes(0, 0, 1, 0, 0)
    if SLOT_137:
        DamageMultiplier(80)

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        Hitstop(20)
        ScreenShake(5000, 3000)


@Subroutine
def Assault_Mid_Atk():
    AttackLevel_(4)
    Damage(870)
    AttackP1(80)
    GroundedHitstunAnimation(3)
    AirPushbackX(20000)
    AirPushbackY(-50000)
    Floorslide(1)
    Hitstun(23)
    AirUntechableTime(40)
    HardKnockdown(1)
    PushbackX(19800)
    HitOverhead(2)
    StarterRating(2)
    UseSlashHitspark(1)
    MoveAttributes(1, 0, 0, 0, 0)
    if SLOT_137:
        DamageMultiplier(80)


@Subroutine
def Assault_Multi_Atk():
    AttackLevel_(3)
    Damage(300)
    AttackP2(79)
    SingleProration(1)
    AirPushbackY(-20000)
    PushbackX(12000)
    AirUntechableTime(60)
    HardKnockdown(10)
    Hitstop(1)
    EnemyHitstopAddition(0, -1, -1)
    UseSlashHitspark(1)
    HitsparkSize(600)
    StarterRating(2)
    MoveAttributes(1, 0, 0, 0, 0)
    AttackDirection(0)
    if SLOT_137:
        DamageMultiplier(80)


@Subroutine
def Assault_MultiFinish_Atk():
    Damage(600)
    Hitstop(11)
    EnemyHitstopAddition(0, 0, 2)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(20000)
    ResetGravity()
    PushbackX(19800)
    HardKnockdown(-1)
    HitsparkSize(1000)
    MoveAttributes(0, 1, 0, 0, 0)
    AttackDirection(1)
    if SLOT_137:
        DamageMultiplier(80)


@Subroutine
def Assault_Chage_Atk():
    AttackLevel_(5)
    Damage(1100)
    AttackP1(90)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(1000)
    YImpulseBeforeWallbounce(1800)
    AirUntechableTime(60)
    PushbackX(19800)
    Hitstop(20)
    StarterRating(2)
    UseSlashHitspark(1)
    FatalCounter(1)
    if SLOT_137:
        DamageMultiplier(80)

    def upon_OPPONENT_HIT_OR_BLOCK():
        ScreenShake(8000, 8000)

    def upon_EVERY_FRAME():
        if SLOT_IsGrounded:
            if SLOT_StateDuration >= 17:
                if not SLOT_2:
                    if CheckInput(0x17):
                        sendToLabel(8)
            if SLOT_StateDuration == 30:
                if not SLOT_2:
                    Damage(1600)
                    AirPushbackY(32000)
                    AttackP1(50)
                    HitOverhead(4)
                    HitLow(4)
                    HitAirUnblockable(4)
                    StarterRating(0)
                    if SLOT_137:
                        DamageMultiplier(80)
                    AltKnockdownEffects(100, 1, 1)
                    SetActionMark(1)
            if SLOT_StateDuration >= 44:
                sendToLabel(9)


@Subroutine
def DriveInit():
    AttackLevel_(4)
    Damage(300)
    AttackP1(80)
    OppPositionOnHit(3, -60000, 0)
    PushbackX(0)
    Hitstop(0)
    EnemyHitstopAddition(12, 24, 29)
    StarterRating(2)
    UseSlashHitspark(1)
    HitOverhead(0)
    SLOT_58 = SLOT_OverdriveTimer
    SpecialCancel(0)
    WhiffCrouchBlockCancel(1)

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        clearUponHandler(OPPONENT_BLOCKS)
        CreateObject('Drive_AddAtk', -1)
        TeleportToObject(22)
        AbsoluteY(0)
        AlphaValue(0)
        SLOT_59 = 0
        SLOT_60 = 0
        SLOT_61 = 0
        SLOT_62 = 0
        SLOT_63 = 0
        if CurrentStateCheck('NmlAtk5D'):
            CreateObject('jbef_DriveHit', -1)
        else:
            if CurrentStateCheck('NmlAtkAIR5D'):
                CreateObject('jbef_Air5DHit', -1)
            elif CurrentStateCheck('AN_NmlAtkAIR6D'):
                CreateObject('jbef_Air6DHit', -1)
            clearUponHandler(LANDING)
            LandingEffects(100, 1, 1)
            EndMomentum(1)
        sendToLabel(0)
    if SLOT_58:

        def upon_OPPONENT_BLOCKS():
            clearUponHandler(OPPONENT_HIT)
            clearUponHandler(OPPONENT_BLOCKS)
            CreateObject('Drive_AddAtk', -1)
            TeleportToObject(22)
            AbsoluteY(0)
            AlphaValue(0)
            SLOT_59 = 0
            SLOT_60 = 0
            SLOT_61 = 0
            SLOT_62 = 0
            SLOT_63 = 0
            if CurrentStateCheck('NmlAtk5D'):
                CreateObject('jbef_DriveHit', -1)
            else:
                if CurrentStateCheck('NmlAtkAIR5D'):
                    CreateObject('jbef_Air5DHit', -1)
                elif CurrentStateCheck('AN_NmlAtkAIR6D'):
                    CreateObject('jbef_Air6DHit', -1)
                clearUponHandler(LANDING)
                LandingEffects(100, 1, 1)
                EndMomentum(1)
            sendToLabel(0)

    def upon_STATE_END():
        ForceFaceSprite()
        AlphaValue(255)


@Subroutine
def Drive_DeriveInputBegin():
    BeginBuffer('NmlAtkGuardCrush')
    BeginBuffer('Assault_A')
    BeginBuffer('Assault_B')
    BeginBuffer('Shot')
    BeginBuffer('Assault_Low')
    BeginBuffer('Assault_Mid')
    BeginBuffer('Assault_Multi')
    BeginBuffer('Assault_ChageAttack')
    BeginBuffer('UltimateAssault')
    BeginBuffer('UltimateAssault_OD')
    BeginBuffer('UltimateChage')


@Subroutine
def Drive_DeriveTimingBegin():
    BufferedOrPressedGoto('NmlAtkGuardCrush')
    BufferedOrPressedGoto('Assault_A')
    BufferedOrPressedGoto('Assault_B')
    BufferedOrPressedGoto('Shot')
    BufferedOrPressedGoto('Assault_Low')
    BufferedOrPressedGoto('Assault_Mid')
    BufferedOrPressedGoto('Assault_Multi')
    BufferedOrPressedGoto('Assault_ChageAttack')
    BufferedOrPressedGoto('UltimateAssault')
    BufferedOrPressedGoto('UltimateAssault_OD')
    BufferedOrPressedGoto('UltimateChage')


@Subroutine
def HE_DeriveInputBegin():
    BeginBuffer('HexaEdge_Upper')
    BeginBuffer('HexaEdge_Low')
    BeginBuffer('HexaEdge_Mid')
    BeginBuffer('HexaEdge_Multi')
    BeginBuffer('HexaEdge_Chage')
    BeginBuffer('HexaEdge_FrontDash')
    BeginBuffer('HexaEdge_BackDash')

    def upon_OPPONENT_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_HIT_OR_BLOCK)
        BufferedOrPressedGoto('HexaEdge_2')
        BufferedOrPressedGoto('HexaEdge_3')
        BufferedOrPressedGoto('HexaEdge_4')
        BufferedOrPressedGoto('HexaEdge_Upper')
        BufferedOrPressedGoto('HexaEdge_Blow')
        BufferedOrPressedGoto('HexaEdge_Low')
        BufferedOrPressedGoto('HexaEdge_Mid')
        BufferedOrPressedGoto('HexaEdge_Multi')
        BufferedOrPressedGoto('HexaEdge_Chage')
        BufferedOrPressedGoto('HexaEdge_FrontDash')
        BufferedOrPressedGoto('HexaEdge_BackDash')


@Subroutine
def HE_DeriveTimingBegin():
    BufferedOrPressedGoto('HexaEdge_2')
    BufferedOrPressedGoto('HexaEdge_3')
    BufferedOrPressedGoto('HexaEdge_4')
    BufferedOrPressedGoto('HexaEdge_Upper')
    BufferedOrPressedGoto('HexaEdge_Blow')
    BufferedOrPressedGoto('HexaEdge_Low')
    BufferedOrPressedGoto('HexaEdge_Mid')
    BufferedOrPressedGoto('HexaEdge_Multi')
    BufferedOrPressedGoto('HexaEdge_Chage')
    BufferedOrPressedGoto('HexaEdge_FrontDash')
    BufferedOrPressedGoto('HexaEdge_BackDash')


@Subroutine
def HE_DeriveClear():
    DisallowGoto('HexaEdge_2')
    DisallowGoto('HexaEdge_3')
    DisallowGoto('HexaEdge_4')
    DisallowGoto('HexaEdge_Upper')
    DisallowGoto('HexaEdge_Blow')
    DisallowGoto('HexaEdge_Low')
    DisallowGoto('HexaEdge_Mid')
    DisallowGoto('HexaEdge_Multi')
    DisallowGoto('HexaEdge_Chage')
    DisallowGoto('HexaEdge_FrontDash')
    DisallowGoto('HexaEdge_BackDash')


@State
def CmnActStand():
    label(0)
    sprite('jb000_00', 7)
    sprite('jb000_01', 7)
    sprite('jb000_02', 7)
    sprite('jb000_03', 7)
    sprite('jb000_04', 7)
    sprite('jb000_05', 7)
    sprite('jb000_06', 7)
    sprite('jb000_07', 7)
    sprite('jb000_08', 7)
    sprite('jb000_09', 7)
    if SLOT_87:
        if not SLOT_123:
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    sprite('jb000_00ex01', 7)
    sprite('jb000_01ex01', 7)
    sprite('jb000_02ex01', 7)
    sprite('jb000_03ex01', 7)
    sprite('jb000_04ex01', 7)
    sprite('jb000_05ex01', 7)
    sprite('jb000_06ex01', 7)
    sprite('jb000_07ex01', 7)
    sprite('jb000_08ex01', 7)
    sprite('jb000_09ex01', 7)
    if SLOT_87:
        if not SLOT_123:
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    sprite('jb000_00ex02', 7)
    sprite('jb000_01ex02', 7)
    sprite('jb000_02ex02', 7)
    sprite('jb000_03ex02', 7)
    sprite('jb000_04ex02', 7)
    sprite('jb000_05ex02', 7)
    sprite('jb000_06ex02', 7)
    sprite('jb000_07ex02', 7)
    sprite('jb000_08ex02', 7)
    sprite('jb000_09ex02', 7)
    if SLOT_87:
        if not SLOT_123:
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb001_00', 6)
    SLOT_88 = 960
    sprite('jb001_01', 6)
    sprite('jb001_02', 6)
    Voiceline('jb000')
    sprite('jb001_03', 6)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_03', 9)
    sprite('jb001_02', 9)
    sprite('jb001_01', 9)
    sprite('jb001_00', 9)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('jb003_00ex00', 3)
    sprite('jb003_01', 3)
    sprite('jb003_00', 3)


@State
def CmnActStand2Crouch():
    sprite('jb010_00', 4)
    sprite('jb010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('jb010_02', 7)
    sprite('jb010_03', 7)
    sprite('jb010_04', 7)
    sprite('jb010_05', 7)
    sprite('jb010_06', 7)
    sprite('jb010_07', 7)
    sprite('jb010_08', 7)
    sprite('jb010_09', 7)
    sprite('jb010_10', 7)
    sprite('jb010_11', 7)
    sprite('jb010_02ex01', 7)
    sprite('jb010_03ex01', 7)
    sprite('jb010_04ex01', 7)
    sprite('jb010_05ex01', 7)
    sprite('jb010_06ex01', 7)
    sprite('jb010_07ex01', 7)
    sprite('jb010_08ex01', 7)
    sprite('jb010_09ex01', 7)
    sprite('jb010_10ex01', 7)
    sprite('jb010_11ex01', 7)
    sprite('jb010_02ex02', 7)
    sprite('jb010_03ex02', 7)
    sprite('jb010_04ex02', 7)
    sprite('jb010_05ex02', 7)
    sprite('jb010_06ex02', 7)
    sprite('jb010_07ex02', 7)
    sprite('jb010_08ex02', 7)
    sprite('jb010_09ex02', 7)
    sprite('jb010_10ex02', 7)
    sprite('jb010_11ex02', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('jb013_00ex00', 3)
    sprite('jb013_01', 3)
    sprite('jb013_00', 3)


@State
def CmnActCrouch2Stand():
    sprite('jb010_01', 4)
    sprite('jb010_00', 4)


@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        if PreviousStateCheck('CmnActFDash'):
            JumpYVelocity(29000)
            ForwardJumpVelocity(5000)
            BackwardJumpVelocity(10000)
        elif PreviousStateCheck('BDash2FDash'):
            JumpYVelocity(29000)
            ForwardJumpVelocity(5000)
            BackwardJumpVelocity(10000)
            PerInertia(60)
        else:
            JumpYVelocity(36000)
            ForwardJumpVelocity(10000)
            BackwardJumpVelocity(8000)
            SuperJumpYVelocity(44000)
            ForwardSuperJumpVelocity(12000)
            BackwardSuperJumpVelocity(9600)
    sprite('jb023_00', 2)
    sprite('jb023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('jb020_00', 4)
    sprite('jb020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('jb020_02', 3)
    sprite('jb020_03', 3)
    sprite('jb020_04', 3)


@State
def CmnActJumpDown():
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(0)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('jb024_00', 3)
    sprite('jb024_01', 3)
    sprite('jb024_02', 3)
    sprite('jb024_03', 3)
    sprite('jb024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('jb024_00', 2)
    sprite('jb024_01', 2)
    sprite('jb024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('jb024_03', 3)
    sprite('jb024_04', 3)


@State
def CmnActFWalk():
    sprite('jb030_00', 7)
    label(0)
    sprite('jb030_01', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb030_02', 7)
    sprite('jb030_03', 7)
    sprite('jb030_04', 7)
    sprite('jb030_05', 7)
    sprite('jb030_06', 7)
    sprite('jb030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb030_08', 7)
    sprite('jb030_09', 7)
    sprite('jb030_10', 7)
    sprite('jb030_11', 7)
    sprite('jb030_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('jb031_00', 7)
    label(0)
    sprite('jb031_01', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb031_02', 7)
    sprite('jb031_03', 7)
    sprite('jb031_04', 7)
    sprite('jb031_05', 7)
    sprite('jb031_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb031_07', 7)
    sprite('jb031_08', 7)
    sprite('jb031_09', 7)
    sprite('jb031_10', 7)
    sprite('jb031_11', 7)
    sprite('jb031_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_StateDuration >= 8:
                if SLOT_19 <= 150000:
                    if SLOT_YRelativeToOpponent <= 100000:
                        WhiffCancel('FDash_Turn')

        def upon_STATE_END():
            if CheckInput(0x5e):
                PerInertia(0)
            elif CheckInput(0x37):
                PerInertia(0)
        WhiffCancelEnable(1)
    sprite('jb032_00', 2)
    sprite('jb032_01', 2)
    label(0)
    sprite('jb032_02', 4)
    DashEffects(100, 1, 1)
    sprite('jb032_03', 3)
    sprite('jb032_04', 3)
    sprite('jb032_05', 4)
    DashEffects(100, 1, 1)
    sprite('jb032_06', 3)
    sprite('jb032_07', 3)
    sprite('jb032_08', 3)
    loopRest()
    gotoLabel(0)


@State
def FDash_Turn():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        ExternalForcesRate(100, 100)
        SetZLine(0, 20)
        uponSendToLabel(LANDING, 1)
    sprite('jb033_00', 1)
    Flip()
    JumpSoundEffects()
    EndMomentum(1)
    physicsXImpulse(-25000)
    physicsYImpulse(15800)
    setGravity(2400)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    setInvincible(1)
    Voiceline('jb005')
    sprite('jb033_01', 3)
    sprite('jb033_02', 3)
    sprite('jb033_03', 3)
    setInvincible(0)
    sprite('jb033_04', 3)
    sprite('jb033_05', 32767)
    loopRest()
    label(1)
    sprite('jb033_06', 1)
    clearUponHandler(EVERY_FRAME)
    LandingEffects(100, 1, 1)
    SetZLine(1, 20)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    setInvincible(0)
    EndMomentum(1)
    sprite('jb033_07', 1)
    sprite('jb033_08', 1)
    sprite('jb033_09', 1)


@State
def CmnActFDashStop():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if CheckInput(0x5e):
                PerInertia(0)
            elif CheckInput(0x37):
                PerInertia(0)
    sprite('jb032_09', 2)
    sprite('jb032_10', 3)
    sprite('jb032_11', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('jb032_12', 2)
    sprite('jb032_13', 2)
    sprite('jb032_14', 2)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        EndMomentum(1)
        uponSendToLabel(LANDING, 0)
        NegativeForBackDash()
        ExternalForcesRate(100, 0)
    sprite('jb033_00', 1)
    sprite('jb033_01', 3)
    physicsXImpulse(-18000)
    SetAcceleration(-1000)
    physicsYImpulse(15800)
    setGravity(2400)
    JumpSoundEffects()
    sprite('jb033_02', 3)
    sprite('jb033_03', 3)
    setInvincible(0)
    sprite('jb033_04', 3)
    sprite('jb033_05', 32767)
    BeginBuffer('BDash2FDash')
    loopRest()
    label(0)
    sprite('jb033_06', 1)
    BufferedOrPressedGoto('BDash2FDash')
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb033_07', 1)
    DisallowGoto('BDash2FDash')
    sprite('jb033_08', 2)
    sprite('jb033_09', 3)


@State
def BDash2FDash():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
    sprite('jb033_06', 2)
    sprite('jb033_07', 2)
    sprite('jb033_08', 2)
    sprite('jb032_01', 2)
    DashEffects(100, 1, 1)
    EnableAfterimage(1)
    EndMomentum(1)
    SetInertia(75000)
    AddX(15000)
    sprite('jb032_02', 2)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffBarrierCancel2(1)
    WhiffJumpCancel(1)
    sprite('jb032_03', 2)
    sprite('jb032_04', 2)
    sprite('jb032_12', 2)
    sprite('jb032_13', 2)
    sprite('jb032_14', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('jb035_00', 3)
    label(0)
    sprite('jb035_01', 3)
    sprite('jb035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('jb036_00', 3)
    label(0)
    sprite('jb036_01', 3)
    sprite('jb036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('jb050_00', 1)
    sprite('jb050_01', 1)
    sprite('jb050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('jb050_01', 1)
    sprite('jb050_02', 1)
    sprite('jb050_01', 2)
    sprite('jb050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('jb050_02', 1)
    sprite('jb050_03', 1)
    sprite('jb050_02', 2)
    sprite('jb050_01', 2)
    sprite('jb050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('jb050_03', 1)
    sprite('jb050_04', 1)
    sprite('jb050_03', 2)
    sprite('jb050_02', 2)
    sprite('jb050_01', 2)
    sprite('jb050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('jb050_04', 1)
    sprite('jb050_04', 1)
    sprite('jb050_04', 2)
    sprite('jb050_03', 2)
    sprite('jb050_02', 2)
    sprite('jb050_01', 2)
    sprite('jb050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('jb052_00', 1)
    sprite('jb052_01', 1)
    sprite('jb052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('jb052_01', 1)
    sprite('jb052_02', 1)
    sprite('jb052_01', 2)
    sprite('jb052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('jb052_02', 1)
    sprite('jb052_03', 1)
    sprite('jb052_02', 2)
    sprite('jb052_01', 2)
    sprite('jb052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('jb052_03', 1)
    sprite('jb052_04', 1)
    sprite('jb052_03', 2)
    sprite('jb052_02', 2)
    sprite('jb052_01', 2)
    sprite('jb052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('jb052_04', 1)
    sprite('jb052_04', 1)
    sprite('jb052_04', 2)
    sprite('jb052_03', 2)
    sprite('jb052_02', 2)
    sprite('jb052_01', 2)
    sprite('jb052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('jb054_00', 1)
    sprite('jb054_01', 1)
    sprite('jb054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('jb054_01', 1)
    sprite('jb054_02', 1)
    sprite('jb054_01', 2)
    sprite('jb054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('jb054_02', 1)
    sprite('jb054_03', 1)
    sprite('jb054_02', 2)
    sprite('jb054_01', 2)
    sprite('jb054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('jb054_03', 1)
    sprite('jb054_04', 1)
    sprite('jb054_03', 2)
    sprite('jb054_02', 2)
    sprite('jb054_01', 2)
    sprite('jb054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('jb054_04', 1)
    sprite('jb054_04', 1)
    sprite('jb054_04', 2)
    sprite('jb054_03', 2)
    sprite('jb054_02', 2)
    sprite('jb054_01', 2)
    sprite('jb054_00', 2)


@State
def CmnActBDownUpper():
    sprite('jb060_00', 4)
    label(0)
    sprite('jb060_01', 4)
    sprite('jb060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('jb060_03', 4)


@State
def CmnActBDownDown():
    sprite('jb060_04', 4)
    label(0)
    sprite('jb060_05', 4)
    sprite('jb060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('jb060_07', 2)
    sprite('jb060_08', 2)


@State
def CmnActBDownBound():
    sprite('jb060_09', 3)
    sprite('jb060_10', 3)
    sprite('jb060_11', 3)
    sprite('jb060_12', 3)
    sprite('jb060_13', 3)


@State
def CmnActBDownLoop():
    sprite('jb060_14', 3)


@State
def CmnActBDown2Stand():
    sprite('jb061_00', 3)
    sprite('jb061_01', 3)
    sprite('jb061_02', 3)
    sprite('jb061_03', 3)
    sprite('jb061_04', 3)
    sprite('jb061_05', 3)
    sprite('jb061_06', 3)
    sprite('jb061_07', 3)
    sprite('jb061_08', 4)


@State
def CmnActFDownUpper():
    sprite('jb063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('jb063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('jb063_02', 3)
    sprite('jb063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('jb063_04', 3)
    sprite('jb063_05', 3)


@State
def CmnActFDownBound():
    sprite('jb063_06', 2)
    sprite('jb063_07', 2)
    sprite('jb063_08', 3)
    sprite('jb063_09', 3)
    sprite('jb063_10', 3)


@State
def CmnActFDownLoop():
    sprite('jb063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('jb064_00', 2)
    sprite('jb064_01', 2)
    sprite('jb064_02', 2)
    sprite('jb064_03', 2)
    sprite('jb064_04', 2)
    sprite('jb064_05', 2)
    sprite('jb064_06', 2)
    sprite('jb064_07', 2)
    sprite('jb064_08', 3)
    sprite('jb064_09', 3)


@State
def CmnActVDownUpper():
    sprite('jb062_00', 3)
    label(0)
    sprite('jb062_01', 3)
    sprite('jb062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('jb062_03', 3)
    sprite('jb062_04', 3)


@State
def CmnActVDownDown():
    sprite('jb062_05', 3)
    sprite('jb062_06', 3)
    label(0)
    sprite('jb062_07', 3)
    sprite('jb062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('jb062_09', 2)
    sprite('jb062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('jb062_09', 2)
    sprite('jb062_10', 2)


@State
def CmnActBlowoff():
    sprite('jb072_00', 3)
    sprite('jb072_01', 3)
    sprite('jb072_02', 3)
    label(0)
    sprite('jb072_01', 3)
    sprite('jb072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('jb074_00', 3)
    sprite('jb074_01', 3)
    sprite('jb074_02', 3)
    sprite('jb074_03', 3)
    sprite('jb074_04', 3)
    sprite('jb074_05', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('jb082_00', 3)
    sprite('jb082_01', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('jb071_04', 1)


@State
def CmnActWallBound():
    sprite('jb073_00', 3)
    sprite('jb073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('jb073_02', 3)
    label(0)
    sprite('jb073_03', 3)
    sprite('jb073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('jb070_00', 2)
    sprite('jb070_01', 2)
    label(0)
    sprite('jb070_02', 3)
    sprite('jb070_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('jb070_04', 4)
    sprite('jb070_05', 4)
    sprite('jb070_06', 4)
    sprite('jb070_07', 4)
    sprite('jb070_08', 4)
    sprite('jb070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('jb070_10', 2)
    sprite('jb070_11', 2)
    sprite('jb070_12', 2)
    sprite('jb070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('jb113_00', 3)
    sprite('jb113_01', 3)
    sprite('jb113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('jb113_00', 3)
    sprite('jb113_01', 3)
    sprite('jb113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('jb113_00', 3)
    sprite('jb113_01', 3)
    sprite('jb113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('jb110_00', 2)
    sprite('jb110_01', 2)
    sprite('jb110_02', 2)
    sprite('jb110_03', 2)
    sprite('jb110_04', 2)
    sprite('jb110_05', 2)
    sprite('jb110_06', 2)
    sprite('jb110_07', 2)
    sprite('jb110_08', 2)
    sprite('jb110_09', 2)
    sprite('jb110_10', 2)
    sprite('jb110_11', 2)
    sprite('jb110_12', 200)
    sprite('jb110_13', 3)
    sprite('jb110_14', 3)


@State
def CmnActUkemiLandB():
    sprite('jb111_00', 2)
    sprite('jb111_01', 2)
    sprite('jb111_02', 2)
    sprite('jb111_03', 2)
    sprite('jb111_04', 2)
    sprite('jb111_05', 2)
    sprite('jb111_06', 2)
    sprite('jb111_07', 2)
    sprite('jb111_08', 2)
    sprite('jb111_09', 2)
    sprite('jb111_10', 2)
    sprite('jb111_11', 2)
    sprite('jb111_12', 200)
    sprite('jb111_13', 3)
    sprite('jb111_14', 3)


@State
def CmnActUkemiLandN():
    sprite('jb112_00', 2)
    sprite('jb112_01', 2)
    sprite('jb112_02', 2)
    sprite('jb112_03', 2)
    sprite('jb112_04', 2)
    sprite('jb112_05', 2)
    sprite('jb112_06', 2)
    sprite('jb112_07', 2)
    sprite('jb112_08', 2)
    sprite('jb112_09', 2)
    sprite('jb112_10', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('jb024_00', 3)
    sprite('jb024_01', 3)
    sprite('jb024_02', 3)
    sprite('jb024_03', 3)
    sprite('jb024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('jb040_00', 3)
    sprite('jb040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('jb040_02', 4)
    sprite('jb040_03', 4)
    sprite('jb040_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('jb040_01', 3)
    sprite('jb040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('jb040_05', 3)
    label(0)
    sprite('jb040_02', 4)
    sprite('jb040_03', 4)
    sprite('jb040_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('jb040_01', 3)
    sprite('jb040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('jb041_00', 3)
    sprite('jb041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('jb041_02', 4)
    sprite('jb041_03', 4)
    sprite('jb041_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('jb041_01', 3)
    sprite('jb041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('jb041_05', 3)
    label(0)
    sprite('jb041_02', 4)
    sprite('jb041_03', 4)
    sprite('jb041_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('jb041_01', 3)
    sprite('jb041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('jb043_00', 3)
    sprite('jb043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('jb043_02', 4)
    sprite('jb043_03', 4)
    sprite('jb043_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('jb043_01', 3)
    sprite('jb043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('jb043_05', 3)
    label(0)
    sprite('jb043_02', 4)
    sprite('jb043_03', 4)
    sprite('jb043_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('jb043_01', 3)
    sprite('jb043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('jb045_00', 3)
    sprite('jb045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('jb045_02', 4)
    sprite('jb045_03', 4)
    sprite('jb045_03', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('jb045_01', 3)
    sprite('jb045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('jb045_05', 3)
    label(0)
    sprite('jb045_02', 4)
    sprite('jb045_03', 4)
    sprite('jb045_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('jb045_01', 3)
    sprite('jb045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('jb090_00', 2)
    sprite('jb090_01', 2)
    sprite('jb090_02', 1)
    SetCommonActionMark(1)
    sprite('jb090_03', 6)
    sprite('jb090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('jb091_00', 2)
    sprite('jb091_01', 2)
    sprite('jb091_02', 1)
    SetCommonActionMark(1)
    sprite('jb091_03', 6)
    sprite('jb091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('jb092_00', 2)
    sprite('jb092_01', 2)
    sprite('jb092_02', 1)
    SetCommonActionMark(1)
    sprite('jb092_03', 6)
    sprite('jb092_04', 6)


@State
def CmnActAirTurn():
    sprite('jb025_00ex00', 3)
    sprite('jb025_01', 3)
    sprite('jb025_00', 3)


@State
def CmnActLockWait():
    sprite('jb040_02', 1)
    sprite('jb040_01', 3)
    sprite('jb040_00', 3)


@State
def CmnActLockReject():
    sprite('jb312_00', 3)
    sprite('jb312_01', 3)
    sprite('jb312_02', 5)
    sprite('jb312_03', 2)
    sprite('jb312_04', 8)
    sprite('jb312_05', 3)
    sprite('jb312_06', 3)
    sprite('jb312_07', 2)


@State
def CmnActAirLockWait():
    sprite('jb045_02', 1)
    sprite('jb045_01', 3)
    sprite('jb045_00', 3)


@State
def CmnActAirLockReject():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            EndYPhysicsImpulse()
    sprite('jb322_00', 3)
    sprite('jb322_01', 3)
    sprite('jb322_02', 6)
    sprite('jb322_03', 6)
    sprite('jb322_04', 2)
    sprite('jb322_05', 3)
    sprite('jb322_06', 3)
    sprite('jb322_07', 3)


@State
def CmnActLandSpin():
    sprite('jb071_00', 4)
    sprite('jb071_01', 4)
    label(0)
    sprite('jb071_02', 2)
    sprite('jb071_03', 2)
    sprite('jb071_04', 2)
    sprite('jb071_05', 2)
    sprite('jb071_06', 2)
    sprite('jb071_07', 2)
    sprite('jb071_08', 2)
    sprite('jb071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('jb071_10', 6)
    sprite('jb071_11', 5)
    sprite('jb071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('jb071_02', 2)
    sprite('jb071_03', 2)
    sprite('jb071_04', 2)
    sprite('jb071_05', 2)
    sprite('jb071_06', 2)
    sprite('jb071_07', 2)
    sprite('jb071_08', 2)
    sprite('jb071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('jb077_00', 2)
    sprite('jb077_01', 2)
    sprite('jb077_00ex00', 2)
    sprite('jb077_01ex00', 2)
    sprite('jb077_00ex01', 2)
    sprite('jb077_01ex01', 2)
    sprite('jb077_00ex02', 2)
    sprite('jb077_01ex02', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('jb077_02', 4)
    label(0)
    sprite('jb077_03', 3)
    sprite('jb077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('jb077_05', 5)
    sprite('jb077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('jb060_07', 3)
    sprite('jb060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('jb060_13', 4)
    sprite('jb060_14', 5)


@State
def CmnActBurstBegin():
    sprite('jb331_00', 32767)


@State
def CmnActBurstLoop():
    sprite('jb331_01', 3)
    label(0)
    sprite('jb331_02', 3)
    sprite('jb331_03', 3)
    sprite('jb331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('jb331_05', 3)
    sprite('jb331_06', 3)


@State
def CmnActAirBurstBegin():
    sprite('jb331_07', 2)
    sprite('jb331_00ex00', 32767)


@State
def CmnActAirBurstLoop():
    sprite('jb331_01ex00', 3)
    label(0)
    sprite('jb331_02ex00', 3)
    sprite('jb331_03ex00', 3)
    sprite('jb331_04ex00', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('jb331_08', 3)
    sprite('jb331_09', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(0)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('jb333_00', 3)
    sprite('jb333_01', 3)
    sprite('jb333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('jb333_03', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('jb333_04', 3)
    sprite('jb333_05', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    sprite('jb333_06', 3)
    sprite('jb333_07', 3)
    label(0)
    sprite('jb333_05', 3)
    sprite('jb333_06', 3)
    sprite('jb333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('jb333_08', 6)
    sprite('jb333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('jb333_10', 3)
    sprite('jb333_11', 3)
    CharacterFlash(16639, 20, 1)
    sprite('jb333_13', 3)
    sprite('jb333_14', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('jb333_15', 3)
    sprite('jb333_05ex00', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    sprite('jb333_06ex00', 3)
    sprite('jb333_07ex00', 3)
    label(0)
    sprite('jb333_05ex00', 3)
    sprite('jb333_06ex00', 3)
    sprite('jb333_07ex00', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('jb333_16', 6)
    sprite('jb333_17', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        callSubroutine('5A_AtkData')
        WhiffCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
    sprite('jb200_00', 2)
    PerInertia(60)
    sprite('jb200_01', 3)
    sprite('jb200_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb200_02', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)
    sprite('jb200_01', 3)
    sprite('jb200_00', 2)


@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('5A_AtkData')
        WhiffCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
    sprite('jb200_04', 2)
    PerInertia(60)
    sprite('jb200_01', 3)
    sprite('jb200_02ex', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb200_02ex', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)
    sprite('jb200_01', 3)
    sprite('jb200_00', 2)


@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        callSubroutine('5A_AtkData')
    sprite('jb200_04', 2)
    PerInertia(60)
    sprite('jb200_01', 3)
    sprite('jb200_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb200_02', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)
    sprite('jb200_01', 3)
    sprite('jb200_00', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(500)
        AirPushbackY(20000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('AddChainD')
    sprite('jb201_00', 2)
    physicsXImpulse(15000)
    sprite('jb201_00', 2)
    XImpulseAcceleration(250)
    sprite('jb201_01', 3)
    RandomCommonVoiceline(1)
    XImpulseAcceleration(10)
    CommonSE('003_swing_grap_0_1')
    sprite('jb201_02', 3)
    sprite('jb201_03', 4)
    Recovery()
    Unknown2063()
    EndMomentum(1)
    sprite('jb201_04', 4)
    sprite('jb201_05', 4)
    sprite('jb201_06', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(570)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(10)
        AirPushbackX(15000)
        AirPushbackY(10000)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('AddChainD')
    sprite('jb202_00', 2)
    sprite('jb202_01', 2)
    physicsXImpulse(4000)
    DashEffects(100, 1, 0)
    sprite('jb202_02', 3)
    RandomCommonVoiceline(2)
    XImpulseAcceleration(500)
    DashEffects(100, 1, 0)
    CommonSE('010_swing_sword_1')
    sprite('jb202_03', 3)
    XImpulseAcceleration(50)
    DashEffects(100, 1, 0)
    sprite('jb202_04', 1)
    XImpulseAcceleration(10)
    StartMultihit()
    CreateObject('jbef202_zanzou', 100)
    sprite('jb202_04', 3)
    sprite('jb202_05', 4)
    sprite('jb202_06', 2)
    XImpulseAcceleration(1000)
    DashEffects(100, 1, 0)
    sprite('jb202_06', 2)
    XImpulseAcceleration(200)
    DashEffects(100, 1, 0)
    CommonSE('010_swing_sword_1')
    sprite('jb202_07', 3)
    EndMomentum(1)
    DashEffects(100, 1, 0)
    RefreshMultihit()
    AirUntechableTime(23)
    ResetPushback()
    AirPushbackY(30000)
    PushbackX(19800)
    CreateObject('jbef202_zanzou_2nd', 100)
    sprite('jb202_08', 4)
    Recovery()
    Unknown2063()
    sprite('jb202_09', 3)
    sprite('jb202_10', 3)
    sprite('jb202_11', 3)
    sprite('jb202_12', 3)
    sprite('jb202_13', 3)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        callSubroutine('2A_AtkData')
        WhiffCancel('AN_NmlAtk2A_2nd')
        HitOrBlockCancel('AN_NmlAtk2A_2nd')
    sprite('jb230_00', 2)
    PerInertia(60)
    sprite('jb230_01', 2)
    sprite('jb230_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb230_03', 3)
    RefreshMultihit()
    sprite('jb230_03', 3)
    WhiffCancelEnable(1)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb230_02', 4)
    sprite('jb230_01', 3)
    WhiffCancelEnable(0)
    sprite('jb230_00', 2)


@State
def AN_NmlAtk2A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('2A_AtkData')
        WhiffCancel('AN_NmlAtk2A_3rd')
        HitOrBlockCancel('AN_NmlAtk2A_3rd')
    sprite('jb230_04', 2)
    PerInertia(60)
    sprite('jb230_05', 2)
    sprite('jb230_06', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb230_07', 3)
    RefreshMultihit()
    sprite('jb230_07', 3)
    WhiffCancelEnable(1)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb230_08', 4)
    sprite('jb230_09', 3)
    WhiffCancelEnable(0)
    sprite('jb230_00', 2)


@State
def AN_NmlAtk2A_3rd():

    def upon_IMMEDIATE():
        callSubroutine('2A_AtkData')
    sprite('jb230_08', 2)
    PerInertia(60)
    sprite('jb230_01', 2)
    sprite('jb230_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('jb230_03', 2)
    RefreshMultihit()
    sprite('jb230_03', 3)
    WhiffCancelEnable(1)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb230_02', 4)
    sprite('jb230_01', 3)
    WhiffCancelEnable(0)
    sprite('jb230_00', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(550)
        AttackP1(90)
        AirPushbackY(20000)
        HitLow(2)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('AddChainD')
    sprite('jb231_00', 3)
    sprite('jb231_01', 2)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('jb231_02', 2)
    sprite('jb231_03', 1)
    StartMultihit()
    sprite('jb231_03', 3)
    sprite('jb231_03', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb231_04', 2)
    sprite('jb231_05', 2)
    sprite('jb231_06', 2)
    sprite('jb231_07', 2)
    sprite('jb231_08', 2)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(660)
        AttackP1(90)
        AttackP2(82)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(28)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        HitOrBlockJumpCancel(1)
        callSubroutine('AddChainD')
        uponSendToLabel(LANDING, 9)
    sprite('jb232_00', 3)
    sprite('jb232_01', 3)
    sprite('jb232_02', 3)
    RandomCommonVoiceline(2)
    CommonSE('010_swing_sword_1')
    sprite('jb232_03', 2)
    StartMultihit()
    CreateObject('jbef232_zanzou', 100)
    AddX(4000)
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('jb232_03', 4)
    physicsYImpulse(20000)
    sprite('jb232_04', 2)
    setInvincible(0)
    sprite('jb232_04', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('jb232_05', 3)
    sprite('jb232_06', 3)
    sprite('jb232_07', 3)
    sprite('jb232_08', 32767)
    label(9)
    sprite('jb232_09', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb232_10', 4)
    sprite('jb232_11', 4)
    sprite('jb232_12', 4)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(550)
        AttackP1(90)
        AttackP2(82)
        AirUntechableTime(26)
        UseSlashHitspark(1)
        AirHitstunAnimation(10)
        MoveAttributes(0, 1, 0, 0, 0)
        HitJumpCancel(1)
        callSubroutine('AddChainD')
        StayAfterMovement(1, 0)
        if SLOT_94:
            SpecialCancel(0)
    sprite('jb235_00', 3)
    sprite('jb235_01', 3)
    sprite('jb235_02', 3)
    RandomCommonVoiceline(2)
    CommonSE('010_swing_sword_1')
    sprite('jb235_03', 3)
    sprite('jb235_04', 3)
    CreateObject('jbef235_zanzou', 100)
    sprite('jb235_05', 3)
    sprite('jb235_06', 3)
    sprite('jb235_07', 3)
    SetXCollisionFromOrigin(200)
    CommonSE('010_swing_sword_1')
    sprite('jb235_08', 2)
    sprite('jb235_09', 3)
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(16000)
    CHHardKnockdown(10)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    HitLow(2)
    MoveAttributes(0, 0, 1, 0, 0)
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            SpecialCancel(1)
    CreateObject('jbef235_zanzou_2nd', 100)
    SetXCollisionFromOrigin(250)
    sprite('jb235_10', 3)
    Recovery()
    Unknown2063()
    sprite('jb235_11', 3)
    sprite('jb235_12', 3)
    SetXCollisionFromOrigin(-1)
    sprite('jb235_13', 3)
    sprite('jb235_14', 3)
    sprite('jb235_15', 3)
    sprite('jb235_16', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AirUntechableTime(14)
        Hitstop(11)
        StarterRating(2)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAirThrow')
        callSubroutine('AddChainD')

        def upon_OPPONENT_HIT_OR_BLOCK():
            SetActionMark(1)
    sprite('jb250_00', 3)
    sprite('jb250_01', 2)
    RandomCommonVoiceline(0)
    sprite('jb250_02', 2)
    CommonSE('003_swing_grap_0_0')
    sprite('jb250_03', 2)
    sprite('jb250_04', 2)
    sprite('jb250_05', 2)
    CommonSE('003_swing_grap_0_0')
    sprite('jb250_06', 2)
    sprite('jb250_07', 2)
    RefreshMultihit()
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SetActionMark(1)
        if SLOT_2:
            HitCancel('NmlAtkAIR5A')
    sprite('jb250_08', 3)
    if SLOT_2:
        HitCancel('NmlAtkAIR5A')
    Recovery()
    Unknown2063()
    sprite('jb250_09', 4)
    sprite('jb250_01', 4)
    sprite('jb250_00', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        AirPushbackY(20000)
        AirUntechableTime(19)
        if SLOT_94:
            HitOrBlockJumpCancel(0)
            SpecialCancel(0)
        else:
            HitOrBlockJumpCancel(1)
        callSubroutine('AddChainD')
    sprite('jb251_00', 3)
    sprite('jb251_01', 3)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('jb251_02', 3)
    sprite('jb251_03', 2)
    sprite('jb251_04', 2)
    sprite('jb251_05', 2)
    sprite('jb251_06', 2)
    CommonSE('003_swing_grap_0_1')
    sprite('jb251_07', 3)
    RefreshMultihit()
    AirHitstunAnimation(10)
    CHAirHitstunAnimation(18)
    AirUntechableTime(26)
    AirPushbackY(36000)
    CHAirPushbackY(42000)
    HitOverhead(0)
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            HitOrBlockJumpCancel(1)
            SpecialCancel(1)
    sprite('jb251_08', 3)
    sprite('jb251_09', 5)
    Recovery()
    Unknown2063()
    sprite('jb251_10', 5)
    sprite('jb251_11', 5)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirUntechableTime(21)
        UseSlashHitspark(1)
        HitOrBlockJumpCancel(1)
        callSubroutine('AddChainD')
        callSubroutine('AddChainD')
    sprite('jb252_00', 3)
    sprite('jb252_01', 3)
    RandomCommonVoiceline(2)
    sprite('jb252_02', 3)
    CommonSE('010_swing_sword_1')
    sprite('jb252_03', 3)
    sprite('jb252_04', 2)
    CreateObject('jbef252_zanzou', 100)
    sprite('jb252_05', 3)
    sprite('jb252_06', 3)
    sprite('jb252_07', 3)
    CommonSE('010_swing_sword_1')
    sprite('jb252_08', 2)
    RefreshMultihit()
    CreateObject('jbef252_zanzou_2nd', 100)
    sprite('jb252_09', 4)
    Recovery()
    Unknown2063()
    ChainCancel(1)
    sprite('jb252_10', 4)
    sprite('jb252_11', 3)
    sprite('jb252_12', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        UseSlashHitspark(1)
        HitJumpCancel(1)
        callSubroutine('AddChainD')
    sprite('jb255_00', 3)
    sprite('jb255_01', 2)
    RandomCommonVoiceline(2)
    ForcedLandingRecovery(5, 1)
    sprite('jb255_02', 2)
    CommonSE('010_swing_sword_1')
    sprite('jb255_03', 2)
    CreateObject('jbef255_zanzou', 100)
    sprite('jb255_04', 3)
    sprite('jb255_05', 4)
    Recovery()
    Unknown2063()
    sprite('jb255_06', 4)
    sprite('jb255_07', 4)
    sprite('jb255_08', 4)
    sprite('jb255_09', 4)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        EnterStateIfEventID(42, 'Atk6AExe')
    sprite('jb210_00', 2)
    PerInertia(30)
    sprite('jb210_00', 2)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(1, 1, 1, 0, 0)
    BlockOverhead(0)
    BlockLow(0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(-2, -1)
    CreateObject('jbef210_atemi', 100)
    PrivateSE('jbse_06')
    sprite('jb210_01', 4)
    sprite('jb210_02', 4)
    sprite('jb210_00', 4)
    setInvincible(0)
    sprite('jb210_01', 4)
    sprite('jb210_02', 4)
    sprite('jb210_00', 4)
    sprite('jb210_01', 4)
    sprite('jb210_11', 4)


@State
def Atk6AExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(50)
        AttackP2(92)
        AirHitstunAnimation(12)
        Hitstun(1)
        AirPushbackX(100000)
        AirPushbackY(15000)
        Hitstun(21)
        AirUntechableTime(60)
        Wallbounce(1)
        Hitstop(20)
        PushbackX(12000)
        HeatGainMultiplier(250)
        StarterRating(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(20000, 10000)
        StayAfterMovement(1, 0)
    sprite('jb210_03', 2)
    setInvincible(1)
    SetZLine(1, 30)
    sprite('jb210_04', 3)
    physicsXImpulse(80000)
    CommonSE('003_swing_grap_0_2')
    sprite('jb210_05', 3)
    XImpulseAcceleration(50)
    Voiceline('jb110')
    sprite('jb210_06', 4)
    EndMomentum(1)
    sprite('jb210_07', 4)
    setInvincible(0)
    Unknown2063()
    sprite('jb210_08', 4)
    sprite('jb210_09', 3)
    sprite('jb210_10', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        EnterStateIfEventID(42, 'Atk6BExe')
    sprite('jb211_00', 2)
    PerInertia(30)
    sprite('jb211_00', 2)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(1, 1, 1, 0, 0)
    BlockMid(0)
    BlockOverhead(0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(-2, -1)
    CreateObject('jbef211_atemi', 100)
    PrivateSE('jbse_06')
    sprite('jb211_01', 4)
    sprite('jb211_02', 4)
    sprite('jb211_00', 4)
    setInvincible(0)
    sprite('jb211_01', 4)
    sprite('jb211_02', 4)
    sprite('jb211_00', 4)
    sprite('jb211_01', 4)
    sprite('jb211_17', 4)


@State
def Atk6BExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(90)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        AirPushbackY(-60000)
        HardKnockdown(1)
        AirUntechableTime(40)
        PushbackX(12000)
        MoveAttributes(0, 0, 1, 0, 0)
        HitLow(2)
        StarterRating(2)
        FatalCounter(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(5000, 5000)
        SpecialCancel(0)
        StayAfterMovement(1, 0)
    sprite('jb211_03', 2)
    SetZLine(1, 30)
    setInvincible(1)
    sprite('jb211_04', 3)
    physicsXImpulse(80000)
    CommonSE('003_swing_grap_0_1')
    sprite('jb211_05', 3)
    XImpulseAcceleration(50)
    sprite('jb211_06', 3)
    Voiceline('jb111')
    XImpulseAcceleration(10)
    sprite('jb211_07', 1)
    setInvincible(0)
    EndMomentum(1)
    sprite('jb211_08', 1)
    sprite('jb211_09', 1)
    CommonSE('003_swing_grap_0_2')
    sprite('jb211_10', 1)
    sprite('jb211_11', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    ResetPushback()
    AirPushbackY(32000)
    HardKnockdown(-1)
    MoveAttributes(0, 1, 0, 0, 0)
    HitLow(0)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SpecialCancel(1)
        HitOrBlockJumpCancel(1)
    sprite('jb211_12', 4)
    Unknown2063()
    sprite('jb211_13', 4)
    sprite('jb211_14', 4)
    sprite('jb211_15', 4)
    sprite('jb211_16', 3)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(70)
        BonusProration(110)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(11)
        AirPushbackY(-60000)
        PushbackX(12000)
        HitOverhead(2)
        HardKnockdown(10)
        FatalCounter(1)
        StarterRating(2)
        UseSlashHitspark(1)
        uponSendToLabel(LANDING, 9)
        callSubroutine('AddChainD')
    sprite('jb212_00', 2)
    sprite('jb212_01', 2)
    Voiceline('jb112')
    sprite('jb212_02', 2)
    sprite('jb212_03', 4)
    EndMomentum(1)
    physicsXImpulse(4000)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('jb212_04', 5)
    CommonSE('006_swing_blade_2')
    sprite('jb212_05', 5)
    sprite('jb212_06', 32767)
    label(9)
    sprite('jb212_07', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    KnockdownEffects(0, 1, 0)
    CreateObject('jbef212_zanzou', 100)
    sprite('jb212_08', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('jb212_09', 3)
    sprite('jb212_10', 3)
    sprite('jb212_11', 3)
    sprite('jb212_12', 3)
    sprite('jb212_13', 3)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('DriveInit')
    sprite('jb203_00', 3)
    sprite('jb203_01', 3)
    EndMomentum(1)
    SpriteIfNot0(2, 2, 58)
    ParticleRotationAngle(0)
    CallCustomizableParticle('jbef_DriveYotyou', 103)
    sprite('jb203_02', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_03', 3)
    SpriteIfNot0(2, 2, 58)
    RandomVoiceline('jb107', 100, 'jb109', 100, '', 0, '', 0)
    sprite('jb203_05', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_06', 2)
    StartMultihit()
    physicsXImpulse(80000)
    ConstantAlphaModifier(-30)
    CreateObject('5DStartEff', 0)
    sprite('jb203_06', 10)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    PrivateSE('jbse_08')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('jb203_06', 3)
    StartMultihit()
    physicsXImpulse(110000)
    TriggerUponForState('5DStartEff', 32)
    sprite('jb203_06', 4)
    physicsXImpulse(40000)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb203_07', 4)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb203_08', 4)
    sprite('jb203_09', 8)
    sprite('jb203_10', 4)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    callSubroutine('Drive_DeriveInputBegin')
    sprite('jb203_11', 10)
    sprite('jb203_11', 10)
    callSubroutine('Drive_DeriveTimingBegin')
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb203_06', 3)
    clearUponHandler(OPPONENT_HIT)
    clearUponHandler(OPPONENT_BLOCKS)
    StartMultihit()
    physicsXImpulse(20000)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    BufferedOrPressedGoto('UltimateChage')
    TriggerUponForState('5DStartEff', 32)
    sprite('jb203_07', 3)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb203_08', 3)
    sprite('jb203_09', 6)
    DisallowGoto('UltimateChage')
    sprite('jb203_10', 3)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    sprite('jb203_11', 6)
    loopRest()
    CopyFromRightToLeft(23, 2, 2, 22, 2, 22)
    if SLOT_IsFacingRight:
        if SLOT_XDistanceFromCenterOfStage <= SLOT_2:
            conditionalSendToLabel(9)
    elif SLOT_XDistanceFromCenterOfStage >= SLOT_2:
        conditionalSendToLabel(9)
    sprite('jb203_14', 3)
    sprite('jb203_15', 3)
    ExitState()
    label(9)
    sprite('jb203_12', 3)
    EnterStateIfEventID(8, 'CmnActStandTurn')
    sprite('jb203_13', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('DriveInit')
        clearUponHandler(LANDING)
    sprite('jb253_00', 3)
    sprite('jb253_01', 3)
    EndMomentum(1)
    ParticleRotationAngle(60000)
    CallCustomizableParticle('jbef_DriveYotyou', 103)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_02ex00', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_03ex00', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_04ex00', 3)
    SpriteIfNot0(2, 2, 58)
    RandomVoiceline('jb107', 100, 'jb109', 100, '', 0, '', 0)
    sprite('jb253_02', 32767)
    CreateObject('AIR5DStartEff', 0)
    physicsXImpulse(40000)
    physicsYImpulse(-80000)
    setGravity(0)
    ConstantAlphaModifier(-20)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    PrivateSE('jbse_08')

    def upon_LANDING():
        LandingEffects(100, 1, 1)
        EndMomentum(1)
        sendToLabel(10)
    loopRest()
    label(0)
    sprite('jb253_03', 3)
    TriggerUponForState('AIR5DStartEff', 32)
    StartMultihit()
    physicsXImpulse(40000)
    sprite('jb253_03', 4)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb253_04', 4)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb253_05', 4)
    sprite('jb253_06', 8)
    sprite('jb253_07', 4)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    callSubroutine('Drive_DeriveInputBegin')
    sprite('jb253_08', 10)
    sprite('jb253_08', 10)
    callSubroutine('Drive_DeriveTimingBegin')
    SpecialCancel(1)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('jb253_03', 3)
    TriggerUponForState('AIR5DStartEff', 32)
    clearUponHandler(OPPONENT_HIT)
    StartMultihit()
    physicsXImpulse(30000)
    BufferedOrPressedGoto('UltimateChage')
    sprite('jb253_03', 3)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb253_04', 3)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    DisallowGoto('UltimateChage')
    sprite('jb253_05', 3)
    sprite('jb253_06', 6)
    sprite('jb253_07', 3)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    sprite('jb253_08', 6)
    loopRest()
    CopyFromRightToLeft(23, 2, 2, 22, 2, 22)
    if SLOT_IsFacingRight:
        if SLOT_XDistanceFromCenterOfStage <= SLOT_2:
            conditionalSendToLabel(9)
    elif SLOT_XDistanceFromCenterOfStage >= SLOT_2:
        conditionalSendToLabel(9)
    sprite('jb253_11', 3)
    sprite('jb253_12', 3)
    ExitState()
    label(9)
    sprite('jb253_09', 3)
    EnterStateIfEventID(8, 'CmnActStandTurn')
    sprite('jb253_10', 3)


@State
def AN_NmlAtkAIR6D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('DriveInit')
        clearUponHandler(LANDING)
    sprite('jb253_00', 3)
    sprite('jb253_01', 3)
    EndMomentum(1)
    ParticleRotationAngle(30000)
    CallCustomizableParticle('jbef_DriveYotyou', 103)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_02ex00', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_03ex00', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('jb203_04ex00', 3)
    SpriteIfNot0(2, 2, 58)
    RandomVoiceline('jb107', 100, 'jb109', 100, '', 0, '', 0)
    sprite('jb253_02', 32767)
    CreateObject('AIR6DStartEff', 0)
    physicsXImpulse(120000)
    physicsYImpulse(-80000)
    setGravity(0)
    ConstantAlphaModifier(-20)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    PrivateSE('jbse_08')

    def upon_LANDING():
        LandingEffects(100, 1, 1)
        EndMomentum(1)
        sendToLabel(10)
    loopRest()
    label(0)
    sprite('jb253_03', 3)
    TriggerUponForState('AIR6DStartEff', 32)
    StartMultihit()
    physicsXImpulse(60000)
    sprite('jb253_03', 4)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb253_04', 4)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb253_05', 4)
    sprite('jb253_06', 8)
    sprite('jb253_07', 4)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    callSubroutine('Drive_DeriveInputBegin')
    sprite('jb253_08', 10)
    sprite('jb253_08', 10)
    callSubroutine('Drive_DeriveTimingBegin')
    SpecialCancel(1)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('jb253_03', 3)
    TriggerUponForState('AIR6DStartEff', 32)
    clearUponHandler(OPPONENT_HIT)
    StartMultihit()
    physicsXImpulse(30000)
    BufferedOrPressedGoto('UltimateChage')
    sprite('jb253_03', 4)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb253_04', 2)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb253_04', 2)
    DisallowGoto('UltimateChage')
    sprite('jb253_05', 4)
    sprite('jb253_06', 8)
    sprite('jb253_07', 3)
    CreateParticle('jbef_noutou', 0)
    PrivateSE('jbse_07')
    sprite('jb253_08', 12)
    loopRest()
    CopyFromRightToLeft(23, 2, 2, 22, 2, 22)
    if SLOT_IsFacingRight:
        if SLOT_XDistanceFromCenterOfStage <= SLOT_2:
            conditionalSendToLabel(9)
    elif SLOT_XDistanceFromCenterOfStage >= SLOT_2:
        conditionalSendToLabel(9)
    sprite('jb253_11', 3)
    sprite('jb253_12', 3)
    ExitState()
    label(9)
    sprite('jb253_09', 3)
    EnterStateIfEventID(8, 'CmnActStandTurn')
    sprite('jb253_10', 3)


@State
def NmlAtk5D_SP():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackOff()
        EnableRapidCancel(0)
        SpecialCancel(0)
        SLOT_58 = SLOT_OverdriveTimer

        def upon_EVERY_FRAME():
            if CheckInput(0x20):
                SLOT_11 = 1
            if SLOT_StateDuration >= 30:
                ObjectUpon(FALLING, 32)
        clearUponHandler(LANDING)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)

        def upon_STATE_END():
            ForceFaceSprite()
            AlphaValue(255)
            SLOT_11 = 0
    sprite('jb203_00', 3)
    SpriteCall('jb253_00', 3, 2, 36)
    sprite('jb203_01', 3)
    SpriteCall('jb253_01', 3, 2, 36)
    EndMomentum(1)
    CreateObject('5D_SPMark', 100)
    RegisterObject(4, 1)
    if random_(2, 0, 50):
        Voiceline('jb106')
        SetActionMark(1)
    else:
        Voiceline('jb108')
    label(100)
    sprite('jb203_02', 3)
    SpriteCall('jb203_02ex00', 3, 2, 36)
    sprite('jb203_03', 3)
    SpriteCall('jb203_03ex00', 3, 2, 36)
    sprite('jb203_04', 3)
    SpriteCall('jb203_04ex00', 3, 2, 36)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(32)
    EnableCollision(0)
    AlphaValue(0)
    if not SLOT_58:
        SLOT_63 = 1

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor <= 1000:
            SLOT_YDistanceFromFloor = 1000
            if not SLOT_58:
                SLOT_63 = 1
    loopRest()
    label(1)
    sprite('jb203_16', 6)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(33)
    EnableCollision(1)
    CreateObject('jbef203_zanzou', 100)
    XImpulseAcceleration(5)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    AlphaValue(255)
    if SLOT_2:
        Voiceline('jb107')
    else:
        Voiceline('jb109')
    EnableRapidCancel(1)
    if SLOT_58:
        SpecialCancel(1)
    sprite('jb203_17', 4)
    sprite('jb203_18', 4)
    sprite('jb203_19', 3)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('jb300_00', 4)
    sprite('jb300_01', 4)
    sprite('jb300_02', 6)
    sprite('jb300_03', 5)
    CommonSE('024_getset_b')
    RandomVoiceline('jb404', 100, 'jb405', 100, '', 0, '', 0)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_01', 6)
    sprite('jb300_00', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('jb201_00', 4)
    sprite('jb201_00', 4)
    physicsXImpulse(40000)
    sprite('jb201_01', 4)
    RandomCommonVoiceline(1)
    XImpulseAcceleration(30)
    CommonSE('003_swing_grap_0_1')
    sprite('jb201_02', 3)
    EndMomentum(1)
    sprite('jb201_02', 2)
    AttackOff()
    sprite('jb201_03', 7)
    sprite('jb201_04', 7)
    sprite('jb201_05', 7)
    sprite('jb201_06', 7)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        PushbackX(8000)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        Blockstun(24)
        AirUntechableTime(60)
        Stagger(60)
        Crumple(50)
        GroundBounce(1)
        BouncePercentage(30)
        HardKnockdown(10)
        UseSlashHitspark(1)
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
    sprite('jb340_00', 3)
    sprite('jb340_01', 1)
    E0EAEffect('GuardCrushWind', 0)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    Voiceline('jb159')
    sprite('jb340_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('jb340_02', 3)
    ParticleColorFromPalette(224, 224, 224)
    sprite('jb340_03', 3)
    label(100)
    sprite('jb340_01', 3)
    sprite('jb340_02', 3)
    sprite('jb340_03', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb340_04', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('jb340_05', 2)
    physicsXImpulse(15000)
    sprite('jb340_06', 2)
    CommonSE('010_swing_sword_2')
    PrivateSE('jbse_03')
    sprite('jb340_07', 2)
    XImpulseAcceleration(50)
    sprite('jb340_08', 2)
    sprite('jb340_09', 1)
    XImpulseAcceleration(0)
    CreateObject('jbef340_zanzou', 100)
    sprite('jb340_09', 2)
    AttackOff()
    EnableAfterimage(0)
    sprite('jb340_10', 4)
    sprite('jb340_11', 4)
    sprite('jb340_12', 3)
    sprite('jb340_13', 3)
    sprite('jb340_14', 3)
    sprite('jb340_15', 3)
    sprite('jb340_16', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('jb310_00', 3)
    sprite('jb310_01', 3)
    sprite('jb310_02', 3)
    sprite('jb310_03', 3)
    CommonSE('010_swing_sword_0')
    Voiceline('jb155')
    sprite('jb310_04', 3)
    sprite('jb310_05', 11)
    sprite('jb310_06', 3)
    sprite('jb310_07', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(-4000)
        AirUntechableTime(60)
        HardKnockdown(10)
        StarterRating(2)
        OppPositionOnHit(1, 0, 200000)
        ShutUp(1)
        DamageEffect(5, '')
        DamageFromStateOnly('ThrowExe')
        SpecialCancel(0)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
    sprite('jb310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('jb311_00', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CommonSE('019_cloth_c')
    sprite('jb311_01', 4)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('jb311_02', 4)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CommonSE('005_swing_grap_2_1')
    Voiceline('jb153')
    sprite('jb311_03', 3)
    sprite('jb311_04', 3)
    sprite('jb311_05', 3)
    sprite('jb311_06', 3)
    sprite('jb311_07', 3)
    CreateObject('jbef311_claw', 100)
    PrivateSE('jbse_02')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    Hitstop(8)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-36000)
    OppPositionOnHit(0, 0, 0)
    UseSlashHitspark(1)
    ShutUp(0)
    DamageEffect(0, '')
    DamageFromStateOnly('')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SpecialCancel(1)
        EnableRapidCancel(1)
        callSubroutine('AddChainD')
    sprite('jb311_08', 3)
    sprite('jb311_09', 3)
    sprite('jb311_10', 3)
    sprite('jb311_11', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('jb310_00', 3)
    sprite('jb310_01', 3)
    sprite('jb310_02', 3)
    sprite('jb310_03', 3)
    CommonSE('010_swing_sword_0')
    Voiceline('jb155')
    sprite('jb310_04', 3)
    sprite('jb310_05', 11)
    sprite('jb310_06', 3)
    sprite('jb310_07', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-1000)
        AirUntechableTime(60)
        Hitstop(8)
        HardKnockdown(10)
        StarterRating(2)
        OppPositionOnHit(1, 110000, 200000)
        DamageFromStateOnly('BackThrowExe')
        SpecialCancel(0)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
    sprite('jb310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('jb313_00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('jb313_01', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('jb313_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('jb313_03', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('jb313_04', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CommonSE('003_swing_grap_0_2')
    sprite('jb313_05', 6)
    Voiceline('jb153')
    sprite('jb313_06', 3)
    sprite('jb313_07', 3)
    sprite('jb311_04', 3)
    Flip()
    sprite('jb311_05', 3)
    sprite('jb311_06', 3)
    sprite('jb311_07', 3)
    CreateObject('jbef311_claw', 100)
    PrivateSE('jbse_02')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1000)
    AttackP2(50)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-36000)
    OppPositionOnHit(0, 0, 0)
    UseSlashHitspark(1)
    DamageFromStateOnly('')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SpecialCancel(1)
        EnableRapidCancel(1)
        callSubroutine('AddChainD')
    sprite('jb311_08', 3)
    sprite('jb311_09', 3)
    sprite('jb311_10', 3)
    sprite('jb311_11', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('jb320_00', 3)
    sprite('jb320_01', 3)
    sprite('jb320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('jb320_03', 3)
    CommonSE('010_swing_sword_0')
    Voiceline('jb155')
    sprite('jb320_04', 3)
    sprite('jb320_05', 11)
    sprite('jb320_06', 3)
    sprite('jb320_07', 3)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(12000)
        AirPushbackY(-25000)
        GroundBounce(1)
        AirUntechableTime(60)
        HardKnockdown(1)
        OppPositionOnHit(1, 200000, 0)
        EnemyHitstopAddition(-11, -11, -11)
        StarterRating(2)
        EndMomentum(1)
        SetZLine(0, 50)
        ForcedLandingRecovery(0, 0)
    sprite('jb320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('jb321_00', 3)
    SetZLine(1, 50)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(8000)
    physicsYImpulse(36000)
    setGravity(1800)
    CameraFollowTarget(23, 22)
    sprite('jb321_01', 3)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('005_swing_grap_2_2')
    Voiceline('jb154')
    sprite('jb321_02', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_03', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_04', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_05', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_06', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PerGravity(150)

    def upon_LANDING():
        clearUponHandler(LANDING)
        sendToLabel(0)
    label(1)
    sprite('jb321_07', 1)
    OppThrowAnimation(31, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('005_swing_grap_2_0')
    sprite('jb321_08', 1)
    OppThrowAnimation(32, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_07ex00', 1)
    OppThrowAnimation(33, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_08ex00', 1)
    OppThrowAnimation(34, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_07ex01', 1)
    OppThrowAnimation(35, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_08ex01', 1)
    OppThrowAnimation(36, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_07ex02', 1)
    OppThrowAnimation(37, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('jb321_08ex02', 1)
    OppThrowAnimation(30, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('jb321_09', 3)
    CameraFollowTarget(0, 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    EndMomentum(1)
    sprite('jb321_10', 3)
    sprite('jb321_11', 3)
    sprite('jb321_12', 3)
    sprite('jb321_13', 3)
    sprite('jb321_14', 3)
    sprite('jb321_15', 3)


@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('jb032_01', 3)
    AirDashEffects(0)
    physicsXImpulse(30000)
    sprite('jb032_02', 3)
    DashEffects(100, 1, 1)
    sprite('jb032_03', 3)
    sprite('jb032_04', 3)

    def upon_EVERY_FRAME():
        if CheckInput(0x79):
            SetInertia(30000)
        else:
            sendToLabel(0)
        if SLOT_51:
            if SLOT_19 <= 150000:
                CopyFromRightToLeft(23, 2, 52, 22, 2, 37)
                if SLOT_52:
                    if CheckInput(0x78):
                        clearUponHandler(EVERY_FRAME)
                        enterState('FDash_Turn')
    label(1)
    sprite('jb032_05', 4)
    DashEffects(100, 1, 1)
    sprite('jb032_06', 3)
    sprite('jb032_07', 3)
    sprite('jb032_08', 3)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffBarrierCancel2(1)
    WhiffJumpCancel(1)
    SLOT_51 = 1
    sprite('jb032_02', 4)
    DashEffects(100, 1, 1)
    sprite('jb032_03', 3)
    sprite('jb032_04', 3)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('jb032_11', 3)
    clearUponHandler(EVERY_FRAME)
    XImpulseAcceleration(0)
    SetInertia(30000)
    sprite('jb032_12', 3)
    sprite('jb032_13', 3)
    sprite('jb032_14', 3)


@State
def ShortBackDash():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        EnterStateIfEventID(8, '_NEUTRAL')

        def upon_LANDING():
            clearUponHandler(LANDING)
            physicsXImpulse(0)
            SetAcceleration(0)
            LandingEffects(100, 1, 1)
            sendToLabel(1)
        NegativeForBackDash()
        ExternalForcesRate(100, 0)
    sprite('jb033_00', 1)
    setInvincible(1)
    EndMomentum(1)
    sprite('jb033_01', 3)
    physicsXImpulse(-15000)
    SetAcceleration(-1000)
    physicsYImpulse(15800)
    setGravity(2400)
    JumpSoundEffects()
    sprite('jb033_02', 3)
    sprite('jb033_02', 1)
    setInvincible(0)
    sprite('jb033_03', 3)
    sprite('jb033_04', 3)
    sprite('jb033_05', 90)
    loopRest()
    label(1)
    sprite('jb033_06', 1)
    sprite('jb033_07', 1)
    sprite('jb033_08', 2)
    sprite('jb032_01', 2)
    DashEffects(100, 1, 1)
    EnableAfterimage(1)
    EndMomentum(1)
    SetInertia(75000)
    AddX(15000)
    sprite('jb032_02', 2)
    sprite('jb032_03', 2)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffBarrierCancel2(1)
    sprite('jb032_04', 2)
    sprite('jb032_12', 2)
    sprite('jb032_13', 2)
    sprite('jb032_14', 2)
    loopRest()


@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_00', 4)
    PerInertia(60)
    Voiceline('jb300')
    sprite('jb400_01', 4)
    sprite('jb400_02', 4)
    physicsXImpulse(40000)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_16', 2)
    EndMomentum(1)
    Voiceline('jb300')
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)
    AddY(80000)
    MoveAttributes(1, 0, 0, 0, 0)
    clearUponHandler(LANDING)

    def upon_LANDING():
        clearUponHandler(EVERY_FRAME)
        SetActionMark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        LandingEffects(100, 1, 1)

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1000)
        if CheckInput(0x45):
            YSpeed(-1000)
        if SLOT_113:
            YSpeed(-1000)
    sprite('jb400_01', 3)
    sprite('jb400_02', 4)
    physicsXImpulse(20000)
    AirDashEffects(1)
    label(0)
    sprite('jb400_03', 2)
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(50)
    PrivateSE('jbse_02')
    sprite('jb400_04', 1)
    sprite('jb400_05', 1)
    sprite('jb400_06', 1)
    physicsXImpulse(40000)
    sprite('jb400_07', 1)
    sprite('jb400_08', 2)
    RefreshMultihit()
    CreateObject('jbef400_slash2', 100)
    XImpulseAcceleration(20)
    PrivateSE('jbse_02')
    sprite('jb400_09', 1)
    sprite('jb400_11', 1)
    SkidEffects(100, 1, 1)
    sprite('jb402_00', 2)
    physicsXImpulse(20000)
    clearUponHandler(EVERY_FRAME)
    sprite('jb402_01', 2)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    uponSendToLabel(LANDING, 9)
    sprite('jb402_02', 2)
    sprite('jb402_03', 2)
    sprite('jb402_04', 3)
    RefreshMultihit()
    callSubroutine('AssaultFinish_Atk')
    CreateObject('jbef402_slash', 100)
    PrivateSE('jbse_02')
    sprite('jb402_05', 3)
    Recovery()
    XImpulseAcceleration(20)
    sprite('jb402_06', 2)
    sprite('jb402_07', 2)
    sprite('jb402_08', 2)
    sprite('jb402_09', 3)
    sprite('jb402_12', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(1)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('jb024_00', 1)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb024_01', 1)
    sprite('jb024_02', 4)
    sprite('jb024_03', 1)
    sprite('jb024_04', 1)


@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_00', 4)
    PerInertia(60)
    Voiceline('jb200')
    sprite('jb400_01', 4)
    sprite('jb400_02', 4)
    physicsXImpulse(40000)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_16', 2)
    EndMomentum(1)
    Voiceline('jb300')
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)
    AddY(80000)
    MoveAttributes(1, 0, 0, 0, 0)
    clearUponHandler(LANDING)

    def upon_LANDING():
        clearUponHandler(EVERY_FRAME)
        SetActionMark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        LandingEffects(100, 1, 1)

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1000)
        if CheckInput(0x45):
            YSpeed(-1000)
        if SLOT_113:
            YSpeed(-1000)
    sprite('jb400_01', 3)
    sprite('jb400_02', 4)
    physicsXImpulse(20000)
    AirDashEffects(1)
    label(0)
    sprite('jb400_03', 2)
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(50)
    PrivateSE('jbse_02')
    sprite('jb400_04', 1)
    sprite('jb400_05', 1)
    sprite('jb400_06', 1)
    physicsXImpulse(40000)
    sprite('jb400_07', 1)
    sprite('jb400_08', 2)
    RefreshMultihit()
    CreateObject('jbef400_slash2', 100)
    XImpulseAcceleration(20)
    PrivateSE('jbse_02')
    sprite('jb400_09', 1)
    sprite('jb400_10', 1)
    sprite('jb400_01', 1)
    sprite('jb400_02', 1)
    physicsXImpulse(40000)
    if SLOT_IsAirborne:
        AirDashEffects(1)
    else:
        PreDashEffects(100, 1, 1)
    sprite('jb400_03', 2)
    RefreshMultihit()
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(50)
    PrivateSE('jbse_02')
    sprite('jb400_04', 1)
    sprite('jb400_11', 1)
    physicsXImpulse(5000)
    sprite('jb401_00', 1)
    if SLOT_IsAirborne:
        AirDashEffects(1)
    else:
        DashEffects(100, 1, 0)
        PreDashEffects(100, 1, 0)
    sprite('jb401_01', 2)
    XImpulseAcceleration(200)
    sprite('jb401_02', 2)
    XImpulseAcceleration(500)
    sprite('jb401_03', 4)
    RefreshMultihit()
    callSubroutine('AssaultUpper_Atk')
    CreateObject('jbef401_slash', 100)
    XImpulseAcceleration(20)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 9)
    PrivateSE('jbse_02')
    sprite('jb401_04', 1)
    sprite('jb401_05', 1)
    sprite('jb401_06', 1)
    sprite('jb401_07', 1)
    sprite('jb401_08', 1)
    sprite('jb402_11', 2)
    sprite('jb402_01', 2)
    PerGravity(50)
    sprite('jb402_02', 2)
    sprite('jb402_03', 2)
    sprite('jb402_04', 3)
    RefreshMultihit()
    callSubroutine('AssaultFinish_Atk')
    AirPushbackX(20000)
    AirPushbackY(-60000)
    CrouchWhiff(1)
    HardKnockdown(1)
    CHGroundBounce(1)
    BouncePercentage(30)
    CreateObject('jbef402_slash', 100)
    PrivateSE('jbse_02')
    Voiceline('jb201')
    sprite('jb402_05', 3)
    Recovery()
    XImpulseAcceleration(50)
    PerGravity(200)
    sprite('jb402_06', 3)
    sprite('jb402_07', 3)
    sprite('jb402_08', 3)
    sprite('jb402_09', 3)
    sprite('jb402_12', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(1)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('jb024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb024_01', 2)
    sprite('jb024_02', 6)
    sprite('jb024_03', 2)
    sprite('jb024_04', 2)


@State
def HexaEdge_1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
        SLOT_62 = 0
        SLOT_64 = 0
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_00', 4)
    PerInertia(60)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_16', 2)
    EndMomentum(1)
    AirDashEffects(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)
    AddY(80000)
    SLOT_59 = 1

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1500)
        if CheckInput(0x45):
            YSpeed(-1500)
    MoveAttributes(1, 0, 0, 0, 0)

    def upon_LANDING():
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        MoveAttributes(0, 1, 0, 0, 0)
    loopRest()
    label(0)
    sprite('jb400_01', 4)
    Voiceline('jb301')
    sprite('jb400_02', 4)
    physicsXImpulse(40000)
    sprite('jb400_03', 3)
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(50)
    YAccel(50)
    callSubroutine('HE_DeriveInputBegin')
    BeginBuffer('HexaEdge_2')
    PrivateSE('jbse_02')
    sprite('jb400_04', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    Recovery()
    clearUponHandler(EVERY_FRAME)
    callSubroutine('HE_DeriveTimingBegin')
    loopRest()
    if SLOT_IsAirborne:
        conditionalSendToLabel(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    SkidEffects(100, 1, 1)
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 3)
    XImpulseAcceleration(50)
    sprite('jb400_13', 3)
    XImpulseAcceleration(0)
    sprite('jb400_14', 3)
    sprite('jb400_15', 2)
    ExitState()
    label(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    YAccel(50)
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('jb400_13', 3)
    EndYPhysicsImpulse()
    sprite('jb400_17', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb400_18', 2)


@State
def HexaEdge_2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_04', 1)
    PerInertia(60)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_04', 1)
    EndMomentum(1)
    AirDashEffects(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1500)
        if CheckInput(0x45):
            YSpeed(-1500)
    MoveAttributes(1, 0, 0, 0, 0)

    def upon_LANDING():
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        MoveAttributes(0, 1, 0, 0, 0)
    loopRest()
    label(0)
    sprite('jb400_05', 2)
    sprite('jb400_06', 2)
    physicsXImpulse(40000)
    sprite('jb400_07', 2)
    sprite('jb400_08', 3)
    CreateObject('jbef400_slash2', 100)
    XImpulseAcceleration(20)
    callSubroutine('HE_DeriveInputBegin')
    BeginBuffer('HexaEdge_3')
    PrivateSE('jbse_02')
    sprite('jb400_09', 3)
    Recovery()
    clearUponHandler(EVERY_FRAME)
    callSubroutine('HE_DeriveTimingBegin')
    loopRest()
    if SLOT_IsAirborne:
        conditionalSendToLabel(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    SkidEffects(100, 1, 1)
    callSubroutine('HE_DeriveClear')
    Voiceline('jb302')
    sprite('jb400_12', 3)
    XImpulseAcceleration(50)
    sprite('jb400_13', 3)
    XImpulseAcceleration(0)
    sprite('jb400_14', 3)
    sprite('jb400_15', 2)
    ExitState()
    label(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    YAccel(50)
    EndYPhysicsImpulse()
    callSubroutine('HE_DeriveClear')
    Voiceline('jb302')
    sprite('jb400_12', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('jb400_13', 3)
    sprite('jb400_17', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb400_18', 2)


@State
def HexaEdge_3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
        Voiceline('jb302')
        SLOT_64 = 1
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_09', 1)
    PerInertia(60)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_09', 1)
    EndMomentum(1)
    AirDashEffects(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1500)
        if CheckInput(0x45):
            YSpeed(-1500)
    MoveAttributes(1, 0, 0, 0, 0)

    def upon_LANDING():
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        MoveAttributes(0, 1, 0, 0, 0)
    loopRest()
    label(0)
    sprite('jb400_16', 2)
    sprite('jb400_01', 2)
    physicsXImpulse(40000)
    sprite('jb400_02', 2)
    sprite('jb400_03', 3)
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(50)
    callSubroutine('HE_DeriveInputBegin')
    BeginBuffer('HexaEdge_4')
    PrivateSE('jbse_02')
    sprite('jb400_04', 3)
    Recovery()
    clearUponHandler(EVERY_FRAME)
    callSubroutine('HE_DeriveTimingBegin')
    loopRest()
    if SLOT_IsAirborne:
        conditionalSendToLabel(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    SkidEffects(100, 1, 1)
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 4)
    XImpulseAcceleration(50)
    sprite('jb400_13', 4)
    XImpulseAcceleration(0)
    sprite('jb400_14', 3)
    sprite('jb400_15', 3)
    ExitState()
    label(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    YAccel(50)
    EndYPhysicsImpulse()
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('jb400_13', 4)
    sprite('jb400_17', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb400_18', 3)


@State
def HexaEdge_4():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('HexaEdge_Atk')
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_04', 1)
    PerInertia(60)
    PreDashEffects(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('jb400_04', 1)
    EndMomentum(1)
    AirDashEffects(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)

    def upon_EVERY_FRAME():
        if CheckInput(0x93):
            YSpeed(1500)
        if CheckInput(0x45):
            YSpeed(-1500)
    MoveAttributes(1, 0, 0, 0, 0)

    def upon_LANDING():
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        MoveAttributes(0, 1, 0, 0, 0)
    loopRest()
    label(0)
    sprite('jb400_05', 2)
    sprite('jb400_06', 2)
    physicsXImpulse(40000)
    sprite('jb400_07', 2)
    sprite('jb400_08', 3)
    CreateObject('jbef400_slash2', 100)
    XImpulseAcceleration(20)
    callSubroutine('HE_DeriveInputBegin')
    BeginBuffer('HexaEdge_Blow')
    DisallowGoto('HexaEdge_Upper')
    PrivateSE('jbse_02')
    sprite('jb400_09', 3)
    Recovery()
    clearUponHandler(EVERY_FRAME)
    callSubroutine('HE_DeriveTimingBegin')
    loopRest()
    if SLOT_IsAirborne:
        conditionalSendToLabel(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    SkidEffects(100, 1, 1)
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 4)
    XImpulseAcceleration(50)
    sprite('jb400_13', 4)
    XImpulseAcceleration(0)
    sprite('jb400_14', 3)
    sprite('jb400_15', 3)
    ExitState()
    label(11)
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    YAccel(50)
    EndYPhysicsImpulse()
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('jb400_13', 4)
    sprite('jb400_17', 3)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb400_18', 3)


@State
def HexaEdge_Blow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(80)
        AirUntechableTime(60)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(40000)
        AirPushbackY(6000)
        Floorslide(10)
        Wallbounce(1)
        NonCornerWallbounce(1)
        WallbounceReboundTime(0)
        UseSlashHitspark(1)
        MoveAttributes(1, 0, 0, 0, 0)
        if SLOT_137:
            DamageMultiplier(80)
        if SLOT_IsAirborne:
            if not SLOT_62:
                SetYCollisionFromOrigin(100)
                PushCollisionHeightLow(80000)

        def upon_STATE_END():
            SLOT_62 = 0
        EnterStateIfEventID(2, 'CmnActJumpLanding')
        ForcedLandingRecovery(10, 1)
    sprite('jb402_00', 2)
    SpriteCall('jb402_11', 2, 2, 62)
    EndMomentum(1)
    physicsXImpulse(20000)
    DespawnEAEffect('jbef400_slash2')
    JumpEffects(3, 100)
    sprite('jb402_01', 2)
    if SLOT_IsAirborne:
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        AddY(-80000)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    sprite('jb402_02', 2)
    sprite('jb402_03', 2)
    Voiceline('jb303')
    sprite('jb402_04', 3)
    CreateObject('jbef402_slash', 100)
    PrivateSE('jbse_02')
    sprite('jb402_05', 3)
    Recovery()
    XImpulseAcceleration(20)
    sprite('jb402_06', 3)
    sprite('jb402_07', 3)
    sprite('jb402_08', 3)
    sprite('jb402_09', 3)
    sprite('jb402_12', 3)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(0)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def HexaEdge_Upper():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(32000)
        AirUntechableTime(28)
        UseSlashHitspark(1)
        if SLOT_IsAirborne:
            MoveAttributes(1, 0, 0, 0, 0)
        SLOT_62 = 1
    sprite('jb400_11', 3)
    physicsXImpulse(5000)
    if SLOT_IsGrounded:
        DashEffects(100, 1, 0)
        PreDashEffects(100, 1, 0)
    else:
        AirDashEffects(1)
        SetYCollisionFromOrigin(100)
        PushCollisionHeightLow(80000)

        def upon_LANDING():
            SetYCollisionFromOrigin(-1)
            PushCollisionHeightLow(-1)
    sprite('jb401_00', 3)
    sprite('jb401_01', 3)
    XImpulseAcceleration(200)
    sprite('jb401_02', 2)
    if not SLOT_64:
        Voiceline('jb302')
    XImpulseAcceleration(500)
    sprite('jb401_03', 4)
    CreateObject('jbef401_slash', 100)
    PrivateSE('jbse_02')
    XImpulseAcceleration(25)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    callSubroutine('HE_DeriveInputBegin')
    BeginBuffer('HexaEdge_Blow')
    DisallowGoto('HexaEdge_Upper')
    DisallowGoto('HexaEdge_FrontDash')
    DisallowGoto('HexaEdge_BackDash')
    uponSendToLabel(LANDING, 9)
    sprite('jb401_04', 4)
    XImpulseAcceleration(80)
    callSubroutine('HE_DeriveTimingBegin')
    sprite('jb401_05', 4)
    XImpulseAcceleration(50)
    sprite('jb401_06', 4)
    XImpulseAcceleration(50)
    sprite('jb401_07', 3)
    callSubroutine('HE_DeriveClear')
    sprite('jb401_08', 3)
    sprite('jb401_12', 3)
    sprite('jb401_13', 3)
    sprite('jb401_14', 3)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(0)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb401_09', 4)
    LandingEffects(100, 1, 0)
    EndMomentum(1)
    sprite('jb401_10', 4)
    sprite('jb401_11', 4)


@State
def HexaEdge_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
        clearUponHandler(OPPONENT_HIT)

        def upon_STATE_END():
            SLOT_62 = 0
        HitCancel('Shot')
    if SLOT_62:
        conditionalSendToLabel(1)
    sprite('jb400_11', 2)
    if SLOT_IsGrounded:
        SetInertia(20000)
        PreDashEffects(100, 1, 0)
    else:
        PopSpeedX()
        XImpulseAcceleration(50)
        physicsYImpulse(6000)
        EndYPhysicsImpulse()
    sprite('jb403_00', 2)
    sprite('jb403_01', 2)
    sprite('jb403_02', 2)
    SpriteIfNot0(32767, 2, 36)
    if SLOT_IsAirborne:
        PerGravity(150)

        def upon_LANDING():
            sendToLabel(0)
    label(0)
    sprite('jb403_03', 2)
    DashEffects(100, 1, 0)
    loopRest()
    gotoLabel(3)
    label(1)
    sprite('jb403_15', 4)
    uponSendToLabel(LANDING, 2)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(50)
    sprite('jb403_16', 32767)
    XImpulseAcceleration(50)
    PerGravity(150)
    label(2)
    sprite('jb403_17', 1)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    SetInertia(20000)
    sprite('jb403_18', 1)
    loopRest()
    label(3)
    sprite('jb403_04', 2)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    Voiceline('jb204')
    sprite('jb403_05', 2)
    EndMomentum(1)
    CreateObject('jbef403_zanzou', 100)
    CreateObject('jbef403_zanzou2', 100)
    sprite('jb403_06', 2)
    Recovery()
    sprite('jb403_07', 4)
    sprite('jb403_08', 4)
    sprite('jb403_09', 3)
    sprite('jb403_10', 3)
    sprite('jb403_11', 3)
    sprite('jb403_12', 3)


@State
def HexaEdge_Mid():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        if SLOT_IsGrounded:
            DashEffects(100, 1, 0)
            PreDashEffects(100, 1, 0)
        if SLOT_IsAirborne:
            SLOT_61 = 1
            if not SLOT_62:
                SetYCollisionFromOrigin(100)
                PushCollisionHeightLow(80000)

        def upon_STATE_END():
            SLOT_62 = 0
        EnterStateIfEventID(2, 'CmnActJumpLanding')
        ForcedLandingRecovery(12, 1)
    if SLOT_62:
        conditionalSendToLabel(0)
    sprite('jb400_11', 1)
    physicsXImpulse(20000)
    Voiceline('jb205')
    sprite('jb404_00', 1)
    sprite('jb404_01', 2)
    if SLOT_IsAirborne:
        SetYCollisionFromOrigin(-1)
        PushCollisionHeightLow(-1)
        AddY(-80000)
    if SLOT_IsGrounded:
        JumpEffects(3, 100)
    XImpulseAcceleration(30)
    physicsYImpulse(23000)
    EndYPhysicsImpulse()
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('jb404_12', 2)
    physicsXImpulse(5000)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    Voiceline('jb205')
    sprite('jb404_01', 2)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    loopRest()
    label(1)
    sprite('jb404_02', 3)
    sprite('jb404_03', 3)
    sprite('jb404_03', 3)
    sprite('jb404_04', 3)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb404_05', 1)
    StartMultihit()
    CreateObject('jbef404_zanzou', 100)
    sprite('jb404_05', 3)
    sprite('jb404_06', 2)
    Recovery()
    sprite('jb404_07', 2)
    sprite('jb404_08', 2)
    sprite('jb404_09', 2)
    sprite('jb404_13', 2)
    sprite('jb404_14', 2)


@State
def HexaEdge_Multi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Multi_Atk')
        if SLOT_IsGrounded:
            DashEffects(100, 1, 0)
            PreDashEffects(100, 1, 0)
        if SLOT_IsAirborne:
            if not SLOT_62:
                SetYCollisionFromOrigin(100)
                PushCollisionHeightLow(80000)

        def upon_STATE_END():
            SLOT_62 = 0
        uponSendToLabel(LANDING, 2)
    if SLOT_62:
        conditionalSendToLabel(1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(0)
    sprite('jb400_11', 3)
    physicsXImpulse(30000)
    sprite('jb405_00', 3)
    sprite('jb405_01', 3)
    EnableCollision(0)
    XImpulseAcceleration(80)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    JumpEffects(3, 100)
    sprite('jb405_02', 3)
    XImpulseAcceleration(80)
    Voiceline('jb206')
    sprite('jb405_03', 3)
    XImpulseAcceleration(80)
    sprite('jb405_04', 3)
    XImpulseAcceleration(80)
    sprite('jb405_05', 3)
    CreateObject('jbef405_loop', 100)
    AttackOff()
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('jb405_06', 3)
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(0)
    sprite('jb400_11', 2)
    physicsXImpulse(30000)
    sprite('jb405_00', 2)
    sprite('jb405_01', 3)
    EnableCollision(0)
    XImpulseAcceleration(80)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    sprite('jb405_02', 3)
    XImpulseAcceleration(80)
    Voiceline('jb206')
    sprite('jb405_03', 3)
    XImpulseAcceleration(80)
    sprite('jb405_04', 3)
    XImpulseAcceleration(80)
    sprite('jb405_05', 3)
    CreateObject('jbef405_loop', 100)
    RefreshMultihit()
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('jb400_18', 3)
    physicsXImpulse(20000)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    sprite('jb405_01', 3)
    EnableCollision(0)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    sprite('jb405_02', 3)
    XImpulseAcceleration(80)
    Voiceline('jb206')
    sprite('jb405_03', 3)
    XImpulseAcceleration(80)
    sprite('jb405_04', 3)
    XImpulseAcceleration(80)
    sprite('jb405_05', 3)
    CreateObject('jbef405_loop', 100)
    RefreshMultihit()
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    label(10)
    sprite('jb405_05', 3)
    RefreshMultihit()
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('jb405_08', 4)
    EndMomentum(1)
    DespawnEAEffect('jbef405_loop')
    LandingEffects(100, 1, 1)
    ScreenShake(0, 8000)
    ForceFaceSprite()
    sprite('jb405_09', 4)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb405_10', 4)
    EnableAfterimage(0)
    CreateObject('jbef405_zanzou', 100)
    RefreshMultihit()
    callSubroutine('Assault_MultiFinish_Atk')
    sprite('jb405_11', 4)
    Recovery()
    Unknown2063()
    sprite('jb405_12', 4)
    sprite('jb405_13', 4)
    sprite('jb405_14', 3)
    sprite('jb405_15', 3)
    sprite('jb405_16', 3)
    sprite('jb405_17', 3)


@State
def HexaEdge_Chage():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Chage_Atk')

        def upon_STATE_END():
            SLOT_62 = 0
    if SLOT_62:
        conditionalSendToLabel(1)
    sprite('jb400_11', 2)
    physicsXImpulse(20000)
    if SLOT_IsAirborne:
        physicsYImpulse(6000)
        EndYPhysicsImpulse()
    sprite('jb400_12', 2)
    XImpulseAcceleration(50)
    sprite('jb400_13', 2)
    XImpulseAcceleration(50)
    sprite('jb406_00', 2)
    XImpulseAcceleration(50)
    SpriteIfNot0(32767, 2, 36)
    if SLOT_IsAirborne:
        PerGravity(150)

        def upon_LANDING():
            sendToLabel(0)
    label(0)
    sprite('jb406_01', 2)
    EndMomentum(1)
    CommonSE('024_getset_b')
    sprite('jb406_02', 2)
    sprite('jb406_03', 2)
    loopRest()
    gotoLabel(3)
    label(1)
    sprite('jb401_06', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(80)
    uponSendToLabel(LANDING, 2)
    sprite('jb401_07', 3)
    XImpulseAcceleration(80)
    sprite('jb401_08', 32767)
    XImpulseAcceleration(80)
    PerGravity(150)
    label(2)
    sprite('jb406_16', 1)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('jb406_01', 1)
    CommonSE('024_getset_b')
    sprite('jb406_02', 1)
    sprite('jb406_03', 1)
    label(3)
    sprite('jb406_04', 3)
    sprite('jb406_05', 3)
    loopRest()
    gotoLabel(3)
    label(8)
    sprite('jb406_06', 3)
    clearUponHandler(EVERY_FRAME)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    Voiceline('jb207')
    EndMomentum(1)
    sprite('jb406_07', 3)
    AddX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    CreateObject('jbef406_zanzou', 100)
    CreateObject('jbef406_zanzou2', 100)
    LandingEffects(100, 1, 0)
    uponSendToLabel(LANDING, 10)
    sprite('jb406_08', 3)
    sprite('jb406_09', 3)
    sprite('jb406_10', 3)
    sprite('jb406_11', 3)
    sprite('jb406_12', 32767)
    label(9)
    sprite('jb406_06', 3)
    clearUponHandler(EVERY_FRAME)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    Voiceline('jb207')
    EndMomentum(1)
    sprite('jb406_07', 1)
    AddX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(24000)
    EndYPhysicsImpulse()
    CreateObject('jbef406_zanzou', 100)
    CreateObject('jbef406_zanzou2', 100)
    LandingEffects(100, 1, 0)
    uponSendToLabel(LANDING, 10)
    sprite('jb406_07', 3)
    StartMultihit()
    sprite('jb406_08', 4)
    sprite('jb406_09', 4)
    sprite('jb406_10', 4)
    sprite('jb406_11', 4)
    sprite('jb406_12', 32767)
    label(10)
    sprite('jb406_13', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('jb406_14', 3)
    AttackOffOrBlockCancel('UltimateChage')
    sprite('jb406_15', 3)


@State
def HexaEdge_FrontDash():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(0)
        IgnoreTurn(1)

        def upon_8():
            ForceFaceSprite()
        ForcedLandingRecovery(6, 1)
        SLOT_60 = 1

        def upon_EVERY_FRAME():
            if SLOT_IsGrounded:
                clearUponHandler(EVERY_FRAME)
                SLOT_59 = 0
                SLOT_60 = 0
                SLOT_61 = 0
                SLOT_62 = 0
                SLOT_63 = 0
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_11', 2)
    EndMomentum(1)
    Voiceline('jb209')
    sprite('jb405_00', 2)
    sprite('jb408_00', 2)
    EnableAfterimage(1)
    CreateObject('jbef408_DashEff', 0)
    AddY(10000)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('jb400_11', 2)
    EndMomentum(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)
    Voiceline('jb209')
    sprite('jb405_00', 2)
    sprite('jb408_00', 2)
    EnableAfterimage(1)
    CreateObject('jbef408_DashEff', 0)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    label(9)
    sprite('jb408_01', 2)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(50000)
    AirDashEffects(1)
    SetZLine(0, 30)
    sprite('jb408_02', 2)
    sprite('jb408_01', 2)
    sprite('jb408_02', 2)
    sprite('jb408_03', 3)
    XImpulseAcceleration(50)
    TriggerUponForState('jbef408_DashEff', 32)
    sprite('jb408_04', 4)
    SetZLine(1, 30)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    EnableAfterimage(0)
    XImpulseAcceleration(50)
    sprite('jb408_05', 4)
    XImpulseAcceleration(50)
    EndYPhysicsImpulse()


@State
def HexaEdge_BackDash():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(0)
        IgnoreTurn(1)

        def upon_8():
            ForceFaceSprite()
        ForcedLandingRecovery(6, 1)
        SLOT_60 = 1

        def upon_EVERY_FRAME():
            if SLOT_IsGrounded:
                clearUponHandler(EVERY_FRAME)
                SLOT_59 = 0
                SLOT_60 = 0
                SLOT_61 = 0
                SLOT_62 = 0
                SLOT_63 = 0
    if SLOT_IsAirborne:
        conditionalSendToLabel(10)
    sprite('jb400_11', 4)
    EndMomentum(1)
    Voiceline('jb209')
    sprite('jb405_00', 4)
    sprite('jb408_00', 4)
    Flip()
    EnableAfterimage(1)
    CreateObject('jbef408_DashEff', 0)
    AddY(10000)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('jb400_11', 4)
    EndMomentum(1)
    SetYCollisionFromOrigin(100)
    PushCollisionHeightLow(80000)
    Voiceline('jb209')
    sprite('jb405_00', 4)
    sprite('jb408_00', 4)
    EnableAfterimage(1)
    CreateObject('jbef408_DashEff', 0)
    SetYCollisionFromOrigin(-1)
    PushCollisionHeightLow(-1)
    AddY(-80000)
    Flip()
    loopRest()
    label(9)
    sprite('jb408_01', 2)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(30000)
    AirDashEffects(1)
    SetZLine(0, 30)
    sprite('jb408_02', 2)
    sprite('jb408_01', 2)
    sprite('jb408_02', 2)
    sprite('jb408_03', 3)
    XImpulseAcceleration(50)
    TriggerUponForState('jbef408_DashEff', 32)
    sprite('jb408_04', 4)
    SetZLine(1, 30)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    EnableAfterimage(0)
    XImpulseAcceleration(50)
    sprite('jb408_05', 4)
    XImpulseAcceleration(50)
    EndYPhysicsImpulse()


@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('jb407_00', 4)
    EndMomentum(1)
    sprite('jb407_01', 5)
    CreateObject('jbef407_NekodamaRady', -1)
    PrivateSE('jbse_04')
    sprite('jb407_02', 5)
    sprite('jb407_03', 5)
    sprite('jb407_04', 5)
    sprite('jb407_05', 5)
    Voiceline('jb208')
    sprite('jb407_06', 5)
    CreateObject('Shot_Eff', 0)
    DespawnEAEffect('jbef407_NekodamaRady')
    CommonSE('016_explode_1')
    sprite('jb407_07', 4)
    SetInertia(-20000)
    sprite('jb407_08', 4)
    sprite('jb407_07', 4)
    sprite('jb407_08', 4)
    EndMomentum(1)
    sprite('jb407_09', 3)


@State
def AirShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        ForcedLandingRecovery(4, 1)
    sprite('jb407_00ex00', 4)
    EndMomentum(1)
    sprite('jb407_01ex00', 5)
    CreateObject('jbef407_NekodamaRady', -1)
    PrivateSE('jbse_04')
    sprite('jb407_02ex00', 5)
    sprite('jb407_03ex00', 5)
    sprite('jb407_04ex00', 5)
    sprite('jb407_05ex00', 5)
    Voiceline('jb208')
    sprite('jb407_06ex00', 5)
    CreateObject('Shot_Eff', 0)
    ObjectUpon(STATE_END, 32)
    DespawnEAEffect('jbef407_NekodamaRady')
    CommonSE('016_explode_1')
    sprite('jb407_07ex00', 4)
    physicsXImpulse(-15000)
    sprite('jb407_08ex00', 4)
    XImpulseAcceleration(60)
    sprite('jb407_07ex00', 4)
    XImpulseAcceleration(60)
    sprite('jb407_08ex00', 4)
    EndMomentum(1)
    EndYPhysicsImpulse()
    sprite('jb407_07ex00', 4)
    sprite('jb407_08ex00', 4)
    sprite('jb407_10', 3)


@State
def AirMoveFront():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        IgnoreTurn(1)

        def upon_8():
            ForceFaceSprite()
        SLOT_60 = 1
    sprite('jb408_00', 3)
    EnableAfterimage(1)
    PushGravity()
    EndMomentum(1)
    CreateObject('jbef408_DashEff', 0)
    Voiceline('jb209')
    sprite('jb408_01', 3)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(60000)
    physicsYImpulse(0)
    setGravity(0)
    SetInertia(0)
    AirDashEffects(1)
    SetZLine(0, 30)
    sprite('jb408_02', 3)
    sprite('jb408_01', 3)
    XImpulseAcceleration(50)
    sprite('jb408_03', 4)
    XImpulseAcceleration(20)
    TriggerUponForState('jbef408_DashEff', 32)
    sprite('jb408_04', 4)
    SetZLine(1, 30)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(20)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    EnableAfterimage(0)
    sprite('jb408_05', 3)


@State
def AirMoveBack():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        IgnoreTurn(1)

        def upon_8():
            ForceFaceSprite()
        SLOT_60 = 1
    sprite('jb408_00', 3)
    Flip()
    EnableAfterimage(1)
    PushGravity()
    EndMomentum(1)
    CreateObject('jbef408_DashEff', 0)
    Voiceline('jb209')
    sprite('jb408_01', 3)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(30000)
    physicsYImpulse(0)
    setGravity(0)
    SetInertia(0)
    AirDashEffects(1)
    SetZLine(0, 30)
    sprite('jb408_02', 3)
    sprite('jb408_01', 3)
    XImpulseAcceleration(50)
    TriggerUponForState('jbef408_DashEff', 32)
    sprite('jb408_03', 4)
    sprite('jb408_04', 4)
    SetZLine(1, 30)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    XImpulseAcceleration(20)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    EnableAfterimage(0)
    sprite('jb408_05', 3)


@State
def Assault_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
        HitCancel('Shot')
        HitOrBlockCancel('UltimateChage')
    sprite('jb403_13', 2)
    SetInertia(30000)
    PreDashEffects(100, 1, 0)
    sprite('jb403_14', 2)
    sprite('jb403_01', 2)
    sprite('jb403_02', 2)
    sprite('jb403_03', 2)
    PerInertia(50)
    DashEffects(100, 1, 0)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb403_04', 2)
    Voiceline('jb204')
    sprite('jb403_05', 2)
    EndMomentum(1)
    CreateObject('jbef403_zanzou', 100)
    CreateObject('jbef403_zanzou2', 100)
    sprite('jb403_06', 2)
    Recovery()
    Unknown2063()
    sprite('jb403_07', 4)
    sprite('jb403_08', 4)
    sprite('jb403_09', 4)
    sprite('jb403_10', 4)
    sprite('jb403_11', 4)
    sprite('jb403_12', 4)


@State
def Assault_Mid():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        uponSendToLabel(LANDING, 9)
        HitOrBlockCancel('UltimateChage')
    sprite('jb404_15', 2)
    Voiceline('jb205')
    sprite('jb404_16', 3)
    sprite('jb404_17', 3)
    sprite('jb404_01', 4)
    physicsXImpulse(20000)
    physicsYImpulse(20000)
    setGravity(1600)
    JumpEffects(3, 100)
    sprite('jb404_02', 4)
    sprite('jb404_03', 4)
    sprite('jb404_04', 3)
    XImpulseAcceleration(80)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb404_05', 1)
    XImpulseAcceleration(80)
    StartMultihit()
    CreateObject('jbef404_zanzou', 100)
    sprite('jb404_05', 3)
    sprite('jb404_06', 3)
    XImpulseAcceleration(80)
    Recovery()
    sprite('jb404_07', 3)
    XImpulseAcceleration(80)
    sprite('jb404_08', 3)
    sprite('jb404_09', 32767)
    label(9)
    sprite('jb404_10', 5)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb404_11', 5)
    AttackOffOrBlockCancel('UltimateChage')


@State
def AirAssault_Mid():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Assault_Mid_Atk')
        SLOT_61 = 1
        ForcedLandingRecovery(12, 1)
        HitOrBlockCancel('UltimateChage')
    sprite('jb404_18', 3)
    EndMomentum(1)
    physicsXImpulse(8000)
    physicsYImpulse(24000)
    EndYPhysicsImpulse()
    Voiceline('jb205')
    sprite('jb404_19', 2)
    sprite('jb404_20', 2)
    sprite('jb404_01', 2)
    sprite('jb404_02', 2)
    sprite('jb404_03', 2)
    XImpulseAcceleration(80)
    sprite('jb404_04', 2)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb404_05', 1)
    XImpulseAcceleration(80)
    StartMultihit()
    CreateObject('jbef404_zanzou', 100)
    sprite('jb404_05', 3)
    sprite('jb404_06', 3)
    XImpulseAcceleration(80)
    Recovery()
    sprite('jb404_07', 2)
    XImpulseAcceleration(80)
    sprite('jb404_08', 2)
    sprite('jb404_09', 2)
    sprite('jb404_13', 2)
    sprite('jb404_14', 2)


@State
def Assault_Multi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Multi_Atk')
        uponSendToLabel(LANDING, 2)
        HitOrBlockCancel('UltimateChage')
    sprite('jb405_00', 3)
    sprite('jb405_01', 3)
    EnableCollision(0)
    physicsXImpulse(30000)
    physicsYImpulse(32000)
    EndYPhysicsImpulse()
    JumpEffects(3, 100)
    sprite('jb405_02', 3)
    XImpulseAcceleration(80)
    Voiceline('jb206')
    sprite('jb405_03', 3)
    XImpulseAcceleration(80)
    sprite('jb405_04', 3)
    XImpulseAcceleration(80)
    sprite('jb405_05', 3)
    CreateObject('jbef405_loop', 100)
    AttackOff()
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('jb405_06', 3)
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    label(10)
    sprite('jb405_05', 3)
    RefreshMultihit()
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('jb405_08', 4)
    EndMomentum(1)
    DespawnEAEffect('jbef405_loop')
    LandingEffects(100, 1, 1)
    ScreenShake(0, 8000)
    ForceFaceSprite()
    sprite('jb405_09', 4)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb405_10', 4)
    EnableAfterimage(0)
    CreateObject('jbef405_zanzou', 100)
    RefreshMultihit()
    callSubroutine('Assault_MultiFinish_Atk')
    sprite('jb405_11', 4)
    Recovery()
    Unknown2063()
    sprite('jb405_12', 4)
    sprite('jb405_13', 4)
    sprite('jb405_14', 3)
    sprite('jb405_15', 3)
    sprite('jb405_16', 3)
    sprite('jb405_17', 3)


@State
def AirAssault_Multi():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Assault_Multi_Atk')
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 2)
        HitOrBlockCancel('UltimateChage')
    sprite('jb405_19', 2)
    physicsXImpulse(15000)
    physicsYImpulse(28000)
    EndYPhysicsImpulse()
    sprite('jb405_01', 3)
    EnableCollision(0)
    JumpEffects(3, 100)
    sprite('jb405_02', 3)
    XImpulseAcceleration(80)
    Voiceline('jb206')
    sprite('jb405_03', 3)
    XImpulseAcceleration(80)
    sprite('jb405_04', 3)
    XImpulseAcceleration(80)
    sprite('jb405_05', 3)
    CreateObject('jbef405_loop', 100)
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    label(10)
    sprite('jb405_05', 3)
    RefreshMultihit()
    sprite('jb405_06', 3)
    RefreshMultihit()
    sprite('jb405_07', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('jb405_08', 4)
    EndMomentum(1)
    DespawnEAEffect('jbef405_loop')
    LandingEffects(100, 1, 1)
    ScreenShake(0, 8000)
    ForceFaceSprite()
    sprite('jb405_09', 4)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb405_10', 4)
    EnableAfterimage(0)
    CreateObject('jbef405_zanzou', 100)
    RefreshMultihit()
    callSubroutine('Assault_MultiFinish_Atk')
    sprite('jb405_11', 4)
    Recovery()
    Unknown2063()
    sprite('jb405_12', 4)
    sprite('jb405_13', 4)
    sprite('jb405_14', 3)
    sprite('jb405_15', 3)
    sprite('jb405_16', 3)
    sprite('jb405_17', 3)


@State
def Assault_ChageAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Chage_Atk')
        HitOrBlockCancel('UltimateChage')
        uponSendToLabel(LANDING, 10)
    sprite('jb406_17', 2)
    physicsXImpulse(20000)
    sprite('jb406_18', 2)
    sprite('jb406_19', 2)
    XImpulseAcceleration(20)
    sprite('jb406_01', 2)
    CommonSE('024_getset_b')
    sprite('jb406_02', 2)
    sprite('jb406_03', 3)
    label(0)
    sprite('jb406_04', 3)
    XImpulseAcceleration(50)
    sprite('jb406_05', 3)
    loopRest()
    gotoLabel(0)
    label(8)
    sprite('jb406_06', 3)
    clearUponHandler(EVERY_FRAME)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    Voiceline('jb207')
    EndMomentum(1)
    sprite('jb406_07', 3)
    AddX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    CreateObject('jbef406_zanzou', 100)
    CreateObject('jbef406_zanzou2', 100)
    LandingEffects(100, 1, 0)
    sprite('jb406_08', 3)
    sprite('jb406_09', 3)
    sprite('jb406_10', 3)
    sprite('jb406_11', 3)
    sprite('jb406_12', 32767)
    label(9)
    sprite('jb406_06', 3)
    clearUponHandler(EVERY_FRAME)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    Voiceline('jb207')
    EndMomentum(1)
    sprite('jb406_07', 1)
    AddX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(24000)
    EndYPhysicsImpulse()
    CreateObject('jbef406_zanzou', 100)
    CreateObject('jbef406_zanzou2', 100)
    LandingEffects(100, 1, 0)
    sprite('jb406_07', 3)
    StartMultihit()
    sprite('jb406_08', 4)
    sprite('jb406_09', 4)
    sprite('jb406_10', 4)
    sprite('jb406_11', 4)
    sprite('jb406_12', 32767)
    label(10)
    sprite('jb406_13', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 0)
    sprite('jb406_14', 3)
    AttackOffOrBlockCancel('UltimateChage')
    sprite('jb406_15', 3)


@State
def UltimateAirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        OppPositionOnHit(1, 110000, -30000)
        AirPushbackX(0)
        AirPushbackY(-80000)
        GroundBounce(1)
        Stagger(100)
        Crumple(100)
        AirUntechableTime(100)
        PushbackX(0)
        Hitstop(1)
        AttackDirection(0)
        DefeatOpponentBehavior(1)
        SLOT_52 = SLOT_32
        if SLOT_32:
            SLOT_52 = 1
            Damage(1250)
        clearUponHandler(LANDING)

        def upon_32():
            clearUponHandler(32)
            EnableRapidCancel(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SLOT_51 = 1
            if SLOT_52:
                CreateObject('jbef_DriveHit', -1)

                def RunOnObject_1():
                    RotationAngle(90000)

        def upon_EVERY_FRAME():
            if SLOT_51:
                clearUponHandler(EVERY_FRAME)
                Damage(200)
        if SLOT_137:
            DamageMultiplier(80)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_32 = 0
    sprite('jb430_00', 3)
    setInvincible(1)
    EndMomentum(1)
    setGravity(-50)
    loopRest()
    if SLOT_52:
        conditionalSendToLabel(100)
    sprite('jb430_01', 3)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('jb430_01', 3)
    DistortionSettings(76, -1, 0)
    HeatChange(-5000)
    ConstantAlphaModifier(-21)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    CreateObject('jbeff_warp', -1)
    EndMomentum(1)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('null', 15)
    TeleportToObject(22)
    AddX(200000)
    AddY(250000)
    ForceFaceSprite()
    CameraControlEnable(1)
    SetXCollisionFromOrigin(40)
    sprite('jb430_01', 3)
    setGravity(-50)
    ConstantAlphaModifier(21)
    CreateObject('jbeff_warp', -1)
    CreateObject('EMB', -1)
    CommonSE('002_highjump_0')
    SLOT_32 = 0
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CameraControlEnable(0)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    label(0)
    sprite('jb430_04', 3)
    Voiceline('jb250')
    physicsYImpulse(5000)
    setGravity(500)
    CommonSE('000_airdash_0')
    sprite('jb430_05', 3)
    sprite('jb430_06', 3)
    sprite('jb430_07', 3)
    sprite('jb430_08', 3)
    sprite('jb430_09', 3)
    sprite('jb430_10', 3)
    PrivateSE('jbse_01')
    sprite('jb430_11', 3)
    sprite('jb430_12', 3)
    physicsYImpulse(-80000)
    setGravity(0)
    uponSendToLabel(LANDING, 1)
    label(9)
    sprite('jb430_12', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb430_12', 1)
    AttackOff()
    SetXCollisionFromOrigin(-1)
    if SLOT_51:
        conditionalSendToLabel(2)
    sprite('jb430_13', 3)
    setInvincible(0)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_17', 4)
    sprite('jb430_18', 4)
    sprite('jb430_19', 4)
    sprite('jb430_20', 4)
    sprite('jb430_21', 4)
    sprite('jb430_22', 4)
    sprite('jb430_23', 4)
    ExitState()
    label(2)
    sprite('jb430_12', 3)
    RefreshMultihit()
    AirHitstunAnimation(2)
    OppPositionOnHit(0, 0, 0)
    GroundBounce(0)
    Hitstop(0)
    HitAnywhere(1)
    OnlyHitPlayer(1)
    DamageFromStateOnly('UltimateAirAssault')
    EnableRapidCancel(0)
    CreateObject('jb430_slashMatome', 100)
    sprite('jb430_13', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    RefreshMultihit()
    Damage(2500)
    Hitstop(20)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(15000)
    AirPushbackY(40000)
    UseSlashHitspark(1)
    DamageEffect(4, 'jbef_driveslash_sumi')
    DefeatOpponentBehavior(0)
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        EnableRapidCancel(1)
    CommonSE('025_cleanhit_slash')
    Voiceline('jb251')
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_17', 4)
    sprite('jb430_18', 4)
    sprite('jb430_19', 4)
    sprite('jb430_20', 4)
    sprite('jb430_21', 4)
    sprite('jb430_22', 4)
    sprite('jb430_23', 4)


@State
def UltimateAirAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        OppPositionOnHit(1, 110000, -30000)
        AirPushbackX(0)
        AirPushbackY(-80000)
        GroundBounce(1)
        Stagger(100)
        Crumple(100)
        AirUntechableTime(100)
        PushbackX(0)
        Hitstop(1)
        AttackDirection(0)
        DefeatOpponentBehavior(1)
        AttackType(4)
        SLOT_52 = SLOT_32
        if SLOT_32:
            SLOT_52 = 1
            Damage(1250)
        clearUponHandler(LANDING)

        def upon_32():
            clearUponHandler(32)
            EnableRapidCancel(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SLOT_51 = 1
            if SLOT_52:
                CreateObject('jbef_DriveHit', -1)

                def RunOnObject_1():
                    RotationAngle(90000)

        def upon_EVERY_FRAME():
            if SLOT_51:
                clearUponHandler(EVERY_FRAME)
                Damage(200)
        if SLOT_137:
            DamageMultiplier(80)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_32 = 0
    sprite('jb430_00', 3)
    setInvincible(1)
    EndMomentum(1)
    setGravity(-50)
    loopRest()
    if SLOT_52:
        conditionalSendToLabel(100)
    sprite('jb430_01', 3)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('jb430_01', 3)
    DistortionSettings(76, -1, 0)
    HeatChange(-5000)
    ConstantAlphaModifier(-21)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    CreateObject('jbeff_warp', -1)
    EndMomentum(1)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('null', 15)
    TeleportToObject(22)
    AddX(200000)
    AddY(250000)
    ForceFaceSprite()
    CameraControlEnable(1)
    SetXCollisionFromOrigin(40)
    sprite('jb430_01', 3)
    setGravity(-50)
    ConstantAlphaModifier(21)
    CreateObject('jbeff_warp', -1)
    CreateObject('EMB', -1)
    CommonSE('002_highjump_0')
    SLOT_32 = 0
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CameraControlEnable(0)
    sprite('jb430_02', 3)
    sprite('jb430_03', 3)
    sprite('jb430_01', 3)
    label(0)
    sprite('jb430_04', 3)
    Voiceline('jb250')
    physicsYImpulse(5000)
    setGravity(500)
    CommonSE('000_airdash_0')
    sprite('jb430_05', 3)
    sprite('jb430_06', 3)
    sprite('jb430_07', 3)
    sprite('jb430_08', 3)
    sprite('jb430_09', 3)
    sprite('jb430_10', 3)
    PrivateSE('jbse_01')
    sprite('jb430_11', 3)
    sprite('jb430_12', 3)
    physicsYImpulse(-80000)
    setGravity(0)
    uponSendToLabel(LANDING, 1)
    label(9)
    sprite('jb430_12', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb430_12', 1)
    AttackOff()
    SetXCollisionFromOrigin(-1)
    if SLOT_51:
        conditionalSendToLabel(2)
    sprite('jb430_13', 3)
    setInvincible(0)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_17', 4)
    sprite('jb430_18', 4)
    sprite('jb430_19', 4)
    sprite('jb430_20', 4)
    sprite('jb430_21', 4)
    sprite('jb430_22', 4)
    sprite('jb430_23', 4)
    ExitState()
    label(2)
    sprite('jb430_13', 3)
    RefreshMultihit()
    AirHitstunAnimation(2)
    OppPositionOnHit(0, 0, 0)
    GroundBounce(0)
    Hitstop(0)
    HitAnywhere(1)
    OnlyHitPlayer(1)
    DamageFromStateOnly('UltimateAirAssault_OD')
    EnableRapidCancel(0)
    CreateObject('jb430_slashMatome', 100)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_14', 3)
    sprite('jb430_15', 3)
    sprite('jb430_16', 3)
    sprite('jb430_24', 3)
    RefreshMultihit()
    Damage(800)
    Hitstop(0)
    EnemyHitstopAddition(3, 3, 3)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(15000)
    AirPushbackY(40000)
    UseSlashHitspark(1)
    DamageEffect(4, 'jbef_driveslash_sumi')
    CreateObject('jb430_ODSlash00', 100)
    CommonSE('025_cleanhit_slash')
    Voiceline('jb251')
    sprite('jb430_24', 3)
    RefreshMultihit()
    sprite('jb430_25', 3)
    RefreshMultihit()
    sprite('jb430_25', 3)
    RefreshMultihit()
    sprite('jb403_05ex00', 4)
    RefreshMultihit()
    Hitstop(20)
    EnemyHitstopAddition(0, 0, 0)
    DefeatOpponentBehavior(0)
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        EnableRapidCancel(1)
    PrivateSE('jbse_03')
    PrivateSE('jbse_09')
    sprite('jb403_06ex00', 4)
    sprite('jb403_07ex00', 30)
    sprite('jb403_08ex00', 6)
    sprite('jb403_09ex00', 6)
    sprite('jb403_10ex00', 6)
    sprite('jb403_11ex00', 6)
    sprite('jb403_12ex00', 2)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        AttackDirection(0)
        DamageEffect(8, '')
        DefeatOpponentBehavior(1)
        SLOT_52 = SLOT_32
        if SLOT_32:
            SLOT_52 = 1
            Damage(1250)

        def upon_32():
            clearUponHandler(32)
            EnableRapidCancel(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            TeleportToObject(22)
            AbsoluteY(0)
            AlphaValue(0)
            CameraFollowTarget(23, 22)
            if SLOT_52:
                CreateObject('jbef_DriveHit', -1)
            sendToLabel(1)
        if SLOT_137:
            DamageMultiplier(80)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_32 = 0
            CameraFollowTarget(0, 0)
    sprite('jb431_00', 5)
    EndMomentum(1)
    loopRest()
    if SLOT_52:
        conditionalSendToLabel(100)
    sprite('jb431_01', 3)
    sprite('jb431_02', 3)
    sprite('jb431_03', 3)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('jb431_01', 3)
    sprite('jb431_02', 3)
    sprite('jb431_03', 3)
    DistortionSettings(76, -1, 0)
    HeatChange(-5000)
    setInvincible(1)
    sprite('jb431_04', 3)
    ConstantAlphaModifier(-21)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    CreateObject('jbeff_warp', -1)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('null', 15)
    TeleportToObject(22)
    AddX(300000)
    AbsoluteY(0)
    ForceFaceSprite()
    SetXCollisionFromOrigin(40)
    sprite('jb431_04', 3)
    ConstantAlphaModifier(21)
    CreateObject('jbeff_warp', -1)
    CreateObject('EMB', -1)
    CommonSE('002_highjump_0')
    SLOT_32 = 0
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    label(0)
    sprite('jb431_07', 3)
    physicsXImpulse(20000)
    SpecificInvincibility(0, 0, 0, 1, 0)
    Voiceline('jb252')
    sprite('jb431_08', 2)
    XImpulseAcceleration(200)
    ConstantAlphaModifier(-20)
    sprite('jb431_09', 12)
    CreateObject('jb431_SlashEff', -1)
    CreateObject('jb431_CircleShockEff', -1)
    XImpulseAcceleration(200)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    PrivateSE('jbse_00')
    sprite('jb431_23', 3)
    clearUponHandler(OPPONENT_HIT)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb431_25', 3)
    sprite('jb431_26', 3)
    sprite('jb431_24', 3)
    sprite('jb431_25', 3)
    sprite('jb431_26', 3)
    sprite('jb431_27', 3)
    sprite('jb340_12ex00', 3)
    sprite('jb340_13ex00', 3)
    sprite('jb340_14ex00', 3)
    sprite('jb340_15ex00', 3)
    sprite('jb340_16ex00', 3)
    ExitState()
    label(1)
    sprite('jb431_09', 10)
    RefreshMultihit()
    Hitstop(0)
    HitAnywhere(1)
    OnlyHitPlayer(1)
    Hitstun(40)
    DamageFromStateOnly('UltimateAssault')
    EnableRapidCancel(0)
    physicsXImpulse(50000)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('jb431_10', 5)
    CreateObject('jb431_SlashEndEff', -1)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    physicsXImpulse(20000)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb431_10', 15)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb431_11', 3)
    sprite('jb431_12', 3)
    sprite('jb431_13', 3)
    sprite('jb431_14', 3)
    RefreshMultihit()
    Damage(2000)
    HitstunReset()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Stagger(30)
    Crumple(60)
    CHStagger(30)
    CHCrumple(60)
    UseSlashHitspark(1)
    DamageEffect(4, 'jbef_driveslash_sumi')
    DefeatOpponentBehavior(0)
    DamageFromStateOnly('')
    clearUponHandler(OPPONENT_HIT)

    def upon_OPPONENT_HIT():
        EnableRapidCancel(1)
    TriggerUponForState('jb431_SlashEndEff', 32)
    Voiceline('jb253')
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_18', 5)
    sprite('jb431_19', 5)
    sprite('jb431_20', 5)
    sprite('jb431_21', 5)
    sprite('jb431_22', 4)


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        AttackDirection(0)
        DamageEffect(8, '')
        DefeatOpponentBehavior(1)
        AttackType(4)
        SLOT_52 = SLOT_32
        if SLOT_32:
            SLOT_52 = 1
            Damage(1250)

        def upon_32():
            clearUponHandler(32)
            EnableRapidCancel(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            TeleportToObject(22)
            AbsoluteY(0)
            AlphaValue(0)
            CameraFollowTarget(22, 22)
            if SLOT_52:
                CreateObject('jbef_DriveHit', -1)
            sendToLabel(1)
        if SLOT_137:
            DamageMultiplier(80)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            SLOT_32 = 0
            CameraFollowTarget(0, 0)
    sprite('jb431_00', 5)
    EndMomentum(1)
    loopRest()
    if SLOT_52:
        conditionalSendToLabel(100)
    sprite('jb431_01', 3)
    sprite('jb431_02', 3)
    sprite('jb431_03', 3)
    DistortionSettings(40, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('jb431_01', 3)
    sprite('jb431_02', 3)
    sprite('jb431_03', 3)
    DistortionSettings(76, -1, 0)
    HeatChange(-5000)
    setInvincible(1)
    sprite('jb431_04', 3)
    ConstantAlphaModifier(-21)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    CreateObject('jbeff_warp', -1)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    sprite('jb431_05', 3)
    sprite('null', 15)
    TeleportToObject(22)
    AddX(300000)
    AbsoluteY(0)
    ForceFaceSprite()
    SetXCollisionFromOrigin(40)
    sprite('jb431_04', 3)
    ConstantAlphaModifier(21)
    CreateObject('jbeff_warp', -1)
    CreateObject('EMB', -1)
    CommonSE('002_highjump_0')
    SLOT_32 = 0
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('jb431_05', 3)
    sprite('jb431_06', 3)
    sprite('jb431_04', 3)
    label(0)
    sprite('jb431_07', 3)
    Voiceline('jb252')
    physicsXImpulse(20000)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('jb431_08', 2)
    XImpulseAcceleration(200)
    ConstantAlphaModifier(-20)
    sprite('jb431_09', 12)
    CreateObject('jb431_SlashEff', -1)
    CreateObject('jb431_CircleShockEff', -1)
    XImpulseAcceleration(200)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    PrivateSE('jbse_00')
    sprite('jb431_23', 3)
    clearUponHandler(OPPONENT_HIT)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb431_25', 3)
    sprite('jb431_26', 3)
    sprite('jb431_24', 3)
    sprite('jb431_25', 3)
    sprite('jb431_26', 3)
    sprite('jb431_27', 3)
    sprite('jb340_12ex00', 3)
    sprite('jb340_13ex00', 3)
    sprite('jb340_14ex00', 3)
    sprite('jb340_15ex00', 3)
    sprite('jb340_16ex00', 3)
    ExitState()
    label(1)
    sprite('jb431_09', 10)
    RefreshMultihit()
    Hitstop(0)
    HitAnywhere(1)
    OnlyHitPlayer(1)
    Hitstun(40)
    DamageFromStateOnly('UltimateAssault_OD')
    EnableRapidCancel(0)
    physicsXImpulse(50000)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('jb431_10', 5)
    CreateObject('jb431OD_SlashEffMatome', 100)
    ConstantAlphaModifier(20)
    AlphaValue(128)
    physicsXImpulse(20000)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('jb431_10', 15)
    EndMomentum(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('jb431_11', 3)
    sprite('jb431_12', 3)
    sprite('jb431_13', 3)
    sprite('jb431_14', 3)
    RefreshMultihit()
    Damage(400)
    HitstunReset()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Stagger(30)
    Crumple(60)
    CHStagger(30)
    CHCrumple(60)
    HitsparkSize(600)
    UseSlashHitspark(1)
    DamageEffect(4, 'jbef_driveslash_sumi')
    TriggerUponForState('jb431OD_SlashEffMatome', 32)
    CameraFollowTarget(23, 22)
    sprite('jb431_15', 3)
    RefreshMultihit()
    sprite('jb431_16', 3)
    RefreshMultihit()
    sprite('jb431_17', 3)
    RefreshMultihit()
    sprite('jb431_15', 3)
    RefreshMultihit()
    sprite('jb431_16', 3)
    RefreshMultihit()
    sprite('jb431_17', 3)
    RefreshMultihit()
    sprite('jb431_15', 3)
    RefreshMultihit()
    sprite('jb431_16', 3)
    RefreshMultihit()
    HitsparkSize(1000)
    DefeatOpponentBehavior(0)
    DamageFromStateOnly('')
    clearUponHandler(OPPONENT_HIT)

    def upon_OPPONENT_HIT():
        EnableRapidCancel(1)
    Voiceline('jb253')
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_17', 3)
    sprite('jb431_15', 3)
    sprite('jb431_16', 3)
    sprite('jb431_18', 5)
    sprite('jb431_19', 5)
    sprite('jb431_20', 5)
    sprite('jb431_21', 5)
    sprite('jb431_22', 4)


@State
def UltimateChage():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EnableAfterimage(1)
        AfterimageInterval(4)
        AfterimageCount(4)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(200, 255, 255, 255)
    sprite('jb432_00', 3)
    sprite('jb432_00', 3)
    DistortionSettings(100, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    setInvincible(1)
    EndMomentum(1)
    Voiceline('jb254')
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraPosition(900)
    sprite('jb432_00', 6)
    SetBackground(2)
    sprite('jb432_01', 6)
    CreateObject('jb432_eyerayEff', 100)
    sprite('jb432_02', 6)
    sprite('jb432_03', 6)
    sprite('jb432_04', 6)
    sprite('jb432_05', 24)
    sprite('jb432_06', 3)
    CreateObject('jb432_BodyAuraEff', 100)
    ScreenShake(20000, 20000)
    Voiceline('jb255')
    SLOT_31 = 1
    sprite('jb432_07', 3)
    PrivateSE('jbse_05')
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    sprite('jb432_07', 3)
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    sprite('jb432_07', 3)
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    setInvincible(0)
    sprite('jb432_10', 3)
    sprite('jb432_11', 3)
    sprite('jb432_12', 3)
    sprite('jb432_13', 3)


@State
def UltimateChageEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EnableAfterimage(1)
        AfterimageBlendMode(0)
        AfterimageInterval(4)
    sprite('jb432_00', 3)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    setInvincible(1)
    Voiceline('jb254')
    sprite('jb432_00', 4)
    sprite('jb432_01', 7)
    CreateObject('jb432_eyerayEff', 100)
    sprite('jb432_02', 7)
    sprite('jb432_03', 7)
    sprite('jb432_04', 7)
    sprite('jb432_05', 20)
    Voiceline('jb255')
    sprite('jb432_06', 3)
    CreateObject('jb432_BodyAuraEff', 100)
    sprite('jb432_07', 3)
    CreateObject('UltimateChageEX_Atk', -1)
    PrivateSE('jbse_05')
    sprite('jb432_08', 3)
    setInvincible(0)
    sprite('jb432_09', 3)
    sprite('jb432_07', 3)
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    sprite('jb432_07', 3)
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    sprite('jb432_07', 3)
    sprite('jb432_08', 3)
    sprite('jb432_09', 3)
    sprite('jb432_10', 3)
    sprite('jb432_11', 3)
    sprite('jb432_12', 2)
    sprite('jb432_13', 2)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('jb440_00', 4)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('jb280')
    sprite('jb312_01ex00', 4)
    sprite('jb312_02ex00', 7)
    sprite('jb312_03ex00', 4)
    CommonSE('003_swing_grap_0_2')
    sprite('jb312_04ex00', 3)
    sprite('jb312_04ex00', 8)
    AttackOff()
    setInvincible(0)
    sprite('jb312_05ex00', 9)
    sprite('jb312_06ex00', 9)
    sprite('jb312_07ex00', 8)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
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
    sprite('jb440_00', 2)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('jb280')
    sprite('jb312_01ex00', 2)
    sprite('jb312_02ex00', 3)
    sprite('jb312_03ex00', 2)
    CommonSE('003_swing_grap_0_2')
    sprite('jb312_04ex00', 3)
    sprite('jb312_04ex00', 8)
    AttackOff()
    setInvincible(0)
    sprite('jb312_05ex00', 9)
    sprite('jb312_06ex00', 9)
    sprite('jb312_07ex00', 8)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(1100)
        AttackP2(100)
        Hitstop(9)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(10)
        YImpulseBeforeWallbounce(0)
        OppPositionOnHit(3, 0, 15000)
        AirUntechableTime(60)
        Wallbounce(1)
        StickToWall(1)
        AirHitstunAfterWallbounce(60)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        DefeatOpponentBehavior(1)
        MinimumDamage(10)
        SetBackground(1)
        CHStateIfCHStart(3)

        def upon_STATE_END():
            TriggerUponForState('BurstDD_Camera', 32)
    sprite('jb312_04ex00', 3)
    AttackOff()
    sprite('jb312_04ex00', 3)
    CreateObject('BurstDD_Camera', -1)
    sprite('jb440_01', 3)
    sprite('jb440_02', 3)
    physicsXImpulse(-15000)
    sprite('jb440_03', 3)
    XImpulseAcceleration(80)
    sprite('jb440_04', 3)
    XImpulseAcceleration(80)
    sprite('jb440_05', 3)
    XImpulseAcceleration(80)
    sprite('jb440_06', 3)
    XImpulseAcceleration(80)
    sprite('jb440_07', 6)
    XImpulseAcceleration(50)
    sprite('jb440_07', 6)
    XImpulseAcceleration(50)
    sprite('jb440_08', 3)
    physicsXImpulse(5000)
    sprite('jb440_09', 3)
    physicsXImpulse(10000)
    CommonSE('000_airdash_0')
    Voiceline('jb281')
    sprite('jb440_10', 1)
    physicsXImpulse(80000)
    SetAcceleration(5000)
    RefreshMultihit()
    CommonSE('006_swing_blade_1')
    sprite('jb440_11', 1)
    CreateObject('jb440_startAtk00', 100)
    PrivateSE('jbse_09')
    sprite('jb440_12', 1)
    sprite('jb440_10', 1)
    sprite('jb440_11', 1)
    sprite('jb440_12', 1)
    label(1)
    sprite('jb440_10', 1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            PrivateFunction5(80)
            if SLOT_XDistanceFromCenterOfStage < SLOT_0:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(2)
        else:
            PrivateFunction5(80)
            if SLOT_XDistanceFromCenterOfStage > SLOT_0:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(2)
    sprite('jb440_11', 1)
    sprite('jb440_12', 1)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('jb440_13', 3)
    EndMomentum(1)
    SetPosXByScreenPer(85)
    sprite('jb440_14', 8)
    sprite('jb440_15', 3)
    sprite('jb440_16', 3)
    RefreshMultihit()
    Hitstop(20)
    AirPushbackY(25000)
    ResetGravity()
    OppPositionOnHit(1, 200000, 150000)
    ResetWallbounce()
    Wallbounce(1)
    StickToWall(0)
    AirHitstunAfterWallbounce(60)
    WallbounceReboundTime(0)
    Unknown11102(1)
    DefeatOpponentBehavior(0)
    HitAnywhere(1)
    physicsXImpulse(-15000)
    physicsYImpulse(28000)
    EndYPhysicsImpulse()
    if SLOT_51:
        DefeatOpponentBehavior(1)
        StickToWall(1)
        physicsXImpulse(-10000)
    CreateObject('jb440_slash00', 100)
    PrivateSE('jbse_03')
    PrivateSE('jbse_09')
    Voiceline('jb282')
    sprite('jb440_17', 3)
    sprite('jb440_18', 3)
    sprite('jb440_19', 2)
    sprite('jb251_05ex00', 3)
    sprite('jb251_06ex00', 3)
    sprite('jb251_07ex00', 3)
    sprite('jb251_08ex00', 3)
    sprite('jb251_09ex00', 3)
    sprite('jb251_10ex00', 3)
    sprite('jb251_11ex00', 32767)
    uponSendToLabel(LANDING, 3)
    label(3)
    sprite('jb024_00', 2)
    EndMomentum(1)
    sprite('jb024_01', 2)
    sprite('jb024_02', 8)
    sprite('jb024_03', 3)
    if SLOT_51:
        sendToLabel(100)
        uponSendToLabel(LANDING, 102)
    sprite('jb024_04', 3)
    ExitState()
    label(100)
    sprite('jb024_03', 2)
    sprite('jb401_02', 2)
    physicsXImpulse(40000)
    CreateObject('jb440_AddAtk', 100)
    PrivateSE('jbse_03')
    PrivateSE('jbse_09')
    sprite('jb401_03', 4)
    RefreshMultihit()
    Damage(3000)
    Hitstop(12)
    OppPositionOnHit(1, 500000, 0)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    ResetVerticalDrag()
    ResetPushback()
    ResetGravity()
    ResetWallbounce()
    DefeatOpponentBehavior(0)
    XImpulseAcceleration(50)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    TriggerUponForState('BurstDD_Camera', 32)
    CommonSE('025_cleanhit_slash')
    Voiceline('jb283')
    sprite('jb401_04', 4)
    XImpulseAcceleration(80)
    sprite('jb401_05', 4)
    XImpulseAcceleration(50)
    sprite('jb401_06', 4)
    XImpulseAcceleration(50)
    sprite('jb401_07', 3)
    sprite('jb401_08', 3)
    sprite('jb401_12', 3)
    sprite('jb401_13', 3)
    sprite('jb401_14', 3)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(101)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('jb401_09', 4)
    LandingEffects(100, 1, 0)
    EndMomentum(1)
    sprite('jb401_10', 4)
    sprite('jb401_11', 4)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DamageFromStateOnly('AstralHeat')
        AttackLevel_(5)
        Damage(0)
        MinimumDamage(100)
        Hitstop(3)
        OppPositionOnHit(1, 180000, 0)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        PushbackX(60000)
        Hitstun(999)
        AirUntechableTime(999)
        Stagger(999)
        Crumple(999)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        AttackDirection(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            CreateObject('Astral_Camera', -1)
            AstralHeatCleanup(1, 1)
            PlayPlayAstralBGM(1)
            DisableOppPushCollision(1)
            EnableCollision(0)
            WallCollisionDetection(0)
            ScreenCollision(0)
            HUDVisibillity(1)
            SetAcceleration(0)
            physicsXImpulse(0)
            SLOT_31 = 0
            SLOT_32 = 0
            sendToLabel(1)
    sprite('jb450_00', 3)
    setInvincible(1)
    EndMomentum(1)
    sprite('jb450_01', 3)
    DistortionSettings(35, -1, 2)
    EmptyHeat()
    CreateObject('EMB_JB_AH', -1)
    sprite('jb450_02', 3)
    sprite('jb450_03', 3)
    sprite('jb450_04', 3)
    sprite('jb450_05', 3)
    sprite('jb450_03', 3)
    sprite('jb450_04', 3)
    sprite('jb450_05', 3)
    sprite('jb450_03', 3)
    sprite('jb450_04', 3)
    sprite('jb450_05', 3)
    sprite('jb450_03', 3)
    sprite('jb450_04', 3)
    sprite('jb450_05', 3)
    sprite('jb450_06', 3)
    CreateObject('jb450_AtkAura', -1)
    CommonSE('022_magiccircle_b')
    sprite('jb450_07', 3)
    setInvincible(0)
    sprite('jb450_08', 3)
    sprite('jb450_09', 3)
    sprite('jb450_07', 4)
    sprite('jb450_08', 4)
    sprite('jb450_09', 4)
    sprite('jb450_07', 5)
    sprite('jb450_08', 5)
    sprite('jb450_09', 5)
    sprite('jb450_39', 6)
    sprite('jb450_40', 6)
    sprite('jb450_41', 14)
    TriggerUponForState('jb450_AtkAura', 32)
    sprite('jb321_13ex00', 7)
    sprite('jb321_14ex00', 7)
    sprite('jb321_15ex00', 7)
    ExitState()
    label(1)
    sprite('keep', 2)
    AttackDirection(1)
    sprite('jb450_07', 3)
    sprite('jb450_08', 3)
    sprite('jb450_09', 3)
    sprite('jb450_07', 3)
    sprite('jb450_08', 3)
    sprite('jb450_09', 3)
    sprite('jb450_07', 3)
    sprite('jb450_08', 3)
    sprite('jb450_09', 3)
    sprite('jb450_07', 3)
    sprite('jb450_08', 3)
    sprite('jb450_09', 3)
    sprite('jb450_10', 3)
    sprite('jb450_11', 3)
    TriggerUponForState('jb450_AtkAura', 32)
    CreateObject('jb450_kaihouAura', -1)
    PrivateSE('jbse_05')
    Voiceline('jb290')
    sprite('jb450_12', 3)
    sprite('jb450_13', 3)
    sprite('jb450_14', 8)
    CreateObject('jb450_kidou', -1)
    EnableAfterimage(1)
    AfterimageInterval(5)
    sprite('jb450_15', 8)
    sprite('jb450_16', 8)
    CreateObject('jb450_kidou2', -1)
    sprite('jb450_17', 8)
    sprite('jb450_18', 3)
    EnableAfterimage(0)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    Voiceline('jb291')
    TriggerUponForState('Astral_Camera', 32)
    CreateObject('jbef_450flash', -1)
    CreateObject('jbef_450weakpointBG', -1)
    if CharacterIDCheck('hz'):
        CreateObject('jbef_450weakpoint_Hazama', -1)
        CreateObject('jbef_450weakpoint', -1)
    elif CharacterIDCheck('tm'):
        CreateObject('jbef_450weakpoint_Terumi', -1)
    elif CharacterIDCheck('su'):
        CreateObject('jbef_450weakpoint_Terumi', -1)
    else:
        CreateObject('jbef_450weakpoint', -1)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    TriggerUponForState('Astral_Camera', 33)
    TriggerUponForState('jbef_450weakpointBG', 32)
    TriggerUponForState('jbef_450weakpoint', 32)
    TriggerUponForState('jbef_450weakpoint_Terumi', 32)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_17', 3)
    sprite('jb450_18', 3)
    sprite('jb450_19', 3)
    sprite('jb450_20', 4)
    sprite('jb450_21', 4)
    sprite('jb450_22', 4)
    sprite('jb450_23', 8)
    sprite('jb450_24', 3)
    CommonSE('000_airdash_0')
    PrivateSE('jbse_00')
    sprite('jb450_25', 3)
    Voiceline('jb292')
    sprite('jb450_25', 4)
    CreateParticle('jbef_450issen', 103)
    CreateObject('jb450_ZanEff', -1)
    AlphaValue(0)
    RotationAngle(340000)
    XSpeed2(110000, 0)
    CreateObject('jb450_BG', -1)
    sprite('jb450_25', 8)
    AttackLevel_(3)
    Damage(4300)
    Hitstop(0)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(0)
    AirPushbackY(1)
    YImpulseBeforeWallbounce(0)
    DisableOppPushCollision(1)
    UseSlashHitspark(1)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-150000)
            AddY(-100000)
    sprite('jb450_25', 10)
    EndMomentum(1)
    sprite('jb450_25', 4)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(55000)
    XSpeed2(100000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-250000)
            AddY(-400000)
    sprite('jb450_25', 7)
    EndMomentum(1)
    sprite('jb450_25', 5)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(325000)
    XSpeed2(110000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-150000)
            AddY(-50000)
    sprite('jb450_25', 3)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(60000)
    XSpeed2(110000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AlphaValue(0)
            AddX(-250000)
            AddY(-400000)
    sprite('jb450_25', 6)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(325000)
    XSpeed2(110000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-150000)
            AddY(-50000)
    sprite('jb450_25', 5)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(60000)
    XSpeed2(120000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-250000)
            AddY(-400000)
    sprite('jb450_25', 2)
    CreateObject('jb450_ZanEff', -1)
    RotationAngle(325000)
    XSpeed2(130000, 0)
    RefreshMultihit()

    def upon_EVERY_FRAME():

        def RunOnObject_22():
            TeleportToObject(22)
            AddX(-150000)
            AddY(-50000)
    sprite('jb450_25', 25)
    clearUponHandler(EVERY_FRAME)
    RotationAngle(0)
    EndMomentum(1)

    def RunOnObject_22():
        AlphaValue(255)
        TeleportToObject(22)
        AddX(-200000)
        AddY(-100000)
    sprite('jb450_25', 20)
    CreateObject('jb450_ZanEff', -1)
    physicsXImpulse(120000)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(1)
    ResetGravity()
    AirUntechableTime(999)
    Floorslide(999)
    RefreshMultihit()
    sprite('jb450_25', 24)
    TriggerUponForState('Astral_Camera', 34)
    sprite('jb450_25', 12)
    RefreshMultihit()
    AttackLevel_(0)
    Damage(0)
    OppPositionOnHit(0, 0, 0)
    EnemyHitstopAddition(999, 999, 999)
    NoAttackOffset(1)
    HitAnywhere(1)
    DamageEffect(8, '')
    TriggerUponForState('Astral_Camera', 35)
    CreateObject('jb450_RedBG', -1)
    CreateObject('jbef_450ZanzoNokosiMato', -1)
    sprite('jb450_26', 10)
    AlphaValue(255)
    EndMomentum(1)
    AbsoluteY(0)
    TeleportToObject(22)
    AddX(400000)
    PrivateSE('jbse_01')
    sprite('jb450_27', 8)
    sprite('jb450_28', 8)
    sprite('jb450_29', 8)
    sprite('jb450_30', 18)
    Voiceline('jb293')
    sprite('jb401_02ex02', 1)
    CreateObject('jb450_Slash', -1)
    PrivateSE('jbse_09')
    TriggerUponForState('Astral_Camera', 36)
    AttackLevel_(5)
    Damage(9000)
    EnemyHitstopAddition(0, 0, 0)
    AirPushbackX(40000)
    AirPushbackY(40000)
    YImpulseBeforeWallbounce(0)
    NoAttackOffset(0)
    DamageEffect(0, '')
    HitAnywhere(1)
    RefreshMultihit()
    sprite('jb401_02ex02', 2)
    sprite('jb450_31', 3)
    DespawnEAEffect('jb450_RedBG')
    CreateObject('jb450_BG2', -1)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    TriggerUponForState('Astral_Camera', 37)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb401_02ex02', 1)
    Damage(20000)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpulseBeforeWallbounce(0)
    DefeatOpponentBehavior(3)
    RefreshMultihit()
    SetBackground(0)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    sprite('jb450_33', 3)
    sprite('jb450_34', 3)
    sprite('jb450_32', 3)
    TriggerUponForState('Astral_Camera', 38)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    sprite('jb450_35', 60)
    sprite('jb450_35', 80)
    WinAction()
    sprite('jb450_36', 7)
    sprite('jb450_37', 7)
    CreateParticle('jbef_noutou_bloom', 0)
    PrivateSE('jbse_07')
    DemoTimer(90)
    sprite('jb450_38', 32767)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('jb054')
    sprite('jb900_00', 6)
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
    sprite('jb900_01', 6)
    sprite('jb900_00', 6)
    CreateObject('jb900_Ase', 0)
    sprite('jb900_02', 6)
    sprite('jb900_00', 6)
    sprite('jb900_01', 6)
    sprite('jb900_00', 6)
    sprite('jb900_02', 20)
    sprite('jb900_00', 6)
    sprite('jb900_01', 20)
    label(0)
    sprite('jb900_00', 6)
    sprite('jb900_02', 6)
    sprite('jb900_00', 6)
    sprite('jb900_01', 6)
    sprite('jb900_00', 6)
    sprite('jb900_02', 6)
    sprite('jb900_00', 6)
    sprite('jb900_01', 6)
    sprite('jb900_00', 6)
    sprite('jb900_02', 20)
    sprite('jb900_00', 6)
    sprite('jb900_01', 20)
    loopRest()
    gotoLabel(0)


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(250000)
    sprite('jb901_00', 50)
    physicsYImpulse(-150)
    sprite('jb901_00', 50)
    physicsYImpulse(150)
    Voiceline('jb055')
    label(0)
    sprite('jb901_00', 50)
    physicsYImpulse(-150)
    sprite('jb901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('jb000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('jb055', 13153, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('jb400', 14177, 12643, 24885, 25399, 12340, 14177, 14179, 
        14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb401', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb404', 14177, 14179, 14177, 13667, 24880, 25399, 24887, 
        25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb406', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('jb407', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('jb410', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb411', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb412', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb413', 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('jb414', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('jb000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb055', 13409, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb400', 14177, 14179, 14177, 13411, 24880, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb401', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb405', 14177, 14179, 14177, 13923, 24880, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb406', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb407', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb410', 14177, 14179, 14177, 14179, 14177, 13667, 
            14177, 13667, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb411', 14177, 14179, 14177, 14179, 14177, 14179, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('jb412', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb413', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('jb414', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            Unknown18011('jb400', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb401', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb500', 14177, 14179, 14177, 14179, 14177, 14179,
                24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb501', 14177, 14179, 14177, 14179, 14177, 13923,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('jb502', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 12641, 25394, 25399, 12342, 14177, 13667, 
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('jb503', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tk'):
            Unknown18011('jb508', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 12849, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb509', 14691, 24880, 25399, 24887, 25399, 24887,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('jb520', 14433, 14435, 14433, 13923, 24885, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb521', 12641, 25394, 24887, 25399, 12343, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('jb532', 12641, 25394, 24887, 25399, 24887, 25399,
                12344, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 
                25394, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb533', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('pt'):
            Unknown18011('jb534', 14433, 14435, 14433, 14179, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb535', 14177, 14179, 14177, 13155, 24885, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('jb400', 14177, 14179, 14177, 13667, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb401', 12641, 25398, 24887, 25399, 12341, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb548', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('jb549', 14177, 14179, 14177, 14179, 14177, 14179,
                12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('jb400', 14177, 14179, 14177, 14179, 13923, 24880,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14179, 24880, 25400, 24888, 
                25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb550', 14177, 14179, 14177, 14435, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb551', 14177, 14179, 14177, 14435, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('jb552', 14177, 12899, 24884, 13617, 14179, 14177,
                14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb553', 14433, 14435, 14433, 14435, 12641, 25397,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 13617, 12899, 24885, 
                25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('jb400', 14433, 14435, 14433, 14435, 12641, 25397,
                12342, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb401', 14433, 14435, 14433, 14435, 14433, 14435,
                12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb558', 14433, 14435, 14433, 14435, 24880, 25399,
                24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('jb559', 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('jb400', 14177, 14179, 14177, 14179, 13923, 24880,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14179, 24880, 25400, 24888, 
                25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('jb564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14179, 24880, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('jb565', 14177, 14179, 14177, 14435, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(100)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('tk'):
        SyncEntry()
        gotoLabel(140)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('vh'):
        SyncEntry()
        gotoLabel(260)
    if CharacterIDCheck('pt'):
        SyncEntry()
        gotoLabel(270)
    if CharacterIDCheck('kk'):
        SyncEntry()
        gotoLabel(340)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ce'):
        SyncEntry()
        gotoLabel(360)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(0)
    sprite('jb600_00', 4)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('jb600_00', 20)
    sprite('jb600_01', 7)
    sprite('jb600_02', 90)
    Voiceline('jb411')
    sprite('jb600_03', 7)
    sprite('jb600_04', 7)
    CommonSE('019_cloth_c')
    sprite('jb600_05', 7)
    sprite('jb600_06', 7)
    sprite('jb600_07', 10)
    CreateObject('jbef600_manto', 100)
    sprite('jb600_08', 7)
    sprite('jb600_09', 7)
    Voiceline('jb412')
    sprite('jb600_10', 7)
    DemoTimer(120)
    ExitState()
    label(10)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('keep', 1)
    Voiceline('jb413')
    SetActionMark(2)
    if SLOT_44:
        SetActionMark(3)
    label(11)
    sprite('jb601_00', 20)
    AddActionMark(-1)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(11)
    sprite('jb601_00', 20)
    sprite('jb601_03', 9)
    Voiceline('jb414')
    sprite('jb601_04', 9)
    DemoTimer(120)
    loopRest()
    ExitState()
    label(100)
    sprite('jb600_00', 4)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(100)
    sprite('jb600_00', 20)
    sprite('jb600_01', 7)
    sprite('jb600_02', 90)
    Voiceline('jb500')
    sprite('jb600_03', 7)
    sprite('jb600_04', 7)
    CommonSE('019_cloth_c')
    sprite('jb600_05', 7)
    sprite('jb600_06', 7)
    sprite('jb600_07', 10)
    CreateObject('jbef600_manto', 100)
    sprite('jb600_08', 7)
    sprite('jb600_09', 7)
    sprite('jb600_10', 7)
    DemoTimer(60)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(110)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(110)
    sprite('keep', 1)
    Voiceline('jb502')
    SetActionMark(3)
    label(111)
    sprite('jb601_00', 20)
    AddActionMark(-1)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(111)
    sprite('jb601_00', 20)
    sprite('jb601_03', 9)
    sprite('jb601_04', 9)
    DemoTimer(60)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(140)
    sprite('jb602_00', 10)
    uponSendToLabel(32, 141)
    sprite('jb602_00', 32767)
    loopRest()
    label(141)
    sprite('jb602_03', 7)
    sprite('jb602_01', 7)
    sprite('jb602_02', 12)
    Voiceline('jb508')
    sprite('jb602_01', 6)
    sprite('jb602_00', 30)
    CreateParticle('jbef_tameiki', 0)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 10)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 60)
    sprite('jb602_06', 8)
    DemoEndOnVoiceEnd(1)
    DemoTimer(60)
    ExitState()
    label(200)
    sprite('null', 1)
    uponSendToLabel(32, 201)

    def upon_33():

        def upon_EVERY_FRAME():
            AddActionMark(1)
            if SLOT_2 >= 340:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(204)
    clearUponHandler(LANDING)
    Visibility(1)
    EndMomentum(1)
    ScreenCollision(0)
    XPositionRelativeFacing(-800000)
    AbsoluteY(400000)
    sprite('null', 32767)
    loopRest()
    label(201)
    sprite('null', 1)
    sprite('jb404_01', 2)
    AttackDefaults_StandingSpecial()
    StrikeProjectileLevel(1)
    AttackLevel_(0)
    sprite('jb404_01', 4)
    Visibility(0)
    uponSendToLabel(LANDING, 202)
    physicsXImpulse(36000)
    physicsYImpulse(1000)
    setGravity(1600)
    sprite('jb404_02', 4)
    sprite('jb404_03', 4)
    sprite('jb404_04', 3)
    XImpulseAcceleration(90)
    PrivateSE('jbse_03')
    CommonSE('010_swing_sword_2')
    sprite('jb404_05', 1)
    StartMultihit()
    CreateObject('jbef404_zanzou', 100)
    sprite('jb404_05', 3)

    def upon_OPPONENT_HIT_OR_BLOCK():
        physicsXImpulse(-5000)
        physicsYImpulse(5000)
        EndYPhysicsImpulse()
    sprite('jb404_06', 3)
    sprite('jb404_07', 3)
    XImpulseAcceleration(80)
    sprite('jb404_08', 3)
    sprite('jb404_09', 3)
    sprite('jb404_13', 3)
    sprite('jb404_14', 3)
    label(202)
    sprite('jb024_00', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    XPositionRelativeFacing(-260000)
    sprite('jb024_01', 3)
    sprite('jb024_02', 5)
    sprite('jb024_03', 3)
    sprite('jb024_04', 3)
    label(203)
    sprite('jb000_00', 7)
    sprite('jb000_01', 7)
    sprite('jb000_02', 7)
    sprite('jb000_03', 7)
    sprite('jb000_04', 7)
    sprite('jb000_05', 7)
    sprite('jb000_06', 7)
    sprite('jb000_07', 7)
    sprite('jb000_08', 7)
    sprite('jb000_09', 7)
    sprite('jb000_00ex01', 7)
    sprite('jb000_01ex01', 7)
    sprite('jb000_02ex01', 7)
    sprite('jb000_03ex01', 7)
    sprite('jb000_04ex01', 7)
    sprite('jb000_05ex01', 7)
    sprite('jb000_06ex01', 7)
    sprite('jb000_07ex01', 7)
    sprite('jb000_08ex01', 7)
    sprite('jb000_09ex01', 7)
    sprite('jb000_00ex02', 7)
    sprite('jb000_01ex02', 7)
    sprite('jb000_02ex02', 7)
    sprite('jb000_03ex02', 7)
    sprite('jb000_04ex02', 7)
    sprite('jb000_05ex02', 7)
    sprite('jb000_06ex02', 7)
    sprite('jb000_07ex02', 7)
    sprite('jb000_08ex02', 7)
    sprite('jb000_09ex02', 7)
    loopRest()
    gotoLabel(203)
    label(204)
    sprite('jb300_00', 4)
    Voiceline('jb520')
    sprite('jb300_01', 4)
    sprite('jb300_02', 6)
    sprite('jb300_03', 5)
    CommonSE('024_getset_b')
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_01', 6)
    sprite('jb300_00', 6)
    DemoTimer(100)
    loopRest()
    ExitState()
    label(260)
    sprite('jb611_02', 8)
    CreateObject('jb611_Tail_Event', -1)
    uponSendToLabel(32, 261)

    def upon_STATE_END():
        DespawnEAEffect('jb611_Tail_Event')
    sprite('jb611_02', 32767)
    loopRest()
    label(261)
    sprite('jb611_02', 30)
    sprite('jb611_02', 60)
    Voiceline('jb532')
    sprite('jb611_01', 8)
    sprite('jb611_00', 8)
    sprite('jb000_00', 7)
    DespawnEAEffect('jb611_Tail_Event')
    sprite('jb300_00', 4)
    sprite('jb300_01', 4)
    sprite('jb300_02', 6)
    sprite('jb300_03', 5)
    CommonSE('024_getset_b')
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_01', 6)
    sprite('jb300_00', 6)
    DemoTimer(70)
    loopRest()
    ExitState()
    label(270)
    sprite('jb602_00', 10)
    uponSendToLabel(32, 271)
    sprite('jb602_00', 32767)
    loopRest()
    label(271)
    sprite('jb602_00', 30)
    sprite('jb602_03', 7)
    sprite('jb602_01', 7)
    sprite('jb602_02', 12)
    Voiceline('jb534')
    sprite('jb602_01', 6)
    sprite('jb602_00', 30)
    CreateParticle('jbef_tameiki', 0)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 10)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 60)
    sprite('jb602_06', 8)
    DemoEndOnVoiceEnd(1)
    DemoTimer(60)
    ExitState()
    label(340)
    sprite('jb602_00', 10)
    uponSendToLabel(32, 341)
    sprite('jb602_00', 32767)
    loopRest()
    label(341)
    sprite('jb602_03', 7)
    sprite('jb602_01', 7)
    sprite('jb602_02', 12)
    sprite('jb602_01', 6)
    sprite('jb602_00', 30)
    CreateParticle('jbef_tameiki', 0)
    sprite('jb602_04', 10)
    Voiceline('jb548')
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 10)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 150)
    sprite('jb602_06', 8)
    DemoEndOnVoiceEnd(1)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(350)
    sprite('null', 1)
    Visibility(1)
    XPositionRelativeFacing(-960000)
    EnableCollision(0)
    ScreenCollision(0)
    AttackDefaults_StandingNormal()
    loopRest()
    label(351)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(351)
    sprite('null', 20)
    sprite('jb400_00', 3)
    Visibility(0)
    sprite('jb400_00', 2)
    physicsXImpulse(55000)
    sprite('jb400_01', 5)
    sprite('jb400_02', 5)
    PreDashEffects(100, 1, 1)
    sprite('jb400_03', 3)
    HitAnywhere(1)
    CreateObject('jbef400_slash', 100)
    XImpulseAcceleration(10)
    PrivateSE('jbse_02')

    def upon_OPPONENT_HIT_OR_BLOCK():
        ScreenShake(1000, 10000)
    sprite('jb400_04', 2)
    sprite('jb400_05', 2)
    sprite('jb400_06', 1)
    sprite('jb400_07', 1)
    sprite('jb400_08', 2)
    RefreshMultihit()
    CreateObject('jbef400_slash2', 100)
    XImpulseAcceleration(20)
    PrivateSE('jbse_02')
    sprite('jb400_09', 2)
    sprite('jb400_11', 3)
    SkidEffects(100, 1, 1)
    sprite('jb402_00', 2)
    physicsXImpulse(5000)
    sprite('jb402_01', 3)
    physicsYImpulse(16000)
    EndYPhysicsImpulse()
    sprite('jb402_02', 4)
    sprite('jb402_03', 3)
    sprite('jb402_04', 3)

    def upon_OPPONENT_HIT_OR_BLOCK():
        physicsXImpulse(-5000)
        physicsYImpulse(15000)
        setGravity(2000)
        ScreenShake(1000, 25000)
    RefreshMultihit()
    CreateObject('jbef402_slash', 100)
    PrivateSE('jbse_02')
    sprite('jb402_05', 2)
    sprite('jb402_06', 2)
    sprite('jb402_07', 2)
    sprite('jb402_08', 2)
    sprite('jb402_09', 3)
    sprite('jb402_12', 3)
    uponSendToLabel(LANDING, 353)
    sprite('jb020_04', 3)
    sprite('jb020_05', 3)
    sprite('jb020_06', 3)
    label(352)
    sprite('jb020_07', 4)
    sprite('jb020_08', 4)
    loopRest()
    gotoLabel(352)
    label(353)
    sprite('jb024_00', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    XPositionRelativeFacing(-260000)
    sprite('jb024_01', 3)
    sprite('jb024_02', 5)
    sprite('jb024_03', 3)
    sprite('jb024_04', 3)
    sprite('jb000_00', 7)
    sprite('jb000_01', 7)
    sprite('jb000_02', 7)
    sprite('jb000_03', 7)
    sprite('jb612_00', 8)
    sprite('jb612_01', 8)
    sprite('jb612_02', 8)
    sprite('jb612_03', 8)
    sprite('jb612_04', 10)
    CommonSE('010_swing_sword_1')
    sprite('jb612_05', 3)
    Voiceline('jb550')
    sprite('jb612_06', 3)
    SetActionMark(8)
    label(354)
    sprite('jb612_07', 7)
    AddActionMark(-1)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(354)
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    sprite('jb603_08', 7)
    sprite('jb603_09', 9)
    sprite('jb603_10', 7)
    ObjectUpon(22, 32)
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(360)
    sprite('jb601_00', 7)

    def upon_32():
        SetActionMark(1)
    label(361)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(361)
    sprite('keep', 1)
    Voiceline('jb552')
    SetActionMark(3)
    label(362)
    sprite('jb601_00', 20)
    AddActionMark(-1)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(362)
    sprite('jb601_00', 20)
    sprite('jb601_03', 9)
    sprite('jb601_04', 9)
    DemoTimer(120)
    loopRest()
    ExitState()
    label(390)
    sprite('jb601_00', 7)
    uponSendToLabel(32, 391)
    sprite('jb601_00', 32767)
    loopRest()
    label(391)
    sprite('keep', 1)
    Voiceline('jb558')
    sprite('jb601_00', 180)
    sprite('jb601_03', 9)
    sprite('jb601_04', 9)
    DemoTimer(120)
    loopRest()
    ExitState()
    label(420)
    sprite('jb603_00', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(420)
    sprite('jb603_00', 8)
    sprite('jb603_00', 180)
    Voiceline('jb564')
    sprite('jb603_01', 8)
    sprite('jb603_02', 8)
    sprite('jb603_03', 8)
    CommonSE('010_swing_sword_1')
    sprite('jb603_04', 8)
    sprite('jb603_05', 4)
    sprite('jb603_05ex', 30)
    sprite('jb603_06', 4)
    ObjectUpon(22, 32)
    sprite('jb603_07', 8)
    sprite('jb603_08', 8)
    sprite('jb603_09', 8)
    sprite('jb603_10', 8)
    DemoEndOnVoiceEnd(1)
    DemoTimer(60)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if not SLOT_86:
        if CharacterIDCheck('tm'):
            conditionalSendToLabel(100)
        if CharacterIDCheck('su'):
            conditionalSendToLabel(100)
        if CharacterIDCheck('ph'):
            conditionalSendToLabel(100)
    sprite('jb611_00', 8)
    CreateObject('jb611_Tail', -1)
    RandomVoiceline('jb400', 100, 'jb401', 100, '', 0, '', 0)
    sprite('jb611_01', 8)
    sprite('jb611_02', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(100)
    sprite('jb300_00', 4)
    sprite('jb300_01', 4)
    sprite('jb300_02', 6)
    sprite('jb300_03', 5)
    CommonSE('024_getset_b')
    RandomVoiceline('jb400', 100, 'jb401', 100, '', 0, '', 0)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 12)
    sprite('jb300_03', 8)
    sprite('jb300_03ex', 12)
    sprite('jb300_04', 8)
    sprite('jb300_04ex', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('tk'):
        conditionalSendToLabel(140)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('vh'):
        conditionalSendToLabel(260)
    if CharacterIDCheck('pt'):
        conditionalSendToLabel(270)
    if CharacterIDCheck('kk'):
        conditionalSendToLabel(340)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ce'):
        conditionalSendToLabel(360)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    label(0)
    sprite('jb610_00', 7)
    StayAfterMovement(1, 0)
    sprite('jb610_01', 7)
    sprite('jb610_02', 7)
    sprite('jb610_03', 10)
    sprite('jb610_04', 4)
    sprite('jb610_05', 4)
    CreateObject('jb610_Slash', -1)
    PrivateSE('jbse_07')
    sprite('jb610_06', 7)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    RandomVoiceline('jb406', 100, 'jb407', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    label(1)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    loopRest()
    gotoLabel(1)
    loopRest()
    label(666)
    sprite('jb000_00', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(100)
    sprite('jb602_06', 6)
    sprite('jb602_04', 6)
    sprite('jb602_00', 6)
    sprite('jb602_03', 6)
    sprite('jb602_01', 7)
    Voiceline('jb501')
    DemoEndOnVoiceEnd(1)
    sprite('jb602_02', 10)
    sprite('jb602_01', 6)
    sprite('jb602_00', 60)
    CreateParticle('jbef_tameiki', 0)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 10)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 32767)
    ExitState()
    label(110)
    sprite('jb610_00', 7)
    StayAfterMovement(1, 0)
    sprite('jb610_01', 7)
    sprite('jb610_02', 7)
    sprite('jb610_03', 10)
    sprite('jb610_04', 4)
    sprite('jb610_05', 4)
    CreateObject('jb610_Slash', -1)
    PrivateSE('jbse_07')
    sprite('jb610_06', 7)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    Voiceline('jb503')
    DemoEndOnVoiceEnd(1)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    label(111)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    loopRest()
    gotoLabel(111)
    label(140)
    sprite('jb602_06', 6)
    sprite('jb602_04', 6)
    sprite('jb602_00', 6)
    sprite('jb602_03', 6)
    sprite('jb602_01', 7)
    sprite('jb602_02', 10)
    sprite('jb602_01', 6)
    Voiceline('jb509')
    DemoEndOnVoiceEnd(1)
    sprite('jb602_00', 60)
    CreateParticle('jbef_tameiki', 0)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 10)
    sprite('jb602_04', 10)
    sprite('jb602_05', 10)
    sprite('jb602_04', 10)
    sprite('jb602_00', 32767)
    loopRest()
    label(200)
    sprite('jb601_04', 9)
    sprite('jb601_03', 9)
    Voiceline('jb521')
    DemoEndOnVoiceEnd(1)
    label(201)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    gotoLabel(201)
    label(260)
    sprite('jb610_00', 7)
    StayAfterMovement(1, 0)
    sprite('jb610_01', 7)
    sprite('jb610_02', 7)
    sprite('jb610_03', 10)
    sprite('jb610_04', 4)
    sprite('jb610_05', 4)
    CreateObject('jb610_Slash', -1)
    PrivateSE('jbse_07')
    sprite('jb610_06', 7)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    Voiceline('jb533')
    DemoEndOnVoiceEnd(1)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    label(261)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    loopRest()
    gotoLabel(261)
    label(270)
    sprite('jb611_00', 8)
    CreateObject('jb611_Tail', -1)
    Voiceline('jb535')
    DemoEndOnVoiceEnd(1)
    sprite('jb611_01', 8)
    sprite('jb611_02', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(340)
    sprite('jb601_04', 9)
    sprite('jb601_03', 9)
    Voiceline('jb549')
    DemoEndOnVoiceEnd(1)
    label(341)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    gotoLabel(341)
    label(350)
    sprite('jb612_00', 8)
    sprite('jb612_01', 8)
    sprite('jb612_02', 8)
    sprite('jb612_03', 8)
    sprite('jb612_04', 10)
    sprite('jb612_05', 3)
    sprite('jb612_06', 3)
    CommonSE('010_swing_sword_1')
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    Voiceline('jb551')
    DemoEndOnVoiceEnd(1)
    sprite('jb612_09', 7)
    label(351)
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    loopRest()
    gotoLabel(351)
    label(360)
    sprite('jb601_04', 9)
    sprite('jb601_03', 9)
    Voiceline('jb553')
    DemoEndOnVoiceEnd(1)
    label(361)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    gotoLabel(361)
    label(390)
    sprite('jb610_00', 7)
    StayAfterMovement(1, 0)
    sprite('jb610_01', 7)
    sprite('jb610_02', 7)
    sprite('jb610_03', 10)
    sprite('jb610_04', 4)
    sprite('jb610_05', 4)
    CreateObject('jb610_Slash', -1)
    PrivateSE('jbse_07')
    sprite('jb610_06', 7)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    Voiceline('jb559')
    DemoEndOnVoiceEnd(1)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    label(391)
    sprite('jb610_07', 6)
    sprite('jb610_08', 6)
    sprite('jb610_09', 6)
    sprite('jb610_10', 6)
    loopRest()
    gotoLabel(391)
    loopRest()
    label(420)
    sprite('jb612_00', 8)
    sprite('jb612_01', 8)
    sprite('jb612_02', 8)
    sprite('jb612_03', 8)
    sprite('jb612_04', 10)
    sprite('jb612_05', 3)
    sprite('jb612_06', 3)
    CommonSE('010_swing_sword_1')
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    Voiceline('jb565')
    DemoEndOnVoiceEnd(1)
    sprite('jb612_09', 7)
    label(421)
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    loopRest()
    gotoLabel(421)


@State
def CmnActLose():
    sprite('jb620_00', 8)
    sprite('jb620_01', 8)
    Voiceline('jb410')
    sprite('jb620_02', 6)
    physicsXImpulse(-1000)
    sprite('jb620_03', 7)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('jb620_04', 7)
    sprite('jb620_05', 7)
    sprite('jb620_06', 7)
    sprite('jb620_07', 32767)
    DemoEndOnVoiceEnd(1)


@State
def EventDefEntryWait():
    label(0)
    sprite('jb000_00', 7)
    sprite('jb000_01', 7)
    sprite('jb000_02', 7)
    sprite('jb000_03', 7)
    sprite('jb000_04', 7)
    sprite('jb000_05', 7)
    sprite('jb000_06', 7)
    sprite('jb000_07', 7)
    sprite('jb000_08', 7)
    sprite('jb000_09', 7)
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
def EventDefChouhatsu():
    sprite('jb300_00', 4)
    sprite('jb300_01', 4)
    sprite('jb300_02', 4)
    sprite('jb300_03', 6)
    sprite('jb300_04', 6)
    sprite('jb300_05', 7)
    sprite('jb300_04', 6)
    sprite('jb300_05', 7)
    sprite('jb300_03', 9)
    sprite('jb300_06', 6)
    sprite('jb300_07', 6)
    sprite('jb300_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefChouhatsu2():
    sprite('jb300_00', 4)
    sprite('jb300_01', 4)
    sprite('jb300_02', 4)
    sprite('jb300_03', 6)
    sprite('jb300_04', 6)
    sprite('jb300_05', 32767)


@State
def EventDefChouhatsuEnd():
    sprite('jb300_03', 6)
    sprite('jb300_06', 6)
    sprite('jb300_07', 6)
    sprite('jb300_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)


@State
def EventYoroke():
    sprite('jb070_07', 32767)
    loopRest()


@State
def EventEntry0_WaitGazingEnemy():
    sprite('jb601_00', 32767)
    loopRest()


@State
def EventEntry0_PrepareForBattle():
    sprite('rg601_00', 6)
    sprite('rg601_01', 6)
    sprite('rg601_02', 6)
    sprite('rg601_03', 6)
    sprite('rg601_04', 6)
    sprite('rg601_05', 6)
    sprite('rg601_06', 6)
    sprite('rg601_07', 6)
    PrivateSE('rgse_05')
    sprite('rg601_08', 6)
    sprite('rg601_09', 6)
    sprite('rg601_10', 6)
    sprite('rg601_11', 4)
    sprite('rg601_12', 4)
    CommonSE('006_swing_blade_1')
    sprite('rg601_13', 4)
    sprite('rg601_14', 4)
    sprite('rg601_15', 4)
    CommonSE('006_swing_blade_1')
    sprite('rg601_16', 4)
    sprite('rg601_17', 6)
    sprite('rg601_18', 6)
    sprite('rg601_19', 3)
    sprite('rg601_20', 6)
    sprite('rg601_21', 6)
    PrivateSE('rgse_00')
    sprite('rg601_22', 6)
    sprite('rg601_23', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventWarpIn():
    AlphaValue(0)
    sprite('rg000_00', 6)
    ConstantAlphaModifier(10)
    CommonSE('001_airbackdash_0')
    sprite('keep', 20)
    CommonSE('000_airdash_2')
    sprite('keep', 1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    loopRest()
    enterState('CmnActStand')


@State
def EventWarpOut():
    sprite('keep', 6)
    ConstantAlphaModifier(-10)
    CommonSE('001_airbackdash_0')
    sprite('keep', 20)
    CommonSE('000_airdash_2')
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(0)
    loopRest()


@State
def Act3Event_Udekumi():
    label(0)
    sprite('jb601_00', 20)
    sprite('jb601_01', 9)
    sprite('jb601_02', 9)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_UdekumiEnd():
    sprite('jb601_03', 9)
    sprite('jb601_04', 9)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Think():
    sprite('jb611_00', 8)
    CreateObject('jb611_Tail_Event', -1)
    sprite('jb611_01', 8)
    sprite('jb611_02', 32767)
    loopRest()


@State
def Act3Event_ThinkEnd():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            DespawnEAEffect('jb611_Tail_Event')
    sprite('jb611_01', 8)
    sprite('jb611_00', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsrg_00():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        StayAfterMovement(1, 0)
        XPositionRelativeFacing(-320000)
    sprite('jb202_05', 3)
    DashEffects(100, 1, 0)
    physicsXImpulse(1000)
    sprite('jb202_06', 4)
    physicsXImpulse(5000)
    DashEffects(100, 1, 0)
    CommonSE('010_swing_sword_1')
    sprite('jb202_07', 11)
    EndMomentum(1)
    DashEffects(100, 1, 0)
    CreateObject('jbef202_zanzou_2nd', 100)
    sprite('jb202_08', 5)
    sprite('jb202_09', 5)
    sprite('jb202_10', 5)
    sprite('jb202_11', 5)
    sprite('jb202_12', 5)
    sprite('jb202_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Reaction():
    sprite('jb001_00', 6)
    sprite('jb001_01', 6)
    sprite('jb001_02', 6)
    sprite('jb001_03', 6)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_06', 8)
    sprite('jb001_04', 8)
    sprite('jb001_03', 9)
    sprite('jb001_02', 9)
    sprite('jb001_01', 9)
    sprite('jb001_00', 9)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Sword():
    sprite('jb612_00', 8)
    sprite('jb612_01', 8)
    sprite('jb612_02', 8)
    sprite('jb612_03', 8)
    sprite('jb612_04', 10)
    CommonSE('010_swing_sword_1')
    sprite('jb612_05', 3)
    sprite('jb612_06', 3)
    label(0)
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_SwordLoop():
    label(0)
    sprite('jb612_07', 7)
    sprite('jb612_08', 7)
    sprite('jb612_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_SwordEnd():
    sprite('jb603_08', 7)
    sprite('jb603_09', 9)
    sprite('jb603_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Tameiki():
    sprite('jb602_06', 7)
    sprite('jb602_04', 7)
    sprite('jb602_00', 10)
    sprite('jb602_01', 7)
    sprite('jb602_02', 15)
    sprite('jb602_03', 6)
    sprite('jb602_00', 32767)
    CreateParticle('jbef_tameiki', 0)
    loopRest()


@State
def Act3Event_TameikiEnd():
    sprite('jb602_04', 7)
    sprite('jb602_06', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Miageru():
    sprite('jb321_15ex00', 7)
    sprite('jb321_14ex00', 7)
    sprite('jb321_13ex00', 7)
    sprite('jb450_39', 6)
    sprite('jb450_40', 7)
    sprite('jb450_41', 32767)
    loopRest()


@State
def Act3Event_MiageruEnd():
    sprite('jb321_13ex00', 8)
    sprite('jb321_14ex00', 8)
    sprite('jb321_15ex00', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Kansyo():
    sprite('keep', 4)
    CreateObject('NOISE', -1)
    CommonSE('023_noize')
    sprite('jb040_00', 3)
    sprite('jb040_01', 3)
    label(0)
    sprite('jb040_02', 4)
    sprite('jb040_03', 4)
    sprite('jb040_04', 4)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_Udekumi2():
    sprite('jb601_00', 32767)
    loopRest()


@State
def Act3Event_UdekumiEnd():
    sprite('jb601_03', 9)
    sprite('jb601_04', 9)
    loopRest()
    enterState('CmnActStand')
