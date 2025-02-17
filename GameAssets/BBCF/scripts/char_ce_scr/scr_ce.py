@Subroutine
def PreInit():
    CharacterID('ce')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(10000)
    WalkFSpeed(6200)
    WalkBSpeed(4800)
    DashFInitialVelocity(16000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(42000)
    AirDashFSpeed(28000)
    AirFDashDuration(20)
    AirDashBSpeed(23000)
    AirBDashDuration(20)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(1)
    FootstepSE(0)
    CreateDecalOn(1)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5AAdd', 0x1)
    SharedGatling('NmlAtk5A')
    Move_Input_(INPUT_HOLD_A)
    FollowupOnly(1)
    SkillEstimateRange(0, 250000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    MoveLow()
    SkillEstimateRange(0, 400000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 250000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2AAdd', 0x1)
    SharedGatling('NmlAtk2A')
    Move_Input_(0x45)
    Move_Input_(INPUT_HOLD_A)
    FollowupOnly(1)
    SkillEstimateRange(0, 250000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    SkillEstimateRange(-100000, 300000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    MoveCancellableFrames(11, 12)
    SkillEstimateRange(-100000, 350000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    SkillEstimateRange(0, 450000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    SkillEstimateRange(0, 400000, -200000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    SkillEstimateRange(-100000, 400000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk3C_Chain', INPUT_3C)
    SharedGatling('NmlAtk3C')
    FollowupOnly(1)
    MoveLow()
    SkillEstimateRange(-100000, 400000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    SkillEstimateRange(-50000, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5DD', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    DamageStunPriority(2000)
    SkillEstimateRange(-250000, 550000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5DDD', 0x1)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    SkillEstimateRange(-250000, 350000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    SkillEstimateRange(-50000, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk6DD', 0x1)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(-250000, 500000, -200000, 250000, 750, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk6DD_Input4', 0x1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AN_NmlAtk6DD')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk6DD_Input7', 0x1)
    Move_Input_(0x85)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AN_NmlAtk6DD')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk6DD_Input9', 0x1)
    Move_Input_(0x9f)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AN_NmlAtk6DD')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    MoveLow()
    SkillEstimateRange(-50000, 450000, -100000, 150000, 750, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2DD', 0x1)
    Move_Input_(0x44)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    MoveLow()
    SkillEstimateRange(-250000, 450000, -200000, 250000, 750, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2DD_Input1', 0x1)
    Move_Input_(0x37)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AN_NmlAtk2DD')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2DD_Input3', 0x1)
    Move_Input_(0x51)
    Move_Input_(INPUT_PRESS_D)
    FollowupOnly(1)
    StateCall('AN_NmlAtk2DD')
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(1)
    SkillEstimateRange(-50000, 250000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5AAdd', 0x1)
    Move_Input_(INPUT_HOLD_A)
    FollowupOnly(1)
    DamageStunPriority(1)
    SkillEstimateRange(-50000, 250000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(-50000, 250000, -350000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SkillEstimateRange(-50000, 450000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    SkillEstimateRange(-150000, 350000, -350000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(4000)
    SkillEstimateRange(0, 250000, -200000, 200000, 250, 0)
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
    SkillEstimateRange(0, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckShotAvailable')
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(1)
    Unknown15027(0)
    GuardStunPriority(1500)
    JumpAvoidPriority(10000)
    SkillEstimateRange(650000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(1)
    OpponentAttackPriority(1)
    AirborneOpponentPriority(1)
    SkillEstimateRange(450000, 900000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(3000)
    SkillEstimateRange(-50000, 300000, -200000, 400000, 500, 10)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    MoveMid()
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(1)
    SkillEstimateRange(150000, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(-50000, 250000, -350000, 150000, 500, 50)
    Move_EndRegister()
    Move_Register('UltimateHeal', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(1200000, 1500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateHealOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3081)
    SkillEstimateRange(1200000, 1500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(2000)
    SkillEstimateRange(250000, 750000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShotOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3081)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(2000)
    SkillEstimateRange(250000, 750000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 450000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_222)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(1)
    GuardStunPriority(1)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)
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
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk5D', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'Assault', 10000000)
    TempPriorityMultiplier('AN_NmlAtk5DDD', 'Shot', 10000000)
    TempPriorityMultiplier('AN_NmlAtk5DDD', 'Assault', 10000000)
    TempPriorityMultiplier('AN_NmlAtk5DDD', 'AntiAir', 10000000)
    TempPriorityMultiplier('AN_NmlAtk5DDD', 'MidAssault', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirAssault', 10000000)
    StylishModeSpecialButton('AntiAir', 0x4, 0xea)
    StylishModeSpecialButton('Shot', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('MidAssault', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk5C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D', 1, 260000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk5C', 'Assault', 12, 0)
    StylishModeCancels('NmlAtk5C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk5D', 'AN_NmlAtk5DD', 0, 0)
    StylishModeCancels('AN_NmlAtk5DD', 'AN_NmlAtk5DDD', 0, 0)
    StylishModeCancels('AN_NmlAtk5DDD', 'UltimateShot', 6, 0)
    StylishModeCancels('AN_NmlAtk5DDD', 'UltimateShotOD', 6, 0)
    StylishModeCancels('AN_NmlAtk5DDD', 'MidAssault', 10, 700000)
    StylishModeCancels('AN_NmlAtk5DDD', 'AstralHeat', 10, 700000)
    StylishModeCancels('AN_NmlAtk5DDD', 'AN_NmlAtk5DDD', 12, 0)
    StylishModeCancels('AN_NmlAtk5DDD', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk2C', 0, 0)
    StylishModeCancels('NmlAtk6C', 'FHighJump', 6, 0)
    StylishModeCancels('NmlAtk6C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk6D', 'AN_NmlAtk6DD', 0, 0)
    StylishModeCancels('AN_NmlAtk6DD', 'AN_NmlAtk5DDD', 0, 0)
    StylishModeCancels('ThrowExe', 'Assault', 0, 0)
    StylishModeCancels('BackThrowExe', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk2C', 1, 400000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk2C', 'Assault', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk3C', 1, 300000)
    StylishModeCancels('NmlAtk2C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk3C', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk2D', 'AN_NmlAtk2DD', 0, 0)
    StylishModeCancels('AN_NmlAtk2DD', 'AN_NmlAtk5DDD', 0, 0)
    StylishModeCancels('AN_NmlAtk2DD', 'MidAssault', 10, 700000)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirAssault', 3, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 13, 0)
    StylishModeCancels('NmlAtkAIR5D', 'AN_NmlAtk5DD', 0, 0)
    StylishModeCancels('NmlAtkAIR5D', 'AN_NmlAtk2DD', 10, 700000)
    HitSprites(0, 'ce062_01')
    HitSprites(1, 'ce062_03')
    HitSprites(2, 'ce062_04')
    HitSprites(3, 'ce062_05')
    HitSprites(4, 'ce062_05')
    HitSprites(5, 'ce062_06')
    HitSprites(6, 'ce062_07')
    HitSprites(7, 'ce041_02')
    HitSprites(8, 'ce040_02')
    HitSprites(9, 'ce045_02')
    HitSprites(10, 'ce060_00')
    HitSprites(11, 'ce060_01')
    HitSprites(12, 'ce060_03')
    HitSprites(13, 'ce060_05')
    HitSprites(14, 'ce060_07')
    HitSprites(15, 'ce060_14')
    HitSprites(16, 'ce050_00')
    HitSprites(17, 'ce052_00')
    HitSprites(18, 'ce054_00')
    HitSprites(19, 'ce000_00')
    HitSprites(20, 'ce000_00')
    HitSprites(25, 'ce063_00')
    HitSprites(26, 'ce063_01')
    HitSprites(27, 'ce063_02')
    HitSprites(28, 'ce063_04')
    HitSprites(29, 'ce063_10')
    HitSprites(30, 'ce077_00')
    HitSprites(31, 'ce077_01')
    HitSprites(32, 'ce077_00ex01')
    HitSprites(33, 'ce077_01ex01')
    HitSprites(34, 'ce077_00ex02')
    HitSprites(35, 'ce077_01ex02')
    HitSprites(36, 'ce077_00ex03')
    HitSprites(37, 'ce077_01ex03')
    HitSprites(24, 'ce073_01')
    CommonVoicelines(0, 'ce000')
    CommonVoicelines(1, 'ce001')
    CommonVoicelines(2, 'ce002')
    CommonVoicelines(3, 'ce003')
    CommonVoicelines(4, 'ce004')
    CommonVoicelines(5, 'ce005')
    CommonVoicelines(6, 'ce006')
    CommonVoicelines(7, 'ce007')
    CommonVoicelines(8, 'ce008')
    CommonVoicelines(9, 'ce009')
    CommonVoicelines(10, 'ce010')
    CommonVoicelines(11, 'ce011')
    CommonVoicelines(12, 'ce012')
    CommonVoicelines(13, 'ce013')
    CommonVoicelines(14, 'ce014')
    CommonVoicelines(15, 'ce015')
    CommonVoicelines(16, 'ce016')
    CommonVoicelines(17, 'ce017')
    CommonVoicelines(18, 'ce018')
    CommonVoicelines(19, 'ce019')
    CommonVoicelines(20, 'ce020')
    CommonVoicelines(21, 'ce021')
    CommonVoicelines(22, 'ce022')
    CommonVoicelines(23, 'ce023')
    CommonVoicelines(24, 'ce024')
    CommonVoicelines(25, 'ce025')
    CommonVoicelines(26, 'ce026')
    CommonVoicelines(27, 'ce027')
    CommonVoicelines(28, 'ce028')
    CommonVoicelines(29, 'ce029')
    CommonVoicelines(30, 'ce030')
    CommonVoicelines(31, 'ce031')
    CommonVoicelines(32, 'ce032')
    CommonVoicelines(33, 'ce033')
    CommonVoicelines(34, 'ce034')
    CommonVoicelines(35, 'ce035')
    CommonVoicelines(36, 'ce036')
    CommonVoicelines(37, 'ce037')
    CommonVoicelines(38, 'ce038')
    CommonVoicelines(39, 'ce039')
    CommonVoicelines(40, 'ce040')
    CommonVoicelines(41, 'ce041')
    CommonVoicelines(42, 'ce042')
    CommonVoicelines(43, 'ce043')
    CommonVoicelines(44, 'ce044')
    CommonVoicelines(45, 'ce045')
    CommonVoicelines(46, 'ce046')
    CommonVoicelines(47, 'ce047')
    CommonVoicelines(48, 'ce048')
    CommonVoicelines(49, 'ce049')
    CommonVoicelines(50, 'ce050')
    CommonVoicelines(51, 'ce051')
    CommonVoicelines(52, 'ce052')
    CommonVoicelines(53, 'ce053')
    CommonVoicelines(54, 'ce100')
    CommonVoicelines(55, 'ce101')
    CommonVoicelines(56, 'ce102')
    CommonVoicelines(57, 'ce103')
    CommonVoicelines(58, 'ce104')
    CommonVoicelines(59, 'ce105')
    CommonVoicelines(60, 'ce106')
    CommonVoicelines(61, 'ce107')
    CommonVoicelines(62, 'ce108')
    CommonVoicelines(63, 'ce109')
    CommonVoicelines(64, 'ce150')
    CommonVoicelines(65, 'ce151')
    CommonVoicelines(66, 'ce152')
    CommonVoicelines(67, 'ce153')
    CommonVoicelines(68, 'ce154')
    CommonVoicelines(69, 'ce155')
    CommonVoicelines(70, 'ce156')
    CommonVoicelines(71, 'ce157')
    CommonVoicelines(72, 'ce158')
    CommonVoicelines(75, 'ce160')
    CommonVoicelines(73, 'ce402')
    CommonVoicelines(74, 'ce403')
    CreateObject('MinervaCreate', -1)
    RegisterObject(11, 1)


@Subroutine
def CheckShotAvailable():
    SLOT_47 = 1
    if SLOT_5:
        SLOT_47 = 0


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnFrameStep():
    if CurrentStateCheck('RlAstralDamage'):
        EnableAfterimage(0)
        AfterimageType(0)
    if SLOT_21:
        if SLOT_IsInHitstun:
            SLOT_6 = 0
            if CurrentStateCheck('RlAstralDamage'):
                if SLOT_65 >= 2:
                    SLOT_4 = 1
        if SLOT_42:
            SLOT_6 = 0
    if SLOT_OverdriveTimer:
        if not SLOT_81:
            if not SLOT_IsInHitstun:
                if not SLOT_42:
                    SLOT_60 = SLOT_60 + 1
                    if not SLOT_CurrentHealth == SLOT_MaxHealth:
                        if SLOT_60 < 300:
                            AddToCurrentHP(2)
                        else:
                            AddToCurrentHP(3)
                    if not SLOT_60 % 20:
                        SLOT_8 = SLOT_8 + 100
    else:
        SLOT_60 = 0
    if SLOT_21:
        TrainingModeSLOT('TRI_CelicaPowerUp', 2, 67)
        if SLOT_67:
            if SLOT_InNeutral:
                SLOT_8 = 1
        else:
            PrivateFunction(1, 2, 76, 2, 75, 2, 7)
            if SLOT_8 > SLOT_7:
                SLOT_8 = SLOT_7
        if SLOT_8:
            SLOT_9 = 1
            if not CurrentStateCheck('UltimateAssault'):
                if not CurrentStateCheck('UltimateAssaultOD'):
                    if not CurrentStateCheck('AstralHeatExe'):
                        if SLOT_CurrentHealth:
                            if not SLOT_IsInHitstun:
                                if not SLOT_10:
                                    CreateObject('RecoveryCapa', 103)
        else:
            SLOT_9 = 0
    else:
        SLOT_8 = 0


@Subroutine
def OnActionBeginPre():
    SLOT_4 = 0


@Subroutine
def OnActionBegin():
    ObjectUpon2(11, 999, 0)


@Subroutine
def MinervaNoneCall():

    def upon_48():
        SLOT_65 = 0


@Subroutine
def MinervaCall():
    SLOT_4 = 1
    RunLoopUpon(17, 2)

    def upon_48():
        SLOT_65 = 2


@Subroutine
def MinervaCallAttack():
    SLOT_4 = 1
    RunLoopUpon(17, 2)

    def upon_48():
        SLOT_65 = 3


@Subroutine
def MinervaNoneCallAttack():

    def upon_48():
        SLOT_65 = 1


@Subroutine
def MinervaNoneReCall():
    SLOT_4 = 0
    clearUponHandler(48)

    def upon_48():
        SLOT_65 = 0


@State
def CmnActStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        StayAfterMovement(1, 0)
        ObjectUpon2(11, 100, 0)

        def upon_STATE_END():
            if SLOT_66:
                ObjectUpon2(11, 100, 0)
                SLOT_66 = 0
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    if CharacterIDCheck('rg'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(100)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(100)
    sprite('ce001_00', 6)
    SLOT_66 = 1
    ObjectUpon2(11, 112, 0)
    SLOT_88 = 960
    Voiceline('ce000')
    sprite('ce001_01', 6)
    sprite('ce001_02', 6)
    sprite('ce001_03', 6)
    sprite('ce001_04', 6)
    sprite('ce001_05', 6)
    label(9)
    sprite('ce001_06', 8)
    sprite('ce001_06ex00', 8)
    sprite('ce001_06ex01', 29)
    sprite('ce001_06', 8)
    sprite('ce001_06ex02', 8)
    sprite('ce001_06ex03', 29)
    gotoLabel(9)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('ce603_01', 6)
    SLOT_88 = 960
    Voiceline('ce000')
    sprite('ce603_00', 90)
    sprite('ce603_01', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 101, 0)
    sprite('ce003_00', 3)
    sprite('ce003_01', 3)
    sprite('ce003_00ex', 3)


@State
def CmnActStand2Crouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_00', 4)
    sprite('ce010_01', 4)


@State
def CmnActCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    label(0)
    sprite('ce010_02', 6)
    sprite('ce010_03', 6)
    sprite('ce010_04', 6)
    sprite('ce010_05', 6)
    sprite('ce010_06', 6)
    sprite('ce010_07', 6)
    sprite('ce010_08', 6)
    sprite('ce010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 101, 0)
    sprite('ce013_00', 3)
    sprite('ce013_01', 3)
    sprite('ce013_00ex', 3)


@State
def CmnActCrouch2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_01', 4)
    sprite('ce010_00', 4)


@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce023_00', 2)
    sprite('ce023_01', 2)


@State
def CmnActJumpUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce020_00', 4)
    sprite('ce020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_02', 3)
    sprite('ce020_03', 3)
    sprite('ce020_04', 3)


@State
def CmnActJumpDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_05', 3)
    sprite('ce020_06', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_01', 3)
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    sprite('ce024_04', 3)
    sprite('ce024_05', 3)


@State
def CmnActLandingStiffLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 2)
    sprite('ce024_01', 2)
    sprite('ce024_02', 32767)


@State
def CmnActLandingStiffEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_03', 3)
    sprite('ce024_04', 3)
    sprite('ce024_05', 3)


@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')

        def upon_17():
            ObjectUpon2(11, 102, 0)

        def upon_STATE_END():
            ObjectUpon2(11, 100, 0)
    sprite('ce030_00', 7)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')

        def upon_17():
            ObjectUpon2(11, 103, 0)

        def upon_STATE_END():
            ObjectUpon2(11, 100, 0)
    sprite('ce030_00ex', 7)
    label(0)
    sprite('ce030_01ex', 7)
    sprite('ce030_02ex', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03ex', 7)
    sprite('ce030_04ex', 7)
    sprite('ce030_05ex', 7)
    sprite('ce030_06ex', 7)
    sprite('ce030_07ex', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08ex', 7)
    sprite('ce030_09ex', 7)
    sprite('ce030_10ex', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce032_00', 3)
    label(0)
    sprite('ce032_01', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    sprite('ce032_02', 4)
    PrivateSE('cese_04')
    sprite('ce032_03', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce032_04', 3)
    sprite('ce032_05', 3)
    sprite('ce032_06', 3)
    sprite('ce032_07', 3)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        callSubroutine('MinervaNoneCall')
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
        InvincibilityDuration(5)
        EndMomentum(1)
    sprite('ce033_00', 2)
    PrivateSE('cese_16')
    sprite('ce033_01', 2)
    physicsXImpulse(-20000)
    sprite('ce033_02', 2)
    AddX(-20000)
    XImpulseAcceleration(150)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)
    XImpulseAcceleration(150)
    sprite('ce033_03', 3)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)
    XImpulseAcceleration(15)
    LandingEffects(100, 1, 1)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)
    XImpulseAcceleration(15)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)
    physicsXImpulse(0)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce035_00', 3)
    label(0)
    sprite('ce035_01', 3)
    CreateObject('ceAirDashEff', 0)
    CreateObject('ceAirDashEff', 1)
    CreateObject('ceAirDashEff', 2)
    sprite('ce035_02', 3)
    sprite('ce035_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce036_00', 3)
    label(0)
    sprite('ce036_01', 3)
    CreateObject('ceAirBDashEff', 0)
    CreateObject('ceAirBDashEff', 1)
    CreateObject('ceAirDashEff', 2)

    def RunOnObject_1():
        Flip()
    sprite('ce036_02', 3)
    sprite('ce036_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_00', 1)
    sprite('ce050_01', 1)
    sprite('ce050_00', 2)


@State
def CmnActHitStandLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_01', 1)
    sprite('ce050_02', 1)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)


@State
def CmnActHitStandLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_02', 1)
    sprite('ce050_03', 1)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)


@State
def CmnActHitStandLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_03', 1)
    sprite('ce050_04', 1)
    sprite('ce050_03', 2)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)


@State
def CmnActHitStandLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_04', 1)
    sprite('ce050_04', 1)
    sprite('ce050_04', 2)
    sprite('ce050_03', 2)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)


@State
def CmnActHitStandLowLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_00', 1)
    sprite('ce052_01', 1)
    sprite('ce052_00', 2)


@State
def CmnActHitStandLowLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_01', 1)
    sprite('ce052_02', 1)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)


@State
def CmnActHitStandLowLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_02', 1)
    sprite('ce052_03', 1)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)


@State
def CmnActHitStandLowLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_03', 1)
    sprite('ce052_04', 1)
    sprite('ce052_03', 2)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)


@State
def CmnActHitStandLowLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_04', 1)
    sprite('ce052_04', 1)
    sprite('ce052_04', 2)
    sprite('ce052_03', 2)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)


@State
def CmnActHitCrouchLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_00', 1)
    sprite('ce054_01', 1)
    sprite('ce054_00', 2)


@State
def CmnActHitCrouchLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_01', 1)
    sprite('ce054_02', 1)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)


@State
def CmnActHitCrouchLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_02', 1)
    sprite('ce054_03', 1)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)


@State
def CmnActHitCrouchLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_03', 1)
    sprite('ce054_04', 1)
    sprite('ce054_03', 2)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)


@State
def CmnActHitCrouchLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_04', 1)
    sprite('ce054_04', 1)
    sprite('ce054_04', 2)
    sprite('ce054_03', 2)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)


@State
def CmnActBDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_00', 4)
    label(0)
    sprite('ce060_01', 4)
    sprite('ce060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_03', 4)


@State
def CmnActBDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_04', 4)
    label(0)
    sprite('ce060_05', 4)
    sprite('ce060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_07', 2)
    sprite('ce060_08', 2)


@State
def CmnActBDownBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_09', 3)
    sprite('ce060_10', 3)
    sprite('ce060_11', 3)
    sprite('ce060_12', 3)
    sprite('ce060_13', 3)


@State
def CmnActBDownLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_14', 1)


@State
def CmnActBDown2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce061_00', 3)
    sprite('ce061_01', 3)
    sprite('ce061_02', 3)
    sprite('ce061_03', 3)
    sprite('ce061_04', 3)
    sprite('ce061_05', 3)
    sprite('ce061_06', 3)
    sprite('ce061_07', 2)
    sprite('ce061_08', 2)
    sprite('ce061_09', 2)


@State
def CmnActFDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_00', 3)


@State
def CmnActFDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_01', 3)


@State
def CmnActFDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce063_02', 3)
    sprite('ce063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_04', 3)
    sprite('ce063_05', 3)


@State
def CmnActFDownBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_06', 2)
    sprite('ce063_07', 2)
    sprite('ce063_08', 3)
    sprite('ce063_09', 3)
    sprite('ce063_10', 3)


@State
def CmnActFDownLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_11', 3)


@State
def CmnActFDown2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce064_00', 2)
    sprite('ce064_01', 2)
    sprite('ce064_02', 2)
    sprite('ce064_03', 2)
    sprite('ce064_04', 2)
    sprite('ce064_05', 2)
    sprite('ce064_06', 2)
    sprite('ce064_07', 2)
    sprite('ce064_08', 3)
    sprite('ce064_09', 3)


@State
def CmnActVDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_00', 3)
    label(0)
    sprite('ce062_01', 3)
    sprite('ce062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_03', 3)
    sprite('ce062_04', 3)


@State
def CmnActVDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_05', 3)
    sprite('ce062_06', 3)
    label(0)
    sprite('ce062_07', 3)
    sprite('ce062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_09', 2)
    sprite('ce062_10', 2)


@State
def CmnActZSpinCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_09', 2)
    sprite('ce062_10', 2)


@State
def CmnActBlowoff():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce072_00', 5)
    sprite('ce072_01', 3)
    sprite('ce072_02', 3)
    label(0)
    sprite('ce072_01', 3)
    sprite('ce072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce074_00', 3)
    sprite('ce074_01', 3)
    sprite('ce074_02', 3)
    sprite('ce074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        CreateObject('dengeki_mv', -1)
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce082_00', 2)
    sprite('ce082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce071_04', 1)


@State
def CmnActWallBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_00', 3)
    sprite('ce073_01', 3)


@State
def CmnActWallBoundDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_02', 3)
    label(0)
    sprite('ce073_03', 3)
    sprite('ce073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_00', 3)
    sprite('ce070_01', 3)
    label(0)
    sprite('ce070_02', 3)
    sprite('ce070_03', 3)
    gotoLabel(0)


@State
def CmnActStaggerDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_04', 4)
    sprite('ce070_05', 4)
    sprite('ce070_06', 4)
    sprite('ce070_07', 4)
    sprite('ce070_08', 4)
    sprite('ce070_09', 4)


@State
def CmnActUkemiStagger():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_10', 1)
    sprite('ce070_11', 2)
    sprite('ce070_12', 3)
    sprite('ce070_13', 3)


@State
def CmnActUkemiAirF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)


@State
def CmnActUkemiAirB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)


@State
def CmnActUkemiAirN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)


@State
def CmnActUkemiLandF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce110_00', 2)
    sprite('ce110_01', 2)
    sprite('ce110_02', 2)
    sprite('ce110_03', 2)
    sprite('ce110_04', 2)
    sprite('ce110_05', 2)
    sprite('ce110_06', 2)
    sprite('ce110_07', 200)
    sprite('ce110_08', 3)
    sprite('ce110_09', 3)


@State
def CmnActUkemiLandB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce111_00', 3)
    sprite('ce111_01', 3)
    sprite('ce111_02', 3)
    sprite('ce111_03', 3)
    sprite('ce111_04', 3)
    sprite('ce111_06', 3)
    sprite('ce111_07', 200)
    sprite('ce111_08', 3)
    sprite('ce111_09', 3)


@State
def CmnActUkemiLandN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce112_00', 2)
    sprite('ce112_01', 2)
    sprite('ce112_02', 2)
    sprite('ce112_03', 2)
    sprite('ce112_04', 2)
    sprite('ce112_05', 2)
    sprite('ce112_06', 2)
    sprite('ce112_07', 2)
    sprite('ce112_08', 2)


@State
def CmnActUkemiLandNLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 3)
    sprite('ce024_01', 3)
    sprite('ce024_02', 3)
    sprite('ce024_03', 3)
    sprite('ce024_04', 3)


@State
def CmnActMidGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_00', 3)
    sprite('ce040_01', 3)


@State
def CmnActMidGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce040_02', 3)
    sprite('ce040_03', 3)
    sprite('ce040_04', 3)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)


@State
def CmnActMidHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_05', 3)
    label(0)
    sprite('ce040_02', 3)
    sprite('ce040_03', 3)
    sprite('ce040_04', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)


@State
def CmnActHighGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_00', 3)
    sprite('ce041_01', 3)


@State
def CmnActHighGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce041_02', 3)
    sprite('ce041_03', 3)
    sprite('ce041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)
    sprite('ce041_00', 3)


@State
def CmnActHighHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_05', 3)
    label(0)
    sprite('ce041_02', 3)
    sprite('ce041_03', 3)
    sprite('ce041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)
    sprite('ce041_00', 3)


@State
def CmnActCrouchGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_00', 3)
    sprite('ce043_01', 3)


@State
def CmnActCrouchGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce043_02', 3)
    sprite('ce043_03', 3)
    sprite('ce043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)
    sprite('ce043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_05', 3)
    label(0)
    sprite('ce043_02', 3)
    sprite('ce043_03', 3)
    sprite('ce043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)
    sprite('ce043_00', 3)


@State
def CmnActAirGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_00', 3)
    sprite('ce045_01', 3)


@State
def CmnActAirGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce045_02', 3)
    sprite('ce045_03', 3)
    sprite('ce045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)
    sprite('ce045_00', 3)


@State
def CmnActAirHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_05', 3)
    label(0)
    sprite('ce045_02', 3)
    sprite('ce045_03', 3)
    sprite('ce045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)
    sprite('ce045_00', 3)


@State
def CmnActGuardBreakStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce090_00', 2)
    sprite('ce090_01', 2)
    sprite('ce090_02', 1)
    SetCommonActionMark(1)
    sprite('ce090_03', 6)
    sprite('ce090_04', 6)


@State
def CmnActGuardBreakCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce091_00', 2)
    sprite('ce091_01', 2)
    sprite('ce091_02', 1)
    SetCommonActionMark(1)
    sprite('ce091_03', 6)
    sprite('ce091_04', 6)


@State
def CmnActGuardBreakAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce092_00', 2)
    sprite('ce092_01', 2)
    sprite('ce092_02', 1)
    SetCommonActionMark(1)
    sprite('ce092_03', 6)
    sprite('ce092_04', 6)


@State
def CmnActAirTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce025_00', 3)
    sprite('ce025_01', 3)
    sprite('ce025_00ex', 3)


@State
def CmnActLockWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_02', 1)
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)


@State
def CmnActLockReject():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce312_00', 7)
    sprite('ce312_01', 7)
    sprite('ce312_02', 2)
    sprite('ce312_03', 2)
    sprite('ce312_04', 3)
    sprite('ce312_05', 3)
    sprite('ce312_06', 3)
    sprite('ce312_07', 3)


@State
def CmnActAirLockWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_02', 1)
    sprite('ce045_01', 3)
    sprite('ce045_00', 3)


@State
def CmnActAirLockReject():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce322_00', 6)
    sprite('ce322_01', 6)
    sprite('ce322_02', 2)
    sprite('ce322_03', 2)
    sprite('ce322_04', 2)
    sprite('ce322_05', 2)
    sprite('ce322_06', 2)
    sprite('ce322_07', 2)
    sprite('ce322_08', 2)
    sprite('ce322_09', 2)


@State
def CmnActLandSpin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce071_00', 4)
    sprite('ce071_01', 4)
    label(0)
    sprite('ce071_02', 2)
    sprite('ce071_03', 2)
    sprite('ce071_04', 2)
    sprite('ce071_05', 2)
    sprite('ce071_06', 2)
    sprite('ce071_07', 2)
    sprite('ce071_08', 2)
    sprite('ce071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce071_10', 6)
    sprite('ce071_11', 5)
    sprite('ce071_12', 5)


@State
def CmnActVertSpin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce071_02', 2)
    sprite('ce071_03', 2)
    sprite('ce071_04', 2)
    sprite('ce071_05', 2)
    sprite('ce071_06', 2)
    sprite('ce071_07', 2)
    sprite('ce071_08', 2)
    sprite('ce071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce077_00', 2)
    sprite('ce077_01', 2)
    sprite('ce077_00ex01', 2)
    sprite('ce077_01ex01', 2)
    sprite('ce077_00ex02', 2)
    sprite('ce077_01ex02', 2)
    sprite('ce077_00ex03', 2)
    sprite('ce077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_02', 4)
    label(0)
    sprite('ce077_03', 3)
    sprite('ce077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_05', 5)
    sprite('ce077_06', 4)


@State
def CmnActAomukeSlideKeep():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_11', 4)
    sprite('ce060_13', 5)


@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_00', 2)
    sprite('ce331_01', 2)
    label(0)
    sprite('ce331_02', 3)
    sprite('ce331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)
    sprite('ce331_05', 2)
    label(0)
    sprite('ce331_06', 3)
    sprite('ce331_07', 3)
    sprite('ce331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_09', 3)
    sprite('ce331_10', 3)


@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_11', 2)
    sprite('ce331_12', 2)
    label(0)
    sprite('ce331_02', 3)
    sprite('ce331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)
    sprite('ce331_05', 2)
    label(0)
    sprite('ce331_06', 3)
    sprite('ce331_07', 3)
    sprite('ce331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_13', 3)
    sprite('ce331_14', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 3)
    sprite('ce333_01', 3)
    sprite('ce333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ce333_03', 32767)
    CreateObject('EMB_CE_OD', 0)
    loopRest()


@State
def CmnActOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)
    sprite('ce333_09', 6)


@State
def CmnActAirOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_10', 3)
    sprite('ce333_11', 3)
    sprite('ce333_12', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ce333_13', 32767)
    CreateObject('EMB_CE_OD', 0)
    loopRest()


@State
def CmnActAirOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_14', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_15', 6)
    sprite('ce333_16', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        SingleProration(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('AN_NmlAtk5AAdd')
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
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
    sprite('ce200_00', 3)
    PerInertia(60)
    sprite('ce200_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce200_02', 3)
    sprite('ce200_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce200_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce200_04', 3)
    RefreshMultihit()
    sprite('ce200_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()
    label(0)
    sprite('keep', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()


@State
def AN_NmlAtk5AAdd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        SingleProration(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('AN_NmlAtk5AAdd')
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
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
    sprite('ce200_05', 3)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce200_02', 3)
    sprite('ce200_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce200_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce200_04', 3)
    RefreshMultihit()
    sprite('ce200_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()
    label(0)
    sprite('keep', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 300, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 15:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce207_00', 3)
    PerInertia(60)
    sprite('ce207_00', 2)
    RandomCommonVoiceline(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_01', 5)
    sprite('ce207_00', 5)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 301, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 20:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce217_00', 3)
    PerInertia(60)
    sprite('ce217_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    sprite('ce217_01', 5)
    sprite('ce217_03', 3)
    sprite('ce217_00', 2)


@Subroutine
def DriveInitFirst():
    Hitstop(9)
    Unknown61(0, 1, 0, 5, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_59 = SLOT_0

    def upon_EVERY_FRAME():
        if SLOT_51:
            clearUponHandler(EVERY_FRAME)
            if SLOT_59 == 1:
                SmartVoiceline('ce300')
            if SLOT_59 == 2:
                SmartVoiceline('ce303')
            if SLOT_59 == 3:
                SmartVoiceline('ce306')
            if SLOT_59 == 4:
                SmartVoiceline('ce309')
            if SLOT_59 == 5:
                SmartVoiceline('ce312')
    callSubroutine('MinervaNoneCallAttack')


@Subroutine
def DriveInitSecond():
    Hitstop(9)

    def upon_EVERY_FRAME():
        if SLOT_51:
            clearUponHandler(EVERY_FRAME)
            if SLOT_59 == 1:
                SmartVoiceline('ce301')
            if SLOT_59 == 2:
                SmartVoiceline('ce304')
            if SLOT_59 == 3:
                SmartVoiceline('ce307')
            if SLOT_59 == 4:
                SmartVoiceline('ce310')
            if SLOT_59 == 5:
                SmartVoiceline('ce313')
    callSubroutine('MinervaNoneCallAttack')


@Subroutine
def DriveInitThird():
    StarterRating(2)

    def upon_EVERY_FRAME():
        if SLOT_51:
            clearUponHandler(EVERY_FRAME)
            if SLOT_59 == 1:
                SmartVoiceline('ce302')
            if SLOT_59 == 2:
                SmartVoiceline('ce305')
            if SLOT_59 == 3:
                SmartVoiceline('ce308')
            if SLOT_59 == 4:
                SmartVoiceline('ce311')
            if SLOT_59 == 5:
                SmartVoiceline('ce314')
    callSubroutine('MinervaNoneCallAttack')


@Subroutine
def DeriveInputFirst():
    BeginBuffer('AN_NmlAtk5DD')
    BeginBuffer('AN_NmlAtk2DD')
    BeginBuffer('AN_NmlAtk2DD_Input1')
    BeginBuffer('AN_NmlAtk2DD_Input3')
    BeginBuffer('AN_NmlAtk6DD')
    BeginBuffer('AN_NmlAtk6DD_Input4')
    BeginBuffer('AN_NmlAtk6DD_Input7')
    BeginBuffer('AN_NmlAtk6DD_Input9')


@Subroutine
def DeriveTimingFirst():
    BufferedOrPressedGoto('AN_NmlAtk5DD')
    BufferedOrPressedGoto('AN_NmlAtk2DD')
    BufferedOrPressedGoto('AN_NmlAtk2DD_Input1')
    BufferedOrPressedGoto('AN_NmlAtk2DD_Input3')
    BufferedOrPressedGoto('AN_NmlAtk6DD')
    BufferedOrPressedGoto('AN_NmlAtk6DD_Input4')
    BufferedOrPressedGoto('AN_NmlAtk6DD_Input7')
    BufferedOrPressedGoto('AN_NmlAtk6DD_Input9')


@Subroutine
def DeriveInputSecond():
    BeginBuffer('AN_NmlAtk5DDD')


@Subroutine
def DeriveTimingSecond():
    BufferedOrPressedGoto('AN_NmlAtk5DDD')


@State
def DriveEnd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
    sprite('ce260_01', 4)
    sprite('ce260_02', 4)
    sprite('ce260_03', 4)
    sprite('ce260_04', 4)
    sprite('ce260_05', 4)


@Subroutine
def Recovery_HP():

    def upon_OPPONENT_HIT():
        if not SLOT_58:
            SLOT_8 = SLOT_8 + 100
            if SLOT_OverdriveTimer:
                pass
            SLOT_63 = SLOT_63 + 1
            if SLOT_63 == 1:
                pass
            if SLOT_63 >= 2:
                SLOT_8 = SLOT_8 + 50
            if SLOT_63 >= 3:
                SLOT_8 = SLOT_8 + 50
            if SLOT_63 >= 4:
                SLOT_8 = SLOT_8 + 50
            if SLOT_63 >= 5:
                SLOT_8 = SLOT_8 + 50
            SLOT_58 = 1
        if CurrentStateCheck('AN_NmlAtk5DDD'):
            AddActionMark(1)


@Subroutine
def OnEnemyComboBreak():
    SLOT_63 = 0


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP2(82)
        DamageEffect(2, 'ceef_hiteffD')
        AirPushbackX(2500)
        AirPushbackY(20000)
        PushbackX(-5000)
        AirUntechableTime(29)
        Hitstun(29)
        FatalCounter(1)
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('DriveInitFirst')
        callSubroutine('Recovery_HP')
    sprite('ce203_00', 5)
    sprite('ce203_01', 5)
    callSubroutine('DeriveInputFirst')
    SLOT_51 = 1
    sprite('ce203_02', 3)
    CreateObject('mv203Eff', -1)
    CommonSE('003_swing_grap_0_0')
    PrivateSE('cese_19')
    sprite('ce203_03', 4)
    physicsXImpulse(-5000)
    Recovery()
    Unknown2063()
    sprite('ce203_04', 3)
    XImpulseAcceleration(25)
    sprite('ce203_05', 2)
    physicsXImpulse(0)
    sprite('keep', 2)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def AN_NmlAtk5DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(280)
        AttackP2(72)
        SingleProration(1)
        HitsparkSize(400)
        PushbackX(2500)
        GroundBounce(1)
        AirUntechableTime(29)
        AirPushbackX(10000)
        AirPushbackY(2000)
        AirHitstunAnimation(9)
        MoveAttributes(0, 0, 1, 0, 0)
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('DriveInitSecond')
        Hitstop(2)
        AttackOff()
        SpecialCancel(0)
        callSubroutine('Recovery_HP')
    sprite('ce260_00', 2)
    sprite('ce204_01', 2)
    setInvincible(1)
    GuardPoint_(0)
    SpecificInvincibility(0, 0, 0, 1, 0)
    DollInvincibility(0)
    BurstInvincibility(0)
    sprite('ce204_02', 2)
    physicsXImpulse(10000)
    sprite('ce204_03', 3)
    RefreshMultihit()
    AirPushbackX(1750)
    AirPushbackY(-25000)
    callSubroutine('DeriveInputSecond')
    sprite('ce204_04', 2)
    SLOT_51 = 1
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(2000)
    GroundBounce(0)
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    physicsXImpulse(30000)
    sprite('ce204_05', 2)
    XImpulseAcceleration(120)
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    CreateObject('mv204Smoke', -1)
    CreateObject('mv204ringLoops', -1)
    sprite('ce204_04', 2)
    RefreshMultihit()
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_17')
    sprite('ce204_05', 2)
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_17')
    sprite('ce204_04', 2)
    RefreshMultihit()
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_17')
    sprite('ce204_05', 2)
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_17')
    sprite('ce204_04', 2)
    RefreshMultihit()
    physicsXImpulse(55000)
    EnableCollision(0)
    AirHitstunAnimation(10)
    AirPushbackX(5400)
    AirPushbackY(24000)
    PushbackX(19800)
    HardKnockdown(0)
    GroundedHitstunAnimation(6)
    Hitstun(18)
    CreateParticle('ceef_204eff', 0)
    CreateParticle('ceef_dasheff_line', 1)
    sprite('ce204_05', 2)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ce204_06', 2)
    CtrlDirectionVsTarget()
    XImpulseAcceleration(80)
    DespawnEAEffect('mv204ringLoops')
    sprite('ce204_07', 2)
    XImpulseAcceleration(80)
    sprite('ce204_08', 2)
    XImpulseAcceleration(80)
    callSubroutine('DeriveTimingSecond')
    SpecialCancel(1)
    sprite('ce204_09', 2)
    XImpulseAcceleration(80)
    sprite('keep', 2)
    XImpulseAcceleration(0)
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def AN_NmlAtk5DDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(82)
        Hitstun(40)
        AirUntechableTime(60)
        GroundedHitstunAnimation(6)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(29000)
        YImpulseBeforeWallbounce(1500)
        StarterRating(2)
        Unknown12052(1)
        DamageEffect(2, 'ceef_hiteffD')
        callSubroutine('DriveInitThird')
        callSubroutine('Recovery_HP')
    sprite('ce270_00', 3)
    sprite('ce270_01', 3)
    CreateObject('mv205ConsentEff', 0)
    sprite('ce270_02', 2)
    sprite('ce270_03', 2)
    sprite('ce270_04', 2)
    SLOT_51 = 1
    CommonSE('005_swing_grap_2_2')
    PrivateSE('cese_22')
    sprite('ce270_05', 4)
    CreateObject('ceef_270', 4)
    CreateParticle('ceef_270burner', 1)
    CreateParticle('ceef_270burner', 2)
    CreateParticle('ceef_270burner', 3)
    sprite('ce270_06', 3)
    sprite('ce270_07', 3)
    loopRest()
    if SLOT_2:
        enterState('Finish_Healing')
    sprite('ce270_11', 3)
    sprite('ce270_12', 3)
    loopRest()
    enterState('DriveEnd')


@State
def Finish_Healing():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('ce270_08', 6)
    sprite('ce270_09', 6)
    sprite('ce270_10', 6)
    sprite('ce432_09', 3)
    callSubroutine('MinervaCallAttack')
    Voiceline('ce109')
    ObjectUpon2(11, 404, 0)
    sprite('ce432_09', 3)
    CreateObject('SuperHealEff', -1)
    SetActionMark(100)

    def upon_EVERY_FRAME():
        if SLOT_21:
            if SLOT_8 > 0:
                if SLOT_8 >= SLOT_2:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_2
                    SLOT_8 = SLOT_8 - SLOT_2
                else:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_8
                    SLOT_8 = SLOT_8 - SLOT_8
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    label(9)
    sprite('ce432_12', 5)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('SuperHealEff', 32)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ce432_13', 4)
    sprite('ce432_14', 4)
    sprite('ce432_15', 4)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        SingleProration(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        WhiffCancel('AN_NmlAtk2AAdd')
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
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MinervaCallAttack')
    sprite('ce230_00', 3)
    PerInertia(60)
    sprite('ce230_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce230_02', 3)
    sprite('ce230_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce230_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce230_04', 3)
    RefreshMultihit()
    sprite('ce230_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce230_01', 3)
    sprite('ce230_00', 3)
    ExitState()
    label(0)
    sprite('keep', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce230_01', 3)
    sprite('ce230_00', 3)
    ExitState()


@State
def AN_NmlAtk2AAdd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        SingleProration(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        WhiffCancel('AN_NmlAtk2AAdd')
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
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MinervaCallAttack')
    sprite('ce230_05', 3)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce230_02', 3)
    sprite('ce230_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce230_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce230_04', 3)
    RefreshMultihit()
    sprite('ce230_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce230_01', 3)
    sprite('ce230_00', 3)
    ExitState()
    label(0)
    sprite('keep', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce230_01', 3)
    sprite('ce230_00', 3)
    ExitState()


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 310, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 15:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce237_00', 3)
    PerInertia(60)
    sprite('ce237_00', 2)
    RandomCommonVoiceline(1)
    sprite('ce237_01', 5)
    sprite('ce237_02', 5)
    sprite('ce237_03', 5)
    sprite('ce237_03', 3)
    sprite('ce237_00', 5)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 311, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 17:
                setInvincible(0)
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce238_00', 3)
    PerInertia(60)
    sprite('ce238_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce238_01', 5)
    sprite('ce238_02', 5)
    sprite('ce238_03', 5)
    sprite('ce238_04', 5)
    sprite('ce238_01', 3)
    sprite('ce238_00', 5)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 312, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 16:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    if PreviousStateCheck('NmlAtk2C'):
        conditionalSendToLabel(1)
    sprite('ce238_00', 3)
    PerInertia(60)
    sprite('ce238_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce238_01', 5)
    sprite('ce238_02', 5)
    sprite('ce238_03', 5)
    sprite('ce238_04', 5)
    sprite('ce238_01', 5)
    sprite('ce238_02', 5)
    sprite('ce238_00', 5)
    ExitState()
    label(1)
    sprite('ce237_00', 3)
    PerInertia(60)
    sprite('ce237_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce237_01', 5)
    sprite('ce237_02', 5)
    sprite('ce237_03', 5)
    sprite('ce237_01', 5)
    sprite('ce237_02', 5)
    sprite('ce237_03', 5)
    sprite('ce237_00', 5)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        HitLow(2)
        Damage(750)
        AttackP1(90)
        AttackP2(72)
        PushbackX(10000)
        GroundedHitstunAnimation(11)
        AirPushbackX(2500)
        AirPushbackY(20000)
        CHHardKnockdown(10)
        AirUntechableTime(29)
        MoveAttributes(0, 0, 1, 0, 0)
        DamageEffect(2, 'ceef_hiteffD')
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('DriveInitFirst')
        callSubroutine('Recovery_HP')
    sprite('ce233_00', 3)
    sprite('ce233_01', 3)
    sprite('ce233_02', 6)
    sprite('ce233_03', 6)
    callSubroutine('DeriveInputFirst')
    SLOT_51 = 1
    sprite('ce233_04', 4)
    physicsXImpulse(35000)
    CreateObject('mv233Eff', 0)
    CommonSE('003_swing_grap_0_2')
    PrivateSE('cese_19')
    sprite('ce233_05', 3)
    XImpulseAcceleration(50)
    sprite('ce233_06', 3)
    Recovery()
    Unknown2063()
    XImpulseAcceleration(50)
    sprite('ce233_07', 2)
    XImpulseAcceleration(0)
    sprite('keep', 2)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def AN_NmlAtk2DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        HitLow(2)
        Damage(750)
        AttackP1(90)
        AttackP2(72)
        SingleProration(1)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(11)
        AirPushbackX(1000)
        AirPushbackY(23000)
        PushbackX(19950)
        AirUntechableTime(29)
        CHAirPushbackX(7000)
        CHAirPushbackY(13500)
        CHHardKnockdown(10)
        MoveAttributes(0, 0, 1, 0, 0)
        DamageEffect(2, 'ceef_hiteffD')
        callSubroutine('DriveInitSecond')
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('Recovery_HP')
    sprite('ce260_00', 2)
    sprite('ce234_00', 2)
    CreateObject('mv234ConsentEff', 0)
    sprite('ce234_01', 2)
    sprite('ce234_02', 2)
    sprite('ce234_03', 2)
    callSubroutine('DeriveInputSecond')
    SLOT_51 = 1
    sprite('ce234_04', 3)
    RefreshMultihit()
    CreateObject('mv234Eff', -1)
    CommonSE('003_swing_grap_0_1')
    PrivateSE('cese_18')
    sprite('ce234_05', 3)
    Recovery()
    Unknown2063()
    TriggerUponForState('mv234ConsentEff', 32)
    sprite('ce234_06', 3)
    sprite('ce234_07', 2)
    TriggerUponForState('mv234ConsentEff', 33)
    sprite('keep', 2)
    callSubroutine('DeriveTimingSecond')
    sprite('ce260_00', 3)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        SingleProration(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('ce250_00', 3)
    sprite('ce250_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce250_02', 3)
    sprite('ce250_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce250_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce250_04', 3)
    RefreshMultihit()
    sprite('ce250_05', 3)
    Recovery()
    Unknown2063()
    sprite('ce250_01', 3)
    sprite('ce250_00', 3)
    ExitState()
    label(0)
    sprite('keep', 2)
    Recovery()
    Unknown2063()
    sprite('ce250_01', 3)
    sprite('ce250_00', 3)
    ExitState()


@State
def AN_NmlAtkAIR5AAdd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        SingleProration(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('ce250_05', 3)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ce250_02', 3)
    sprite('ce250_03', 2)
    if not CheckInput(INPUT_HOLD_A):
        sendToLabel(0)
    sprite('ce250_03', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce250_04', 3)
    RefreshMultihit()
    sprite('ce250_05', 3)
    Recovery()
    Unknown2063()
    sprite('ce250_01', 3)
    sprite('ce250_00', 3)
    ExitState()
    label(0)
    sprite('keep', 2)
    Recovery()
    Unknown2063()
    sprite('ce250_01', 3)
    sprite('ce250_00', 3)
    ExitState()


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 330, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 15:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce257_00', 3)
    sprite('ce257_00', 2)
    RandomCommonVoiceline(1)
    sprite('ce257_01', 5)
    sprite('ce257_02', 5)
    sprite('ce257_03', 5)
    sprite('ce257_04', 5)
    sprite('ce257_00', 5)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 331, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 20:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce258_00', 3)
    sprite('ce258_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce258_01', 5)
    sprite('ce258_02', 5)
    sprite('ce258_03', 5)
    sprite('ce258_04', 5)
    sprite('ce258_01', 5)
    sprite('ce258_02', 5)
    sprite('ce258_00', 5)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(600)
        AttackP1(80)
        AttackP2(82)
        AirPushbackX(10000)
        AirPushbackY(-60000)
        HardKnockdown(1)
        EnemyHitstopAddition(0, 0, 0)
        AirUntechableTime(30)
        PushbackX(15000)
        callSubroutine('DriveInitFirst')
        HitOverhead(0)
        Hitstop(3)
        DamageEffect(2, 'ceef_hiteffD')
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('Recovery_HP')
    sprite('ce253_00', 3)
    sprite('ce253_01', 3)
    EndMomentum(1)
    physicsXImpulse(4500)
    SetAcceleration(300)
    physicsYImpulse(25000)
    setGravity(2200)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)

    def upon_FALLING():
        clearUponHandler(FALLING)
        sendToLabel(100)
    PushCollisionHeightLow(100000)
    sprite('ce253_02', 3)
    sprite('ce213_03', 3)
    sprite('ce213_04', 3)
    sprite('ce213_05', 2)
    sprite('ce213_06', 32767)
    label(100)
    sprite('keep', 3)
    SLOT_51 = 1
    callSubroutine('DeriveInputFirst')
    YSpeed(-30000)
    PrivateSE('cese_19')
    label(0)
    sprite('ce213_08ex00', 3)
    CreateObject('mv213Eff', -1)
    sprite('ce213_08ex01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    EndMomentum(1)
    callSubroutine('DeriveInputFirst')
    clearUponHandler(LANDING)
    CreateParticle('ceef_402_stone', 0)
    sprite('ce213_08', 2)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    EnemyHitstopAddition(0, 0, 8)
    AirPushbackX(6500)
    AirPushbackY(-18000)
    GroundBounce(1)
    BouncePercentage(100)
    HardKnockdownReset()
    Hitstop(9)
    AltKnockdownEffects(100, 1, 1)
    DespawnEAEffect('mv213Eff')
    sprite('ce213_09', 3)
    Recovery()
    Unknown2063()
    sprite('ce213_10', 3)
    sprite('ce213_11', 3)
    sprite('ce260_00', 5)
    callSubroutine('DeriveTimingFirst')
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(510)
        AttackP1(80)
        AttackP2(92)
        SingleProration(1)
        BonusProration(110)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(7500)
        CHAirPushbackY(4500)
        AirUntechableTime(33)
        CHAirUntechableTime(43)
        HardKnockdown(1)
        StarterRating(2)
        SpecialCancel(0)
        uponSendToLabel(LANDING, 0)
        callSubroutine('MinervaCall')
    sprite('ce210_00', 3)
    sprite('ce210_01', 3)
    ObjectUpon2(11, 110, 0)
    sprite('ce210_02', 3)
    sprite('ce210_03', 3)
    sprite('ce210_04', 3)
    sprite('ce210_05', 3)
    CommonSE('004_swing_grap_1_1')
    physicsXImpulse(2000)
    sprite('ce210_06', 5)
    ObjectUpon2(11, 111, 0)
    XImpulseAcceleration(250)
    sprite('ce210_07', 5)
    SmartVoiceline('ce108')
    XImpulseAcceleration(150)
    physicsYImpulse(7500)
    EndYPhysicsImpulse()
    sprite('ce210_08', 32767)
    StartMultihit()
    label(0)
    sprite('ce210_09', 5)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(550)
    HitOverhead(0)
    HitLow(2)
    MoveAttributes(0, 0, 1, 0, 0)
    GroundedHitstunAnimation(2)
    Stagger(35)
    Crumple(25)
    AirPushbackX(27500)
    AirPushbackY(3000)
    CHAirPushbackX(15000)
    CHAirPushbackY(5500)
    AirUntechableTime(27)
    HardKnockdown(13)
    ResetPushbackX()
    XImpulseAcceleration(200)
    clearUponHandler(LANDING)
    LandingEffects(100, 1, 1)
    sprite('ce210_10', 4)
    XImpulseAcceleration(25)
    Recovery()
    Unknown2063()
    sprite('ce210_11', 4)
    EndMomentum(1)
    ObjectUpon2(11, 100, 0)
    sprite('ce210_12', 4)
    sprite('ce210_13', 4)
    sprite('ce210_14', 4)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        NoAttackDuringAction(1)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 320, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 15:
                setInvincible(0)
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce218_00', 3)
    sprite('ce218_00', 2)
    RandomCommonVoiceline(1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('ce218_01', 5)
    sprite('ce218_02', 5)
    sprite('ce218_03', 5)
    sprite('ce218_04', 5)
    sprite('ce218_02', 5)
    sprite('ce218_01', 2)
    sprite('ce218_00', 5)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        NoAttackDuringAction(1)
        HitJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 321, 0)
        ObjectHitbox(11)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 24:
                Recovery()
                Unknown2063()
                clearUponHandler(EVERY_FRAME)
    sprite('ce208_00', 3)
    sprite('ce208_00', 2)
    RandomCommonVoiceline(2)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_00', 3)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(850)
        AttackP1(90)
        AttackP2(72)
        PushbackX(20000)
        GroundedHitstunAnimation(3)
        AirPushbackY(-30000)
        HardKnockdown(10)
        DamageEffect(2, 'ceef_hiteffD')
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('DriveInitFirst')
        uponSendToLabel(LANDING, 1)
        callSubroutine('Recovery_HP')
    sprite('ce213_00', 2)
    sprite('ce213_01', 2)
    physicsXImpulse(15000)
    physicsYImpulse(20000)
    setGravity(3000)
    sprite('ce213_02', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('ce213_03', 3)
    sprite('ce213_04', 3)
    sprite('ce213_05', 3)
    SLOT_51 = 1
    label(0)
    sprite('ce213_06', 3)
    CreateObject('mv213Eff', -1)
    PrivateSE('cese_19')
    sprite('ce213_07', 3)
    gotoLabel(0)
    label(1)
    sprite('ce213_08', 3)
    EndMomentum(1)
    callSubroutine('DeriveInputFirst')
    clearUponHandler(LANDING)
    AltKnockdownEffects(100, 1, 1)
    sprite('ce213_09', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    physicsXImpulse(10000)
    physicsYImpulse(2000)
    GravityDefault()
    sprite('ce213_10', 3)
    XImpulseAcceleration(50)
    sprite('ce213_11', 2)
    XImpulseAcceleration(0)
    sprite('keep', 2)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 3)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def AN_NmlAtk6DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(600)
        AttackP2(72)
        SingleProration(1)
        AirPushbackX(4000)
        AirPushbackY(22000)
        StarterRating(2)
        Unknown12052(1)
        callSubroutine('Recovery_HP')
    sprite('ce260_00', 1)
    sprite('ce214_00', 1)
    physicsXImpulse(3000)
    sprite('ce214_01', 2)
    XImpulseAcceleration(500)
    sprite('ce214_02', 2)
    sprite('ce214_03', 2)
    XImpulseAcceleration(50)
    SLOT_51 = 1
    callSubroutine('DeriveInputSecond')
    Hitstop(6)
    sprite('ce214_04', 4)
    CreateObject('mv214Eff', -1)
    RefreshMultihit()
    XImpulseAcceleration(75)
    AttackLevel_(4)
    DamageEffect(2, 'ceef_hiteffD')
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(2)
    Stagger(46)
    Crumple(36)
    AirUntechableTime(29)
    HitAirUnblockable(0)
    Hitstop(9)
    PushbackX(19950)
    callSubroutine('DriveInitSecond')
    CommonSE('005_swing_grap_2_2')
    PrivateSE('cese_18')
    sprite('ce214_05', 3)
    Recovery()
    Unknown2063()
    XImpulseAcceleration(75)
    sprite('ce214_06', 2)
    XImpulseAcceleration(75)
    sprite('ce214_07', 2)
    XImpulseAcceleration(75)
    sprite('ce214_08', 1)
    sprite('keep', 2)
    XImpulseAcceleration(0)
    callSubroutine('DeriveTimingSecond')
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    if random_(2, 0, 50):
        Voiceline('ce404')
    else:
        Voiceline('ce405')
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    sprite('ce300_05', 8)
    sprite('ce300_05ex', 20)
    sprite('ce300_06', 8)
    sprite('ce300_06ex', 20)
    sprite('ce300_07', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        callSubroutine('MinervaNoneCallAttack')
    sprite('ce203_00', 3)
    sprite('ce203_00', 3)
    sprite('ce203_01', 6)
    sprite('ce203_02', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('ce203_03', 3)
    sprite('ce203_04', 3)
    sprite('ce203_05', 3)
    sprite('ce260_00', 5)
    sprite('ce260_01', 5)
    sprite('ce260_02', 5)
    sprite('ce260_03', 5)
    sprite('ce260_04', 5)
    sprite('ce260_05', 5)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(17)
        AirPushbackX(500)
        AirPushbackY(38000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(60)
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
        callSubroutine('MinervaNoneCallAttack')
    sprite('ce340_00', 3)
    sprite('ce340_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    Voiceline('ce159')
    HeatChange(-2500)
    CreateObject('mv340ConsentEff', 0)
    sprite('ce340_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('ce340_02', 2)
    sprite('ce340_03', 2)
    sprite('ce340_04', 4)
    sprite('ce340_05', 3)
    sprite('ce340_06', 3)
    label(100)
    sprite('ce340_07', 3)
    sprite('ce340_08', 3)
    sprite('ce340_09', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('ce340_07', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('ce340_08', 3)
    sprite('ce340_09', 3)
    sprite('ce340_10', 1)
    CreateParticle('ceef_340_tukieff', 0)
    PrivateSE('cese_06')
    sprite('ce340_10', 2)
    TriggerUponForState('mv340ConsentEff', 32)
    StartMultihit()
    AltKnockdownEffects(100, 1, 1)
    EnableAfterimage(0)
    sprite('ce340_11', 6)
    sprite('ce340_12', 6)
    sprite('ce340_13', 3)
    sprite('ce340_14', 3)
    sprite('ce340_15', 3)
    sprite('ce340_16', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ce310_00', 3)
    sprite('ce310_01', 3)
    sprite('ce310_02', 3)
    sprite('ce310_03', 2)
    CommonSE('010_swing_sword_0')
    sprite('ce310_04', 2)
    sprite('ce310_05', 4)
    SmartVoiceline('ce155')
    sprite('ce310_06', 5)
    sprite('ce310_07', 5)
    sprite('ce310_08', 5)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(3)
        Damage(1500)
        AttackP2(50)
        Hitstop(0)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        UseSlashHitspark(1)
        AirPushbackY(30000)
        AirUntechableTime(60)
        StarterRating(2)
        SetZLine(1, 50)
        StayAfterMovement(1, 0)
    sprite('ce310_02', 6)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ce311_00', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('mv311ConsentEff', 1)
    sprite('ce311_01', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    Voiceline('ce153')
    sprite('ce311_02', 20)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_04', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PrivateSE('cese_20')
    sprite('ce311_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_06', 10)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_07', 3)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    TriggerUponForState('mv311ConsentEff', 32)
    OppPositionOnHit(1, 150000, 100000)
    sprite('ce311_08', 2)
    CreateObject('mv311Eff', -1)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    TriggerUponForState('mv311ConsentEff', 33)
    sprite('ce311_10', 3)
    sprite('ce311_11', 3)
    sprite('ce311_12', 3)
    sprite('ce311_13', 3)
    sprite('ce311_14', 3)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ce310_00', 3)
    sprite('ce310_01', 3)
    sprite('ce310_02', 3)
    sprite('ce310_03', 2)
    CommonSE('010_swing_sword_0')
    sprite('ce310_04', 2)
    sprite('ce310_05', 4)
    SmartVoiceline('ce155')
    sprite('ce310_06', 5)
    sprite('ce310_07', 5)
    sprite('ce310_08', 5)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(3)
        Damage(1500)
        AttackP2(50)
        Hitstop(0)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        UseSlashHitspark(1)
        AirPushbackY(30000)
        AirUntechableTime(60)
        StarterRating(2)
        SetZLine(1, 50)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        StayAfterMovement(1, 0)
    sprite('ce310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ce310_00ex', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce003_00ex01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce003_01ex01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce003_00ex02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('ce310_00exex01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_02', 6)
    Voiceline('ce153')
    Flip()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('mv311ConsentEff', 1)
    sprite('ce311_03', 20)
    AddX(110000)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_04', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    PrivateSE('cese_20')
    sprite('ce311_05', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_06', 10)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ce311_07', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    TriggerUponForState('mv311ConsentEff', 32)
    OppPositionOnHit(1, 150000, 100000)
    sprite('ce311_08', 2)
    CreateObject('mv311Eff', -1)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    TriggerUponForState('mv311ConsentEff', 33)
    sprite('ce311_10', 3)
    sprite('ce311_11', 3)
    sprite('ce311_12', 3)
    sprite('ce311_13', 3)
    sprite('ce311_14', 3)
    endState()


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('ce320_00', 3)
    sprite('ce320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ce320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('ce320_03', 3)
    sprite('ce320_04', 3)
    SmartVoiceline('ce155')
    sprite('ce320_05', 5)
    sprite('ce320_06', 4)
    sprite('ce320_07', 4)
    sprite('ce320_08', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        SetZLine(1, 50)
        AttackLevel_(2)
        Damage(500)
        AttackP2(50)
        AttackP1(100)
        AirUntechableTime(60)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(1500)
        AirPushbackY(30000)
        YImpulseBeforeWallbounce(1350)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        ForcedLandingRecovery(0, 0)
        StarterRating(2)
    sprite('ce320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('ce321_00', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_01', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_02', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_03', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_04', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_05', 3)
    OppThrowAnimation(9, 0)
    sprite('ce321_06', 3)
    CreateObject('mv321BomEff', -1)
    CommonSE('016_explode_1')
    CommonSE('016_explode_2')
    sprite('ce321_07', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1000)
    AttackP2(100)
    AirPushbackX(60000)
    AirPushbackY(15000)
    Hitstop(0)
    AirUntechableTime(60)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Wallbounce(1)
    WallbounceReboundTime(25)
    UseFireHitspark(1)
    sprite('ce321_07', 2)
    StartMultihit()
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    Voiceline('ce154')
    sprite('ce321_08', 3)
    sprite('ce321_09', 3)
    sprite('ce321_10', 3)
    setGravity(2400)
    sprite('ce321_11', 3)
    sprite('ce321_12', 3)


@Subroutine
def DriveCancelDirection():
    if SLOT_6:
        ForceFaceSprite()


@Subroutine
def Recovery_MutekiHP():
    CopyFromRightToLeft(23, 2, 58, 23, 2, 75)

    def upon_GUARDPOINT_ACTIVATION():
        SLOT_57 = 1

    def upon_51():
        if SLOT_57:
            if not SLOT_52:
                CopyFromRightToLeft(23, 2, 57, 23, 2, 75)
                PrivateFunction(1, 2, 58, 2, 57, 2, 8)
                SLOT_8 = SLOT_8 * 150
                SLOT_8 = SLOT_8 / 100

    def upon_14():
        SLOT_57 = 0


@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        AirUntechableTime(33)
        Blockstun(25)
        AirPushbackX(18000)
        AirPushbackY(20000)
        PushbackX(50000)
        AttackDirection(0)
        DamageEffect(2, 'ceef_hiteffH')
        DistanceCheck(1000000, 0, -1, -1)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        SetYCollisionFromOrigin(260)
        callSubroutine('Recovery_MutekiHP')
    if SLOT_9:
        conditionalSendToLabel(100)
    sprite('ce400_00', 1)
    sprite('ce400_01', 1)
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)
    XImpulseAcceleration(50)
    sprite('ce215_00', 1)
    CreateObject('mv215ConsentEff', 0)
    XImpulseAcceleration(50)
    sprite('ce215_00', 1)
    XImpulseAcceleration(50)
    sprite('ce215_01', 2)
    sprite('ce215_02', 2)
    sprite('ce215_03', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardPoint_(1)
    ArmorChipDamage(100)
    ArmorHealth(1500)
    GuardpointHitstop(-2, -1)
    sprite('ce215_04', 1)
    Voiceline('ce201')
    physicsXImpulse(0)
    sprite('ce215_05', 2)
    PrivateSE('cese_22')
    CreateObject('ce215JetEff', 1)
    CreateObject('ce215JetEff', 2)
    CreateObject('AssaultPlug', 0)
    RegisterObject(4, 1)
    SLOT_51 = 1
    DeleteObject(5)
    CreateObject('Cable', 109)
    RegisterObject(5, 1)
    ObjectHitbox(5)
    StartMultihit()
    physicsXImpulse(30000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
        sendToLabel(2)
    sprite('ce215_06', 2)
    XImpulseAcceleration(200)
    sprite('ce215_05', 2)
    XImpulseAcceleration(140)
    sprite('ce215_06', 2)
    sprite('ce215_05', 2)
    loopRest()
    if not SLOT_57:
        notConditionalSendToLabel(3)
    sprite('ce215_06', 2)
    sprite('ce215_05', 2)
    gotoLabel(3)
    label(2)
    sprite('keep', 3)
    XImpulseAcceleration(80)
    label(3)
    sprite('ce215_07', 2)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    TriggerUponForState('ce215JetEff', 32)
    TriggerUponForState('mv215ConsentEff', 33)
    XImpulseAcceleration(50)
    setInvincible(0)
    Recovery()
    sprite('ce215_07', 2)
    XImpulseAcceleration(50)
    sprite('ce215_08', 5)
    ObjectUpon(FALLING, 33)
    SLOT_51 = 0
    XImpulseAcceleration(50)
    sprite('ce215_09', 5)
    XImpulseAcceleration(40)
    sprite('ce215_10', 4)
    XImpulseAcceleration(40)
    sprite('ce215_11', 4)
    XImpulseAcceleration(40)
    sprite('ce215_12', 4)
    XImpulseAcceleration(0)
    ExitState()
    label(100)
    sprite('ce400_00', 1)
    Damage(1200)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(28000)
    AirPushbackY(10000)
    Floorslide(15)
    SLOT_52 = 1
    SLOT_8 = 0
    CharacterFlash(14474340, 10, 2)
    sprite('ce400_01', 1)
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)
    XImpulseAcceleration(50)
    sprite('ce400_03', 1)
    CreateObject('mv215ConsentEff', 0)
    XImpulseAcceleration(50)
    sprite('ce400_03', 1)
    XImpulseAcceleration(50)
    sprite('ce400_04', 1)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardPoint_(1)
    GuardpointHitstop(-1, -1)
    sprite('ce400_05', 1)
    sprite('ce400_06', 2)
    sprite('ce400_07', 2)
    sprite('ce400_08', 1)
    Voiceline('ce201')
    XImpulseAcceleration(0)
    if SLOT_52:
        GotoState('Assault_Tame')
    sprite('ce400_09', 2)
    PrivateSE('cese_09')
    CreateObject('ce400JetEff', 1)
    CreateObject('ce400JetEff', 2)
    CreateObject('ce400JetEffBackFireAtk', 3)
    CreateObject('mv400windMatome', -1)
    CreateObject('AssaultPlug', 0)
    RegisterObject(4, 1)
    SLOT_51 = 1
    DeleteObject(5)
    CreateObject('Cable', 109)
    RegisterObject(5, 1)
    ObjectHitbox(5)
    StartMultihit()
    physicsXImpulse(30000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
        TriggerUponForState('ce400JetEffBackFireAtk', 33)
        sendToLabel(102)
    sprite('ce400_10', 2)
    XImpulseAcceleration(200)
    sprite('ce400_09', 2)
    XImpulseAcceleration(140)
    sprite('ce400_10', 2)
    sprite('ce400_09', 2)
    loopRest()
    if not SLOT_57:
        notConditionalSendToLabel(103)
    sprite('ce400_10', 2)
    sprite('ce400_09', 2)
    gotoLabel(103)
    label(102)
    sprite('keep', 3)
    XImpulseAcceleration(80)
    label(103)
    sprite('ce400_11', 2)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    TriggerUponForState('mv215ConsentEff', 33)
    TriggerUponForState('ce400JetEff', 32)
    DespawnEAEffect('mv400windMatome')
    XImpulseAcceleration(50)
    setInvincible(0)
    Recovery()
    sprite('ce400_11', 2)
    XImpulseAcceleration(50)
    sprite('ce215_08', 5)
    TriggerUponForState('ce400JetEffBackFireAtk', 33)
    ObjectUpon(FALLING, 33)
    SLOT_51 = 0
    XImpulseAcceleration(50)
    sprite('ce215_09', 5)
    XImpulseAcceleration(40)
    sprite('ce215_10', 4)
    XImpulseAcceleration(40)
    sprite('ce215_11', 4)
    XImpulseAcceleration(40)
    sprite('ce215_12', 4)
    XImpulseAcceleration(0)


@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(50)
        AttackP2(82)
        Hitstop(15)
        AirUntechableTime(42)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(12000)
        AirPushbackY(45000)
        DamageEffect(2, 'ceef_hiteffH')
        HitAirUnblockable(3)
        StarterRating(0)

        def upon_OPPONENT_COUNTER_HIT():
            Hitstop(25)
            EnemyHitstopAddition(0, 0, 8)
            CommonSE('025_cleanhit_grap')
        CHAirUntechableTime(70)
        CHAirPushbackX(7500)
        CHAirPushbackY(90000)
        if SLOT_8:
            GroundedHitstunAnimation(13)
            AirHitstunAnimation(13)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_94:
                    if CheckInput(0x32):
                        if CheckInput(0x17):
                            clearUponHandler(EVERY_FRAME)
                            if SLOT_52:
                                sendToLabel(101)
                            else:
                                sendToLabel(1)
                elif CheckInput(0x17):
                    clearUponHandler(EVERY_FRAME)
                    if SLOT_52:
                        sendToLabel(101)
                    else:
                        sendToLabel(1)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        callSubroutine('Recovery_MutekiHP')
        if SLOT_137:
            DamageMultiplier(80)
    if SLOT_9:
        conditionalSendToLabel(100)
    sprite('ce401_00', 1)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    GuardPoint_(1)
    GuardpointBlockUnblockable(0)
    ArmorChipDamage(100)
    ArmorHealth(2500)
    GuardpointHitstop(-2, -1)
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    if SLOT_44:
        Voiceline('ce203')
    CreateObject('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_02', 1)
    SetActionMark(1)
    sprite('ce205_03', 3)
    CreateObject('mv401tameMatome', -1)
    PrivateSE('cese_07')
    PrivateSE('cese_07')
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    PrivateSE('cese_07')
    PrivateSE('cese_07')
    sprite('ce205_03', 3)
    sprite('ce205_03ex01', 2)
    sprite('ce205_03ex01', 1)
    AttackLevel_(5)
    Damage(1200)
    AttackP2(84)
    AirUntechableTime(52)
    CHAirUntechableTime(80)
    FatalCounter(1)
    if SLOT_137:
        DamageMultiplier(80)
    SLOT_53 = 1
    PrivateSE('cese_27')
    PrivateSE('cese_27')
    PrivateSE('cese_27')
    clearUponHandler(EVERY_FRAME)
    label(1)
    sprite('ce205_04', 2)
    TriggerUponForState('mv401tameMatome', 32)
    sprite('ce205_05', 2)
    if not SLOT_44:
        Voiceline('ce203')
    CommonSE('005_swing_grap_2_2')
    PrivateSE('cese_11')
    physicsXImpulse(15000)
    if SLOT_53:
        XSpeed(10000)
    sprite('ce205_06', 2)
    CreateObject('mv204Smoke', -1)
    CreateObject('mv205Eff', -1)
    XImpulseAcceleration(80)
    sprite('ce205_06', 2)
    XImpulseAcceleration(50)
    sprite('ce205_07', 9)
    SpriteIfNot0(8, 2, 53)
    AltKnockdownEffects(100, 1, 1)
    setInvincible(0)
    XImpulseAcceleration(50)
    sprite('ce205_08', 9)
    SpriteIfNot0(8, 2, 53)
    XImpulseAcceleration(50)
    sprite('ce205_09', 7)
    TriggerUponForState('mv205ConsentEff', 32)
    XImpulseAcceleration(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)
    ExitState()
    label(100)
    sprite('ce401_00', 1)
    Damage(1500)
    if SLOT_137:
        DamageMultiplier(80)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    GuardPoint_(1)
    GuardpointBlockUnblockable(0)
    GuardpointHitstop(-1, -1)
    SLOT_52 = 1
    SLOT_8 = 0
    CharacterFlash(14474340, 10, 2)
    sprite('ce401_01', 1)
    sprite('ce401_02', 2)
    if SLOT_44:
        Voiceline('ce203')
    CreateObject('mv205ConsentEff', 0)
    sprite('ce401_03', 1)
    setInvincible(1)
    sprite('ce401_04', 1)
    sprite('ce401_05', 1)
    sprite('ce401_05', 1)
    SetActionMark(1)
    sprite('ce401_06', 3)
    CreateObject('mv401tameMatome', -1)
    PrivateSE('cese_07')
    PrivateSE('cese_07')
    sprite('ce401_05ex00', 3)
    sprite('ce401_06ex00', 3)
    PrivateSE('cese_07')
    PrivateSE('cese_07')
    sprite('ce401_05ex01', 3)
    sprite('ce401_06ex01', 2)
    sprite('ce401_06ex01', 1)
    AttackLevel_(5)
    Damage(1800)
    if SLOT_137:
        DamageMultiplier(80)
    AttackP2(84)
    AirUntechableTime(52)
    CHAirUntechableTime(80)
    FatalCounter(1)
    SLOT_53 = 1
    PrivateSE('cese_27')
    PrivateSE('cese_27')
    PrivateSE('cese_27')
    clearUponHandler(EVERY_FRAME)
    label(101)
    sprite('ce401_07', 2)
    TriggerUponForState('mv401tameMatome', 32)
    sprite('ce401_08', 2)
    if not SLOT_44:
        Voiceline('ce203')
    CommonSE('005_swing_grap_2_2')
    PrivateSE('cese_11')
    physicsXImpulse(30000)
    if SLOT_53:
        XSpeed(10000)
        GotoState('AntiAir_Tame')
    sprite('ce401_09', 2)
    CreateObject('ce401PanchEff', -1)
    XImpulseAcceleration(80)
    sprite('ce401_09', 2)
    XImpulseAcceleration(50)
    sprite('ce401_10', 9)
    SpriteIfNot0(8, 2, 53)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 5000)
    setInvincible(0)
    XImpulseAcceleration(50)
    sprite('ce401_11', 9)
    SpriteIfNot0(8, 2, 53)
    XImpulseAcceleration(50)
    sprite('ce205_09', 7)
    TriggerUponForState('mv205ConsentEff', 32)
    XImpulseAcceleration(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)


@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        AttackP2(82)
        AirUntechableTime(45)
        Hitstop(16)
        HitOverhead(2)
        HitAirUnblockable(3)
        GroundedHitstunAnimation(9)
        AirPushbackY(-56000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(40)
        StarterRating(2)
        AttackDirection(0)
        SetYCollisionFromOrigin(240)
        SetXCollisionFromOrigin(200)
        DamageEffect(2, 'ceef_hiteffH')
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        callSubroutine('Recovery_MutekiHP')
        if SLOT_137:
            DamageMultiplier(80)
    if SLOT_9:
        conditionalSendToLabel(100)
    sprite('ce402_00', 2)
    sprite('ce402_01', 2)
    sprite('ce402_02', 3)
    sprite('ce235_00', 3)
    CreateObject('mv235ConsentEff', 0)
    sprite('ce235_01', 3)
    sprite('ce235_02', 3)
    setInvincible(1)
    SpecificInvincibility(1, 1, 0, 0, 0)
    GuardPoint_(1)
    ArmorChipDamage(100)
    ArmorHealth(1500)
    GuardpointHitstop(-2, -1)
    sprite('ce235_03', 3)
    sprite('ce235_04', 5)
    Voiceline('ce202')
    CommonSE('005_swing_grap_2_2')
    TriggerUponForState('mv235ConsentEff', 32)
    physicsXImpulse(60000)
    SetAcceleration(-7000)
    sprite('ce235_05', 5)
    PrivateSE('cese_22')
    CreateObject('mv235Eff', -1)
    TriggerUponForState('mv235ConsentEff', 33)
    AltKnockdownEffects(100, 1, 1)
    EndMomentum(1)
    SetYCollisionFromOrigin(100)
    SetXCollisionFromOrigin(100)
    sprite('ce235_06', 5)
    setInvincible(0)
    Recovery()
    sprite('ce235_07', 5)
    sprite('ce235_08', 5)
    sprite('ce235_09', 5)
    sprite('ce235_10', 4)
    ExitState()
    label(100)
    sprite('ce402_00', 3)
    Damage(1100)
    if SLOT_137:
        DamageMultiplier(80)
    AirUntechableTime(51)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    BouncePercentage(60)
    SLOT_52 = 1
    SLOT_8 = 0
    CharacterFlash(14474340, 10, 2)
    sprite('ce402_01', 3)
    sprite('ce402_02', 4)
    sprite('ce402_03', 3)
    CreateObject('mv235ConsentEff', 0)
    sprite('ce402_04', 3)
    setInvincible(1)
    SpecificInvincibility(1, 1, 0, 1, 0)
    GuardPoint_(1)
    GuardpointHitstop(-1, -1)
    sprite('ce402_05', 3)
    sprite('ce235_04', 5)
    Voiceline('ce202')
    CommonSE('005_swing_grap_2_2')
    CreateParticle('ceef_402_dashsmoke', 0)
    CreateParticle('ceef_402_dashsmoke', 1)
    TriggerUponForState('mv235ConsentEff', 32)
    physicsXImpulse(90000)
    SetAcceleration(-7000)
    sprite('ce402_06', 5)
    PrivateSE('cese_10')
    CreateObject('mv402Eff', -1)
    CreateParticle('ceef_402_stone', 0)
    TriggerUponForState('mv235ConsentEff', 33)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 5000)
    EndMomentum(1)
    SetYCollisionFromOrigin(100)
    SetXCollisionFromOrigin(100)
    sprite('ce402_07', 4)
    setInvincible(0)
    Recovery()
    sprite('ce402_08', 3)
    sprite('ce235_08', 3)
    sprite('ce235_09', 3)
    sprite('ce235_10', 3)


@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 400, 0)
        ObjectHitbox(11)
    if PreviousStateCheck('NmlAtk6C'):
        conditionalSendToLabel(1)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    Voiceline('ce200')
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    PrivateSE('cese_08')
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_01', 3)
    sprite('ce208_00', 3)
    ExitState()
    label(1)
    sprite('ce217_00', 5)
    sprite('ce217_01', 5)
    Voiceline('ce200')
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    PrivateSE('cese_08')
    sprite('ce217_04', 5)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 3)
    sprite('ce217_00', 3)


@State
def AirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1000)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        AirUntechableTime(20)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(-70000)
        HardKnockdown(1)
        EnableEmergencyTechAirHit(1)
        DamageEffect(2, 'ce404StarEff')
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        EndMomentum(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 401, 0)
    sprite('ce404_00', 3)
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    sprite('ce404_01', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    if SLOT_44:
        Voiceline('ce204')
    sprite('ce404_02', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('ce404_03', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('ce404_04', 2)
    XImpulseAcceleration(75)
    YAccel(75)
    if not SLOT_44:
        Voiceline('ce204')
    sprite('ce404_05', 3)
    CreateObject('ce404KickEff', 100)
    EndMomentum(1)
    physicsXImpulse(54000)
    physicsYImpulse(-63000)
    CommonSE('000_airdash_0')
    CommonSE('004_swing_grap_1_2')
    PrivateSE('cese_01')
    sprite('ce404_06', 3)
    label(0)
    sprite('ce404_05', 3)
    sprite('ce404_06', 3)
    gotoLabel(0)
    label(1)
    sprite('ce404_07', 4)
    TriggerUponForState('ce404KickEff', 32)
    clearUponHandler(LANDING)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    EndMomentum(1)
    Recovery()
    sprite('ce404_08', 4)
    sprite('ce404_09', 4)
    sprite('ce404_10', 4)
    sprite('ce404_11', 4)


@State
def UltimateHeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 100, 0)
    sprite('ce432_00', 3)
    CreateObject('ceef_healjunbieff', -1)
    Voiceline('ce256')
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('EMB_CE', -1)
    DistortionSettings(91, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    setInvincible(1)
    ObjectUpon2(11, 404, 0)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    TriggerUponForState('ceef_healjunbieff', 32)
    CreateObject('ceef_HealKurukuru', -1)
    sprite('ce432_01', 3)
    sprite('ce432_04', 6)
    sprite('ce432_05', 6)
    sprite('ce432_06', 6)
    sprite('ce432_07', 6)
    sprite('ce432_08', 6)
    sprite('ce432_09', 6)
    RunLoopUpon(17, 120)
    uponSendToLabel(17, 101)
    Voiceline('ce257')
    CreateObject('SuperHealEff', -1)
    PrivateFunction(3, 2, 8, 0, 30, 2, 51)

    def upon_EVERY_FRAME():
        if SLOT_21:
            if SLOT_8 > 0:
                if SLOT_8 >= SLOT_51:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_51
                    SLOT_8 = SLOT_8 - SLOT_51
                else:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_8
                    SLOT_8 = SLOT_8 - SLOT_8
            if not SLOT_CurrentHealth == SLOT_MaxHealth:
                AddToCurrentHP(10)
    label(100)
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    sprite('ce432_09', 6)
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 5)
    SetBackground(0)
    clearUponHandler(17)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('SuperHealEff', 32)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_8
    SLOT_8 = SLOT_8 - SLOT_8
    sprite('ce432_13', 5)
    sprite('ce432_14', 5)
    sprite('ce432_15', 5)


@State
def UltimateHealOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackType(4)
        PreventBlocking(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 100, 0)
    sprite('ce432_00', 3)
    CreateObject('ceef_healjunbieff', -1)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('ceef_HealJunbiAnim_R', -1)
    CreateObject('ceef_HealJunbiAnim_L', -1)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    sprite('ce432_01', 3)
    CreateObject('EMB_CE', -1)
    DistortionSettings(91, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    setInvincible(1)
    ObjectUpon2(11, 404, 0)
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    TriggerUponForState('ceef_healjunbieff', 32)
    CreateObject('ceef_HealKurukuru', -1)
    sprite('ce432_01', 3)
    sprite('ce432_04', 6)
    sprite('ce432_05', 6)
    sprite('ce432_06', 6)
    sprite('ce432_07', 6)
    sprite('ce432_08', 6)
    sprite('ce432_09', 6)
    RunLoopUpon(17, 102)
    uponSendToLabel(17, 101)
    Voiceline('ce257')
    CreateObject('SuperHealEffOD', -1)
    PrivateFunction(3, 2, 8, 0, 30, 2, 51)

    def upon_EVERY_FRAME():
        if SLOT_21:
            if SLOT_8 > 0:
                if SLOT_8 >= SLOT_51:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_51
                    SLOT_8 = SLOT_8 - SLOT_51
                else:
                    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_8
                    SLOT_8 = SLOT_8 - SLOT_8
            if not SLOT_CurrentHealth == SLOT_MaxHealth:
                AddToCurrentHP(10)
    label(100)
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    sprite('ce432_09', 6)
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 5)
    SetBackground(0)
    clearUponHandler(17)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('SuperHealEffOD', 32)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    SLOT_CurrentHealth = SLOT_CurrentHealth + SLOT_8
    SLOT_8 = SLOT_8 - SLOT_8
    sprite('ce432_13', 5)
    sprite('ce432_14', 5)
    sprite('ce432_15', 5)


@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 402, 0)
        ObjectHitbox(11)
        NoAttackDuringAction(1)
        setInvincible(1)
    sprite('ce208_00', 5)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_CE', -1)
    Voiceline('ce250')
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    setInvincible(0)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    Voiceline('ce251')
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    setInvincible(0)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)


@State
def UltimateShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 403, 0)
        ObjectHitbox(11)
        NoAttackDuringAction(1)
        setInvincible(1)
    sprite('ce208_00', 5)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_CE', -1)
    Voiceline('ce250')
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    setInvincible(0)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    if CharacterIDCheck('rg'):
        Voiceline('ce251')
    elif CharacterIDCheck('tm'):
        Voiceline('ce251')
    elif CharacterIDCheck('ph'):
        Voiceline('ce251')
    else:
        Voiceline('ce252')
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    setInvincible(0)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            clearUponHandler(EVERY_FRAME)
            CameraFast(1)
            CameraLookAtEnemy(1)
            CameraNoScreenCollision(1)
            WallCollisionDetection(0)
            sendToLabel(3)
        uponSendToLabel(33, 4)
        uponSendToLabel(32, 9)
        AttackLevel_(3)
        Damage(100)
        if SLOT_137:
            DamageMultiplier(80)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        OnlyHitPlayer(1)
        CallObject('CeMinervaLight')
        AirHitstunAnimation(4)
        AirUntechableTime(35)
        Hitstun(35)
        Hitstop(1)
        PushbackX(0)
        EnableRapidCancel(0)
        PassByArmor(1)
        AttackDirection(0)
        UseSlashHitspark(1)
        BlendMode_Normal()
        DamageFromStateOnly('UltimateAssaultAddAttack')

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            CameraNoCeiling(0)
            CameraNoScreenCollision(0)
            CameraControlInfinity(0)
            HUDVisibillity(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                PrivateFunction5(115)
                if SLOT_XDistanceFromCenterOfStage < SLOT_0:
                    sendToLabel(1)
            else:
                PrivateFunction5(115)
                if SLOT_XDistanceFromCenterOfStage > SLOT_0:
                    sendToLabel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('mv430_00', 5)
    setInvincible(1)
    BurstInvincibility(0)
    DistortionSettings(113, -1, 2)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    sprite('mv430_01', 5)
    CreateObject('mv430ConsentEff', 0)
    Voiceline('ce253')
    sprite('mv430_02', 3)
    CreateObject('ThrowUpCelica', -1)
    BurstInvincibility(1)
    sprite('mv430_03', 3)
    sprite('mv430_04', 8)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    CameraForAstralHeat(60, 120)
    sprite('mv430_05', 6)
    sprite('mv430_06', 6)
    sprite('mv430_07', 6)
    sprite('mv430_08', 6)
    sprite('mv430_09', 2)
    sprite('mv430_10', 8)
    CreateObject('HensinThunder', -1)
    TriggerUponForState('mv430ConsentEff', 32)
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)
    sprite('mv430_12', 10)
    physicsXImpulse(2500)
    EnableAfterimage(1)
    AfterimageInterval(3)
    AfterimageCount(3)
    AfterimageColor_1(200, 200, 250, 250)
    AfterimageColor_2(150, 150, 200, 200)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    sprite('mv430_13', 10)
    XImpulseAcceleration(200)
    CameraNoCeiling(0)
    CameraNoScreenCollision(0)
    CameraControlInfinity(0)
    sprite('mv430_14', 10)
    DespawnEAEffect('HensinThunder')
    XImpulseAcceleration(200)
    AlphaValue(255)
    ConstantAlphaModifier(-21)
    sprite('mv430_15', 3)
    AlphaValue(64)
    ConstantAlphaModifier(0)
    StartMultihit()
    AirDashEffects(1)
    PrivateSE('cese_09')
    EnableCollision(0)
    SetXCollisionFromOrigin(250)
    WallCollisionDetection(0)
    ScreenCollision(0)
    sprite('mv430_15', 60)
    EnableAfterimage(0)
    XImpulseAcceleration(900)
    SetAcceleration(1000)
    label(1)
    sprite('null', 5)
    Flip()
    EndMomentum(1)
    SetPosXByScreenPer(0)
    EnableCollision(1)
    SetXCollisionFromOrigin(100)
    WallCollisionDetection(1)
    ScreenCollision(1)
    sprite('null', 15)
    SetBackground(0)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 12)
    SetPosYByScreenPer(40)
    physicsYImpulse(-30000)
    EndYPhysicsImpulse()
    ConstantAlphaModifier(21)
    label(11)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)
    Voiceline('ce254')
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    AlphaValue(255)
    setInvincible(0)
    sprite('ce024_01', 4)
    sprite('ce024_02', 4)
    sprite('ce024_03', 6)
    sprite('ce024_04', 6)
    ExitState()
    label(3)
    sprite('mv430_15', 5)
    AlphaValue(64)
    ConstantAlphaModifier(-12)
    StartMultihit()
    SetAcceleration(0)
    SetXCollisionFromOrigin(150)
    sprite('mv430_15', 25)
    physicsXImpulse(0)
    Visibility(1)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('null', 130)
    CreateObject('ShungokuEff', -1)
    HUDVisibillity(1)
    CreateObject('UltimateAssaultAddAttack', -1)

    def RunOnObject_22():
        Visibility(1)
        AlphaValue(0)
    label(4)
    sprite('mv430_15', 2)
    RefreshMultihit()
    Damage(2000)
    if SLOT_137:
        DamageMultiplier(80)
    DefeatOpponentBehavior(0)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Crumple(9999)
    Stagger(40)
    Hitstop(0)
    DamageEffect(5, '')
    AlphaValue(255)
    Visibility(0)

    def RunOnObject_22():
        AlphaValue(255)
        Visibility(0)
    physicsXImpulse(30000)
    GotoState('UltimateAssaultFinish')
    sprite('mv430_15', 1)
    sprite('mv430_20', 6)
    DespawnEAEffect('ShungokuEff')
    HUDVisibillity(0)
    SetBackground(0)
    WallCollisionDetection(1)
    ScreenCollision(1)
    XImpulseAcceleration(130)
    CameraLookAtEnemy(0)
    CameraNoScreenCollision(0)
    CameraControlInfinity(0)
    sprite('mv430_21', 8)
    XImpulseAcceleration(50)
    sprite('mv430_22', 10)
    XImpulseAcceleration(50)
    sprite('mv430_22', 10)
    XImpulseAcceleration(50)
    sprite('mv430_23', 6)
    XImpulseAcceleration(50)
    sprite('mv430_24', 6)
    XImpulseAcceleration(50)
    sprite('mv430_19', 180)
    Flip()
    WhiffCrouchBlockCancel(1)
    CreateObject('ThrowDownCelica', -1)
    XImpulseAcceleration(0)
    label(9)
    sprite('ce024_02', 1)
    Voiceline('ce254')
    clearUponHandler(32)
    EnableRapidCancel(0)
    EnableCollision(1)
    setInvincible(0)
    CommonSE('024_getset_a')
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    sprite('ce024_04', 5)
    sprite('ce024_05', 5)


@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            clearUponHandler(EVERY_FRAME)
            CameraFast(1)
            CameraLookAtEnemy(1)
            CameraNoScreenCollision(1)
            WallCollisionDetection(0)
            sendToLabel(3)
        uponSendToLabel(33, 4)
        uponSendToLabel(32, 9)
        AttackLevel_(3)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        OnlyHitPlayer(1)
        CallObject('CeMinervaLight')
        AirHitstunAnimation(4)
        AirUntechableTime(25)
        Hitstun(25)
        Hitstop(1)
        PushbackX(0)
        EnableRapidCancel(0)
        PassByArmor(1)
        AttackDirection(0)
        UseSlashHitspark(1)
        BlendMode_Normal()
        DamageEffect(5, '')
        DamageFromStateOnly('UltimateAssaultOD')

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            CameraNoCeiling(0)
            CameraNoScreenCollision(0)
            CameraControlInfinity(0)
            HUDVisibillity(0)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                PrivateFunction5(115)
                if SLOT_XDistanceFromCenterOfStage < SLOT_0:
                    sendToLabel(1)
            else:
                PrivateFunction5(115)
                if SLOT_XDistanceFromCenterOfStage > SLOT_0:
                    sendToLabel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('mv430_00', 5)
    setInvincible(1)
    BurstInvincibility(0)
    DistortionSettings(113, -1, 2)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    sprite('mv430_01', 5)
    CreateObject('mv430ConsentEff', 0)
    Voiceline('ce253')
    sprite('mv430_02', 3)
    CreateObject('ThrowUpCelica', -1)
    BurstInvincibility(1)
    sprite('mv430_03', 3)
    sprite('mv430_04', 8)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    CameraForAstralHeat(60, 120)
    sprite('mv430_05', 6)
    sprite('mv430_06', 6)
    sprite('mv430_07', 6)
    sprite('mv430_08', 6)
    sprite('mv430_09', 2)
    sprite('mv430_10', 8)
    TriggerUponForState('mv430ConsentEff', 32)
    CreateObject('HensinThunder', -1)
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)
    sprite('mv430_12', 10)
    physicsXImpulse(2500)
    EnableAfterimage(1)
    AfterimageInterval(3)
    AfterimageCount(3)
    AfterimageColor_1(200, 200, 250, 250)
    AfterimageColor_2(150, 150, 200, 200)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    sprite('mv430_13', 10)
    XImpulseAcceleration(200)
    CameraNoCeiling(0)
    CameraNoScreenCollision(0)
    CameraControlInfinity(0)
    sprite('mv430_14', 10)
    DespawnEAEffect('HensinThunder')
    XImpulseAcceleration(200)
    AlphaValue(255)
    ConstantAlphaModifier(-12)
    sprite('mv430_15', 3)
    AlphaValue(128)
    ConstantAlphaModifier(0)
    StartMultihit()
    AirDashEffects(1)
    PrivateSE('cese_09')
    EnableCollision(0)
    SetXCollisionFromOrigin(250)
    WallCollisionDetection(0)
    ScreenCollision(0)
    sprite('mv430_15', 60)
    EnableAfterimage(0)
    XImpulseAcceleration(900)
    SetAcceleration(1000)
    label(1)
    sprite('null', 5)
    Flip()
    EndMomentum(1)
    SetPosXByScreenPer(0)
    EnableCollision(1)
    SetXCollisionFromOrigin(100)
    WallCollisionDetection(1)
    ScreenCollision(1)
    sprite('null', 15)
    SetBackground(0)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 12)
    SetPosYByScreenPer(40)
    physicsYImpulse(-30000)
    EndYPhysicsImpulse()
    ConstantAlphaModifier(21)
    label(11)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)
    Voiceline('ce254')
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    AlphaValue(255)
    setInvincible(0)
    sprite('ce024_01', 4)
    sprite('ce024_02', 4)
    sprite('ce024_03', 6)
    sprite('ce024_04', 6)
    ExitState()
    label(3)
    sprite('mv430_20', 1)
    physicsXImpulse(90000)
    SetAcceleration(0)
    AddCombo(1)
    sprite('mv430_20', 1)
    AddCombo(1)
    sprite('mv430_20', 1)
    AddCombo(1)
    sprite('mv430_21', 3)
    CreateObject('ShungokuODSlashEff', -1)
    sprite('mv430_22', 2)
    XImpulseAcceleration(30)
    sprite('mv430_22', 4)
    XImpulseAcceleration(50)
    sprite('mv430_15', 1)
    RefreshMultihit()
    AirUntechableTime(40)
    Hitstun(40)
    UseSlashHitspark(1)
    HitsparkSize(700)
    Flip()
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('mv430_20', 1)
    physicsXImpulse(90000)
    AddCombo(1)
    sprite('mv430_20', 1)
    AddCombo(1)
    sprite('mv430_20', 1)
    AddCombo(1)
    CreateObject('ShungokuODSlashEff2', -1)
    sprite('mv430_21', 3)
    XImpulseAcceleration(25)
    sprite('mv430_22', 2)
    XImpulseAcceleration(50)
    sprite('mv430_22', 1)
    sprite('mv430_22', 22)
    sprite('mv430_15', 3)
    uponSendToLabel(OPPONENT_HIT, 100)
    Flip()
    physicsXImpulse(9000)
    StartMultihit()
    sprite('mv430_15', 15)
    XImpulseAcceleration(1500)
    RefreshMultihit()
    Hitstop(0)
    CreateObject('ShungokuODSlashEff3', -1)
    DamageEffect(5, '')
    DamageFromStateOnly('UltimateAssaultAddAttackOD')
    sprite('keep', 1)
    sendToLabel(1)
    label(100)
    sprite('mv430_15', 3)
    clearUponHandler(OPPONENT_HIT)
    AlphaValue(64)
    ConstantAlphaModifier(-21)
    StartMultihit()
    SetXCollisionFromOrigin(150)
    sprite('mv430_15', 25)
    physicsXImpulse(0)
    Visibility(1)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('null', 130)
    CreateObject('ShungokuEff', -1)
    HUDVisibillity(1)
    CreateObject('UltimateAssaultAddAttackOD', -1)
    CreateObject('ShungokuODFinishEff', -1)

    def RunOnObject_22():
        Visibility(1)
        AlphaValue(0)
        ConstantAlphaModifier(0)
    label(4)
    sprite('mv430_15', 2)
    RefreshMultihit()
    Damage(2000)
    if SLOT_137:
        DamageMultiplier(80)
    MinimumDamage(35)
    DefeatOpponentBehavior(0)
    AttackType(4)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Crumple(9999)
    Stagger(40)
    Visibility(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)

    def RunOnObject_22():
        AlphaValue(255)
        ConstantAlphaModifier(0)
        Visibility(0)
    physicsXImpulse(30000)
    GotoState('UltimateAssaultODFinish')
    sprite('mv430_15', 1)
    sprite('mv430_20', 6)
    DespawnEAEffect('ShungokuEff')
    HUDVisibillity(0)
    SetBackground(0)
    WallCollisionDetection(1)
    ScreenCollision(1)
    XImpulseAcceleration(130)
    CameraLookAtEnemy(0)
    CameraNoScreenCollision(0)
    CameraControlInfinity(0)
    sprite('mv430_21', 8)
    XImpulseAcceleration(50)
    sprite('mv430_22', 10)
    XImpulseAcceleration(50)
    sprite('mv430_22', 10)
    XImpulseAcceleration(50)
    sprite('mv430_23', 6)
    XImpulseAcceleration(50)
    sprite('mv430_24', 6)
    XImpulseAcceleration(50)
    sprite('mv430_19', 180)
    Flip()
    WhiffCrouchBlockCancel(1)
    CreateObject('ThrowDownCelica', -1)
    XImpulseAcceleration(0)
    label(9)
    sprite('ce024_02', 1)
    Voiceline('ce254')
    clearUponHandler(32)
    EnableRapidCancel(0)
    EnableCollision(1)
    setInvincible(0)
    CommonSE('024_getset_a')
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    sprite('ce024_04', 5)
    sprite('ce024_05', 5)


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
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('MinervaAtkBurstDD')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(0)
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('ce040_00ex01', 6)
    Voiceline('ce280')
    setInvincible(1)
    EndMomentum(1)
    E0EAEffect('BurstDDeff', 103)
    sprite('ce040_01ex01', 6)
    sprite('ce312_00ex01', 4)
    sprite('ce312_01ex01', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('ce312_02ex01', 3)
    sprite('ce312_02ex01', 3)
    AttackOff()
    setInvincible(0)
    sprite('ce312_03ex01', 10)
    sprite('ce312_04ex01', 6)
    sprite('ce312_05ex01', 6)
    sprite('ce312_06ex01', 6)
    sprite('ce312_07ex01', 3)


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
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('MinervaAtkBurstDD')
        MinimumDamage(10)

        def upon_OPPONENT_HIT():
            PushbackX(0)
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
    sprite('ce040_00ex01', 3)
    Voiceline('ce280')
    setInvincible(1)
    EndMomentum(1)
    E0EAEffect('BurstDDeff', 103)
    sprite('ce040_01ex01', 2)
    sprite('ce312_00ex01', 2)
    sprite('ce312_01ex01', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('ce312_02ex01', 3)
    sprite('ce312_02ex01', 3)
    AttackOff()
    setInvincible(0)
    sprite('ce312_03ex01', 10)
    sprite('ce312_04ex01', 6)
    sprite('ce312_05ex01', 6)
    sprite('ce312_06ex01', 6)
    sprite('ce312_07ex01', 3)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(41, 9)
        SetBackground(1)

        def upon_STATE_END():
            PreventSelfPush(0)
            DespawnEAEffect('BurstDD_Camera')
        CreateObject('BurstDD_Camera', -1)
    sprite('ce312_03ex01', 3)
    sprite('ce312_04ex01', 3)
    sprite('ce312_05ex01', 3)
    sprite('ce312_06ex01', 3)
    sprite('ce312_07ex01', 3)
    sprite('ce207_00ex01', 3)
    callSubroutine('MinervaCallAttack')
    ObjectUpon2(11, 450, 0)
    ObjectHitbox(11)
    NoAttackDuringAction(1)
    PreventSelfPush(1)
    label(0)
    sprite('ce207_01ex01', 5)
    sprite('ce207_02ex01', 5)
    sprite('ce207_03ex01', 5)
    sprite('ce207_04ex01', 5)
    gotoLabel(0)
    label(1)
    sprite('ce207_00ex01', 4)
    Voiceline('ce281')
    sprite('ce217_00', 4)
    label(11)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    gotoLabel(11)
    label(2)
    sprite('ce217_00', 4)
    sprite('ce218_00', 4)
    label(21)
    sprite('ce218_01', 5)
    sprite('ce218_02', 5)
    sprite('ce218_03', 5)
    sprite('ce218_04', 5)
    gotoLabel(21)
    label(3)
    sprite('ce218_00', 4)
    sprite('ce208_00ex01', 4)
    label(31)
    sprite('ce208_01ex01', 5)
    sprite('ce208_02ex01', 5)
    sprite('ce208_03ex01', 5)
    sprite('ce208_04ex01', 5)
    gotoLabel(31)
    label(9)
    sprite('ce440_00', 4)
    Voiceline('ce282')
    physicsXImpulse(-3000)
    sprite('ce440_01', 4)
    XImpulseAcceleration(200)
    sprite('ce440_02', 4)
    sprite('ce440_03', 4)
    XImpulseAcceleration(80)
    sprite('ce440_04', 4)
    XImpulseAcceleration(80)
    sprite('ce440_05', 4)
    XImpulseAcceleration(80)
    sprite('ce440_06', 4)
    XImpulseAcceleration(80)
    sprite('ce440_07', 4)
    EndMomentum(1)
    sprite('ce440_08', 20)
    CrouchState(1)
    sprite('ce440_09', 6)
    sprite('ce440_10', 6)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(2100)
        Crumple(2000)
        AirUntechableTime(500)
        PushbackX(30000)
        Hitstop(0)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(0)
        OppPositionOnHit(1, 100000, 0)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeatExe')
        DamageEffect(5, '')
        EnterStateIfEventID(12, 'AstralHeatExe')
        IgnoreScreenfreeze(1)
        EndMomentum(1)
        setInvincible(1)
        AttackOff()
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 100, 0)
    sprite('ce450_00', 6)
    sprite('ce450_01', 4)
    Voiceline('ce290')
    DistortionSettings(52, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_CE_AH', -1)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    CreateObject('ceef450_Kousoku', -1)
    RefreshMultihit()
    CommonSE('022_magiccircle_a')
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    AttackOff()
    setInvincible(0)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_28', 5)
    sprite('ce450_29', 5)
    sprite('ce450_23', 5)
    sprite('ce450_24', 5)
    sprite('ce450_25', 5)
    sprite('ce450_26', 5)
    LandingEffects(100, 1, 1)
    sprite('ce450_27', 5)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(0)
        MinimumDamage(100)
        IgnoreComboTime(1)
        Hitstop(0)
        DefeatOpponentBehavior(1)
        AirPushbackX(1000)
        AirPushbackY(-50000)
        HardKnockdown(150)
        PassByArmor(1)
        OppPositionOnHit(1, 50000, 100000)
        EnableCollision(0)
        AstralHeatCleanup(1, 1)
        PlayPlayAstralBGM(0)
        CameraNoCeiling(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        CameraWinnerControlStop(1)
        WallCollisionDetection(0)
        ScreenCollision(0)
        AttackOff()
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 500, 0)
        ObjectHitbox(11)
        CommonSE('107_throw_catch')

        def upon_48():
            if SLOT_2:

                def RunOnObject_22():
                    AddToCurrentHP(100)
    sprite('ce450_02', 5)
    TriggerUponForState('ceef450_Kousoku', 32)
    sprite('ce450_03', 5)
    sprite('ce450_04', 5)
    sprite('ce450_05', 5)
    sprite('ce450_06', 5)
    Voiceline('ce291')
    sprite('ce450_07', 5)
    sprite('ce450_08', 5)
    sprite('ce450_09', 5)
    sprite('ce450_10', 5)
    sprite('ce450_11', 5)
    sprite('ce450_12', 5)
    sprite('ce450_13', 5)
    sprite('ce450_14', 5)
    sprite('ce450_15', 5)
    SetActionMark(1)
    CreateObject('ceef450_BG', -1)
    PrivateSE('cese_03')
    TriggerUponForState('ceef450_Kousoku', 33)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    Voiceline('ce292')
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    Voiceline('ce293')
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    TriggerUponForState('ceef450_BG', 32)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    CameraControlEnable(0)
    sprite('ce450_15', 5)
    CreateObject('AstCameraObj', -1)
    RegisterObject(4, 1)
    sprite('ce450_16', 30)
    BlendMode_Normal()
    ConstantAlphaModifier(-26)
    SetActionMark(0)

    def RunOnObject_22():
        AddToCurrentHP(100000)
        BlendMode_Normal()
        ConstantAlphaModifier(-26)
        AbsoluteY(100000000)
        setGravity(0)
    SetBackground(3)
    HUDVisibillity(1)
    sprite('ce450_16', 260)
    CreateObject('AHCamera', -1)
    CreateObject('AHKiraEff', -1)
    sprite('ce450_16', 10)
    SetBackground(2)
    sprite('ce450_16', 25)

    def RunOnObject_22():
        AbsoluteY(0)
    TriggerUponForState('AHCamera', 32)
    sprite('ce450_16', 10)
    sprite('ce450_16', 5)
    CreateObject('ceef450_BG3', -1)
    ConstantAlphaModifier(26)

    def RunOnObject_22():
        BlendMode_Normal()
        ConstantAlphaModifier(26)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    Voiceline('ce294')
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    RefreshMultihit()
    DisableOppPushCollision(1)
    OppPositionOnHit(0, -1, -1)
    DamageEffect(2, 'ceef_hiteffAst')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(-200000)
    AirPushbackY(50000)
    AirUntechableTime(200)
    HardKnockdown(200)
    Hitstop(60)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    CreateObject('mv450HanaTiri', -1)
    CreateObject('mv450SmokeMato', -1)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    CreateObject('AstDeathAttack', -1)
    CreateObject('mv450WhiteOut', -1)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    ObjectUpon(FALLING, 32)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_22', 5)
    XPositionRelativeFacing(260000)
    sprite('ce450_23', 5)
    sprite('ce450_24', 5)
    sprite('ce450_25', 5)
    sprite('ce450_26', 5)
    LandingEffects(100, 1, 1)
    sprite('ce450_27', 5)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    label(100)
    sprite('ce000_00', 50)
    TriggerUponForState('ceef450_BG3', 32)
    TriggerUponForState('AHCamera', 33)
    sprite('ce620_00', 8)
    WinAction()
    Voiceline('ce295')
    sprite('ce620_01', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    sprite('ce620_04', 8)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce000_00', 8)
    sprite('ce610_00', 8)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 75)
    sprite('ce610_05', 32767)
    EndDemo()
    loopRest()


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('ce054')
    sprite('ce900_00', 32767)
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
    sprite('ce901_00', 6)
    physicsYImpulse(-150)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    physicsYImpulse(150)
    Voiceline('ce055')
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    label(0)
    sprite('ce901_00', 6)
    physicsYImpulse(-150)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    physicsYImpulse(150)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    sprite('ce901_00', 6)
    sprite('ce901_01', 6)
    sprite('ce901_02', 6)
    gotoLabel(0)


@Subroutine
def MouthTableInit():
    Unknown18011('ce000', 13921, 13923, 13921, 13923, 12897, 25396, 54, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce055', 13153, 25392, 12849, 13921, 13923, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce400', 13921, 13923, 13921, 13923, 13921, 13155, 24886, 
        25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
        24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ce401', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce404', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 13153, 48, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce405', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 12899, 24880, 25398, 
        24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce406', 13921, 13923, 13921, 13923, 13921, 13155, 24880, 
        25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
        24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce407', 13921, 13923, 13921, 13923, 13921, 12899, 24881, 
        25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce408', 13921, 13155, 24880, 25398, 24887, 25399, 24886, 
        25398, 14389, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ce411', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce412', 13921, 13923, 13921, 13923, 13921, 12643, 24888, 
        25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce414', 12897, 25396, 24889, 25398, 24886, 25398, 12342, 
        12641, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce415', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce416', 13921, 13923, 13921, 13923, 12643, 24888, 25398, 
        24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 14389, 
        13921, 13923, 13921, 13923, 24880, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ce417', 13921, 13923, 13921, 13923, 13921, 13923, 24886, 
        49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('ce000', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 14433, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ce055', 13153, 25392, 12849, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce400', 13921, 13923, 13921, 13155, 24888, 25398, 
            24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
            25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce401', 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce404', 13923, 24880, 25398, 24886, 25398, 24886, 
            25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce405', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 12899, 24880, 
            25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce406', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ce407', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 12899, 24880, 25398, 24886, 25398, 24886, 25398, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ce408', 13921, 13411, 24880, 25398, 24886, 25398, 
            24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ce411', 12897, 25395, 13364, 13921, 13923, 13921, 
            13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce412', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 12643, 24885, 25398, 24886, 25398, 24886, 25398, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ce414', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24880, 
            49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ce415', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 48, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('ce416', 13921, 13923, 13921, 13155, 24886, 25398, 
            24886, 25398, 24886, 25398, 24886, 25398, 12340, 12641, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ce417', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 12899, 24880, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rg'):
            Unknown18011('ce000', 14177, 12899, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ce400', 14433, 14435, 14433, 12899, 24885, 25400,
                24888, 25400, 24888, 25400, 24888, 12337, 14435, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 12899, 24880, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('ce000', 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce400', 14177, 14179, 14177, 13155, 24880, 25399,
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('ce401', 14177, 13411, 24885, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('ce000', 14177, 14179, 14177, 12643, 24885, 25399,
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce400', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('ce401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 12643, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('ce000', 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce400', 14177, 14179, 14177, 13155, 24880, 25399,
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('ce401', 14177, 13411, 24885, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            if SLOT_138:
                Unknown18011('ce500', 12897, 25392, 24886, 25398, 24886, 
                    25398, 24886, 25398, 24886, 25398, 14386, 13921, 13923,
                    13921, 13923, 13921, 12899, 24880, 25398, 24886, 25398,
                    24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce501', 13921, 13923, 13921, 12899, 24880, 
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 12341,
                    13921, 13923, 13921, 13923, 13921, 12899, 24880, 25398,
                    24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('ce500', 13921, 13667, 13921, 13667, 13921, 
                    12899, 24884, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce501', 14433, 12643, 24885, 25398, 24886, 
                    13618, 12899, 24885, 25399, 24887, 25399, 24887, 25399,
                    24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('ce502', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 
                24885, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce503', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13411, 24885, 25400, 
                24886, 25401, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ca'):
            Unknown18011('ce519', 13921, 13923, 24880, 25398, 24886, 25398,
                24886, 25398, 12340, 13921, 13923, 13921, 99, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ce520', 13921, 13923, 13921, 13923, 13921, 13411,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                12339, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            if SLOT_140:
                Unknown18011('ce519', 13921, 13923, 13921, 13923, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    13411, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce520', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13155, 24885, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('ce520', 13921, 13923, 13921, 13923, 13921, 12899,
                24880, 25398, 24886, 25398, 24886, 25398, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ce521', 13921, 13923, 13921, 13667, 24887, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('ce532', 13921, 13923, 13921, 13923, 13921, 13155,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce533', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13155, 
                25397, 24886, 25398, 24886, 24886, 25398, 12339, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('pt'):
            if SLOT_138:
                Unknown18011('ce534', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 14179, 24880, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce535', 13921, 13923, 13921, 13923, 13921, 
                    13923, 24880, 25398, 24886, 25398, 24886, 25398, 12339,
                    13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0)
            else:
                Unknown18011('ce534', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13155, 24880,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('ce535', 12641, 25392, 24886, 25398, 24886, 
                    25398, 24886, 25398, 24886, 25398, 13362, 13921, 13923,
                    14433, 12643, 24880, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('ce546', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13411, 24880, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce547', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13155, 24885, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ce546', 13921, 13923, 13921, 13923, 13921, 
                    13155, 24885, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 12337, 13923,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
                Unknown18011('ce547', 12641, 25400, 13618, 13921, 13923, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('ce548', 14433, 13923, 14433, 13923, 13921, 13923,
                13921, 13923, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce549', 12641, 25392, 24886, 12337, 13923, 12641,
                25392, 24886, 12337, 13923, 13921, 13923, 13153, 25392, 
                13620, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 99,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('ce550', 13921, 13923, 13921, 13923, 13921, 13923,
                24885, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce551', 13921, 13923, 13921, 13411, 24885, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            if SLOT_138:
                Unknown18011('ce558', 13921, 13923, 13921, 13923, 13921, 
                    13923, 24885, 25398, 24886, 25398, 24886, 25398, 25398,
                    12341, 13921, 13923, 13921, 13411, 24885, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce559', 13921, 13923, 13921, 14435, 24880, 
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('ce558', 13665, 13667, 13665, 13667, 13665, 
                    13411, 24880, 25398, 24886, 25398, 24886, 25398, 12340,
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ce559', 13921, 13923, 13921, 14435, 24880, 
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('ce564', 14177, 14179, 14177, 13667, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 25399, 24885, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce565', 14177, 14179, 14177, 14179, 14177, 14179,
                24880, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('ce570', 14177, 12899, 24880, 25399, 24887, 25399,
                24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ce571', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 13617, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 
                25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)


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
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('ca'):
        if SLOT_140:
            gotoLabel(2190)
        else:
            gotoLabel(190)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('vh'):
        SyncEntry()
        gotoLabel(260)
    if CharacterIDCheck('pt'):
        SyncEntry()
        if SLOT_138:
            gotoLabel(270)
        else:
            gotoLabel(1270)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('kk'):
        SyncEntry()
        gotoLabel(340)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ph'):
        if SLOT_138:
            gotoLabel(390)
        else:
            gotoLabel(1390)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('ce020_07', 1)
    Visibility(1)
    AbsoluteY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        gotoLabel(0)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 2)
    Visibility(0)
    physicsYImpulse(-40000)
    label(1)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(1)
    label(2)
    sprite('ce024_00', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    sprite('ce600_00', 6)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 6)
    Voiceline('ce412')
    label(3)
    sprite('ce600_01ex1', 3)
    if SLOT_97:
        conditionalSendToLabel(3)
    sprite('ce600_02', 8)
    loopRest()
    ExitState()
    label(10)
    sprite('ce601_00', 3)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('ce601_00', 1)
    Voiceline('ce416')
    label(11)
    sprite('ce601_00', 3)
    if SLOT_97:
        conditionalSendToLabel(11)
    sprite('ce601_01', 6)
    sprite('ce601_02', 6)
    ObjectUpon2(11, 601, 0)
    sprite('ce601_03', 62)
    Voiceline('ce417')
    sprite('ce601_04', 6)
    sprite('ce601_05', 4)
    sprite('ce601_06', 4)
    sprite('ce601_07', 6)
    ExitState()
    label(20)
    sprite('ce601_00', 3)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('ce601_00', 1)
    Voiceline('ce414')
    label(21)
    sprite('ce601_00', 3)
    if SLOT_97:
        conditionalSendToLabel(21)
    sprite('ce601_01', 6)
    sprite('ce601_02', 6)
    ObjectUpon2(11, 601, 0)
    sprite('ce601_03', 62)
    Voiceline('ce415')
    sprite('ce601_04', 6)
    sprite('ce601_05', 4)
    sprite('ce601_06', 4)
    sprite('ce601_07', 6)
    ExitState()
    label(100)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(101)
    sprite('ce010_02', 7)
    sprite('ce010_03', 7)
    sprite('ce010_04', 7)
    sprite('ce010_05', 7)
    sprite('ce010_06', 7)
    sprite('ce010_07', 7)
    sprite('ce010_08', 7)
    sprite('ce010_09', 7)
    if SLOT_17:
        conditionalSendToLabel(101)
    sprite('ce010_01', 5)
    Voiceline('ce500')
    sprite('ce010_00', 5)
    sprite('ce000_00', 5)
    sprite('ce208_00', 5)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    sprite('ce208_03', 7)
    sprite('ce208_04', 7)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    sprite('ce208_03', 7)
    sprite('ce208_04', 7)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    sprite('ce208_03', 7)
    sprite('ce208_04', 7)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    sprite('ce208_03', 7)
    sprite('ce208_04', 7)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    sprite('ce208_03', 7)
    sprite('ce208_04', 7)
    sprite('ce208_01', 7)
    sprite('ce208_02', 7)
    ObjectUpon2(11, 608, 0)
    sprite('ce208_00', 5)
    loopRest()
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    ObjectUpon(22, 32)
    ExitState()
    label(1100)
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    XPositionRelativeFacing(-12800000)
    label(1101)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1101)
    sprite('null', 20)
    sprite('ce000_00ex999', 25)
    Voiceline('ce500')
    SLOT_51 = 1
    XPositionRelativeFacing(-800000)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 602, 0)
    CreateObject('EntryCelicaDummy', -1)
    RegisterObject(4, 1)
    sprite('ce000_00ex999', 10)
    CreateObject('EntryCable', 109)
    RegisterObject(5, 1)
    sprite('ce000_00ex999', 2)
    ObjectUpon(5, 32)
    sprite('ce000_00ex999', 10)
    ObjectUpon(FALLING, 32)
    sprite('ce000_00ex999', 80)
    sprite('ce000_00ex999', 80)
    ObjectUpon(22, 32)
    sprite('ce000_00ex999', 37)
    physicsXImpulse(11000)
    TriggerUponForState('MinervaEntry02', 33)
    sprite('ce602_12', 5)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    ObjectUpon(FALLING, 33)
    SLOT_51 = 0
    TriggerUponForState('MinervaEntry02', 34)
    sprite('ce000_11', 5)
    loopRest()
    ExitState()
    label(110)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    uponSendToLabel(32, 112)
    sprite('ce603_00', 6)
    label(111)
    sprite('ce603_00', 6)
    gotoLabel(111)
    label(112)
    sprite('ce603_00', 5)
    clearUponHandler(32)
    Voiceline('ce502')
    DemoTimer(200)
    label(113)
    sprite('ce603_00', 5)
    if SLOT_97:
        conditionalSendToLabel(113)
    sprite('ce603_00', 6)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(190)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    uponSendToLabel(32, 192)
    sprite('ce603_00', 6)
    label(191)
    sprite('ce603_00', 6)
    gotoLabel(191)
    label(192)
    sprite('ce603_00', 5)
    clearUponHandler(32)
    Voiceline('ce519')
    DemoTimer(200)
    label(113)
    sprite('ce603_00', 5)
    if SLOT_97:
        conditionalSendToLabel(113)
    sprite('ce603_00', 6)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2190)
    sprite('ce603_00', 6)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(2191)
    sprite('ce603_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2191)
    label(2191)
    sprite('ce603_00', 20)
    sprite('ce603_00', 200)
    Voiceline('ce519')
    sprite('ce603_00', 6)
    ObjectUpon2(11, 608, 0)
    ObjectUpon(22, 32)
    sprite('ce603_01', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(200)
    sprite('ce020_07', 1)
    Visibility(1)
    AbsoluteY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(200)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 202)
    Visibility(0)
    physicsYImpulse(-40000)
    label(201)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(201)
    label(202)
    sprite('ce024_00', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    sprite('ce600_00', 6)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 20)
    sprite('ce600_02', 8)
    loopRest()
    loopRest()
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    Voiceline('ce520')
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    ObjectUpon(22, 32)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    ExitState()
    label(260)
    sprite('ce020_07', 1)
    Visibility(1)
    AbsoluteY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(260)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 262)
    Visibility(0)
    physicsYImpulse(-40000)
    label(261)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(261)
    label(262)
    sprite('ce024_00', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    sprite('ce600_00', 6)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 20)
    sprite('ce600_02', 8)
    loopRest()
    loopRest()
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    Voiceline('ce532')
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(270)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    label(271)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(271)
    label(272)
    SLOT_4 = 0
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    sprite('ce300_05', 15)
    Voiceline('ce534')
    DemoTimer(260)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 15)
    sprite('ce300_06ex', 90)
    sprite('ce300_06ex', 5)
    sprite('ce300_07', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(1270)
    sprite('ce603_00', 1)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(1271)
    sprite('ce603_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1271)
    sprite('ce603_00', 10)
    sprite('ce603_00', 160)
    Voiceline('ce534')
    sprite('ce603_00', 20)
    sprite('ce603_00', 5)
    ObjectUpon(22, 32)
    uponSendToLabel(32, 1273)
    label(1272)
    sprite('ce603_00', 1)
    loopRest()
    gotoLabel(1272)
    label(1273)
    sprite('ce603_00', 6)
    clearUponHandler(32)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    uponSendToLabel(32, 332)
    label(331)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(331)
    label(332)
    SLOT_4 = 0
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    sprite('ce300_05', 15)
    Voiceline('ce546')
    DemoTimer(260)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 15)
    sprite('ce300_06ex', 90)
    sprite('ce300_06ex', 5)
    ObjectUpon(22, 32)
    sprite('ce300_07', 6)
    loopRest()
    ExitState()
    label(2330)
    sprite('null', 1)
    callSubroutine('MinervaCall')
    uponSendToLabel(32, 2332)
    label(2331)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(2331)
    label(2332)
    sprite('ce610_00', 6)
    sprite('ce610_01', 6)
    sprite('ce610_02', 6)
    sprite('ce610_03', 6)
    sprite('ce610_04', 7)
    sprite('ce610_05', 180)
    Voiceline('ce546')
    sprite('ce610_02', 7)
    sprite('ce610_01', 7)
    sprite('ce610_00', 7)
    DemoTimer(40)
    loopRest()
    ExitState()
    label(340)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    label(341)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(341)
    label(342)
    SLOT_4 = 0
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    sprite('ce300_05', 15)
    Voiceline('ce548')
    DemoTimer(260)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 15)
    sprite('ce300_06ex', 90)
    sprite('ce300_06ex', 5)
    sprite('ce300_07', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(350)
    sprite('ce020_07', 1)
    Visibility(1)
    AbsoluteY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(350)
    sprite('ce020_07', 60)
    uponSendToLabel(LANDING, 352)
    Voiceline('ce550')
    sprite('ce020_07', 2)
    Visibility(0)
    physicsYImpulse(-40000)
    label(351)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(351)
    label(352)
    sprite('ce024_00', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    loopRest()
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    ObjectUpon(22, 32)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    ExitState()
    label(390)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(391)
    sprite('ce603_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(391)
    label(392)
    sprite('ce603_00', 5)
    Voiceline('ce558')
    label(393)
    sprite('ce603_00', 5)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(393)
    sprite('ce603_00', 25)
    sprite('ce603_00', 5)
    ObjectUpon(22, 32)
    uponSendToLabel(32, 395)
    label(394)
    sprite('ce603_00', 5)
    gotoLabel(394)
    label(395)
    sprite('ce603_00', 6)
    clearUponHandler(32)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    loopRest()
    ExitState()
    label(1390)
    sprite('ce603_00', 1)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(1391)
    sprite('ce603_00', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(1391)
    label(1392)
    sprite('ce603_00', 20)
    sprite('ce603_00', 240)
    Voiceline('ce558')
    sprite('ce603_00', 20)
    sprite('ce603_00', 255)
    ObjectUpon(22, 32)
    sprite('ce603_00', 6)
    clearUponHandler(32)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    loopRest()
    ExitState()
    label(420)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 607, 0)
    label(421)
    sprite('ce603_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(421)
    label(422)
    sprite('ce603_00', 20)
    sprite('ce603_00', 120)
    Voiceline('ce564')
    sprite('ce603_00', 25)
    sprite('ce603_00', 32767)
    ObjectUpon(22, 32)
    uponSendToLabel(32, 425)
    label(425)
    sprite('ce603_00', 6)
    clearUponHandler(32)
    ObjectUpon2(11, 608, 0)
    sprite('ce603_01', 6)
    loopRest()
    ExitState()
    label(440)
    sprite('ce020_07', 1)
    Visibility(1)
    AbsoluteY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(440)
    sprite('ce020_07', 2)
    uponSendToLabel(LANDING, 442)
    Visibility(0)
    physicsYImpulse(-40000)
    label(441)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(441)
    label(442)
    sprite('ce024_00', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 0)
    LandingEffects(0, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    CreateParticle('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    sprite('ce600_00', 6)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 180)
    Voiceline('ce570')
    DemoEndOnVoiceEnd(1)
    sprite('ce600_02', 8)
    sprite('ce000_00', 7)
    ObjectUpon(22, 32)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 100, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('keep', 1)
    if SLOT_109:
        conditionalSendToLabel(5)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 603, 0)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(1)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    TriggerUponForState('MinervaRoundWin', 32)
    sprite('ce615_00', 9)
    sprite('ce615_01', 9)
    sprite('ce615_02', 9)
    sprite('ce615_03', 6)
    sprite('ce615_04', 6)
    if random_(2, 0, 50):
        Voiceline('ce400')
    else:
        Voiceline('ce401')
    CreateObject('ce615Eff', 0)
    CreateObject('ce615Eff2', -1)
    PrivateSE('cese_03')
    label(2)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    if SLOT_97:
        conditionalSendToLabel(2)
    sprite('keep', 1)
    DemoTimer(30)
    label(3)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    gotoLabel(3)
    loopRest()
    label(5)
    sprite('ce610_00', 8)
    ObjectUpon2(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    Voiceline('ce406')
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    label(6)
    sprite('ce610_05', 3)
    if SLOT_97:
        conditionalSendToLabel(6)
    sprite('ce610_05', 3)
    DemoTimer(50)
    sprite('ce610_05', 32767)
    loopRest()


@State
def CmnActMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    if SLOT_109:
        conditionalSendToLabel(1)
    if SLOT_123:
        conditionalSendToLabel(1)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('rg'):
        if SLOT_138:
            gotoLabel(100)
        else:
            gotoLabel(1100)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('ca'):
        if SLOT_140:
            gotoLabel(2190)
        else:
            gotoLabel(190)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('vh'):
        conditionalSendToLabel(260)
    if CharacterIDCheck('pt'):
        if SLOT_138:
            gotoLabel(270)
        else:
            gotoLabel(1270)
    if CharacterIDCheck('kg'):
        if SLOT_140:
            gotoLabel(2330)
        else:
            gotoLabel(330)
    if CharacterIDCheck('kk'):
        conditionalSendToLabel(340)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    if CharacterIDCheck('ta'):
        gotoLabel(666)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(1)
    sprite('ce610_00', 8)
    ObjectUpon2(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    if random_(2, 0, 50):
        Voiceline('ce406')
    else:
        Voiceline('ce407')
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    label(0)
    sprite('ce610_05', 3)
    if SLOT_97:
        conditionalSendToLabel(0)
    sprite('ce610_05', 3)
    DemoTimer(50)
    sprite('ce610_05', 32767)
    loopRest()
    label(10)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(12)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 605, 0)
    label(11)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(11)
    label(12)
    physicsXImpulse(0)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_00', 7)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    Voiceline('ce408')
    if SLOT_43:
        DemoTimer(220)
    else:
        DemoTimer(150)
    sprite('ce611_00', 7)
    label(13)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    if SLOT_97:
        conditionalSendToLabel(13)
    label(14)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    gotoLabel(14)
    label(666)
    sprite('ce610_00', 8)
    ObjectUpon2(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    if random_(2, 0, 50):
        Voiceline('ce406')
    else:
        Voiceline('ce407')
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    label(667)
    sprite('ce610_05', 3)
    if SLOT_97:
        conditionalSendToLabel(667)
    sprite('ce610_05', 3)
    DemoTimer(50)
    sprite('ce610_05', 32767)
    loopRest()
    label(100)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 603, 0)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(102)
    label(101)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(101)
    label(102)
    physicsXImpulse(0)
    TriggerUponForState('MinervaRoundWin', 32)
    sprite('ce615_00', 9)
    Voiceline('ce501')
    DemoEndOnVoiceEnd(1)
    sprite('ce615_01', 9)
    sprite('ce615_02', 9)
    sprite('ce615_03', 6)
    sprite('ce615_04', 6)
    CreateObject('ce615Eff', 0)
    CreateObject('ce615Eff2', -1)
    PrivateSE('cese_03')
    label(103)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    gotoLabel(103)
    label(1100)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(1102)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 605, 0)
    label(1101)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(1101)
    label(1102)
    sprite('ce010_00', 7)
    physicsXImpulse(0)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    sprite('ce611_00', 7)
    sprite('ce611_01', 10)
    Voiceline('ce501')
    sprite('ce611_01', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(110)
    sprite('ce300_00', 6)
    callSubroutine('MinervaNoneReCall')
    sprite('ce300_01', 6)
    Voiceline('ce503')
    DemoEndOnVoiceEnd(1)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    label(111)
    sprite('ce300_05', 8)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 8)
    sprite('ce300_06ex', 60)
    gotoLabel(111)
    label(190)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    ObjectUpon2(11, 604, 0)
    sprite('ce603_01', 6)
    sprite('ce603_00', 32767)
    Voiceline('ce520')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(2190)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    ObjectUpon2(11, 604, 0)
    sprite('ce603_01', 6)
    sprite('ce603_00', 32767)
    Voiceline('ce520')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(200)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 650, 0)
    sprite('ce620_00', 7)
    Voiceline('ce521')
    DemoEndOnVoiceEnd(1)
    sprite('ce620_01', 7)
    sprite('ce620_02', 5)
    sprite('ce620_03', 8)
    sprite('ce620_04', 6)
    sprite('ce620_05', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_01', 10)
    sprite('ce620_06', 8)
    sprite('ce620_07', 8)
    sprite('ce620_08', 32767)
    loopRest()
    label(260)
    sprite('ce300_00', 6)
    callSubroutine('MinervaNoneReCall')
    sprite('ce300_01', 6)
    Voiceline('ce533')
    DemoEndOnVoiceEnd(1)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    label(111)
    sprite('ce300_05', 8)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 8)
    sprite('ce300_06ex', 60)
    gotoLabel(111)
    label(270)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(272)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 605, 0)
    label(271)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(271)
    label(272)
    sprite('ce010_00', 7)
    physicsXImpulse(0)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    Voiceline('ce535')
    DemoEndOnVoiceEnd(1)
    sprite('ce611_00', 7)
    label(273)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    loopRest()
    gotoLabel(273)
    label(1270)
    sprite('ce000_00', 8)
    sprite('ce000_11', 8)
    CameraControlEnable(1)
    sprite('ce603_01', 8)
    sprite('ce603_00', 32767)
    AddX(-2000)
    Voiceline('ce535')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(330)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(332)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 605, 0)
    label(331)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('ce010_00', 7)
    physicsXImpulse(0)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    sprite('ce611_00', 7)
    sprite('ce611_01', 10)
    Voiceline('ce547')
    sprite('ce611_01', 32767)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(2330)
    sprite('keep', 1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2332)
    sprite('ce030_00', 7)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    ObjectUpon2(11, 605, 0)
    label(2331)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(2331)
    label(2332)
    sprite('ce010_00', 7)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    sprite('ce611_00', 7)
    sprite('ce611_01', 10)
    Voiceline('ce547')
    DemoEndOnVoiceEnd(1)
    sprite('ce611_01', 32767)
    loopRest()
    label(340)
    sprite('ce001_00', 6)
    SLOT_66 = 1
    ObjectUpon2(11, 112, 0)
    Voiceline('ce549')
    DemoEndOnVoiceEnd(1)
    sprite('ce001_01', 6)
    sprite('ce001_02', 6)
    sprite('ce001_03', 6)
    sprite('ce001_04', 6)
    sprite('ce001_05', 6)
    label(341)
    sprite('ce001_06', 8)
    sprite('ce001_06ex00', 8)
    sprite('ce001_06ex01', 29)
    sprite('ce001_06', 8)
    sprite('ce001_06ex02', 8)
    sprite('ce001_06ex03', 29)
    gotoLabel(341)
    label(350)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    ObjectUpon2(11, 604, 0)
    sprite('ce603_01', 6)
    sprite('ce603_00', 32767)
    Voiceline('ce551')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(390)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    ObjectUpon2(11, 604, 0)
    sprite('ce603_01', 6)
    sprite('ce603_00', 32767)
    Voiceline('ce559')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(420)
    sprite('keep', 1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(422)
    sprite('ce030_00', 7)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    ObjectUpon2(11, 605, 0)
    label(421)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(421)
    label(422)
    sprite('ce010_00', 6)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 6)
    sprite('ce611_00', 6)
    sprite('ce611_01', 10)
    Voiceline('ce565')
    DemoEndOnVoiceEnd(1)
    sprite('ce611_01', 32767)
    loopRest()
    label(440)
    sprite('keep', 1)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(442)
    sprite('ce030_00', 7)
    ObjectUpon2(11, 605, 0)
    label(441)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(441)
    label(442)
    sprite('ce010_00', 7)
    physicsXImpulse(0)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    sprite('ce611_00', 7)
    Voiceline('ce571')
    DemoEndOnVoiceEnd(1)
    label(443)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    loopRest()
    gotoLabel(443)


@State
def CmnActLose():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 606, 0)
    sprite('ce620_00', 7)
    sprite('ce620_01', 7)
    sprite('ce620_02', 5)
    sprite('ce620_03', 8)
    sprite('ce620_04', 6)
    sprite('ce620_05', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_01', 20)
    sprite('ce620_06', 8)
    Voiceline('ce411')
    sprite('ce620_07', 8)
    label(0)
    sprite('ce620_08', 3)
    if SLOT_97:
        conditionalSendToLabel(0)
    sprite('ce620_08', 32767)
    DemoTimer(30)


@State
def EventDefEntryWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWaitNoMvSignal():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
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
def EventDefChouhatsuLoop():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 15)
    label(0)
    sprite('ce300_05', 15)
    sprite('ce300_05ex', 60)
    sprite('ce300_06', 15)
    sprite('ce300_06ex', 60)
    loopRest()
    gotoLabel(0)


@State
def EventDefChouhatsuLoop2():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('ce300_00', 6)
    sprite('ce300_01', 6)
    sprite('ce300_02', 6)
    sprite('ce300_03', 6)
    sprite('ce300_04', 8)
    label(0)
    sprite('ce300_05', 12)
    sprite('ce300_05ex', 30)
    sprite('ce300_06', 12)
    sprite('ce300_06ex', 30)
    loopRest()
    gotoLabel(0)


@State
def EventDefChouhatsuLoopEnd():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
    sprite('ce300_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKyoroKyoro():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    sprite('ce620_00', 8)
    sprite('ce620_01', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    sprite('ce620_04', 8)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce620_01', 8)
    sprite('ce620_00', 8)
    loopRest()
    enterState('EventDefEntryWaitNoMvSignal')


@State
def EventKyoroKyoroNoMvSignal():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce620_00', 8)
    sprite('ce620_01', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    sprite('ce620_04', 8)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce620_01', 8)
    sprite('ce620_00', 8)
    loopRest()
    enterState('EventDefEntryWaitNoMvSignal')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    XPositionRelativeFacing(-900000)


@State
def EventTalkMv():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    sprite('ce030_00', 7)
    physicsXImpulse(1500)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTalkMvNoMvSignal():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce030_00', 7)
    physicsXImpulse(2000)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTarn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    sprite('ce003_00', 4)
    sprite('ce003_00', 3)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTarnMVFaceup():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 651, 0)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTarnNoMVSignal():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTarnToStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 652, 0)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        ObjectUpon2(11, 660, 0)
    sprite('ce030_00', 7)
    physicsXImpulse(2000)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    gotoLabel(0)


@State
def EventWalkFast():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        ObjectUpon2(11, 661, 0)
    sprite('ce030_00', 7)
    physicsXImpulse(4000)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    gotoLabel(0)


@State
def EventWalkFastNoMVSignal():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('ce030_00', 7)
    physicsXImpulse(4000)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    gotoLabel(0)


@State
def EventVsRMBackStep():
    sprite('ce033_00', 2)
    sprite('ce033_01', 2)
    sprite('ce033_02', 2)
    AddX(-40000)
    physicsXImpulse(-4000)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)
    XImpulseAcceleration(500)
    sprite('ce033_03', 3)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_04', 3)
    XImpulseAcceleration(30)
    LandingEffects(100, 1, 1)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_05', 3)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_06', 3)
    XImpulseAcceleration(50)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalkInWait():
    sprite('null', 3)
    ScreenCollision(0)
    XPositionRelativeFacing(-900000)
    loopRest()
    enterState('CmnActStand')


@State
def EventWalkIn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        ObjectUpon2(11, 660, 0)
        ScreenCollision(0)
        XPositionRelativeFacing(-900000)
        SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('ce030_00', 7)
    physicsXImpulse(4000)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventKyoroKyoro2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce620_00', 8)
    sprite('ce620_01', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    sprite('ce620_04', 8)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce620_01', 8)
    sprite('ce620_00', 8)
    loopRest()
    enterState('CmnActStand')


@State
def EventEntry():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-900000)
        if SLOT_19 < 520000:
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
    sprite('ce030_00', 4)
    physicsXImpulse(4650)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 111, 0)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    XPositionRelativeFacing(-260000)
    physicsXImpulse(0)
    CameraControlEnable(0)
    ObjectUpon2(11, 100, 0)
    enterState('CmnActStand')


@State
def EventKyoroKyoro3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    SLOT_51 = 0
    label(2)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    SLOT_51 = SLOT_51 + 1
    sprite('ce620_04', 8)
    XImpulseAcceleration(60)
    if SLOT_51 >= 3:
        sendToLabel(3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ce620_02', 1)
    sprite('ce620_03', 0)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsKKWait():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-100000)
    label(0)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventAssaultOut():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DamageEffect(2, 'ceef_hiteffH')
        callSubroutine('MinervaNoneCallAttack')
        ScreenCollision(0)
        EnableCollision(0)
    sprite('ce400_00', 1)
    sprite('ce400_01', 1)
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)
    XImpulseAcceleration(50)
    sprite('ce215_00', 1)
    CreateObject('mv215ConsentEff', 0)
    XImpulseAcceleration(50)
    sprite('ce215_00', 1)
    XImpulseAcceleration(50)
    sprite('ce215_01', 2)
    sprite('ce215_02', 40)
    sprite('ce215_03', 40)
    sprite('ce215_04', 1)
    Flip()
    physicsXImpulse(0)
    sprite('ce215_05', 2)
    PrivateSE('cese_22')
    CreateObject('ce215JetEff', 1)
    CreateObject('ce215JetEff', 2)
    CreateObject('AssaultPlug', 0)
    RegisterObject(4, 1)
    SLOT_51 = 1
    DeleteObject(5)
    CreateObject('Cable', 109)
    RegisterObject(5, 1)
    ObjectHitbox(5)
    physicsXImpulse(30000)
    label(0)
    sprite('ce215_06', 2)
    sprite('ce215_05', 2)
    sprite('ce215_06', 2)
    sprite('ce215_05', 3)
    sprite('ce215_06', 2)
    sprite('ce215_05', 3)
    sprite('ce215_06', 2)
    sprite('ce215_05', 3)
    sprite('ce215_06', 2)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    TriggerUponForState('ce215JetEff', 32)
    TriggerUponForState('mv215ConsentEff', 33)
    SLOT_51 = 0
    ObjectUpon(FALLING, 33)
    sprite('ce215_05', 32767)
    ObjectUpon(FALLING, 33)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsTKEntry01():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        EnableCollision(0)
        ScreenCollision(0)
        CameraControlEnable(1)
        AddX(-50000)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def EventVsTKEntry02():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        EnableCollision(0)
        ScreenCollision(0)
        SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('ce030_00', 4)
    physicsXImpulse(4650)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 111, 0)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    XPositionRelativeFacing(-260000)
    physicsXImpulse(0)
    ObjectUpon2(11, 100, 0)
    enterState('CmnActStand')


@State
def EventStandToCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_00', 4)
    sprite('ce010_01', 4)
    label(0)
    sprite('ce010_02', 6)
    sprite('ce010_03', 6)
    sprite('ce010_04', 6)
    sprite('ce010_05', 6)
    sprite('ce010_06', 6)
    sprite('ce010_07', 6)
    sprite('ce010_08', 6)
    sprite('ce010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventCrouchToStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_01', 4)
    sprite('ce010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsKGStandWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        XPositionRelativeFacing(-360000)
    sprite('keep', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventDashOut():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        EnableCollision(0)
        ScreenCollision(0)
        SetZVal(-500)
    RunLoopUpon(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('ce032_00', 3)
    physicsXImpulse(22000)
    label(0)
    sprite('ce032_01', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    sprite('ce032_02', 4)
    PrivateSE('cese_04')
    sprite('ce032_03', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def EventVsRGEntry01():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        CameraControlEnable(1)
        EnableCollision(0)
        ScreenCollision(0)
        SetActionMark(1)
        uponSendToLabel(32, 2)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('ce032_00', 3)
    physicsXImpulse(22000)
    label(0)
    sprite('ce032_01', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    sprite('ce032_02', 4)
    PrivateSE('cese_04')
    sprite('ce032_03', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    XPositionRelativeFacing(-260000)
    physicsXImpulse(0)
    ObjectUpon2(11, 100, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('keep', 2)
    CameraControlEnable(0)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsRGEntry02():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_00', 32767)
    loopRest()


@State
def EventVsRGStandWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        XPositionRelativeFacing(-1000000)
        ScreenCollision(0)
    label(1)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(1)


@State
def EventVsNTAtk6C():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        callSubroutine('MinervaCallAttack')
        ObjectUpon2(11, 321, 0)
        ObjectHitbox(11)
        RunLoopUpon(17, 19)

        def upon_17():
            clearUponHandler(17)
            ObjectUpon(22, 32)
    label(1)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(1)


@State
def EventVsNTTalkMv():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
        RunLoopUpon(17, 300)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    enterState('EventVsNTTalkMv2')


@State
def EventVsNTTalkMv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_00', 3)
    physicsXImpulse(0)
    sprite('ce041_01', 3)
    label(2)
    sprite('ce041_02', 6)
    sprite('ce041_03', 6)
    sprite('ce041_04', 6)
    loopRest()
    gotoLabel(2)


@State
def EventVsNTTalkMvEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)
    sprite('ce041_00', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Entry1():
    sprite('ce601_00', 1)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    sprite('ce601_00', 32767)
    loopRest()


@State
def Act2Event_Entry1End():
    sprite('keep', 2)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    sprite('ce601_01', 6)
    sprite('ce601_02', 6)
    ObjectUpon2(11, 601, 0)
    sprite('ce601_03', 100)
    sprite('ce601_04', 6)
    sprite('ce601_05', 6)
    sprite('ce601_06', 6)
    sprite('ce601_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_MagaoLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('ce603_00', 32767)
    loopRest()


@State
def Act2Event_Magao():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('keep', 2)
    sprite('ce603_01', 6)
    sprite('ce603_00', 32767)
    loopRest()


@State
def Act2Event_MagaoEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('keep', 2)
    sprite('ce603_01', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cevslc_00():

    def upon_IMMEDIATE():
        Visibility(0)
        XPositionRelativeFacing(-720000)
        CameraControlEnable(1)
        EnableCollision(0)
        ScreenCollision(0)
    sprite('ce601_00', 2)
    sprite('ce601_00', 2)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    sprite('ce601_00', 32767)
    loopRest()


@State
def Act2Event_cevslc_01():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        EnableCollision(0)
        ScreenCollision(0)
        CameraControlEnable(1)

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
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    sprite('ce601_01', 6)
    sprite('ce601_02', 6)
    ObjectUpon2(11, 601, 0)
    sprite('ce601_03', 30)
    sprite('ce601_03', 30)
    CameraControlEnable(0)
    sprite('ce601_04', 6)
    sprite('ce601_05', 6)
    sprite('ce601_06', 6)
    sprite('ce601_07', 6)
    sprite('ce030_00', 4)
    physicsXImpulse(6200)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 111, 0)
    label(9)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cevspt_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-720000)
        EnableCollision(0)
        ScreenCollision(0)

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
    sprite('keep', 2)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 4)
    physicsXImpulse(6200)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 111, 0)
    label(9)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ce620_02', 8)
    ObjectUpon2(11, 100, 0)
    sprite('ce620_03', 8)
    sprite('ce620_04', 6)
    sprite('ce620_05', 24)
    sprite('ce620_04', 6)
    sprite('ce620_02', 6)
    sprite('ce620_03', 24)
    sprite('ce620_02', 6)
    sprite('ce620_04', 6)
    sprite('ce620_05', 24)
    sprite('ce620_04', 6)
    sprite('ce620_02', 6)
    sprite('ce620_03', 24)
    sprite('ce620_02', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Kyoro():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('ce620_00', 6)
    sprite('ce620_01', 6)
    sprite('ce620_02', 8)
    sprite('ce620_03', 32767)
    loopRest()


@State
def Act2Event_KyoroEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('keep', 2)
    sprite('ce620_02', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cevspt_01():
    sprite('ce030_00', 4)
    physicsXImpulse(5500)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 605, 0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce010_00', 7)
    EndMomentum(1)
    SetZVal(250)
    TriggerUponForState('MinervaWin02', 32)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    sprite('ce611_00', 7)
    sprite('ce611_01', 32767)
    loopRest()


@State
def Act2Event_cevsjn_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-720000)
        EnableCollision(0)
        ScreenCollision(0)

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
    sprite('keep', 2)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 4)
    physicsXImpulse(6200)
    callSubroutine('MinervaCall')
    sprite('ce030_00', 3)
    ObjectUpon2(11, 111, 0)
    label(9)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ce000_00', 3)
    ObjectUpon2(11, 100, 0)
    sprite('ce208_00', 4)
    label(1)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    loopRest()
    gotoLabel(1)


@State
def Act2Event_cevsjn_01():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('keep', 2)
    sprite('ce208_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cevsjn_02():
    sprite('ce064_09', 3)
    AddInertia(10000)
    CreateObject('Act2Event_Yure', -1)
    sprite('ce064_08', 3)
    sprite('ce064_07', 3)
    sprite('ce064_05', 3)
    sprite('ce064_03', 40)
    EndMomentum(1)
    LandingEffects(0, 1, 1)
    sprite('ce064_04', 6)
    sprite('ce064_05', 6)
    sprite('ce064_06', 6)
    sprite('ce064_07', 6)
    sprite('ce064_08', 6)
    sprite('ce064_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_phvsce_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('ce070_00', 3)
    sprite('ce070_00', 16)
    CallCustomizableParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    AddInertia(-11000)
    ScreenShake(5000, 20000)
    sprite('ce070_01', 5)
    sprite('ce070_02', 5)
    sprite('ce070_03', 5)
    sprite('ce070_04', 5)
    sprite('ce070_05', 5)
    sprite('ce070_06', 5)
    sprite('ce070_07', 5)
    sprite('ce070_08', 5)
    sprite('ce070_09', 5)
    sprite('ce063_11', 5)
    LandingEffects(0, 1, 1)
    CommonSE('209_down_normal_0')
    sprite('ce064_00', 5)
    sprite('ce064_01', 5)
    sprite('ce064_02', 32767)
    loopRest()


@State
def Act2Event_NoDisp_amvsce():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
        XPositionRelativeFacing(-950000)
    sprite('null', 32767)
    loopRest()


@State
def Act2EventWalkIn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ScreenCollision(0)
        ScreenCollision(0)
        SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('null', 1)
    sprite('ce030_00', 4)
    AddX(-50000)
    physicsXImpulse(3200)
    sprite('ce030_00', 1)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 600, 0)
    sprite('ce030_00', 1)
    ObjectUpon2(11, 111, 0)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce030_00', 7)
    callSubroutine('MinervaCall')
    ObjectUpon2(11, 650, 0)
    physicsXImpulse(1500)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(3)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(3)


@State
def Act2EventTalkMv():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    sprite('ce030_00', 7)
    physicsXImpulse(1500)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    sprite('ce003_00', 7)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2EventTarn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 650, 0)
    sprite('ce003_00', 4)
    sprite('ce003_00', 3)
    physicsXImpulse(0)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        SetYCollisionFromOrigin(240)
        SetXCollisionFromOrigin(200)
        DamageEffect(2, 'ceef_hiteffH')
        callSubroutine('MinervaNoneCallAttack')
    sprite('ce402_00', 2)
    sprite('ce402_01', 2)
    sprite('ce402_02', 3)
    sprite('ce235_00', 3)
    CreateObject('mv235ConsentEff', 0)
    sprite('ce235_01', 3)
    sprite('ce235_02', 3)
    sprite('ce235_03', 3)
    sprite('ce235_04', 5)
    CommonSE('005_swing_grap_2_2')
    TriggerUponForState('mv235ConsentEff', 32)
    physicsXImpulse(26000)
    SetAcceleration(-2000)
    sprite('ce235_05', 5)
    PrivateSE('cese_22')
    CreateObject('mv235Eff', -1)
    TriggerUponForState('mv235ConsentEff', 33)
    AltKnockdownEffects(100, 1, 1)
    EndMomentum(1)
    SetYCollisionFromOrigin(100)
    SetXCollisionFromOrigin(100)
    sprite('ce235_06', 5)
    sprite('ce235_07', 5)
    sprite('ce235_08', 5)
    sprite('ce235_09', 5)
    sprite('ce235_10', 4)


@State
def Act2Eventbackstep_amvsce():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        ExternalForcesRate(100, 0)
        EndMomentum(1)
    sprite('ce033_00', 2)
    PrivateSE('cese_16')
    sprite('ce033_01', 2)
    physicsXImpulse(-11500)
    sprite('ce033_02', 2)
    AddX(-20000)
    XImpulseAcceleration(150)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)
    XImpulseAcceleration(150)
    sprite('ce033_03', 3)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)
    XImpulseAcceleration(15)
    LandingEffects(100, 1, 1)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)
    XImpulseAcceleration(15)
    CreateParticle('ceef_bstepeff_line', 0)
    CreateParticle('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act2Event_Kyoro_amvsce():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce003_00', 3)
    Flip()
    sprite('ce003_01', 7)
    sprite('ce003_00ex', 7)
    sprite('ce620_00', 6)
    sprite('ce620_01', 6)
    sprite('ce620_02', 8)
    sprite('ce620_03', 32767)
    loopRest()


@State
def Act2Event_Lose_amvsce():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce440_09', 32767)
    loopRest()


@State
def Act2Event_LoseEnd_amvsce():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce440_09', 6)
    sprite('ce440_10', 6)
    sprite('ce010_02', 6)
    sprite('ce010_01', 4)
    sprite('ce010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevsny_00():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('null', 32767)
    Visibility(1)
    CreateObject('Act3Event_CreateNO', -1)


@State
def Act3Event_cevsny_01():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        EnableCollision(0)
        ScreenCollision(0)
        SetActionMark(1)
        XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 370000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -370000:
            sendToLabel(1)
    sprite('ce032_00', 3)
    physicsXImpulse(22000)
    label(0)
    sprite('ce032_01', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    sprite('ce032_02', 4)
    PrivateSE('cese_04')
    sprite('ce032_03', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce032_04', 4)
    CommonSE('208_brake_normal')
    physicsXImpulse(0)
    SetInertia(10000)
    clearUponHandler(EVERY_FRAME)
    sprite('ce032_05', 4)
    sprite('ce032_06', 4)
    CommonSE('208_brake_normal')
    sprite('ce032_07', 4)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevsny_02_Loop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce217_00', 3)
    sprite('ce217_00', 2)
    label(0)
    sprite('ce217_01', 6)
    sprite('ce217_02', 6)
    sprite('ce217_03', 6)
    sprite('ce217_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevsny_02_LoopEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        TriggerUponForState('Act3Event_CreateNO', 32)
    sprite('ce217_01', 5)
    sprite('ce217_03', 5)
    sprite('ce217_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevskk_00_Loop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('ce218_00', 6)
    label(0)
    sprite('ce218_01', 6)
    sprite('ce218_02', 6)
    sprite('ce218_03', 6)
    sprite('ce218_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevskk_00_LoopEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        ObjectUpon2(11, 100, 0)
    sprite('ce218_02', 5)
    sprite('ce218_01', 5)
    sprite('ce218_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevskk_01_Loop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce207_00', 6)
    label(0)
    sprite('ce207_01', 6)
    sprite('ce207_02', 6)
    sprite('ce207_03', 6)
    sprite('ce207_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevskk_01_LoopEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce207_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevskk_02_Loop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 6)
    sprite('ce333_01', 6)
    sprite('ce333_02', 6)
    sprite('ce333_03', 6)
    sprite('ce333_04', 6)
    CreateObject('Act3Event_HealEff', 0)
    label(0)
    sprite('ce333_05', 6)
    sprite('ce333_06', 6)
    sprite('ce333_07', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevskk_02_LoopEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)
    sprite('ce333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsce_00():

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
    sprite('ce032_00', 2)
    physicsXImpulse(20000)
    label(9)
    sprite('ce032_01', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    sprite('ce032_02', 4)
    PrivateSE('cese_04')
    sprite('ce032_03', 4)
    CreateParticle('ceef_dasheff_line', 0)
    CreateParticle('ceef_dasheff_line', 1)
    PrivateSE('cese_04')
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ce032_04', 3)
    physicsXImpulse(0)
    SetInertia(10000)
    sprite('ce032_05', 3)
    sprite('ce032_06', 3)
    sprite('ce032_07', 3)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsce_01():
    sprite('ce600_02', 8)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 8)
    sprite('ce600_01ex2', 32767)


@State
def Act3Event_jbvsce_02():
    sprite('ce600_02', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsce_03():
    sprite('ce070_02', 32767)


@State
def Act3Event_jbvsce_04():
    sprite('ce070_02', 20)
    ConstantAlphaModifier(-12)
    CommonSE('000_airdash_0')
    loopRest()
    sprite('ce070_02', 32767)
    AlphaValue(0)
    Visibility(1)
