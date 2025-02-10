@Subroutine
def PreInit():
    CharacterID('ma')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(6200)
    WalkBSpeed(4800)
    DashFInitialVelocity(16000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(42000)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    ResourceGauge(3, 0, 0, 1, 3, 3, 0, 0)
    CPUJumpPriority(500)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    MoveLow()
    SkillEstimateRange(0, 300000, -150000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    SkillEstimateRange(0, 350000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2B_Input5', 0x1)
    StateCall('NmlAtk2B')
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x2000)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    AirborneOpponentPriority(4000)
    DamageStunPriority(1)
    SkillEstimateRange(-150000, 500000, 150000, 500000, 500, 10)
    Move_EndRegister()
    Move_Register('com1_2nd', 0x1)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('com1_2nd_4NOT', 0x1)
    StateCall('com1_2nd')
    Move_Input_(0x66)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('com1_3rd_ShotA', 0x1)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    MoveMaxChainRepeat(4)
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(300000, 700000, -200000, 1000000, 50, 1000)
    Move_EndRegister()
    Move_Register('com1_3rd_ShotB', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    SharedGatling('com1_3rd_ShotA')
    MoveLow()
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(300000, 700000, -200000, 1000000, 50, 1000)
    Move_EndRegister()
    Move_Register('com1_Ex3rd_ShotA', 0x1)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    SharedGatling('com1_3rd_ShotA')
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(300000, 700000, -200000, 1000000, 50, 1000)
    Move_EndRegister()
    Move_Register('com1_Ex3rd_ShotB', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    SharedGatling('com1_3rd_ShotA')
    MoveLow()
    DamageStunPriority(500)
    GuardStunPriority(2000)
    SkillEstimateRange(300000, 700000, -200000, 1000000, 50, 1000)
    Move_EndRegister()
    Move_Register('com1_3rd_3', 0x1)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 650000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com2_2nd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com3_kamae', 0x1)
    Move_Input_(INPUT_HOLD_B)
    FollowupOnly(1)
    MoveButtonHoldTime(1, 10, 20)
    SkillEstimateRange(0, 450000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com3_1', 0x1)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    MoveLow()
    SkillEstimateRange(0, 350000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('com3_1_InputC', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    StateCall('com3_1')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('com3_2', 0x1)
    Move_Input_(0x93)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    MoveMid()
    SkillEstimateRange(0, 550000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com3_2_InputC', 0x1)
    Move_Input_(0x93)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    StateCall('com3_2')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('com3_3', 0x1)
    Move_Input_(0x79)
    Move_Input_(0xa7)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 550000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('com3_3_InputC', 0x1)
    Move_Input_(0x79)
    Move_Input_(0xa7)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    StateCall('com3_3')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('com4_2nd', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 750000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com4_3rd_1', 0x1)
    Move_Input_(INPUT_PRESS_A)
    FollowupOnly(1)
    MoveMid()
    SkillEstimateRange(0, 650000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('com4_3rd_2', 0x1)
    Move_Input_(INPUT_PRESS_B)
    FollowupOnly(1)
    MoveMid()
    DamageStunPriority(1)
    SkillEstimateRange(0, 750000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('com4_3rd_3', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    Unknown15026(2, 53, 55)
    SkillEstimateRange(0, 650000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('com5_2nd', 0x1)
    Move_Input_(INPUT_PRESS_C)
    FollowupOnly(1)
    MoveLow()
    DamageStunPriority(2000)
    SkillEstimateRange(0, 700000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('FuncAtkDrive')
    OpponentAttackPriority(1)
    SkillEstimateRange(800000, 1800000, -200000, 500000, 500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5DD', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    SkillEstimateRange(0, 800000, -200000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(500)
    SkillEstimateRange(-100000, 250000, -150000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(-50000, 300000, -250000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    OpponentAttackPriority(1)
    SkillEstimateRange(-100000, 350000, -300000, 300000, 1500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    CallSkillConditions('FuncAtkDrive')
    SkillEstimateRange(800000, 1800000, -500000, 500000, 500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5DD', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    SkillEstimateRange(-500000, 800000, -500000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 230000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 230000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 250000, -200000, 200000, 1200, 50)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x3008)
    Move_Input_(0x108)
    DamageStunPriority(4000)
    GuardStunPriority(4000)
    OpponentAttackPriority(0)
    SkillEstimateRange(0, 1200000, -200000, 350000, 200, 10)
    Move_EndRegister()
    Move_Register('Assault_A_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_A_EX')
    DamageStunPriority(3000)
    GuardStunPriority(0)
    SkillEstimateRange(400000, 700000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_A_EX_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(0x108)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Assault_A_EX')
    DamageStunPriority(3000)
    GuardStunPriority(0)
    SkillEstimateRange(400000, 700000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_A')
    DamageStunPriority(10000)
    SkillEstimateRange(400000, 700000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_A_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Assault_A')
    DamageStunPriority(10000)
    GuardStunPriority(0)
    SkillEstimateRange(400000, 700000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_B_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_B_EX')
    DamageStunPriority(3000)
    GuardStunPriority(0)
    SkillEstimateRange(900000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('Assault_B_EX_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(0x108)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Assault_B_EX')
    DamageStunPriority(3000)
    GuardStunPriority(0)
    SkillEstimateRange(900000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_B')
    DamageStunPriority(10000)
    GuardStunPriority(0)
    SkillEstimateRange(900000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('Assault_B_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Assault_B')
    DamageStunPriority(10000)
    GuardStunPriority(0)
    SkillEstimateRange(900000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('Assault_C_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_C_EX')
    GuardStunPriority(0)
    DamageStunPriority(3000)
    SkillEstimateRange(150000, 800000, 300000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_C_EX_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(0x108)
    Move_Input_(INPUT_PRESS_C)
    CallFunction('Func_Assault_C_EX')
    GuardStunPriority(0)
    DamageStunPriority(3000)
    SkillEstimateRange(150000, 800000, 300000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_C', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    FollowupOnly(1)
    CallFunction('Func_Assault_C')
    GuardStunPriority(0)
    DamageStunPriority(10000)
    SkillEstimateRange(150000, 800000, 300000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_C_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    CallFunction('Func_Assault_C')
    GuardStunPriority(0)
    DamageStunPriority(10000)
    SkillEstimateRange(150000, 800000, 300000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('Backflip', INPUT_SPECIALMOVE)
    Move_Condition(0x3008)
    Move_Input_(0x109)
    CallSkillConditions('Check_Backflip')
    AirborneOpponentPriority(2000)
    DamageStunPriority(2000)
    GuardStunPriority(4000)
    SkillEstimateRange(-50000, 450000, -500000, 500000, 250, 10)
    Move_EndRegister()
    Move_Register('Backflip_A_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x81)
    FollowupOnly(1)
    GuardStunPriority(10000)
    SkillEstimateRange(-200000, 200000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_A', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x81)
    FollowupOnly(1)
    CallFunction('Func_Backflip_A')
    SkillEstimateRange(-200000, 200000, -1000000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_A_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Backflip_A')
    SkillEstimateRange(-200000, 200000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_B_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x81)
    FollowupOnly(1)
    GuardStunPriority(10000)
    SkillEstimateRange(150000, 550000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_B', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x81)
    FollowupOnly(1)
    CallFunction('Func_Backflip_B')
    SkillEstimateRange(0, 550000, -1000000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_B_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Backflip_B')
    SkillEstimateRange(0, 550000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_C_EX', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x81)
    FollowupOnly(1)
    GuardStunPriority(10000)
    SkillEstimateRange(300000, 1000000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_C', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x81)
    FollowupOnly(1)
    CallFunction('Func_Backflip_C')
    DamageStunPriority(10000)
    SkillEstimateRange(300000, 1000000, -1000000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_C_nama', INPUT_SPECIALMOVE)
    AddChain(1)
    Move_Condition(0x3050)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    CallFunction('Func_Backflip_C')
    DamageStunPriority(20000)
    SkillEstimateRange(300000, 1000000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateJump', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateJump_nama', INPUT_DISTORTION)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CallFunction('Func_Assault_D')
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateJumpOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateJumpOD_nama', INPUT_DISTORTION)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    CallFunction('Func_Assault_D_OD')
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(6000)
    SkillEstimateRange(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_nama', INPUT_DISTORTION)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CallFunction('Func_Backflip_D')
    OpponentAttackPriority(6000)
    SkillEstimateRange(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(6000)
    SkillEstimateRange(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD_nama', INPUT_DISTORTION)
    AddChain(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    CallFunction('Func_Backflip_D_OD')
    OpponentAttackPriority(6000)
    SkillEstimateRange(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_222)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(8000)
    SkillEstimateRange(0, 450000, -200000, 200000, 250, 0)
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
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk2C', 'FHighJump', 10000000)
    TempPriorityMultiplier('com1_Ex3rd_ShotA', 'Assault', 10000000)
    TempPriorityMultiplier('com1_Ex3rd_ShotB', 'Assault', 10000000)
    TempPriorityMultiplier('com1_3rd_3', 'Assault', 10000000)
    TempPriorityMultiplier('com4_3rd_1', 'Assault', 10000000)
    TempPriorityMultiplier('com4_3rd_3', 'Assault', 10000000)
    TempPriorityMultiplier('com5_2nd', 'Assault', 10000000)
    TempPriorityMultiplier('com5_2nd', 'UltimateAssault', 10000000)
    TempPriorityMultiplier('com5_2nd', 'UltimateAssaultOD', 10000000)
    TempPriorityMultiplier('Assault_C', 'Backflip', 10000000)
    TempPriorityMultiplier('Assault_C_nama', 'Backflip', 10000000)
    TempPriorityMultiplier('Assault_C_EX', 'Backflip', 10000000)
    TempPriorityMultiplier('Assault_C_EX_nama', 'Backflip', 10000000)
    StylishModeSpecialButton('Backflip', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0xea)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('Backflip', 0x4, 0x45)
    StylishModeCancels('NmlAtk5A', 'com1_2nd_4NOT', 0, 0)
    StylishModeCancels('NmlAtk5B', 'com4_2nd', 0, 0)
    StylishModeCancels('NmlAtk5B', 'com2_2nd', 1, 300000)
    StylishModeCancels('NmlAtk5C', 'com4_2nd', 0, 0)
    StylishModeCancels('NmlAtk5D', 'AN_NmlAtk5DD', 0, 0)
    StylishModeCancels('AN_NmlAtk5DD', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk2A', 'com5_2nd', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 1, 300000)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5A', 3, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2A', 13, 0)
    StylishModeCancels('NmlAtk2B', 'com5_2nd', 0, 0)
    StylishModeCancels('NmlAtk2B', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 0, 0)
    StylishModeCancels('NmlAtk2C', 'VJump', 1, 150000)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 13, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('NmlAtkAIR5C', 'Backflip', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5D', 'AN_NmlAtkAIR5DD', 0, 0)
    StylishModeCancels('AN_NmlAtkAIR5DD', 'Backflip', 0, 0)
    StylishModeCancels('com1_2nd', 'com1_3rd_ShotA', 0, 0)
    StylishModeCancels('com1_2nd', 'com1_3rd_3', 1, 600000)
    StylishModeCancels('com1_2nd', 'FJump', 12, 0)
    StylishModeCancels('com1_3rd_3', 'Assault', 0, 0)
    StylishModeCancels('com1_3rd_3', 'UltimateAssault', 6, 0)
    StylishModeCancels('com1_3rd_3', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('com1_3rd_3', 'AstralHeat', 6, 0)
    StylishModeCancels('com2_2nd', 'Assault', 0, 0)
    StylishModeCancels('com2_2nd', 'UltimateAssault', 6, 0)
    StylishModeCancels('com2_2nd', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('com2_2nd', 'UltimateJump', 10, 200000)
    StylishModeCancels('com2_2nd', 'UltimateJumpOD', 10, 200000)
    StylishModeCancels('com4_2nd', 'com4_3rd_2', 0, 0)
    StylishModeCancels('com4_2nd', 'com4_3rd_3', 6, 0)
    StylishModeCancels('com4_2nd', 'com4_3rd_1', 13, 0)
    StylishModeCancels('com4_3rd_1', 'UltimateAssault', 6, 0)
    StylishModeCancels('com4_3rd_1', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('com5_2nd', 'Assault', 0, 0)
    StylishModeCancels('com5_2nd', 'UltimateAssault', 6, 0)
    StylishModeCancels('com5_2nd', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('com5_2nd', 'UltimateJump', 10, 200000)
    StylishModeCancels('com5_2nd', 'UltimateJumpOD', 10, 200000)
    StylishModeCancels('Assault_C', 'Backflip', 0, 0)
    StylishModeCancels('Assault_C_EX', 'Backflip', 0, 0)
    StylishModeCancels('Assault', 'Assault_A', 0, 0)
    HitSprites(0, 'ma062_01')
    HitSprites(1, 'ma062_03')
    HitSprites(2, 'ma062_04')
    HitSprites(3, 'ma062_05')
    HitSprites(4, 'ma062_05')
    HitSprites(5, 'ma062_06')
    HitSprites(6, 'ma062_07')
    HitSprites(7, 'ma041_02')
    HitSprites(8, 'ma040_02')
    HitSprites(9, 'ma045_02')
    HitSprites(10, 'ma060_00')
    HitSprites(11, 'ma060_01')
    HitSprites(12, 'ma060_03')
    HitSprites(13, 'ma060_05')
    HitSprites(14, 'ma060_07')
    HitSprites(15, 'ma060_14')
    HitSprites(16, 'ma050_00')
    HitSprites(17, 'ma052_00')
    HitSprites(18, 'ma054_00')
    HitSprites(19, 'ma000_00')
    HitSprites(20, 'ma000_00')
    HitSprites(25, 'ma063_00')
    HitSprites(26, 'ma063_01')
    HitSprites(27, 'ma063_02')
    HitSprites(28, 'ma063_04')
    HitSprites(29, 'ma063_10')
    HitSprites(30, 'ma077_00')
    HitSprites(31, 'ma077_01')
    HitSprites(32, 'ma077_00ex01')
    HitSprites(33, 'ma077_01ex01')
    HitSprites(34, 'ma077_00ex02')
    HitSprites(35, 'ma077_01ex02')
    HitSprites(36, 'ma077_00ex03')
    HitSprites(37, 'ma077_01ex03')
    HitSprites(24, 'ma073_01')
    CommonVoicelines(0, 'ma000')
    CommonVoicelines(1, 'ma001')
    CommonVoicelines(2, 'ma002')
    CommonVoicelines(3, 'ma003')
    CommonVoicelines(4, 'ma004')
    CommonVoicelines(5, 'ma005')
    CommonVoicelines(6, 'ma006')
    CommonVoicelines(7, 'ma007')
    CommonVoicelines(8, 'ma008')
    CommonVoicelines(9, 'ma009')
    CommonVoicelines(10, 'ma010')
    CommonVoicelines(11, 'ma011')
    CommonVoicelines(12, 'ma012')
    CommonVoicelines(13, 'ma013')
    CommonVoicelines(14, 'ma014')
    CommonVoicelines(15, 'ma015')
    CommonVoicelines(16, 'ma016')
    CommonVoicelines(17, 'ma017')
    CommonVoicelines(18, 'ma018')
    CommonVoicelines(19, 'ma019')
    CommonVoicelines(20, 'ma020')
    CommonVoicelines(21, 'ma021')
    CommonVoicelines(22, 'ma022')
    CommonVoicelines(23, 'ma023')
    CommonVoicelines(24, 'ma024')
    CommonVoicelines(25, 'ma025')
    CommonVoicelines(26, 'ma026')
    CommonVoicelines(27, 'ma027')
    CommonVoicelines(28, 'ma028')
    CommonVoicelines(29, 'ma029')
    CommonVoicelines(30, 'ma030')
    CommonVoicelines(31, 'ma031')
    CommonVoicelines(32, 'ma032')
    CommonVoicelines(33, 'ma033')
    CommonVoicelines(34, 'ma034')
    CommonVoicelines(35, 'ma035')
    CommonVoicelines(36, 'ma036')
    CommonVoicelines(37, 'ma037')
    CommonVoicelines(38, 'ma038')
    CommonVoicelines(39, 'ma039')
    CommonVoicelines(40, 'ma040')
    CommonVoicelines(41, 'ma041')
    CommonVoicelines(42, 'ma042')
    CommonVoicelines(43, 'ma043')
    CommonVoicelines(44, 'ma044')
    CommonVoicelines(45, 'ma045')
    CommonVoicelines(46, 'ma046')
    CommonVoicelines(47, 'ma047')
    CommonVoicelines(48, 'ma048')
    CommonVoicelines(49, 'ma049')
    CommonVoicelines(50, 'ma050')
    CommonVoicelines(51, 'ma051')
    CommonVoicelines(52, 'ma052')
    CommonVoicelines(53, 'ma053')
    CommonVoicelines(54, 'ma100')
    CommonVoicelines(55, 'ma101')
    CommonVoicelines(56, 'ma102')
    CommonVoicelines(57, 'ma103')
    CommonVoicelines(58, 'ma104')
    CommonVoicelines(59, 'ma105')
    CommonVoicelines(60, 'ma106')
    CommonVoicelines(61, 'ma107')
    CommonVoicelines(62, 'ma108')
    CommonVoicelines(63, 'ma109')
    CommonVoicelines(64, 'ma150')
    CommonVoicelines(65, 'ma151')
    CommonVoicelines(66, 'ma152')
    CommonVoicelines(67, 'ma153')
    CommonVoicelines(68, 'ma154')
    CommonVoicelines(69, 'ma155')
    CommonVoicelines(70, 'ma156')
    CommonVoicelines(71, 'ma157')
    CommonVoicelines(72, 'ma158')
    CommonVoicelines(75, 'ma160')
    CommonVoicelines(73, 'ma402')
    CommonVoicelines(74, 'ma403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def MatchInit2():
    pass


@Subroutine
def FuncAtkDrive():
    SLOT_47 = 0
    if CheckInput(0x1d):
        if CheckInput(0x93):
            SLOT_64 = 1
            SLOT_47 = SLOT_0
        elif CheckInput(0x45):
            SLOT_64 = 2
            SLOT_47 = SLOT_0
        else:
            SLOT_64 = 0
            SLOT_47 = 1
    if SLOT_113:
        SLOT_47 = 1


@Subroutine
def FuncSpeciaInput():
    BeginBuffer('Assault')
    BeginBuffer('Assault_A_EX_nama')
    BeginBuffer('Assault_B_EX_nama')
    BeginBuffer('Assault_C_EX_nama')
    BeginBuffer('Backflip')
    BeginBuffer('UltimateJump')
    BeginBuffer('UltimateJumpOD')
    BeginBuffer('UltimateAssault')
    BeginBuffer('UltimateAssaultOD')
    BeginBuffer('AstralHeat')
    BeginBuffer('BurstDD')
    BeginBuffer('NmlAtkGuardCrush')


@Subroutine
def FuncSpeciaTiming():
    BufferedOrPressedGoto('Assault')
    BufferedOrPressedGoto('Assault_A_EX_nama')
    BufferedOrPressedGoto('Assault_B_EX_nama')
    BufferedOrPressedGoto('Assault_C_EX_nama')
    BufferedOrPressedGoto('Backflip')
    BufferedOrPressedGoto('UltimateJump')
    BufferedOrPressedGoto('UltimateJumpOD')
    BufferedOrPressedGoto('UltimateAssault')
    BufferedOrPressedGoto('UltimateAssaultOD')
    BufferedOrPressedGoto('AstralHeat')
    BufferedOrPressedGoto('BurstDD')
    BufferedOrPressedGoto('NmlAtkGuardCrush')


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_21:
            if SLOT_4:
                SLOT_4 = SLOT_4 + -1
                if SLOT_4 <= 0:
                    SLOT_4 = 0


@Subroutine
def OnLanding():
    SLOT_34 = 3


@Subroutine
def OnDamage():
    if SLOT_IsGrounded:
        SLOT_34 = 3


@Subroutine
def OnActionBegin():
    if not CurrentStateCheck('Assault'):
        if not CurrentStateCheck('Backflip'):
            SLOT_60 = 0
            SLOT_61 = 0


@Subroutine
def Check_Backflip():
    SLOT_47 = 0
    if SLOT_34 > 1:
        SLOT_47 = 1


@Subroutine
def Func_Assault_A():
    if not SLOT_60 == 11:
        SLOT_60 = 1


@Subroutine
def Func_Assault_B():
    if not SLOT_60 == 12:
        SLOT_60 = 2


@Subroutine
def Func_Assault_C():
    if not SLOT_60 == 13:
        SLOT_60 = 3


@Subroutine
def Func_Assault_A_EX():
    SLOT_60 = 11


@Subroutine
def Func_Assault_B_EX():
    SLOT_60 = 12


@Subroutine
def Func_Assault_C_EX():
    SLOT_60 = 13


@Subroutine
def Func_Backflip_A():
    if not SLOT_60 == 11:
        SLOT_60 = 1


@Subroutine
def Func_Backflip_B():
    if not SLOT_60 == 12:
        SLOT_60 = 2


@Subroutine
def Func_Backflip_C():
    if not SLOT_60 == 13:
        SLOT_60 = 3


@Subroutine
def Func_Assault_D():
    if not SLOT_60 == 21:
        SLOT_60 = 20


@Subroutine
def Func_Assault_D_OD():
    SLOT_60 = 21


@Subroutine
def Func_Backflip_D():
    if not SLOT_60 == 31:
        SLOT_60 = 30


@Subroutine
def Func_Backflip_D_OD():
    SLOT_60 = 31


@State
def CmnActStand():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
    label(0)
    sprite('ma000_00', 7)
    if SLOT_6:
        if PreviousStateCheck('NmlAtk5D'):
            CreateObject('maef_catch', 0)

            def RunOnObject_1():
                RotationAngle(-225000)
        if PreviousStateCheck('AN_NmlAtk5DD'):
            CreateObject('maef_catch', 0)

            def RunOnObject_1():
                RotationAngle(-225000)
    sprite('ma000_01', 7)
    sprite('ma000_02', 7)
    sprite('ma000_03', 7)
    sprite('ma000_04', 7)
    sprite('ma000_05', 7)
    sprite('ma000_06', 7)
    sprite('ma000_07', 7)
    sprite('ma000_08', 7)
    sprite('ma000_09', 7)
    sprite('ma000_10', 7)
    sprite('ma000_11', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(0, 2, 123):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('ma001_00', 7)
    SLOT_88 = 960
    Voiceline('ma000')
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('ma003_00', 3)
    sprite('ma003_01', 3)
    sprite('ma003_00ex01', 3)


@State
def CmnActStand2Crouch():
    sprite('ma010_00', 4)
    sprite('ma010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('ma010_02', 6)
    sprite('ma010_03', 6)
    sprite('ma010_04', 6)
    sprite('ma010_05', 6)
    sprite('ma010_06', 6)
    sprite('ma010_07', 6)
    sprite('ma010_08', 6)
    sprite('ma010_09', 6)
    sprite('ma010_10', 6)
    sprite('ma010_11', 6)
    sprite('ma010_12', 6)
    sprite('ma010_13', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('ma013_00', 3)
    sprite('ma013_01', 3)
    sprite('ma013_00ex01', 3)


@State
def CmnActCrouch2Stand():
    sprite('ma010_01', 4)
    sprite('ma010_00', 4)


@State
def CmnActJumpPre():
    sprite('ma023_00', 2)
    sprite('ma023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('ma020_00', 4)
    sprite('ma020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('ma020_02', 3)
    sprite('ma020_03', 3)
    sprite('ma020_04', 3)


@State
def CmnActJumpDown():
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(0)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('ma024_00', 3)
    sprite('ma024_01', 3)
    sprite('ma024_02', 3)
    sprite('ma024_03', 3)
    sprite('ma024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('ma024_00', 2)
    sprite('ma024_01', 2)
    sprite('ma024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('ma024_03', 3)
    sprite('ma024_04', 3)


@State
def CmnActFWalk():
    sprite('ma030_00', 7)
    label(0)
    sprite('ma030_01', 7)
    sprite('ma030_02', 7)
    sprite('ma030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_04', 7)
    sprite('ma030_05', 7)
    sprite('ma030_06', 7)
    sprite('ma030_07', 7)
    sprite('ma030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_09', 7)
    sprite('ma030_10', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('ma031_00', 7)
    label(0)
    sprite('ma031_01', 7)
    sprite('ma031_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma031_03', 7)
    sprite('ma031_04', 7)
    sprite('ma031_05', 7)
    sprite('ma031_06', 7)
    sprite('ma031_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma031_08', 7)
    sprite('ma031_09', 7)
    sprite('ma031_10', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('ma032_00', 2)
    label(0)
    sprite('ma032_01', 4)
    sprite('ma032_02', 3)
    sprite('ma032_03', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_04', 3)
    sprite('ma032_05', 3)
    sprite('ma032_06', 4)
    sprite('ma032_07', 3)
    sprite('ma032_08', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_09', 3)
    sprite('ma032_10', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('ma032_11', 4)
    sprite('ma032_12', 4)
    sprite('ma032_13', 4)
    sprite('ma032_14', 4)
    sprite('ma032_15', 4)


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
    sprite('ma033_00', 2)
    sprite('ma033_01', 3)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    Voiceline('ma005')
    sprite('ma033_02', 2)
    sprite('ma033_02', 1)
    setInvincible(0)
    loopRest()
    label(0)
    sprite('ma033_01', 3)
    sprite('ma033_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma033_03', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('ma033_04', 2)
    sprite('ma033_05', 2)
    sprite('ma033_06', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('ma035_00', 3)
    label(0)
    sprite('ma035_01', 3)
    sprite('ma035_02', 3)
    sprite('ma035_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('ma036_00', 3)
    label(0)
    sprite('ma036_01', 3)
    sprite('ma036_02', 3)
    sprite('ma036_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('ma050_00', 1)
    sprite('ma050_01', 1)
    sprite('ma050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('ma050_01', 1)
    sprite('ma050_02', 1)
    sprite('ma050_01', 2)
    sprite('ma050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('ma050_02', 1)
    sprite('ma050_03', 1)
    sprite('ma050_02', 2)
    sprite('ma050_01', 2)
    sprite('ma050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('ma050_03', 1)
    sprite('ma050_04', 1)
    sprite('ma050_03', 2)
    sprite('ma050_02', 2)
    sprite('ma050_01', 2)
    sprite('ma050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('ma050_04', 1)
    sprite('ma050_04', 1)
    sprite('ma050_04', 2)
    sprite('ma050_03', 2)
    sprite('ma050_02', 2)
    sprite('ma050_01', 2)
    sprite('ma050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('ma052_00', 1)
    sprite('ma052_01', 1)
    sprite('ma052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('ma052_01', 1)
    sprite('ma052_02', 1)
    sprite('ma052_01', 2)
    sprite('ma052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('ma052_02', 1)
    sprite('ma052_03', 1)
    sprite('ma052_02', 2)
    sprite('ma052_01', 2)
    sprite('ma052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('ma052_03', 1)
    sprite('ma052_04', 1)
    sprite('ma052_03', 2)
    sprite('ma052_02', 2)
    sprite('ma052_01', 2)
    sprite('ma052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('ma052_04', 1)
    sprite('ma052_04', 1)
    sprite('ma052_04', 2)
    sprite('ma052_03', 2)
    sprite('ma052_02', 2)
    sprite('ma052_01', 2)
    sprite('ma052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('ma054_00', 1)
    sprite('ma054_01', 1)
    sprite('ma054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('ma054_01', 1)
    sprite('ma054_02', 1)
    sprite('ma054_01', 2)
    sprite('ma054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('ma054_02', 1)
    sprite('ma054_03', 1)
    sprite('ma054_02', 2)
    sprite('ma054_01', 2)
    sprite('ma054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('ma054_03', 1)
    sprite('ma054_04', 1)
    sprite('ma054_03', 2)
    sprite('ma054_02', 2)
    sprite('ma054_01', 2)
    sprite('ma054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('ma054_04', 1)
    sprite('ma054_04', 1)
    sprite('ma054_04', 2)
    sprite('ma054_03', 2)
    sprite('ma054_02', 2)
    sprite('ma054_01', 2)
    sprite('ma054_00', 2)


@State
def CmnActBDownUpper():
    sprite('ma060_00', 4)
    label(0)
    sprite('ma060_01', 4)
    sprite('ma060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('ma060_03', 4)


@State
def CmnActBDownDown():
    sprite('ma060_04', 4)
    label(0)
    sprite('ma060_05', 4)
    sprite('ma060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('ma060_07', 2)
    sprite('ma060_08', 2)


@State
def CmnActBDownBound():
    sprite('ma060_09', 3)
    sprite('ma060_10', 3)
    sprite('ma060_11', 3)
    sprite('ma060_12', 3)
    sprite('ma060_13', 3)


@State
def CmnActBDownLoop():
    sprite('ma060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('ma061_00', 4)
    sprite('ma061_01', 3)
    sprite('ma061_02', 3)
    sprite('ma061_03', 3)
    sprite('ma061_04', 3)
    sprite('ma061_05', 3)
    sprite('ma061_06', 3)
    sprite('ma061_07', 3)
    sprite('ma061_08', 3)


@State
def CmnActFDownUpper():
    sprite('ma063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('ma063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('ma063_02', 3)
    sprite('ma063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('ma063_04', 3)
    sprite('ma063_05', 3)


@State
def CmnActFDownBound():
    sprite('ma063_06', 2)
    sprite('ma063_07', 2)
    sprite('ma063_08', 3)
    sprite('ma063_09', 3)
    sprite('ma063_10', 3)


@State
def CmnActFDownLoop():
    sprite('ma063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('ma064_00', 3)
    sprite('ma064_01', 3)
    sprite('ma064_02', 3)
    sprite('ma064_03', 3)
    sprite('ma064_04', 3)
    sprite('ma064_05', 3)
    sprite('ma064_06', 3)
    sprite('ma064_07', 3)
    sprite('ma064_08', 3)


@State
def CmnActVDownUpper():
    sprite('ma062_00', 3)
    label(0)
    sprite('ma062_01', 3)
    sprite('ma062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('ma062_03', 3)
    sprite('ma062_04', 3)


@State
def CmnActVDownDown():
    sprite('ma062_05', 3)
    sprite('ma062_06', 3)
    label(0)
    sprite('ma062_07', 3)
    sprite('ma062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('ma062_09', 2)
    sprite('ma062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('ma062_09', 2)
    sprite('ma062_10', 2)


@State
def CmnActBlowoff():
    sprite('ma072_00', 3)
    sprite('ma072_01', 3)
    sprite('ma072_02', 3)
    label(0)
    sprite('ma072_01', 3)
    sprite('ma072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ma074_00', 3)
    sprite('ma074_01', 3)
    sprite('ma074_02', 3)
    sprite('ma074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('ma082_00', 2)
    sprite('ma082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('ma071_04', 1)


@State
def CmnActWallBound():
    sprite('ma073_00', 3)
    sprite('ma073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('ma073_02', 3)
    label(0)
    sprite('ma073_03', 3)
    sprite('ma073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('ma070_00', 2)
    sprite('ma070_01', 2)
    label(0)
    sprite('ma070_02', 5)
    sprite('ma070_03', 5)
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('ma070_04', 4)
    sprite('ma070_05', 4)
    sprite('ma070_06', 4)
    sprite('ma070_07', 4)
    sprite('ma070_08', 4)
    sprite('ma070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('ma070_10', 2)
    sprite('ma070_11', 2)
    sprite('ma070_12', 2)
    sprite('ma070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('ma113_00', 3)
    sprite('ma113_01', 3)
    sprite('ma113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('ma113_00', 3)
    sprite('ma113_01', 3)
    sprite('ma113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('ma113_00', 3)
    sprite('ma113_01', 3)
    sprite('ma113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('ma110_00', 2)
    sprite('ma110_01', 2)
    sprite('ma110_02', 2)
    sprite('ma110_03', 2)
    sprite('ma110_04', 2)
    sprite('ma110_05', 2)
    sprite('ma110_06', 2)
    sprite('ma110_07', 2)
    sprite('ma110_08', 200)
    sprite('ma110_09', 3)
    sprite('ma110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('ma111_00', 2)
    sprite('ma111_01', 2)
    sprite('ma111_02', 2)
    sprite('ma111_03', 2)
    sprite('ma111_04', 2)
    sprite('ma111_05', 2)
    sprite('ma111_06', 2)
    sprite('ma111_07', 2)
    sprite('ma111_08', 200)
    sprite('ma111_09', 3)
    sprite('ma111_10', 3)


@State
def CmnActUkemiLandN():
    sprite('ma112_00', 2)
    sprite('ma112_01', 2)
    sprite('ma112_02', 2)
    sprite('ma112_03', 2)
    sprite('ma112_04', 2)
    sprite('ma112_05', 2)
    sprite('ma112_06', 2)
    sprite('ma112_07', 2)
    sprite('ma112_08', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('ma024_00', 3)
    sprite('ma024_01', 3)
    sprite('ma024_02', 3)
    sprite('ma024_03', 3)
    sprite('ma024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('ma040_00', 3)
    sprite('ma040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ma040_02', 4)
    sprite('ma040_03', 4)
    sprite('ma040_04', 4)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('ma040_01', 3)
    sprite('ma040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('ma040_05', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('ma040_01', 3)
    sprite('ma040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('ma041_00', 3)
    sprite('ma041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ma041_02', 4)
    sprite('ma041_03', 4)
    sprite('ma041_04', 4)
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('ma041_01', 3)
    sprite('ma041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('ma041_05', 3)


@State
def CmnActHighHeavyGuardEnd():
    sprite('ma041_01', 3)
    sprite('ma041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('ma043_00', 3)
    sprite('ma043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ma043_02', 4)
    sprite('ma043_03', 4)
    sprite('ma043_04', 4)
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('ma043_01', 3)
    sprite('ma043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ma043_05', 3)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ma043_01', 3)
    sprite('ma043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('ma045_00', 3)
    sprite('ma045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ma045_02', 4)
    sprite('ma045_03', 4)
    sprite('ma045_04', 4)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('ma045_01', 3)
    sprite('ma045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('ma045_05', 3)


@State
def CmnActAirHeavyGuardEnd():
    sprite('ma045_01', 3)
    sprite('ma045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('ma090_00', 2)
    sprite('ma090_01', 2)
    sprite('ma090_02', 1)
    SetCommonActionMark(1)
    sprite('ma090_03', 6)
    sprite('ma090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('ma091_00', 2)
    sprite('ma091_01', 2)
    sprite('ma091_02', 1)
    SetCommonActionMark(1)
    sprite('ma091_03', 6)
    sprite('ma091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('ma092_00', 2)
    sprite('ma092_01', 2)
    sprite('ma092_02', 1)
    SetCommonActionMark(1)
    sprite('ma092_03', 6)
    sprite('ma092_04', 6)


@State
def CmnActAirTurn():
    sprite('ma025_00', 4)
    sprite('ma025_01', 4)
    sprite('ma025_00ex01', 4)


@State
def CmnActLockWait():
    sprite('ma040_02', 1)
    sprite('ma040_01', 3)
    sprite('ma040_00', 3)


@State
def CmnActLockReject():
    sprite('ma312_00', 3)
    sprite('ma312_01', 3)
    sprite('ma312_02', 3)
    sprite('ma312_03', 6)
    sprite('ma312_04', 5)
    sprite('ma312_05', 3)
    sprite('ma312_06', 3)
    sprite('ma312_07', 3)


@State
def CmnActAirLockWait():
    sprite('ma045_02', 1)
    sprite('ma045_01', 3)
    sprite('ma045_00', 3)


@State
def CmnActAirLockReject():
    sprite('ma322_00', 3)
    sprite('ma322_01', 3)
    sprite('ma322_02', 3)
    sprite('ma322_03', 6)
    sprite('ma322_04', 6)
    sprite('ma322_05', 4)
    sprite('ma322_06', 4)


@State
def CmnActLandSpin():
    sprite('ma071_00', 4)
    sprite('ma071_01', 4)
    label(0)
    sprite('ma071_02', 2)
    sprite('ma071_03', 2)
    sprite('ma071_04', 2)
    sprite('ma071_05', 2)
    sprite('ma071_06', 2)
    sprite('ma071_07', 2)
    sprite('ma071_08', 2)
    sprite('ma071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('ma071_10', 6)
    sprite('ma071_11', 5)
    sprite('ma071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('ma071_02', 2)
    sprite('ma071_03', 2)
    sprite('ma071_04', 2)
    sprite('ma071_05', 2)
    sprite('ma071_06', 2)
    sprite('ma071_07', 2)
    sprite('ma071_08', 2)
    sprite('ma071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('ma077_00', 2)
    sprite('ma077_01', 2)
    sprite('ma077_00ex01', 2)
    sprite('ma077_01ex01', 2)
    sprite('ma077_00ex02', 2)
    sprite('ma077_01ex02', 2)
    sprite('ma077_00ex03', 2)
    sprite('ma077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('ma077_02', 4)
    label(0)
    sprite('ma077_03', 3)
    sprite('ma077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('ma077_05', 5)
    sprite('ma077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ma060_07', 3)
    sprite('ma060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('ma060_11', 4)
    sprite('ma060_13', 5)


@State
def CmnActBurstBegin():
    sprite('ma331_00', 2)
    sprite('ma331_01', 2)
    label(0)
    sprite('ma331_02', 3)
    sprite('ma331_03', 3)
    sprite('ma331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('ma331_05', 2)
    label(0)
    sprite('ma331_06', 3)
    sprite('ma331_07', 3)
    sprite('ma331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('ma331_09', 3)
    sprite('ma331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('ma331_11', 2)
    sprite('ma331_12', 2)
    label(0)
    sprite('ma331_02', 3)
    sprite('ma331_03', 3)
    sprite('ma331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('ma331_05', 2)
    label(0)
    sprite('ma331_06', 3)
    sprite('ma331_07', 3)
    sprite('ma331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('ma331_13', 4)
    sprite('ma331_14', 4)
    sprite('ma020_06', 4)
    label(0)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('ma333_00', 3)
    sprite('ma333_01', 3)
    sprite('ma333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ma333_03', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('ma333_04', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)
    sprite('ma333_06', 3)
    sprite('ma333_07', 3)
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('ma333_08', 6)
    sprite('ma333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('ma333_10', 3)
    sprite('ma333_11', 3)
    sprite('ma333_12', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ma333_13', 32767)
    CreateObject('EMB_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('ma333_14', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)
    sprite('ma333_06', 3)
    sprite('ma333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('ma333_15', 6)
    sprite('ma333_16', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AttackP2(85)
        PushbackX(12000)
        AirUntechableTime(14)
        Hitstun(14)
        AirPushbackY(16000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com1_2nd_4NOT')
                HitOrBlockCancel('com2_2nd')
                HitOrBlockCancel('com4_2nd')
                DisallowGoto('com1_2nd_4NOT')
                DisallowGoto('com2_2nd')
                DisallowGoto('com4_2nd')
            else:
                BufferedOrPressedGoto('com1_2nd_4NOT')
                BufferedOrPressedGoto('com2_2nd')
                BufferedOrPressedGoto('com4_2nd')
            SLOT_61 = 1
    if PreviousStateCheck('NmlAtk5A'):
        conditionalSendToLabel(1)
    sprite('ma200_00', 1)
    PerInertia(60)
    sprite('ma200_01', 2)
    CommonSE('004_swing_grap_1_0')
    gotoLabel(9)
    label(1)
    sprite('ma200_01', 3)
    PerInertia(60)
    CommonSE('004_swing_grap_1_0')
    label(9)
    sprite('ma200_02', 2)
    RandomCommonVoiceline(0)
    sprite('ma200_03', 1)
    BeginBuffer('com1_2nd_4NOT')
    BeginBuffer('com2_2nd')
    BeginBuffer('com4_2nd')
    sprite('ma200_03', 2)
    BufferedOrPressedGoto('com1_2nd_4NOT')
    BufferedOrPressedGoto('com2_2nd')
    BufferedOrPressedGoto('com4_2nd')
    sprite('ma200_03', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ma200_04', 5)
    sprite('ma200_05', 3)
    WhiffCancelEnable(0)
    DisallowGoto('com1_2nd_4NOT')
    DisallowGoto('com2_2nd')
    DisallowGoto('com4_2nd')
    if SLOT_94:
        ChainCancel(0)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk5D')
        HitJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com1_2nd')
                HitOrBlockCancel('com2_2nd')
                HitOrBlockCancel('com4_2nd')
                DisallowGoto('com1_2nd')
                DisallowGoto('com2_2nd')
                DisallowGoto('com4_2nd')
            else:
                BufferedOrPressedGoto('com1_2nd')
                BufferedOrPressedGoto('com2_2nd')
                BufferedOrPressedGoto('com4_2nd')

        def upon_OPPONENT_HIT():
            SLOT_61 = 1
        StayAfterMovement(1, 0)
    sprite('ma201_00', 3)
    sprite('ma201_01', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('ma201_02', 2)
    BeginBuffer('com1_2nd')
    BeginBuffer('com2_2nd')
    BeginBuffer('com4_2nd')
    RandomCommonVoiceline(1)
    sprite('ma201_03', 4)
    sprite('ma201_04', 4)
    BufferedOrPressedGoto('com1_2nd')
    BufferedOrPressedGoto('com2_2nd')
    BufferedOrPressedGoto('com4_2nd')
    Recovery()
    Unknown2063()
    sprite('ma201_05', 3)
    DisallowGoto('com1_2nd')
    DisallowGoto('com2_2nd')
    DisallowGoto('com4_2nd')
    if SLOT_94:
        ChainCancel(0)
    sprite('ma201_06', 3)
    sprite('ma201_07', 3)
    sprite('ma201_08', 3)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(3)
        Hitstun(22)
        AirPushbackY(20000)
        FatalCounter(1)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')
        HitJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com4_2nd')
                DisallowGoto('com4_2nd')
            else:
                BufferedOrPressedGoto('com4_2nd')

        def upon_OPPONENT_HIT():
            SLOT_61 = 1
        StayAfterMovement(1, 0)
    sprite('ma202_00', 3)
    sprite('ma202_01', 3)
    RandomCommonVoiceline(2)
    CreateObject('maef_202', -1)
    sprite('ma202_02', 3)
    CommonSE('006_swing_blade_1')
    sprite('ma202_03', 3)
    sprite('ma202_04', 4)
    BeginBuffer('com4_2nd')
    CreateObject('maef_202_2', -1)
    sprite('ma202_05', 1)
    Recovery()
    Unknown2063()
    sprite('ma202_05', 2)
    BufferedOrPressedGoto('com4_2nd')
    sprite('ma202_06', 3)
    sprite('ma202_07', 3)
    sprite('ma202_08', 3)
    DisallowGoto('com4_2nd')
    if SLOT_94:
        ChainCancel(0)
    sprite('ma202_09', 2)
    sprite('ma202_10', 2)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(85)
        PushbackX(12000)
        AirUntechableTime(14)
        Hitstun(14)
        AirPushbackY(16000)
        HitLow(2)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('Atk2B_Input5')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com5_2nd')
            else:
                BufferedOrPressedGoto('com5_2nd')
    if PreviousStateCheck('NmlAtk2A'):
        conditionalSendToLabel(1)
    sprite('ma230_00', 2)
    PerInertia(60)
    sprite('ma230_01', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('ma230_02', 2)
    gotoLabel(9)
    label(1)
    sprite('ma230_01', 3)
    PerInertia(60)
    CommonSE('004_swing_grap_1_0')
    sprite('ma230_02', 3)
    label(9)
    sprite('ma230_03', 1)
    RandomCommonVoiceline(0)
    BeginBuffer('com5_2nd')
    sprite('ma230_03', 2)
    BufferedOrPressedGoto('com5_2nd')
    sprite('ma230_04', 3)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ma230_02', 3)
    DisallowGoto('com5_2nd')
    if SLOT_94:
        ChainCancel(0)
        WhiffCancelEnable(0)
    sprite('ma230_01', 2)
    sprite('ma230_00', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AttackP2(89)
        AirUntechableTime(40)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(4000)
        AirPushbackY(16000)
        CHHardKnockdown(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5D')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com5_2nd')
                DisallowGoto('com5_2nd')
            else:
                BufferedOrPressedGoto('com5_2nd')
    sprite('ma231_00', 3)
    sprite('ma231_01', 2)
    CommonSE('008_swing_pole_1')
    sprite('ma231_02', 2)
    sprite('ma231_03', 2)
    RandomCommonVoiceline(1)
    BeginBuffer('com5_2nd')
    CreateObject('maef_231', -1)
    sprite('ma231_04', 3)
    sprite('ma231_05', 6)
    BufferedOrPressedGoto('com5_2nd')
    Recovery()
    Unknown2063()
    sprite('ma231_06', 4)
    DisallowGoto('com5_2nd')
    if SLOT_94:
        ChainCancel(0)
    sprite('ma231_07', 4)
    sprite('ma231_08', 4)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(850)
        AttackP1(90)
        AttackP2(82)
        AirUntechableTime(26)
        AirPushbackX(8000)
        AirPushbackY(32000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma232_00', 3)
    sprite('ma232_01', 2)
    RandomCommonVoiceline(2)
    sprite('ma232_02', 2)
    CommonSE('006_swing_blade_1')
    sprite('ma232_03', 2)
    sprite('ma232_04', 4)
    CreateObject('maef_232', -1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('ma232_05', 5)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ma232_06', 5)
    sprite('ma232_07', 5)
    sprite('ma232_08', 5)
    sprite('ma232_09', 5)
    sprite('ma232_10', 5)


@Subroutine
def com2nd_Init():
    PreviousStateCheck('NmlAtk5A')
    SLOT_51 = SLOT_0
    PreviousStateCheck('NmlAtk5B')
    SLOT_52 = SLOT_0
    PreviousStateCheck('NmlAtk5C')
    SLOT_53 = SLOT_0


@State
def com1_2nd():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        callSubroutine('com2nd_Init')
        AttackLevel_(3)
        Damage(600)
        AirUntechableTime(24)
        Hitstun(22)
        AirPushbackY(20000)
        PushbackX(30400)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com1_3rd_ShotA')
                HitOrBlockCancel('com1_3rd_ShotB')
                HitOrBlockCancel('com1_3rd_3')
                DisallowGoto('com1_3rd_ShotA')
                DisallowGoto('com1_3rd_ShotB')
                DisallowGoto('com1_3rd_3')
            else:
                BufferedOrPressedGoto('com1_3rd_ShotA')
                BufferedOrPressedGoto('com1_3rd_ShotB')
                BufferedOrPressedGoto('com1_3rd_3')
            SLOT_61 = 1
    if SLOT_52:
        conditionalSendToLabel(1)
    sprite('ma200_04', 1)
    sprite('ma500_00', 2)
    sprite('ma500_01', 2)
    physicsXImpulse(20000)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ma201_04', 1)
    sprite('ma500_10', 2)
    sprite('ma500_01', 2)
    AddX(40000)
    physicsXImpulse(20000)
    loopRest()
    label(9)
    sprite('ma500_02', 2)
    BeginBuffer('com1_3rd_ShotA')
    BeginBuffer('com1_3rd_ShotB')
    BeginBuffer('com1_3rd_3')
    Voiceline('ma110')
    CommonSE('008_swing_pole_1')
    sprite('ma500_03', 3)
    CreateObject('maef_500', -1)
    EndMomentum(1)
    sprite('ma500_04', 3)
    Recovery()
    Unknown2063()
    sprite('ma500_05', 2)
    BufferedOrPressedGoto('com1_3rd_ShotA')
    BufferedOrPressedGoto('com1_3rd_ShotB')
    BufferedOrPressedGoto('com1_3rd_3')
    sprite('ma500_06', 2)
    sprite('ma500_07', 2)
    DisallowGoto('com1_3rd_ShotA')
    DisallowGoto('com1_3rd_ShotB')
    DisallowGoto('com1_3rd_3')
    if SLOT_94:
        ChainCancel(0)
    sprite('ma500_08', 2)
    sprite('ma500_09', 2)


@State
def com1_3rd_ShotA():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        BonusProration(110)
        AirUntechableTime(30)
        AirPushbackX(8000)
        PushbackX(12000)
        Hitstop(6)
        UseSlashHitspark(1)
        SpecialCancel(0)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(13)
        PreviousStateCheck('com1_2nd')
        SLOT_51 = SLOT_0
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('ma502_06', 5)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ma501_00', 3)
    sprite('ma501_01', 3)
    sprite('ma501_02', 3)
    label(9)
    sprite('ma501_03', 3)
    SmartRandomVoiceline('ma111', 100, 'ma112', 100, '', 0, '', 0)
    CommonSE('008_swing_pole_1')
    CreateObject('maef_501_zanzou', -1)
    if not SLOT_51:
        StartMultihit()
    BeginBuffer('com1_Ex3rd_ShotA')
    BeginBuffer('com1_Ex3rd_ShotB')
    callSubroutine('FuncSpeciaInput')
    sprite('ma501_03', 2)
    StartMultihit()
    sprite('ma501_04', 3)
    CreateObject('maef_muzzle', 0)
    sprite('ma501_04', 2)
    CreateObject('maef_501_atk', 0)
    ObjectUpon(STATE_END, 32)
    sprite('ma501_05', 3)
    sprite('ma501_05', 1)
    callSubroutine('FuncSpeciaTiming')
    sprite('ma501_05', 1)
    BufferedOrPressedGoto('com1_Ex3rd_ShotA')
    BufferedOrPressedGoto('com1_Ex3rd_ShotB')
    sprite('ma501_06', 5)
    DisallowGoto('com1_Ex3rd_ShotA')
    DisallowGoto('com1_Ex3rd_ShotB')
    sprite('ma501_07', 5)
    sprite('ma501_08', 5)
    Recovery()
    sprite('ma501_09', 5)
    CommonSE('008_swing_pole_1')
    sprite('ma501_10', 5)
    sprite('ma501_11', 5)
    sprite('ma501_12', 5)


@State
def com1_3rd_ShotB():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        BonusProration(110)
        AirUntechableTime(30)
        AirPushbackX(8000)
        PushbackX(12000)
        Hitstop(6)
        UseSlashHitspark(1)
        SpecialCancel(0)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(13)
        PreviousStateCheck('com1_2nd')
        SLOT_51 = SLOT_0
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('ma502_06', 5)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ma501_00', 3)
    sprite('ma501_01', 3)
    sprite('ma501_02', 3)
    label(9)
    sprite('ma501_03', 3)
    SmartRandomVoiceline('ma111', 100, 'ma112', 100, '', 0, '', 0)
    CommonSE('008_swing_pole_1')
    CreateObject('maef_501_zanzou', -1)
    if not SLOT_51:
        StartMultihit()
    BeginBuffer('com1_Ex3rd_ShotA')
    BeginBuffer('com1_Ex3rd_ShotB')
    callSubroutine('FuncSpeciaInput')
    sprite('ma501_03', 2)
    StartMultihit()
    sprite('ma501_04', 3)
    CreateObject('maef_muzzle', 1)
    sprite('ma501_04', 2)
    StartMultihit()
    CreateObject('maef_501_atk', 1)
    ObjectUpon(STATE_END, 33)
    sprite('ma501_05', 3)
    sprite('ma501_05', 1)
    callSubroutine('FuncSpeciaTiming')
    sprite('ma501_05', 1)
    BufferedOrPressedGoto('com1_Ex3rd_ShotA')
    BufferedOrPressedGoto('com1_Ex3rd_ShotB')
    sprite('ma501_06', 5)
    DisallowGoto('com1_Ex3rd_ShotA')
    DisallowGoto('com1_Ex3rd_ShotB')
    sprite('ma501_07', 5)
    sprite('ma501_08', 5)
    Recovery()
    sprite('ma501_09', 5)
    CommonSE('008_swing_pole_1')
    sprite('ma501_10', 5)
    sprite('ma501_11', 5)
    sprite('ma501_12', 5)


@State
def com1_Ex3rd_ShotA():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
    sprite('ma502_00', 5)
    sprite('ma502_01', 3)
    sprite('ma502_02', 3)
    SmartRandomVoiceline('ma111', 100, 'ma112', 100, '', 0, '', 0)
    CommonSE('008_swing_pole_1')
    sprite('ma502_03', 3)
    CreateObject('maef_502_zanzou', -1)
    BeginBuffer('com1_3rd_ShotA')
    BeginBuffer('com1_3rd_ShotB')
    callSubroutine('FuncSpeciaInput')
    sprite('ma502_03', 3)
    CreateObject('maef_muzzle', 0)
    sprite('ma502_04', 5)
    CreateObject('maef_501_atk', 0)
    ObjectUpon(STATE_END, 32)
    sprite('ma502_05', 3)
    sprite('ma502_05', 1)
    callSubroutine('FuncSpeciaTiming')
    sprite('ma502_05', 1)
    BufferedOrPressedGoto('com1_3rd_ShotA')
    BufferedOrPressedGoto('com1_3rd_ShotB')
    sprite('ma501_07', 5)
    DisallowGoto('com1_3rd_ShotA')
    DisallowGoto('com1_3rd_ShotB')
    sprite('ma501_08', 5)
    Recovery()
    sprite('ma501_09', 5)
    CommonSE('008_swing_pole_1')
    sprite('ma501_10', 5)
    sprite('ma501_11', 5)
    sprite('ma501_12', 5)


@State
def com1_Ex3rd_ShotB():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
    sprite('ma502_00', 5)
    sprite('ma502_01', 3)
    sprite('ma502_02', 3)
    SmartRandomVoiceline('ma111', 100, 'ma112', 100, '', 0, '', 0)
    CommonSE('008_swing_pole_1')
    sprite('ma502_03', 2)
    CreateObject('maef_502_zanzou', -1)
    BeginBuffer('com1_3rd_ShotA')
    BeginBuffer('com1_3rd_ShotB')
    callSubroutine('FuncSpeciaInput')
    sprite('ma502_03', 3)
    CreateObject('maef_muzzle', 1)
    sprite('ma502_04', 5)
    CreateObject('maef_501_atk', 1)
    ObjectUpon(STATE_END, 33)
    sprite('ma502_05', 3)
    sprite('ma502_05', 1)
    callSubroutine('FuncSpeciaTiming')
    sprite('ma502_05', 1)
    BufferedOrPressedGoto('com1_3rd_ShotA')
    BufferedOrPressedGoto('com1_3rd_ShotB')
    sprite('ma501_07', 5)
    DisallowGoto('com1_3rd_ShotA')
    DisallowGoto('com1_3rd_ShotB')
    sprite('ma501_08', 5)
    Recovery()
    sprite('ma501_09', 5)
    CommonSE('008_swing_pole_1')
    sprite('ma501_10', 5)
    sprite('ma501_11', 5)
    sprite('ma501_12', 5)


@State
def com1_3rd_3():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1200)
        AttackP2(82)
        AirUntechableTime(34)
        GroundedHitstunAnimation(6)
        Hitstun(9)
        CHHitstun(18)
        PushbackX(50000)
        AirPushbackX(40000)
        AirPushbackY(12000)
        CHAirPushbackX(50000)
        FatalCounter(1)
        CHWallbounce(1)
        CHFloorslide(10)
        AttackDirection(0)
        UseSlashHitspark(1)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        HitCancel('NmlAtk5D')
    sprite('ma503_00', 3)
    sprite('ma503_01', 3)
    sprite('ma503_02', 3)
    sprite('ma503_03', 3)
    Voiceline('ma113')
    sprite('ma503_04', 3)
    CreateObject('maef_503', -1)
    CreateObject('maef_503_wind', -1)
    physicsXImpulse(60000)
    AltKnockdownEffects(100, 1, 1)
    PreDashEffects(100, 1, 1)
    sprite('ma503_05', 4)
    XImpulseAcceleration(50)
    sprite('ma503_06', 3)
    XImpulseAcceleration(30)
    Recovery()
    Unknown2063()
    DashEffects(100, 1, 1)
    sprite('ma503_07', 3)
    XImpulseAcceleration(30)
    DashEffects(100, 1, 1)
    sprite('ma503_08', 3)
    XImpulseAcceleration(30)
    SkidEffects(100, 1, 1)
    sprite('ma503_09', 3)
    XImpulseAcceleration(0)
    sprite('ma503_10', 3)
    sprite('ma503_11', 3)


@State
def com2_2nd():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        callSubroutine('com2nd_Init')
        AttackLevel_(3)
        Damage(900)
        PushbackX(8000)
        AirHitstunAnimation(13)
        CHGroundedHitstunAnimation(2)
        AirPushbackX(18000)
        AirPushbackY(12000)
        AirUntechableTime(26)
        Hitstun(19)
        HitOrBlockCancel('com3_kamae')
        HitOrBlockCancel('NmlAtk5D')
        HitJumpCancel(1)

        def upon_OPPONENT_HIT():
            SLOT_61 = 1

        def upon_EVERY_FRAME():
            if CheckInput(0x5f):
                SetActionMark(1)
                clearUponHandler(EVERY_FRAME)
        StayAfterMovement(1, 0)
    if SLOT_52:
        conditionalSendToLabel(1)
    sprite('ma200_04', 1)
    sprite('ma510_00', 2)
    sprite('ma510_01', 2)
    physicsXImpulse(10000)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ma201_04', 1)
    sprite('ma510_11', 2)
    sprite('ma510_01', 2)
    AddX(50000)
    physicsXImpulse(10000)
    loopRest()
    label(9)
    sprite('ma510_02', 2)
    XImpulseAcceleration(50)
    sprite('ma510_03', 2)
    XImpulseAcceleration(50)
    CommonSE('004_swing_grap_1_2')
    loopRest()
    if SLOT_2:
        enterState('com3_kamae')
    sprite('ma510_04', 4)
    Voiceline('ma114')
    XImpulseAcceleration(0)
    sprite('ma510_05', 3)
    Recovery()
    Unknown2063()
    sprite('ma510_06', 1)
    if CheckInput(INPUT_HOLD_B):
        enterState('com3_kamae')
    sprite('ma510_06', 2)
    AttackOffOrBlockCancel('com3_kamae')
    sprite('ma510_07', 2)
    sprite('ma510_08', 2)
    sprite('ma510_09', 2)
    sprite('ma510_10', 2)


@State
def com3_kamae():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        WhiffCancel('com3_1')
        WhiffCancel('com3_1_InputC')
        WhiffCancel('com3_2')
        WhiffCancel('com3_2_InputC')
        WhiffCancel('com3_3')
        WhiffCancel('com3_3_InputC')
        PreviousStateCheck('com3_1')
        SLOT_51 = SLOT_0
        SetActionMark(10)
        StayAfterMovement(1, 0)

        def upon_GUARDPOINT_ACTIVATION():
            SetActionMark(10)
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('ma510_06', 3)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ma520_06', 4)
    sprite('ma520_07', 4)
    loopRest()
    label(1)
    sprite('ma511_00', 4)
    AddActionMark(-1)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(5, 15)
    WhiffCancelEnable(1)
    sprite('ma511_01', 2)
    sprite('ma511_01', 2)
    uponSendToLabel(RELEASE_B, 9)
    sprite('ma511_02', 4)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1)
    label(9)
    sprite('ma510_07', 2)
    clearUponHandler(RELEASE_B)
    WhiffCancelEnable(0)
    setInvincible(0)
    sprite('ma510_08', 2)
    sprite('ma510_09', 2)
    sprite('ma510_10', 2)


@State
def com3_1():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        BonusProration(110)
        AirUntechableTime(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        AirPushbackY(-60000)
        HardKnockdown(1)
        PushbackX(19800)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        SpecialCancel(0)
        StayAfterMovement(1, 0)
    sprite('ma520_00', 3)
    sprite('ma520_01', 3)
    sprite('ma520_02', 4)
    physicsXImpulse(4000)
    CommonSE('004_swing_grap_1_1')
    sprite('ma520_03', 2)
    CreateObject('maef_520_slash', -1)
    XImpulseAcceleration(500)
    SmartVoiceline('ma116')
    sprite('ma520_04', 3)
    XImpulseAcceleration(0)
    sprite('ma520_05', 5)
    XImpulseAcceleration(30)
    Recovery()
    Unknown2063()
    sprite('ma520_05', 1)
    XImpulseAcceleration(0)
    if CheckInput(INPUT_HOLD_B):
        enterState('com3_kamae')
    sprite('ma520_08', 4)
    sprite('ma520_09', 4)


@State
def com3_2():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(90)
        AttackP2(82)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackY(-55000)
        YImpulseBeforeWallbounce(0)
        BouncePercentage(50)
        AirUntechableTime(50)
        GroundBounce(1)
        EnemyHitstopAddition(0, 0, 0)
        StarterRating(2)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        SpecialCancel(0)
        StayAfterMovement(1, 1)
    sprite('ma521_00', 3)
    Voiceline('ma117')
    sprite('ma521_01', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('ma521_02', 3)
    SetXCollisionFromOrigin(150)
    sprite('ma521_03', 3)
    sprite('ma521_04', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('ma521_05', 2)
    sprite('ma521_06', 3)
    CreateObject('maef_521_kick', -1)
    sprite('ma521_07', 3)
    SetXCollisionFromOrigin(200)
    sprite('ma521_08', 2)
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('ma521_09', 3)
    EndMomentum(1)
    AddX(280000)
    LandingEffects(100, 1, 1)
    SetXCollisionFromOrigin(-1)
    sprite('ma521_10', 3)
    sprite('ma521_11', 3)
    sprite('ma521_12', 3)
    sprite('ma521_13', 3)
    sprite('ma521_14', 3)
    sprite('ma521_15', 3)


@State
def com3_3():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(68000)
        AirPushbackY(12000)
        AirUntechableTime(42)
        Floorslide(10)
        WallbounceReboundTime(5)
        CHWallbounceReboundTime(10)
        UseSlashHitspark(1)
        FatalCounter(1)
        SpecialCancel(0)
        StayAfterMovement(1, 0)
    sprite('ma522_00', 4)
    sprite('ma522_01', 4)
    Voiceline('ma118')
    sprite('ma522_02', 4)
    physicsXImpulse(20000)
    CommonSE('006_swing_blade_2')
    sprite('ma522_03', 3)
    CreateObject('maef_522', 0)
    CreateObject('maef_522_ribon', -1)
    XImpulseAcceleration(500)
    PreDashEffects(100, 1, 1)
    sprite('ma522_04', 3)
    XImpulseAcceleration(20)
    sprite('ma522_05', 3)
    XImpulseAcceleration(50)
    sprite('ma522_06', 6)
    Recovery()
    Unknown2063()
    TriggerUponForState('maef_522', 32)
    DespawnEAEffect('maef_522_ribon')
    XImpulseAcceleration(50)
    sprite('ma522_07', 4)
    XImpulseAcceleration(50)
    sprite('ma522_08', 4)
    XImpulseAcceleration(0)
    sprite('ma522_09', 4)
    sprite('ma522_10', 3)


@State
def com4_2nd():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        callSubroutine('com2nd_Init')
        AttackLevel_(3)
        Damage(850)
        Hitstun(19)
        AirUntechableTime(22)
        AirPushbackX(20000)
        AirPushbackY(14000)
        CHAirPushbackX(14000)
        CHAirPushbackY(20000)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_94:
                HitOrBlockCancel('com4_3rd_1')
                HitOrBlockCancel('com4_3rd_2')
                HitOrBlockCancel('com4_3rd_3')
                DisallowGoto('com4_3rd_1')
                DisallowGoto('com4_3rd_2')
                DisallowGoto('com4_3rd_3')
            else:
                BufferedOrPressedGoto('com4_3rd_1')
                BufferedOrPressedGoto('com4_3rd_2')
                BufferedOrPressedGoto('com4_3rd_3')
        StayAfterMovement(1, 0)
    if SLOT_52:
        conditionalSendToLabel(1)
    if SLOT_53:
        conditionalSendToLabel(2)
    sprite('ma200_04', 1)
    sprite('ma530_00', 1)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ma201_04', 1)
    sprite('ma530_12', 1)
    LandingEffects(100, 1, 1)
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('keep', 1)
    StartMultihit()
    AddX(-64000)
    sprite('ma530_13', 1)
    loopRest()
    label(9)
    sprite('ma530_01', 2)
    sprite('ma530_02', 2)
    sprite('ma530_03', 2)
    CommonSE('006_swing_blade_1')
    Voiceline('ma119')
    physicsXImpulse(25000)
    if SLOT_52:
        XImpulseAcceleration(150)
    if SLOT_53:
        XImpulseAcceleration(200)
    BeginBuffer('com4_3rd_1')
    BeginBuffer('com4_3rd_2')
    BeginBuffer('com4_3rd_3')
    sprite('ma530_04', 3)
    CreateObject('maef_530', -1)
    XImpulseAcceleration(20)
    sprite('ma530_04', 2)
    XImpulseAcceleration(50)
    sprite('ma530_05', 2)
    BufferedOrPressedGoto('com4_3rd_1')
    BufferedOrPressedGoto('com4_3rd_2')
    BufferedOrPressedGoto('com4_3rd_3')
    Recovery()
    Unknown2063()
    XImpulseAcceleration(50)
    sprite('ma530_06', 3)
    sprite('ma530_07', 3)
    XImpulseAcceleration(50)
    DisallowGoto('com4_3rd_1')
    DisallowGoto('com4_3rd_2')
    DisallowGoto('com4_3rd_3')
    if SLOT_94:
        ChainCancel(0)
    sprite('ma530_08', 3)
    XImpulseAcceleration(50)
    sprite('ma530_09', 3)
    AddX(-40000)
    sprite('ma530_10', 2)
    EndMomentum(1)
    sprite('ma530_11', 2)


@State
def com4_3rd_1():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        AttackP2(82)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(3)
        AirPushbackX(2000)
        AirPushbackY(-60000)
        YImpulseBeforeWallbounce(0)
        Hitstun(23)
        AirUntechableTime(60)
        GroundBounce(1)
        BouncePercentage(40)
        StarterRating(2)
        HitOverhead(2)
        UseSlashHitspark(1)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        HitCancel('NmlAtk5D')
        StayAfterMovement(1, 0)
    sprite('ma531_00', 3)
    PopSpeedX()
    sprite('ma531_01', 3)
    XImpulseAcceleration(80)
    sprite('ma531_02', 3)
    SetXCollisionFromOrigin(150)
    AddX(60000)
    XImpulseAcceleration(80)
    sprite('ma531_03', 3)
    XImpulseAcceleration(80)
    sprite('ma531_04', 3)
    XImpulseAcceleration(80)
    sprite('ma531_05', 5)
    Voiceline('ma120')
    EndMomentum(1)
    CommonSE('006_swing_blade_2')
    sprite('ma531_06', 2)
    ScreenShake(5000, 10000)
    CreateObject('maef_531', -1)
    sprite('ma531_06ex01', 2)
    sprite('ma531_07', 2)
    sprite('ma531_07', 2)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ma531_08', 4)
    sprite('ma531_09', 3)
    sprite('ma531_10', 2)
    SetXCollisionFromOrigin(-1)
    sprite('ma531_11', 2)
    sprite('ma531_12', 2)


@State
def com4_3rd_2():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(980)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(3)
        PushbackX(19800)
        AirPushbackY(-50000)
        HardKnockdown(15)
        StarterRating(2)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        SpecialCancel(0)
        StayAfterMovement(1, 1)
    sprite('ma532_00', 2)
    PopSpeedX()
    XImpulseAcceleration(80)
    Voiceline('ma121')
    CommonSE('019_cloth_b')
    sprite('ma532_01', 2)
    XImpulseAcceleration(80)
    sprite('ma532_02', 2)
    XImpulseAcceleration(80)
    sprite('ma532_03', 3)
    sprite('ma532_04', 3)
    sprite('ma532_05', 3)
    sprite('ma532_06', 3)
    physicsXImpulse(15000)
    CommonSE('004_swing_grap_1_2')
    sprite('ma532_07', 3)
    sprite('ma532_08', 3)
    XImpulseAcceleration(200)
    sprite('ma532_09', 3)
    EndMomentum(1)
    AddX(380000)
    LandingEffects(100, 1, 1)
    sprite('ma532_10', 3)
    sprite('ma532_11', 2)
    Recovery()
    Unknown2063()
    sprite('ma532_12', 2)
    sprite('ma532_13', 2)


@State
def com4_3rd_3():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(230)
        AttackP2(69)
        SingleProration(1)
        AirPushbackY(8000)
        AirPushbackX(12000)
        AirUntechableTime(35)
        Hitstun(25)
        Hitstop(2)
        ChipPercentage(5)
        HitAirUnblockable(0)
        UseSlashHitspark(1)
        DistanceCheck(1000000, 0, -1, -1)
        SpecialCancel(0)

        def upon_45():
            if CheckInput(0x14):
                SLOT_51 = SLOT_51 + SLOT_0

        def upon_EVERY_FRAME():
            if SLOT_2:
                HitBackReturnIgnore(1)
            else:
                HitBackReturnIgnore(0)
            if SLOT_54:
                SpecialCancel(0)
                AttackOffOrBlockCancel('NmlAtk5D')
                SLOT_52 = 0
            if SLOT_55:
                GroundedHitstunAnimation(13)
                AirHitstunAnimation(13)
                AirPushbackX(12000)
                AirPushbackY(20000)
                SLOT_52 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            XImpulseAcceleration(80)
            if SLOT_52:
                SpecialCancel(1)
                HitOrBlockCancel('NmlAtk5D')
            if SLOT_2:
                SetActionMark(0)
            else:
                SetActionMark(1)
    sprite('ma533_00', 2)
    PopSpeedX()
    XImpulseAcceleration(40)
    sprite('ma533_01', 2)
    sprite('ma533_02', 2)
    sprite('ma533_03', 1)
    StartMultihit()
    CreateObject('maef_533', -1)
    Voiceline('ma122')
    loopRest()
    SLOT_51 = 0
    sprite('ma533_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_04', 3)
    RefreshMultihit()
    sprite('ma533_05', 1)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    SLOT_52 = 1
    sprite('ma533_05', 2)
    SpecialCancel(1)
    HitOrBlockCancel('NmlAtk5D')
    sprite('ma533_03ex00', 3)
    RefreshMultihit()
    sprite('ma533_04ex00', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_05ex00', 3)
    RefreshMultihit()
    loopRest()
    if CheckInput(INPUT_HOLD_C):
        SLOT_51 = SLOT_51 + SLOT_0
    if not SLOT_51:
        notConditionalSendToLabel(9)
    SLOT_51 = 0
    sprite('ma533_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    XImpulseAcceleration(50)
    SLOT_53 = 1
    sprite('ma533_04', 3)
    RefreshMultihit()
    sprite('ma533_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_03ex00', 3)
    RefreshMultihit()
    sprite('ma533_04ex00', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_05ex00', 3)
    RefreshMultihit()
    loopRest()
    if not SLOT_51:
        notConditionalSendToLabel(9)
    SLOT_51 = 0
    sprite('ma533_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    XImpulseAcceleration(50)
    SLOT_54 = 1
    sprite('ma533_04', 3)
    RefreshMultihit()
    sprite('ma533_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_03ex00', 3)
    RefreshMultihit()
    sprite('ma533_04ex00', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_05ex00', 3)
    RefreshMultihit()
    loopRest()
    if not SLOT_51:
        notConditionalSendToLabel(9)
    SLOT_51 = 0
    sprite('ma533_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    XImpulseAcceleration(50)
    SLOT_55 = 1
    sprite('ma533_04', 3)
    RefreshMultihit()
    sprite('ma533_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_03ex00', 3)
    RefreshMultihit()
    sprite('ma533_04ex00', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ma533_05ex00', 3)
    RefreshMultihit()
    loopRest()
    label(9)
    sprite('ma533_06', 3)
    DespawnEAEffect('maef_533')
    clearUponHandler(16)
    Recovery()
    Unknown2063()
    XImpulseAcceleration(50)
    sprite('ma533_07', 3)
    XImpulseAcceleration(50)
    sprite('ma501_09', 4)
    EndMomentum(1)
    sprite('ma501_10', 4)
    sprite('ma501_11', 4)
    sprite('ma501_12', 4)


@State
def com5_2nd():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        HitLow(2)
        AirPushbackX(24000)
        AirPushbackY(15000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(28)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')
        PreviousStateCheck('NmlAtk2B')
        SLOT_51 = SLOT_0
        StayAfterMovement(1, 0)
    if SLOT_51:
        conditionalSendToLabel(1)
    sprite('ma230_04', 1)
    sprite('ma540_00', 3)
    sprite('ma540_01', 3)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ma231_05', 1)
    sprite('ma540_11', 3)
    AddX(25000)
    sprite('ma540_12', 3)
    loopRest()
    label(9)
    sprite('ma540_02', 2)
    Voiceline('ma123')
    sprite('ma540_03', 2)
    CreateObject('maef_540', -1)
    CommonSE('006_swing_blade_1')
    sprite('ma540_04', 3)
    sprite('ma540_05', 3)
    sprite('ma540_06', 3)
    Recovery()
    Unknown2063()
    sprite('ma540_07', 4)
    sprite('ma540_08', 4)
    sprite('ma540_09', 4)
    sprite('ma540_10', 4)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        AirUntechableTime(14)
        Hitstun(14)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma250_00', 2)
    PreviousStateCheck('NmlAtkAIR5A')
    SpriteCall('ma250_01', 2, 2, 0)
    sprite('ma250_01', 1)
    sprite('ma250_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('ma250_03', 3)
    sprite('ma250_04', 3)
    Recovery()
    Unknown2063()
    sprite('ma250_01', 3)
    sprite('ma250_00', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        AirUntechableTime(20)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma251_00', 3)
    sprite('ma251_01', 3)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_2')
    sprite('ma251_02', 2)
    sprite('ma251_03', 4)
    sprite('ma251_04', 2)
    sprite('ma251_05', 2)
    sprite('ma251_06', 4)
    Recovery()
    Unknown2063()
    sprite('ma251_07', 4)
    sprite('ma251_08', 4)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        UseSlashHitspark(1)
        AirUntechableTime(23)
        Hitstun(19)
        AirPushbackX(3000)
        CHAirPushbackX(10000)
        CHAirPushbackY(-30000)
        CHHardKnockdown(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma252_00', 2)
    sprite('ma252_01', 2)
    sprite('ma252_02', 3)
    RandomCommonVoiceline(2)
    CommonSE('006_swing_blade_1')
    sprite('ma252_03', 3)
    sprite('ma252_04', 4)
    CreateObject('maef_252', -1)
    sprite('ma252_05', 4)
    Recovery()
    Unknown2063()
    sprite('ma252_06', 4)
    sprite('ma252_07', 4)
    sprite('ma252_08', 4)
    sprite('ma252_09', 4)
    sprite('ma252_10', 4)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        SLOT_51 = 1
        SLOT_7 = 0
        SLOT_53 = SLOT_OverdriveTimer
        if CheckInput(INPUT_HOLD_D):
            SLOT_56 = 1

        def upon_EVERY_FRAME():
            if CheckInput(0x20):
                SLOT_57 = 1
            if SLOT_StateDuration >= 120:
                SLOT_57 = 1
            if not SLOT_57:
                if SLOT_56:
                    if SLOT_54:
                        if SLOT_64 == 0:
                            if CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 1
                                sendToLabel(10)
                            if CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 2
                                sendToLabel(20)
                        if SLOT_64 == 1:
                            if not CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                        if SLOT_64 >= 2:
                            if not CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                    elif not SLOT_57:
                        if CheckInput(0x93):
                            SLOT_64 = 1
                        elif CheckInput(0x45):
                            SLOT_64 = 2
                        else:
                            SLOT_64 = 0
            if SLOT_54:
                SLOT_55 = SLOT_55 + 1
                if SLOT_7:
                    Unknown23099(127)
                    if SLOT_53:
                        SLOT_55 >= 44
                    else:
                        SLOT_55 >= 64
                    if SLOT_0:
                        SLOT_52 = 1
                        SLOT_57 = 1
                else:
                    if SLOT_53:
                        SLOT_55 >= 30
                    else:
                        SLOT_55 >= 50
                    if SLOT_0:
                        AltKnockdownEffects(100, 1, 0)
                        PrivateSE('mase_01')
                        TriggerUponForState('maef_D_particle_a', 32)
                        TriggerUponForState('maef_D_particle_b', 32)
                        TriggerUponForState('maef_D_particle_c', 32)
                        SLOT_7 = 1
                        SLOT_52 = 0
                        SLOT_56 = 0
            if SLOT_52:
                if SLOT_57:
                    clearUponHandler(EVERY_FRAME)
                    if SLOT_64 <= 1:
                        sendToLabel(50)
                    if SLOT_64 >= 2:
                        sendToLabel(52)

        def upon_33():
            DisallowGoto('AN_NmlAtk5DD')

        def upon_STATE_END():
            if SLOT_58:
                SLOT_6 = 1
    sprite('ma203_00', 3)
    SLOT_59 = 0
    sprite('ma203_01', 3)
    SpriteIfNot0(2, 2, 53)
    if random_(2, 0, 50):
        SLOT_59 = 1
        Voiceline('ma106')
    else:
        Voiceline('ma108')
    sprite('ma203_02', 3)
    SpriteIfNot0(2, 2, 53)
    sprite('ma203_03', 1)
    sprite('ma203_03', 1)
    SLOT_54 = 1
    SLOT_56 = 0
    if SLOT_64 == 1:
        conditionalSendToLabel(9)
    if SLOT_64 == 2:
        conditionalSendToLabel(19)
    sprite('ma203_03', 1)
    sprite('ma203_04', 1)
    CreateObject('maef_D_hold', 0)
    PrivateSE('mase_09')
    sprite('ma203_04', 1)
    gotoLabel(0)
    label(9)
    sprite('ma204_00', 2)
    sprite('ma204_01', 4)
    CreateObject('maef_203_up2', 0)
    PrivateSE('mase_09')
    sprite('ma204_02', 3)
    SLOT_52 = 1
    SLOT_56 = 1
    loopRest()
    gotoLabel(11)
    label(19)
    sprite('ma205_00', 2)
    sprite('ma205_01', 4)
    CreateObject('maef_203_down2', 0)
    PrivateSE('mase_09')
    sprite('ma205_02', 3)
    SLOT_52 = 1
    SLOT_56 = 1
    loopRest()
    gotoLabel(21)
    label(0)
    sprite('ma203_04', 3)
    CreateObject('maef_D_hold', 0)
    sprite('ma203_05', 3)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma203_06', 3)
    label(1)
    sprite('ma203_05', 3)
    sprite('ma203_06', 3)
    sprite('ma203_04', 3)
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ma204_00', 3)
    CreateObject('maef_203_up', 0)
    sprite('ma204_01', 3)
    CreateObject('maef_203_up2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma204_02', 3)
    label(11)
    sprite('ma204_03', 3)
    sprite('ma204_01', 3)
    sprite('ma204_02', 3)
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ma205_00', 3)
    CreateObject('maef_203_down', 0)
    sprite('ma205_01', 3)
    CreateObject('maef_203_down2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma205_02', 3)
    label(21)
    sprite('ma205_03', 3)
    sprite('ma205_01', 3)
    sprite('ma205_02', 3)
    loopRest()
    gotoLabel(21)
    label(50)
    sprite('keep', 3)
    SpriteIfNot0(1, 2, 53)
    sprite('ma203_07', 3)
    SpriteCall('ma204_04', 3, 2, 64)
    SpriteIfNot0(2, 2, 53)
    if SLOT_59:
        Voiceline('ma107')
    else:
        Voiceline('ma109')
    BeginBuffer('AN_NmlAtk5DD')
    sprite('ma203_08', 3)
    SLOT_58 = 1
    DespawnEAEffect('maef_D')
    if SLOT_64:
        CreateObject('ma203Shot', 1)
        RegisterObject(11, 1)
        ObjectUpon2(11, 2, 0)
        PrivateSE('mase_02')
    else:
        CreateObject('ma203Shot', 0)
        RegisterObject(11, 1)
        ObjectUpon2(11, 0, 0)
        PrivateSE('mase_02')
    sprite('ma203_09', 3)
    BufferedOrPressedGoto('AN_NmlAtk5DD')
    Unknown23099(0)
    sprite('ma203_10', 3)
    sprite('ma203_11', 3)
    sprite('ma203_09', 3)
    sprite('ma203_10', 3)
    sprite('ma203_11', 3)
    sprite('ma203_09', 2)
    loopRest()
    gotoLabel(99)
    label(52)
    sprite('keep', 3)
    SpriteIfNot0(1, 2, 53)
    sprite('ma205_04', 3)
    SpriteIfNot0(2, 2, 53)
    if SLOT_59:
        Voiceline('ma107')
    else:
        Voiceline('ma109')
    BeginBuffer('AN_NmlAtk5DD')
    sprite('ma203_09', 3)
    SLOT_58 = 1
    DespawnEAEffect('maef_D')
    CreateObject('ma203Shot', 0)
    RegisterObject(11, 1)
    ObjectUpon2(11, 1, 0)
    PrivateSE('mase_02')
    sprite('ma203_10', 3)
    BufferedOrPressedGoto('AN_NmlAtk5DD')
    Unknown23099(0)
    sprite('ma203_11', 3)
    sprite('ma203_09', 3)
    sprite('ma203_10', 3)
    sprite('ma203_11', 3)
    sprite('ma203_09', 3)
    sprite('ma203_10', 2)
    label(99)
    sprite('keep', 1)
    DisallowGoto('AN_NmlAtk5DD')
    sprite('ma203_12', 4)
    sprite('ma203_13', 4)
    SLOT_51 = 0
    sprite('ma203_14', 4)
    CreateObject('maef_catch', 0)

    def RunOnObject_1():
        RotationAngle(34000)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_58 = 0
    sprite('ma203_15', 4)
    sprite('ma203_16', 4)
    sprite('ma203_17', 4)


@State
def AN_NmlAtk5DD():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        SpecialCancel(0)

        def upon_STATE_END():
            ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
        SLOT_58 = 1
    sprite('keep', 1)
    sprite('ma203_18', 3)
    sprite('ma203_19', 3)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    if SLOT_OverdriveTimer:
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('ma203_20', 3)
    sprite('ma203_21', 3)
    SpecialCancelOnHit(1)
    if SLOT_OverdriveTimer:
        SpecialCancel(1)
    sprite('ma203_22', 3)
    sprite('ma203_23', 3)
    sprite('ma203_21', 3)
    sprite('ma203_22', 3)
    sprite('ma203_24', 4)
    sprite('ma203_14', 4)
    CreateObject('maef_catch', 0)

    def RunOnObject_1():
        RotationAngle(35000)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_58 = 0
    sprite('ma203_15', 4)
    sprite('ma203_16', 4)
    sprite('ma203_17', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        PushSpeedX()
        PushSpeedY()
        ExternalForcesRate(0, 0)
        SLOT_51 = 1
        SLOT_7 = 0
        SLOT_53 = SLOT_OverdriveTimer
        if CheckInput(INPUT_HOLD_D):
            SLOT_56 = 1

        def upon_EVERY_FRAME():
            if CheckInput(0x20):
                SLOT_57 = 1
            if SLOT_StateDuration >= 120:
                SLOT_57 = 1
            if not SLOT_57:
                if SLOT_56:
                    if SLOT_54:
                        if SLOT_64 == 0:
                            if CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 1
                                sendToLabel(10)
                            if CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 2
                                sendToLabel(20)
                        if SLOT_64 == 1:
                            if not CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                        if SLOT_64 >= 2:
                            if not CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                    elif not SLOT_57:
                        if CheckInput(0x93):
                            SLOT_64 = 1
                        elif CheckInput(0x45):
                            SLOT_64 = 2
                        else:
                            SLOT_64 = 0
            if SLOT_54:
                SLOT_55 = SLOT_55 + 1
                if SLOT_7:
                    Unknown23099(127)
                    if SLOT_53:
                        SLOT_55 >= 44
                    else:
                        SLOT_55 >= 64
                    if SLOT_0:
                        SLOT_52 = 1
                        SLOT_57 = 1
                else:
                    if SLOT_53:
                        SLOT_55 >= 30
                    else:
                        SLOT_55 >= 50
                    if SLOT_0:
                        ScreenShake(0, 5000)
                        PrivateSE('mase_01')
                        TriggerUponForState('maef_D_particle_a', 32)
                        TriggerUponForState('maef_D_particle_b', 32)
                        TriggerUponForState('maef_D_particle_c', 32)
                        SLOT_7 = 1
                        SLOT_52 = 0
                        SLOT_56 = 0
            if SLOT_52:
                if SLOT_57:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(50)

        def upon_LANDING():
            ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
            DespawnEAEffect('maef_D')

        def upon_33():
            DisallowGoto('AN_NmlAtkAIR5DD')
    sprite('ma253_00', 3)
    SLOT_59 = 0
    sprite('ma253_01', 3)
    if SLOT_55 >= 50:
        SLOT_59 = 1
        Voiceline('ma106')
    else:
        Voiceline('ma108')
    ForcedLandingRecovery(9, 1)
    sprite('ma253_02', 3)
    SpriteIfNot0(2, 2, 53)
    EndMomentum(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma253_03', 2)
    XImpulseAcceleration(20)
    YAccel(30)
    sprite('ma253_03', 1)
    SLOT_54 = 1
    SLOT_56 = 0
    if SLOT_64 == 1:
        conditionalSendToLabel(9)
    if SLOT_64 == 2:
        conditionalSendToLabel(19)
    sprite('ma254_00', 3)
    YAccel(10)
    setGravity(50)
    sprite('ma254_01', 3)
    CreateObject('maef_AirD_hold', 0)
    PrivateSE('mase_09')
    sprite('ma254_02', 1)
    sprite('ma254_02', 2)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma254_03', 3)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ma253_04', 3)
    YAccel(10)
    setGravity(50)
    sprite('ma253_04', 3)
    CreateObject('maef_253_up2', 0)
    PrivateSE('mase_09')
    sprite('ma253_05', 1)
    sprite('ma253_05', 2)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma253_06', 3)
    loopRest()
    gotoLabel(11)
    label(19)
    sprite('ma255_00', 3)
    YAccel(10)
    setGravity(50)
    sprite('ma255_01', 3)
    CreateObject('maef_253_down2', 0)
    PrivateSE('mase_09')
    sprite('ma255_02', 1)
    sprite('ma255_02', 2)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma255_03', 3)
    loopRest()
    gotoLabel(21)
    label(0)
    sprite('ma254_01', 3)
    CreateObject('maef_AirD_hold', 0)
    sprite('ma254_02', 3)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma254_03', 3)
    label(1)
    sprite('ma254_01', 3)
    sprite('ma254_02', 3)
    sprite('ma254_03', 3)
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ma254_00', 3)
    CreateObject('maef_253_up', 0)
    sprite('ma253_04', 3)
    CreateObject('maef_253_up2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma253_05', 3)
    label(11)
    sprite('ma253_04', 3)
    sprite('ma253_05', 3)
    sprite('ma253_06', 3)
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ma255_00', 3)
    CreateObject('maef_253_down', 0)
    sprite('ma255_01', 3)
    CreateObject('maef_253_down2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma255_02', 3)
    label(21)
    sprite('ma255_01', 3)
    sprite('ma255_02', 3)
    sprite('ma255_03', 3)
    loopRest()
    gotoLabel(21)
    label(50)
    sprite('keep', 3)
    SpriteIfNot0(1, 2, 53)
    sprite('ma254_04', 3)
    SLOT_64 >= 2
    SpriteCall('ma255_04', 3, 2, 0)
    SLOT_64 == 1
    SpriteCall('ma253_07', 3, 2, 0)
    SpriteIfNot0(2, 2, 53)
    if SLOT_59:
        Voiceline('ma107')
    else:
        Voiceline('ma109')
    BeginBuffer('AN_NmlAtkAIR5DD')
    sprite('ma253_08', 3)
    SLOT_58 = 1
    DespawnEAEffect('maef_D')
    if SLOT_64:
        if SLOT_64 >= 2:
            CreateObject('ma203Shot', 2)
            RegisterObject(11, 1)
            ObjectUpon2(11, 5, 0)
            PrivateSE('mase_02')
        else:
            CreateObject('ma203Shot', 0)
            RegisterObject(11, 1)
            ObjectUpon2(11, 4, 0)
            PrivateSE('mase_02')
    else:
        CreateObject('ma203Shot', 1)
        RegisterObject(11, 1)
        ObjectUpon2(11, 3, 0)
        PrivateSE('mase_02')
    sprite('ma253_09', 3)
    PushSpeedY()
    EndMomentum(1)
    BufferedOrPressedGoto('AN_NmlAtkAIR5DD')
    Unknown23099(0)
    sprite('ma253_10', 3)
    sprite('ma253_11', 3)
    sprite('ma253_09', 3)
    sprite('ma253_10', 3)
    sprite('ma253_11', 3)
    sprite('ma253_09', 2)
    label(99)
    sprite('keep', 1)
    DisallowGoto('AN_NmlAtkAIR5DD')
    PopSpeedY()
    EndYPhysicsImpulse()
    PerGravity(80)
    sprite('ma253_12', 4)
    sprite('ma253_13', 4)
    sprite('ma253_14', 4)
    CreateObject('maef_catch', 0)

    def RunOnObject_1():
        RotationAngle(-35000)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_58 = 0
    sprite('ma253_15', 4)
    sprite('ma253_16', 4)
    sprite('ma253_17', 4)
    sprite('ma020_05', 3)
    Recovery()
    sprite('ma020_06', 3)
    label(999)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    gotoLabel(999)


@State
def AN_NmlAtkAIR5DD():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        SpecialCancel(0)

        def upon_LANDING():
            ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)

        def upon_STATE_END():
            ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
        SLOT_58 = 1
    sprite('keep', 1)
    sprite('ma253_18', 3)
    sprite('ma253_19', 3)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    if SLOT_OverdriveTimer:
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('ma253_20', 3)
    sprite('ma253_21', 3)
    SpecialCancelOnHit(1)
    if SLOT_OverdriveTimer:
        SpecialCancel(1)
    sprite('ma253_22', 3)
    sprite('ma253_23', 3)
    sprite('ma253_21', 3)
    sprite('ma253_22', 3)
    EndYPhysicsImpulse()
    PerGravity(80)
    sprite('ma253_24', 4)
    sprite('ma253_14', 4)
    CreateObject('maef_catch', 0)

    def RunOnObject_1():
        RotationAngle(-35000)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_58 = 0
    sprite('ma253_15', 4)
    sprite('ma253_16', 4)
    sprite('ma253_17', 3)
    sprite('ma020_05', 3)
    Recovery()
    sprite('ma020_06', 3)
    label(999)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    gotoLabel(999)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('ma300_00', 6)
    sprite('ma300_01', 6)
    CommonSE('019_cloth_a')
    RandomVoiceline('ma404', 100, 'ma405', 100, '', 0, '', 0)
    sprite('ma300_02', 6)
    sprite('ma300_03', 6)
    sprite('ma300_04', 6)
    sprite('ma300_05', 6)
    sprite('ma300_06', 6)
    sprite('ma300_07', 6)
    sprite('ma001_08', 6)
    sprite('ma001_09', 6)
    sprite('ma001_10', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        StayAfterMovement(1, 0)
    sprite('ma510_00', 3)
    sprite('ma510_01', 3)
    physicsXImpulse(20000)
    sprite('ma510_02', 3)
    XImpulseAcceleration(50)
    sprite('ma510_03', 3)
    AddX(30000)
    XImpulseAcceleration(50)
    sprite('ma510_04', 3)
    XImpulseAcceleration(0)
    sprite('ma510_05', 4)
    sprite('ma510_06', 5)
    sprite('ma510_07', 5)
    sprite('ma510_08', 6)
    sprite('ma510_09', 6)
    sprite('ma510_10', 6)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(17)
        AirPushbackX(3000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        StarterRating(2)
        UseSlashHitspark(1)

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
    sprite('ma340_00', 3)
    sprite('ma340_01', 1)
    Voiceline('ma159')
    E0EAEffect('GuardCrushWind', 0)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    sprite('ma340_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('ma340_02', 4)
    sprite('ma340_03', 4)
    sprite('ma340_04', 4)
    label(100)
    sprite('ma340_02', 4)
    sprite('ma340_03', 4)
    sprite('ma340_04', 4)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('ma340_05', 4)
    CommonSE('006_swing_blade_1')
    sprite('ma340_06', 4)
    physicsXImpulse(10000)
    sprite('ma340_07', 1)
    XImpulseAcceleration(30)
    CreateObject('maef_340', -1)
    sprite('ma340_07', 2)
    AttackOff()
    EnableAfterimage(0)
    sprite('ma340_08', 3)
    XImpulseAcceleration(50)
    sprite('ma340_09', 3)
    XImpulseAcceleration(50)
    sprite('ma340_10', 3)
    XImpulseAcceleration(50)
    sprite('ma340_11', 3)
    XImpulseAcceleration(50)
    sprite('ma340_12', 3)
    XImpulseAcceleration(50)
    sprite('ma340_13', 3)
    XImpulseAcceleration(50)
    sprite('ma340_14', 3)
    XImpulseAcceleration(50)
    sprite('ma340_15', 2)
    XImpulseAcceleration(0)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ma310_00', 3)
    sprite('ma310_01', 3)
    sprite('ma310_02', 3)
    sprite('ma310_03', 3)
    CommonSE('010_swing_sword_0')
    sprite('ma310_04', 3)
    Voiceline('ma155')
    sprite('ma310_05', 11)
    sprite('ma310_06', 3)
    sprite('ma310_07', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirUntechableTime(80)
        AirPushbackX(1000)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(2400)
        StarterRating(2)
        UseSlashHitspark(1)
        DamageFromStateOnly('ThrowExe')
        SpecialCancel(0)
        EnableRapidCancel(0)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
    sprite('ma310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ma311_00', 4)
    SetXCollisionFromOrigin(100)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    Voiceline('ma153')
    sprite('ma311_01', 4)
    SetXCollisionFromOrigin(200)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CommonSE('006_swing_blade_1')
    sprite('ma311_02', 4)
    SetXCollisionFromOrigin(300)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ma311_03', 8)
    SetXCollisionFromOrigin(400)
    CameraFollowTarget(23, 23)

    def RunOnObject_22():
        ForceShadowOff(1)
        CreateParticle('maef_311shadow', -1)
    sprite('ma311_04', 4)
    SetXCollisionFromOrigin(500)
    sprite('ma311_05', 4)
    SetXCollisionFromOrigin(-1)
    sprite('ma311_05ex1', 4)
    sprite('ma311_05ex2', 14)
    sprite('ma311_05ex2', 8)
    CreateObject('maef_311_shadow2', -1)
    sprite('ma311_06', 4)
    sprite('ma311_07', 4)
    CommonSE('006_swing_blade_1')
    sprite('ma311_08', 3)
    CameraFollowTarget(0, 0)
    CreateObject('maef_311', -1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    Hitstop(12)
    AttackP2(50)
    AirPushbackX(3000)
    AirPushbackY(-60000)
    ResetGravity()
    GroundBounce(1)
    BouncePercentage(30)
    HardKnockdown(1)
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        SpecialCancel(1)
        EnableRapidCancel(1)
    sprite('ma311_09', 3)
    sprite('ma311_10', 3)
    sprite('ma311_11', 3)
    sprite('ma311_12', 3)
    sprite('ma311_13', 3)
    sprite('ma311_14', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ma310_00', 3)
    sprite('ma310_01', 3)
    sprite('ma310_02', 3)
    sprite('ma310_03', 3)
    CommonSE('010_swing_sword_0')
    sprite('ma310_04', 3)
    Voiceline('ma155')
    sprite('ma310_05', 11)
    sprite('ma310_06', 3)
    sprite('ma310_07', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        AirPushbackX(-7000)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(2400)
        StarterRating(2)
        UseSlashHitspark(1)
        DamageFromStateOnly('BackThrowExe')
        SpecialCancel(0)
        EnableRapidCancel(0)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
    sprite('ma310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ma311_00', 4)
    SetXCollisionFromOrigin(100)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    Voiceline('ma153')
    sprite('ma311_01', 4)
    SetXCollisionFromOrigin(200)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CommonSE('006_swing_blade_1')
    sprite('ma311_02', 4)
    SetXCollisionFromOrigin(300)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ma311_03', 8)
    SetXCollisionFromOrigin(400)
    CameraFollowTarget(23, 23)

    def RunOnObject_22():
        ForceShadowOff(1)
        CreateParticle('maef_311shadow', -1)
    sprite('ma311_04', 4)
    SetXCollisionFromOrigin(500)
    sprite('ma311_05', 4)
    SetXCollisionFromOrigin(-1)
    sprite('ma311_05ex1', 4)
    sprite('ma311_05ex2', 14)
    sprite('ma311_05ex2', 8)
    ForceFaceSprite()
    CreateObject('maef_311_shadow2_b', -1)
    sprite('ma311_06', 4)
    sprite('ma311_07', 4)
    CommonSE('006_swing_blade_1')
    sprite('ma311_08', 3)
    CameraFollowTarget(0, 0)
    CreateObject('maef_311', -1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    Hitstop(12)
    AttackP2(50)
    AirPushbackX(3000)
    AirPushbackY(-60000)
    ResetGravity()
    GroundBounce(1)
    BouncePercentage(30)
    HardKnockdown(1)
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        SpecialCancel(1)
        EnableRapidCancel(1)
    sprite('ma311_09', 3)
    sprite('ma311_10', 3)
    sprite('ma311_11', 3)
    sprite('ma311_12', 3)
    sprite('ma311_13', 3)
    sprite('ma311_14', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('ma320_00', 3)
    sprite('ma320_01', 3)
    sprite('ma320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('ma320_03', 3)
    Voiceline('ma155')
    CommonSE('010_swing_sword_0')
    sprite('ma320_04', 4)
    sprite('ma320_05', 8)
    sprite('ma320_06', 4)
    sprite('ma320_07', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirPushbackX(1500)
        AirPushbackY(30000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        StarterRating(2)
        DamageFromStateOnly('AirThrowExe')
        SpecialCancel(0)
        EnableRapidCancel(0)
        EndMomentum(1)
        ForcedLandingRecovery(0, 0)
    sprite('ma320_02', 5)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('ma321_00', 4)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CommonSE('008_swing_pole_2')
    sprite('ma321_01', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ma321_02', 4)
    physicsYImpulse(1000)
    Voiceline('ma154')
    sprite('ma321_03', 5)
    sprite('ma321_04', 5)
    sprite('ma321_05', 5)
    sprite('ma321_06', 3)
    sprite('ma321_07', 3)
    CommonSE('006_swing_blade_1')
    sprite('ma321_08', 3)
    sprite('ma321_09', 4)
    CreateObject('maef_321', -1)
    physicsXImpulse(-20000)
    physicsYImpulse(15000)
    setGravity(2000)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    Hitstop(12)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(60000)
    AirPushbackY(20000)
    Wallbounce(1)
    WallbounceReboundTime(30)
    Wallstick(1)
    WallstickDuration(25)
    AirHitstunAfterWallbounce(50)
    UseSlashHitspark(1)
    DamageFromStateOnly('')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SpecialCancel(1)
        EnableRapidCancel(1)
    sprite('ma321_10', 4)
    XImpulseAcceleration(80)
    sprite('ma321_11', 4)
    XImpulseAcceleration(20)
    sprite('ma321_12', 4)
    XImpulseAcceleration(20)
    EndYPhysicsImpulse()
    sprite('ma321_13', 4)
    sprite('ma321_14', 4)


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        ForceFaceSprite()
        PreventBlocking(1)
        WhiffCancelEnable(1)
        WhiffCancel('UltimateJump')
        WhiffCancel('UltimateJumpOD')
        WhiffCancel('UltimateAssault')
        WhiffCancel('UltimateAssaultOD')
        BeginBuffer('Assault_A_EX')
        BeginBuffer('Assault_B_EX')
        BeginBuffer('Assault_C_EX')
        RunLoopUpon(17, 4)

        def upon_17():
            DisallowGoto3('Assault_A_EX')
            DisallowGoto3('Assault_B_EX')
            DisallowGoto3('Assault_C_EX')
            BeginBuffer('Assault_A')
            BeginBuffer('Assault_B')
            BeginBuffer('Assault_C')
            WhiffJumpCancel(0)
            WhiffBarrierCancel2(0)
            SLOT_61 = 0
            clearUponHandler(17)
        if SLOT_60:
            if SLOT_60 == 20:
                enterState('UltimateJump')
            if SLOT_60 == 21:
                enterState('UltimateJumpOD')
            if SLOT_60 == 30:
                enterState('UltimateAssault')
            if SLOT_60 == 31:
                enterState('UltimateAssaultOD')
        SLOT_4 = 8
        if SLOT_93:
            WhiffJumpCancel(1)
            WhiffBarrierCancel2(1)
        if SLOT_61:
            WhiffJumpCancel(1)
        PreviousStateCheck('Assault')
        SLOT_51 = SLOT_0

        def upon_STATE_END():
            SLOT_60 = 0
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('ma400_00', 3)
    if SLOT_6:
        if PreviousStateCheck('NmlAtk5D'):
            CreateObject('maef_catch', 0)

            def RunOnObject_1():
                RotationAngle(-210000)
        if PreviousStateCheck('AN_NmlAtk5DD'):
            CreateObject('maef_catch', 0)

            def RunOnObject_1():
                RotationAngle(-210000)
    label(0)
    sprite('ma400_01', 3)
    CommonSE('000_airdash_0')
    sprite('ma400_02', 2)
    if not SLOT_60:
        SmartVoiceline('ma200')
    physicsXImpulse(45000)
    PreDashEffects(100, 1, 1)
    WhiffCancel('Assault')
    WhiffCancel('Backflip')
    BufferedOrPressedGoto('Assault_A')
    BufferedOrPressedGoto('Assault_B')
    BufferedOrPressedGoto('Assault_C')
    BufferedOrPressedGoto('Assault_A_EX')
    BufferedOrPressedGoto('Assault_B_EX')
    BufferedOrPressedGoto('Assault_C_EX')

    def upon_EVERY_FRAME():
        if SLOT_60:
            if SLOT_60 == 1:
                enterState('Assault_A')
            if SLOT_60 == 2:
                enterState('Assault_B')
            if SLOT_60 == 3:
                enterState('Assault_C')
            if SLOT_60 == 11:
                enterState('Assault_A_EX')
            if SLOT_60 == 12:
                enterState('Assault_B_EX')
            if SLOT_60 == 13:
                enterState('Assault_C_EX')
    sprite('ma400_03', 2)
    AddInertia(28000)
    XImpulseAcceleration(80)
    sprite('ma400_02', 2)
    sprite('ma400_03', 2)
    XImpulseAcceleration(80)
    sprite('ma400_02', 2)
    sprite('ma400_03', 2)
    XImpulseAcceleration(60)
    sprite('ma400_02', 2)
    XImpulseAcceleration(60)
    sprite('ma400_04', 4)
    XImpulseAcceleration(50)
    ForceFaceSprite()
    clearUponHandler(EVERY_FRAME)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    sprite('ma400_05', 4)
    EndMomentum(1)


@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP2(69)
        Hitstun(22)
        AirUntechableTime(30)
        AirPushbackX(33000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        UseSlashHitspark(1)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(4)
            AttackP2(72)
            SingleProration(1)
            Hitstun(26)
            Hitstop(6)
            GroundedHitstunAnimation(2)

            def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
                SetActionMark(1)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(250)
        else:

            def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
                SetActionMark(1)
                sendToLabel(9)
    sprite('ma401_00', 1)
    Voiceline('ma201')
    sprite('ma401_01', 1)
    sprite('ma401_02', 1)
    sprite('ma401_03', 1)
    sprite('ma401_04', 2)
    CreateObject('maef_401', 0)
    DashEffects(100, 1, 1)
    PrivateSE('mase_06')
    EndMomentum(1)
    physicsXImpulse(60000)
    sprite('ma401_05', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05ex01', 1)
    TriggerUponForState('maef_401', 32)
    AddInertia(30000)
    if not SLOT_2:
        clearUponHandler(EVERY_FRAME)
        AttackLevel_(4)
        DamageMultiplier(110)
        AttackP2(82)
        CHGroundedHitstunAnimation(2)
        AirHitstunAnimation(10)
        AirPushbackX(-2000)
        AirPushbackY(22000)
        PushbackX(12000)
        Hitstop(12)
        SetActionMark(481)
        GuardCrush(100, 1)
        GuardCrushHitstun(25)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_A_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    label(9)
    sprite('ma401_06', 3)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    Recovery()
    XImpulseAcceleration(50)
    TriggerUponForState('maef_401', 32)
    sprite('ma401_07', 3)
    XImpulseAcceleration(50)
    PerInertia(0)
    sprite('ma401_08', 3)
    XImpulseAcceleration(50)
    sprite('ma401_09', 3)
    sprite('ma401_10', 3)
    sprite('ma401_11', 3)
    EndMomentum(1)
    sprite('ma401_12', 2)


@State
def Assault_A_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AttackP2(69)
        Hitstun(22)
        AirUntechableTime(30)
        AirPushbackX(33000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        UseSlashHitspark(1)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(4)
            AttackP2(72)
            SingleProration(1)
            Hitstun(26)
            Hitstop(6)
            GroundedHitstunAnimation(2)

            def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
                SetActionMark(1)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(275)
        else:

            def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
                SetActionMark(1)
                sendToLabel(9)
    sprite('ma401_00', 1)
    Voiceline('ma201')
    sprite('ma401_01', 1)
    sprite('ma401_02', 1)
    sprite('ma401_03', 1)
    sprite('ma401_04', 2)
    CreateObject('maef_401', 0)
    DashEffects(100, 1, 1)
    PrivateSE('mase_06')
    EndMomentum(1)
    physicsXImpulse(60000)
    sprite('ma401_05', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05ex01', 1)
    TriggerUponForState('maef_401', 32)
    AddInertia(30000)
    if not SLOT_2:
        clearUponHandler(EVERY_FRAME)
        AttackLevel_(4)
        DamageMultiplier(110)
        AttackP2(82)
        CHGroundedHitstunAnimation(2)
        AirHitstunAnimation(10)
        AirPushbackX(-2000)
        AirPushbackY(22000)
        PushbackX(12000)
        Hitstop(12)
        SetActionMark(481)
        GuardCrush(100, 1)
        GuardCrushHitstun(25)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_A_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    label(9)
    sprite('ma401_06', 3)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    Recovery()
    XImpulseAcceleration(50)
    TriggerUponForState('maef_401', 32)
    sprite('ma401_07', 3)
    XImpulseAcceleration(50)
    PerInertia(0)
    sprite('ma401_08', 3)
    XImpulseAcceleration(50)
    sprite('ma401_09', 3)
    sprite('ma401_10', 3)
    sprite('ma401_11', 3)
    EndMomentum(1)
    sprite('ma401_12', 2)


@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1250)
        AttackP2(72)
        AirUntechableTime(36)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(44000)
        AirPushbackY(13000)
        HardKnockdown(1)
        EnableEmergencyTechAirHit(1)
        UseSlashHitspark(1)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(5)
            AttackP2(74)
            SingleProration(1)
            AirUntechableTime(52)
            Hitstop(3)
            Wallbounce(1)
            WallbounceReboundTime(0)
            GroundedHitstunAnimation(2)
            HitsparkSize(800)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(125)
                    AirPushbackX(55000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)
    sprite('ma401_00', 4)
    Voiceline('ma202')
    PerInertia(30)
    sprite('ma401_01', 4)
    sprite('ma401_02', 3)
    sprite('ma401_03', 3)
    sprite('ma401_04', 2)
    CreateObject('maef_401', 0)
    DashEffects(100, 1, 1)
    PrivateSE('mase_06')
    EndMomentum(1)
    physicsXImpulse(90000)
    if CheckInput(0x5e):
        XSpeed(-15000)
    sprite('ma401_05', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_04', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05ex01', 1)
    TriggerUponForState('maef_401', 32)
    AddInertia(30000)
    if not SLOT_2:
        clearUponHandler(EVERY_FRAME)
        AttackLevel_(5)
        DamageMultiplier(110)
        AttackP2(84)
        PushbackX(12000)
        Hitstop(13)
        EnableEmergencyTechAirHit(0)
        SetActionMark(481)
        GuardCrush(100, 1)
        GuardCrushHitstun(35)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_B_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    sprite('ma401_06', 3)
    Recovery()
    XImpulseAcceleration(20)
    sprite('ma401_07', 3)
    XImpulseAcceleration(50)
    PerInertia(0)
    sprite('ma401_08', 3)
    XImpulseAcceleration(50)
    sprite('ma401_09', 3)
    sprite('ma401_10', 3)
    sprite('ma401_11', 3)
    EndMomentum(1)
    sprite('ma401_12', 2)


@State
def Assault_B_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1375)
        AttackP2(72)
        AirUntechableTime(36)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(44000)
        AirPushbackY(13000)
        HardKnockdown(1)
        EnableEmergencyTechAirHit(1)
        UseSlashHitspark(1)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(5)
            AttackP2(74)
            SingleProration(1)
            AirUntechableTime(52)
            Hitstop(3)
            Wallbounce(1)
            WallbounceReboundTime(0)
            GroundedHitstunAnimation(2)
            HitsparkSize(800)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(137)
                    AirPushbackX(55000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)
    sprite('ma401_00', 4)
    Voiceline('ma202')
    PerInertia(30)
    sprite('ma401_01', 4)
    sprite('ma401_02', 3)
    sprite('ma401_03', 3)
    sprite('ma401_04', 2)
    CreateObject('maef_401', 0)
    DashEffects(100, 1, 1)
    PrivateSE('mase_06')
    EndMomentum(1)
    physicsXImpulse(90000)
    if CheckInput(0x5e):
        XSpeed(-15000)
    sprite('ma401_05', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_04', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_05ex01', 1)
    TriggerUponForState('maef_401', 32)
    AddInertia(30000)
    if not SLOT_2:
        clearUponHandler(EVERY_FRAME)
        AttackLevel_(5)
        DamageMultiplier(110)
        AttackP2(84)
        PushbackX(12000)
        Hitstop(13)
        EnableEmergencyTechAirHit(0)
        SetActionMark(481)
        GuardCrush(100, 1)
        GuardCrushHitstun(35)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_B_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    sprite('ma401_06', 3)
    Recovery()
    XImpulseAcceleration(20)
    sprite('ma401_07', 3)
    XImpulseAcceleration(50)
    PerInertia(0)
    sprite('ma401_08', 3)
    XImpulseAcceleration(50)
    sprite('ma401_09', 3)
    sprite('ma401_10', 3)
    sprite('ma401_11', 3)
    EndMomentum(1)
    sprite('ma401_12', 2)


@State
def Assault_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(70)
        AttackP2(72)
        AirUntechableTime(40)
        AirPushbackX(22000)
        AirPushbackY(36000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        HitAirUnblockable(3)
        CrouchWhiff(1)
        UseSlashHitspark(1)
        StarterRating(0)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(5)
            AttackP2(74)
            SingleProration(1)
            AirUntechableTime(60)
            Hitstop(3)
            HitsparkSize(800)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(130)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)

        def upon_OPPONENT_HIT():
            SLOT_51 = 1
        uponSendToLabel(LANDING, 9)
    sprite('ma401_00', 2)
    Voiceline('ma203')
    setInvincible(1)
    sprite('ma401_01', 2)
    sprite('ma401_02', 2)
    sprite('ma401_03', 2)
    BeginBuffer('Backflip')
    sprite('ma401_13', 2)
    CreateObject('maef_401C', 0)
    PrivateSE('mase_06')
    EndMomentum(1)
    SetInertia(10000)
    physicsXImpulse(60000)
    physicsYImpulse(40000)
    SetAcceleration(-3000)
    setGravity(2000)
    sprite('ma401_14', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_13', 2)
    setInvincible(0)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_14', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_14ex01', 1)
    TriggerUponForState('maef_401C', 32)
    if not SLOT_2:
        AttackLevel_(5)
        DamageMultiplier(110)
        AttackP2(84)
        AirPushbackY(40000)
        AirPushbackX(3000)
        AirUntechableTime(60)
        Hitstop(13)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_C_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    sprite('ma401_15', 3)
    if SLOT_51:
        BufferedOrPressedGoto('Backflip')
    PerAcceleration(0)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma401_16', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma321_11', 3)
    sprite('ma321_12', 3)
    sprite('ma321_13', 3)
    sprite('ma321_14', 3)
    sprite('ma020_04', 3)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(0)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    WhiffCancelEnable(0)
    sprite('ma024_00', 2)
    sprite('ma024_01', 3)
    sprite('ma024_02', 3)
    sprite('ma024_03', 2)
    sprite('ma024_04', 2)


@State
def Assault_C_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1430)
        AttackP1(70)
        AttackP2(72)
        AirUntechableTime(40)
        AirPushbackX(22000)
        AirPushbackY(36000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        HitAirUnblockable(3)
        CrouchWhiff(1)
        UseSlashHitspark(1)
        StarterRating(0)
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            AttackLevel_(5)
            AttackP2(74)
            SingleProration(1)
            AirUntechableTime(60)
            Hitstop(3)
            HitsparkSize(800)

            def upon_EVERY_FRAME():
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    Damage(143)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)

        def upon_OPPONENT_HIT():
            SLOT_51 = 1
        uponSendToLabel(LANDING, 9)
    sprite('ma401_00', 2)
    Voiceline('ma203')
    setInvincible(1)
    sprite('ma401_01', 2)
    sprite('ma401_02', 2)
    sprite('ma401_03', 2)
    BeginBuffer('Backflip')
    sprite('ma401_13', 2)
    CreateObject('maef_401C', 0)
    PrivateSE('mase_06')
    EndMomentum(1)
    SetInertia(10000)
    physicsXImpulse(60000)
    physicsYImpulse(40000)
    SetAcceleration(-3000)
    setGravity(2000)
    sprite('ma401_14', 2)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_13', 2)
    setInvincible(0)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_14', 1)
    if SLOT_58:
        RefreshMultihit()
    sprite('ma401_14ex01', 1)
    TriggerUponForState('maef_401C', 32)
    if not SLOT_2:
        AttackLevel_(5)
        DamageMultiplier(110)
        AttackP2(84)
        AirPushbackY(40000)
        AirPushbackX(3000)
        AirUntechableTime(60)
        Hitstop(13)
        DamageEffect(2, 'maef_401_hit')
        GotoState('Assault_C_SP')
        CreateObject('maef_401_impact', 0)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(0, 15000)
    sprite('ma401_15', 3)
    if SLOT_51:
        BufferedOrPressedGoto('Backflip')
    PerAcceleration(0)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma401_16', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma321_11', 3)
    sprite('ma321_12', 3)
    sprite('ma321_13', 3)
    sprite('ma321_14', 3)
    sprite('ma020_04', 3)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(0)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    WhiffCancelEnable(0)
    sprite('ma024_00', 2)
    sprite('ma024_01', 3)
    sprite('ma024_02', 3)
    sprite('ma024_03', 2)
    sprite('ma024_04', 2)


@State
def Backflip():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        WhiffCancelEnable(1)
        WhiffCancel('UltimateJump')
        WhiffCancel('UltimateJumpOD')
        WhiffCancel('UltimateAssault')
        WhiffCancel('UltimateAssaultOD')
        BeginBuffer('NmlAtkAIR5D')
        BeginBuffer('Backflip_A')
        BeginBuffer('Backflip_B')
        BeginBuffer('Backflip_C')
        RunLoopUpon(17, 4)

        def upon_17():
            WhiffJumpCancel(0)
            WhiffBarrierCancel2(0)
            SLOT_61 = 0
            AddAirJumpCount(-1)
            AddAirDashCount(-1)
            SLOT_34 = SLOT_34 + -1
            clearUponHandler(17)
        if SLOT_60:
            if SLOT_60 == 20:
                enterState('UltimateJump')
            if SLOT_60 == 21:
                enterState('UltimateJumpOD')
            if SLOT_60 == 30:
                enterState('UltimateAssault')
            if SLOT_60 == 31:
                enterState('UltimateAssaultOD')
        if SLOT_61:
            WhiffJumpCancel(1)
        PreviousStateCheck('Assault')
        SLOT_51 = SLOT_0

        def upon_STATE_END():
            if SLOT_4 >= 4:
                SLOT_4 = 4
    if SLOT_IsAirborne:
        conditionalSendToLabel(100)
    sprite('ma402_00', 2)
    SpriteCall('ma402_08', 2, 2, 51)
    PerInertia(150)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    SLOT_4 = 8
    if SLOT_93:
        WhiffJumpCancel(1)
        WhiffBarrierCancel2(1)
    sprite('ma402_01', 2)
    sprite('ma402_02', 5)
    SpecificInvincibility(1, 1, 1, 1, 1)
    JumpEffects(0, 0)
    EnableAfterimage(1)
    physicsXImpulse(-16000)
    physicsYImpulse(28000)
    EndYPhysicsImpulse()
    ForcedLandingRecovery(4, 1)
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('ma402_10', 2)
    SLOT_4 = 16
    XImpulseAcceleration(-20)
    XSpeed(-4000)
    physicsYImpulse(60000)
    setGravity(2400)
    if SLOT_93:
        WhiffJumpCancel(1)
    sprite('ma402_09', 2)
    sprite('ma402_02', 2)
    YAccel(60)
    setInvincible(1)
    JumpSoundEffects()
    CommonSE('000_airdash_0')
    EnableAfterimage(1)
    ForcedLandingRecovery(4, 1)
    loopRest()
    label(9)
    sprite('ma402_03', 5)
    if not SLOT_60:
        SmartVoiceline('ma204')
    WhiffCancel('Backflip')
    BufferedOrPressedGoto('Backflip_A')
    BufferedOrPressedGoto('Backflip_B')
    BufferedOrPressedGoto('Backflip_C')
    BufferedOrPressedGoto('Backflip_A_EX')
    BufferedOrPressedGoto('Backflip_B_EX')
    BufferedOrPressedGoto('Backflip_C_EX')
    BufferedOrPressedGoto('NmlAtkAIR5D')

    def upon_EVERY_FRAME():
        if CheckInput(0x79):
            if SLOT_2:
                WhiffNormalCancel(1)
        else:
            WhiffNormalCancel(0)
            if SLOT_60:
                if SLOT_60 == 1:
                    enterState('Backflip_A')
                if SLOT_60 == 2:
                    enterState('Backflip_B')
                if SLOT_60 == 3:
                    enterState('Backflip_C')
    sprite('ma402_04', 5)
    setInvincible(0)
    SetActionMark(1)
    DisallowGoto('Backflip_A')
    DisallowGoto('Backflip_B')
    DisallowGoto('Backflip_C')
    WhiffCancel('Backflip_A_EX')
    WhiffCancel('Backflip_B_EX')
    WhiffCancel('Backflip_C_EX')
    sprite('ma402_05', 5)
    sprite('ma402_06', 5)
    EndYPhysicsImpulse()
    sprite('ma402_07', 5)
    sprite('ma020_04', 3)
    Recovery()
    clearUponHandler(EVERY_FRAME)
    WhiffNormalCancel(1)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(0)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(0)


@Subroutine
def Backflip_Init():
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 9)
    XImpulseAcceleration(-10)
    PerInertia(10)
    physicsYImpulse(15000)
    setGravity(750)
    SLOT_58 = SLOT_OverdriveTimer
    AttackLevel_(4)
    AttackP1(80)
    AttackP2(82)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirUntechableTime(40)
    HardKnockdown(1)
    UseSlashHitspark(1)
    StarterRating(2)


@State
def Backflip_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(900)
        AirPushbackX(1000)
        AirPushbackY(-72000)

        def upon_OPPONENT_HIT():
            setGravity(1000)
        callSubroutine('Backflip_Init')
    sprite('ma403_00', 2)
    Voiceline('ma205')
    sprite('ma403_01', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_02', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_03', 2)
    sprite('ma403_04', 2)
    sprite('ma403_05', 3)
    CreateObject('maef_403', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsYImpulse(-66000)
    EndYPhysicsImpulse()
    sprite('ma403_06', 3)
    label(0)
    sprite('ma403_05', 3)
    sprite('ma403_06', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_07', 2)
    DespawnEAEffect('maef_403')
    DespawnEAEffect('maef_401_ring')
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    if SLOT_58:
        CreateObject('maef_403_landing', 0)
        ScreenShake(0, 15000)
        AltKnockdownEffects(100, 0, 1)
        RefreshMultihit()
        EnemyHitstopAddition(4, 4, 9)
        AirPushbackX(-3000)
        AirPushbackY(25000)
        HardKnockdown(-1)
        UsePunchHitspark(1)
    else:
        AttackOff()
        Recovery()
    sprite('ma403_07', 4)
    AttackOff()
    Recovery()
    sprite('ma403_08', 6)
    sprite('ma403_09', 3)
    sprite('ma403_10', 3)


@State
def Backflip_A_EX():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(900)
        AirPushbackX(1000)
        AirPushbackY(-72000)

        def upon_OPPONENT_HIT():
            setGravity(1000)
        callSubroutine('Backflip_Init')
    sprite('ma403_00', 4)
    SpriteIfNot0(2, 2, 58)
    Voiceline('ma205')
    sprite('ma403_01', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_02', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_03', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_04', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_05', 3)
    CreateObject('maef_403', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsYImpulse(-66000)
    EndYPhysicsImpulse()
    sprite('ma403_06', 3)
    label(0)
    sprite('ma403_05', 3)
    sprite('ma403_06', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_07', 2)
    DespawnEAEffect('maef_403')
    DespawnEAEffect('maef_401_ring')
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    CreateObject('maef_403_landing', 0)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 0, 1)
    RefreshMultihit()
    EnemyHitstopAddition(4, 4, 9)
    AirPushbackX(-3000)
    AirPushbackY(25000)
    HardKnockdown(-1)
    UsePunchHitspark(1)
    sprite('ma403_07', 4)
    AttackOff()
    Recovery()
    sprite('ma403_08', 6)
    sprite('ma403_09', 3)
    sprite('ma403_10', 3)


@State
def Backflip_B():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(1000)
        AirPushbackX(24000)
        AirPushbackY(-58000)
        YImpulseBeforeWallbounce(1000)
        Floorslide(5)

        def upon_OPPONENT_HIT():
            SetAcceleration(450)
            setGravity(900)
        callSubroutine('Backflip_Init')
    sprite('ma403_11', 2)
    Voiceline('ma206')
    sprite('ma403_12', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_13', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_14', 2)
    sprite('ma403_15', 2)
    sprite('ma403_16', 3)
    CreateObject('maef_403B', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsXImpulse(30000)
    physicsYImpulse(-60000)
    sprite('ma403_17', 3)
    label(0)
    sprite('ma403_16', 3)
    sprite('ma403_17', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)
    DespawnEAEffect('maef_403B')
    DespawnEAEffect('maef_401_ring')
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    if SLOT_58:
        CreateObject('maef_403_landing', 0)
        ScreenShake(0, 15000)
        AltKnockdownEffects(100, 0, 1)
        RefreshMultihit()
        AirPushbackX(8000)
        AirPushbackY(30000)
        ResetGravity()
        EnemyHitstopAddition(4, 4, 9)
        HardKnockdown(-1)
        FloorslideReset()
        UsePunchHitspark(1)
    else:
        AttackOff()
        Recovery()
    sprite('ma403_18', 4)
    AttackOff()
    Recovery()
    sprite('ma403_19', 8)
    XImpulseAcceleration(50)
    sprite('ma403_09', 3)
    EndMomentum(1)
    sprite('ma403_10', 3)


@State
def Backflip_B_EX():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(1000)
        AirPushbackX(24000)
        AirPushbackY(-58000)
        YImpulseBeforeWallbounce(1000)
        Floorslide(5)

        def upon_OPPONENT_HIT():
            SetAcceleration(450)
            setGravity(900)
        callSubroutine('Backflip_Init')
    sprite('ma403_11', 4)
    SpriteIfNot0(2, 2, 58)
    Voiceline('ma206')
    sprite('ma403_12', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_13', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_14', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_15', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_16', 3)
    CreateObject('maef_403B', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsXImpulse(30000)
    physicsYImpulse(-60000)
    sprite('ma403_17', 3)
    label(0)
    sprite('ma403_16', 3)
    sprite('ma403_17', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)
    DespawnEAEffect('maef_403B')
    DespawnEAEffect('maef_401_ring')
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    CreateObject('maef_403_landing', 0)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 0, 1)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(30000)
    ResetGravity()
    EnemyHitstopAddition(4, 4, 9)
    HardKnockdown(-1)
    FloorslideReset()
    UsePunchHitspark(1)
    sprite('ma403_18', 4)
    AttackOff()
    Recovery()
    sprite('ma403_19', 8)
    XImpulseAcceleration(50)
    sprite('ma403_09', 3)
    EndMomentum(1)
    sprite('ma403_10', 3)


@State
def Backflip_C():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(1100)
        AirPushbackX(40000)
        AirPushbackY(-66000)
        YImpulseBeforeWallbounce(1000)
        Floorslide(5)

        def upon_OPPONENT_HIT():
            SetAcceleration(800)
            setGravity(800)
        callSubroutine('Backflip_Init')
        YAccel(200)
    sprite('ma403_11', 2)
    Voiceline('ma207')
    sprite('ma403_12ex', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_13ex', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_14ex', 2)
    sprite('ma403_15ex', 2)
    sprite('ma403_20', 3)
    CreateObject('maef_403C', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsXImpulse(50000)
    physicsYImpulse(-50000)
    sprite('ma403_21', 3)
    label(0)
    sprite('ma403_20', 3)
    sprite('ma403_21', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)
    DespawnEAEffect('maef_403C')
    DespawnEAEffect('maef_401_ring')
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    if SLOT_58:
        CreateObject('maef_403_landing', 0)
        ScreenShake(0, 15000)
        AltKnockdownEffects(100, 0, 1)
        RefreshMultihit()
        AirPushbackX(8000)
        AirPushbackY(30000)
        ResetGravity()
        EnemyHitstopAddition(4, 4, 9)
        HardKnockdown(-1)
        FloorslideReset()
        UsePunchHitspark(1)
    else:
        AttackOff()
        Recovery()
    sprite('ma403_18', 4)
    AttackOff()
    Recovery()
    sprite('ma403_19', 8)
    XImpulseAcceleration(50)
    sprite('ma403_09', 3)
    EndMomentum(1)
    sprite('ma403_10', 3)


@State
def Backflip_C_EX():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(1100)
        AirPushbackX(40000)
        AirPushbackY(-66000)
        YImpulseBeforeWallbounce(1000)
        Floorslide(5)

        def upon_OPPONENT_HIT():
            SetAcceleration(800)
            setGravity(800)
        callSubroutine('Backflip_Init')
    sprite('ma403_11', 4)
    SpriteIfNot0(2, 2, 58)
    Voiceline('ma207')
    sprite('ma403_12ex', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_13ex', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ma403_14ex', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_15ex', 4)
    SpriteIfNot0(2, 2, 58)
    sprite('ma403_20', 3)
    CreateObject('maef_403C', 0)
    PrivateSE('mase_05')
    EndMomentum(1)
    physicsXImpulse(50000)
    physicsYImpulse(-50000)
    sprite('ma403_21', 3)
    label(0)
    sprite('ma403_20', 3)
    sprite('ma403_21', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)
    DespawnEAEffect('maef_403C')
    DespawnEAEffect('maef_401_ring')
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    CreateObject('maef_403_landing', 0)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 0, 1)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(30000)
    ResetGravity()
    EnemyHitstopAddition(4, 4, 9)
    HardKnockdown(-1)
    FloorslideReset()
    UsePunchHitspark(1)
    sprite('ma403_18', 4)
    AttackOff()
    Recovery()
    sprite('ma403_19', 8)
    XImpulseAcceleration(50)
    sprite('ma403_09', 3)
    EndMomentum(1)
    sprite('ma403_10', 3)


@State
def UltimateJump():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        MinimumDamage(20)
        StarterRating(2)
        PushbackX(8000)
        EnemyHitstopAddition(0, -5, -5)
        HitAirUnblockable(3)
        AirUntechableTime(100)
        HardKnockdown(1)
        AirPushbackX(-1000)
        AirPushbackY(60000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AttackDirection(0)
        UseSlashHitspark(1)
        PassByArmor(1)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
            EndYPhysicsImpulse()

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SLOT_51 = 1
            NoDamageAction(1)
            CameraFollowTarget(22, 22)
            CameraLookAtEnemy(1)
        uponSendToLabel(LANDING, 99)
    sprite('ma431_00', 3)
    sprite('ma431_01', 3)
    setInvincible(1)
    DistortionSettings(25, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    Voiceline('ma252')
    sprite('ma431_02', 3)
    EndMomentum(1)
    sprite('ma431_03', 15)
    CreateObject('maef431', -1)
    sprite('ma431_04', 3)
    CreateObject('maef431_jump', -1)
    sprite('ma431_05', 3)
    sprite('ma431_06ex01', 1)
    JumpEffects(1, 0)
    sprite('ma431_06', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(10000)
    YImpulseBeforeWallbounce(10)
    EnemyHitstopAddition(0, 0, 8)
    Hitstop(6)
    EnableRapidCancel(0)
    physicsXImpulse(0)
    physicsYImpulse(120000)
    setGravity(-10000)

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor >= 2600000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            AbsoluteY(2600000)
            sendToLabel(11)
    sprite('ma431_07', 4)
    CameraFollowTarget(22, 22)
    SetXCollisionFromOrigin(10)
    label(5)
    sprite('ma431_06', 3)
    sprite('ma431_07', 3)
    loopRest()
    gotoLabel(5)
    label(11)
    sprite('null', 10)
    SpriteCall('null', 20, 2, 51)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 9)
    DespawnEAEffect('maef431_jump')
    SetXCollisionFromOrigin(-1)
    if SLOT_51:
        TeleportToObject(22)
        AddY(800000)
    CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
    AddX(-5000)
    sprite('ma431_08', 1)
    Voiceline('ma253')
    if SLOT_XDistanceFromFowardCorner <= 200000:
        SLOT_XDistanceFromCenterOfStage = 1750000
    RefreshMultihit()
    Damage(2200)
    PushbackX(30400)
    HitAirUnblockable(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(1500)
    AirPushbackY(-160000)
    YImpulseBeforeWallbounce(2000)
    HardKnockdown(50)
    MoveAttributes(1, 0, 0, 0, 0)
    DefeatOpponentBehavior(0)
    ForceFaceSprite()
    if SLOT_51:
        Hitstop(0)
    physicsYImpulse(-150000)
    setGravity(20000)

    def upon_OPPONENT_HIT():
        CommonSE('025_cleanhit_slash')
        physicsYImpulse(-80000)
        setGravity(10000)
    sprite('ma431_08', 4)
    CreateObject('maef431_fall', -1)
    PrivateSE('mase_08')
    PrivateSE('mase_08')
    label(0)
    sprite('ma431_09', 4)
    sprite('ma431_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma431_10', 15)
    CameraFollowTarget(0, 0)
    CameraLookAtEnemy(0)
    DespawnEAEffect('maef431_fall')
    CreateObject('maef431_crash', -1)
    EnableRapidCancel(1)
    EndMomentum(1)
    setInvincible(0)
    LandingEffects(100, 1, 1)
    sprite('ma431_11', 5)
    sprite('ma431_12', 3)
    ForceFaceSprite()
    sprite('ma431_13', 3)
    sprite('ma402_02', 4)
    physicsXImpulse(-8000)
    physicsYImpulse(28000)
    setGravity(1800)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 99)
    sprite('ma402_03', 3)
    sprite('ma402_04', 3)
    sprite('ma402_05', 3)
    sprite('ma402_06', 3)
    sprite('ma402_07', 3)
    sprite('ma020_04', 3)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(1)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('ma024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('ma024_01', 2)
    sprite('ma024_02', 2)
    sprite('ma024_03', 2)
    sprite('ma024_04', 2)


@State
def UltimateJumpOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        AttackP2(84)
        SingleProration(1)
        MinimumDamage(20)
        StarterRating(2)
        PushbackX(8000)
        EnemyHitstopAddition(0, -5, -5)
        HitAirUnblockable(3)
        AirUntechableTime(100)
        HardKnockdown(1)
        AirPushbackX(-1000)
        AirPushbackY(60000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AttackDirection(0)
        UseSlashHitspark(1)
        AttackType(4)
        PassByArmor(1)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
            EndYPhysicsImpulse()

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SLOT_51 = 1
            NoDamageAction(1)
            CameraFollowTarget(22, 22)
            CameraLookAtEnemy(1)
            sendToLabel(10)
        uponSendToLabel(LANDING, 99)
    sprite('ma431_00', 3)
    sprite('ma431_01', 3)
    setInvincible(1)
    DistortionSettings(25, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', -1)
    Voiceline('ma252')
    sprite('ma431_02', 3)
    EndMomentum(1)
    sprite('ma431_03', 15)
    CreateObject('maef431', -1)
    sprite('ma431_04', 3)
    CreateObject('maef431_jump_od', -1)
    sprite('ma431_05', 3)
    sprite('ma431_06ex01', 1)
    JumpEffects(1, 0)
    sprite('ma431_06', 3)
    clearUponHandler(OPPONENT_HIT)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(10000)
    YImpulseBeforeWallbounce(10)
    EnemyHitstopAddition(0, 0, 8)
    Hitstop(6)
    EnableRapidCancel(0)
    physicsXImpulse(0)
    physicsYImpulse(120000)
    setGravity(-10000)

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor >= 2600000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            AbsoluteY(2600000)
            sendToLabel(11)
    sprite('ma431_07', 4)
    CameraFollowTarget(22, 22)
    SetXCollisionFromOrigin(10)
    label(5)
    sprite('ma431_06', 3)
    sprite('ma431_07', 3)
    loopRest()
    gotoLabel(5)
    label(10)
    sprite('ma431_07', 2)
    RefreshMultihit()
    DistanceCheck(-1, -1, -1, -1)
    Damage(300)
    Hitstop(3)
    EnemyHitstopAddition(0, -2, -2)
    AttackDirection(1)
    AirPushbackY(40000)
    YImpulseBeforeWallbounce(10)
    DefeatOpponentBehavior(1)
    physicsXImpulse(0)
    physicsYImpulse(80000)
    setGravity(0)
    SetXCollisionFromOrigin(10)
    EnableRapidCancel(0)
    sprite('ma431_06', 2)
    RefreshMultihit()
    sprite('ma431_07', 2)
    RefreshMultihit()
    sprite('ma431_06', 2)
    RefreshMultihit()
    sprite('ma431_07', 2)
    RefreshMultihit()
    sprite('ma431_06', 2)
    RefreshMultihit()
    sprite('ma431_07', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(1000)
    YImpulseBeforeWallbounce(10)
    EnemyHitstopAddition(0, 0, 8)
    Hitstop(6)
    sprite('ma431_06', 3)

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor >= 2600000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            AbsoluteY(2600000)
            sendToLabel(11)
    loopRest()
    gotoLabel(5)
    label(11)
    sprite('null', 10)
    clearUponHandler(EVERY_FRAME)
    SpriteCall('null', 20, 2, 51)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 9)
    DespawnEAEffect('maef431_jump_od')
    SetXCollisionFromOrigin(-1)
    if SLOT_51:
        TeleportToObject(22)
        AddY(800000)
    CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
    AddX(-5000)
    sprite('ma431_08', 1)
    Voiceline('ma253')
    if SLOT_XDistanceFromFowardCorner <= 200000:
        SLOT_XDistanceFromCenterOfStage = 1750000
    RefreshMultihit()
    Damage(2200)
    PushbackX(30400)
    HitAirUnblockable(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(1500)
    AirPushbackY(-160000)
    YImpulseBeforeWallbounce(2000)
    HardKnockdown(50)
    MoveAttributes(1, 0, 0, 0, 0)
    DefeatOpponentBehavior(0)
    ForceFaceSprite()
    if SLOT_51:
        Hitstop(0)
    physicsYImpulse(-150000)
    setGravity(20000)

    def upon_OPPONENT_HIT():
        CommonSE('025_cleanhit_slash')
        physicsYImpulse(-80000)
        setGravity(10000)
    sprite('ma431_08', 4)
    CreateObject('maef431_fall_od', -1)
    PrivateSE('mase_08')
    PrivateSE('mase_08')
    label(0)
    sprite('ma431_09', 4)
    sprite('ma431_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma431_10', 15)
    CameraFollowTarget(0, 0)
    CameraLookAtEnemy(0)
    DespawnEAEffect('maef431_fall_od')
    CreateObject('maef431_crash_od', -1)
    EnableRapidCancel(1)
    EndMomentum(1)
    setInvincible(0)
    LandingEffects(100, 1, 1)
    sprite('ma431_11', 5)
    sprite('ma431_12', 3)
    ForceFaceSprite()
    sprite('ma431_13', 3)
    sprite('ma402_02', 4)
    physicsXImpulse(-8000)
    physicsYImpulse(28000)
    setGravity(1800)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 99)
    sprite('ma402_03', 3)
    sprite('ma402_04', 3)
    sprite('ma402_05', 3)
    sprite('ma402_06', 3)
    sprite('ma402_07', 3)
    sprite('ma020_04', 3)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(1)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('ma024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('ma024_01', 2)
    sprite('ma024_02', 2)
    sprite('ma024_03', 2)
    sprite('ma024_04', 2)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1500)
        AttackP1(60)
        MinimumDamage(30)
        AirUntechableTime(60)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Floorslide(10)
        AirPushbackX(60000)
        AirPushbackY(12000)
        EnemyHitstopAddition(10, 10, 18)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        Wallstick(1)
        WallstickDuration(25)
        HardKnockdown(1)
        UseSlashHitspark(1)
        StarterRating(0)
        AbsoluteY(0)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)
        GuardpointHitstop(-1, -1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ma430_00', 3)
    sprite('ma430_01', 3)
    CreateObject('maef430_hold', -1)
    CreateObject('maef430_hold_yari_dust', -1)
    PrivateSE('mase_09')
    sprite('ma430_02', 3)
    sprite('ma430_02', 1)
    SetActionMark(4)
    uponSendToLabel(RELEASE_D, 0)
    loopRest()
    label(10)
    sprite('ma430_03', 5)
    CreateObject('maef430_hold_yari', 0)
    CreateObject('maef430_hold_yari_aura', 0)
    PerInertia(60)
    AddActionMark(-1)
    Damage(2000)
    sprite('ma430_04', 5)
    PerInertia(60)
    sprite('ma430_05', 5)
    PerInertia(60)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(10)
    label(0)
    sprite('ma430_06', 3)
    TriggerUponForState('maef430_hold', 32)
    DespawnEAEffect('maef430_hold_yari')
    DespawnEAEffect('maef430_hold_yari_aura')
    DespawnEAEffect('maef430_hold_yari_dust')
    clearUponHandler(RELEASE_D)
    DistortionSettings(40, -1, 0)
    CreateObject('EMB', -1)
    HeatChange(-5000)
    Voiceline('ma250')
    PerInertia(50)
    GuardPoint_(0)
    SpecificInvincibility(1, 1, 1, 1, 1)
    if not SLOT_2:
        Damage(3000)
    uponSendToLabel(LANDING, 9)
    sprite('ma430_07', 3)
    sprite('ma430_08', 3)
    sprite('ma402_01ex01', 2)
    CreateObject('maef430_ex', 0)
    CreateObject('maef430_ex', 1)
    EndMomentum(1)
    sprite('ma402_02ex01', 4)
    CreateObject('maef430_ex', 0)
    CreateObject('maef430_ex', 1)
    physicsXImpulse(-12000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('ma402_03ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_04ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_05ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_06ex01', 4)
    sprite('ma430_09', 40)
    label(9)
    sprite('ma430_10', 2)
    XImpulseAcceleration(30)
    CreateObject('maef430', -1)
    sprite('ma430_11', 2)
    CreateObject('maef430_lance', -1)
    sprite('ma430_12', 2)
    sprite('ma430_13', 2)
    EndMomentum(1)
    sprite('ma430_14', 2)
    sprite('ma430_15', 2)
    DespawnEAEffect('maef430')
    PrivateSE('mase_07')
    PrivateSE('mase_07')
    sprite('ma430_16', 2)
    SetXCollisionFromOrigin(150)
    physicsXImpulse(120000)
    sprite('ma430_17', 2)
    Voiceline('ma251')
    CreateObject('maef430_strike', -1)
    CreateObject('maef430_bg', -1)
    XImpulseAcceleration(0)
    sprite('ma430_18', 3)
    sprite('ma430_19', 3)
    sprite('ma430_20', 3)
    setInvincible(0)
    AttackOff()
    sprite('ma430_18', 3)
    sprite('ma430_19', 3)
    sprite('ma430_20', 3)
    sprite('ma430_21', 4)
    sprite('ma430_22', 4)
    SetXCollisionFromOrigin(-1)
    sprite('ma001_03', 4)
    CreateObject('maef_001_zanzou', -1)
    CommonSE('008_swing_pole_2')
    sprite('ma001_04', 4)
    sprite('ma001_05', 4)
    sprite('ma001_06', 4)
    sprite('ma001_07', 4)
    CreateObject('maef_001_zanzou2', -1)
    CommonSE('008_swing_pole_2')
    sprite('ma001_08', 4)
    sprite('ma001_09', 3)
    sprite('ma001_10', 2)


@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1800)
        AttackP1(60)
        MinimumDamage(30)
        AirUntechableTime(60)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Floorslide(10)
        AirPushbackX(60000)
        AirPushbackY(12000)
        EnemyHitstopAddition(10, 10, 18)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        Wallstick(1)
        WallstickDuration(25)
        HardKnockdown(1)
        UseSlashHitspark(1)
        StarterRating(0)
        AttackType(4)

        def upon_OPPONENT_HIT():
            CreateObject('maef430_od', -1)
        AbsoluteY(0)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)
        GuardpointHitstop(-1, -1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ma430_00', 3)
    sprite('ma430_01', 3)
    CreateObject('maef430_hold', -1)
    CreateObject('maef430_hold_yari_dust', -1)
    PrivateSE('mase_09')
    sprite('ma430_02', 3)
    sprite('ma430_02', 1)
    SetActionMark(4)
    uponSendToLabel(RELEASE_D, 0)
    loopRest()
    label(10)
    sprite('ma430_03', 5)
    CreateObject('maef430_hold_yari', 0)
    CreateObject('maef430_hold_yari_aura', 0)
    PerInertia(60)
    AddActionMark(-1)
    Damage(2400)
    sprite('ma430_04', 5)
    PerInertia(60)
    sprite('ma430_05', 5)
    PerInertia(60)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(10)
    label(0)
    sprite('ma430_06', 3)
    TriggerUponForState('maef430_hold', 32)
    DespawnEAEffect('maef430_hold_yari')
    DespawnEAEffect('maef430_hold_yari_aura')
    DespawnEAEffect('maef430_hold_yari_dust')
    clearUponHandler(RELEASE_D)
    DistortionSettings(40, -1, 0)
    CreateObject('EMB', -1)
    HeatChange(-5000)
    Voiceline('ma250')
    PerInertia(50)
    GuardPoint_(0)
    SpecificInvincibility(1, 1, 1, 1, 1)
    if not SLOT_2:
        Damage(3600)
    uponSendToLabel(LANDING, 9)
    sprite('ma430_07', 3)
    sprite('ma430_08', 3)
    sprite('ma402_01ex01', 2)
    CreateObject('maef430_ex', 0)
    EndMomentum(1)
    sprite('ma402_02ex01', 4)
    CreateObject('maef430_ex', 0)
    CreateObject('maef430_ex', 1)
    physicsXImpulse(-12000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('ma402_03ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_04ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_05ex01', 4)
    CreateObject('maef430_ex', 0)
    sprite('ma402_06ex01', 4)
    sprite('ma430_09', 40)
    label(9)
    sprite('ma430_10', 2)
    XImpulseAcceleration(30)
    CreateObject('maef430', -1)
    sprite('ma430_11', 2)
    CreateObject('maef430_lance', -1)
    sprite('ma430_12', 2)
    sprite('ma430_13', 2)
    EndMomentum(1)
    sprite('ma430_14', 2)
    sprite('ma430_15', 2)
    DespawnEAEffect('maef430')
    PrivateSE('mase_07')
    PrivateSE('mase_07')
    sprite('ma430_16', 2)
    SetXCollisionFromOrigin(150)
    physicsXImpulse(120000)
    PreDashEffects(100, 1, 1)
    sprite('ma430_17', 2)
    Voiceline('ma251')
    CreateObject('maef430_strike', -1)
    CreateObject('maef430_bg', -1)
    ScreenShake(16000, 16000)
    XImpulseAcceleration(0)
    AltKnockdownEffects(100, 1, 1)
    sprite('ma430_18', 3)
    SkidEffects(100, 1, 1)
    sprite('ma430_19', 3)
    sprite('ma430_20', 3)
    setInvincible(0)
    AttackOff()
    sprite('ma430_18', 3)
    sprite('ma430_19', 3)
    sprite('ma430_20', 3)
    sprite('ma430_21', 4)
    sprite('ma430_22', 4)
    SetXCollisionFromOrigin(-1)
    sprite('ma001_03', 4)
    CreateObject('maef_001_zanzou', -1)
    CommonSE('008_swing_pole_2')
    sprite('ma001_04', 4)
    sprite('ma001_05', 4)
    sprite('ma001_06', 4)
    sprite('ma001_07', 4)
    CreateObject('maef_001_zanzou2', -1)
    CommonSE('008_swing_pole_2')
    sprite('ma001_08', 4)
    sprite('ma001_09', 3)
    sprite('ma001_10', 2)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(0)
        MinimumDamage(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 200000, 0)
        UseSlashHitspark(1)
        DefeatOpponentBehavior(1)
        EnemyHitstopAddition(20, 0, 0)
        DamageFromStateOnly('AstralHeatExe')
        EnterStateIfEventID(12, 'AstralHeatExe')
        setInvincible(1)
    sprite('ma450_00', 3)
    sprite('ma450_01', 3)
    sprite('ma450_02', 3)
    Voiceline('ma290')
    if SLOT_43:
        Mouth(14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885,
            12337, 14179, 12897, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Mouth(14177, 14179, 12641, 25396, 13361, 14177, 14179, 14177, 14179,
            14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    DistortionSettings(105, -1, 2)
    CreateObject('EMB_MA_AH', -1)
    EmptyHeat()
    CreateObject('maef450', -1)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_02', 3)
    sprite('ma450_03', 3)
    sprite('ma450_04', 3)
    sprite('ma450_05', 4)
    sprite('ma450_06', 3)
    sprite('ma450_06', 1)
    CommonSE('006_swing_blade_2')
    sprite('ma450_07', 3)
    sprite('ma450_08', 3)
    AddX(50000)
    sprite('ma450_09', 3)
    CreateObject('maef450_slash', -1)
    sprite('ma450_10', 3)
    setInvincible(0)
    sprite('ma450_11', 3)
    sprite('ma450_12', 3)
    sprite('ma450_10', 3)
    sprite('ma450_11', 3)
    sprite('ma450_12', 3)
    sprite('ma450_10', 3)
    sprite('ma450_11', 3)
    sprite('ma450_12', 3)
    sprite('ma450_36', 4)
    sprite('ma450_37', 4)
    sprite('ma001_01', 4)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 4)
    sprite('ma001_03', 4)
    sprite('ma001_04', 4)
    sprite('ma001_05', 4)
    sprite('ma001_06', 4)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 4)
    sprite('ma001_08', 4)
    sprite('ma001_09', 4)
    sprite('ma001_10', 4)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(2000)
        MinimumDamage(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(9999)
        UseSlashHitspark(1)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeatExe')
        HitAnywhere(1)
        HUDVisibillity(1)
        AstralHeatCleanup(1, 1)
        PlayPlayAstralBGM(0)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraControlEnable(1)
    sprite('ma450_10', 3)
    sprite('ma450_11', 3)
    sprite('ma450_12', 3)
    sprite('ma450_10', 3)
    sprite('ma450_11', 3)
    sprite('ma450_12', 3)
    sprite('ma450_10', 4)
    Voiceline('ma291')
    sprite('ma450_11', 4)
    sprite('ma450_12', 4)
    sprite('ma450_13', 4)
    sprite('ma450_14', 4)
    sprite('ma450_15', 4)
    sprite('ma450_16', 4)
    sprite('ma450_17', 4)
    sprite('ma450_18', 3)
    physicsXImpulse(2000)
    sprite('ma450_19', 3)
    XImpulseAcceleration(200)
    sprite('ma450_20', 3)
    XImpulseAcceleration(200)
    CommonSE('006_swing_blade_2')
    sprite('ma450_21', 3)
    XImpulseAcceleration(80)
    sprite('ma450_22', 3)
    physicsXImpulse(50000)
    sprite('ma450_23', 3)
    Voiceline('ma292')
    RefreshMultihit()
    EndMomentum(1)
    CreateObject('maef450_upper', -1)
    sprite('ma450_24', 3)
    sprite('ma450_25', 3)
    sprite('ma450_26', 3)
    sprite('ma450_27', 4)
    sprite('ma450_28', 4)
    sprite('ma530_07', 4)
    AddX(-100000)
    sprite('ma530_08', 4)
    sprite('ma530_09', 4)
    AddX(-40000)
    sprite('ma530_10', 4)
    EndMomentum(1)
    sprite('ma530_11', 4)
    sprite('ma000_00', 3)
    sprite('ma023_00', 4)
    sprite('ma023_01', 4)
    sprite('ma020_00', 4)
    JumpEffects(1, 0)
    physicsYImpulse(90000)
    CameraControlEnable(0)
    CreateObject('AstralCamera', -1)
    sprite('ma020_01', 4)

    def RunOnObject_22():
        Visibility(1)
        XPositionRelativeFacing(0)
        AbsoluteY(6000000)
        setGravity(0)
    sprite('ma020_00', 4)
    sprite('ma020_01', 4)
    sprite('null', 30)
    TriggerUponForState('AstralCamera', 33)
    sprite('null', 20)
    EndMomentum(1)
    XPositionRelativeFacing(0)
    AbsoluteY(1400000)
    TriggerUponForState('AstralCamera', 34)
    sprite('ma450_29', 3)
    SetScaleSpeed(-1)
    physicsYImpulse(200)
    CreateObject('maef450_charge', 0)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    Voiceline('ma293')
    if SLOT_43:
        Mouth(14177, 12643, 24880, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Mouth(14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    SetScaleSpeed(0)
    physicsYImpulse(0)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    if SLOT_43:
        Voiceline('ma294')
        Mouth(14177, 14179, 14177, 14179, 12641, 25396, 13361, 13153, 25397,
            55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    if SLOT_44:
        Voiceline('ma294')
        Mouth(14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_29', 3)
    sprite('ma450_30', 3)
    sprite('ma450_31', 3)
    sprite('ma450_32', 3)
    sprite('ma450_32ex', 3)
    CreateObject('maef450_throw', 0)
    DespawnEAEffect('maef450_charge')
    PrivateSE('mase_07')
    PrivateSE('mase_08')
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    TriggerUponForState('AstralCamera', 35)
    DespawnEAEffect('maef450_throw')
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    ConstantAlphaModifier(-36)
    sprite('ma450_33', 3)
    sprite('ma450_33ex', 3)
    sprite('ma450_33', 3)
    sprite('null', 33)
    sprite('null', 285)
    TriggerUponForState('AstralCamera', 36)
    sprite('null', 30)
    TriggerUponForState('AstralCamera', 37)
    sprite('ma450_23', 60)
    Visibility(1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(22000)
    MinimumDamage(100)
    AirPushbackX(0)
    AirPushbackY(100000)
    YImpulseBeforeWallbounce(0)
    Hitstop(0)
    AirUntechableTime(9999)
    DefeatOpponentBehavior(3)
    DamageEffect(9, '')
    SetBackground(0)
    sprite('null', 60)
    Visibility(0)
    sprite('null', 40)
    CameraControlEnable(0)
    CreateObject('ma450yari_dummy', -1)
    sprite('ma450_38', 3)
    uponSendToLabel(LANDING, 99)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    AbsoluteY(800000)
    AddX(-180000)
    EndYPhysicsImpulse()
    sprite('ma450_39', 3)
    label(0)
    sprite('ma450_40', 4)
    sprite('ma450_41', 4)
    gotoLabel(0)
    label(99)
    sprite('ma450_42', 3)
    CommonSE('204_runjump_normal_1')
    sprite('ma450_43', 3)
    sprite('ma450_44', 3)
    sprite('ma450_45', 3)
    sprite('ma450_46', 3)
    sprite('ma450_47', 3)
    sprite('ma450_34', 4)
    AddX(180000)
    DespawnEAEffect('ma450yari_dummy')
    sprite('ma450_35', 4)
    sprite('ma601_05', 6)
    CommonSE('024_getset_b')
    sprite('ma601_06', 6)
    sprite('ma601_07', 6)
    sprite('ma601_08', 15)
    sprite('ma601_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('ma601_10', 6)
    sprite('ma601_11', 8)
    sprite('ma601_12', 8)
    sprite('ma601_13', 6)
    sprite('ma601_14', 6)
    sprite('ma000_00', 8)
    WinAction()
    sprite('ma610_00', 7)
    sprite('ma610_01', 8)
    sprite('ma610_02', 12)
    sprite('ma610_03', 6)
    sprite('ma610_04', 12)
    sprite('ma610_05', 6)
    sprite('ma610_06', 6)
    Voiceline('ma406')
    DemoEndOnVoiceEnd(1)
    sprite('ma610_06', 32767)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('ma054')
    sprite('ma900_00', 32767)
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
    sprite('ma901_00', 50)
    physicsYImpulse(-150)
    sprite('ma901_00', 50)
    physicsYImpulse(150)
    Voiceline('ma055')
    label(0)
    sprite('ma901_00', 50)
    physicsYImpulse(-150)
    sprite('ma901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 400000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            PushbackX(19800)
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
    sprite('ma312_00ex01', 6)
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('ma312_01ex01', 7)
    sprite('ma312_02ex01', 3)
    CommonSE('006_swing_blade_2')
    sprite('ma312_02ex01', 3)
    sprite('ma312_03ex01', 3)
    Voiceline('ma280')
    CreateObject('maef_440', -1)
    sprite('ma312_03ex01', 5)
    AttackOff()
    setInvincible(0)
    sprite('ma312_04ex01', 8)
    sprite('ma312_05ex01', 7)
    sprite('ma312_06ex01', 7)
    sprite('ma312_07ex01', 7)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 400000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            PushbackX(19800)
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
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('ma312_00ex01', 3)
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('ma312_01ex01', 3)
    sprite('ma312_02ex01', 3)
    CommonSE('006_swing_blade_2')
    sprite('ma312_03ex01', 3)
    Voiceline('ma280')
    CreateObject('maef_440', -1)
    sprite('ma312_03ex01', 5)
    AttackOff()
    setInvincible(0)
    sprite('ma312_04ex01', 8)
    sprite('ma312_05ex01', 7)
    sprite('ma312_06ex01', 7)
    sprite('ma312_07ex01', 7)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(5)
        Damage(200)
        AttackP2(100)
        Hitstun(30)
        AirUntechableTime(100)
        PushbackX(3000)
        Hitstop(1)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        DefeatOpponentBehavior(1)
        HitsparkSize(750)
        HitAnywhere(1)
        MinimumDamage(10)
        SetBackground(1)
        CreateObject('BurstDD_Camera', -1)

        def upon_STATE_END():
            DespawnEAEffect('BurstDD_Camera')
    sprite('ma440_00', 6)
    sprite('ma440_01', 6)
    EndMomentum(1)
    AddX(59000)
    sprite('ma440_02', 6)
    sprite('ma440_03', 3)
    HitBackReturnIgnore(1)
    Voiceline('ma281')
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash1', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_04', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash2', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash3', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_06', 3)
    RefreshMultihit()
    sprite('ma440_07', 3)
    sprite('ma440_08', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash4', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_09', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash5', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash1', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_04', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash2', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash3', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_06', 3)
    RefreshMultihit()
    sprite('ma440_07', 3)
    sprite('ma440_08', 2)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash4', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_08', 1)
    if SLOT_51:
        conditionalSendToLabel(100)
    sprite('ma440_09', 3)
    RefreshMultihit()
    Damage(200)
    DefeatOpponentBehavior(0)
    EnemyHitstopAddition(10, 10, 10)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(40000)
    CreateObject('maef_440_slash5', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_10', 4)
    sprite('ma440_11', 8)
    sprite('ma440_12', 4)
    DespawnEAEffect('BurstDD_Camera')
    sprite('ma440_13', 4)
    sprite('ma501_08', 5)
    CommonSE('008_swing_pole_2')
    AddX(-20000)
    sprite('ma501_09', 5)
    sprite('ma501_10', 5)
    sprite('ma501_11', 5)
    sprite('ma501_12', 5)
    loopRest()
    ExitState()
    label(100)
    sprite('ma440_09', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    CreateObject('maef_440_slash5', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_03', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash1', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_04', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash2', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_05', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash3', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_06', 3)
    RefreshMultihit()
    sprite('ma440_07', 3)
    sprite('ma440_08', 3)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    CreateObject('maef_440_slash4', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_09', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    EnemyHitstopAddition(10, 10, 10)
    PushbackX(30400)
    HitBackReturnIgnore(0)
    CreateObject('maef_440_slash5', -1)
    if SLOT_51:
        ScreenShake(10000, 10000)
    sprite('ma440_10', 6)
    sprite('ma440_14', 8)
    sprite('ma440_15', 8)
    CommonSE('006_swing_blade_2')
    sprite('ma440_16', 8)
    sprite('ma440_17', 4)
    StartMultihit()
    physicsXImpulse(140000)
    sprite('ma440_17', 1)
    Voiceline('ma282')
    XImpulseAcceleration(50)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    AttackLevel_(5)
    Damage(1700)
    Hitstop(15)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(40000)
    HitsparkSize(1000)
    CommonSE('025_cleanhit_slash')
    CreateObject('maef_440_finish', -1)
    CreateObject('maef_440_finish2', -1)
    if SLOT_51:
        ScreenShake(32000, 32000)
    sprite('ma440_17', 3)
    EndMomentum(1)
    sprite('ma440_18', 5)
    sprite('ma440_19', 5)
    sprite('ma440_20', 5)
    sprite('ma440_21', 5)
    sprite('ma440_22', 5)
    sprite('ma440_23', 5)
    DespawnEAEffect('BurstDD_Camera')
    sprite('ma503_09', 5)
    AddX(-30000)
    CommonSE('008_swing_pole_2')
    sprite('ma503_10', 5)
    sprite('ma503_11', 5)


@Subroutine
def MouthTableInit():
    Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma055', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma400', 12897, 25392, 13620, 14177, 14179, 14177, 14179, 
        14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 12899, 24885, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma404', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma406', 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma407', 14177, 13155, 24880, 25399, 24887, 25399, 24887, 
        25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma408', 13665, 13667, 13665, 12643, 24888, 25398, 24886, 
        25398, 24886, 25398, 24886, 25398, 24886, 12849, 13923, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma411', 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma412', 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma413', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma414', 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma415', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ma416', 14177, 13155, 24880, 25399, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ma055', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ma400', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 12641, 25394, 12850, 13921, 13923, 13921, 13923, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 12641, 25394, 12339, 14177, 14179, 14177, 14179, 
            14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 
            25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma405', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma406', 14177, 13667, 13921, 13923, 13921, 13923, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma407', 14177, 12643, 24888, 25399, 24887, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma408', 14177, 12643, 24888, 25398, 24886, 25398, 
            24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma411', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma412', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma413', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma414', 14177, 14179, 14177, 14179, 14177, 14179, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma415', 13921, 13923, 13921, 13923, 13921, 13923, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ma416', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('no'):
            Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ma400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma401', 13921, 13923, 13921, 13923, 13921, 13923,
                12641, 25397, 13619, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ma400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 
                24887, 25398, 24886, 25398, 24886, 25401, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 13155,
                24885, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mu'):
            Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ma400', 14177, 14179, 14177, 13667, 24886, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 25399, 24887, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ma400', 14177, 14179, 14177, 14179, 14177, 13155,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('iz'):
            Unknown18011('ma000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ma400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('ma502', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma503', 12641, 25394, 12342, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('ma504', 12643, 12337, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma505', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 
                12338, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('ma524', 12641, 25396, 24887, 13361, 13923, 24880,
                25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma525', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mu'):
            Unknown18011('ma528', 14177, 13155, 24885, 25399, 24887, 25399,
                24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 
                12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('ma529', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 12641, 25396, 13620, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('ma530', 14177, 13155, 24885, 25399, 24887, 25399,
                24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 
                12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma531', 14435, 24880, 25399, 24887, 25399, 24887,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('iz'):
            Unknown18011('ma538', 14177, 14179, 14177, 14435, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma539', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 12641, 25396, 13875, 14177, 14179, 14177, 
                12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 
                12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('ma546', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 12643, 12336, 14177, 14179, 14177, 
                14179, 14177, 14179, 13921, 13923, 13921, 12899, 24880, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ma547', 14177, 14179, 14177, 14179, 14177, 14179,
                12641, 25394, 13619, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(120)
    if CharacterIDCheck('tb'):
        SyncEntry()
        gotoLabel(220)
    if CharacterIDCheck('mu'):
        SyncEntry()
        gotoLabel(240)
    if CharacterIDCheck('mk'):
        SyncEntry()
        gotoLabel(250)
    if CharacterIDCheck('iz'):
        SyncEntry()
        gotoLabel(290)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(1)
    if random_(2, 0, 50):
        conditionalSendToLabel(2)
    label(0)
    sprite('ma600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('ma600_00', 10)
    sprite('ma600_00', 60)
    Voiceline('ma414')
    sprite('ma600_01', 6)
    sprite('ma600_02', 6)
    sprite('ma600_03', 6)
    CommonSE('019_cloth_c')
    sprite('ma600_04', 6)
    sprite('ma600_05', 6)
    sprite('ma600_06', 7)
    CommonSE('019_cloth_c')
    sprite('ma600_07', 7)
    sprite('ma600_08', 7)
    sprite('ma600_09', 6)
    CreateObject('maef_600', -1)
    sprite('ma600_10', 7)
    sprite('ma600_11', 6)
    sprite('ma600_12', 6)
    sprite('ma600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('ma600_14', 6)
    Voiceline('ma415')
    sprite('ma501_10', 6)
    sprite('ma501_11', 6)
    sprite('ma501_12', 6)
    DemoTimer(90)
    loopRest()
    ExitState()
    label(1)
    sprite('ma601_00', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('ma601_00', 10)
    sprite('ma601_00', 30)
    Voiceline('ma412')
    SpriteIfNot0(50, 2, 44)
    sprite('ma601_00', 40)
    CreateObject('maef_601', -1)
    sprite('ma601_01', 6)
    DespawnEAEffect('maef_601')
    CreateParticle('maef_601smoke', -1)
    ScreenShake(10000, 10000)
    PrivateSE('mase_04')
    sprite('ma601_02', 6)
    sprite('ma601_03', 6)
    sprite('ma601_04', 6)
    sprite('ma601_05', 7)
    sprite('ma601_06', 7)
    sprite('ma601_07', 7)
    sprite('ma601_08', 7)
    sprite('ma601_09', 5)
    CommonSE('008_swing_pole_2')
    sprite('ma601_10', 7)
    sprite('ma601_11', 7)
    Voiceline('ma413')
    sprite('ma601_12', 7)
    sprite('ma601_13', 7)
    sprite('ma601_14', 7)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(2)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_01', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_01', 7)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_03', 7)
    sprite('ma602_04', 7)
    sprite('ma602_05', 7)
    sprite('ma602_06', 7)
    sprite('ma602_07', 5)
    sprite('ma602_08', 40)
    Voiceline('ma416')
    sprite('ma602_09', 6)
    sprite('ma602_10', 6)
    sprite('ma602_11', 6)
    sprite('ma602_12', 6)
    sprite('ma602_13', 10)
    sprite('ma602_12', 6)
    sprite('ma602_11', 6)
    sprite('ma602_10', 6)
    sprite('ma602_09', 6)
    sprite('ma602_08', 30)
    sprite('ma602_14', 6)
    sprite('ma203_14', 6)
    sprite('ma203_15', 6)
    sprite('ma203_16', 6)
    sprite('ma203_17', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(110)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_01', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(110)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_01', 7)
    sprite('ma602_00', 7)
    sprite('ma602_01', 7)
    sprite('ma602_02', 7)
    sprite('ma602_03', 7)
    sprite('ma602_04', 7)
    sprite('ma602_05', 7)
    sprite('ma602_06', 7)
    sprite('ma602_07', 5)
    sprite('ma602_08', 10)
    sprite('ma602_08', 30)
    Voiceline('ma502')
    sprite('ma602_09', 6)
    sprite('ma602_10', 6)
    sprite('ma602_11', 6)
    sprite('ma602_12', 6)
    sprite('ma602_13', 10)
    sprite('ma602_12', 6)
    sprite('ma602_11', 6)
    sprite('ma602_10', 6)
    sprite('ma602_09', 6)
    sprite('ma602_08', 30)
    sprite('ma602_14', 6)
    sprite('ma203_14', 6)
    ObjectUpon(22, 32)
    sprite('ma203_15', 6)
    sprite('ma203_16', 6)
    sprite('ma203_17', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(120)
    sprite('ma602_00', 2)

    def upon_32():
        SetActionMark(1)
    label(121)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(121)
    label(122)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    Voiceline('ma504')
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(9)
    label(123)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(123)
    sprite('ma602_03', 7)
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(220)
    sprite('ma602_00', 2)

    def upon_32():
        SetActionMark(1)
    label(221)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(221)
    label(222)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    Voiceline('ma524')
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(7)
    label(223)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(223)
    sprite('ma602_03', 7)
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(240)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(240)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    Voiceline('ma528')
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(5)
    label(241)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(241)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    ObjectUpon(22, 32)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(6)
    label(242)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(242)
    sprite('ma602_03', 7)
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(250)
    sprite('ma602_00', 2)

    def upon_32():
        SetActionMark(1)
    label(251)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(251)
    label(252)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    Voiceline('ma530')
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(9)
    label(253)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(253)
    sprite('ma602_03', 7)
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(290)
    sprite('ma601_00', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(290)
    sprite('ma601_00', 90)
    sprite('ma601_00', 320)
    Voiceline('ma538')
    sprite('ma601_00', 40)
    CreateObject('maef_601', -1)
    sprite('ma601_01', 6)
    DespawnEAEffect('maef_601')
    CreateParticle('maef_601smoke', -1)
    ScreenShake(10000, 10000)
    PrivateSE('mase_04')
    sprite('ma601_02', 6)
    sprite('ma601_03', 6)
    sprite('ma601_04', 6)
    sprite('ma601_05', 7)
    sprite('ma601_06', 7)
    sprite('ma601_07', 7)
    sprite('ma601_08', 7)
    sprite('ma601_09', 5)
    CommonSE('008_swing_pole_2')
    sprite('ma601_10', 7)
    sprite('ma601_11', 7)
    ObjectUpon(22, 32)
    sprite('ma601_12', 7)
    sprite('ma601_13', 7)
    sprite('ma601_14', 7)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(330)
    sprite('ma602_00', 2)

    def upon_32():
        SetActionMark(1)
    label(331)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(331)
    label(332)
    sprite('ma602_00', 8)
    sprite('ma602_01', 8)
    Voiceline('ma546')
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    SetActionMark(10)
    label(333)
    sprite('ma602_00', 8)
    AddActionMark(-1)
    sprite('ma602_01', 8)
    sprite('ma602_02', 8)
    sprite('ma602_01', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(333)
    sprite('ma602_03', 7)
    sprite('ma001_01', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_02', 7)
    sprite('ma001_03', 7)
    CreateObject('maef_001_zanzou', -1)
    sprite('ma001_04', 7)
    sprite('ma001_05', 7)
    sprite('ma001_06', 7)
    CommonSE('008_swing_pole_2')
    sprite('ma001_07', 7)
    CreateObject('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    DemoTimer(30)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('ma000_00', 7)
    sprite('ma615_00', 6)
    sprite('ma615_01', 6)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    RandomVoiceline('ma400', 100, 'ma401', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    label(0)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    loopRest()
    gotoLabel(0)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(120)
    if CharacterIDCheck('tb'):
        conditionalSendToLabel(220)
    if CharacterIDCheck('mu'):
        conditionalSendToLabel(240)
    if CharacterIDCheck('mk'):
        conditionalSendToLabel(250)
    if CharacterIDCheck('iz'):
        conditionalSendToLabel(290)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if not SLOT_123:
        if not SLOT_109:
            if random_(2, 0, 50):
                conditionalSendToLabel(1)
    sprite('ma610_00', 7)
    sprite('ma610_01', 8)
    sprite('ma610_02', 12)
    sprite('ma610_03', 6)
    sprite('ma610_04', 12)
    sprite('ma610_05', 6)
    sprite('ma610_06', 6)
    Voiceline('ma406')
    DemoEndOnVoiceEnd(1)
    sprite('ma610_06', 32767)
    label(1)
    sprite('ma611_00', 5)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraNoScreenCollision(1)
    Voiceline('ma407')
    sprite('ma611_01', 5)
    sprite('ma611_02', 5)
    sprite('ma611_03', 10)
    sprite('ma611_04', 5)
    AddX(-40000)
    sprite('ma611_05', 5)
    AddX(-40000)
    sprite('ma602_08', 80)
    SpriteIfNot0(30, 2, 44)
    AddX(-10000)
    sprite('ma602_09', 3)
    sprite('ma602_10', 3)
    sprite('ma602_11', 3)
    sprite('ma602_12', 3)
    sprite('ma602_13', 6)
    sprite('ma602_12', 3)
    sprite('ma602_11', 3)
    sprite('ma602_10', 3)
    sprite('ma602_09', 3)
    sprite('ma602_08', 3)
    SpriteIfNot0(40, 2, 44)
    sprite('ma602_08', 20)
    Voiceline('ma408')
    DemoEndOnVoiceEnd(1)
    sprite('ma003_00', 3)
    Flip()
    sprite('ma003_01', 3)
    sprite('ma003_00ex01', 3)
    sprite('ma032_00ex', 4)
    PreDashEffects(100, 1, 1)
    physicsXImpulse(5000)
    SetAcceleration(500)
    sprite('ma032_01ex', 4)
    sprite('ma032_02ex', 3)
    sprite('ma032_03ex', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_04ex', 3)
    sprite('ma032_05ex', 3)
    sprite('ma032_06ex', 4)
    sprite('ma032_07ex', 3)
    sprite('ma032_08ex', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_09ex', 3)
    sprite('ma032_10ex', 3)
    sprite('ma032_01ex', 4)
    sprite('ma032_02ex', 3)
    sprite('ma032_03ex', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_04ex', 3)
    sprite('ma032_05ex', 3)
    sprite('ma032_06ex', 4)
    sprite('ma032_07ex', 3)
    sprite('ma032_08ex', 3)
    DashEffects(100, 1, 1)
    sprite('ma032_09ex', 3)
    sprite('ma032_10ex', 3)
    label(2)
    sprite('ma032_01ex', 4)
    sprite('ma032_02ex', 3)
    sprite('ma032_03ex', 3)
    sprite('ma032_04ex', 3)
    sprite('ma032_05ex', 3)
    sprite('ma032_06ex', 4)
    sprite('ma032_07ex', 3)
    sprite('ma032_08ex', 3)
    sprite('ma032_09ex', 3)
    sprite('ma032_10ex', 3)
    loopRest()
    gotoLabel(2)
    label(666)
    sprite('ma000_00', 7)
    sprite('ma000_01', 7)
    sprite('ma000_02', 7)
    sprite('ma000_03', 7)
    sprite('ma000_04', 7)
    sprite('ma000_05', 7)
    sprite('ma000_06', 7)
    sprite('ma000_07', 7)
    sprite('ma000_08', 7)
    sprite('ma000_09', 7)
    sprite('ma000_10', 7)
    sprite('ma000_11', 7)
    loopRest()
    ExitState()
    label(110)
    sprite('ma000_00', 7)
    sprite('ma615_00', 6)
    sprite('ma615_01', 6)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    Voiceline('ma503')
    DemoEndOnVoiceEnd(1)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    label(111)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    loopRest()
    gotoLabel(111)
    label(120)
    sprite('ma610_00', 7)
    sprite('ma610_01', 8)
    sprite('ma610_02', 12)
    sprite('ma610_03', 6)
    sprite('ma610_04', 12)
    sprite('ma610_05', 6)
    sprite('ma610_06', 6)
    Voiceline('ma505')
    DemoEndOnVoiceEnd(1)
    sprite('ma610_06', 32767)
    loopRest()
    label(220)
    sprite('ma610_00', 7)
    sprite('ma610_01', 8)
    sprite('ma610_02', 12)
    sprite('ma610_03', 6)
    sprite('ma610_04', 12)
    sprite('ma610_05', 6)
    sprite('ma610_06', 6)
    Voiceline('ma525')
    DemoEndOnVoiceEnd(1)
    sprite('ma610_06', 32767)
    loopRest()
    label(240)
    sprite('ma615_00', 6)
    sprite('ma615_01', 6)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    Voiceline('ma529')
    DemoEndOnVoiceEnd(1)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    label(241)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    loopRest()
    gotoLabel(241)
    label(250)
    sprite('ma610_00', 7)
    sprite('ma610_01', 8)
    sprite('ma610_02', 12)
    sprite('ma610_03', 6)
    sprite('ma610_04', 12)
    sprite('ma610_05', 6)
    sprite('ma610_06', 6)
    Voiceline('ma531')
    DemoEndOnVoiceEnd(1)
    sprite('ma610_06', 32767)
    loopRest()
    label(290)
    sprite('ma615_00', 6)
    sprite('ma615_01', 6)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    Voiceline('ma539')
    DemoEndOnVoiceEnd(1)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    label(291)
    sprite('ma615_02', 9)
    sprite('ma615_03', 9)
    sprite('ma615_04', 9)
    sprite('ma615_05', 10)
    sprite('ma615_06', 9)
    loopRest()
    gotoLabel(291)
    label(330)
    sprite('ma001_01', 6)
    sprite('ma620_00', 6)
    CommonSE('008_swing_pole_2')
    sprite('ma203_00', 6)
    sprite('ma620_01', 6)
    sprite('ma620_02', 6)
    sprite('ma620_02ex1', 6)
    sprite('ma620_02ex2', 6)
    sprite('ma620_03', 6)
    sprite('ma620_04', 6)
    sprite('ma620_05', 6)
    Voiceline('ma547')
    DemoEndOnVoiceEnd(1)
    sprite('ma620_05ex1', 32767)
    loopRest()


@State
def CmnActLose():
    sprite('ma000_00', 6)
    sprite('ma001_01', 6)
    sprite('ma620_00', 6)
    CommonSE('008_swing_pole_2')
    sprite('ma203_00', 6)
    sprite('ma620_01', 6)
    sprite('ma620_02', 6)
    sprite('ma620_02ex1', 6)
    sprite('ma620_02ex2', 6)
    sprite('ma620_03', 6)
    Voiceline('ma411')
    DemoEndOnVoiceEnd(1)
    sprite('ma620_04', 6)
    sprite('ma620_05', 6)
    sprite('ma620_05ex1', 32767)
    loopRest()


@State
def Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)
        ObjectUpon2(11, 11, 0)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_Ojigi():
    sprite('ma620_00', 7)
    sprite('ma602_07', 7)
    sprite('ma602_08', 20)
    sprite('ma602_09', 6)
    sprite('ma602_10', 6)
    sprite('ma602_11', 6)
    sprite('ma602_12', 6)
    sprite('ma602_13', 10)
    sprite('ma602_12', 6)
    sprite('ma602_11', 6)
    sprite('ma602_10', 6)
    sprite('ma602_09', 6)
    sprite('ma602_08', 10)
    sprite('ma602_14', 6)
    sprite('ma203_14', 6)
    sprite('ma203_15', 6)
    sprite('ma203_16', 6)
    sprite('ma203_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_OjigiHalf():
    sprite('ma620_00', 7)
    sprite('ma602_07', 7)
    sprite('ma602_08', 32767)
    loopRest()


@State
def Act3Event_OjigiHalfEnd():
    sprite('ma602_09', 6)
    sprite('ma602_10', 6)
    sprite('ma602_11', 6)
    sprite('ma602_12', 6)
    sprite('ma602_13', 10)
    sprite('ma602_12', 6)
    sprite('ma602_11', 6)
    sprite('ma602_10', 6)
    sprite('ma602_09', 6)
    sprite('ma602_08', 10)
    sprite('ma602_14', 6)
    sprite('ma203_14', 6)
    sprite('ma203_15', 6)
    sprite('ma203_16', 6)
    sprite('ma203_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Kobushi():
    sprite('ma610_00', 6)
    sprite('ma610_01', 6)
    sprite('ma610_02', 32767)
    loopRest()


@State
def Act3Event_KobushiEnd():
    sprite('ma610_02', 6)
    sprite('ma610_01', 6)
    sprite('ma610_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Chouhatsu():
    sprite('ma300_00', 7)
    sprite('ma300_01', 7)
    CommonSE('019_cloth_a')
    sprite('ma300_02', 7)
    sprite('ma300_03', 7)
    sprite('ma300_04', 7)
    sprite('ma300_05', 12)
    sprite('ma300_06', 7)
    sprite('ma300_07', 7)
    sprite('ma001_08', 7)
    sprite('ma001_09', 7)
    sprite('ma001_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavslc_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
        XPositionRelativeFacing(-720000)
    label(0)
    sprite('ma000_00', 7)
    sprite('ma000_01', 7)
    sprite('ma000_02', 7)
    sprite('ma000_03', 7)
    sprite('ma000_04', 7)
    sprite('ma000_05', 7)
    sprite('ma000_06', 7)
    sprite('ma000_07', 7)
    sprite('ma000_08', 7)
    sprite('ma000_09', 7)
    sprite('ma000_10', 7)
    sprite('ma000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavslc_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
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
    sprite('ma030_00', 7)
    physicsXImpulse(5000)
    label(9)
    sprite('ma030_01', 7)
    sprite('ma030_02', 7)
    sprite('ma030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_04', 7)
    sprite('ma030_05', 7)
    sprite('ma030_06', 7)
    sprite('ma030_07', 7)
    sprite('ma030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_09', 7)
    sprite('ma030_10', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavslc_02():

    def upon_IMMEDIATE():

        def upon_32():
            SetActionMark(1)
    sprite('ma615_00', 6)
    sprite('ma615_01', 6)
    label(0)
    sprite('ma615_02', 11)
    sprite('ma615_03', 10)
    sprite('ma615_04', 10)
    sprite('ma615_05', 11)
    sprite('ma615_06', 9)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(0)
    sprite('ma615_02', 11)
    sprite('ma615_01', 6)
    sprite('ma615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavsmk_00():
    sprite('ma611_00', 5)
    sprite('ma611_01', 5)
    sprite('ma611_02', 5)
    sprite('ma611_03', 30)
    sprite('ma611_02', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavsmk_01():
    sprite('ma000_00', 6)
    sprite('ma001_01', 6)
    sprite('ma620_00', 6)
    sprite('ma203_00', 6)
    sprite('ma620_01', 6)
    sprite('ma620_02', 6)
    sprite('ma620_02ex1', 6)
    sprite('ma620_02ex2', 6)
    sprite('ma620_03', 6)
    sprite('ma620_04', 6)
    sprite('ma620_05', 6)
    sprite('ma620_05ex1', 32767)
    loopRest()


@State
def Act3Event_mavsmk_02():
    sprite('keep', 2)
    sprite('ma620_03', 6)
    sprite('ma620_02ex2', 6)
    sprite('ma620_02ex1', 6)
    sprite('ma620_02', 6)
    sprite('ma620_01', 6)
    sprite('ma620_00', 6)
    sprite('ma001_01', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavsmk_03():
    sprite('ma333_00', 4)
    sprite('ma333_01', 4)
    sprite('ma333_02', 4)
    sprite('ma333_03', 32767)
    loopRest()


@State
def Act3Event_mavsmk_04():
    sprite('keep', 2)
    sprite('ma333_04', 4)
    CommonSE('302_spsys_burst')
    E0EAEffect('GuardCrushWind', 65535)

    def RunOnObject_1():
        Size(1400)
    ScreenShake(1000, 50000)
    label(0)
    sprite('ma333_05', 5)
    sprite('ma333_06', 5)
    sprite('ma333_07', 5)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavsmk_05():
    sprite('keep', 2)
    sprite('ma333_08', 6)
    sprite('ma333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavspt_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(0)
    label(0)
    sprite('ma000_00', 7)
    sprite('ma000_01', 7)
    sprite('ma000_02', 7)
    sprite('ma000_03', 7)
    sprite('ma000_04', 7)
    sprite('ma000_05', 7)
    sprite('ma000_06', 7)
    sprite('ma000_07', 7)
    sprite('ma000_08', 7)
    sprite('ma000_09', 7)
    sprite('ma000_10', 7)
    sprite('ma000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        ObjectUpon(22, 32)
        CameraControlEnable(1)
    label(0)
    sprite('ma000_00', 7)
    sprite('ma000_01', 7)
    sprite('ma000_02', 7)
    sprite('ma000_03', 7)
    sprite('ma000_04', 7)
    sprite('ma000_05', 7)
    sprite('ma000_06', 7)
    sprite('ma000_07', 7)
    sprite('ma000_08', 7)
    sprite('ma000_09', 7)
    sprite('ma000_10', 7)
    sprite('ma000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_02():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(0)
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
    sprite('ma030_00', 7)
    physicsXImpulse(5000)
    label(9)
    sprite('ma030_01', 7)
    sprite('ma030_02', 7)
    sprite('ma030_03', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_04', 7)
    sprite('ma030_05', 7)
    sprite('ma030_06', 7)
    sprite('ma030_07', 7)
    sprite('ma030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_09', 7)
    sprite('ma030_10', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavspt_03():
    label(0)
    sprite('ma450_02', 6)
    sprite('ma450_03', 6)
    sprite('ma450_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_04():
    sprite('ma450_01', 6)
    sprite('ma450_00', 6)
    loopRest()
    enterState('Act3Event_Kobushi')


@State
def Act3Event_mavspt_05():
    sprite('ma040_00', 4)
    CreateParticle('story_teni', 103)
    CommonSE('000_airdash_2')
    CommonSE('022_magiccircle_b')
    ConstantAlphaModifier(-4)
    sprite('ma040_01', 4)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    CreateParticle('haef_event_lose_end', 103)
    sprite('keep', 1)
    Visibility(1)
    ForceShadowOff(1)
    label(0)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavsrl_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        AlphaValue(0)

        def upon_STATE_END():
            AlphaValue(255)
    sprite('ma040_02', 5)
    CreateParticle('story_teni', 103)
    CommonSE('000_airdash_2')
    CommonSE('022_magiccircle_b')
    ConstantAlphaModifier(4)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    CreateParticle('haef_event_lose_end', 103)
    sprite('ma040_03', 5)
    sprite('ma040_04', 5)
    sprite('ma040_02', 5)
    sprite('ma040_01', 6)
    sprite('ma040_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavsrl_01():

    def upon_IMMEDIATE():
        uponSendToLabel(LANDING, 0)
    sprite('ma402_00', 4)
    sprite('ma402_01', 4)
    sprite('ma402_02', 5)
    physicsXImpulse(-8000)
    physicsYImpulse(32000)
    setGravity(2400)
    sprite('ma402_03', 5)
    sprite('ma402_04', 5)
    sprite('ma402_05', 5)
    sprite('ma402_06', 5)
    sprite('ma430_09', 5)
    sprite('ma020_04', 3)
    sprite('ma020_05', 3)
    sprite('ma020_06', 3)
    label(9)
    sprite('ma020_07', 4)
    sprite('ma020_08', 4)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ma430_10', 6)
    clearUponHandler(LANDING)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    PreDashEffects(100, 1, 1)
    sprite('ma430_11', 6)
    label(1)
    sprite('ma430_12', 6)
    sprite('ma430_13', 6)
    sprite('ma430_14', 6)
    loopRest()
    gotoLabel(1)


@State
def Act3Event_mavsrl_02():
    sprite('ma010_01', 5)
    sprite('ma010_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavsrl_03():
    sprite('ma450_00', 6)
    sprite('ma450_01', 6)
    label(0)
    sprite('ma450_02', 6)
    sprite('ma450_03', 6)
    sprite('ma450_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavsrl_04():
    sprite('ma450_05', 4)
    sprite('ma450_06', 4)
    sprite('ma450_07', 4)
    sprite('ma450_08', 4)
    AddX(50000)
    CommonSE('008_swing_pole_2')
    sprite('ma450_09', 6)
    label(0)
    sprite('ma450_10', 6)
    sprite('ma450_11', 6)
    sprite('ma450_12', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavsrl_05():
    sprite('ma450_36', 4)
    AddX(-50000)
    sprite('ma450_37', 4)
    loopRest()
    enterState('CmnActStand')
