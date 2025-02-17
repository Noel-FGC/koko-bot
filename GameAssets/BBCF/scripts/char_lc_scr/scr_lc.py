@Subroutine
def PreInit():
    CharacterID('lc')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    JumpYVelocity(36000)
    SuperJumpYVelocity(47000)
    ForwardSuperJumpVelocity(7500)
    BackwardSuperJumpVelocity(6500)
    Gravity(1700)
    AirFDashDuration(18)
    AirDashFSpeed(33000)
    AirBDashDuration(30)
    AirDashBSpeed(21000)
    AirBDashGravity(-1350)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(2)
    CreateDecalOn(1)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    Move_Condition(0x305b)
    MoveMid()
    SkillEstimateRange(0, 300000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk6A_NoRod', INPUT_6A)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    MoveMid()
    SkillEstimateRange(0, 300000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    Move_Condition(0x305b)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 400000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Atk5B_NoRod', INPUT_5B)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 300000, -100000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    Move_Condition(0x305b)
    SkillEstimateRange(300000, 700000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk6B_NoRod', INPUT_6B)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 500000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4B', INPUT_4B)
    Move_Condition(0x305b)
    SkillEstimateRange(-100000, 250000, 200000, 600000, 1000, 0)
    Move_EndRegister()
    Move_Register('Atk4B_NoRod', INPUT_4B)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(-100000, 250000, 50000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    Move_Condition(0x305b)
    MoveLow()
    SkillEstimateRange(100000, 400000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2B_NoRod', INPUT_2B)
    Move_Condition(0x305d)
    SharedGatling('Atk5B_NoRod')
    MoveLow()
    SkillEstimateRange(100000, 400000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2B_NoRod_OD', INPUT_2B)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    StateCall('Atk2B_NoRod')
    Move_Condition(0x3081)
    MoveLow()
    SkillEstimateRange(100000, 400000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    Move_Condition(0x305b)
    MoveCancellableFrames(52, 55)
    SkillEstimateRange(300000, 700000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk5C_NoRod', INPUT_5C)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 430000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    Move_Condition(0x305b)
    SkillEstimateRange(400000, 700000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk6C_NoRod', INPUT_6C)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 300000, -100000, 240000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    Move_Condition(0x305b)
    DamageStunPriority(1)
    SkillEstimateRange(200000, 500000, 100000, 450000, 3000, 50)
    Move_EndRegister()
    Move_Register('Atk2C_NoRod', INPUT_2C)
    Move_Condition(0x305d)
    SharedGatling('Atk5C_NoRod')
    MoveMaxChainRepeat(2)
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, 100000, 450000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2C_NoRod_OD', INPUT_2C)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    StateCall('Atk2C_NoRod')
    Move_Condition(0x3081)
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, 100000, 450000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    Move_Condition(0x305b)
    SkillEstimateRange(300000, 500000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk3C_NoRod', INPUT_3C)
    Move_Condition(0x305d)
    MoveMaxChainRepeat(2)
    MoveLow()
    SkillEstimateRange(0, 450000, 0, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    Move_Condition(0x305b)
    MovePriority(1)
    SkillEstimateRange(400000, 800000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk5D_NoRod', INPUT_5D)
    Move_Condition(0x305c)
    Move_Condition(0x304c)
    CallSkillConditions('CheckNotOD')
    DamageStunPriority(1)
    Move_EndRegister()
    Move_Register('NmlAtk4D', INPUT_4D)
    Move_Condition(0x305b)
    MoveMid()
    SkillEstimateRange(200000, 400000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    Move_Condition(0x305b)
    GuardStunPriority(1000)
    SkillEstimateRange(200000, 600000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    Move_Condition(0x305b)
    MovePriority(1)
    SkillEstimateRange(400000, 800000, 0, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk2D_NoRod', INPUT_2D)
    Move_Condition(0x305c)
    DamageStunPriority(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(0, 200000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    Move_Condition(0x305b)
    SkillEstimateRange(-300000, 300000, -300000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('AtkAIR5B_NoRod', INPUT_J5B)
    MoveMaxChainRepeat(2)
    Move_Condition(0x305d)
    SkillEstimateRange(0, 350000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    Move_Condition(0x305b)
    SkillEstimateRange(200000, 500000, 0, 300000, 3000, 50)
    Move_EndRegister()
    Move_Register('AtkAIR5C_NoRod', INPUT_J5C)
    SharedGatling('AtkAIR5B_NoRod')
    Move_Condition(0x305d)
    DamageStunPriority(3000)
    SkillEstimateRange(-100000, 250000, -300000, 70000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x305b)
    MovePriority(1)
    SkillEstimateRange(200000, 1000000, -1000000, 0, 1000, 0)
    Move_EndRegister()
    Move_Register('AtkAIR5D_NoRod', INPUT_J5D)
    Move_Condition(0x305c)
    CallSkillConditions('CheckNotOD')
    DamageStunPriority(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2D', INPUT_J2D)
    Move_Condition(0x305b)
    SkillEstimateRange(-200000, 200000, -1000000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('BDash_2nd', INPUT_SPECIALMOVE)
    AddChain(1)
    FollowupOnly(1)
    Move_Input_(0x85)
    Move_EndRegister()
    Move_Register('RodOverDriveAttack', INPUT_SPECIALMOVE)
    ForceSkillDirection(1)
    Move_Input_(0x1d)
    IndependentInput(1, 0, 0)
    CallFunction('RodODAttack')
    AddChain(1)
    MovePriority(1)
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
    SkillEstimateRange(0, 200000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x3062)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    MoveMaxChainRepeat(1)
    MoveLow()
    SkillEstimateRange(0, 400000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('Assault2', INPUT_SPECIALMOVE)
    Move_Condition(0x3062)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    MoveMaxChainRepeat(1)
    MoveMid()
    SkillEstimateRange(250000, 450000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('AirAssault2', INPUT_SPECIALMOVE)
    Move_Condition(0x3062)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    SharedGatling('Assault2')
    SkillEstimateRange(250000, 450000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('Assault3', INPUT_SPECIALMOVE)
    Move_Condition(0x3062)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    MoveMaxChainRepeat(1)
    OpponentAttackPriority(2000)
    MoveCPULevel(500, 1000, 1, 1000)
    SkillEstimateRange(0, 350000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('AirAssault3', INPUT_SPECIALMOVE)
    Move_Condition(0x3062)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    SharedGatling('Assault3')
    SkillEstimateRange(0, 350000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('DashAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x305d)
    Move_Condition(0x2000)
    Move_Input_(INPUT_421)
    Move_Input_(INPUT_PRESS_C)
    MoveButtonHoldTime(2, 17, 20)
    SkillEstimateRange(400000, 800000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('JumpToRod_Ride', INPUT_SPECIALMOVE)
    Move_Condition(0x3065)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_A)
    OldSpecialInput(4)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('JumpToRod_Kick', INPUT_SPECIALMOVE)
    Move_Condition(0x3065)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_B)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('JumpToRod_Jump', INPUT_SPECIALMOVE)
    Move_Condition(0x3065)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_C)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('RideEnd', INPUT_SPECIALMOVE)
    AddChain(1)
    FollowupOnly(1)
    Move_Input_(0x45)
    Move_EndRegister()
    Move_Register('RideAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 200000, -600000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('RideAttackB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_B)
    SkillEstimateRange(0, 200000, -600000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('RideAttackC', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_C)
    SkillEstimateRange(0, 200000, -600000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('RideAttackD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 200000, -600000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('RocketLandF', INPUT_SPECIALMOVE)
    Move_Condition(0x305c)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    NeutralOnly(1)
    MovePriority(10)
    MoveComboPriority(10)
    Move_EndRegister()
    Move_Register('RocketLandB', INPUT_SPECIALMOVE)
    Move_Condition(0x305c)
    Move_Condition(0x2000)
    Move_Input_(INPUT_421)
    Move_Input_(INPUT_PRESS_D)
    NeutralOnly(1)
    MovePriority(10)
    MoveComboPriority(10)
    Move_EndRegister()
    Move_Register('RocketAirF', INPUT_SPECIALMOVE)
    Move_Condition(0x305c)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    NeutralOnly(1)
    MovePriority(10)
    MoveComboPriority(10)
    Move_EndRegister()
    Move_Register('RocketAirB', INPUT_SPECIALMOVE)
    Move_Condition(0x305c)
    Move_Condition(0x2001)
    Move_Input_(INPUT_421)
    Move_Input_(INPUT_PRESS_D)
    NeutralOnly(1)
    MovePriority(10)
    MoveComboPriority(10)
    Move_EndRegister()
    Move_Register('TonNanShaPeiAntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x3060)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('TonNanShaPeiAntiLand', INPUT_SPECIALMOVE)
    Move_Condition(0x3061)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    OldSpecialInput(1)
    OpponentAttackPriority(3000)
    MoveCPULevel(500, 1000, 1, 1000)
    SkillEstimateRange(0, 300000, 0, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('KantsuA', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(400000, 800000, 200000, 600000, 500, 50)
    Move_EndRegister()
    Move_Register('KantsuB', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_B)
    SkillEstimateRange(400000, 800000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('KantsuC', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_C)
    MoveLow()
    SkillEstimateRange(300000, 700000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('KantsuD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('RenchanB', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(600000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('RenchanC', INPUT_SPECIALMOVE)
    Move_Condition(0x305b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(900000, 1500000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('UltimateNingyouU', INPUT_DISTORTION)
    Move_Condition(0x305e)
    Move_Condition(0x3060)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(400)
    AirborneOpponentPriority(3000)
    Move_EndRegister()
    Move_Register('UltimateNingyouD', INPUT_DISTORTION)
    Move_Condition(0x305e)
    Move_Condition(0x3061)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(400)
    DamageStunPriority(3000)
    Move_EndRegister()
    Move_Register('UltimateRush', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(1500)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateRush_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    OpponentAttackPriority(1500)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateBakuhatsu', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_6428)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(2000)
    SkillEstimateRange(300000, 800000, -100000, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateBakuhatsu_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_6428)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    DamageStunPriority(2000)
    SkillEstimateRange(300000, 800000, -100000, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    FollowupOnly(1)
    Move_Input_(INPUT_46)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('AstralHeat_OD', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_34123646)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    StateCall('AstralHeat')
    Move_EndRegister()
    Move_Register('DashRodReturn', 0x1)
    Move_Condition(0x305c)
    Move_Input_(0x1d)
    FollowupOnly(1)
    CallFunction('FuncDashRodReturn')
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
    SkillEstimateRange(0, 550000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 550000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(0, 550000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk4D', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('Atk6A_NoRod', 'Atk5C_NoRod', 10000000)
    TempPriorityMultiplier('Atk2B_NoRod', 'Atk5B_NoRod', 10000000)
    TempPriorityMultiplier('Atk5B_NoRod', 'Atk6B_NoRod', 10000000)
    TempPriorityMultiplier('Atk6B_NoRod', 'Atk5C_NoRod', 10000000)
    TempPriorityMultiplier('Atk5C_NoRod', 'Atk2C_NoRod', 10000000)
    TempPriorityMultiplier('Atk2C_NoRod', 'Atk3C_NoRod', 10000000)
    TempPriorityMultiplier('Atk5C_NoRod', 'Assault', 10000000)
    TempPriorityMultiplier('Atk3C_NoRod', 'Assault', 10000000)
    TempPriorityMultiplier('Assault', 'Assault3', 10000000)
    TempPriorityMultiplier('Assault3', 'AirAssault2', 10000000)
    TempPriorityMultiplier('AirAssault3', 'AirAssault2', 10000000)
    TempPriorityMultiplier('AirAssault2', 'JumpToRod_Kick', 10000000)
    TempPriorityMultiplier('AirAssault2', 'JumpToRod_Jump', 10000000)
    StylishModeSpecialButton('AntiAir', 0x4, 0xea)
    StylishModeSpecialButton('KantsuB', 0x4, 0x79)
    StylishModeSpecialButton('UltimateRush', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateRush_OD', 0x4, 0x5f)
    StylishModeSpecialButton('RenchanB', 0x4, 0x45)
    StylishModeSpecialButton('Assault3', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0xea)
    StylishModeSpecialButton('DashAssault', 0x4, 0x79)
    StylishModeSpecialButton('UltimateRush', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateRush_OD', 0x4, 0x5f)
    StylishModeSpecialButton('Assault2', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault2', 0x4, 0xea)
    StylishModeSpecialButton('AirAssault3', 0x4, 0xea)
    StylishModeSpecialButton('AirAssault2', 0x4, 0x45)
    StylishModeSpecialButton('RideAttackB', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk2B', 10, 300000)
    StylishModeCancels('NmlAtk5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk2C', 1, 170000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6D', 1, 300000)
    StylishModeCancels('NmlAtk5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk4B', 6, 0)
    StylishModeCancels('NmlAtk4B', 'KantsuB', 0, 0)
    StylishModeCancels('NmlAtk4B', 'KantsuA', 6, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk6C', 13, 0)
    StylishModeCancels('NmlAtk6B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6D', 'AntiAir', 6, 0)
    StylishModeCancels('NmlAtk6D', 'UltimateRush', 6, 0)
    StylishModeCancels('NmlAtk6D', 'UltimateRush_OD', 6, 0)
    StylishModeCancels('ThrowExe', 'AntiAir', 0, 0)
    StylishModeCancels('BackThrowExe', 'AntiAir', 0, 0)
    StylishModeCancels('NmlAtk5A', 'Atk5B_NoRod', 0, 0)
    StylishModeCancels('Atk5B_NoRod', 'Atk2B_NoRod', 0, 0)
    StylishModeCancels('Atk5B_NoRod', 'Atk5C_NoRod', 6, 0)
    StylishModeCancels('Atk5B_NoRod', 'FJump', 12, 0)
    StylishModeCancels('Atk5C_NoRod', 'Atk3C_NoRod', 0, 0)
    StylishModeCancels('Atk5C_NoRod', 'FJump', 12, 0)
    StylishModeCancels('Atk6A_NoRod', 'Assault', 6, 0)
    StylishModeCancels('Atk6B_NoRod', 'FJump', 12, 0)
    StylishModeCancels('Atk6B_NoRod', 'Atk5C_NoRod', 0, 0)
    StylishModeCancels('Assault', 'Assault3', 6, 0)
    StylishModeCancels('Assault2', 'Assault', 6, 0)
    StylishModeCancels('Assault3', 'AirAssault2', 6, 0)
    StylishModeCancels('ThrowExe', 'Assault3', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk6B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk4B', 1, 400000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6D', 0, 0)
    StylishModeCancels('NmlAtk3C', 'KantsuB', 0, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateRush', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateRush_OD', 6, 0)
    StylishModeCancels('NmlAtk2A', 'Atk2B_NoRod', 0, 0)
    StylishModeCancels('Atk2B_NoRod', 'Atk2C_NoRod', 0, 0)
    StylishModeCancels('Atk2C_NoRod', 'Atk3C_NoRod', 0, 0)
    StylishModeCancels('Atk3C_NoRod', 'Assault', 0, 0)
    StylishModeCancels('Atk3C_NoRod', 'UltimateRush', 6, 0)
    StylishModeCancels('Atk3C_NoRod', 'UltimateRush_OD', 6, 0)
    StylishModeCancels('Atk3C_NoRod', 'DashAssault', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5A', 'AtkAIR5B_NoRod', 0, 0)
    StylishModeCancels('AtkAIR5B_NoRod', 'AtkAIR5C_NoRod', 0, 0)
    StylishModeCancels('AtkAIR5B_NoRod', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('AtkAIR5C_NoRod', 'AirAssault3', 12, 0)
    StylishModeCancels('AtkAIR5C_NoRod', 'AtkAIR5B_NoRod', 0, 0)
    StylishModeCancels('AirAssault3', 'AirAssault2', 6, 0)
    StylishModeCancels('AirAssault2', 'Assault', 6, 0)
    StylishModeCancels('RideAttack', 'AstralHeat', 6, 0)
    HitSprites(0, 'lc062_01')
    HitSprites(1, 'lc062_03')
    HitSprites(2, 'lc062_04')
    HitSprites(3, 'lc062_05')
    HitSprites(4, 'lc062_05')
    HitSprites(5, 'lc062_06')
    HitSprites(6, 'lc062_07')
    HitSprites(7, 'lc041_02')
    HitSprites(8, 'lc040_02')
    HitSprites(9, 'lc045_02')
    HitSprites(10, 'lc060_00')
    HitSprites(11, 'lc060_01')
    HitSprites(12, 'lc060_03')
    HitSprites(13, 'lc060_05')
    HitSprites(14, 'lc060_07')
    HitSprites(15, 'lc060_14')
    HitSprites(16, 'lc050_00')
    HitSprites(17, 'lc052_00')
    HitSprites(18, 'lc054_00')
    HitSprites(19, 'lc000_00')
    HitSprites(20, 'lc000_00')
    HitSprites(25, 'lc063_00')
    HitSprites(26, 'lc063_01')
    HitSprites(27, 'lc063_02')
    HitSprites(28, 'lc063_04')
    HitSprites(29, 'lc063_11')
    HitSprites(30, 'lc077_00')
    HitSprites(31, 'lc077_01')
    HitSprites(32, 'lc077_00ex01')
    HitSprites(33, 'lc077_01ex01')
    HitSprites(34, 'lc077_00ex02')
    HitSprites(35, 'lc077_01ex02')
    HitSprites(36, 'lc077_00ex03')
    HitSprites(37, 'lc077_01ex03')
    HitSprites(24, 'lc073_01')
    CommonVoicelines(0, 'lc000')
    CommonVoicelines(1, 'lc001')
    CommonVoicelines(2, 'lc002')
    CommonVoicelines(3, 'lc003')
    CommonVoicelines(4, 'lc004')
    CommonVoicelines(5, 'lc005')
    CommonVoicelines(6, 'lc006')
    CommonVoicelines(7, 'lc007')
    CommonVoicelines(8, 'lc008')
    CommonVoicelines(9, 'lc009')
    CommonVoicelines(10, 'lc010')
    CommonVoicelines(11, 'lc011')
    CommonVoicelines(12, 'lc012')
    CommonVoicelines(13, 'lc013')
    CommonVoicelines(14, 'lc014')
    CommonVoicelines(15, 'lc015')
    CommonVoicelines(16, 'lc016')
    CommonVoicelines(17, 'lc017')
    CommonVoicelines(18, 'lc018')
    CommonVoicelines(19, 'lc019')
    CommonVoicelines(20, 'lc020')
    CommonVoicelines(21, 'lc021')
    CommonVoicelines(22, 'lc022')
    CommonVoicelines(23, 'lc023')
    CommonVoicelines(24, 'lc024')
    CommonVoicelines(25, 'lc025')
    CommonVoicelines(26, 'lc026')
    CommonVoicelines(27, 'lc027')
    CommonVoicelines(28, 'lc028')
    CommonVoicelines(29, 'lc029')
    CommonVoicelines(30, 'lc030')
    CommonVoicelines(31, 'lc031')
    CommonVoicelines(32, 'lc032')
    CommonVoicelines(33, 'lc033')
    CommonVoicelines(34, 'lc034')
    CommonVoicelines(35, 'lc035')
    CommonVoicelines(36, 'lc036')
    CommonVoicelines(37, 'lc037')
    CommonVoicelines(38, 'lc038')
    CommonVoicelines(39, 'lc039')
    CommonVoicelines(40, 'lc040')
    CommonVoicelines(41, 'lc041')
    CommonVoicelines(42, 'lc042')
    CommonVoicelines(43, 'lc043')
    CommonVoicelines(44, 'lc044')
    CommonVoicelines(45, 'lc045')
    CommonVoicelines(46, 'lc046')
    CommonVoicelines(47, 'lc047')
    CommonVoicelines(48, 'lc048')
    CommonVoicelines(49, 'lc049')
    CommonVoicelines(50, 'lc050')
    CommonVoicelines(51, 'lc051')
    CommonVoicelines(52, 'lc052')
    CommonVoicelines(53, 'lc053')
    CommonVoicelines(54, 'lc100')
    CommonVoicelines(55, 'lc101')
    CommonVoicelines(56, 'lc102')
    CommonVoicelines(57, 'lc103')
    CommonVoicelines(58, 'lc104')
    CommonVoicelines(59, 'lc105')
    CommonVoicelines(60, 'lc106')
    CommonVoicelines(61, 'lc107')
    CommonVoicelines(62, 'lc108')
    CommonVoicelines(63, 'lc109')
    CommonVoicelines(64, 'lc150')
    CommonVoicelines(65, 'lc151')
    CommonVoicelines(66, 'lc152')
    CommonVoicelines(67, 'lc153')
    CommonVoicelines(68, 'lc154')
    CommonVoicelines(69, 'lc155')
    CommonVoicelines(70, 'lc156')
    CommonVoicelines(71, 'lc157')
    CommonVoicelines(72, 'lc158')
    CommonVoicelines(75, 'lc160')
    CommonVoicelines(73, 'lc402')
    CommonVoicelines(74, 'lc403')
    CreateObject('RodCreate', -1)
    RegisterObject(11, 1)


@Subroutine
def MatchInit2():
    SLOT_7 = 5


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def RodODAttack():
    if SLOT_OverdriveTimer:
        if not SLOT_62:
            ObjectUpon2(11, 45, 0)
            if not SLOT_8:
                if SLOT_94:
                    SLOT_8 = 5
                else:
                    if CheckInput(0x37):
                        SLOT_8 = 1
                    if CheckInput(0x44):
                        SLOT_8 = 2
                    if CheckInput(0x51):
                        SLOT_8 = 3
                    if CheckInput(0x5e):
                        SLOT_8 = 4
                    if CheckInput(0x6b):
                        SLOT_8 = 5
                    if CheckInput(0x78):
                        SLOT_8 = 6
                    if CheckInput(0x85):
                        SLOT_8 = 7
                    if CheckInput(0x92):
                        SLOT_8 = 8
                    if CheckInput(0x9f):
                        SLOT_8 = 9


@Subroutine
def CheckNotOD():
    SLOT_47 = 0
    if not SLOT_OverdriveTimer:
        SLOT_47 = 1


@Subroutine
def CheckRodGrip():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    PrivateFunction(9, 2, 67, 0, 0, 2, 47)


@Subroutine
def CheckRodReturnable():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    SLOT_67 == 1
    PrivateFunction(0, 2, 0, 2, 47, 2, 47)
    SLOT_67 == 2
    PrivateFunction(0, 2, 0, 2, 47, 2, 47)


@Subroutine
def CheckRodNoGrip():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    PrivateFunction(15, 2, 67, 0, 0, 2, 47)


@Subroutine
def CheckRodLandStand():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    PrivateFunction(9, 2, 67, 0, 2, 2, 47)


@Subroutine
def CheckRodReturnableOrGrip():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    SLOT_67 == 0
    PrivateFunction(0, 2, 0, 2, 47, 2, 47)
    SLOT_67 == 1
    PrivateFunction(0, 2, 0, 2, 47, 2, 47)
    SLOT_67 == 2
    PrivateFunction(0, 2, 0, 2, 47, 2, 47)


@Subroutine
def CheckRodUpReturnable():
    callSubroutine('CheckRodReturnable')
    CopyFromRightToLeft(23, 2, 67, 11, 2, 64)
    SLOT_67 and 8
    PrivateFunction(5, 2, 0, 2, 47, 2, 47)


@Subroutine
def CheckRodDownReturnable():
    callSubroutine('CheckRodReturnable')
    CopyFromRightToLeft(23, 2, 67, 11, 2, 64)
    SLOT_67 and 8
    random_(1, 2, 0)
    PrivateFunction(5, 2, 0, 2, 47, 2, 47)


@Subroutine
def RodNoHit():

    def upon_EVERY_FRAME():
        TriggerUponForState('RodReturn', 39)
        TriggerUponForState('RodTonNanShaPeiAntiAir', 39)
        TriggerUponForState('RodTonNanShaPeiAntiLand', 39)
        TriggerUponForState('RodKantsuA', 39)
        TriggerUponForState('RodKantsuA2nd', 39)
        TriggerUponForState('RodKantsuB', 39)
        TriggerUponForState('RodKantsuB2nd', 39)
        TriggerUponForState('RodKantsuC', 39)
        TriggerUponForState('RodKantsuC2nd', 39)
        TriggerUponForState('RodAntiAir', 39)
        TriggerUponForState('RodNingyouU', 39)
        TriggerUponForState('RodNingyouD', 39)
        TriggerUponForState('RodOverDriveAttack', 39)


@Subroutine
def ODChain_Land():
    if SLOT_OverdriveTimer:
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('Atk6A_NoRod')
        HitOrBlockCancel('Atk5B_NoRod')
        HitOrBlockCancel('Atk2B_NoRod_OD')
        HitOrBlockCancel('Atk6B_NoRod')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk2C_NoRod_OD')
        HitOrBlockCancel('Atk6C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockJumpCancel(1)


@Subroutine
def ODChain_Air():
    if SLOT_OverdriveTimer:
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('AtkAIR5B_NoRod')
        HitOrBlockCancel('AtkAIR5C_NoRod')
        HitOrBlockJumpCancel(1)


@Subroutine
def CheckAssaultAvailable():
    CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
    PrivateFunction(15, 2, 67, 0, 0, 2, 47)
    if SLOT_47 == 0:
        if SLOT_59:
            SLOT_47 = 1


@Subroutine
def AssaultChain():
    HitOrBlockCancel('Assault')
    HitOrBlockCancel('Assault2')
    HitOrBlockCancel('AirAssault2')
    HitOrBlockCancel('Assault3')
    HitOrBlockCancel('AirAssault3')
    HitCancel('TonNanShaPeiAntiAir')
    HitCancel('TonNanShaPeiAntiLand')
    HitCancel('JumpToRod_Ride')
    HitCancel('JumpToRod_Kick')
    HitCancel('JumpToRod_Jump')
    SLOT_59 = SLOT_60
    SLOT_60 = 0
    SLOT_59 = SLOT_59 + 1
    if SLOT_59 == 2:
        SLOT_52 = 1
    if SLOT_59 == 3:
        AttackLevel_(4)
        EnableAfterimage(1)
        SLOT_53 = 1

        def upon_OPPONENT_HIT():
            Hitstop(20)
            SLOT_51 = 1


@Subroutine
def CheckJumpToRodAvailable():
    if SLOT_66:
        if SLOT_66 <= 1:
            CopyFromRightToLeft(23, 2, 67, 11, 2, 65)
            PrivateFunction(9, 2, 67, 0, 2, 2, 47)


@Subroutine
def OnPreSkillCheck():
    SLOT_47 = 0
    callSubroutine('CheckRodGrip')
    ObjectMoveCheck(0, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodReturnable')
    ObjectMoveCheck(1, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodNoGrip')
    ObjectMoveCheck(2, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodLandStand')
    ObjectMoveCheck(3, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodReturnableOrGrip')
    ObjectMoveCheck(4, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodUpReturnable')
    ObjectMoveCheck(5, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckRodDownReturnable')
    ObjectMoveCheck(6, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckAssaultAvailable')
    ObjectMoveCheck(7, 2, 47)
    SLOT_47 = 0
    callSubroutine('CheckJumpToRodAvailable')
    ObjectMoveCheck(10, 2, 47)


@Subroutine
def FuncDashRodReturn():
    ObjectUpon2(11, 2, 0)
    CreateObject('LcefRodReturn', 0)
    DashKeepInputTime(12)
    SmartVoiceline('lc211')


@Subroutine
def OnIdling():
    if not SLOT_YDistanceFromFloor:
        SLOT_66 = 1

    def upon_14():
        SLOT_62 = 0


@Subroutine
def OnActionBegin():
    ObjectUpon2(11, 14, 0)


@Subroutine
def OnFinalize():
    SLOT_60 = SLOT_59
    SLOT_59 = 0


@State
def CmnActStand():
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('lc001_00', 7)
    SLOT_88 = 960
    Voiceline('lc000')
    sprite('lc001_01', 7)
    sprite('lc001_02', 7)
    sprite('lc001_03', 7)
    sprite('lc001_04', 7)
    sprite('lc001_03', 7)
    sprite('lc001_02', 7)
    sprite('lc001_01', 7)
    sprite('lc001_00', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('lc003_00', 3)
    sprite('lc003_01', 3)
    sprite('lc003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('lc010_00', 4)
    sprite('lc010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('lc010_02', 8)
    sprite('lc010_03', 8)
    sprite('lc010_04', 8)
    sprite('lc010_05', 8)
    sprite('lc010_06', 8)
    sprite('lc010_05', 8)
    sprite('lc010_04', 8)
    sprite('lc010_03', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('lc013_00', 3)
    sprite('lc013_01', 3)
    sprite('lc013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('lc010_01', 4)
    sprite('lc010_00', 4)


@State
def CmnActJumpPre():
    sprite('lc023_00', 2)
    sprite('lc023_01', 2)


@State
def CmnActJumpUpper():
    sprite('lc020_00', 4)
    SmartVoiceline('lc002')
    sprite('lc020_01', 4)
    label(0)
    sprite('lc020_00', 4)
    sprite('lc020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('lc020_02', 3)
    sprite('lc020_03', 3)
    sprite('lc020_04', 3)


@State
def CmnActJumpDown():
    sprite('lc020_05', 3)
    sprite('lc020_06', 3)
    label(0)
    sprite('lc020_07', 4)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('lc024_00', 3)
    sprite('lc024_01', 3)
    sprite('lc024_02', 3)
    sprite('lc024_03', 3)
    sprite('lc024_04', 3)
    sprite('lc024_05', 3)
    sprite('lc024_06', 3)


@State
def CmnActLandingStiffLoop():
    sprite('lc024_00', 2)
    sprite('lc024_01', 2)
    sprite('lc024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('lc024_03', 3)
    sprite('lc024_04', 3)
    sprite('lc024_05', 3)
    sprite('lc024_06', 3)


@State
def CmnActAirTurn():
    sprite('lc025_00', 4)
    sprite('lc025_01', 4)
    sprite('lc025_02', 4)


@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
    sprite('lc030_00', 6)
    label(0)
    sprite('lc030_01', 6)
    sprite('lc030_02', 6)
    sprite('lc030_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_04', 6)
    sprite('lc030_05', 6)
    sprite('lc030_06', 6)
    sprite('lc030_07', 6)
    sprite('lc030_08', 6)
    sprite('lc030_09', 6)
    sprite('lc030_10', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_11', 6)
    sprite('lc030_12', 6)
    sprite('lc030_13', 6)
    sprite('lc030_14', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActFWalkEnd():
    sprite('lc030_15', 6)


@State
def CmnActBWalk():
    sprite('lc031_00', 6)
    label(0)
    sprite('lc031_01', 6)
    sprite('lc031_02', 6)
    sprite('lc031_03', 6)
    sprite('lc031_04', 4)
    sprite('lc031_05', 4)
    sprite('lc031_06', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc031_07', 6)
    sprite('lc031_08', 6)
    sprite('lc031_09', 6)
    sprite('lc031_10', 6)
    sprite('lc031_11', 6)
    sprite('lc031_12', 6)
    sprite('lc031_13', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc031_14', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('lc032_00', 3)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    WhiffCancelEnable(1)
    WhiffCancel('DashRodReturn')
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    sprite('lc032_01', 3)

    def upon_STATE_END():
        WhiffCancelEnable(0)
        PreventWhiffCancel('DashRodReturn')
    loopRest()
    label(0)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    sprite('lc032_01', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('lc032_13', 3)
    sprite('lc032_14', 3)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        EndMomentum(1)
        setInvincible(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('lc033_00', 1)
    sprite('lc033_00', 2)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    sprite('lc033_01', 2)
    sprite('lc033_02', 3)
    setGravity(850)
    setInvincible(0)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    BeginBuffer('BDash_2nd')
    sprite('lc033_03', 3)
    label(0)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc033_04', 2)
    XImpulseAcceleration(50)
    LandingEffects(100, 1, 1)
    sprite('lc033_04', 1)
    physicsXImpulse(0)
    BufferedOrPressedGoto('BDash_2nd')
    sprite('lc033_04', 1)
    DisallowGoto('BDash_2nd')
    sprite('lc033_05', 3)


@State
def BDash_2nd():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
        setInvincible(1)
        StayAfterMovement(1, 0)
        ExternalForcesRate(100, 0)
        WhiffCancel('FAirDash')
        WhiffCancel('NmlAtkAIR5A')
        WhiffCancel('NmlAtkAIR5B')
        WhiffCancel('NmlAtkAIR5C')
        WhiffCancel('NmlAtkAIR5D')
        WhiffCancel('NmlAtkAIR2D')
        WhiffCancel('NmlAtkAirThrow')
        WhiffCancel('AtkAIR5B_NoRod')
        WhiffCancel('AtkAIR5C_NoRod')
        WhiffCancel('AtkAIR5D_NoRod')
        WhiffCancel('RocketAirF')
        WhiffCancel('RocketAirB')
        WhiffCancel('JumpToRod_Ride')
        WhiffCancel('JumpToRod_Kick')
        WhiffCancel('JumpToRod_Jump')
    sprite('lc033_06', 4)
    SmartVoiceline('lc005')
    sprite('lc033_07', 5)
    physicsXImpulse(-9000)
    physicsYImpulse(18000)
    setGravity(1350)
    CommonSE('019_cloth_a')
    sprite('lc033_08', 5)
    setInvincible(0)
    sprite('lc033_09', 5)
    sprite('lc033_10', 5)
    WhiffCancelEnable(1)
    sprite('lc033_11', 5)
    sprite('lc033_12', 20)
    uponSendToLabel(LANDING, 1)
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(LANDING)
    sprite('lc033_13', 3)
    WhiffCancelEnable(0)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('lc033_14', 3)
    sprite('lc033_15', 3)


@State
def CmnActAirFDash():
    sprite('lc035_00', 2)
    SmartVoiceline('lc004')
    sprite('lc035_01', 2)
    sprite('lc035_02', 3)
    sprite('lc035_03', 3)
    sprite('lc035_04', 3)
    sprite('lc035_01', 2)
    sprite('lc035_02', 3)
    sprite('lc035_03', 3)
    sprite('lc035_04', 3)
    sprite('lc035_05', 2)


@State
def CmnActAirBDash():
    sprite('lc351_00', 3)
    physicsYImpulse(18000)
    SmartVoiceline('lc006')
    sprite('lc033_07ex00', 4)
    sprite('lc033_08ex00', 4)
    sprite('lc033_09ex00', 4)
    sprite('lc033_10ex00', 4)
    sprite('lc351_01', 4)
    sprite('lc351_02', 4)
    sprite('lc351_03', 3)


@State
def CmnActHitStandLv1():
    sprite('lc050_00', 1)
    sprite('lc050_01', 1)
    sprite('lc050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('lc050_01', 1)
    sprite('lc050_02', 1)
    sprite('lc050_01', 2)
    sprite('lc050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('lc050_02', 1)
    sprite('lc050_03', 1)
    sprite('lc050_02', 2)
    sprite('lc050_01', 2)
    sprite('lc050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('lc050_03', 1)
    sprite('lc050_04', 1)
    sprite('lc050_03', 2)
    sprite('lc050_02', 2)
    sprite('lc050_01', 2)
    sprite('lc050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('lc050_04', 1)
    sprite('lc050_04', 1)
    sprite('lc050_04', 2)
    sprite('lc050_03', 2)
    sprite('lc050_02', 2)
    sprite('lc050_01', 2)
    sprite('lc050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('lc052_00', 1)
    sprite('lc052_01', 1)
    sprite('lc052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('lc052_01', 1)
    sprite('lc052_02', 1)
    sprite('lc052_01', 2)
    sprite('lc052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('lc052_02', 1)
    sprite('lc052_03', 1)
    sprite('lc052_02', 2)
    sprite('lc052_01', 2)
    sprite('lc052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('lc052_03', 1)
    sprite('lc052_04', 1)
    sprite('lc052_03', 2)
    sprite('lc052_02', 2)
    sprite('lc052_01', 2)
    sprite('lc052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('lc052_04', 1)
    sprite('lc052_04', 1)
    sprite('lc052_04', 2)
    sprite('lc052_03', 2)
    sprite('lc052_02', 2)
    sprite('lc052_01', 2)
    sprite('lc052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('lc054_00', 1)
    sprite('lc054_01', 1)
    sprite('lc054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('lc054_01', 1)
    sprite('lc054_02', 1)
    sprite('lc054_01', 2)
    sprite('lc054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('lc054_02', 1)
    sprite('lc054_03', 1)
    sprite('lc054_02', 2)
    sprite('lc054_01', 2)
    sprite('lc054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('lc054_03', 1)
    sprite('lc054_04', 1)
    sprite('lc054_03', 2)
    sprite('lc054_02', 2)
    sprite('lc054_01', 2)
    sprite('lc054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('lc054_04', 1)
    sprite('lc054_04', 1)
    sprite('lc054_04', 2)
    sprite('lc054_03', 2)
    sprite('lc054_02', 2)
    sprite('lc054_01', 2)
    sprite('lc054_00', 2)


@State
def CmnActBDownUpper():
    sprite('lc060_00', 4)
    label(0)
    sprite('lc060_01', 4)
    sprite('lc060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('lc060_03', 4)


@State
def CmnActBDownDown():
    sprite('lc060_04', 4)
    label(0)
    sprite('lc060_05', 4)
    sprite('lc060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('lc060_07', 2)
    sprite('lc060_08', 2)


@State
def CmnActBDownBound():
    sprite('lc060_09', 3)
    sprite('lc060_10', 3)
    sprite('lc060_11', 3)
    sprite('lc060_12', 3)
    sprite('lc060_13', 3)


@State
def CmnActBDownLoop():
    sprite('lc060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('lc061_00', 3)
    sprite('lc061_01', 3)
    sprite('lc061_02', 3)
    sprite('lc061_03', 3)
    sprite('lc061_04', 3)
    sprite('lc061_05', 3)
    sprite('lc061_06', 2)
    sprite('lc061_07', 2)
    CommonSE('019_cloth_a')
    sprite('lc061_08', 2)
    sprite('lc061_09', 2)
    sprite('lc061_10', 2)
    sprite('lc061_11', 2)
    sprite('lc061_12', 2)
    sprite('lc061_13', 2)
    sprite('lc061_14', 2)


@State
def CmnActFDownUpper():
    sprite('lc063_00', 4)


@State
def CmnActFDownUpperEnd():
    sprite('lc063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('lc063_02', 3)
    sprite('lc063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('lc063_04', 3)
    sprite('lc063_05', 1)


@State
def CmnActFDownBound():
    sprite('lc063_06', 2)
    sprite('lc063_07', 2)
    sprite('lc063_08', 3)
    sprite('lc063_09', 3)
    sprite('lc063_10', 2)


@State
def CmnActFDownLoop():
    sprite('lc063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('lc064_00', 2)
    sprite('lc064_01', 2)
    sprite('lc064_02', 2)
    sprite('lc064_03', 2)
    sprite('lc064_04', 2)
    sprite('lc064_05', 2)
    CommonSE('019_cloth_a')
    sprite('lc064_06', 2)
    sprite('lc064_07', 2)
    sprite('lc064_08', 2)
    sprite('lc064_09', 2)
    sprite('lc064_10', 2)
    sprite('lc064_11', 2)
    sprite('lc064_12', 2)
    sprite('lc064_13', 2)
    sprite('lc064_14', 2)


@State
def CmnActVDownUpper():
    sprite('lc062_00', 3)
    label(0)
    sprite('lc062_01', 3)
    sprite('lc062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('lc062_03', 3)
    sprite('lc062_04', 3)


@State
def CmnActVDownDown():
    sprite('lc062_05', 3)
    sprite('lc062_06', 3)
    label(0)
    sprite('lc062_07', 3)
    sprite('lc062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('lc062_09', 2)
    sprite('lc062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('lc062_09', 2)
    sprite('lc062_10', 2)


@State
def CmnActBlowoff():
    sprite('lc072_00', 3)
    sprite('lc072_01', 3)
    sprite('lc072_02', 3)
    label(0)
    sprite('lc072_01', 3)
    sprite('lc072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('lc074_00', 3)
    sprite('lc074_01', 3)
    sprite('lc074_02', 3)
    sprite('lc074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('lc082_00', 2)
    sprite('lc082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('lc071_04', 1)


@State
def CmnActWallBound():
    sprite('lc073_00', 3)
    sprite('lc073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('lc073_02', 3)
    label(0)
    sprite('lc073_03', 3)
    sprite('lc073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('lc070_00', 2)
    sprite('lc070_01', 2)
    sprite('lc070_02', 2)
    label(0)
    sprite('lc070_03', 4)
    sprite('lc070_04', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('lc070_05', 5)
    sprite('lc070_06', 5)
    sprite('lc070_07', 4)
    sprite('lc070_08', 4)
    sprite('lc070_09', 3)
    sprite('lc070_10', 3)


@State
def CmnActUkemiStagger():
    sprite('lc070_11', 3)
    sprite('lc070_12', 2)
    sprite('lc070_13', 2)
    sprite('lc070_14', 1)


@State
def CmnActUkemiAirF():
    sprite('lc113_00', 3)
    sprite('lc113_01', 3)
    sprite('lc113_02', 9)


@State
def CmnActUkemiAirB():
    sprite('lc113_00', 3)
    sprite('lc113_01', 3)
    sprite('lc113_02', 9)


@State
def CmnActUkemiAirN():
    sprite('lc113_00', 3)
    sprite('lc113_01', 3)
    sprite('lc113_02', 9)


@State
def CmnActUkemiLandF():
    sprite('lc110_00', 2)
    sprite('lc110_01', 2)
    sprite('lc110_02', 2)
    sprite('lc110_03', 2)
    sprite('lc110_04', 2)
    sprite('lc110_05', 2)
    sprite('lc110_06', 2)
    sprite('lc110_07', 200)
    sprite('lc110_08', 2)
    sprite('lc110_09', 2)
    sprite('lc110_10', 2)


@State
def CmnActUkemiLandB():
    sprite('lc111_00', 3)
    sprite('lc111_01', 3)
    sprite('lc111_02', 3)
    sprite('lc111_03', 3)
    sprite('lc111_04', 2)
    sprite('lc111_05', 2)
    sprite('lc111_06', 2)
    sprite('lc111_07', 200)
    sprite('lc111_08', 2)
    sprite('lc111_09', 2)
    sprite('lc111_10', 2)


@State
def CmnActUkemiLandN():
    sprite('lc112_00', 2)
    sprite('lc112_01', 2)
    sprite('lc112_02', 2)
    sprite('lc112_03', 2)
    sprite('lc112_04', 2)
    sprite('lc112_05', 2)
    sprite('lc112_06', 2)
    sprite('lc112_07', 2)
    sprite('lc112_08', 2)
    sprite('lc112_09', 2)
    sprite('lc112_10', 2)
    sprite('lc112_11', 2)
    sprite('lc112_12', 7)


@State
def CmnActUkemiLandNLanding():
    sprite('lc024_00', 3)
    sprite('lc024_01', 3)
    sprite('lc024_02', 3)
    sprite('lc024_03', 3)
    sprite('lc024_04', 3)
    sprite('lc024_05', 3)
    sprite('lc024_06', 3)


@State
def CmnActMidGuardPre():
    sprite('lc040_00', 3)
    sprite('lc040_01', 3)


@State
def CmnActMidGuardLoop():
    sprite('lc040_02', 3)


@State
def CmnActMidGuardEnd():
    sprite('lc040_01', 3)
    sprite('lc040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('lc040_03', 3)
    sprite('lc040_02', 3)


@State
def CmnActMidHeavyGuardEnd():
    sprite('lc040_01', 3)
    sprite('lc040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('lc041_00', 3)
    sprite('lc041_01', 3)


@State
def CmnActHighGuardLoop():
    sprite('lc041_02', 3)


@State
def CmnActHighGuardEnd():
    sprite('lc041_01', 3)
    sprite('lc041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('lc041_03', 3)
    sprite('lc041_02', 3)


@State
def CmnActHighHeavyGuardEnd():
    sprite('lc041_01', 3)
    sprite('lc041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('lc043_00', 3)
    sprite('lc043_01', 3)


@State
def CmnActCrouchGuardLoop():
    sprite('lc043_02', 3)


@State
def CmnActCrouchGuardEnd():
    sprite('lc043_01', 3)
    sprite('lc043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('lc043_05', 3)
    sprite('lc043_04', 3)
    sprite('lc043_03', 3)
    sprite('lc043_02', 3)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('lc043_01', 3)
    sprite('lc043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('lc045_00', 3)
    sprite('lc045_01', 3)


@State
def CmnActAirGuardLoop():
    sprite('lc045_02', 3)


@State
def CmnActAirGuardEnd():
    sprite('lc045_01', 3)
    sprite('lc045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('lc045_05', 3)
    sprite('lc045_04', 3)
    sprite('lc045_03', 3)
    sprite('lc045_02', 3)


@State
def CmnActAirHeavyGuardEnd():
    sprite('lc045_01', 3)
    sprite('lc045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('lc090_00', 2)
    sprite('lc090_01', 2)
    sprite('lc090_02', 1)
    SetCommonActionMark(1)
    sprite('lc090_03', 6)
    sprite('lc090_04', 5)


@State
def CmnActGuardBreakCrouch():
    sprite('lc091_00', 2)
    sprite('lc091_01', 2)
    sprite('lc091_02', 1)
    SetCommonActionMark(1)
    sprite('lc091_03', 6)
    sprite('lc091_04', 5)


@State
def CmnActGuardBreakAir():
    sprite('lc092_00', 2)
    sprite('lc092_01', 2)
    sprite('lc092_02', 1)
    SetCommonActionMark(1)
    sprite('lc092_03', 6)
    sprite('lc092_04', 5)


@State
def CmnActLockWait():
    sprite('lc040_02', 1)
    sprite('lc040_01', 3)
    sprite('lc040_00', 3)


@State
def CmnActLockReject():
    sprite('lc312_00', 2)
    sprite('lc312_01', 2)
    sprite('lc312_02', 2)
    sprite('lc312_03', 6)
    sprite('lc312_04', 3)
    sprite('lc312_05', 2)
    sprite('lc312_06', 2)
    sprite('lc312_07', 2)
    sprite('lc312_08', 2)
    sprite('lc312_09', 6)


@State
def CmnActAirLockWait():
    sprite('lc045_02', 1)
    sprite('lc045_01', 3)
    sprite('lc045_00', 3)


@State
def CmnActAirLockReject():
    sprite('lc322_00', 3)
    sprite('lc322_01', 3)
    sprite('lc322_02', 5)
    sprite('lc322_03', 3)
    sprite('lc322_04', 3)
    sprite('lc322_05', 3)
    sprite('lc322_06', 9)


@State
def CmnActLandSpin():
    sprite('lc071_00', 4)
    sprite('lc071_01', 4)
    label(0)
    sprite('lc071_02', 2)
    sprite('lc071_03', 2)
    sprite('lc071_04', 2)
    sprite('lc071_05', 2)
    sprite('lc071_06', 2)
    sprite('lc071_07', 2)
    sprite('lc071_08', 2)
    sprite('lc071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('lc071_10', 6)
    sprite('lc071_11', 5)
    sprite('lc071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('lc071_02', 2)
    sprite('lc071_03', 2)
    sprite('lc071_04', 2)
    sprite('lc071_05', 2)
    sprite('lc071_06', 2)
    sprite('lc071_07', 2)
    sprite('lc071_08', 2)
    sprite('lc071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('lc077_00', 2)
    sprite('lc077_01', 2)
    sprite('lc077_00ex01', 2)
    sprite('lc077_01ex01', 2)
    sprite('lc077_00ex02', 2)
    sprite('lc077_01ex02', 2)
    sprite('lc077_00ex03', 2)
    sprite('lc077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('lc077_02', 4)
    label(0)
    sprite('lc077_03', 3)
    sprite('lc077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('lc077_05', 5)
    sprite('lc077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('lc060_07', 4)
    sprite('lc060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('lc060_11', 5)
    sprite('lc060_12', 4)


@State
def CmnActBurstBegin():
    sprite('lc331_00', 2)
    sprite('lc331_01', 2)
    label(0)
    sprite('lc331_02', 2)
    sprite('lc331_03', 2)
    sprite('lc331_04', 2)
    sprite('lc331_05', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('lc331_06', 3)
    label(0)
    sprite('lc331_07', 3)
    sprite('lc331_08', 3)
    sprite('lc331_09', 3)
    sprite('lc331_10', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('lc331_11', 2)
    sprite('lc331_12', 2)
    sprite('lc331_13', 2)


@State
def CmnActAirBurstBegin():
    sprite('lc332_01', 2)
    label(0)
    sprite('lc332_02', 2)
    sprite('lc332_03', 2)
    sprite('lc332_04', 2)
    sprite('lc332_05', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('lc332_06', 2)
    label(0)
    sprite('lc332_07', 3)
    sprite('lc332_08', 3)
    sprite('lc332_09', 3)
    sprite('lc332_10', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('lc332_11', 3)
    sprite('lc332_12', 3)
    sprite('lc020_05', 3)
    sprite('lc020_06', 3)
    label(0)
    sprite('lc020_07', 4)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    SLOT_62 = 1
    sprite('lc333_00', 3)
    sprite('lc333_01', 3)
    sprite('lc333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('lc333_03', 32767)
    CreateObject('EMB_LC_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('lc333_04', 3)
    ObjectUpon2(11, 44, 0)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('lc333_05', 3)
    sprite('lc333_06', 3)
    sprite('lc333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():

    def upon_STATE_END():
        SLOT_62 = 0
    sprite('lc333_08', 4)
    sprite('lc333_09', 4)
    sprite('lc333_10', 4)


@State
def CmnActAirOverDriveBegin():
    SLOT_62 = 1
    sprite('lc333_11', 3)
    sprite('lc333_12', 3)
    sprite('lc333_13', 3)
    CharacterFlash(16639, 20, 1)
    sprite('lc333_14', 32767)
    CreateObject('EMB_LC_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('lc333_15', 3)
    ObjectUpon2(11, 44, 0)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('lc333_05', 3)
    sprite('lc333_06', 3)
    sprite('lc333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():

    def upon_STATE_END():
        SLOT_62 = 0
    sprite('lc333_16', 4)
    sprite('lc333_17', 4)
    sprite('lc333_18', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('Atk6A_NoRod')
        HitOrBlockCancel('Atk5B_NoRod')
        HitOrBlockCancel('Atk2B_NoRod')
        HitOrBlockCancel('Atk6B_NoRod')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
    sprite('lc200_00', 1)
    PerInertia(60)
    sprite('lc200_01', 2)
    sprite('lc200_02', 1)
    sprite('lc200_03', 1)
    RandomCommonVoiceline(0)
    sprite('lc200_04', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('lc200_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('lc200_06', 4)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(650)
        HitOrBlockJumpCancel(1)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
    sprite('lc201_00', 2)
    ObjectUpon2(11, 36, 0)
    ObjectHitbox(11)
    sprite('lc201_01', 2)
    sprite('lc201_02', 2)
    sprite('lc201_03', 2)
    sprite('lc201_04', 2)
    sprite('lc201_05', 3)
    RandomCommonVoiceline(1)
    sprite('lc201_06', 5)
    Recovery()
    Unknown2063()
    AttackOff()
    sprite('lc201_07', 5)
    sprite('lc201_08', 4)
    sprite('lc201_09', 4)
    sprite('lc201_10', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(550)
        SingleProration(1)
        PushbackX(11500)
        Hitstop(14)
        Hitstun(21)
        StayAfterMovement(1, 0)
        ObjectHitbox(11)
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        HitJumpCancel(1)
        AttackOff()
    sprite('lc202_01', 2)
    ObjectUpon2(11, 19, 0)
    ObjectUpon2(11, 11, 0)
    sprite('lc202_02', 2)
    sprite('lc202_03', 2)
    AddX(50000)
    sprite('lc202_04', 2)
    AddX(50000)
    CreateObject('LcefKikouCharge', 0)
    sprite('lc202_05', 3)
    RandomCommonVoiceline(2)
    sprite('lc202_06', 2)
    sprite('lc202_07', 2)
    sprite('lc202_09ex01', 3)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    CommonSE('008_swing_pole_1')
    RefreshMultihit()
    CreateObject('LcefKikouPtcRod', 1)
    sprite('lc202_10', 3)
    sprite('lc202_11', 3)
    RefreshMultihit()
    PushbackX(23000)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    CommonSE('008_swing_pole_1')
    sprite('lc202_13', 1)
    sprite('lc202_13', 2)
    Recovery()
    Unknown2063()
    sprite('lc202_14', 3)
    AddX(-25000)
    AttackOff()
    sprite('lc202_15', 3)
    AddX(-25000)
    sprite('lc202_16', 3)
    AddX(-25000)
    sprite('lc202_17', 3)
    AddX(-25000)
    sprite('lc202_18', 3)
    sprite('lc202_19', 3)
    sprite('lc202_20', 3)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('Atk6A_NoRod')
        HitOrBlockCancel('Atk5B_NoRod')
        HitOrBlockCancel('Atk2B_NoRod')
        HitOrBlockCancel('Atk6B_NoRod')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
    sprite('lc230_00', 3)
    PerInertia(60)
    sprite('lc230_01', 3)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('lc230_02', 3)
    sprite('lc230_03', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('lc230_04', 4)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        HitLow(2)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
    sprite('lc231_00', 2)
    ObjectUpon2(11, 39, 0)
    sprite('lc231_01', 2)
    sprite('lc231_02', 2)
    sprite('lc231_03', 2)
    sprite('lc231_04', 2)
    sprite('lc231_05', 2)
    sprite('lc231_06', 2)
    sprite('lc231_07', 2)
    sprite('lc231_08', 2)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    ObjectHitbox(11)
    sprite('lc231_09', 2)
    sprite('lc231_10', 2)
    ObjectHitbox(0)
    Recovery()
    Unknown2063()
    sprite('lc231_11', 2)
    sprite('lc231_12', 3)
    sprite('lc231_13', 3)
    sprite('lc231_14', 3)
    sprite('lc231_15', 3)
    sprite('lc231_16', 3)
    sprite('lc231_17', 3)
    sprite('lc231_18', 2)
    sprite('lc231_19', 2)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP2(79)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(9000)
        AirPushbackY(30000)
        AirUntechableTime(30)
        CHAirUntechableTime(62)
        CHAirHitstunAnimation(13)
        CHGroundedHitstunAnimation(13)
        CHAirPushbackX(9000)
        CHAirPushbackY(54000)
        Hitstop(13)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
    sprite('lc232_00', 1)
    physicsXImpulse(10000)
    sprite('lc232_01', 1)
    sprite('lc232_02', 1)
    sprite('lc232_03', 1)
    RandomCommonVoiceline(2)
    ObjectUpon2(11, 3, 0)
    sprite('lc232_04', 2)
    sprite('lc232_05', 3)
    physicsXImpulse(0)
    sprite('lc232_06', 2)
    sprite('lc232_07', 2)
    CreateObject('LcefUpper', 0)
    sprite('lc232_08', 3)
    ObjectHitbox(11)
    CreateParticle('lcef_232airwall01', 0)
    CommonSE('003_swing_grap_0_2')
    sprite('lc232_09', 3)
    Recovery()
    Unknown2063()
    AttackOff()
    sprite('lc232_10', 3)
    sprite('lc232_11', 3)
    ObjectHitbox(0)
    sprite('lc232_12', 3)
    sprite('lc232_13', 3)
    sprite('lc232_14', 3)
    sprite('lc232_15', 3)
    sprite('lc232_16', 3)
    sprite('lc232_17', 2)
    sprite('lc232_18', 2)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(90)
        AttackP2(92)
        Hitstop(14)
        AirUntechableTime(40)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(18000)
        HitLow(2)
        CHHardKnockdown(10)
        EnableEmergencyTechAirHit(1)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('lc234_00', 2)
    ObjectUpon2(11, 40, 0)
    sprite('lc234_01', 2)
    sprite('lc234_02', 2)
    sprite('lc234_03', 2)
    sprite('lc234_04', 2)
    sprite('lc234_05', 2)
    sprite('lc234_06', 2)
    sprite('lc234_07', 2)
    sprite('lc234_08', 3)
    sprite('lc234_09', 4)
    ObjectHitbox(11)
    RandomCommonVoiceline(2)
    sprite('lc234_10', 4)
    sprite('lc234_11', 4)
    sprite('lc234_12', 4)
    ObjectHitbox(0)
    Recovery()
    Unknown2063()
    sprite('lc234_13', 4)
    sprite('lc234_14', 4)
    sprite('lc234_15', 3)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(700)
        AttackP1(90)
        Hitstop(14)
        Blockstun(20)
        AirUntechableTime(42)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(3800)
        AirPushbackY(-60000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(36)
        HitOverhead(2)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        SpecialCancel(0)
        HitOrBlockCancel('NmlAtk4B')
    sprite('lc213_00', 3)
    ObjectUpon2(11, 8, 0)
    sprite('lc213_01', 3)
    sprite('lc213_02', 2)
    sprite('lc213_03', 2)
    sprite('lc213_04', 2)
    sprite('lc213_05', 2)
    sprite('lc213_06', 2)
    sprite('lc213_07', 2)
    sprite('lc210_07', 2)
    sprite('lc210_08', 2)
    sprite('lc210_09', 2)
    CommonSE('003_swing_grap_0_0')
    SmartVoiceline('lc108')
    sprite('lc210_10', 3)
    ObjectHitbox(11)
    sprite('lc210_11', 3)
    Recovery()
    Unknown2063()
    sprite('lc210_12', 3)
    ObjectHitbox(0)
    sprite('lc210_13', 2)
    sprite('lc210_14', 2)
    sprite('lc210_15', 2)
    sprite('lc210_16', 2)
    sprite('lc210_17', 2)
    sprite('lc210_18', 2)
    sprite('lc210_19', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(850)
        AttackP1(100)
        AttackP2(84)
        NonCornerWallbounce(1)
        AirHitstunAnimation(9)
        Wallbounce(1)
        AirPushbackX(20000)
        AirUntechableTime(33)
        AirHitstunAfterWallbounce(40)
        Hitstop(15)
        NonCornerCHWallbounce(0)
        CHAirHitstunAnimation(12)
        CHAirPushbackX(50000)
        CHAirPushbackY(12000)
        CHAirUntechableTime(60)
        CHWallbounce(1)
        CHWallbounceReboundTime(10)
        StayAfterMovement(1, 0)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        HitOrBlockCancel('NmlAtk6C')
        HitJumpCancel(1)
    sprite('lc211_01', 2)
    ObjectUpon2(11, 37, 0)
    sprite('lc211_02', 2)
    sprite('lc211_02', 2)
    sprite('lc211_03', 2)
    sprite('lc211_04', 3)
    sprite('lc211_05', 2)
    sprite('lc211_06', 3)
    loopRest()
    if not SLOT_94:
        if CheckInput(INPUT_HOLD_B):
            conditionalSendToLabel(88)
    sprite('lc211_07', 4)
    CommonSE('003_swing_grap_0_1')
    RandomCommonVoiceline(1)
    ObjectHitbox(11)
    sprite('lc211_08', 2)
    sprite('lc211_09', 2)
    ObjectHitbox(0)
    Recovery()
    Unknown2063()
    sprite('lc211_10', 3)
    sprite('lc211_11', 3)
    sprite('lc211_12', 3)
    sprite('lc211_13', 2)
    sprite('lc211_14', 2)
    sprite('lc211_15', 2)
    loopRest()
    ExitState()
    label(88)
    sprite('lc211_16', 2)
    ObjectUpon2(11, 43, 0)
    sprite('lc211_11', 3)
    sprite('lc211_12', 3)
    sprite('lc211_13', 2)
    sprite('lc211_14', 1)
    sprite('lc211_15', 1)


@State
def NmlAtk4B():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(750)
        AttackP1(80)
        AttackP2(82)
        Hitstop(14)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirUntechableTime(40)
        EnemyHitstopAddition(0, 8, 8)
        AirPushbackX(2000)
        AirPushbackY(30000)
        HitOrBlockCancel('NmlAtk6B')
    sprite('lc261_00', 2)
    ObjectUpon2(11, 46, 0)
    sprite('lc261_01', 5)
    sprite('lc261_02', 6)
    SmartVoiceline('lc110')
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('lc261_03', 2)
    CommonSE('003_swing_grap_0_1')
    sprite('lc261_04', 3)
    ObjectHitbox(11)
    sprite('lc261_05', 4)
    setInvincible(0)
    Recovery()
    Unknown2063()
    ObjectHitbox(0)
    sprite('lc261_06', 4)
    sprite('lc261_07', 4)
    sprite('lc261_08', 4)
    sprite('lc261_09', 6)
    sprite('lc261_10', 6)
    loopRest()


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(350)
        SingleProration(1)
        AttackP2(94)
        Hitstop(0)
        EnemyHitstopAddition(4, 4, 4)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(6)
        AirUntechableTime(38)
        Hitstun(28)
        PushbackX(19800)
        AirPushbackX(8000)
        AirPushbackY(45000)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        SpecialCancel(0)
        StayAfterMovement(1, 0)
        FatalCounter(1)
        if SLOT_94:
            ChainCancel(0)
    sprite('lc214_00', 3)
    ObjectUpon2(11, 38, 0)
    sprite('lc214_01', 4)
    sprite('lc214_03', 3)
    sprite('lc214_04', 3)
    sprite('lc214_05', 3)
    sprite('lc214_06', 3)
    sprite('lc214_07', 3)
    SmartVoiceline('lc109')
    sprite('lc214_08', 3)
    SetXCollisionFromOrigin(200)
    RefreshMultihit()
    sprite('lc214_09', 3)
    RefreshMultihit()
    sprite('lc214_10', 3)
    RefreshMultihit()
    sprite('lc214_11', 3)
    RefreshMultihit()
    GotoState('AN_NmlAtk6C_4th')
    if SLOT_94:

        def upon_OPPONENT_HIT_OR_BLOCK():
            ChainCancel(1)
    sprite('lc214_11', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('lc214_12', 4)
    sprite('lc214_14', 4)
    SetXCollisionFromOrigin(-1)
    sprite('lc214_15', 3)
    sprite('lc214_16', 3)
    sprite('lc214_17', 3)
    sprite('lc214_18', 4)
    sprite('lc214_19', 3)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        AirPushbackY(15000)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('AtkAIR5B_NoRod')
        HitOrBlockCancel('AtkAIR5C_NoRod')
        HitOrBlockCancel('AtkAIR5D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Air')
    sprite('lc250_00', 2)
    sprite('lc250_01', 1)
    sprite('lc250_01', 1)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('lc250_02', 2)
    sprite('lc250_03', 4)
    sprite('lc250_04', 3)
    Recovery()
    Unknown2063()
    sprite('lc250_05', 2)
    sprite('lc250_06', 2)
    sprite('lc250_07', 2)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockJumpCancel(1)
    sprite('lc251_02', 3)
    ObjectUpon2(11, 41, 0)
    sprite('lc251_03', 3)
    sprite('lc251_04', 2)
    sprite('lc251_05', 2)
    sprite('lc251_07', 3)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    ObjectHitbox(11)
    sprite('lc251_08', 3)
    ObjectHitbox(0)
    Recovery()
    Unknown2063()
    sprite('lc251_09', 3)
    sprite('lc251_10', 3)
    sprite('lc251_11', 3)
    sprite('lc251_12', 3)
    sprite('lc251_13', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        Hitstop(13)
        CHAirHitstunAnimation(12)
        CHGroundedHitstunAnimation(12)
        NonCornerWallbounce(1)
        CHAirPushbackX(60000)
        CHAirUntechableTime(80)
        CHWallbounce(1)
        CHWallbounceReboundTime(5)
        ForcedLandingRecovery(5, 1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockJumpCancel(1)
    sprite('lc252_00', 2)
    ObjectUpon2(11, 11, 0)
    sprite('lc252_01', 2)
    sprite('lc252_02', 2)
    sprite('lc252_03', 2)
    sprite('lc252_04', 2)
    sprite('lc252_05', 2)
    sprite('lc252_06', 2)
    RandomCommonVoiceline(2)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    CommonSE('008_swing_pole_2')
    sprite('lc252_07', 2)
    sprite('lc252_08', 2)
    sprite('lc252_09', 2)
    Recovery()
    Unknown2063()
    sprite('lc252_10', 2)
    sprite('lc252_11', 2)
    sprite('lc252_12', 2)
    sprite('lc252_13', 2)
    sprite('lc252_14', 2)
    sprite('lc252_15', 2)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        AttackOff()
    sprite('lc203_00', 2)
    sprite('lc203_01', 2)
    sprite('lc203_02', 2)
    sprite('lc203_03', 2)
    sprite('lc203_04', 3)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 1, 0)
    SmartVoiceline('lc106')
    sprite('lc203_05', 5)
    sprite('lc203_06', 3)
    sprite('lc203_07', 3)
    sprite('lc203_08', 3)
    sprite('lc203_09', 2)


@State
def NmlAtk4D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        BonusProration(110)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(6000)
        Floorslide(30)
        AirUntechableTime(40)
        MoveAttributes(1, 0, 0, 0, 0)
        HitOverhead(2)
        HitAirUnblockable(0)
        StarterRating(2)
        SpecialCancel(0)
        StayAfterMovement(1, 0)
        EnableCollision(1)
        ExternalForcesRate(0, 0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
    sprite('lc216_00', 3)
    SmartVoiceline('lc101')
    ObjectUpon2(11, 11, 0)
    sprite('lc216_01', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('lc216_02', 3)
    sprite('lc216_02', 3)
    sprite('lc216_03', 3)
    sprite('lc216_04', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    sprite('lc216_05', 2)
    CommonSE('003_swing_grap_0_2')
    sprite('lc216_06', 2)
    sprite('lc216_07', 9)
    CreateObject('LcefRodSetNotPosLink', 0)
    ObjectUpon2(11, 4, 0)
    RandomCommonVoiceline(2)
    AddY(70000)
    physicsXImpulse(28000)
    physicsYImpulse(9000)
    setGravity(1700)
    sprite('lc216_08', 2)
    setInvincible(0)
    CommonSE('003_swing_grap_0_1')
    Recovery()
    Unknown2063()
    XImpulseAcceleration(70)
    sprite('lc216_09', 2)
    XImpulseAcceleration(70)
    sprite('lc216_10', 3)
    XImpulseAcceleration(70)
    sprite('lc216_11', 10)
    loopRest()
    label(1)
    clearUponHandler(LANDING)
    sprite('lc024_01', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc024_02', 2)
    sprite('lc024_03', 1)
    sprite('lc024_04', 1)
    sprite('lc024_05', 1)
    sprite('lc024_06', 1)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(600)
        AttackP2(84)
        SingleProration(1)
        PushbackX(8000)
        StayAfterMovement(1, 0)
        AirPushbackX(15000)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(2400)
        AirUntechableTime(31)
        SpecialCancel(1)
        FatalCounter(1)
        if SLOT_94:
            SpecialCancel(0)
    sprite('lc215_00', 3)
    physicsXImpulse(-2000)
    LandingEffects(100, 1, 0)
    EnableAfterimage(1)
    SmartVoiceline('lc101')
    sprite('lc215_01', 3)
    sprite('lc215_02', 3)
    sprite('lc215_02', 5)
    EndMomentum(0)
    sprite('lc215_03', 3)
    CreateObject('LcefTetsuzanko', 0)
    DashEffects(100, 1, 0)
    physicsXImpulse(72000)
    CommonSE('003_swing_grap_0_2')
    sprite('lc215_04', 3)
    physicsXImpulse(36000)
    sprite('lc215_05', 3)
    if SLOT_94:
        SpecialCancel(1)
    physicsXImpulse(19000)
    sprite('lc215_06', 2)
    physicsXImpulse(12000)
    ObjectUpon2(11, 11, 0)
    sprite('lc215_07', 1)
    EnableAfterimage(0)
    EndMomentum(0)
    sprite('lc215_08', 1)
    SmartVoiceline('lc100')
    CommonSE('005_swing_grap_2_2')
    Damage(600)
    Hitstun(25)
    AirUntechableTime(31)
    SpecialCancel(0)
    AirPushbackX(40000)
    AirPushbackY(4000)
    PushbackX(6000)
    Blockstun(24)
    HardKnockdown(0)
    SpecialCancel(0)
    AirHitstunAnimation(12)
    NonCornerWallbounce(1)
    Wallstick(1)
    WallstickDuration(20)
    AirHitstunAfterWallbounce(50)
    sprite('lc215_09', 5)
    RefreshMultihit()
    sprite('lc215_10', 3)
    Recovery()
    Unknown2063()
    sprite('lc215_11', 1)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 6, 0)
    sprite('lc215_11', 3)
    sprite('lc215_12', 3)
    AddX(-40000)
    sprite('lc215_13', 3)
    sprite('lc215_14', 4)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        PreventBlocking(1)
        AttackOff()
    sprite('lc233_00', 2)
    sprite('lc233_01', 2)
    sprite('lc233_02', 2)
    sprite('lc233_03', 2)
    sprite('lc233_04', 2)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 13, 0)
    SmartVoiceline('lc106')
    sprite('lc233_05', 3)
    sprite('lc233_06', 2)
    sprite('lc233_07', 2)
    sprite('lc233_08', 2)
    sprite('lc233_09', 2)
    sprite('lc233_10', 2)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        PushSpeedX()
        PushSpeedY()
        AttackDefaults_AirNormal()
        AttackOff()
        ForcedLandingRecovery(5, 1)
    sprite('lc253_00', 3)
    ObjectUpon2(11, 11, 0)
    sprite('lc253_01', 2)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(60)
    YAccel(10)
    YSpeed(8000)
    setGravity(800)
    sprite('lc253_02', 2)
    EndMomentum(1)
    setGravity(0)
    sprite('lc253_03', 2)
    sprite('lc253_04', 2)
    sprite('lc253_05', 2)
    sprite('lc253_06', 2)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 32, 0)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(1500)
    SmartVoiceline('lc106')
    sprite('lc253_08', 2)
    sprite('lc253_09', 3)
    sprite('lc253_10', 3)
    sprite('lc253_11', 3)
    sprite('lc253_12', 3)
    WhiffCancel('JumpToRod_Ride')
    WhiffCancel('JumpToRod_Kick')
    WhiffCancel('JumpToRod_Jump')
    sprite('lc253_13', 2)
    sprite('lc033_07ex00', 2)
    sprite('lc033_08ex00', 2)
    sprite('lc033_09ex00', 2)
    sprite('lc033_10ex00', 2)
    sprite('lc253_14', 2)
    sprite('lc253_15', 2)
    sprite('lc253_16', 2)


@State
def NmlAtkAIR2D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AirPushbackX(0)
        AirPushbackY(-65000)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(10)
        HitOverhead(0)
        SpecialCancel(0)
    sprite('lc260_00', 3)
    ObjectUpon2(11, 11, 0)
    sprite('lc260_01', 2)
    sprite('lc260_02', 2)
    sprite('lc260_03', 2)
    EndMomentum(1)
    SetXCollisionFromOrigin(50)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc260_04', 2)
    SmartVoiceline('lc103')
    setGravity(2000)
    sprite('lc260_05', 3)
    sprite('lc260_06', 2)
    sprite('lc260_07', 3)
    CommonSE('008_swing_pole_1')
    physicsYImpulse(-40000)
    label(0)
    sprite('lc260_08', 3)
    CommonSE('008_swing_pole_1')
    sprite('lc260_09', 3)
    CommonSE('008_swing_pole_1')
    sprite('lc260_10', 3)
    CommonSE('008_swing_pole_1')
    sprite('lc260_07', 3)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc260_11', 2)
    SmartVoiceline('lc106')
    CommonSE('003_swing_grap_0_2')
    LandingEffects(100, 1, 1)
    sprite('lc260_12', 2)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 30, 0)
    CommonSE('204_runjump_normal_0')
    sprite('lc260_13', 2)
    SetXCollisionFromOrigin(-1)
    sprite('lc260_14', 2)
    sprite('lc260_15', 2)
    AttackLevel_(3)
    Hitstop(8)
    HitOverhead(0)
    HitLow(2)
    MoveAttributes(0, 0, 1, 0, 0)
    PushbackX(-14000)
    RefreshMultihit()
    GroundedHitstunAnimation(0)
    sprite('lc260_16', 2)
    Recovery()
    Unknown2063()
    sprite('lc260_17', 2)
    sprite('lc260_18', 2)
    sprite('lc260_19', 2)


@State
def Atk5B_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(500)
        AirUntechableTime(19)
        Hitstop(8)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk6A_NoRod')
        HitOrBlockCancel('Atk6B_NoRod')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk2B_NoRod')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk6C_NoRod')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk5B_NoRod')
    sprite('lc201_00', 1)
    sprite('lc201_01', 2)
    sprite('lc201_02', 2)
    sprite('lc201_03', 1)
    sprite('lc201_04', 1)
    sprite('lc201_05', 3)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('lc201_06', 4)
    Recovery()
    Unknown2063()
    sprite('lc201_07', 3)
    sprite('lc201_08', 3)
    sprite('lc201_09', 2)
    sprite('lc201_10', 2)


@State
def Atk5C_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        ProjectileLevel(1)
        Damage(700)
        UseSlashHitspark(1)
        PushbackX(30000)
        CHGroundedHitstunAnimation(2)
        StayAfterMovement(1, 0)
        Hitstop(10)
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk5C_NoRod')
    sprite('lc202_01', 2)
    sprite('lc202_02', 2)
    sprite('lc202_03', 2)
    AddX(50000)
    sprite('lc202_04', 2)
    AddX(50000)
    CreateObject('LcefKikouCharge', 0)
    sprite('lc202_05', 2)
    RandomCommonVoiceline(2)
    sprite('lc202_06', 2)
    sprite('lc202_07', 2)
    sprite('lc202_09', 3)
    CommonSE('004_swing_grap_1_2')
    CommonSE('016_explode_0')
    CreateObject('LcefKikouPtc', 0)
    CreateObject('LcefKikouWave', 0)
    CreateParticle('lcef_202airwall01', 1)
    sprite('lc202_10', 3)
    Recovery()
    Unknown2063()
    sprite('lc202_11', 3)
    sprite('lc202_13', 3)
    sprite('lc202_14', 3)
    AddX(-25000)
    sprite('lc202_15', 3)
    AddX(-25000)
    sprite('lc202_16', 3)
    AddX(-25000)
    sprite('lc202_17', 3)
    AddX(-25000)
    sprite('lc202_18', 3)
    sprite('lc202_19', 3)
    sprite('lc202_20', 3)


@State
def Atk2B_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(450)
        HitLow(2)
        AttackP1(90)
        Hitstop(8)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk5B_NoRod')
        HitOrBlockCancel('Atk6B_NoRod')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk2B_NoRod_OD')
    sprite('lc231_00', 1)
    sprite('lc231_01', 1)
    sprite('lc231_02', 2)
    sprite('lc231_03', 2)
    sprite('lc231_04', 2)
    sprite('lc231_05', 1)
    sprite('lc231_06', 1)
    sprite('lc231_07', 1)
    sprite('lc231_08', 2)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('lc231_09', 2)
    Recovery()
    Unknown2063()
    sprite('lc231_10', 2)
    sprite('lc231_11', 2)
    sprite('lc231_12', 2)
    sprite('lc231_13', 2)
    sprite('lc231_14', 2)
    sprite('lc231_15', 2)
    sprite('lc231_16', 2)
    sprite('lc231_17', 2)
    sprite('lc231_18', 2)
    sprite('lc231_19', 2)


@State
def Atk2C_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(650)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        StayAfterMovement(1, 0)
        Hitstop(10)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk6C_NoRod')
        HitOrBlockCancel('Atk3C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk2C_NoRod_OD')
    sprite('lc232_00', 1)
    physicsXImpulse(10000)
    sprite('lc232_01', 1)
    sprite('lc232_02', 1)
    sprite('lc232_03', 1)
    RandomCommonVoiceline(2)
    sprite('lc232_04', 1)
    sprite('lc232_05', 2)
    physicsXImpulse(0)
    sprite('lc232_06', 2)
    sprite('lc232_07', 2)
    CreateObject('LcefUpper', 0)
    sprite('lc232_08', 3)
    CreateParticle('lcef_232airwall01', 0)
    CommonSE('003_swing_grap_0_2')
    sprite('lc232_09', 3)
    Recovery()
    Unknown2063()
    sprite('lc232_10', 3)
    sprite('lc232_11', 3)
    sprite('lc232_12', 1)
    sprite('lc232_13', 1)
    sprite('lc232_14', 1)
    sprite('lc232_15', 1)
    sprite('lc232_16', 2)
    sprite('lc232_17', 2)
    sprite('lc232_18', 2)


@State
def Atk3C_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Hitstop(10)
        Damage(650)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(15000)
        AirUntechableTime(40)
        CHHardKnockdown(3)
        EnableEmergencyTechAirHit(1)
        AttackP1(90)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk3C_NoRod')
    sprite('lc236_00', 2)
    sprite('lc236_01', 3)
    sprite('lc236_02', 3)
    SmartVoiceline('lc108')
    sprite('lc236_03', 3)
    SetXCollisionFromOrigin(150)
    sprite('lc236_04', 3)
    CommonSE('019_cloth_b')
    CommonSE('003_swing_grap_0_2')
    SetXCollisionFromOrigin(200)
    sprite('lc236_06', 3)
    sprite('lc236_07', 3)
    Recovery()
    Unknown2063()
    sprite('lc236_08', 3)
    sprite('lc236_10', 3)
    sprite('lc236_11', 3)
    sprite('lc236_12', 3)
    SetXCollisionFromOrigin(-1)
    sprite('lc236_13', 3)
    sprite('lc236_14', 3)


@State
def Atk6A_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(550)
        AttackP1(90)
        Hitstop(10)
        AirUntechableTime(26)
        GroundedHitstunAnimation(3)
        AirPushbackY(-24000)
        HardKnockdown(10)
        HitOverhead(2)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk6A_NoRod')
    sprite('lc210_00', 2)
    sprite('lc210_01', 3)
    sprite('lc210_02', 2)
    sprite('lc210_03', 2)
    sprite('lc210_04', 2)
    sprite('lc210_05', 2)
    sprite('lc210_06', 2)
    sprite('lc210_07', 2)
    sprite('lc210_08', 2)
    sprite('lc210_09', 2)
    CommonSE('003_swing_grap_0_1')
    SmartVoiceline('lc108')
    sprite('lc210_10', 3)
    sprite('lc210_11', 2)
    Recovery()
    Unknown2063()
    sprite('lc210_12', 2)
    sprite('lc210_13', 2)
    sprite('lc210_14', 2)
    sprite('lc210_15', 2)
    sprite('lc210_16', 2)
    sprite('lc210_17', 2)
    sprite('lc210_18', 2)
    sprite('lc210_19', 2)


@State
def Atk6B_NoRod():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(660)
        Hitstop(8)
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Atk4B_NoRod')
        HitOrBlockCancel('Atk5C_NoRod')
        HitOrBlockCancel('Atk2C_NoRod')
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk6B_NoRod')
    sprite('lc211_01', 2)
    sprite('lc211_02', 2)
    sprite('lc211_03', 2)
    sprite('lc211_04', 4)
    sprite('lc211_05', 3)
    sprite('lc211_06', 3)
    loopRest()
    if not SLOT_94:
        if CheckInput(INPUT_HOLD_B):
            conditionalSendToLabel(88)
    sprite('lc211_07', 4)
    CommonSE('003_swing_grap_0_2')
    RandomCommonVoiceline(1)
    sprite('lc211_08', 2)
    Recovery()
    Unknown2063()
    sprite('lc211_09', 2)
    sprite('lc211_10', 3)
    sprite('lc211_11', 3)
    sprite('lc211_12', 3)
    sprite('lc211_13', 3)
    sprite('lc211_14', 3)
    sprite('lc211_15', 3)
    loopRest()
    ExitState()
    label(88)
    sprite('lc211_16', 3)
    sprite('lc211_11', 2)
    sprite('lc211_12', 2)
    sprite('lc211_13', 1)
    sprite('lc211_14', 1)
    sprite('lc211_15', 1)


@State
def Atk4B_NoRod():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AttackP2(89)
        AirHitstunAnimation(18)
        AirUntechableTime(42)
        AirPushbackX(2000)
        AirPushbackY(35000)
        Hitstop(8)
        callSubroutine('ODChain_Land')
        AttackOffOrBlockCancel('Atk4B_NoRod')
    sprite('lc261_00', 2)
    sprite('lc261_01', 4)
    sprite('lc261_02', 5)
    SmartVoiceline('lc110')
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('lc261_03', 2)
    CommonSE('003_swing_grap_0_1')
    sprite('lc261_04', 3)
    sprite('lc261_05', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('lc261_06', 3)
    sprite('lc261_07', 3)
    sprite('lc261_08', 3)
    sprite('lc261_09', 4)
    sprite('lc261_10', 4)
    loopRest()


@State
def Atk6C_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(540)
        AttackP1(90)
        SingleProration(1)
        BonusProration(110)
        Hitstop(10)
        AirUntechableTime(41)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        AirPushbackX(2000)
        AirPushbackY(32000)
        PushbackX(9000)
        Stagger(37)
        Crumple(29)
        ExternalForcesRate(100, 0)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        HitOrBlockCancel('Atk5D_NoRod')
        HitOrBlockCancel('Atk2D_NoRod')
        HitOrBlockCancel('AtkAIR5D_NoRod')
    sprite('lc212_01', 4)
    sprite('lc212_02', 4)
    sprite('lc212_03', 2)
    physicsXImpulse(3000)
    sprite('lc212_05', 2)
    physicsXImpulse(0)
    SmartVoiceline('lc102')
    CommonSE('004_swing_grap_1_1')
    sprite('lc212_06', 2)
    sprite('lc212_07', 2)
    sprite('lc212_08', 2)
    sprite('lc212_09', 2)
    sprite('lc212_10', 2)
    sprite('lc212_11', 3)
    physicsXImpulse(8000)
    physicsYImpulse(16000)
    setGravity(1450)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc212_12', 3)
    sprite('lc212_14', 3)
    sprite('lc212_15', 3)
    sprite('lc212_16', 3)
    sprite('lc212_17', 3)
    SmartVoiceline('lc109')
    CommonSE('003_swing_grap_0_2')
    Damage(750)
    GroundedHitstunAnimation(10)
    AirPushbackX(10000)
    AirPushbackY(-35000)
    YImpulseBeforeWallbounce(0)
    HardKnockdown(15)
    EnableEmergencyTechAirHit(1)
    HitOverhead(2)
    MoveAttributes(1, 0, 0, 0, 0)
    HitAirUnblockable(0)
    RefreshMultihit()
    sprite('lc212_18', 3)
    Recovery()
    Unknown2063()
    sprite('lc212_19', 40)
    loopRest()
    label(1)
    clearUponHandler(LANDING)
    sprite('lc212_20', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc212_21', 3)


@State
def AtkAIR5B_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        AirPushbackY(31000)
        AirUntechableTime(20)
        Hitstop(9)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('AtkAIR5C_NoRod')
        HitOrBlockCancel('AtkAIR5D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Air')
        AttackOffOrBlockCancel('AtkAIR5B_NoRod')
    sprite('lc251_02', 2)
    sprite('lc251_03', 2)
    sprite('lc251_04', 2)
    sprite('lc251_05', 2)
    sprite('lc251_07', 4)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('lc251_08', 2)
    Recovery()
    Unknown2063()
    sprite('lc251_09', 2)
    sprite('lc251_10', 2)
    sprite('lc251_11', 2)
    sprite('lc251_12', 2)
    sprite('lc251_13', 2)


@State
def AtkAIR5C_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        Hitstop(9)
        AirPushbackX(26000)
        AirPushbackY(-18000)
        AirUntechableTime(56)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('AtkAIR5B_NoRod')
        HitOrBlockCancel('AtkAIR5D_NoRod')
        HitOrBlockJumpCancel(1)
        callSubroutine('ODChain_Air')
        AttackOffOrBlockCancel('AtkAIR5C_NoRod')
    sprite('lc254_00', 1)
    sprite('lc254_01', 2)
    sprite('lc254_02', 2)
    sprite('lc254_03', 2)
    sprite('lc254_04', 2)
    sprite('lc254_05', 1)
    sprite('lc254_06', 1)
    sprite('lc254_07', 3)
    CommonSE('019_cloth_c')
    CommonSE('003_swing_grap_0_2')
    RandomCommonVoiceline(2)
    sprite('lc254_08', 2)
    Recovery()
    Unknown2063()
    sprite('lc254_09', 2)
    sprite('lc254_10', 2)
    sprite('lc254_11', 2)
    sprite('lc254_12', 2)
    sprite('lc254_13', 2)
    sprite('lc254_14', 2)
    sprite('lc254_15', 2)
    sprite('lc254_16', 2)
    sprite('lc254_17', 2)
    sprite('lc254_18', 2)


@State
def Atk5D_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        AttackOff()
    sprite('lc205_00', 2)
    sprite('lc205_01', 2)
    sprite('lc205_02', 3)
    sprite('lc205_03', 4)
    CreateObject('LcefRodReturn', 0)
    ObjectUpon2(11, 2, 0)
    SmartVoiceline('lc107')
    sprite('lc205_04', 3)
    sprite('lc205_05', 3)
    sprite('lc205_06', 3)
    sprite('lc205_07', 3)
    WhiffCrouchCancel(1)
    WhiffFWalkCancel(1)
    WhiffFDashCancel(1)
    WhiffBWalkCancel(1)
    WhiffBDashCancel(1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffOverdriveCancel(1)
    WhiffJumpCancel(1)
    WhiffStandingTurnCancel(1)
    WhiffCrouchBlockCancel(1)
    WhiffBlockCancel(1)
    WhiffBarrierCancel2(1)
    EnablePreGuard(1)
    sprite('lc205_08', 3)
    sprite('lc205_09', 2)
    sprite('lc205_10', 2)
    sprite('lc205_11', 3)
    sprite('lc205_12', 3)
    sprite('lc205_13', 3)
    sprite('lc205_14', 3)
    sprite('lc205_15', 3)
    sprite('lc205_16', 3)


@State
def Atk2D_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        PreventBlocking(1)
        AttackOff()
    sprite('lc235_00', 2)
    sprite('lc235_01', 2)
    sprite('lc235_02', 2)
    sprite('lc235_03', 2)
    sprite('lc235_04', 3)
    CreateObject('LcefRodReturn', 0)
    ObjectUpon2(11, 2, 0)
    SmartVoiceline('lc107')
    sprite('lc235_05', 2)
    sprite('lc235_06', 2)
    sprite('lc235_07', 2)
    sprite('lc235_08', 2)
    sprite('lc235_09', 1)
    sprite('lc235_09', 1)
    WhiffCrouchCancel(1)
    WhiffFWalkCancel(1)
    WhiffFDashCancel(1)
    WhiffBWalkCancel(1)
    WhiffBDashCancel(1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffOverdriveCancel(1)
    WhiffJumpCancel(1)
    WhiffStandingTurnCancel(1)
    WhiffCrouchBlockCancel(1)
    WhiffBlockCancel(1)
    WhiffBarrierCancel2(1)
    EnablePreGuard(1)
    sprite('lc235_10', 2)
    sprite('lc235_11', 2)
    sprite('lc235_12', 2)
    sprite('lc235_13', 1)
    sprite('lc235_14', 1)
    sprite('lc235_15', 1)


@State
def AtkAIR5D_NoRod():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        ForcedLandingRecovery(8, 1)
    sprite('lc255_00', 2)
    sprite('lc255_01', 2)
    sprite('lc255_02', 2)
    EndMomentum(1)
    setGravity(0)
    sprite('lc255_03', 2)
    sprite('lc255_04', 2)
    sprite('lc255_05', 2)
    CreateObject('LcefRodReturn', 0)
    ObjectUpon2(11, 2, 0)
    SmartVoiceline('lc107')
    sprite('lc255_06', 1)
    sprite('lc255_07', 1)
    sprite('lc255_08', 2)
    sprite('lc255_09', 2)
    sprite('lc255_10', 2)
    sprite('lc255_11', 2)
    EndYPhysicsImpulse()
    sprite('lc255_12', 2)
    sprite('lc255_13', 2)
    sprite('lc255_14', 2)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffFAirDashCancel(1)
    WhiffBAirDashCancel(1)
    sprite('lc255_15', 2)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('lc300_00', 5)
    sprite('lc300_01', 5)
    if random_(2, 0, 50):
        Voiceline('lc404')
    else:
        Voiceline('lc405')
    sprite('lc300_02', 5)
    sprite('lc300_03', 5)
    sprite('lc300_04', 5)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 5)
    sprite('lc300_06', 5)
    sprite('lc300_07', 5)
    sprite('lc300_08', 5)
    sprite('lc300_09', 5)
    sprite('lc300_10', 5)
    sprite('lc300_11', 5)
    sprite('lc300_12', 5)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        StayAfterMovement(1, 0)
        EndMomentum(1)
    sprite('lc211_01', 2)
    sprite('lc211_02', 2)
    sprite('lc211_03', 2)
    sprite('lc211_04', 2)
    sprite('lc211_05', 2)
    sprite('lc211_06', 2)
    sprite('lc211_07ex00', 2)
    sprite('lc211_08', 2)
    sprite('lc211_08', 6)
    AttackOff()
    sprite('lc211_09', 4)
    sprite('lc211_10', 4)
    sprite('lc211_11', 4)
    sprite('lc211_12', 4)
    sprite('lc211_13', 4)
    sprite('lc211_14', 4)
    sprite('lc211_15', 4)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(60)
        HardKnockdown(1)
        GroundBounce(1)
        BouncePercentage(30)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        UseFireHitspark(1)
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
    sprite('lc420_00', 3)
    sprite('lc420_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    Voiceline('lc159')
    HeatChange(-2500)
    sprite('lc420_01', 2)
    CharacterFlash(16763080, 8, 2)
    CreateObject('GuardCrushDragon', -1)
    loopRest()
    label(100)
    sprite('lc420_02', 3)
    sprite('lc420_03', 3)
    sprite('lc420_04', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('lc420_05', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('lc420_06', 2)
    TriggerUponForState('GuardCrushDragon', 32)
    CommonSE('004_swing_grap_1_1')
    CommonSE('004_swing_grap_1_0')
    sprite('lc420_07', 2)
    sprite('lc420_08', 2)
    StartMultihit()
    sprite('lc420_08', 1)
    sprite('lc420_09', 5)
    EnableAfterimage(0)
    sprite('lc420_10', 5)
    sprite('lc420_11', 5)
    sprite('lc420_12', 5)
    sprite('lc420_13', 3)
    sprite('lc420_14', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('lc310_00', 3)
    sprite('lc310_01', 3)
    sprite('lc310_02', 3)
    sprite('lc310_03', 3)
    SmartVoiceline('lc155')
    CommonSE('003_swing_grap_0_0')
    sprite('lc310_04', 8)
    StartMultihit()
    sprite('lc310_05', 3)
    sprite('lc310_06', 3)
    sprite('lc310_07', 3)
    sprite('lc310_08', 3)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(40)
        Crumple(35)
        AirUntechableTime(40)
        AttackP2(100)
        SpecialCancel(0)
        callSubroutine('RodNoHit')

        def upon_STATE_END():
            TriggerUponForState('RodReturn', 40)
    sprite('lc310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('lc311_00', 3)
    Voiceline('lc153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('lc311_01', 4)
    sprite('lc311_02', 3)
    sprite('lc311_03', 3)
    sprite('lc311_03', 3)
    sprite('lc311_05', 3)
    sprite('lc311_06', 3)
    sprite('lc311_07', 4)
    AttackLevel_(3)
    Damage(1500)
    AttackP2(50)
    AirPushbackX(10000)
    AirPushbackY(35000)
    PushbackX(50000)
    AirUntechableTime(45)
    Hitstun(45)
    GroundedHitstunAnimation(9)
    StarterRating(2)
    RefreshMultihit()
    Voiceline('lc113')

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SpecialCancel(1)
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
        TriggerUponForState('RodReturn', 40)
    sprite('lc311_08', 3)
    sprite('lc311_09', 3)
    sprite('lc311_10', 3)
    sprite('lc311_11', 3)
    sprite('lc311_12', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('lc310_00', 3)
    sprite('lc310_01', 3)
    sprite('lc310_02', 3)
    sprite('lc310_03', 3)
    SmartVoiceline('lc155')
    CommonSE('003_swing_grap_0_0')
    sprite('lc310_04', 8)
    StartMultihit()
    sprite('lc310_05', 3)
    sprite('lc310_06', 3)
    sprite('lc310_07', 3)
    sprite('lc310_08', 3)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(3)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-12000)
        AirPushbackY(40000)
        YImpulseBeforeWallbounce(1600)
        Hitstop(0)
        AirUntechableTime(62)
        StarterRating(2)
        SpecialCancel(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
    sprite('lc310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('lc313_00', 3)
    Voiceline('lc153')
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_01', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_02', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_03', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_04', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_05', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_06', 3)
    OppThrowAnimation(7, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('lc313_07', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_08', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_09', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_10', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_11', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_12', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc313_13', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    RefreshMultihit()
    Voiceline('lc113')
    sprite('lc313_14', 3)
    sprite('lc313_15', 3)
    sprite('lc313_16', 3)
    sprite('lc313_17', 3)
    sprite('lc313_18', 3)
    sprite('lc313_19', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('lc320_00', 3)
    sprite('lc320_01', 3)
    sprite('lc320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('lc320_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('lc320_04', 3)
    sprite('lc320_05', 7)
    SmartVoiceline('lc155')
    sprite('lc320_06', 6)
    sprite('lc320_07', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SetZLine(1, 50)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AttackLevel_(3)
        Damage(1500)
        AttackP2(50)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(-50000)
        AirUntechableTime(60)
        HardKnockdown(3)
        GroundBounce(1)
        BouncePercentage(50)
        StarterRating(2)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        ForcedLandingRecovery(0, 0)
    sprite('lc321_00', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('lc321_01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    SmartVoiceline('lc154')
    sprite('lc321_02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_04', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_06', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_07', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_08', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_09', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('lc321_10', 4)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('lc114')
    sprite('lc321_11', 4)
    sprite('lc321_12', 4)
    sprite('lc321_13', 4)


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Hitstop(9)
        AirUntechableTime(34)
        MoveAttributes(0, 0, 1, 0, 0)
        AirPushbackX(8000)
        AirPushbackY(23000)
        callSubroutine('AssaultChain')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc405_00', 2)
    sprite('lc405_01', 2)
    sprite('lc405_02', 2)
    physicsXImpulse(15000)
    CommonSE('019_cloth_b')
    DashEffects(100, 1, 1)
    sprite('lc405_03', 2)
    sprite('lc405_04', 2)
    sprite('lc405_05', 3)
    CommonSE('003_swing_grap_0_1')
    CommonSE('019_cloth_a')
    XImpulseAcceleration(80)
    Voiceline('lc207')
    sprite('lc405_06', 2)
    XImpulseAcceleration(80)
    Recovery()
    if SLOT_51:
        Voiceline('lc300')
    sprite('lc405_07', 2)
    XImpulseAcceleration(80)
    sprite('lc405_08', 2)
    XImpulseAcceleration(80)
    sprite('lc405_09', 2)
    physicsXImpulse(0)
    sprite('lc405_10', 2)
    sprite('lc405_11', 2)
    sprite('lc405_12', 2)
    sprite('lc405_13', 2)
    sprite('lc405_14', 2)
    sprite('lc405_15', 2)


@State
def Assault2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        Hitstop(9)
        AirUntechableTime(41)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(16000)
        AirPushbackY(-70000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(30)
        CHHardKnockdown(10)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        StarterRating(2)
        callSubroutine('AssaultChain')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc406_00', 2)
    sprite('lc406_01', 2)
    sprite('lc406_02', 2)
    sprite('lc406_03', 2)
    sprite('lc406_04', 2)
    JumpEffects(0, -1)
    sprite('lc406_05', 2)
    CommonSE('019_cloth_b')
    physicsXImpulse(16000)
    physicsYImpulse(20000)
    setGravity(1800)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 2)
    sprite('lc406_06', 2)
    sprite('lc406_07', 2)
    sprite('lc406_08', 3)
    CommonSE('019_cloth_c')
    CommonSE('003_swing_grap_0_1')
    sprite('lc406_09', 3)
    sprite('lc406_10', 3)
    Voiceline('lc208')
    sprite('lc406_11', 3)
    sprite('lc406_12', 2)
    Recovery()
    if SLOT_51:
        Voiceline('lc300')
    sprite('lc406_13', 2)
    sprite('lc406_14', 32767)
    loopRest()
    label(2)
    clearUponHandler(LANDING)
    sprite('lc406_15', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc406_16', 3)
    AttackOffCancel('JumpToRod_Ride')
    AttackOffCancel('JumpToRod_Kick')
    AttackOffCancel('JumpToRod_Jump')
    sprite('lc405_13', 3)
    sprite('lc405_14', 3)
    sprite('lc405_15', 2)


@State
def AirAssault2():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        Hitstop(9)
        AirUntechableTime(41)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(19000)
        AirPushbackY(-70000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(30)
        CHHardKnockdown(10)
        MoveAttributes(1, 0, 0, 0, 0)
        HitOverhead(2)
        StarterRating(2)
        callSubroutine('AssaultChain')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc406_01', 2)
    AddY(30000)
    physicsXImpulse(16000)
    physicsYImpulse(30000)
    setGravity(1800)
    if SLOT_59 == 1:
        physicsXImpulse(16000)
        physicsYImpulse(24000)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc406_02', 2)
    sprite('lc406_03', 2)
    sprite('lc406_04', 2)
    sprite('lc406_05', 2)
    CommonSE('019_cloth_b')
    sprite('lc406_06', 3)
    sprite('lc406_07', 3)
    sprite('lc406_08', 3)
    CommonSE('019_cloth_c')
    CommonSE('003_swing_grap_0_2')
    sprite('lc406_09', 3)
    sprite('lc406_10', 3)
    Voiceline('lc208')
    sprite('lc406_11', 3)
    sprite('lc406_12', 2)
    Recovery()
    if SLOT_51:
        Voiceline('lc300')
    XImpulseAcceleration(80)
    sprite('lc406_13', 2)
    XImpulseAcceleration(80)
    sprite('lc406_14', 3)
    XImpulseAcceleration(80)
    sprite('lc020_06', 4)
    XImpulseAcceleration(80)
    loopRest()
    label(0)
    sprite('lc020_07', 4)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc406_15', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc406_16', 3)
    AttackOffCancel('JumpToRod_Ride')
    AttackOffCancel('JumpToRod_Kick')
    AttackOffCancel('JumpToRod_Jump')
    sprite('lc405_13', 3)
    sprite('lc405_14', 3)
    sprite('lc405_15', 2)


@State
def Assault3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        Hitstop(9)
        AirUntechableTime(47)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(38000)
        HitAirUnblockable(2)
        callSubroutine('AssaultChain')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc407_00', 2)
    sprite('lc407_01', 3)
    JumpEffects(0, -1)
    sprite('lc407_02', 2)
    CommonSE('019_cloth_b')
    physicsXImpulse(8500)
    physicsYImpulse(21000)
    setGravity(1500)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc407_03', 2)
    Voiceline('lc209')
    sprite('lc407_04', 2)
    CommonSE('019_cloth_c')
    CommonSE('003_swing_grap_0_2')
    sprite('lc407_05', 2)
    setInvincible(0)
    sprite('lc407_06', 2)
    Recovery()
    if SLOT_51:
        Voiceline('lc300')
    sprite('lc407_07', 2)
    sprite('lc407_08', 2)
    sprite('lc407_09', 3)
    XImpulseAcceleration(40)
    sprite('lc407_10', 3)
    XImpulseAcceleration(80)
    sprite('lc407_11', 3)
    XImpulseAcceleration(80)
    sprite('lc407_12', 3)
    XImpulseAcceleration(80)
    sprite('lc407_13', 3)
    loopRest()
    label(0)
    sprite('lc020_07', 3)
    XImpulseAcceleration(90)
    sprite('lc020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc024_00', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc405_13', 4)
    sprite('lc405_14', 4)
    sprite('lc405_15', 3)


@State
def AirAssault3():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(800)
        Hitstop(9)
        AirUntechableTime(47)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        AirPushbackY(44400)
        HitAirUnblockable(2)
        callSubroutine('AssaultChain')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc407_02', 2)
    CommonSE('019_cloth_b')
    physicsXImpulse(8500)
    physicsYImpulse(21000)
    setGravity(1400)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc407_03', 2)
    Voiceline('lc209')
    sprite('lc407_04', 2)
    CommonSE('019_cloth_c')
    CommonSE('003_swing_grap_0_1')
    sprite('lc407_05', 2)
    sprite('lc407_06', 2)
    Recovery()
    if SLOT_51:
        Voiceline('lc300')
    sprite('lc407_07', 2)
    sprite('lc407_08', 2)
    sprite('lc407_09', 3)
    setGravity(1450)
    XImpulseAcceleration(40)
    sprite('lc407_10', 3)
    XImpulseAcceleration(80)
    sprite('lc407_11', 3)
    XImpulseAcceleration(80)
    sprite('lc407_12', 3)
    XImpulseAcceleration(80)
    sprite('lc407_13', 3)
    loopRest()
    label(0)
    sprite('lc020_07', 3)
    XImpulseAcceleration(90)
    sprite('lc020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc024_00', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc405_13', 4)
    sprite('lc405_14', 4)
    sprite('lc405_15', 3)


@State
def DashAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(2)
        Damage(450)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        AirPushbackY(5000)
        AirPushbackX(3000)
        Hitstop(2)
        PushbackX(2000)
        AirUntechableTime(34)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 240000:
                    SetActionMark(0)
                    sendToLabel(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc419_00', 3)
    sprite('lc419_01', 2)
    SpecificInvincibility(0, 1, 0, 0, 0)
    InvincibilityDuration(12)
    AltKnockdownEffects(100, 1, 0)
    CommonSE('000_airdash_1')
    sprite('lc419_02', 3)
    CreateObject('419smoke', -1)
    AddX(30000)
    physicsXImpulse(50000)
    sprite('lc419_03', 3)
    sprite('lc419_02', 3)
    SetActionMark(1)
    uponSendToLabel(RELEASE_C, 0)
    sprite('lc419_03', 3)
    sprite('lc419_02', 3)
    sprite('lc419_03', 3)
    loopRest()
    label(0)
    sprite('lc419_04', 3)
    clearUponHandler(RELEASE_C)
    clearUponHandler(EVERY_FRAME)
    XImpulseAcceleration(50)
    CommonSE('004_swing_grap_1_2')
    CommonSE('003_swing_grap_0_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    CommonSE('016_explode_0')
    SmartVoiceline('lc217')
    sprite('lc419_05', 2)
    CreateObject('419atkeff', -1)
    XImpulseAcceleration(50)
    RefreshMultihit()
    if SLOT_51:
        FatalCounter(1)
    sprite('lc419_05', 2)
    XImpulseAcceleration(0)
    RefreshMultihit()
    TriggerUponForState('419smoke', 32)
    sprite('lc419_06', 3)
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(13)
    AirUntechableTime(45)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackY(22000)
    AirPushbackX(35000)
    PushbackX(19800)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(34)
    NonCornerWallbounce(1)
    CHAirPushbackX(60000)
    NonCornerCHWallbounce(0)
    CHWallbounceReboundTime(10)
    if SLOT_51:
        AttackLevel_(5)
        Damage(1200)
        Hitstop(20)
        AirPushbackY(22000)
        AirPushbackX(70000)
        WallbounceReboundTime(20)
        AirHitstunAfterWallbounce(60)
        NonCornerWallbounce(0)
        CHAirPushbackX(70000)
        CHWallbounceReboundTime(20)
    sprite('lc419_07', 4)
    Recovery()
    sprite('lc419_08', 4)
    sprite('lc419_09', 4)
    sprite('lc419_10', 4)
    loopRest()
    ExitState()
    label(1)
    sprite('lc419_02', 3)
    clearUponHandler(RELEASE_C)
    clearUponHandler(EVERY_FRAME)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(60000)
    SLOT_51 = 1
    GotoState('DashAssault_Tame')
    sprite('lc419_03', 3)
    sprite('lc419_02', 3)
    XImpulseAcceleration(50)
    sprite('lc419_11', 3)
    XImpulseAcceleration(50)
    sprite('lc419_12', 5)
    XImpulseAcceleration(25)
    sprite('lc419_02', 2)
    AltKnockdownEffects(100, 1, 1)
    EnableCollision(1)
    SetXCollisionFromOrigin(-40)
    Flip()
    physicsXImpulse(80000)
    sprite('lc419_03', 2)
    loopRest()
    gotoLabel(0)


@State
def RocketLandF():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc413_00', 2)
    ObjectUpon2(11, 33, 0)
    SmartVoiceline('lc212')
    sprite('lc413_01', 2)
    sprite('lc413_02', 2)
    sprite('lc413_03', 2)
    sprite('lc413_04', 2)
    sprite('lc413_05', 2)
    sprite('lc413_06', 2)
    sprite('lc413_07', 2)


@State
def RocketLandB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc413_00', 1)
    ObjectUpon2(11, 34, 0)
    SmartVoiceline('lc213')
    sprite('lc413_01', 1)
    sprite('lc413_02', 2)
    sprite('lc413_03', 2)
    sprite('lc413_08', 2)
    sprite('lc413_09', 2)
    sprite('lc413_10', 2)
    sprite('lc413_11', 2)
    sprite('lc413_12', 2)


@State
def RocketAirF():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
    sprite('lc414_00', 2)
    SmartVoiceline('lc214')
    sprite('lc414_01', 2)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(0)
    ObjectUpon2(11, 56, 0)
    sprite('lc414_02', 2)
    sprite('lc414_03', 2)
    sprite('lc414_04', 2)
    sprite('lc414_05', 2)
    sprite('lc414_06', 2)
    sprite('lc414_07', 2)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(30)
    YAccel(30)
    setGravity(2000)
    sprite('lc414_08', 2)
    sprite('lc414_09', 2)


@State
def RocketAirB():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
    sprite('lc414_00', 3)
    SmartVoiceline('lc215')
    sprite('lc414_01', 3)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    setGravity(0)
    ObjectUpon2(11, 57, 0)
    sprite('lc414_10', 3)
    sprite('lc414_11', 3)
    sprite('lc414_12', 3)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(30)
    YAccel(30)
    setGravity(2000)
    sprite('lc414_13', 3)
    sprite('lc414_14', 2)


@State
def TonNanShaPeiAntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc418_00', 3)
    SmartVoiceline('lc216')
    sprite('lc418_01', 3)
    sprite('lc418_02', 3)
    sprite('lc418_03', 4)
    sprite('lc418_04', 4)
    sprite('lc418_05', 5)
    CreateObject('LcefRodReturn', 0)
    ObjectUpon2(11, 20, 0)
    sprite('lc418_06', 4)
    sprite('lc418_07', 4)
    sprite('lc418_08', 4)
    sprite('lc418_09', 4)


@State
def TonNanShaPeiAntiLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc417_00', 2)
    SmartVoiceline('lc216')
    sprite('lc417_01', 2)
    sprite('lc417_02', 2)
    sprite('lc417_03', 2)
    sprite('lc417_04', 3)
    sprite('lc417_05', 3)
    sprite('lc417_06', 5)
    CreateObject('LcefRodReturn', 0)
    ObjectUpon2(11, 21, 0)
    sprite('lc417_07', 5)
    sprite('lc417_08', 5)
    sprite('lc417_09', 5)
    sprite('lc417_10', 5)
    sprite('lc417_11', 5)


@Subroutine
def LC_JumpToRodSpeed():
    EndMomentum(1)
    setGravity(2500)
    CopyFromRightToLeft(3, 2, 54, 11, 2, 83)
    PrivateFunction(1, 2, 54, 2, 83, 2, 54)
    PrivateFunction(3, 2, 54, 0, 20, 2, 54)
    if SLOT_IsFacingRight:
        PrivateFunction(2, 2, 54, 0, -1, 2, 54)
    SLOT_XVelocity = SLOT_54
    if SLOT_XVelocity >= 30000:
        SLOT_XVelocity = 30000
    if SLOT_XVelocity <= -30000:
        SLOT_XVelocity = -30000
    PrivateFunction(1, 0, 1200000, 2, 23, 2, 55)
    PrivateFunction(3, 2, 55, 0, 20, 2, 55)
    SLOT_YVelocity = SLOT_55
    if SLOT_YVelocity >= 46153:
        SLOT_YVelocity = 46153
    if SLOT_YVelocity <= 12000:
        SLOT_YVelocity = 12000


@Subroutine
def LC_JumpToRodSpeedX():
    CopyFromRightToLeft(3, 2, 54, 11, 2, 83)
    PrivateFunction(1, 2, 54, 2, 83, 2, 54)
    PrivateFunction(3, 2, 54, 0, 19, 2, 54)
    if SLOT_IsFacingRight:
        PrivateFunction(2, 2, 54, 0, -1, 2, 54)
    SLOT_XVelocity = SLOT_54
    if SLOT_XVelocity >= 30000:
        SLOT_XVelocity = 30000
    if SLOT_XVelocity <= -30000:
        SLOT_XVelocity = -30000


@State
def JumpToRod_Ride():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        ExternalForcesRate(0, 0)
        SetZLine(0, 30)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(3, 2, 56, 11, 2, 25)
            if SLOT_56 >= 55000:
                CopyFromRightToLeft(3, 2, 56, 11, 2, 26)
                if SLOT_56 >= 55000:
                    CallPrivateFunction('LC_JumpToRodNearCheck1', 0, 0, 0, 
                        0, 0, 0, 0, 0)
            CopyFromRightToLeft(3, 2, 56, 11, 2, 83)
            PrivateFunction(1, 2, 56, 2, 83, 2, 56)
            if SLOT_56 <= 60000:
                if SLOT_56 >= -60000:
                    XImpulseAcceleration(60)
        SLOT_63 = 0
        SLOT_64 = 0
        EnableCollision(0)
    sprite('lc023_00', 1)
    sprite('lc023_01', 1)
    SmartVoiceline('lc007')
    if not SLOT_YDistanceFromFloor:
        JumpEffects(0, -1)
    loopRest()
    CopyFromRightToLeft(3, 2, 51, 11, 2, 22)
    PrivateFunction(1, 2, 51, 2, 22, 2, 51)
    if SLOT_IsFacingRight:
        if SLOT_51 <= 1:
            conditionalSendToLabel(10)
    if not SLOT_IsFacingRight:
        if SLOT_51 >= 1:
            conditionalSendToLabel(10)
    sprite('lc409_00', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 2)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    SLOT_64 = 1
    sprite('lc409_01', 3)
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_02', 3)
    sprite('lc409_03', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_04', 3)
    sprite('lc409_05', 3)
    sprite('lc409_06', 3)
    label(1)
    sprite('lc409_07', 3)
    sprite('lc409_08', 3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('lc409_09', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_10', 3)
    sprite('lc409_11', 3)
    sprite('lc409_12', 3)
    sprite('lc409_13', 3)
    loopRest()
    ExitState()
    label(10)
    sprite('lc409_14', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 12)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    SLOT_63 = 1
    sprite('lc409_15', 3)
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_16', 3)
    sprite('lc409_17', 3)
    sprite('lc409_18', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_19', 3)
    sprite('lc409_20', 3)
    label(11)
    sprite('lc409_21', 3)
    sprite('lc409_22', 3)
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('lc409_23', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_24', 3)
    sprite('lc409_25', 3)
    sprite('lc409_26', 3)
    sprite('lc409_27', 3)


@State
def Ride():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        EndMomentum(1)
        PreventBlocking(1)
        AttackOff()
        WhiffCancelEnable(1)
        WhiffCancel('RideEnd')
        WhiffCancel('RideAttack')
        WhiffCancel('RideAttackB')
        WhiffCancel('RideAttackC')
        WhiffCancel('RideAttackD')
        WhiffCancel('AstralHeat')
        EnableAfterimage(0)
        ExternalForcesRate(0, 0)
        HitBackReturnIgnore(1)
        SetXCollisionFromOrigin(1)
        WhiffAirJumpCancel(1)
        WhiffFAirDashCancel(1)
        WhiffBAirDashCancel(1)
        EnableCollision(0)
        SetZLine(0, 30)
        RunLoopUpon(17, 180)
        uponSendToLabel(17, 99)
        CopyFromRightToLeft(3, 2, 83, 11, 2, 83)

        def upon_EVERY_FRAME():
            if SLOT_51:
                CopyFromRightToLeft(3, 2, 83, 11, 2, 83)
                if not SLOT_21:
                    SLOT_51 = 0
                    sendToLabel(99)
                CopyFromRightToLeft(3, 2, 52, 22, 2, 22)
                PrivateFunction(1, 2, 52, 2, 22, 2, 52)
                if SLOT_IsFacingRight:
                    if SLOT_52 >= 1:
                        SLOT_51 = 0
                        sendToLabel(50)
                if not SLOT_IsFacingRight:
                    if SLOT_52 <= 1:
                        SLOT_51 = 0
                        sendToLabel(50)
    if SLOT_63:
        conditionalSendToLabel(10)
    if SLOT_64:
        conditionalSendToLabel(5)
    label(0)
    sprite('lc410_02', 7)
    SLOT_51 = 1
    SLOT_63 = 0
    SLOT_64 = 0
    sprite('lc410_03', 7)
    sprite('lc410_04', 7)
    sprite('lc410_03', 7)
    loopRest()
    gotoLabel(0)
    label(5)
    sprite('lc410_00', 1)
    SLOT_63 = 0
    SLOT_64 = 0
    sprite('lc410_01', 1)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('lc410_21', 2)
    SLOT_63 = 0
    SLOT_64 = 0
    loopRest()
    gotoLabel(0)
    label(50)
    sprite('lc410_18', 2)
    sprite('lc410_19', 2)
    sprite('lc410_20', 2)
    sprite('lc410_02', 1)
    Flip()
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('lc020_05', 1)
    physicsYImpulse(-8000)


@State
def RideEnd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        EndMomentum(1)
        PreventBlocking(1)
        AttackOff()
        HitBackReturnIgnore(1)
        SetXCollisionFromOrigin(150)
        PushCollisionHeightLow(150)
    sprite('lc020_05', 1)
    physicsYImpulse(-8000)


@State
def RideAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(92)
        SameMoveProration(80)
        CrouchWhiff(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-3000)
        AirPushbackY(33000)
        AirUntechableTime(35)
        AttackDirection(1)
        PushbackX(0)
        GuardCrush(1, 1)
        ExternalForcesRate(0, 0)
        SetXCollisionFromOrigin(1)
        HitBackReturnIgnore(1)
        SetXCollisionFromOrigin(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('RideEnd')
        EnableCollision(0)
        SetZLine(0, 30)
        EndMomentum(1)
        EnterStateIfEventID(8, 'Ride')

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(3, 2, 83, 11, 2, 83)
        SLOT_63 = 0
        SLOT_64 = 0
        ForceFaceSprite()
        HitOrBlockCancel('AstralHeat')
    sprite('lc410_05', 2)
    sprite('lc410_06', 2)
    sprite('lc410_07', 3)
    sprite('lc410_08', 2)
    SmartVoiceline('lc100')
    sprite('lc410_09', 2)
    CommonSE('003_swing_grap_0_2')
    sprite('lc410_10', 2)
    Recovery()
    sprite('lc410_11', 3)
    sprite('lc410_12', 2)
    sprite('lc410_13', 2)
    sprite('lc410_14', 2)
    sprite('lc410_15', 2)
    sprite('lc410_16', 2)
    sprite('lc410_17', 2)


@State
def RideAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(800)
        Hitstop(9)
        AirUntechableTime(47)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(6000)
        AirPushbackY(36000)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        SLOT_63 = 0
        SLOT_64 = 0
        ForceFaceSprite()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc020_05', 2)
    ObjectUpon2(11, 18, 0)
    CommonSE('019_cloth_a')
    physicsXImpulse(8500)
    setGravity(1600)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc020_06', 2)
    sprite('lc407_01', 2)
    sprite('lc407_02', 2)
    sprite('lc407_03', 2)
    Voiceline('lc209')
    sprite('lc407_04', 2)
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    CommonSE('005_swing_grap_2_1')
    CommonSE('003_swing_grap_0_2')
    sprite('lc407_05', 2)
    sprite('lc407_06', 2)
    Recovery()
    sprite('lc407_07', 2)
    sprite('lc407_08', 2)
    sprite('lc407_09', 3)
    setGravity(1450)
    XImpulseAcceleration(40)
    sprite('lc407_10', 3)
    XImpulseAcceleration(80)
    sprite('lc407_11', 3)
    XImpulseAcceleration(80)
    sprite('lc407_12', 3)
    XImpulseAcceleration(80)
    sprite('lc407_13', 3)
    loopRest()
    label(0)
    sprite('lc020_07', 3)
    XImpulseAcceleration(90)
    sprite('lc020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc405_13', 4)
    sprite('lc405_14', 4)
    sprite('lc405_15', 3)


@State
def RideAttackC():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        Hitstop(16)
        AirUntechableTime(41)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(6000)
        AirPushbackY(-88000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(30)
        CHHardKnockdown(10)
        HitOverhead(2)
        StarterRating(2)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        ForceFaceSprite()
        SLOT_63 = 0
        SLOT_64 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc406_03', 2)
    ObjectUpon2(11, 18, 0)
    AddY(30000)
    physicsXImpulse(17000)
    setGravity(1800)
    sprite('lc406_04', 2)
    sprite('lc406_05', 2)
    CommonSE('019_cloth_a')
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc406_06', 2)
    sprite('lc406_07', 2)
    sprite('lc406_08', 2)
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    CommonSE('004_swing_grap_1_1')
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_0')
    sprite('lc406_09', 2)
    sprite('lc406_10', 2)
    Voiceline('lc208')
    sprite('lc406_11ex', 3)
    sprite('lc406_12', 2)
    Recovery()
    sprite('lc406_13', 2)
    sprite('lc406_14', 3)
    XImpulseAcceleration(80)
    sprite('lc020_06', 4)
    XImpulseAcceleration(80)
    loopRest()
    label(0)
    sprite('lc020_07', 4)
    XImpulseAcceleration(90)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc406_15', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc406_16', 2)
    sprite('lc405_13', 2)
    sprite('lc405_14', 3)
    sprite('lc405_15', 2)


@State
def RideAttackD():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        AttackP2(89)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-12000)
        AirPushbackY(-65000)
        AirUntechableTime(40)
        HardKnockdown(1)
        Hitstop(7)
        AttackDirection(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        HitOverhead(2)
        SLOT_63 = 0
        SLOT_64 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc260_00ex01', 1)
    AddY(-80000)
    setGravity(1000)
    EnableCollision(0)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('lc260_01ex01', 1)
    sprite('lc260_02ex01', 1)
    sprite('lc260_03ex01', 1)
    sprite('lc260_04ex01', 1)
    SmartVoiceline('lc103')
    sprite('lc260_05ex01', 1)
    sprite('lc260_06ex01', 1)
    label(0)
    sprite('lc260_07ex01', 3)
    CommonSE('019_cloth_c')
    physicsYImpulse(-40000)
    sprite('lc260_08ex01', 3)
    sprite('lc260_09ex01', 3)
    sprite('lc260_10ex01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc260_11ex01', 2)
    LandingEffects(100, 1, 1)
    sprite('lc260_12ex01', 2)
    sprite('lc260_13ex01', 2)
    EnableCollision(1)
    sprite('lc260_14ex01', 2)
    sprite('lc260_15ex01', 3)
    HitOverhead(0)
    HitLow(2)
    MoveAttributes(0, 0, 1, 0, 0)
    AirPushbackX(4000)
    AirPushbackY(30000)
    HardKnockdown(0)
    RefreshMultihit()
    sprite('lc260_16ex01', 3)
    Recovery()
    sprite('lc260_17ex01', 2)
    sprite('lc260_18ex01', 2)
    sprite('lc260_19ex01', 2)


@State
def JumpToRod_Kick():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        ExternalForcesRate(0, 0)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(3, 2, 56, 11, 2, 25)
            if SLOT_56 >= 55000:
                CopyFromRightToLeft(3, 2, 56, 11, 2, 26)
                if SLOT_56 >= 55000:
                    CallPrivateFunction('LC_JumpToRodNearCheck2', 0, 0, 0, 
                        0, 0, 0, 0, 0)
            CopyFromRightToLeft(3, 2, 56, 11, 2, 83)
            PrivateFunction(1, 2, 56, 2, 83, 2, 56)
            if SLOT_56 <= 60000:
                if SLOT_56 >= -60000:
                    XImpulseAcceleration(60)
        SLOT_63 = 0
        SLOT_64 = 0
    sprite('lc023_00', 1)
    sprite('lc023_01', 1)
    SmartVoiceline('lc007')
    if not SLOT_YDistanceFromFloor:
        JumpEffects(0, -1)
    loopRest()
    CopyFromRightToLeft(3, 2, 51, 11, 2, 22)
    PrivateFunction(1, 2, 51, 2, 22, 2, 51)
    if SLOT_IsFacingRight:
        if SLOT_51 <= 1:
            conditionalSendToLabel(10)
    if not SLOT_IsFacingRight:
        if SLOT_51 >= 1:
            conditionalSendToLabel(10)
    sprite('lc409_00', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 2)
    CommonSE('204_runjump_normal_1')
    CommonSE('208_brake_normal')
    EnableCollision(0)
    SLOT_64 = 1
    sprite('lc409_01', 3)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_02', 3)
    sprite('lc409_03', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_04', 3)
    sprite('lc409_05', 3)
    sprite('lc409_06', 3)
    label(1)
    sprite('lc409_07', 2)
    PerGravity(110)
    sprite('lc409_08', 2)
    PerGravity(110)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('lc409_09', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_10', 3)
    sprite('lc409_11', 3)
    sprite('lc409_12', 3)
    sprite('lc409_13', 3)
    loopRest()
    ExitState()
    label(10)
    sprite('lc409_14', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 12)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    EnableCollision(0)
    SLOT_63 = 1
    sprite('lc409_15', 3)
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_16', 3)
    sprite('lc409_17', 3)
    sprite('lc409_18', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_19', 3)
    sprite('lc409_20', 3)
    label(11)
    sprite('lc409_21', 2)
    PerGravity(110)
    sprite('lc409_22', 2)
    PerGravity(110)
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('lc409_23', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_24', 3)
    sprite('lc409_25', 3)
    sprite('lc409_26', 3)
    sprite('lc409_27', 3)
    loopRest()
    ExitState()
    label(3)
    enterState('JumpToRod_Kick2')


@State
def JumpToRod_Kick2():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackOff()
        EnableCollision(0)
        ExternalForcesRate(0, 0)
    if SLOT_63:
        conditionalSendToLabel(50)
    sprite('lc411_00', 1)
    AddX(-40000)
    SLOT_63 = 0
    SLOT_64 = 0
    sprite('lc411_01', 1)
    CommonSE('208_brake_normal')
    CommonSE('208_brake_normal')
    AddX(20000)
    loopRest()
    gotoLabel(60)
    label(50)
    sprite('lc411_15', 1)
    ForceFaceSprite()
    AddX(-20000)
    SLOT_63 = 0
    SLOT_64 = 0
    sprite('lc411_16', 1)
    CommonSE('208_brake_normal')
    CommonSE('208_brake_normal')
    loopRest()
    label(60)
    sprite('lc411_02', 1)
    AddX(20000)
    sprite('lc411_03', 1)
    AddX(20000)
    sprite('lc411_04', 1)
    AddX(20000)
    sprite('lc411_05', 1)
    physicsXImpulse(0)
    sprite('lc411_06', 2)
    SmartVoiceline('lc102')
    ObjectUpon2(11, 17, 0)
    sprite('lc411_07', 2)
    CommonSE('003_swing_grap_0_1')
    CommonSE('005_swing_grap_2_2')
    sprite('lc411_08', 2)
    sprite('lc411_09', 3)
    EndYPhysicsImpulse()
    sprite('lc411_10', 3)
    sprite('lc411_11', 3)
    sprite('lc411_12', 3)
    sprite('lc411_13', 3)
    sprite('lc411_14', 32767)
    EnableCollision(1)


@State
def JumpToRod_Jump():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        ExternalForcesRate(0, 0)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(3, 2, 56, 11, 2, 25)
            if SLOT_56 >= 55000:
                CopyFromRightToLeft(3, 2, 56, 11, 2, 26)
                if SLOT_56 >= 55000:
                    CallPrivateFunction('LC_JumpToRodNearCheck2', 0, 0, 0, 
                        0, 0, 0, 0, 0)
            CopyFromRightToLeft(3, 2, 56, 11, 2, 83)
            PrivateFunction(1, 2, 56, 2, 83, 2, 56)
            if SLOT_56 <= 60000:
                if SLOT_56 >= -60000:
                    XImpulseAcceleration(60)
        SLOT_63 = 0
        SLOT_64 = 0
    sprite('lc023_00', 1)
    sprite('lc023_01', 1)
    SmartVoiceline('lc007')
    if not SLOT_YDistanceFromFloor:
        JumpEffects(0, -1)
    loopRest()
    CopyFromRightToLeft(3, 2, 51, 11, 2, 22)
    PrivateFunction(1, 2, 51, 2, 22, 2, 51)
    if SLOT_IsFacingRight:
        if SLOT_51 <= 1:
            conditionalSendToLabel(10)
    if not SLOT_IsFacingRight:
        if SLOT_51 >= 1:
            conditionalSendToLabel(10)
    sprite('lc409_00', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 2)
    CommonSE('204_runjump_normal_1')
    CommonSE('208_brake_normal')
    EnableCollision(0)
    SLOT_64 = 1
    sprite('lc409_01', 3)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_02', 3)
    sprite('lc409_03', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_04', 3)
    sprite('lc409_05', 3)
    sprite('lc409_06', 3)
    label(1)
    sprite('lc409_07', 3)
    sprite('lc409_08', 3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('lc409_09', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_10', 3)
    sprite('lc409_11', 3)
    sprite('lc409_12', 3)
    sprite('lc409_13', 3)
    loopRest()
    ExitState()
    label(10)
    sprite('lc409_14', 3)
    callSubroutine('LC_JumpToRodSpeed')
    uponSendToLabel(LANDING, 12)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    EnableCollision(0)
    SLOT_63 = 1
    sprite('lc409_15', 3)
    SLOT_66 = SLOT_66 + -1
    sprite('lc409_16', 3)
    sprite('lc409_17', 3)
    sprite('lc409_18', 3)
    callSubroutine('LC_JumpToRodSpeedX')
    sprite('lc409_19', 3)
    sprite('lc409_20', 3)
    label(11)
    sprite('lc409_21', 2)
    sprite('lc409_22', 2)
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('lc409_23', 3)
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('lc409_24', 3)
    sprite('lc409_25', 3)
    sprite('lc409_26', 3)
    sprite('lc409_27', 3)
    loopRest()
    ExitState()
    label(3)
    enterState('JumpToRod_Jump2')


@State
def JumpToRod_Jump2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        AttackOff()
        EnableCollision(0)
        StayAfterMovement(1, 0)
        ExternalForcesRate(0, 0)
    if SLOT_63:
        conditionalSendToLabel(50)
    sprite('lc412_00', 2)
    CopyFromRightToLeft(3, 2, 83, 11, 2, 83)
    ObjectUpon2(11, 18, 0)
    SLOT_63 = 0
    SLOT_64 = 0
    loopRest()
    gotoLabel(60)
    label(50)
    sprite('lc412_13', 2)
    ForceFaceSprite()
    CopyFromRightToLeft(3, 2, 83, 11, 2, 83)
    ObjectUpon2(11, 18, 0)
    SLOT_63 = 0
    SLOT_64 = 0
    loopRest()
    label(60)
    sprite('lc412_01', 3)
    AddY(-60000)
    sprite('lc412_02', 3)
    sprite('lc412_03', 2)
    AddX(128000)
    physicsXImpulse(25000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    CommonSE('019_cloth_a')
    CommonSE('002_highjump_1')
    SmartVoiceline('lc101')
    sprite('lc412_04', 2)
    sprite('lc412_05', 1)
    sprite('lc412_06', 1)
    sprite('lc412_07', 1)
    EnableCollision(1)
    sprite('lc412_08', 1)
    sprite('lc412_09', 1)
    sprite('lc412_10', 1)
    sprite('lc412_11', 1)
    sprite('lc412_12', 1)


@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        setInvincible(1)
        StayAfterMovement(1, 0)
        if SLOT_94:
            SpecificInvincibility(0, 1, 0, 1, 1)
    sprite('lc404_00', 2)
    sprite('lc404_01', 2)
    CreateParticle('lcef_drgnMorf', 0)
    sprite('lc404_02', 2)
    LandingEffects(100, 1, 0)
    sprite('lc404_03', 2)
    sprite('lc404_04', 1)
    ObjectUpon2(11, 31, 0)
    Voiceline('lc210')
    CommonSE('016_explode_0')
    CommonSE('016_explode_0')
    CommonSE('006_swing_blade_2')
    sprite('lc404_05', 1)
    sprite('lc404_06', 2)
    sprite('lc404_07', 1)
    sprite('lc404_08', 1)
    sprite('lc404_09', 1)
    sprite('lc404_10', 3)
    setInvincible(0)
    sprite('lc404_11', 5)
    sprite('lc404_12', 5)
    sprite('lc404_13', 5)
    sprite('lc404_14', 5)
    sprite('lc404_15', 5)
    sprite('lc404_16', 5)
    sprite('lc404_17', 5)
    sprite('lc404_18', 5)


@State
def KantsuA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        uponSendToLabel(32, 9)

        def upon_33():
            Recovery()

        def upon_EVERY_FRAME():
            if CheckInput(0x5):
                if SLOT_StateDuration >= 12:
                    clearUponHandler(EVERY_FRAME)
                    DisallowGoto2('KantsuD')
                    EnableAfterimage(1)
                    setInvincible(0)
                    sendToLabel(1)
    sprite('lc400_01', 3)
    ObjectUpon2(11, 22, 0)
    BeginBuffer('KantsuD')
    sprite('lc400_02', 3)
    sprite('lc400_03', 1)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(1, 1, 0, 1, 0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(12, 12)
    CreateParticle('lcef_kantsuloop', -1)
    Voiceline('lc200')
    sprite('lc400_03', 2)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    CommonSE('019_cloth_a')
    sprite('lc400_05', 3)
    BufferedOrPressedGoto('KantsuD')
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    sprite('lc400_05', 3)
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    sprite('lc400_10', 3)
    setInvincible(0)
    clearUponHandler(EVERY_FRAME)
    DisallowGoto2('KantsuD')
    sprite('lc400_11', 3)
    ExitState()
    label(1)
    sprite('lc401_00', 3)
    ObjectUpon2(11, 23, 0)
    Voiceline('lc201')
    sprite('lc401_01', 3)
    sprite('lc401_02', 4)
    sprite('lc401_03', 18)
    sprite('lc401_04', 4)
    sprite('lc401_05', 4)
    sprite('lc401_06', 4)
    ExitState()
    label(9)
    sprite('lc401_03', 22)
    sprite('lc401_04', 6)
    sprite('lc401_05', 6)
    sprite('lc401_06', 6)


@State
def KantsuB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        uponSendToLabel(32, 9)

        def upon_33():
            Recovery()

        def upon_EVERY_FRAME():
            if CheckInput(0xe):
                if SLOT_StateDuration >= 12:
                    clearUponHandler(EVERY_FRAME)
                    DisallowGoto2('KantsuD')
                    EnableAfterimage(1)
                    setInvincible(0)
                    sendToLabel(1)
    sprite('lc400_01', 3)
    ObjectUpon2(11, 22, 0)
    BeginBuffer('KantsuD')
    sprite('lc400_02', 3)
    sprite('lc400_03', 1)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(1, 1, 0, 1, 0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(12, 12)
    CreateParticle('lcef_kantsuloop', -1)
    Voiceline('lc200')
    sprite('lc400_03', 2)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    CommonSE('019_cloth_a')
    sprite('lc400_05', 3)
    BufferedOrPressedGoto('KantsuD')
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    sprite('lc400_05', 3)
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    sprite('lc400_10', 3)
    setInvincible(0)
    clearUponHandler(EVERY_FRAME)
    DisallowGoto2('KantsuD')
    sprite('lc400_11', 3)
    ExitState()
    label(1)
    sprite('lc402_00', 3)
    ObjectUpon2(11, 24, 0)
    Voiceline('lc202')
    sprite('lc402_01', 3)
    sprite('lc402_02', 4)
    sprite('lc402_03', 18)
    sprite('lc402_04', 4)
    sprite('lc402_05', 4)
    sprite('lc402_06', 4)
    ExitState()
    label(9)
    sprite('lc402_03', 22)
    sprite('lc402_04', 6)
    sprite('lc402_05', 6)
    sprite('lc402_06', 6)


@State
def KantsuC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        uponSendToLabel(32, 9)

        def upon_33():
            Recovery()

        def upon_EVERY_FRAME():
            if CheckInput(0x17):
                if SLOT_StateDuration >= 12:
                    clearUponHandler(EVERY_FRAME)
                    DisallowGoto2('KantsuD')
                    EnableAfterimage(1)
                    setInvincible(0)
                    sendToLabel(1)
    sprite('lc400_01', 3)
    ObjectUpon2(11, 22, 0)
    BeginBuffer('KantsuD')
    sprite('lc400_02', 3)
    sprite('lc400_03', 1)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(1, 1, 0, 1, 0)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(12, 12)
    CreateParticle('lcef_kantsuloop', -1)
    Voiceline('lc200')
    sprite('lc400_03', 2)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    CommonSE('019_cloth_a')
    sprite('lc400_05', 3)
    BufferedOrPressedGoto('KantsuD')
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    CommonSE('011_spin_0')
    sprite('lc400_05', 3)
    sprite('lc400_06', 3)
    sprite('lc400_07', 3)
    CommonSE('011_spin_2')
    sprite('lc400_08', 3)
    sprite('lc400_09', 3)
    sprite('lc400_04', 3)
    sprite('lc400_10', 3)
    setInvincible(0)
    clearUponHandler(EVERY_FRAME)
    DisallowGoto2('KantsuD')
    sprite('lc400_11', 3)
    ExitState()
    label(1)
    sprite('lc403_00', 2)
    Voiceline('lc203')
    sprite('lc403_01', 2)
    ObjectUpon2(11, 25, 0)
    sprite('lc403_02', 2)
    sprite('lc403_03', 2)
    sprite('lc403_04', 4)
    sprite('lc403_05', 8)
    sprite('lc403_06', 4)
    sprite('lc403_07', 4)
    sprite('lc403_08', 4)
    sprite('lc403_09', 4)
    sprite('lc403_10', 4)
    ExitState()
    label(9)
    sprite('lc403_05', 15)
    sprite('lc403_06', 5)
    sprite('lc403_07', 5)
    sprite('lc403_08', 5)
    sprite('lc403_09', 5)
    sprite('lc403_10', 5)


@State
def KantsuD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EnableAfterimage(1)
        PreventBlocking(1)
    sprite('lc400_04', 3)
    ObjectUpon2(11, 0, 0)
    sprite('lc400_05', 3)
    sprite('lc400_10', 4)
    sprite('lc400_11', 4)


@State
def RenchanB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc421_00', 2)
    ObjectUpon2(11, 11, 0)
    sprite('lc421_01', 2)
    sprite('lc421_02', 3)
    sprite('lc421_05', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('lc421_06', 3)
    Voiceline('lc218')
    CommonSE('008_swing_pole_2')
    sprite('lc421_07', 4)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 15, 0)
    sprite('lc421_08', 4)
    sprite('lc421_09', 4)
    sprite('lc421_10', 4)
    sprite('lc421_11', 4)
    sprite('lc421_12', 4)
    sprite('lc421_13', 4)
    sprite('lc421_14', 4)


@State
def RenchanC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('lc421_00', 3)
    ObjectUpon2(11, 11, 0)
    sprite('lc421_01', 3)
    sprite('lc421_02', 3)
    sprite('lc421_03', 3)
    sprite('lc421_04', 3)
    sprite('lc421_02', 3)
    sprite('lc421_03', 3)
    sprite('lc421_04', 3)
    sprite('lc421_02', 3)
    sprite('lc421_05', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('lc421_06', 3)
    Voiceline('lc218')
    CommonSE('008_swing_pole_2')
    sprite('lc421_07', 2)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 16, 0)
    sprite('lc421_08', 2)
    sprite('lc421_09', 2)
    sprite('lc421_10', 2)
    sprite('lc421_11', 2)
    sprite('lc421_12', 2)
    sprite('lc421_13', 2)
    sprite('lc421_14', 2)


@State
def UltimateNingyouU():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(6)
        AfterimageColor_1(255, 255, 128, 0)
        AfterimageColor_2(0, 255, 255, 255)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('lc432_00', 2)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('lc432_01', 2)
    sprite('lc432_02', 2)
    sprite('lc432_03', 2)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_LC', -1)
    CreateParticle('lcef_mantenlight', 0)
    sprite('lc432_04', 2)
    sprite('lc432_05', 2)
    sprite('lc432_06', 2)
    sprite('lc432_07', 2)
    sprite('lc432_08', 2)
    sprite('lc432_09', 2)
    sprite('lc432_10', 2)
    sprite('lc432_11', 2)
    sprite('lc432_12', 8)
    CreateObject('LcefRodReturnDD', 0)
    ObjectUpon2(11, 47, 0)
    Voiceline('lc252')
    setInvincible(0)
    sprite('lc432_13', 8)
    sprite('lc432_14', 8)
    sprite('lc432_15', 4)
    sprite('lc432_16', 4)
    sprite('lc432_17', 4)
    sprite('lc432_18', 4)
    sprite('lc432_19', 4)
    sprite('lc432_20', 4)
    sprite('lc432_21', 4)


@State
def UltimateNingyouD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(6)
        AfterimageColor_1(255, 255, 128, 0)
        AfterimageColor_2(0, 255, 255, 255)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('lc432_00', 2)
    sprite('lc432_01', 2)
    sprite('lc432_02', 2)
    sprite('lc432_03', 2)
    sprite('lc432_04', 2)
    sprite('lc432_05', 2)
    sprite('lc432_06', 2)
    sprite('lc432_07', 2)
    sprite('lc432_08', 2)
    sprite('lc432_09', 3)
    sprite('lc432_10', 2)
    sprite('lc432_11', 2)
    sprite('lc432_12', 27)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_LC', -1)
    CreateParticle('lcef_mantenlight', 1)
    CreateObject('LcefRodReturnDD', 0)
    ObjectUpon2(11, 48, 0)
    Voiceline('lc252')
    setInvincible(1)
    sprite('lc432_12', 3)
    setInvincible(0)
    sprite('lc432_13', 5)
    sprite('lc432_14', 5)
    sprite('lc432_15', 4)
    sprite('lc432_16', 4)
    sprite('lc432_17', 4)
    sprite('lc432_18', 4)
    sprite('lc432_19', 4)
    sprite('lc432_20', 4)
    sprite('lc432_21', 4)


@State
def UltimateBakuhatsu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        StayAfterMovement(1, 0)
        setInvincible(1)
    sprite('lc433_00', 3)
    sprite('lc433_01', 2)
    sprite('lc433_01', 1)
    CreateObject('EMB_LC', -1)
    DistortionSettings(63, -1, 0)
    HeatChange(-5000)
    CreateObject('DistAura', -1)
    Voiceline('lc250')
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(6)
    AfterimageColor_1(255, 255, 128, 0)
    AfterimageColor_2(0, 255, 255, 255)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    sprite('lc433_02', 3)
    sprite('lc433_03', 3)
    sprite('lc433_04', 3)
    sprite('lc433_05', 3)
    sprite('lc433_06', 3)
    sprite('lc433_07', 3)
    sprite('lc433_08', 3)
    sprite('lc433_09', 3)
    sprite('lc433_10', 2)
    sprite('lc433_11', 2)
    sprite('lc433_12', 5)
    sprite('lc433_13', 5)
    sprite('lc433_14', 4)
    sprite('lc433_15', 4)
    sprite('lc433_16', 4)
    sprite('lc433_17', 4)
    sprite('lc433_18', 4)
    sprite('lc433_19', 4)
    CreateObject('AuraPoll', -1)
    CreateObject('AuraPollHand', 0)
    EnableAfterimage(0)
    CommonSE('213_bound_1')
    CommonSE('200_walk_normal_0')
    sprite('lc433_20', 2)
    PrivateSE('lcse_20')
    sprite('lc433_20', 2)
    setInvincible(0)
    sprite('lc433_21', 4)
    sprite('lc433_22', 4)
    sprite('lc433_23', 4)
    sprite('lc433_24', 4)
    CommonSE('015_blaze_0')
    sprite('lc433_25', 3)
    sprite('lc433_26', 3)
    sprite('lc433_27', 3)
    sprite('lc433_28', 3)
    sprite('lc433_29', 3)
    sprite('lc433_30', 3)


@State
def UltimateBakuhatsu_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        StayAfterMovement(1, 0)
        setInvincible(1)
        AttackType(4)
    sprite('lc433_00', 3)
    sprite('lc433_01', 2)
    sprite('lc433_01', 1)
    CreateObject('EMB_LC', -1)
    DistortionSettings(63, -1, 0)
    HeatChange(-5000)
    CreateObject('DistAura', -1)
    Voiceline('lc250')
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(6)
    AfterimageColor_1(255, 255, 128, 0)
    AfterimageColor_2(0, 255, 255, 255)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    sprite('lc433_02', 3)
    sprite('lc433_03', 3)
    sprite('lc433_04', 3)
    sprite('lc433_05', 3)
    sprite('lc433_06', 3)
    sprite('lc433_07', 3)
    sprite('lc433_08', 3)
    sprite('lc433_09', 3)
    sprite('lc433_10', 2)
    sprite('lc433_11', 2)
    sprite('lc433_12', 5)
    sprite('lc433_13', 5)
    sprite('lc433_14', 4)
    sprite('lc433_15', 4)
    sprite('lc433_16', 4)
    sprite('lc433_17', 4)
    sprite('lc433_18', 4)
    sprite('lc433_19', 4)
    CreateObject('AuraPoll_OD', -1)
    CreateObject('AuraPollHand', 0)
    EnableAfterimage(0)
    CommonSE('213_bound_1')
    CommonSE('200_walk_normal_0')
    sprite('lc433_20', 2)
    PrivateSE('lcse_20')
    sprite('lc433_20', 2)
    setInvincible(0)
    sprite('lc433_21', 4)
    sprite('lc433_22', 4)
    sprite('lc433_23', 4)
    sprite('lc433_24', 4)
    CommonSE('015_blaze_0')
    sprite('lc433_25', 3)
    sprite('lc433_26', 3)
    sprite('lc433_27', 3)
    sprite('lc433_28', 3)
    sprite('lc433_29', 3)
    sprite('lc433_30', 3)


@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(4)
        Damage(500)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(96)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(60)
        Crumple(45)
        Hitstop(20)
        AirUntechableTime(80)
        Hitstun(30)
        OppPositionOnHit(1, 250000, 0)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        if SLOT_StateDuration >= 12:
            EnterStateIfEventID(12, 'UltimateRush_NoRod_Ranbu')
            SLOT_51 = 1
        else:
            EnterStateIfEventID(12, 'UltimateRush_Ranbu')

        def upon_OPPONENT_HIT():
            ForceFaceSprite()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc434_00', 6)
    SmartVoiceline('lc253')
    CreateObject('EMB_LC', -1)
    DistortionSettings(55, -1, 0)
    HeatChange(-5000)
    CreateObject('DistAura', -1)
    sprite('lc434_01', 6)
    sprite('lc434_02', 6)
    sprite('lc434_03', 6)
    sprite('lc434_04', 8)
    CreateObject('aurastart', -1)
    sprite('lc434_05', 8)
    sprite('lc434_06', 8)
    CreateObject('auraball', -1)
    sprite('lc434_07', 8)
    sprite('lc434_08', 3)
    sprite('lc434_09', 3)
    sprite('lc419_02', 2)
    physicsXImpulse(60000)
    if SLOT_51:
        XImpulseAcceleration(75)
    AltKnockdownEffects(100, 1, 1)
    sprite('lc419_03', 2)
    sprite('lc419_04', 2)
    XImpulseAcceleration(30)
    CommonSE('003_swing_grap_0_1')
    CommonSE('004_swing_grap_1_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    CommonSE('016_explode_0')
    callSubroutine('RodNoHit')
    sprite('lc419_05ex', 3)
    XImpulseAcceleration(0)
    RefreshMultihit()
    sprite('lc419_06ex', 3)
    sprite('lc419_06ex', 3)
    AttackOff()
    clearUponHandler(EVERY_FRAME)
    setInvincible(0)
    sprite('lc419_07', 6)
    sprite('lc419_08', 6)
    sprite('lc419_09', 6)
    sprite('lc419_10', 6)


@State
def UltimateRush_Ranbu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        AttackP2(96)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirPushbackX(3000)
        AirPushbackY(24000)
        PushbackX(-2000)
        Hitstop(2)
        AirUntechableTime(80)
        Hitstun(30)
        DefeatOpponentBehavior(1)
        MinimumDamage(15)
        CHStateIfCHStart(3)
        callSubroutine('RodNoHit')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc419_07', 1)
    sprite('lc419_08', 1)
    sprite('lc419_09', 1)
    sprite('lc419_10', 1)
    sprite('lc231_00', 2)
    ObjectUpon2(11, 39, 0)
    EnableAfterimage(1)
    sprite('lc231_01', 2)
    sprite('lc231_02', 2)
    sprite('lc231_03', 2)
    sprite('lc231_04', 2)
    sprite('lc231_05', 2)
    sprite('lc231_06', 2)
    physicsXImpulse(2000)
    sprite('lc231_07', 2)
    sprite('lc231_08', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_2')
    ObjectHitbox(11)
    RefreshMultihit()
    sprite('lc231_08', 2)
    RefreshMultihit()
    sprite('lc231_09', 1)
    sprite('lc231_10', 1)
    ObjectHitbox(0)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    PushbackX(-3000)
    sprite('lc201_00', 2)
    ObjectUpon2(11, 36, 0)
    ObjectHitbox(11)
    sprite('lc201_01', 2)
    sprite('lc201_02', 2)
    sprite('lc201_03', 2)
    sprite('lc201_04', 2)
    sprite('lc201_05', 1)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_2')
    XImpulseAcceleration(50)
    sprite('lc201_05', 1)
    RefreshMultihit()
    sprite('lc201_05', 1)
    RefreshMultihit()
    sprite('lc201_06', 2)
    ObjectHitbox(0)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    PushbackX(19800)
    sprite('lc202_01', 2)
    StayAfterMovement(0, 0)
    ObjectUpon2(11, 19, 0)
    ObjectUpon2(11, 11, 0)
    sprite('lc202_02', 2)
    sprite('lc202_03', 2)
    AddX(50000)
    sprite('lc202_04', 2)
    AddX(50000)
    CreateObject('LcefKikouCharge', 0)
    sprite('lc202_05', 3)
    RandomCommonVoiceline(2)
    sprite('lc202_06', 2)
    sprite('lc202_07', 2)
    sprite('lc202_09ex01', 2)
    XImpulseAcceleration(50)
    ObjectHitbox(11)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    CommonSE('008_swing_pole_1')
    CommonSE('006_swing_blade_1')
    RefreshMultihit()
    CreateObject('LcefKikouPtcRod', 1)
    sprite('lc202_09ex01', 2)
    ObjectHitbox(11)
    RefreshMultihit()
    sprite('lc202_10', 3)
    sprite('lc202_11', 1)
    ObjectHitbox(11)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    CommonSE('008_swing_pole_1')
    CommonSE('006_swing_blade_1')
    RefreshMultihit()
    sprite('lc202_11', 1)
    ObjectHitbox(11)
    RefreshMultihit()
    sprite('lc202_13', 2)
    sprite('lc202_14', 2)
    XImpulseAcceleration(0)
    AddX(-25000)
    AttackOff()
    Hitstop(6)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    sprite('lc211_01', 2)
    StayAfterMovement(1, 0)
    ObjectUpon2(11, 37, 0)
    sprite('lc211_02', 2)
    sprite('lc211_02', 2)
    sprite('lc211_03', 2)
    sprite('lc211_04', 3)
    sprite('lc211_05', 2)
    sprite('lc211_06', 3)
    sprite('lc211_07', 4)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_1')
    ObjectHitbox(11)
    sprite('lc211_08', 2)
    sprite('lc211_09', 2)
    ObjectHitbox(0)
    sprite('lc211_10', 2)
    sprite('lc211_11', 2)
    sprite('lc211_12', 2)
    Hitstop(8)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(24000)
    PushbackX(4000)
    sprite('lc215_00', 2)
    AddX(150000)
    physicsXImpulse(-2000)
    LandingEffects(100, 1, 0)
    sprite('lc215_01', 2)
    sprite('lc215_02', 3)
    EndMomentum(0)
    if CheckInput(INPUT_HOLD_D):
        Hitstop(14)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        SLOT_52 = 1
    sprite('lc215_03', 2)
    RefreshMultihit()
    CreateObject('LcefTetsuzanko', 0)
    DashEffects(100, 1, 0)
    physicsXImpulse(50000)
    RandomCommonVoiceline(0)
    CommonSE('005_swing_grap_2_1')

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SetActionMark(1)
    sprite('lc215_04', 2)
    sprite('lc215_05', 2)
    XImpulseAcceleration(25)
    sprite('lc215_06', 1)
    XImpulseAcceleration(50)
    sprite('lc215_06', 1)
    if SLOT_52:
        conditionalSendToLabel(10)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackY(45000)
    YImpulseBeforeWallbounce(1200)
    Hitstop(16)
    sprite('lc261_00', 2)
    if SLOT_2:
        CameraControlEnable(1)
    AddX(50000)
    sprite('lc261_01', 2)
    sprite('lc261_01', 2)
    ObjectUpon2(11, 46, 0)
    sprite('lc261_01', 3)
    sprite('lc261_02', 9)
    sprite('lc261_03', 2)
    Voiceline('lc109')
    CommonSE('004_swing_grap_1_1')
    sprite('lc261_04', 2)
    ObjectHitbox(11)
    RefreshMultihit()

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SLOT_51 = 1
    sprite('lc261_05', 2)
    XImpulseAcceleration(50)
    sprite('lc261_06', 2)
    XImpulseAcceleration(50)
    sprite('lc261_07', 2)
    XImpulseAcceleration(0)
    sprite('lc261_08', 2)
    sprite('lc261_09', 2)
    sprite('lc261_10', 1)
    sprite('lc261_10', 1)
    if SLOT_51:
        conditionalSendToLabel(2)
    loopRest()
    ExitState()
    label(2)
    AttackOff()
    EnableRapidCancel(0)
    sprite('lc434_48', 2)
    sprite('lc434_49', 2)
    sprite('lc434_50', 2)
    sprite('lc434_51', 2)
    sprite('lc434_52', 2)
    sprite('lc434_53', 2)
    sprite('lc434_54', 2)
    sprite('lc434_55', 2)
    sprite('lc434_56', 3)
    ObjectUpon2(11, 11, 0)
    CommonSE('003_swing_grap_0_2')
    sprite('lc434_57', 3)
    CommonSE('005_swing_grap_2_1')
    sprite('lc434_58', 3)
    sprite('lc434_59', 3)
    sprite('lc434_60', 3)
    sprite('lc434_61', 3)
    sprite('lc434_30', 4)
    sprite('lc434_31', 4)
    physicsXImpulse(7500)
    SetXCollisionFromOrigin(300)
    sprite('lc434_32', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(320)
    sprite('lc434_33', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(340)
    sprite('lc434_34', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(360)
    sprite('lc434_35', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(380)
    sprite('lc434_36', 4)
    CreateObject('434atkeff', -1)
    CommonSE('008_swing_pole_2')
    CommonSE('008_swing_pole_1')
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(400)
    sprite('lc434_37', 4)
    RefreshMultihit()
    Damage(2400)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackY(74000)
    YImpulseBeforeWallbounce(3000)
    HardKnockdown(10)
    Hitstop(0)
    DefeatOpponentBehavior(0)
    HitBackReturnObject(0)
    EndMomentum(1)
    if SLOT_43:
        Voiceline('lc105')
    else:
        Voiceline('lc104')
    CommonSE('025_cleanhit_grap')
    ScreenShake(50000, 50000)
    GotoState('ranbu_Rod_Finish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc434_38', 4)
    sprite('lc434_39', 6)
    setInvincible(0)
    sprite('lc434_40', 6)
    sprite('lc434_41', 6)
    sprite('lc434_42', 18)
    SetXCollisionFromOrigin(-1)
    EnableAfterimage(1)
    AttackOff()
    sprite('lc434_43', 6)
    sprite('lc434_44', 6)
    sprite('lc434_45', 6)
    sprite('lc434_46', 6)
    sprite('lc434_47', 6)
    loopRest()
    ExitState()
    label(10)
    if SLOT_2:
        CameraControlEnable(1)
    sprite('lc215_06', 1)
    ObjectUpon2(11, 11, 0)
    sprite('lc215_07', 3)
    EndMomentum(0)
    sprite('lc215_08', 3)
    CommonSE('005_swing_grap_2_2')
    sprite('lc215_09', 3)
    RefreshMultihit()
    Stagger(75)
    Crumple(100)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    ResetPushbackX()

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SLOT_51 = 1
    sprite('lc215_10', 3)
    sprite('lc215_11', 1)
    CreateObject('LcefRodSet', 0)
    ObjectUpon2(11, 6, 0)
    sprite('lc215_11', 1)
    sprite('lc215_12', 2)
    AddX(-40000)
    sprite('lc215_13', 2)
    sprite('lc215_14', 1)
    sprite('lc215_14', 1)
    if SLOT_51:
        conditionalSendToLabel(99)
    loopRest()
    ExitState()
    label(99)
    EnableRapidCancel(0)
    sprite('lc434_10', 4)
    sprite('lc434_11', 4)
    CommonSE('005_swing_grap_2_2')
    sprite('lc434_12', 4)
    sprite('lc434_13', 4)
    sprite('lc434_14', 4)
    sprite('lc434_15', 4)
    sprite('lc434_16', 6)
    CommonSE('005_swing_grap_2_0')
    sprite('lc434_17', 8)
    sprite('lc434_18', 10)
    sprite('lc434_19', 6)
    physicsXImpulse(5000)
    CommonSE('003_swing_grap_0_1')
    sprite('lc434_20', 20)
    CreateObject('434atkeff2', -1)
    RefreshMultihit()
    Damage(2400)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    WallbounceReboundTime(1)
    AirPushbackX(80000)
    AirPushbackY(100)
    YImpulseBeforeWallbounce(0)
    HardKnockdown(15)
    DefeatOpponentBehavior(0)
    HitBackReturnObject(0)
    EndMomentum(1)
    if SLOT_43:
        Voiceline('lc105')
    else:
        Voiceline('lc104')
    PrivateSE('lcse_22')
    PrivateSE('lcse_22')
    ScreenShake(50000, 50000)
    XImpulseAcceleration(25)
    GotoState('ranbu_Rod_DFinish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc434_21', 4)
    setInvincible(0)
    XImpulseAcceleration(25)
    EnableAfterimage(0)
    sprite('lc434_22', 4)
    sprite('lc434_22ex', 10)
    XImpulseAcceleration(0)
    sprite('lc434_23', 4)
    sprite('lc434_24', 4)
    sprite('lc434_25', 4)
    sprite('lc434_26', 4)
    sprite('lc434_27', 4)
    sprite('lc434_28', 4)
    sprite('lc434_29', 4)


@State
def UltimateRush_NoRod_Ranbu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        AttackP2(96)
        MinimumDamage(15)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(0)
        PushbackX(5000)
        Hitstop(2)
        AirUntechableTime(80)
        Hitstun(30)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        callSubroutine('RodNoHit')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc419_07', 3)
    sprite('lc419_08', 3)
    sprite('lc419_09', 3)
    sprite('lc419_10', 3)
    sprite('lc215_00', 3)
    physicsXImpulse(-2000)
    LandingEffects(100, 1, 0)
    EnableAfterimage(1)
    SmartVoiceline('lc101')
    sprite('lc215_01', 3)
    sprite('lc215_02', 3)
    sprite('lc215_02', 5)
    sprite('lc215_03', 4)
    RefreshMultihit()
    CreateObject('LcefTetsuzanko', 0)
    DashEffects(100, 1, 0)
    physicsXImpulse(80000)
    sprite('lc210_02', 1)
    XImpulseAcceleration(10)
    sprite('lc210_04', 1)
    sprite('lc210_06', 1)
    sprite('lc210_07', 1)
    sprite('lc210_08', 1)
    sprite('lc210_09', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('lc210_10', 1)
    RefreshMultihit()
    sprite('lc210_11', 1)
    sprite('lc405_00', 1)
    sprite('lc405_01', 1)
    sprite('lc405_02', 1)
    XImpulseAcceleration(200)
    CommonSE('019_cloth_a')
    DashEffects(100, 1, 1)
    sprite('lc405_03', 1)
    sprite('lc405_04', 1)
    sprite('lc405_05', 1)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    XImpulseAcceleration(50)
    sprite('lc405_06', 1)
    XImpulseAcceleration(10)
    sprite('lc211_01', 1)
    StayAfterMovement(1, 0)
    AddX(-50000)
    sprite('lc211_02', 1)
    sprite('lc211_03', 1)
    sprite('lc211_04', 1)
    sprite('lc211_05', 1)
    sprite('lc211_07', 1)
    RefreshMultihit()
    CommonSE('004_swing_grap_1_1')
    sprite('lc211_08', 1)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(36000)
    sprite('lc212_01', 1)
    StayAfterMovement(0, 0)
    AddX(100000)
    sprite('lc212_02', 1)
    sprite('lc212_03', 1)
    sprite('lc212_05', 1)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_1')
    HitAnywhere(1)
    sprite('lc212_06', 1)
    HitAnywhere(0)
    sprite('lc212_07', 1)
    AirPushbackX(0)
    AirPushbackY(18000)
    sprite('lc407_01', 3)
    JumpEffects(0, -1)
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(1500)
    sprite('lc407_02', 2)
    CommonSE('019_cloth_a')
    sprite('lc407_03', 2)
    sprite('lc407_04', 2)
    RefreshMultihit()
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    CommonSE('003_swing_grap_0_2')
    sprite('lc407_05', 2)
    sprite('lc407_06', 2)
    AirPushbackX(2000)
    AirPushbackY(-2000)
    sprite('lc406_01', 2)
    XImpulseAcceleration(80)
    sprite('lc406_03', 2)
    JumpEffects(0, -1)
    sprite('lc406_05', 2)
    CommonSE('019_cloth_a')
    setGravity(1800)
    sprite('lc406_06', 2)
    sprite('lc406_07', 2)
    sprite('lc406_08', 2)
    RandomCommonVoiceline(0)
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    CommonSE('004_swing_grap_1_2')
    sprite('lc406_09', 2)
    sprite('lc406_11', 3)
    RefreshMultihit()
    sprite('lc406_12', 2)
    sprite('lc406_13', 2)
    sprite('lc406_14', 3)
    Hitstop(1)
    AirPushbackX(-2000)
    AirPushbackY(15000)
    sprite('lc201_00', 1)
    XImpulseAcceleration(15)
    sprite('lc201_01', 1)
    sprite('lc201_02', 1)
    sprite('lc201_03', 1)
    sprite('lc201_04', 1)
    sprite('lc201_05', 1)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_2')
    sprite('lc201_06', 1)
    AirPushbackX(0)
    AirPushbackY(25000)
    sprite('lc311_02', 2)
    sprite('lc311_03', 2)
    sprite('lc311_03', 2)
    sprite('lc311_05', 2)
    sprite('lc311_06', 2)
    sprite('lc311_07', 3)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    sprite('lc311_08', 3)
    sprite('lc311_09', 3)
    sprite('lc311_10', 3)
    sprite('lc311_11', 3)
    sprite('lc311_12', 3)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(5000)
    AirPushbackY(30000)
    sprite('lc261_00', 1)
    AddX(50000)
    sprite('lc261_01', 2)
    sprite('lc261_02', 2)
    sprite('lc261_03', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('lc261_04', 3)
    RefreshMultihit()
    EndMomentum(1)

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SetActionMark(1)
    sprite('lc261_05', 3)
    sprite('lc261_06', 3)
    sprite('lc261_07', 3)
    Stagger(75)
    Crumple(100)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    ResetPushbackX()
    sprite('lc202_01', 2)
    if SLOT_2:
        CameraControlEnable(1)
    physicsXImpulse(-4000)
    sprite('lc202_02', 2)
    sprite('lc202_03', 2)
    sprite('lc202_04', 4)
    CreateObject('LcefKikouCharge', 0)
    sprite('lc202_05', 4)
    XImpulseAcceleration(-300)
    RandomCommonVoiceline(2)
    sprite('lc202_06', 2)
    sprite('lc202_07', 2)
    sprite('lc202_09', 2)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_2')
    CommonSE('016_explode_0')
    CommonSE('004_swing_grap_1_1')
    CommonSE('005_swing_grap_2_1')
    CreateObject('LcefKikouPtc', 0)
    CreateObject('LcefKikouWave', 0)
    CreateParticle('lcef_202airwall01', 1)
    sprite('lc202_09', 1)
    RefreshMultihit()

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SLOT_51 = 1
    XImpulseAcceleration(0)
    sprite('lc202_10', 3)
    sprite('lc202_11', 3)
    sprite('lc202_13', 3)
    sprite('lc202_14', 2)
    sprite('lc202_15', 2)
    sprite('lc202_16', 2)
    sprite('lc202_17', 2)
    sprite('lc202_18', 2)
    sprite('lc202_19', 2)
    sprite('lc202_20', 1)
    sprite('lc202_20', 1)
    if SLOT_51:
        conditionalSendToLabel(2)
    loopRest()
    ExitState()
    label(2)
    EnableRapidCancel(0)
    sprite('lc434_10', 4)
    sprite('lc434_11', 4)
    CommonSE('005_swing_grap_2_2')
    sprite('lc434_12', 4)
    sprite('lc434_13', 4)
    sprite('lc434_14', 4)
    sprite('lc434_15', 4)
    sprite('lc434_16', 6)
    CommonSE('005_swing_grap_2_0')
    sprite('lc434_17', 8)
    sprite('lc434_18', 10)
    sprite('lc434_19', 6)
    physicsXImpulse(5000)
    CommonSE('004_swing_grap_1_0')
    sprite('lc434_20', 20)
    CreateObject('434atkeff2', -1)
    RefreshMultihit()
    Damage(2400)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    WallbounceReboundTime(1)
    AirPushbackX(80000)
    AirPushbackY(100)
    YImpulseBeforeWallbounce(0)
    HardKnockdown(15)
    DefeatOpponentBehavior(0)
    HitBackReturnObject(0)
    EndMomentum(1)
    if SLOT_43:
        Voiceline('lc105')
    else:
        Voiceline('lc104')
    PrivateSE('lcse_22')
    ScreenShake(50000, 50000)
    XImpulseAcceleration(25)
    GotoState('ranbu_NoRod_Finish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc434_21', 4)
    setInvincible(0)
    XImpulseAcceleration(25)
    EnableAfterimage(0)
    sprite('lc434_22', 4)
    sprite('lc434_22ex', 10)
    XImpulseAcceleration(0)
    sprite('lc434_23', 4)
    sprite('lc434_24', 4)
    sprite('lc434_25', 4)
    sprite('lc434_26', 4)
    sprite('lc434_27', 4)
    sprite('lc434_28', 4)
    sprite('lc434_29', 4)


@State
def UltimateRush_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(4)
        Damage(500)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(96)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(60)
        Crumple(45)
        Hitstop(20)
        AirUntechableTime(80)
        Hitstun(30)
        HardKnockdown(1)
        OppPositionOnHit(1, 250000, 0)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        EnterStateIfEventID(12, 'UltimateRush_OD_Ranbu')
        AttackType(4)

        def upon_OPPONENT_HIT():
            ForceFaceSprite()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc434_00', 6)
    SmartVoiceline('lc253')
    CreateObject('EMB_LC', -1)
    DistortionSettings(55, -1, 0)
    HeatChange(-5000)
    CreateObject('DistAura', -1)
    sprite('lc434_01', 6)
    sprite('lc434_02', 6)
    sprite('lc434_03', 6)
    sprite('lc434_04', 8)
    CreateObject('aurastart', -1)
    sprite('lc434_05', 8)
    sprite('lc434_06', 8)
    CreateObject('auraball', -1)
    sprite('lc434_07', 8)
    sprite('lc434_08', 3)
    sprite('lc434_09', 3)
    sprite('lc419_02', 2)
    physicsXImpulse(60000)
    if SLOT_51:
        XImpulseAcceleration(75)
    AltKnockdownEffects(100, 1, 1)
    sprite('lc419_03', 2)
    sprite('lc419_04', 2)
    XImpulseAcceleration(30)
    CommonSE('003_swing_grap_0_1')
    CommonSE('004_swing_grap_1_2')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    CommonSE('016_explode_0')
    callSubroutine('RodNoHit')
    sprite('lc419_05ex', 3)
    XImpulseAcceleration(0)
    RefreshMultihit()
    sprite('lc419_06ex', 3)
    sprite('lc419_06ex', 3)
    AttackOff()
    clearUponHandler(EVERY_FRAME)
    setInvincible(0)
    sprite('lc419_07', 6)
    sprite('lc419_08', 6)
    sprite('lc419_09', 6)
    sprite('lc419_10', 6)


@State
def UltimateRush_OD_Ranbu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackType(4)
        AttackLevel_(4)
        Damage(300)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(96)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(0)
        PushbackX(5000)
        Hitstop(1)
        AirUntechableTime(80)
        Hitstun(30)
        HardKnockdown(1)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        callSubroutine('RodNoHit')

        def upon_STATE_END():
            SetZVal(0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('lc419_07', 3)
    sprite('lc419_08', 3)
    sprite('lc419_09', 3)
    sprite('lc419_10', 3)
    sprite('lc215_00', 3)
    physicsXImpulse(-2000)
    LandingEffects(100, 1, 0)
    EnableAfterimage(1)
    SmartVoiceline('lc101')
    sprite('lc215_01', 3)
    sprite('lc215_02', 3)
    sprite('lc215_02', 5)
    sprite('lc215_03', 4)
    RefreshMultihit()
    CreateObject('LcefTetsuzanko', 0)
    DashEffects(100, 1, 0)
    physicsXImpulse(80000)
    sprite('lc210_02', 1)
    XImpulseAcceleration(10)
    sprite('lc210_04', 1)
    sprite('lc210_06', 1)
    sprite('lc210_07', 1)
    sprite('lc210_08', 1)
    sprite('lc210_09', 1)
    CommonSE('003_swing_grap_0_1')
    CommonSE('004_swing_grap_1_0')
    CommonSE('004_swing_grap_1_1')
    sprite('lc210_10', 1)
    RefreshMultihit()
    sprite('lc210_11', 1)
    sprite('lc405_00', 1)
    sprite('lc405_01', 1)
    sprite('lc405_02', 1)
    XImpulseAcceleration(200)
    CommonSE('019_cloth_a')
    DashEffects(100, 1, 1)
    sprite('lc405_03', 1)
    sprite('lc405_04', 1)
    sprite('lc405_05', 1)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_1')
    CommonSE('004_swing_grap_1_2')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    XImpulseAcceleration(50)
    sprite('lc405_06', 1)
    XImpulseAcceleration(10)
    sprite('lc211_01', 1)
    StayAfterMovement(1, 0)
    AddX(-50000)
    sprite('lc211_02', 1)
    sprite('lc211_03', 1)
    sprite('lc211_04', 1)
    sprite('lc211_05', 1)
    sprite('lc211_07', 1)
    RefreshMultihit()
    CommonSE('004_swing_grap_1_1')
    CommonSE('004_swing_grap_1_0')
    sprite('lc211_08', 1)
    PushbackX(-3000)
    sprite('lc212_01', 1)
    StayAfterMovement(0, 0)
    AddX(100000)
    XImpulseAcceleration(200)
    sprite('lc212_02', 1)
    sprite('lc212_03', 1)
    sprite('lc212_05', 1)
    RefreshMultihit()
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_1')
    sprite('lc212_06', 1)
    sprite('lc212_07', 1)
    PushbackX(0)
    sprite('lc407_01', 3)
    JumpEffects(0, -1)
    physicsXImpulse(3000)
    physicsYImpulse(30000)
    setGravity(1500)
    sprite('lc407_02', 2)
    CommonSE('019_cloth_a')
    sprite('lc407_03', 2)
    sprite('lc407_04', 2)
    RefreshMultihit()
    CommonSE('019_cloth_c')
    CommonSE('019_cloth_a')
    CommonSE('005_swing_grap_2_1')
    CommonSE('003_swing_grap_0_2')
    CommonSE('004_swing_grap_1_1')
    sprite('lc407_05', 2)
    sprite('lc407_06', 2)
    sprite('lc406_01', 2)
    XImpulseAcceleration(200)
    sprite('lc406_03', 2)
    JumpEffects(0, -1)
    sprite('lc406_05', 2)
    CommonSE('019_cloth_a')
    setGravity(2200)
    sprite('lc406_06', 2)
    sprite('lc406_07', 2)
    sprite('lc406_08', 2)
    RandomCommonVoiceline(0)
    CommonSE('019_cloth_c')
    CommonSE('004_swing_grap_1_1')
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_0')
    sprite('lc406_09', 2)
    sprite('lc406_11', 3)
    RefreshMultihit()

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SLOT_51 = 1
        PerGravity(50)
    sprite('lc406_12', 2)
    sprite('lc406_13', 2)
    sprite('lc406_14', 2)
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('lc020_06', 4)
    XImpulseAcceleration(80)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 101)
    label(100)
    sprite('lc020_07', 4)
    XImpulseAcceleration(90)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(100)
    label(101)
    clearUponHandler(LANDING)
    sprite('lc406_15', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc406_16', 2)
    sprite('lc405_13', 2)
    sprite('lc405_14', 3)
    sprite('lc405_15', 2)
    loopRest()
    ExitState()
    label(0)
    AttackLevel_(2)
    Damage(100)
    AttackP2(99)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    PushbackX(500)
    Hitstop(2)

    def upon_OPPONENT_HIT():
        ScreenShake(0, 2000)
    EndMomentum(1)
    AddX(30000)
    physicsXImpulse(2000)
    setGravity(100)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc450_22', 3)
    sprite('lc450_23', 2)
    SetZVal(-500)
    RefreshMultihit()
    Voiceline('lc108')
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_23', 1)
    RefreshMultihit()
    UseFireHitspark(1)
    AttackLevel_(5)
    Damage(150)
    PushbackX(1000)
    setGravity(150)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc450_24', 1)
    RefreshMultihit()
    UseFireHitspark(0)
    sprite('lc450_25', 1)
    RefreshMultihit()
    sprite('lc450_26', 1)
    RefreshMultihit()
    sprite('lc450_23', 1)
    RefreshMultihit()
    UseFireHitspark(1)
    sprite('lc450_24', 1)
    RefreshMultihit()
    UseFireHitspark(0)
    sprite('lc450_25', 1)
    RefreshMultihit()
    sprite('lc450_26', 1)
    RefreshMultihit()
    sprite('lc450_23', 1)
    RefreshMultihit()
    UseFireHitspark(1)
    sprite('lc450_24', 1)
    RefreshMultihit()
    UseFireHitspark(0)
    sprite('lc450_25', 1)
    RefreshMultihit()
    UseFireHitspark(1)
    sprite('lc450_26', 1)
    RefreshMultihit()
    UseFireHitspark(0)
    sprite('lc450_23', 1)
    RefreshMultihit()
    UseFireHitspark(1)
    sprite('lc450_24', 1)
    RefreshMultihit()
    sprite('lc450_25', 1)
    RefreshMultihit()
    sprite('lc450_26', 1)
    RefreshMultihit()
    sprite('lc212_11', 3)
    physicsXImpulse(2000)
    physicsYImpulse(8000)
    setGravity(1450)
    sprite('lc212_12', 3)
    sprite('lc212_14', 3)
    sprite('lc212_15', 3)
    sprite('lc212_16', 3)
    sprite('lc212_17', 3)
    CommonSE('003_swing_grap_0_1')
    AttackLevel_(4)
    Damage(300)
    AttackP2(96)
    UseFireHitspark(0)
    RefreshMultihit()

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        SetActionMark(1)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc212_18', 3)
    sprite('lc212_19', 3)
    sprite('lc420_00', 2)
    if SLOT_2:
        CameraControlEnable(1)
    CreateObject('UltimateRush_Dragon', -1)
    EndMomentum(1)

    def upon_32():
        SLOT_52 = 1
    sprite('lc420_01', 2)
    sprite('lc420_02', 2)
    sprite('lc420_03', 2)
    sprite('lc420_04', 2)
    sprite('lc420_02', 2)
    sprite('lc420_03', 2)
    sprite('lc420_05', 2)
    sprite('lc420_06', 2)
    Voiceline('lc109')
    CommonSE('003_swing_grap_0_2')
    sprite('lc420_07', 2)
    sprite('lc420_08', 2)
    sprite('lc420_09', 2)
    sprite('lc420_10', 2)
    sprite('lc420_11', 2)
    sprite('lc420_12', 7)
    sprite('lc420_12', 1)
    if SLOT_52:
        conditionalSendToLabel(2)
    sprite('lc420_13', 5)
    sprite('lc420_14', 5)
    loopRest()
    ExitState()
    label(2)
    EnableRapidCancel(0)
    sprite('lc434_10', 4)
    sprite('lc434_11', 4)
    CommonSE('005_swing_grap_2_1')
    sprite('lc434_12', 4)
    sprite('lc434_13', 4)
    sprite('lc434_14', 4)
    sprite('lc434_15', 4)
    sprite('lc434_16', 6)
    CommonSE('005_swing_grap_2_2')
    sprite('lc434_17', 8)
    sprite('lc434_18', 10)
    sprite('lc434_19', 6)
    physicsXImpulse(5000)
    CommonSE('004_swing_grap_1_0')
    sprite('lc434_20', 20)
    CreateObject('434atkeff2', -1)
    RefreshMultihit()
    Damage(1800)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    WallbounceReboundTime(1)
    AirPushbackX(80000)
    AirPushbackY(100)
    YImpulseBeforeWallbounce(0)
    HardKnockdown(15)
    DefeatOpponentBehavior(0)
    HitBackReturnObject(0)
    EndMomentum(1)
    if SLOT_43:
        Voiceline('lc105')
    else:
        Voiceline('lc104')
    PrivateSE('lcse_22')
    CommonSE('025_cleanhit_grap')
    CommonSE('025_cleanhit_grap')
    ScreenShake(50000, 50000)
    XImpulseAcceleration(25)
    GotoState('ranbu_OD_Finish')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('lc434_21', 4)
    setInvincible(0)
    XImpulseAcceleration(25)
    EnableAfterimage(0)
    sprite('lc434_22', 4)
    sprite('lc434_22ex', 10)
    XImpulseAcceleration(0)
    sprite('lc434_23', 4)
    sprite('lc434_24', 4)
    sprite('lc434_25', 4)
    sprite('lc434_26', 4)
    sprite('lc434_27', 4)
    sprite('lc434_28', 4)
    sprite('lc434_29', 4)


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
        DamageFromStateOnly('RodBurstDD')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(70000)
            ObjectUpon2(11, 0, 0)
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)
            SLOT_62 = 1

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)
            TriggerUponForState('RodOverDriveAttack', 36)

        def upon_STATE_END():
            DepleteOD()
            SLOT_62 = 0
    sprite('lc040_01ex01', 3)
    SmartVoiceline('lc280')
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('lc312_00ex01', 4)
    sprite('lc312_01ex01', 4)
    sprite('lc312_02ex01', 4)
    physicsXImpulse(3000)
    sprite('lc312_03ex01', 4)
    XImpulseAcceleration(2000)
    sprite('lc312_04ex01', 3)
    EndMomentum(1)
    sprite('lc312_04ex01', 5)
    AttackOff()
    setInvincible(0)
    sprite('lc312_05ex01', 8)
    sprite('lc312_06ex01', 6)
    sprite('lc312_07ex01', 5)
    sprite('lc312_08ex01', 5)
    sprite('lc312_09ex01', 5)


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
        DamageFromStateOnly('RodBurstDD')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(70000)
            ObjectUpon2(11, 0, 0)
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)
            SLOT_62 = 1

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)
            TriggerUponForState('RodOverDriveAttack', 36)

        def upon_STATE_END():
            DepleteOD()
            SLOT_62 = 0
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('lc040_01ex01', 1)
    SmartVoiceline('lc280')
    E0EAEffect('BurstDDeff', 103)
    setInvincible(1)
    EndMomentum(1)
    sprite('lc312_00ex01', 2)
    sprite('lc312_01ex01', 2)
    sprite('lc312_02ex01', 2)
    physicsXImpulse(6000)
    sprite('lc312_03ex01', 2)
    XImpulseAcceleration(2000)
    CommonSE('005_swing_grap_2_2')
    sprite('lc312_04ex01', 3)
    EndMomentum(1)
    sprite('lc312_04ex01', 5)
    AttackOff()
    setInvincible(0)
    sprite('lc312_05ex01', 8)
    sprite('lc312_06ex01', 6)
    sprite('lc312_07ex01', 5)
    sprite('lc312_08ex01', 5)
    sprite('lc312_09ex01', 5)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(1634)
        AirUntechableTime(100)
        Hitstop(0)
        EnemyHitstopAddition(30, 30, 30)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(100000)
        YImpulseBeforeWallbounce(5000)
        DefeatOpponentBehavior(0)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        if SLOT_51:
            Damage(3610)

        def upon_OPPONENT_HIT():
            AddCombo(1)

        def upon_STATE_END():
            DespawnEAEffect('BurstDD_Camera')
            EnableCollision(1)
            WallCollisionDetection(1)
            HUDVisibillity(0)
        SetBackground(1)
        EnableCollision(0)
        HitAnywhere(1)
    sprite('lc312_05ex01', 5)
    sprite('lc312_06ex01', 5)
    sprite('lc440_00', 3)
    uponSendToLabel(33, 1)
    CreateParticle('lcef_mantenlight', 0)
    CreateObject('LcefRodReturnDD', 0)
    ObjectUpon2(11, 49, 0)
    SLOT_52 = 10
    label(0)
    sprite('lc440_01', 3)
    SLOT_52 = SLOT_52 + -1
    sprite('lc440_02', 3)
    sprite('lc440_03', 3)
    loopRest()
    if SLOT_52:
        conditionalSendToLabel(0)
    label(1)
    sprite('lc418_07ex01', 2)
    CreateObject('BurstDD_Camera', -1)
    RegisterObject(4, 1)
    sprite('lc418_08ex01', 2)
    sprite('lc418_09ex01', 2)
    ObjectUpon(FALLING, 33)
    EnableCollision(0)
    WallCollisionDetection(0)
    HUDVisibillity(1)
    sprite('lc409_00ex01', 2)
    CopyFromRightToLeft(23, 2, 52, 4, 2, 83)
    if SLOT_IsFacingRight:
        PrivateFunction(0, 2, 52, 0, 900000, 2, 53)
    else:
        PrivateFunction(0, 2, 52, 0, -900000, 2, 53)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_53 <= SLOT_XDistanceFromCenterOfStage:
                XImpulseAcceleration(0)
        elif SLOT_53 >= SLOT_XDistanceFromCenterOfStage:
            XImpulseAcceleration(0)
    physicsXImpulse(-22000)
    physicsYImpulse(40000)
    setGravity(3000)
    sprite('lc409_01ex01', 2)
    sprite('lc409_02ex01', 4)
    sprite('lc409_03ex01', 4)
    sprite('lc409_04ex01', 4)
    sprite('lc409_05ex01', 4)
    sprite('lc409_06ex01', 4)
    uponSendToLabel(LANDING, 3)
    label(2)
    sprite('lc409_07ex01', 3)
    sprite('lc409_08ex01', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('lc450_15ex01', 2)
    sprite('lc450_16ex01', 4)
    sprite('lc450_17ex01', 4)
    sprite('lc450_18ex01', 4)
    sprite('lc450_16ex01', 4)
    sprite('lc450_17ex01', 4)
    sprite('lc450_18ex01', 3)
    CommonSE('002_highjump_1')
    TriggerUponForState('RodBurstDD', 34)
    clearUponHandler(EVERY_FRAME)
    EndMomentum(1)

    def RunOnObject_22():
        TeleportToObject(22)
        AddX(-920000)
        physicsXImpulse(0)
        AbsoluteY(1830000)
        physicsYImpulse(-10000)
        setGravity(0)
    sprite('lc450_19ex01', 3)
    ObjectUpon(FALLING, 34)
    sprite('lc450_20ex01', 3)
    sprite('lc409_14ex01', 3)
    physicsXImpulse(33000)
    physicsYImpulse(68000)
    EnableAfterimage(1)
    sprite('lc409_15ex01', 3)
    sprite('lc409_14ex01', 3)
    sprite('lc409_15ex01', 3)
    sprite('lc409_14ex01', 3)
    sprite('lc440_04', 3)
    TriggerUponForState('RodBurstDD', 35)
    uponSendToLabel(LANDING, 5)
    sprite('lc440_05', 3)
    SmartVoiceline('lc281')
    sprite('lc440_06', 1)
    CreateObject('BurstDD_BG', 0)
    CommonSE('016_explode_1')
    CommonSE('025_cleanhit_grap')
    if SLOT_51:
        CreateObject('BurstDD_bomb', -1)
        CommonSE('025_cleanhit_grap')
        PrivateSE('lcse_22')
        EnemyHitstopAddition(57, 57, 57)
    physicsXImpulse(52800)
    physicsYImpulse(34000)
    setGravity(2200)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('lc440_06', 2)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    loopRest()
    if not SLOT_51:
        notConditionalSendToLabel(31)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    sprite('lc440_07', 3)
    sprite('lc440_08', 3)
    sprite('lc440_09', 3)
    label(31)
    sprite('lc440_07', 2)
    TriggerUponForState('BurstDD_BG', 32)
    HUDVisibillity(0)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    sprite('lc440_08', 2)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('lc440_10', 3)
    XImpulseAcceleration(80)
    YAccel(50)
    sprite('lc440_11', 3)
    ObjectUpon(FALLING, 35)
    XImpulseAcceleration(80)
    YAccel(50)
    loopRest()
    TriggerUponForState('RodBurstDD', 37)
    label(4)
    sprite('lc409_21ex01', 3)
    XImpulseAcceleration(70)
    sprite('lc409_21ex01', 3)
    XImpulseAcceleration(70)
    sprite('lc409_22ex01', 3)
    XImpulseAcceleration(70)
    sprite('lc409_22ex01', 3)
    XImpulseAcceleration(70)
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('lc409_23ex01', 2)
    EndMomentum(1)
    sprite('lc409_24ex01', 5)
    sprite('lc409_25ex01', 5)
    sprite('lc409_26ex01', 5)
    sprite('lc409_27ex01', 5)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DefeatOpponentBehavior(1)
        AttackLevel_(4)
        Damage(0)
        MinimumDamage(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackDirection(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(200)
        MoveAttributes(1, 0, 0, 0, 0)
        AirUntechableTime(200)
        Hitstun(200)
        HardKnockdown(200)
        Hitstop(20)
        EnemyHitstopAddition(20, 50, 50)
        OppPositionOnHit(3, 128000, -256000)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        DisableOppPushCollision(1)
        DamageFromStateOnly('AstralHeat2')
        PreventBlocking(1)
        ExternalForcesRate(0, 0)
        SetXCollisionFromOrigin(1)
        setInvincible(1)
        if SLOT_OverdriveTimer:
            EndMomentum(1)
        else:
            EnableCollision(0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)

        def upon_OPPONENT_HIT():
            clearUponHandler(LANDING)
            enterState('AstralHeat2')
        IgnoreTurn(1)
    sprite('lc450_00', 2)
    sprite('lc432_00', 2)
    AddX(8000)
    AddY(12500)
    sprite('lc432_01', 2)
    sprite('lc432_02', 2)
    sprite('lc432_03', 2)
    sprite('lc432_04', 2)
    sprite('lc432_05', 2)
    CommonSE('019_cloth_b')
    sprite('lc432_06', 2)
    sprite('lc432_07', 2)
    sprite('lc432_08', 2)
    sprite('lc432_09', 2)
    sprite('lc450_01', 2)
    sprite('lc450_02', 45)
    DistortionSettings(81, -1, 2)
    EnableCollision(0)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_LC_AH', -1)
    AddX(2000)
    AddY(-8000)
    UsePunchHitspark(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(10)
    AfterimageMask_1(0, 255, 128, 0)
    AfterimageMask_2(0, 255, 128, 0)
    AfterimageSize_1(1000)
    AfterimageSize_2(1500)
    Voiceline('lc290')
    sprite('lc450_03', 4)
    sprite('lc450_04', 4)
    sprite('lc450_05', 6)
    CreateParticle('lcef_aststart', -1)
    sprite('lc450_06', 2)
    CommonSE('002_highjump_0')
    CommonSE('002_highjump_2')
    CommonSE('002_highjump_1')
    CommonSE('015_blaze_1')
    ScreenShake(0, 6000)
    sprite('null', 19)
    CreateObject('AstJumpLC', -1)
    sprite('null', 1)
    if CheckInput(0x79):
        Flip()
    SetXCollisionFromOrigin(100)
    loopRest()
    uponSendToLabel(RELEASE_D, 2)
    sprite('null', 100)
    loopRest()
    label(2)
    clearUponHandler(RELEASE_D)
    sprite('lc450_07', 3)
    PreventBlocking(0)
    SetPosXByScreenPer(50)
    AddX(-540000)
    AbsoluteY(320000)
    physicsXImpulse(96000)
    physicsYImpulse(-9000)
    EndYPhysicsImpulse()
    ScreenShake(0, 14500)
    CommonSE('015_blaze_2')
    EnableCollision(1)
    loopRest()
    label(0)
    sprite('lc450_07', 3)
    CommonSE('019_cloth_b')
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    sprite('lc450_08', 3)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    sprite('lc450_09', 3)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    CreateParticle('lcef_astatkjump', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    EnableAfterimage(0)
    SetBackground(0)
    sprite('lc450_38', 6)
    JumpEffects(0, -1)
    DashEffects(100, 1, 1)
    XImpulseAcceleration(50)
    SetBackground(0)
    EnableAfterimage(0)
    setInvincible(0)
    sprite('lc450_39', 4)
    DashEffects(100, 1, 1)
    XImpulseAcceleration(10)
    sprite('lc450_39', 3)
    DashEffects(100, 1, 1)
    sprite('lc450_40', 6)
    sprite('lc205_06', 5)
    physicsXImpulse(0)
    sprite('lc205_07', 5)
    sprite('lc205_08', 5)
    sprite('lc205_09', 5)
    sprite('lc205_10', 5)
    sprite('lc205_11', 5)
    WhiffCrouchBlockCancel(1)
    IgnoreTurn(0)
    sprite('lc205_12', 5)
    sprite('lc205_13', 5)
    sprite('lc205_14', 5)
    sprite('lc205_15', 5)
    sprite('lc205_16', 5)
    loopRest()


@State
def AstralHeat2():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(1000)
        MinimumDamage(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(1000)
        AirPushbackX(-500)
        AirPushbackY(63000)
        YImpulseBeforeWallbounce(600)
        Hitstop(20)
        DisableOppPushCollision(1)
        UsePunchHitspark(1)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        setInvincible(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoCeiling(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        PlayPlayAstralBGM(1)
        AstralHeatCleanup(1, 0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        HUDVisibillity(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(10)
        AfterimageMask_1(0, 0, 0, 255)
        AfterimageMask_2(0, 0, 0, 255)
        AfterimageSize_1(1000)
        AfterimageSize_2(1300)
    sprite('lc450_10', 4)
    physicsXImpulse(15000)
    physicsYImpulse(-10000)
    SetAcceleration(-1000)
    setGravity(1000)
    sprite('lc450_11', 4)
    sprite('lc450_12', 4)
    PreDashEffects(100, 1, 1)
    SetAcceleration(0)
    sprite('lc212_05ah', 2)
    HitAnywhere(1)
    ForceFaceSprite()
    physicsXImpulse(20000)
    SetAcceleration(-2000)
    AbsoluteY(0)
    CameraFast(1)
    CameraForAstralHeat(30, 80)
    ScreenShake(0, 18500)
    CommonSE('004_swing_grap_1_2')
    CommonSE('004_swing_grap_1_1')
    if SLOT_43:
        Voiceline('lc154')
    else:
        Voiceline('lc153')
    sprite('lc212_06ah', 2)
    CameraFast(0)
    sprite('lc450_13', 2)
    sprite('lc450_14', 2)
    sprite('lc450_15', 2)
    JumpEffects(0, -1)
    CommonSE('208_brake_normal')
    sprite('lc450_16', 4)
    SetAcceleration(-2500)
    physicsXImpulse(40000)
    PreDashEffects(100, 1, 0)
    CommonSE('208_brake_normal')
    sprite('lc450_17', 4)
    PreDashEffects(100, 1, 0)
    DashEffects(100, 1, 0)
    CommonSE('208_brake_normal')
    sprite('lc450_18', 4)
    DashEffects(100, 1, 0)
    DashEffects(100, 1, 0)
    CommonSE('208_brake_normal')
    sprite('lc450_19', 4)
    DashEffects(100, 1, 0)
    sprite('lc450_20', 16)
    EndMomentum(1)
    DashEffects(100, 1, 1)
    sprite('lc405_01', 4)
    JumpEffects(3, -1)
    CommonSE('000_airdash_2')
    CameraFast(1)
    physicsXImpulse(-6000)
    physicsYImpulse(4000)
    CreateObject('AstWhite', -1)
    ConstantAlphaModifier(-25)
    sprite('lc405_02', 4)
    EndMomentum(1)
    setGravity(0)
    sprite('null', 30)
    sprite('null', 30)
    AddX(-400000)
    AbsoluteY(3600000)
    SetBackground(2)
    sprite('lc450_21', 10)
    DistortionSettings(240, -1, 1)
    ConstantAlphaModifier(30)
    SetZVal(500)
    AstralHeatCleanup(1, 0)
    CommonSE('000_airdash_0')
    sprite('lc450_22', 30)
    CameraFast(0)
    sprite('null', 5)
    CreateObject('AstCutA', -1)
    AbsoluteY(3600000)
    CreateObject('CyuRenPouTou', -1)
    sprite('null', 75)
    Voiceline('lc291')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    OppPositionOnHit(1, 140000, -160000)
    AttackP2(99)
    Damage(375)
    MinimumDamage(100)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpulseBeforeWallbounce(0)
    Hitstop(2)

    def upon_OPPONENT_HIT():
        ScreenShake(0, 8500)
        if SLOT_2:
            ScreenShake(0, 8500)
            SetActionMark(0)
            AddCombo(2)
            if SLOT_51:
                AddCombo(1)
        else:
            ScreenShake(8500, 0)
            SetActionMark(1)
            if SLOT_51:
                AddCombo(1)
    sprite('lc450_23', 2)
    RefreshMultihit()
    SetZVal(-500)
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    SLOT_51 = 1
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_23', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_24', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_25', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    sprite('lc450_26', 2)
    RefreshMultihit()
    OppPositionOnHit(0, 0, 0)
    AirPushbackX(-4000)
    EndMomentum(1)
    setGravity(0)
    sprite('lc450_27', 5)
    clearUponHandler(OPPONENT_HIT)
    physicsXImpulse(4000)
    physicsYImpulse(5000)
    setGravity(350)
    SetZVal(500)
    sprite('lc450_28', 5)
    sprite('lc450_29', 5)
    sprite('lc450_30', 5)
    sprite('lc450_31', 5)
    sprite('lc450_32', 5)
    sprite('lc450_33', 5)
    sprite('lc450_34', 5)
    sprite('lc450_35', 5)
    EndMomentum(1)
    setGravity(0)
    ScreenShake(0, 17500)
    CommonSE('004_swing_grap_1_1')
    CommonSE('004_swing_grap_1_2')
    CameraFast(1)
    sprite('lc450_36', 3)
    SetZVal(0)
    PrivateSE('lcse_21')
    CommonSE('025_cleanhit_grap')
    CommonSE('025_cleanhit_grap')
    if SLOT_43:
        Voiceline('lc105')
    else:
        Voiceline('lc104')
    sprite('lc450_37', 3)
    Damage(16000)
    DefeatOpponentBehavior(3)
    HitAnywhere(1)
    EnemyHitstopAddition(0, 0, 0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(25)
    AirPushbackX(64000)
    AirPushbackY(-56000)
    YImpulseBeforeWallbounce(1500)
    RefreshMultihit()
    ParticleRotationAngle(-30000)
    CallCustomizableParticle('lcef_AH_shock', 0)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    sprite('lc450_36', 3)
    sprite('lc450_37', 3)
    SLOT_61 = 1
    sprite('null', 20)
    XPositionRelativeFacing(0)
    AbsoluteY(800000)
    setGravity(500)
    Flip()
    ForceShadowOn(1)
    CameraFast(0)
    CreateObject('LastLookAtStage', -1)
    EnableAfterimage(0)
    SetBackground(0)
    KeepBackground(1)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 3)
    label(2)
    sprite('lc020_07', 4)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('lc450_41', 6)
    LandingEffects(100, 1, 1)
    sprite('lc450_42', 6)
    sprite('lc450_43', 6)
    sprite('lc450_44', 6)
    sprite('lc450_45', 6)
    sprite('lc450_46', 6)
    sprite('lc450_47', 6)
    sprite('lc450_48', 6)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_PLAYER_DAMAGED():
            Voiceline('lc054')
    sprite('lc900_00', 32767)
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
        AbsoluteY(240000)
    sprite('lc901_00', 50)
    physicsYImpulse(-150)
    sprite('lc901_00', 50)
    physicsYImpulse(150)
    Voiceline('lc055')
    Mouth(13665, 13667, 13665, 13667, 13665, 13667, 13153, 25392, 53, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('lc901_00', 50)
    physicsYImpulse(-150)
    sprite('lc901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('lc000', 13923, 24880, 25398, 24886, 25398, 24886, 25398, 
        24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc056', 13921, 13923, 13921, 13923, 13921, 13923, 12897, 
        25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc400', 12641, 25392, 13362, 13921, 13923, 13921, 13923, 
        13921, 13667, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc401', 13921, 13923, 13921, 12899, 24880, 25398, 24886, 
        25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc404', 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
        24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc406', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc407', 14179, 24880, 25400, 24887, 25400, 24887, 25400, 
        24887, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc408', 14433, 14179, 14433, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc412', 14689, 13411, 24880, 25401, 24889, 25401, 24889, 
        25401, 24889, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc413', 14177, 14179, 14177, 14179, 14177, 13155, 24880, 
        25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 55, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc414', 14177, 14179, 14177, 12899, 24880, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc415', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc416', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('lc417', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('lc000', 14433, 14435, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 14433, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('lc400', 12643, 24882, 25399, 24887, 25399, 55, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc401', 13921, 13923, 13921, 13923, 13921, 12643, 
            24880, 25398, 24886, 25398, 24886, 25398, 24886, 25397, 24885, 
            25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc404', 14433, 14435, 14433, 13923, 24880, 25398, 
            24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc405', 14177, 14179, 14177, 14179, 14177, 12643, 
            24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('lc406', 13923, 14177, 14179, 14177, 14179, 14177, 
            14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc407', 14177, 14179, 14177, 14179, 14177, 13411, 
            24880, 25400, 13362, 13409, 25394, 13618, 14433, 14435, 14433, 
            14435, 12897, 25392, 13874, 14177, 12643, 24880, 25399, 24887, 
            25398, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )
        Unknown18011('lc408', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 
            25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc412', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('lc413', 14433, 14435, 14433, 14435, 14433, 14435, 
            13153, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc414', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc415', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc416', 14433, 12643, 24880, 12337, 14435, 14433, 
            14435, 14433, 14435, 14433, 13923, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('lc417', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('tk'):
            Unknown18011('lc000', 14433, 13411, 24880, 25399, 24887, 25399,
                24887, 25399, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc400', 14177, 14179, 14177, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('lc401', 12641, 25397, 24887, 25399, 12339, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tg'):
            Unknown18011('lc000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('lc400', 14177, 14179, 14177, 14179, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc401', 13921, 13923, 13921, 13923, 13921, 12899,
                24885, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ar'):
            Unknown18011('lc000', 14177, 13155, 24880, 25399, 24887, 25399,
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc400', 13921, 13923, 13921, 13923, 13921, 13923,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc401', 13921, 13923, 13921, 13923, 13921, 13667,
                24885, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('bn'):
            Unknown18011('lc000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('lc400', 13921, 13923, 13921, 13923, 13921, 13923,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('lc401', 12641, 25398, 12339, 14433, 14435, 14433,
                14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
                14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('lc000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('lc400', 13921, 13923, 13921, 13923, 13921, 13923,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('lc401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                12641, 25397, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tk'):
            Unknown18011('lc508', 14177, 14179, 14177, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 13411, 24885, 25399, 
                13622, 14177, 14179, 14177, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc509', 14177, 12899, 24880, 25399, 12340, 13921,
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('tg'):
            Unknown18011('lc510', 14433, 14435, 14433, 13923, 24880, 25400,
                24888, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('lc511', 14177, 14179, 14177, 14179, 14433, 12899,
                24880, 25398, 24886, 25398, 24886, 25398, 13621, 14177, 
                13667, 14177, 13923, 24882, 25398, 24886, 25398, 24886, 
                25398, 24886, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ar'):
            Unknown18011('lc514', 14177, 13411, 24885, 25398, 24886, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc515', 14177, 14179, 14177, 13923, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('bn'):
            Unknown18011('lc516', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25399, 24887, 25399, 13617, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc517', 13921, 13923, 13921, 13923, 13921, 13667,
                24880, 25398, 24886, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('lc546', 13921, 13667, 24882, 25398, 24888, 25399,
                12344, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 12899, 24880, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('lc547', 13921, 13411, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13411, 24885, 25397, 24885, 25397, 
                24885, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('lc546', 12897, 25392, 24886, 25398, 12342, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('lc547', 13921, 13411, 13921, 13923, 13921, 
                    12899, 24882, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
        if CharacterIDCheck('kk'):
            if SLOT_138:
                Unknown18011('lc548', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('lc549', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('lc548', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13155, 24880,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('lc549', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 12899, 24885, 25398, 24886, 25398, 24886,
                    25397, 24885, 12337, 13667, 13665, 13667, 13665, 13667,
                    12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tk'):
        SyncEntry()
        gotoLabel(140)
    if CharacterIDCheck('tg'):
        SyncEntry()
        gotoLabel(150)
    if CharacterIDCheck('ar'):
        SyncEntry()
        gotoLabel(170)
    if CharacterIDCheck('bn'):
        SyncEntry()
        gotoLabel(180)
    if CharacterIDCheck('kg'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('kk'):
        if SLOT_138:
            gotoLabel(340)
        else:
            gotoLabel(1340)
    label(482)
    if random_(2, 0, 12):
        conditionalSendToLabel(1)
    if random_(2, 0, 25):
        conditionalSendToLabel(2)
    label(0)
    sprite('lc600_00', 6)
    ObjectUpon2(11, 11, 0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('lc600_00', 50)
    if SLOT_44:
        Voiceline('lc412')
    sprite('lc600_00', 40)
    if SLOT_43:
        Voiceline('lc412')
    sprite('lc600_01', 6)
    sprite('lc600_02', 6)
    sprite('lc600_03', 6)
    sprite('lc600_04', 6)
    sprite('lc600_05', 6)
    sprite('lc600_06', 6)
    sprite('lc600_07', 8)
    sprite('lc600_08', 7)
    sprite('lc600_09', 7)
    sprite('lc600_10', 6)
    CreateObject('RodEntry600', -1)
    CommonSE('200_walk_normal_1')
    sprite('lc600_11', 6)
    sprite('lc600_12', 6)
    sprite('lc600_13', 6)
    sprite('lc600_14', 6)
    sprite('lc600_15', 6)
    ObjectUpon2(11, 10, 0)
    sprite('lc600_16', 5)
    Voiceline('lc413')
    if SLOT_43:
        DemoTimer(140)
    else:
        DemoTimer(110)
    loopRest()
    ExitState()
    label(1)
    sprite('lc600_00', 6)
    ObjectUpon2(11, 11, 0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('lc600_00', 125)
    Voiceline('lc416')
    sprite('lc600_01', 7)
    sprite('lc600_02', 7)
    sprite('lc600_03', 7)
    Voiceline('lc417')
    sprite('lc600_04', 6)
    sprite('lc600_05', 6)
    sprite('lc600_06', 6)
    sprite('lc600_07', 8)
    sprite('lc600_08', 7)
    sprite('lc600_09', 7)
    sprite('lc600_10', 5)
    CreateObject('RodEntry600', -1)
    CommonSE('200_walk_normal_1')
    sprite('lc600_11', 5)
    sprite('lc600_12', 5)
    sprite('lc600_13', 5)
    sprite('lc600_14', 5)
    sprite('lc600_15', 5)
    ObjectUpon2(11, 10, 0)
    sprite('lc600_16', 5)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(2)
    sprite('lc601_00', 6)
    ObjectUpon2(11, 11, 0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2)
    sprite('lc601_00', 155)
    Voiceline('lc414')
    sprite('lc601_01', 6)
    sprite('lc601_02', 6)
    sprite('lc601_03', 6)
    sprite('lc601_04', 6)
    sprite('lc601_05', 6)
    sprite('lc601_06', 6)
    sprite('lc601_07', 6)
    Voiceline('lc415')
    CommonSE('019_cloth_c')
    sprite('lc601_08', 6)
    sprite('lc601_09', 6)
    sprite('lc601_10', 6)
    ObjectUpon2(11, 10, 0)
    sprite('lc601_11', 6)
    sprite('lc601_12', 6)
    sprite('lc601_13', 6)
    sprite('lc601_14', 6)
    sprite('lc601_15', 6)
    sprite('lc601_16', 6)
    sprite('lc601_17', 6)
    sprite('lc601_18', 6)
    sprite('lc601_19', 3)
    sprite('lc601_20', 6)
    sprite('lc601_21', 6)
    CommonSE('200_walk_normal_1')
    if SLOT_43:
        DemoTimer(70)
    else:
        DemoTimer(60)
    loopRest()
    ExitState()
    label(140)
    sprite('lc000_00', 7)
    uponSendToLabel(32, 141)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(140)
    label(141)
    sprite('lc300_00', 5)
    sprite('lc300_01', 5)
    Voiceline('lc508')
    sprite('lc300_02', 5)
    sprite('lc300_03', 5)
    sprite('lc300_04', 5)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 5)
    sprite('lc300_06', 5)
    sprite('lc300_07', 60)
    sprite('lc300_08', 5)
    sprite('lc300_09', 5)
    sprite('lc300_10', 5)
    sprite('lc300_11', 5)
    sprite('lc300_12', 5)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    ObjectUpon(22, 32)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    DemoTimer(20)
    loopRest()
    ExitState()
    label(150)
    uponSendToLabel(32, 152)
    label(151)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(151)
    label(152)
    clearUponHandler(32)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 180)
    Voiceline('lc510')
    DemoTimer(300)
    sprite('lc630_06', 4)
    sprite('lc630_05', 4)
    sprite('lc630_04', 4)
    sprite('lc630_03', 4)
    sprite('lc630_02', 4)
    sprite('lc630_01', 4)
    sprite('lc630_00', 4)
    loopRest()
    ExitState()
    label(170)
    sprite('lc630_07', 1)
    XPositionRelativeFacing(-120000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(170)
    sprite('lc630_07', 30)
    sprite('lc630_07', 120)
    Voiceline('lc514')
    DemoEndOnVoiceEnd(1)
    sprite('lc630_06', 6)
    sprite('lc630_05', 6)
    sprite('lc630_04', 6)
    sprite('lc630_03', 6)
    sprite('lc630_02', 6)
    sprite('lc630_01', 6)
    sprite('lc630_00', 6)
    ObjectUpon(22, 32)
    label(171)
    sprite('lc000_00', 7)
    uponSendToLabel(32, 172)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('lc033_00', 1)
    sprite('lc033_00', 2)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    uponSendToLabel(LANDING, 174)
    sprite('lc033_01', 2)
    sprite('lc033_02', 3)
    setGravity(1600)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    label(173)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    gotoLabel(173)
    label(174)
    sprite('lc033_04', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    clearUponHandler(LANDING)
    sprite('lc033_05', 3)
    loopRest()
    ExitState()
    label(180)
    uponSendToLabel(32, 182)
    label(181)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(181)
    label(182)
    clearUponHandler(32)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 180)
    Voiceline('lc516')
    DemoTimer(220)
    sprite('lc630_06', 4)
    sprite('lc630_05', 4)
    sprite('lc630_04', 4)
    sprite('lc630_03', 4)
    sprite('lc630_02', 4)
    sprite('lc630_01', 4)
    sprite('lc630_00', 4)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    uponSendToLabel(32, 332)
    label(331)
    sprite('lc000_00', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('lc300_00', 7)
    Voiceline('lc546')
    sprite('lc300_01', 7)
    sprite('lc300_02', 7)
    sprite('lc300_03', 7)
    sprite('lc300_04', 7)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 7)
    sprite('lc300_06', 7)
    sprite('lc300_07', 360)
    sprite('lc300_08', 7)
    sprite('lc300_09', 7)
    sprite('lc300_10', 7)
    sprite('lc300_11', 7)
    sprite('lc300_12', 7)
    DemoTimer(40)
    loopRest()
    ExitState()
    label(2330)
    sprite('null', 1)
    uponSendToLabel(32, 2332)
    label(2331)
    sprite('lc000_00', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(2331)
    label(2332)
    sprite('lc630_00', 6)
    sprite('lc630_01', 6)
    sprite('lc630_02', 6)
    sprite('lc630_03', 6)
    sprite('lc630_04', 6)
    sprite('lc630_05', 6)
    Voiceline('lc546')
    sprite('lc630_06', 6)
    sprite('lc630_07', 120)
    sprite('lc630_06', 6)
    sprite('lc630_05', 6)
    sprite('lc630_04', 6)
    sprite('lc630_03', 6)
    sprite('lc630_02', 6)
    sprite('lc630_01', 6)
    sprite('lc630_00', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(340)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(340)
    sprite('lc630_00', 7)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 120)
    Voiceline('lc548')
    sprite('lc630_03', 7)
    ObjectUpon(22, 32)
    sprite('lc630_02', 7)
    sprite('lc630_01', 7)
    sprite('lc630_00', 7)
    loopRest()
    ExitState()
    label(1340)
    sprite('null', 1)
    ObjectUpon2(11, 11, 0)
    AddX(-700000)
    ScreenCollision(0)
    EnableCollision(0)
    label(1341)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1341)
    sprite('null', 10)
    sprite('lc032_00', 3)
    ObjectUpon2(11, 10, 0)
    physicsXImpulse(18000)

    def upon_EVERY_FRAME():
        if SLOT_19 <= 310000:
            clearUponHandler(EVERY_FRAME)
            ObjectUpon(22, 32)
            XPositionRelativeFacing(-50000)
            XImpulseAcceleration(10)
            sendToLabel(1343)
    sprite('lc032_01', 3)
    label(1342)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    sprite('lc032_01', 3)
    loopRest()
    gotoLabel(1342)
    label(1343)
    sprite('lc032_13', 3)
    sprite('lc032_14', 3)
    sprite('lc033_00', 1)
    sprite('lc033_00', 2)
    uponSendToLabel(LANDING, 1345)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    sprite('lc033_01', 2)
    sprite('lc033_02', 3)
    setGravity(850)
    setInvincible(0)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    BeginBuffer('BDash_2nd')
    sprite('lc033_03', 3)
    label(1344)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    gotoLabel(1344)
    label(1345)
    sprite('lc033_04', 4)
    clearUponHandler(LANDING)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    sprite('lc033_05', 3)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    Voiceline('lc548')
    DemoEndOnVoiceEnd(1)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    ObjectUpon(22, 33)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('ar'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('kk'):
        conditionalSendToLabel(100)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(0)
    sprite('lc300_00', 7)
    Voiceline('lc400')
    DemoEndOnVoiceEnd(1)
    sprite('lc300_01', 7)
    sprite('lc300_02', 7)
    sprite('lc300_03', 7)
    sprite('lc300_04', 7)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 7)
    sprite('lc300_06', 7)
    sprite('lc300_07', 32767)
    loopRest()
    label(0)
    sprite('lc300_00', 7)
    Voiceline('lc401')
    DemoEndOnVoiceEnd(1)
    sprite('lc300_01', 7)
    sprite('lc300_02', 7)
    sprite('lc300_03', 7)
    sprite('lc300_04', 7)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 7)
    sprite('lc300_06', 7)
    sprite('lc300_07', 32767)
    loopRest()
    label(100)
    sprite('lc630_00', 7)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 7)
    sprite('lc630_04', 7)
    sprite('lc630_05', 7)
    sprite('lc630_06', 6)
    sprite('lc630_07', 32767)
    if random_(2, 0, 50):
        Voiceline('lc400')
    else:
        Voiceline('lc401')
    DemoEndOnVoiceEnd(1)
    loopRest()


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tk'):
        conditionalSendToLabel(140)
    if CharacterIDCheck('tg'):
        conditionalSendToLabel(150)
    if CharacterIDCheck('ar'):
        conditionalSendToLabel(170)
    if CharacterIDCheck('bn'):
        conditionalSendToLabel(180)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('kk'):
        if SLOT_138:
            gotoLabel(340)
        else:
            gotoLabel(1340)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('lc610_00', 4)
    Voiceline('lc406')
    sprite('lc610_01', 4)
    sprite('lc610_02', 4)
    sprite('lc610_03', 4)
    sprite('lc610_04', 4)
    sprite('lc610_05', 4)
    CommonSE('019_cloth_a')
    sprite('lc610_06', 4)
    CreateObject('EF_PandaWin', 0)
    CommonSE('200_walk_normal_1')
    CommonSE('205_runjump_garden_2')
    sprite('lc610_07', 6)
    sprite('lc610_08', 6)
    sprite('lc610_09', 6)
    DemoTimer(140)
    label(99)
    sprite('lc610_10', 6)
    sprite('lc610_11', 6)
    sprite('lc610_12', 6)
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('lc610_00', 4)
    Voiceline('lc408')
    sprite('lc610_01', 4)
    sprite('lc610_02', 4)
    sprite('lc610_03', 4)
    sprite('lc610_04', 4)
    sprite('lc610_05', 4)
    CommonSE('019_cloth_a')
    sprite('lc610_06', 4)
    CreateObject('EF_PandaWin', 0)
    CommonSE('200_walk_normal_1')
    CommonSE('205_runjump_garden_2')
    sprite('lc610_07', 6)
    sprite('lc610_08', 6)
    sprite('lc610_09', 6)
    DemoTimer(140)
    label(98)
    sprite('lc610_10', 6)
    sprite('lc610_11', 6)
    sprite('lc610_12', 6)
    loopRest()
    gotoLabel(98)
    label(0)
    sprite('lc611_00', 7)
    if SLOT_43:
        DemoTimer(165)
    else:
        DemoTimer(375)
    Voiceline('lc407')
    sprite('lc611_00', 7)
    sprite('lc611_01', 7)
    sprite('lc611_02', 7)
    sprite('lc611_03', 7)
    sprite('lc611_04', 7)
    sprite('lc611_05', 7)
    sprite('lc611_06', 5)
    sprite('lc611_07', 5)
    sprite('lc611_08', 5)
    sprite('lc611_09', 5)
    sprite('lc611_10', 5)
    sprite('lc611_11', 5)
    sprite('lc611_12', 5)
    sprite('lc611_13', 100)
    sprite('lc611_13', 100)
    sprite('lc611_13', 32767)
    loopRest()
    label(140)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc509')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(150)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc511')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(170)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc515')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(180)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc517')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(330)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc547')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(2330)
    sprite('lc630_00', 6)
    sprite('lc630_01', 6)
    sprite('lc630_02', 6)
    sprite('lc630_03', 6)
    sprite('lc630_04', 6)
    sprite('lc630_05', 6)
    sprite('lc630_06', 6)
    sprite('lc630_07', 32767)
    Voiceline('lc547')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(340)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc549')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(1340)
    sprite('lc630_00', 4)
    sprite('lc630_01', 4)
    sprite('lc630_02', 4)
    sprite('lc630_03', 4)
    sprite('lc630_04', 4)
    sprite('lc630_05', 4)
    sprite('lc630_06', 4)
    sprite('lc630_07', 32767)
    Voiceline('lc549')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(666)
    sprite('lc610_00', 4)
    if random_(2, 0, 50):
        Voiceline('lc406')
    else:
        Voiceline('lc408')
    DemoEndOnVoiceEnd(1)
    sprite('lc610_01', 4)
    sprite('lc610_02', 4)
    sprite('lc610_03', 4)
    sprite('lc610_04', 4)
    sprite('lc610_05', 4)
    CommonSE('019_cloth_a')
    sprite('lc610_06', 4)
    CreateObject('EF_PandaWin', 0)
    CommonSE('200_walk_normal_1')
    CommonSE('205_runjump_garden_2')
    sprite('lc610_07', 6)
    sprite('lc610_08', 6)
    sprite('lc610_09', 6)
    label(667)
    sprite('lc610_10', 6)
    sprite('lc610_11', 6)
    sprite('lc610_12', 6)
    loopRest()
    gotoLabel(667)


@State
def CmnActLose():
    sprite('lc620_00', 6)
    Voiceline('lc411')
    StayAfterMovement(1, 0)
    sprite('lc620_01', 6)
    sprite('lc620_02', 6)
    CreateParticle('lcef_tear', 0)
    sprite('lc620_03', 6)
    CreateParticle('lcef_tear', 0)
    sprite('lc620_04', 6)
    CreateParticle('lcef_tear', 0)
    sprite('lc620_05', 6)
    CreateParticle('lcef_tear', 0)
    sprite('lc620_06', 6)
    CreateParticle('lcef_tear', 0)
    sprite('lc620_07', 6)
    CreateParticle('lcef_tear', 0)
    CommonSE('205_runjump_garden_1')
    sprite('lc620_08', 6)
    CreateParticle('lcef_tear', 0)
    DemoTimer(90)
    sprite('lc620_09', 3)
    CreateParticle('lcef_tearfall', 0)
    CreateParticle('lcef_tearfall', 1)
    sprite('lc620_09ex01', 30)
    label(0)
    sprite('lc620_09ex01', 33)
    CreateParticle('lcef_tearfall', 0)
    CreateParticle('lcef_tearfall', 1)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWait():
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
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
    sprite('lc063_11', 32767)
    ObjectUpon2(11, 50, 0)


@State
def EventDefLose2():
    sprite('lc620_09', 32767)
    AddX(260000)
    ObjectUpon2(11, 50, 0)


@State
def EventDefLose3():
    sprite('lc070_03', 32767)
    loopRest()


@State
def EventNoDisp():
    sprite('keep', 32767)
    Visibility(1)
    ObjectUpon2(11, 11, 0)
    loopRest()


@State
def EventEntryWearingCoat():
    sprite('lc601_00', 32767)
    loopRest()


@State
def EventEntryPutOffCoat():
    sprite('lc601_01', 6)
    sprite('lc601_02', 6)
    sprite('lc601_03', 6)
    sprite('lc601_04', 6)
    sprite('lc601_05', 6)
    sprite('lc601_06', 6)
    sprite('lc601_07', 6)
    CommonSE('019_cloth_c')
    sprite('lc601_08', 6)
    sprite('lc601_09', 6)
    sprite('lc601_10', 6)
    sprite('lc601_11', 6)
    sprite('lc601_12', 6)
    sprite('lc601_13', 6)
    sprite('lc601_14', 6)
    sprite('lc601_15', 6)
    sprite('lc601_16', 6)
    sprite('lc601_17', 6)
    sprite('lc601_18', 6)
    sprite('lc601_19', 3)
    sprite('lc601_20', 6)
    sprite('lc601_21', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSTK1():
    sprite('lc000_00', 1)
    XPositionRelativeFacing(-10000)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSTK2():
    sprite('lc351_00', 3)
    physicsXImpulse(-8000)
    physicsYImpulse(18000)
    setGravity(1350)
    CommonSE('019_cloth_a')
    sprite('lc033_07ex00', 4)
    sprite('lc033_08ex00', 4)
    sprite('lc033_09ex00', 4)
    sprite('lc033_10ex00', 4)
    sprite('lc351_01', 4)
    sprite('lc351_02', 4)
    sprite('lc351_03', 3)
    sprite('lc024_00', 4)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc024_01', 4)
    sprite('lc024_02', 4)
    sprite('lc024_03', 4)
    sprite('lc024_04', 4)
    sprite('lc024_05', 4)
    sprite('lc024_06', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSTK3():
    sprite('lc300_00', 7)
    sprite('lc300_01', 7)
    sprite('lc300_02', 7)
    sprite('lc300_03', 7)
    sprite('lc300_04', 7)
    sprite('lc300_05', 7)
    sprite('lc300_06', 7)
    sprite('lc300_07', 7)
    sprite('lc300_06', 32767)


@State
def EventVSRC1():
    sprite('lc000_00', 3)
    Visibility(1)
    ObjectUpon2(11, 11, 0)
    XPositionRelativeFacing(-960000)
    ScreenCollision(0)


@State
def EventVSRC2():
    sprite('lc032_00', 3)
    Visibility(0)
    ScreenCollision(0)
    physicsXImpulse(18000)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    XImpulseAcceleration(80)
    sprite('lc032_13', 3)
    sprite('lc032_14', 3)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSRC3():
    sprite('lc630_00', 7)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 32767)


@State
def EventVSRC4():
    sprite('lc630_03', 7)
    sprite('lc630_02', 7)
    sprite('lc630_01', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventDash():
    sprite('lc032_00', 3)
    ScreenCollision(0)
    Flip()
    physicsXImpulse(18000)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    label(0)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    loopRest()
    gotoLabel(0)


@State
def EventUtsumukiStart():
    sprite('lc630_00', 7)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 7)
    sprite('lc630_04', 7)
    sprite('lc630_05', 7)
    sprite('lc630_06', 7)
    loopRest()
    enterState('EventUtsumuki')


@State
def EventUtsumuki():
    sprite('lc630_07', 32767)


@State
def EventUtsumukiEnd():
    sprite('lc630_07', 7)
    sprite('lc630_05', 7)
    sprite('lc630_04', 7)
    sprite('lc630_03', 7)
    sprite('lc630_02', 7)
    sprite('lc630_01', 7)
    sprite('lc630_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventYorokeStart():
    sprite('lc070_00', 2)
    sprite('lc070_01', 2)
    sprite('lc070_02', 2)
    loopRest()
    enterState('EventYoroke')


@State
def EventYoroke():
    label(0)
    sprite('lc070_03', 4)
    loopRest()
    gotoLabel(0)


@State
def EventYorokeToDown():
    sprite('lc070_05', 5)
    ObjectUpon2(11, 50, 0)
    AddX(60000)
    sprite('lc070_06', 5)
    sprite('lc070_07', 4)
    sprite('lc070_08', 4)
    sprite('lc070_09', 3)
    sprite('lc070_10', 3)
    AddX(40000)
    sprite('lc063_11', 32767)
    loopRest()


@State
def EventBackStep():

    def upon_IMMEDIATE():
        uponSendToLabel(LANDING, 1)
    sprite('lc033_00', 2)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    sprite('lc033_01', 2)
    sprite('lc033_02', 1)
    setGravity(850)
    label(0)
    sprite('lc033_02', 2)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc033_04', 2)
    XImpulseAcceleration(50)
    LandingEffects(100, 1, 1)
    sprite('lc033_04', 1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    sprite('lc033_04', 1)
    sprite('lc033_05', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventLockWait():
    sprite('lc040_02', 32767)


@State
def EventLockReject():
    sprite('lc312_00', 2)
    AddX(150000)
    CreateParticle('ef_offset', 103)
    CommonSE('107_throw_comeout')
    AddX(-150000)
    sprite('lc312_01', 2)
    sprite('lc312_02', 2)
    sprite('lc312_03', 6)
    sprite('lc312_04', 3)
    sprite('lc312_05', 2)
    sprite('lc312_06', 2)
    sprite('lc312_07', 2)
    sprite('lc312_08', 2)
    sprite('lc312_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventTKvsLCEntry():
    sprite('lc000_08', 7)
    XPositionRelativeFacing(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventLCvsARAirRod():
    sprite('keep', 32767)
    AbsoluteY(1000000)
    setGravity(0)
    ObjectUpon2(11, 53, 0)
    loopRest()


@State
def EventLCvsARRodReturn():
    sprite('keep', 1)
    ObjectUpon2(11, 54, 0)
    loopRest()
    enterState('EventUtsumukiEnd')


@State
def EventFallToStand():
    sprite('lc020_05', 3)
    setGravity(1400)
    uponSendToLabel(LANDING, 72)
    sprite('lc020_06', 600)
    label(71)
    sprite('lc020_07', 4)
    sprite('lc020_08', 4)
    loopRest()
    gotoLabel(71)
    label(72)
    clearUponHandler(LANDING)
    sprite('lc024_00', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc024_01', 4)
    sprite('lc024_02', 4)
    sprite('lc024_03', 4)
    sprite('lc024_04', 4)
    sprite('lc024_05', 4)
    sprite('lc024_06', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventCAVsLCEntry():
    sprite('lc070_00', 2)
    sprite('lc070_01', 2)
    sprite('lc070_02', 2)
    sprite('lc070_03', 4)
    sprite('lc070_04', 60)
    sprite('lc070_11', 7)
    sprite('lc070_12', 7)
    sprite('lc070_13', 7)
    sprite('lc070_14', 7)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventCAVsLCLoser():
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('lc033_00', 2)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    sprite('lc033_01', 2)
    sprite('lc033_02', 1)
    setGravity(850)
    sprite('lc033_02', 2)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(LANDING)
    sprite('lc033_04', 2)
    XImpulseAcceleration(50)
    LandingEffects(100, 1, 1)
    sprite('lc033_04', 1)
    physicsXImpulse(0)
    sprite('lc033_04', 1)
    sprite('lc033_05', 3)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDefChouhatsu():
    sprite('lc300_00', 5)
    sprite('lc300_01', 5)
    sprite('lc300_02', 5)
    sprite('lc300_03', 5)
    sprite('lc300_04', 5)
    CommonSE('208_brake_normal')
    sprite('lc300_05', 5)
    sprite('lc300_06', 5)
    sprite('lc300_07', 5)
    sprite('lc300_08', 5)
    sprite('lc300_09', 5)
    sprite('lc300_10', 5)
    sprite('lc300_11', 5)
    sprite('lc300_12', 5)
    enterState('CmnActStand')


@State
def EventWin1Start():
    sprite('lc615_06', 32767)


@State
def EventWin1End():
    sprite('lc615_06', 6)
    sprite('lc615_03', 6)
    sprite('lc615_02', 6)
    sprite('lc615_01', 6)
    sprite('lc615_00', 6)
    enterState('CmnActStand')


@State
def EventBackStep2():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 10)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('lc033_00', 2)
    physicsXImpulse(-15000)
    physicsYImpulse(2400)
    setInvincible(1)
    sprite('lc033_01', 2)
    sprite('lc033_02', 1)
    setGravity(850)
    uponSendToLabel(LANDING, 1)
    label(0)
    sprite('lc033_02', 2)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(LANDING)
    sprite('lc033_04', 2)
    XImpulseAcceleration(50)
    LandingEffects(100, 1, 1)
    sprite('lc033_04', 1)
    physicsXImpulse(0)
    sprite('lc033_04', 1)
    sprite('lc033_05', 3)
    setInvincible(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalk():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('lc030_00', 6)
    physicsXImpulse(4650)
    label(0)
    sprite('lc030_01', 6)
    sprite('lc030_02', 6)
    sprite('lc030_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_04', 6)
    sprite('lc030_05', 6)
    sprite('lc030_06', 6)
    sprite('lc030_07', 6)
    sprite('lc030_08', 6)
    sprite('lc030_09', 6)
    sprite('lc030_10', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_11', 6)
    sprite('lc030_12', 6)
    sprite('lc030_13', 6)
    sprite('lc030_14', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventKamae1Start():
    sprite('lc420_00', 3)
    sprite('lc420_01', 3)
    sprite('lc420_01', 3)
    sprite('lc420_02', 3)
    sprite('lc420_05', 6)
    sprite('lc420_06', 5)
    sprite('lc420_07', 4)
    LandingEffects(100, 1, 1)
    sprite('lc420_08', 7)
    sprite('lc420_09', 7)
    sprite('lc420_10', 7)
    sprite('lc420_11', 7)
    sprite('lc420_12', 32767)
    loopRest()


@State
def EventKamae1End():
    sprite('lc420_13', 7)
    sprite('lc420_14', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)
        ObjectUpon2(11, 11, 0)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Entry1():
    sprite('lc601_00', 1)
    ObjectUpon2(11, 11, 0)
    sprite('lc601_00', 32767)
    loopRest()


@State
def Act2Event_Entry1End():
    sprite('keep', 2)
    ObjectUpon2(11, 11, 0)
    sprite('lc601_01', 6)
    sprite('lc601_02', 6)
    sprite('lc601_03', 6)
    sprite('lc601_04', 6)
    sprite('lc601_05', 6)
    sprite('lc601_06', 6)
    sprite('lc601_07', 6)
    CommonSE('019_cloth_c')
    sprite('lc601_08', 6)
    sprite('lc601_09', 6)
    sprite('lc601_10', 6)
    ObjectUpon2(11, 10, 0)
    sprite('lc601_11', 6)
    sprite('lc601_12', 6)
    sprite('lc601_13', 6)
    sprite('lc601_14', 6)
    sprite('lc601_15', 6)
    sprite('lc601_16', 6)
    sprite('lc601_17', 6)
    sprite('lc601_18', 6)
    sprite('lc601_19', 3)
    sprite('lc601_20', 6)
    sprite('lc601_21', 6)
    CommonSE('200_walk_normal_1')
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Smile():
    sprite('lc300_00', 7)
    sprite('lc300_01', 7)
    sprite('lc300_02', 7)
    sprite('lc300_03', 7)
    sprite('lc300_04', 7)
    sprite('lc300_05', 7)
    sprite('lc300_06', 7)
    sprite('lc300_07', 7)
    sprite('lc300_06', 32767)
    loopRest()


@State
def Act2Event_Sad():
    sprite('lc630_07', 32767)
    loopRest()


@State
def Act2Event_ToSad():
    sprite('lc630_00', 6)
    sprite('lc630_01', 6)
    sprite('lc630_02', 6)
    sprite('lc630_03', 6)
    sprite('lc630_04', 6)
    sprite('lc630_05', 6)
    sprite('lc630_06', 6)
    sprite('lc630_07', 32767)
    loopRest()


@State
def Act2Event_SadEnd():
    sprite('lc630_06', 6)
    sprite('lc630_05', 6)
    sprite('lc630_04', 6)
    sprite('lc630_03', 6)
    sprite('lc630_02', 6)
    sprite('lc630_01', 6)
    sprite('lc630_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Odoroki():
    sprite('lc630_00', 5)
    sprite('lc630_01', 5)
    sprite('lc630_02', 5)
    sprite('lc630_03', 20)
    sprite('lc630_03', 6)
    sprite('lc630_02', 6)
    sprite('lc630_01', 6)
    sprite('lc630_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_YorokeStart():
    sprite('lc070_00', 2)
    sprite('lc070_01', 2)
    sprite('lc070_02', 2)
    loopRest()
    enterState('Act2Event_Yoroke')


@State
def Act2Event_Yoroke():
    sprite('lc070_04', 32767)
    loopRest()


@State
def Act2Event_YorokeEnd():
    sprite('lc070_11', 5)
    sprite('lc070_12', 5)
    sprite('lc070_13', 5)
    sprite('lc070_14', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_YorokeToDown():
    sprite('lc070_05', 5)
    ObjectUpon2(11, 50, 0)
    AddX(60000)
    sprite('lc070_06', 5)
    sprite('lc070_07', 4)
    sprite('lc070_08', 4)
    sprite('lc070_09', 3)
    sprite('lc070_10', 3)
    AddX(40000)
    sprite('lc063_11', 32767)
    KnockdownEffects(100, 0, 1)
    loopRest()


@State
def Act2Event_YorokeToDownEnd():
    sprite('lc064_00', 4)
    sprite('lc064_01', 4)
    sprite('lc064_02', 4)
    sprite('lc064_03', 4)
    sprite('lc064_04', 4)
    sprite('lc064_05', 4)
    CommonSE('019_cloth_a')
    ObjectUpon2(11, 10, 0)
    sprite('lc064_06', 4)
    sprite('lc064_07', 4)
    sprite('lc064_08', 4)
    sprite('lc064_09', 4)
    sprite('lc064_10', 4)
    sprite('lc064_11', 4)
    sprite('lc064_12', 4)
    sprite('lc064_13', 4)
    sprite('lc064_14', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_lcvsrl_00():

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 3:
            if SLOT_52 % 2:
                AddX(1000)
            else:
                AddX(-1000)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1

    def upon_STATE_END():
        clearUponHandler(EVERY_FRAME)
        XPositionRelativeFacing(-260000)
    sprite('lc050_00', 4)
    sprite('lc050_01', 8)
    sprite('lc050_00', 4)
    sprite('lc630_00', 7)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 7)
    sprite('lc630_04', 7)
    sprite('lc630_05', 7)
    sprite('lc630_06', 7)
    sprite('lc630_07', 32767)
    loopRest()


@State
def Act2Event_UtsumukiEnd():
    sprite('lc630_07', 7)
    sprite('lc630_05', 7)
    sprite('lc630_04', 7)
    sprite('lc630_03', 7)
    sprite('lc630_02', 7)
    sprite('lc630_01', 7)
    sprite('lc630_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_YureMotion():
    sprite('lc630_00', 7)
    CreateObject('Act2Event_Yure', -1)
    sprite('lc630_01', 7)
    sprite('lc630_02', 7)
    sprite('lc630_03', 32767)
    loopRest()


@State
def Act3Event_novslc_00():

    def upon_IMMEDIATE():
        Visibility(1)
        XPositionRelativeFacing(-1865000)
        ScreenCollision(0)
        ObjectUpon2(11, 58, 0)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 22)
    sprite('null', 2)
    ObjectUpon(22, 32)
    loopRest()


@State
def Act3Event_novslc_01():

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
    sprite('lc032_00', 3)
    physicsXImpulse(24000)
    label(9)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('lc032_13', 6)
    physicsXImpulse(0)
    SetInertia(10000)
    ObjectUpon2(11, 0, 0)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    sprite('lc032_14', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_novslc_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('lc000_00', 7)
    sprite('lc070_00', 17)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    ScreenShake(1000, 20000)
    ObjectUpon2(11, 59, 0)
    sprite('lc070_00', 4)
    AddInertia(-11000)
    sprite('lc070_01', 4)
    sprite('lc070_02', 4)
    sprite('lc070_03', 32767)
    loopRest()


@State
def Act3Event_novslc_03():
    sprite('lc070_05', 5)
    sprite('lc070_06', 5)
    sprite('lc070_07', 5)
    sprite('lc070_08', 5)
    sprite('lc070_09', 5)
    sprite('lc070_10', 5)
    sprite('lc063_11', 32767)
    CommonSE('209_down_normal_0')
    AddX(100000)
    loopRest()


@State
def Act3Event_tkvslc_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        NoAttackDuringAction(1)
        uponSendToLabel(32, 0)
    label(9)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('lc201_00', 3)
    ObjectUpon2(11, 36, 0)
    ObjectHitbox(11)
    ObjectUpon(22, 32)
    sprite('lc201_01', 3)
    sprite('lc201_02', 3)
    sprite('lc201_03', 3)
    sprite('lc201_04', 3)
    sprite('lc201_05', 3)
    sprite('lc201_06', 5)
    sprite('lc201_07', 5)
    sprite('lc201_08', 4)
    sprite('lc201_09', 4)
    sprite('lc201_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tkvslc_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('lc000_00', 5)
    sprite('lc070_00', 10)
    CommonSE('100_hit_grap_0')
    ScreenShake(1000, 20000)
    ObjectUpon2(11, 59, 0)
    sprite('lc070_00', 4)
    AddInertia(-11000)
    sprite('lc070_01', 4)
    sprite('lc070_02', 4)
    sprite('lc070_03', 32767)
    loopRest()


@State
def Act3Event_tkvslc_02():
    sprite('lc070_11', 5)
    ObjectUpon2(11, 0, 0)
    sprite('lc070_12', 5)
    sprite('lc070_13', 5)
    sprite('lc070_14', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tkvslc_03():

    def upon_IMMEDIATE():
        ScreenCollision(0)
    sprite('lc003_00', 4)
    Flip()
    sprite('lc003_01', 4)
    sprite('lc003_02', 4)
    sprite('lc032_00', 3)
    physicsXImpulse(12000)
    SetAcceleration(1000)
    SetActionMark(2)
    label(9)
    sprite('lc032_01', 3)
    AddActionMark(-1)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(9)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_DashIn():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-1200000)
        ScreenCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 360000:
                    sendToLabel(0)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage > -360000:
                sendToLabel(0)
                clearUponHandler(EVERY_FRAME)
    sprite('lc032_00', 3)
    physicsXImpulse(21000)
    label(9)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('lc032_13', 6)
    physicsXImpulse(0)
    SetInertia(10000)
    sprite('lc032_14', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_EntryWait():
    sprite('keep', 32767)
    Visibility(1)
    XPositionRelativeFacing(-900000)
    ScreenCollision(0)
    ObjectUpon2(11, 11, 0)
    loopRest()


@State
def Act3Event_WalkIn():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-700000)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    sendToLabel(1)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                sendToLabel(1)
    sprite('lc030_00', 6)
    physicsXImpulse(4650)
    label(0)
    sprite('lc030_01', 6)
    sprite('lc030_02', 6)
    sprite('lc030_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_04', 6)
    sprite('lc030_05', 6)
    sprite('lc030_06', 6)
    sprite('lc030_07', 6)
    sprite('lc030_08', 6)
    sprite('lc030_09', 6)
    sprite('lc030_10', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_11', 6)
    sprite('lc030_12', 6)
    sprite('lc030_13', 6)
    sprite('lc030_14', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    EndMomentum(1)
    clearUponHandler(EVERY_FRAME)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act3Event_lcvsrl_00():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        NoDamageAction(1)
        AddX(60000)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc040_02', 3)
    sprite('lc090_00', 14)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('lc090_01', 6)
    AddInertia(-8000)
    sprite('lc090_02', 14)
    sprite('lc090_03', 7)
    sprite('lc090_04', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_lcvskk_00():
    sprite('keep', 1)
    sprite('lc003_00', 6)
    Flip()
    sprite('lc003_01', 6)
    sprite('lc003_02', 6)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_lcvskk_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
    sprite('lc030_00', 6)
    physicsXImpulse(4650)
    sprite('lc030_01', 6)
    sprite('lc030_02', 6)
    sprite('lc030_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_04', 6)
    sprite('lc030_05', 6)
    sprite('lc030_06', 6)
    sprite('lc030_07', 6)
    sprite('lc030_08', 6)
    sprite('lc030_09', 6)
    sprite('lc030_10', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('lc030_11', 6)
    sprite('lc030_12', 6)
    sprite('lc030_13', 6)
    sprite('lc030_14', 6)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    CameraControlEnable(1)
    EndMomentum(1)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    label(0)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_lcvskk_02():
    sprite('lc434_48', 2)
    sprite('lc434_49', 2)
    sprite('lc434_50', 2)
    sprite('lc434_51', 2)
    sprite('lc434_52', 2)
    sprite('lc434_53', 2)
    sprite('lc434_54', 2)
    sprite('lc434_55', 2)
    sprite('lc434_56', 3)
    ObjectUpon2(11, 11, 0)
    CommonSE('003_swing_grap_0_2')
    sprite('lc434_57', 3)
    CommonSE('005_swing_grap_2_1')
    sprite('lc434_58', 3)
    sprite('lc434_59', 3)
    sprite('lc434_60', 3)
    sprite('lc434_61', 3)
    sprite('lc434_30', 4)
    sprite('lc434_31', 4)
    SetXCollisionFromOrigin(300)
    sprite('lc434_32', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(320)
    sprite('lc434_33', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(340)
    sprite('lc434_34', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(360)
    sprite('lc434_35', 4)
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(380)
    sprite('lc434_36', 4)
    CommonSE('008_swing_pole_2')
    CommonSE('008_swing_pole_1')
    CommonSE('006_swing_blade_2')
    SetXCollisionFromOrigin(400)
    sprite('lc434_37', 4)
    sprite('lc434_38', 4)
    sprite('lc434_39', 6)
    sprite('lc434_40', 6)
    sprite('lc434_41', 6)
    sprite('lc434_42', 32767)
    loopRest()


@State
def Act3Event_lcvskk_03():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 11, 0)
    sprite('lc434_43', 6)
    sprite('lc434_44', 6)
    sprite('lc434_45', 6)
    sprite('lc434_46', 6)
    sprite('lc434_47', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_lcvsar_00():

    def upon_IMMEDIATE():
        NoDamageAction(1)
    sprite('lc202_01', 2)
    sprite('lc202_02', 2)
    sprite('lc202_03', 2)
    AddX(50000)
    sprite('lc202_04', 2)
    AddX(50000)
    CreateObject('LcefKikouCharge', 0)
    sprite('lc202_05', 2)
    sprite('lc202_06', 2)
    sprite('lc202_07', 2)
    sprite('lc202_09', 15)
    ObjectUpon(22, 32)
    CommonSE('004_swing_grap_1_2')
    CommonSE('016_explode_0')
    CreateObject('LcefKikouPtc', 0)
    CreateObject('LcefKikouWave', 0)
    CreateParticle('lcef_202airwall01', 1)
    sprite('lc202_10', 3)
    sprite('lc202_11', 3)
    sprite('lc202_13', 3)
    sprite('lc202_14', 3)
    AddX(-25000)
    sprite('lc202_15', 3)
    AddX(-25000)
    sprite('lc202_16', 3)
    AddX(-25000)
    sprite('lc202_17', 3)
    AddX(-25000)
    sprite('lc202_18', 3)
    sprite('lc202_19', 3)
    sprite('lc202_20', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_lcvsar_01():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        EnableCollision(0)

        def upon_32():
            Visibility(1)
            ObjectUpon2(11, 11, 0)
    sprite('keep', 6)
    sprite('lc419_00', 3)
    sprite('lc419_01', 2)
    AltKnockdownEffects(100, 1, 0)
    sprite('lc419_02', 3)
    CreateObject('419smoke', -1)
    AddX(30000)
    physicsXImpulse(30000)
    sprite('lc419_03', 3)
    sprite('lc419_04', 3)
    XImpulseAcceleration(50)
    CommonSE('004_swing_grap_1_2')
    CommonSE('003_swing_grap_0_2')
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_b')
    CommonSE('016_explode_0')
    sprite('lc419_05', 2)
    CreateObject('419atkeff', -1)
    XImpulseAcceleration(50)
    sprite('lc419_05', 2)
    XImpulseAcceleration(0)
    TriggerUponForState('419smoke', 32)
    sprite('lc419_06', 3)
    sprite('lc419_07', 4)
    sprite('lc419_08', 4)
    sprite('lc419_09', 4)
    sprite('lc419_10', 4)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_bnvslc_00():

    def upon_IMMEDIATE():
        Visibility(1)
        XPositionRelativeFacing(-1865000)
        ScreenCollision(0)
        ObjectUpon2(11, 58, 0)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 22)
    sprite('null', 2)
    ObjectUpon(22, 32)
    loopRest()


@State
def Act3Event_bnvslc_01():

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
    sprite('lc032_00', 3)
    physicsXImpulse(24000)
    label(9)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('lc032_13', 6)
    physicsXImpulse(0)
    SetInertia(10000)
    ObjectUpon2(11, 0, 0)
    CommonSE('011_spin_2')
    CommonSE('011_spin_1')
    CommonSE('011_spin_0')
    sprite('lc032_14', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_bnvslc_02():
    sprite('lc070_04', 32767)
    ObjectUpon2(11, 50, 0)
    loopRest()


@State
def Act3Event_bnvslc_03():
    sprite('lc070_05', 5)
    sprite('lc070_06', 5)
    sprite('lc070_07', 4)
    sprite('lc070_08', 4)
    sprite('lc070_09', 3)
    sprite('lc070_10', 3)
    sprite('lc063_11', 32767)
    AddX(120000)
    KnockdownEffects(100, 0, 1)
    loopRest()


@State
def Act3Event_CAvsLC01():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        XPositionRelativeFacing(-160000)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc092_00', 10)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('104_guard_grap_1')
    CommonSE('106_guard_crush')
    ScreenShake(3000, 18000)
    sprite('lc092_00', 2)
    uponSendToLabel(LANDING, 2)
    physicsXImpulse(-8000)
    physicsYImpulse(15000)
    setGravity(1200)
    sprite('lc092_01', 2)
    sprite('lc092_02', 20)
    sprite('lc092_03', 6)
    sprite('lc092_04', 32767)
    loopRest()
    label(2)
    sprite('lc024_00', 6)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('lc024_01', 6)
    sprite('lc010_02', 6)
    sprite('lc010_03', 6)
    sprite('lc010_04', 6)
    sprite('lc010_05', 6)
    sprite('lc010_06', 6)
    sprite('lc010_05', 6)
    sprite('lc010_04', 6)
    sprite('lc010_01', 6)
    sprite('lc010_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_CAvsLC02():
    sprite('lc630_00', 6)
    ObjectUpon(22, 33)
    sprite('lc630_01', 6)
    sprite('lc630_02', 6)
    sprite('lc630_03', 6)
    sprite('lc630_04', 6)
    sprite('lc630_05', 6)
    sprite('lc630_06', 6)
    sprite('lc630_07', 32767)
    loopRest()


@State
def Act3Event_mavslc_00():

    def upon_IMMEDIATE():
        Flip()
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavslc_01():
    sprite('keep', 1)
    sprite('lc003_00', 6)
    Flip()
    sprite('lc003_01', 6)
    sprite('lc003_02', 6)
    label(0)
    sprite('lc000_00', 7)
    sprite('lc000_01', 7)
    sprite('lc000_02', 7)
    sprite('lc000_03', 7)
    sprite('lc000_04', 7)
    sprite('lc000_05', 7)
    sprite('lc000_06', 7)
    sprite('lc000_07', 7)
    sprite('lc000_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavslc_02():
    sprite('lc300_06', 2)
    ObjectUpon(22, 32)
    sprite('lc300_06', 32767)
    loopRest()


@State
def Act3Event_mavslc_03():
    sprite('lc300_07', 7)
    sprite('lc300_08', 7)
    sprite('lc300_09', 7)
    sprite('lc300_10', 7)
    sprite('lc300_11', 7)
    sprite('lc300_12', 7)
    loopRest()
    enterState('CmnActStand')
