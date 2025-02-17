@Subroutine
def PreInit():
    CharacterID('iz')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(4800)
    WalkBSpeed(3200)
    DashFInitialVelocity(18000)
    DashFAccel(200)
    DashFMaxVelocity(28000)
    JumpYVelocity(31000)
    SuperJumpYVelocity(38000)
    Gravity(1850)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    if SLOT_116:
        Health(14000)
        WalkFSpeed(7200)
        WalkBSpeed(4800)
        DashFInitialVelocity(23000)
        DashFMaxVelocity(28000)
        OverdriveDuration(780, 780, 780, 780, 780, 780, 780, 780, 780, 780)
    ResourceGauge(0, 1, 2, 8, 8, 0, -16744320, -12240)
    ResourceGauge(1, 1, 42, 1, 720, 0, -52429, -52429)
    HideResourceGauge(1, 1)
    ResourceBarFlashIfFull(1, 1)
    CPUJumpPriority(100)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 300000, -100000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    DamageStunPriority(1)
    SkillEstimateRange(0, 400000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    MoveLow()
    DamageStunPriority(4000)
    SkillEstimateRange(0, 430000, -150000, 120000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(200)
    SkillEstimateRange(100000, 500000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMid()
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    AirborneOpponentPriority(0)
    SkillEstimateRange(0, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    Move_Condition(0x3008)
    DamageStunPriority(1500)
    SkillEstimateRange(0, 400000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk5C', INPUT_5C)
    Move_Condition(0x3000)
    SkillEstimateRange(-50000, 350000, -150000, 400000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    Move_Condition(0x3008)
    DamageStunPriority(1)
    SkillEstimateRange(150000, 450000, -150000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk6C', INPUT_6C)
    Move_Condition(0x3000)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(150000, 500000, -150000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    Move_Condition(0x3008)
    SkillEstimateRange(0, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk2C', INPUT_2C)
    Move_Condition(0x3000)
    AirborneOpponentPriority(1)
    MoveCancellableFrames(40, 42)
    SkillEstimateRange(0, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    Move_Condition(0x3008)
    MoveLow()
    SkillEstimateRange(0, 300000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk3C', INPUT_3C)
    Move_Condition(0x3000)
    MoveLow()
    DamageStunPriority(500)
    SkillEstimateRange(0, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    Move_Condition(0x3008)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(0, 400000, -250000, 600000, 0, 1000)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk5D', INPUT_5D)
    Move_Condition(0x3000)
    TempPriorityMultiplierInterval(0, 0, 250, 1000, 0)
    SkillEstimateRange(0, 300000, -250000, 600000, 0, 1000)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    Move_Condition(0x3008)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(0, 400000, -250000, 600000, 0, 1000)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtk2D', INPUT_2D)
    Move_Condition(0x3000)
    TempPriorityMultiplierInterval(0, 0, 250, 1000, 0)
    SkillEstimateRange(0, 300000, -250000, 600000, 0, 1000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(250)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    GuardStunPriority(2000)
    SkillEstimateRange(-150000, 250000, -300000, 100000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    Move_Condition(0x3008)
    SkillEstimateRange(-50000, 350000, -500000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtkAIR5C', INPUT_J5C)
    Move_Condition(0x3000)
    DamageStunPriority(3000)
    SkillEstimateRange(-150000, 250000, -350000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x3008)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1000)
    SkillEstimateRange(-250000, 250000, -250000, 250000, 0, 1000)
    Move_EndRegister()
    Move_Register('Kakusei_NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x3000)
    TempPriorityMultiplierInterval(0, 0, 250, 1000, 0)
    SkillEstimateRange(-200000, 200000, -200000, 200000, 0, 1000)
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
    Move_Register('Shot_A', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(1)
    AirborneOpponentPriority(1)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1000000, -100000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Shot_D', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(300000, 800000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShot_A', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    GuardStunPriority(1)
    OpponentAttackPriority(2000)
    SkillEstimateRange(200000, 600000, -1000000, -200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShot_D', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(200000, 600000, -1000000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(1200)
    SkillEstimateRange(0, 550000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash_Gedan', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    MoveLow()
    AirborneOpponentPriority(0)
    GuardStunPriority(1200)
    SkillEstimateRange(100000, 400000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('Iai_AntiAirA', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    AirborneOpponentPriority(3000)
    SkillEstimateRange(100000, 500000, -130000, 500000, 350, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash_Gedan_Easy', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_B)
    StateCall('Iai_Slash_Gedan')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Iai_AntiAirB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(1)
    OpponentAttackPriority(5000)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(-200000, 200000, -100000, 600000, 250, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAirB', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    SkillEstimateRange(0, 650000, -150000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAirC', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    SkillEstimateRange(0, 650000, -300000, -100000, 150, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAirA', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    SkillEstimateRange(0, 650000, 200000, 500000, 150, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAirC_Easy', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_B)
    StateCall('Iai_SlashAirC')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Iai_Slash_Next', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    SkillEstimateRange(250000, 1000000, -200000, 30000, 1500, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash_NextAir', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    SkillEstimateRange(250000, 1000000, -200000, 30000, 1500, 0)
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Iai_AntiAir_Next', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(1500)
    DamageStunPriority(10000)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(1000)
    GuardStunPriority(0)
    SkillEstimateRange(0, 400000, -150000, 200000, 150, 0)
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Warp_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(1)
    GuardStunPriority(1000)
    SkillEstimateRange(0, 400000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('Warp_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(1)
    Unknown15027(0)
    GuardStunPriority(250)
    TempPriorityMultiplierInterval(0, 250, 1000, 0, 4000)
    SkillEstimateRange(0, 500000, -200000, 500000, 250, 50)
    Move_EndRegister()
    Move_Register('Warp_C', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(1)
    DamageStunPriority(0)
    GuardStunPriority(4000)
    SkillEstimateRange(0, 500000, -500000, 500000, 250, 50)
    Move_EndRegister()
    Move_Register('Warp_D_Land', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(0)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 400000, -200000, 600000, 0, 200)
    Move_EndRegister()
    Move_Register('Warp_D_Air', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(0)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 400000, -300000, 100000, 0, 100)
    Move_EndRegister()
    Move_Register('Warp_D_LandHitOnly', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2000)
    FollowupOnly(1)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    TempPriorityMultiplierInterval(0, 250, 1000, 0, 2500)
    SkillEstimateRange(-200000, 600000, -200000, 800000, 1000, 0)
    Move_EndRegister()
    Move_Register('Warp_D_AirHitOnly', INPUT_SPECIALMOVE)
    Move_Condition(0x3000)
    CallSkillConditions('CheckExGageVal1')
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    TempPriorityMultiplierInterval(0, 500, 1000, 0, 1500)
    SkillEstimateRange(-200000, 600000, -300000, 800000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(4000)
    DamageStunPriority(2500)
    GuardStunPriority(0)
    SkillEstimateRange(50000, 700000, 50000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    OpponentAttackPriority(4000)
    DamageStunPriority(2500)
    GuardStunPriority(0)
    SkillEstimateRange(50000, 700000, 50000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('SummonFunnel', INPUT_DISTORTION)
    Move_Condition(0x3000)
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(500)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x2000)
    Move_Condition(0x304a)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(1)
    OpponentAttackPriority(1500)
    DamageStunPriority(2500)
    SkillEstimateRange(150000, 700000, -150000, 550000, 250, 0)
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
    SkillEstimateRange(0, 600000, -200000, 150000, 500, 10)
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
    SkillEstimateRange(0, 600000, -200000, 150000, 500, 10)
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
    SkillEstimateRange(0, 600000, -200000, 150000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'Iai_Slash', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'Iai_Slash_Gedan', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Iai_Slash', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Iai_Slash_Gedan', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Iai_AntiAirA', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Iai_Slash', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'AstralHeat', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'Iai_SlashAirC', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'Kakusei_NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'Kakusei_NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'Kakusei_NmlAtk5C', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk5C', 'Iai_Slash', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk5C', 'Iai_AntiAirA', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk5C', 'Iai_AntiAirB', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk2C', 'Kakusei_NmlAtk3C', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk2C', 'AstralHeat', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtk3C', 'Iai_Slash', 10000000)
    TempPriorityMultiplier('Kakusei_NmlAtkAIR5C', 'AirAssault', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirShot_A', 10000000)
    TempPriorityMultiplier('Iai_Slash', 'Iai_Slash_Next', 10000000)
    TempPriorityMultiplier('Iai_Slash', 'Warp_B', 10000000)
    TempPriorityMultiplier('Iai_Slash', 'Warp_C', 10000000)
    TempPriorityMultiplier('Iai_Slash_Gedan', 'Iai_Slash_Next', 10000000)
    TempPriorityMultiplier('Iai_Slash_Gedan', 'Warp_A', 10000000)
    TempPriorityMultiplier('Iai_Slash_Gedan', 'Warp_C', 10000000)
    TempPriorityMultiplier('Iai_AntiAirA', 'Iai_AntiAir_Next', 10000000)
    TempPriorityMultiplier('Iai_AntiAirA', 'Warp_B', 10000000)
    TempPriorityMultiplier('Iai_AntiAirA', 'Warp_C', 10000000)
    TempPriorityMultiplier('Iai_AntiAirA', 'Warp_D_LandHitOnly', 10000000)
    TempPriorityMultiplier('Iai_AntiAirB', 'Iai_AntiAir_Next', 10000000)
    TempPriorityMultiplier('Iai_AntiAirB', 'Warp_D_LandHitOnly', 10000000)
    TempPriorityMultiplier('AirAssault', 'Warp_D_AirHitOnly', 10000000)
    TempPriorityMultiplier('AirAssault', 'Iai_AntiAir_Next', 10000000)
    TempPriorityMultiplier('Shot_A', 'Warp_D_Air', 10000000)
    TempPriorityMultiplier('AirShot_A', 'Warp_D_Air', 10000000)
    TempPriorityMultiplier('Iai_AntiAir_Next', 'Warp_B', 10000000)
    TempPriorityMultiplier('Iai_AntiAir_Next', 'Warp_C', 10000000)
    TempPriorityMultiplier('Iai_Slash_Next', 'Warp_B', 10000000)
    TempPriorityMultiplier('Iai_Slash_Next', 'Warp_C', 10000000)
    TempPriorityMultiplier('UltimateAssault', 'Warp_D_Land', 10000000)
    TempPriorityMultiplier('UltimateAssault_OD', 'Warp_D_Land', 10000000)
    StylishModeSpecialButton('Iai_AntiAirB', 0x4, 0xea)
    StylishModeSpecialButton('Iai_Slash', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('Shot_A', 0x4, 0x45)
    StylishModeSpecialButton('Shot_D', 0x4, 0x45)
    StylishModeSpecialButton('Iai_SlashAirC', 0x4, 0xea)
    StylishModeSpecialButton('Iai_SlashAirB', 0x4, 0x79)
    StylishModeSpecialButton('Warp_D_Air', 0x4, 0x5f)
    StylishModeSpecialButton('AirShot_A', 0x4, 0x45)
    StylishModeSpecialButton('AirShot_D', 0x4, 0x45)
    StylishModeSpecialButton('Warp_D_LandHitOnly', 0x4, 0xea)
    StylishModeSpecialButton('Warp_D_AirHitOnly', 0x4, 0xea)
    StylishModeSpecialButton('Iai_Slash_Next', 0x4, 0xea)
    StylishModeSpecialButton('Iai_AntiAir_Next', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5B', 'Iai_Slash', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 1, 350000)
    StylishModeCancels('NmlAtk5B', 'Kakusei_NmlAtk5C', 1, 250000)
    StylishModeCancels('NmlAtk5B', 'Iai_AntiAirA', 3, 0)
    StylishModeCancels('NmlAtk5C', 'Iai_Slash_Gedan', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 1, 200000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk5C', 'Iai_AntiAirA', 12, 0)
    StylishModeCancels('NmlAtk5C', 'Shot_A', 13, 0)
    StylishModeCancels('Kakusei_NmlAtk5C', 'Kakusei_NmlAtk3C', 0, 0)
    StylishModeCancels('Kakusei_NmlAtk5C', 'Kakusei_NmlAtk2C', 8, 0)
    StylishModeCancels('Kakusei_NmlAtk5C', 'FJump', 12, 0)
    StylishModeCancels('Kakusei_NmlAtk5C', 'Shot_A', 13, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk6A', 'Iai_AntiAirA', 12, 0)
    StylishModeCancels('NmlAtk6B', 'Iai_SlashAirC', 6, 0)
    StylishModeCancels('NmlAtk6B', 'AirShot_A', 13, 0)
    StylishModeCancels('NmlAtk6C', 'Iai_Slash_Gedan', 0, 0)
    StylishModeCancels('Kakusei_NmlAtk6C', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5C', 12, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 12, 0)
    StylishModeCancels('NmlAtk2C', 'Iai_Slash_Gedan', 0, 0)
    StylishModeCancels('NmlAtk2C', 'Iai_AntiAirA', 3, 0)
    StylishModeCancels('NmlAtk2C', 'Shot_A', 13, 0)
    StylishModeCancels('Kakusei_NmlAtk2C', 'Shot_A', 0, 0)
    StylishModeCancels('Kakusei_NmlAtk2C', 'Kakusei_NmlAtk3C', 6, 0)
    StylishModeCancels('Kakusei_NmlAtk2C', 'Kakusei_NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk3C', 'Iai_Slash', 0, 0)
    StylishModeCancels('Kakusei_NmlAtk3C', 'Iai_Slash', 0, 0)
    StylishModeCancels('Kakusei_NmlAtk3C', 'UltimateAssault', 6, 0)
    StylishModeCancels('Kakusei_NmlAtk3C', 'UltimateAssault_OD', 6, 0)
    StylishModeCancels('Kakusei_NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'Kakusei_NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('Kakusei_NmlAtkAIR5C', 'Iai_SlashAirC', 0, 0)
    StylishModeCancels('Kakusei_NmlAtkAIR5C', 'Iai_SlashAirA', 3, 0)
    StylishModeCancels('Kakusei_NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('Iai_Slash', 'Warp_B', 0, 0)
    StylishModeCancels('Iai_Slash', 'Iai_Slash_Next', 6, 0)
    StylishModeCancels('Iai_Slash', 'Warp_C', 13, 0)
    StylishModeCancels('Iai_Slash_Gedan', 'Warp_A', 0, 0)
    StylishModeCancels('Iai_Slash_Gedan', 'Iai_Slash_Next', 6, 0)
    StylishModeCancels('Iai_Slash_Gedan', 'Warp_C', 13, 0)
    StylishModeCancels('Iai_AntiAirA', 'Warp_B', 0, 0)
    StylishModeCancels('Iai_AntiAirA', 'Warp_D_LandHitOnly', 6, 0)
    StylishModeCancels('Iai_AntiAirA', 'Warp_C', 13, 0)
    StylishModeCancels('Iai_AntiAirB', 'Iai_AntiAir_Next', 0, 0)
    StylishModeCancels('Iai_SlashAirA', 'Iai_AntiAir_Next', 0, 0)
    StylishModeCancels('Iai_SlashAirA', 'Warp_D_Air', 4, 0)
    StylishModeCancels('Iai_SlashAirB', 'Iai_AntiAir_Next', 0, 0)
    StylishModeCancels('Iai_SlashAirB', 'Warp_D_Air', 4, 0)
    StylishModeCancels('Iai_SlashAirC', 'Iai_AntiAir_Next', 0, 0)
    StylishModeCancels('Iai_SlashAirC', 'Warp_D_Air', 4, 0)
    StylishModeCancels('Iai_AntiAir_Next', 'Warp_B', 0, 0)
    StylishModeCancels('Iai_Slash_Next', 'Warp_B', 0, 0)
    StylishModeCancels('Shot_D', 'Warp_D_Land', 0, 0)
    StylishModeCancels('AirShot_A', 'Warp_D_Air', 0, 0)
    StylishModeCancels('AirShot_D', 'Warp_D_Air', 0, 0)
    StylishModeCancels('ThrowExe', 'Warp_B', 0, 0)
    StylishModeCancels('BackThrowExe', 'Warp_B', 0, 0)
    HitSprites(0, 'iz062_01')
    HitSprites(1, 'iz062_03')
    HitSprites(2, 'iz062_04')
    HitSprites(3, 'iz062_05')
    HitSprites(4, 'iz062_05')
    HitSprites(5, 'iz062_06')
    HitSprites(6, 'iz062_07')
    HitSprites(7, 'iz041_02')
    HitSprites(8, 'iz040_02')
    HitSprites(9, 'iz045_02')
    HitSprites(10, 'iz060_00')
    HitSprites(11, 'iz060_01')
    HitSprites(12, 'iz060_03')
    HitSprites(13, 'iz060_05')
    HitSprites(14, 'iz060_07')
    HitSprites(15, 'iz060_14')
    HitSprites(16, 'iz050_00')
    HitSprites(17, 'iz052_00')
    HitSprites(18, 'iz054_00')
    HitSprites(19, 'iz000_00')
    HitSprites(20, 'iz000_00')
    HitSprites(25, 'iz063_00')
    HitSprites(26, 'iz063_01')
    HitSprites(27, 'iz063_02')
    HitSprites(28, 'iz063_04')
    HitSprites(29, 'iz063_10')
    HitSprites(30, 'iz077_00')
    HitSprites(31, 'iz077_01')
    HitSprites(32, 'iz077_00ex01')
    HitSprites(33, 'iz077_01ex01')
    HitSprites(34, 'iz077_00ex02')
    HitSprites(35, 'iz077_01ex02')
    HitSprites(36, 'iz077_00ex03')
    HitSprites(37, 'iz077_01ex03')
    HitSprites(24, 'iz073_01')
    CommonVoicelines(0, 'iz000')
    CommonVoicelines(1, 'iz001')
    CommonVoicelines(2, 'iz002')
    CommonVoicelines(3, 'iz003')
    CommonVoicelines(4, 'iz004')
    CommonVoicelines(5, 'iz005')
    CommonVoicelines(6, 'iz006')
    CommonVoicelines(7, 'iz007')
    CommonVoicelines(8, 'iz008')
    CommonVoicelines(9, 'iz009')
    CommonVoicelines(10, 'iz010')
    CommonVoicelines(11, 'iz011')
    CommonVoicelines(12, 'iz012')
    CommonVoicelines(13, 'iz013')
    CommonVoicelines(14, 'iz014')
    CommonVoicelines(15, 'iz015')
    CommonVoicelines(16, 'iz016')
    CommonVoicelines(17, 'iz017')
    CommonVoicelines(18, 'iz018')
    CommonVoicelines(19, 'iz019')
    CommonVoicelines(20, 'iz020')
    CommonVoicelines(21, 'iz021')
    CommonVoicelines(22, 'iz022')
    CommonVoicelines(23, 'iz023')
    CommonVoicelines(24, 'iz024')
    CommonVoicelines(25, 'iz025')
    CommonVoicelines(26, 'iz026')
    CommonVoicelines(27, 'iz027')
    CommonVoicelines(28, 'iz028')
    CommonVoicelines(29, 'iz029')
    CommonVoicelines(30, 'iz030')
    CommonVoicelines(31, 'iz031')
    CommonVoicelines(32, 'iz032')
    CommonVoicelines(33, 'iz033')
    CommonVoicelines(34, 'iz034')
    CommonVoicelines(35, 'iz035')
    CommonVoicelines(36, 'iz036')
    CommonVoicelines(37, 'iz037')
    CommonVoicelines(38, 'iz038')
    CommonVoicelines(39, 'iz039')
    CommonVoicelines(40, 'iz040')
    CommonVoicelines(41, 'iz041')
    CommonVoicelines(42, 'iz042')
    CommonVoicelines(43, 'iz043')
    CommonVoicelines(44, 'iz044')
    CommonVoicelines(45, 'iz045')
    CommonVoicelines(46, 'iz046')
    CommonVoicelines(47, 'iz047')
    CommonVoicelines(48, 'iz048')
    CommonVoicelines(49, 'iz049')
    CommonVoicelines(50, 'iz050')
    CommonVoicelines(51, 'iz051')
    CommonVoicelines(52, 'iz052')
    CommonVoicelines(53, 'iz053')
    CommonVoicelines(54, 'iz100')
    CommonVoicelines(55, 'iz101')
    CommonVoicelines(56, 'iz102')
    CommonVoicelines(57, 'iz103')
    CommonVoicelines(58, 'iz104')
    CommonVoicelines(59, 'iz105')
    CommonVoicelines(60, 'iz106')
    CommonVoicelines(61, 'iz107')
    CommonVoicelines(62, 'iz108')
    CommonVoicelines(63, 'iz109')
    CommonVoicelines(64, 'iz150')
    CommonVoicelines(65, 'iz151')
    CommonVoicelines(66, 'iz152')
    CommonVoicelines(67, 'iz153')
    CommonVoicelines(68, 'iz154')
    CommonVoicelines(69, 'iz155')
    CommonVoicelines(70, 'iz156')
    CommonVoicelines(71, 'iz157')
    CommonVoicelines(72, 'iz158')
    CommonVoicelines(75, 'iz160')
    CommonVoicelines(73, 'iz402')
    CommonVoicelines(74, 'iz403')
    CreateObject('EffLightSaber', -1)
    CreateObject('Twindrive0', -1)
    CreateObject('Twindrive1', -1)


@Subroutine
def MatchInit2():
    TrainingModeSLOT('TRI_IzayoiActiveMode', 2, 67)
    if SLOT_67:
        if not SLOT_4:
            SLOT_4 = 1


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        TrainingModeSLOT('TRI_IzayoiInstall', 2, 67)
        if SLOT_67:
            if SLOT_InNeutral:
                if SLOT_31 < SLOT_67:
                    SLOT_31 = SLOT_67
        if SLOT_60 > 0:
            SLOT_60 = SLOT_60 + -1
        if SLOT_32:
            if SLOT_21:
                if SLOT_32 > 0:
                    if SLOT_OverdriveTimer:
                        SLOT_32 = SLOT_32 + -1
                    else:
                        SLOT_32 = SLOT_32 + -2
                TrainingModeSLOT('TRI_IzayoiSupportBit', 2, 67)
                if SLOT_67:
                    SLOT_32 = 720
        if SLOT_21:
            if SLOT_116:
                SLOT_DamageMultiplier = 110
                HeatChange(3)
    if not SLOT_21:
        SLOT_32 = 0
    if SLOT_OverdriveTimer:
        if not SLOT_81:
            if SLOT_4:
                SLOT_61 = SLOT_61 + 2
            else:
                SLOT_61 = SLOT_61 + 3
        if SLOT_61 >= 120:
            SLOT_31 = SLOT_31 + 1
            SLOT_61 = 0
        if not SLOT_OverdriveTimer:
            SLOT_61 = 0


@Subroutine
def OnActionBeginPre():
    if SLOT_4:
        WalkFSpeed(6200)
        WalkBSpeed(4800)
        AirDashFSpeed(32000)
        AirFDashDuration(18)
        AirDashBSpeed(25000)
        AirBDashDuration(12)
        AirFDashGravity(0)
        AirBDashGravity(0)
        AirDashCount(2)
        Unknown12040(120000)
        DashFInitialVelocity(0)
        DashFAccel(0)
        DashFMaxVelocity(0)
        JumpYVelocity(35000)
        SuperJumpYVelocity(42000)
    else:
        WalkFSpeed(5200)
        WalkBSpeed(3200)
        DashFInitialVelocity(16000)
        DashFAccel(200)
        DashFMaxVelocity(32000)
        AirDashFSpeed(26000)
        AirFDashDuration(16)
        AirDashBSpeed(24000)
        AirBDashDuration(12)
        AirFDashGravity(0)
        AirBDashGravity(0)
        AirDashCount(1)
        Unknown12040(0)
        DashFInitialVelocity(18000)
        DashFAccel(200)
        DashFMaxVelocity(28000)
        JumpYVelocity(38000)
        SuperJumpYVelocity(43000)
        Gravity(1850)
        GroundDashCount(1)


@Subroutine
def CheckExGageVal1():
    SLOT_47 = 0
    if SLOT_31 >= 1:
        SLOT_47 = 1


@Subroutine
def CheckExGageVal2():
    SLOT_47 = 0
    if SLOT_31 >= 2:
        SLOT_47 = 1


@Subroutine
def CheckExGageVal3():
    SLOT_47 = 0
    if SLOT_31 >= 3:
        SLOT_47 = 1


@Subroutine
def CheckExGageVal4():
    SLOT_47 = 0
    if SLOT_31 >= 4:
        SLOT_47 = 1


@Subroutine
def AdditionalExGage():
    if not SLOT_4:

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_31 = SLOT_31 + 1

        def upon_OPPONENT_HIT():
            SLOT_31 = SLOT_31 + 1


@Subroutine
def MyStatusSave():
    SLOT_6 = SLOT_4


@Subroutine
def CheckShieidBitAvailable():
    if SLOT_21:
        if SLOT_60 == 0:
            ObjectUpon(FALLING, 35)
            ObjectUpon(5, 35)
            SLOT_60 = 60


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnPreDraw():
    CallPrivateFunction('IzLightSaberSwitch', 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActStand():
    label(0)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    if random_(2, 0, 40):
        gotoLabel(30)
    if random_(2, 0, 30):
        gotoLabel(31)
    if random_(2, 0, 50):
        gotoLabel(32)
    label(30)
    sprite('iz002_00', 6)
    SLOT_88 = 960
    Voiceline('iz000')
    sprite('iz002_01', 6)
    sprite('iz002_02', 6)
    sprite('iz002_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_04', 6)
    sprite('iz002_05', 6)
    sprite('iz002_06', 6)
    sprite('iz002_07', 6)
    sprite('iz002_08', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_09', 6)
    sprite('iz002_10', 6)
    loopRest()
    gotoLabel(0)
    label(31)
    sprite('iz002_11', 4)
    SLOT_88 = 960
    Voiceline('iz000')
    PrivateSE('izse_01')
    sprite('iz002_12', 4)
    sprite('iz002_13', 4)
    sprite('iz002_14', 4)
    sprite('iz002_15', 5)
    sprite('iz002_16', 5)
    sprite('iz002_17', 5)
    sprite('iz002_18', 5)
    sprite('iz002_19', 5)
    loopRest()
    gotoLabel(0)
    label(32)
    sprite('iz002_20', 7)
    SLOT_88 = 960
    Voiceline('iz000')
    sprite('iz002_21', 7)
    sprite('iz002_22', 7)
    sprite('iz002_23', 7)
    sprite('iz002_24', 7)
    sprite('iz002_25', 7)
    sprite('iz002_26', 7)
    sprite('iz002_27', 7)
    sprite('iz002_28', 7)
    sprite('iz002_29', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('iz003_00', 3)
    SmartVoiceline('iz001')
    sprite('iz003_01', 3)
    sprite('iz003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('iz010_00', 4)
    sprite('iz010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('iz010_02', 7)
    sprite('iz010_03', 7)
    sprite('iz010_04', 7)
    sprite('iz010_05', 7)
    sprite('iz010_06', 7)
    sprite('iz010_07', 7)
    sprite('iz010_08', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('iz013_00', 3)
    sprite('iz013_01', 3)
    sprite('iz013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('iz010_01', 4)
    sprite('iz010_00', 4)


@State
def CmnActJumpPre():
    sprite('iz023_00', 2)
    sprite('iz023_01', 2)


@State
def CmnActJumpUpper():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    SmartVoiceline('iz002')
    label(10)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    SmartVoiceline('iz002')
    label(11)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    SmartVoiceline('iz003')
    label(22)
    sprite('iz020_00', 3)
    sprite('iz020_01', 3)
    loopRest()
    gotoLabel(22)


@State
def CmnActJumpUpperEnd():
    sprite('iz020_02', 3)
    sprite('iz020_03', 3)
    sprite('iz020_04', 3)


@State
def CmnActJumpDown():
    sprite('iz020_05', 3)
    sprite('iz020_06', 3)
    label(0)
    sprite('iz020_07', 4)
    sprite('iz020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('iz024_00', 3)
    sprite('iz024_01', 3)
    sprite('iz024_02', 3)
    sprite('iz024_03', 3)
    sprite('iz024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('iz024_00', 2)
    sprite('iz024_01', 2)
    sprite('iz024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('iz024_03', 3)
    sprite('iz024_04', 3)


@State
def CmnActFWalk():
    sprite('iz030_00', 7)
    label(0)
    sprite('iz030_01', 7)
    sprite('iz030_02', 7)
    sprite('iz030_03', 7)
    sprite('iz030_04', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz030_05', 7)
    sprite('iz030_06', 7)
    sprite('iz030_07', 7)
    sprite('iz030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('iz031_00', 7)
    label(0)
    sprite('iz031_01', 7)
    sprite('iz031_02', 7)
    sprite('iz031_03', 7)
    sprite('iz031_04', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz031_05', 7)
    sprite('iz031_06', 7)
    sprite('iz031_07', 7)
    sprite('iz031_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        if SLOT_4:
            enterState('SpDashF_Land')
    sprite('iz032_00', 2)
    label(0)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('iz032_09', 3)
    sprite('iz032_10', 3)
    sprite('iz032_11', 3)
    loopRest()
    ExitState()


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
        InvincibilityDuration(5)
        if SLOT_4:
            enterState('SpDashB_Land')
    sprite('iz033_00', 1)
    sprite('iz033_01', 2)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('iz033_02', 3)
    sprite('iz033_03', 1)
    sprite('iz033_03', 2)
    loopRest()
    label(0)
    sprite('iz033_02', 3)
    sprite('iz033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz033_04', 3)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('iz033_05', 3)
    ExitState()


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        if SLOT_4:
            enterState('SpDashF_Air')
    sprite('iz035_00', 3)
    SmartVoiceline('iz004')
    label(0)
    sprite('iz035_01', 3)
    sprite('iz035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        if SLOT_4:
            enterState('SpDashB_Air')
    sprite('iz036_00', 3)
    SmartVoiceline('iz006')
    label(0)
    sprite('iz036_01', 3)
    sprite('iz036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('iz050_00', 1)
    sprite('iz050_01', 1)
    sprite('iz050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('iz050_01', 1)
    sprite('iz050_02', 1)
    sprite('iz050_01', 2)
    sprite('iz050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('iz050_02', 1)
    sprite('iz050_03', 1)
    sprite('iz050_02', 2)
    sprite('iz050_01', 2)
    sprite('iz050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('iz050_03', 1)
    sprite('iz050_04', 1)
    sprite('iz050_03', 2)
    sprite('iz050_02', 2)
    sprite('iz050_01', 2)
    sprite('iz050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('iz050_04', 1)
    sprite('iz050_04', 1)
    sprite('iz050_04', 2)
    sprite('iz050_03', 2)
    sprite('iz050_02', 2)
    sprite('iz050_01', 2)
    sprite('iz050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('iz052_00', 1)
    sprite('iz052_01', 1)
    sprite('iz052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('iz052_01', 1)
    sprite('iz052_02', 1)
    sprite('iz052_01', 2)
    sprite('iz052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('iz052_02', 1)
    sprite('iz052_03', 1)
    sprite('iz052_02', 2)
    sprite('iz052_01', 2)
    sprite('iz052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('iz052_03', 1)
    sprite('iz052_04', 1)
    sprite('iz052_03', 2)
    sprite('iz052_02', 2)
    sprite('iz052_01', 2)
    sprite('iz052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('iz052_04', 1)
    sprite('iz052_04', 1)
    sprite('iz052_04', 2)
    sprite('iz052_03', 2)
    sprite('iz052_02', 2)
    sprite('iz052_01', 2)
    sprite('iz052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('iz054_00', 1)
    sprite('iz054_01', 1)
    sprite('iz054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('iz054_01', 1)
    sprite('iz054_02', 1)
    sprite('iz054_01', 2)
    sprite('iz054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('iz054_02', 1)
    sprite('iz054_03', 1)
    sprite('iz054_02', 2)
    sprite('iz054_01', 2)
    sprite('iz054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('iz054_03', 1)
    sprite('iz054_04', 1)
    sprite('iz054_03', 2)
    sprite('iz054_02', 2)
    sprite('iz054_01', 2)
    sprite('iz054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('iz054_04', 1)
    sprite('iz054_04', 1)
    sprite('iz054_04', 2)
    sprite('iz054_03', 2)
    sprite('iz054_02', 2)
    sprite('iz054_01', 2)
    sprite('iz054_00', 2)


@State
def CmnActBDownUpper():
    sprite('iz060_00', 4)
    label(0)
    sprite('iz060_01', 4)
    sprite('iz060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('iz060_03', 4)


@State
def CmnActBDownDown():
    sprite('iz060_04', 4)
    label(0)
    sprite('iz060_05', 4)
    sprite('iz060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('iz060_07', 2)
    sprite('iz060_08', 2)


@State
def CmnActBDownBound():
    sprite('iz060_09', 3)
    sprite('iz060_10', 3)
    sprite('iz060_11', 3)
    sprite('iz060_12', 3)
    sprite('iz060_13', 3)


@State
def CmnActBDownLoop():
    sprite('iz060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('iz061_00', 3)
    sprite('iz061_01', 3)
    sprite('iz061_02', 3)
    sprite('iz061_03', 3)
    sprite('iz061_04', 3)
    sprite('iz061_05', 3)
    sprite('iz061_06', 2)
    sprite('iz061_07', 2)
    sprite('iz061_08', 2)
    sprite('iz061_09', 2)
    sprite('iz061_10', 2)


@State
def CmnActFDownUpper():
    sprite('iz063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('iz063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('iz063_02', 3)
    sprite('iz063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('iz063_04', 3)
    sprite('iz063_05', 3)


@State
def CmnActFDownBound():
    sprite('iz063_06', 2)
    sprite('iz063_07', 2)
    sprite('iz063_08', 3)
    sprite('iz063_09', 3)
    sprite('iz063_10', 3)


@State
def CmnActFDownLoop():
    sprite('iz063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('iz064_00', 2)
    sprite('iz064_01', 2)
    sprite('iz064_02', 2)
    sprite('iz064_03', 2)
    sprite('iz064_04', 2)
    sprite('iz064_05', 2)
    sprite('iz064_06', 2)
    sprite('iz064_07', 2)
    sprite('iz064_08', 2)
    sprite('iz064_09', 2)


@State
def CmnActVDownUpper():
    sprite('iz062_00', 3)
    label(0)
    sprite('iz062_01', 3)
    sprite('iz062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('iz062_03', 3)
    sprite('iz062_04', 3)


@State
def CmnActVDownDown():
    sprite('iz062_05', 3)
    sprite('iz062_06', 3)
    label(0)
    sprite('iz062_07', 3)
    sprite('iz062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('iz062_09', 2)
    sprite('iz062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('iz062_09', 2)
    sprite('iz062_10', 2)


@State
def CmnActBlowoff():
    sprite('iz072_00', 3)
    sprite('iz072_01', 3)
    sprite('iz072_02', 3)
    label(0)
    sprite('iz072_01', 3)
    sprite('iz072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('iz074_00', 3)
    sprite('iz074_01', 3)
    sprite('iz074_02', 3)
    sprite('iz074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('iz082_00', 2)
    sprite('iz082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('iz071_04', 1)


@State
def CmnActWallBound():
    sprite('iz073_00', 3)
    sprite('iz073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('iz073_02', 3)
    label(0)
    sprite('iz073_03', 3)
    sprite('iz073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('iz070_00', 3)
    sprite('iz070_01', 3)
    sprite('iz070_02', 3)
    sprite('iz070_03', 3)
    sprite('iz070_02', 4)
    sprite('iz070_03', 4)
    label(0)
    sprite('iz070_02', 7)
    sprite('iz070_03', 7)
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('iz070_04', 2)
    sprite('iz070_05', 3)
    sprite('iz070_06', 4)
    sprite('iz070_07', 6)
    sprite('iz070_08', 5)
    sprite('iz070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('iz070_10', 2)
    sprite('iz070_11', 2)
    sprite('iz070_12', 2)
    sprite('iz070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('iz113_00', 3)
    sprite('iz113_01', 3)
    sprite('iz113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('iz113_00', 3)
    sprite('iz113_01', 3)
    sprite('iz113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('iz113_00', 3)
    sprite('iz113_01', 3)
    sprite('iz113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('iz110_00', 2)
    sprite('iz110_01', 2)
    sprite('iz110_02', 2)
    sprite('iz110_03', 2)
    sprite('iz110_04', 2)
    sprite('iz110_06', 2)
    sprite('iz110_07', 2)
    sprite('iz110_08', 200)
    sprite('iz110_09', 3)
    sprite('iz110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('iz111_00', 3)
    sprite('iz111_01', 3)
    sprite('iz111_02', 3)
    sprite('iz111_03', 3)
    sprite('iz111_04', 3)
    sprite('iz111_06', 3)
    sprite('iz111_07', 200)
    sprite('iz111_08', 3)
    sprite('iz111_09', 3)


@State
def CmnActUkemiLandN():
    sprite('iz112_00', 2)
    sprite('iz112_01', 2)
    sprite('iz112_02', 2)
    sprite('iz112_03', 2)
    sprite('iz112_04', 2)
    sprite('iz112_05', 2)
    sprite('iz112_06', 2)
    sprite('iz112_07', 2)
    sprite('iz112_08', 2)
    sprite('iz112_09', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('iz024_00', 3)
    sprite('iz024_01', 3)
    sprite('iz024_02', 3)
    sprite('iz024_03', 3)
    sprite('iz024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('iz040_00', 3)
    sprite('iz040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('iz040_02', 3)
    sprite('iz040_03', 3)
    sprite('iz040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('iz040_01', 3)
    sprite('iz040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('iz040_05', 3)
    label(0)
    sprite('iz040_02', 3)
    sprite('iz040_03', 3)
    sprite('iz040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('iz040_01', 3)
    sprite('iz040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('iz041_00', 3)
    sprite('iz041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('iz041_02', 3)
    sprite('iz041_03', 3)
    sprite('iz041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('iz041_01', 3)
    sprite('iz041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('iz041_05', 3)
    label(0)
    sprite('iz041_02', 3)
    sprite('iz041_03', 3)
    sprite('iz041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('iz041_01', 3)
    sprite('iz041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('iz043_00', 3)
    sprite('iz043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('iz043_02', 3)
    sprite('iz043_03', 3)
    sprite('iz043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('iz043_01', 3)
    sprite('iz043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('iz043_05', 3)
    label(0)
    sprite('iz043_02', 3)
    sprite('iz043_03', 3)
    sprite('iz043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('iz043_01', 3)
    sprite('iz043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('iz045_00', 3)
    sprite('iz045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('iz045_02', 3)
    sprite('iz045_03', 3)
    sprite('iz045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('iz045_01', 3)
    sprite('iz045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('iz045_05', 3)
    label(0)
    sprite('iz045_02', 3)
    sprite('iz045_03', 3)
    sprite('iz045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('iz045_01', 3)
    sprite('iz045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('iz090_00', 2)
    sprite('iz090_01', 2)
    sprite('iz090_02', 1)
    SetCommonActionMark(1)
    sprite('iz090_03', 6)
    sprite('iz090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('iz091_00', 2)
    sprite('iz091_01', 2)
    sprite('iz091_02', 1)
    SetCommonActionMark(1)
    sprite('iz091_03', 6)
    sprite('iz091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('iz092_00', 2)
    sprite('iz092_01', 2)
    sprite('iz092_02', 1)
    SetCommonActionMark(1)
    sprite('iz092_03', 6)
    sprite('iz092_04', 6)


@State
def CmnActAirTurn():
    sprite('iz025_00', 4)
    sprite('iz025_01', 4)
    sprite('iz025_02', 4)


@State
def CmnActLockWait():
    sprite('iz040_02', 1)
    sprite('iz040_01', 3)
    sprite('iz040_00', 3)


@State
def CmnActLockReject():
    sprite('iz312_00', 3)
    sprite('iz312_01', 3)
    sprite('iz312_02', 3)
    sprite('iz312_03', 3)
    sprite('iz312_04', 3)
    sprite('iz312_05', 3)
    sprite('iz312_06', 3)
    sprite('iz312_07', 3)


@State
def CmnActAirLockWait():
    sprite('iz045_02', 1)
    sprite('iz045_01', 3)
    sprite('iz045_00', 3)


@State
def CmnActAirLockReject():
    sprite('iz322_00', 3)
    sprite('iz322_01', 3)
    sprite('iz322_02', 8)
    sprite('iz322_03', 3)
    sprite('iz322_04', 3)
    sprite('iz322_05', 3)
    sprite('iz322_06', 3)
    sprite('iz322_07', 3)


@State
def CmnActLandSpin():
    sprite('iz071_00', 4)
    sprite('iz071_01', 4)
    label(0)
    sprite('iz071_02', 2)
    sprite('iz071_03', 2)
    sprite('iz071_04', 2)
    sprite('iz071_05', 2)
    sprite('iz071_06', 2)
    sprite('iz071_07', 2)
    sprite('iz071_08', 2)
    sprite('iz071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('iz071_10', 6)
    sprite('iz071_11', 5)
    sprite('iz071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('iz071_02', 2)
    sprite('iz071_03', 2)
    sprite('iz071_04', 2)
    sprite('iz071_05', 2)
    sprite('iz071_06', 2)
    sprite('iz071_07', 2)
    sprite('iz071_08', 2)
    sprite('iz071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('iz077_00', 2)
    sprite('iz077_01', 2)
    sprite('iz077_00ex01', 2)
    sprite('iz077_01ex01', 2)
    sprite('iz077_00ex02', 2)
    sprite('iz077_01ex02', 2)
    sprite('iz077_00ex03', 2)
    sprite('iz077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('iz077_02', 4)
    label(0)
    sprite('iz077_03', 3)
    sprite('iz077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('iz077_05', 5)
    sprite('iz077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('iz060_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('iz060_11', 4)
    sprite('iz060_13', 5)


@State
def CmnActBurstBegin():
    sprite('iz331_00', 2)
    sprite('iz331_01', 2)
    label(0)
    sprite('iz331_02', 3)
    sprite('iz331_03', 3)
    sprite('iz331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('iz331_05', 2)
    label(0)
    sprite('iz331_06', 3)
    sprite('iz331_07', 3)
    sprite('iz331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('iz331_09', 3)
    sprite('iz331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('iz331_11', 2)
    sprite('iz331_12', 2)
    label(0)
    sprite('iz331_02', 3)
    sprite('iz331_03', 3)
    sprite('iz331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('iz331_05', 2)
    label(0)
    sprite('iz331_06', 3)
    sprite('iz331_07', 3)
    sprite('iz331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('iz331_13', 3)
    sprite('iz331_14', 3)
    label(0)
    sprite('iz020_07', 4)
    sprite('iz020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():

    def upon_IMMEDIATE():
        SLOT_61 = 0
    sprite('iz333_00', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_armchange', 0)
    sprite('iz333_01', 3)
    sprite('iz333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('iz333_03', 32767)
    CreateObject('EMB_IZ_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('iz333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('iz333_05', 3)
    CreateObject('OverDriveAura', 0)
    CreateObject('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)
    sprite('iz333_07', 3)
    sprite('iz333_05', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('iz333_08', 3)
    CreateParticle('izef_armchange', 0)
    sprite('iz333_09', 3)
    sprite('iz333_10', 3)
    sprite('iz333_11', 3)


@State
def CmnActAirOverDriveBegin():

    def upon_IMMEDIATE():
        SLOT_61 = 0
    sprite('iz333_12', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_armchange', 0)
    sprite('iz333_13', 3)
    sprite('iz333_14', 3)
    CharacterFlash(16639, 20, 1)
    sprite('iz333_15', 32767)
    CreateObject('EMB_IZ_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('iz333_16', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('iz333_05', 3)
    CreateObject('OverDriveAura', 0)
    CreateObject('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)
    sprite('iz333_07', 3)
    sprite('iz333_05', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('iz333_08', 3)
    CreateParticle('izef_armchange', 0)
    sprite('iz333_09', 3)
    sprite('iz333_17', 3)
    sprite('iz333_18', 3)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
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
        HitOrBlockCancel('Kakusei_NmlAtk5C')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('iz200_00', 1)
    PerInertia(60)
    sprite('iz200_01', 1)
    sprite('iz200_01', 1)
    RandomCommonVoiceline(0)
    CommonSE('008_swing_pole_0')
    HitOrBlockJumpCancel(1)
    sprite('iz200_02', 2)
    RandomCommonVoiceline(0)
    sprite('iz200_03', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz200_04', 3)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('iz200_02', 2)
    sprite('iz200_01', 2)
    sprite('iz200_00', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(640)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Kakusei_NmlAtk5C')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        StayAfterMovement(1, 0)
    sprite('iz201_00', 2)
    sprite('iz201_01', 2)
    sprite('iz201_02', 2)
    PrivateSE('izse_01')
    sprite('iz201_03', 2)
    sprite('iz201_04', 1)
    CommonSE('004_swing_grap_1_1')
    RandomCommonVoiceline(1)
    sprite('iz201_05', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz201_06', 3)
    sprite('iz201_07', 2)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('iz201_08', 3)
    sprite('iz201_09', 3)
    sprite('iz201_10', 3)
    sprite('iz201_11', 3)
    sprite('iz201_12', 4)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(850)
        UseSlashHitspark(1)
        PushbackX(30400)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitJumpCancel(1)
    sprite('iz202_00', 3)
    sprite('iz202_01', 3)
    RandomCommonVoiceline(2)
    physicsXImpulse(15000)
    sprite('iz202_02', 3)
    PrivateSE('izse_01')
    XImpulseAcceleration(50)
    sprite('iz202_03', 2)
    CreateObject('5CZanzo', 0)
    CommonSE('008_swing_pole_2')
    XImpulseAcceleration(25)
    sprite('iz202_04', 3)
    callSubroutine('CheckShieidBitAvailable')
    XImpulseAcceleration(0)
    sprite('iz202_05', 3)
    sprite('iz202_06', 2)
    Recovery()
    Unknown2063()
    sprite('iz202_07', 3)
    sprite('iz202_08', 3)
    sprite('iz202_09', 3)
    sprite('iz202_10', 3)
    sprite('iz202_11', 3)
    sprite('iz202_12', 3)


@State
def Kakusei_NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(850)
        AirUntechableTime(19)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('iz203_00', 2)
    sprite('iz203_01', 1)
    RandomCommonVoiceline(2)
    sprite('iz203_01', 2)
    PrivateSE('izse_01')
    sprite('iz203_02', 3)
    sprite('iz203_03', 3)
    CommonSE('008_swing_pole_2')
    CreateObject('Kaku5CZanzo', -1)
    callSubroutine('CheckShieidBitAvailable')
    CreateObject('5CKakuseiAura', 0)
    CreateObject('5CKakuseiAura_oku', 1)
    sprite('iz203_03', 2)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('iz203_04', 1)
    sprite('iz203_05', 2)
    sprite('iz203_05ex00', 3)
    sprite('iz203_06', 3)
    sprite('iz203_07', 2)
    sprite('iz203_08', 2)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('iz204_00', 2)
    EndMomentum(1)
    sprite('iz204_01', 1)
    sprite('iz204_02', 3)
    CreateObject('KakuseiMagicCircle', -1)
    CreateObject('Install', -1)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle_front', -1)
    ParticleLayer(5)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle', -1)
    CreateObject('KakuseiAura', 0)
    CreateObject('KakuseiAura_oku', 1)
    CreateObject('5DLightsaber_on', -1)
    CharacterFlash(8421504, 6, 1)
    CommonSE('022_magiccircle_b')
    sprite('iz204_03', 3)
    SLOT_4 = 1
    sprite('iz204_04', 3)
    StopCharacterFlash2()
    sprite('iz204_02ex00', 3)
    CharacterFlash(0, 6, 1)
    sprite('iz204_03ex00', 3)
    sprite('iz204_04', 3)
    sprite('iz204_05', 2)
    sprite('iz204_06', 1)


@State
def Kakusei_NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('iz204_00', 3)
    EndMomentum(1)
    sprite('iz204_01', 3)
    CommonSE('022_magiccircle_a')
    sprite('iz204_02', 4)
    CreateObject('5DLightsaber_off', -1)
    sprite('iz204_03', 4)
    SLOT_4 = 0
    sprite('iz204_04', 4)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    sprite('iz204_05', 3)
    sprite('iz204_06', 2)
    loopRest()


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        PreventBlocking(1)
    sprite('iz234_00', 2)
    sprite('iz234_01', 1)
    sprite('iz234_02', 3)
    CreateObject('KakuseiMagicCircle', -1)
    CreateObject('Install', -1)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle_front', -1)
    ParticleLayer(5)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle', -1)
    CreateObject('2DKakuseiAura', 0)
    CreateObject('2DKakuseiAura_oku', 1)
    CreateObject('2DLightsaber_on', -1)
    CharacterFlash(8421504, 6, 1)
    CommonSE('022_magiccircle_b')
    sprite('iz234_03', 3)
    SLOT_4 = 1
    sprite('iz234_04', 3)
    sprite('iz234_02ex00', 3)
    sprite('iz234_03', 3)
    sprite('iz234_04', 3)
    sprite('iz234_05', 2)
    sprite('iz234_06', 1)
    loopRest()


@State
def Kakusei_NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        PreventBlocking(1)
    sprite('iz234_00', 3)
    sprite('iz234_01', 3)
    CommonSE('022_magiccircle_a')
    sprite('iz234_02', 4)
    CreateObject('2DLightsaber_off', -1)
    sprite('iz234_03', 4)
    SLOT_4 = 0
    sprite('iz234_04', 4)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    sprite('iz234_05', 3)
    sprite('iz234_06', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
    sprite('iz254_00', 2)
    sprite('iz254_01', 1)
    sprite('iz254_02', 1)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('iz254_02', 2)
    CreateObject('KakuseiMagicCircle', 2)
    CreateObject('Install', 2)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle_front', 2)
    ParticleLayer(5)
    ParticleSize(800)
    CallCustomizableParticle('izef_drivecircle', 2)
    CreateObject('AirKakuseiAura_oku', 1)
    CreateObject('AirKakuseiAura', 0)
    CreateObject('AirLightsaber_on', -1)
    CharacterFlash(8421504, 6, 1)
    CommonSE('022_magiccircle_b')
    sprite('iz254_03', 3)
    SLOT_4 = 1
    AddAirDashCount(1)
    sprite('iz254_04', 3)
    sprite('iz254_02ex00', 3)
    sprite('iz254_03', 3)
    sprite('iz254_04', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(75)
    sprite('iz254_05', 2)
    sprite('iz254_06', 1)
    loopRest()


@State
def Kakusei_NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
    sprite('iz254_00', 3)
    sprite('iz254_01', 3)
    CommonSE('022_magiccircle_a')
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('iz254_02', 4)
    CreateObject('AirLightsaber_off', -1)
    sprite('iz254_03', 4)
    SLOT_4 = 0
    AddAirDashCount(-1)
    sprite('iz254_04', 4)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    sprite('iz254_05', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    XImpulseAcceleration(75)
    sprite('iz254_06', 3)
    loopRest()


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        PushbackX(12000)
        HitAirUnblockable(0)
        HitLow(2)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Kakusei_NmlAtk5C')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('iz230_00', 2)
    PerInertia(60)
    sprite('iz230_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('iz230_02', 2)
    sprite('iz230_03', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz230_04', 3)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('iz230_05', 3)
    sprite('iz230_06', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(550)
        HitLow(2)
        AttackP1(90)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Kakusei_NmlAtk5C')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
    sprite('iz231_00', 2)
    sprite('iz231_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_1')
    sprite('iz231_02', 2)
    sprite('iz231_03', 2)
    sprite('iz231_04', 2)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz231_05', 3)
    Recovery()
    Unknown2063()
    sprite('iz231_06', 3)
    sprite('iz231_07', 3)
    sprite('iz231_08', 3)
    sprite('iz231_09', 3)
    sprite('iz231_10', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(830)
        CHGroundedHitstunAnimation(2)
        Stagger(25)
        FatalCounter(1)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('iz232_00', 3)
    sprite('iz232_01', 3)
    sprite('iz232_02', 3)
    RandomCommonVoiceline(1)
    PrivateSE('izse_01')
    sprite('iz232_03', 2)
    CommonSE('008_swing_pole_2')
    sprite('iz232_04', 3)
    CreateObject('2CZanzo', -1)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz232_05', 3)
    sprite('iz232_06', 3)
    Recovery()
    Unknown2063()
    sprite('iz232_07', 3)
    sprite('iz232_08', 3)
    sprite('iz232_09', 3)
    sprite('iz232_10', 3)


@State
def Kakusei_NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(750)
        AttackP1(100)
        UseSlashHitspark(1)
        PushbackX(5000)
        AirPushbackX(4000)
        AirPushbackY(13000)
        AirUntechableTime(26)
        StayAfterMovement(1, 0)
        FatalCounter(1)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('Kakusei_NmlAtk6C')
        HitOrBlockCancel('Kakusei_NmlAtk3C')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        HitJumpCancel(1)
    sprite('iz233_00', 3)
    sprite('iz233_01', 3)
    sprite('iz233_02', 1)
    sprite('iz233_02', 5)
    CreateObject('2CKakuseiAura', 0)
    PrivateSE('izse_01')
    sprite('iz233_03', 3)
    CommonSE('008_swing_pole_2')
    sprite('iz233_04', 2)
    CreateObject('Kaku2CZanzo00', -1)
    RandomCommonVoiceline(2)
    sprite('iz233_05', 3)
    physicsXImpulse(0)
    sprite('iz233_06', 2)
    sprite('iz233_07', 3)
    PrivateSE('izse_01')
    sprite('iz233_08', 1)
    sprite('iz233_09', 3)
    RefreshMultihit()
    PushbackX(-24000)
    AirPushbackX(-4000)
    AirPushbackY(20000)
    CreateObject('Kaku2CZanzo01', -1)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz233_10', 2)
    Recovery()
    Unknown2063()
    sprite('iz233_11', 2)
    sprite('iz233_12', 2)
    sprite('iz233_13', 3)
    sprite('iz233_14', 2)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        AttackP2(89)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(16000)
        AirUntechableTime(40)
        CHHardKnockdown(1)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        StayAfterMovement(1, 0)
    sprite('iz235_00', 2)
    sprite('iz235_01', 3)
    SmartVoiceline('iz107')
    sprite('iz235_02', 2)
    PrivateSE('izse_01')
    sprite('iz235_03', 2)
    physicsXImpulse(20000)
    sprite('iz235_04', 2)
    XImpulseAcceleration(75)
    CreateObject('3CZanzo00', -1)
    CommonSE('008_swing_pole_2')
    sprite('iz235_05', 3)
    XImpulseAcceleration(50)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz235_06', 3)
    XImpulseAcceleration(50)
    Recovery()
    Unknown2063()
    sprite('iz235_07', 3)
    XImpulseAcceleration(50)
    sprite('iz235_08', 3)
    XImpulseAcceleration(50)
    sprite('iz235_09', 3)
    XImpulseAcceleration(50)
    sprite('iz235_10', 3)
    XImpulseAcceleration(50)
    CommonSE('019_cloth_a')
    sprite('iz235_11', 3)
    XImpulseAcceleration(50)
    sprite('iz235_12', 3)
    XImpulseAcceleration(0)


@State
def Kakusei_NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(13000)
        AirUntechableTime(40)
        CHHardKnockdown(10)
        FatalCounter(1)
        StayAfterMovement(1, 0)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
    sprite('iz236_00', 4)
    SmartVoiceline('iz106')
    sprite('iz236_01', 4)
    sprite('iz236_02', 4)
    CommonSE('001_airbackdash_0')
    sprite('iz236_03', 3)
    XSpeed(40000)
    CreateObject('Kakusei3CAura', 0)
    sprite('iz236_04', 2)
    CreateObject('Kakusei3CAuraFire', 0)
    CreateParticle('izef_Drivelight_side', 0)
    CommonSE('004_swing_grap_1_2')
    sprite('iz236_05', 2)
    sprite('iz236_04', 2)
    CreateParticle('izef_Drivelight_side', 0)
    XImpulseAcceleration(90)
    sprite('iz236_06', 3)
    callSubroutine('CheckShieidBitAvailable')
    Recovery()
    Unknown2063()
    TriggerUponForState('Kakusei3CAura', 32)
    TriggerUponForState('Kakusei3CAuraFire', 32)
    XImpulseAcceleration(60)
    sprite('iz236_07', 3)
    XImpulseAcceleration(40)
    sprite('iz236_08', 3)
    XImpulseAcceleration(20)
    sprite('iz236_09', 3)
    sprite('iz236_10', 3)
    sprite('iz236_11', 2)
    sprite('iz236_12', 2)
    sprite('iz236_13', 2)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockCancel('Kakusei_NmlAtkAIR5C')
        HitOrBlockCancel('Kakusei_NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('iz250_00', 2)
    sprite('iz250_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('iz250_02', 1)
    sprite('iz250_03', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz250_04', 3)
    Recovery()
    Unknown2063()
    sprite('iz250_02', 3)
    sprite('iz250_01', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('Kakusei_NmlAtkAIR5C')
        HitOrBlockCancel('Kakusei_NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('iz255_00', 3)
    sprite('iz255_01', 2)
    sprite('iz255_02', 2)
    RandomCommonVoiceline(1)
    sprite('iz255_03', 2)
    CommonSE('003_swing_grap_0_1')
    sprite('iz255_04', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz255_05', 3)
    sprite('iz255_05', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('iz255_06', 6)
    sprite('iz255_07', 6)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AirUntechableTime(40)
        UseSlashHitspark(1)
        AirPushbackX(9800)
        AirPushbackY(-45000)
        HitOrBlockCancel('NmlAtkAIR5D')
    sprite('iz252_00', 3)
    sprite('iz252_01', 3)
    sprite('iz252_02', 2)
    PrivateSE('izse_01')
    CommonSE('008_swing_pole_2')
    RandomCommonVoiceline(2)
    sprite('iz252_03', 3)
    CreateObject('AIR5CZanzo', 0)
    sprite('iz252_04', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz252_05', 3)
    CommonSE('019_cloth_a')
    sprite('iz252_06', 3)
    Recovery()
    Unknown2063()
    sprite('iz252_07', 3)
    sprite('iz252_08', 3)
    sprite('iz252_09', 3)
    sprite('iz252_10', 3)
    sprite('iz252_11', 3)


@State
def Kakusei_NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        UseSlashHitspark(1)
        AirUntechableTime(20)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('iz253_00', 1)
    sprite('iz253_01', 2)
    sprite('iz253_02', 2)
    sprite('iz253_03', 2)
    PrivateSE('izse_08')
    CommonSE('008_swing_pole_2')
    RandomCommonVoiceline(2)
    sprite('iz253_04', 2)
    sprite('iz253_05', 2)
    CommonSE('019_cloth_a')
    sprite('iz253_06', 5)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz253_07', 3)
    Recovery()
    Unknown2063()
    CreateParticle('izef_fire', 0)
    CreateParticle('izef_fire', 1)
    CreateParticle('izef_fire_dust', 2)
    CreateParticle('izef_fire_dust', 3)
    sprite('iz253_08', 3)
    sprite('iz253_09', 3)
    sprite('iz253_10', 3)
    sprite('iz253_11', 3)
    sprite('iz253_12', 3)
    sprite('iz253_13', 3)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AirUntechableTime(26)
        GroundedHitstunAnimation(3)
        AirPushbackX(24000)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('Kakusei_NmlAtk5C')
        HitOrBlockCancel('Kakusei_NmlAtk2C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('Kakusei_NmlAtk5D')
        HitOrBlockCancel('Kakusei_NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('iz210_00', 2)
    sprite('iz210_01', 1)
    RandomCommonVoiceline(2)
    sprite('iz210_01', 2)
    sprite('iz210_02', 3)
    sprite('iz210_03', 3)
    CommonSE('006_swing_blade_1')
    sprite('iz210_04', 1)
    CreateObject('6AZanzo', -1)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz210_04', 2)
    sprite('iz210_05', 3)
    Recovery()
    Unknown2063()
    sprite('iz210_06', 3)
    sprite('iz210_07', 3)
    sprite('iz210_08', 3)
    sprite('iz210_09', 3)
    sprite('iz210_10', 3)
    sprite('iz210_11', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        BonusProration(110)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(9)
        AirPushbackX(8000)
        AirPushbackY(-30000)
        CHGroundBounce(1)
        CHBouncePercentage(70)
        CHAirUntechableTime(36)
        HardKnockdown(1)
        UseSlashHitspark(1)
        SpecialCancel(1)
        StarterRating(2)
        HitAirUnblockable(0)
        SetActionMark(1)

        def upon_EVERY_FRAME():
            if not CheckInput(INPUT_HOLD_B):
                SetActionMark(0)
    sprite('iz211_00', 3)
    sprite('iz211_01', 4)
    Voiceline('iz109')
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    sprite('iz211_02', 3)
    CommonSE('004_swing_grap_1_1')
    physicsXImpulse(8500)
    physicsYImpulse(17000)
    setGravity(1800)
    sprite('iz211_03', 3)
    sprite('iz211_04', 2)
    sprite('iz211_05', 2)
    sprite('iz211_06', 2)
    sprite('iz211_07', 2)
    if SLOT_2:
        conditionalSendToLabel(1)
    sprite('iz211_08', 2)
    CommonSE('006_swing_blade_2')
    sprite('iz211_09', 3)
    setInvincible(0)
    CreateObject('6BZanzo', -1)
    sprite('iz211_10', 32767)
    callSubroutine('CheckShieidBitAvailable')
    Recovery()
    uponSendToLabel(LANDING, 0)
    label(0)
    sprite('iz211_11', 3)
    XImpulseAcceleration(25)
    SFX_FOOTSTEP_(100, 1, 1)
    SpecialCancel(0)
    sprite('iz211_12', 3)
    XImpulseAcceleration(0)
    sprite('iz211_13', 3)
    sprite('iz211_14', 2)
    sprite('iz211_15', 2)
    sprite('iz211_16', 2)
    ExitState()
    label(1)
    sprite('keep', 1)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz211_17', 3)
    PerGravity(200)
    sprite('iz211_18', 32767)
    uponSendToLabel(LANDING, 2)
    label(2)
    sprite('iz211_19', 2)
    XImpulseAcceleration(25)
    setInvincible(0)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz211_20', 2)
    physicsXImpulse(0)
    sprite('iz211_21', 1)
    sprite('iz211_22', 1)
    sprite('iz211_23', 1)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        PushbackX(8000)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        FatalCounter(1)
    sprite('iz212_00', 3)
    sprite('iz212_01', 2)
    setInvincible(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    SmartVoiceline('iz108')
    sprite('iz212_02', 3)
    physicsXImpulse(-4000)
    sprite('iz212_03', 2)
    sprite('iz212_04', 3)
    setInvincible(0)
    physicsXImpulse(26000)
    sprite('iz212_05', 3)
    sprite('iz212_06', 2)
    CommonSE('006_swing_blade_2')
    CreateObject('6CZanzo', -1)
    sprite('iz212_07', 3)
    physicsXImpulse(0)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz212_08', 3)
    Recovery()
    Unknown2063()
    sprite('iz212_09', 3)
    sprite('iz212_10', 3)
    sprite('iz212_11', 3)
    sprite('iz212_12', 3)
    sprite('iz212_13', 3)
    sprite('iz212_14', 3)
    sprite('iz212_15', 3)
    sprite('iz212_16', 3)
    sprite('iz212_17', 3)


@State
def Kakusei_NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(900)
        AttackP2(82)
        UseSlashHitspark(1)
        AirPushbackX(3000)
        AirPushbackY(37000)
        CHAirPushbackY(42000)
        GroundedHitstunAnimation(10)
        PushbackX(30000)
        AirUntechableTime(26)
        CHAirUntechableTime(50)
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        HitJumpCancel(1)
        FatalCounter(1)
    sprite('iz213_00', 2)
    sprite('iz213_01', 2)
    sprite('iz213_02', 2)
    CommonSE('001_airbackdash_0')
    physicsXImpulse(70000)
    sprite('iz213_03', 3)
    XImpulseAcceleration(50)
    PrivateSE('izse_08')
    sprite('iz213_04', 3)
    XImpulseAcceleration(50)
    SmartVoiceline('iz108')
    sprite('iz213_05', 3)
    XImpulseAcceleration(50)
    sprite('iz213_06', 2)
    physicsXImpulse(0)
    sprite('iz213_07', 2)
    CommonSE('008_swing_pole_2')
    sprite('iz213_08', 3)
    sprite('iz213_09', 3)
    callSubroutine('CheckShieidBitAvailable')
    CreateParticle('izef_fire', 0)
    CreateParticle('izef_fire_dust', 1)
    CreateParticle('izef_fire_dust', 2)
    CreateParticle('izef_fire_dust', 3)
    Recovery()
    Unknown2063()
    sprite('iz213_10', 2)
    sprite('iz213_11', 2)
    sprite('iz213_12', 2)
    sprite('iz213_13', 2)
    sprite('iz213_14', 2)
    sprite('iz213_15', 2)
    sprite('iz213_16', 1)
    sprite('iz213_17', 1)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(100)
        UseSlashHitspark(1)
        SpecialCancel(0)
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('iz300_00', 2)
    sprite('iz300_01', 2)
    sprite('iz300_02', 2)
    if random_(2, 0, 50):
        Voiceline('iz404')
    else:
        Voiceline('iz405')
    sprite('iz300_03', 6)
    PrivateSE('izse_01')
    sprite('iz300_04', 3)
    sprite('iz300_05', 3)
    sprite('iz300_06', 3)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz300_07', 3)
    sprite('iz300_08', 3)
    sprite('iz300_09', 3)
    sprite('iz300_10', 3)
    sprite('iz300_11', 3)
    sprite('iz300_12', 3)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        AirPushbackY(45000)
    sprite('iz213_00', 2)
    sprite('iz213_01', 2)
    CommonSE('001_airbackdash_0')
    physicsXImpulse(30000)
    sprite('iz213_04', 2)
    PrivateSE('izse_08')
    sprite('iz213_05', 3)
    sprite('iz213_06', 3)
    physicsXImpulse(0)
    sprite('iz213_07', 3)
    CommonSE('008_swing_pole_2')
    sprite('iz213_08', 4)
    callSubroutine('CheckShieidBitAvailable')
    sprite('iz213_09', 3)
    CreateParticle('izef_fire', 0)
    CreateParticle('izef_fire_dust', 1)
    CreateParticle('izef_fire_dust', 2)
    CreateParticle('izef_fire_dust', 3)
    sprite('iz213_10', 3)
    sprite('iz213_11', 3)
    sprite('iz213_12', 3)
    sprite('iz213_13', 3)
    sprite('iz213_14', 3)
    sprite('iz213_15', 3)
    sprite('iz213_16', 3)
    sprite('iz213_17', 3)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(17)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(60)
        HardKnockdown(1)
        GroundBounce(1)
        BouncePercentage(30)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        UseSlashHitspark(1)
        StarterRating(2)
        callSubroutine('MyStatusSave')

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
    sprite('iz210_00', 3)
    sprite('iz210_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    Voiceline('iz159')
    HeatChange(-2500)
    sprite('iz210_01', 4)
    CharacterFlash(16763080, 8, 2)
    sprite('iz412_02', 3)
    label(100)
    sprite('iz412_00', 3)
    sprite('iz412_01', 3)
    sprite('iz412_02', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('iz412_01', 3)
    sprite('iz210_02', 3)
    sprite('iz210_03', 2)
    PrivateSE('izse_01')
    sprite('iz412_03', 1)
    CommonSE('004_swing_grap_1_1')
    CreateObject('GuardCrushZanzo', -1)
    sprite('iz412_03', 2)
    StartMultihit()
    EnableAfterimage(0)
    sprite('iz412_04', 4)
    sprite('iz412_05', 4)
    sprite('iz412_06', 4)
    sprite('iz412_07', 4)
    sprite('iz412_08', 3)
    sprite('iz412_09', 2)
    sprite('iz412_10', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('iz310_00', 3)
    sprite('iz310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('iz310_02', 3)
    sprite('iz310_03', 4)
    sprite('iz310_04', 7)
    SmartVoiceline('iz155')
    sprite('iz310_05', 4)
    sprite('iz310_06', 4)
    sprite('iz310_07', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        Hitstop(0)
        EnemyHitstopAddition(0, 12, 12)
        AirHitstunAnimation(7)
        GroundedHitstunAnimation(7)
        GuardCrushHitstun(40)
        UseSlashHitspark(1)
        Hitstun(200)
        PushbackX(0)
        AttackP2(100)
        SpecialCancel(0)
        StarterRating(2)
        StayAfterMovement(1, 0)
    sprite('iz310_02ex00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    CreateObject('ThrowLock_MagicCircle', 1)
    CreateObject('ThrowFunnel', -1)
    StartMultihit()
    ThrowLock(1)
    sprite('iz311_00', 4)
    SmartVoiceline('iz153')
    sprite('iz311_01', 4)
    physicsXImpulse(-30000)
    sprite('iz311_02', 4)
    XImpulseAcceleration(40)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz311_03', 6)
    XImpulseAcceleration(25)
    sprite('iz311_04', 6)
    XImpulseAcceleration(0)
    sprite('iz311_05', 3)
    TriggerUponForState('ThrowFunnel', 33)
    EnableCollision(1)
    XSpeed(48000)
    SetXCollisionFromOrigin(250)
    sprite('iz311_06', 1)
    RefreshMultihit()
    physicsXImpulse(0)
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    Hitstop(0)
    EnemyHitstopAddition(0, 10, 0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Wallbounce(1)
    WallbounceReboundTime(10)
    Floorslide(30)
    UseSlashHitspark(1)
    AirPushbackX(50000)
    AirPushbackY(8000)
    YImpulseBeforeWallbounce(800)
    AirUntechableTime(60)
    AttackP1(100)
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    TriggerUponForState('ThrowLock_MagicCircle', 32)
    sprite('iz311_06', 13)
    SpecialCancel(1)
    sprite('iz311_07', 4)
    sprite('iz311_08', 4)
    sprite('iz311_09', 4)
    sprite('iz311_10', 4)
    sprite('iz311_11', 4)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('iz310_00', 3)
    sprite('iz310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('iz310_02', 3)
    sprite('iz310_03', 4)
    sprite('iz310_04', 7)
    SmartVoiceline('iz155')
    sprite('iz310_05', 4)
    sprite('iz310_06', 4)
    sprite('iz310_07', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        Hitstop(0)
        EnemyHitstopAddition(0, 12, 12)
        AirHitstunAnimation(7)
        GroundedHitstunAnimation(7)
        GuardCrushHitstun(40)
        UseSlashHitspark(1)
        Hitstun(200)
        AttackP2(100)
        AirPushbackX(-32000)
        AirPushbackY(0)
        PushbackX(-32000)
        Hitstop(0)
        AirUntechableTime(48)
        AttackP2(100)
        StarterRating(2)
        SpecialCancel(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        StayAfterMovement(1, 0)
    sprite('iz310_02ex00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    StartMultihit()
    CreateObject('ThrowLock_MagicCircle', 1)
    CreateObject('ThrowFunnel', -1)
    ThrowLock(1)
    sprite('iz311_00', 4)
    SmartVoiceline('iz153')
    sprite('iz311_01', 4)
    sprite('iz311_02', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz313_00', 3)
    sprite('iz313_01', 4)
    physicsXImpulse(60000)
    sprite('iz313_02', 4)
    AddX(100000)
    XImpulseAcceleration(40)
    CreateParticle('ef_hitmd', 0)
    sprite('iz313_03', 4)
    XImpulseAcceleration(30)
    sprite('iz313_04', 3)
    XImpulseAcceleration(20)
    sprite('iz311_04', 6)
    XImpulseAcceleration(0)
    ForceFaceSprite()
    sprite('iz311_05', 3)
    TriggerUponForState('ThrowFunnel', 33)
    EnableCollision(1)
    ForceFaceSprite()
    XSpeed(48000)
    SetXCollisionFromOrigin(250)
    sprite('iz311_06', 1)
    RefreshMultihit()
    physicsXImpulse(0)
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    Hitstop(0)
    EnemyHitstopAddition(0, 10, 0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Wallbounce(1)
    WallbounceReboundTime(10)
    Floorslide(30)
    UseSlashHitspark(1)
    AirPushbackX(50000)
    AirPushbackY(8000)
    YImpulseBeforeWallbounce(800)
    AirUntechableTime(60)
    AttackP1(100)
    TriggerUponForState('ThrowLock_MagicCircle', 32)
    sprite('iz311_06', 13)
    SpecialCancel(1)
    sprite('iz311_07', 4)
    sprite('iz311_08', 4)
    sprite('iz311_09', 4)
    sprite('iz311_10', 4)
    sprite('iz311_11', 4)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('iz320_00', 3)
    sprite('iz320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('iz320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('iz320_03', 4)
    sprite('iz320_04', 4)
    sprite('iz320_05', 7)
    SmartVoiceline('iz155')
    sprite('iz320_06', 4)
    sprite('iz320_07', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SpecialCancel(0)
        AttackLevel_(2)
        Damage(0)
        AirPushbackX(0)
        AirPushbackY(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(200)
        AttackP2(100)
        Hitstop(0)
        EnableRapidCancel(0)
        UseSlashHitspark(1)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        SetZLine(0, 50)
        ForcedLandingRecovery(0, 0)
    sprite('iz320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    CreateObject('AirThrowLock_MagicCircle', 0)
    StartMultihit()
    sprite('iz321_00', 3)
    YImpulseBeforeWallbounce(0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('iz321_01', 1)
    physicsXImpulse(-6000)
    physicsYImpulse(24000)
    setGravity(1000)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    Voiceline('iz154')
    CommonSE('004_swing_grap_1_1')
    sprite('iz321_01', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('iz321_02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('iz321_03', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('iz321_04', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('iz321_05', 3)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_06', 3)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_07', 3)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_08', 3)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_09', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_10', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    label(0)
    sprite('iz321_11', 3)
    RefreshMultihit()
    AttackDefaults_Throw('AirThrowExe2', 1, 1, 0)
    RangeCheck(220000)
    DistanceCheck(-1, -1, 280000, -180000)
    ThrowTechWindow(-1)
    TriggerUponForState('AirThrowLock_MagicCircle', 32)
    CreateObject('AirThrowAura1', 1)
    CreateObject('AirThrowAuraFire', 2)
    physicsXImpulse(32000)
    physicsYImpulse(-42000)
    setGravity(2500)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_12', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_13', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    loopRest()
    gotoLabel(0)


@State
def AirThrowExe2():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SpecialCancel(0)
        AttackLevel_(4)
        Damage(0)
        AirPushbackX(0)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        UseSlashHitspark(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(200)
        AttackP2(50)
        Hitstop(0)
        EnableRapidCancel(0)
        AttackOff()
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        StarterRating(2)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        SetZLine(0, 50)
    sprite('iz321_11', 3)
    RangeCheck(220000)
    DistanceCheck(-1, -1, 280000, -180000)
    ThrowTechWindow(-1)
    CreateObject('AirThrowAura2', 1)
    CreateObject('AirThrowAuraFire', 2)
    physicsXImpulse(32000)
    physicsYImpulse(-42000)
    setGravity(2500)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    label(0)
    sprite('iz321_12', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_13', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('iz321_11', 3)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz321_14', 1)
    OppThrowAnimation(13, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    ScreenShake(0, 30000)
    TriggerUponForState('AirThrowAura2', 32)
    TriggerUponForState('AirThrowAuraFire', 32)
    sprite('iz321_15', 2)
    RefreshMultihit()
    Damage(1500)
    EnableRapidCancel(1)
    sprite('iz321_16', 3)
    physicsXImpulse(-5000)
    physicsYImpulse(18000)
    setGravity(1200)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('iz321_17', 3)
    sprite('iz321_18', 3)
    sprite('iz321_19', 3)
    sprite('iz321_20', 3)
    sprite('iz321_21', 3)
    sprite('iz020_04', 3)
    sprite('iz020_05', 3)
    sprite('iz020_06', 3)
    label(110)
    sprite('iz020_07', 3)
    sprite('iz020_08', 3)
    loopRest()
    gotoLabel(110)


@State
def SpDashF_Land():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()

        def upon_EVERY_FRAME():
            if SLOT_XVelocity > 29200:
                SLOT_XVelocity = 29200
            if SLOT_2:
                WhiffNormalCancel(1)
                WhiffSpecialCancel(1)
                if not CheckInput(0x79):
                    sendToLabel(1)
                if CheckInput(0x9f):
                    if not SLOT_YVelocity >= 20000:
                        YSpeed(500)
                if CheckInput(0x51):
                    YSpeed(-500)

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(60)
                YAccel(50)
                EndYPhysicsImpulse()
        EndMomentum(1)
        ForcedLandingRecovery(5, 1)
    sprite('iz350_00', 2)
    sprite('iz350_01', 2)
    PrivateSE('izse_02')
    sprite('iz350_02', 2)
    CreateObject('HoverDashAura', 0)
    CreateParticle('izef_Drivelight', 1)
    physicsXImpulse(24000)
    physicsYImpulse(10000)
    SetAcceleration(800)
    sprite('iz350_03', 2)
    sprite('iz350_04', 1)
    sprite('iz350_04', 1)
    SetActionMark(1)
    sprite('iz350_05', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_02', 2)
    sprite('iz350_03', 2)
    sprite('iz350_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_05', 2)
    sprite('iz350_02', 2)
    sprite('iz350_03', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_04', 2)
    sprite('iz350_05', 2)
    sprite('iz350_02', 2)
    label(1)
    sprite('iz350_06', 4)
    clearUponHandler(EVERY_FRAME)
    SetAcceleration(0)
    TriggerUponForState('HoverDashAura', 32)
    CreateParticle('izef_Drivelight', 0)


@State
def SpDashF_Air():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()

        def upon_EVERY_FRAME():
            if SLOT_XVelocity > 29200:
                SLOT_XVelocity = 29200
            if SLOT_2:
                WhiffNormalCancel(1)
                WhiffSpecialCancel(1)
                WhiffFAirDashCancel(1)
                WhiffBAirDashCancel(1)
                if not CheckInput(0x79):
                    sendToLabel(1)
                if CheckInput(0x9f):
                    if not SLOT_YVelocity >= 3000:
                        YSpeed(500)
                if CheckInput(0x51):
                    YSpeed(-500)

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(60)
                YAccel(50)
                EndYPhysicsImpulse()
        SLOT_62 = 1
        EndMomentum(1)
        ForcedLandingRecovery(5, 1)
    sprite('iz350_06', 2)
    sprite('iz350_02', 2)
    PrivateSE('izse_02')
    CreateObject('HoverDashAura', 0)
    CreateParticle('izef_Drivelight', 1)
    physicsXImpulse(18000)
    physicsYImpulse(-6000)
    SetAcceleration(800)
    sprite('iz350_03', 2)
    sprite('iz350_04', 2)
    sprite('iz350_05', 1)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_05', 1)
    SetActionMark(1)
    sprite('iz350_02', 2)
    sprite('iz350_03', 2)
    sprite('iz350_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_05', 2)
    sprite('iz350_02', 2)
    sprite('iz350_03', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_04', 2)
    sprite('iz350_05', 2)
    sprite('iz350_02', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz350_03', 2)
    sprite('iz350_04', 2)
    sprite('iz350_05', 2)
    label(1)
    sprite('iz350_06', 4)
    clearUponHandler(EVERY_FRAME)
    SetAcceleration(0)
    TriggerUponForState('HoverDashAura', 32)
    CreateParticle('izef_Drivelight', 0)


@State
def SpDashB_Land():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()

        def upon_EVERY_FRAME():
            if SLOT_2:
                WhiffNormalCancel(1)
                WhiffSpecialCancel(1)
                if not CheckInput(0x5f):
                    sendToLabel(1)

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(30)
                YAccel(50)
                EndYPhysicsImpulse()
        InvincibilityDuration(5)
        EndMomentum(1)
        ForcedLandingRecovery(3, 1)
    sprite('iz351_00', 2)
    sprite('iz351_01', 2)
    PrivateSE('izse_02')
    sprite('iz351_02', 2)
    CreateParticle('izef_Drivelight', 0)
    CreateObject('BackHoverDashAura', 0)
    CreateObject('BackHoverDashAura_oku', 1)
    physicsXImpulse(-26000)
    physicsYImpulse(10000)
    setGravity(-400)
    SetAcceleration(600)
    sprite('iz351_03', 2)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    sprite('iz351_03', 2)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    SetActionMark(1)
    sprite('iz351_03', 2)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    label(1)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('BackHoverDashAura', 32)
    TriggerUponForState('BackHoverDashFire', 32)
    TriggerUponForState('BackHoverDashAura_oku', 32)
    sprite('iz351_06', 4)


@State
def SpDashB_Air():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()

        def upon_EVERY_FRAME():
            if SLOT_2:
                WhiffNormalCancel(1)
                WhiffSpecialCancel(1)
                WhiffFAirDashCancel(1)
                WhiffBAirDashCancel(1)
                if not CheckInput(0x5f):
                    sendToLabel(1)

        def upon_STATE_END():
            if not SLOT_IsInHitstun:
                XImpulseAcceleration(30)
                YAccel(50)
                EndYPhysicsImpulse()
        SLOT_63 = 1
        EndMomentum(1)
        ForcedLandingRecovery(3, 1)
    sprite('iz351_06', 2)
    sprite('iz351_02', 2)
    PrivateSE('izse_02')
    CreateParticle('izef_Drivelight', 0)
    CreateObject('BackHoverDashAura', 0)
    CreateObject('BackHoverDashAura_oku', 1)
    physicsXImpulse(-26000)
    physicsYImpulse(5000)
    setGravity(-400)
    SetAcceleration(600)
    sprite('iz351_03', 2)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    sprite('iz351_03', 2)
    SetActionMark(1)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    sprite('iz351_03', 2)
    sprite('iz351_04', 2)
    CreateParticle('izef_Drivelight', 0)
    sprite('iz351_05', 2)
    label(1)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('BackHoverDashAura', 32)
    TriggerUponForState('BackHoverDashFire', 32)
    TriggerUponForState('BackHoverDashAura_oku', 32)
    sprite('iz351_06', 4)


@State
def Shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MyStatusSave')
        WhiffCancel('Warp_D_Land')
        WhiffCancel('Warp_D_Air')
    sprite('iz400_00', 3)
    Voiceline('iz200')
    sprite('iz400_01', 3)
    CreateObject('Shot', 0)
    sprite('iz400_02', 3)
    PrivateSE('izse_05')
    sprite('iz400_03', 3)
    EndMomentum(1)
    sprite('iz400_04', 3)
    physicsXImpulse(-4000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05', 3)
    sprite('iz400_06', 3)
    WhiffCancelEnable(1)
    sprite('iz400_07', 32767)
    uponSendToLabel(LANDING, 0)
    loopRest()
    label(0)
    sprite('iz400_08', 3)
    XImpulseAcceleration(60)
    sprite('iz400_09', 3)
    physicsXImpulse(0)
    WhiffCancelEnable(0)
    LandingEffects(100, 1, 1)
    sprite('iz400_10', 3)
    sprite('iz400_11', 3)
    Recovery()
    sprite('iz400_12', 3)
    sprite('iz400_13', 2)
    sprite('iz400_14', 2)


@State
def Shot_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
        WhiffCancel('Warp_D_Land')
        WhiffCancel('Warp_D_Air')
        SetActionMark(0)
        if SLOT_OverdriveTimer:
            SetActionMark(1)
    sprite('iz400_00', 3)
    Voiceline('iz201')
    sprite('iz400_01ex00', 3)
    if not SLOT_2:
        CreateObject('shotD_Matome', -1)
    else:
        CreateObject('shotD_MatomeOD', -1)
    sprite('iz400_02ex00', 3)
    sprite('iz400_03ex00', 3)
    EndMomentum(1)
    CreateObject('ShotD_Aura', 1)
    sprite('iz400_04ex00', 3)
    PrivateSE('izse_05')
    CreateObject('ShotD_Aura_back', 0)
    physicsXImpulse(-10000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05ex00', 3)
    WhiffCancelEnable(1)
    sprite('iz400_06ex00', 3)
    sprite('iz400_07ex00', 3)
    sprite('iz400_08ex00', 32767)
    uponSendToLabel(LANDING, 0)
    loopRest()
    label(0)
    sprite('iz400_09ex00', 2)
    XImpulseAcceleration(60)
    sprite('iz400_09ex00', 2)
    XImpulseAcceleration(20)
    LandingEffects(100, 1, 1)
    sprite('iz400_10ex00', 3)
    WhiffCancelEnable(0)
    sprite('iz400_11', 3)
    sprite('iz400_12', 3)
    physicsXImpulse(0)
    Recovery()
    sprite('iz400_13', 2)
    sprite('iz400_14', 2)


@State
def AirShot_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('MyStatusSave')
        WhiffCancel('Warp_D_Air')
    sprite('iz401_00', 1)
    Voiceline('iz200')
    ForcedLandingRecovery(7, 1)
    SetInertia(0)
    physicsXImpulse(-6000)
    physicsYImpulse(24000)
    setGravity(1300)
    sprite('iz401_00', 3)
    sprite('iz401_01', 4)
    CreateObject('Air_Shot', 0)
    sprite('iz401_02', 4)
    PrivateSE('izse_05')
    sprite('iz401_03', 3)
    sprite('iz401_04', 3)
    CommonSE('003_swing_grap_0_1')
    WhiffCancelEnable(1)
    sprite('iz401_05', 3)
    sprite('iz401_06', 3)
    sprite('iz401_07', 3)
    sprite('iz401_06', 3)
    sprite('iz401_08', 3)
    sprite('iz401_09', 3)
    sprite('iz401_10', 3)
    sprite('iz401_11', 3)
    sprite('iz401_12', 3)


@State
def AirShot_D():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
        WhiffCancel('Warp_D_Air')
        SetActionMark(0)
        if SLOT_OverdriveTimer:
            SetActionMark(1)
    sprite('iz401_00', 1)
    Voiceline('iz201')
    SetInertia(0)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    setGravity(0)
    sprite('iz401_00', 3)
    sprite('iz401_01ex00', 4)
    if not SLOT_2:
        CreateObject('AirshotD_Matome', -1)
    else:
        CreateObject('AirshotD_MatomeOD', -1)
    sprite('iz401_02ex00', 4)
    sprite('iz401_03ex00', 3)
    PrivateSE('izse_05')
    sprite('iz401_04ex00', 3)
    CreateObject('AirShotAura', 0)
    SetInertia(0)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setGravity(1300)
    CommonSE('003_swing_grap_0_1')
    WhiffCancelEnable(1)
    sprite('iz401_05ex00', 3)
    sprite('iz401_06ex00', 3)
    sprite('iz401_07ex00', 3)
    sprite('iz401_08ex00', 3)
    sprite('iz401_09ex00', 3)
    sprite('iz401_10', 4)
    sprite('iz401_11', 4)
    sprite('iz401_12', 4)


@Subroutine
def Iai_CancelInit():
    HitOrBlockCancel('Warp_A')
    HitOrBlockCancel('Warp_B')
    HitOrBlockCancel('Warp_C')
    HitCancel('Warp_D_LandHitOnly')


@State
def Iai_Slash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(900)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        AirPushbackX(27000)
        AirPushbackY(15000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        UseSlashHitspark(1)
        Hitstop(6)
        StayAfterMovement(1, 0)
        HitAirUnblockable(3)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('Iai_CancelInit')
        HitOrBlockCancel('Iai_Slash_Next')
        ChainCancel(1)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        if not SLOT_94:
            WhiffCancel('Iai_Slash_Next')
            if SLOT_OverdriveTimer:
                WhiffCancel('Warp_D_Land')
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if CheckInput(0x17):
                SLOT_51 = 1
            if SLOT_94:
                SLOT_51 = 1
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
            if SLOT_2:
                if CheckInput(INPUT_HOLD_A):
                    if not SLOT_94:
                        clearUponHandler(EVERY_FRAME)
                        Unknown23170('KamaeStop')
                        sendToLabel(1)

        def upon_STATE_END():
            EndSE()
    sprite('iz402_00', 2)
    EnableAfterimage(1)
    sprite('iz402_01', 1)
    sprite('iz402_01', 1)
    if not SLOT_94:
        WhiffCancelEnable(1)
    sprite('iz402_02', 3)
    PrivateSE('izse_03_start')
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    sprite('iz402_03', 3)
    SetActionMark(1)
    sprite('iz402_04', 3)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    SpecialSE('izse_03_loop')
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    label(0)
    clearUponHandler(RELEASE_C)
    SetActionMark(0)
    Voiceline('iz203')
    sprite('iz402_05', 2)
    EndSE()
    CommonSE('010_swing_sword_2')
    PrivateSE('izse_01')
    CreateObject('Iai_SlashZanzo00', -1)
    TriggerUponForState('Iaimcircle', 33)
    DeleteObject(6)
    DeleteObject(7)
    WhiffCancelEnable(0)
    sprite('iz402_06', 3)
    sprite('iz402_07', 3)
    StartMultihit()
    Recovery()
    sprite('iz402_08', 4)
    sprite('iz402_09', 4)
    sprite('iz402_10', 4)
    label(1)
    clearUponHandler(RELEASE_C)
    SetActionMark(0)
    EndSE()
    Recovery()
    WhiffCancelEnable(0)
    EnableAfterimage(0)
    sprite('iz402_11', 3)
    sprite('iz402_12', 3)
    sprite('iz402_13', 3)


@State
def Iai_Slash_Gedan():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(850)
        AttackP1(90)
        AttackP2(79)
        PushbackX(8000)
        AirPushbackY(12000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HardKnockdown(12)
        EnableEmergencyTechAirHit(1)
        MoveAttributes(0, 0, 1, 0, 0)
        CHAirPushbackX(-800)
        CHAirPushbackY(26000)
        HitAirUnblockable(3)
        HitLow(2)
        AirUntechableTime(30)
        UseSlashHitspark(1)
        Hitstop(6)
        StayAfterMovement(1, 0)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('Iai_CancelInit')
        HitOrBlockCancel('Iai_Slash_Next')
        ChainCancel(1)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        if not SLOT_94:
            WhiffCancel('Iai_Slash_Next')
            if SLOT_OverdriveTimer:
                WhiffCancel('Warp_D_Land')
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if CheckInput(0xe):
                SLOT_51 = 1
            if SLOT_94:
                SLOT_51 = 1
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
            if SLOT_2:
                if CheckInput(INPUT_HOLD_A):
                    if not SLOT_94:
                        clearUponHandler(EVERY_FRAME)
                        Unknown23170('KamaeStop')
                        sendToLabel(1)

        def upon_STATE_END():
            EndSE()
    sprite('iz402_00', 3)
    EnableAfterimage(1)
    sprite('iz402_01', 3)
    if not SLOT_94:
        WhiffCancelEnable(1)
    sprite('iz402_02', 1)
    PrivateSE('izse_03_start')
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    sprite('iz402_02', 2)
    SetActionMark(1)
    sprite('iz402_03', 3)
    sprite('iz402_04', 3)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    SpecialSE('izse_03_loop')
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    label(0)
    sprite('keep', 2)
    clearUponHandler(RELEASE_B)
    SetActionMark(0)
    Voiceline('iz202')
    sprite('iz402_05ex', 3)
    EndSE()
    PrivateSE('izse_01')
    CommonSE('010_swing_sword_2')
    sprite('iz402_06ex', 3)
    CreateObject('Iai_SlashZanzo_Gedan', -1)
    TriggerUponForState('Iaimcircle', 33)
    DeleteObject(6)
    DeleteObject(7)
    WhiffCancelEnable(0)
    sprite('iz402_07ex', 4)
    StartMultihit()
    Recovery()
    sprite('iz402_08', 5)
    sprite('iz402_09', 5)
    sprite('iz402_10', 5)
    label(1)
    clearUponHandler(RELEASE_B)
    SetActionMark(0)
    EndSE()
    Recovery()
    WhiffCancelEnable(0)
    EnableAfterimage(0)
    sprite('iz402_11', 3)
    sprite('iz402_12', 3)
    sprite('iz402_13', 3)


@State
def Iai_Slash_Next():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1100)
        AttackP2(72)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10500)
        AirPushbackY(37000)
        AirUntechableTime(44)
        YImpulseBeforeWallbounce(1650)
        CHAirPushbackX(8000)
        CHAirPushbackY(34000)
        CHGravity(1600)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        HitAirUnblockable(3)
        FatalCounter(1)
        if SLOT_OverdriveTimer:
            SLOT_52 = 1
        if SLOT_52:
            SingleProration(1)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                EnableCollision(0)
                SetXCollisionFromOrigin(40)
                sendToLabel(1)
        callSubroutine('Iai_CancelInit')
        HitCancel('Warp_D_Land')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Land')
        ChainCancel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageMask_1(0, 0, 255, 64)
        AfterimageMask_2(0, 0, 200, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        SLOT_31 = SLOT_31 + -1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('iz403_00', 1)
    ForceFaceSprite()
    PrivateSE('izse_04')
    CharacterFlash(2148384, 4, 2)
    CreateObject('firespark', -1)
    Voiceline('iz204')
    if SLOT_52:
        physicsXImpulse(72500)
    else:
        physicsXImpulse(58000)
    sprite('iz403_00', 2)
    DespawnEAEffect('Iaimcircle')
    DeleteObject(6)
    DeleteObject(7)
    sprite('iz403_00', 3)
    CreateObject('firespark', -1)
    sprite('iz403_01', 2)
    CreateObject('firespark', -1)
    WhiffCancelEnable(1)
    sprite('iz403_02', 3)
    EnemyHitstopAddition(0, 5, 5)
    PrivateSE('izse_01')
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    setInvincible(0)
    physicsXImpulse(8000)
    sprite('iz403_03', 3)
    Recovery()
    XImpulseAcceleration(25)
    sprite('iz403_04', 3)
    XImpulseAcceleration(25)
    sprite('iz403_05', 3)
    ChainCancel(1)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('iz403_06', 3)
    sprite('iz403_07', 3)
    ChainCancel(0)
    WhiffCancelEnable(0)
    sprite('iz403_08', 2)
    sprite('iz403_09', 2)
    sprite('iz403_10', 2)
    ExitState()
    label(1)
    sprite('iz403_00', 2)
    DespawnEAEffect('Iaimcircle')
    DeleteObject(6)
    DeleteObject(7)
    AlphaValue(128)
    sprite('iz403_00', 2)
    TeleportToObject(22)
    AddX(400000)
    AbsoluteY(0)
    ForceFaceSprite()
    CreateObject('firespark', -1)
    sprite('iz403_01', 2)
    sprite('iz403_02', 2)
    PrivateSE('izse_01')
    TeleportToObject(22)
    AddX(-200000)
    AbsoluteY(0)
    physicsXImpulse(60000)
    AlphaValue(255)
    RefreshMultihit()
    HitsparkSize(400)
    Damage(150)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(10000)
    Hitstop(2)
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    sprite('iz403_03', 2)
    AlphaValue(128)
    sprite('iz403_00', 2)
    TeleportToObject(22)
    AbsoluteY(0)
    AddX(400000)
    ForceFaceSprite()
    XImpulseAcceleration(10)
    CreateObject('firespark', -1)
    sprite('iz403_01', 2)
    CreateObject('firespark', -1)
    WhiffCancelEnable(1)
    sprite('iz403_02', 2)
    TeleportToObject(22)
    AddX(-200000)
    AbsoluteY(0)
    physicsXImpulse(60000)
    RefreshMultihit()
    PrivateSE('izse_01')
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    sprite('iz403_02', 2)
    RefreshMultihit()
    XImpulseAcceleration(35)
    sprite('iz403_02', 2)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(50)
    AirPushbackX(10000)
    AirPushbackY(37000)
    CHAirPushbackX(15000)
    CHAirPushbackY(34000)
    XImpulseAcceleration(50)
    sprite('iz403_03', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EnableCollision(1)
    Recovery()
    XImpulseAcceleration(25)
    sprite('iz403_04', 3)
    XImpulseAcceleration(50)
    sprite('iz403_05', 3)
    ChainCancel(1)
    EnableAfterimage(0)
    sprite('iz403_06', 3)
    XImpulseAcceleration(50)
    sprite('iz403_07', 3)
    XImpulseAcceleration(50)
    ChainCancel(0)
    WhiffCancelEnable(0)
    sprite('iz403_08', 2)
    XImpulseAcceleration(50)
    sprite('iz403_09', 2)
    XImpulseAcceleration(0)
    sprite('iz403_10', 2)
    ExitState()


@State
def Iai_Slash_NextAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1100)
        AttackP2(82)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(18000)
        AirPushbackY(30000)
        AirUntechableTime(44)
        YImpulseBeforeWallbounce(1650)
        CHAirPushbackX(8000)
        CHAirPushbackY(34000)
        CHGravity(1600)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        HitAirUnblockable(3)
        FatalCounter(1)
        if SLOT_OverdriveTimer:
            SLOT_52 = 1
        if SLOT_52:
            AirPushbackX(10000)
            YImpulseBeforeWallbounce(1600)
        callSubroutine('Iai_CancelInit')
        HitCancel('Warp_D_Land')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Land')
        ChainCancel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageMask_1(0, 0, 255, 64)
        AfterimageMask_2(0, 0, 200, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        SLOT_31 = SLOT_31 + -1

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_29 < 200000:
                    clearUponHandler(EVERY_FRAME)
                    SetActionMark(0)
                    sendToLabel(100)
        if SLOT_59 == 5:
            sendToLabel(10)
        if SLOT_59 == 6:
            sendToLabel(10)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        AttackOff()
    sprite('keep', 1)
    label(10)
    sprite('iz413_15', 2)
    CreateObject('Iai_AntiAir_Next_413F', -1)
    CreateObject('Iai_AntiAir_Next_413B', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    sprite('iz413_16', 2)
    PrivateSE('izse_04')
    sprite('iz413_17', 2)
    gotoLabel(5)
    label(5)
    sprite('iz403_00', 5)
    TeleportToObject(22)
    AbsoluteY(0)
    AddX(-500000)
    AlphaValue(0)
    ConstantAlphaModifier(63)
    EndMomentum(1)
    if SLOT_59 == 5:
        EndMomentum(1)
        AddX(400000)
    SLOT_59 = 0
    EnableCollision(1)
    ForceFaceSprite()
    CreateObject('Iai_AntiAir_Next_403F', -1)
    CreateObject('Iai_AntiAir_Next_403B', -1)
    CharacterFlash(2148384, 4, 2)
    sprite('iz403_00', 1)
    AlphaValue(255)
    CreateObject('firespark', -1)
    Voiceline('iz204')
    if SLOT_52:
        physicsXImpulse(72000)
    else:
        physicsXImpulse(58000)
    if SLOT_52:
        sendToLabel(1)
    label(0)
    sprite('iz403_00', 2)
    DespawnEAEffect('Iaimcircle')
    DeleteObject(6)
    DeleteObject(7)
    sprite('iz403_00', 3)
    CreateObject('firespark', -1)
    sprite('iz403_01', 2)
    CreateObject('firespark', -1)
    WhiffCancelEnable(1)
    sprite('iz403_02', 3)
    RefreshMultihit()
    PrivateSE('izse_01')
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    setInvincible(0)
    physicsXImpulse(8000)
    sprite('iz403_03', 3)
    Recovery()
    XImpulseAcceleration(60)
    sprite('iz403_04', 3)
    XImpulseAcceleration(20)
    sprite('iz403_05', 3)
    ChainCancel(1)
    EndMomentum(1)
    EnableAfterimage(0)
    sprite('iz403_06', 3)
    sprite('iz403_07', 3)
    ChainCancel(0)
    WhiffCancelEnable(0)
    sprite('iz403_08', 2)
    sprite('iz403_09', 2)
    sprite('iz403_10', 2)
    ExitState()
    label(1)
    sprite('iz403_00', 1)
    HitsparkSize(400)
    Damage(600)
    SingleProration(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(10000)
    Hitstop(3)
    SetActionMark(1)
    DespawnEAEffect('Iaimcircle')
    DeleteObject(6)
    DeleteObject(7)
    sprite('iz403_00', 10)
    label(100)
    sprite('iz403_00', 4)
    clearUponHandler(EVERY_FRAME)
    sprite('iz403_00', 2)
    CreateObject('firespark', -1)
    AlphaValue(255)
    ConstantAlphaModifier(-127)
    sprite('iz403_01', 1)
    TeleportToObject(22)
    AddX(60000)
    AbsoluteY(0)
    AlphaValue(0)
    ConstantAlphaModifier(127)
    ForceFaceSprite()
    CreateObject('firespark', -1)
    WhiffCancelEnable(1)
    XImpulseAcceleration(25)
    sprite('iz403_02', 3)
    RefreshMultihit()
    PrivateSE('izse_01')
    EnableCollision(0)
    physicsXImpulse(90000)
    CHAirPushbackX(0)
    CHAirPushbackY(10000)
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    sprite('iz403_03', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-63)
    XImpulseAcceleration(50)
    sprite('null', 1)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('iz403_00', 2)
    AddX(400000)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    ForceFaceSprite()
    XImpulseAcceleration(10)
    sprite('iz403_00', 3)
    CreateObject('firespark', -1)
    sprite('iz403_01', 2)
    CreateObject('firespark', -1)
    WhiffCancelEnable(1)
    XImpulseAcceleration(25)
    sprite('iz403_02', 2)
    TeleportToObject(22)
    physicsXImpulse(60000)
    AddX(-200000)
    AbsoluteY(0)
    RefreshMultihit()
    PrivateSE('izse_01')
    CreateObject('Ia_SlashNextZanzo', -1)
    CreateObject('IaiSlashNextAura', 0)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_side', 0)
    sprite('iz403_02', 2)
    RefreshMultihit()
    XImpulseAcceleration(50)
    sprite('iz403_02', 2)
    RefreshMultihit()
    AirUntechableTime(50)
    AirPushbackX(20000)
    AirPushbackY(33000)
    CHAirPushbackX(15000)
    CHAirPushbackY(34000)
    XImpulseAcceleration(50)
    sprite('iz403_03', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EnableCollision(1)
    Recovery()
    XImpulseAcceleration(80)
    sprite('iz403_04', 3)
    XImpulseAcceleration(50)
    sprite('iz403_05', 3)
    ChainCancel(1)
    EnableAfterimage(0)
    sprite('iz403_06', 3)
    XImpulseAcceleration(50)
    sprite('iz403_07', 3)
    XImpulseAcceleration(50)
    ChainCancel(0)
    WhiffCancelEnable(0)
    sprite('iz403_08', 2)
    XImpulseAcceleration(50)
    sprite('iz403_09', 2)
    XImpulseAcceleration(0)
    sprite('iz403_10', 2)
    ExitState()


@State
def Iai_AntiAirA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(950)
        AttackP1(80)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(17000)
        AirPushbackY(53000)
        UseSlashHitspark(1)
        AirUntechableTime(41)
        Hitstop(6)
        StayAfterMovement(1, 0)
        HitAirUnblockable(3)
        StarterRating(2)

        def upon_OPPONENT_HIT():
            SLOT_59 = 1
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        callSubroutine('Iai_CancelInit')
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_Land')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Land')
        if not SLOT_94:
            WhiffCancel('Iai_Slash_Next')
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if CheckInput(0xe):
                SLOT_51 = 1
            if SLOT_94:
                SLOT_51 = 1
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
            if SLOT_2:
                if CheckInput(INPUT_HOLD_A):
                    if not SLOT_94:
                        clearUponHandler(EVERY_FRAME)
                        Unknown23170('KamaeStop')
                        sendToLabel(1)
        ChainCancel(1)

        def upon_STATE_END():
            EndSE()
    sprite('iz402_00', 2)
    EnableAfterimage(1)
    sprite('iz402_01', 1)
    sprite('iz402_01', 1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    WhiffCancelEnable(1)
    sprite('iz402_02', 2)
    PrivateSE('izse_03_start')
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    SetActionMark(1)
    sprite('iz402_03', 4)
    setInvincible(0)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    SpecialSE('izse_03_loop')
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    label(0)
    clearUponHandler(RELEASE_B)
    SetActionMark(0)
    Voiceline('iz202')
    sprite('iz404_00', 1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('iz404_01', 2)
    EndSE()
    PrivateSE('izse_01')
    CreateObject('Iai_SlashZanzo_AntiAirA', -1)
    TriggerUponForState('Iaimcircle', 33)
    CommonSE('010_swing_sword_2')
    DeleteObject(6)
    DeleteObject(7)
    PreventWhiffCancel('Iai_Slash_Next')
    sprite('iz404_02', 3)
    sprite('iz404_03', 5)
    setInvincible(0)
    ChainCancel(1)
    Recovery()
    sprite('iz404_04', 5)
    sprite('iz404_05', 5)
    sprite('iz404_06', 5)
    WhiffCancelEnable(0)
    ChainCancel(0)
    EnableAfterimage(0)
    sprite('iz404_07', 4)
    sprite('iz404_08', 4)
    sprite('iz404_09', 4)
    ExitState()
    label(1)
    clearUponHandler(RELEASE_B)
    SetActionMark(0)
    EndSE()
    Recovery()
    sprite('iz402_11', 4)
    setInvincible(0)
    WhiffCancelEnable(0)
    sprite('iz402_12', 4)
    sprite('iz402_13', 4)


@State
def Iai_AntiAirB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(45000)
        CHAirPushbackY(45000)
        UseSlashHitspark(1)
        AirUntechableTime(60)
        Hitstop(6)
        StayAfterMovement(1, 0)
        HitAirUnblockable(3)
        StarterRating(0)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)

        def upon_OPPONENT_HIT():
            SLOT_59 = 2
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_Land')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Land')
        setInvincible(1)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if CheckInput(0x17):
                SLOT_51 = 1
            if SLOT_94:
                SLOT_51 = 1
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
            if SLOT_2:
                if CheckInput(INPUT_HOLD_A):
                    if not SLOT_94:
                        clearUponHandler(EVERY_FRAME)
                        Unknown23170('KamaeStop')
                        sendToLabel(1)
        ChainCancel(1)

        def upon_STATE_END():
            EndSE()
    sprite('iz405_00', 2)
    EnableAfterimage(1)
    sprite('iz405_01', 1)
    sprite('iz405_01', 2)
    WhiffCancelEnable(1)
    sprite('iz405_02', 3)
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    sprite('iz405_03', 2)
    PrivateSE('izse_03_start')
    sprite('iz405_03', 2)
    SetActionMark(1)
    sprite('iz405_02', 4)
    setInvincible(0)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    SpecialSE('izse_03_loop')
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    sprite('iz405_02', 4)
    sprite('iz405_03', 4)
    label(0)
    clearUponHandler(RELEASE_C)
    SetActionMark(0)
    sprite('iz405_04', 3)
    Voiceline('iz205')
    EndSE()
    PrivateSE('izse_01')
    sprite('iz405_05', 3)
    CreateObject('Iai_SlashZanzo_AntiAirB', -1)
    TriggerUponForState('Iaimcircle', 33)
    CommonSE('010_swing_sword_2')
    DeleteObject(6)
    DeleteObject(7)
    sprite('iz405_06', 4)
    setInvincible(0)
    ChainCancel(1)
    sprite('iz405_07', 4)
    sprite('iz405_08', 4)
    sprite('iz405_09', 15)
    sprite('iz405_10', 3)
    EnableAfterimage(0)
    ChainCancel(0)
    sprite('iz405_11', 4)
    sprite('iz405_12', 4)
    sprite('iz405_13', 4)
    sprite('iz405_14', 4)
    ExitState()
    label(1)
    clearUponHandler(RELEASE_C)
    SetActionMark(0)
    EndSE()
    sprite('iz405_03', 4)
    setInvincible(0)
    sprite('iz405_02', 4)
    sprite('iz405_01', 8)
    sprite('iz405_00', 8)


@State
def Iai_SlashAirA():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(1080)
        AttackP1(90)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(17000)
        AirPushbackY(53000)
        UseSlashHitspark(1)
        AirUntechableTime(43)
        Hitstop(6)
        StayAfterMovement(1, 0)
        StarterRating(3)

        def upon_OPPONENT_HIT():
            SLOT_59 = 4
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        callSubroutine('Iai_CancelInit')
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_Air')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Air')
        callSubroutine('AdditionalExGage')
    sprite('iz413_00', 2)
    EndMomentum(1)
    sprite('iz413_01', 1)
    sprite('iz413_01', 1)
    WhiffCancelEnable(1)
    sprite('iz413_02', 2)
    sprite('iz413_05', 2)
    PrivateSE('izse_01')
    sprite('iz413_06', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('izef_413_a', -1)
    Voiceline('iz211')
    sprite('iz413_07', 3)
    sprite('iz413_08', 4)
    Recovery()
    sprite('iz413_09', 4)
    sprite('iz413_10', 4)
    sprite('iz413_11', 4)
    ChainCancel(0)
    sprite('iz413_01', 4)
    GravityDefault()
    sprite('iz413_00', 4)
    sprite('iz020_05', 4)
    WhiffCancelEnable(0)
    sprite('iz020_06', 4)
    label(0)
    sprite('iz020_07', 3)
    sprite('iz020_08', 3)
    gotoLabel(0)


@State
def Iai_SlashAirB():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(1050)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        AirPushbackX(15000)
        AirPushbackY(48000)
        AirUntechableTime(44)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        UseSlashHitspark(1)
        Hitstop(6)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            SLOT_59 = 5
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        callSubroutine('Iai_CancelInit')
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_Air')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Air')
        callSubroutine('AdditionalExGage')
    sprite('iz413_00', 2)
    EndMomentum(1)
    sprite('iz413_01', 1)
    sprite('iz413_01', 1)
    WhiffCancelEnable(1)
    sprite('iz413_02', 2)
    sprite('iz413_03', 1)
    PrivateSE('izse_01')
    sprite('iz413_04', 1)
    sprite('iz413_12', 2)
    Voiceline('iz212')
    CommonSE('010_swing_sword_2')
    sprite('iz413_13', 3)
    CreateObject('izef_413_b', -1)
    sprite('iz413_14', 3)
    Recovery()
    sprite('iz413_15', 4)
    sprite('iz413_16', 4)
    sprite('iz413_17', 4)
    ChainCancel(0)
    sprite('iz413_18', 3)
    sprite('iz413_01', 3)
    GravityDefault()
    sprite('iz413_00', 4)
    sprite('iz020_05', 4)
    WhiffCancelEnable(0)
    sprite('iz020_06', 4)
    label(0)
    sprite('iz020_07', 3)
    sprite('iz020_08', 3)
    gotoLabel(0)


@State
def Iai_SlashAirC():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(1020)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        AirPushbackX(6500)
        AirPushbackY(45000)
        AirUntechableTime(44)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        UseSlashHitspark(1)
        Hitstop(6)
        StayAfterMovement(1, 0)

        def upon_OPPONENT_HIT():
            SLOT_59 = 6
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        callSubroutine('AdditionalExGage')
        callSubroutine('MyStatusSave')
        callSubroutine('Iai_CancelInit')
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_Air')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Air')
        callSubroutine('AdditionalExGage')
    sprite('iz413_00', 2)
    EndMomentum(1)
    sprite('iz413_01', 1)
    sprite('iz413_01', 1)
    WhiffCancelEnable(1)
    sprite('iz413_02', 2)
    sprite('iz413_03', 1)
    PrivateSE('izse_01')
    sprite('iz413_04', 1)
    sprite('iz413_12ex', 2)
    Voiceline('iz213')
    CreateObject('izef_413_c', -1)
    CommonSE('010_swing_sword_2')
    sprite('iz413_13ex', 3)
    sprite('iz413_14ex', 3)
    Recovery()
    sprite('iz413_15', 4)
    sprite('iz413_16', 4)
    sprite('iz413_17', 3)
    ChainCancel(0)
    sprite('iz413_18', 3)
    sprite('iz413_01', 3)
    GravityDefault()
    sprite('iz413_00', 4)
    sprite('iz020_05', 4)
    WhiffCancelEnable(0)
    sprite('iz020_06', 4)
    label(0)
    sprite('iz020_07', 3)
    sprite('iz020_08', 3)
    gotoLabel(0)


@State
def Iai_AntiAir_Next():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-60000)
        BouncePercentage(14)
        GroundBounce(1)
        UseSlashHitspark(1)
        AirUntechableTime(100)
        EnemyHitstopAddition(0, 6, 6)
        Hitstop(2)
        if SLOT_OverdriveTimer:
            SLOT_52 = 1
        if SLOT_52:
            Damage(850)
        StayAfterMovement(1, 0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        if SLOT_59 == 1:
            sendToLabel(2)
        if SLOT_59 == 2:
            sendToLabel(3)
        if SLOT_59 == 3:
            sendToLabel(4)
        if SLOT_59 == 4:
            sendToLabel(10)
        if SLOT_59 == 5:
            sendToLabel(10)
        if SLOT_59 == 6:
            sendToLabel(10)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        callSubroutine('Iai_CancelInit')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Land')
        NoAttackDuringAction(1)
        SLOT_31 = SLOT_31 + -1
        EndMomentum(1)
    sprite('keep', 1)
    Voiceline('iz207')
    label(2)
    sprite('iz404_03', 2)
    CreateObject('Iai_AntiAir_Next_404F', -1)
    CreateObject('Iai_AntiAir_Next_404B', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    sprite('iz404_04', 2)
    PrivateSE('izse_04')
    sprite('iz404_05', 2)
    gotoLabel(5)
    label(3)
    sprite('iz405_07', 2)
    CreateObject('Iai_AntiAir_Next_405F', -1)
    CreateObject('Iai_AntiAir_Next_405B', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    sprite('iz405_08', 2)
    PrivateSE('izse_04')
    sprite('iz405_09', 2)
    gotoLabel(5)
    label(4)
    sprite('iz408_07', 3)
    CreateObject('Iai_AntiAir_Next_408F', -1)
    CreateObject('Iai_AntiAir_Next_408B', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    sprite('iz408_08', 3)
    PrivateSE('izse_04')
    gotoLabel(5)
    label(10)
    sprite('iz413_15', 2)
    CreateObject('Iai_AntiAir_Next_413F', -1)
    CreateObject('Iai_AntiAir_Next_413B', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    sprite('iz413_16', 2)
    PrivateSE('izse_04')
    sprite('iz413_17', 2)
    gotoLabel(5)
    label(5)
    sprite('iz406_00', 1)
    ConstantAlphaModifier(30)
    EnableCollision(0)
    ForceFaceSprite()
    TeleportToObject(22)
    if SLOT_59 == 1:
        AddY(300000)
        AddX(200000)
        SLOT_59 = 0
    if SLOT_59 == 2:
        AddY(160000)
        AddX(-60000)
        SLOT_59 = 0
    if SLOT_59 == 3:
        EndMomentum(1)
        AddY(220000)
        AddX(250000)
        SLOT_59 = 0
    if SLOT_59 == 4:
        EndMomentum(1)
        AddX(250000)
        AddY(240000)
        SLOT_59 = 0
    if SLOT_59 == 5:
        EndMomentum(1)
        AddX(200000)
        AddY(120000)
        SLOT_59 = 0
    if SLOT_59 == 6:
        EndMomentum(1)
        AddX(-50000)
        AddY(90000)
        SLOT_59 = 0
    sprite('iz406_00', 3)
    CreateObject('Iai_AntiAir_Next_406F', -1)
    CreateObject('Iai_AntiAir_Next_406B', -1)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    sprite('iz406_01', 4)
    CharacterFlash(2148384, 10, 2)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(5)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setGravity(0)
    physicsYImpulse(2000)
    if SLOT_52:
        sendToLabel(100)
    sprite('iz406_02', 4)
    sprite('iz406_03', 4)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('iz406_04', 4)
    sprite('iz406_05', 4)
    sprite('iz406_06', 3)
    NoAttackDuringAction(0)
    PrivateSE('izse_01')
    physicsYImpulse(-80000)
    if SLOT_52:
        setGravity(15000)
    else:
        setGravity(7000)
    CreateObject('Iai_AntiAirNext_Zanzo', -1)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_length', 2)
    CreateObject('IaiAntiAirNextAuraL', 0)
    CreateObject('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)
    sprite('iz406_07', 3)
    sprite('iz406_08', 3)
    gotoLabel(0)
    label(100)
    sprite('iz406_02', 4)
    sprite('iz406_03', 4)
    sprite('iz406_04', 4)
    sprite('iz406_05', 4)
    sprite('iz406_06', 1)
    NoAttackDuringAction(0)
    PrivateSE('izse_01')
    Damage(700)
    SingleProration(1)
    physicsYImpulse(-80000)
    setGravity(7000)
    CreateObject('Iai_AntiAirNext_Zanzo', -1)
    ParticleLayer(5)
    CallCustomizableParticle('izef_iaislashnext_length', 2)
    sprite('iz406_06', 1)
    RefreshMultihit()
    sprite('iz406_06', 1)
    RefreshMultihit()
    label(101)
    sprite('iz406_06', 3)
    sprite('iz406_07', 3)
    sprite('iz406_08', 3)
    gotoLabel(101)
    label(1)
    sprite('iz406_09', 5)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    TriggerUponForState('Iai_AntiAirNext_Zanzo', 32)
    TriggerUponForState('IaiAntiAirNextAuraL', 32)
    TriggerUponForState('IaiAntiAirNextAuraR', 32)
    EndMomentum(1)
    sprite('iz406_10', 9)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('iz406_11', 3)
    sprite('iz406_12', 5)
    sprite('iz406_13', 5)
    ExitState()


@State
def AirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(1100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP2(79)
        AirUntechableTime(46)
        AirPushbackX(16000)
        CHAirPushbackX(4000)
        AirPushbackY(45000)
        UseSlashHitspark(1)

        def upon_OPPONENT_HIT():
            SLOT_59 = 3
        HitCancel('Iai_AntiAir_Next')
        HitCancel('Warp_D_AirHitOnly')
        if SLOT_OverdriveTimer:
            WhiffCancel('Warp_D_Air')
        callSubroutine('AdditionalExGage')
    sprite('iz408_00', 3)
    Voiceline('iz206')
    physicsYImpulse(0)
    setGravity(0)
    XImpulseAcceleration(60)
    sprite('iz408_01', 3)
    sprite('iz408_02', 3)
    CommonSE('008_swing_pole_2')
    PrivateSE('izse_01')
    sprite('iz408_03', 2)
    CreateObject('AirAssaultZanzo', -1)
    XSpeed(3000)
    YSpeed(3000)
    WhiffCancelEnable(1)
    sprite('iz408_04', 3)
    physicsXImpulse(-7500)
    physicsYImpulse(12000)
    GravityDefault()
    sprite('iz408_05', 2)
    Recovery()
    YSpeed(7000)
    ChainCancel(1)
    sprite('iz408_06', 2)
    sprite('iz408_07', 2)
    sprite('iz408_08', 2)
    ChainCancel(0)
    sprite('iz408_09', 2)
    sprite('iz408_10', 2)
    WhiffCancelEnable(0)
    sprite('iz408_11', 3)
    sprite('iz408_12', 3)
    label(0)
    sprite('iz020_07', 3)
    sprite('iz020_08', 3)
    gotoLabel(0)


@Subroutine
def WarpFlexCancel():
    WhiffCancel('NmlAtkThrow')
    WhiffCancel('NmlAtkBackThrow')
    WhiffCancel('Iai_Slash')
    WhiffCancel('Iai_Slash_Gedan')
    WhiffCancel('Iai_AntiAirA')
    WhiffCancel('Iai_AntiAirB')
    WhiffCancel('Shot_A')
    WhiffCancel('Shot_D')
    if op(15, 2, 51, 0, 1):
        WhiffCancel('Warp_A')
    if op(15, 2, 51, 0, 2):
        WhiffCancel('Warp_B')
    if op(15, 2, 51, 0, 3):
        WhiffCancel('Warp_C')
    WhiffCancel('Warp_D_Land')


@State
def Warp_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
        SLOT_51 = 1
        callSubroutine('MyStatusSave')
        callSubroutine('WarpFlexCancel')
    sprite('iz409_00', 2)
    Voiceline('iz208')
    SetXCollisionFromOrigin(50)
    sprite('iz409_01', 3)
    sprite('iz409_02', 3)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    sprite('iz409_02', 3)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_03', 3)
    physicsXImpulse(3000)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz409_03', 3)
    physicsXImpulse(12000)
    sprite('iz409_03', 1)
    physicsXImpulse(100000)
    sprite('iz409_03', 1)
    physicsXImpulse(40000)
    sprite('iz409_03', 1)
    physicsXImpulse(-100000)
    sprite('iz409_03', 1)
    physicsXImpulse(-40000)
    sprite('iz409_03', 2)
    EnableCollision(1)
    ForceFaceSprite()
    physicsXImpulse(-6000)
    ConstantAlphaModifier(60)
    setInvincible(0)
    sprite('iz409_04', 2)
    CreateObject('Warp_A_Zanzo00', -1)
    CreateObject('Warp_A_Zanzo01', -1)
    sprite('iz409_05', 3)
    XImpulseAcceleration(10)
    sprite('iz409_06', 3)
    WhiffNormalCancel(1)
    WhiffCancelEnable(1)
    sprite('iz409_07', 3)
    sprite('iz409_08', 3)
    sprite('iz409_09', 3)


@State
def Warp_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
        SLOT_51 = 2
        callSubroutine('MyStatusSave')
        callSubroutine('WarpFlexCancel')
    sprite('iz409_00', 3)
    Voiceline('iz209')
    SetXCollisionFromOrigin(50)
    sprite('iz409_01', 4)
    sprite('iz409_02', 3)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    sprite('iz409_02', 3)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_03', 3)
    physicsXImpulse(3000)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz409_03', 3)
    physicsXImpulse(12000)
    sprite('iz409_03', 3)
    XImpulseAcceleration(1200)
    sprite('iz409_03', 2)
    CreateObject('firespark', 0)
    EnableCollision(1)
    ForceFaceSprite()
    XImpulseAcceleration(10)
    ConstantAlphaModifier(60)
    sprite('iz409_04', 2)
    setInvincible(0)
    sprite('iz409_05', 3)
    sprite('iz409_06', 3)
    XImpulseAcceleration(20)
    sprite('iz409_07', 3)
    WhiffNormalCancel(1)
    WhiffCancelEnable(1)
    sprite('iz409_08', 3)
    sprite('iz409_09', 3)


@State
def Warp_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
        NegativeForBackDash()
        SLOT_51 = 3
        callSubroutine('MyStatusSave')
        callSubroutine('WarpFlexCancel')
    sprite('iz409_00', 4)
    Voiceline('iz210')
    SetXCollisionFromOrigin(50)
    sprite('iz409_01', 5)
    sprite('iz409_02', 3)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    sprite('iz409_02', 3)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_10', 3)
    physicsXImpulse(-3000)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    setInvincible(1)
    sprite('iz409_10', 3)
    physicsXImpulse(-16000)
    sprite('iz409_10', 2)
    XImpulseAcceleration(900)
    sprite('iz409_10', 2)
    CreateParticle('izef_firespark', 0)
    EnableCollision(1)
    ForceFaceSprite()
    physicsXImpulse(-6000)
    ConstantAlphaModifier(60)
    setInvincible(0)
    sprite('iz409_11', 3)
    XImpulseAcceleration(90)
    sprite('iz409_12', 3)
    XImpulseAcceleration(90)
    sprite('iz409_13', 1)
    XImpulseAcceleration(90)
    sprite('iz409_13', 2)
    WhiffNormalCancel(1)
    WhiffCancelEnable(1)
    sprite('iz409_14', 3)
    XImpulseAcceleration(20)
    sprite('iz409_15', 3)
    sprite('iz409_16', 3)


@State
def Warp_D_Land():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        Unknown2061(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
            ForceFaceSprite()
            ResetAirJumpCount()
            ResetAirDashCount()
            EnableAfterimage(0)
            RenderLayer(0)
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
    sprite('iz409_00', 1)
    SetXCollisionFromOrigin(50)
    sprite('iz409_01', 2)
    sprite('iz409_02', 3)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff_D', 0)
    sprite('iz409_02', 3)
    ConstantAlphaModifier(-40)
    BlendMode_Normal()
    sprite('iz410_00ex', 3)
    physicsXImpulse(3000)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    AlphaValue(0)
    setInvincible(1)
    sprite('iz410_01ex', 3)
    physicsXImpulse(12000)
    sprite('null', 3)
    XImpulseAcceleration(800)
    sprite('iz410_02ex', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
    if SLOT_51 <= 430000:
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    TeleportToObject(22)
    sprite('iz409_10ex00', 1)
    AddX(70000)
    AbsoluteY(0)
    EndMomentum(1)
    ForceFaceSprite()
    RenderLayer(5)
    sprite('iz409_10ex00', 2)
    CreateObject('WarpHoverAura', 1)
    CreateParticle('izef_firespark', 0)
    EnableCollision(1)
    ConstantAlphaModifier(60)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)
    sprite('iz409_12ex00', 2)
    sprite('iz409_13ex00', 2)
    sprite('iz409_14ex00', 1)
    sprite('iz409_15ex00', 1)
    sprite('iz409_16', 1)
    ExitState()
    label(1)
    TeleportToObject(22)
    sprite('iz410_02', 2)
    EnableCollision(1)
    AddX(70000)
    AddY(-60000)
    EndMomentum(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    ConstantAlphaModifier(60)
    RenderLayer(5)
    sprite('iz410_03', 2)
    CreateObject('WarpHoverAura_Air', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz410_04', 2)
    sprite('iz410_05', 2)
    sprite('iz410_06', 2)
    sprite('iz410_07', 1)
    sprite('iz410_07', 1)
    EndYPhysicsImpulse()


@State
def Warp_D_LandHitOnly():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
        Unknown2061(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
            ForceFaceSprite()
            ResetAirJumpCount()
            ResetAirDashCount()
            EnableAfterimage(0)
            RenderLayer(0)
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
    sprite('iz409_00', 1)
    SetXCollisionFromOrigin(50)
    sprite('iz409_01', 2)
    sprite('iz409_02', 3)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff_D', 0)
    sprite('iz409_02', 3)
    ConstantAlphaModifier(-40)
    BlendMode_Normal()
    sprite('iz410_00ex', 3)
    physicsXImpulse(3000)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    AlphaValue(0)
    setInvincible(1)
    sprite('iz410_01ex', 3)
    physicsXImpulse(12000)
    sprite('null', 3)
    XImpulseAcceleration(800)
    sprite('iz410_02ex', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
    if SLOT_51 <= 430000:
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    TeleportToObject(22)
    sprite('iz409_10ex00', 1)
    AddX(70000)
    AbsoluteY(0)
    EndMomentum(1)
    ForceFaceSprite()
    RenderLayer(5)
    sprite('iz409_10ex00', 2)
    CreateObject('WarpHoverAura', 1)
    CreateParticle('izef_firespark', 0)
    EnableCollision(1)
    ConstantAlphaModifier(60)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)
    sprite('iz409_12ex00', 2)
    sprite('iz409_13ex00', 2)
    sprite('iz409_14ex00', 1)
    sprite('iz409_15ex00', 1)
    sprite('iz409_16', 1)
    ExitState()
    label(1)
    TeleportToObject(22)
    sprite('iz410_02', 2)
    EnableCollision(1)
    AddX(70000)
    AddY(-40000)
    EndMomentum(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    ConstantAlphaModifier(60)
    RenderLayer(5)
    sprite('iz410_03', 1)
    CreateObject('WarpHoverAura_Air', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz410_04', 1)
    sprite('iz410_05', 1)
    sprite('iz410_06', 1)
    sprite('iz410_07', 1)
    sprite('iz410_07', 1)
    EndYPhysicsImpulse()


@State
def Warp_D_Air():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        Unknown2061(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
            ForceFaceSprite()
            ResetAirJumpCount()
            ResetAirDashCount()
            EnableAfterimage(0)
            RenderLayer(0)
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
    sprite('iz410_00', 4)
    SetXCollisionFromOrigin(50)
    XImpulseAcceleration(50)
    physicsYImpulse(0)
    setGravity(0)
    sprite('iz410_01', 4)
    sprite('iz410_02', 1)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Air_Zanzo00', -1)
    CreateObject('Warp_D_Air_Zanzo01', -1)
    CreateObject('WarpEff_D', 0)
    sprite('iz410_02', 3)
    physicsXImpulse(3000)
    BlendMode_Normal()
    ConstantAlphaModifier(-40)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(0)
    sprite('iz410_00ex01', 3)
    physicsXImpulse(12000)
    AlphaValue(0)
    sprite('iz410_01ex01', 3)
    XImpulseAcceleration(800)
    sprite('iz410_02ex01', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
    if SLOT_51 <= 430000:
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    TeleportToObject(22)
    sprite('iz409_10ex00', 1)
    AddX(70000)
    AbsoluteY(0)
    EndMomentum(1)
    ConstantAlphaModifier(60)
    ForceFaceSprite()
    RenderLayer(5)
    sprite('iz409_10ex00', 2)
    CreateObject('WarpHoverAura', 1)
    CreateParticle('izef_firespark', 0)
    EnableCollision(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)
    sprite('iz409_12ex00', 2)
    sprite('iz409_13ex00', 2)
    sprite('iz409_14ex00', 1)
    sprite('iz409_15ex00', 1)
    sprite('iz409_16', 1)
    ExitState()
    label(1)
    TeleportToObject(22)
    sprite('iz410_02', 2)
    EnableCollision(1)
    AddX(70000)
    AddY(-60000)
    EndMomentum(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    ConstantAlphaModifier(60)
    RenderLayer(5)
    sprite('iz410_03', 2)
    CreateObject('WarpHoverAura_Air', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz410_04', 2)
    sprite('iz410_05', 1)
    sprite('iz410_06', 1)
    sprite('iz410_07', 1)
    sprite('iz410_07', 1)
    EndYPhysicsImpulse()


@State
def Warp_D_AirHitOnly():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        PreventBlocking(1)
        Unknown2061(1)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
            ForceFaceSprite()
            ResetAirJumpCount()
            ResetAirDashCount()
            EnableAfterimage(0)
            RenderLayer(0)
        SLOT_31 = SLOT_31 + -1
        callSubroutine('MyStatusSave')
    sprite('iz410_00', 4)
    SetXCollisionFromOrigin(50)
    XImpulseAcceleration(50)
    physicsYImpulse(0)
    setGravity(0)
    sprite('iz410_01', 4)
    sprite('iz410_02', 1)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Air_Zanzo00', -1)
    CreateObject('Warp_D_Air_Zanzo01', -1)
    CreateObject('WarpEff_D', 0)
    sprite('iz410_02', 3)
    physicsXImpulse(3000)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    CommonSE('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(0)
    sprite('iz410_02', 3)
    physicsXImpulse(12000)
    sprite('iz410_02', 3)
    XImpulseAcceleration(800)
    sprite('iz410_02', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
    if SLOT_51 <= 430000:
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    TeleportToObject(22)
    sprite('iz409_10ex00', 1)
    AddX(70000)
    AbsoluteY(0)
    EndMomentum(1)
    ConstantAlphaModifier(60)
    ForceFaceSprite()
    RenderLayer(5)
    sprite('iz409_10ex00', 2)
    CreateObject('WarpHoverAura', 1)
    CreateParticle('izef_firespark', 0)
    EnableCollision(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)
    sprite('iz409_12ex00', 2)
    sprite('iz409_13ex00', 2)
    sprite('iz409_14ex00', 1)
    sprite('iz409_15ex00', 1)
    sprite('iz409_16', 1)
    ExitState()
    label(1)
    TeleportToObject(22)
    sprite('iz410_02', 2)
    EnableCollision(1)
    AddX(70000)
    AddY(-80000)
    EndMomentum(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    ConstantAlphaModifier(60)
    RenderLayer(5)
    sprite('iz410_03', 2)
    CreateObject('WarpHoverAura_Air', 0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 0, 255, 64)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    setInvincible(0)
    sprite('iz410_04', 2)
    sprite('iz410_05', 2)
    sprite('iz410_06', 2)
    sprite('iz410_07', 1)
    sprite('iz410_07', 1)
    EndYPhysicsImpulse()


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MyStatusSave')
        AttackLevel_(4)
        Damage(2500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(82)
        AirUntechableTime(40)
        Floorslide(20)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirPushbackY(20000)
        AirPushbackX(50000)
        ProjectileLevel(2)
        UseSlashHitspark(1)
        setInvincible(1)
        MinimumDamage(30)
        StayAfterMovement(1, 0)
        StarterRating(0)
        HitCancel('Warp_D_LandHitOnly')
    sprite('iz430_00', 3)
    DistortionSettings(88, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_IZ', -1)
    sprite('iz430_01', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    sprite('iz430_04', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    PrivateSE('izse_06')
    sprite('iz430_04', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    sprite('iz430_04', 3)
    sprite('iz430_05', 3)
    CreateObject('DD_3d_zanzoh', 0)
    CreateObject('DD_pt_edge', 0)
    CreateObject('DD_pt_circle', 0)
    SmartVoiceline('iz250')
    sprite('iz430_06', 3)
    sprite('iz430_07', 3)
    CreateObject('DD_3Dcircle_out', -1)
    CreateObject('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)
    sprite('iz430_09', 3)
    sprite('iz430_10', 3)
    sprite('iz430_11', 3)
    sprite('iz430_12', 3)
    sprite('iz430_13', 3)
    sprite('iz430_14', 2)
    sprite('iz430_15', 2)
    sprite('iz430_16', 4)
    sprite('iz430_17', 5)
    sprite('iz430_18', 18)
    sprite('iz430_18', 1)
    if SLOT_4 == 1:
        sendToLabel(1)
    else:
        sendToLabel(0)
    label(0)
    sprite('iz430_19', 2)
    sprite('iz430_20', 3)
    Voiceline('iz251')
    ScreenShake(60000, 20000)
    CreateObject('DD_sword', 0)
    CreateObject('DD_sword_env', 0)
    CreateObject('DD_3d_swordaura', 0)
    sprite('iz430_21', 3)
    ScreenShake(5000, 0)
    sprite('iz430_22', 3)
    sprite('iz430_20', 3)
    AttackOff()
    setInvincible(0)
    sprite('iz430_21', 3)
    sprite('iz430_22', 3)
    sprite('iz430_20', 3)
    sprite('iz430_21', 3)
    sprite('iz430_22', 3)
    TriggerUponForState('DD_3d_swordaura', 32)
    sprite('iz430_23', 3)
    sprite('iz430_24', 3)
    gotoLabel(2)
    label(1)
    sprite('iz430_19ex00', 2)
    sprite('iz430_20ex00', 1)
    Voiceline('iz251')
    ScreenShake(20000, 0)
    CreateObject('DD_sword', -1)
    CreateObject('DD_sword_env', -1)
    CreateObject('DD_3d_swordaura', -1)
    CreateObject('UltimateAssaultAura', 0)
    CreateObject('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex00', 2)
    if SLOT_OverdriveTimer:
        WhiffCancelEnable(1)
    sprite('iz430_21ex00', 3)
    sprite('iz430_22ex00', 3)
    sprite('iz430_20ex00', 3)
    AttackOff()
    setInvincible(0)
    sprite('iz430_21ex00', 3)
    sprite('iz430_22ex00', 3)
    sprite('iz430_20ex00', 3)
    sprite('iz430_21ex00', 3)
    sprite('iz430_22ex00', 3)
    sprite('iz430_23ex00', 3)
    TriggerUponForState('DD_3d_swordaura', 32)
    sprite('iz430_24ex00', 3)
    gotoLabel(2)
    label(2)
    sprite('iz430_25', 5)
    WhiffCancelEnable(0)
    sprite('iz430_26', 5)
    sprite('iz430_27', 5)
    sprite('iz430_28', 5)
    sprite('iz430_29', 5)


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MyStatusSave')
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(82)
        AirUntechableTime(40)
        Floorslide(20)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirPushbackY(20000)
        AirPushbackX(50000)
        ProjectileLevel(2)
        UseSlashHitspark(1)
        setInvincible(1)
        MinimumDamage(30)
        AttackType(4)
        AttackType(4)
        StayAfterMovement(1, 0)
        StarterRating(0)
        HitCancel('Warp_D_LandHitOnly')
        WhiffCancel('Warp_D_Land')
    sprite('iz430_00', 3)
    DistortionSettings(88, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_IZ', -1)
    sprite('iz430_01', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    sprite('iz430_04', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    PrivateSE('izse_06')
    sprite('iz430_04', 3)
    sprite('iz430_02', 3)
    sprite('iz430_03', 3)
    sprite('iz430_04', 3)
    sprite('iz430_05', 3)
    CreateObject('DD_3d_zanzoh', 0)
    CreateObject('DD_pt_edge', 0)
    CreateObject('DD_pt_circle', 0)
    Voiceline('iz250')
    sprite('iz430_06', 3)
    sprite('iz430_07', 3)
    CreateObject('DD_3Dcircle_out', -1)
    CreateObject('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)
    sprite('iz430_09', 3)
    sprite('iz430_10', 3)
    sprite('iz430_11', 3)
    sprite('iz430_12', 3)
    sprite('iz430_13', 3)
    sprite('iz430_14', 2)
    sprite('iz430_15', 2)
    sprite('iz430_16', 4)
    sprite('iz430_17', 5)
    sprite('iz430_18', 18)
    sprite('iz430_18', 1)
    sprite('iz430_19ex00', 2)
    sprite('iz430_20ex01', 1)
    Damage(3000)
    if SLOT_137:
        DamageMultiplier(80)
    Voiceline('iz251')
    ScreenShake(20000, 0)
    CreateObject('DD_sword_OD', -1)
    CreateObject('DD_sword_env_OD', -1)
    CreateObject('DD_3d_swordaura', -1)
    CreateObject('UltimateAssaultAura', 0)
    CreateObject('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex01', 2)
    WhiffCancelEnable(1)
    sprite('iz430_21ex01', 3)
    sprite('iz430_22ex01', 3)
    sprite('iz430_20ex01', 3)
    AttackOff()
    setInvincible(0)
    sprite('iz430_21ex01', 3)
    sprite('iz430_22ex01', 3)
    sprite('iz430_20ex00', 3)
    sprite('iz430_21ex00', 3)
    sprite('iz430_22ex00', 3)
    sprite('iz430_23ex00', 3)
    TriggerUponForState('DD_3d_swordaura', 32)
    sprite('iz430_24ex00', 3)
    gotoLabel(2)
    label(2)
    sprite('iz430_25', 5)
    WhiffCancelEnable(0)
    sprite('iz430_26', 5)
    sprite('iz430_27', 5)
    sprite('iz430_28', 5)
    sprite('iz430_29', 5)


@State
def SummonFunnel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        StayAfterMovement(1, 0)
        PreventBlocking(1)
        SLOT_32 = 0
        ObjectUpon(FALLING, 41)
        ObjectUpon(5, 41)
    sprite('iz431_00', 3)
    sprite('iz431_01', 3)
    Voiceline('iz252')
    DistortionSettings(154, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB_IZ', -1)
    CreateObject('iz431_mahojin', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 200, 255, 200)
    AfterimageMask_2(0, 0, 200, 0)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    setInvincible(1)
    SLOT_60 = 0
    sprite('iz431_02', 25)
    sprite('iz431_03', 3)
    sprite('iz431_04', 3)
    sprite('iz431_05', 3)
    sprite('iz431_06', 3)
    sprite('iz431_07', 3)
    sprite('iz431_08', 3)
    sprite('iz431_09', 3)
    sprite('iz431_10', 3)
    sprite('iz431_11', 3)
    sprite('iz431_12', 3)
    sprite('iz431_13', 3)
    sprite('iz431_14', 5)
    PrivateSE('izse_07')
    CharacterFlash(9895830, 30, 2)
    CreateParticle('GNptcCharget', 0)
    CreateParticle('GNptcCharget', 1)
    sprite('iz431_15', 6)
    sprite('iz431_16', 7)
    sprite('iz431_17', 20)
    sprite('iz431_18', 2)
    sprite('iz431_19', 4)
    Voiceline('iz253')
    CreateObject('SummonFunnelF', -1)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    SLOT_32 = 720
    CreateObject('ShieildBit', 1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 33)
    CreateObject('ShieildBit', 0)
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    setInvincible(0)
    sprite('iz431_21', 3)
    sprite('iz431_22', 2)
    sprite('iz431_24', 4)
    sprite('iz431_25', 4)
    EnableAfterimage(0)
    sprite('iz431_26', 4)
    sprite('iz431_27', 4)
    sprite('iz431_28', 4)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        EndMomentum(1)
        DefeatOpponentBehavior(1)
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(200)
        Damage(0)
        AirUntechableTime(1000)
        Hitstun(1000)
        HardKnockdown(200)
        Hitstop(20)
        EnemyHitstopAddition(-5, 1000, 1000)
        OppPositionOnHit(3, 128000, -256000)
        IgnoreComboTime(1)
        SingleComboCorrection(1)
        MinimumDamage(100)
        UseSlashHitspark(1)
        DisableOppPushCollision(1)
        setInvincible(1)

        def upon_OPPONENT_HIT():
            enterState('AstralHeatExe')
            AstralHeatCleanup(1, 1)
    sprite('iz450_00', 3)
    Voiceline('iz290')
    sprite('iz450_01', 3)
    DistortionSettings(131, -1, 2)
    EmptyHeat()
    CameraControlEnable(1)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_IZ_AH', -1)
    sprite('iz450_02', 3)
    sprite('iz450_03', 3)
    sprite('iz450_04', 3)
    sprite('iz450_02', 3)
    CreateObject('AST1st_mahojin', -1)
    sprite('iz450_03', 3)
    sprite('iz450_04', 3)
    sprite('iz450_02', 3)
    sprite('iz450_03', 3)
    sprite('iz450_04', 3)
    sprite('iz450_02', 3)
    sprite('iz450_03', 3)
    sprite('iz450_04', 3)
    sprite('iz450_02', 3)
    sprite('iz450_03', 3)
    sprite('iz450_04', 3)
    sprite('iz450_05', 6)
    sprite('iz450_06', 6)
    sprite('iz450_07', 4)
    CreateParticle('izef_AH_changelightA', -1)
    sprite('iz450_08', 4)
    sprite('iz450_09', 4)
    sprite('iz450_07', 4)
    CharacterFlash(16777215, 12, 1)
    sprite('iz450_08', 4)
    sprite('iz450_09', 4)
    sprite('iz450_07', 4)
    sprite('iz450_08', 4)
    CreateObject('AST_changeBG', 0)
    sprite('iz450_09', 4)
    CreateParticle('izef_AH_changelightB', 0)
    CreateObject('AST_changelightC', 0)
    CommonSE('022_magiccircle_b')
    CommonSE('022_magiccircle_b')
    sprite('iz450_10', 6)
    CharacterFlash(0, 12, 1)
    sprite('iz450_11', 16)
    CreateObject('AST_1stAuraR', 0)
    CreateObject('AST_1stAuraL', 1)
    sprite('iz450_12', 6)
    sprite('iz450_13', 6)
    sprite('iz450_14', 6)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(0)
    AfterimageCount(5)
    AfterimageMask_1(0, 0, 255, 128)
    AfterimageMask_2(0, 0, 255, 128)
    AfterimageSize_1(1000)
    AfterimageSize_2(1500)
    sprite('iz450_15', 6)
    sprite('iz450_16', 3)
    physicsXImpulse(60000)
    sprite('iz450_17', 3)
    sprite('iz450_18', 3)
    sprite('iz450_19', 5)
    setInvincible(0)
    XImpulseAcceleration(80)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 8, 1)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    CreateParticle('izef_dellight', 2)
    CreateParticle('izef_dellight', 3)
    CreateParticle('izef_dellight', 4)
    CreateParticle('izef_dellight', 5)
    CreateParticle('izef_dellight', 6)
    CreateParticle('izef_dellight', 7)
    sprite('iz450_20', 5)
    XImpulseAcceleration(60)
    sprite('iz450_21', 5)
    XImpulseAcceleration(40)
    sprite('iz450_22', 5)
    XImpulseAcceleration(10)
    sprite('iz450_23', 5)
    physicsXImpulse(0)
    EnableAfterimage(0)
    sprite('iz450_24', 5)
    sprite('iz450_25', 5)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(5, 0, 0)
        DamageFromStateOnly('AstralHeatExe')
        UseSlashHitspark(1)
        AstralHeatCleanup(1, 1)
        PlayPlayAstralBGM(1)
        CameraControlEnable(1)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        HUDVisibillity(1)
    sprite('iz450_16', 3)
    CreateObject('AstWhite', -1)
    StartMultihit()
    sprite('iz450_17', 3)
    StartMultihit()
    sprite('iz450_18', 3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    StartMultihit()
    sprite('iz450_16', 1)
    StartMultihit()
    sprite('null', 195)
    CreateObject('iz450cutin', -1)
    SetBackground(3)
    AbsoluteY(7800000)
    AlphaValue(0)

    def RunOnObject_22():
        Visibility(1)
        AbsoluteY(6000000)
        XPositionRelativeFacing(0)
        setGravity(0)
    sprite('null', 45)
    CreateObject('AST_2ndAura', -1)
    sprite('null', 60)
    CreateObject('iz450dammy', -1)
    sprite('null', 40)
    PrivateSE('izse_09')
    sprite('null', 115)
    sprite('null', 5)
    ScreenShake(0, 2000)
    CommonSE('019_quake_1')
    sprite('null', 5)
    ScreenShake(0, 2000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 2000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 2000)
    sprite('null', 5)
    ScreenShake(0, 2000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 2000)
    SpecialSE('izse_09_loop')
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 3000)
    sprite('null', 5)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 3000)
    sprite('null', 5)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 5000)
    sprite('null', 5)
    ScreenShake(0, 5000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 5000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 5000)
    EndSE()
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 5000)
    sprite('null', 5)
    PrivateSE('izse_10')
    ScreenShake(0, 30000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 30000)
    sprite('null', 5)
    ScreenShake(0, 20000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 20000)
    sprite('null', 5)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    sprite('null', 5)
    ScreenShake(0, 10000)
    CommonSE('019_quake_0')
    sprite('null', 20)
    CreateObject('AstWhitefinish', -1)
    CreateObject('izef_ah_Ryuhai', -1)
    sprite('null', 5)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 1)
    SetBackground(2)
    sprite('null', 10)
    XPositionRelativeFacing(0)
    AbsoluteY(6000000)
    setGravity(0)
    CreateObject('ASTbg', -1)
    sprite('null', 60)
    CreateObject('izef_ah_javelin2', -1)
    sprite('null', 30)
    TriggerUponForState('ASTbg', 32)
    CreateObject('izef_ah_javelin3', -1)
    CreateParticle('izef_ahfinish_nigiyakasi', -1)

    def RunOnObject_22():
        Visibility(0)
        RenderLayer(2)
        Size(600)
        AddY(100000)
    sprite('null', 15)
    ScreenShake(15000, 15000)
    CommonSE('025_cleanhit_slash')
    sprite('null', 90)
    CreateObject('AstralHeatKillObject', -1)
    ScreenShake(300000, 300000)
    TriggerUponForState('izef_ah_javelin00', 32)
    TriggerUponForState('izef_ah_javelin_backfire00', 32)
    sprite('iz450_44', 10)
    SetBackground(0)
    CameraControlEnable(1)
    CameraLookAtEnemy(1)
    CameraControlInfinity(1)
    sprite('iz450_44', 7)
    FaceRight()
    AlphaValue(255)
    XPositionRelativeFacing(200000)
    AbsoluteY(0)
    CallCustomizableParticle('izef_ah_finishhane', -1)

    def RunOnObject_22():
        Visibility(1)
    sprite('iz450_45', 7)
    sprite('iz450_46', 7)
    sprite('iz450_47', 7)
    sprite('iz450_48', 7)
    WinAction()
    DemoTimer(90)
    sprite('iz450_44', 7)
    Voiceline('iz408')
    sprite('iz450_45', 7)
    sprite('iz450_46', 7)
    sprite('iz450_47', 7)
    sprite('iz450_48', 7)
    label(0)
    sprite('iz450_44', 7)
    sprite('iz450_45', 7)
    sprite('iz450_46', 7)
    sprite('iz450_47', 7)
    sprite('iz450_48', 7)
    gotoLabel(0)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('iz054')
    sprite('iz900_00', 32767)
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
    sprite('iz901_00', 50)
    physicsYImpulse(-150)
    sprite('iz901_00', 50)
    physicsYImpulse(150)
    Voiceline('iz055')
    label(0)
    sprite('iz901_00', 50)
    physicsYImpulse(-150)
    sprite('iz901_00', 50)
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
        OppPositionOnHit(1, 300000, 0)
        PushbackX(19800)
        UseSlashHitspark(1)
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        DamageFromStateOnly('BurstDDFunnel')

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('iz440_00', 4)
    E0EAEffect('BurstDDeff', 103)
    sprite('iz440_01', 4)
    Voiceline('iz280')
    sprite('iz440_02', 4)
    sprite('iz440_03', 3)
    sprite('iz440_04', 2)
    sprite('iz311_05ex01', 2)
    AddX(100000)
    SetXCollisionFromOrigin(250)
    CommonSE('006_swing_blade_2')
    sprite('iz311_06ex01', 3)
    AddX(90000)
    sprite('iz311_07ex01', 6)
    setInvincible(0)
    SetXCollisionFromOrigin(-1)
    sprite('iz311_08ex01', 6)
    sprite('iz311_09ex01', 6)
    AddX(-60000)
    sprite('iz311_10ex01', 6)
    AddX(-60000)
    sprite('iz311_11ex01', 5)
    AddX(-70000)
    sprite('iz311_12ex01', 5)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        OppPositionOnHit(1, 300000, 0)
        PushbackX(19800)
        UseSlashHitspark(1)
        Blockstun(26)
        Hitstop(20)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        DamageFromStateOnly('BurstDDFunnel')

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
    sprite('iz440_00', 2)
    E0EAEffect('BurstDDeff', 103)
    sprite('iz440_01', 2)
    Voiceline('iz280')
    sprite('iz440_02', 2)
    sprite('iz440_03', 1)
    sprite('iz440_04', 1)
    sprite('iz311_05ex01', 1)
    AddX(100000)
    SetXCollisionFromOrigin(250)
    CommonSE('006_swing_blade_2')
    sprite('iz311_06ex01', 3)
    AddX(90000)
    sprite('iz311_07ex01', 6)
    setInvincible(0)
    SetXCollisionFromOrigin(-1)
    sprite('iz311_08ex01', 6)
    sprite('iz311_09ex01', 6)
    AddX(-60000)
    sprite('iz311_10ex01', 6)
    AddX(-60000)
    sprite('iz311_11ex01', 5)
    AddX(-70000)
    sprite('iz311_12ex01', 5)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(60000)
        AirUntechableTime(60)
        Wallbounce(1)
        WallbounceReboundTime(5)
        HardKnockdown(10)
        MinimumDamage(10)
        SetBackground(1)
        callSubroutine('MyStatusSave')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(34)
            sendToLabel(2)
    sprite('iz311_06ex01', 3)
    CreateObject('BurstDD_MagicCircle', -1)
    CreateObject('BurstDDCamera', -1)
    StartMultihit()
    sprite('iz311_07ex01', 6)
    sprite('iz311_08ex01', 6)
    sprite('iz311_09ex01', 4)
    physicsXImpulse(-10000)
    sprite('iz311_10ex01', 4)
    XImpulseAcceleration(25)
    sprite('iz311_11ex01', 4)
    XImpulseAcceleration(25)
    sprite('iz400_01ex01', 4)
    Voiceline('iz281')
    CreateObject('BurstDDFunnel', -1)
    if SLOT_51:
        ObjectUpon(STATE_END, 32)
    sprite('iz400_02ex01', 4)
    XImpulseAcceleration(0)
    sprite('iz400_03ex01', 4)
    sprite('iz400_04ex01', 4)
    sprite('iz400_05ex01', 4)
    label(100)
    sprite('iz400_06ex01', 4)
    sprite('iz400_07ex01', 4)
    sprite('iz400_08ex01', 4)
    gotoLabel(100)
    label(1)
    sprite('iz400_09ex01', 4)
    sprite('iz440_05', 4)
    sprite('iz440_06', 4)
    sprite('iz440_07', 4)
    CreateObject('BurstDDSlashEff', -1)
    sprite('iz440_08', 4)
    sprite('iz440_09', 4)
    sprite('iz440_10', 4)
    label(200)
    sprite('iz440_11', 4)
    sprite('iz440_12', 4)
    sprite('iz440_13', 4)
    gotoLabel(200)
    label(2)
    sprite('iz440_14', 3)
    sprite('iz440_15', 3)
    sprite('iz440_16', 3)
    sprite('iz440_17', 3)
    sprite('iz440_18', 3)
    sprite('iz440_19', 3)
    sprite('iz440_20', 3)
    sprite('iz440_21', 3)
    sprite('iz440_22', 3)
    if SLOT_44:
        Voiceline('iz282')
    sprite('iz440_23', 3)
    sprite('iz440_21', 3)
    sprite('iz440_22', 3)
    sprite('iz440_23', 3)
    sprite('iz440_21', 3)
    sprite('iz440_22', 3)
    sprite('iz440_23', 3)
    sprite('iz440_21', 3)
    sprite('iz440_22', 3)
    sprite('iz440_23', 3)
    sprite('iz440_21', 3)
    if not SLOT_44:
        Voiceline('iz282')
    sprite('iz440_22', 3)
    sprite('iz440_23', 3)
    sprite('iz440_24', 6)
    sprite('iz440_25', 6)
    sprite('iz440_26', 2)
    sprite('iz440_27', 3)
    CreateObject('BurstDDSlashEff2', -1)
    sprite('iz440_28', 3)
    sprite('iz440_29', 3)
    sprite('iz440_27', 3)
    sprite('iz440_28', 3)
    sprite('iz440_29', 3)
    sprite('iz440_27', 3)
    sprite('iz440_28', 3)
    sprite('iz440_29', 3)
    CreateObject('BurstDDRetrunEff', -1)
    sprite('iz440_30', 5)
    TriggerUponForState('BurstDDCamera', 33)
    sprite('iz440_31', 5)
    sprite('iz203_06ex01', 5)
    sprite('iz203_07ex01', 5)
    sprite('iz203_08ex01', 5)
    loopRest()


@Subroutine
def MouthTableInit():
    Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz055', 13665, 13667, 13665, 13667, 13665, 13667, 13665, 
        13667, 13921, 13923, 13921, 13923, 12897, 25392, 54, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz291', 14433, 13667, 13921, 13923, 13921, 13923, 13665, 
        13667, 14177, 13923, 14177, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz292', 14433, 13667, 13665, 13667, 13665, 13667, 13665, 
        13667, 13665, 13667, 13921, 13667, 13921, 13411, 13409, 13411, 
        14177, 13667, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz293', 14177, 13923, 14177, 13923, 13665, 13411, 14177, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz294', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 
        13411, 12641, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz295', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 
        13411, 12641, 25398, 24884, 25396, 25396, 24884, 13873, 13411, 
        13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('iz400', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz401', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz404', 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz405', 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz406', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        13923, 13921, 13923, 12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz407', 14433, 14435, 14433, 14435, 14433, 13411, 24885, 
        25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz408', 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz412', 14433, 13923, 14433, 13923, 14433, 13923, 14433, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz413', 14433, 13923, 14433, 13923, 14433, 13923, 14433, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz414', 14433, 13923, 14433, 13923, 14433, 13923, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz415', 14433, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('iz417', 14433, 13923, 14433, 13923, 14433, 99, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz291', 13921, 13923, 13921, 13923, 13921, 13923, 
            12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz292', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 12641, 25392, 56, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('iz293', 13409, 13411, 13409, 13411, 13409, 13411, 
            13409, 13411, 12641, 25398, 24884, 25396, 52, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('iz294', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz295', 13409, 13411, 13409, 13411, 13409, 13411, 
            13409, 13411, 12641, 25398, 24884, 25396, 52, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('iz400', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('iz401', 13921, 13923, 13921, 13923, 13921, 13923, 
            14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz405', 14177, 14179, 14177, 14179, 14177, 13923, 
            13921, 13923, 13921, 13923, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('iz406', 13409, 13667, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 
            25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz407', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz408', 13921, 13923, 13921, 13923, 13921, 13923, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('iz412', 14433, 13923, 14433, 13923, 14433, 13923, 
            14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz413', 14433, 13923, 14433, 13923, 14433, 13923, 
            14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz414', 14433, 13923, 14433, 13923, 14433, 13923, 
            14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz415', 14433, 13923, 14433, 13923, 14433, 13923, 
            14433, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('iz417', 14433, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('jn'):
            Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 14179,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz400', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('iz400', 14177, 14179, 14177, 13411, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 13155,
                24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('iz400', 14177, 14179, 14177, 14179, 14177, 
                    13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 13155,
                24880, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 13617, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz400', 14177, 14179, 14177, 13667, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mu'):
            if SLOT_140:
                Unknown18011('iz000', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 13155, 24880, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('iz400', 14177, 14179, 14177, 13411, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 
                    13155, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ma'):
            Unknown18011('iz000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz400', 13921, 13923, 13921, 13667, 24880, 25399,
                24887, 25399, 24887, 25399, 13617, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            if SLOT_138:
                Unknown18011('iz500', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('iz501', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880,
                    25399, 24887, 25398, 12342, 13921, 13923, 14433, 14179,
                    13921, 13923, 14433, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('iz500', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13155, 24886,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('iz501', 14433, 14435, 14433, 14435, 14433, 
                    14435, 14177, 14179, 14177, 13923, 24885, 25398, 24886,
                    25398, 24886, 25398, 24886, 12337, 13923, 13921, 13923,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('iz502', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13155, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz503', 14177, 14179, 14177, 13411, 24885, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('iz504', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('iz505', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 12340, 13921, 13923, 14433, 
                14179, 13921, 13923, 14433, 14179, 14433, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('iz520', 14177, 14179, 14177, 13411, 24885, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz521', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 24880, 25398, 24886, 25398, 
                12342, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('iz530', 14177, 14179, 14177, 13411, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz531', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 
                24880, 25399, 24887, 25399, 12340, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            if SLOT_140:
                Unknown18011('iz530', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13667, 24880, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown18011('iz531', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13411, 24880, 25398, 24886, 25398, 24886, 25398, 25398,
                    54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('iz546', 14177, 13155, 14177, 13411, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz547', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mu'):
            if SLOT_140:
                Unknown18011('iz528', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13411, 24880, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('iz529', 13921, 13923, 13921, 13923, 13921, 
                    13667, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ma'):
            Unknown18011('iz568', 14177, 14179, 14177, 13667, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 12339, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('iz569', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 24880, 25399, 24887, 25399, 
                24887, 25399, 14386, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('ma'):
        SyncEntry()
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(120)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('mu'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2240)
    if CharacterIDCheck('mk'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2250)
        else:
            gotoLabel(250)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('ma'):
        SyncEntry()
        gotoLabel(430)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('iz600_00', 6)
    sprite('iz600_00', 60)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('iz600_00', 45)
    Voiceline('iz412')
    sprite('iz600_01', 5)
    sprite('iz600_02', 5)
    sprite('iz600_03', 6)
    CreateParticle('izef_entryhane', -1)
    CreateParticle('izef_entrymcB', -1)
    CommonSE('019_cloth_c')
    sprite('iz600_04', 6)
    sprite('iz600_05', 6)
    sprite('iz600_06', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 18)
    sprite('iz600_07', 6)
    sprite('iz600_07ex00', 6)
    sprite('iz600_08', 6)
    sprite('iz600_09', 6)
    CharacterFlash2(0, 6)
    CommonSE('022_magiccircle_b')
    sprite('iz600_10', 7)
    StopCharacterFlash2()
    sprite('iz600_11', 7)
    sprite('iz600_12', 7)
    sprite('iz600_13', 6)
    Voiceline('iz413')
    sprite('iz600_14', 6)
    sprite('iz600_15', 5)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(10)
    sprite('iz601_00', 6)
    sprite('iz601_00', 60)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('iz601_00', 30)
    Voiceline('iz414')
    sprite('iz601_00', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('iz601_01', 7)
    sprite('iz601_02', 7)
    sprite('iz601_03', 7)
    sprite('iz601_04', 5)
    sprite('iz601_05', 5)
    sprite('iz601_06', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    CreateParticle('izef_entrylightB', 0)
    sprite('iz601_08', 7)
    sprite('iz601_09', 7)
    if SLOT_43:
        Voiceline('iz415')
        DemoTimer(110)
    CreateObject('iz601amourlight', -1)
    CommonSE('022_magiccircle_a')
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_12', 7)
    sprite('iz601_13', 7)
    sprite('iz601_14', 7)
    sprite('iz601_15', 7)
    sprite('iz601_16', 7)
    sprite('iz601_17', 7)
    CreateParticle('izef_armchange', 0)
    sprite('iz601_18', 7)
    CreateObject('iz601swdlight', -1)
    sprite('iz601_19', 7)
    sprite('iz601_20', 7)
    sprite('iz601_20', 1)
    if SLOT_44:
        Voiceline('iz415')
        DemoTimer(90)
    loopRest()
    ExitState()
    label(20)
    sprite('iz602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('iz602_01', 6)
    sprite('iz602_02', 6)
    sprite('iz602_03', 6)
    sprite('iz602_04', 6)
    sprite('iz602_05', 6)
    sprite('iz602_06', 6)
    sprite('iz602_07', 6)
    sprite('iz602_08', 6)
    sprite('iz000_00', 7)
    Voiceline('iz417')
    DemoTimer(60)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    ExitState()
    label(100)
    uponSendToLabel(32, 102)
    label(101)
    sprite('iz602_00', 6)
    loopRest()
    gotoLabel(101)
    label(102)
    clearUponHandler(32)
    sprite('iz602_00', 30)
    Voiceline('iz500')
    DemoTimer(180)
    sprite('iz602_01', 8)
    sprite('iz602_02', 6)
    sprite('iz602_03', 6)
    sprite('iz602_04', 6)
    sprite('iz602_05', 6)
    sprite('iz602_06', 6)
    sprite('iz602_07', 6)
    sprite('iz602_08', 6)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    loopRest()
    sprite('iz300_00', 6)
    sprite('iz300_01', 6)
    sprite('iz300_02', 6)
    sprite('iz300_03', 6)
    PrivateSE('izse_01')
    sprite('iz300_04', 4)
    sprite('iz300_05', 4)
    sprite('iz300_06', 4)
    sprite('iz300_07', 4)
    sprite('iz300_08', 4)
    sprite('iz300_09', 4)
    sprite('iz300_10', 4)
    sprite('iz300_11', 4)
    sprite('iz300_12', 4)
    ExitState()
    label(1100)
    sprite('iz602_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1100)
    sprite('iz602_00', 10)
    sprite('iz602_00', 30)
    Voiceline('iz500')
    DemoEndOnVoiceEnd(1)
    sprite('iz602_01', 8)
    sprite('iz602_02', 6)
    sprite('iz602_03', 6)
    sprite('iz602_04', 6)
    sprite('iz602_05', 6)
    sprite('iz602_06', 6)
    sprite('iz602_07', 6)
    sprite('iz602_08', 6)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz300_00', 6)
    sprite('iz300_01', 6)
    sprite('iz300_02', 6)
    sprite('iz300_03', 6)
    PrivateSE('izse_01')
    sprite('iz300_04', 4)
    sprite('iz300_05', 4)
    sprite('iz300_06', 4)
    sprite('iz300_07', 4)
    sprite('iz300_08', 10)
    sprite('iz300_09', 4)
    sprite('iz300_10', 4)
    sprite('iz300_11', 4)
    sprite('iz300_12', 4)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(110)
    sprite('iz600_00', 1)
    if SLOT_17:
        conditionalSendToLabel(110)
    sprite('iz600_00', 30)
    sprite('iz600_00', 140)
    Voiceline('iz502')
    DemoEndOnVoiceEnd(1)
    sprite('iz600_01', 6)
    sprite('iz600_02', 6)
    sprite('iz600_03', 6)
    CreateParticle('izef_entryhane', -1)
    CreateParticle('izef_entrymcB', -1)
    CommonSE('019_cloth_c')
    sprite('iz600_04', 6)
    sprite('iz600_05', 6)
    sprite('iz600_06', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 18)
    sprite('iz600_07', 6)
    sprite('iz600_07ex00', 6)
    sprite('iz600_08', 6)
    sprite('iz600_09', 6)
    CharacterFlash2(0, 6)
    CommonSE('022_magiccircle_b')
    ObjectUpon(22, 32)
    sprite('iz600_10', 7)
    StopCharacterFlash2()
    sprite('iz600_11', 7)
    sprite('iz600_12', 7)
    sprite('iz600_13', 6)
    sprite('iz600_14', 6)
    sprite('iz600_15', 5)
    loopRest()
    ExitState()
    label(120)
    sprite('iz600_00', 6)
    sprite('iz600_00', 60)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(120)
    sprite('iz600_00', 45)
    Voiceline('iz504')
    DemoTimer(300)
    sprite('iz600_01', 5)
    sprite('iz600_02', 5)
    sprite('iz600_03', 6)
    CreateParticle('izef_entryhane', -1)
    CreateParticle('izef_entrymcB', -1)
    CommonSE('019_cloth_c')
    sprite('iz600_04', 6)
    sprite('iz600_05', 6)
    sprite('iz600_06', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 18)
    sprite('iz600_07', 6)
    sprite('iz600_07ex00', 6)
    sprite('iz600_08', 6)
    sprite('iz600_09', 6)
    CharacterFlash2(0, 6)
    CommonSE('022_magiccircle_b')
    sprite('iz600_10', 7)
    StopCharacterFlash2()
    sprite('iz600_11', 7)
    sprite('iz600_12', 7)
    sprite('iz600_13', 6)
    sprite('iz600_14', 6)
    sprite('iz600_15', 5)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(200)
    sprite('iz601_00', 6)
    sprite('iz601_00', 60)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(200)
    sprite('iz601_00', 200)
    Voiceline('iz520')
    sprite('iz601_00', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    sprite('iz601_01', 7)
    sprite('iz601_02', 7)
    sprite('iz601_03', 7)
    sprite('iz601_04', 5)
    sprite('iz601_05', 5)
    sprite('iz601_06', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    CreateParticle('izef_entrylightB', 0)
    sprite('iz601_08', 7)
    sprite('iz601_09', 7)
    CreateObject('iz601amourlight', -1)
    CommonSE('022_magiccircle_a')
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_12', 7)
    sprite('iz601_13', 7)
    sprite('iz601_14', 7)
    sprite('iz601_15', 7)
    sprite('iz601_16', 7)
    sprite('iz601_17', 7)
    CreateParticle('izef_armchange', 0)
    sprite('iz601_18', 7)
    CreateObject('iz601swdlight', -1)
    sprite('iz601_19', 7)
    sprite('iz601_20', 7)
    sprite('iz601_20', 1)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(250)
    uponSendToLabel(32, 252)
    label(251)
    sprite('iz602_00', 6)
    loopRest()
    gotoLabel(251)
    label(252)
    clearUponHandler(32)
    sprite('iz602_00', 30)
    Voiceline('iz530')
    sprite('iz602_01', 8)
    sprite('iz602_02', 6)
    sprite('iz602_03', 6)
    sprite('iz602_04', 6)
    sprite('iz602_05', 6)
    sprite('iz602_06', 6)
    sprite('iz602_07', 6)
    sprite('iz602_08', 6)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    loopRest()
    sprite('iz300_00', 6)
    sprite('iz300_01', 6)
    sprite('iz300_02', 6)
    sprite('iz300_03', 6)
    PrivateSE('izse_01')
    sprite('iz300_04', 4)
    sprite('iz300_05', 4)
    sprite('iz300_06', 4)
    sprite('iz300_07', 4)
    sprite('iz300_08', 4)
    sprite('iz300_09', 4)
    sprite('iz300_10', 4)
    sprite('iz300_11', 4)
    sprite('iz300_12', 4)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2250)
    sprite('iz601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2250)
    sprite('iz601_00', 20)
    sprite('iz601_00', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    uponSendToLabel(32, 2252)
    sprite('iz601_01', 7)
    sprite('iz601_02', 7)
    sprite('iz601_03', 7)
    sprite('iz601_04', 5)
    sprite('iz601_05', 5)
    sprite('iz601_06', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    CreateParticle('izef_entrylightB', 0)
    sprite('iz601_08', 7)
    sprite('iz601_09', 7)
    CreateObject('iz601amourlight', -1)
    CommonSE('022_magiccircle_a')
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_12', 7)
    sprite('iz601_13', 7)
    sprite('iz601_14', 7)
    sprite('iz601_15', 7)
    sprite('iz601_16', 7)
    sprite('iz601_17', 7)
    CreateParticle('izef_armchange', 0)
    ObjectUpon(22, 32)
    sprite('iz601_18', 7)
    CreateObject('iz601swdlight', -1)
    sprite('iz601_19', 7)
    sprite('iz601_20', 7)
    label(2251)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(2251)
    label(2252)
    sprite('iz001_00', 6)
    Voiceline('iz530')
    sprite('iz001_01', 6)
    sprite('iz001_02', 6)
    sprite('iz001_03', 6)
    PrivateSE('izse_01')
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    SetActionMark(6)
    label(2253)
    sprite('iz001_04', 6)
    AddActionMark(-1)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2253)
    sprite('iz001_09', 6)
    sprite('iz001_10', 6)
    sprite('iz001_11', 6)
    DemoTimer(40)
    loopRest()
    ExitState()
    label(2240)
    sprite('iz601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2240)
    sprite('iz601_00', 20)
    sprite('iz601_00', 6)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    uponSendToLabel(32, 2242)
    sprite('iz601_01', 7)
    sprite('iz601_02', 7)
    sprite('iz601_03', 7)
    sprite('iz601_04', 5)
    sprite('iz601_05', 5)
    sprite('iz601_06', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    sprite('iz601_07', 6)
    CreateParticle('izef_entrylightB', 0)
    sprite('iz601_08', 7)
    sprite('iz601_09', 7)
    CreateObject('iz601amourlight', -1)
    CommonSE('022_magiccircle_a')
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_12', 7)
    sprite('iz601_13', 7)
    sprite('iz601_14', 7)
    sprite('iz601_15', 7)
    sprite('iz601_16', 7)
    sprite('iz601_17', 7)
    CreateParticle('izef_armchange', 0)
    sprite('iz601_18', 7)
    CreateObject('iz601swdlight', -1)
    sprite('iz601_19', 7)
    sprite('iz601_20', 7)
    label(2241)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(2241)
    label(2242)
    sprite('iz001_00', 6)
    Voiceline('iz528')
    sprite('iz001_01', 6)
    sprite('iz001_02', 6)
    sprite('iz001_03', 6)
    PrivateSE('izse_01')
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    SetActionMark(2)
    label(2243)
    sprite('iz001_04', 6)
    AddActionMark(-1)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2243)
    sprite('iz001_09', 6)
    sprite('iz001_10', 6)
    sprite('iz001_11', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(330)
    uponSendToLabel(32, 332)
    label(331)
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    Voiceline('iz546')
    label(333)
    sprite('iz001_04', 6)
    sprite('iz001_05', 6)
    sprite('iz001_06', 6)
    sprite('iz001_07', 6)
    sprite('iz001_08', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(333)
    sprite('iz001_09', 6)
    ObjectUpon(22, 32)
    sprite('iz001_10', 6)
    sprite('iz001_11', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(430)
    sprite('iz600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(430)
    sprite('iz600_00', 20)

    def upon_32():
        SetActionMark(1)
    sprite('iz600_01', 5)
    sprite('iz600_02', 5)
    sprite('iz600_03', 6)
    CreateParticle('izef_entryhane', -1)
    CreateParticle('izef_entrymcB', -1)
    CommonSE('019_cloth_c')
    sprite('iz600_04', 6)
    sprite('iz600_05', 6)
    sprite('iz600_06', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 18)
    sprite('iz600_07', 6)
    sprite('iz600_07ex00', 6)
    sprite('iz600_08', 6)
    sprite('iz600_09', 6)
    CharacterFlash2(0, 6)
    CommonSE('022_magiccircle_b')
    sprite('iz600_10', 7)
    StopCharacterFlash2()
    sprite('iz600_11', 7)
    sprite('iz600_12', 7)
    sprite('iz600_13', 6)
    sprite('iz600_14', 6)
    sprite('iz600_15', 5)
    ObjectUpon(22, 32)
    sprite('iz001_00', 7)
    sprite('iz001_01', 7)
    sprite('iz001_02', 7)
    sprite('iz001_03', 7)
    PrivateSE('izse_01')
    label(431)
    sprite('iz001_04', 7)
    sprite('iz001_05', 7)
    sprite('iz001_06', 7)
    sprite('iz001_07', 7)
    sprite('iz001_08', 7)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(431)
    sprite('iz001_04', 7)
    sprite('iz001_05', 7)
    sprite('iz001_06', 7)
    Voiceline('iz568')
    sprite('iz001_07', 7)
    sprite('iz001_08', 7)
    sprite('iz001_09', 6)
    sprite('iz001_10', 6)
    sprite('iz001_11', 6)
    DemoTimer(265)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('iz615_00', 6)
    if random_(2, 0, 50):
        Voiceline('iz400')
    else:
        Voiceline('iz401')
    DemoEndOnVoiceEnd(1)
    sprite('iz615_01', 6)
    sprite('iz615_02', 6)
    sprite('iz615_03', 6)
    sprite('iz615_04', 6)
    sprite('iz615_05', 6)
    sprite('iz615_06', 6)
    sprite('iz615_07', 6)
    sprite('iz615_08', 32767)


@State
def CmnActMatchWin():
    if SLOT_61:
        conditionalSendToLabel(10)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('no'):
        conditionalSendToLabel(120)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('mu'):
        if SLOT_140:
            conditionalSendToLabel(2240)
    if CharacterIDCheck('mk'):
        if SLOT_140:
            gotoLabel(2250)
        else:
            gotoLabel(250)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('ma'):
        conditionalSendToLabel(430)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    if SLOT_44:
        conditionalSendToLabel(5)
    sprite('iz610_00', 7)
    sprite('iz610_00', 7)
    sprite('iz610_01', 7)
    sprite('iz610_02', 7)
    sprite('iz610_03', 7)
    sprite('iz610_04', 7)
    Voiceline('iz407')
    DemoEndOnVoiceEnd(1)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    label(1)
    sprite('iz610_04', 7)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    loopRest()
    gotoLabel(1)
    label(5)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz407')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(16)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(16)
    label(10)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz408')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(11)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('iz612_00', 5)
    sprite('iz612_01', 5)
    sprite('iz612_02', 5)
    sprite('iz612_03', 5)
    sprite('iz612_04', 5)
    sprite('iz612_05', 5)
    sprite('iz612_06', 5)
    Voiceline('iz406')
    DemoEndOnVoiceEnd(1)
    sprite('iz612_07', 5)
    sprite('iz612_08', 6)
    sprite('iz612_09', 6)
    sprite('iz612_10', 6)
    sprite('iz612_11', 6)
    label(21)
    sprite('iz612_07', 6)
    sprite('iz612_08', 6)
    sprite('iz612_09', 6)
    sprite('iz612_10', 6)
    sprite('iz612_11', 6)
    loopRest()
    gotoLabel(21)
    label(100)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz501')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(101)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(101)
    label(1100)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz501')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(1101)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(1101)
    label(110)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz503')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(111)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(111)
    label(120)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz505')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(121)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(121)
    label(200)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz521')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(201)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(201)
    label(2240)
    sprite('iz610_00', 7)
    sprite('iz610_01', 7)
    sprite('iz610_02', 7)
    Voiceline('iz529')
    DemoEndOnVoiceEnd(1)
    sprite('iz610_03', 7)
    label(2241)
    sprite('iz610_04', 7)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    loopRest()
    gotoLabel(2241)
    label(250)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz531')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(251)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(251)
    label(2250)
    sprite('iz610_00', 7)
    sprite('iz610_01', 7)
    sprite('iz610_02', 7)
    Voiceline('iz531')
    DemoEndOnVoiceEnd(1)
    sprite('iz610_03', 7)
    label(2251)
    sprite('iz610_04', 7)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    loopRest()
    gotoLabel(2251)
    label(330)
    sprite('iz610_00', 7)
    sprite('iz610_01', 7)
    sprite('iz610_02', 7)
    Voiceline('iz547')
    DemoEndOnVoiceEnd(1)
    sprite('iz610_03', 7)
    label(331)
    sprite('iz610_04', 7)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    loopRest()
    gotoLabel(331)
    label(430)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    Voiceline('iz569')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(431)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(431)
    label(666)
    sprite('iz611_00', 6)
    sprite('iz611_01', 6)
    sprite('iz611_02', 6)
    sprite('iz611_03', 6)
    sprite('iz611_04', 6)
    sprite('iz611_05', 6)
    sprite('iz611_06', 6)
    sprite('iz611_07', 6)
    sprite('iz611_08', 6)
    sprite('iz611_09', 6)
    sprite('iz611_10', 6)
    if random_(2, 0, 50):
        Voiceline('iz407')
    else:
        Voiceline('iz408')
    DemoEndOnVoiceEnd(1)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    label(667)
    sprite('iz611_10', 6)
    sprite('iz611_11', 6)
    sprite('iz611_12', 6)
    sprite('iz611_13', 6)
    loopRest()
    gotoLabel(667)


@State
def CmnActLose():
    sprite('iz620_00', 6)
    ParticleColorFromPalette(64, 65, 66)
    ParticleSize(300)
    CallCustomizableParticle('izef_timeout', 0)
    Voiceline('iz411')
    sprite('iz620_01', 6)
    ParticleColorFromPalette(64, 65, 66)
    ParticleSize(300)
    CallCustomizableParticle('izef_timeout', 0)
    sprite('iz620_02', 6)
    ParticleColorFromPalette(64, 65, 66)
    ParticleSize(300)
    CallCustomizableParticle('izef_timeout', 0)
    sprite('iz620_03', 6)
    sprite('iz620_04', 6)
    sprite('iz620_05', 6)
    sprite('iz620_06', 6)
    sprite('iz620_07', 6)
    sprite('iz620_08', 32767)
    DemoTimer(90)


@State
def EventDefEntryWait():
    label(0)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
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
    sprite('iz063_11', 32767)


@State
def EventEntryStand():
    label(0)
    sprite('iz601_00', 6)
    sprite('iz601_01', 6)
    sprite('iz601_02', 6)
    sprite('iz601_03', 6)
    loopRest()
    gotoLabel(0)


@State
def EventEntryStandToPrepare():
    sprite('iz601_04', 5)
    sprite('iz601_05', 5)
    sprite('iz601_06', 6)
    enterState('EventEntryStandToPrepare2')


@State
def EventEntryStand2():
    sprite('iz601_04', 6)
    sprite('iz601_05', 6)
    sprite('iz601_06', 32767)
    loopRest()


@State
def EventEntryStandToPrepare2():
    sprite('iz601_07', 60)
    CreateObject('EntryFallSword', -1)
    CommonSE('011_spin_0')
    CommonSE('005_swing_grap_2_2')
    CreateParticle('izef_entrylightB', 0)
    sprite('iz601_08', 7)
    sprite('iz601_09', 7)
    CreateObject('iz601amourlight', -1)
    CommonSE('022_magiccircle_a')
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_10', 7)
    sprite('iz601_11', 7)
    sprite('iz601_12', 7)
    sprite('iz601_13', 7)
    sprite('iz601_14', 7)
    sprite('iz601_15', 7)
    sprite('iz601_16', 7)
    sprite('iz601_17', 7)
    CreateParticle('izef_armchange', 0)
    sprite('iz601_18', 7)
    CreateObject('iz601swdlight', -1)
    sprite('iz601_19', 7)
    sprite('iz601_20', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventExcite():
    sprite('iz300_00', 4)
    sprite('iz300_01', 4)
    sprite('iz300_02', 4)
    sprite('iz300_03', 4)
    PrivateSE('izse_01')
    sprite('iz300_04', 10)
    sprite('iz300_05', 6)
    sprite('iz300_06', 6)
    sprite('iz300_07', 6)
    sprite('iz300_08', 30)
    sprite('iz300_09', 8)
    sprite('iz300_10', 6)
    sprite('iz300_11', 6)
    sprite('iz300_12', 4)
    enterState('CmnActStand')


@State
def EventEntryVsRCWait():
    sprite('iz000_00', 7)
    CreateObject('EventJNVsRCDownLoop', 0)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventJNWarp():
    sprite('keep', 1)
    ObjectUpon(STATE_END, 32)
    loopRest()
    enterState('CmnActStand')


@State
def EventEntryVSJN():
    sprite('null', 1)
    CreateObject('EventTBYoroke', 0)
    sprite('null', 32767)


@State
def EventEntryVSJN2():
    sprite('iz000_00', 7)
    ObjectUpon(STATE_END, 32)
    enterState('CmnActStand')


@State
def EventEntryChangeIZWait():
    sprite('iz600_00', 32767)


@State
def EventEntryChangeIZ():
    sprite('iz600_00', 6)
    sprite('iz600_01', 5)
    sprite('iz600_02', 5)
    sprite('iz600_03', 6)
    CreateParticle('izef_entryhane', -1)
    CreateParticle('izef_entrymcB', -1)
    CommonSE('019_cloth_c')
    sprite('iz600_04', 6)
    sprite('iz600_05', 6)
    sprite('iz600_06', 6)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 18)
    sprite('iz600_07', 6)
    sprite('iz600_07ex00', 6)
    sprite('iz600_08', 6)
    sprite('iz600_09', 6)
    CharacterFlash2(0, 6)
    CommonSE('022_magiccircle_b')
    sprite('iz600_10', 7)
    StopCharacterFlash2()
    sprite('iz600_11', 7)
    sprite('iz600_12', 7)
    sprite('iz600_13', 6)
    sprite('iz600_14', 6)
    sprite('iz600_15', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventNYvsIZDash():
    RunLoopUpon(17, 40)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('iz032_00', 2)
    physicsXImpulse(24000)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    CameraControlEnable(1)
    label(0)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz032_09', 3)
    physicsXImpulse(40)
    sprite('iz032_10', 3)
    physicsXImpulse(40)
    sprite('iz032_11', 3)
    physicsXImpulse(40)
    loopRest()
    label(2)
    sprite('iz000_00', 7)
    physicsXImpulse(0)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(2)


@State
def EventIZWin():
    sprite('iz610_00', 7)
    sprite('iz610_01', 7)
    sprite('iz610_02', 7)
    sprite('iz610_03', 7)
    label(0)
    sprite('iz610_04', 7)
    sprite('iz610_05', 7)
    sprite('iz610_06', 7)
    sprite('iz610_07', 7)
    sprite('iz610_08', 7)
    loopRest()
    gotoLabel(0)


@State
def EventIZWinEnd():
    sprite('iz610_03', 7)
    sprite('iz610_02', 7)
    sprite('iz610_01', 7)
    sprite('iz610_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventStandTurn():
    sprite('iz003_00', 3)
    Flip()
    sprite('iz003_01', 3)
    sprite('iz003_02', 3)
    loopRest()
    label(0)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    sprite('iz000_00', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDashScreenOut():
    SLOT_51 = 0
    sprite('iz032_01', 4)
    Flip()
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(30000)

    def upon_EVERY_FRAME():
        if SLOT_51 > 1:
            sendToLabel(1)
    label(0)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    loopRest()
    SLOT_51 = SLOT_51 + 1
    gotoLabel(0)
    label(1)
    sprite('null', 32767)


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventIZvsRGIai_Slash():

    def upon_IMMEDIATE():
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
    sprite('iz402_00', 2)
    EnableAfterimage(1)
    sprite('iz402_01', 1)
    sprite('iz402_01', 1)
    sprite('iz402_02', 3)
    PrivateSE('izse_03_start')
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    label(0)
    sprite('iz402_05', 2)
    ObjectUpon(22, 32)
    EndSE()
    CommonSE('010_swing_sword_2')
    PrivateSE('izse_01')
    CreateObject('Iai_SlashZanzo00', -1)
    TriggerUponForState('Iaimcircle', 33)
    DeleteObject(6)
    DeleteObject(7)
    WhiffCancelEnable(0)
    sprite('iz402_06', 3)
    sprite('iz402_07', 3)
    sprite('iz402_08', 4)
    sprite('iz402_09', 4)
    sprite('iz402_10', 4)
    label(1)
    EndSE()
    EnableAfterimage(0)
    sprite('iz402_11', 3)
    sprite('iz402_12', 3)
    sprite('iz402_13', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventExciteLoop():
    sprite('iz300_00', 4)
    sprite('iz300_01', 4)
    sprite('iz300_02', 4)
    sprite('iz300_03', 4)
    PrivateSE('izse_01')
    sprite('iz300_04', 10)
    sprite('iz300_05', 32767)


@State
def EventExciteLoopEnd():
    sprite('iz300_09', 8)
    sprite('iz300_10', 6)
    sprite('iz300_11', 6)
    sprite('iz300_12', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventYorokeLose():
    sprite('iz070_03', 32767)


@State
def EventYorokeLoseDown():
    sprite('iz070_04', 6)
    sprite('iz070_05', 6)
    sprite('iz070_06', 6)
    sprite('iz070_07', 6)
    sprite('iz070_08', 6)
    sprite('iz070_09', 6)
    sprite('iz063_11', 32767)


@State
def Act2Event_Chouhatsu():
    sprite('iz300_00', 6)
    sprite('iz300_01', 6)
    sprite('iz300_02', 6)
    sprite('iz300_03', 8)
    PrivateSE('izse_01')
    sprite('iz300_04', 4)
    sprite('iz300_05', 4)
    sprite('iz300_06', 6)
    sprite('iz300_07', 6)
    sprite('iz300_08', 6)
    sprite('iz300_09', 6)
    sprite('iz300_10', 6)
    sprite('iz300_11', 6)
    sprite('iz300_12', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RoundWin():
    sprite('iz615_00', 6)
    sprite('iz615_01', 6)
    sprite('iz615_02', 6)
    sprite('iz615_03', 6)
    sprite('iz615_04', 6)
    sprite('iz615_05', 6)
    sprite('iz615_06', 6)
    sprite('iz615_07', 6)
    PrivateSE('izse_01')
    sprite('iz615_08', 32767)


@State
def Act2Event_RoundWinEnd():
    sprite('iz615_08', 5)
    sprite('iz615_07', 5)
    sprite('iz615_06', 5)
    sprite('iz615_05', 5)
    sprite('iz615_04', 5)
    sprite('iz615_03', 5)
    sprite('iz615_02', 5)
    sprite('iz615_01', 5)
    sprite('iz615_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_01():
    sprite('iz001_00', 7)
    sprite('iz001_01', 7)
    sprite('iz001_02', 7)
    sprite('iz001_03', 7)
    PrivateSE('izse_01')
    sprite('iz001_04', 7)
    sprite('iz001_05', 7)
    sprite('iz001_06', 7)
    sprite('iz001_07', 7)
    sprite('iz001_08', 7)
    sprite('iz001_09', 7)
    sprite('iz001_10', 7)
    sprite('iz001_11', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_01_Loop():
    sprite('iz001_00', 7)
    sprite('iz001_01', 7)
    sprite('iz001_02', 7)
    sprite('iz001_03', 7)
    PrivateSE('izse_01')
    label(0)
    sprite('iz001_04', 7)
    sprite('iz001_05', 7)
    sprite('iz001_06', 7)
    sprite('iz001_07', 7)
    sprite('iz001_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Reaction_01_End():
    sprite('iz001_09', 7)
    sprite('iz001_10', 7)
    sprite('iz001_11', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_izvsha_Yure():
    sprite('iz001_09', 7)
    CreateObject('Act2Event_Yure', -1)
    sprite('iz001_10', 7)
    sprite('iz001_11', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_02():
    sprite('iz002_00', 6)
    sprite('iz002_01', 6)
    sprite('iz002_02', 6)
    sprite('iz002_03', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_04', 6)
    sprite('iz002_05', 6)
    sprite('iz002_06', 6)
    sprite('iz002_07', 6)
    sprite('iz002_08', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_09', 6)
    sprite('iz002_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_03_1():
    sprite('iz002_11', 4)
    sprite('iz002_12', 4)
    PrivateSE('izse_01')
    sprite('iz002_13', 4)
    sprite('iz002_14', 4)
    sprite('iz002_15', 5)
    sprite('iz002_16', 5)
    sprite('iz002_17', 5)
    sprite('iz002_18', 5)
    sprite('iz002_19', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_03_2():
    sprite('iz002_11', 4)
    sprite('iz002_12', 4)
    PrivateSE('izse_01')
    sprite('iz002_13', 4)
    sprite('iz002_14', 4)
    sprite('iz002_15', 5)
    sprite('iz002_16', 5)
    sprite('iz002_17', 5)
    sprite('iz002_12', 4)
    PrivateSE('izse_01')
    sprite('iz002_13', 4)
    sprite('iz002_14', 4)
    sprite('iz002_15', 5)
    sprite('iz002_16', 5)
    sprite('iz615_00', 6)
    sprite('iz615_01', 6)
    sprite('iz615_02', 6)
    sprite('iz615_03', 6)
    sprite('iz615_04', 6)
    sprite('iz615_05', 6)
    sprite('iz615_06', 6)
    sprite('iz615_07', 6)
    PrivateSE('izse_01')
    sprite('iz615_08', 32767)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Reaction_04():
    sprite('iz002_20', 7)
    sprite('iz002_21', 7)
    sprite('iz002_22', 7)
    sprite('iz002_23', 7)
    sprite('iz002_24', 7)
    sprite('iz002_25', 7)
    sprite('iz002_26', 7)
    sprite('iz002_27', 7)
    sprite('iz002_28', 7)
    sprite('iz002_29', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_odoroku():
    sprite('iz033_00', 7)
    sprite('iz033_05', 7)
    LandingEffects(100, 1, 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RunningEntry():
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
    sprite('iz032_01', 4)
    physicsXImpulse(20000)
    label(0)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    DashEffects(100, 1, 1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act2Event_izvsha_00():
    sprite('iz002_11', 4)
    PrivateSE('izse_05')
    AddX(230000)
    sprite('iz002_12', 4)
    PrivateSE('izse_01')
    sprite('iz002_13', 8)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('104_guard_grap_2')
    CommonSE('301_overdrive_end')
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_1')
    ScreenShake(10000, 50000)
    sprite('iz002_14', 2)
    AddInertia(-25000)
    sprite('iz002_15', 2)
    sprite('iz002_16', 2)
    sprite('iz002_17', 2)
    sprite('iz002_12', 2)
    PrivateSE('izse_01')
    sprite('iz002_13', 2)
    sprite('iz002_14', 2)
    sprite('iz002_15', 2)
    sprite('iz002_16', 2)
    sprite('iz002_17', 2)
    sprite('iz002_12', 2)
    PrivateSE('izse_01')
    sprite('iz002_13', 2)
    sprite('iz002_14', 2)
    sprite('iz002_15', 2)
    sprite('iz002_16', 2)
    sprite('iz002_17', 2)
    sprite('iz002_12', 2)
    EndMomentum(1)
    PrivateSE('izse_01')
    sprite('iz002_13', 2)
    sprite('iz002_14', 2)
    sprite('iz002_15', 2)
    sprite('iz002_16', 2)
    sprite('iz002_17', 5)
    sprite('iz002_18', 5)
    sprite('iz002_19', 5)
    loopRest()
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_izvshz_00():
    sprite('iz202_00', 3)
    sprite('iz202_01', 3)
    sprite('iz202_02', 3)
    PrivateSE('izse_01')
    sprite('iz202_03', 2)
    CommonSE('008_swing_pole_2')
    sprite('iz202_04', 15)
    sprite('iz202_05', 3)
    sprite('iz202_06', 2)
    sprite('iz202_07', 3)
    sprite('iz202_08', 3)
    sprite('iz202_09', 3)
    sprite('iz202_10', 3)
    sprite('iz202_11', 3)
    sprite('iz202_12', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_izvshz_01():
    sprite('iz032_00', 3)
    physicsXImpulse(24000)
    sprite('iz032_01', 3)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 3)
    sprite('iz032_09', 4)
    physicsXImpulse(0)
    SetInertia(10000)
    sprite('iz032_10', 4)
    sprite('iz032_11', 4)
    loopRest()
    EndMomentum(1)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz003_00', 4)
    Flip()
    sprite('iz003_01', 4)
    sprite('iz003_02', 4)
    label(0)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_izvshz_02():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('iz032_00', 2)
    physicsXImpulse(24000)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    SetActionMark(3)
    label(0)
    sprite('iz032_04', 4)
    AddActionMark(-1)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('null', 2)
    EndMomentum(1)
    Visibility(1)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_mkvsiz_00():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        StayAfterMovement(1, 0)
        uponSendToLabel(32, 0)

        def upon_STATE_END():
            EndSE()
    sprite('iz402_00', 4)
    sprite('iz402_01', 4)
    sprite('iz402_02', 4)
    PrivateSE('izse_03_start')
    CreateObject('Iaimcircle', -1)
    CreateObject('Iai_hold', 100)
    RegisterObject(6, 1)
    CreateObject('Iai_hold_add', 100)
    RegisterObject(7, 1)
    sprite('iz402_03', 3)
    sprite('iz402_04', 3)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    sprite('iz402_03', 4)
    SpecialSE('izse_03_loop')
    sprite('iz402_04', 4)
    label(9)
    sprite('iz402_03', 4)
    sprite('iz402_04', 4)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('iz402_05', 2)
    EndSE()
    CommonSE('010_swing_sword_2')
    PrivateSE('izse_01')
    CreateObject('Iai_SlashZanzo00', -1)
    TriggerUponForState('Iaimcircle', 33)
    DeleteObject(6)
    DeleteObject(7)
    sprite('iz402_06', 15)
    sprite('iz402_07', 3)
    sprite('iz402_08', 4)
    sprite('iz402_09', 4)
    sprite('iz402_10', 4)
    sprite('iz402_11', 4)
    sprite('iz402_12', 4)
    sprite('iz402_13', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvsiz_01():
    sprite('iz002_20', 7)
    sprite('iz002_21', 7)
    sprite('iz002_22', 7)
    sprite('iz002_23', 7)
    sprite('iz002_24', 7)
    sprite('iz002_25', 7)
    sprite('iz002_26', 7)
    sprite('iz002_27', 7)
    sprite('iz002_28', 7)
    sprite('iz002_29', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvsiz_02():
    sprite('iz431_00', 4)
    sprite('iz431_01', 4)
    sprite('iz431_02', 4)
    sprite('iz431_03', 4)
    sprite('iz431_04', 4)
    sprite('iz431_05', 4)
    sprite('iz431_06', 4)
    sprite('iz431_07', 4)
    sprite('iz431_08', 4)
    sprite('iz431_09', 4)
    sprite('iz431_10', 32767)


@State
def Act3Event_mkvsiz_03():
    sprite('iz431_11', 4)
    sprite('iz431_12', 4)
    sprite('iz431_13', 4)
    sprite('iz431_14', 5)
    PrivateSE('izse_07')
    CreateParticle('GNptcCharget', 0)
    CreateParticle('GNptcCharget', 1)
    sprite('iz431_15', 6)
    sprite('iz431_16', 7)
    sprite('iz431_17', 30)
    sprite('iz431_18', 2)
    sprite('iz431_19', 4)
    ScreenShake(2000, 60000)
    CreateObject('SummonFunnelF', -1)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_24', 4)
    sprite('iz431_25', 4)
    sprite('iz431_26', 4)
    sprite('iz431_27', 4)
    sprite('iz431_28', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_amvsiz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(200000)
    sprite('iz070_00', 4)
    CommonSE('104_guard_grap_1')
    ScreenShake(3000, 18000)
    AddInertia(-40000)
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_1')
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    sprite('iz070_01', 4)
    sprite('iz070_02', 4)
    sprite('iz070_03', 32767)
    loopRest()


@State
def Act3Event_amvsiz_01():
    sprite('iz070_04', 6)
    EndMomentum(1)
    sprite('iz070_05', 6)
    sprite('iz070_06', 6)
    sprite('iz070_07', 6)
    sprite('iz070_08', 6)
    sprite('iz070_09', 6)
    sprite('iz063_11', 32767)
    KnockdownEffects(100, 1, 1)
    AddX(50000)


@State
def Act3Event_amvsiz_02():
    sprite('iz063_11', 40)
    ObjectUpon(22, 32)
    sprite('null', 32767)
    CreateObject('Act3Event_IZDummy', -1)
    AddX(900000)
    Visibility(1)


@State
def Act3Event_izvsno_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-1200000)
        ScreenCollision(0)
        EnableCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 360000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage > -360000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
    sprite('iz032_00', 2)
    physicsXImpulse(24000)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    label(0)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz032_09', 3)
    physicsXImpulse(0)
    DashEffects(100, 1, 1)
    AddInertia(5000)
    sprite('iz032_10', 3)
    sprite('iz032_11', 3)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_izvsno_01():
    sprite('iz431_10', 22)
    sprite('iz431_11', 4)
    sprite('iz431_12', 4)
    sprite('iz431_13', 4)
    sprite('iz431_14', 5)
    PrivateSE('izse_07')
    CreateParticle('GNptcCharget', 0)
    CreateParticle('GNptcCharget', 1)
    sprite('iz431_15', 6)
    sprite('iz431_16', 7)
    sprite('iz431_17', 30)
    sprite('iz431_18', 2)
    sprite('iz431_19', 4)
    ScreenShake(2000, 60000)
    CreateObject('SummonFunnelF', -1)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_23', 3)
    sprite('iz431_20', 3)
    sprite('iz431_21', 3)
    sprite('iz431_22', 3)
    sprite('iz431_24', 4)
    sprite('iz431_25', 4)
    sprite('iz431_26', 4)
    sprite('iz431_27', 4)
    sprite('iz431_28', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_izvsno_02():
    sprite('iz032_00', 2)
    physicsXImpulse(24000)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    sprite('iz010_00', 4)
    physicsXImpulse(0)
    sprite('iz010_01', 4)
    label(0)
    sprite('iz010_02', 7)
    sprite('iz010_03', 7)
    sprite('iz010_04', 7)
    sprite('iz010_05', 7)
    sprite('iz010_06', 7)
    sprite('iz010_07', 7)
    sprite('iz010_08', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_izvsno_03():
    sprite('iz010_01', 4)
    sprite('iz010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_izvsha_00():
    sprite('iz602_00', 32767)
    loopRest()


@State
def Act3Event_izvsha_01():
    sprite('iz602_01', 6)
    sprite('iz602_02', 6)
    sprite('iz602_03', 6)
    sprite('iz602_04', 6)
    sprite('iz602_05', 6)
    sprite('iz602_06', 6)
    sprite('iz602_07', 6)
    sprite('iz602_08', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_esvsiz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-1200000)
        ScreenCollision(0)
        EnableCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 360000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage > -360000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
    sprite('iz032_00', 2)
    physicsXImpulse(24000)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    label(0)
    sprite('iz032_04', 4)
    sprite('iz032_05', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_06', 4)
    sprite('iz032_07', 4)
    sprite('iz032_08', 4)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_02', 4)
    sprite('iz032_03', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz032_09', 3)
    physicsXImpulse(0)
    DashEffects(100, 1, 1)
    AddInertia(10000)
    sprite('iz032_10', 4)
    sprite('iz032_11', 4)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_esvsiz_01():
    EnableCollision(0)
    AttackOff()

    def upon_STATE_END():
        CameraControlEnable(0)
    label(0)
    CameraControlEnable(1)
    XPositionRelativeFacing(-500000)
    AbsoluteY(200000)
    sprite('iz413_02', 1)
    sprite('iz413_05', 2)
    PrivateSE('izse_01')
    sprite('iz413_06', 2)
    CommonSE('010_swing_sword_2')
    CreateObject('izef_413_a', -1)
    sprite('iz413_07', 3)
    CommonSE('100_hit_grap_3')
    sprite('iz413_08', 1)
    sprite('iz413_09', 1)
    CommonSE('105_guard_slash_0')
    loopRest()
    sprite('iz252_01', 1)
    sprite('iz252_02', 2)
    PrivateSE('izse_01')
    CommonSE('008_swing_pole_2')
    sprite('iz252_03', 2)
    sprite('iz252_04', 3)
    CommonSE('101_hit_slash_1')
    sprite('iz252_06', 1)
    sprite('iz252_07', 1)
    CommonSE('105_guard_slash_1')
    loopRest()
    sprite('iz409_00', 2)
    sprite('iz409_01', 2)
    sprite('iz409_02', 2)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    sprite('iz409_02', 2)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_03', 2)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    loopRest()
    label(1)
    sprite('null', 5)
    CameraControlEnable(0)
    XPositionRelativeFacing(200000)
    AbsoluteY(700000)
    sprite('iz409_03', 2)
    CreateObject('firespark', 0)
    ConstantAlphaModifier(60)
    sprite('iz409_04', 2)
    sprite('iz409_05', 2)
    loopRest()
    sprite('iz201_03', 1)
    sprite('iz201_04', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('iz201_05', 3)
    CommonSE('100_hit_grap_2')
    sprite('iz201_06', 2)
    sprite('iz201_07', 2)
    sprite('iz201_08', 1)
    CommonSE('105_guard_slash_2')
    sprite('iz201_09', 1)
    loopRest()
    sprite('iz253_03', 1)
    PrivateSE('izse_08')
    CommonSE('008_swing_pole_2')
    sprite('iz253_04', 1)
    sprite('iz253_05', 2)
    sprite('iz253_06', 3)
    CommonSE('101_hit_slash_1')
    sprite('iz253_07', 2)
    sprite('iz253_08', 2)
    sprite('iz253_09', 1)
    CommonSE('105_guard_slash_1')
    sprite('iz253_10', 1)
    loopRest()
    sprite('iz409_00', 2)
    sprite('iz409_01', 2)
    sprite('iz409_02', 2)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    sprite('iz409_02', 2)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_03', 2)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    loopRest()
    label(2)
    sprite('null', 5)
    CameraControlEnable(1)
    XPositionRelativeFacing(-100000)
    AbsoluteY(1200000)
    sprite('iz409_03', 2)
    CreateObject('firespark', 0)
    ConstantAlphaModifier(60)
    sprite('iz409_04', 2)
    sprite('iz409_05', 2)
    loopRest()
    sprite('iz211_04', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('iz211_05', 1)
    sprite('iz211_06', 1)
    sprite('iz211_07', 1)
    sprite('iz211_08', 2)
    CommonSE('006_swing_blade_2')
    sprite('iz211_09', 3)
    CommonSE('100_hit_grap_2')
    sprite('iz211_10', 2)
    sprite('iz211_11', 1)
    CommonSE('105_guard_slash_0')
    sprite('iz211_12', 1)
    loopRest()
    sprite('iz203_01', 1)
    PrivateSE('izse_01')
    sprite('iz203_02', 2)
    sprite('iz203_03', 3)
    CommonSE('101_hit_slash_1')
    sprite('iz203_04', 1)
    sprite('iz203_05', 1)
    CommonSE('105_guard_slash_2')
    loopRest()
    sprite('iz409_00', 2)
    sprite('iz409_01', 2)
    sprite('iz409_02', 2)
    PrivateSE('izse_04')
    CreateObject('Warp_D_Land_Zanzo00', -1)
    CreateObject('Warp_D_Land_Zanzo01', -1)
    CreateObject('WarpEff', 0)
    CameraControlEnable(0)
    sprite('iz409_02', 2)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    sprite('iz409_03', 1)
    AlphaValue(0)
    CommonSE('001_airbackdash_0')
    loopRest()
    sprite('null', 32767)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    loopRest()


@State
def Act3Event_esvsiz_02():
    uponSendToLabel(32, 1)
    ScreenCollision(0)
    sprite('null', 1)
    sprite('iz409_03', 2)
    CreateObject('firespark', 0)
    ConstantAlphaModifier(60)
    sprite('iz409_04', 2)
    sprite('iz409_05', 3)
    sprite('iz409_06', 5)
    sprite('iz409_07', 6)
    sprite('iz409_08', 6)
    sprite('iz409_09', 6)
    loopRest()
    label(0)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz070_00', 4)
    CommonSE('104_guard_grap_1')
    ScreenShake(20000, 20000)
    AddInertia(-200000)
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_1')
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    sprite('iz070_01', 4)
    ScreenShake(10000, 10000)
    CommonSE('001_airbackdash_1')
    sprite('iz070_02', 4)
    ScreenShake(5000, 5000)
    sprite('iz070_03', 20)
    sprite('iz070_03', 32767)
    EndMomentum(1)
    CommonSE('213_bound_0')
    if SLOT_IsFacingRight:
        XPositionRelativeFacingAbsolute(1550000)
    else:
        XPositionRelativeFacingAbsolute(-1550000)
    loopRest()


@State
def Act3Event_esvsiz_03():
    sprite('iz070_02', 3)
    AddX(500)
    ScreenCollision(0)
    sprite('iz070_02', 3)
    AddX(-500)
    sprite('iz070_01', 3)
    AddX(500)
    sprite('iz070_01', 3)
    AddX(-500)
    sprite('iz070_00', 3)
    AddX(500)
    sprite('iz070_00', 3)
    AddX(-500)
    loopRest()
    label(0)
    sprite('iz000_00', 7)
    sprite('iz000_01', 7)
    sprite('iz000_02', 7)
    sprite('iz000_03', 7)
    sprite('iz000_04', 7)
    sprite('iz000_05', 7)
    sprite('iz000_06', 7)
    sprite('iz000_07', 7)
    sprite('iz000_08', 7)
    sprite('iz000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_esvsiz_04():
    sprite('iz615_00', 6)
    ScreenCollision(0)
    sprite('iz615_01', 6)
    sprite('iz615_02', 6)
    sprite('iz615_03', 6)
    sprite('iz615_04', 6)
    sprite('iz615_05', 6)
    sprite('iz615_06', 6)
    sprite('iz615_07', 6)
    PrivateSE('izse_01')
    sprite('iz615_08', 32767)


@State
def Act3Event_esvsiz_90():

    def upon_IMMEDIATE():
        AddX(70000)
        NoAttackDuringAction(1)
    sprite('iz040_02', 3)
    sprite('iz040_03', 3)
    sprite('iz040_04', 3)
    sprite('iz090_00', 16)
    sprite('iz090_00', 4)
    AddInertia(-8000)
    sprite('iz070_01', 4)
    sprite('iz070_02', 6)
    sprite('iz070_03', 32767)
    loopRest()


@State
def Act3Event_esvsiz_91():
    sprite('iz070_10', 4)
    sprite('iz070_11', 4)
    sprite('iz070_12', 4)
    sprite('iz070_13', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_esvsiz_92():
    sprite('iz032_00', 3)
    physicsXImpulse(12000)
    sprite('iz032_01', 4)
    DashEffects(100, 1, 1)
    sprite('iz032_09', 3)
    physicsXImpulse(0)
    DashEffects(100, 1, 1)
    AddInertia(10000)
    sprite('iz032_10', 4)
    sprite('iz032_11', 4)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')
