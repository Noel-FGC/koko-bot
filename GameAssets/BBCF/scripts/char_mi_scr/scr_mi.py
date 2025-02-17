@Subroutine
def PreInit():
    CharacterID('mi')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    BlendMode_Normal()
    Health(10500)
    WalkFSpeed(6200)
    WalkBSpeed(4800)
    DashFInitialVelocity(9800)
    DashFAccel(660)
    Gravity(1350)
    DoubleJumpCount(0)
    AirDashFSpeed(28000)
    AirFDashDuration(23)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    ResourceGauge(0, 0, 0, 1, 240, 240, -65536, -65536)
    ResourceGauge(2, 0, 0, 1, 150, 0, -65536, -65536)
    ResourceGauge(3, 0, 0, 1, 10000, 10000, -65536, -65536)
    CPUJumpPriority(100)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('SoshiteTokiwaUgokidasu', 0x602)
    Move_Condition(0x3007)
    Move_Condition(0x300c)
    Move_EndRegister()
    Move_Register('Flying_Start', 0x1)
    Move_Condition(0x2001)
    Move_Input_(0xd9)
    Move_Condition(0x3008)
    Move_Condition(0x302e)
    Move_Condition(0x3036)
    CallSkillConditions('CheckFlying')
    SkillEstimateRange(-150000, 450000, -150000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('Flying_Start2', 0x1)
    StateCall('Flying_Start')
    Move_Condition(0x2001)
    Move_Input_(0xd9)
    Move_Condition(0x3008)
    Move_Condition(0x302e)
    FollowupOnly(1)
    CallSkillConditions('CheckFlying')
    Unknown15027(5000)
    SkillEstimateRange(-150000, 450000, -50000, 300000, 1000, 100)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(1)
    DamageStunPriority(500)
    SkillEstimateRange(0, 250000, -50000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(1500)
    DamageStunPriority(2000)
    SkillEstimateRange(-100000, 250000, 50000, 350000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(1)
    DamageStunPriority(500)
    SkillEstimateRange(0, 300000, -100000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 400000, -50000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMaxChainRepeat(2)
    MoveMid()
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -400000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    AirborneOpponentPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(0, 400000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 500000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5CC', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300b)
    Move_Condition(0x303e)
    SkillEstimateRange(0, 650000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(2000)
    Unknown15027(3000)
    SkillEstimateRange(0, 250000, -200000, 250000, 250, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk6CC', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300b)
    Move_Condition(0x303e)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    SkillEstimateRange(0, 450000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2CC', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300b)
    Move_Condition(0x303e)
    SkillEstimateRange(0, 600000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveMaxChainRepeat(2)
    MoveLow()
    AirborneOpponentPriority(1)
    SkillEstimateRange(0, 500000, -100000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', 0x1)
    MoveMaxChainRepeat(2)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x300b)
    CallSkillConditions('Check5D')
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    SkillEstimateRange(800000, 1500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5D_Open', 0x1)
    StateCall('NmlAtk5D')
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3003)
    CallSkillConditions('Check5D')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5D_Chain', 0x1)
    StateCall('NmlAtk5D')
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3003)
    CallSkillConditions('Check5D')
    CallFunction('Request5D')
    FollowupOnly(1)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    MoveMaxChainRepeat(2)
    Move_Condition(0x300b)
    CallSkillConditions('Check5D')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5D_Open', 0x1)
    StateCall('NmlAtkAIR5D')
    Move_Condition(0x2001)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3003)
    CallSkillConditions('Check5D')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5D_Chain', 0x1)
    StateCall('NmlAtkAIR5D')
    Move_Condition(0x2001)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3003)
    CallSkillConditions('Check5D')
    CallFunction('RequestAIR5D')
    FollowupOnly(1)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk6D', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func6D')
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('NmlAtk4D', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x5f)
    Move_Input_(0x3f)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func4D')
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk4D_OD', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func4D')
    Move_Condition(0x3081)
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('NmlAtk1D', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x37)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func1D')
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('NmlAtk2D', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x44)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func2D')
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('NmlAtk3D', 0x1)
    IndependentInput(1, 0, 0)
    Move_Input_(0x51)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x303e)
    CallSkillConditions('CheckFunnel')
    CallFunction('Func3D')
    AddChain(1)
    DamageStunPriority(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(-100000, 300000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(-100000, 400000, -150000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SkillEstimateRange(-100000, 450000, -350000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    SkillEstimateRange(0, 450000, -300000, 200000, 2000, 50)
    Move_Condition(0x300b)
    Move_Condition(0x303e)
    MoveButtonHoldTime(2, 28, 30)
    SkillEstimateRange(-180000, 180000, -350000, 200000, 1000, 10)
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
    SkillEstimateRange(-100000, 350000, -100000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(1)
    GuardStunPriority(500)
    SkillEstimateRange(0, 500000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('AssaultLow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 500000, -500000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('ShockWave', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('ShotLaser', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x300b)
    CallSkillConditions('Check5D')
    OpponentAttackPriority(1)
    DamageStunPriority(40000)
    SkillEstimateRange(700000, 1200000, -800000, 800000, 25, 1)
    Move_EndRegister()
    Move_Register('ShotLaser_Open', INPUT_SPECIALMOVE)
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckFunnel')
    CallFunction('FuncLaser')
    AddChain(1)
    OpponentAttackPriority(1)
    DamageStunPriority(40000)
    SkillEstimateRange(700000, 1200000, -800000, 800000, 25, 1)
    Move_EndRegister()
    Move_Register('ShotSaws', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x300b)
    CallSkillConditions('Check5D')
    OpponentAttackPriority(1)
    DamageStunPriority(10000)
    GuardStunPriority(40000)
    SkillEstimateRange(400000, 900000, -200000, 300000, 25, 1)
    Move_EndRegister()
    Move_Register('ShotSaws_Open', INPUT_SPECIALMOVE)
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckFunnel')
    CallFunction('FuncSaws')
    AddChain(1)
    OpponentAttackPriority(1)
    DamageStunPriority(10000)
    GuardStunPriority(40000)
    SkillEstimateRange(400000, 900000, -200000, 300000, 25, 1)
    Move_EndRegister()
    Move_Register('SpecialShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300c)
    MoveButtonHoldTime(2, 20, 60)
    OpponentAttackPriority(1)
    DamageStunPriority(2000)
    GuardStunPriority(1)
    SkillEstimateRange(500000, 1500000, -800000, -200000, 500, 10)
    Move_EndRegister()
    Move_Register('DrainThrow', INPUT_SPECIALMOVE)
    NeutralOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_C)
    MoveThrow()
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 225000, -200000, 200000, 2000, 0)
    Move_EndRegister()
    Move_Register('Barrier_On', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x300a)
    TempPriorityMultiplierInterval(3, 400, 500, 0, 1000)
    OpponentAttackPriority(1)
    DamageStunPriority(3000)
    GuardStunPriority(1)
    SkillEstimateRange(350000, 1000000, -200000, 200000, 100, 10)
    Move_EndRegister()
    Move_Register('Barrier_Off', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3002)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(-250000, 250000, -200000, 250000, 500, 10)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_B)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(-100000, 300000, -150000, 150000, 150, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(3500)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 350000, -200000, 200000, 750, 10)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    OpponentAttackPriority(3500)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 350000, -200000, 200000, 750, 10)
    Move_EndRegister()
    Move_Register('UltimateTimeStopThrow', INPUT_DISTORTION)
    NeutralOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300f)
    MoveThrow()
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 250000, -200000, 200000, 2500, 0)
    Move_EndRegister()
    Move_Register('UltimateTimeStopThrow_OD', INPUT_DISTORTION)
    NeutralOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x300f)
    Move_Condition(0x3081)
    MoveThrow()
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 250000, -200000, 200000, 2500, 0)
    Move_EndRegister()
    Move_Register('UltimateTimeStopThrow_SP', INPUT_DISTORTION)
    NeutralOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3007)
    MoveThrow()
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 250000, -200000, 200000, 2500, 0)
    Move_EndRegister()
    Move_Register('UltimateTimeStop', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2003)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(1000000, 1500000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('UltimateTimeStop_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2003)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3081)
    DamageStunPriority(4000)
    GuardStunPriority(4000)
    SkillEstimateRange(1000000, 1500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(0xf7)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(-250000, 250000, -200000, 800000, 500, 10)
    Move_EndRegister()
    Move_Register('BurstDD_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    Move_Input_(INPUT_HOLD_B)
    Move_Input_(INPUT_HOLD_C)
    Move_Input_(INPUT_HOLD_D)
    Move_Condition(0x3081)
    CallSkillConditions('Func_BurstDD_Easy')
    OpponentAttackPriority(4000)
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
    OpponentAttackPriority(4000)
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
    OpponentAttackPriority(4000)
    GuardStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk6A', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'AN_NmlAtk5CC', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('AN_NmlAtk5CC', 'Assault', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'AN_NmlAtk2CC', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'ShockWave', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'AirAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'Flying_Start', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'Flying_Start2', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'ShockWave', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'AN_NmlAtk6CC', 10000000)
    TempPriorityMultiplier('AN_NmlAtk6CC', 'ShockWave', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirAssault', 10000000)
    TempPriorityMultiplier('AirAssault', 'Flying_Start', 10000000)
    TempPriorityMultiplier('AirAssault', 'Flying_Start2', 10000000)
    StylishModeSpecialButton('ShockWave', 0x4, 0xea)
    StylishModeSpecialButton('Assault', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('SpecialShot', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'FJump', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk2C', 8, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 13, 0)
    StylishModeCancels('NmlAtk5C', 'ShockWave', 0, 0)
    StylishModeCancels('NmlAtk5C', 'AN_NmlAtk5CC', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 6, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 8, 0)
    StylishModeCancels('AN_NmlAtk5CC', 'ShockWave', 0, 0)
    StylishModeCancels('AN_NmlAtk5CC', 'Assault', 6, 0)
    StylishModeCancels('NmlAtk6A', 'AirAssault', 0, 0)
    StylishModeCancels('NmlAtk6A', 'Flying_Start2', 0, 0)
    StylishModeCancels('NmlAtk6B', 'ShockWave', 0, 0)
    StylishModeCancels('NmlAtk6B', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk6B', 'UltimateAssault_OD', 7, 0)
    StylishModeCancels('NmlAtk6C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk6C', 'AssaultLow', 2, 0)
    StylishModeCancels('NmlAtk6C', 'ShockWave', 13, 0)
    StylishModeCancels('ThrowExe', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 1, 300000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'AN_NmlAtk2CC', 8, 0)
    StylishModeCancels('AN_NmlAtk2CC', 'AssaultLow', 6, 0)
    StylishModeCancels('AN_NmlAtk2CC', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'FJump', 0, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault', 5, 50)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault_OD', 5, 50)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'Flying_Start', 0, 0)
    HitSprites(0, 'mi062_01')
    HitSprites(1, 'mi062_03')
    HitSprites(2, 'mi062_04')
    HitSprites(3, 'mi062_05')
    HitSprites(4, 'mi062_05')
    HitSprites(5, 'mi062_06')
    HitSprites(6, 'mi062_07')
    HitSprites(7, 'mi041_02')
    HitSprites(8, 'mi040_02')
    HitSprites(9, 'mi045_02')
    HitSprites(10, 'mi060_00')
    HitSprites(11, 'mi060_01')
    HitSprites(12, 'mi060_03')
    HitSprites(13, 'mi060_05')
    HitSprites(14, 'mi060_07')
    HitSprites(15, 'mi060_14')
    HitSprites(16, 'mi050_00')
    HitSprites(17, 'mi052_00')
    HitSprites(18, 'mi054_00')
    HitSprites(19, 'mi000_00')
    HitSprites(20, 'mi000_00')
    HitSprites(25, 'mi063_00')
    HitSprites(26, 'mi063_01')
    HitSprites(27, 'mi063_02')
    HitSprites(28, 'mi063_04')
    HitSprites(29, 'mi063_10')
    HitSprites(30, 'mi077_00')
    HitSprites(31, 'mi077_01')
    HitSprites(32, 'mi077_00ex01')
    HitSprites(33, 'mi077_01ex01')
    HitSprites(34, 'mi077_00ex02')
    HitSprites(35, 'mi077_01ex02')
    HitSprites(36, 'mi077_00ex03')
    HitSprites(37, 'mi077_01ex03')
    HitSprites(24, 'mi073_01')
    CommonVoicelines(0, 'mi000')
    CommonVoicelines(1, 'mi001')
    CommonVoicelines(2, 'mi002')
    CommonVoicelines(3, 'mi003')
    CommonVoicelines(4, 'mi004')
    CommonVoicelines(5, 'mi005')
    CommonVoicelines(6, 'mi006')
    CommonVoicelines(7, 'mi007')
    CommonVoicelines(8, 'mi008')
    CommonVoicelines(9, 'mi009')
    CommonVoicelines(10, 'mi010')
    CommonVoicelines(11, 'mi011')
    CommonVoicelines(12, 'mi012')
    CommonVoicelines(13, 'mi013')
    CommonVoicelines(14, 'mi014')
    CommonVoicelines(15, 'mi015')
    CommonVoicelines(16, 'mi016')
    CommonVoicelines(17, 'mi017')
    CommonVoicelines(18, 'mi018')
    CommonVoicelines(19, 'mi019')
    CommonVoicelines(20, 'mi020')
    CommonVoicelines(21, 'mi021')
    CommonVoicelines(22, 'mi022')
    CommonVoicelines(23, 'mi023')
    CommonVoicelines(24, 'mi024')
    CommonVoicelines(25, 'mi025')
    CommonVoicelines(26, 'mi026')
    CommonVoicelines(27, 'mi027')
    CommonVoicelines(28, 'mi028')
    CommonVoicelines(29, 'mi029')
    CommonVoicelines(30, 'mi030')
    CommonVoicelines(31, 'mi031')
    CommonVoicelines(32, 'mi032')
    CommonVoicelines(33, 'mi033')
    CommonVoicelines(34, 'mi034')
    CommonVoicelines(35, 'mi035')
    CommonVoicelines(36, 'mi036')
    CommonVoicelines(37, 'mi037')
    CommonVoicelines(38, 'mi038')
    CommonVoicelines(39, 'mi039')
    CommonVoicelines(40, 'mi040')
    CommonVoicelines(41, 'mi041')
    CommonVoicelines(42, 'mi042')
    CommonVoicelines(43, 'mi043')
    CommonVoicelines(44, 'mi044')
    CommonVoicelines(45, 'mi045')
    CommonVoicelines(46, 'mi046')
    CommonVoicelines(47, 'mi047')
    CommonVoicelines(48, 'mi048')
    CommonVoicelines(49, 'mi049')
    CommonVoicelines(50, 'mi050')
    CommonVoicelines(51, 'mi051')
    CommonVoicelines(52, 'mi052')
    CommonVoicelines(53, 'mi053')
    CommonVoicelines(54, 'mi100')
    CommonVoicelines(55, 'mi101')
    CommonVoicelines(56, 'mi102')
    CommonVoicelines(57, 'mi103')
    CommonVoicelines(58, 'mi104')
    CommonVoicelines(59, 'mi105')
    CommonVoicelines(60, 'mi106')
    CommonVoicelines(61, 'mi107')
    CommonVoicelines(62, 'mi108')
    CommonVoicelines(63, 'mi109')
    CommonVoicelines(64, 'mi150')
    CommonVoicelines(65, 'mi151')
    CommonVoicelines(66, 'mi152')
    CommonVoicelines(67, 'mi153')
    CommonVoicelines(68, 'mi154')
    CommonVoicelines(69, 'mi155')
    CommonVoicelines(70, 'mi156')
    CommonVoicelines(71, 'mi157')
    CommonVoicelines(72, 'mi158')
    CommonVoicelines(75, 'mi160')
    CommonVoicelines(73, 'mi402')
    CommonVoicelines(74, 'mi403')
    CreateObject('FunnelCreate', -1)
    RegisterObject(11, 1)
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(64)


@Subroutine
def OnFrameStep():
    if SLOT_IsInHitstun:
        SLOT_4 = 0
        SLOT_6 = 0
        SLOT_7 = 0
    if not SLOT_81:
        if SLOT_4:
            if SLOT_31:
                if not CurrentStateCheck('Flying_Start'):
                    SLOT_31 = SLOT_31 + -1
                JumpYVelocity(8000)
                SuperJumpYVelocity(-8000)
                PushCollisionHeightLow(110000)
                SetYCollisionFromOrigin(190)
                if CurrentStateCheck('Flying_Start'):
                    SetYCollisionFromOrigin(270)
        else:
            JumpYVelocity(30000)
            SuperJumpYVelocity(42000)
            PushCollisionHeightLow(-1)
            SetYCollisionFromOrigin(-1)
            TriggerUponForState('huyu', 33)
    if SLOT_123:
        if not SLOT_21:
            if SLOT_11:
                if SLOT_11 > 1:
                    SLOT_11 = SLOT_11 + -1
                callSubroutine('RequestSoshiteTokiwaUgokidasu')
    if SLOT_21:
        if not SLOT_81:
            SLOT_33 = SLOT_33 + -1
            if SLOT_OverdriveTimer:
                SLOT_33 = SLOT_33 + -1
            if SLOT_7:
                DisableBarrier(1)
            if SLOT_33:
                DisableBarrier(1)
            if SLOT_6:
                if not SLOT_11:
                    SLOT_6 = SLOT_6 + -1
                if SLOT_6 <= 1:
                    SLOT_6 = 1
                DisableBarrier(1)
                if SLOT_6 <= 1:
                    setInvincible(1)
                    GuardPoint_(0)
                    GuardpointBlockUnblockable(0)
                    SpecificInvincibility(1, 1, 1, 1, 1)
                    BurstInvincibility(0)
                else:
                    setInvincible(1)
                    GuardpointBlockUnblockable(0)
                    GuardpointHitstop(-2, -1)
                    SpecificInvincibility(1, 1, 1, 1, 0)
                    if SLOT_56:
                        GuardPoint_(0)
                    else:
                        GuardPoint_(1)
                if SLOT_136 <= 0:
                    SLOT_6 = 1
                else:
                    BarrierGaugeOnCall(-25, 120)

                def upon_GUARDPOINT_ACTIVATION():
                    BarrierGaugeOnCall(-1000, 120)
                    if SLOT_4:
                        SLOT_4 = 0
                        SLOT_31 = 0
                        enterState('CmnActJumpDown')
                        EndYPhysicsImpulse()
            if SLOT_11:
                StopClock(1)
                NoDamageAction(1)
                DisableBarrier(1)

                def RunOnObject_22():
                    PreventSelfPush(1)
                if not SLOT_58:
                    SLOT_DamageMultiplier = 80
                    IgnoreBurst(1)
                    ResetPushback()
                    ResetCHPushback()
                    ResetVerticalDrag()
                    ResetCHVerticalDrag()
                    ResetGravity()
                    ResetCHGravity()
                    AirHitstunAnimationReset()
                    CHAirHitstunAnimationReset()
                    ResetGroundedHitstunAnimation()
                    ResetCHGroundedHitstunAnimation()
                    PushbackX(0)
                    PassByArmor(1)
                    DefeatOpponentBehavior(1)
                    CounterHitSetting(1)
                    NoAttackOffset(1)
                    EnemyHitstopAddition(0, 9999, 9999)
                    ShutUp(1)
                    HitOverhead(3)
                    HitLow(3)
                    HitAirUnblockable(4)
                    OppMovementUnlock(1)
                    if SLOT_11 == 1:
                        SLOT_11 = 1
                        Unknown23169(1)
                        NoDamageAction(0)
                    else:
                        SLOT_11 = SLOT_11 + -1
            else:
                SLOT_DamageMultiplier = 100
            if SLOT_11 == 1:
                callSubroutine('Flying_End')
                callSubroutine('Barrier_End')
                callSubroutine('RequestSoshiteTokiwaUgokidasu')
            if not SLOT_33:
                if not SLOT_6:
                    if not SLOT_7:
                        if not SLOT_11:
                            if not SLOT_11 == 1:
                                DisableBarrier(0)
    else:
        DespawnEAEffect('mi404_eff')
        if SLOT_4:
            SLOT_4 = 0
            SLOT_31 = 0


@Subroutine
def OnLanding():
    SLOT_61 = 0
    SLOT_4 = 0
    SLOT_31 = 240


@Subroutine
def OnGuard():
    SLOT_4 = 0


@Subroutine
def OnDamage():
    SLOT_61 = 0
    SLOT_4 = 0
    SLOT_6 = 0
    SLOT_7 = 0
    if SLOT_IsGrounded:
        SLOT_31 = 240


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def Funnel_PalletChange():

    def RunOnObject_11():
        PaletteIndex(2)
    TriggerUponForState('FunnelThudenrEff', 32)
    TriggerUponForState('FunnelThudenrEffSub', 32)


@Subroutine
def Funnel_PalletModori():

    def RunOnObject_11():
        PaletteIndex(0)
    TriggerUponForState('FunnelThudenrEff', 33)
    TriggerUponForState('FunnelThudenrEffSub', 33)


@Subroutine
def OnActionBeginPre():
    SLOT_34 = SLOT_136


@Subroutine
def OnActionBegin():
    callSubroutine('Flying_End')


@Subroutine
def OnFinalize():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 41)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    callSubroutine('Barrier_End')
    SLOT_60 = 0


@Subroutine
def FuncLaser():
    SLOT_33 = 150
    CreateObject('FunnelLaser', -1)
    SLOT_7 = 0


@Subroutine
def FuncSaws():
    SLOT_33 = 150
    CreateObject('FunnelSaws', -1)
    SLOT_7 = 0


@Subroutine
def Func6D():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_33 = 150
    CreateObject('Funnel6D', -1)
    if SLOT_OverdriveTimer:
        CreateObject('mi408_CreateEff', -1)


@Subroutine
def Func4D():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_33 = 150
    CreateObject('Funnel4D', -1)
    ObjectUpon(STATE_END, 32)
    CreateObject('Funnel4D', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('Funnel4D', -1)
    ObjectUpon(STATE_END, 34)
    if SLOT_OverdriveTimer:
        CreateObject('mi408_CreateEff', -1)


@Subroutine
def Func1D():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_33 = 150
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 32)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 33)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 34)
    if SLOT_OverdriveTimer:
        CreateObject('mi408_CreateEff', -1)


@Subroutine
def Func2D():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_33 = 150
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 35)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 36)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 37)
    if SLOT_OverdriveTimer:
        CreateObject('mi408_CreateEff', -1)


@Subroutine
def Func3D():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_33 = 150
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 38)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 39)
    CreateObject('Funnel2D', -1)
    ObjectUpon(STATE_END, 40)
    if SLOT_OverdriveTimer:
        CreateObject('mi408_CreateEff', -1)


@Subroutine
def Request5D():
    SLOT_33 = 10
    enterState('NmlAtk5D')


@Subroutine
def RequestAIR5D():
    SLOT_33 = 10
    enterState('NmlAtkAIR5D')


@Subroutine
def CheckHaveFunnel3():
    SLOT_47 = 0
    if not SLOT_115:
        if not SLOT_57:
            if not SLOT_33:
                SLOT_47 = 1


@Subroutine
def CheckFunnel():
    SLOT_47 = 0
    if not SLOT_115:
        if not SLOT_57:
            if not SLOT_33:
                if SLOT_7:
                    SLOT_47 = 1
                elif SLOT_OverdriveTimer:
                    SLOT_47 = 1


@Subroutine
def Check5D():
    SLOT_47 = 0
    if not SLOT_115:
        if not SLOT_57:
            if not SLOT_33:
                if not SLOT_OverdriveTimer:
                    SLOT_47 = 1


@Subroutine
def CheckFlying():
    if SLOT_21:
        random_(1, 2, 61)
        SLOT_47 = SLOT_0
    else:
        SLOT_47 = 0


@Subroutine
def DeleteFunnel():
    DespawnEAEffect('Funnel5C')
    DespawnEAEffect('Funnel2C')
    DespawnEAEffect('Funnel6C')
    DespawnEAEffect('FunnelAir5C')
    DespawnEAEffect('Funnel2D')
    DespawnEAEffect('Funnel4D')
    DespawnEAEffect('Funnel6D')
    DespawnEAEffect('FunnelLaser')
    DespawnEAEffect('FunnelLaser_Atk')
    DespawnEAEffect('FunnelSaws')
    DespawnEAEffect('Funnel_Mhoujin')


@Subroutine
def Guard_Init():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    SLOT_57 = 1

    def upon_EVERY_FRAME():
        callSubroutine('Flying_End')


@Subroutine
def Flying_End():
    if SLOT_4:
        if SLOT_31 == 0:
            SLOT_4 = 0
            EndYPhysicsImpulse()
            XImpulseAcceleration(40)
            enterState('CmnActJumpDown')


@Subroutine
def Barrier_End():
    if SLOT_6:
        if SLOT_6 <= 1:
            SLOT_6 = 0
            setInvincible(0)


@Subroutine
def RequestSoshiteTokiwaUgokidasu():
    if SLOT_11:
        if SLOT_11 == 1:
            if SLOT_IsGrounded:
                if not SLOT_8:
                    EnterStateIfNotInState('SoshiteTokiwaUgokidasu')


@State
def CmnActStand():
    label(0)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(0, 2, 123):
        conditionalSendToLabel(0)
    if random_(0, 2, 7):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('mi000_00', 1)
    SLOT_88 = 960
    ObjectUpon2(11, 101, 0)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():

    def upon_IMMEDIATE():
        if SLOT_7:
            ObjectUpon2(11, 1103, 0)
        else:
            ObjectUpon2(11, 103, 0)
    sprite('mi003_00', 3)
    sprite('mi003_01', 3)
    sprite('mi003_00ex01', 3)


@State
def CmnActStand2Crouch():

    def upon_IMMEDIATE():
        SLOT_60 = 1
    sprite('mi010_00', 4)
    sprite('mi010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('mi010_02', 8)
    sprite('mi010_03', 8)
    sprite('mi010_04', 8)
    sprite('mi010_05', 8)
    sprite('mi010_06', 8)
    sprite('mi010_07', 8)
    sprite('mi010_08', 8)
    sprite('mi010_09', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        if SLOT_7:
            ObjectUpon2(11, 1103, 0)
        else:
            ObjectUpon2(11, 103, 0)
    sprite('mi013_00', 3)
    sprite('mi013_01', 3)
    sprite('mi013_00ex01', 3)


@State
def CmnActCrouch2Stand():

    def upon_IMMEDIATE():
        SLOT_60 = 1
    sprite('mi010_01', 4)
    sprite('mi010_00', 4)


@State
def CmnActJumpPre():
    sprite('mi023_00', 2)
    sprite('mi023_01', 2)


@State
def CmnActJumpUpper():

    def upon_IMMEDIATE():
        if SLOT_4:
            SLOT_4 = 0
            EndYPhysicsImpulse()
    label(0)
    sprite('mi020_00', 4)
    sprite('mi020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('mi020_02', 3)
    sprite('mi020_03', 3)
    sprite('mi020_04', 3)


@State
def CmnActJumpDown():
    sprite('mi020_05', 4)
    sprite('mi020_06', 4)
    label(0)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('mi024_00', 3)
    sprite('mi024_01', 3)
    sprite('mi024_02', 3)
    sprite('mi024_03', 2)
    sprite('mi024_04', 2)
    sprite('mi024_05', 2)


@State
def CmnActLandingStiffLoop():
    sprite('mi024_00', 2)
    sprite('mi024_01', 2)
    sprite('mi024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('mi024_03', 2)
    sprite('mi024_04', 2)
    sprite('mi024_05', 2)


@State
def CmnActFWalk():
    sprite('mi030_00', 7)
    label(0)
    sprite('mi030_01', 7)
    sprite('mi030_02', 7)
    sprite('mi030_03', 7)
    sprite('mi030_04', 7)
    sprite('mi030_05', 7)
    sprite('mi030_06', 7)
    sprite('mi030_07', 7)
    sprite('mi030_08', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('mi031_00', 7)
    label(0)
    sprite('mi031_01', 7)
    sprite('mi031_02', 7)
    sprite('mi031_03', 7)
    sprite('mi031_04', 7)
    sprite('mi031_05', 7)
    sprite('mi031_06', 7)
    sprite('mi031_07', 7)
    sprite('mi031_08', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        if not SLOT_7:
            ObjectUpon2(11, 132, 0)
    sprite('mi032_00', 4)
    CommonSE('000_airdash_0')
    label(0)
    sprite('mi032_01', 4)
    sprite('mi032_02', 4)
    sprite('mi032_03', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('mi032_04', 4)
    sprite('mi032_05', 4)
    sprite('mi032_06', 4)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        setInvincible(1)
        EndMomentum(1)
    sprite('mi033_00', 2)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    SmartVoiceline('mi005')
    sprite('mi033_01', 3)
    physicsXImpulse(-36000)
    CommonSE('001_airbackdash_0')
    sprite('mi033_02', 2)
    sprite('mi033_02', 1)
    setInvincible(0)
    sprite('mi033_03', 2)
    sprite('mi033_03', 1)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('mi035_00', 2)
    SLOT_60 = 1
    label(0)
    sprite('mi035_01', 2)
    sprite('mi035_02', 2)
    sprite('mi035_03', 2)
    sprite('mi035_04', 2)
    sprite('mi035_05', 2)
    sprite('mi035_06', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('mi036_00', 2)
    SLOT_60 = 1
    label(0)
    sprite('mi036_01', 2)
    sprite('mi036_02', 2)
    sprite('mi036_03', 2)
    sprite('mi036_04', 2)
    sprite('mi036_05', 2)
    sprite('mi036_06', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('mi050_00', 1)
    sprite('mi050_01', 1)
    sprite('mi050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('mi050_01', 1)
    sprite('mi050_02', 1)
    sprite('mi050_01', 2)
    sprite('mi050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('mi050_02', 1)
    sprite('mi050_03', 1)
    sprite('mi050_02', 2)
    sprite('mi050_01', 2)
    sprite('mi050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('mi050_03', 1)
    sprite('mi050_04', 1)
    sprite('mi050_05', 2)
    sprite('mi050_06', 2)
    sprite('mi050_07', 2)
    sprite('mi050_08', 2)


@State
def CmnActHitStandLv5():
    sprite('mi050_04', 1)
    sprite('mi050_04', 1)
    sprite('mi050_04', 2)
    sprite('mi050_05', 2)
    sprite('mi050_06', 2)
    sprite('mi050_07', 2)
    sprite('mi050_08', 2)


@State
def CmnActHitStandLowLv1():
    sprite('mi052_00', 1)
    sprite('mi052_01', 1)
    sprite('mi052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('mi052_01', 1)
    sprite('mi052_02', 1)
    sprite('mi052_01', 2)
    sprite('mi052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('mi052_02', 1)
    sprite('mi052_03', 1)
    sprite('mi052_02', 2)
    sprite('mi052_01', 2)
    sprite('mi052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('mi052_03', 1)
    sprite('mi052_04', 1)
    sprite('mi052_05', 2)
    sprite('mi052_06', 2)
    sprite('mi052_07', 2)
    sprite('mi052_08', 2)


@State
def CmnActHitStandLowLv5():
    sprite('mi052_04', 1)
    sprite('mi052_04', 1)
    sprite('mi052_04', 2)
    sprite('mi052_05', 2)
    sprite('mi052_06', 2)
    sprite('mi052_07', 2)
    sprite('mi052_08', 2)


@State
def CmnActHitCrouchLv1():
    sprite('mi054_00', 1)
    sprite('mi054_01', 1)
    sprite('mi054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('mi054_01', 1)
    sprite('mi054_02', 1)
    sprite('mi054_01', 2)
    sprite('mi054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('mi054_02', 1)
    sprite('mi054_03', 1)
    sprite('mi054_02', 2)
    sprite('mi054_01', 2)
    sprite('mi054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('mi054_03', 1)
    sprite('mi054_04', 1)
    sprite('mi054_05', 2)
    sprite('mi054_06', 2)
    sprite('mi054_07', 2)
    sprite('mi054_08', 2)


@State
def CmnActHitCrouchLv5():
    sprite('mi054_04', 1)
    sprite('mi054_04', 1)
    sprite('mi054_04', 2)
    sprite('mi054_05', 2)
    sprite('mi054_06', 2)
    sprite('mi054_07', 2)
    sprite('mi054_08', 2)


@State
def CmnActBDownUpper():
    sprite('mi060_00', 4)
    label(0)
    sprite('mi060_01', 4)
    sprite('mi060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('mi060_03', 4)


@State
def CmnActBDownDown():
    sprite('mi060_04', 4)
    label(0)
    sprite('mi060_05', 4)
    sprite('mi060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('mi060_07', 2)
    sprite('mi060_08', 2)


@State
def CmnActBDownBound():
    sprite('mi060_09', 3)
    sprite('mi060_10', 3)
    sprite('mi060_11', 3)
    sprite('mi060_12', 3)
    sprite('mi060_13', 3)


@State
def CmnActBDownLoop():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi060_14', 1)


@State
def CmnActBDown2Stand():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi061_00', 4)
    sprite('mi061_01', 4)
    sprite('mi061_02', 4)
    sprite('mi061_03', 4)
    sprite('mi061_04', 3)
    sprite('mi061_05', 3)
    sprite('mi061_06', 3)
    sprite('mi061_07', 3)
    sprite('mi061_08', 3)


@State
def CmnActFDownUpper():
    sprite('mi063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('mi063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('mi063_02', 3)
    sprite('mi063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('mi063_04', 3)
    sprite('mi063_05', 3)


@State
def CmnActFDownBound():
    sprite('mi063_06', 2)
    sprite('mi063_07', 2)
    sprite('mi063_08', 2)
    sprite('mi063_09', 2)
    sprite('mi063_10', 3)


@State
def CmnActFDownLoop():
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi063_11', 3)


@State
def CmnActFDown2Stand():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi064_00', 3)
    sprite('mi064_01', 3)
    sprite('mi064_02', 3)
    sprite('mi064_03', 3)
    sprite('mi064_04', 3)
    sprite('mi064_05', 3)
    sprite('mi064_06', 3)
    sprite('mi064_07', 3)
    sprite('mi064_08', 3)
    sprite('mi064_09', 3)


@State
def CmnActVDownUpper():
    sprite('mi062_00', 3)
    label(0)
    sprite('mi062_01', 3)
    sprite('mi062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('mi062_03', 3)
    sprite('mi062_04', 3)


@State
def CmnActVDownDown():
    sprite('mi062_05', 3)
    sprite('mi062_06', 3)
    label(0)
    sprite('mi062_07', 3)
    sprite('mi062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('mi062_09', 2)
    sprite('mi062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('mi062_09', 2)
    sprite('mi062_10', 2)


@State
def CmnActBlowoff():
    sprite('mi072_00', 3)
    sprite('mi072_01', 3)
    sprite('mi072_02', 3)
    label(0)
    sprite('mi072_01', 3)
    sprite('mi072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('mi074_00', 3)
    sprite('mi074_01', 3)
    sprite('mi074_02', 3)
    sprite('mi074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('mi082_00', 2)
    sprite('mi082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('mi071_04', 1)


@State
def CmnActWallBound():
    sprite('mi073_00', 3)
    sprite('mi073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('mi073_02', 3)
    label(0)
    sprite('mi073_03', 3)
    sprite('mi073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('mi070_00', 3)
    sprite('mi070_01', 3)
    sprite('mi070_02', 2)
    sprite('mi070_03', 2)
    sprite('mi070_04', 2)
    sprite('mi070_05', 2)


@State
def CmnActStaggerDown():
    sprite('mi070_06', 6)
    sprite('mi070_07', 6)
    sprite('mi070_08', 6)
    sprite('mi070_09', 6)


@State
def CmnActUkemiStagger():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi070_10', 2)
    sprite('mi070_11', 2)
    sprite('mi070_12', 2)
    sprite('mi070_13', 2)


@State
def CmnActUkemiAirF():
    SLOT_60 = 1
    sprite('mi113_00', 3)
    sprite('mi113_01', 3)
    sprite('mi113_02', 3)
    SLOT_60 = 0


@State
def CmnActUkemiAirB():
    SLOT_60 = 1
    sprite('mi113_00', 3)
    sprite('mi113_01', 3)
    sprite('mi113_02', 3)
    SLOT_60 = 0


@State
def CmnActUkemiAirN():
    SLOT_60 = 1
    sprite('mi113_00', 3)
    sprite('mi113_01', 3)
    sprite('mi113_02', 3)
    SLOT_60 = 0


@State
def CmnActUkemiLandF():
    SLOT_60 = 2
    sprite('mi110_00', 3)
    sprite('mi110_01', 3)
    sprite('mi110_02', 3)
    sprite('mi110_03', 3)
    sprite('mi110_04', 3)
    sprite('mi110_05', 3)
    sprite('mi110_06', 3)
    sprite('mi110_07', 200)
    SLOT_60 = 0
    sprite('mi110_08', 3)
    sprite('mi110_09', 3)


@State
def CmnActUkemiLandB():
    SLOT_60 = 2
    sprite('mi111_00', 3)
    sprite('mi111_01', 3)
    sprite('mi111_02', 3)
    sprite('mi111_03', 3)
    sprite('mi111_04', 3)
    sprite('mi111_05', 3)
    sprite('mi111_06', 3)
    sprite('mi111_07', 200)
    SLOT_60 = 0
    sprite('mi111_08', 3)
    sprite('mi111_09', 3)


@State
def CmnActUkemiLandN():
    SLOT_60 = 1
    sprite('mi112_00', 3)
    sprite('mi112_01', 3)
    sprite('mi112_02', 3)
    sprite('mi112_03', 3)
    sprite('mi112_04', 3)
    sprite('mi112_05', 3)
    sprite('mi112_06', 3)
    sprite('mi112_07', 3)


@State
def CmnActUkemiLandNLanding():
    sprite('mi024_00', 3)
    sprite('mi024_01', 3)
    sprite('mi024_02', 3)
    sprite('mi024_03', 3)
    sprite('mi024_04', 3)


@State
def CmnActMidGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi040_00', 3)
    sprite('mi040_01', 3)


@State
def CmnActMidGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    label(0)
    sprite('mi040_02', 2)
    sprite('mi040_02ex00', 2)
    sprite('mi040_03', 2)
    sprite('mi040_03ex00', 2)
    sprite('mi040_04', 2)
    sprite('mi040_04ex00', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi040_01', 3)
    sprite('mi040_00', 3)


@State
def CmnActMidHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi040_05', 3)
    label(0)
    sprite('mi040_02', 2)
    sprite('mi040_02ex00', 2)
    sprite('mi040_03', 2)
    sprite('mi040_03ex00', 2)
    sprite('mi040_04', 2)
    sprite('mi040_04ex00', 2)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi040_01', 3)
    sprite('mi040_00', 3)


@State
def CmnActHighGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi041_00', 3)
    sprite('mi041_01', 3)


@State
def CmnActHighGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    label(0)
    sprite('mi041_02', 2)
    sprite('mi041_02ex00', 2)
    sprite('mi041_03', 2)
    sprite('mi041_03ex00', 2)
    sprite('mi041_04', 2)
    sprite('mi041_04ex00', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi041_01', 3)
    sprite('mi041_00', 3)


@State
def CmnActHighHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi041_05', 3)
    label(0)
    sprite('mi041_02', 2)
    sprite('mi041_02ex00', 2)
    sprite('mi041_03', 2)
    sprite('mi041_03ex00', 2)
    sprite('mi041_04', 2)
    sprite('mi041_04ex00', 2)
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi041_01', 3)
    sprite('mi041_00', 3)


@State
def CmnActCrouchGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi043_00', 3)
    sprite('mi043_01', 3)


@State
def CmnActCrouchGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    label(0)
    sprite('mi043_02', 2)
    sprite('mi043_02ex00', 2)
    sprite('mi043_03', 2)
    sprite('mi043_03ex00', 2)
    sprite('mi043_04', 2)
    sprite('mi043_04ex00', 2)
    loopRest()
    gotoLabel(0)

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')


@State
def CmnActCrouchGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi043_01', 3)
    sprite('mi043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi043_05', 3)
    label(0)
    sprite('mi043_02', 2)
    sprite('mi043_02ex00', 2)
    sprite('mi043_03', 2)
    sprite('mi043_03ex00', 2)
    sprite('mi043_04', 2)
    sprite('mi043_04ex00', 2)
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi043_01', 3)
    sprite('mi043_00', 3)


@State
def CmnActAirGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi045_00', 3)
    sprite('mi045_01', 3)


@State
def CmnActAirGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    label(0)
    sprite('mi045_02', 2)
    sprite('mi045_02ex00', 2)
    sprite('mi045_03', 2)
    sprite('mi045_03ex00', 2)
    sprite('mi045_04', 2)
    sprite('mi045_04ex00', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi045_01', 3)
    sprite('mi045_00', 3)


@State
def CmnActAirHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi045_05', 3)
    label(0)
    sprite('mi045_02', 2)
    sprite('mi045_02ex00', 2)
    sprite('mi045_03', 2)
    sprite('mi045_03ex00', 2)
    sprite('mi045_04', 2)
    sprite('mi045_04ex00', 2)
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi045_01', 3)
    sprite('mi045_00', 3)


@State
def CmnActGuardBreakStand():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi090_00', 2)
    sprite('mi090_01', 2)
    sprite('mi090_02', 1)
    SetCommonActionMark(1)
    sprite('mi090_03', 6)
    sprite('mi090_04', 6)


@State
def CmnActGuardBreakCrouch():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi091_00', 2)
    sprite('mi091_01', 2)
    sprite('mi091_02', 1)
    SetCommonActionMark(1)
    sprite('mi091_03', 6)
    sprite('mi091_04', 6)


@State
def CmnActGuardBreakAir():

    def upon_IMMEDIATE():
        callSubroutine('Guard_Init')
    sprite('mi092_00', 2)
    sprite('mi092_01', 2)
    sprite('mi092_02', 1)
    SetCommonActionMark(1)
    sprite('mi092_03', 6)
    sprite('mi092_04', 6)


@State
def CmnActAirTurn():

    def upon_IMMEDIATE():
        if SLOT_7:
            ObjectUpon2(11, 1103, 0)
        else:
            ObjectUpon2(11, 103, 0)
    sprite('mi025_00', 4)
    sprite('mi025_01', 4)
    sprite('mi025_00ex01', 4)


@State
def CmnActLockWait():

    def upon_IMMEDIATE():
        SLOT_4 = 0
        SLOT_7 = 0
    sprite('mi040_02', 1)
    sprite('mi040_01', 3)
    sprite('mi040_00', 3)


@State
def CmnActLockReject():
    sprite('mi312_00', 3)
    sprite('mi312_01', 3)
    sprite('mi312_02', 3)
    sprite('mi312_03', 3)
    sprite('mi312_04', 3)
    sprite('mi312_05', 3)
    sprite('mi312_06', 3)
    sprite('mi312_07', 2)
    sprite('mi312_08', 2)
    sprite('mi312_09', 2)
    sprite('mi312_10', 2)


@State
def CmnActAirLockWait():

    def upon_IMMEDIATE():
        SLOT_4 = 0
        SLOT_7 = 0
    sprite('mi045_02', 1)
    sprite('mi045_01', 3)
    sprite('mi045_00', 3)


@State
def CmnActAirLockReject():
    sprite('mi322_00', 3)
    sprite('mi322_01', 3)
    sprite('mi322_02', 3)
    sprite('mi322_03', 3)
    sprite('mi322_04', 3)
    sprite('mi322_05', 3)
    sprite('mi322_06', 3)
    sprite('mi322_07', 2)
    sprite('mi322_08', 2)
    sprite('mi322_09', 2)
    sprite('mi322_10', 2)


@State
def CmnActLandSpin():
    sprite('mi071_00', 4)
    sprite('mi071_01', 4)
    label(0)
    sprite('mi071_02', 2)
    sprite('mi071_03', 2)
    sprite('mi071_04', 2)
    sprite('mi071_05', 2)
    sprite('mi071_06', 2)
    sprite('mi071_07', 2)
    sprite('mi071_08', 2)
    sprite('mi071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('mi071_10', 6)
    sprite('mi071_11', 5)
    sprite('mi071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('mi071_02', 2)
    sprite('mi071_03', 2)
    sprite('mi071_04', 2)
    sprite('mi071_05', 2)
    sprite('mi071_06', 2)
    sprite('mi071_07', 2)
    sprite('mi071_08', 2)
    sprite('mi071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('mi077_00', 2)
    sprite('mi077_01', 2)
    sprite('mi077_00ex01', 2)
    sprite('mi077_01ex01', 2)
    sprite('mi077_00ex02', 2)
    sprite('mi077_01ex02', 2)
    sprite('mi077_00ex03', 2)
    sprite('mi077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('mi077_02', 4)
    label(0)
    sprite('mi077_03', 3)
    sprite('mi077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('mi077_05', 5)
    sprite('mi077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('mi060_07', 3)
    sprite('mi060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('mi060_11', 3)
    sprite('mi060_12', 3)
    sprite('mi060_13', 3)


@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_00', 2)
    sprite('mi331_01', 2)
    label(0)
    sprite('mi331_02', 3)
    sprite('mi331_03', 3)
    sprite('mi331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_05', 2)
    label(0)
    sprite('mi331_06', 3)
    sprite('mi331_07', 3)
    sprite('mi331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_09', 3)
    sprite('mi331_10', 3)


@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_11', 2)
    sprite('mi331_12', 2)
    label(0)
    sprite('mi331_02', 3)
    sprite('mi331_03', 3)
    sprite('mi331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_05', 2)
    label(0)
    sprite('mi331_06', 3)
    sprite('mi331_07', 3)
    sprite('mi331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
    sprite('mi331_13', 2)
    sprite('mi331_14', 2)
    sprite('mi020_05', 3)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 41)
    sprite('mi020_06', 3)
    label(0)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('DeleteFunnel')
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1

        def upon_EVERY_FRAME():
            if SLOT_31 <= 1:
                SLOT_31 = SLOT_31 + 1
    sprite('mi333_00', 3)
    sprite('mi333_01', 3)
    sprite('mi333_02', 3)
    CreateObject('EMB_OD', -1)
    CharacterFlash(16639, 20, 1)
    sprite('mi333_03', 32767)
    loopRest()


@State
def CmnActOverDriveLoop():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1
    sprite('mi333_04', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('mi333_05', 3)
    SetCompositeColor(0, 255, 255, 255, 255)
    sprite('mi333_06', 3)
    sprite('mi333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1
    sprite('mi333_08', 6)
    sprite('mi333_09', 6)


@State
def CmnActAirOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('DeleteFunnel')
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1
    sprite('mi333_10', 3)
    sprite('mi333_11', 3)
    sprite('mi333_12', 3)
    CreateObject('EMB_OD', -1)
    CharacterFlash(16639, 20, 1)
    sprite('mi333_13', 32767)
    loopRest()


@State
def CmnActAirOverDriveLoop():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1
    sprite('mi333_14', 3)
    StopCharacterFlash1(16534)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('mi333_05', 3)
    SetCompositeColor(0, 255, 255, 255, 255)
    sprite('mi333_06', 3)
    sprite('mi333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 333, 0)
        SLOT_57 = 1
    sprite('mi333_15', 6)
    sprite('mi333_16', 6)


@State
def Flying_Start():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffBlockCancel(1)
        WhiffBarrierCancel2(1)
        ForceFaceSprite()
        SLOT_61 = 1
        SLOT_4 = 1

        def upon_STATE_END():
            TriggerUponForState('huyu', 32)
            SLOT_31 = SLOT_31 + -1
        if SLOT_YDistanceFromFloor >= 600000:
            SLOT_31 = 42
        elif SLOT_YDistanceFromFloor >= 400000:
            SLOT_31 = 120
        else:
            SLOT_31 = 240
    sprite('mi024_00', 3)
    DespawnEAEffect('huyu')
    CreateObject('huyu', -1)
    EndMomentum(1)
    physicsYImpulse(5000)
    setGravity(500)
    PrivateSE('mise_02')
    sprite('mi024_01', 3)
    sprite('mi024_02', 3)
    sprite('mi024_03', 3)
    sprite('mi024_04', 3)
    sprite('mi024_05', 2)
    sprite('mi024_05', 1)


@Subroutine
def Func_Flying():
    if SLOT_4:
        AttackDirection(0)
        HitOverhead(0)
        HitLow(0)
        HitAirUnblockable(0)
        MoveAttributes(1, 0, 0, 0, 0)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('AN_NmlAtkAIR5D_Chain')
        HitOrBlockJumpCancel(1)

        def upon_EVERY_FRAME():
            if SLOT_31 <= 1:
                SLOT_31 = 1
                ChainCancel(0)
                SpecialCancel(0)
                SpecialCancelOnHit(0)

        def upon_STATE_END():
            if SLOT_31 <= 1:
                SLOT_31 = 0


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
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
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('Func_Flying')
    sprite('mi200_00', 1)
    PerInertia(60)
    sprite('mi200_01', 2)
    sprite('mi200_02', 2)
    RandomCommonVoiceline(0)
    sprite('mi200_03', 4)
    CommonSE('003_swing_grap_0_0')
    sprite('mi200_04', 3)
    Recovery()
    Unknown2063()
    sprite('mi200_05', 3)
    sprite('mi200_06', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(85)
        Damage(650)
        AirPushbackY(20000)
        AirUntechableTime(17)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        HitJumpCancel(1)
        callSubroutine('Func_Flying')
    sprite('mi201_00', 1)
    sprite('mi201_01', 2)
    sprite('mi201_02', 2)
    sprite('mi201_03', 2)
    RandomCommonVoiceline(1)
    sprite('mi201_04', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('mi201_05', 3)
    sprite('mi201_06', 3)
    Recovery()
    Unknown2063()
    sprite('mi201_07', 3)
    sprite('mi201_08', 3)
    sprite('mi201_09', 3)
    sprite('mi201_10', 3)
    sprite('mi201_11', 3)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(840)
        AirUntechableTime(25)
        AirPushbackX(20000)
        AirPushbackY(15000)
        AirHitstunAnimation(17)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        HitJumpCancel(1)
        callSubroutine('Func_Flying')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            BufferedOrPressedGoto('AN_NmlAtk5CC')
    sprite('mi202_00', 3)
    sprite('mi202_01', 3)
    physicsXImpulse(3000)
    sprite('mi202_02', 2)
    XImpulseAcceleration(400)
    CommonSE('004_swing_grap_1_2')
    sprite('mi202_03', 2)
    RandomCommonVoiceline(2)
    XImpulseAcceleration(400)
    sprite('mi202_04', 3)
    CreateObject('mi202eff', 0)
    XImpulseAcceleration(30)
    PrivateSE('mise_04')
    BeginBuffer('AN_NmlAtk5CC')
    sprite('mi202_05', 3)
    XImpulseAcceleration(0)
    Recovery()
    Unknown2063()
    BufferedOrPressedGoto('AN_NmlAtk5CC')
    sprite('mi202_06', 3)
    sprite('mi202_07', 3)
    sprite('mi202_08', 3)
    DisallowGoto2('AN_NmlAtk5CC')
    sprite('mi202_09', 3)
    sprite('mi202_10', 3)
    sprite('mi202_11', 3)
    sprite('mi202_12', 3)


@State
def AN_NmlAtk5CC():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        callSubroutine('Func_Flying')
        CreateObject('Funnel5C', -1)

        def RunOnObject_11():
            Visibility(1)
    sprite('mi202_05', 3)
    sprite('mi202_06', 3)
    sprite('mi202_07', 3)
    sprite('mi202_05', 3)
    sprite('mi202_06', 3)
    sprite('mi202_07', 3)
    sprite('mi202_05', 3)
    sprite('mi202_06', 3)
    sprite('mi202_07', 3)
    sprite('mi202_08', 2)
    Recovery()
    sprite('mi202_09', 2)
    sprite('mi202_10', 2)
    sprite('mi202_11', 2)
    sprite('mi202_12', 2)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
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
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('Func_Flying')
    sprite('mi230_00', 1)
    PerInertia(60)
    sprite('mi230_01', 2)
    sprite('mi230_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('mi230_03', 3)
    sprite('mi230_04', 3)
    Recovery()
    Unknown2063()
    sprite('mi230_02', 2)
    sprite('mi230_01', 2)
    sprite('mi230_00', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(500)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        callSubroutine('Func_Flying')
        SLOT_60 = 2
    sprite('mi231_00', 1)
    sprite('mi231_01', 2)
    sprite('mi231_02', 2)
    sprite('mi231_03', 2)
    physicsXImpulse(4000)
    CommonSE('003_swing_grap_0_1')
    sprite('mi231_04', 1)
    StartMultihit()
    XImpulseAcceleration(500)
    RandomCommonVoiceline(1)
    sprite('mi231_04', 3)
    sprite('mi231_05', 3)
    sprite('mi231_05', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    XImpulseAcceleration(40)
    sprite('mi231_06', 6)
    XImpulseAcceleration(40)
    sprite('mi231_07', 6)
    XImpulseAcceleration(40)
    sprite('mi231_08', 6)
    XImpulseAcceleration(0)
    sprite('mi231_09', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(880)
        AirUntechableTime(25)
        AirPushbackX(2000)
        UseSlashHitspark(1)
        FatalCounter(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        callSubroutine('Func_Flying')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            BufferedOrPressedGoto('AN_NmlAtk2CC')
    sprite('mi232_00', 3)
    sprite('mi232_01', 3)
    sprite('mi232_02', 3)
    sprite('mi232_03', 3)
    AddX(50000)
    sprite('mi232_04', 3)
    sprite('mi232_05', 3)
    RandomCommonVoiceline(2)
    CommonSE('006_swing_blade_2')
    PrivateSE('mise_04')
    sprite('mi232_06', 3)
    CreateObject('mi232', -1)
    BeginBuffer('AN_NmlAtk2CC')
    sprite('mi232_07', 4)
    Recovery()
    Unknown2063()
    sprite('mi232_08', 4)
    sprite('mi232_09', 3)
    BufferedOrPressedGoto('AN_NmlAtk2CC')
    sprite('mi232_10', 3)
    sprite('mi232_11', 3)
    sprite('mi232_12', 2)
    DisallowGoto2('AN_NmlAtk2CC')
    sprite('mi232_13', 2)
    sprite('mi232_14', 2)
    sprite('mi232_15', 2)
    sprite('mi232_16', 2)


@State
def AN_NmlAtk2CC():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        CrouchState(1)
        callSubroutine('Func_Flying')
        CreateObject('Funnel2C', -1)

        def RunOnObject_11():
            Visibility(1)
    sprite('mi232_09', 3)
    sprite('mi232_10', 3)
    sprite('mi232_11', 3)
    sprite('mi232_09', 3)
    sprite('mi232_10', 3)
    sprite('mi232_11', 3)
    sprite('mi232_09', 3)
    sprite('mi232_10', 3)
    sprite('mi232_11', 3)
    sprite('mi232_12', 2)
    sprite('mi232_13', 2)
    sprite('mi232_14', 2)
    Recovery()
    sprite('mi232_15', 2)
    sprite('mi232_16', 2)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        AttackP2(82)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(18000)
        AirUntechableTime(29)
        CHHardKnockdown(10)
        HitLow(2)
        UseSlashHitspark(1)
        HitCancel('NmlAtk5D')
        HitCancel('AN_NmlAtk5D_Chain')
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        callSubroutine('Func_Flying')
        if SLOT_4:
            SpecialCancel(1)
            HitOrBlockCancel('NmlAtk5D')
            HitOrBlockCancel('AN_NmlAtk5D_Chain')
        SLOT_60 = 2
    sprite('mi235_00', 2)
    sprite('mi235_01', 2)
    sprite('mi235_02', 3)
    sprite('mi235_03', 3)
    physicsXImpulse(3000)
    sprite('mi235_04', 3)
    SetInertia(20000)
    XImpulseAcceleration(300)
    RandomCommonVoiceline(2)
    CommonSE('004_swing_grap_1_2')
    sprite('mi235_05', 3)
    XImpulseAcceleration(300)
    sprite('mi235_06', 3)
    XImpulseAcceleration(300)
    sprite('mi235_05', 3)
    XImpulseAcceleration(60)
    sprite('mi235_07', 2)
    XImpulseAcceleration(60)
    PerInertia(0)
    Recovery()
    Unknown2063()
    SLOT_60 = 0
    sprite('mi235_07', 2)
    XImpulseAcceleration(60)
    sprite('mi235_08', 2)
    XImpulseAcceleration(60)
    sprite('mi235_08', 2)
    XImpulseAcceleration(60)
    sprite('mi235_09', 5)
    XImpulseAcceleration(0)
    sprite('mi235_10', 5)
    sprite('mi235_11', 5)
    sprite('mi235_12', 5)
    sprite('mi235_13', 5)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(770)
        AttackP1(90)
        AttackP2(79)
        HitAirUnblockable(3)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(-2000)
        AirUntechableTime(30)
        SLOT_2 = SLOT_4
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            BeginBuffer('Flying_Start2')
        callSubroutine('Func_Flying')
    sprite('mi210_00', 3)
    sprite('mi210_01', 3)
    physicsXImpulse(15000)
    sprite('mi210_02', 3)
    SmartVoiceline('mi108')
    CommonSE('004_swing_grap_1_2')
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('mi210_03', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(20000)
    setGravity(1800)
    SLOT_4 = 0
    sprite('mi210_04', 4)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('mi210_05', 3)
    sprite('mi210_06', 3)
    sprite('mi210_07', 2)
    sprite('mi210_08', 2)
    sprite('mi020_05', 4)
    BufferedOrPressedGoto('Flying_Start2')
    sprite('mi020_06', 4)
    label(0)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('mi024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('mi024_01', 2)
    sprite('mi024_02', 1)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(980)
        AttackP1(80)
        BonusProration(110)
        GroundedHitstunAnimation(9)
        AirPushbackY(-21000)
        HardKnockdown(10)
        PushbackX(12000)
        HitOverhead(2)
        StarterRating(2)
        HitCancel('NmlAtk5D')
        HitCancel('AN_NmlAtk5D_Chain')
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        callSubroutine('Func_Flying')
        if SLOT_4:
            SpecialCancel(1)

        def upon_LANDING():
            HitOrBlockJumpCancel(0)
            EndMomentum(1)
            LandingEffects(100, 1, 1)
    sprite('mi211_00', 2)
    sprite('mi211_01', 2)
    sprite('mi211_02', 2)
    physicsXImpulse(5000)
    RandomCommonVoiceline(2)
    CommonSE('019_cloth_c')
    sprite('mi211_03', 2)
    sprite('mi211_04', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    sprite('mi211_05', 2)
    sprite('mi211_06', 3)
    XImpulseAcceleration(300)
    physicsYImpulse(8000)
    setGravity(2000)
    SLOT_4 = 0
    ForcedLandingRecovery(6, 1)
    sprite('mi211_07', 3)
    sprite('mi211_08', 3)
    sprite('mi211_09', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('mi211_10', 4)
    setInvincible(0)
    sprite('mi211_11', 3)
    Recovery()
    Unknown2063()
    sprite('mi211_12', 3)
    sprite('mi211_13', 3)
    sprite('mi211_14', 3)
    sprite('mi211_15', 3)
    sprite('mi211_16', 3)
    sprite('mi211_17', 3)
    loopRest()
    SpriteCall('mi211_18', 2, 2, 4)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(650)
        AttackP1(90)
        AttackP2(82)
        SingleProration(1)
        AirUntechableTime(25)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(20000)
        PushbackX(19800)
        AttackDirection(0)
        if not SLOT_4:
            HitLow(2)
            MoveAttributes(0, 0, 1, 0, 0)
            StarterRating(2)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('AN_NmlAtk5D_Chain')
        HitJumpCancel(1)
        callSubroutine('Func_Flying')
        if SLOT_94:
            SpecialCancel(0)
    sprite('mi212_00', 5)
    sprite('mi212_01', 4)
    physicsXImpulse(2000)
    sprite('mi212_02', 4)
    XImpulseAcceleration(200)
    sprite('mi212_03', 4)
    XImpulseAcceleration(250)
    sprite('mi212_04', 3)
    XImpulseAcceleration(300)
    CreateObject('mi212eff', -1)
    sprite('mi212_05', 3)
    XImpulseAcceleration(50)
    RandomCommonVoiceline(2)
    CommonSE('004_swing_grap_1_1')
    sprite('mi212_06', 3)
    XImpulseAcceleration(50)
    sprite('mi212_07', 2)
    XImpulseAcceleration(50)
    sprite('mi212_08', 2)
    XImpulseAcceleration(200)
    sprite('mi212_09', 2)
    XImpulseAcceleration(200)
    CommonSE('004_swing_grap_1_2')
    CommonSE('006_swing_blade_2')
    PrivateSE('mise_04')
    BeginBuffer('AN_NmlAtk6CC')
    sprite('mi212_10', 3)
    CreateObject('mi212eff2', -1)
    RefreshMultihit()
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(2)
    PushbackX(1000)
    AirPushbackX(2000)
    AirPushbackY(-60000)
    AirUntechableTime(60)
    GroundBounce(1)
    BouncePercentage(30)
    EndMomentum(1)
    HitJumpCancel(0)
    if not SLOT_4:
        HitOverhead(2)
        HitLow(0)
        MoveAttributes(0, 1, 0, 0, 0)

    def upon_OPPONENT_HIT():
        BufferedOrPressedGoto('AN_NmlAtk6CC')
        if SLOT_94:
            SpecialCancel(1)
            if SLOT_4:
                if not SLOT_31:
                    SpecialCancel(0)
    sprite('mi212_11', 3)
    Recovery()
    Unknown2063()
    sprite('mi212_12', 3)
    sprite('mi212_13', 3)
    sprite('mi212_11', 3)
    sprite('mi212_12', 3)
    DisallowGoto2('AN_NmlAtk6CC')
    sprite('mi212_13', 3)
    sprite('mi212_14', 4)
    sprite('mi212_15', 4)
    sprite('mi212_16', 4)
    sprite('mi212_17', 4)


@State
def AN_NmlAtk6CC():

    def upon_IMMEDIATE():
        TurnLimitByInitialize(1)
        AttackDefaults_StandingNormal()
        callSubroutine('Func_Flying')
        CreateObject('Funnel6C', -1)

        def RunOnObject_11():
            Visibility(1)
    sprite('mi212_11', 3)
    sprite('mi212_12', 3)
    sprite('mi212_13', 3)
    sprite('mi212_11', 3)
    sprite('mi212_12', 3)
    sprite('mi212_13', 3)
    sprite('mi212_11', 3)
    sprite('mi212_12', 3)
    sprite('mi212_13', 3)
    sprite('mi212_14', 4)
    sprite('mi212_15', 4)
    Recovery()
    sprite('mi212_16', 4)
    sprite('mi212_17', 4)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('AN_NmlAtkAIR5D_Chain')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('Flying_Start')
    sprite('mi250_00', 3)
    sprite('mi250_01', 3)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('mi250_02', 3)
    sprite('mi250_03', 3)
    Recovery()
    Unknown2063()
    sprite('mi250_04', 3)
    sprite('mi250_00', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AirUntechableTime(17)
        Damage(560)
        AttackP1(80)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('AN_NmlAtkAIR5D_Chain')
        HitOrBlockCancel('Flying_Start')
    sprite('mi251_00', 2)
    sprite('mi251_01', 3)
    sprite('mi251_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_1')
    sprite('mi251_03', 3)
    sprite('mi251_04', 3)
    sprite('mi251_05', 3)
    Recovery()
    Unknown2063()
    sprite('mi251_06', 3)
    sprite('mi251_07', 3)
    sprite('mi251_08', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AirPushbackY(8000)
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('AN_NmlAtkAIR5D_Chain')
        HitOrBlockCancel('Flying_Start')
    sprite('mi252_00', 3)
    sprite('mi252_01', 3)
    sprite('mi252_02', 3)
    sprite('mi252_03', 3)
    RandomCommonVoiceline(2)
    CommonSE('004_swing_grap_1_1')
    PrivateSE('mise_04')
    sprite('mi252_04', 3)
    CreateObject('mi252eff', -1)

    def RunOnObject_1():
        Rotation(95000)
        AddY(140000)
        AddX(185000)
    sprite('mi252_05', 2)
    sprite('mi252_06', 2)
    if SLOT_7:
        Recovery()
    else:
        SLOT_52 = 1
        if not SLOT_33:
            CreateObject('FunnelAir5C', -1)

            def RunOnObject_11():
                Visibility(1)
    Unknown2063()
    sprite('mi252_07', 2)
    sprite('mi252_08', 4)
    sprite('mi252_09', 4)
    sprite('mi252_10', 4)
    sprite('mi252_11', 3)
    Recovery()
    sprite('mi252_12', 3)
    sprite('mi252_13', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(300)
        AttackP1(80)
        AttackP2(94)
        AirPushbackX(1000)
        AirPushbackY(8000)
        Hitstop(1)
        PushbackX(6000)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HitOverhead(0)
        StarterRating(2)
        HitOrBlockCancel('Flying_Start')
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)

        def upon_EVERY_FRAME():
            SLOT_33 = 120

        def upon_STATE_END():
            SLOT_33 = 0
    sprite('mi254_00', 2)
    sprite('mi254_01', 2)
    sprite('mi254_02', 2)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(10)
    YAccel(10)
    PerGravity(10)
    sprite('mi254_03', 2)
    sprite('mi254_04', 2)
    sprite('mi254_05', 2)
    Voiceline('mi109')
    sprite('mi254_06', 4)
    CreateObject('FuncAir2C', -1)
    RefreshMultihit()
    sprite('mi254_07', 4)
    RefreshMultihit()
    sprite('mi254_08', 4)
    RefreshMultihit()
    loopRest()
    if not CheckInput(INPUT_HOLD_C):
        notConditionalSendToLabel(9)
    sprite('mi254_06', 4)
    RefreshMultihit()
    sprite('mi254_07', 4)
    RefreshMultihit()
    sprite('mi254_08', 4)
    RefreshMultihit()
    sprite('mi254_06', 4)
    RefreshMultihit()
    sprite('mi254_07', 4)
    RefreshMultihit()
    sprite('mi254_08', 4)
    RefreshMultihit()
    sprite('mi254_06', 4)
    RefreshMultihit()
    sprite('mi254_07', 4)
    RefreshMultihit()
    sprite('mi254_08', 4)
    RefreshMultihit()
    label(9)
    sprite('mi254_09', 2)
    Recovery()
    Unknown2063()
    PopGravity()
    sprite('mi254_10', 2)
    sprite('mi254_11', 2)
    sprite('mi254_12', 4)
    TriggerUponForState('FuncAir2C', 32)
    sprite('mi254_13', 2)
    sprite('mi254_14', 2)
    sprite('mi254_15', 2)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
        SLOT_57 = 1
        callSubroutine('DeleteFunnel')
        DespawnEAEffect('Funnel_Mhoujin')
    if SLOT_7:
        conditionalSendToLabel(0)
    sprite('mi203_00', 1)
    SLOT_60 = 1
    sprite('mi203_01', 1)
    sprite('mi203_02', 1)
    sprite('mi203_03', 4)
    ObjectUpon2(11, 203, 0)
    SLOT_60 = 0
    Voiceline('mi106')
    sprite('mi203_04', 4)
    sprite('mi203_05', 4)
    SLOT_57 = 0
    sprite('mi203_06', 4)
    sprite('mi203_07', 4)
    CreateObject('FunnelThudenrEffTenkai', 100)
    sprite('mi203_10', 2)
    sprite('mi203_11', 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mi203_11', 1)
    sprite('mi203_10', 1)
    sprite('mi203_09', 1)
    sprite('mi204_00', 3)
    ObjectUpon2(11, 204, 0)
    Voiceline('mi107')
    sprite('mi204_01', 3)
    sprite('mi204_02', 3)
    sprite('mi204_03', 3)
    sprite('mi203_02', 3)
    sprite('mi204_04', 3)
    CreateObject('FunnelThudenrEffShunou', 100)
    sprite('mi203_01', 3)
    sprite('mi203_00', 2)
    label(9)
    sprite('keep', 1)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        SLOT_57 = 1
    if SLOT_7:
        conditionalSendToLabel(0)
    sprite('mi253_00', 2)
    SLOT_60 = 1
    sprite('mi253_01', 2)
    sprite('mi253_02', 2)
    sprite('mi253_03', 4)
    ObjectUpon2(11, 203, 0)
    SLOT_60 = 0
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    Voiceline('mi106')
    sprite('mi253_04', 4)
    sprite('mi253_05', 4)
    SLOT_57 = 1
    sprite('mi253_06', 4)
    sprite('mi253_07', 4)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(50)
    CreateObject('FunnelThudenrEffTenkai', 100)
    sprite('mi253_10', 2)
    sprite('mi253_11', 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mi253_11', 2)
    sprite('mi253_10', 2)
    sprite('mi253_09', 2)
    sprite('mi253_12', 3)
    ObjectUpon2(11, 204, 0)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    Voiceline('mi107')
    sprite('mi253_13', 3)
    sprite('mi253_14', 3)
    sprite('mi253_15', 3)
    sprite('mi253_02', 3)
    sprite('mi253_16', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(50)
    CreateObject('FunnelThudenrEffShunou', 100)
    sprite('mi253_01', 3)
    sprite('mi253_00', 2)
    label(9)
    sprite('keep', 1)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        if not SLOT_4:
            RunLoopUpon(17, 61)

            def upon_17():
                WhiffBlockCancel(1)
                WhiffBarrierCancel2(1)
                WhiffSpecialCancel(1)
                if SLOT_4:
                    if not SLOT_31:
                        WhiffBlockCancel(0)
                        WhiffBarrierCancel2(0)
                        WhiffSpecialCancel(0)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    RandomVoiceline('mi404', 100, 'mi405', 100, 'mi404', 100, 'mi405', 100)
    sprite('mi300_06', 60)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('mi201_00', 3)
    sprite('mi201_01', 3)
    sprite('mi201_02', 3)
    sprite('mi201_03', 3)
    sprite('mi201_04ex00', 3)
    sprite('mi201_04', 3)
    AttackOff()
    sprite('mi201_05', 6)
    sprite('mi201_06', 4)
    sprite('mi201_07', 4)
    sprite('mi201_08', 4)
    sprite('mi201_09', 4)
    sprite('mi201_10', 4)
    sprite('mi201_11', 3)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        Blockstun(24)
        AirUntechableTime(60)
        Stagger(60)
        Crumple(50)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(12)
        AirPushbackX(45000)
        AirPushbackY(18000)
        Floorslide(15)
        Wallbounce(1)
        WallbounceReboundTime(30)
        Wallstick(1)
        WallstickDuration(35)
        AirHitstunAfterWallbounce(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        UseSlashHitspark(1)
        StarterRating(2)
        if SLOT_4:
            AttackDirection(0)
            MoveAttributes(1, 0, 0, 0, 0)

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

        def upon_45():
            if SLOT_7:
                SLOT_51 = 1
            elif SLOT_33:
                SLOT_51 = 1
            else:
                SLOT_51 = 0
            if not SLOT_51:
                ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)

                def upon_STATE_END():
                    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi340_17', 1)
    sprite('mi340_00', 2)
    SpriteCall('mi340_17', 2, 2, 51)
    sprite('mi340_01', 1)
    SpriteCall('mi340_18', 1, 2, 51)
    E0EAEffect('GuardCrushWind', 65535)
    HeatChange(-2500)
    Voiceline('mi159')
    sprite('mi340_01', 2)
    SpriteCall('mi340_18', 2, 2, 51)
    CharacterFlash(16763080, 8, 2)
    sprite('mi340_02', 3)
    SpriteCall('mi340_19', 3, 2, 51)
    sprite('mi340_03', 3)
    SpriteCall('mi340_20', 3, 2, 51)
    label(100)
    sprite('mi340_04', 3)
    SpriteCall('mi340_21', 3, 2, 51)
    if not SLOT_51:
        CommonSE('011_spin_0')
    sprite('mi340_05', 3)
    SpriteCall('mi340_22', 3, 2, 51)
    sprite('mi340_06', 3)
    SpriteCall('mi340_23', 3, 2, 51)
    if not SLOT_51:
        CommonSE('011_spin_0')
    sprite('mi340_04ex', 3)
    SpriteCall('mi340_21', 3, 2, 51)
    sprite('mi340_05ex', 3)
    SpriteCall('mi340_22', 3, 2, 51)
    if not SLOT_51:
        CommonSE('011_spin_0')
    sprite('mi340_06ex', 3)
    SpriteCall('mi340_23', 3, 2, 51)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('mi340_07', 4)
    SpriteCall('mi340_24', 4, 2, 51)
    physicsXImpulse(30000)
    CommonSE('004_swing_grap_1_2')
    sprite('mi340_08', 4)
    SpriteCall('mi340_25', 4, 2, 51)
    XImpulseAcceleration(30)
    sprite('mi340_09', 1)
    SpriteCall('mi340_26', 1, 2, 51)
    XImpulseAcceleration(0)
    sprite('mi340_09', 2)
    SpriteCall('mi340_26', 2, 2, 51)
    AttackOff()
    EnableAfterimage(0)
    sprite('mi340_10', 3)
    SpriteCall('mi340_27', 3, 2, 51)
    sprite('mi340_11', 3)
    SpriteCall('mi340_28', 3, 2, 51)
    sprite('mi340_12', 4)
    SpriteCall('mi340_29', 4, 2, 51)
    sprite('mi340_13', 4)
    SpriteCall('mi340_30', 4, 2, 51)
    sprite('mi340_14', 3)
    SpriteCall('mi340_31', 3, 2, 51)
    sprite('mi340_15', 3)
    SpriteCall('mi340_32', 3, 2, 51)
    sprite('mi340_16', 3)
    SpriteCall('mi340_33', 3, 2, 51)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('ThrowExe', 1, 1, 0)
            EndMomentum(1)
        else:
            AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        if SLOT_11:
            AttackOff()

        def upon_OPPONENT_HIT():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
        DistanceCheck(200000, 1, 130000, 0)
    sprite('mi310_00', 3)
    sprite('mi310_01', 3)
    sprite('mi310_02', 3)
    SLOT_56 = 1
    sprite('mi310_03', 3)
    SLOT_56 = 0
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi310_04', 4)
    sprite('mi310_05', 4)
    sprite('mi310_06', 4)
    sprite('mi310_07', 4)
    sprite('mi310_08', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(80)
        AirPushbackY(-50000)
        GroundBounce(1)
        BouncePercentage(40)
        HardKnockdown(1)
        UseSlashHitspark(1)
        StarterRating(2)
        StayAfterMovement(1, 0)
        if SLOT_4:
            HitOrBlockJumpCancel(1)

            def upon_EVERY_FRAME():
                if SLOT_31 <= 1:
                    SLOT_31 = 1
                    SpecialCancel(0)
        SLOT_57 = 1

        def upon_OPPONENT_HIT():
            SLOT_57 = 0

        def upon_STATE_END():
            if SLOT_4:
                if SLOT_31 <= 1:
                    SLOT_31 = 0
    sprite('mi310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi311_00', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    if not SLOT_7:
        ObjectUpon2(11, 311, 0)
    sprite('mi311_01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_02', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_03', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_04', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi311_05', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('mi153')
    sprite('mi311_06', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi311_07', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi311_08', 5)
    OppThrowAnimation(14, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CommonSE('006_swing_blade_2')
    sprite('mi311_09', 1)
    StartMultihit()
    OppThrowAnimation(14, 0)
    OppThrowPosition(1, 5, 5, 0, 0)
    CreateParticle('mief311_spark', 0)
    CreateObject('mi311eff', -1)

    def RunOnObject_1():
        AddX(100000)
    CreateObject('mi311eff', -1)

    def RunOnObject_1():
        Flip()
        AddX(75000)
    sprite('mi311_09', 4)
    sprite('mi311_10', 5)
    sprite('mi311_11', 5)
    sprite('mi311_12', 5)
    sprite('mi311_13', 3)
    sprite('mi311_14', 3)
    sprite('mi211_15ex00', 3)
    sprite('mi211_16ex00', 3)
    sprite('mi211_17ex00', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('BackThrowExe', 1, 1, 0)
            EndMomentum(1)
        else:
            AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        if SLOT_11:
            AttackOff()

        def upon_OPPONENT_HIT():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
        DistanceCheck(200000, 1, 130000, 0)
    sprite('mi310_00', 3)
    sprite('mi310_01', 3)
    sprite('mi310_02', 3)
    SLOT_56 = 1
    sprite('mi310_03', 3)
    SLOT_56 = 0
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi310_04', 4)
    sprite('mi310_05', 4)
    sprite('mi310_06', 4)
    sprite('mi310_07', 4)
    sprite('mi310_08', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(16000)
        AirPushbackY(22000)
        StarterRating(2)
        HitAnywhere(1)
        OppPositionOnHit(1, 100000, 100000)
        SpecialCancel(0)
        EnableRapidCancel(0)
        DamageFromStateOnly('BackThrowExe')
        DamageEffect(8, '')
        ShutUp(1)
        StayAfterMovement(1, 0)
        if SLOT_4:

            def upon_EVERY_FRAME():
                if SLOT_31 <= 1:
                    SLOT_31 = 1
                    SpecialCancel(0)
        SLOT_57 = 1

        def upon_STATE_END():
            ForceFaceSprite()
            if SLOT_4:
                if SLOT_31 <= 1:
                    SLOT_31 = 0
    sprite('mi310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi311_00', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    if not SLOT_7:
        ObjectUpon2(11, 313, 0)
    SetXCollisionFromOrigin(200)
    sprite('mi311_01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_02', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_03', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi311_04', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi313_00', 5)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    Voiceline('mi153')
    sprite('mi313_01', 5)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CommonSE('004_swing_grap_1_2')
    sprite('mi313_02', 8)
    Flip()
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    SetXCollisionFromOrigin(300)
    sprite('mi313_03', 6)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    SetXCollisionFromOrigin(400)
    sprite('mi313_04', 6)
    SetXCollisionFromOrigin(500)
    sprite('mi313_05', 6)
    SetXCollisionFromOrigin(600)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    CommonSE('006_swing_blade_2')
    sprite('mi313_06', 4)
    CreateObject('mi312', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1500)
    AttackP2(50)
    Hitstop(10)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(80000)
    AirPushbackY(16000)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    UseSlashHitspark(1)
    WhiffCrouchBlockCancel(1)
    OppPositionOnHit(0, 0, 0)
    DamageFromStateOnly('')
    DamageEffect(0, '')
    ShutUp(0)

    def upon_OPPONENT_HIT():
        SLOT_57 = 0
        SetXCollisionFromOrigin(-1)
        SpecialCancel(1)
        EnableRapidCancel(1)
        if SLOT_4:
            HitOrBlockJumpCancel(1)
            if not SLOT_31:
                SpecialCancel(0)
    sprite('mi313_07', 4)
    sprite('mi313_08', 4)
    sprite('mi313_09', 4)
    sprite('mi313_10', 4)
    sprite('mi313_11', 4)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
        if SLOT_11:
            AttackOff()

        def upon_OPPONENT_HIT():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
    sprite('mi320_00', 3)
    sprite('mi320_01', 3)
    sprite('mi320_02', 3)
    ForcedLandingRecovery(4, 1)
    SLOT_56 = 1
    sprite('mi320_03', 3)
    SLOT_56 = 0
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi320_04', 3)
    sprite('mi320_05', 3)
    sprite('mi320_06', 5)
    sprite('mi320_07', 3)
    sprite('mi320_08', 3)
    sprite('mi320_09', 3)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(-1)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(100)
        GroundBounce(1)
        BouncePercentage(50)
        AirHitstunAfterWallbounce(100)
        HardKnockdown(1)
        StarterRating(2)
        HitAnywhere(1)
        SpecialCancel(0)
        EnableRapidCancel(0)
        DamageFromStateOnly('AirThrowExe')
        DamageEffect(8, '')
        ShutUp(1)
        EndMomentum(1)
        ForcedLandingRecovery(0, 0)
        SLOT_57 = 1

        def upon_OPPONENT_HIT():
            SLOT_57 = 0
    sprite('mi320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi321_00', 4)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    if not SLOT_7:
        ObjectUpon2(11, 321, 0)
    sprite('mi321_01', 4)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CommonSE('019_cloth_c')
    sprite('mi321_02', 5)
    AttackOff()
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    physicsYImpulse(18000)
    setGravity(1000)
    sprite('mi321_02', 3)
    RefreshMultihit()
    sprite('mi321_03', 3)
    sprite('mi321_04', 3)
    Voiceline('mi154')
    CommonSE('004_swing_grap_1_2')
    sprite('mi321_05', 3)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    Hitstop(12)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    ResetPushback()
    AirPushbackY(-80000)
    HardKnockdown(0)
    DamageFromStateOnly('')
    DamageEffect(0, '')
    ShutUp(0)

    def upon_OPPONENT_HIT():
        SpecialCancel(1)
        EnableRapidCancel(1)
        HitOrBlockCancel('Flying_Start')
    sprite('mi321_06', 3)
    sprite('mi321_07', 3)
    sprite('mi321_08', 3)
    sprite('mi321_09', 3)
    sprite('mi321_10', 3)
    sprite('mi321_11', 3)


@State
def SpecialShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_55 = 1

        def upon_RELEASE_C():
            if SLOT_2:
                if CheckInput(0x5f):
                    TriggerUponForState('mi400_eff', 32)
                clearUponHandler(32)
                clearUponHandler(RELEASE_C)
                clearUponHandler(EVERY_FRAME)
                sendToLabel(2)

        def upon_EVERY_FRAME():
            if SLOT_11:
                if SLOT_11 == 1:
                    if SLOT_2:
                        clearUponHandler(32)
                        clearUponHandler(RELEASE_C)
                        clearUponHandler(EVERY_FRAME)
                        clearUponHandler(STATE_END)
                        sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(RELEASE_C)
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2)

        def upon_STATE_END():
            TriggerUponForState('mi400_eff', 32)
    sprite('mi400_00', 2)
    CreateObject('mi400_effMato', -1)
    Voiceline('mi200')
    PrivateSE('mise_08')
    sprite('mi400_01', 6)
    PrivateSE('mise_08')
    sprite('mi400_02', 6)
    PrivateSE('mise_08')
    sprite('mi400_03', 6)
    PrivateSE('mise_08')
    sprite('mi400_01', 4)
    PrivateSE('mise_08')
    sprite('mi400_02', 4)
    PrivateSE('mise_08')
    sprite('mi400_03', 4)
    loopRest()
    SetActionMark(1)
    label(1)
    sprite('mi400_01', 3)
    PrivateSE('mise_08')
    sprite('mi400_02', 3)
    sprite('mi400_03', 3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('mi400_04', 4)
    clearUponHandler(32)
    clearUponHandler(RELEASE_C)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(STATE_END)
    TriggerUponForState('mi400_effMato', 33)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_0')
    sprite('mi400_05', 4)
    sprite('mi400_06', 4)
    sprite('mi400_07', 3)
    sprite('mi400_08', 3)
    sprite('mi400_09', 3)
    sprite('mi400_07', 3)
    sprite('mi400_08', 3)
    sprite('mi400_09', 3)
    sprite('mi400_07', 3)
    sprite('mi400_08', 3)
    sprite('mi400_09', 3)
    sprite('mi400_07', 3)
    sprite('mi400_08', 3)
    sprite('mi400_09', 3)
    sprite('mi400_19', 3)
    sprite('mi400_20', 3)
    sprite('mi400_21', 3)


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        AirUntechableTime(50)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(100000)
        AirPushbackY(5000)
        YImpulseBeforeWallbounce(1000)
        PushbackX(19800)
        WallbounceReboundTime(0)
        NonCornerWallbounce(1)
        NonCornerCHWallbounce(0)
        AttackDirection(0)
        FatalCounter(1)
        CHHardKnockdown(10)
        if SLOT_4:
            MoveAttributes(1, 0, 0, 0, 0)

        def upon_OPPONENT_HIT():
            CreateObject('mi401_shotei', -1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)

            def RunOnObject_11():
                AlphaValue(255)
                ConstantAlphaModifier(0)
    sprite('mi401_00', 2)
    SLOT_60 = 1
    sprite('mi401_01', 2)
    sprite('mi401_02', 3)
    AlphaValue(180)
    ConstantAlphaModifier(-30)

    def RunOnObject_11():
        AlphaValue(180)
        ConstantAlphaModifier(-30)
    sprite('mi401_03', 3)
    Voiceline('mi202')
    physicsXImpulse(50000)
    SetXCollisionFromOrigin(150)
    CreateObject('mi401_shockMato', -1)
    CommonSE('000_airdash_0')
    sprite('mi401_04', 3)
    AlphaValue(0)

    def RunOnObject_11():
        AlphaValue(0)
    DespawnEAEffect('mi401_shockMato')
    sprite('mi401_03', 3)
    sprite('mi401_05', 2)
    ConstantAlphaModifier(30)

    def RunOnObject_11():
        ConstantAlphaModifier(30)
    XImpulseAcceleration(80)
    sprite('mi401_06', 2)
    XImpulseAcceleration(80)
    sprite('mi401_07', 2)
    AlphaValue(255)

    def RunOnObject_11():
        AlphaValue(255)
    XImpulseAcceleration(80)
    sprite('mi401_08', 2)
    XImpulseAcceleration(80)
    CommonSE('004_swing_grap_1_2')
    sprite('mi401_09', 4)
    CreateObject('mi401_shotei2', -1)
    ScreenShake(10000, 10000)
    XImpulseAcceleration(0)
    SetXCollisionFromOrigin(100)
    sprite('mi401_10', 2)
    Recovery()
    sprite('mi401_11', 2)
    sprite('mi401_12', 2)
    sprite('mi401_13', 2)
    SLOT_60 = 0
    sprite('mi401_14', 2)
    sprite('mi401_15', 2)
    sprite('mi401_16', 2)
    sprite('mi401_17', 2)


@State
def AssaultLow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(15000)
        AirPushbackY(15000)
        AirUntechableTime(40)
        HardKnockdown(1)
        EnableEmergencyTechAirHit(1)
        MoveAttributes(0, 0, 1, 0, 0)
        HitLow(2)
        StarterRating(2)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)

            def RunOnObject_11():
                AlphaValue(255)
                ConstantAlphaModifier(0)
    sprite('mi401_00', 3)
    SLOT_60 = 1
    sprite('mi401_01', 3)
    sprite('mi401_02', 3)
    sprite('mi401_02', 3)
    AlphaValue(180)
    ConstantAlphaModifier(-30)

    def RunOnObject_11():
        AlphaValue(180)
        ConstantAlphaModifier(-30)
    sprite('mi401_03', 3)
    Voiceline('mi203')

    def upon_EVERY_FRAME():
        if SLOT_IsAirborne:
            if SLOT_19 <= 200000:
                physicsXImpulse(0)
            else:
                physicsXImpulse(50000)
        else:
            physicsXImpulse(50000)
    SLOT_YVelocity = SLOT_YDistanceFromFloor
    YAccel(-100)
    YAccel(5)
    SetXCollisionFromOrigin(150)
    SLOT_4 = 0
    CreateObject('mi401_shockMato', -1)
    CommonSE('000_airdash_0')
    sprite('mi401_04', 3)
    AlphaValue(0)
    DespawnEAEffect('mi401_shockMato')
    sprite('mi401_03', 3)
    clearUponHandler(EVERY_FRAME)
    physicsXImpulse(50000)
    AbsoluteY(0)
    sprite('mi401_18', 6)
    SLOT_60 = 3
    XImpulseAcceleration(80)
    ConstantAlphaModifier(30)

    def RunOnObject_11():
        ConstantAlphaModifier(30)
    CommonSE('004_swing_grap_1_2')
    sprite('mi401_19', 3)
    AlphaValue(255)

    def RunOnObject_11():
        AlphaValue(255)
    CreateObject('mi401_Gedan', -1)
    CreateObject('mi401_Gedan2', -1)
    CommonSE('213_bound_0')
    sprite('mi401_20', 3)
    sprite('mi401_19', 3)
    sprite('mi401_20', 3)
    sprite('mi401_21', 2)
    Recovery()
    DespawnEAEffect('mi401_Gedan')
    DespawnEAEffect('mi401_Gedan2')
    XImpulseAcceleration(80)
    sprite('mi401_22', 2)
    XImpulseAcceleration(80)
    SLOT_60 = 1
    sprite('mi401_23', 2)
    XImpulseAcceleration(0)
    sprite('mi401_24', 2)
    SLOT_60 = 0
    sprite('mi401_25', 2)
    sprite('mi401_26', 2)
    sprite('mi401_27', 2)
    sprite('mi401_28', 2)


@State
def ShockWave():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('mi402_00', 3)
    CreateObject('mi402_eff', -1)
    PrivateSE('mise_07')
    CommonSE('019_quake_1')
    sprite('mi402_01', 2)
    sprite('mi402_02', 2)
    sprite('mi402_03', 2)
    sprite('mi402_04', 3)
    TriggerUponForState('mi402_eff', 33)
    sprite('mi402_05', 3)
    Voiceline('mi204')
    sprite('mi402_06', 3)
    sprite('mi402_07', 3)
    sprite('mi402_08', 3)
    sprite('mi402_06', 3)
    sprite('mi402_07', 3)
    sprite('mi402_08', 3)
    Recovery()
    sprite('mi402_09', 3)
    sprite('mi406_24', 3)
    sprite('mi406_25', 3)
    sprite('mi406_26', 3)


@State
def AirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(60)
        AirPushbackY(-60000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(30)
        CHHardKnockdown(10)
        AttackDirection(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            BeginBuffer('Flying_Start')
            sendToLabel(1)

        def upon_LANDING():
            TriggerUponForState('mi403Eff', 32)

        def upon_STATE_END():
            TriggerUponForState('mi403Eff', 32)
    sprite('mi403_00', 2)
    EndMomentum(1)
    physicsXImpulse(12000)
    physicsYImpulse(10000)
    setGravity(1000)
    ForcedLandingRecovery(6, 1)
    sprite('mi403_01', 2)
    sprite('mi403_02', 3)
    sprite('mi403_03', 3)
    sprite('mi403_04', 3)
    Voiceline('mi205')
    CreateObject('mi403Eff', -1)
    PrivateSE('mise_07')
    label(0)
    sprite('mi403_05', 3)
    PerGravity(150)
    sprite('mi403_06', 3)
    sprite('mi403_07', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi403_08', 4)
    TriggerUponForState('mi403Eff', 32)
    Recovery()
    XImpulseAcceleration(-100)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    BeginBuffer('Flying_Start')
    sprite('mi403_09', 4)
    sprite('mi403_10', 4)
    sprite('mi403_11', 4)
    sprite('mi020_05', 4)
    BufferedOrPressedGoto('Flying_Start')
    sprite('mi020_06', 4)
    label(2)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(2)


@State
def Barrier_On():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('mi404_00', 4)
    sprite('mi404_01', 4)
    sprite('mi404_02', 4)
    Voiceline('mi209')
    if SLOT_7:
        ObjectUpon2(11, 1404, 0)
    else:
        ObjectUpon2(11, 404, 0)
    sprite('mi404_03', 4)
    sprite('mi404_04', 4)
    CreateObject('mi404_eff', -1)
    PrivateSE('mise_11')
    PrivateSE('mise_11')

    def upon_EVERY_FRAME():
        if SLOT_136 <= 0:
            setInvincible(0)
            SLOT_6 = 0
            clearUponHandler(EVERY_FRAME)
    BarrierGaugeOnCall(-2000, 120)
    sprite('mi404_05', 4)
    sprite('mi404_06', 4)
    sprite('mi404_04', 4)
    sprite('mi404_05', 4)
    sprite('mi404_06', 4)
    sprite('mi404_07', 3)
    sprite('mi404_08', 3)


@State
def Barrier_Off():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(950)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        Hitstop(4)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(36000)
        StrikeProjectileLevel(0)
        ProjectileLevel(2)
        MoveAttributes(0, 0, 0, 1, 0)
        StarterRating(0)

        def upon_OPPONENT_HIT():
            BarrierGaugeOnCall(1000, 0)
        SLOT_6 = 0
        setInvincible(1)
    sprite('mi405_00', 2)
    sprite('mi405_01', 2)
    sprite('mi405_02', 2)
    sprite('mi405_03', 2)
    Voiceline('mi210')
    sprite('mi405_04', 3)
    CreateParticle('mief404_endaura', -1)
    CreateObject('mi404_effImp2', -1)
    ScreenShake(10000, 10000)
    PrivateSE('mise_12')
    sprite('mi405_05', 4)
    sprite('mi405_06', 4)
    clearUponHandler(EVERY_FRAME)
    setInvincible(0)
    sprite('mi405_07', 4)
    sprite('mi405_05ex', 4)
    sprite('mi405_06ex', 4)
    sprite('mi405_07ex', 4)
    sprite('mi405_08', 3)
    sprite('mi405_09', 3)


@State
def DrainThrow():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('DrainThrowExe', 2, 1, 0)
        else:
            AttackDefaults_Throw('DrainThrowExe', 2, 0, 0)
        RangeCheck(120000)
        DistanceCheck(250000, 1, 100000, -100000)
        if SLOT_11:
            AttackOff()
        EndMomentum(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
        SLOT_6 = 0
        setInvincible(0)
    sprite('mi406_00', 2)
    sprite('mi406_01', 2)
    sprite('mi406_02', 2)
    sprite('mi406_03', 3)
    sprite('mi406_04', 3)
    sprite('mi406_05', 3)
    sprite('mi406_06', 3)
    sprite('mi406_07', 3)
    CommonSE('010_swing_sword_0')
    sprite('mi406_08', 4)
    sprite('mi406_09', 4)
    Voiceline('mi155')
    sprite('mi400_15', 4)
    sprite('mi400_16', 4)
    sprite('mi400_17', 4)
    sprite('mi400_18', 4)
    sprite('mi400_19', 4)
    sprite('mi400_20', 3)
    sprite('mi400_21', 3)


@State
def DrainThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(100)
        AirPushbackX(12000)
        AirPushbackY(30000)
        YImpulseBeforeWallbounce(1600)
        Hitstop(4)
        UseSlashHitspark(1)
        OppPositionOnHit(1, 110000, -1)
        StarterRating(2)

        def upon_OPPONENT_HIT():
            HPManipulationNoKill(500)
            if not SLOT_136 == 0:
                BarrierGaugeOnCall(3000, 0)

            def RunOnObject_22():
                BarrierGaugeOnCall(-2000, 0)
        SLOT_6 = 0
        StayAfterMovement(1, 0)
    sprite('mi406_05', 4)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi406_10', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi406_11', 10)
    Voiceline('mi206')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi406_12', 5)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi406_13', 5)
    OppThrowAnimation(11, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    SLOT_60 = 1
    sprite('mi406_14', 5)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_15', 5)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_16', 5)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_16ex1', 5)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_16ex2', 24)
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_17', 2)
    Voiceline('mi207')
    OppThrowAnimation(12, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('mi406_18', 2)
    CreateObject('mi406_Kyuketu', -1)
    RefreshMultihit()
    SLOT_60 = 0
    PrivateSE('mise_09')
    sprite('mi406_19', 2)
    sprite('mi406_20', 8)
    sprite('mi406_21', 8)
    sprite('mi406_22', 4)
    sprite('mi406_23', 4)
    sprite('mi406_24', 4)
    sprite('mi406_25', 4)
    sprite('mi406_26', 4)


@State
def ShotLaser():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('mi407_00', 4)
    sprite('mi407_01', 4)
    callSubroutine('FuncLaser')
    sprite('mi407_02', 4)
    sprite('mi407_03', 3)
    sprite('mi407_04', 3)
    sprite('mi407_05', 3)
    sprite('mi407_06', 3)
    sprite('mi407_07', 3)
    sprite('mi407_08', 3)
    sprite('mi407_10', 3)
    sprite('mi407_11', 3)


@State
def ShotSaws():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_33 = 150
    sprite('mi408_00', 3)
    sprite('mi408_01', 3)
    sprite('mi408_02', 3)
    sprite('mi408_03', 3)
    sprite('mi408_04', 3)
    callSubroutine('FuncSaws')
    sprite('mi408_05', 3)
    sprite('mi408_06', 3)
    sprite('mi408_07', 3)
    sprite('mi408_08', 3)
    sprite('mi408_09', 3)
    sprite('mi408_10', 3)
    sprite('mi408_07', 3)
    sprite('mi408_08', 3)
    sprite('mi408_09', 3)
    sprite('mi408_10', 3)
    sprite('mi408_07', 4)
    sprite('mi408_08', 4)
    sprite('mi408_09', 4)
    sprite('mi408_10', 4)
    sprite('mi408_11', 3)
    sprite('mi408_12', 3)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(999)
        Crumple(999)
        Hitstun(999)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        if SLOT_4:
            AirPushbackX(30000)
            AirHitstunAnimation(5)
            Restand(1)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)
        SLOT_57 = 1
        SLOT_58 = 1

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            callSubroutine('DeleteFunnel')
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
            if SLOT_11:
                StopTimestopEffect('')
                PaletteIndex(0)
                StopClock(0)
                SLOT_11 = 0
                callSubroutine('Funnel_PalletModori')
                Unknown23169(0)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        RunLoopUpon(17, 3)

        def upon_17():
            TriggerUponForState('Funnel4D', 41)
            TriggerUponForState('Funnel6D', 41)
            TriggerUponForState('Funnel2D', 41)
    sprite('mi040_00ex01', 3)
    E0EAEffect('BurstDDeff', 103)
    sprite('mi040_01ex01', 3)
    sprite('mi040_02ex01', 3)
    sprite('mi312_00', 5)
    CommonSE('004_swing_grap_1_1')
    sprite('mi440_00', 2)
    sprite('mi440_00', 3)
    physicsXImpulse(30000)
    Voiceline('mi280')
    sprite('mi440_01', 3)
    physicsXImpulse(0)
    sprite('mi440_02', 4)
    setInvincible(0)
    sprite('mi440_03', 4)
    sprite('mi440_04', 4)
    sprite('mi312_06ex01', 4)
    sprite('mi312_07ex01', 4)
    sprite('mi312_08ex01', 5)
    sprite('mi312_09ex01', 5)
    sprite('mi312_10ex01', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(999)
        Crumple(999)
        Hitstun(999)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 250000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        if SLOT_4:
            AirPushbackX(30000)
            AirHitstunAnimation(5)
            Restand(1)
        setInvincible(1)
        EndMomentum(1)
        StayAfterMovement(1, 0)
        SLOT_57 = 1
        SLOT_58 = 1

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            callSubroutine('DeleteFunnel')
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
            if SLOT_11:
                StopTimestopEffect('')
                PaletteIndex(0)
                StopClock(0)
                SLOT_11 = 0
                callSubroutine('Funnel_PalletModori')
                Unknown23169(0)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('mi040_00ex01', 1)
    E0EAEffect('BurstDDeff', 103)
    sprite('mi040_01ex01', 1)
    sprite('mi040_02ex01', 1)
    sprite('mi312_00', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('mi440_00', 3)
    physicsXImpulse(30000)
    Voiceline('mi280')
    sprite('mi440_01', 3)
    physicsXImpulse(0)
    sprite('mi440_02', 4)
    setInvincible(0)
    sprite('mi440_03', 4)
    sprite('mi440_04', 4)
    sprite('mi312_06ex01', 4)
    sprite('mi312_07ex01', 4)
    sprite('mi312_08ex01', 5)
    sprite('mi312_09ex01', 5)
    sprite('mi312_10ex01', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(2400)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(30)
        Crumple(9999)
        Hitstop(0)
        PushbackX(12000)
        HitsparkSize(0)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDDAdd')
        DefeatOpponentBehavior(0)
        MinimumDamage(10)
        AttackOff()
        if SLOT_51:
            Damage(5100)
        SLOT_57 = 1
        CameraNoScreenCollision(1)
        SetBackground(1)
        SLOT_6 = 0
    sprite('mi440_01', 2)
    sprite('mi440_02', 2)
    sprite('mi440_03', 2)
    sprite('mi440_04', 4)
    sprite('mi312_06ex01', 4)
    sprite('mi312_07ex01', 4)
    sprite('mi312_08ex01', 4)
    sprite('mi312_09ex01', 4)
    sprite('mi312_10ex01', 3)
    sprite('mi312_10ex01', 1)
    if not SLOT_4:
        if SLOT_51:
            sendToLabel(100)
        else:
            sendToLabel(0)
    loopRest()
    sprite('mi023_00', 2)
    SLOT_4 = 0
    EndYPhysicsImpulse()

    def upon_LANDING():
        if SLOT_51:
            sendToLabel(100)
        else:
            sendToLabel(0)
    sprite('mi023_01', 2)
    sprite('mi020_02', 3)
    sprite('mi020_03', 3)
    sprite('mi020_04', 3)
    sprite('mi020_05', 4)
    sprite('mi020_06', 4)
    label(1)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    PerGravity(110)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('mi400_11ex01', 6)
    CreateObject('mi440_Camera', -1)
    CreateObject('mi440_juso', -1)
    PrivateSE('mise_12')
    sprite('mi400_12ex01', 6)
    sprite('mi400_13ex01', 6)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    TriggerUponForState('mi440_juso', 32)
    CreateObject('mi440_Gaikotu', -1)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_15ex01', 3)
    sprite('mi400_16ex01', 3)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi400_17ex01', 3)
    sprite('mi440_07', 30)
    HUDVisibillity(1)
    ScreenShake(7500, 7500)
    CreateObject('mi440_BlackBG', -1)
    TriggerUponForState('mi440_Camera', 32)

    def RunOnObject_22():
        StopCharacterFlash1(-1)
        PreventSelfPush(1)
        EndSprite(1)
    TriggerUponForState('mi440_Gaikotu', 32)
    sprite('mi440_08', 6)
    physicsXImpulse(2000)
    sprite('mi440_09', 6)
    XImpulseAcceleration(200)
    sprite('mi440_10', 8)
    XImpulseAcceleration(300)
    sprite('mi440_11', 8)
    XImpulseAcceleration(400)
    Voiceline('mi281')
    sprite('mi440_12', 4)
    XImpulseAcceleration(0)
    ScreenShake(30000, 10000)
    CommonSE('103_hit_counter_slash_0')
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_16', 14)
    CreateObject('mi440_Blood', -1)
    ScreenShake(6000, 5000)
    CommonSE('020_blood_1')
    CommonSE('101_hit_slash_1')
    sprite('mi440_17', 8)
    physicsXImpulse(-2500)
    sprite('mi440_18', 6)
    sprite('mi440_19', 4)
    XImpulseAcceleration(0)
    sprite('mi440_20', 20)
    sprite('mi440_21', 4)
    sprite('mi406_18ex01', 4)
    sprite('mi406_19ex01', 10)
    SetInertia(-20000)
    RefreshMultihit()
    HUDVisibillity(0)
    DespawnEAEffect('mi440_Gaikotu')
    DespawnEAEffect('mi440_GaikotuSotoba')
    CreateObject('mi440_Flash', -1)
    CreateObject('mi440_BloodBig', -1)
    ScreenShake(20000, 20000)
    StopCharacterFlash1(0)

    def RunOnObject_22():
        StopCharacterFlash1(0)
    DespawnEAEffect('mi440_juso')
    TriggerUponForState('mi440_BlackBG', 32)
    CommonSE('025_cleanhit_slash')
    sprite('mi406_20ex01', 10)
    Voiceline('mi282')
    sprite('mi406_21ex01', 10)
    TriggerUponForState('mi440_Camera', 33)
    TriggerUponForState('mi440_BloodBig', 32)
    TriggerUponForState('mi440_BloodBigEX', 32)
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('mi400_11ex01', 6)
    CreateObject('mi440_Camera', -1)
    CreateObject('mi440_juso', -1)
    sprite('mi400_12ex01', 6)
    sprite('mi400_13ex01', 6)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    TriggerUponForState('mi440_juso', 32)
    CreateObject('mi440_GaikotuEx', -1)
    CreateObject('mi440_GaikotuSotoba', -1)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_14ex01', 4)
    sprite('mi440_05', 4)
    sprite('mi440_06', 4)
    sprite('mi400_15ex01', 3)
    sprite('mi400_16ex01', 3)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi400_17ex01', 3)
    sprite('mi440_07', 30)
    HUDVisibillity(1)
    ScreenShake(7500, 7500)
    CreateObject('mi440_BlackBG', -1)
    TriggerUponForState('mi440_Camera', 32)

    def RunOnObject_22():
        StopCharacterFlash1(-1)
        PreventSelfPush(1)
        EndSprite(1)
    TriggerUponForState('mi440_GaikotuEx', 32)
    TriggerUponForState('mi440_GaikotuSotoba', 32)
    sprite('mi440_08', 6)
    physicsXImpulse(2000)
    sprite('mi440_09', 6)
    XImpulseAcceleration(200)
    sprite('mi440_10', 8)
    XImpulseAcceleration(300)
    sprite('mi440_11', 8)
    Voiceline('mi281')
    XImpulseAcceleration(400)
    sprite('mi440_12', 4)
    XImpulseAcceleration(0)
    ScreenShake(30000, 10000)
    CommonSE('103_hit_counter_slash_0')
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_13', 6)
    sprite('mi440_14', 6)
    sprite('mi440_15', 6)
    sprite('mi440_16', 4)
    CreateObject('mi440_Blood', -1)
    ScreenShake(6000, 5000)
    CommonSE('020_blood_1')
    CommonSE('101_hit_slash_1')
    sprite('mi440_17', 4)
    physicsXImpulse(-5000)
    sprite('mi440_18', 4)
    XImpulseAcceleration(200)
    CreateObject('mi440_Juwa', -1)
    TriggerUponForState('mi440_GaikotuEx', 33)
    TriggerUponForState('mi440_GaikotuSotoba', 33)
    StopCharacterFlash1(0)
    ColorForTransition(4278190080)

    def RunOnObject_22():
        StopCharacterFlash1(0)
        ColorForTransition(4278190080)
    sprite('mi440_19', 4)
    XImpulseAcceleration(50)
    sprite('mi440_20', 4)
    XImpulseAcceleration(50)
    sprite('mi440_21', 4)
    XImpulseAcceleration(50)
    sprite('mi406_18ex01', 20)
    XImpulseAcceleration(0)
    sprite('mi406_19ex01', 10)
    ColorTransition(4294967295, 20)
    SetInertia(-20000)
    RefreshMultihit()
    HUDVisibillity(0)
    DespawnEAEffect('mi440_GaikotuEx')
    DespawnEAEffect('mi440_GaikotuSotoba')
    CreateObject('mi440_Flash', -1)
    CreateObject('mi440_BloodBigEX', -1)
    ScreenShake(20000, 20000)
    DespawnEAEffect('mi440_juso')
    TriggerUponForState('mi440_BlackBG', 32)
    CommonSE('025_cleanhit_slash')
    sprite('mi406_20ex01', 10)
    Voiceline('mi282')
    sprite('mi406_21ex01', 10)
    TriggerUponForState('mi440_Camera', 33)
    TriggerUponForState('mi440_BloodBig', 32)
    TriggerUponForState('mi440_BloodBigEX', 32)
    loopRest()
    gotoLabel(9)
    label(9)
    sprite('mi406_22ex01', 8)
    sprite('mi406_23ex01', 8)
    sprite('mi406_24ex01', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi406_25ex01', 6)
    TriggerUponForState('mi440_Juwa', 32)
    sprite('mi406_26ex01', 4)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(800)
        AttackP2(72)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(1000)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(80)
        Hitstop(20)
        OppPositionOnHit(1, 150000, 10000)
        OnlyHitPlayer(1)
        OppMovementUnlock(1)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        DamageFromStateOnly('UltimateAssaultAdd')
        if SLOT_4:
            MoveAttributes(1, 0, 0, 0, 0)
        SLOT_58 = 1

        def upon_OPPONENT_HIT():
            if SLOT_21:
                EnableAfterimage(0)
                CameraControlEnable(1)
                SetActionMark(1)
                EnableCollision(0)
                if SLOT_11:
                    StopTimestopEffect('')
                    PaletteIndex(0)
                    StopClock(0)
                    SLOT_11 = 0
                    callSubroutine('Funnel_PalletModori')
                    Unknown23169(0)
                EnableRapidCancel(0)
    sprite('mi430_00', 3)
    setInvincible(1)
    sprite('mi430_01', 3)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    Voiceline('mi261')
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_01', 3)
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_01', 3)
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_04', 3)
    physicsXImpulse(4000)
    sprite('mi430_05', 3)
    XImpulseAcceleration(600)
    CommonSE('004_swing_grap_1_2')
    PrivateSE('mise_04')
    sprite('mi430_06', 4)
    CreateObject('mi430_KickEff', -1)
    EndMomentum(1)
    sprite('mi430_07', 4)
    if not SLOT_2:
        setInvincible(0)
    sprite('mi430_08', 4)
    if SLOT_2:
        enterState('UltimateAssaultAdd')
    sprite('mi430_09', 6)
    sprite('mi430_10', 6)
    sprite('mi430_01', 6)
    sprite('mi430_00', 6)


@State
def UltimateAssaultAdd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(500)
        AirUntechableTime(80)
        Hitstop(5)
        EnemyHitstopAddition(0, 8, 8)
        OppPositionOnHit(1, 250000, -50000)
        CHStateIfCHStart(3)
        AttackDirection(0)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('UltimateAssaultAdd')
        HitAnywhere(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_OPPONENT_HIT():
            ScreenShake(5000, 5000)
            CreateObject('mi430_HitEff', 101)
            HUDVisibillity(1)
        SLOT_4 = 0
        SetXCollisionFromOrigin(40)
        HitBackReturnObject(0)
        CameraLookAtEnemy(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        SLOT_57 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            HUDVisibillity(0)
        SLOT_6 = 0
        DespawnEAEffect('Funnel_Mhoujin')
    sprite('mi430_08', 20)
    CreateObject('mi430_Sand', -1)
    CommonSE('000_airdash_0')
    sprite('mi231_02ex00', 10)
    AlphaValue(255)
    AddX(310000)
    AddY(1000000)
    ForceFaceSprite()
    sprite('mi231_03ex00', 5)
    sprite('mi231_04ex00', 5)
    RefreshMultihit()
    Voiceline('mi258')
    sprite('mi231_05ex00', 20)
    CreateObject('mi430_Sand2', -1)
    CommonSE('000_airdash_0')
    sprite('mi231_02ex00', 10)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(1000000)
    ForceFaceSprite()
    HUDVisibillity(0)
    sprite('mi231_02ex00', 5)
    sprite('mi231_03ex00', 5)
    sprite('mi231_04ex00', 5)
    RefreshMultihit()
    AirPushbackX(-60000)
    FlipOnHit(1)
    sprite('mi231_05ex00', 20)
    CreateObject('mi430_Sand2', -1)
    CommonSE('000_airdash_0')
    sprite('mi430_11', 5)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(1200000)
    AddY(90000)
    ForceFaceSprite()
    HUDVisibillity(0)
    sprite('mi430_11', 5)
    physicsXImpulse(-8000)
    SetAcceleration(2000)
    physicsYImpulse(8000)
    setGravity(2000)
    sprite('mi430_11', 3)
    sprite('mi430_12', 3)
    sprite('mi430_13', 3)
    sprite('mi430_14', 1)
    clearUponHandler(OPPONENT_HIT)
    EnableRapidCancel(0)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    OppPositionOnHit(0, 0, 0)
    sprite('mi430_14', 3)
    clearUponHandler(OPPONENT_HIT)
    RefreshMultihit()
    DamageFromStateOnly('UltimateAssaultExe')
    AttackDefaults_Throw('UltimateAssaultExe', 3, 0, 0)
    DistanceCheck(-1, -1, -1, -1)
    RangeCheck(-1)
    ThrowTechWindow(-1)
    PreventAirborneHit(0)
    DoNotHitKnockedDownOpp(0)
    loopRest()


@State
def UltimateAssaultExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        ThrowTechWindow(-1)
        AttackLevel_(4)
        Damage(2500)
        MinimumDamage(20)
        AttackP2(100)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        WallbounceReboundTime(0)
        AirPushbackX(50000)
        AirPushbackY(10000)
        AirUntechableTime(80)
        Hitstop(20)
        CHStateIfCHStart(3)
        OppPositionOnHit(1, 120000, 100000)
        OnlyHitPlayer(1)
        setInvincible(1)
        clearUponHandler(LANDING)

        def upon_LANDING():
            sendToLabel(1)
            ScreenShake(5000, 40000)
            KnockdownEffects(100, 1, 1)
            physicsXImpulse(40000)
            SetAcceleration(-1000)
            YAccel(0)
            CameraFast(0)
        CameraLookAtEnemy(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        CameraFast(1)
        CameraPosition(850)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        SLOT_57 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            HUDVisibillity(0)
    sprite('mi430_14', 3)
    StartMultihit()
    physicsXImpulse(11250)
    physicsYImpulse(-45000)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    label(0)
    sprite('mi430_15', 2)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_16', 2)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi430_17', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    OppThrowAnimation(14, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('209_down_normal_1')
    CommonSE('100_hit_grap_3')
    sprite('mi430_18', 3)
    OppThrowAnimation(15, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_19', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('213_bound_0')
    sprite('mi430_20', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('213_bound_1')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('209_down_normal_0')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CameraPosition(1000)
    CommonSE('209_down_normal_1')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_24', 3)
    EndMomentum(1)
    physicsXImpulse(0)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('002_highjump_1')
    sprite('mi430_25', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_26', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_27', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_28', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('mi430_HitEff2', -1)
    sprite('mi430_29', 3)
    Voiceline('mi259')
    YAccel(0)
    PerGravity(50)
    CameraNoScreenCollision(0)
    CameraControlEnable(0)
    uponSendToLabel(LANDING, 9)
    CommonSE('025_cleanhit_grap')
    HUDVisibillity(1)
    sprite('mi430_30', 3)
    HUDVisibillity(0)
    sprite('mi430_31', 3)
    sprite('mi321_10', 3)
    sprite('mi321_11', 3)
    sprite('mi020_04', 4)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    CreateObject('mi408_CreateEff', -1)
    SLOT_57 = 0
    sprite('mi020_05', 4)
    sprite('mi020_06', 4)
    label(2)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('mi024_00', 4)
    LandingEffects(100, 1, 1)
    sprite('mi024_01', 4)
    sprite('mi024_02', 4)
    sprite('mi024_03', 4)
    sprite('mi024_04', 4)
    sprite('mi024_05', 4)


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(800)
        AttackP2(72)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(1000)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(80)
        Hitstop(20)
        OppPositionOnHit(1, 150000, 10000)
        OnlyHitPlayer(1)
        OppMovementUnlock(1)
        AttackType(4)
        DefeatOpponentBehavior(1)
        StarterRating(2)
        DamageFromStateOnly('UltimateAssaultAdd_OD')
        if SLOT_4:
            MoveAttributes(1, 0, 0, 0, 0)
        SLOT_58 = 1

        def upon_OPPONENT_HIT():
            if SLOT_21:
                EnableAfterimage(0)
                CameraControlEnable(1)
                SetActionMark(1)
                EnableCollision(0)
                if SLOT_11:
                    StopTimestopEffect('')
                    PaletteIndex(0)
                    StopClock(0)
                    SLOT_11 = 0
                    callSubroutine('Funnel_PalletModori')
                    Unknown23169(0)
                EnableRapidCancel(0)
    sprite('mi430_00', 3)
    setInvincible(1)
    sprite('mi430_01', 3)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    Voiceline('mi261')
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_01', 3)
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_01', 3)
    sprite('mi430_02', 3)
    sprite('mi430_03', 3)
    sprite('mi430_04', 3)
    physicsXImpulse(4000)
    sprite('mi430_05', 3)
    XImpulseAcceleration(600)
    CommonSE('004_swing_grap_1_2')
    PrivateSE('mise_04')
    sprite('mi430_06', 4)
    CreateObject('mi430_KickEff', -1)
    EndMomentum(1)
    sprite('mi430_07', 4)
    if not SLOT_2:
        setInvincible(0)
    sprite('mi430_08', 4)
    if not SLOT_11:
        if SLOT_2:
            enterState('UltimateAssaultAdd_OD')
    sprite('mi430_09', 6)
    sprite('mi430_10', 6)
    sprite('mi430_01', 6)
    sprite('mi430_00', 6)


@State
def UltimateAssaultAdd_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(100)
        AirUntechableTime(80)
        Hitstop(5)
        EnemyHitstopAddition(0, 8, 8)
        OppPositionOnHit(1, 250000, -50000)
        CHStateIfCHStart(3)
        AttackDirection(0)
        OnlyHitPlayer(1)
        AttackType(4)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('UltimateAssaultAdd_OD')
        HitAnywhere(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_OPPONENT_HIT():
            ScreenShake(5000, 5000)
            CreateObject('mi430_HitEff', 101)
            HUDVisibillity(1)
        SLOT_4 = 0
        SetXCollisionFromOrigin(40)
        HitBackReturnObject(0)
        CameraLookAtEnemy(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        SLOT_57 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            HUDVisibillity(0)
        SLOT_6 = 0
        DespawnEAEffect('Funnel_Mhoujin')
    sprite('mi430_08', 20)
    CreateObject('mi430_Sand', -1)
    CommonSE('000_airdash_0')
    sprite('mi231_02ex00', 5)
    AlphaValue(255)
    AddX(310000)
    AddY(1000000)
    ForceFaceSprite()
    Voiceline('mi250')
    sprite('mi231_02ex00', 5)
    sprite('mi231_03ex00', 5)
    sprite('mi231_04ex00', 5)
    RefreshMultihit()
    sprite('mi231_05ex00', 20)
    CreateObject('mi430_Sand2', -1)
    CommonSE('000_airdash_0')
    sprite('mi252_03ex00', 13)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(1000000)
    ForceFaceSprite()
    HUDVisibillity(0)
    sprite('mi252_04ex00', 5)
    RefreshMultihit()
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    AirPushbackX(30000)
    AirPushbackY(-30000)
    YImpulseBeforeWallbounce(0)
    HardKnockdown(1)
    OppPositionOnHit(1, 200000, 50000)
    sprite('mi252_05ex00', 3)
    sprite('mi252_06ex00', 20)
    CreateObject('mi430_Sand3', -1)
    CommonSE('000_airdash_0')
    sprite('mi201_01ex00', 8)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(800000)
    AddY(-600000)
    ForceFaceSprite()
    Voiceline('mi251')
    HUDVisibillity(0)
    sprite('mi201_02ex00', 3)
    sprite('mi201_03ex00', 3)
    sprite('mi201_04ex00', 5)
    RefreshMultihit()
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(70000)
    AirPushbackY(8000)
    YImpulseBeforeWallbounce(500)
    OppPositionOnHit(1, 250000, 100000)
    sprite('mi201_05ex00', 20)
    CreateObject('mi430_Sand4', -1)
    CommonSE('000_airdash_0')
    sprite('mi212_02', 8)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(1300000)
    AddY(-170000)
    ForceFaceSprite()
    HUDVisibillity(0)
    sprite('mi212_03', 3)
    sprite('mi212_04', 3)
    sprite('mi212_05', 3)
    Voiceline('mi252')
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(50000)
    AirPushbackY(50000)
    OppPositionOnHit(1, 150000, 0)
    sprite('mi212_06', 3)
    sprite('mi212_07', 20)
    CreateObject('mi430_Sand5', -1)
    CommonSE('000_airdash_0')
    sprite('mi430_11', 5)
    AlphaValue(255)
    TeleportToObject(22)
    AddX(1200000)
    AddY(900000)
    ForceFaceSprite()
    HUDVisibillity(0)
    sprite('mi430_11', 5)
    physicsXImpulse(-8000)
    SetAcceleration(2000)
    physicsYImpulse(8000)
    setGravity(2000)
    sprite('mi430_11', 3)
    sprite('mi430_12', 3)
    sprite('mi430_13', 3)
    sprite('mi430_14', 1)
    Voiceline('mi253')
    clearUponHandler(OPPONENT_HIT)
    EnableRapidCancel(0)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    OppPositionOnHit(0, 0, 0)
    sprite('mi430_14', 3)
    RefreshMultihit()
    DamageFromStateOnly('UltimateAssaultExe_OD')
    AttackDefaults_Throw('UltimateAssaultExe_OD', 3, 0, 0)
    DistanceCheck(-1, -1, -1, -1)
    RangeCheck(-1)
    ThrowTechWindow(-1)
    PreventAirborneHit(0)
    DoNotHitKnockedDownOpp(0)
    loopRest()


@State
def UltimateAssaultExe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        ThrowTechWindow(-1)
        AttackLevel_(4)
        Damage(2800)
        MinimumDamage(20)
        AttackP2(100)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        WallbounceReboundTime(0)
        AirPushbackX(50000)
        AirPushbackY(10000)
        AirUntechableTime(80)
        Hitstop(20)
        CHStateIfCHStart(3)
        OppPositionOnHit(1, 120000, 100000)
        AttackType(4)
        OnlyHitPlayer(1)
        setInvincible(1)
        clearUponHandler(LANDING)

        def upon_LANDING():
            sendToLabel(1)
            ScreenShake(5000, 40000)
            KnockdownEffects(100, 1, 1)
            physicsXImpulse(60000)
            SetAcceleration(-1500)
            YAccel(0)
            CameraFast(0)
        CameraLookAtEnemy(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        CameraFast(1)
        CameraPosition(850)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        SLOT_57 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            HUDVisibillity(0)
    sprite('mi430_14', 3)
    StartMultihit()
    physicsXImpulse(11250)
    physicsYImpulse(-45000)
    EndYPhysicsImpulse()
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    label(0)
    sprite('mi430_15', 2)
    PerGravity(120)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_16', 2)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi430_17', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    OppThrowAnimation(14, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('209_down_normal_1')
    CommonSE('100_hit_grap_3')
    sprite('mi430_18', 3)
    OppThrowAnimation(15, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_19', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('213_bound_0')
    sprite('mi430_20', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('213_bound_1')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('209_down_normal_0')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('209_down_normal_1')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('209_down_normal_0')
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_21', 3)
    AddCombo(1)
    CreateObject('mi430_Smoke', -1)
    CommonSE('209_down_normal_1')
    CameraPosition(1000)
    sprite('mi430_22', 3)
    sprite('mi430_23', 3)
    sprite('mi430_24', 3)
    EndMomentum(1)
    physicsXImpulse(0)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('002_highjump_1')
    sprite('mi430_25', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_26', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_27', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('mi430_28', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('mi430_HitEff2', -1)
    sprite('mi430_29', 3)
    Voiceline('mi254')
    YAccel(0)
    PerGravity(50)
    CameraNoScreenCollision(0)
    CameraControlEnable(0)
    uponSendToLabel(LANDING, 9)
    CommonSE('025_cleanhit_grap')
    HUDVisibillity(1)
    sprite('mi430_30', 3)
    HUDVisibillity(0)
    sprite('mi430_31', 3)
    sprite('mi321_10', 3)
    sprite('mi321_11', 3)
    sprite('mi020_04', 4)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    CreateObject('mi408_CreateEff', -1)
    SLOT_57 = 0
    sprite('mi020_05', 4)
    sprite('mi020_06', 4)
    label(2)
    sprite('mi020_07', 4)
    sprite('mi020_08', 4)
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('mi024_00', 4)
    LandingEffects(100, 1, 1)
    sprite('mi024_01', 4)
    sprite('mi024_02', 4)
    sprite('mi024_03', 4)
    sprite('mi024_04', 4)
    sprite('mi024_05', 4)


@State
def UltimateTimeStopThrow():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('UltimateTimeStopThrowExe', 3, 1, 0)
        else:
            AttackDefaults_Throw('UltimateTimeStopThrowExe', 3, 0, 0)
        RangeCheck(120000)
        DistanceCheck(250000, 1, 150000, -150000)
        if SLOT_11:
            ThrowTechWindow(-1)
        AttackOff()
        EndMomentum(1)
        StayAfterMovement(1, 0)
        if SLOT_7:
            ObjectUpon2(11, 1431, 0)
        else:
            ObjectUpon2(11, 431, 0)
        SLOT_57 = 1
        SLOT_58 = 1
        callSubroutine('DeleteFunnel')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
    sprite('mi431_00', 6)
    sprite('mi431_01', 6)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('mi431_02', 6)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    SLOT_56 = 1
    setInvincible(0)
    RefreshMultihit()
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    SLOT_56 = 0
    AttackOff()
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_22', 4)
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi431_23', 4)
    sprite('mi431_24', 4)
    sprite('mi431_25', 4)
    sprite('mi431_26', 4)
    sprite('mi431_27', 4)
    SetInertia(-10000)
    TriggerUponForState('FunnelTimeStopThrow', 32)
    TriggerUponForState('FunnelTimeStopThrow_Open', 32)
    sprite('mi431_28', 4)
    sprite('mi431_29', 4)
    sprite('mi431_30', 4)
    sprite('mi431_31', 4)
    sprite('mi431_32', 4)


@State
def UltimateTimeStopThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(0)
        Damage(150)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(0)
        PushbackX(0)
        Stagger(100)
        Crumple(100)
        AirUntechableTime(100)
        HitAnywhere(1)
        DamageEffect(8, '')
        ShutUp(1)
        EnemyHitstopAddition(0, 9999, 9999)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('UltimateTimeStopThrowExe')
        OnlyHitPlayer(1)
        StarterRating(0)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
        CameraLookAtEnemy(1)
        callSubroutine('DeleteFunnel')
        SLOT_57 = 1
        SLOT_58 = 1
    sprite('mi431_03', 4)
    AttackOff()
    OppThrowAnimation(17, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    Voiceline('mi257')
    sprite('mi431_06', 8)
    CreateObject('mi431_KyushuSoul', 0)
    RefreshMultihit()
    physicsXImpulse(-4000)
    PrivateSE('mise_13')
    sprite('mi431_07', 8)
    XImpulseAcceleration(200)
    SetAcceleration(300)
    sprite('mi431_08', 8)
    sprite('mi431_09', 6)
    XImpulseAcceleration(-50)
    sprite('mi431_10', 6)
    sprite('mi431_11', 4)
    XImpulseAcceleration(250)
    SetAcceleration(-300)
    AddX(150000)
    SetBackground(2)
    EnableCollision(0)
    sprite('mi431_12', 4)
    if SLOT_XDistanceFromFowardCorner <= 160000:

        def RunOnObject_22():
            AddX(110000)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    RefreshMultihit()
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        if SLOT_21:
            TimestopEffect('')
            SLOT_11 = SLOT_11 + 180
            PaletteIndex(2)
            callSubroutine('Funnel_PalletChange')
            SetBackground(0)

    def upon_STATE_END():
        ForceFaceSprite()
    PrivateSE('mise_14')
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    TriggerUponForState('FunnelTimeStopThrow', 33)
    TriggerUponForState('FunnelTimeStopThrow_Open', 33)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    CameraLookAtEnemy(0)
    physicsXImpulse(3000)
    sprite('mi431_16', 5)
    sprite('mi431_17', 5)
    TriggerUponForState('FunnelTimeStopThrow', 34)
    TriggerUponForState('FunnelTimeStopThrow_Open', 34)
    sprite('mi431_18', 5)
    sprite('mi431_19', 5)
    sprite('mi431_20', 5)
    physicsXImpulse(0)
    sprite('mi431_21', 5)


@State
def UltimateTimeStopThrow_OD():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('UltimateTimeStopThrowExe_OD', 3, 1, 0)
        else:
            AttackDefaults_Throw('UltimateTimeStopThrowExe_OD', 3, 0, 0)
        AttackType(4)
        RangeCheck(120000)
        DistanceCheck(250000, 1, 150000, -150000)
        if SLOT_11:
            ThrowTechWindow(-1)
        AttackOff()
        EndMomentum(1)
        StayAfterMovement(1, 0)
        if SLOT_7:
            ObjectUpon2(11, 1431, 0)
        else:
            ObjectUpon2(11, 431, 0)
        SLOT_57 = 1
        SLOT_58 = 1
        callSubroutine('DeleteFunnel')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
    sprite('mi431_00', 6)
    sprite('mi431_01', 6)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('mi431_02', 6)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    SLOT_56 = 1
    setInvincible(0)
    RefreshMultihit()
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    SLOT_56 = 0
    AttackOff()
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_22', 4)
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi431_23', 4)
    sprite('mi431_24', 4)
    sprite('mi431_25', 4)
    sprite('mi431_26', 4)
    sprite('mi431_27', 4)
    SetInertia(-10000)
    TriggerUponForState('FunnelTimeStopThrow', 32)
    TriggerUponForState('FunnelTimeStopThrow_Open', 32)
    sprite('mi431_28', 4)
    sprite('mi431_29', 4)
    sprite('mi431_30', 4)
    sprite('mi431_31', 4)
    sprite('mi431_32', 4)


@State
def UltimateTimeStopThrowExe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(0)
        Damage(250)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(0)
        PushbackX(0)
        Stagger(100)
        Crumple(100)
        AirUntechableTime(100)
        HitAnywhere(1)
        DamageEffect(8, '')
        ShutUp(1)
        EnemyHitstopAddition(0, 9999, 9999)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('UltimateTimeStopThrowExe_OD')
        StarterRating(0)
        OnlyHitPlayer(1)
        AttackType(4)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
        CameraLookAtEnemy(1)
        callSubroutine('DeleteFunnel')
        SLOT_57 = 1
        SLOT_58 = 1
    sprite('mi431_03', 4)
    AttackOff()
    OppThrowAnimation(17, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    Voiceline('mi257')
    sprite('mi431_06', 8)
    CreateObject('mi431_KyushuSoul', 0)
    RefreshMultihit()
    physicsXImpulse(-4000)
    PrivateSE('mise_13')
    sprite('mi431_07', 8)
    XImpulseAcceleration(200)
    SetAcceleration(300)
    sprite('mi431_08', 8)
    sprite('mi431_09', 6)
    XImpulseAcceleration(-50)
    sprite('mi431_10', 6)
    sprite('mi431_11', 4)
    XImpulseAcceleration(250)
    SetAcceleration(-300)
    AddX(150000)
    SetBackground(2)
    EnableCollision(0)
    sprite('mi431_12', 4)
    if SLOT_XDistanceFromFowardCorner <= 160000:

        def RunOnObject_22():
            AddX(110000)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    RefreshMultihit()
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        if SLOT_21:
            TimestopEffect('')
            SLOT_11 = SLOT_11 + 300
            PaletteIndex(2)
            callSubroutine('Funnel_PalletChange')
            SetBackground(0)

    def upon_STATE_END():
        ForceFaceSprite()
    PrivateSE('mise_14')
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    TriggerUponForState('FunnelTimeStopThrow', 33)
    TriggerUponForState('FunnelTimeStopThrow_Open', 33)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    CameraLookAtEnemy(0)
    physicsXImpulse(3000)
    sprite('mi431_16', 5)
    sprite('mi431_17', 5)
    TriggerUponForState('FunnelTimeStopThrow', 34)
    TriggerUponForState('FunnelTimeStopThrow_Open', 34)
    sprite('mi431_18', 5)
    sprite('mi431_19', 5)
    sprite('mi431_20', 5)
    physicsXImpulse(0)
    sprite('mi431_21', 5)


@State
def UltimateTimeStopThrow_SP():

    def upon_IMMEDIATE():
        if SLOT_4:
            AttackDefaults_Throw('UltimateTimeStopThrowExe_SP', 3, 1, 0)
        else:
            AttackDefaults_Throw('UltimateTimeStopThrowExe_SP', 3, 0, 0)
        RangeCheck(120000)
        DistanceCheck(250000, 1, 150000, -150000)
        if SLOT_11:
            ThrowTechWindow(-1)
        AttackOff()
        EndMomentum(1)
        StayAfterMovement(1, 0)
        if SLOT_7:
            ObjectUpon2(11, 1431, 0)
        else:
            ObjectUpon2(11, 431, 0)
        SLOT_57 = 1
        SLOT_58 = 1
        callSubroutine('DeleteFunnel')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_31 <= 60:
                SLOT_31 = SLOT_31 + 60
    sprite('mi431_00', 6)
    sprite('mi431_01', 6)
    DistortionSettings(30, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    setInvincible(1)
    sprite('mi431_02', 6)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    SLOT_56 = 1
    setInvincible(0)
    RefreshMultihit()
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    SLOT_56 = 0
    AttackOff()
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_22', 4)
    Voiceline('mi155')
    CommonSE('010_swing_sword_0')
    sprite('mi431_23', 4)
    sprite('mi431_24', 4)
    sprite('mi431_25', 4)
    sprite('mi431_26', 4)
    sprite('mi431_27', 4)
    SetInertia(-10000)
    TriggerUponForState('FunnelTimeStopThrow', 32)
    TriggerUponForState('FunnelTimeStopThrow_Open', 32)
    sprite('mi431_28', 4)
    sprite('mi431_29', 4)
    sprite('mi431_30', 4)
    sprite('mi431_31', 4)
    sprite('mi431_32', 4)


@State
def UltimateTimeStopThrowExe_SP():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(0)
        Damage(200)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(0)
        PushbackX(0)
        Stagger(100)
        Crumple(100)
        AirUntechableTime(100)
        HitAnywhere(1)
        DamageEffect(8, '')
        ShutUp(1)
        EnemyHitstopAddition(0, 9999, 9999)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('UltimateTimeStopThrowExe_SP')
        OnlyHitPlayer(1)
        StarterRating(0)
        EnableRapidCancel(0)
        StayAfterMovement(1, 0)
        CameraLookAtEnemy(1)
        callSubroutine('DeleteFunnel')
        SLOT_57 = 1
        SLOT_58 = 1
    sprite('mi431_03', 4)
    AttackOff()
    OppThrowAnimation(17, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    sprite('mi431_03', 4)
    sprite('mi431_04', 4)
    sprite('mi431_05', 4)
    Voiceline('mi257')
    sprite('mi431_06', 8)
    CreateObject('mi431_KyushuSoul', 0)
    RefreshMultihit()
    physicsXImpulse(-4000)
    PrivateSE('mise_13')
    sprite('mi431_07', 8)
    XImpulseAcceleration(200)
    SetAcceleration(300)
    sprite('mi431_08', 8)
    sprite('mi431_09', 6)
    XImpulseAcceleration(-50)
    sprite('mi431_10', 6)
    sprite('mi431_11', 4)
    XImpulseAcceleration(250)
    SetAcceleration(-300)
    AddX(150000)
    SetBackground(2)
    EnableCollision(0)
    sprite('mi431_12', 4)
    if SLOT_XDistanceFromFowardCorner <= 160000:

        def RunOnObject_22():
            AddX(110000)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    RefreshMultihit()
    DamageFromStateOnly('')

    def upon_OPPONENT_HIT():
        if SLOT_21:
            TimestopEffect('')
            SLOT_11 = SLOT_11 + 120
            PaletteIndex(2)
            callSubroutine('Funnel_PalletChange')
            SetBackground(0)

    def upon_STATE_END():
        ForceFaceSprite()
    PrivateSE('mise_14')
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    PerAcceleration(50)
    XImpulseAcceleration(50)
    TriggerUponForState('FunnelTimeStopThrow', 33)
    TriggerUponForState('FunnelTimeStopThrow_Open', 33)
    sprite('mi431_13', 4)
    sprite('mi431_14', 4)
    sprite('mi431_15', 4)
    CameraLookAtEnemy(0)
    physicsXImpulse(3000)
    sprite('mi431_16', 5)
    sprite('mi431_17', 5)
    TriggerUponForState('FunnelTimeStopThrow', 34)
    TriggerUponForState('FunnelTimeStopThrow_Open', 34)
    sprite('mi431_18', 5)
    sprite('mi431_19', 5)
    sprite('mi431_20', 5)
    physicsXImpulse(0)
    sprite('mi431_21', 5)


@State
def UltimateTimeStop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Damage(0)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        DefeatOpponentBehavior(1)
        Hitstop(0)
        EnemyHitstopAddition(0, 9999, 9999)
        ShutUp(1)
        DamageEffect(8, '')
        GuardEffect(8, '')
        HitOverhead(100)
        HitLow(100)
        HitAirUnblockable(100)
        HitAnywhere(1)
        PreventBlocking(1)
        OppMovementUnlock(1)
        PassByArmor(1)
        BurstAttribute(1)
        OnlyHitPlayer(1)
        StarterRating(0)
        Unknown12055(1)
        AttackOff()
        SLOT_58 = 1
        EnableRapidCancel(0)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 165:
                if SLOT_IsGrounded:
                    sendToLabel(1)
            if SLOT_StateDuration >= 225:
                if SLOT_IsGrounded:
                    sendToLabel(2)

        def upon_OPPONENT_HIT():
            TimestopEffect('')
            PaletteIndex(2)
            callSubroutine('Funnel_PalletChange')
            SLOT_11 = 360
    sprite('mi432_00', 5)
    sprite('mi432_01', 5)
    sprite('mi432_02', 5)
    sprite('mi432_03', 5)
    sprite('mi432_04', 5)
    sprite('mi432_05', 5)
    sprite('mi432_06', 5)
    sprite('mi432_07', 5)
    sprite('mi432_08', 5)
    sprite('mi432_09', 5)
    sprite('mi432_10', 5)
    sprite('mi432_11', 5)
    sprite('mi432_12', 6)
    Voiceline('mi255')
    CreateObject('mi432_Tame', -1)
    PrivateSE('mise_13')
    if SLOT_4:
        SLOT_4 = 0
        SLOT_31 = 0
        EndYPhysicsImpulse()
        PerGravity(10)
    sprite('mi432_13', 6)
    sprite('mi432_14', 6)
    label(0)
    sprite('mi432_12', 6)
    PerGravity(110)
    CommonSE('019_quake_1')
    sprite('mi432_13', 6)
    CommonSE('019_quake_1')
    sprite('mi432_14', 6)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi432_12', 3)
    PerGravity(110)
    CommonSE('019_quake_1')
    sprite('mi432_13', 3)
    CommonSE('019_quake_1')
    sprite('mi432_14', 3)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('mi432_12', 5)
    clearUponHandler(EVERY_FRAME)
    sprite('mi432_13', 5)
    sprite('mi432_14', 5)
    callSubroutine('DeleteFunnel')
    sprite('mi432_15', 1)
    if SLOT_21:
        RefreshMultihit()
    HeatChange(-10000)
    TriggerUponForState('mi432_Tame', 32)
    CreateObject('mi432_Kaiho', -1)
    ScreenShake(20000, 20000)
    PrivateSE('mise_14')
    callSubroutine('DeleteFunnel')
    NoDamageAction(1)
    setInvincible(1)
    BurstInvincibility(1)
    sprite('mi432_15', 4)
    EndAttack()
    NoDamageAction(0)
    BurstInvincibility(0)
    callSubroutine('DeleteFunnel')
    sprite('mi432_16', 5)
    sprite('mi432_17', 5)
    sprite('mi432_18', 5)
    sprite('mi432_19', 5)
    sprite('mi432_20', 5)
    sprite('mi432_16', 5)
    sprite('mi432_17', 5)
    sprite('mi432_18', 5)
    sprite('mi432_19', 5)
    sprite('mi432_20', 5)
    if SLOT_11:
        Voiceline('mi256')
    sprite('mi432_21', 5)
    sprite('mi432_22', 5)


@State
def UltimateTimeStop_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Damage(0)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        DefeatOpponentBehavior(1)
        Hitstop(0)
        EnemyHitstopAddition(0, 9999, 9999)
        ShutUp(1)
        DamageEffect(8, '')
        GuardEffect(8, '')
        HitOverhead(100)
        HitLow(100)
        HitAirUnblockable(100)
        HitAnywhere(1)
        PreventBlocking(1)
        OppMovementUnlock(1)
        PassByArmor(1)
        BurstAttribute(1)
        OnlyHitPlayer(1)
        StarterRating(0)
        Unknown12055(1)
        AttackType(4)
        AttackOff()
        SLOT_58 = 1
        EnableRapidCancel(0)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 105:
                if SLOT_IsGrounded:
                    sendToLabel(1)
            if SLOT_StateDuration >= 165:
                if SLOT_IsGrounded:
                    sendToLabel(2)

        def upon_OPPONENT_HIT():
            TimestopEffect('')
            PaletteIndex(2)
            callSubroutine('Funnel_PalletChange')
            SLOT_11 = 360
    sprite('mi432_00', 5)
    sprite('mi432_01', 5)
    sprite('mi432_02', 5)
    sprite('mi432_03', 5)
    sprite('mi432_04', 5)
    sprite('mi432_05', 5)
    sprite('mi432_06', 5)
    sprite('mi432_07', 5)
    sprite('mi432_08', 5)
    sprite('mi432_09', 5)
    sprite('mi432_10', 5)
    sprite('mi432_11', 5)
    sprite('mi432_12', 6)
    Voiceline('mi255')
    CreateObject('mi432_Tame', -1)
    PrivateSE('mise_13')
    if SLOT_4:
        SLOT_4 = 0
        SLOT_31 = 0
        EndYPhysicsImpulse()
        PerGravity(10)
    sprite('mi432_13', 6)
    sprite('mi432_14', 6)
    label(0)
    sprite('mi432_12', 6)
    PerGravity(110)
    CommonSE('019_quake_1')
    sprite('mi432_13', 6)
    CommonSE('019_quake_1')
    sprite('mi432_14', 6)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi432_12', 3)
    PerGravity(110)
    CommonSE('019_quake_1')
    sprite('mi432_13', 3)
    CommonSE('019_quake_1')
    sprite('mi432_14', 3)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('mi432_12', 5)
    clearUponHandler(EVERY_FRAME)
    sprite('mi432_13', 5)
    sprite('mi432_14', 5)
    callSubroutine('DeleteFunnel')
    sprite('mi432_15', 1)
    if SLOT_21:
        RefreshMultihit()
    HeatChange(-10000)
    TriggerUponForState('mi432_Tame', 32)
    CreateObject('mi432_Kaiho', -1)
    ScreenShake(20000, 20000)
    PrivateSE('mise_14')
    callSubroutine('DeleteFunnel')
    NoDamageAction(1)
    setInvincible(1)
    BurstInvincibility(1)
    sprite('mi432_15', 4)
    EndAttack()
    NoDamageAction(0)
    BurstInvincibility(0)
    callSubroutine('DeleteFunnel')
    sprite('mi432_16', 5)
    sprite('mi432_17', 5)
    sprite('mi432_18', 5)
    sprite('mi432_19', 5)
    sprite('mi432_20', 5)
    sprite('mi432_16', 5)
    sprite('mi432_17', 5)
    sprite('mi432_18', 5)
    sprite('mi432_19', 5)
    sprite('mi432_20', 5)
    if SLOT_11:
        Voiceline('mi256')
    sprite('mi432_21', 5)
    sprite('mi432_22', 5)


@State
def SoshiteTokiwaUgokidasu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        CameraControlEnable(1)
        setInvincible(1)
        PreventSelfPush(1)
        EndMomentum(1)
        SLOT_57 = 1

        def upon_EVERY_FRAME():
            callSubroutine('DeleteFunnel')
    sprite('mi312_10ex01', 6)
    sprite('mi400_11', 6)
    sprite('mi400_12', 6)
    sprite('mi400_13', 6)
    sprite('mi400_14', 6)
    sprite('mi440_05', 6)
    sprite('mi440_06', 6)
    sprite('mi400_15', 6)
    Voiceline('mi260')
    sprite('mi400_16', 6)
    sprite('mi400_17', 90)
    sprite('mi400_17', 40)
    CreateObject('mi432_Kaiho', -1)
    Unknown30014('')
    PaletteIndex(0)
    StopClock(0)
    SLOT_11 = 0
    callSubroutine('Funnel_PalletModori')
    Unknown23169(0)
    CreateObject('TimeStopFinish', -1)
    CameraControlEnable(0)
    sprite('mi400_18', 6)
    sprite('mi400_19', 6)
    sprite('mi400_20', 6)
    sprite('mi400_21', 6)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        EndMomentum(0)
        AttackLevel_(5)
        Damage(1000)
        MinimumDamage(100)
        Hitstop(0)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(40000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(9999)
        HardKnockdown(120)
        DisableOppPushCollision(1)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeat')
        AttackOff()
        ObjectUpon2(11, 333, 0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            sendToLabel(0)
            PlayPlayAstralBGM(0)
            CreateObject('AstralCamera', -1)
            SLOT_4 = 0
            AstralHeatCleanup(1, 0)
            SLOT_6 = 0
            if SLOT_11:
                StopTimestopEffect('')
                SLOT_11 = 0
                PaletteIndex(0)

        def upon_EVERY_FRAME():
            callSubroutine('DeleteFunnel')
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        SLOT_57 = 1
        SLOT_58 = 1

        def upon_STATE_END():
            SLOT_7 = 0
        SLOT_6 = 0
        random_(2, 0, 50)
        SLOT_2 = SLOT_0
    sprite('mi450_00', 6)
    setInvincible(1)
    sprite('mi450_01', 6)
    if SLOT_2:
        Voiceline('mi290')
    else:
        Voiceline('mi293')
    DistortionSettings(30, -1, 2)
    CreateObject('EMB_MI_AH', -1)
    EmptyHeat()
    sprite('mi450_02', 6)
    sprite('mi450_03', 6)
    sprite('mi450_04', 6)
    sprite('mi450_05', 6)
    sprite('mi450_06', 6)
    CreateObject('mi450_Start', -1)
    PrivateSE('mise_12')
    sprite('mi450_07', 3)
    CommonSE('015_blaze_2')
    sprite('mi450_08', 3)
    sprite('mi450_09', 3)
    CommonSE('015_blaze_1')
    sprite('mi450_07ex', 2)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('mi450_08ex', 2)
    sprite('mi450_09ex', 2)
    sprite('mi450_07', 2)
    sprite('mi450_08', 2)
    sprite('mi450_09', 2)
    sprite('mi450_07ex', 2)
    sprite('mi450_08ex', 2)
    sprite('mi450_09ex', 2)
    sprite('mi450_07', 2)
    setInvincible(0)
    AttackOff()
    sprite('mi450_08', 2)
    sprite('mi450_09', 2)
    sprite('mi450_07ex', 2)
    sprite('mi450_08ex', 2)
    sprite('mi450_09ex', 2)
    sprite('mi450_07', 2)
    DespawnEAEffect('mi450_Start')
    sprite('mi450_08', 2)
    sprite('mi450_09', 2)
    sprite('mi450_07ex', 2)
    sprite('mi450_08ex', 2)
    sprite('mi450_09ex', 2)
    sprite('mi450_07', 4)
    sprite('mi450_08', 4)
    sprite('mi450_09', 4)
    sprite('mi450_07ex', 4)
    sprite('mi450_08ex', 4)
    sprite('mi450_09ex', 4)
    sprite('mi450_07', 4)
    sprite('mi450_08', 4)
    sprite('mi450_09', 4)
    sprite('mi450_07ex', 4)
    sprite('mi450_08ex', 4)
    sprite('mi450_09ex', 4)
    sprite('mi450_10', 3)
    sprite('mi450_11', 3)
    sprite('mi450_12', 3)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 60)
    clearUponHandler(EVERY_FRAME)
    SLOT_11 = 0
    setInvincible(1)
    CreateObject('mi450_OnryoBasira', -1)
    sprite('keep', 60)
    CreateObject('mi450_Kirikae', -1)
    PrivateSE('mise_13')
    sprite('keep', 50)
    TriggerUponForState('mi450_OnryoBasira', 32)
    TriggerUponForState('AstralCamera', 32)
    DespawnEAEffect('mi450_Start')

    def RunOnObject_22():
        AbsoluteY(3000000)
        physicsYImpulse(20000)
    CommonSE('001_airbackdash_1')
    loopRest()
    label(1)
    sprite('mi020_00', 4)
    EndMomentum(1)
    TeleportToObject(22)
    AbsoluteY(3000000)
    AddX(-100000)
    physicsYImpulse(40000)
    setGravity(-2000)

    def upon_EVERY_FRAME():
        if SLOT_YRelativeToOpponent <= 200000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(3)
    sprite('mi020_01', 4)
    label(2)
    sprite('mi020_00', 4)
    sprite('mi020_01', 4)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('mi450_13', 6)
    Flip()
    TriggerUponForState('mi450_OnryoBasira', 32)
    TriggerUponForState('AstralCamera', 33)
    EndMomentum(1)
    RefreshMultihit()
    Damage(0)
    FlipOnHit(1)
    HitsparkSize(0)
    AirHitstunAnimation(1)
    AirPushbackX(0)
    AirPushbackY(-1)
    sprite('mi450_14', 6)
    sprite('mi450_15', 6)
    sprite('mi450_16', 6)
    sprite('mi450_17', 6)
    sprite('mi450_18', 6)
    sprite('mi450_19', 6)
    sprite('mi450_20', 6)
    sprite('mi450_21', 6)
    EndMomentum(1)
    sprite('null', 40)
    CreateObject('mi450_CutTest', -1)

    def RunOnObject_22():
        Visibility(1)
    AddX(-50000)
    PrivateSE('mise_14')
    sprite('null', 100)
    if SLOT_2:
        Voiceline('mi291')
    else:
        Voiceline('mi294')
    sprite('mi450_21', 40)
    TriggerUponForState('AstralCamera', 34)
    CreateObject('mi450_GamenAura00', -1)
    CreateObject('mi450_BigOnryo', -1)
    CreateObject('mi450_BigOnryo2', -1)

    def RunOnObject_1():
        AddX(750000)
        AddY(-25000)
        Flip()
    CreateObject('mi450_BigOnryo2', -1)

    def RunOnObject_1():
        AddX(-750000)
        AddY(-25000)
    PrivateSE('mise_12')
    CreateObject('mi450_BigOnryo2', -1)

    def RunOnObject_1():
        AddX(350000)
        AddY(160000)
        AddScale(-400)
        Flip()
    CreateObject('mi450_BigOnryo2', -1)

    def RunOnObject_1():
        AddX(-350000)
        AddY(160000)
        AddScale(-400)
    CreateObject('mi450_BigOnryo3', -1)

    def RunOnObject_1():
        AddX(370000)
        AddY(-75000)
        AddScale(200)
        Flip()
    CreateObject('mi450_BigOnryo3', -1)

    def RunOnObject_1():
        AddX(-370000)
    TriggerUponForState('mi450_CutTest', 32)

    def RunOnObject_22():
        Visibility(0)
    sprite('mi450_22', 8)
    PrivateSE('mise_07')
    sprite('mi450_23', 6)
    sprite('mi450_24', 6)
    AddY(30000)
    sprite('mi450_25', 6)
    sprite('mi450_26', 4)
    sprite('mi450_24', 4)
    PrivateSE('mise_07')
    sprite('mi450_25', 4)
    sprite('mi450_26', 4)
    sprite('mi450_24', 4)
    PrivateSE('mise_07')
    sprite('mi450_25', 4)
    sprite('mi450_26', 4)
    PrivateSE('mise_07')
    sprite('mi450_24', 4)
    sprite('mi450_25', 4)
    sprite('mi450_26', 4)
    PrivateSE('mise_07')
    sprite('mi450_24', 4)
    sprite('mi450_25', 4)
    sprite('mi450_26', 4)
    CreateObject('mi450_fallspeed', -1)
    DespawnEAEffect('mi450_GamenAura00')
    TriggerUponForState('AstralCamera', 35)
    PrivateSE('mise_15')
    sprite('mi450_27', 3)
    RefreshMultihit()
    Hitstop(0)
    AirPushbackY(-60000)
    YImpulseBeforeWallbounce(0)

    def upon_LANDING():
        sendToLabel(4)
    sprite('mi450_28', 3)
    physicsYImpulse(-60000)
    label(100)
    sprite('mi450_28', 3)
    CommonSE('019_quake_0')
    sprite('mi450_27', 3)
    CommonSE('016_explode_0')
    loopRest()
    gotoLabel(100)
    label(4)
    sprite('keep', 10)
    TriggerUponForState('mi450_BigOnryo', 32)
    TriggerUponForState('mi450_BigOnryo2', 32)
    TriggerUponForState('mi450_BigOnryo3', 32)
    TriggerUponForState('AstralCamera', 36)
    CreateObject('mi450_GroundAura', -1)
    CommonSE('016_explode_2')
    sprite('keep', 60)
    DespawnEAEffect('mi450_fallspeed')
    if SLOT_2:
        Voiceline('mi292')
    else:
        Voiceline('mi295')
    sprite('keep', 13)
    CreateObject('mi450_EndAnim', -1)
    sprite('keep', 10)
    TriggerUponForState('AstralCamera', 37)
    TriggerUponForState('mi450_GroundAura', 32)
    sprite('keep', 50)
    RefreshMultihit()
    Damage(35000)
    AirPushbackX(0)
    AirPushbackY(100000)
    YImpulseBeforeWallbounce(0)
    Hitstop(0)
    AirUntechableTime(9999)
    DefeatOpponentBehavior(3)
    HitAnywhere(1)
    sprite('mi450_29', 4)
    CreateObject('mi450_EndAura', -1)
    sprite('mi450_29', 4)
    CreateObject('mi450_EndAura', -1)

    def RunOnObject_1():
        AddX(350000)
        AddScaleY(-350)
    sprite('mi450_29', 130)
    CreateObject('mi450_EndAura', -1)

    def RunOnObject_1():
        AddX(-350000)
        AddScaleY(-350)
    SLOT_7 = 0
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraWinnerControlStop(1)
    SLOT_60 = 3
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    ObjectUpon2(11, 100, 0)
    sprite('mi450_29', 10)
    sprite('mi450_30', 8)
    sprite('mi450_31', 8)
    SLOT_60 = 1
    sprite('mi450_32', 8)
    sprite('mi450_33', 8)
    sprite('mi000_00', 8)
    WinAction()
    sprite('mi611_00', 7)
    CrouchState(0)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi408')
    DemoEndOnVoiceEnd(1)
    label(200)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(200)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('mi054')
    sprite('mi900_00', 32767)
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
    CreateObject('mi900_Fire', 0)
    CreateObject('mi900_Fire', 1)
    CreateObject('mi900_Fire', 2)
    CreateObject('mi900_Fire', 3)
    CreateObject('mi900_Fire', 4)
    CreateObject('mi900_Fire', 5)
    CreateObject('mi900_Fire', 6)
    CreateObject('mi900_Fire', 7)
    CreateObject('mi900_Fire', 8)
    CreateObject('mi900_Fire', 9)
    CreateObject('mi900_Gaikotu', 10)
    CreateObject('mi900_Gaikotu2', 11)
    CreateObject('mi900_Gaikotu3', 12)
    CreateObject('mi900_bloom', -1)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(150000)
    sprite('mi901_00', 50)
    physicsYImpulse(-150)
    sprite('mi901_00', 50)
    physicsYImpulse(150)
    Voiceline('mi055')
    label(0)
    sprite('mi901_00', 32767)
    physicsYImpulse(-150)
    sprite('mi901_00', 32767)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('mi000', 14433, 14435, 14433, 14435, 14177, 14179, 14177, 
        14179, 14433, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi055', 14177, 14179, 14177, 14179, 14177, 13155, 24886, 
        25399, 24887, 12849, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi400', 14177, 14179, 14177, 14179, 14177, 14435, 14177, 
        14179, 14177, 13667, 13665, 13667, 14689, 13923, 13921, 13923, 
        13921, 14691, 14689, 14179, 14689, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi401', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi404', 12641, 25393, 12593, 14177, 14179, 14177, 14179, 
        14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi406', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi407', 12641, 25394, 24887, 25399, 24887, 25399, 24887, 
        25399, 24887, 25399, 14135, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi408', 12641, 25394, 24887, 25399, 24887, 25399, 24887, 
        25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi411', 14177, 14179, 14177, 13667, 24882, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi412', 14177, 14179, 12641, 25394, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi414', 14177, 14179, 12641, 25394, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('mi416', 14177, 14179, 14177, 14179, 14177, 14179, 12641, 
        24882, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('mi000', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi055', 14177, 14179, 14177, 14179, 14177, 13155, 
            24886, 25399, 24887, 12849, 14435, 14433, 14435, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('mi400', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14435, 14433, 14435, 14433, 14179, 24882, 25399, 24887, 
            25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
            55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi401', 12641, 25393, 24888, 25400, 24888, 25400, 
            24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 13923, 24880, 25398, 24886, 25398, 24886, 
            25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi405', 14177, 14179, 14177, 12643, 24882, 25399, 
            24887, 25399, 24887, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi406', 14177, 14179, 14177, 14179, 12641, 25394, 
            24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 
            14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi407', 14177, 14179, 14177, 12643, 24882, 25399, 
            24887, 25399, 24887, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi408', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 
            25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi411', 14177, 14179, 14177, 14179, 14177, 13923, 
            24880, 12849, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi412', 12641, 25397, 12337, 24880, 25399, 24887, 
            25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('mi414', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 
            14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('mi416', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 12641, 25394, 24887, 25399, 24887, 
            25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            Unknown18011('mi000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('mi400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14179, 14177, 14179, 14177, 13667, 
                24885, 12849, 12643, 24888, 25397, 24885, 25397, 53, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi401', 13921, 13923, 13921, 14179, 24882, 25400,
                24888, 25398, 24888, 25398, 24886, 12849, 14179, 14177, 
                14179, 14177, 14179, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('mi000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 12899, 24885, 25399, 24887, 25399, 24887, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi400', 14433, 14435, 14433, 12643, 24882, 25400,
                12849, 14433, 13923, 13921, 14179, 12641, 25393, 24885, 
                12593, 14179, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi401', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 24885, 25398, 24886, 12593, 12643, 24882, 
                25398, 24886, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('mi000', 13878, 13921, 13923, 13921, 13923, 13921,
                13923, 13921, 14179, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('mi400', 14433, 14435, 14433, 13923, 24885, 25400,
                24888, 13617, 13923, 13921, 13923, 12641, 25394, 24887, 
                25399, 24887, 12849, 14179, 14177, 14179, 14177, 14691, 
                14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi401', 12641, 25394, 24886, 25398, 24886, 25398,
                13622, 12641, 25397, 12849, 13921, 13923, 14433, 14435, 
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('mi000', 13921, 13923, 13921, 13923, 12641, 24882,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 12849, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14433, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            Unknown18011('mi500', 14179, 24885, 25399, 24887, 25399, 24887,
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi501', 14433, 13923, 14433, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13665, 13667, 
                13665, 13667, 12641, 25397, 12341, 13921, 13923, 13921, 
                13923, 13921, 13923, 12641, 25394, 24886, 25398, 24886, 
                12337, 13923, 14433, 13923, 14433, 13923, 13921, 13923, 
                12641, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('mi502', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi503', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 12897, 25392, 12344, 14177, 
                14179, 14177, 14179, 14177, 14179, 12641, 25396, 24887, 
                25399, 24887, 25399, 24887, 25400, 24888, 25400, 24888, 
                13617, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('mi504', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi505', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('mi506', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi507', 12641, 25392, 24888, 25400, 24888, 25400,
                24888, 25398, 24886, 25398, 24886, 25398, 24886, 25400, 
                24888, 12337, 13923, 13921, 13923, 14433, 14435, 12641, 
                25394, 12342, 13921, 13923, 13921, 13923, 13921, 13923, 
                12641, 25397, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('mi520', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14435, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi521', 14177, 14179, 14177, 14179, 14177, 14179,
                12641, 25396, 13620, 12641, 25392, 24886, 25398, 24886, 
                25398, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 
                14385, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('hz'):
            Unknown18011('mi526', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 12643, 12336, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('mi527', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 12641, 25400, 12344, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('mi536', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 12643, 12338, 13921, 
                13923, 13921, 14435, 24880, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('mi537', 14177, 14179, 12897, 25392, 12340, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 12897, 
                25392, 12341, 12641, 25396, 24886, 12337, 13923, 12641, 
                25396, 24886, 25398, 24886, 25398, 24886, 25398, 12337, 
                12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('am'):
            Unknown18011('mi540', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 13411, 24888, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                14385, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi541', 12897, 25392, 24887, 25399, 24887, 25399,
                24887, 25399, 24887, 12338, 13155, 24880, 25400, 24888, 
                12337, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 12641, 25400, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('az'):
            Unknown18011('mi544', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 12643, 12336, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi545', 14177, 14179, 14177, 14179, 12641, 25396,
                24887, 25398, 24886, 25398, 24886, 12338, 12643, 24880, 
                12337, 14435, 14177, 14179, 14177, 14179, 14177, 13923, 
                13921, 13923, 13921, 13923, 12641, 25394, 24886, 25400, 
                24888, 25400, 24888, 14385, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('mi544', 14433, 14435, 14433, 14435, 14433, 
                    14435, 14433, 12643, 12336, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('mi545', 14433, 14435, 14433, 14435, 14433, 
                    14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433,
                    14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('mi546', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('mi547', 12641, 25396, 24888, 25399, 24887, 25399,
                24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 12338, 14435, 24886, 12337, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 12897, 25392, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('mi546', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('mi547', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 13667, 24886, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('mi548', 14433, 14435, 14433, 14435, 14433, 13923,
                13921, 13923, 13921, 13923, 13921, 13155, 24880, 25398, 
                24886, 25398, 24886, 25398, 24886, 24886, 25398, 12345, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi549', 14177, 14179, 14177, 14179, 14177, 14179,
                13921, 13923, 13921, 13923, 12641, 25392, 24886, 12338, 
                13411, 24880, 25400, 24886, 25400, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 12337, 
                13921, 13923, 13921, 13923, 12641, 25400, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            if SLOT_140:
                Unknown18011('mi548', 14433, 14435, 14433, 14435, 24885, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 13624, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('mi549', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('mi550', 14433, 14435, 14433, 14435, 14433, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 14435, 24888, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi551', 12641, 25396, 24887, 25398, 24886, 13361,
                13923, 24885, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 24886, 12849, 12643, 24882, 25398, 24886, 25398, 
                24886, 25399, 24887, 14385, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('mi558', 14433, 14435, 14433, 14435, 14433, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13411, 24882, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('mi559', 14177, 14179, 14177, 14179, 14177, 14179,
                12897, 25392, 13620, 14433, 13411, 14433, 13411, 13921, 
                13923, 13921, 13923, 13921, 13923, 12641, 25394, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25399, 24887, 
                25399, 24887, 25399, 24887, 14385, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
        if CharacterIDCheck('nt'):
            Unknown18011('mi560', 14433, 14435, 14433, 14435, 14433, 13923,
                13921, 12643, 12341, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('mi561', 13921, 13923, 13921, 13923, 13921, 13923,
                12897, 25392, 12337, 24880, 12337, 13411, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                14177, 14179, 14177, 14179, 14177, 14179, 12641, 25400, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('mi564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 24885, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('mi565', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)


@State
def CmnActEntry():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(100)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('no'):
        SyncEntry()
        gotoLabel(120)
    if CharacterIDCheck('rc'):
        SyncEntry()
        gotoLabel(130)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('hz'):
        SyncEntry()
        gotoLabel(220)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('am'):
        SyncEntry()
        gotoLabel(300)
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
    if CharacterIDCheck('kk'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(340)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('nt'):
        SyncEntry()
        gotoLabel(400)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    label(0)
    sprite('mi600_00', 1)
    sprite('mi600_00', 7)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    RandomVoiceline('mi412', 100, 'mi414', 100, '', 0, '', 0)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    physicsYImpulse(-500)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    DemoTimer(45)
    ExitState()
    label(1)
    sprite('null', 1)
    sprite('null', 5)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    Voiceline('mi416')
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    DemoTimer(90)
    loopRest()
    ExitState()
    label(100)
    sprite('mi600_00', 1)
    sprite('mi600_00', 32767)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 101)
    loopRest()
    label(101)
    sprite('mi600_00', 10)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    Voiceline('mi500')
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(110)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(110)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    SetActionMark(3)
    label(111)
    sprite('mi000_00', 8)
    AddActionMark(-1)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(111)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi502')
    DemoTimer(270)
    sprite('mi300_06', 240)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    ExitState()
    label(120)
    sprite('mi600_00', 1)
    sprite('mi600_00', 1)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 101)
    label(121)
    sprite('mi600_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(121)
    label(122)
    sprite('mi600_00', 20)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    Voiceline('mi504')
    DemoEndOnVoiceEnd(1)
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    SetActionMark(3)
    label(123)
    sprite('mi600_08', 8)
    AddActionMark(-1)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(123)
    sprite('mi600_11', 8)
    ObjectUpon(22, 32)
    sprite('mi600_12', 8)
    loopRest()
    ExitState()
    label(130)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(130)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    SetActionMark(2)
    label(131)
    sprite('mi000_00', 8)
    AddActionMark(-1)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(131)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi506')
    DemoTimer(210)
    sprite('mi300_06', 160)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    ExitState()
    label(200)
    sprite('mi600_00', 1)
    sprite('mi600_00', 1)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 205)
    label(201)
    sprite('mi600_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(201)
    label(202)
    sprite('mi600_00', 20)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    SetActionMark(3)
    label(203)
    sprite('mi600_08', 8)
    AddActionMark(-1)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(203)
    sprite('mi600_11', 8)
    ObjectUpon(22, 32)
    sprite('mi600_12', 8)
    label(204)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    gotoLabel(204)
    label(205)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi520')
    DemoTimer(290)
    sprite('mi300_06', 270)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    ExitState()
    label(220)
    sprite('null', 1)
    uponSendToLabel(32, 221)
    sprite('null', 32767)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    label(221)
    sprite('null', 23)
    clearUponHandler(32)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi300_00', 6)
    Voiceline('mi526')
    DemoEndOnVoiceEnd(1)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 270)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    sprite('null', 1)
    if SLOT_17:
        conditionalSendToLabel(280)
    sprite('null', 70)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    uponSendToLabel(32, 282)
    ObjectUpon(22, 32)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    label(281)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    loopRest()
    gotoLabel(281)
    label(282)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    Voiceline('mi536')
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('keep', 1)
    clearUponHandler(32)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    DemoTimer(210)
    sprite('mi300_06', 115)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    DemoTimer(20)
    loopRest()
    ExitState()
    label(300)
    sprite('mi600_00', 1)
    sprite('mi600_00', 1)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    if SLOT_17:
        conditionalSendToLabel(300)
    loopRest()
    label(301)
    sprite('mi600_00', 36)
    sprite('mi600_00', 8)
    clearUponHandler(32)
    Voiceline('mi540')
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    physicsYImpulse(-500)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    ObjectUpon(22, 32)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    ExitState()
    label(320)
    sprite('mi600_00', 1)
    sprite('mi600_00', 32767)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 321)
    loopRest()
    label(321)
    sprite('mi600_00', 8)
    clearUponHandler(32)
    Voiceline('mi544')
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    physicsYImpulse(-500)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    DemoTimer(80)
    ExitState()
    label(2320)
    sprite('keep', 2)
    uponSendToLabel(32, 2322)
    XPositionRelativeFacing(0)
    label(2321)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    gotoLabel(2321)
    label(2322)
    sprite('mi033_00', 2)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('mi033_01', 3)
    physicsXImpulse(-28000)
    CommonSE('001_airbackdash_0')
    sprite('mi033_02', 3)
    sprite('mi033_03', 3)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_04', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_05', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    XImpulseAcceleration(70)
    sprite('mi033_06', 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    EnableAfterimage(0)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    Voiceline('mi544')
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 250)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(330)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    Voiceline('mi546')
    loopRest()
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 180)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    ObjectUpon(22, 32)
    sprite('mi000_09', 8)
    loopRest()
    ExitState()
    label(2330)
    sprite('null', 2)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        if SLOT_19 < 920000:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2332)
    label(2331)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    gotoLabel(2331)
    label(2332)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 210)
    Voiceline('mi546')
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    DemoTimer(30)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(340)
    sprite('mi600_00', 1)
    sprite('mi600_00', 32767)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 341)
    loopRest()
    label(341)
    sprite('mi600_00', 60)
    sprite('mi600_00', 8)
    clearUponHandler(32)
    Voiceline('mi548')
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    physicsYImpulse(-500)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 84)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    DemoTimer(20)
    ExitState()
    label(2340)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2340)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    Voiceline('mi548')
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 280)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    ObjectUpon(22, 32)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    ExitState()
    label(350)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    label(351)
    sprite('null', 1)
    if SLOT_17:
        conditionalSendToLabel(351)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    ObjectUpon(22, 32)
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    SetActionMark(2)
    uponSendToLabel(32, 353)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    label(352)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    loopRest()
    gotoLabel(352)
    label(353)
    sprite('keep', 1)
    clearUponHandler(32)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi550')
    DemoTimer(210)
    sprite('mi300_06', 160)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    DemoTimer(55)
    loopRest()
    ExitState()
    label(390)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()
    sprite('null', 1)
    if SLOT_17:
        conditionalSendToLabel(390)
    sprite('null', 20)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    SetActionMark(2)
    uponSendToLabel(32, 392)
    ObjectUpon(22, 32)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    label(391)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    loopRest()
    gotoLabel(391)
    label(392)
    sprite('keep', 1)
    clearUponHandler(32)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi558')
    DemoTimer(210)
    sprite('mi300_06', 160)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    DemoTimer(55)
    loopRest()
    ExitState()
    label(400)
    sprite('mi600_00', 1)
    sprite('mi600_00', 32767)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 401)
    loopRest()
    label(401)
    sprite('mi600_00', 15)
    clearUponHandler(32)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    Voiceline('mi560')
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    physicsYImpulse(-500)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    DemoTimer(180)
    ExitState()
    label(420)
    sprite('mi600_00', 1)
    sprite('mi600_00', 32767)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    uponSendToLabel(32, 421)
    loopRest()
    label(421)
    sprite('mi600_00', 10)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    Voiceline('mi564')
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    EndMomentum(1)
    DemoTimer(160)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
    sprite('keep', 1)
    if not SLOT_7:
        notConditionalSendToLabel(9999)
    sprite('mi203_11', 3)
    sprite('mi203_10', 3)
    sprite('mi203_09', 3)
    sprite('mi204_00', 5)
    ObjectUpon2(11, 204, 0)
    sprite('mi204_01', 5)
    sprite('mi204_02', 5)
    sprite('mi204_03', 5)
    sprite('mi203_02', 5)
    sprite('mi204_04', 5)
    CreateObject('FunnelThudenrEffShunou', 100)
    sprite('mi203_01', 5)
    sprite('mi203_00', 4)
    label(9999)
    sprite('mi615_00', 7)
    ObjectUpon2(11, 615, 0)
    sprite('mi615_01', 7)
    sprite('mi615_02', 7)
    sprite('mi615_03', 7)
    PrivateSE('mise_00')
    sprite('mi615_04', 7)
    sprite('mi615_05', 7)
    sprite('mi615_06', 7)
    RandomVoiceline('mi400', 100, 'mi401', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    sprite('mi615_07', 7)
    sprite('mi615_08', 7)
    sprite('mi615_09', 32767)
    loopRest()


@State
def CmnActMatchWin():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
    if SLOT_7:
        conditionalSendToLabel(9999)
    label(0)
    if SLOT_109:
        conditionalSendToLabel(666)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        conditionalSendToLabel(1100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(1110)
    if CharacterIDCheck('no'):
        conditionalSendToLabel(1120)
    if CharacterIDCheck('rc'):
        conditionalSendToLabel(1130)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(1200)
    if CharacterIDCheck('hz'):
        conditionalSendToLabel(1230)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(1280)
    if CharacterIDCheck('am'):
        conditionalSendToLabel(1300)
    if CharacterIDCheck('az'):
        if SLOT_140:
            gotoLabel(2320)
        else:
            gotoLabel(1320)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(1330)
    if CharacterIDCheck('kk'):
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(1340)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(1350)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(1390)
    if CharacterIDCheck('nt'):
        conditionalSendToLabel(1400)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(1420)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(2)
    sprite('mi400_00', 6)
    StayAfterMovement(1, 0)
    sprite('mi400_01', 6)
    sprite('mi400_02', 6)
    sprite('mi400_03', 6)
    sprite('mi400_04', 6)
    sprite('mi400_05', 6)
    sprite('mi400_06', 6)
    CreateObject('mi600_HukuGround', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddScale(500)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)

    def RunOnObject_22():
        Visibility(1)
        AbsoluteY(1800000)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CameraControlEnable(1)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    RandomVoiceline('mi406', 100, 'mi407', 100, '', 0, '', 0)
    DemoEndOnVoiceEnd(1)
    label(1)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')

    def RunOnObject_22():
        Visibility(1)
        AbsoluteY(1800000)
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi408')
    DemoEndOnVoiceEnd(1)
    label(3)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(3)
    label(666)
    sprite('mi615_00', 7)
    ObjectUpon2(11, 615, 0)
    sprite('mi615_01', 7)
    sprite('mi615_02', 7)
    sprite('mi615_03', 7)
    PrivateSE('mise_00')
    sprite('mi615_04', 7)
    sprite('mi615_05', 7)
    sprite('mi615_06', 7)
    RandomVoiceline('mi406', 100, 'mi407', 100, 'mi408', 100, '', 0)
    DemoEndOnVoiceEnd(1)
    sprite('mi615_07', 7)
    sprite('mi615_08', 7)
    sprite('mi615_09', 32767)
    loopRest()
    label(1100)
    if SLOT_123:
        conditionalSendToLabel(666)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi501')
    DemoEndOnVoiceEnd(1)
    label(1101)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(1101)
    label(1110)
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 90)
    Voiceline('mi503')
    DemoEndOnVoiceEnd(1)
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    label(1120)
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    Voiceline('mi505')
    DemoEndOnVoiceEnd(1)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    label(1130)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi507')
    DemoEndOnVoiceEnd(1)
    label(1131)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(1131)
    label(1200)
    sprite('mi400_00', 6)
    StayAfterMovement(1, 0)
    sprite('mi400_01', 6)
    sprite('mi400_02', 6)
    sprite('mi400_03', 6)
    sprite('mi400_04', 6)
    sprite('mi400_05', 6)
    sprite('mi400_06', 6)
    CreateObject('mi600_HukuGround', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddScale(500)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CameraControlEnable(1)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    Voiceline('mi521')
    DemoEndOnVoiceEnd(1)
    label(1201)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1201)
    label(1230)
    sprite('mi400_00', 6)
    StayAfterMovement(1, 0)
    sprite('mi400_01', 6)
    sprite('mi400_02', 6)
    sprite('mi400_03', 6)
    sprite('mi400_04', 6)
    sprite('mi400_05', 6)
    sprite('mi400_06', 6)
    CreateObject('mi600_HukuGround', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddScale(500)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)
    loopRest()
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CameraControlEnable(1)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    Voiceline('mi527')
    DemoEndOnVoiceEnd(1)
    label(1231)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1231)
    label(1280)
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    Voiceline('mi537')
    DemoEndOnVoiceEnd(1)
    label(1281)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1281)
    label(1300)
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    Voiceline('mi541')
    DemoEndOnVoiceEnd(1)
    label(1301)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1301)
    label(1320)
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    Voiceline('mi545')
    DemoEndOnVoiceEnd(1)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    ExitState()
    label(2320)
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    Voiceline('mi545')
    DemoEndOnVoiceEnd(1)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    ExitState()
    label(1330)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi547')
    DemoEndOnVoiceEnd(1)
    label(1331)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(1331)
    ExitState()
    label(2330)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi547')
    DemoEndOnVoiceEnd(1)
    label(2331)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(2331)
    label(1340)
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    Voiceline('mi549')
    DemoEndOnVoiceEnd(1)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    ExitState()
    label(2340)
    sprite('mi611_00', 7)
    ObjectUpon2(11, 611, 0)
    CreateObject('mi611_Camera', -1)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi611_01', 7)
    EnableAfterimage(1)
    ForceFloorReflectOff(1)
    ForceShadowOff(1)
    sprite('mi611_02', 7)
    sprite('mi611_03', 7)
    CreateObject('mi611_Soul', 0)
    PrivateSE('mise_01')
    PrivateSE('mise_01')
    sprite('mi611_04', 7)
    sprite('mi611_05', 7)
    sprite('mi611_06', 7)
    sprite('mi611_07', 7)
    sprite('mi611_08', 7)
    sprite('mi611_09', 7)
    sprite('mi611_10', 7)
    CreateObject('mi611_Ray', -1)
    sprite('mi611_11', 7)
    loopRest()
    TriggerUponForState('FunnelMatchWin2', 32)
    Voiceline('mi549')
    DemoEndOnVoiceEnd(1)
    label(2341)
    sprite('mi611_12', 7)
    sprite('mi611_13', 7)
    sprite('mi611_14', 7)
    sprite('mi611_15', 7)
    loopRest()
    gotoLabel(2341)
    label(1350)
    sprite('mi300_00', 7)
    sprite('mi300_01', 7)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    Voiceline('mi551')
    DemoEndOnVoiceEnd(1)
    sprite('mi300_06', 32767)
    loopRest()
    ExitState()
    label(1390)
    sprite('mi610_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi610_01', 8)
    sprite('mi610_02', 8)
    sprite('mi610_03', 8)
    sprite('mi610_04', 4)
    sprite('mi610_04', 4)
    sprite('mi610_05', 8)
    CreateParticle('mief600_flash', -1)
    StopCharacterFlash1(-2960641)
    CharacterFlash(0, 30, 1)
    CommonSE('022_magiccircle_b')
    sprite('mi610_06', 8)
    CameraControlEnable(1)
    CreateObject('mi610_Kaiho', -1)
    PaletteIndex(6)
    Voiceline('mi559')
    DemoEndOnVoiceEnd(1)
    label(1391)
    sprite('mi610_07', 8)
    sprite('mi610_08', 8)
    sprite('mi610_09', 8)
    sprite('mi610_10', 8)
    loopRest()
    gotoLabel(1391)
    ExitState()
    label(1400)
    sprite('mi400_00', 6)
    StayAfterMovement(1, 0)
    sprite('mi400_01', 6)
    Voiceline('mi561')
    DemoEndOnVoiceEnd(1)
    sprite('mi400_02', 6)
    sprite('mi400_03', 6)
    sprite('mi400_04', 6)
    sprite('mi400_05', 6)
    sprite('mi400_06', 6)
    CreateObject('mi600_HukuGround', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddScale(500)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
    sprite('mi400_07', 6)
    sprite('mi400_08', 6)
    sprite('mi400_09', 6)
    sprite('mi400_10', 6)
    loopRest()
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    label(1420)
    sprite('mi620_00', 7)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 7)
    sprite('mi620_02', 7)
    sprite('mi620_03', 7)
    sprite('mi620_04', 7)
    sprite('mi620_05', 7)
    Voiceline('mi565')
    DemoEndOnVoiceEnd(1)
    sprite('mi620_06', 7)
    sprite('mi620_07', 7)
    sprite('mi620_08', 7)
    sprite('mi620_09', 32767)
    loopRest()
    label(9999)
    sprite('mi203_11', 3)
    sprite('mi203_10', 3)
    sprite('mi203_09', 3)
    sprite('mi204_00', 5)
    ObjectUpon2(11, 204, 0)
    sprite('mi204_01', 5)
    sprite('mi204_02', 5)
    sprite('mi204_03', 5)
    sprite('mi203_02', 5)
    sprite('mi204_04', 5)
    CreateObject('FunnelThudenrEffShunou', 100)
    sprite('mi203_01', 5)
    sprite('mi203_00', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActLose():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi620_00', 6)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 6)
    sprite('mi620_02', 6)
    sprite('mi620_03', 6)
    sprite('mi620_04', 6)
    sprite('mi620_05', 6)
    Voiceline('mi411')
    sprite('mi620_06', 6)
    sprite('mi620_07', 6)
    sprite('mi620_08', 6)
    sprite('mi620_09', 32767)
    DemoTimer(90)


@State
def EventDefEntryWait():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
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
def EventDefChouhatsuLoop():
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 32767)
    loopRest()


@State
def EventDefChouhatsuLoopEnd():
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Chouhatsu():
    sprite('mi300_00', 6)
    sprite('mi300_01', 6)
    sprite('mi300_02', 6)
    sprite('mi300_03', 6)
    sprite('mi300_04', 6)
    sprite('mi300_05', 6)
    sprite('mi300_06', 32767)
    loopRest()


@State
def Act2Event_ChouhatsuEnd():
    sprite('mi300_07', 6)
    sprite('mi300_08', 6)
    sprite('mi300_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventBurstLoop():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi331_00', 6)
    sprite('mi331_01', 6)
    sprite('mi331_02', 6)
    sprite('mi331_03', 6)
    sprite('mi331_04', 6)
    sprite('mi331_05', 6)
    label(0)
    sprite('mi331_06', 6)
    sprite('mi331_07', 6)
    sprite('mi331_08', 6)
    loopRest()
    gotoLabel(0)


@State
def EventBurstLoopWait():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    label(0)
    sprite('mi331_06', 6)
    sprite('mi331_07', 6)
    sprite('mi331_08', 6)
    loopRest()
    gotoLabel(0)


@State
def EventBurstLoopEnd():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi331_09', 6)
    sprite('mi331_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Entry():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
    sprite('mi600_00', 1)
    sprite('mi600_00', 1)
    PaletteIndex(6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi600_00', 32767)
    loopRest()


@State
def Act2Event_EntryEnd():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi600_00', 8)
    CommonSE('019_cloth_c')
    sprite('mi600_01', 8)
    sprite('mi600_02', 8)
    PaletteIndex(0)
    CreateObject('mi600_Huku', -1)
    sprite('mi600_03', 8)
    CommonSE('019_cloth_b')
    sprite('mi600_04', 8)
    sprite('mi600_05', 8)
    sprite('mi600_06', 8)
    sprite('mi600_07', 8)
    sprite('mi600_08', 8)
    CreateObject('mi600_Cicle', -1)
    PrivateSE('mise_01')
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_08', 8)
    sprite('mi600_09', 8)
    sprite('mi600_10', 8)
    sprite('mi600_11', 8)
    sprite('mi600_12', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Lose():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi620_00', 6)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 6)
    sprite('mi620_02', 6)
    sprite('mi620_03', 6)
    sprite('mi620_04', 6)
    sprite('mi620_05', 6)
    sprite('mi620_06', 6)
    sprite('mi620_07', 6)
    sprite('mi620_08', 6)
    sprite('mi620_09', 32767)
    loopRest()


@State
def Act2Event_Down():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi063_11', 32767)
    loopRest()


@State
def Act2Event_Blue():
    sprite('keep', 2)
    sprite('mi431_00', 6)
    ObjectUpon2(11, 431, 0)
    EndMomentum(1)
    sprite('mi431_01', 6)
    sprite('mi431_02', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    DeleteObject(11)
    label(0)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_BlueEnd():
    sprite('keep', 2)
    sprite('mi431_02', 6)
    sprite('mi431_01', 6)
    sprite('mi431_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoroke():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        XPositionRelativeFacing(-160000)
    sprite('mi070_00', 15)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('mi070_01', 4)
    sprite('mi070_02', 4)
    sprite('mi070_03', 4)
    sprite('mi070_04', 4)
    sprite('mi070_05', 32767)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()


@State
def Act2Event_ptvsmi_00():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi070_10', 6)
    sprite('mi070_11', 6)
    sprite('mi070_12', 6)
    sprite('mi070_13', 6)
    sprite('mi000_00', 8)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    sprite('mi431_00', 6)
    ObjectUpon2(11, 431, 0)
    EndMomentum(1)
    sprite('mi431_01', 6)
    sprite('mi431_02', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    sprite('mi431_03', 6)
    DeleteObject(11)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    label(0)
    sprite('mi431_03', 6)
    sprite('mi431_04', 6)
    sprite('mi431_05', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_mkvsmi_00():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi070_11', 32767)
    loopRest()


@State
def Act2Event_mkvsmi_01():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi070_11', 20)
    sprite('mi070_11', 15)
    CreateObject('mi600_HukuGround', -1)
    ConstantAlphaModifier(-17)
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def Act2Event_ntvsmi_00():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
        XPositionRelativeFacing(-160000)
    sprite('mi070_00', 15)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('mi070_01', 4)
    sprite('mi070_02', 4)
    sprite('mi070_03', 4)
    sprite('mi070_04', 4)
    sprite('mi070_05', 5)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('mi070_10', 6)
    sprite('mi070_11', 32767)
    loopRest()


@State
def Act2Event_ntvsmi_01():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi070_12', 6)
    sprite('mi070_13', 6)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_tgvsmi_00():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_NoDisp():
    sprite('null', 1)
    sprite('null', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_Entry():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_WarpOut():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    sprite('mi620_00', 6)
    CreateObject('mi408_CreateEff', -1)
    sprite('mi620_01', 6)
    sprite('mi620_02', 6)
    sprite('mi620_03', 6)
    sprite('mi620_04', 6)
    sprite('mi620_05', 6)
    sprite('mi620_06', 6)
    sprite('mi620_07', 6)
    sprite('mi620_08', 6)
    sprite('mi620_09', 18)
    sprite('mi620_09', 24)
    CreateObject('Act3Event_EffWarpOut', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi620_09', 32767)
    Visibility(1)
    CommonSE('022_magiccircle_c')
    loopRest()


@State
def Act3Event_mivskg_00():

    def upon_IMMEDIATE():
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)

        def upon_STATE_END():
            ObjectUpon(22, 32)
    sprite('null', 23)
    CreateObject('mi601_doro', -1)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_07')
    sprite('mi601_00', 10)
    CommonSE('012_stab_fast')
    sprite('mi601_01', 10)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_middle')
    sprite('mi601_02', 10)
    sprite('mi601_03', 10)
    PrivateSE('mise_00')
    sprite('mi601_04', 8)
    sprite('mi601_05', 8)
    sprite('mi000_00', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 40)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Turn():
    sprite('mi003_00', 3)
    Flip()
    sprite('mi003_01', 3)
    sprite('mi003_00ex01', 3)
    label(0)
    sprite('mi000_00', 8)
    sprite('mi000_01', 8)
    sprite('mi000_02', 8)
    sprite('mi000_03', 8)
    sprite('mi000_04', 8)
    sprite('mi000_05', 8)
    sprite('mi000_06', 8)
    sprite('mi000_07', 8)
    sprite('mi000_08', 8)
    sprite('mi000_09', 8)
    loopRest()
    gotoLabel(0)
