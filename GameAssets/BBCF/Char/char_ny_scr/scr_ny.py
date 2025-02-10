@Subroutine
def PreInit():
    CharacterID('ny')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(10000)
    WalkFSpeed(5500)
    WalkBSpeed(5000)
    DashFInitialVelocity(22000)
    DashFAccel(320)
    DashFMaxVelocity(30000)
    JumpYVelocity(33000)
    SuperJumpYVelocity(40000)
    ForwardJumpVelocity(7600)
    ForwardSuperJumpVelocity(11000)
    BackwardJumpVelocity(7000)
    BackwardSuperJumpVelocity(9000)
    Gravity(1700)
    AirDashFSpeed(30000)
    AirFDashDuration(18)
    AirDashBSpeed(29000)
    AirBDashDuration(12)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    LandPreJumpActionNormalAttackAvailable(60)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepSE(4)
    CreateDecalOn(1)
    if SLOT_116:
        Health(13000)
        WalkFSpeed(8250)
        WalkBSpeed(7500)
        DashFInitialVelocity(27000)
        DashFMaxVelocity(35000)
        AirDashCount(2)
        AirDashFSpeed(36000)
        AirFDashDuration(15)
        AirDashBSpeed(35000)
        AirBDashDuration(10)
        OverdriveDuration(780, 780, 780, 780, 780, 780, 780, 780, 780, 780)
    ResourceGauge(0, 1, 17, 1, 240, 240, -12583009, -12583009)
    ResourceBarFlashIfFull(0, 1)
    ResourceBarVisibility(0, 1)
    CPURetreatPriority(5000)
    Move_Register('SpecialDashF', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    Unknown15027(0)
    DamageStunPriority(0)
    GuardStunPriority(2000)
    AddChain(1)
    SkillEstimateRange(0, 400000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_44)
    FollowupOnly(1)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    AddChain(1)
    SkillEstimateRange(450000, 850000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashAirF', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_66)
    Move_Condition(0x2007)
    FollowupOnly(1)
    Move_Condition(0x3036)
    Unknown15027(0)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    AddChain(1)
    SkillEstimateRange(450000, 1250000, -500000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashAirB', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_44)
    Move_Condition(0x2007)
    FollowupOnly(1)
    Move_Condition(0x3036)
    GuardStunPriority(2000)
    AddChain(1)
    SkillEstimateRange(450000, 1250000, -500000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    DamageStunPriority(1500)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 350000, -200000, 300000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 400000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Atk6B_Input5', 0x1)
    StateCall('NmlAtk6B')
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x2000)
    SkillEstimateRange(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    SkillEstimateRange(0, 350000, -100000, 130000, 1000, 50)
    MoveLow()
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    MoveCancellableFrames(35, 36)
    DamageStunPriority(250)
    SkillEstimateRange(300000, 500000, -200000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    AirborneOpponentPriority(1500)
    DamageStunPriority(1500)
    MoveCancellableFrames(35, 37)
    SkillEstimateRange(0, 550000, -100000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    MoveCancellableFrames(25, 26)
    SkillEstimateRange(-100000, 250000, -100000, 400000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    MoveCancellableFrames(28, 30)
    SkillEstimateRange(0, 550000, -100000, 160000, 1000, 50)
    Move_EndRegister()
    Move_Register('TimelagShot_Atk', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_D)
    IndependentInput(1, 0, 0)
    CallSkillConditions('CheckLockReject')
    CallFunction('Func_TimelagShot_Atk')
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    MoveMaxChainRepeat(3)
    DisallowSameSkill(1)
    DamageStunPriority(1500)
    SkillEstimateRange(350000, 1200000, -200000, 180000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(5000)
    SkillEstimateRange(350000, 1200000, -200000, 250000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6D_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(400000, 1000000, 30000, 800000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4D_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(550000, 1800000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2D_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(150000, 850000, 300000, 1200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    SharedGatling('NmlAtk5D')
    DisallowSameSkill(1)
    AirborneOpponentPriority(2500)
    GuardStunPriority(1)
    SkillEstimateRange(400000, 1000000, 200000, 800000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4D', INPUT_4D)
    SharedGatling('NmlAtk5D')
    DisallowSameSkill(1)
    MoveMid()
    AirborneOpponentPriority(1)
    OpponentAttackPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(550000, 1800000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    SharedGatling('NmlAtk5D')
    DisallowSameSkill(1)
    AirborneOpponentPriority(2000)
    GuardStunPriority(1)
    SkillEstimateRange(300000, 700000, 400000, 1200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    MoveMaxChainRepeat(3)
    DisallowSameSkill(1)
    SkillEstimateRange(350000, 900000, 50000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_2nd', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(200000, 1200000, 50000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2D_2nd', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(200000, 1200000, -300000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6D_2nd', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveComboPriority(10000)
    DamageStunPriority(2000)
    SkillEstimateRange(200000, 1200000, -300000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2D', INPUT_J2D)
    SharedGatling('NmlAtkAIR5D')
    DisallowSameSkill(1)
    SkillEstimateRange(250000, 650000, -400000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6D', INPUT_J6D)
    Move_Input_(0xa7)
    SharedGatling('NmlAtkAIR5D')
    DisallowSameSkill(1)
    SkillEstimateRange(350000, 900000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    DamageStunPriority(1500)
    SkillEstimateRange(100000, 450000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    MoveCancellableFrames(28, 30)
    DamageStunPriority(2000)
    SkillEstimateRange(-100000, 400000, -250000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    MoveCancellableFrames(28, 30)
    DamageStunPriority(1500)
    SkillEstimateRange(-100000, 350000, -250000, 150000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 300000, -200000, 200000, 500, 0)
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
    SkillEstimateRange(30000, 210000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('LargeShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x3008)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(0x5)
    CPUUsable(0)
    PlayerUsable(0)
    OpponentAttackPriority(1)
    MoveComboPriority(1)
    MoveButtonHoldTime(3, 15, 25)
    SkillEstimateRange(1000000, 1500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('LargeShot_2nd', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_HOLD_C)
    Move_Condition(0x306c)
    CPUUsable(0)
    PlayerUsable(0)
    SkillEstimateRange(1000000, 1500000, -200000, 600000, 5000, 50)
    Move_EndRegister()
    Move_Register('GedanShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(1)
    SkillEstimateRange(150000, 750000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('GedanShot_2nd', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_HOLD_C)
    MoveCPULevel(700, 1000, 50, 1000)
    SkillEstimateRange(900000, 1500000, -200000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('ChudanShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(250000, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('ChudanShot_2nd', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_HOLD_C)
    Move_Condition(0x3002)
    Move_EndRegister()
    Move_Register('TimelagShot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x300d)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(0x5)
    OpponentAttackPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(2000)
    MoveButtonHoldTime(3, 15, 25)
    SkillEstimateRange(700000, 1500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('BackAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(1500)
    MoveComboPriority(1)
    SkillEstimateRange(-100000, 300000, -50000, 500000, 750, 0)
    Move_EndRegister()
    Move_Register('BackAssault_Air', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    MoveComboPriority(1)
    SkillEstimateRange(-100000, 300000, -200000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('SlowFieldA', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x302e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(0)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 700000, -200000, 500000, 250, 50)
    Move_EndRegister()
    Move_Register('SlowFieldB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x302e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(0)
    MoveComboPriority(0)
    GuardStunPriority(1500)
    SkillEstimateRange(700000, 1200000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('SlowFieldC', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x302e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(0)
    MoveComboPriority(0)
    GuardStunPriority(1500)
    SkillEstimateRange(1200000, 2000000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('UltimateMultiSword', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xcf)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    SkillEstimateRange(500000, 1800000, -200000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('UltimateMultiSwordOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xcf)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    DamageStunPriority(5000)
    SkillEstimateRange(500000, 1800000, -200000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordLand', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(3000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveCPULevel(700, 1000, 50, 1000)
    SkillEstimateRange(150000, 450000, -200000, 400000, 1000, 10)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordLandOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(3000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    MoveCPULevel(700, 1000, 50, 1000)
    SkillEstimateRange(150000, 450000, -200000, 400000, 1000, 10)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordAir', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(1)
    MoveCPULevel(700, 1000, 50, 1000)
    SkillEstimateRange(0, 400000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordAirOD', INPUT_DISTORTION)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    MovePriority(1)
    MoveCPULevel(700, 1000, 50, 1000)
    SkillEstimateRange(0, 400000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_PRESS_D)
    GuardStunPriority(1500)
    MoveComboPriority(5000)
    SkillEstimateRange(0, 125000, -200000, 150000, 1000, 5)
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
    SkillEstimateRange(350000, 1200000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(350000, 1200000, -200000, 200000, 500, 10)
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
    SkillEstimateRange(350000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6A', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'BHighJump', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'BackAssault', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'GedanShot', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'BackAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'GedanShot', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'UltimateMultiSword', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR2C', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'NmlAtk5D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'SlowFieldB', 10000000)
    TempPriorityMultiplier('NmlAtk5D', 'SlowFieldC', 10000000)
    TempPriorityMultiplier('NmlAtk5D_2nd', 'NmlAtk4D', 10000000)
    TempPriorityMultiplier('NmlAtk5D_2nd', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk4D', 'NmlAtk4D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtk4D_2nd', 'GedanShot', 10000000)
    TempPriorityMultiplier('NmlAtk6D', 'NmlAtk6D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtk6D_2nd', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk2D', 'NmlAtk2D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtk2D_2nd', 'BHighJump', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5D', 'NmlAtkAIR5D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5D_2nd', 'NmlAtkAIR6D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR6D', 'NmlAtkAIR6D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtkAIR6D_2nd', 'NmlAtkAIR2D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR6D_2nd', 'ChudanShot', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2D', 'NmlAtkAIR2D_2nd', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2D_2nd', 'ChudanShot', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2D_2nd', 'SpecialDashAirB', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2D_2nd', 'UltimateLargeSwordAir', 10000000
        )
    TempPriorityMultiplier('NmlAtkAIR2D_2nd', 'UltimateLargeSwordAirOD', 
        10000000)
    TempPriorityMultiplier('GedanShot', 'LargeShot', 10000000)
    TempPriorityMultiplier('AntiAir', 'SlowFieldA', 10000000)
    StylishModeSpecialButton('BackAssault', 0x4, 0xea)
    StylishModeSpecialButton('GedanShot', 0x4, 0x79)
    StylishModeSpecialButton('UltimateLargeSwordLand', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateLargeSwordLandOD', 0x4, 0x5f)
    StylishModeSpecialButton('TimelagShot', 0x4, 0x45)
    StylishModeSpecialButton('BackAssault_Air', 0x4, 0xea)
    StylishModeSpecialButton('UltimateLargeSwordAir', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateLargeSwordAirOD', 0x4, 0x5f)
    StylishModeSpecialButton('ChudanShot', 0x4, 0x45)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 1, 200000)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 12, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk6C', 12, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk6C', 'GedanShot', 0, 0)
    StylishModeCancels('NmlAtk6C', 'UltimateMultiSword', 3, 0)
    StylishModeCancels('NmlAtk6C', 'UltimateMultiSwordOD', 3, 0)
    StylishModeCancels('NmlAtk5D', 'NmlAtk5D_2nd', 0, 0)
    StylishModeCancels('NmlAtk5D_2nd', 'NmlAtk4D', 0, 0)
    StylishModeCancels('NmlAtk5D_2nd', 'GedanShot', 1, 700000)
    StylishModeCancels('NmlAtk5D_2nd', 'NmlAtk6D', 3, 0)
    StylishModeCancels('NmlAtk6D', 'NmlAtk6D_2nd', 0, 0)
    StylishModeCancels('NmlAtk6D_2nd', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk4D', 'NmlAtk4D_2nd', 0, 0)
    StylishModeCancels('NmlAtk4D_2nd', 'GedanShot', 0, 0)
    StylishModeCancels('NmlAtk4D_2nd', 'NmlAtk2D', 3, 0)
    StylishModeCancels('NmlAtk4D_2nd', 'SlowFieldC', 13, 0)
    StylishModeCancels('NmlAtk2D', 'NmlAtk2D_2nd', 0, 0)
    StylishModeCancels('NmlAtk2D_2nd', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk2D_2nd', 'VHighJump', 1, 600000)
    StylishModeCancels('GedanShot', 'SlowFieldC', 0, 0)
    StylishModeCancels('BackAssault', 'SlowFieldB', 0, 0)
    StylishModeCancels('SlowFieldB', 'NmlAtk5D', 0, 0)
    StylishModeCancels('SlowFieldB', 'NmlAtk5C', 10, 600000)
    StylishModeCancels('SlowFieldC', 'TimelagShot', 0, 0)
    StylishModeCancels('SlowFieldC', 'NmlAtk5C', 10, 600000)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5B', 1, 200000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk6B', 1, 200000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk2C', 12, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk3C', 'GedanShot', 0, 0)
    StylishModeCancels('NmlAtk3C', 'BackAssault', 1, 250000)
    StylishModeCancels('NmlAtk3C', 'UltimateLargeSwordLand', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateLargeSwordLandOD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 10, 400000)
    StylishModeCancels('NmlAtk3C', 'GedanShot', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5A', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 2, 100000)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR2C', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'ChudanShot', 3, 0)
    StylishModeCancels('NmlAtkAIR2C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR2C', 'ChudanShot', 3, 0)
    StylishModeCancels('NmlAtkAIR5D', 'NmlAtkAIR5D_2nd', 0, 0)
    StylishModeCancels('NmlAtkAIR5D_2nd', 'FJump', 0, 0)
    StylishModeCancels('NmlAtkAIR5D_2nd', 'NmlAtkAIR6D', 2, 320000)
    StylishModeCancels('NmlAtkAIR2D', 'NmlAtkAIR2D_2nd', 0, 0)
    StylishModeCancels('NmlAtkAIR2D_2nd', 'NmlAtkAIR6D', 0, 0)
    StylishModeCancels('NmlAtkAIR2D_2nd', 'NmlAtkAIR5D', 12, 0)
    StylishModeCancels('NmlAtkAIR2D_2nd', 'NmlAtkAIR6D', 13, 0)
    StylishModeCancels('NmlAtkAIR6D', 'NmlAtkAIR6D_2nd', 0, 0)
    StylishModeCancels('NmlAtkAIR6D_2nd', 'NmlAtkAIR2D', 0, 0)
    StylishModeCancels('NmlAtkAIR6D_2nd', 'ChudanShot', 6, 0)
    StylishModeCancels('NmlAtkAIR6D_2nd', 'FJump', 12, 0)
    StylishModeCancels('ThrowExe', 'NmlAtk5D', 0, 0)
    StylishModeCancels('ThrowExe', 'BackAssault', 10, 650000)
    StylishModeCancels('BackThrowExe', 'SlowFieldB', 0, 0)
    StylishModeCancels('BackThrowExe', 'NmlAtk6D', 10, 3200000)
    HitSprites(0, 'ny062_01')
    HitSprites(1, 'ny062_03')
    HitSprites(2, 'ny062_04')
    HitSprites(3, 'ny062_05')
    HitSprites(4, 'ny062_06')
    HitSprites(5, 'ny062_07')
    HitSprites(6, 'ny062_09')
    HitSprites(7, 'ny041_02')
    HitSprites(8, 'ny040_02')
    HitSprites(9, 'ny045_02')
    HitSprites(10, 'ny060_00')
    HitSprites(11, 'ny060_01')
    HitSprites(12, 'ny060_03')
    HitSprites(13, 'ny060_05')
    HitSprites(14, 'ny060_07')
    HitSprites(15, 'ny060_14')
    HitSprites(16, 'ny050_00')
    HitSprites(17, 'ny052_00')
    HitSprites(18, 'ny054_00')
    HitSprites(19, 'ny000_00')
    HitSprites(20, 'ny000_00')
    HitSprites(25, 'ny063_00')
    HitSprites(26, 'ny063_01')
    HitSprites(27, 'ny063_02')
    HitSprites(28, 'ny063_05')
    HitSprites(29, 'ny063_11')
    HitSprites(30, 'ny077_00')
    HitSprites(31, 'ny077_01')
    HitSprites(32, 'ny077_00ex00')
    HitSprites(33, 'ny077_01ex00')
    HitSprites(34, 'ny077_00ex01')
    HitSprites(35, 'ny077_01ex01')
    HitSprites(36, 'ny077_00ex02')
    HitSprites(37, 'ny077_01ex02')
    HitSprites(24, 'ny073_01')
    CommonVoicelines(0, 'ny000')
    CommonVoicelines(1, 'ny001')
    CommonVoicelines(2, 'ny002')
    CommonVoicelines(3, 'ny003')
    CommonVoicelines(4, 'ny004')
    CommonVoicelines(5, 'ny005')
    CommonVoicelines(6, 'ny006')
    CommonVoicelines(7, 'ny007')
    CommonVoicelines(8, 'ny008')
    CommonVoicelines(9, 'ny009')
    CommonVoicelines(10, 'ny010')
    CommonVoicelines(11, 'ny011')
    CommonVoicelines(12, 'ny012')
    CommonVoicelines(13, 'ny013')
    CommonVoicelines(14, 'ny014')
    CommonVoicelines(15, 'ny015')
    CommonVoicelines(16, 'ny016')
    CommonVoicelines(17, 'ny017')
    CommonVoicelines(18, 'ny018')
    CommonVoicelines(19, 'ny019')
    CommonVoicelines(20, 'ny020')
    CommonVoicelines(21, 'ny021')
    CommonVoicelines(22, 'ny022')
    CommonVoicelines(23, 'ny023')
    CommonVoicelines(24, 'ny024')
    CommonVoicelines(25, 'ny025')
    CommonVoicelines(26, 'ny026')
    CommonVoicelines(27, 'ny027')
    CommonVoicelines(28, 'ny028')
    CommonVoicelines(29, 'ny029')
    CommonVoicelines(30, 'ny030')
    CommonVoicelines(31, 'ny031')
    CommonVoicelines(32, 'ny032')
    CommonVoicelines(33, 'ny033')
    CommonVoicelines(34, 'ny034')
    CommonVoicelines(35, 'ny035')
    CommonVoicelines(36, 'ny036')
    CommonVoicelines(37, 'ny037')
    CommonVoicelines(38, 'ny038')
    CommonVoicelines(39, 'ny039')
    CommonVoicelines(40, 'ny040')
    CommonVoicelines(41, 'ny041')
    CommonVoicelines(42, 'ny042')
    CommonVoicelines(43, 'ny043')
    CommonVoicelines(44, 'ny044')
    CommonVoicelines(45, 'ny045')
    CommonVoicelines(46, 'ny046')
    CommonVoicelines(47, 'ny047')
    CommonVoicelines(48, 'ny048')
    CommonVoicelines(49, 'ny049')
    CommonVoicelines(50, 'ny050')
    CommonVoicelines(51, 'ny051')
    CommonVoicelines(52, 'ny052')
    CommonVoicelines(53, 'ny053')
    CommonVoicelines(54, 'ny100')
    CommonVoicelines(55, 'ny101')
    CommonVoicelines(56, 'ny102')
    CommonVoicelines(57, 'ny103')
    CommonVoicelines(58, 'ny104')
    CommonVoicelines(59, 'ny105')
    CommonVoicelines(60, 'ny108')
    CommonVoicelines(61, 'ny108')
    CommonVoicelines(62, 'ny108')
    CommonVoicelines(63, 'ny108')
    CommonVoicelines(64, 'ny150')
    CommonVoicelines(65, 'ny151')
    CommonVoicelines(66, 'ny152')
    CommonVoicelines(67, 'ny153')
    CommonVoicelines(68, 'ny154')
    CommonVoicelines(69, 'ny155')
    CommonVoicelines(70, 'ny156')
    CommonVoicelines(71, 'ny157')
    CommonVoicelines(72, 'ny158')
    CommonVoicelines(75, 'ny160')
    CommonVoicelines(73, 'ny402')
    CommonVoicelines(74, 'ny403')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnEnemyComboBreak():
    SLOT_62 = 0


@Subroutine
def DriveVoice():
    SLOT_62 = SLOT_62 + 1
    if SLOT_62 == 1:
        pass
    elif SLOT_62 == 2:
        Voiceline('ny302')
    elif SLOT_62 == 3:
        Voiceline('ny303')
    elif SLOT_62 == 4:
        Voiceline('ny304')
    elif SLOT_62 == 5:
        Voiceline('ny305')
    elif SLOT_62 == 6:
        Voiceline('ny306')
    elif SLOT_62 == 7:
        Voiceline('ny307')
    elif SLOT_62 == 8:
        Voiceline('ny308')
    elif SLOT_62 == 9:
        Voiceline('ny309')
    elif SLOT_62 == 10:
        Voiceline('ny310')
    elif SLOT_62 == 11:
        Voiceline('ny311')
    elif SLOT_62 == 12:
        Voiceline('ny312')
    elif SLOT_62 == 13:
        Voiceline('ny313')
    elif SLOT_62 == 14:
        Voiceline('ny314')
    elif SLOT_62 == 15:
        Voiceline('ny315')
    elif SLOT_62 == 16:
        Voiceline('ny316')
    elif SLOT_62 == 17:
        Voiceline('ny317')
    elif SLOT_62 == 18:
        Voiceline('ny318')
    elif SLOT_62 == 19:
        Voiceline('ny319')
    elif SLOT_62 == 20:
        Voiceline('ny320')
    elif SLOT_62 >= 21:
        SmartVoiceline('ny321')


@Subroutine
def OnFinalize():
    AddActionMark(0)
    CopyFromRightToLeft(23, 2, 71, 22, 2, 30)
    if not SLOT_71:
        SLOT_62 = 0


@Subroutine
def OnPreDraw():
    CallPrivateFunction('NY_Light', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def CheckLockReject():
    if not CurrentStateCheck('CmnActLockReject'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('CmnActAirLockReject'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('CmnActOverDriveLoop'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('CmnActAirOverDriveLoop'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('CmnActAirOverDriveEnd'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if not CurrentStateCheck('TimelagShot'):
        SLOT_47 = 1
    else:
        SLOT_47 = 0


@Subroutine
def Func_TimelagShot_Atk():
    TriggerUponForState('TimelagShot_Obj_Summon', 41)


@Subroutine
def MatchInit2():
    pass


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_21:
            if SLOT_116:
                HeatChange(3)
        if SLOT_21:
            if SLOT_IsUnlimited:
                HeatChange(2)
        SLOT_31 = SLOT_31 + 1
        if SLOT_OverdriveTimer:
            SLOT_31 = SLOT_31 + 1
        if SLOT_31 >= 240:
            ResourceGaugeX(0, 0)
        else:
            ResourceGaugeX(0, 1)
    if SLOT_IsGrounded:
        SLOT_6 = 1
    TrainingModeSLOT('TRI_RambdasGravity', 2, 67)
    if SLOT_67:
        if SLOT_InNeutral:
            SLOT_31 = SLOT_31 + 100000


@State
def CmnActStand():
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('ny000_00', 1)
    SLOT_88 = 960
    Voiceline('ny000')
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('ny003_02', 3)
    sprite('ny003_01', 3)
    SmartVoiceline('ny001')
    sprite('ny003_00', 3)


@State
def CmnActStand2Crouch():
    sprite('ny010_00', 4)
    sprite('ny010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('ny010_02', 6)
    sprite('ny010_03', 6)
    sprite('ny010_04', 6)
    sprite('ny010_05', 6)
    sprite('ny010_06', 6)
    sprite('ny010_07', 6)
    sprite('ny010_08', 6)
    sprite('ny010_09', 6)
    sprite('ny010_10', 6)
    sprite('ny010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('ny013_02', 3)
    sprite('ny013_01', 3)
    sprite('ny013_00', 3)


@State
def CmnActCrouch2Stand():
    sprite('ny010_01', 4)
    sprite('ny010_00', 4)


@State
def CmnActJumpPre():
    sprite('ny023_00', 2)
    PrivateSE('nyse_03')
    sprite('ny023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('ny020_00', 3)
    sprite('ny020_01', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('ny020_02', 3)
    sprite('ny020_03', 4)


@State
def CmnActJumpDown():
    sprite('ny020_04', 3)
    sprite('ny020_05', 3)
    label(0)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('ny024_00', 3)
    CommonSE('205_runjump_garden_0')
    sprite('ny024_01', 3)
    sprite('ny024_02', 3)
    sprite('ny024_03', 3)
    sprite('ny024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('ny024_00', 2)
    sprite('ny024_01', 2)
    sprite('ny024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('ny024_03', 3)
    sprite('ny024_04', 3)


@State
def CmnActFWalk():
    sprite('ny030_00', 7)
    label(0)
    sprite('ny030_01', 7)
    PrivateSE('GG2_218SE')
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_02', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_03', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_04', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_05', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_06', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_07', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_08', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_09', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_10', 7)
    CreateParticle('nyef_ny030', -1)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('ny031_00', 7)
    label(0)
    sprite('ny031_01', 7)
    PrivateSE('GG2_218SE')
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_02', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_03', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_04', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_05', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_06', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_07', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_08', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_09', 7)
    CreateParticle('nyef_ny031', -1)
    sprite('ny031_10', 7)
    CreateParticle('nyef_ny031', -1)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('ny032_00', 2)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    label(0)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('ny032_05', 4)
    PrivateSE('nyse_22')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_06', 4)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        InvincibilityDuration(7)
        EndMomentum(1)
    sprite('ny033_00', 2)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    SmartVoiceline('ny005')
    sprite('ny033_00', 2)
    PrivateSE('nyse_22')
    physicsXImpulse(-36000)
    sprite('ny033_01', 2)
    CreateParticle('nyef_ny033', 106)
    sprite('ny033_02', 2)
    CreateParticle('nyef_ny033', 106)
    sprite('ny033_03', 2)
    sprite('ny033_04', 1)
    XImpulseAcceleration(70)
    sprite('ny033_04', 1)
    XImpulseAcceleration(70)
    sprite('ny033_01', 1)
    XImpulseAcceleration(70)
    sprite('ny033_01', 1)
    XImpulseAcceleration(70)
    sprite('ny033_01', 1)
    XImpulseAcceleration(70)
    sprite('ny033_01', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)


@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)
    sprite('ny033_06', 4)


@State
def CmnActAirFDash():
    sprite('ny035_00', 2)
    SmartVoiceline('ny004')
    sprite('ny035_01', 3)
    sprite('ny035_02', 3)
    sprite('ny035_03', 3)
    sprite('ny035_04', 3)
    sprite('ny035_05', 3)
    sprite('ny035_06', 3)


@State
def CmnActAirBDash():
    sprite('ny036_00', 2)
    SmartVoiceline('ny006')
    sprite('ny036_01', 2)
    sprite('ny036_02', 2)
    sprite('ny036_03', 2)
    sprite('ny036_04', 2)
    sprite('ny036_05', 3)
    sprite('ny036_06', 3)


@State
def CmnActHitStandLv1():
    sprite('ny050_00', 1)
    sprite('ny050_01', 7)
    sprite('ny050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('ny050_01', 1)
    sprite('ny050_02', 7)
    sprite('ny050_01', 2)
    sprite('ny050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('ny050_02', 1)
    sprite('ny050_03', 7)
    sprite('ny050_02', 2)
    sprite('ny050_01', 2)
    sprite('ny050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('ny050_03', 1)
    sprite('ny050_04', 8)
    sprite('ny050_03', 2)
    sprite('ny050_02', 2)
    sprite('ny050_01', 2)
    sprite('ny050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('ny050_04', 1)
    sprite('ny050_04', 8)
    sprite('ny050_04', 2)
    sprite('ny050_03', 2)
    sprite('ny050_02', 2)
    sprite('ny050_01', 2)
    sprite('ny050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('ny052_00', 1)
    sprite('ny052_01', 7)
    sprite('ny052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('ny052_01', 1)
    sprite('ny052_02', 7)
    sprite('ny052_01', 2)
    sprite('ny052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('ny052_02', 1)
    sprite('ny052_03', 7)
    sprite('ny052_02', 2)
    sprite('ny052_01', 2)
    sprite('ny052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('ny052_03', 1)
    sprite('ny052_04', 8)
    sprite('ny052_03', 2)
    sprite('ny052_02', 2)
    sprite('ny052_01', 2)
    sprite('ny052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('ny052_04', 1)
    sprite('ny052_04', 23)
    sprite('ny052_04', 2)
    sprite('ny052_03', 2)
    sprite('ny052_02', 2)
    sprite('ny052_01', 2)
    sprite('ny052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('ny054_00', 1)
    sprite('ny054_01', 9)
    sprite('ny054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('ny054_01', 1)
    sprite('ny054_02', 11)
    sprite('ny054_01', 2)
    sprite('ny054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('ny054_02', 1)
    sprite('ny054_03', 12)
    sprite('ny054_02', 2)
    sprite('ny054_01', 2)
    sprite('ny054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('ny054_03', 1)
    sprite('ny054_04', 12)
    sprite('ny054_03', 2)
    sprite('ny054_02', 2)
    sprite('ny054_01', 2)
    sprite('ny054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('ny054_04', 1)
    sprite('ny054_04', 25)
    sprite('ny054_04', 2)
    sprite('ny054_03', 2)
    sprite('ny054_02', 2)
    sprite('ny054_01', 2)
    sprite('ny054_00', 2)


@State
def CmnActBDownUpper():
    sprite('ny060_00', 4)
    label(0)
    sprite('ny060_01', 4)
    sprite('ny060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('ny060_03', 4)


@State
def CmnActBDownDown():
    sprite('ny060_04', 4)
    label(0)
    sprite('ny060_05', 4)
    sprite('ny060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('ny060_07', 2)
    sprite('ny060_08', 2)


@State
def CmnActBDownBound():
    sprite('ny060_09', 2)
    sprite('ny060_10', 2)
    sprite('ny060_11', 2)
    sprite('ny060_12', 3)
    sprite('ny060_13', 3)


@State
def CmnActBDownLoop():
    sprite('ny060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('ny061_00', 3)
    CommonSE('205_runjump_garden_0')
    PrivateSE('nyse_03')
    sprite('ny061_01', 3)
    sprite('ny061_02', 3)
    sprite('ny061_03', 3)
    sprite('ny061_04', 3)
    sprite('ny061_05', 3)
    sprite('ny061_06', 3)
    sprite('ny061_07', 3)
    sprite('ny061_08', 2)
    sprite('ny061_09', 2)


@State
def CmnActFDownUpper():
    sprite('ny063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('ny063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('ny063_02', 3)
    sprite('ny063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('ny063_04', 3)
    sprite('ny063_05', 3)


@State
def CmnActFDownBound():
    sprite('ny063_06', 2)
    sprite('ny063_07', 2)
    sprite('ny063_08', 3)
    sprite('ny063_09', 3)
    sprite('ny063_10', 3)


@State
def CmnActFDownLoop():
    sprite('ny063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('ny064_00', 2)
    CommonSE('205_runjump_garden_0')
    PrivateSE('nyse_03')
    sprite('ny064_01', 2)
    sprite('ny064_02', 2)
    sprite('ny064_03', 2)
    sprite('ny064_04', 2)
    sprite('ny064_05', 2)
    sprite('ny064_06', 2)
    sprite('ny064_07', 2)
    sprite('ny064_08', 2)
    sprite('ny064_09', 2)


@State
def CmnActVDownUpper():
    sprite('ny062_00', 3)
    label(0)
    sprite('ny062_01', 3)
    sprite('ny062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('ny062_03', 3)
    sprite('ny062_04', 3)


@State
def CmnActVDownDown():
    sprite('ny062_05', 3)
    sprite('ny062_06', 3)
    label(0)
    sprite('ny062_07', 3)
    sprite('ny062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('ny062_09', 2)
    sprite('ny062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('ny062_09', 2)
    sprite('ny062_10', 2)


@State
def CmnActBlowoff():
    sprite('ny072_00', 3)
    sprite('ny072_01', 3)
    sprite('ny072_02', 3)
    label(0)
    sprite('ny072_01', 3)
    sprite('ny072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ny074_00', 3)
    sprite('ny074_01', 3)
    sprite('ny074_02', 3)
    sprite('ny074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('ny082_00', 2)
    sprite('ny082_00', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('ny071_04', 1)


@State
def CmnActWallBound():
    sprite('ny073_00', 3)
    sprite('ny073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('ny073_02', 3)
    label(0)
    sprite('ny073_03', 3)
    sprite('ny073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('ny070_00', 2)
    sprite('ny070_01', 2)
    label(0)
    sprite('ny070_02', 4)
    sprite('ny070_03', 4)
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('ny070_04', 4)
    sprite('ny070_05', 4)
    sprite('ny070_06', 4)
    sprite('ny070_07', 5)
    sprite('ny070_08', 5)
    sprite('ny070_09', 2)


@State
def CmnActUkemiStagger():
    sprite('ny070_10', 2)
    sprite('ny070_11', 2)
    sprite('ny070_12', 2)
    sprite('ny070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('ny113_00', 3)
    sprite('ny113_01', 3)
    sprite('ny113_02', 9)


@State
def CmnActUkemiAirB():
    sprite('ny113_00', 3)
    sprite('ny113_01', 3)
    sprite('ny113_02', 9)


@State
def CmnActUkemiAirN():
    sprite('ny113_00', 3)
    sprite('ny113_01', 3)
    sprite('ny113_02', 9)


@State
def CmnActUkemiLandF():
    sprite('ny110_00', 2)
    sprite('ny110_01', 2)
    sprite('ny110_02', 2)
    sprite('ny110_03', 2)
    sprite('ny110_04', 2)
    sprite('ny110_05', 2)
    sprite('ny110_06', 2)
    sprite('ny110_07', 2)
    sprite('ny110_08', 200)
    sprite('ny110_09', 3)
    sprite('ny110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('ny111_00', 3)
    sprite('ny111_01', 3)
    sprite('ny111_02', 3)
    sprite('ny111_03', 3)
    sprite('ny111_04', 3)
    sprite('ny111_06', 3)
    sprite('ny111_07', 200)
    sprite('ny111_08', 2)
    sprite('ny111_09', 2)
    sprite('ny111_10', 2)


@State
def CmnActUkemiLandN():
    sprite('ny112_00', 2)
    sprite('ny112_01', 2)
    sprite('ny112_02', 2)
    sprite('ny112_03', 2)
    sprite('ny112_04', 2)
    sprite('ny112_05', 2)
    sprite('ny112_06', 2)
    sprite('ny112_07', 2)
    sprite('ny112_08', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('ny024_00', 3)
    sprite('ny024_01', 3)
    sprite('ny024_02', 3)
    sprite('ny024_03', 3)
    sprite('ny024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('ny040_00', 3)
    sprite('ny040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ny040_02', 2)
    sprite('ny040_03', 2)
    sprite('ny040_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('ny040_01', 3)
    sprite('ny040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('ny040_05', 2)
    label(0)
    sprite('ny040_02', 2)
    sprite('ny040_03', 2)
    sprite('ny040_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('ny040_01', 3)
    sprite('ny040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('ny041_00', 3)
    sprite('ny041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ny041_02', 2)
    sprite('ny041_03', 2)
    sprite('ny041_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('ny041_01', 3)
    sprite('ny041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('ny041_05', 2)
    label(0)
    sprite('ny041_02', 2)
    sprite('ny041_03', 2)
    sprite('ny041_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('ny041_01', 3)
    sprite('ny041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('ny043_00', 3)
    sprite('ny043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ny043_02', 2)
    sprite('ny043_03', 2)
    sprite('ny043_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('ny043_01', 3)
    sprite('ny043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ny043_05', 2)
    label(0)
    sprite('ny043_02', 2)
    sprite('ny043_03', 2)
    sprite('ny043_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ny043_01', 3)
    sprite('ny043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('ny045_00', 3)
    sprite('ny045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ny045_02', 2)
    sprite('ny045_03', 2)
    sprite('ny045_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('ny045_01', 3)
    sprite('ny045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('ny045_05', 2)
    label(0)
    sprite('ny045_02', 2)
    sprite('ny045_03', 2)
    sprite('ny045_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('ny045_01', 3)
    sprite('ny045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('ny090_00', 2)
    sprite('ny090_01', 2)
    sprite('ny090_02', 1)
    SetCommonActionMark(1)
    sprite('ny090_03', 6)
    sprite('ny090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('ny091_00', 2)
    sprite('ny091_01', 2)
    sprite('ny091_02', 1)
    SetCommonActionMark(1)
    sprite('ny091_03', 6)
    sprite('ny091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('ny092_00', 2)
    sprite('ny092_01', 2)
    sprite('ny092_02', 1)
    SetCommonActionMark(1)
    sprite('ny092_03', 6)
    sprite('ny092_04', 6)


@State
def CmnActAirTurn():
    sprite('ny025_00', 4)
    sprite('ny025_01', 4)
    sprite('ny025_02', 4)


@State
def CmnActLockWait():
    sprite('ny040_02', 1)
    sprite('ny040_01', 3)
    sprite('ny040_00', 3)


@State
def CmnActLockReject():
    sprite('ny312_00', 2)
    sprite('ny312_01', 2)
    sprite('ny312_02', 2)
    sprite('ny312_03', 8)
    sprite('ny312_04', 4)
    sprite('ny312_05', 3)
    sprite('ny312_06', 2)
    sprite('ny312_07', 3)
    sprite('ny312_08', 3)


@State
def CmnActAirLockWait():
    sprite('ny045_02', 1)
    sprite('ny045_01', 3)
    sprite('ny045_00', 3)


@State
def CmnActAirLockReject():
    sprite('ny322_00', 2)
    sprite('ny322_01', 2)
    sprite('ny322_02', 2)
    sprite('ny322_03', 8)
    sprite('ny322_04', 4)
    sprite('ny322_05', 3)
    sprite('ny322_06', 3)
    sprite('ny322_07', 3)
    sprite('ny322_08', 2)


@State
def CmnActLandSpin():
    sprite('ny071_00', 3)
    sprite('ny071_01', 3)
    sprite('ny071_02', 3)
    label(0)
    sprite('ny071_03', 2)
    sprite('ny071_04', 2)
    sprite('ny071_05', 2)
    sprite('ny071_06', 2)
    sprite('ny071_07', 2)
    sprite('ny071_08', 2)
    sprite('ny071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('ny071_10', 6)
    sprite('ny071_11', 5)
    sprite('ny071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('ny071_03', 2)
    sprite('ny071_04', 2)
    sprite('ny071_05', 2)
    sprite('ny071_06', 2)
    sprite('ny071_07', 2)
    sprite('ny071_08', 2)
    sprite('ny071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('ny077_00', 2)
    sprite('ny077_01', 2)
    sprite('ny077_00ex00', 2)
    sprite('ny077_01ex00', 2)
    sprite('ny077_00ex01', 2)
    sprite('ny077_01ex01', 2)
    sprite('ny077_00ex02', 2)
    sprite('ny077_01ex02', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('ny077_02', 4)
    label(0)
    sprite('ny077_03', 3)
    sprite('ny077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('ny077_05', 5)
    sprite('ny077_06', 4)


@State
def CmnActAomukeSlideKeep():
    sprite('ny060_07', 3)
    label(0)
    sprite('ny060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('ny060_11', 4)
    sprite('ny060_13', 5)


@State
def CmnActBurstBegin():
    sprite('ny331_00', 2)
    label(0)
    sprite('ny331_01', 3)
    sprite('ny331_02', 3)
    sprite('ny331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('ny331_04', 2)
    label(0)
    sprite('ny331_05', 3)
    sprite('ny331_06', 3)
    sprite('ny331_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('ny331_08', 2)
    sprite('ny331_09', 2)
    sprite('ny331_10', 2)


@State
def CmnActAirBurstBegin():
    sprite('ny332_00', 2)
    label(0)
    sprite('ny332_01', 3)
    sprite('ny332_02', 3)
    sprite('ny332_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('ny332_04', 2)
    label(0)
    sprite('ny332_05', 3)
    sprite('ny332_06', 3)
    sprite('ny332_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('ny332_08', 3)
    sprite('ny332_09', 3)
    sprite('ny332_10', 3)
    sprite('ny020_04', 3)
    sprite('ny020_05', 3)
    label(0)
    sprite('ny020_06', 4)
    sprite('ny020_07', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('ny333_00', 3)
    sprite('ny333_01', 3)
    sprite('ny333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ny333_03', 32767)
    CreateObject('EMB_NY_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('ny333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)
    sprite('ny333_06', 3)
    sprite('ny333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('ny333_08', 4)
    sprite('ny333_09', 4)
    sprite('ny333_10', 4)


@State
def CmnActAirOverDriveBegin():
    sprite('ny333_11', 3)
    sprite('ny333_12', 3)
    sprite('ny333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ny333_03', 32767)
    CreateObject('EMB_NY_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('ny333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)
    sprite('ny333_06', 3)
    sprite('ny333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('ny333_13', 4)
    sprite('ny333_14', 4)
    sprite('ny333_15', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        AirPushbackY(14000)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HitAirUnblockable(0)
        StarterRating(2)
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
        WhiffCancel('NmlAtk5A')
        HitOrBlockJumpCancel(1)
    sprite('ny200_00', 1)
    PerInertia(60)
    sprite('ny200_01', 2)
    sprite('ny200_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('007_swing_knife_0')
    sprite('ny200_03', 3)
    sprite('ny200_04', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ny200_02', 3)
    WhiffCancelEnable(1)
    sprite('ny200_01', 3)
    sprite('ny200_00', 3)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(510)
        PushbackX(15300)
        AirPushbackY(18000)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('Atk6B_Input5')
        WhiffCancel('Atk6B_Input5')
        HitOrBlockJumpCancel(1)
    sprite('ny201_00', 6)
    sprite('ny201_01', 1)
    sprite('ny201_02', 3)
    CommonSE('003_swing_grap_0_1')
    RandomCommonVoiceline(1)
    sprite('ny201_03', 1)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ny201_03add01', 1)
    sprite('ny201_03', 6)
    sprite('ny201_03', 2)
    WhiffCancelEnable(0)
    sprite('ny201_01', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk6C')

        def upon_STATE_END():
            ObjectUpon(6, 41)

        def upon_EVERY_FRAME():
            if SLOT_94:
                ChainCancel(0)
                if SLOT_StateDuration >= 45:
                    ChainCancel(1)
    sprite('ny202_00', 3)
    CreateObject('Funnel5CMain', -1)
    RegisterObject(6, 1)
    sprite('ny202_01', 2)
    sprite('ny202_02', 2)
    RandomCommonVoiceline(2)
    sprite('ny202_03', 1)
    sprite('ny202_04', 1)
    sprite('ny202_05', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 34)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 35)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 36)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 37)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 38)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 1)
    ObjectUpon(6, 39)
    sprite('ny202_07', 2)
    sprite('ny202_06', 1)
    sprite('ny202_06', 3)
    ObjectUpon(6, 40)
    sprite('ny202_07', 3)
    sprite('ny202_06', 7)
    sprite('ny202_06', 8)
    Recovery()
    Unknown2063()
    sprite('ny202_08', 4)
    CreateObject('FunnelRevive', -1)
    sprite('ny202_09', 4)
    sprite('ny202_10', 4)
    sprite('ny202_11', 4)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HitAirUnblockable(0)
        StarterRating(2)
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
        WhiffCancel('NmlAtk2A')
    sprite('ny230_00', 2)
    PerInertia(60)
    sprite('ny230_01', 1)
    sprite('ny230_02', 1)
    sprite('ny230_03', 2)
    sprite('ny230_04', 1)
    RandomCommonVoiceline(0)
    CommonSE('007_swing_knife_0')
    sprite('ny230_05', 3)
    sprite('ny230_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ny230_02', 3)
    sprite('ny230_01', 3)
    sprite('ny230_00', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(480)
        HitLow(2)
        AttackP1(90)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('Atk6B_Input5')
    sprite('ny231_00', 3)
    sprite('ny231_01', 3)
    sprite('ny231_02', 2)
    RandomCommonVoiceline(1)
    CommonSE('006_swing_blade_0')
    sprite('ny231_03', 4)
    CreateParticle('nyef_ny030back', 0)
    CreateParticle('nyef_ny030back', 1)
    CreateParticle('nyef_ny030back', 2)
    CreateParticle('nyef_ny030back', 3)
    CreateParticle('nyef_ny030back', 4)
    sprite('ny231_04', 4)
    Recovery()
    Unknown2063()
    sprite('ny231_05', 3)
    sprite('ny231_06', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(140)
        AttackP1(90)
        SingleProration(1)
        CHGroundedHitstunAnimation(9)
        AirUntechableTime(23)
        Hitstun(23)
        Hitstop(2)
        MoveAttributes(0, 1, 0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        HitAirUnblockable(3)
        AttackOff()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5C')

        def upon_EVERY_FRAME():
            if SLOT_94:
                HitOrBlockJumpCancel(0)
                ChainCancel(0)
                if SLOT_StateDuration >= 22:
                    HitOrBlockJumpCancel(1)
                    ChainCancel(1)
    sprite('ny232_00', 6)
    sprite('ny232_01', 4)
    sprite('ny232_02', 3)
    RandomCommonVoiceline(2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    CommonSE('006_swing_blade_1')
    sprite('ny232_03', 1)
    RefreshMultihit()
    sprite('ny232_03', 1)
    RefreshMultihit()
    sprite('ny232_04', 1)
    CreateObject('2CZanzo', -1)
    RefreshMultihit()
    CommonSE('006_swing_blade_1')
    HitAirUnblockable(0)
    sprite('ny232_04', 1)
    RefreshMultihit()
    sprite('ny232_04ex01', 1)
    setInvincible(0)
    RefreshMultihit()
    sprite('ny232_04ex01', 1)
    RefreshMultihit()
    sprite('ny232_05', 2)
    RefreshMultihit()
    sprite('ny232_05ex01', 2)
    RefreshMultihit()
    sprite('ny232_05ex02', 2)
    Recovery()
    Unknown2063()
    sprite('ny232_06', 9)
    sprite('ny232_07', 5)
    sprite('ny232_08', 4)
    sprite('ny232_09', 4)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(140)
        AttackP1(90)
        SingleProration(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(21000)
        AirUntechableTime(36)
        CHHardKnockdown(1)
        Hitstop(3)
        HitLow(2)
        UseSlashHitspark(1)
        HitsparkSize(700)
        AttackOff()

        def upon_EVERY_FRAME():
            if SLOT_94:
                SpecialCancel(0)
                if SLOT_StateDuration >= 19:
                    SpecialCancel(1)
    sprite('ny234_00', 3)
    sprite('ny234_01', 3)
    sprite('ny234_02', 2)
    sprite('ny234_03', 2)
    CommonSE('006_swing_blade_1')
    RandomCommonVoiceline(2)
    sprite('ny234_04', 1)
    RefreshMultihit()
    CreateObject('3CZanzo', -1)
    sprite('ny234_04', 1)
    RefreshMultihit()
    sprite('ny234_05', 1)
    RefreshMultihit()
    sprite('ny234_05', 1)
    RefreshMultihit()
    CHHardKnockdown(0)
    HitLow(0)
    HitAirUnblockable(0)
    sprite('ny234_06', 1)
    RefreshMultihit()
    CommonSE('006_swing_blade_1')
    sprite('ny234_06', 1)
    RefreshMultihit()
    sprite('ny234_07', 1)
    RefreshMultihit()
    sprite('ny234_07', 1)
    RefreshMultihit()
    sprite('ny234_08', 5)
    Recovery()
    Unknown2063()
    sprite('ny234_09', 5)
    sprite('ny234_10', 6)
    sprite('ny234_11', 6)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        UseSlashHitspark(1)
        HitsparkSize(600)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
    sprite('ny250_00', 1)
    sprite('ny250_01', 2)
    sprite('ny250_02', 3)
    sprite('ny250_03', 1)
    CommonSE('007_swing_knife_0')
    RandomCommonVoiceline(0)
    sprite('ny250_04', 2)
    sprite('ny250_05', 2)
    Recovery()
    Unknown2063()
    sprite('ny250_03', 2)
    sprite('ny250_02', 2)
    sprite('ny250_01', 2)
    sprite('ny250_00', 2)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(590)
        UseSlashHitspark(1)
        AttackP1(80)
        HitsparkSize(700)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('ny251_00', 3)
    sprite('ny251_01', 3)
    sprite('ny251_02', 2)
    RandomCommonVoiceline(1)
    CommonSE('006_swing_blade_0')
    sprite('ny251_03', 4)
    sprite('ny251_04', 4)
    Recovery()
    Unknown2063()
    sprite('ny251_05', 4)
    sprite('ny251_06', 4)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(150)
        AttackP1(80)
        SingleProration(1)
        AirPushbackY(12000)
        AirUntechableTime(20)
        Hitstop(2)
        HitsparkSize(500)
        UseSlashHitspark(1)
        AttackOff()

        def upon_EVERY_FRAME():
            if SLOT_94:
                HitOrBlockJumpCancel(0)
                ChainCancel(0)
                if SLOT_StateDuration >= 18:
                    HitOrBlockJumpCancel(1)
                    ChainCancel(1)
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockJumpCancel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            YSpeed(2000)
    sprite('ny252_00', 2)
    sprite('ny252_01', 3)
    sprite('ny252_02', 3)
    CommonSE('006_swing_blade_1')
    RandomCommonVoiceline(2)
    sprite('ny252_03', 1)
    RefreshMultihit()
    sprite('ny252_03', 1)
    RefreshMultihit()
    sprite('ny252_04', 2)
    RefreshMultihit()
    sprite('ny252_05', 2)
    CreateObject('8CZanzo', 0)
    RefreshMultihit()
    CommonSE('006_swing_blade_1')
    sprite('ny252_06', 2)
    RefreshMultihit()
    sprite('ny252_07', 2)
    RefreshMultihit()
    sprite('ny252_08', 2)
    RefreshMultihit()
    sprite('ny252_09', 2)
    RefreshMultihit()
    sprite('ny252_10', 4)
    Recovery()
    Unknown2063()
    sprite('ny252_11', 5)
    sprite('ny252_12', 6)
    sprite('ny252_13', 10)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(150)
        AttackP1(80)
        SingleProration(1)
        AirHitstunAnimation(10)
        AirPushbackX(8000)
        AirPushbackY(32000)
        AirUntechableTime(24)
        Hitstop(3)
        HitsparkSize(500)
        UseSlashHitspark(1)
        AttackOff()

        def upon_EVERY_FRAME():
            if SLOT_94:
                HitOrBlockJumpCancel(0)
                SpecialCancel(0)
                if SLOT_StateDuration >= 20:
                    HitOrBlockJumpCancel(1)
                    SpecialCancel(1)
        HitOrBlockJumpCancel(1)
    sprite('ny254_00', 1)
    sprite('ny254_01', 1)
    sprite('ny254_02', 2)
    sprite('ny254_03', 2)
    sprite('ny254_04', 2)
    sprite('ny254_05', 2)
    sprite('ny254_06', 2)
    CommonSE('006_swing_blade_0')
    RandomCommonVoiceline(2)
    sprite('ny254_07', 2)
    sprite('ny254_08', 1)
    RefreshMultihit()
    CreateObject('82CZanzo', 0)
    sprite('ny254_08', 1)
    RefreshMultihit()
    sprite('ny254_09', 1)
    RefreshMultihit()
    HitOverhead(0)
    sprite('ny254_09', 1)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('ny254_10', 1)
    RefreshMultihit()
    sprite('ny254_10', 1)
    RefreshMultihit()
    sprite('ny254_11', 1)
    RefreshMultihit()
    sprite('ny254_11', 1)
    RefreshMultihit()
    sprite('ny254_12', 2)
    Recovery()
    Unknown2063()
    sprite('ny254_13', 2)
    sprite('ny254_14', 2)
    sprite('ny254_15', 2)
    sprite('ny254_16', 2)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(670)
        AttackP1(90)
        AirPushbackY(20000)
        AirUntechableTime(26)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
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
    sprite('ny210_00', 2)
    sprite('ny210_01', 2)
    sprite('ny210_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    RandomCommonVoiceline(1)
    sprite('ny210_03', 4)
    sprite('ny210_04', 1)
    CommonSE('004_swing_grap_1_0')
    sprite('ny210_04', 5)
    setInvincible(0)
    sprite('ny210_05', 3)
    Recovery()
    Unknown2063()
    sprite('ny210_06', 4)
    sprite('ny210_07', 4)
    sprite('ny210_08', 3)
    sprite('ny210_00', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(740)
        AirPushbackY(18000)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockJumpCancel(1)
    sprite('ny211_00', 3)
    sprite('ny211_01', 2)
    sprite('ny211_02', 2)
    sprite('ny211_03', 2)
    RandomCommonVoiceline(1)
    CommonSE('010_swing_sword_1')
    sprite('ny211_04', 2)
    sprite('ny211_05', 3)
    sprite('ny211_04', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ny211_03', 3)
    sprite('ny211_02', 3)
    sprite('ny211_01', 3)
    sprite('ny211_00', 3)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(180)
        AttackP2(82)
        SingleProration(1)
        AirHitstunAnimation(17)
        CHGroundedHitstunAnimation(17)
        AirPushbackX(45000)
        AirPushbackY(15000)
        Blockstun(21)
        Hitstun(24)
        AirUntechableTime(36)
        Hitstop(2)
        Floorslide(10)
        FatalCounter(1)
        UseSlashHitspark(1)
        HitsparkSize(700)
        AttackOff()
        HitOrBlockCancel('SpecialDashF')
        HitOrBlockCancel('SpecialDashB')
        if SLOT_94:
            SpecialCancel(0)
    sprite('ny213_00', 3)
    sprite('ny213_01', 3)
    sprite('ny213_02', 3)
    sprite('ny213_03', 3)
    sprite('ny213_04', 3)
    sprite('ny213_05', 3)
    CommonSE('006_swing_blade_1')
    sprite('ny213_06', 3)
    SmartVoiceline('ny108')
    sprite('ny213_07', 1)
    RefreshMultihit()
    CreateObject('6CZanzo', -1)
    sprite('ny213_07', 1)
    RefreshMultihit()
    sprite('ny213_08', 1)
    RefreshMultihit()
    HitAirUnblockable(0)
    sprite('ny213_08', 1)
    RefreshMultihit()
    sprite('ny213_09', 1)
    CommonSE('011_spin_0')
    RefreshMultihit()
    sprite('ny213_09', 1)
    RefreshMultihit()
    sprite('ny213_10', 1)
    RefreshMultihit()
    sprite('ny213_10', 1)
    RefreshMultihit()
    sprite('ny213_11', 6)
    if SLOT_94:
        SpecialCancel(1)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ny213_12', 2)
    sprite('ny213_12', 4)
    sprite('ny213_13', 6)
    sprite('ny213_14', 6)


@Subroutine
def D_DefaultCancel():
    HitOrBlockCancel('NmlAtk5D')
    HitOrBlockCancel('NmlAtk4D')
    HitOrBlockCancel('NmlAtk2D')
    HitOrBlockCancel('NmlAtk6D')
    HitOrBlockCancel('NmlAtkAIR5D')
    HitOrBlockCancel('NmlAtkAIR2D')
    HitOrBlockCancel('NmlAtkAIR6D')
    WhiffCancel('SpecialDashF')
    WhiffCancel('SpecialDashB')
    WhiffCancel('SpecialDashAirF')
    WhiffCancel('SpecialDashAirB')
    HitJumpCancel(1)
    SLOT_58 = SLOT_OverdriveTimer
    SetActionMark(3)

    def upon_41():
        SLOT_51 = 1
        WhiffCancelEnable(1)

        def upon_EVERY_FRAME():
            AddActionMark(-1)
            if not SLOT_2:
                clearUponHandler(EVERY_FRAME)
                Unknown2063()


@Subroutine
def D_DefaultFlexCancel():
    WhiffCancel('SpecialDashF')
    WhiffCancel('SpecialDashB')
    WhiffCancel('SpecialDashAirF')
    WhiffCancel('SpecialDashAirB')

    def upon_32():
        WhiffSpecialCancel(1)
        WhiffCancelEnable(1)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtk5D_2nd')
    sprite('ny203_00', 4)
    sprite('ny203_01', 4)
    sprite('ny203_02', 3)
    CreateObject('NY_Sword5D', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_Sword5DAdd', -1)
    CreateObject('NY_SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny203_03', 3)
    sprite('ny203_04', 18)
    sprite('ny203_03', 4)
    sprite('ny203_02', 4)
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_01', 4)
    sprite('ny203_00', 4)


@State
def NmlAtk5D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtk5D')
    sprite('ny203_07', 3)
    sprite('ny203_08', 3)
    sprite('ny203_09', 3)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 32)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 32)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny203_10', 9)
    sprite('ny203_10', 2)
    sprite('ny203_11', 4)
    sprite('ny203_12', 4)
    sprite('ny203_13', 4)
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtk6D_2nd')
    sprite('ny214_00', 3)
    sprite('ny214_01', 3)
    sprite('ny214_02', 2)
    CreateObject('NY_Sword6D', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_Sword6DAdd', -1)
    CreateObject('NY_SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny214_03', 2)
    sprite('ny214_04', 2)
    sprite('ny214_05', 8)
    sprite('ny214_05', 10)
    sprite('ny214_04', 3)
    sprite('ny214_03', 3)
    Recovery()
    sprite('ny214_02', 3)
    WhiffCancelEnable(0)
    sprite('ny214_01', 3)
    sprite('ny214_00', 3)


@State
def NmlAtk6D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtk6D')
    sprite('ny214_08', 3)
    sprite('ny214_09', 3)
    sprite('ny214_10', 3)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 33)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 33)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny214_11', 3)
    sprite('ny214_12', 16)
    sprite('ny214_13', 4)
    sprite('ny214_14', 4)
    sprite('ny203_13', 4)
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)


@State
def NmlAtk4D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtk4D_2nd')
    sprite('ny215_00', 3)
    sprite('ny215_01', 3)
    if SLOT_58:
        CreateObject('NY_Sword4D', -1)
        ObjectUpon(STATE_END, 35)
        CreateObject('NY_Sword4DAdd', -1)
    else:
        CreateObject('NY_Sword4D', -1)
        ObjectUpon(STATE_END, 34)
    CreateObject('NY_SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny215_01', 3)
    sprite('ny215_02', 5)
    sprite('ny215_03', 4)
    sprite('ny215_04', 4)
    sprite('ny215_05', 10)
    sprite('ny215_05', 10)
    sprite('ny215_04', 3)
    sprite('ny215_03', 3)
    Recovery()
    sprite('ny215_02', 3)
    WhiffCancelEnable(0)
    sprite('ny215_01', 3)
    sprite('ny215_00', 3)


@State
def NmlAtk4D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtk4D')
    sprite('ny215_08', 3)
    sprite('ny215_09', 3)
    sprite('ny215_10', 2)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 34)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 34)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny215_11', 2)
    sprite('ny215_12', 12)
    sprite('ny215_13', 4)
    sprite('ny215_14', 4)
    sprite('ny203_13', 4)
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtk2D_2nd')
    sprite('ny233_00', 3)
    sprite('ny233_01', 3)
    sprite('ny233_02', 2)
    CreateObject('NY_Sword2D', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_Sword2DAdd', -1)
    CreateObject('NY_SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny233_03', 2)
    sprite('ny233_04', 2)
    sprite('ny233_05', 21)
    sprite('ny233_06', 4)
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny233_07', 4)
    sprite('ny233_08', 4)


@State
def NmlAtk2D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtk2D')
    sprite('ny233_09', 3)
    sprite('ny233_10', 3)
    sprite('ny233_11', 3)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 35)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 35)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny233_12', 20)
    sprite('ny233_12', 10)
    sprite('ny233_13', 6)
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny233_14', 6)


@Subroutine
def PopSpeed():
    PopSpeedX()
    PopSpeedY()
    PopInertia()
    XImpulseAcceleration(60)
    YAccel(80)
    EndYPhysicsImpulse()


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtkAIR5D_2nd')
    sprite('ny253_00', 3)
    sprite('ny253_01', 3)
    sprite('ny253_02', 4)
    NoAttackDuringAction(1)
    CreateObject('NY_SwordAirD', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_SwordAir5DAdd', -1)
    CreateObject('NY_SummonAirDmc', 0)
    PushSpeedX()
    PushSpeedY()
    PushInertia()
    EndMomentum(1)
    ForcedLandingRecovery(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny253_03', 4)
    sprite('ny253_04', 4)
    sprite('ny253_05', 16)
    sprite('ny253_06', 4)
    sprite('ny253_07', 4)
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny253_08', 4)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)


@State
def NmlAtkAIR5D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtkAIR5D')
    sprite('ny253_09', 3)
    CreateObject('NY_SummonAirDmc', 0)
    sprite('ny253_10', 3)
    sprite('ny253_11', 2)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 36)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 36)
    sprite('ny253_12', 15)
    sprite('ny253_13', 3)
    WhiffCancelEnable(0)
    sprite('ny253_13', 3)
    Recovery()
    sprite('ny253_14', 6)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)


@State
def NmlAtkAIR2D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtkAIR2D_2nd')
    sprite('ny255_00', 3)
    sprite('ny255_01', 3)
    sprite('ny255_02', 4)
    NoAttackDuringAction(1)
    CreateObject('NY_SwordAir2D', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_SwordAir2DAdd', -1)
    CreateObject('NY_SummonAirDmc', 0)
    PushSpeedX()
    PushSpeedY()
    PushInertia()
    EndMomentum(1)
    ForcedLandingRecovery(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny255_03', 4)
    sprite('ny255_04', 4)
    sprite('ny255_05', 16)
    sprite('ny255_06', 4)
    sprite('ny255_06', 2)
    Recovery()
    sprite('ny255_07', 2)
    WhiffCancelEnable(0)
    sprite('ny255_07', 4)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)


@State
def NmlAtkAIR2D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtkAIR2D')
    sprite('ny255_08', 3)
    CreateObject('NY_SummonAirDmc', 0)
    sprite('ny255_09', 3)
    sprite('ny255_10', 2)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 37)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 37)
    sprite('ny255_11', 15)
    sprite('ny255_12', 3)
    WhiffCancelEnable(0)
    sprite('ny255_12', 3)
    Recovery()
    sprite('ny255_13', 6)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)


@State
def NmlAtkAIR6D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        HitOrBlockCancel('NmlAtkAIR6D_2nd')
    sprite('ny256_00', 3)
    sprite('ny256_01', 3)
    sprite('ny256_02', 4)
    CreateObject('NY_SwordAir6D', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 32)
        CreateObject('NY_SwordAir6DAdd', -1)
    CreateObject('NY_SummonAirDmc', 0)
    PushSpeedX()
    PushSpeedY()
    PushInertia()
    EndMomentum(1)
    ForcedLandingRecovery(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny256_03', 4)
    sprite('ny256_04', 16)
    sprite('ny256_05', 8)
    sprite('ny256_06', 4)
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_06', 4)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)


@State
def NmlAtkAIR6D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('D_DefaultCancel')
        callSubroutine('D_DefaultFlexCancel')
        AttackOffOrBlockCancel('NmlAtkAIR6D')
    sprite('ny256_07', 2)
    sprite('ny256_08', 2)
    CreateObject('NY_SummonAirDmc', 0)
    sprite('ny256_09', 2)
    sprite('ny256_10', 2)
    CreateObject('NY_SwordDChain', -1)
    ObjectUpon(STATE_END, 38)
    if SLOT_58:
        CreateObject('NY_SwordDChainOD', -1)
        ObjectUpon(STATE_END, 38)
    sprite('ny256_11', 15)
    sprite('ny256_12', 3)
    WhiffCancelEnable(0)
    sprite('ny256_12', 3)
    Recovery()
    sprite('ny256_13', 6)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    Voiceline('ny404')
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    label(1)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(1)
    sprite('ny300_04', 12)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        UseSlashHitspark(1)
    sprite('ny211_00', 3)
    sprite('ny211_01', 3)
    sprite('ny211_02', 3)
    sprite('ny211_03', 3)
    CommonSE('010_swing_sword_1')
    sprite('ny211_04ex1', 2)
    sprite('ny211_05', 13)
    AttackOff()
    sprite('ny211_03', 5)
    sprite('ny211_02', 5)
    sprite('ny211_01', 5)
    sprite('ny211_00', 4)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(12)
        AirPushbackX(45000)
        AirPushbackY(18000)
        AirUntechableTime(60)
        Floorslide(15)
        Wallbounce(1)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickDuration(35)
        AirHitstunAfterWallbounce(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        UseSlashHitspark(1)
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
    sprite('ny409_00', 3)
    sprite('ny409_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    Voiceline('ny159')
    HeatChange(-2500)
    sprite('ny409_01', 2)
    CharacterFlash(16763080, 8, 2)
    label(100)
    sprite('ny409_02', 3)
    sprite('ny409_03', 3)
    sprite('ny409_04', 3)
    gotoLabel(100)
    label(0)
    sprite('keep', 2)
    clearUponHandler(EVERY_FRAME)
    sprite('ny409_05', 5)
    CommonSE('006_swing_blade_2')
    sprite('ny409_06', 2)
    StartMultihit()
    sprite('ny409_06', 1)
    sprite('ny409_07', 3)
    EnableAfterimage(0)
    sprite('ny409_08', 4)
    sprite('ny409_09', 3)
    sprite('ny409_10', 3)
    sprite('ny409_11', 3)
    sprite('ny409_12', 3)
    sprite('ny409_13', 3)
    sprite('ny409_14', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ny310_00', 3)
    sprite('ny310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ny310_02', 3)
    sprite('ny310_03', 11)
    SmartVoiceline('ny155')
    sprite('ny310_04', 4)
    StartMultihit()
    sprite('ny310_05', 4)
    sprite('ny310_06', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirPushbackX(18000)
        AirPushbackY(36000)
        AirUntechableTime(40)
        OppPositionOnHit(1, 1000, 116000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(100)
        UseSlashHitspark(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        if SLOT_94:
            ChainCancel(0)
    sprite('ny310_02', 4)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ny311_00', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_02', 7)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_03', 8)
    Voiceline('ny153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_04', 9)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('010_swing_sword_1')
    sprite('ny311_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateParticle('nyef_throw', 0)
    ScreenShake(15000, 0)
    sprite('ny311_06', 5)
    sprite('ny311_07', 5)
    sprite('ny311_08', 5)
    sprite('ny311_09', 5)
    if SLOT_94:
        ChainCancel(1)
    sprite('ny311_10', 5)
    sprite('ny311_11', 5)
    sprite('ny311_12', 5)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ny310_00', 3)
    sprite('ny310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ny310_02', 3)
    sprite('ny310_03', 11)
    SmartVoiceline('ny155')
    sprite('ny310_04', 4)
    StartMultihit()
    sprite('ny310_05', 4)
    sprite('ny310_06', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirPushbackX(18000)
        AirPushbackY(36000)
        AirUntechableTime(40)
        OppPositionOnHit(1, -1000, 116000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(100)
        UseSlashHitspark(1)
        StarterRating(2)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtk4D')
        if SLOT_94:
            ChainCancel(0)
    sprite('ny310_02', 4)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ny311_00', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SetXCollisionFromOrigin(200)
    sprite('ny311_01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_02', 7)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_03', 8)
    Voiceline('ny153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny311_04', 9)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('010_swing_sword_1')
    SetXCollisionFromOrigin(-1)
    sprite('ny311_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateParticle('nyef_throw', 0)
    ScreenShake(15000, 0)
    sprite('ny311_06', 5)
    AddX(100)
    sprite('ny311_07', 5)
    sprite('ny313_00', 5)
    sprite('ny313_01', 5)
    sprite('ny313_02', 5)
    if SLOT_94:
        ChainCancel(1)
    sprite('ny313_03', 5)
    sprite('ny313_04', 5)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('ny320_00', 3)
    sprite('ny320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ny320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('ny320_03', 3)
    sprite('ny320_04', 8)
    SmartVoiceline('ny155')
    sprite('ny320_05', 3)
    sprite('ny320_06', 3)
    sprite('ny320_07', 3)
    sprite('ny320_08', 3)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SpecialCancel(0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirPushbackX(-12000)
        AirPushbackY(-50000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        GroundBounce(1)
        AirUntechableTime(53)
        StarterRating(2)
        Hitstop(0)
        OppPositionOnHit(1, 10000, 10000)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        ForcedLandingRecovery(0, 0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        SetZLine(0, 50)
    sprite('ny320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('ny321_00', 4)
    OppThrowAnimation(25, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ny321_01', 6)
    physicsYImpulse(25000)
    setGravity(1800)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    Voiceline('ny154')
    CommonSE('004_swing_grap_1_1')
    sprite('ny321_02', 5)
    OppThrowAnimation(26, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ny321_03', 4)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ny321_04', 4)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ny321_05', 4)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    label(0)
    sprite('ny321_06', 3)
    OppThrowAnimation(27, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ny321_07', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny321_08', 1)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    ScreenShake(0, 30000)
    sprite('ny321_09', 2)
    sprite('ny321_10', 1)
    sprite('ny321_11', 1)
    sprite('ny321_12', 3)
    physicsXImpulse(8000)
    physicsYImpulse(24000)
    EndYPhysicsImpulse()
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('ny321_13', 3)
    sprite('ny321_14', 3)
    sprite('ny321_15', 3)
    sprite('ny321_16', 3)
    sprite('ny020_04', 3)
    Flip()
    sprite('ny020_05', 3)
    label(110)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    loopRest()
    gotoLabel(110)


@State
def SpecialDashF():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
    sprite('ny035_05ex01', 3)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('ny035_00ex01', 6)
    physicsXImpulse(3000)
    sprite('ny035_01ex01', 2)
    sprite('ny035_02ex01', 3)
    Voiceline('ny205')
    physicsXImpulse(36000)
    CommonSE('000_airdash_0')
    EnableCollision(0)
    sprite('ny035_03ex01', 3)
    CreateParticle('nyef_ny032', 0)
    XImpulseAcceleration(220)
    BlendMode_Normal()
    ConstantAlphaModifier(-40)
    sprite('ny035_04ex01', 3)
    CreateParticle('nyef_ny032', 0)
    sprite('ny035_05ex01', 3)
    CreateParticle('nyef_ny032', 0)
    sprite('ny033_04', 1)
    ForceFaceSprite()
    XImpulseAcceleration(70)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('ny033_04', 1)
    XImpulseAcceleration(70)
    EnableCollision(1)
    sprite('ny033_04', 1)
    XImpulseAcceleration(70)
    sprite('ny033_04', 1)
    XImpulseAcceleration(70)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_05', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 1)
    XImpulseAcceleration(70)
    sprite('ny033_06', 4)
    XImpulseAcceleration(70)


@State
def SpecialDashB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NegativeForBackDash()
        PreventBlocking(1)
        InvincibilityDuration(8)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
    sprite('ny024_00', 2)
    sprite('ny024_01', 2)
    sprite('ny410_02', 2)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('ny410_03', 2)
    sprite('ny410_04', 4)
    Voiceline('ny206')
    PrivateSE('nyse_03')
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    JumpEffects(0, 100)
    AddX(-50000)
    physicsXImpulse(-36000)
    physicsYImpulse(48000)
    SetAcceleration(200)
    sprite('ny410_05', 3)
    XImpulseAcceleration(60)
    YAccel(60)
    sprite('ny410_05', 3)
    XImpulseAcceleration(60)
    YAccel(60)
    sprite('ny410_15', 4)
    XImpulseAcceleration(30)
    YAccel(30)
    setGravity(1400)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    sprite('ny410_15', 4)
    XImpulseAcceleration(30)
    PerAcceleration(0)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    BlendMode_Off()
    sprite('ny410_16', 4)
    XImpulseAcceleration(30)


@State
def SpecialDashAirF():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        AddAirJumpCount(-1)
        AddAirDashCount(-1)
        EndMomentum(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
    sprite('ny035_05', 3)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('ny035_00', 3)
    physicsXImpulse(3000)
    sprite('ny035_01', 2)
    sprite('ny035_02', 2)
    Voiceline('ny205')
    physicsXImpulse(15000)
    EnableCollision(0)
    sprite('ny035_03', 3)
    AirDashEffects(1)
    XImpulseAcceleration(220)
    BlendMode_Normal()
    ConstantAlphaModifier(-40)
    sprite('ny035_04', 3)
    sprite('ny035_05', 3)
    sprite('ny036_05', 2)
    ForceFaceSprite()
    setGravity(1400)
    XImpulseAcceleration(70)
    EnableCollision(1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('ny036_05', 4)
    XImpulseAcceleration(70)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCrouchBlockCancel(1)
    sprite('ny020_05', 4)
    XImpulseAcceleration(70)
    sprite('ny020_06', 4)
    XImpulseAcceleration(70)
    sprite('ny020_06', 4)
    XImpulseAcceleration(70)


@State
def SpecialDashAirB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NegativeForBackDash()
        PreventBlocking(1)
        AddAirJumpCount(-1)
        AddAirDashCount(-1)
        EndMomentum(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
    sprite('ny036_00', 3)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('ny036_00', 3)
    physicsXImpulse(-4000)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    sprite('ny036_01', 3)
    sprite('ny036_02', 3)
    Voiceline('ny206')
    physicsXImpulse(-25000)
    AirDashEffects(1)
    sprite('ny036_03', 3)
    sprite('ny036_04', 3)
    sprite('ny036_05', 3)
    sprite('ny036_05', 4)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    BlendMode_Off()
    XImpulseAcceleration(70)
    EndYPhysicsImpulse()
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    sprite('ny020_05', 4)
    XImpulseAcceleration(70)
    sprite('ny020_06', 4)
    XImpulseAcceleration(70)


@State
def LargeShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_EVERY_FRAME():
            if not SLOT_94:
                CheckInput(INPUT_HOLD_D)
                SLOT_2 = SLOT_2 + SLOT_0
                if SLOT_51:
                    if CheckInput(INPUT_PRESS_C):
                        sendToLabel(0)

        def upon_STATE_END():
            ExtendCollisionX(0)
            SLOT_7 = 0
        SLOT_7 = 0
        HitCancel('SlowFieldA')
        HitCancel('SlowFieldB')
        HitCancel('SlowFieldC')
        if SLOT_OverdriveTimer:
            SLOT_7 = 1
            WhiffCancel('SpecialDashF')
            WhiffCancel('SpecialDashB')
    sprite('ny400_00', 4)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny400_01', 4)
    sprite('ny400_02', 3)
    ExtendCollisionX(50)
    sprite('ny400_03', 5)
    Voiceline('ny202')
    CreateObject('NY_SlowHand', 0)
    CommonSE('015_blaze_1')
    sprite('ny400_03', 5)
    SLOT_51 = 1
    sprite('ny400_03', 10)
    CreateObject('NY_SlowHand', 0)
    CommonSE('015_blaze_1')
    WhiffCancelEnable(1)
    loopRest()
    if not SLOT_2 == SLOT_StateDuration:
        notConditionalSendToLabel(1)
    sprite('ny400_03', 10)
    CreateObject('NY_SlowHand', 0)
    CommonSE('015_blaze_1')
    ScreenShake(2000, 0)
    sprite('ny400_03', 10)
    CreateObject('NY_SlowHand', 0)
    CommonSE('015_blaze_1')
    ScreenShake(4000, 0)
    sprite('ny400_03', 10)
    CreateObject('NY_SlowHand', 0)
    CommonSE('015_blaze_1')
    ScreenShake(8000, 0)
    sprite('ny400_04', 3)
    clearUponHandler(EVERY_FRAME)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    sprite('ny400_05', 3)
    CreateObject('NY_SummonDmc', -1)
    CreateObject('NY_TripleSword_D', -1)
    sprite('ny400_06', 3)
    sprite('ny400_07', 3)
    WhiffCancelEnable(1)
    sprite('ny400_08', 3)
    sprite('ny400_09', 3)
    loopRest()
    gotoLabel(9)
    label(0)
    clearUponHandler(EVERY_FRAME)
    SLOT_51 = 0
    sprite('ny400_04', 3)
    CreateObject('NY_SummonDmc', -1)
    CreateObject('NY_TripleSword_C', -1)
    ScreenShake(10000, 0)
    sprite('ny400_05', 6)
    WhiffCancelEnable(1)
    sprite('ny400_06', 6)
    sprite('ny400_07', 6)
    sprite('ny400_08', 6)
    sprite('ny400_09', 6)
    loopRest()
    gotoLabel(9)
    label(1)
    clearUponHandler(EVERY_FRAME)
    SLOT_51 = 0
    sprite('ny400_04', 3)
    CreateObject('NY_SummonDmc', -1)
    CreateObject('NY_TripleSword', -1)
    ScreenShake(12000, 0)
    sprite('ny400_05', 5)
    sprite('ny400_06', 5)
    sprite('ny400_07', 5)
    WhiffCancelEnable(1)
    sprite('ny400_08', 5)
    sprite('ny400_09', 5)
    label(9)
    sprite('ny400_10', 5)
    WhiffCancelEnable(0)
    sprite('ny400_11', 5)
    ExtendCollisionX(0)
    sprite('ny400_12', 5)


@State
def GedanShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_EVERY_FRAME():
            if not SLOT_94:
                CheckInput(INPUT_HOLD_D)
                SLOT_2 = SLOT_2 + SLOT_0
                if CheckInput(INPUT_PRESS_C):
                    SLOT_51 = 1
        HitOrBlockCancel('SlowFieldA')
        HitOrBlockCancel('SlowFieldB')
        HitOrBlockCancel('SlowFieldC')
        HitCancel('TimelagShot')
        if SLOT_OverdriveTimer:
            SLOT_58 = 1
            WhiffCancel('SpecialDashF')
            WhiffCancel('SpecialDashB')
    sprite('ny401_00', 3)
    CreateObject('NY_SummonDmc', -1)
    PrivateSE('nyse_30')
    sprite('ny401_01', 3)
    sprite('ny401_02', 3)
    sprite('ny401_03', 3)
    Voiceline('ny200')
    sprite('ny401_04', 3)
    sprite('ny401_05', 1)
    if SLOT_51:
        conditionalSendToLabel(0)
    if not SLOT_2 == SLOT_StateDuration:
        notConditionalSendToLabel(1)
    clearUponHandler(EVERY_FRAME)
    sprite('ny401_05', 2)
    sprite('ny401_06', 5)
    sprite('ny401_07', 5)
    CreateObject('BottomSword_D', -1)
    CommonSE('006_swing_blade_2')
    sprite('ny401_08', 7)
    WhiffCancelEnable(1)
    sprite('ny401_09', 5)
    sprite('ny401_10', 5)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ny401_05', 2)
    sprite('ny401_06', 5)
    sprite('ny401_07', 6)
    CreateObject('BottomSword_C', -1)
    CommonSE('006_swing_blade_2')
    sprite('ny401_08', 7)
    WhiffCancelEnable(1)
    sprite('ny401_09', 6)
    sprite('ny401_10', 6)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ny401_05', 1)
    CreateObject('BottomSword', -1)
    CommonSE('006_swing_blade_2')
    sprite('ny401_06', 5)
    WhiffCancelEnable(1)
    sprite('ny401_07', 6)
    sprite('ny401_08', 7)
    sprite('ny401_09', 6)
    sprite('ny401_10', 6)
    label(9)
    sprite('ny401_11', 5)
    sprite('ny401_12', 5)
    sprite('ny401_13', 5)


@State
def ChudanShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()

        def upon_EVERY_FRAME():
            if not SLOT_94:
                CheckInput(INPUT_HOLD_D)
                SLOT_2 = SLOT_2 + SLOT_0
                if SLOT_6:
                    if CheckInput(INPUT_PRESS_C):
                        SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        SLOT_58 = SLOT_OverdriveTimer
        WhiffCancel('SpecialDashAirF')
        WhiffCancel('SpecialDashAirB')
    sprite('ny402_00', 3)
    XImpulseAcceleration(10)
    YAccel(10)
    PerInertia(10)
    setGravity(0)
    physicsYImpulse(1100)
    Voiceline('ny203')
    sprite('ny402_01', 3)
    sprite('ny402_02', 3)
    CreateObject('NY_SummonAirDmc', 0)
    CreateObject('NY_AirCurveSword13Mode', -1)
    if SLOT_58:
        ObjectUpon(STATE_END, 34)
    sprite('ny402_03', 3)
    sprite('ny402_04', 1)
    ForcedLandingRecovery(10, 1)
    if SLOT_51:
        conditionalSendToLabel(0)
    if not SLOT_2 == SLOT_StateDuration:
        notConditionalSendToLabel(1)
    clearUponHandler(EVERY_FRAME)
    sprite('ny402_04', 1)
    SLOT_6 = 0
    DespawnEAEffect('NY_AirCurveSword13Mode')
    sprite('ny402_05', 5)
    sprite('ny402_06', 4)
    sprite('ny402_07', 4)
    CreateObject('NY_AirCurveSword_D', -1)
    if not SLOT_58:
        ObjectUpon(STATE_END, 32)
    else:
        ObjectUpon(STATE_END, 33)
    sprite('ny402_08', 4)
    setGravity(1700)
    if SLOT_58:
        WhiffCancelEnable(1)
    sprite('ny402_09', 4)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ny402_04', 1)
    SLOT_6 = 0
    DespawnEAEffect('NY_AirCurveSword13Mode')
    ForcedLandingRecovery(0, 0)
    if SLOT_58:
        WhiffCancelEnable(1)
    sprite('ny402_05', 5)
    setGravity(1700)
    sprite('ny402_06', 4)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffCancel('SpecialDashAirF')
    WhiffCancel('SpecialDashAirB')
    WhiffCancelEnable(1)
    sprite('ny402_07', 4)
    sprite('ny402_08', 4)
    setGravity(2500)
    YSpeed(-3000)
    sprite('ny402_09', 4)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ny402_04', 1)
    sprite('ny402_05', 5)
    sprite('ny402_06', 5)
    sprite('ny402_07', 5)
    sprite('ny402_08', 5)
    if SLOT_58:
        WhiffCancelEnable(1)
    sprite('ny402_09', 5)
    label(9)
    sprite('ny020_04', 5)
    setGravity(2500)
    YSpeed(-3000)
    sprite('ny020_05', 5)
    sprite('ny020_06', 5)
    sprite('ny020_07', 5)


@State
def TimelagShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)

        def upon_EVERY_FRAME():
            if not SLOT_94:
                CheckInput(INPUT_HOLD_D)
                SLOT_2 = SLOT_2 + SLOT_0
                if CheckInput(INPUT_PRESS_C):
                    SLOT_51 = 1
        SLOT_58 = SLOT_OverdriveTimer
        SLOT_9 = 0
    sprite('ny411_00', 3)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny411_01', 3)
    sprite('ny411_02', 3)
    sprite('ny411_03', 3)
    sprite('ny411_04', 3)
    Voiceline('ny207')
    sprite('ny411_05', 3)
    sprite('ny411_06', 3)
    sprite('ny411_07', 2)
    CreateObject('TimelagShot_Obj_Summon', -1)
    sprite('ny411_07', 1)
    if SLOT_51:
        conditionalSendToLabel(0)
    if not SLOT_2 == SLOT_StateDuration:
        notConditionalSendToLabel(1)
    clearUponHandler(EVERY_FRAME)
    sprite('ny411_08', 3)
    TriggerUponForState('TimelagShot_Obj_Summon', 33)

    def upon_EVERY_FRAME():
        if CheckInput(INPUT_PRESS_C):
            sendToLabel(0)
    sprite('ny411_09', 3)
    sprite('ny411_10', 3)
    sprite('ny411_08', 3)
    sprite('ny411_09', 3)
    sprite('ny411_10', 3)
    sprite('ny411_11', 3)
    SLOT_51 = 0
    clearUponHandler(EVERY_FRAME)
    loopRest()
    gotoLabel(9)
    label(0)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('TimelagShot_Obj_Summon', 32)
    SLOT_9 = 2
    SLOT_52 = 0
    sprite('ny411_08', 3)
    sprite('ny411_09', 3)
    sprite('ny411_10', 3)
    sprite('ny411_08', 3)
    sprite('ny411_09', 3)
    sprite('ny411_10', 3)
    sprite('ny411_11', 3)
    loopRest()
    gotoLabel(9)
    label(1)
    SLOT_52 = 1
    sprite('ny411_08', 3)
    sprite('ny411_09', 3)
    sprite('ny411_10', 3)
    sprite('ny411_11', 3)
    loopRest()
    gotoLabel(9)
    label(9)
    sprite('ny203_13', 3)
    sprite('ny203_14', 3)
    sprite('ny203_15', 3)
    if SLOT_52:
        TriggerUponForState('TimelagShot_Obj_Summon', 32)
        SLOT_9 = 3
    sprite('ny203_16', 3)
    sprite('ny203_17', 3)


@State
def BackAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SingleProration(1)
        Hitstop(2)
        HitAirUnblockable(3)
        AirUntechableTime(49)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(6500)
        AirPushbackY(44000)
        UseSlashHitspark(1)
        HitsparkSize(600)
        PushbackX(12000)
        StarterRating(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2:
                Damage(140)
                if SLOT_137:
                    DamageMultiplier(80)
                HitAirUnblockable(0)
        uponSendToLabel(LANDING, 1)
        HitCancel('SlowFieldA')
        HitCancel('SlowFieldB')
        HitCancel('SlowFieldC')
    sprite('ny407_00', 2)
    sprite('ny407_01', 2)
    Voiceline('ny204')
    sprite('ny407_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    CommonSE('006_swing_blade_2')
    PrivateSE('nyse_33')
    sprite('ny407_03', 2)
    sprite('ny407_04', 3)
    physicsXImpulse(-4500)
    physicsYImpulse(21000)
    setGravity(2400)
    sprite('ny407_05', 1)
    CreateObject('407slash', -1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    setInvincible(0)
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_07', 4)
    Recovery()
    sprite('ny407_08', 32767)
    label(1)
    sprite('ny407_09', 4)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(50)
    sprite('ny407_10', 4)
    XImpulseAcceleration(50)
    sprite('ny407_11', 4)
    XImpulseAcceleration(50)
    sprite('ny407_12', 3)
    EndMomentum(1)
    sprite('ny407_13', 3)
    sprite('ny407_14', 3)
    sprite('ny407_15', 3)
    sprite('ny407_16', 3)


@State
def BackAssault_Air():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        SingleProration(1)
        Hitstop(2)
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(45000)
        UseSlashHitspark(1)
        HitsparkSize(600)
        MoveAttributes(1, 0, 0, 0, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SetActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2:
                Damage(140)
                if SLOT_137:
                    DamageMultiplier(80)
        uponSendToLabel(LANDING, 1)
        HitCancel('SlowFieldA')
        HitCancel('SlowFieldB')
        HitCancel('SlowFieldC')
    sprite('ny407_03', 4)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 0, 1)
    Voiceline('ny204')
    CommonSE('006_swing_blade_2')
    PrivateSE('nyse_33')
    sprite('ny407_04', 4)
    physicsXImpulse(-4500)
    YSpeed(21000)
    YAccel(70)
    setGravity(2400)
    sprite('ny407_05', 1)
    CreateObject('407slash', -1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_05', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    setInvincible(0)
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_06', 1)
    RefreshMultihit()
    sprite('ny407_07', 4)
    Recovery()
    label(0)
    sprite('ny407_08', 3)
    PerGravity(110)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny407_09', 3)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(50)
    sprite('ny407_10', 3)
    XImpulseAcceleration(50)
    sprite('ny407_11', 3)
    XImpulseAcceleration(50)
    sprite('ny407_12', 3)
    EndMomentum(1)
    sprite('ny407_13', 3)
    sprite('ny407_14', 3)
    sprite('ny407_15', 3)
    sprite('ny407_16', 3)


@Subroutine
def SlowField_Chain():
    WhiffCancel('NmlAtk5A')
    WhiffCancel('NmlAtk5B')
    WhiffCancel('NmlAtk5C')
    WhiffCancel('NmlAtk2A')
    WhiffCancel('NmlAtk2B')
    WhiffCancel('NmlAtk2C')
    WhiffCancel('NmlAtk3C')
    WhiffCancel('NmlAtk6A')
    WhiffCancel('NmlAtk6B')
    WhiffCancel('NmlAtk6C')
    WhiffCancel('NmlAtk5D')
    WhiffCancel('NmlAtk4D')
    WhiffCancel('NmlAtk2D')
    WhiffCancel('NmlAtk6D')
    WhiffCancel('NmlAtkExcite')
    WhiffCancel('NmlAtkGuardCrush')
    WhiffCancel('NmlAtkThrow')
    WhiffCancel('NmlAtkBackThrow')
    WhiffCancel('LargeShot')
    WhiffCancel('TimelagShot')
    WhiffCancel('GedanShot')
    WhiffCancel('BackAssault')
    WhiffCancel('UltimateMultiSword')
    WhiffCancel('UltimateMultiSwordOD')
    WhiffCancel('UltimateLargeSwordLand')
    WhiffCancel('UltimateLargeSwordLandOD')


@State
def SlowFieldA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        NoAttackDuringAction(1)
        WhiffCancelEnable(1)
    sprite('ny403_00', 2)
    sprite('ny403_01', 2)
    sprite('ny403_02', 2)
    BeginBuffer('SpecialDashF')
    BeginBuffer('SpecialDashB')
    sprite('ny403_03', 2)
    sprite('ny403_07', 2)
    Voiceline('ny201')
    sprite('ny403_08', 2)
    sprite('ny403_09', 3)
    CommonSE('005_swing_grap_2_1')
    ObjectUpon(FALLING, 35)
    CreateObject('SummonSlowArea', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    CreateObject('NY_SlowHand', 0)
    SLOT_31 = 0
    BufferedOrPressedGoto('SpecialDashF')
    BufferedOrPressedGoto('SpecialDashB')
    sprite('ny403_10', 3)
    sprite('ny403_11', 6)
    callSubroutine('SlowField_Chain')
    sprite('ny403_12', 6)
    sprite('ny403_13', 6)
    sprite('ny403_14', 3)
    sprite('ny403_14', 3)
    DisallowGoto('SpecialDashF')
    DisallowGoto('SpecialDashB')
    WhiffCancelEnable(0)


@State
def SlowFieldB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        NoAttackDuringAction(1)
        WhiffCancelEnable(1)
    sprite('ny403_00', 2)
    sprite('ny403_01', 2)
    sprite('ny403_02', 2)
    BeginBuffer('SpecialDashF')
    BeginBuffer('SpecialDashB')
    sprite('ny403_03', 2)
    sprite('ny403_07', 2)
    Voiceline('ny201')
    sprite('ny403_08', 2)
    sprite('ny403_09', 3)
    CommonSE('005_swing_grap_2_1')
    ObjectUpon(FALLING, 35)
    CreateObject('SummonSlowArea', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 33)
    CreateObject('NY_SlowHand', 0)
    SLOT_31 = 0
    BufferedOrPressedGoto('SpecialDashF')
    BufferedOrPressedGoto('SpecialDashB')
    sprite('ny403_10', 3)
    sprite('ny403_11', 6)
    callSubroutine('SlowField_Chain')
    sprite('ny403_12', 6)
    sprite('ny403_13', 6)
    sprite('ny403_14', 3)
    sprite('ny403_14', 3)
    DisallowGoto('SpecialDashF')
    DisallowGoto('SpecialDashB')
    WhiffCancelEnable(0)


@State
def SlowFieldC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        NoAttackDuringAction(1)
        WhiffCancelEnable(1)
    sprite('ny403_00', 2)
    sprite('ny403_01', 2)
    sprite('ny403_02', 2)
    BeginBuffer('SpecialDashF')
    BeginBuffer('SpecialDashB')
    sprite('ny403_03', 2)
    sprite('ny403_07', 2)
    Voiceline('ny201')
    sprite('ny403_08', 2)
    sprite('ny403_09', 3)
    CommonSE('005_swing_grap_2_1')
    ObjectUpon(FALLING, 35)
    CreateObject('SummonSlowArea', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 34)
    CreateObject('NY_SlowHand', 0)
    SLOT_31 = 0
    BufferedOrPressedGoto('SpecialDashF')
    BufferedOrPressedGoto('SpecialDashB')
    sprite('ny403_10', 3)
    sprite('ny403_11', 6)
    callSubroutine('SlowField_Chain')
    sprite('ny403_12', 6)
    sprite('ny403_13', 6)
    sprite('ny403_14', 3)
    sprite('ny403_14', 3)
    DisallowGoto('SpecialDashF')
    DisallowGoto('SpecialDashB')
    WhiffCancelEnable(0)


@State
def UltimateMultiSword():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackOff()
        setInvincible(1)
        StrikeProjectilesBypass(0)
        DollInvincibility(0)
    sprite('ny430_00', 5)
    sprite('ny430_01', 5)
    sprite('ny430_02', 5)
    sprite('ny430_02', 19)
    DistortionSettings(41, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    Voiceline('ny250')
    StrikeProjectilesBypass(1)
    DollInvincibility(1)
    sprite('ny430_02', 1)
    StrikeProjectilesBypass(0)
    DollInvincibility(0)
    sprite('ny430_02', 10)
    CreateObject('NY_SumDDMultiSword', -1)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny430_02', 5)
    sprite('ny430_03', 5)
    sprite('ny430_04', 5)
    sprite('ny430_05', 2)
    setInvincible(0)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_10', 4)
    sprite('ny430_11', 4)
    sprite('ny430_12', 4)


@State
def UltimateMultiSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackType(4)
        AttackOff()
        setInvincible(1)
    sprite('ny430_00', 5)
    sprite('ny430_01', 5)
    sprite('ny430_02', 5)
    sprite('ny430_02', 19)
    DistortionSettings(41, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    Voiceline('ny250')
    StrikeProjectilesBypass(1)
    DollInvincibility(1)
    sprite('ny430_02', 1)
    StrikeProjectilesBypass(0)
    DollInvincibility(0)
    sprite('ny430_02', 10)
    CreateObject('NY_SumDDMultiSwordOD', -1)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny430_02', 5)
    sprite('ny430_03', 5)
    sprite('ny430_04', 5)
    sprite('ny430_05', 2)
    setInvincible(0)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_10', 4)
    sprite('ny430_11', 4)
    sprite('ny430_12', 4)


@State
def UltimateLargeSwordLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackOff()
    sprite('ny431_00', 4)
    setInvincible(1)
    sprite('ny431_01', 5)
    sprite('ny431_02', 5)
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    CreateObject('NY_SummonDmc', -1)
    Voiceline('ny251')
    sprite('ny431_03', 5)
    sprite('ny431_04', 5)
    PrivateSE('nyse_26')
    CreateObject('SummonDDBigSword', -1)
    sprite('ny431_05', 30)
    sprite('ny431_06', 2)
    sprite('ny431_07', 2)
    sprite('ny431_08', 2)
    sprite('ny431_09', 3)
    sprite('ny431_10', 3)
    setInvincible(0)
    sprite('ny431_11', 3)
    sprite('ny431_12', 3)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_13', 4)
    sprite('ny431_14', 4)
    sprite('ny431_15', 4)
    sprite('ny431_16', 4)


@State
def UltimateLargeSwordLandOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackOff()
        AttackType(4)
    sprite('ny431_00', 4)
    setInvincible(1)
    sprite('ny431_01', 5)
    sprite('ny431_02', 5)
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    CreateObject('NY_SummonDmc', -1)
    Voiceline('ny251')
    sprite('ny431_03', 5)
    sprite('ny431_04', 5)
    PrivateSE('nyse_26')
    CreateObject('SummonDDBigSwordOverDrive', -1)
    sprite('ny431_05', 30)
    sprite('ny431_06', 2)
    sprite('ny431_07', 2)
    sprite('ny431_08', 2)
    sprite('ny431_09', 3)
    sprite('ny431_10', 3)
    setInvincible(0)
    sprite('ny431_11', 3)
    sprite('ny431_12', 3)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_13', 4)
    sprite('ny431_14', 4)
    sprite('ny431_15', 4)
    sprite('ny431_16', 4)


@State
def UltimateLargeSwordAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackOff()
    sprite('ny020_03', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetInertia(0)
    physicsYImpulse(800)
    ForcedLandingRecovery(6, 1)
    sprite('ny020_02', 2)
    sprite('ny431_air00', 3)
    sprite('ny431_air01', 4)
    DistortionSettings(42, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    CreateParticle('nyef_sumDDmc', -1)
    CreateObject('NY_SummonAirDmc', 0)
    Voiceline('ny251')
    sprite('ny431_air02', 4)
    PrivateSE('nyse_26')
    CreateObject('SummonDDBigSword', -1)
    sprite('ny431_air03', 4)
    sprite('ny431_air04', 30)
    physicsYImpulse(0)
    sprite('ny431_air05', 2)
    setInvincible(0)
    sprite('ny431_air06', 2)
    sprite('ny431_air07', 2)
    sprite('ny431_air08', 3)
    sprite('ny431_air09', 3)
    sprite('ny431_air10', 3)
    sprite('ny431_air11', 3)
    sprite('ny431_air08', 4)
    sprite('ny431_air09', 4)
    sprite('ny431_air10', 4)
    CreateParticle('nyef_sumDDmcend', -1)
    sprite('ny431_air11', 4)
    sprite('ny431_air12', 2)
    sprite('ny431_air13', 2)
    EndYPhysicsImpulse()
    physicsYImpulse(10000)
    sprite('ny020_02', 2)
    sprite('ny020_04', 3)
    sprite('ny020_05', 3)
    label(0)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    loopRest()
    gotoLabel(0)


@State
def UltimateLargeSwordAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        AttackOff()
        AttackType(4)
    sprite('ny020_03', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetInertia(0)
    physicsYImpulse(800)
    ForcedLandingRecovery(6, 1)
    sprite('ny020_02', 2)
    sprite('ny431_air00', 3)
    sprite('ny431_air01', 4)
    DistortionSettings(42, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_NY', -1)
    CreateParticle('nyef_sumDDmc', -1)
    CreateObject('NY_SummonAirDmc', 0)
    Voiceline('ny251')
    sprite('ny431_air02', 4)
    PrivateSE('nyse_26')
    CreateObject('SummonDDBigSwordOverDrive', -1)
    sprite('ny431_air03', 4)
    sprite('ny431_air04', 30)
    physicsYImpulse(0)
    sprite('ny431_air05', 2)
    setInvincible(0)
    sprite('ny431_air06', 2)
    sprite('ny431_air07', 2)
    sprite('ny431_air08', 3)
    sprite('ny431_air09', 3)
    sprite('ny431_air10', 3)
    sprite('ny431_air11', 3)
    sprite('ny431_air08', 4)
    sprite('ny431_air09', 4)
    sprite('ny431_air10', 4)
    CreateParticle('nyef_sumDDmcend', -1)
    sprite('ny431_air11', 4)
    sprite('ny431_air12', 2)
    sprite('ny321_10', 1)
    sprite('ny321_11', 1)
    sprite('ny321_12', 3)
    physicsXImpulse(-8000)
    physicsYImpulse(20000)
    setGravity(500)
    Flip()
    ForcedLandingRecovery(10, 1)
    sprite('ny321_13', 3)
    sprite('ny321_14', 3)
    sprite('ny321_15', 3)
    sprite('ny321_16', 3)
    sprite('ny020_02', 2)
    XImpulseAcceleration(50)
    EndYPhysicsImpulse()
    ForceFaceSprite()
    sprite('ny020_04', 3)
    sprite('ny020_05', 3)
    label(0)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    loopRest()
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        setInvincible(1)
        EndMomentum(1)

        def upon_40():
            SLOT_52 = 1
            NoDamageAction(1)

        def upon_32():
            setInvincible(0)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 14:
                CreateObject('BurstDD_Shot', -1)
                CommonSE('006_swing_blade_2')
                clearUponHandler(EVERY_FRAME)

        def upon_STATE_END():
            DepleteOD()
    sprite('ny440_00', 3)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('ny280')
    sprite('ny440_01', 4)
    sprite('ny440_02', 4)
    physicsXImpulse(-5000)
    sprite('ny440_03', 3)
    sprite('ny440_04', 3)
    sprite('ny440_05', 2)
    physicsXImpulse(-20000)
    sprite('ny440_06', 3)
    sprite('ny440_07', 3)
    sprite('ny440_08', 3)
    physicsXImpulse(-10000)
    sprite('ny440_09', 1)
    sprite('ny440_09', 2)
    setInvincible(0)
    sprite('ny440_10', 2)
    sprite('ny440_11', 2)
    sprite('ny440_12', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('ny024_03ex01', 2)
    sprite('ny024_04ex01', 2)
    sprite('ny203_13', 4)
    if SLOT_52:
        enterState('BurstDDAdd')
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        setInvincible(1)
        EndMomentum(1)

        def upon_40():
            SLOT_52 = 1
            NoDamageAction(1)

        def upon_32():
            setInvincible(0)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 4:
                CreateObject('BurstDD_Shot', -1)
                CommonSE('006_swing_blade_2')
                clearUponHandler(EVERY_FRAME)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('ny440_00', 1)
    E0EAEffect('BurstDDeff', 103)
    Voiceline('ny280')
    sprite('ny440_01', 1)
    sprite('ny440_02', 1)
    physicsXImpulse(-10000)
    sprite('ny440_03', 2)
    sprite('ny440_04', 2)
    sprite('ny440_05', 2)
    physicsXImpulse(-20000)
    sprite('ny440_06', 3)
    sprite('ny440_07', 3)
    sprite('ny440_08', 3)
    physicsXImpulse(-10000)
    sprite('ny440_09', 1)
    sprite('ny440_09', 2)
    setInvincible(0)
    sprite('ny440_10', 2)
    sprite('ny440_11', 2)
    sprite('ny440_12', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('ny024_03ex01', 2)
    sprite('ny024_04ex01', 2)
    sprite('ny203_13', 4)
    if SLOT_52:
        enterState('BurstDDAdd')
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        SetBackground(1)
        uponSendToLabel(32, 0)
    sprite('ny615_01ex01', 6)
    if SLOT_51:
        CreateObject('BurstDD_ShotMatoSP', -1)
    else:
        CreateObject('BurstDD_ShotMato', -1)
    CreateObject('BurstDD_DummyCamera', -1)
    Voiceline('ny281')
    sprite('ny615_02ex01', 6)
    sprite('ny615_03ex01', 6)
    sprite('ny615_04ex01', 6)
    sprite('ny615_05ex01', 6)
    sprite('ny615_06ex01', 6)
    sprite('ny615_07ex01', 6)
    sprite('ny615_08ex01', 6)
    sprite('ny615_09ex01', 6)
    sprite('ny615_10ex01', 6)
    sprite('ny615_11ex01', 6)
    sprite('ny615_09ex01', 6)
    sprite('ny615_10ex01', 6)
    sprite('ny615_11ex01', 6)
    sprite('ny615_09ex01', 6)
    sprite('ny615_10ex01', 6)
    sprite('ny615_11ex01', 6)
    sprite('ny615_09ex01', 6)
    sprite('ny615_10ex01', 6)
    sprite('ny615_11ex01', 6)
    label(0)
    sprite('ny615_09ex01', 6)
    sprite('ny615_10ex01', 6)
    sprite('ny615_11ex01', 6)
    sprite('ny440_13', 6)
    sprite('ny440_14', 6)
    sprite('ny440_15', 6)
    SetActionMark(5)
    label(1)
    sprite('ny440_16', 5)
    AddActionMark(-1)
    sprite('ny440_17', 5)
    sprite('ny440_18', 5)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1)
    sprite('ny440_19', 8)
    TriggerUponForState('BurstDD_DummyCamera', 41)
    sprite('ny440_20', 8)
    sprite('ny203_13ex01', 6)
    sprite('ny203_14ex01', 6)
    sprite('ny203_15ex01', 6)
    sprite('ny203_16ex01', 6)
    sprite('ny203_17ex01', 6)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(210)
        Crumple(200)
        Hitstop(0)
        OppPositionOnHit(1, 200000, 0)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeatCatch')
        EnterStateIfEventID(12, 'AstralHeatCatch')
        IgnoreScreenfreeze(1)
    sprite('ny450_00', 4)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 0, 0)
    Voiceline('ny290')
    sprite('ny450_01', 4)
    sprite('ny450_02', 4)
    sprite('ny450_03', 3)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    DistortionSettings(101, -1, 2)
    EmptyHeat()
    CreateObject('EMB_NY_AH', -1)
    CreateParticle('nyef_ashstart', -1)
    CreateParticle('nyef_ashstartmc', -1)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    CommonSE('019_quake_1')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    CommonSE('019_quake_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('019_quake_1')
    CommonSE('013_thunder_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    CommonSE('013_thunder_0')
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    CreateParticle('nyef_ash_front', 0)
    CreateParticle('nyef_ash', 1)
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_02', 3)
    sprite('ny450_03', 3)
    sprite('ny450_04', 3)
    sprite('ny450_05', 3)
    sprite('ny450_06', 3)
    PrivateSE('nyse_30')
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    setInvincible(0)
    AttackOff()
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_09', 4)
    sprite('ny450_10', 4)
    sprite('ny450_11', 4)
    sprite('ny450_12', 4)


@State
def AstralHeatCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AstralHeatExe', 5, 0, 0)
        setInvincible(1)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        PreventAirborneHit(0)
        AttackLevel_(0)
        Damage(0)
        PassByArmor(1)
        AstralHeatCleanup(1, 1)
        HitAnywhere(1)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SetZVal(-500)
        EnableRapidCancel(0)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    setInvincible(0)
    AttackOff()
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_09', 4)
    sprite('ny450_10', 4)
    sprite('ny450_11', 4)
    sprite('ny450_12', 4)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(5, 0, 0)
        AttackLevel_(0)
        Damage(0)
        GroundedHitstunAnimation(9)
        UseSlashHitspark(1)
        AirPushbackX(100)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        Hitstop(0)
        EnemyHitstopAddition(1000, 1000, 1000)
        AirUntechableTime(1000)
        DamageFromStateOnly('AstralHeatExe')
    sprite('ny450_06', 25)
    AttackOff()
    OppThrowAnimation(8, 0)
    OppThrowPosition(2, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('ny450_06', 3)
    PlayPlayAstralBGM(0)
    RefreshMultihit()
    CreateParticle('nyef_ashlock', 0)
    CreateParticle('nyef_ashmc', 2)
    CreateParticle('nyef_whitelight', 101)
    sprite('ny450_07', 3)
    Voiceline('ny291')
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_06', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_07', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_08', 3)
    CommonSE('015_blaze_1')
    sprite('ny450_06', 3)
    sprite('ny450_07', 3)
    sprite('ny450_08', 3)
    sprite('null', 10)
    CreateObject('StartWhite', -1)
    HUDVisibillity(1)
    sprite('null', 10)
    AddY(2800000)
    CameraFast(1)
    sprite('null', 562)
    SetBackground(3)
    CreateObject('NY_AHAnime', -1)
    AstralHeatCleanup(1, 1)
    sprite('vrnyef_astdamagedmy', 60)
    DeleteObject(1)
    CreateObject('FinishWhite', -1)
    SetBackground(2)
    CreateObject('AstralLookAtMeDummy', -1)
    RegisterObject(5, 1)
    CommonSE('025_cleanhit_slash')
    RefreshMultihit()
    Damage(40000)
    DefeatOpponentBehavior(3)
    AttackDirection(3)
    HitAnywhere(1)
    YImpulseBeforeWallbounce(2000)
    Hitstop(20)
    EnemyHitstopAddition(0, 0, 0)
    CreateObject('AstrakFinishPtc', -1)
    sprite('ny020_06', 3)
    AddX(-128000)
    setGravity(1000)
    uponSendToLabel(LANDING, 17)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 3)
    sprite('ny020_06', 3)
    sprite('ny020_07', 32767)
    label(17)
    sprite('ny024_00', 4)
    CommonSE('205_runjump_garden_0')
    DeleteObject(5)
    EndAttack()
    SLOT_61 = 1
    CameraControlEnable(1)
    CameraControlInfinity(1)
    CameraFast(0)
    sprite('ny024_01', 4)
    sprite('ny024_02', 4)
    sprite('ny024_03', 4)
    sprite('ny024_04', 4)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('ny054')
    sprite('ny900_00', 6)
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
    SetZVal(1000)
    sprite('ny900_00', 32767)
    CreateObject('RLAstSmoke', -1)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(250000)
    sprite('ny902_00', 50)
    physicsYImpulse(-150)
    sprite('ny902_00', 50)
    physicsYImpulse(150)
    Voiceline('ny055')
    label(0)
    sprite('ny902_00', 50)
    physicsYImpulse(-150)
    sprite('ny902_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('ny000', 12641, 25392, 24885, 12337, 13667, 12641, 25392, 
        53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny055', 13921, 13667, 13921, 13667, 13153, 25392, 56, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny400', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 25397, 24885, 12338, 13667, 12897, 25392, 53, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny401', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny404', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny406', 12643, 24880, 25400, 24888, 25400, 24888, 25400, 
        24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny407', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny408', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ny412', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny413', 12643, 24880, 12337, 12643, 24880, 12337, 12643, 
        24880, 12337, 12643, 24880, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ny414', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ny415', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ny416', 14433, 14435, 12641, 25392, 12337, 12641, 25392, 
        12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('ny000', 13665, 13667, 13665, 13667, 13665, 13667, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny400', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 25397, 24885, 12338, 12643, 48, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ny401', 12643, 24880, 12337, 12643, 24880, 25400, 
            24888, 25400, 24888, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )
        Unknown18011('ny404', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny406', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 24880, 25400, 24888, 25400, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('ny407', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 24880, 12337, 12643, 48, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('ny408', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny412', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny413', 12643, 24880, 12337, 12643, 24880, 12337, 
            12643, 24880, 12337, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny414', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny415', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ny416', 12643, 24880, 12337, 12643, 24880, 12337, 
            13667, 24885, 12337, 12643, 24880, 12337, 12643, 48, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            if SLOT_138:
                Unknown18011('ny000', 13921, 13923, 13921, 13923, 13921, 
                    13411, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ny400', 14433, 14435, 14433, 14435, 14433, 
                    13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 14385, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown18011('ny401', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('ny000', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ny400', 14433, 14435, 14433, 14435, 14433, 
                    13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 14385, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown18011('ny401', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('nt'):
            Unknown18011('ny000', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny400', 13923, 13921, 13923, 13921, 13923, 13921,
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('ny401', 13923, 13921, 13923, 13921, 13923, 13921,
                13667, 24880, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            Unknown18011('ny500', 13921, 13923, 13921, 13923, 13921, 14179,
                24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                12340, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny501', 14177, 14435, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('ny505', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 24885, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ny504', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('ny536', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 12643, 12337, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny537', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('ny546', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14435, 24880, 25399, 24887, 25399, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny547', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('nt'):
            Unknown18011('ny560', 13921, 13923, 13921, 13923, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 14385, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny561', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ny560', 14435, 14177, 14179, 14177, 14179, 
                    14177, 14179, 14177, 13923, 24885, 25399, 24887, 25399,
                    24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399,
                    24887, 25399, 24887, 14385, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('ny558', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 
                24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ny559', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14179, 24880, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('ph'):
        SyncEntry()
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('ph'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('nt'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2400)
        else:
            gotoLabel(400)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    label(482)
    if random_(2, 0, 25):
        conditionalSendToLabel(1)
    if random_(2, 0, 33):
        conditionalSendToLabel(5)
    if random_(2, 0, 50):
        conditionalSendToLabel(2)
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    Voiceline('ny412')
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    sprite('ny300_04', 1)
    Voiceline('ny413')
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    DemoTimer(90)
    loopRest()
    ExitState()
    label(5)
    sprite('null', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(5)
    sprite('ny600_00', 6)
    AbsoluteY(640000)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    if SLOT_43:
        Mouth(14433, 14435, 14177, 14691, 14689, 14691, 14689, 99, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Mouth(14433, 14435, 14177, 13923, 24880, 25400, 24888, 25399, 13361,
            14689, 14691, 14689, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Voiceline('ny412')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    if SLOT_43:
        Mouth(12641, 25394, 24889, 25401, 24889, 25401, 24889, 25401, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Voiceline('ny413')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    DemoTimer(100)
    loopRest()
    ExitState()
    label(1)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1)
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    Voiceline('ny416')
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(2)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2)
    sprite('ny601_00', 1)
    Voiceline('ny414')
    label(3)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    if SLOT_97:
        conditionalSendToLabel(3)
    sprite('ny601_00', 1)
    Voiceline('ny415')
    label(4)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    if SLOT_97:
        conditionalSendToLabel(4)
    sprite('ny601_03', 2)
    sprite('ny601_04', 2)
    sprite('ny601_05', 2)
    sprite('ny601_06', 6)
    CreateParticle('nyef_entrymcB', -1)
    CommonSE('022_magiccircle_a')
    sprite('ny601_07', 6)
    sprite('ny601_08', 6)
    sprite('ny601_09', 6)
    sprite('ny601_10', 6)
    sprite('ny601_11', 6)
    sprite('ny601_12', 6)
    sprite('ny601_13', 6)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(99)
    sprite('null', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(99)
    sprite('ny600_00', 6)
    AbsoluteY(640000)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    Voiceline('ny416')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    if SLOT_44:
        Mouth(13411, 14689, 14691, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    DemoTimer(100)
    loopRest()
    ExitState()
    label(100)
    sprite('null', 1)
    AbsoluteY(640000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(100)
    sprite('ny600_00', 6)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    uponSendToLabel(32, 102)
    label(101)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    Voiceline('ny500')
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(1100)
    sprite('ny601_00', 1)

    def upon_32():
        SetActionMark(1)
        Voiceline('ny500')
    label(1101)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1101)
    label(1102)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(1102)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 4)
    sprite('keep', 1)
    SetActionMark(2)
    label(1103)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1103)
    sprite('keep', 1)
    SetActionMark(3)
    label(1104)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(1000, 3000)
    CommonSE('019_quake_0')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_02', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_00', 5)
    ScreenShake(1000, 3000)
    CommonSE('019_quake_0')
    sprite('ny601_01', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_02', 5)
    ScreenShake(1000, 3000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1104)
    sprite('keep', 1)
    SetActionMark(3)
    label(1105)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(2000, 5000)
    CommonSE('019_quake_1')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_02', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_00', 5)
    ScreenShake(2000, 5000)
    CommonSE('019_quake_1')
    sprite('ny601_01', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_02', 5)
    ScreenShake(2000, 5000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1105)
    sprite('ny601_03', 2)
    sprite('ny601_04', 2)
    sprite('ny601_05', 2)
    sprite('ny601_06', 6)
    CreateParticle('nyef_entrymcB', -1)
    CommonSE('022_magiccircle_a')
    ScreenShake(50000, 50000)
    sprite('ny601_07', 6)
    sprite('ny601_08', 6)
    sprite('ny601_09', 6)
    sprite('ny601_10', 6)
    sprite('ny601_11', 6)
    sprite('ny601_12', 6)
    sprite('ny601_13', 6)
    loopRest()
    ExitState()
    label(120)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(120)
    sprite('keep', 2)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    Voiceline('ny504')
    DemoEndOnVoiceEnd(1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 4)
    sprite('keep', 1)
    SetActionMark(10)
    label(121)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(121)
    sprite('keep', 1)
    SetActionMark(2)
    label(122)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(1000, 3000)
    CommonSE('019_quake_0')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_02', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_00', 5)
    ScreenShake(1000, 3000)
    CommonSE('019_quake_0')
    sprite('ny601_01', 5)
    ScreenShake(1000, 3000)
    sprite('ny601_02', 5)
    ScreenShake(1000, 3000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(122)
    sprite('keep', 1)
    SetActionMark(2)
    label(123)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(2000, 5000)
    CommonSE('019_quake_1')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_02', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_00', 5)
    ScreenShake(2000, 5000)
    CommonSE('019_quake_1')
    sprite('ny601_01', 5)
    ScreenShake(2000, 5000)
    sprite('ny601_02', 5)
    ScreenShake(2000, 5000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(123)
    sprite('ny601_03', 2)
    sprite('ny601_04', 2)
    sprite('ny601_05', 2)
    sprite('ny601_06', 6)
    CreateParticle('nyef_entrymcB', -1)
    CommonSE('022_magiccircle_a')
    ScreenShake(5000, 30000)
    sprite('ny601_07', 6)
    sprite('ny601_08', 6)
    sprite('ny601_09', 6)
    sprite('ny601_10', 6)
    sprite('ny601_11', 6)
    sprite('ny601_12', 6)
    sprite('ny601_13', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2120)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2120)
    sprite('keep', 2)
    sprite('ny601_00', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    Voiceline('ny504')
    DemoEndOnVoiceEnd(1)
    sprite('ny601_01', 5)
    sprite('ny601_02', 4)
    sprite('keep', 1)
    SetActionMark(10)
    label(2121)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    sprite('ny601_00', 5)
    sprite('ny601_01', 5)
    sprite('ny601_02', 5)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2121)
    sprite('keep', 1)
    SetActionMark(2)
    label(2122)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(100, 3000)
    CommonSE('019_quake_0')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(100, 3000)
    sprite('ny601_02', 5)
    ScreenShake(100, 3000)
    sprite('ny601_00', 5)
    ScreenShake(100, 3000)
    CommonSE('019_quake_0')
    sprite('ny601_01', 5)
    ScreenShake(100, 3000)
    sprite('ny601_02', 5)
    ScreenShake(100, 3000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2122)
    sprite('keep', 1)
    SetActionMark(2)
    label(2123)
    sprite('ny601_00', 5)
    AddActionMark(-1)
    ScreenShake(500, 5000)
    CommonSE('019_quake_1')
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_01', 5)
    ScreenShake(500, 5000)
    sprite('ny601_02', 5)
    ScreenShake(500, 5000)
    sprite('ny601_00', 5)
    ScreenShake(500, 5000)
    CommonSE('019_quake_1')
    sprite('ny601_01', 5)
    ScreenShake(500, 5000)
    sprite('ny601_02', 5)
    ScreenShake(500, 5000)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2123)
    sprite('ny601_03', 2)
    sprite('ny601_04', 2)
    sprite('ny601_05', 2)
    sprite('ny601_06', 6)
    CreateParticle('nyef_entrymcB', -1)
    CommonSE('022_magiccircle_a')
    ScreenShake(1000, 50000)
    sprite('ny601_07', 6)
    sprite('ny601_08', 6)
    sprite('ny601_09', 6)
    sprite('ny601_10', 6)
    sprite('ny601_11', 6)
    sprite('ny601_12', 6)
    sprite('ny601_13', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    sprite('null', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(280)
    sprite('ny600_00', 6)
    AbsoluteY(640000)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    Voiceline('ny536')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    uponSendToLabel(32, 332)
    label(331)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('ny300_00', 4)
    Voiceline('ny546')
    DemoTimer(300)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    label(334)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(334)
    loopRest()
    sprite('ny300_04', 12)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    loopRest()
    ExitState()
    label(400)
    sprite('null', 1)
    AbsoluteY(640000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(400)
    sprite('ny600_00', 6)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    ObjectUpon(22, 32)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    sprite('ny600_11', 6)
    Voiceline('ny560')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    ObjectUpon(22, 32)
    sprite('ny600_23', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(2400)
    sprite('null', 1)
    AbsoluteY(640000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2400)
    sprite('ny600_00', 6)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    ObjectUpon(22, 32)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    sprite('ny600_11', 6)
    Voiceline('ny560')
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    ObjectUpon(22, 32)
    sprite('ny600_23', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(390)
    sprite('null', 1)
    AbsoluteY(640000)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(390)
    sprite('ny600_00', 6)
    setGravity(57)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_03', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    uponSendToLabel(32, 392)
    label(391)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    loopRest()
    gotoLabel(391)
    label(392)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    Voiceline('ny558')
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    DemoTimer(30)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if random_(2, 0, 50):
        conditionalSendToLabel(0)
    sprite('ny615_00', 6)
    sprite('ny615_01', 6)
    sprite('ny615_02', 6)
    sprite('ny615_03', 8)
    Voiceline('ny400')
    DemoEndOnVoiceEnd(1)
    sprite('ny615_04', 6)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_05', 6)
    sprite('ny615_06', 6)
    sprite('ny615_07', 6)
    sprite('ny615_08', 6)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    label(4)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    loopRest()
    gotoLabel(4)
    label(0)
    sprite('ny615_00', 6)
    sprite('ny615_01', 6)
    sprite('ny615_02', 6)
    sprite('ny615_03', 8)
    Voiceline('ny401')
    DemoEndOnVoiceEnd(1)
    sprite('ny615_04', 6)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_05', 6)
    sprite('ny615_06', 6)
    sprite('ny615_07', 6)
    sprite('ny615_08', 6)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    label(5)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    loopRest()
    gotoLabel(5)


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
        conditionalSendToLabel(120)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(280)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('nt'):
        conditionalSendToLabel(400)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('ny610_00', 5)
    sprite('ny610_01', 5)
    sprite('ny610_02', 5)
    sprite('ny610_03', 5)
    sprite('ny610_04', 4)
    sprite('ny610_05', 4)
    sprite('ny610_06', 4)
    sprite('ny610_07', 4)
    Voiceline('ny406')
    sprite('ny610_08', 4)
    sprite('ny610_09', 4)
    sprite('ny610_10', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    if SLOT_43:
        DemoTimer(110)
    else:
        DemoTimer(130)
    label(2)
    sprite('ny610_11', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    loopRest()
    gotoLabel(2)
    ExitState()
    label(0)
    sprite('ny610_00', 5)
    sprite('ny610_01', 5)
    sprite('ny610_02', 5)
    sprite('ny610_03', 5)
    sprite('ny610_04', 4)
    sprite('ny610_05', 4)
    sprite('ny610_06', 4)
    sprite('ny610_07', 4)
    Voiceline('ny407')
    sprite('ny610_08', 4)
    sprite('ny610_09', 4)
    sprite('ny610_10', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    DemoTimer(120)
    label(3)
    sprite('ny610_11', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    loopRest()
    gotoLabel(3)
    ExitState()
    label(1)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    DemoTimer(110)
    Voiceline('ny407')
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(4)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(4)
    ExitState()
    label(100)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny501')
    DemoEndOnVoiceEnd(1)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(101)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(101)
    ExitState()
    label(1100)
    if SLOT_109:
        conditionalSendToLabel(482)
    if SLOT_123:
        conditionalSendToLabel(482)
    ForceFaceSprite()
    CameraControlEnable(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 600000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            XSpeed(2000)
            Voiceline('ny501')
            DemoEndOnVoiceEnd(1)
            sendToLabel(1102)
    sprite('ny032_00', 2)
    physicsXImpulse(22000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    label(1101)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    gotoLabel(1101)
    label(1102)
    sprite('ny407_00', 2)
    SetZVal(-500)
    AttackOff()
    EnableCollision(0)
    Flip()

    def upon_LANDING():
        clearUponHandler(EVERY_FRAME)
        sendToLabel(1103)
    sprite('ny407_01', 2)
    sprite('ny407_02', 3)
    CommonSE('006_swing_blade_2')
    PrivateSE('nyse_33')
    sprite('ny407_03', 3)

    def upon_EVERY_FRAME():
        PrivateFunction3(22, 0, 0, 10, 0)
    sprite('ny407_04', 3)
    physicsYImpulse(40000)
    setGravity(2400)
    sprite('ny407_05', 1)
    sprite('ny407_05', 5)
    sprite('ny407_06', 6)
    sprite('ny407_07', 6)
    sprite('ny407_08', 32767)
    loopRest()
    label(1103)
    sprite('ny407_09', 4)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    sprite('ny407_10', 4)
    sprite('ny407_11', 4)
    sprite('ny407_12', 3)
    sprite('ny407_13', 2)
    sprite('ny407_14', 2)
    sprite('ny407_15', 2)
    sprite('ny407_16', 2)
    sprite('ny003_02', 2)
    PrivateSE('nyse_22')
    Flip()
    sprite('ny003_01', 2)
    sprite('ny000_00', 2)
    physicsYImpulse(500)
    sprite('ny611_00', 3)
    sprite('ny611_01', 3)
    sprite('ny611_02', 3)
    sprite('ny611_03', 3)
    sprite('ny611_04', 3)
    sprite('ny601_03', 5)
    sprite('ny601_02', 3)
    sprite('ny601_01', 1)
    sprite('ny601_02', 2)
    sprite('ny601_03', 2)
    sprite('ny601_04', 2)
    sprite('ny601_05', 2)
    sprite('ny601_06', 2)
    EndMomentum(1)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 30:
            if SLOT_52 % 2:
                physicsYImpulse(200)
            else:
                physicsYImpulse(-200)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1
    CreateParticle('nyef_entrymcB', -1)
    CommonSE('022_magiccircle_a')
    ScreenShake(5000, 30000)
    sprite('ny601_07', 2)
    sprite('ny601_08', 2)
    label(1104)
    sprite('ny601_09', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny601_10', 5)
    sprite('ny601_09', 5)
    sprite('ny601_10', 5)
    sprite('ny601_09', 5)
    sprite('ny601_10', 5)
    loopRest()
    gotoLabel(1104)
    ExitState()
    label(120)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny505')
    DemoEndOnVoiceEnd(1)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(121)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(121)
    ExitState()
    label(280)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny537')
    DemoEndOnVoiceEnd(1)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(281)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(281)
    ExitState()
    label(330)
    sprite('ny610_00', 5)
    sprite('ny610_01', 5)
    sprite('ny610_02', 5)
    sprite('ny610_03', 5)
    sprite('ny610_04', 4)
    sprite('ny610_05', 4)
    sprite('ny610_06', 4)
    sprite('ny610_07', 4)
    Voiceline('ny547')
    sprite('ny610_08', 4)
    DemoEndOnVoiceEnd(1)
    sprite('ny610_09', 4)
    sprite('ny610_10', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    label(2)
    sprite('ny610_11', 5)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    sprite('ny610_11', 5)
    sprite('ny610_12', 5)
    sprite('ny610_13', 5)
    loopRest()
    gotoLabel(2)
    ExitState()
    label(400)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny561')
    DemoEndOnVoiceEnd(1)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(401)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(401)
    ExitState()
    label(390)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny559')
    DemoEndOnVoiceEnd(1)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(391)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(391)
    ExitState()
    label(666)
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    Voiceline('ny408')
    DemoTimer(110)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_17', 7)
    label(667)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(667)


@State
def CmnActLose():
    sprite('ny620_00', 6)
    Voiceline('ny411')
    sprite('ny620_01', 6)
    sprite('ny620_02', 6)
    sprite('ny620_03', 6)
    sprite('ny620_04', 6)
    sprite('ny620_05', 6)
    sprite('ny620_06', 6)
    sprite('ny620_07', 6)
    sprite('ny620_08', 6)
    DemoTimer(90)
    label(0)
    sprite('ny620_08ex01', 1)
    CreateParticle('nyef_timeupptc', -1)
    if random_(2, 0, 20):
        CommonSE('014_electric_s')
    sprite('ny620_08ex02', 1)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWait():
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
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
    label(0)
    sprite('ny620_08ex01', 1)
    CreateParticle('nyef_timeupptc', -1)
    if random_(2, 0, 20):
        CommonSE('014_electric_s')
    sprite('ny620_08ex02', 1)
    loopRest()
    gotoLabel(0)


@State
def EventDown():
    StayAfterMovement(1, 0)
    sprite('ny070_00', 2)
    sprite('ny070_01', 2)
    sprite('ny070_02', 4)
    CommonSE('205_runjump_garden_0')
    sprite('ny070_03', 4)
    sprite('ny070_04', 4)
    sprite('ny070_05', 4)
    sprite('ny070_06', 4)
    sprite('ny070_07', 5)
    sprite('ny070_08', 5)
    sprite('ny070_09', 2)
    Unknown1004()
    sprite('ny063_11', 32767)
    Unknown1005()
    loopRest()


@State
def EventEntryFall():
    XPositionRelativeFacing(-260000)
    AbsoluteY(640000)
    setGravity(57)

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor < 120000:
            sendToLabel(1)
    sprite('ny600_00', 1)
    label(0)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(LANDING, 3)
    label(2)
    sprite('ny600_03', 15)
    YAccel(60)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    CommonSE('019_cloth_a')
    sprite('ny600_03', 15)
    YAccel(60)
    sprite('ny600_03', 15)
    YAccel(60)
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)
    sprite('ny600_03', 6)
    EndMomentum(1)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    label(4)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    gotoLabel(4)


@State
def EventEntryBootMurakumo():
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventGoStand():
    sprite('ny620_08', 5)
    sprite('ny620_07', 5)
    sprite('ny620_06', 5)
    sprite('ny620_05', 5)
    sprite('ny620_04', 5)
    sprite('ny620_03', 5)
    sprite('ny620_02', 5)
    sprite('ny620_01', 5)
    sprite('ny620_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventChouhatu():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    sprite('ny300_04', 12)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    enterState('CmnActStand')


@State
def EventWarpOutSimple():

    def upon_IMMEDIATE():
        SetZVal(-500)
        ScreenCollision(0)
        BlendMode_Normal()
    sprite('keep', 26)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('keep', 1)
    XPositionRelativeFacing(-500000)
    sprite('null', 32767)
    loopRest()


@State
def EventCrouch():
    label(0)
    sprite('ny010_02', 6)
    sprite('ny010_03', 6)
    sprite('ny010_04', 6)
    sprite('ny010_05', 6)
    sprite('ny010_06', 6)
    sprite('ny010_07', 6)
    sprite('ny010_08', 6)
    sprite('ny010_09', 6)
    sprite('ny010_10', 6)
    sprite('ny010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def EventCrouchToStand():
    sprite('ny010_01', 4)
    sprite('ny010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)


@State
def EventWarpIn():
    SetZVal(-500)
    BlendMode_Normal()
    ScreenCollision(0)
    sprite('ny331_00', 2)
    AlphaValue(0)
    sprite('ny331_04', 4)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(10)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    label(0)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    gotoLabel(0)


@State
def EventWarpInToStand():
    sprite('ny331_08', 6)
    sprite('ny331_09', 6)
    sprite('ny331_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventWarpOut():
    SetZVal(-500)
    BlendMode_Normal()
    ScreenCollision(0)
    sprite('ny331_00', 2)
    sprite('ny331_01', 15)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ny331_02', 15)
    sprite('ny331_03', 15)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('001_airbackdash_0')
    sprite('ny331_01', 15)
    sprite('ny331_02', 15)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ny331_03', 15)
    sprite('ny331_01', 15)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('001_airbackdash_0')
    sprite('ny331_02', 15)
    sprite('ny331_04', 4)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    CreateParticle('haef_event_lose_end', 103)
    sprite('ny331_05', 6)
    XPositionRelativeFacing(-900000)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    sprite('ny331_08', 2)
    sprite('ny331_09', 2)
    sprite('ny331_10', 2)


@State
def EventLoseDownLoop():
    sprite('ny063_11', 32767)
    loopRest()


@State
def EventLoseDown2WorpWait():
    sprite('ny064_00', 8)
    sprite('ny064_01', 8)
    sprite('ny064_02', 8)
    label(1)
    sprite('ny064_03', 90)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    PrivateSE('nyse_28')
    loopRest()
    gotoLabel(1)


@State
def EventLoseWorpout():
    sprite('ny064_03', 25)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventRGVsNY_FallSword():
    sprite('null', 1)
    CreateObject('EntryFallSword_RGVsNY', 0)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    loopRest()


@State
def EventRGVsNY_Transform():
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    ObjectUpon(STATE_END, 32)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    enterState('CmnActStand')


@State
def EventRGVsNY_Attack():
    XPositionRelativeFacing(-260000)
    AttackDefaults_StandingDD()
    AttackLevel_(4)
    setInvincible(1)
    uponSendToLabel(32, 1)
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('ny232_00', 3)
    sprite('ny232_01', 2)
    sprite('ny232_02', 3)
    CommonSE('010_swing_sword_2')
    sprite('ny232_03', 1)
    sprite('ny232_03', 1)
    sprite('ny232_04', 1)
    CreateObject('2CZanzo', -1)
    CommonSE('010_swing_sword_2')
    sprite('ny232_04', 1)
    sprite('ny232_04ex01', 1)
    sprite('ny232_04ex01', 1)
    sprite('ny232_05', 2)
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_2')
    ScreenShake(2000, 6000)
    sprite('ny232_05ex01', 2)
    sprite('ny232_05ex02', 2)
    sprite('ny232_06', 3)
    sprite('ny232_07', 3)
    sprite('ny232_08', 3)
    sprite('ny232_09', 3)
    sprite('ny010_01', 3)
    sprite('ny010_00', 3)
    loopRest()
    uponSendToLabel(32, 3)
    label(2)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(32)
    sprite('ny213_00', 3)
    sprite('ny213_01', 3)
    sprite('ny213_02', 3)
    sprite('ny213_03', 3)
    sprite('ny213_04', 3)
    sprite('ny213_05', 3)
    CommonSE('011_spin_0')
    sprite('ny213_06', 3)
    sprite('ny213_07', 1)
    RefreshMultihit()
    CreateObject('6CZanzo', -1)
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_2')
    ScreenShake(8000, 4000)
    sprite('ny213_07', 1)
    sprite('ny213_08', 1)
    sprite('ny213_08', 1)
    sprite('ny213_09', 1)
    CommonSE('011_spin_0')
    sprite('ny213_09', 1)
    sprite('ny213_10', 1)
    sprite('ny213_10', 1)
    sprite('ny213_11', 6)
    sprite('ny213_12', 2)
    sprite('ny213_12', 4)
    sprite('ny213_13', 6)
    sprite('ny213_14', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventNYAttack5D():
    sprite('ny203_00', 4)
    sprite('ny203_01', 4)
    sprite('ny203_02', 4)
    sprite('ny203_03', 4)
    sprite('ny203_04', 4)
    sprite('ny203_05', 4)
    sprite('ny203_06', 4)
    sprite('ny203_07', 4)
    sprite('ny203_08', 4)
    sprite('ny203_09', 4)
    sprite('ny203_10', 4)
    sprite('ny203_11', 4)
    sprite('ny203_12', 4)
    sprite('ny203_13', 4)
    sprite('ny203_14', 4)
    sprite('ny203_15', 4)
    sprite('ny203_16', 4)
    sprite('ny203_17', 4)
    enterState('CmnActStand')


@State
def EventNYStanding():
    sprite('ny450_00', 6)
    sprite('ny450_01', 6)
    label(0)
    sprite('ny450_02', 6)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny450_03', 6)
    sprite('ny450_04', 6)
    gotoLabel(0)
    enterState('CmnActStand')


@State
def EventNYStandingEnd():
    sprite('ny450_01', 6)
    sprite('ny450_00', 6)
    enterState('CmnActStand')


@State
def EventDown2():
    sprite('ny620_08', 32767)


@State
def EventChouhatuLoop():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    label(0)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    loopRest()
    gotoLabel(0)


@State
def EventChouhatuLoopEnd():
    sprite('ny300_04', 12)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    enterState('CmnActStand')


@State
def EventDashScreenOut():
    sprite('ny032_00', 2)
    Flip()
    ScreenCollision(0)
    EnableCollision(0)
    CreateObject('EventRL', 0)
    sprite('ny032_00', 2)
    physicsXImpulse(32000)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    Visibility(1)
    loopRest()


@State
def EventLargeSwordLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackOff()
    sprite('ny431_00', 4)
    sprite('ny431_01', 5)
    sprite('ny431_02', 5)
    DistortionSettings(52, -1, 0)
    CreateObject('EMB_NY', -1)
    CreateObject('NY_SummonDmc', -1)
    sprite('ny431_03', 5)
    sprite('ny431_04', 5)
    PrivateSE('nyse_26')
    CreateObject('SummonDDBigSword', -1)
    sprite('ny431_05', 30)
    sprite('ny431_06', 2)
    sprite('ny431_07', 2)
    sprite('ny431_08', 2)
    sprite('ny431_09', 3)
    ObjectUpon(22, 32)
    sprite('ny431_10', 3)
    sprite('ny431_11', 3)
    sprite('ny431_12', 3)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_13', 4)
    sprite('ny431_14', 4)
    sprite('ny431_15', 4)
    sprite('ny431_16', 4)


@State
def EventLoseDown():
    sprite('ny064_00', 8)
    sprite('ny064_01', 8)
    sprite('ny064_02', 8)
    label(1)
    sprite('ny064_03', 90)
    CommonSE('electric_s')
    loopRest()
    gotoLabel(1)


@State
def Act2Event_Chouhatsu():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    label(0)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_ChouhatsuEnd():
    sprite('ny300_04', 12)
    sprite('ny300_04', 1)
    CreateObject('EF_ny300', 0)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Chouhatsu2():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    CreateObject('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 20)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Chouhatsu2End():
    sprite('ny300_04', 1)
    sprite('ny300_04', 10)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    TriggerUponForState('Event_EF_ny300', 32)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Damage():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('ny070_00', 15)
    CallCustomizableParticle('ptef_hit_middle', 103)
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('ny070_01', 4)
    sprite('ny070_02', 4)
    sprite('ny070_03', 32767)
    loopRest()


@State
def Act2Event_DamageEnd():
    sprite('ny070_10', 5)
    sprite('ny070_11', 5)
    sprite('ny070_12', 5)
    sprite('ny070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_TimeUp():
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    label(0)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Warp():
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    sprite('ny611_11', 7)
    ConstantAlphaModifier(-12)
    CreateParticle('nyef_entrymc', 0)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('022_magiccircle_c')
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    Visibility(1)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_RoundWin():
    sprite('ny615_00', 6)
    sprite('ny615_01', 6)
    sprite('ny615_02', 6)
    sprite('ny615_03', 8)
    sprite('ny615_04', 6)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_05', 6)
    sprite('ny615_06', 6)
    sprite('ny615_07', 6)
    sprite('ny615_08', 6)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    label(0)
    sprite('ny615_09', 5)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    sprite('ny615_09', 5)
    sprite('ny615_10', 5)
    sprite('ny615_11', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_RoundWinEnd():
    sprite('keep', 2)
    sprite('ny615_08', 6)
    sprite('ny615_07', 6)
    sprite('ny615_06', 6)
    sprite('ny615_05', 6)
    sprite('ny615_04', 6)
    sprite('ny615_03', 6)
    sprite('ny615_02', 6)
    sprite('ny615_01', 6)
    sprite('ny615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_OverDrive():
    sprite('ny333_00', 6)
    sprite('ny333_01', 6)
    sprite('ny333_02', 6)
    sprite('ny333_03', 32767)
    loopRest()


@State
def Act2Event_OverDriveActivate():
    sprite('keep', 2)
    sprite('ny333_04', 4)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(30000, 60000)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    loopRest()
    enterState('Act2Event_OverDriveEnd')


@State
def Act2Event_OverDriveEnd():
    sprite('ny333_08', 4)
    sprite('ny333_09', 4)
    sprite('ny333_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_5D():
    sprite('ny203_00', 5)
    sprite('ny203_01', 5)
    sprite('ny203_02', 5)
    sprite('ny203_03', 5)
    sprite('ny203_04', 20)
    sprite('ny203_03', 5)
    sprite('ny203_02', 5)
    sprite('ny203_01', 5)
    sprite('ny203_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_rlvsny_01():
    label(0)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_bnvsny_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-60000)
    sprite('keep', 1)
    CreateObject('Act2Event_Nirvana', -1)
    RegisterObject(4, 1)
    CreateObject('Act2Event_Carl', -1)
    RegisterObject(5, 1)
    Flip()
    loopRest()
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_bnvsny_01():
    sprite('keep', 2)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    ObjectUpon(5, 32)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_bnvsny_02():
    sprite('keep', 2)
    ObjectUpon(FALLING, 41)
    ObjectUpon(5, 41)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_rmvsny_00():
    sprite('keep', 2)
    sprite('ny615_08', 7)
    sprite('ny615_07', 7)
    sprite('ny615_06', 7)
    sprite('ny333_01', 6)
    sprite('ny333_02', 6)
    sprite('ny333_03', 120)
    label(0)
    sprite('ny333_03', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act2Event_rmvsny_01():
    sprite('keep', 2)
    sprite('ny333_04', 4)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    sprite('ny333_05', 5)
    sprite('ny333_06', 5)
    sprite('ny333_07', 5)
    loopRest()
    enterState('Act2Event_OverDriveEnd')


@State
def Act2Event_rmvsny_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('ny070_00', 15)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitmz', 103)
    CommonSE('101_hit_slash_1')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('ny070_01', 4)
    sprite('ny070_02', 4)
    sprite('ny070_03', 32767)
    loopRest()


@State
def Act2Event_rmvsny_03():
    sprite('ny611_00', 6)
    sprite('ny611_01', 6)
    sprite('ny611_02', 6)
    sprite('ny611_03', 6)
    sprite('ny611_04', 6)
    sprite('ny611_05', 6)
    sprite('ny611_06', 6)
    sprite('ny611_07', 6)
    sprite('ny611_08', 6)
    sprite('ny611_09', 6)
    sprite('ny611_10', 6)
    sprite('ny611_11', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_12', 7)
    sprite('ny611_13', 7)
    label(0)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_rmvsny_04():
    sprite('keep', 2)
    ConstantAlphaModifier(-12)
    CreateParticle('nyef_entrymc', 0)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('022_magiccircle_c')
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    sprite('ny611_14', 7)
    CreateObject('Act2Event_Yure', -1)
    sprite('ny611_15', 7)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    Visibility(1)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_rmvsny_05():
    sprite('keep', 2)
    sprite('ny032_00', 2)
    Flip()
    ScreenCollision(0)
    EnableCollision(0)
    sprite('ny032_00', 2)
    physicsXImpulse(32000)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    CreateObject('Act2Event_Yure', -1)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    Visibility(1)
    EndMomentum(1)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_azvsny_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-60000)
        Flip()
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_azvsny_01():
    sprite('keep', 2)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    ObjectUpon(22, 33)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_azvsny_02():
    sprite('keep', 2)
    ObjectUpon(22, 34)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    sprite('ny032_00', 2)
    physicsXImpulse(21000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    physicsXImpulse(0)
    AddInertia(10000)
    sprite('ny310_00', 3)
    sprite('ny310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ny310_02', 3)
    sprite('ny310_03', 16)
    EndMomentum(1)
    XPositionRelativeFacing(260000)
    sprite('ny310_04', 5)
    sprite('ny310_05', 5)
    sprite('ny310_06', 5)
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_azvsny_03():
    sprite('keep', 2)
    sprite('ny003_02', 2)
    Flip()
    sprite('ny003_01', 2)
    sprite('ny003_00', 2)
    sprite('ny431_00', 4)
    sprite('ny431_01', 4)
    sprite('ny431_02', 4)
    sprite('ny431_03', 4)
    sprite('ny431_04', 4)
    PrivateSE('nyse_26')
    CreateObject('Event_SummonDDBigSword', -1)
    sprite('ny431_05', 4)
    sprite('ny431_06', 2)
    sprite('ny431_07', 2)
    sprite('ny431_08', 2)
    sprite('ny431_09', 3)
    sprite('ny431_10', 3)
    sprite('ny431_11', 3)
    sprite('ny431_12', 3)
    sprite('ny431_09', 4)
    sprite('ny431_10', 4)
    sprite('ny431_11', 4)
    sprite('ny431_12', 4)
    sprite('ny431_09', 5)
    sprite('ny431_10', 5)
    sprite('ny431_11', 5)
    sprite('ny431_12', 5)
    sprite('ny431_13', 5)
    sprite('ny431_14', 5)
    sprite('ny431_15', 5)
    sprite('ny431_16', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_CameraCreate():
    sprite('keep', 1)
    CreateObject('Act2Event_Camera_nyvspt', 100)
    enterState('CmnActStand')


@State
def Act2Event_Legacy():
    sprite('ny430_00', 5)
    sprite('ny430_01', 5)
    sprite('ny430_02', 5)
    sprite('ny430_03', 5)
    sprite('ny430_04', 5)
    sprite('ny430_05', 1)
    CreateObject('Act2AZvsNY_SumDDMultiSword', -1)

    def RunOnObject_1():
        AddX(-120000)
    sprite('ny430_05', 1)
    CreateObject('NY_SummonDmc', -1)

    def RunOnObject_1():
        AddX(-120000)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_10', 4)
    sprite('ny430_11', 4)
    sprite('ny430_12', 4)
    enterState('CmnActStand')


@State
def Act2EventWait_azvsny():
    sprite('keep', 1)
    AddX(-55000)
    sprite('keep', 1)
    enterState('CmnActStand')


@State
def Act2Event_azvsny00():
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_azvsny01():
    sprite('ny032_00', 2)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('ny032_00', 2)
    physicsXImpulse(32000)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    sprite('ny032_02', 4)
    sprite('ny032_03', 4)
    sprite('ny032_04', 4)
    Visibility(1)
    loopRest()


@State
def Event_Act2EntryFall():
    XPositionRelativeFacing(-260000)
    AbsoluteY(640000)
    setGravity(57)

    def upon_EVERY_FRAME():
        if SLOT_YDistanceFromFloor < 120000:
            sendToLabel(1)
    sprite('ny600_00', 1)
    label(0)
    sprite('ny600_00', 6)
    CommonSE('019_cloth_a')
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    sprite('ny600_00', 6)
    sprite('ny600_01', 6)
    sprite('ny600_02', 6)
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(LANDING, 3)
    label(2)
    sprite('ny600_03', 15)
    YAccel(60)
    PrivateSE('nyse_28')
    CommonSE('019_cloth_a')
    sprite('ny600_03', 15)
    YAccel(60)
    sprite('ny600_03', 15)
    YAccel(60)
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)
    sprite('ny600_03', 6)
    EndMomentum(1)
    CommonSE('019_cloth_a')
    sprite('ny600_04', 6)
    CommonSE('201_walk_garden_0')
    sprite('ny600_05', 6)
    LandingEffects(0, 1, 1)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny600_06', 6)
    sprite('ny600_07', 6)
    sprite('ny600_08', 6)
    sprite('ny600_09', 6)
    sprite('ny600_10', 6)
    label(4)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    gotoLabel(4)


@State
def EventAct2EntryBootMurakumo():
    sprite('ny600_11', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('ny600_12', 6)
    sprite('ny600_13', 3)
    sprite('ny600_13', 3)
    PrivateSE('nyse_28')
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_15', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 30)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('019_cloth_a')
    PrivateSE('nyse_03')
    sprite('ny600_16', 12)
    sprite('ny600_17', 6)
    CreateParticle('nyef_entrylightB', 0)
    sprite('ny600_18', 6)
    CharacterFlash2(0, 10)
    sprite('ny600_19', 6)
    CommonSE('022_magiccircle_a')
    sprite('ny600_20', 6)
    sprite('ny600_21', 6)
    sprite('ny600_22', 6)
    sprite('ny600_23', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2EventARvsNY():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        XPositionRelativeFacing(-10000)
    label(0)
    sprite('ny620_08ex01', 4)
    CreateParticle('nyef_timeupptc', -1)
    if random_(2, 0, 10):
        CommonSE('014_electric_s')
    sprite('ny620_08ex02', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    Visibility(1)
    XPositionRelativeFacing(-900000)


@State
def Act2Event_ny_bn():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)

        def upon_32():
            ObjectUpon(FALLING, 35)
            TriggerUponForState('Act2Event_moyamoya', 32)
            sendToLabel(1)
    sprite('ny403_00', 2)
    sprite('ny403_01', 2)
    sprite('ny403_02', 2)
    sprite('ny403_03', 2)
    sprite('ny403_07', 2)
    sprite('ny403_08', 2)
    sprite('ny403_09', 3)
    CommonSE('005_swing_grap_2_1')
    ObjectUpon(FALLING, 35)
    CreateObject('Act2EventSummonSlowArea', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    CreateObject('NY_SlowHand', 0)
    SLOT_31 = 0
    CreateObject('Act2Event_moyamoya', 0)
    sprite('ny403_10', 3)
    sprite('ny403_11', 6)
    sprite('ny403_12', 6)
    label(0)
    sprite('ny403_09', 3)
    sprite('ny403_10', 3)
    sprite('ny403_11', 6)
    sprite('ny403_12', 6)
    gotoLabel(0)
    label(1)
    sprite('ny403_13', 6)
    sprite('ny403_14', 3)
    sprite('ny403_14', 3)
    enterState('CmnActStand')


@State
def Act2Event_Shake_nyvsbn():

    def upon_EVERY_FRAME():
        AddActionMark(1)
        if SLOT_2 >= 8:
            ScreenShake(3000, 2000)
            AddActionMark(-8)
            CommonSE('019_quake_0')
    sprite('keep', 2)
    sprite('ny615_08', 6)
    sprite('ny615_07', 6)
    sprite('ny615_06', 6)
    sprite('ny615_05', 6)
    sprite('ny615_04', 6)
    sprite('ny615_03', 6)
    sprite('ny615_02', 6)
    sprite('ny615_01', 6)
    sprite('ny615_00', 6)
    loopRest()
    label(0)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2EventNYvsCA00():

    def upon_IMMEDIATE():

        def upon_32():
            CreateObject('Act2EventSumDDMultiSword', -1)
            EnableAfterimage(1)
            AfterimageBlendMode(2)
            AfterimageCount(3)
            AfterimageMask_1(0, 255, 0, 127)
            AfterimageMask_2(0, 127, 0, 255)
            AfterimageSize_1(1030)
            AfterimageSize_2(1050)
            sendToLabel(0)
        uponSendToLabel(33, 1)
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    ObjectUpon(22, 32)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    label(2)
    sprite('ny300_04', 40)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    label(0)
    sprite('ny300_04', 8)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    sprite('ny300_04', 8)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    sprite('ny300_04', 8)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    sprite('ny300_04', 8)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    sprite('ny300_04', 8)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    gotoLabel(0)
    label(1)
    sprite('ny300_04', 3)
    TriggerUponForState('Act2EventEffBarrier', 32)
    ObjectUpon(22, 33)
    sprite('ny300_05', 3)
    sprite('ny300_06', 3)
    sprite('ny300_07', 3)
    label(5)
    sprite('ny300_08', 40)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    gotoLabel(5)


@State
def Act2EventNYvsCA00End():
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2EventNYvsCA02():
    sprite('null', 32767)
    ObjectUpon(22, 34)
    Visibility(1)


@State
def Act2EventNYvsCA03():
    SetZVal(-500)
    BlendMode_Normal()
    ScreenCollision(0)
    sprite('ny331_00', 2)
    AlphaValue(0)
    ObjectUpon(22, 35)
    sprite('ny331_04', 4)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(10)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    label(0)
    sprite('ny331_05', 6)
    sprite('ny331_06', 6)
    sprite('ny331_07', 6)
    gotoLabel(0)


@State
def Act2EventNYvsCA04():
    sprite('keep', 2)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RoundWinEnd2():
    sprite('ny615_08', 6)
    sprite('ny615_07', 6)
    sprite('ny615_06', 6)
    sprite('ny615_05', 6)
    sprite('ny615_00', 6)
    loopRest()
    enterState('EventDefEntryWait')


@State
def Act2Event_Signal0():
    sprite('keep', 2)
    ObjectUpon(22, 32)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Signal1():
    sprite('keep', 2)
    ObjectUpon(22, 33)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Signal2():
    sprite('keep', 2)
    ObjectUpon(22, 34)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_BDash():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
    sprite('ny033_00', 3)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(950)
    sprite('ny033_00', 3)
    PrivateSE('nyse_22')
    physicsXImpulse(-36000)
    sprite('ny033_01', 2)
    CreateParticle('nyef_ny033', 106)
    sprite('ny033_02', 2)
    CreateParticle('nyef_ny033', 106)
    sprite('ny033_03', 2)
    sprite('ny033_04', 2)
    sprite('ny033_01', 4)
    sprite('ny033_05', 4)
    sprite('ny033_06', 5)
    sprite('null', 2)
    EndMomentum(1)
    Visibility(1)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Down():
    StayAfterMovement(1, 0)
    sprite('ny070_00', 2)
    sprite('ny070_01', 2)
    sprite('ny070_02', 4)
    sprite('ny070_03', 4)
    sprite('ny070_04', 4)
    sprite('ny070_05', 6)
    KnockdownEffects(100, 1, 1)
    sprite('ny070_06', 7)
    sprite('ny070_07', 5)
    sprite('ny070_08', 5)
    sprite('ny070_09', 4)
    KnockdownEffects(100, 1, 1)
    Unknown1004()
    sprite('ny063_11', 32767)
    Unknown1005()
    loopRest()


@State
def Act3Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_novsny_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-960000)
        ScreenCollision(0)
    sprite('null', 20)
    sprite('ny430_05', 1)
    CreateObject('Act3Event_NY_SumDDMultiSword', -1)

    def RunOnObject_1():
        AddX(-120000)
    sprite('ny430_05', 1)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    ObjectUpon(22, 32)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_06', 3)
    sprite('ny430_07', 3)
    sprite('ny430_08', 3)
    sprite('ny430_09', 3)
    sprite('ny430_10', 4)
    sprite('ny430_11', 4)
    sprite('ny430_12', 32767)


@State
def Act3Event_novsny_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-960000)
        ScreenCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 360000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
                    physicsXImpulse(0)
                    SetInertia(10000)
            elif SLOT_XDistanceFromCenterOfStage > -360000:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(0)
                physicsXImpulse(0)
                SetInertia(10000)
    sprite('ny032_00', 2)
    physicsXImpulse(24000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    label(9)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ny032_05', 6)
    PrivateSE('nyse_22')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_06', 6)
    loopRest()
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act3Event_novsny_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('ny000_00', 7)
    sprite('ny070_00', 17)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('ny070_01', 4)
    AddInertia(-11000)
    sprite('ny070_02', 4)
    sprite('ny070_03', 32767)
    loopRest()


@State
def Act3Event_novsny_03():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('ny032_00', 2)
    physicsXImpulse(12000)
    SetAcceleration(1000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    SetActionMark(5)
    label(9)
    sprite('ny032_01', 4)
    AddActionMark(-1)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(9)
    label(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_novsny_04():
    sprite('ny070_10', 5)
    sprite('ny070_11', 5)
    sprite('ny070_12', 5)
    sprite('ny070_13', 5)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    sprite('ny000_00', 6)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_havsny_00():
    sprite('ny064_00', 8)
    sprite('ny064_01', 8)
    sprite('ny064_02', 8)
    sprite('ny064_03', 32767)


@State
def Act3Event_havsny_01():
    sprite('ny064_03', 4)
    CreateObject('Act3Event_TeniObj', -1)
    ConstantAlphaModifier(-4)
    sprite('ny064_03', 4)
    sprite('ny064_03', 5)
    sprite('ny064_03', 5)
    sprite('ny064_03', 32767)
    Visibility(1)


@State
def Act3Event_havsny_02():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('ny010_01', 3)
    sprite('ny010_00', 3)
    sprite('ny003_02', 3)
    Flip()
    sprite('ny003_01', 3)
    sprite('ny003_00', 3)
    sprite('ny032_00', 2)
    physicsXImpulse(12000)
    SetAcceleration(1000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    SetActionMark(5)
    label(9)
    sprite('ny032_01', 4)
    AddActionMark(-1)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(9)
    label(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_nyvsha_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)

        def upon_32():
            sendToLabel(1)
    sprite('ny030_00', 7)
    physicsXImpulse(1650)
    sprite('ny030_01', 7)
    PrivateSE('GG2_218SE')
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_02', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_03', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_04', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_05', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_06', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_07', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_08', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_09', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_10', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_01', 7)
    PrivateSE('GG2_218SE')
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_02', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_03', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny030_04', 7)
    CreateParticle('nyef_ny030', -1)
    sprite('ny000_00', 6)
    EndMomentum(1)
    label(0)
    sprite('ny000_01', 6)
    sprite('ny000_02', 6)
    sprite('ny000_03', 6)
    sprite('ny000_04', 6)
    sprite('ny000_05', 6)
    sprite('ny000_06', 6)
    sprite('ny000_07', 6)
    sprite('ny000_08', 6)
    sprite('ny000_09', 6)
    sprite('ny000_00', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny090_00', 10)
    EndMomentum(1)
    sprite('ny090_00', 10)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('104_guard_grap_1')
    CommonSE('106_guard_crush')
    ScreenShake(3000, 18000)
    AddInertia(-60000)
    sprite('ny090_01', 4)
    sprite('ny090_02', 6)
    CameraControlEnable(1)
    sprite('ny090_03', 60)
    sprite('ny090_04', 6)
    ObjectUpon(22, 32)
    sprite('ny000_00', 6)
    sprite('ny032_00', 2)
    physicsXImpulse(32000)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_01', 4)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_05', 5)
    AddInertia(10000)
    physicsXImpulse(0)
    sprite('ny032_06', 5)
    sprite('ny032_06', 1)
    EndMomentum(1)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_nyvsha_01():
    sprite('ny203_00', 6)
    sprite('ny203_01', 6)
    sprite('ny203_02', 6)
    sprite('ny203_03', 8)
    sprite('ny203_04', 12)
    sprite('ny203_05', 6)
    sprite('ny203_06', 6)
    sprite('ny203_01', 6)
    sprite('ny203_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_nyvsrm_00():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    sprite('ny300_04', 32767)


@State
def Act3Event_nyvsrm_01():
    sprite('keep', 2)
    sprite('ny300_03', 6)
    sprite('ny300_02', 6)
    sprite('ny300_01', 6)
    sprite('ny300_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_nyvsrm_02():
    label(0)
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    sprite('ny611_14', 7)
    sprite('ny611_15', 7)
    sprite('ny611_16', 7)
    sprite('ny611_17', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_nyvsrm_03():
    sprite('ny611_13', 6)
    CreateParticle('nyef_entrymc', 0)
    PrivateSE('nyse_28')
    sprite('ny611_10', 6)
    sprite('ny611_09', 6)
    sprite('ny611_08', 6)
    sprite('ny611_07', 6)
    sprite('ny611_06', 6)
    sprite('ny611_05', 6)
    sprite('ny611_04', 6)
    sprite('ny611_03', 6)
    sprite('ny611_02', 7)
    sprite('ny611_01', 7)
    sprite('ny611_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_nyvsrm_04():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    CreateObject('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 20)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    sprite('ny300_04', 80)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_nyvsrc_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('ny032_00', 2)
    physicsXImpulse(12000)
    SetAcceleration(1000)
    PrivateSE('nyse_20')
    CreateParticle('nyef_ny030', -1)
    SetActionMark(5)
    label(9)
    sprite('ny032_01', 4)
    AddActionMark(-1)
    sprite('ny032_02', 4)
    PrivateSE('nyse_21')
    sprite('ny032_03', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    sprite('ny032_04', 4)
    PrivateSE('nyse_21')
    CreateParticle('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(9)
    label(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_nyvsmu_00():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('ny409_00', 3)
    sprite('ny409_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    sprite('ny409_01', 2)
    sprite('ny409_02', 3)
    sprite('ny409_03', 3)
    sprite('ny409_04', 3)
    sprite('ny409_05', 5)
    CommonSE('006_swing_blade_2')
    sprite('ny409_06', 2)
    sprite('ny409_06', 1)
    ObjectUpon(22, 32)
    sprite('ny409_07', 3)
    sprite('ny409_08', 4)
    sprite('ny409_09', 3)
    sprite('ny409_10', 3)
    sprite('ny409_11', 3)
    sprite('ny409_12', 3)
    sprite('ny409_13', 3)
    sprite('ny409_14', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_nyvsmu_01():
    sprite('ny450_00', 6)
    sprite('ny450_01', 6)
    label(0)
    sprite('ny450_02', 6)
    sprite('ny450_03', 6)
    sprite('ny450_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevsny_00():
    sprite('ny300_04', 1)
    ObjectUpon(22, 32)
    sprite('ny300_04', 10)
    sprite('ny300_05', 6)
    sprite('ny300_06', 6)
    sprite('ny300_07', 6)
    TriggerUponForState('Event_EF_ny300', 32)
    sprite('ny300_08', 8)
    sprite('ny300_09', 20)
    sprite('ny300_10', 4)
    sprite('ny300_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevsny_01():

    def upon_EVERY_FRAME():
        Unknown61(0, 1, 0, 30, 0, 0, 0, 9999, 0, 9999, 0, 9999)
        SLOT_51 = SLOT_0
        if SLOT_51 > 15:
            if random_(2, 0, 10):
                CommonSE('014_electric_s')
            CreateParticle('nyef_timeupptc', -1)
    label(0)
    sprite('ny010_02', 6)
    sprite('ny010_03', 6)
    sprite('ny010_04', 6)
    sprite('ny010_05', 6)
    sprite('ny010_06', 6)
    sprite('ny010_07', 6)
    sprite('ny010_08', 6)
    sprite('ny010_09', 6)
    sprite('ny010_10', 6)
    sprite('ny010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevsny_02():

    def upon_IMMEDIATE():
        SetZVal(-500)
        ScreenCollision(0)
        BlendMode_Normal()
    sprite('keep', 26)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    CreateObject('Act3Event_teni', -1)

    def RunOnObject_1():
        AddX(-20000)
        AddY(120000)
    sprite('keep', 1)
    XPositionRelativeFacing(-500000)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_cevsny_03():
    sprite('ny300_00', 4)
    sprite('ny300_01', 4)
    sprite('ny300_02', 6)
    sprite('ny300_03', 6)
    sprite('ny300_04', 20)
    CreateObject('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 100)
    CreateParticle('nyef_entrymc', -1)
    PrivateSE('nyse_28')
    loopRest()
    gotoLabel(0)
