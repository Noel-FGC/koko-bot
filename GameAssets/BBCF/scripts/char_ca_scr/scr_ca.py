@Subroutine
def PreInit():
    CharacterID('ca')


@Subroutine
def MatchInit():
    Health(10000)
    WalkFSpeed(7700)
    WalkBSpeed(5000)
    JumpYVelocity(32000)
    SuperJumpYVelocity(39000)
    Gravity(1650)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(5)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(1)
    FootstepSE(1)
    CreateDecalOn(1)
    CPUJumpPriority(1000)
    CPURetreatPriority(1000)
    Move_Register('PosingStandStarting', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3000)
    Move_Input_(0x6b)
    Move_EndRegister()
    Move_Register('PosingStandAttack', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3001)
    Move_Input_(0x6b)
    Move_EndRegister()
    Move_Register('PosingCrouchStarting', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3000)
    Move_Input_(0x45)
    Move_EndRegister()
    Move_Register('PosingCrouchAttack', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3001)
    Move_Input_(0x45)
    Move_EndRegister()
    Move_Register('PosingAirStarting', 0x1)
    Move_Condition(0x2001)
    Move_Condition(0x3000)
    Move_EndRegister()
    Move_Register('PosingAirAttack', 0x1)
    Move_Condition(0x2001)
    Move_Condition(0x3001)
    Move_EndRegister()
    Move_Register('SpecialPosingStandAttack', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3002)
    Move_Input_(0x6b)
    Move_EndRegister()
    Move_Register('SpecialPosingCrouchAttack', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3002)
    Move_Input_(0x45)
    Move_EndRegister()
    Move_Register('SpecialPosingAirAttack', 0x1)
    Move_Condition(0x2001)
    Move_Condition(0x3002)
    Move_EndRegister()
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(2)
    MovePriority(2000)
    SkillEstimateRange(0, 200000, -100000, 200000, 3000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    DamageStunPriority(1)
    AirborneOpponentPriority(3000)
    SkillEstimateRange(0, 350000, 100000, 350000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 250000, -100000, 200000, 3000, 50)
    MoveLow()
    Move_EndRegister()
    Move_Register('Atk6B_Input5', 0x1)
    StateCall('NmlAtk6B')
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x2000)
    MoveComboPriority(3000)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(3000)
    SkillEstimateRange(100000, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    SkillEstimateRange(0, 420000, -100000, 200000, 500, 50)
    MoveLow()
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 50)
    MoveLow()
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    DamageStunPriority(2000)
    SkillEstimateRange(200000, 550000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    GuardStunPriority(3000)
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -100000, 200000, 1000, 50)
    MoveMid()
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    MovePriority(1)
    MoveComboPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 240000, -100000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    DamageStunPriority(1)
    SkillEstimateRange(0, 440000, -100000, 200000, 1000, 50)
    MoveLow()
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(0, 300000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(0, 300000, -130000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    DamageStunPriority(3000)
    SkillEstimateRange(0, 300000, -400000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    MoveMaxChainRepeat(1)
    MoveComboPriority(1)
    SkillEstimateRange(-150000, 150000, -500000, 100000, 2500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    CPUUsable(0)
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
    SkillEstimateRange(30000, 210000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Rolling_A', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    MovePriority(1)
    DamageStunPriority(1)
    AirborneOpponentPriority(1)
    MoveComboPriority(1)
    SkillEstimateRange(0, 300000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Rolling_B', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    GuardStunPriority(1)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    AirborneOpponentPriority(3000)
    SkillEstimateRange(0, 400000, -150000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Air_MultiHit', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    MovePriority(1)
    MoveComboPriority(1)
    SkillEstimateRange(-150000, 250000, -300000, 200000, 1000, 1)
    Move_EndRegister()
    Move_Register('RemoteThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    MovePriority(1)
    MoveComboPriority(1)
    DamageStunPriority(3000)
    SkillEstimateRange(0, 450000, -200000, 50000, 1000, 0)
    Move_EndRegister()
    Move_Register('OrderNirvanaRush', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackable')
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_RELEASE_D)
    MovePriority(1)
    AirborneOpponentPriority(1)
    GuardStunPriority(10000)
    DamageStunPriority(10000)
    OpponentAttackPriority(10000)
    MoveTarget(11)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('OrderNirvanaRushOD', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackableOD')
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_RELEASE_D)
    MovePriority(1)
    AirborneOpponentPriority(1)
    GuardStunPriority(10000)
    DamageStunPriority(10000)
    OpponentAttackPriority(10000)
    MoveTarget(11)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('OrderNirvanaRushAir', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackable')
    Move_Condition(0x2002)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_RELEASE_D)
    MovePriority(1)
    AirborneOpponentPriority(1)
    GuardStunPriority(10000)
    DamageStunPriority(10000)
    OpponentAttackPriority(10000)
    MoveTarget(11)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('OrderNirvanaRushAirOD', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackableOD')
    Move_Condition(0x2002)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_RELEASE_D)
    MovePriority(1)
    AirborneOpponentPriority(1)
    GuardStunPriority(10000)
    DamageStunPriority(10000)
    OpponentAttackPriority(10000)
    MoveTarget(11)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('OrderNirvanaStrike', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackable')
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_RELEASE_D)
    MoveTarget(11)
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 600000, 1000, 10)
    Move_EndRegister()
    Move_Register('OrderNirvanaStrikeOD', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackableOD')
    Move_Condition(0x2002)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_RELEASE_D)
    MoveTarget(11)
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 600000, 1000, 10)
    Move_EndRegister()
    Move_Register('OrderNirvanaStrikeAir', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackable')
    Move_Condition(0x2002)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_RELEASE_D)
    MoveTarget(11)
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 600000, 1, 1)
    Move_EndRegister()
    Move_Register('OrderNirvanaStrikeAirOD', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackableOD')
    Move_Condition(0x2002)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214214)
    Move_Input_(INPUT_RELEASE_D)
    MoveTarget(11)
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 300000, -200000, 600000, 1, 1)
    Move_EndRegister()
    Move_Register('UltimateHaguruma', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    MovePriority(500)
    OpponentAttackPriority(5000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateHagurumaOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    MovePriority(500)
    OpponentAttackPriority(5000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 300000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateLock', INPUT_DISTORTION)
    CallSkillConditions('CheckNirvanaAttackableOD')
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_RELEASE_D)
    OpponentAttackPriority(5000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(0, 400000, -150000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    CallSkillConditions('CheckNirvanaAttackable')
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_64641236)
    Move_Input_(INPUT_RELEASE_D)
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
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk2A', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk2B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'UltimateHaguruma', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Rolling_A', 5000000)
    TempPriorityMultiplier('NmlAtk6A', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'RemoteThrow', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'Air_MultiHit', 10000000)
    TempPriorityMultiplier('NmlAtkAIR2C', 'Air_MultiHit', 10000000)
    StylishModeSpecialButton('Rolling_A', 0x4, 0xea)
    StylishModeSpecialButton('Rolling_B', 0x4, 0x79)
    StylishModeSpecialButton('UltimateHaguruma', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateHagurumaOD', 0x4, 0x5f)
    StylishModeSpecialButton('RemoteThrow', 0x4, 0x45)
    StylishModeSpecialButton('Air_MultiHit', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk2A', 1, 150000)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 1, 300000)
    StylishModeCancels('NmlAtk5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6B', 1, 300000)
    StylishModeCancels('NmlAtk5C', 'RemoteThrow', 6, 0)
    StylishModeCancels('NmlAtk5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk6A', 'Rolling_A', 0, 0)
    StylishModeCancels('NmlAtk6A', 'RemoteThrow', 6, 0)
    StylishModeCancels('NmlAtk6A', 'FHighJump', 12, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk2C', 6, 0)
    StylishModeCancels('NmlAtk6C', 'RemoteThrow', 6, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5A', 1, 150000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 1, 150000)
    StylishModeCancels('NmlAtk2B', 'NmlAtk2C', 12, 0)
    StylishModeCancels('NmlAtk2C', 'FJump', 0, 0)
    StylishModeCancels('NmlAtk3C', 'Rolling_A', 0, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateHaguruma', 5, 50)
    StylishModeCancels('NmlAtk3C', 'UltimateHagurumaOD', 5, 50)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'Rolling_A', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtkAIR2C', 'Air_MultiHit', 0, 0)
    StylishModeCancels('ThrowExe', 'Rolling_A', 0, 0)
    StylishModeCancels('BackThrowExe', 'Rolling_A', 0, 0)
    StylishModeCancels('BackThrowExe', 'AstralHeat', 6, 0)
    HitSprites(0, 'ca062_01')
    HitSprites(1, 'ca062_03')
    HitSprites(2, 'ca062_04')
    HitSprites(3, 'ca062_05')
    HitSprites(4, 'ca062_05')
    HitSprites(5, 'ca062_06')
    HitSprites(6, 'ca062_07')
    HitSprites(7, 'ca041_02')
    HitSprites(8, 'ca040_02')
    HitSprites(9, 'ca045_02')
    HitSprites(10, 'ca060_00')
    HitSprites(11, 'ca060_01')
    HitSprites(12, 'ca060_03')
    HitSprites(13, 'ca060_05')
    HitSprites(14, 'ca060_07')
    HitSprites(15, 'ca060_14')
    HitSprites(16, 'ca050_00')
    HitSprites(17, 'ca052_00')
    HitSprites(18, 'ca054_00')
    HitSprites(19, 'ca000_00')
    HitSprites(20, 'ca000_00')
    HitSprites(25, 'ca063_00')
    HitSprites(26, 'ca063_01')
    HitSprites(27, 'ca063_02')
    HitSprites(28, 'ca063_04')
    HitSprites(29, 'ca063_11')
    HitSprites(30, 'ca077_00')
    HitSprites(31, 'ca077_01')
    HitSprites(32, 'ca077_00ex00')
    HitSprites(33, 'ca077_01ex00')
    HitSprites(34, 'ca077_00ex01')
    HitSprites(35, 'ca077_01ex01')
    HitSprites(36, 'ca077_00ex02')
    HitSprites(37, 'ca077_01ex02')
    HitSprites(24, 'ca073_01')
    CommonVoicelines(2, 'ca002')
    CommonVoicelines(5, 'ca005')
    CommonVoicelines(7, 'ca007')
    CommonVoicelines(8, 'ca008')
    CommonVoicelines(9, 'ca009')
    CommonVoicelines(10, 'ca010')
    CommonVoicelines(11, 'ca011')
    CommonVoicelines(12, 'ca012')
    CommonVoicelines(15, 'ca015')
    CommonVoicelines(16, 'ca016')
    CommonVoicelines(17, 'ca017')
    CommonVoicelines(18, 'ca018')
    CommonVoicelines(19, 'ca019')
    CommonVoicelines(20, 'ca020')
    CommonVoicelines(21, 'ca021')
    CommonVoicelines(22, 'ca022')
    CommonVoicelines(23, 'ca023')
    CommonVoicelines(24, 'ca024')
    CommonVoicelines(25, 'ca025')
    CommonVoicelines(26, 'ca026')
    CommonVoicelines(27, 'ca027')
    CommonVoicelines(28, 'ca028')
    CommonVoicelines(30, 'ca030')
    CommonVoicelines(31, 'ca031')
    CommonVoicelines(41, 'ca041')
    CommonVoicelines(42, 'ca042')
    CommonVoicelines(43, 'ca043')
    CommonVoicelines(44, 'ca044')
    CommonVoicelines(45, 'ca045')
    CommonVoicelines(46, 'ca046')
    CommonVoicelines(47, 'ca047')
    CommonVoicelines(48, 'ca048')
    CommonVoicelines(49, 'ca049')
    CommonVoicelines(50, 'ca050')
    CommonVoicelines(51, 'ca051')
    CommonVoicelines(52, 'ca052')
    CommonVoicelines(53, 'ca053')
    CommonVoicelines(54, 'ca100')
    CommonVoicelines(55, 'ca101')
    CommonVoicelines(56, 'ca102')
    CommonVoicelines(57, 'ca103')
    CommonVoicelines(58, 'ca104')
    CommonVoicelines(59, 'ca105')
    CommonVoicelines(60, 'ca106')
    CommonVoicelines(61, 'ca107')
    CommonVoicelines(70, 'ca156')
    CommonVoicelines(71, 'ca157')
    CommonVoicelines(72, 'ca158')
    CommonVoicelines(75, 'ca160')
    CommonVoicelines(73, 'ca402')
    CommonVoicelines(74, 'ca403')
    CreateObject('NirvanaCreate', -1)
    RegisterObject(11, 1)
    ResourceGauge(0, 1, 5, 1, 10000, 0, -16736256, -192)


@Subroutine
def MatchInit2():
    CallPrivateFunction('CA_NirvanaPosReset', 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_59 = 5
    SLOT_60 = 100


@Subroutine
def CheckNirvanaAttackable():
    CallPrivateFunction('CheckNirvanaAttackableSub', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def CheckNirvanaAttackableOD():
    if SLOT_OverdriveTimer:
        CallPrivateFunction('CheckNirvanaAttackableSub', 0, 0, 0, 0, 0, 0, 0, 0
            )


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def CheckJ2CActivate():
    SLOT_47 = 1
    if SLOT_YDistanceFromFloor <= 100000:
        SLOT_YVelocity <= 0
        SLOT_47 = SLOT_0


@Subroutine
def OnFrameStep():
    TrainingModeSLOT('TRI_CarlsDoll', 2, 67)
    if SLOT_67:
        CopyFromRightToLeft(11, 2, 75, 23, 0, 9999999)
    if SLOT_OverdriveTimer:
        SLOT_60 = 100
    elif SLOT_IsInHitstun:
        SLOT_60 = 100
    elif SLOT_42:
        SLOT_60 = 100
    else:
        SLOT_60 = 100
    CallPrivateFunction('CA_ExGageByNirvanaHitPoint', 0, 0, 0, 0, 0, 0, 0, 0)
    CopyFromRightToLeft(23, 2, 31, 11, 2, 75)
    if SLOT_4:
        SLOT_4 = SLOT_4 + -1
    if SLOT_5:
        SLOT_5 = SLOT_5 + -1
    if SLOT_6:
        SLOT_6 = SLOT_6 + -1


@State
def CmnActStand():
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('ca001_00', 6)
    SLOT_88 = 960
    Voiceline('ca000')
    sprite('ca001_01', 6)
    sprite('ca001_02', 6)
    sprite('ca001_03', 6)
    sprite('ca001_04', 6)
    sprite('ca001_05', 6)
    sprite('ca001_06', 6)
    sprite('ca001_07', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca001_08', 6)
    SLOT_88 = 300
    sprite('ca001_09', 6)
    sprite('ca001_10', 6)
    sprite('ca001_11', 6)
    sprite('ca001_12', 6)
    sprite('ca001_13', 6)
    sprite('ca001_14', 6)
    sprite('ca001_15', 6)
    sprite('ca001_16', 6)
    sprite('ca001_17', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('ca003_00', 3)
    sprite('ca003_01', 3)
    sprite('ca003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('ca010_00', 4)
    sprite('ca010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('ca010_02', 6)
    sprite('ca010_03', 6)
    sprite('ca010_04', 6)
    sprite('ca010_05', 6)
    sprite('ca010_06', 6)
    sprite('ca010_07', 6)
    sprite('ca010_08', 6)
    sprite('ca010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('ca013_00', 3)
    sprite('ca013_01', 3)
    sprite('ca013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('ca010_01', 4)
    sprite('ca010_00', 4)


@State
def CmnActJumpPre():
    sprite('ca023_00', 2)
    sprite('ca023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('ca020_00', 3)
    sprite('ca020_01', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('ca020_02', 3)
    sprite('ca020_03', 3)


@State
def CmnActJumpDown():
    sprite('ca020_04', 3)
    sprite('ca020_05', 3)
    label(0)
    sprite('ca020_06', 4)
    sprite('ca020_07', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('ca024_00', 3)
    sprite('ca024_01', 3)
    sprite('ca024_02', 3)
    sprite('ca024_03', 3)
    sprite('ca024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('ca024_00', 2)
    sprite('ca024_01', 2)
    sprite('ca024_02', 2)
    sprite('ca024_03', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('ca024_03', 3)
    sprite('ca024_04', 3)


@State
def CmnActFWalk():
    sprite('ca030_00', 5)
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('ca031_00', 6)
    label(0)
    sprite('ca031_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_02', 6)
    sprite('ca031_03', 6)
    sprite('ca031_04', 6)
    sprite('ca031_05', 6)
    sprite('ca031_06', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_07', 6)
    sprite('ca031_08', 6)
    sprite('ca031_09', 6)
    sprite('ca031_10', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        WhiffCancel('Air_MultiHit')
        WhiffCancelEnable(1)
    sprite('ca032_00', 2)
    DashEffects(100, 1, 1)
    WhiffJumpCancel(1)
    IgnoreInertia(1)
    AddInertia(21600)
    WhiffNormalCancel(1)
    sprite('ca032_01', 2)
    physicsXImpulse(30000)
    sprite('ca032_01', 1)
    sprite('ca032_01', 1)
    WhiffJumpCancel(0)
    WhiffNormalCancel(0)
    sprite('ca032_02', 1)
    physicsYImpulse(10000)
    setGravity(1500)
    sprite('ca032_02', 1)
    sprite('ca032_01', 1)
    sprite('ca032_01', 1)
    setGravity(3500)
    sprite('ca032_02', 1)
    sprite('ca032_02', 1)
    sprite('ca032_01', 1)
    sprite('ca032_01', 1)
    sprite('ca032_02', 1)
    sprite('ca032_02', 1)
    sprite('ca032_01', 1)
    sprite('ca032_01', 1)
    sprite('ca032_02', 1)
    sprite('ca032_02', 1)
    sprite('ca032_01', 1)
    sprite('ca032_01', 1)
    sprite('ca032_02', 1)
    sprite('ca032_02', 32767)
    label(1)
    sprite('ca032_03', 2)
    LandingEffects(100, 1, 1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    EndMomentum(1)
    sprite('ca032_04', 2)
    sprite('ca032_05', 2)


@State
def CmnActFDashStop():
    pass


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
    sprite('ca033_00', 2)
    sprite('ca033_01', 2)
    physicsXImpulse(-22000)
    physicsYImpulse(11000)
    setGravity(1800)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    setInvincible(0)
    label(0)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca033_04', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('ca033_05', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('ca035_00', 3)
    label(0)
    sprite('ca035_01', 3)
    sprite('ca035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('ca036_00', 3)
    label(0)
    sprite('ca036_01', 3)
    sprite('ca036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('ca050_00', 1)
    sprite('ca050_01', 1)
    sprite('ca050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('ca050_01', 1)
    sprite('ca050_02', 1)
    sprite('ca050_01', 2)
    sprite('ca050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('ca050_02', 1)
    sprite('ca050_03', 1)
    sprite('ca050_02', 2)
    sprite('ca050_01', 2)
    sprite('ca050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('ca050_03', 1)
    sprite('ca050_04', 1)
    sprite('ca050_03', 2)
    sprite('ca050_02', 2)
    sprite('ca050_01', 2)
    sprite('ca050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('ca050_04', 1)
    sprite('ca050_04', 1)
    sprite('ca050_04', 2)
    sprite('ca050_03', 2)
    sprite('ca050_02', 2)
    sprite('ca050_01', 2)
    sprite('ca050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('ca052_00', 1)
    sprite('ca052_01', 1)
    sprite('ca052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('ca052_01', 1)
    sprite('ca052_02', 1)
    sprite('ca052_01', 2)
    sprite('ca052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('ca052_02', 1)
    sprite('ca052_03', 1)
    sprite('ca052_02', 2)
    sprite('ca052_01', 2)
    sprite('ca052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('ca052_03', 1)
    sprite('ca052_04', 1)
    sprite('ca052_03', 2)
    sprite('ca052_02', 2)
    sprite('ca052_01', 2)
    sprite('ca052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('ca052_04', 1)
    sprite('ca052_04', 1)
    sprite('ca052_04', 2)
    sprite('ca052_03', 2)
    sprite('ca052_02', 2)
    sprite('ca052_01', 2)
    sprite('ca052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('ca054_00', 1)
    sprite('ca054_01', 1)
    sprite('ca054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('ca054_01', 1)
    sprite('ca054_02', 1)
    sprite('ca054_01', 2)
    sprite('ca054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('ca054_02', 1)
    sprite('ca054_03', 1)
    sprite('ca054_02', 2)
    sprite('ca054_01', 2)
    sprite('ca054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('ca054_03', 1)
    sprite('ca054_04', 1)
    sprite('ca054_03', 2)
    sprite('ca054_02', 2)
    sprite('ca054_01', 2)
    sprite('ca054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('ca054_04', 1)
    sprite('ca054_04', 1)
    sprite('ca054_04', 2)
    sprite('ca054_03', 2)
    sprite('ca054_02', 2)
    sprite('ca054_01', 2)
    sprite('ca054_00', 2)


@State
def CmnActBDownUpper():
    sprite('ca060_00', 4)
    label(0)
    sprite('ca060_01', 4)
    sprite('ca060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('ca060_03', 4)


@State
def CmnActBDownDown():
    sprite('ca060_04', 4)
    label(0)
    sprite('ca060_05', 4)
    sprite('ca060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('ca060_07', 2)
    sprite('ca060_08', 2)


@State
def CmnActBDownBound():
    sprite('ca060_09', 3)
    sprite('ca060_10', 3)
    sprite('ca060_11', 3)
    sprite('ca060_12', 3)
    sprite('ca060_13', 3)


@State
def CmnActBDownLoop():
    sprite('ca060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('ca061_00', 2)
    sprite('ca061_01', 2)
    sprite('ca061_02', 2)
    sprite('ca061_03', 2)
    sprite('ca061_04', 2)
    sprite('ca061_05', 3)
    sprite('ca061_06', 3)
    sprite('ca061_07', 3)
    sprite('ca061_08', 4)
    sprite('ca061_09', 4)
    sprite('ca061_10', 4)


@State
def CmnActFDownUpper():
    sprite('ca063_00', 4)


@State
def CmnActFDownUpperEnd():
    sprite('ca063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('ca063_02', 3)
    sprite('ca063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('ca063_04', 2)
    sprite('ca063_05', 2)


@State
def CmnActFDownBound():
    sprite('ca063_06', 2)
    sprite('ca063_07', 2)
    sprite('ca063_08', 2)
    sprite('ca063_09', 3)
    sprite('ca063_10', 3)


@State
def CmnActFDownLoop():
    sprite('ca063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('ca064_00', 2)
    sprite('ca064_01', 2)
    sprite('ca064_02', 2)
    sprite('ca064_03', 2)
    sprite('ca064_04', 2)
    sprite('ca064_05', 3)
    sprite('ca064_06', 3)
    sprite('ca064_07', 3)
    sprite('ca064_08', 4)
    sprite('ca064_09', 4)
    sprite('ca064_10', 4)


@State
def CmnActVDownUpper():
    sprite('ca062_00', 3)
    label(0)
    sprite('ca062_01', 3)
    sprite('ca062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('ca062_03', 3)
    sprite('ca062_04', 3)


@State
def CmnActVDownDown():
    sprite('ca062_05', 3)
    sprite('ca062_06', 3)
    label(0)
    sprite('ca062_07', 3)
    sprite('ca062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('ca062_09', 2)
    sprite('ca062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('ca062_09', 2)
    sprite('ca062_10', 2)


@State
def CmnActBlowoff():
    sprite('ca072_00', 3)
    sprite('ca072_01', 3)
    sprite('ca072_02', 3)
    label(0)
    sprite('ca072_01', 3)
    sprite('ca072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ca074_00', 3)
    sprite('ca074_01', 3)
    sprite('ca074_02', 3)
    sprite('ca074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('ca082_00', 2)
    sprite('ca082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('ca071_04', 1)


@State
def CmnActWallBound():
    sprite('ca073_00', 3)
    sprite('ca073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('ca073_02', 3)
    label(0)
    sprite('ca073_03', 3)
    sprite('ca073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('ca070_00', 3)
    sprite('ca070_01', 3)
    sprite('ca070_02', 3)
    sprite('ca070_01', 3)
    sprite('ca070_02', 3)
    sprite('ca070_03', 3)
    sprite('ca070_02', 4)
    sprite('ca070_03', 4)
    sprite('ca070_02', 5)
    sprite('ca070_03', 5)
    label(0)
    sprite('ca070_02', 6)
    sprite('ca070_03', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('ca070_04', 2)
    sprite('ca070_05', 3)
    sprite('ca070_06', 4)
    sprite('ca070_07', 4)
    sprite('ca070_08', 6)
    sprite('ca070_09', 5)


@State
def CmnActUkemiStagger():
    sprite('ca070_10', 2)
    sprite('ca070_11', 2)
    sprite('ca070_12', 3)
    sprite('ca070_13', 3)


@State
def CmnActUkemiAirF():
    sprite('ca113_00', 3)
    sprite('ca113_01', 3)
    sprite('ca113_02', 9)


@State
def CmnActUkemiAirB():
    sprite('ca113_00', 3)
    sprite('ca113_01', 3)
    sprite('ca113_02', 9)


@State
def CmnActUkemiAirN():
    sprite('ca113_00', 3)
    sprite('ca113_01', 3)
    sprite('ca113_02', 9)


@State
def CmnActUkemiLandF():
    sprite('ca110_00', 3)
    sprite('ca110_01', 3)
    sprite('ca110_02', 3)
    sprite('ca110_03', 3)
    sprite('ca110_04', 3)
    sprite('ca110_06', 3)
    sprite('ca110_07', 200)
    sprite('ca110_09', 3)
    sprite('ca110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('ca111_00', 3)
    sprite('ca111_01', 3)
    sprite('ca111_02', 3)
    sprite('ca111_03', 3)
    sprite('ca111_04', 3)
    sprite('ca111_06', 3)
    sprite('ca111_07', 200)
    sprite('ca111_09', 3)
    sprite('ca111_10', 3)


@State
def CmnActUkemiLandN():
    sprite('ca112_00', 2)
    sprite('ca112_01', 2)
    sprite('ca112_02', 2)
    sprite('ca112_03', 2)
    sprite('ca112_04', 2)
    sprite('ca112_05', 2)
    sprite('ca112_06', 2)
    sprite('ca112_07', 2)
    sprite('ca112_08', 2)
    sprite('ca112_09', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('ca024_00', 3)
    sprite('ca024_01', 3)
    sprite('ca024_02', 3)
    sprite('ca024_03', 3)
    sprite('ca024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('ca040_00', 3)
    sprite('ca040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ca040_02', 3)
    sprite('ca040_03', 3)
    sprite('ca040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('ca040_01', 3)
    sprite('ca040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('ca040_05', 3)
    label(0)
    sprite('ca040_02', 3)
    sprite('ca040_03', 3)
    sprite('ca040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('ca040_01', 3)
    sprite('ca040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('ca041_00', 3)
    sprite('ca041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ca041_02', 3)
    sprite('ca041_03', 3)
    sprite('ca041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('ca041_01', 3)
    sprite('ca041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('ca041_05', 3)
    label(0)
    sprite('ca041_02', 3)
    sprite('ca041_03', 3)
    sprite('ca041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('ca041_01', 3)
    sprite('ca041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('ca043_00', 3)
    sprite('ca043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ca043_02', 3)
    sprite('ca043_03', 3)
    sprite('ca043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('ca043_01', 3)
    sprite('ca043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ca043_05', 3)
    label(0)
    sprite('ca043_02', 3)
    sprite('ca043_03', 3)
    sprite('ca043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ca043_01', 3)
    sprite('ca043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('ca045_00', 3)
    sprite('ca045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ca045_02', 3)
    sprite('ca045_03', 3)
    sprite('ca045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('ca045_01', 3)
    sprite('ca045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('ca045_05', 3)
    label(0)
    sprite('ca045_02', 3)
    sprite('ca045_03', 3)
    sprite('ca045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('ca045_01', 3)
    sprite('ca045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('ca090_00', 2)
    sprite('ca090_01', 2)
    sprite('ca090_02', 1)
    SetCommonActionMark(1)
    sprite('ca090_03', 6)
    sprite('ca090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('ca091_00', 2)
    sprite('ca091_01', 2)
    sprite('ca091_02', 1)
    SetCommonActionMark(1)
    sprite('ca091_03', 6)
    sprite('ca091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('ca092_00', 2)
    sprite('ca092_01', 2)
    sprite('ca092_02', 1)
    SetCommonActionMark(1)
    sprite('ca092_03', 6)
    sprite('ca092_04', 6)


@State
def CmnActAirTurn():
    sprite('ca025_00', 4)
    sprite('ca025_01', 4)
    sprite('ca025_02', 4)


@State
def CmnActLockWait():
    sprite('ca040_01', 2)
    sprite('ca040_02', 2)
    sprite('ca040_03', 2)
    sprite('ca040_04', 2)


@State
def CmnActLockReject():
    sprite('ca312_00', 2)
    sprite('ca312_01', 2)
    sprite('ca312_02', 2)
    sprite('ca312_03', 3)
    sprite('ca312_04', 3)
    sprite('ca312_05', 3)
    sprite('ca312_06', 3)
    sprite('ca312_07', 3)
    sprite('ca312_08', 3)


@State
def CmnActAirLockWait():
    sprite('ca045_02', 2)
    sprite('ca045_03', 2)
    sprite('ca045_04', 2)


@State
def CmnActAirLockReject():
    sprite('ca322_00', 2)
    sprite('ca322_01', 2)
    sprite('ca322_02', 2)
    sprite('ca322_03', 2)
    sprite('ca322_04', 2)
    sprite('ca322_05', 2)
    sprite('ca322_06', 2)
    sprite('ca322_07', 2)
    sprite('ca322_08', 2)
    sprite('ca322_09', 2)


@State
def CmnActLandSpin():
    sprite('ca071_00', 4)
    sprite('ca071_01', 4)
    label(0)
    sprite('ca071_02', 2)
    sprite('ca071_03', 2)
    sprite('ca071_04', 2)
    sprite('ca071_05', 2)
    sprite('ca071_06', 2)
    sprite('ca071_07', 2)
    sprite('ca071_08', 2)
    sprite('ca071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('ca071_10', 6)
    sprite('ca071_11', 5)
    sprite('ca071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('ca071_02', 2)
    sprite('ca071_03', 2)
    sprite('ca071_04', 2)
    sprite('ca071_05', 2)
    sprite('ca071_06', 2)
    sprite('ca071_07', 2)
    sprite('ca071_08', 2)
    sprite('ca071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('ca077_00', 2)
    sprite('ca077_01', 2)
    sprite('ca077_00ex00', 2)
    sprite('ca077_01ex00', 2)
    sprite('ca077_00ex01', 2)
    sprite('ca077_01ex01', 2)
    sprite('ca077_00ex02', 2)
    sprite('ca077_01ex02', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('ca077_02', 4)
    label(0)
    sprite('ca077_03', 3)
    sprite('ca077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('ca077_05', 5)
    sprite('ca077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ca060_07', 4)
    sprite('ca060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('ca060_11', 5)
    sprite('ca060_12', 4)


@State
def CmnActBurstBegin():
    sprite('ca331_00', 2)
    sprite('ca331_01', 2)
    label(0)
    sprite('ca331_02', 3)
    sprite('ca331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('ca331_04', 2)
    sprite('ca331_05', 2)
    sprite('ca331_06', 2)
    label(0)
    sprite('ca331_07', 3)
    sprite('ca331_08', 3)
    sprite('ca331_09', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('ca331_10', 3)
    sprite('ca331_11', 3)


@State
def CmnActAirBurstBegin():
    sprite('ca332_00', 2)
    sprite('ca332_01', 2)
    label(0)
    sprite('ca332_02', 3)
    sprite('ca332_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('ca332_04', 2)
    sprite('ca332_05', 2)
    sprite('ca332_06', 2)
    label(0)
    sprite('ca332_07', 2)
    sprite('ca332_08', 2)
    sprite('ca332_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('ca332_10', 2)
    sprite('ca332_11', 2)
    sprite('ca020_04', 3)
    sprite('ca020_05', 3)
    label(0)
    sprite('ca020_06', 4)
    sprite('ca020_07', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('ca333_00', 3)
    sprite('ca333_01', 3)
    sprite('ca333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ca333_03', 32767)
    CreateObject('EMB_CA_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('ca333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ca333_05', 3)
    sprite('ca333_06', 3)
    sprite('ca333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('ca333_08', 4)
    sprite('ca333_09', 4)
    sprite('ca333_10', 4)


@State
def CmnActAirOverDriveBegin():
    sprite('ca333_11', 3)
    sprite('ca333_12', 3)
    sprite('ca333_13', 3)
    CharacterFlash(16639, 20, 1)
    sprite('ca333_14', 32767)
    CreateObject('EMB_CA_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('ca333_15', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('ca333_05', 3)
    sprite('ca333_06', 3)
    sprite('ca333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('ca333_16', 4)
    sprite('ca333_17', 4)
    sprite('ca333_18', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
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
        HitOrBlockJumpCancel(1)
    sprite('ca200_00', 3)
    PerInertia(60)
    sprite('ca200_01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ca200_02', 3)
    sprite('ca200_03', 1)
    Recovery()
    Unknown2063()
    sprite('ca200_04', 1)
    sprite('ca200_05', 2)
    sprite('ca200_06', 2)
    sprite('ca200_07', 2)
    sprite('ca200_08', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(520)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('Atk6B_Input5')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockJumpCancel(1)
    sprite('ca201_00', 2)
    sprite('ca201_01', 2)
    sprite('ca201_02', 2)
    sprite('ca201_03', 1)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_1')
    sprite('ca201_04', 1)
    sprite('ca201_05', 2)
    ParticleRotationAngle(-28000)
    CallCustomizableParticle('caef_flag_hit', 0)
    sprite('ca201_06', 3)
    Recovery()
    Unknown2063()
    sprite('ca201_07', 3)
    sprite('ca201_08', 2)
    sprite('ca201_09', 2)
    sprite('ca201_10', 2)
    sprite('ca201_11', 2)
    sprite('ca201_12', 2)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(780)
        UseSlashHitspark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        AirUntechableTime(19)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitJumpCancel(1)
    sprite('ca202_00', 2)
    sprite('ca202_01', 2)
    sprite('ca202_02', 2)
    sprite('ca202_03', 2)
    sprite('ca202_04', 2)
    RandomCommonVoiceline(2)
    CommonSE('010_swing_sword_1')
    sprite('ca202_05', 1)
    sprite('ca202_06', 1)
    sprite('ca202_07', 3)
    CreateParticle('caef_spear_light', 0)
    ParticleRotationAngle(25000)
    CallCustomizableParticle('caef_spear', 1)
    sprite('ca202_08', 3)
    Recovery()
    Unknown2063()
    sprite('ca202_09', 3)
    sprite('ca202_10', 2)
    sprite('ca202_11', 2)
    sprite('ca202_12', 2)
    sprite('ca202_13', 2)
    sprite('ca202_14', 2)
    sprite('ca202_15', 2)
    sprite('ca202_16', 2)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        pass
    sprite('ca000_00', 1)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        HitAirUnblockable(0)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk5A')
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
        HitJumpCancel(1)
    sprite('ca230_00', 2)
    PerInertia(60)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ca230_01', 2)
    sprite('ca230_02', 2)
    sprite('ca230_03', 3)
    sprite('ca230_04', 2)
    Recovery()
    Unknown2063()
    sprite('ca230_05', 2)
    sprite('ca230_06', 2)
    sprite('ca230_07', 1)
    sprite('ca230_08', 1)
    sprite('ca230_09', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(480)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('Atk6B_Input5')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
    sprite('ca231_00', 2)
    sprite('ca231_01', 2)
    sprite('ca231_02', 2)
    RandomCommonVoiceline(1)
    CommonSE('010_swing_sword_0')
    sprite('ca231_03', 1)
    sprite('ca231_04', 1)
    sprite('ca231_05', 2)
    CreateParticle('caef_flag_hit', 0)
    sprite('ca231_06', 2)
    sprite('ca231_07', 3)
    Recovery()
    Unknown2063()
    sprite('ca231_08', 3)
    sprite('ca231_09', 3)
    sprite('ca231_10', 2)
    sprite('ca231_11', 2)
    sprite('ca231_12', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(760)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP1(90)
        AttackP2(82)
        AirPushbackY(34000)
        AirUntechableTime(29)
        MoveAttributes(0, 1, 0, 0, 0)
        HitOrBlockJumpCancel(1)
    sprite('ca232_00', 4)
    sprite('ca232_01', 3)
    sprite('ca232_02', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    CommonSE('005_swing_grap_2_0')
    sprite('ca232_03', 3)
    sprite('ca232_04', 3)
    ScreenShake(0, 5000)
    RandomCommonVoiceline(2)
    ParticleRotationAngle(20000)
    CallCustomizableParticle('caef_ca232', 0)
    sprite('ca232_05', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ca232_06', 3)
    sprite('ca232_07', 3)
    sprite('ca232_08', 3)
    sprite('ca232_09', 3)
    sprite('ca232_10', 3)
    sprite('ca232_11', 3)
    sprite('ca232_12', 3)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(720)
        UseSlashHitspark(1)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(16000)
        AirUntechableTime(40)
        CHHardKnockdown(3)
        EnableEmergencyTechAirHit(1)
    sprite('ca235_00', 2)
    sprite('ca235_01', 2)
    sprite('ca235_02', 2)
    sprite('ca235_03', 2)
    RandomCommonVoiceline(2)
    sprite('ca235_04', 2)
    sprite('ca235_05', 1)
    physicsXImpulse(12000)
    sprite('ca235_06', 1)
    sprite('ca235_07', 1)
    CreateParticle('caef_spear', 0)
    XImpulseAcceleration(180)
    sprite('ca235_08', 2)
    CommonSE('009_swing_rapier_2')
    CreateParticle('caef_spear_light', 0)
    sprite('ca235_09', 2)
    sprite('ca235_10', 2)
    CommonSE('009_swing_rapier_2')
    sprite('ca235_08', 2)
    CreateParticle('caef_spear', 0)
    sprite('ca235_09', 2)
    CommonSE('009_swing_rapier_2')
    sprite('ca235_11', 2)
    XImpulseAcceleration(25)
    Recovery()
    Unknown2063()
    sprite('ca235_12', 3)
    sprite('ca235_13', 3)
    physicsXImpulse(3000)
    sprite('ca235_14', 3)
    sprite('ca235_15', 3)
    physicsXImpulse(1000)
    sprite('ca235_16', 3)
    sprite('ca235_17', 3)
    physicsXImpulse(0)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        pass
    sprite('ca000_00', 1)


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
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('ca250_00', 1)
    sprite('ca250_01', 2)
    sprite('ca250_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('ca250_03', 4)
    sprite('ca250_04', 1)
    Recovery()
    Unknown2063()
    sprite('ca250_05', 2)
    sprite('ca250_06', 2)
    sprite('ca250_07', 2)
    sprite('ca250_08', 2)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(550)
        AirPushbackY(27000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockJumpCancel(1)
        AirUntechableTime(17)
        AttackP1(80)
        PushbackX(7500)
    sprite('ca251_00', 2)
    sprite('ca251_01', 2)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_2')
    sprite('ca251_02', 2)
    sprite('ca251_03', 2)
    sprite('ca251_04', 3)
    CreateParticle('caef_flag_swing', 0)
    sprite('ca251_06', 3)
    Recovery()
    Unknown2063()
    sprite('ca251_07', 3)
    sprite('ca251_08', 3)
    sprite('ca251_09', 3)
    sprite('ca251_10', 3)
    sprite('ca251_11', 3)
    sprite('ca251_12', 3)
    sprite('ca251_13', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(820)
        AttackP1(80)
        BonusProration(110)
        AirPushbackX(10000)
        AirPushbackY(-20000)
        YImpulseBeforeWallbounce(4000)
        AirUntechableTime(30)
        UseSlashHitspark(1)
    sprite('ca252_00', 2)
    sprite('ca252_01', 2)
    sprite('ca252_02', 2)
    RandomCommonVoiceline(2)
    sprite('ca252_03', 2)
    CommonSE('009_swing_rapier_2')
    sprite('ca252_04', 1)
    sprite('ca252_05', 2)
    sprite('ca252_06', 3)
    CreateParticle('caef_spear_light', 0)
    sprite('ca252_07', 3)
    Recovery()
    Unknown2063()
    sprite('ca252_08', 3)
    sprite('ca252_09', 3)
    sprite('ca252_10', 3)
    sprite('ca252_11', 3)
    sprite('ca252_12', 3)
    sprite('ca252_13', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(850)
        AirUntechableTime(28)
        Hitstun(19)
        UseSlashHitspark(1)
        AttackP1(80)
        HitCancel('NmlAtkAIR5A')
        HitCancel('NmlAtkAIR5B')
        HitCancel('NmlAtkAIR5C')
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        AirPushbackY(28000)
        ChainCancel(0)
        HitOverhead(0)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 2)
    sprite('ca255_00', 3)
    sprite('ca255_01', 3)
    PushSpeedX()
    EndMomentum(1)
    PopSpeedX()
    XImpulseAcceleration(50)
    physicsYImpulse(3000)
    setGravity(600)
    sprite('ca255_02', 3)
    XImpulseAcceleration(25)
    RandomCommonVoiceline(2)
    CreateParticle('caef_spear_light', 0)
    EnableAfterimage(1)
    loopRest()
    sprite('ca255_03', 2)
    XImpulseAcceleration(0)
    physicsYImpulse(-21000)
    setGravity(1400)
    label(0)
    sprite('ca255_04', 2)
    CommonSE('009_swing_rapier_2')
    ParticleRotationAngle(90000)
    CallCustomizableParticle('caef_spear', 0)
    sprite('ca255_05', 2)
    CreateParticle('caef_ca255', 0)
    sprite('ca255_03', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca255_15', 2)
    physicsXImpulse(0)
    SetXCollisionFromOrigin(-1)
    EnableAfterimage(0)
    LandingEffects(100, 1, 1)
    Recovery()
    sprite('ca255_16', 2)
    sprite('ca255_17', 2)
    sprite('ca255_18', 2)
    sprite('ca255_19', 2)
    sprite('ca255_20', 2)
    sprite('ca255_21', 3)
    sprite('ca255_22', 3)
    loopRest()
    ExitState()
    label(2)
    sprite('ca255_06', 2)
    SetXCollisionFromOrigin(-1)
    EnableAfterimage(0)
    physicsYImpulse(18000)
    physicsXImpulse(18000)
    Recovery()
    sprite('ca255_07', 2)
    sprite('ca255_08', 2)
    sprite('ca255_09', 2)
    sprite('ca255_10', 3)
    ForceFaceSprite()
    ChainCancel(1)
    XImpulseAcceleration(75)
    sprite('ca255_11', 3)
    sprite('ca255_12', 4)
    sprite('ca255_13', 4)
    XImpulseAcceleration(75)
    sprite('ca255_14', 4)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        pass
    sprite('ca000_00', 1)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        UseSlashHitspark(1)
        AttackP1(90)
        HitAirUnblockable(3)
        AirUntechableTime(26)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirPushbackX(10000)
        HitOrBlockJumpCancel(1)
    sprite('ca210_00', 2)
    sprite('ca210_01', 2)
    sprite('ca210_02', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('ca210_03', 2)
    sprite('ca210_04', 1)
    RandomCommonVoiceline(1)
    sprite('ca210_05', 1)
    CommonSE('009_swing_rapier_1')
    sprite('ca210_06', 2)
    sprite('ca210_07', 2)
    sprite('ca210_08', 4)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ca210_09', 4)
    sprite('ca210_10', 4)
    sprite('ca210_11', 4)
    sprite('ca210_12', 4)
    sprite('ca210_13', 4)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(95)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        PushbackX(7500)
        SetXCollisionFromOrigin(50)
        CHAirHitstunAnimation(11)
        CHGroundedHitstunAnimation(6)
        CHAirPushbackX(-2000)
        CHAirPushbackY(24000)
        CHAirUntechableTime(42)
        CHHitstun(42)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ca211_00', 3)
    sprite('ca211_01', 3)
    physicsXImpulse(20000)
    sprite('ca211_02', 4)
    sprite('ca211_03', 2)
    LandingEffects(100, 1, 1)
    sprite('ca211_04', 2)
    CommonSE('008_swing_pole_2')
    RandomCommonVoiceline(1)
    XImpulseAcceleration(50)
    CreateParticle('caef_flag_swing', 0)
    sprite('ca211_05', 2)
    sprite('ca211_06', 2)
    XImpulseAcceleration(50)
    sprite('ca211_07', 2)
    XImpulseAcceleration(50)
    sprite('ca211_08', 2)
    XImpulseAcceleration(0)
    Recovery()
    Unknown2063()
    sprite('ca211_09', 2)
    sprite('ca211_11', 2)
    sprite('ca211_12', 3)
    sprite('ca211_13', 3)
    sprite('ca211_14', 4)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        HitOverhead(2)
        UseSlashHitspark(1)
        GroundedHitstunAnimation(3)
        AirUntechableTime(35)
        AirPushbackY(-50000)
        GroundBounce(1)
        BouncePercentage(25)
        StarterRating(2)
        FatalCounter(1)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ca213_00', 3)
    sprite('ca213_01', 3)
    sprite('ca213_02', 3)
    physicsXImpulse(2500)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('ca213_03', 3)
    XImpulseAcceleration(360)
    physicsYImpulse(8500)
    setGravity(2000)
    sprite('ca213_03', 3)
    XImpulseAcceleration(200)
    sprite('ca213_04', 32767)
    label(1)
    sprite('ca213_05', 2)
    XImpulseAcceleration(50)
    RandomCommonVoiceline(2)
    setInvincible(0)
    LandingEffects(100, 1, 1)
    CommonSE('010_swing_sword_1')
    sprite('ca213_06', 3)
    XImpulseAcceleration(0)
    ParticleSize(1125)
    CallCustomizableParticle('caef_ca213', 0)
    ScreenShake(0, 5000)
    sprite('ca213_07', 3)
    sprite('ca213_08', 4)
    Recovery()
    Unknown2063()
    sprite('ca212_12ex01', 3)
    sprite('ca212_13ex01', 3)
    sprite('ca212_14', 3)
    sprite('ca212_15', 3)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        pass
    sprite('ca000_00', 1)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    if random_(2, 0, 50):
        gotoLabel(1)
    sprite('ca300_00', 3)
    sprite('ca300_00', 4)
    Voiceline('ca405')
    sprite('ca300_01', 7)
    sprite('ca300_02', 7)
    sprite('ca300_03', 7)
    sprite('ca300_04', 7)
    sprite('ca300_05', 7)
    sprite('ca300_06', 7)
    sprite('ca300_07', 7)
    sprite('ca300_08', 7)
    sprite('ca300_09', 7)
    sprite('ca300_10', 7)
    sprite('ca300_11', 7)
    loopRest()
    ExitState()
    label(1)
    if not SLOT_140:
        gotoLabel(100)
    if SLOT_44:
        gotoLabel(100)
    CopyFromRightToLeft(23, 2, 51, 11, 2, 22)
    if SLOT_XDistanceFromCenterOfStage > SLOT_51:
        if SLOT_IsFacingRight:
            gotoLabel(2)
    elif not SLOT_IsFacingRight:
        gotoLabel(2)
    sprite('ca003_00', 6)
    Flip()
    sprite('ca003_01', 6)
    sprite('ca003_02', 6)
    loopRest()
    label(2)
    sprite('ca612_00', 6)
    Voiceline('ca404')
    loopRest()
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    label(3)
    sprite('ca612_03', 1)
    if SLOT_97:
        conditionalSendToLabel(3)
    sprite('ca612_02', 6)
    sprite('ca612_01', 6)
    sprite('ca612_00', 6)
    loopRest()
    ExitState()
    label(100)
    sprite('ca300_00', 3)
    sprite('ca300_00', 4)
    Voiceline('ca404')
    sprite('ca300_01', 7)
    sprite('ca300_02', 7)
    sprite('ca300_03', 7)
    sprite('ca300_04', 7)
    sprite('ca300_05', 7)
    sprite('ca300_06', 7)
    sprite('ca300_07', 7)
    sprite('ca300_08', 7)
    sprite('ca300_09', 7)
    sprite('ca300_10', 7)
    sprite('ca300_11', 7)
    loopRest()
    ExitState()


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
    sprite('ca212_00', 2)
    sprite('ca212_01', 2)
    sprite('ca212_02', 3)
    sprite('ca212_03', 3)
    sprite('ca212_07', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('ca212_08', 3)
    CreateParticle('caef_ca232', 0)
    sprite('ca212_09', 4)
    sprite('ca212_10', 4)
    sprite('ca212_11', 4)
    sprite('ca212_12', 5)
    sprite('ca212_13', 5)
    sprite('ca212_14', 5)
    sprite('ca212_15', 5)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(11)
        AirPushbackX(2000)
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
        StayAfterMovement(1, 0)

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
    sprite('ca407_00', 3)
    sprite('ca407_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    Voiceline('ca159')
    HeatChange(-2500)
    sprite('ca407_01', 1)
    CharacterFlash(16763080, 8, 2)
    label(100)
    sprite('ca407_02', 3)
    CommonSE('011_spin_2')
    sprite('ca407_03', 3)
    CommonSE('011_spin_2')
    sprite('ca407_04', 3)
    CommonSE('011_spin_2')
    gotoLabel(100)
    label(0)
    sprite('ca407_02', 3)
    CommonSE('008_swing_pole_1')
    clearUponHandler(EVERY_FRAME)
    sprite('ca407_03', 3)
    CommonSE('011_spin_2')
    sprite('ca407_05', 3)
    CommonSE('010_swing_sword_1')
    sprite('ca407_06', 1)
    CreateParticle('caef_guardcrash', 0)
    sprite('ca407_06', 3)
    StartMultihit()
    EnableAfterimage(0)
    sprite('ca407_07', 4)
    CommonSE('213_bound_1')
    sprite('ca407_08', 4)
    sprite('ca407_09', 4)
    sprite('ca407_10', 3)
    sprite('ca212_13', 3)
    AddX(60000)
    sprite('ca212_14', 2)
    sprite('ca212_15', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ca310_00', 3)
    sprite('ca310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ca310_02', 3)
    sprite('ca310_03', 3)
    sprite('ca310_04', 4)
    SmartVoiceline('ca155')
    sprite('ca310_05', 4)
    sprite('ca310_06', 4)
    sprite('ca310_07', 4)
    sprite('ca310_08', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(-30000)
        HardKnockdown(33)
    sprite('ca310_02', 3)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('ca311_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca311_01', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca311_02', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca311_03', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca311_04', 3)
    Voiceline('ca153')
    CommonSE('005_swing_grap_2_1')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca311_05', 3)
    ScreenShake(0, 10000)
    sprite('ca311_06', 2)
    sprite('ca311_07', 2)
    sprite('ca311_08', 2)
    sprite('ca311_09', 2)
    sprite('ca311_10', 2)
    sprite('ca311_11', 2)
    sprite('ca311_12', 2)
    sprite('ca311_13', 2)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('ca310_00', 3)
    sprite('ca310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ca310_02', 3)
    sprite('ca310_03', 3)
    sprite('ca310_04', 4)
    SmartVoiceline('ca155')
    sprite('ca310_05', 4)
    sprite('ca310_06', 4)
    sprite('ca310_07', 4)
    sprite('ca310_08', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(-38000)
        AirUntechableTime(100)
        AttackDirection(1)
        GroundBounce(1)
        BouncePercentage(100)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
    sprite('ca310_02', 3)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('ca313_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca313_01', 3)
    CommonSE('008_swing_pole_2')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca313_02', 3)
    Voiceline('ca153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca313_03', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 1, 50, 0)
    sprite('ca313_04', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('ca313_05', 3)
    OppThrowAnimation(5, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ca313_06', 3)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('ca313_07', 3)
    sprite('ca313_08', 3)
    sprite('ca313_09', 3)
    sprite('ca313_10', 3)
    sprite('ca313_11', 3)
    sprite('ca313_12', 3)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        SetZLine(0, 50)
        RangeCheck(120000)
    sprite('ca320_00', 3)
    sprite('ca320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('ca320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('ca320_03', 3)
    SmartVoiceline('ca155')
    sprite('ca320_04', 4)
    sprite('ca320_05', 4)
    sprite('ca320_06', 4)
    sprite('ca320_07', 4)
    sprite('ca320_08', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        Hitstop(0)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-200000)
        AirPushbackX(0)
        GroundBounce(1)
        BouncePercentage(20)
        AirUntechableTime(80)
        ForcedLandingRecovery(0, 0)
    sprite('ca320_02', 5)
    StartMultihit()
    OppThrowAnimation(9, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('ca321_01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca321_02', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca321_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca321_04', 4)
    Voiceline('ca154')
    CommonSE('005_swing_grap_2_1')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('ca321_05', 4)
    sprite('ca321_06', 3)
    sprite('ca321_07', 3)
    sprite('ca321_08', 3)
    sprite('ca321_09', 3)
    GravityDefault()
    sprite('ca321_10', 3)
    sprite('ca321_11', 3)
    sprite('ca321_12', 3)


@State
def OrderNirvanaRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
    sprite('ca432_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ca432_01', 3)
    sprite('ca432_01', 3)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(40, -1, 0)
    InvincibilityDuration(40)
    sprite('ca432_02', 5)
    sprite('ca432_03', 5)
    sprite('ca432_04', 5)
    sprite('ca432_05', 6)
    sprite('ca432_06', 7)
    sprite('ca432_07', 8)
    sprite('ca432_08', 4)
    Voiceline('ca251')
    sprite('ca432_09', 4)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_13', 6)
    sprite('ca432_14', 6)
    sprite('ca432_15', 6)


@State
def OrderNirvanaRushOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        AttackType(4)
    sprite('ca432_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ca432_01', 3)
    sprite('ca432_01', 3)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(40, -1, 0)
    InvincibilityDuration(40)
    sprite('ca432_02', 5)
    sprite('ca432_03', 5)
    sprite('ca432_04', 5)
    sprite('ca432_05', 6)
    sprite('ca432_06', 7)
    sprite('ca432_07', 8)
    sprite('ca432_08', 4)
    Voiceline('ca251')
    sprite('ca432_09', 4)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_13', 6)
    sprite('ca432_14', 6)
    sprite('ca432_15', 6)


@State
def OrderNirvanaRushAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        EndMomentum(1)
    sprite('ca432_01ex01', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ca432_02ex01', 3)
    sprite('ca432_02ex01', 2)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(50, -1, 0)
    setInvincible(1)
    Voiceline('ca251')
    sprite('ca432_03ex01', 5)
    sprite('ca432_04ex01', 5)
    sprite('ca432_05ex01', 6)
    sprite('ca432_06ex01', 7)
    sprite('ca432_07ex01', 8)
    sprite('ca432_08ex01', 4)
    sprite('ca432_09ex01', 4)
    sprite('ca432_10ex01', 3)
    setInvincible(0)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_13ex01', 6)
    sprite('ca432_16', 6)
    sprite('ca432_17', 6)


@State
def OrderNirvanaRushAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        EndMomentum(1)
        AttackType(4)
    sprite('ca432_01ex01', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ca432_02ex01', 3)
    sprite('ca432_02ex01', 2)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(50, -1, 0)
    setInvincible(1)
    Voiceline('ca251')
    sprite('ca432_03ex01', 5)
    sprite('ca432_04ex01', 5)
    sprite('ca432_05ex01', 6)
    sprite('ca432_06ex01', 7)
    sprite('ca432_07ex01', 8)
    sprite('ca432_08ex01', 4)
    sprite('ca432_09ex01', 4)
    sprite('ca432_10ex01', 3)
    setInvincible(0)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_13ex01', 6)
    sprite('ca432_16', 6)
    sprite('ca432_17', 6)


@State
def OrderNirvanaStrike():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
    sprite('ca432_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 34)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(103, -1, 0)
    setInvincible(1)
    Voiceline('ca252')
    sprite('ca432_01', 6)
    sprite('ca432_02', 5)
    sprite('ca432_03', 5)
    sprite('ca432_04', 5)
    sprite('ca432_05', 6)
    sprite('ca432_06', 7)
    sprite('ca432_07', 8)
    sprite('ca432_08', 4)
    sprite('ca432_09', 4)
    sprite('ca432_10', 3)
    setInvincible(0)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_13', 6)
    sprite('ca432_14', 6)
    sprite('ca432_15', 6)


@State
def OrderNirvanaStrikeOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
    sprite('ca432_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 34)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(135, -1, 0)
    setInvincible(1)
    Voiceline('ca252')
    sprite('ca432_01', 6)
    sprite('ca432_02', 5)
    sprite('ca432_03', 5)
    sprite('ca432_04', 5)
    sprite('ca432_05', 6)
    sprite('ca432_06', 7)
    sprite('ca432_07', 8)
    sprite('ca432_08', 4)
    sprite('ca432_09', 4)
    sprite('ca432_10', 3)
    setInvincible(0)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 2)
    sprite('ca432_13', 6)
    sprite('ca432_14', 6)
    sprite('ca432_15', 6)


@State
def OrderNirvanaStrikeAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        EndMomentum(1)
    sprite('ca432_01ex01', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 34)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(103, -1, 0)
    setInvincible(1)
    Voiceline('ca252')
    sprite('ca432_02ex01', 5)
    sprite('ca432_03ex01', 5)
    sprite('ca432_04ex01', 5)
    sprite('ca432_05ex01', 6)
    sprite('ca432_06ex01', 7)
    sprite('ca432_07ex01', 8)
    sprite('ca432_08ex01', 4)
    sprite('ca432_09ex01', 4)
    sprite('ca432_10ex01', 3)
    setInvincible(0)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_13ex01', 6)
    sprite('ca432_16', 6)
    sprite('ca432_17', 6)


@State
def OrderNirvanaStrikeAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
        AttackType(4)
        EndMomentum(1)
    sprite('ca432_01ex01', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 34)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(135, -1, 0)
    setInvincible(1)
    Voiceline('ca252')
    sprite('ca432_02ex01', 5)
    sprite('ca432_03ex01', 5)
    sprite('ca432_04ex01', 5)
    sprite('ca432_05ex01', 6)
    sprite('ca432_06ex01', 7)
    sprite('ca432_07ex01', 8)
    sprite('ca432_08ex01', 4)
    sprite('ca432_09ex01', 4)
    sprite('ca432_10ex01', 3)
    setInvincible(0)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_12ex01', 3)
    sprite('ca432_11ex01', 3)
    sprite('ca432_10ex01', 2)
    sprite('ca432_13ex01', 6)
    sprite('ca432_16', 6)
    sprite('ca432_17', 6)


@State
def UltimateLock():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
    sprite('ca432_00', 6)
    setInvincible(1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 41)
    HeatChange(-5000)
    CreateObject('EMB_CA', -1)
    DistortionSettings(89, -1, 0)
    Voiceline('ca253')
    sprite('ca432_01', 6)

    def upon_32():
        sendToLabel(1)

    def upon_33():
        sendToLabel(2)
    sprite('ca432_02', 5)
    sprite('ca432_03', 5)
    sprite('ca432_04', 5)
    sprite('ca432_05', 6)
    sprite('ca432_06', 7)
    sprite('ca432_07', 8)
    sprite('ca432_08', 4)
    sprite('ca432_09', 4)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_10', 3)
    sprite('ca432_11', 3)
    sprite('ca432_12', 3)
    sprite('ca432_11', 3)
    sprite('ca432_13', 6)
    sprite('ca432_14', 6)
    sprite('ca432_15', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sendToLabel(2)
    label(1)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca615_00', 10)
    Voiceline('ca254')
    sprite('ca615_01', 7)
    sprite('ca615_02', 7)
    sprite('ca615_03', 7)
    sprite('ca615_04', 7)
    sprite('ca615_05', 7)
    sprite('ca615_06', 7)
    CommonSE('204_runjump_normal_0')
    PrivateSE('case_25')
    CreateParticle('rcef_pachinB', 0)
    sprite('ca615_07', 50)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca300_00', 7)
    sprite('ca300_01', 7)
    sprite('ca300_02', 7)
    sprite('ca300_03', 7)
    sprite('ca300_04', 7)
    sprite('ca300_05', 7)
    sprite('ca300_06', 7)
    sprite('ca300_07', 7)
    sprite('ca300_08', 7)
    sprite('ca300_09', 7)
    sprite('ca300_10', 7)
    sprite('ca300_11', 7)
    loopRest()
    ExitState()
    label(2)
    sprite('ca001_00', 5)
    setInvincible(0)
    sprite('ca001_01', 5)
    sprite('ca001_02', 5)
    sprite('ca001_03', 5)
    sprite('ca001_04', 6)
    sprite('ca001_05', 6)
    sprite('ca001_06', 6)
    sprite('ca001_07', 6)
    loopRest()
    ExitState()


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(33)
            ObjectGotoState(11, 'GoAstral', 1)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(32)
            clearUponHandler(33)
            sendToLabel(10)
    sprite('ca001_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    DistortionSettings(100, -1, 2)
    EmptyHeat()
    CreateObject('EMB_CA_AH', -1)
    Voiceline('ca290')
    sprite('ca001_01', 6)
    sprite('ca001_02', 6)
    sprite('ca001_03', 50)
    sprite('ca001_04', 5)
    sprite('ca001_05', 5)
    sprite('ca001_06', 5)
    sprite('ca001_07', 5)
    sprite('ca000_00', 5)
    sprite('ca450_00', 5)
    sprite('ca450_01', 5)
    sprite('ca450_02', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    label(10)
    sprite('ca450_16', 5)
    setInvincible(0)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('ca450_17', 5)
    ExitState()
    label(1)
    sprite('ca450_03', 5)
    sprite('ca450_04', 5)
    sprite('ca450_05', 5)
    sprite('ca450_06', 6)
    sprite('ca450_07', 6)
    sprite('ca450_08', 6)
    sprite('ca450_09', 6)
    sprite('ca450_10', 6)
    sprite('ca450_11', 6)

    def RunOnObject_22():
        CharacterFlash2(-1, 10)
    sprite('ca450_12', 6)
    CreateObject('AstKyushu', -1)
    sprite('ca450_13', 5)

    def RunOnObject_22():
        Visibility(1)
        SetScaleSpeed(0)
        Size(1000)
    sprite('ca450_14', 5)
    sprite('ca450_15', 5)
    sprite('ca450_13', 5)
    sprite('ca450_14', 5)
    sprite('ca450_15', 5)
    sprite('ca450_13', 5)
    sprite('ca450_14', 5)
    sprite('ca450_14', 5)
    sprite('ca450_15', 5)
    sprite('ca450_13', 5)
    sprite('ca450_14', 5)
    sprite('ca450_15', 5)
    sprite('ca450_13', 5)
    sprite('ca450_14', 5)
    Visibility(1)
    sprite('ca450_15', 280)
    sprite('ca450_15', 200)
    sprite('ca450_13', 5)
    SetPosXByScreenPer(50)
    Visibility(0)


@State
def OrderNirvanaBomb():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
    sprite('ca001_00', 6)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 33)
    DistortionSettings(16, -1, 2)
    EmptyHeat()
    CreateObject('EMB_CA_AH', -1)
    Voiceline('ca307')
    sprite('ca001_01', 6)
    sprite('ca001_02', 6)
    sprite('ca001_03', 24)
    setInvincible(0)
    sprite('ca001_04', 6)
    sprite('ca001_05', 6)
    sprite('ca001_06', 6)
    sprite('ca001_07', 6)


@State
def ShortDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('ca032_00', 2)
    AirDashEffects(0)
    sprite('ca032_01', 1)
    physicsXImpulse(25000)
    physicsYImpulse(10000)
    setGravity(2100)
    label(0)
    sprite('ca032_01', 2)
    sprite('ca032_02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca032_03', 2)
    LandingEffects(100, 1, 1)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    EndMomentum(1)
    sprite('ca032_04', 2)
    sprite('ca032_05', 2)


@State
def Rolling_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('ca404_00', 2)
    setInvincible(1)
    GuardPoint_(0)
    SpecificInvincibility(0, 0, 0, 1, 0)
    CreateParticle('caef_ca404', -1)
    Voiceline('ca200')
    EnableCollision(0)
    physicsXImpulse(17500)
    DashEffects(100, 1, 0)
    sprite('ca404_01', 2)
    sprite('ca404_02', 2)
    sprite('ca404_03', 2)
    CommonSE('019_cloth_a')
    sprite('ca404_04', 2)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(140)
    sprite('ca404_05', 2)
    CommonSE('019_cloth_a')
    sprite('ca404_06', 2)
    sprite('ca404_08', 2)
    CommonSE('019_cloth_a')
    DashEffects(100, 1, 0)
    sprite('ca404_09', 2)
    setInvincible(0)
    DashEffects(100, 1, 0)
    XImpulseAcceleration(50)
    sprite('ca404_10', 2)
    DashEffects(100, 1, 0)
    EnableCollision(1)
    sprite('ca404_11', 2)
    XImpulseAcceleration(50)
    sprite('ca404_12', 2)
    sprite('ca404_13', 2)
    AddInertia(3000)
    sprite('ca404_14', 2)
    WhiffNormalCancel(1)
    ForceFaceSprite()


@State
def Rolling_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        PreventBlocking(1)
    sprite('ca404_00', 2)
    setInvincible(1)
    GuardPoint_(0)
    SpecificInvincibility(1, 1, 0, 0, 0)
    CreateParticle('caef_dash_smoke', -1)
    CreateParticle('caef_ca404', -1)
    Voiceline('ca201')
    EnableCollision(0)
    physicsXImpulse(20000)
    DashEffects(100, 1, 0)
    sprite('ca404_01', 2)
    sprite('ca404_02', 2)
    CreateParticle('caef_dash_smoke', -1)
    DashEffects(100, 1, 0)
    sprite('ca404_03', 2)
    CommonSE('019_cloth_a')
    sprite('ca404_04', 2)
    CreateParticle('caef_dash_smoke', -1)
    CreateParticle('caef_ca404', -1)
    DashEffects(100, 1, 0)
    physicsXImpulse(28000)
    sprite('ca404_05', 2)
    CommonSE('019_cloth_a')
    sprite('ca404_06', 2)
    CreateParticle('caef_dash_smoke', -1)
    DashEffects(100, 1, 0)
    sprite('ca404_07', 2)
    CommonSE('019_cloth_a')
    sprite('ca404_04', 2)
    CreateParticle('caef_dash_smoke', -1)
    sprite('ca404_08', 3)
    CreateParticle('caef_ca404', -1)
    CommonSE('019_cloth_a')
    DashEffects(100, 1, 0)
    sprite('ca404_09', 3)
    DashEffects(100, 1, 0)
    physicsXImpulse(14000)
    sprite('ca404_10', 3)
    DashEffects(100, 1, 0)
    EnableCollision(1)
    sprite('ca404_11', 3)
    physicsXImpulse(10000)
    sprite('ca404_12', 3)
    setInvincible(0)
    sprite('ca404_13', 3)
    sprite('ca404_14', 3)
    AddInertia(6000)
    Flip()


@State
def Air_MultiHit():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(3)
        Damage(700)
        ProjectileLevel(0)
        StrikeProjectileLevel(1)
        AttackP1(80)
        Hitstop(0)
        PushbackX(12000)
        Blockstun(11)
        AttackP2(92)
        SameMoveProration(10)
        SingleProration(1)
        VoodooDamageMultiplier(3)
        MoveAttributes(1, 0, 0, 0, 0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(10000)
        AirUntechableTime(45)
        ForcedLandingRecovery(2, 1)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            AddActionMark(1)
            if SLOT_2 >= 2:
                Damage(100)
                if SLOT_137:
                    DamageMultiplier(80)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ca406_00', 2)
    sprite('ca406_01', 2)
    sprite('ca406_02', 3)
    CommonSE('019_cloth_b')
    sprite('ca406_03', 3)
    sprite('ca406_04', 2)
    Voiceline('ca202')
    physicsXImpulse(-3000)
    physicsYImpulse(6500)
    setGravity(300)
    sprite('ca406_05', 2)
    UsePunchHitspark(1)
    UseSlashHitspark(0)
    CreateObject('multi_bishop', 0)
    ObjectHitbox(1)
    sprite('ca406_06', 2)
    sprite('ca406_07', 2)
    RefreshMultihit()
    UsePunchHitspark(1)
    UseSlashHitspark(0)
    CreateObject('multi_pawn', 0)
    ObjectHitbox(1)
    sprite('ca406_08', 2)
    sprite('ca406_09', 2)
    RefreshMultihit()
    UsePunchHitspark(0)
    UseSlashHitspark(1)
    CreateObject('multi_knight', 0)
    ObjectHitbox(1)
    sprite('ca406_10', 2)
    sprite('ca406_05', 2)
    RefreshMultihit()
    UsePunchHitspark(1)
    UseSlashHitspark(0)
    CreateObject('multi_bishop', 0)
    ObjectHitbox(1)
    sprite('ca406_06', 2)
    sprite('ca406_07', 2)
    RefreshMultihit()
    UsePunchHitspark(1)
    UseSlashHitspark(0)
    CreateObject('multi_pawn', 0)
    ObjectHitbox(1)
    sprite('ca406_08', 2)
    sprite('ca406_09', 2)
    RefreshMultihit()
    UsePunchHitspark(0)
    UseSlashHitspark(1)
    CreateObject('multi_knight', 0)
    ObjectHitbox(1)
    sprite('ca406_10', 2)
    sprite('ca406_05', 3)
    AttackOff()
    Recovery()
    EndYPhysicsImpulse()
    sprite('ca406_06', 3)
    sprite('ca406_07', 3)
    sprite('ca406_08', 3)
    sprite('ca406_09', 3)
    sprite('ca406_10', 3)
    sprite('ca406_11', 4)
    sprite('ca406_12', 4)
    sprite('ca406_13', 4)


@State
def RemoteThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        StayAfterMovement(1, 0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
    sprite('ca405_00', 2)
    sprite('ca405_01', 2)
    CommonSE('019_cloth_c')
    sprite('ca405_02', 2)
    CreateObject('Throw_Pawn15', 0)
    sprite('ca405_03', 2)
    sprite('ca405_04', 2)
    loopRest()
    label(0)
    sprite('ca405_05', 2)
    sprite('ca405_06', 2)
    sprite('ca405_07', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('ca405_25', 3)
    Recovery()
    sprite('ca405_26', 3)
    sprite('ca405_27', 3)
    sprite('ca405_28', 3)
    sprite('ca405_29', 3)
    ExitState()
    label(2)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('ca405_08', 5)
    SLOT_58 = 1
    sprite('ca405_09', 5)
    sprite('ca405_10', 5)
    sprite('ca405_11', 3)
    Voiceline('ca203')
    sprite('ca405_12', 3)
    sprite('ca405_13', 3)
    sprite('ca405_14', 3)
    sprite('ca405_15', 2)
    sprite('ca405_16', 2)
    PrivateSE('case_08')
    sprite('ca405_17', 2)
    sprite('ca405_15', 2)
    sprite('ca405_16', 2)
    sprite('ca405_18', 3)
    sprite('ca405_19', 3)
    sprite('ca405_20', 3)
    sprite('ca405_21', 3)
    sprite('ca405_22', 3)
    sprite('ca405_23', 3)
    sprite('ca405_24', 3)


@State
def UltimateHaguruma():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        StayAfterMovement(1, 0)
        RunLoopUpon(17, 166)

        def upon_17():
            sendToLabel(1)
    sprite('ca430_00', 4)
    sprite('ca430_01', 3)
    sprite('ca430_01', 1)
    CreateObject('EMB_CA', -1)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    Voiceline('ca250')
    setInvincible(1)
    sprite('ca430_02', 4)
    sprite('ca430_03', 4)
    sprite('ca430_04', 4)
    sprite('ca430_05', 4)
    CreateObject('ca_gear', 0)
    setInvincible(0)
    sprite('ca430_06', 3)
    sprite('ca430_07', 3)
    sprite('ca430_08', 3)
    sprite('ca430_09', 3)
    sprite('ca430_10', 3)
    sprite('ca430_11', 3)
    sprite('ca430_12', 3)
    sprite('ca430_13', 3)
    sprite('ca430_14', 3)
    sprite('ca430_15', 3)
    sprite('ca430_16', 3)
    sprite('ca430_17', 3)
    label(0)
    sprite('ca430_18', 3)
    sprite('ca430_19', 3)
    sprite('ca430_20', 3)
    sprite('ca430_21', 3)
    gotoLabel(0)
    label(1)
    sprite('ca430_22', 5)
    EnableAfterimage(0)
    sprite('ca430_23', 5)
    sprite('ca430_24', 5)


@State
def UltimateHagurumaOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        StayAfterMovement(1, 0)
        AttackType(4)
        RunLoopUpon(17, 178)

        def upon_17():
            sendToLabel(1)
    sprite('ca430_00', 4)
    sprite('ca430_01', 3)
    sprite('ca430_01', 1)
    CreateObject('EMB_CA', -1)
    DistortionSettings(50, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    Voiceline('ca250')
    setInvincible(1)
    sprite('ca430_02', 4)
    sprite('ca430_03', 4)
    sprite('ca430_04', 4)
    sprite('ca430_05', 4)
    CreateObject('ca_gearOD', 0)
    setInvincible(0)
    sprite('ca430_06', 3)
    sprite('ca430_07', 3)
    sprite('ca430_08', 3)
    sprite('ca430_09', 3)
    sprite('ca430_10', 3)
    sprite('ca430_11', 3)
    sprite('ca430_12', 3)
    sprite('ca430_13', 3)
    sprite('ca430_14', 3)
    sprite('ca430_15', 3)
    sprite('ca430_16', 3)
    sprite('ca430_17', 3)
    label(0)
    sprite('ca430_18', 3)
    sprite('ca430_19', 3)
    sprite('ca430_20', 3)
    sprite('ca430_21', 3)
    gotoLabel(0)
    label(1)
    sprite('ca430_22', 5)
    EnableAfterimage(0)
    sprite('ca430_23', 5)
    sprite('ca430_24', 5)


@State
def PosingStandStarting():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
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
    sprite('ca203_00', 4)
    sprite('ca203_01', 4)
    sprite('ca203_02', 4)
    sprite('ca203_03', 4)
    sprite('ca203_04', 4)
    sprite('ca203_05', 4)
    sprite('ca203_06', 4)
    sprite('ca203_07', 4)
    sprite('ca203_08', 4)


@State
def PosingStandAttack():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
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
    sprite('ca204_00', 4)
    sprite('ca204_01', 4)
    sprite('ca204_02', 4)
    sprite('ca204_03', 4)
    sprite('ca204_04', 4)
    sprite('ca204_05', 4)
    sprite('ca204_06', 4)
    sprite('ca204_07', 4)
    sprite('ca204_08', 4)


@State
def PosingCrouchStarting():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        CrouchState(1)
        WhiffStandCancel(1)
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
    sprite('ca233_00', 4)
    sprite('ca233_01', 4)
    sprite('ca233_02', 4)
    sprite('ca233_03', 4)
    sprite('ca233_04', 4)
    sprite('ca233_05', 4)
    sprite('ca233_06', 4)
    sprite('ca233_07', 4)


@State
def PosingCrouchAttack():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        CrouchState(1)
        WhiffStandCancel(1)
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
    sprite('ca234_00', 4)
    sprite('ca234_01', 4)
    sprite('ca234_02', 4)
    sprite('ca234_03', 4)
    sprite('ca234_04', 4)
    sprite('ca234_05', 4)
    sprite('ca234_06', 4)
    sprite('ca234_07', 4)


@State
def PosingAirStarting():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        AirDashMomentum(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffOverdriveCancel(1)
        WhiffAirJumpCancel(1)
        WhiffFAirDashCancel(1)
        WhiffBAirDashCancel(1)
        WhiffBlockCancel(1)
        WhiffBarrierCancel2(1)
        EnablePreGuard(1)
    sprite('ca253_00', 4)
    sprite('ca253_01', 4)
    sprite('ca253_02', 4)
    sprite('ca253_03', 4)
    sprite('ca253_04', 4)
    sprite('ca253_05', 4)
    sprite('ca253_06', 4)
    sprite('ca253_07', 4)


@State
def PosingAirAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        AirDashMomentum(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffOverdriveCancel(1)
        WhiffAirJumpCancel(1)
        WhiffFAirDashCancel(1)
        WhiffBAirDashCancel(1)
        WhiffBlockCancel(1)
        WhiffBarrierCancel2(1)
        EnablePreGuard(1)
    sprite('ca254_00', 4)
    sprite('ca254_01', 4)
    sprite('ca254_02', 4)
    sprite('ca254_03', 4)
    sprite('ca254_04', 4)
    sprite('ca254_05', 4)
    sprite('ca254_06', 4)
    sprite('ca254_07', 4)


@State
def SpecialPosingStandAttack():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
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
    sprite('ca402_00', 4)
    sprite('ca402_01', 4)
    sprite('ca402_02', 4)
    sprite('ca402_03', 4)
    sprite('ca402_04', 4)
    sprite('ca402_05', 4)
    sprite('ca402_06', 4)
    sprite('ca402_07', 4)
    sprite('ca402_08', 4)
    sprite('ca402_09', 4)
    sprite('ca402_10', 4)
    sprite('ca402_11', 4)
    sprite('ca402_12', 4)


@State
def SpecialPosingCrouchAttack():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        CrouchState(1)
        WhiffStandCancel(1)
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
    sprite('ca234_00', 4)
    sprite('ca234_01', 4)
    sprite('ca234_02', 4)
    sprite('ca234_03', 4)
    sprite('ca234_04', 4)
    sprite('ca234_05', 4)
    sprite('ca234_06', 4)
    sprite('ca234_07', 4)


@State
def SpecialPosingAirAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AirNoAttack()
        SLOT_4 = 0
        SLOT_5 = 0
        SLOT_6 = 0
        AirDashMomentum(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffOverdriveCancel(1)
        WhiffAirJumpCancel(1)
        WhiffFAirDashCancel(1)
        WhiffBAirDashCancel(1)
        WhiffBlockCancel(1)
        WhiffBarrierCancel2(1)
        EnablePreGuard(1)
    sprite('ca402_00', 4)
    sprite('ca402_01', 4)
    sprite('ca402_02', 4)
    sprite('ca402_03', 4)
    sprite('ca402_04', 4)
    sprite('ca402_05', 4)
    sprite('ca402_06', 4)
    sprite('ca402_07', 4)
    sprite('ca402_08', 4)
    sprite('ca402_09', 4)
    sprite('ca402_10', 4)
    sprite('ca402_11', 4)
    sprite('ca402_12', 4)
    sprite('ca402_13', 4)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('ca054')
    sprite('ca910_00', 32767)
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
    CreateObject('RLAstString', 0)
    CreateObject('RLAstString_nl', 1)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(240000)
    sprite('ca911_00', 50)
    physicsYImpulse(-150)
    sprite('ca911_00', 50)
    physicsYImpulse(150)
    Voiceline('ca055')
    label(0)
    sprite('ca911_00', 50)
    physicsYImpulse(-150)
    sprite('ca911_00', 50)
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
        Blockstun(26)
        Hitstop(20)
        PushbackX(12000)
        OppPositionOnHit(1, 200000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAtkBishop')
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
    sprite('ca440_00', 5)
    sprite('ca440_01', 5)
    sprite('ca440_02', 5)
    sprite('ca440_03', 4)
    physicsXImpulse(5000)
    CommonSE('006_swing_blade_1')
    Voiceline('ca280')
    sprite('ca440_04', 3)
    E0EAEffect('BurstDDeff', 103)
    XImpulseAcceleration(800)
    sprite('ca440_04', 4)
    setInvincible(0)
    StartMultihit()
    XImpulseAcceleration(25)
    sprite('ca440_05', 4)
    XImpulseAcceleration(25)
    sprite('ca440_05', 4)
    XImpulseAcceleration(0)
    sprite('ca440_06', 8)
    sprite('ca440_07', 8)
    sprite('ca440_08', 3)
    sprite('ca440_09', 3)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        Blockstun(26)
        Hitstop(20)
        PushbackX(12000)
        OppPositionOnHit(1, 200000, 0)
        UseSlashHitspark(1)
        DamageFromStateOnly('BurstDDAtkBishop')
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
    sprite('ca440_00', 3)
    sprite('ca440_01', 2)
    sprite('ca440_02', 2)
    sprite('ca440_03', 2)
    physicsXImpulse(5000)
    CommonSE('006_swing_blade_1')
    Voiceline('ca280')
    sprite('ca440_04', 3)
    E0EAEffect('BurstDDeff', 103)
    XImpulseAcceleration(800)
    sprite('ca440_04', 4)
    setInvincible(0)
    StartMultihit()
    XImpulseAcceleration(25)
    sprite('ca440_05', 4)
    XImpulseAcceleration(25)
    sprite('ca440_05', 4)
    XImpulseAcceleration(0)
    sprite('ca440_06', 8)
    sprite('ca440_07', 8)
    sprite('ca440_08', 3)
    sprite('ca440_09', 3)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(3)
        Damage(600)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(50000)
        AirUntechableTime(60)
        Wallbounce(1)
        WallbounceReboundTime(5)
        HardKnockdown(10)
        MinimumDamage(10)
        AttackOff()
        SetBackground(1)
    sprite('ca440_04', 1)
    StartMultihit()
    sprite('ca440_05', 3)
    sprite('ca440_10', 3)
    CreateObject('BurstDDAtkBishop', -1)
    sprite('ca440_11', 3)
    sprite('ca440_12', 4)
    sprite('ca440_13', 6)
    sprite('ca440_14', 6)
    sprite('ca440_15', 2)
    sprite('keep', 1)
    Voiceline('ca281')
    if SLOT_51:
        sendToLabel(100)
    sprite('ca440_16', 2)
    RunLoopUpon(17, 95)

    def upon_17():
        sendToLabel(50)
    sprite('ca440_16', 1)
    CreateObject('BurstDDAtkPawn', -1)
    label(10)
    sprite('ca440_17', 4)
    sprite('ca440_18', 4)
    sprite('ca440_19', 4)
    sprite('ca440_18', 4)
    gotoLabel(10)
    label(50)
    sprite('ca440_17', 4)
    TriggerUponForState('BurstDDAtkPawn', 33)
    sprite('ca440_18', 4)
    sprite('ca440_19', 4)
    sprite('ca440_18', 4)
    sprite('ca440_20', 4)
    TriggerUponForState('BurstDDAtkBishop', 32)
    TriggerUponForState('BurstDDAtkPawn', 32)
    sprite('ca440_21', 4)
    sprite('ca440_22', 4)
    gotoLabel(200)
    label(100)
    sprite('ca440_16', 2)
    RunLoopUpon(17, 245)

    def upon_17():
        sendToLabel(150)
    sprite('ca440_16', 1)
    CreateObject('BurstDDAtkPawnPowerUp', -1)
    label(110)
    sprite('ca440_17', 4)
    sprite('ca440_18', 4)
    sprite('ca440_19', 4)
    sprite('ca440_18', 4)
    gotoLabel(110)
    label(150)
    sprite('ca440_17', 4)
    TriggerUponForState('BurstDDAtkPawnPowerUp', 33)
    sprite('ca440_18', 4)
    sprite('ca440_19', 4)
    sprite('ca440_18', 4)
    sprite('ca440_20', 4)
    TriggerUponForState('BurstDDAtkBishop', 32)
    TriggerUponForState('BurstDDAtkPawnPowerUp', 32)
    sprite('ca440_21', 4)
    sprite('ca440_22', 4)
    gotoLabel(200)
    label(200)
    sprite('ca000_00', 4)
    CreateObject('BurstDDAtkRook', -1)
    sprite('ca300_00ex01', 7)
    sprite('ca300_01ex01', 7)
    sprite('ca300_02ex01', 7)
    sprite('ca300_03ex01', 7)
    sprite('ca300_04ex01', 7)
    sprite('ca300_01ex01', 7)
    sprite('ca300_02ex01', 7)
    sprite('ca300_03ex01', 7)
    TriggerUponForState('BurstDDAtkRook', 32)
    sprite('ca300_04ex01', 7)
    sprite('ca440_23', 4)
    sprite('ca440_24', 4)
    sprite('ca440_25', 4)
    sprite('ca440_26', 4)
    sprite('ca440_27', 4)
    sprite('ca440_28', 4)
    sprite('ca300_11ex01', 4)


@Subroutine
def MouthTableInit():
    Unknown18011('ca000', 14433, 14435, 13921, 13923, 14433, 14435, 14433, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca055', 12641, 25392, 12341, 12641, 25397, 12849, 13153, 
        25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca400', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca401', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca404', 14177, 14179, 14177, 14179, 14177, 12899, 24885, 
        25399, 24887, 25399, 24887, 25401, 24889, 25400, 24888, 25398, 54, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca405', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca406', 14433, 14691, 14433, 14691, 14433, 13155, 24880, 
        25398, 24887, 25398, 24887, 25398, 24887, 25398, 24887, 25398, 
        24887, 25398, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('ca407', 14433, 14435, 14433, 12899, 24886, 25399, 24887, 
        25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca408', 14433, 14435, 12641, 25394, 24888, 25400, 24888, 
        25400, 24888, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca412', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca413', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
        14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca415', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ca417', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('ca000', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('ca400', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca401', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca404', 14433, 14435, 14433, 14435, 13921, 12643, 
            24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ca405', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca406', 12641, 25392, 24886, 25399, 24887, 25399, 
            24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ca407', 14433, 14435, 14433, 12899, 24884, 25398, 
            24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ca408', 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca412', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca413', 14689, 14691, 14689, 14691, 14689, 14691, 
            14689, 14691, 14689, 14691, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ca415', 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ca417', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('rl'):
            Unknown18011('ca000', 14433, 14435, 14433, 14435, 14177, 14179,
                14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca400', 14433, 14435, 14433, 14435, 14433, 12899,
                24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('ca401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('am'):
            Unknown18011('ca000', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('ca400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 12641, 25397, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if not SLOT_140:
            Unknown18011('ca404', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca407', 14433, 13155, 24880, 25400, 24888, 25400,
                24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('ca414', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca415', 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            if SLOT_140:
                Unknown18011('ca504', 13411, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ca505', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14435, 24880, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('ca536', 12641, 25392, 24888, 12337, 14179, 24880,
                25400, 24888, 25400, 24888, 25400, 24888, 25400, 12341, 
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('ca531', 14177, 14179, 14177, 13923, 24880, 25399,
                24887, 25399, 13620, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ca536', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 13667, 24885, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ca537', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('am'):
            Unknown18011('ca540', 12641, 25392, 24888, 12337, 12643, 12336,
                12641, 25392, 24888, 12337, 14435, 12641, 25392, 24888, 
                12337, 14435, 12641, 25392, 24888, 12337, 14435, 12641, 
                25392, 24888, 12337, 14435, 24880, 12337, 13923, 24880, 
                12337, 14435, 12641, 25392, 12338, 12641, 25392, 24888, 
                12337, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca541', 14177, 14179, 14177, 13155, 24880, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 12343, 14177, 14179, 14177, 
                13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ca540', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ca541', 13921, 13923, 13921, 12643, 24888, 
                    25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('ca552', 12641, 25392, 24888, 12337, 14435, 12641,
                25392, 12342, 12641, 25392, 24888, 12337, 14435, 12641, 
                25392, 24888, 12337, 14435, 12641, 48, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ca553', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ca552', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ca553', 14177, 14179, 14177, 13923, 24885, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('no'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2120)
    if CharacterIDCheck('rl'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2280)
        else:
            gotoLabel(280)
    if CharacterIDCheck('am'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2300)
        else:
            gotoLabel(300)
    if CharacterIDCheck('ce'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    label(482)
    if random_(2, 0, 33):
        gotoLabel(10)
    if random_(2, 0, 50):
        gotoLabel(20)
    label(0)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 256, 0)
    loopRest()
    if SLOT_17:
        gotoLabel(0)
    if SLOT_43:
        gotoLabel(1)
    else:
        gotoLabel(2)
    label(1)
    sprite('ca600_00', 90)
    Voiceline('ca414')
    sprite('ca600_01', 8)
    Voiceline('ca415')
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(2)
    sprite('ca600_00', 75)
    Voiceline('ca414')
    sprite('ca600_01', 5)
    Voiceline('ca415')
    sprite('ca600_02', 5)
    sprite('ca600_03', 5)
    sprite('ca600_04', 5)
    sprite('ca600_05', 5)
    sprite('ca600_06', 5)
    sprite('ca600_07', 5)
    sprite('ca600_08', 5)
    sprite('ca600_09', 5)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(10)
    sprite('ca601_00', 6)
    ObjectUpon2(11, 257, 0)
    loopRest()
    if SLOT_17:
        gotoLabel(10)
    if SLOT_43:
        gotoLabel(11)
    else:
        gotoLabel(12)
    label(11)
    sprite('ca601_00', 16)
    Voiceline('ca412')
    sprite('ca601_01', 8)
    sprite('ca601_02', 8)
    sprite('ca601_03', 8)
    sprite('ca601_04', 60)
    sprite('ca601_05', 8)
    Voiceline('ca413')
    DemoEndOnVoiceEnd(1)
    sprite('ca601_06', 8)
    sprite('ca601_07', 8)
    sprite('ca601_08', 8)
    sprite('ca601_09', 8)
    sprite('ca601_10', 8)
    sprite('ca601_11', 8)
    sprite('ca001_08', 8)
    sprite('ca001_09', 8)
    sprite('ca001_10', 8)
    sprite('ca001_11', 8)
    sprite('ca001_12', 8)
    sprite('ca001_13', 8)
    sprite('ca001_14', 8)
    sprite('ca001_15', 8)
    sprite('ca001_16', 8)
    sprite('ca001_17', 8)
    loopRest()
    ExitState()
    label(12)
    sprite('ca601_00', 16)
    Voiceline('ca412')
    sprite('ca601_01', 8)
    sprite('ca601_02', 8)
    sprite('ca601_03', 8)
    sprite('ca601_04', 40)
    sprite('ca601_05', 8)
    Voiceline('ca413')
    sprite('ca601_06', 8)
    sprite('ca601_07', 8)
    sprite('ca601_08', 8)
    sprite('ca601_09', 8)
    sprite('ca601_10', 8)
    sprite('ca601_11', 8)
    sprite('ca001_08', 8)
    sprite('ca001_09', 8)
    sprite('ca001_10', 8)
    sprite('ca001_11', 8)
    sprite('ca001_12', 8)
    sprite('ca001_13', 8)
    sprite('ca001_14', 8)
    sprite('ca001_15', 8)
    sprite('ca001_16', 8)
    sprite('ca001_17', 8)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(20)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 256, 0)
    loopRest()
    if SLOT_17:
        gotoLabel(20)
    if SLOT_43:
        gotoLabel(21)
    else:
        gotoLabel(22)
    label(21)
    sprite('ca600_00', 90)
    Voiceline('ca416')
    sprite('ca600_01', 8)
    Voiceline('ca417')
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(22)
    sprite('ca600_00', 75)
    Voiceline('ca416')
    sprite('ca600_01', 8)
    Voiceline('ca417')
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    DemoTimer(80)
    loopRest()
    ExitState()
    label(2120)
    sprite('ca001_03', 2)

    def upon_EVERY_FRAME():
        if not SLOT_17:
            AddActionMark(1)
        if SLOT_2 >= 20:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2121)
    sprite('ca001_03', 32767)
    label(2121)
    sprite('ca001_03', 260)
    Voiceline('ca504')
    sprite('ca001_04', 7)
    sprite('ca001_05', 7)
    sprite('ca001_06', 7)
    sprite('ca001_07', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 256, 0)
    uponSendToLabel(32, 282)
    loopRest()
    label(281)
    sprite('ca600_00', 6)
    gotoLabel(281)
    label(282)
    sprite('ca600_00', 6)
    sprite('ca600_01', 5)
    Voiceline('ca536')
    sprite('ca600_02', 5)
    sprite('ca600_03', 5)
    sprite('ca600_04', 5)
    sprite('ca600_05', 5)
    sprite('ca600_06', 5)
    sprite('ca600_07', 5)
    sprite('ca600_08', 5)
    sprite('ca600_09', 5)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2280)
    sprite('null', 1)
    ObjectUpon2(11, 1792, 0)
    ScreenCollision(0)
    EnableCollision(0)
    XPositionRelativeFacing(-960000)

    def upon_EVERY_FRAME():
        if SLOT_29 <= 560000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            XPositionRelativeFacing(-260000)
            sendToLabel(2284)
    loopRest()
    label(2281)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2281)
    label(2282)
    sprite('null', 30)
    CreateObject('Act3Event_Fuoco', -1)
    RegisterObject(4, 1)
    sprite('ca030_00', 5)
    physicsXImpulse(4000)
    label(2283)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(2283)
    label(2284)
    sprite('ca000_00', 6)
    uponSendToLabel(32, 2285)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca612_00', 6)
    Voiceline('ca536')
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 240)
    sprite('ca612_03', 32767)
    ObjectUpon(22, 32)
    label(2285)
    sprite('ca612_02', 6)
    sprite('ca612_01', 3)
    sprite('ca612_01', 3)
    ObjectUpon2(11, 273, 0)
    ObjectUpon(FALLING, 32)
    sprite('ca612_00', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    ExitState()
    label(300)
    uponSendToLabel(32, 302)
    label(301)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 256, 0)
    loopRest()
    gotoLabel(301)
    label(302)
    sprite('ca600_00', 8)
    clearUponHandler(32)
    Voiceline('ca540')
    DemoTimer(560)
    sprite('ca600_01', 8)
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    loopRest()
    ExitState()
    label(2300)
    sprite('ca601_00', 6)
    uponSendToLabel(32, 2301)
    ObjectUpon2(11, 257, 0)
    loopRest()
    gotoLabel(2300)
    label(2301)
    sprite('ca601_00', 16)
    clearUponHandler(32)
    Voiceline('ca540')
    sprite('ca601_06', 8)
    sprite('ca601_07', 8)
    sprite('ca601_08', 8)
    sprite('ca601_09', 8)
    sprite('ca601_10', 8)
    sprite('ca601_11', 8)
    sprite('ca001_08', 8)
    sprite('ca001_09', 8)
    sprite('ca001_10', 8)
    sprite('ca001_11', 8)
    sprite('ca001_12', 8)
    sprite('ca001_13', 8)
    sprite('ca001_14', 8)
    sprite('ca001_15', 8)
    sprite('ca001_16', 8)
    sprite('ca001_17', 8)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(360)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 256, 0)
    if SLOT_17:
        conditionalSendToLabel(360)
    sprite('ca600_00', 8)
    Voiceline('ca552')
    sprite('ca600_01', 8)
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    loopRest()
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    ObjectUpon(22, 32)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    ExitState()
    label(2360)
    sprite('ca600_00', 6)
    uponSendToLabel(32, 2361)
    ObjectUpon2(11, 256, 0)
    gotoLabel(2360)
    label(2361)
    sprite('ca600_00', 8)
    Voiceline('ca552')
    sprite('ca600_01', 8)
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    DemoTimer(120)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    label(99)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    CallPrivateFunction('CheckNirvanaAttackableSub', 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_47:
        notConditionalSendToLabel(99)
    CallPrivateFunction('ForceNirvanaRest', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ca615_00', 12)
    if random_(2, 0, 50):
        Voiceline('ca400')
    else:
        Voiceline('ca401')
    DemoEndOnVoiceEnd(1)
    sprite('ca615_01', 7)
    sprite('ca615_02', 7)
    sprite('ca615_03', 7)
    sprite('ca615_04', 7)
    sprite('ca615_05', 7)
    sprite('ca615_06', 7)
    PrivateSE('case_25')
    CreateParticle('rcef_pachinB', 0)
    sprite('ca615_07', 32767)
    loopRest()


@State
def CmnActMatchWin():
    label(99)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    CallPrivateFunction('CheckNirvanaAttackableSub', 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_47:
        notConditionalSendToLabel(99)
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('no'):
        if SLOT_0:
            if SLOT_140:
                conditionalSendToLabel(2120)
    if CharacterIDCheck('rl'):
        if SLOT_140:
            gotoLabel(2280)
        else:
            gotoLabel(280)
    if CharacterIDCheck('am'):
        if SLOT_140:
            gotoLabel(2300)
        else:
            gotoLabel(300)
    if CharacterIDCheck('ce'):
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if SLOT_109:
        conditionalSendToLabel(20)
    if SLOT_123:
        conditionalSendToLabel(20)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    if SLOT_43:
        conditionalSendToLabel(5)
    uponSendToLabel(32, 1)
    uponSendToLabel(LANDING, 3)
    ObjectUpon2(11, 512, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 4)
    Voiceline('ca406')
    ForceFaceSprite()
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(2)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 90)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    sprite('ca610_05', 6)
    ObjectUpon2(11, 512, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    DemoTimer(60)
    label(4)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ca612_00', 6)
    ObjectUpon2(11, 513, 0)
    Voiceline('ca406')
    DemoEndOnVoiceEnd(1)
    loopRest()
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()
    ExitState()
    label(10)
    sprite('ca611_00', 7)
    ObjectUpon2(11, 513, 0)
    Voiceline('ca408')
    sprite('ca611_01', 7)
    sprite('ca611_02', 7)
    sprite('ca611_03', 7)
    CreateObject('Wave_Pawn_Hands', 0)
    sprite('ca611_04', 7)
    sprite('ca611_05', 7)
    sprite('ca611_06', 7)
    sprite('ca611_07', 7)
    sprite('ca611_08', 7)
    sprite('ca611_09', 7)
    DemoTimer(80)
    label(11)
    sprite('ca611_10', 6)
    sprite('ca611_11', 6)
    sprite('ca611_12', 6)
    loopRest()
    gotoLabel(11)
    label(20)
    CallPrivateFunction('ForceNirvanaRest', 0, 0, 0, 0, 0, 0, 0, 0)
    CopyFromRightToLeft(23, 2, 51, 11, 2, 22)
    if SLOT_XDistanceFromCenterOfStage > SLOT_51:
        if SLOT_IsFacingRight:
            gotoLabel(22)
    elif not SLOT_IsFacingRight:
        gotoLabel(22)
    sprite('ca003_00', 6)
    Flip()
    sprite('ca003_01', 6)
    sprite('ca003_02', 6)
    loopRest()
    label(22)
    sprite('ca612_00', 6)
    Voiceline('ca407')
    DemoEndOnVoiceEnd(1)
    loopRest()
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()
    ExitState()
    label(2120)
    if SLOT_109:
        conditionalSendToLabel(482)
    CallPrivateFunction('ForceNirvanaRest', 0, 0, 0, 0, 0, 0, 0, 0)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2122)
    sprite('ca030_00', 5)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    label(2121)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(2121)
    label(2122)
    sprite('keep', 1)
    sprite('ca612_00', 6)
    Voiceline('ca505')
    DemoEndOnVoiceEnd(1)
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()
    label(280)
    sprite('ca001_00', 6)
    Voiceline('ca537')
    DemoEndOnVoiceEnd(1)
    sprite('ca001_01', 6)
    sprite('ca001_02', 6)
    sprite('ca001_03', 6)
    sprite('ca001_04', 32767)
    loopRest()
    ExitState()
    label(2280)
    sprite('ca001_00', 6)
    CallPrivateFunction('ForceNirvanaRest', 0, 0, 0, 0, 0, 0, 0, 0)
    Voiceline('ca537')
    DemoEndOnVoiceEnd(1)
    sprite('ca001_01', 6)
    sprite('ca001_02', 6)
    sprite('ca001_03', 6)
    sprite('ca001_04', 32767)
    loopRest()
    label(300)
    if SLOT_109:
        conditionalSendToLabel(482)
    sprite('ca300_00', 7)
    Voiceline('ca541')
    DemoEndOnVoiceEnd(1)
    sprite('ca300_01', 7)
    sprite('ca300_02', 7)
    sprite('ca300_03', 7)
    sprite('ca300_04', 7)
    sprite('ca300_05', 7)
    sprite('ca300_06', 7)
    sprite('ca300_07', 7)
    sprite('ca300_08', 7)
    sprite('ca300_09', 7)
    sprite('ca300_10', 7)
    sprite('ca300_11', 7)
    uponSendToLabel(32, 302)
    uponSendToLabel(LANDING, 304)
    ObjectUpon2(11, 512, 0)
    loopRest()
    label(301)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(301)
    label(302)
    sprite('ca610_00', 4)
    ForceFaceSprite()
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(303)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(303)
    label(304)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 30)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    sprite('ca610_05', 6)
    ObjectUpon2(11, 512, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    label(305)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(305)
    label(2300)
    if SLOT_109:
        conditionalSendToLabel(482)
    sprite('ca300_00', 7)
    Voiceline('ca541')
    DemoEndOnVoiceEnd(1)
    ObjectUpon2(11, 512, 0)
    sprite('ca300_01', 7)
    sprite('ca300_02', 7)
    sprite('ca300_03', 7)
    sprite('ca300_04', 7)
    sprite('ca300_05', 7)
    sprite('ca300_06', 7)
    sprite('ca300_07', 7)
    sprite('ca300_08', 7)
    sprite('ca300_09', 7)
    sprite('ca300_10', 7)
    sprite('ca300_11', 7)
    uponSendToLabel(32, 2302)
    uponSendToLabel(LANDING, 2304)
    loopRest()
    label(2301)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(2301)
    label(2302)
    sprite('ca610_00', 4)
    ForceFaceSprite()
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(2303)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(2303)
    label(2304)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 30)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    sprite('ca610_05', 6)
    ObjectUpon2(11, 512, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    label(2305)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(2305)
    label(360)
    sprite('ca612_00', 6)
    ObjectUpon2(11, 513, 0)
    Voiceline('ca553')
    DemoEndOnVoiceEnd(1)
    loopRest()
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()
    ExitState()
    label(2360)
    sprite('keep', 1)
    CopyFromRightToLeft(23, 2, 51, 11, 2, 22)
    if SLOT_XDistanceFromCenterOfStage > SLOT_51:
        if SLOT_IsFacingRight:
            gotoLabel(2361)
    elif not SLOT_IsFacingRight:
        gotoLabel(2361)
    sprite('ca003_00', 6)
    Flip()
    sprite('ca003_01', 6)
    sprite('ca003_02', 6)
    loopRest()
    label(2361)
    sprite('ca612_00', 6)
    Voiceline('ca553')
    DemoEndOnVoiceEnd(1)
    ObjectUpon2(11, 513, 0)
    loopRest()
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()
    label(666)
    sprite('ca611_00', 7)
    ObjectUpon2(11, 513, 0)
    if random_(2, 0, 50):
        Voiceline('ca407')
    else:
        Voiceline('ca408')
    DemoEndOnVoiceEnd(1)
    sprite('ca611_01', 7)
    sprite('ca611_02', 7)
    sprite('ca611_03', 7)
    CreateObject('Wave_Pawn_Hands', 0)
    sprite('ca611_04', 7)
    sprite('ca611_05', 7)
    sprite('ca611_06', 7)
    sprite('ca611_07', 7)
    sprite('ca611_08', 7)
    sprite('ca611_09', 7)
    label(667)
    sprite('ca611_10', 6)
    sprite('ca611_11', 6)
    sprite('ca611_12', 6)
    loopRest()
    gotoLabel(667)


@State
def CmnActLose():
    label(99)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    CallPrivateFunction('CheckNirvanaAttackableSub', 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_47:
        notConditionalSendToLabel(99)
    label(11)
    sprite('ca620_00', 6)
    ObjectUpon2(11, 769, 0)
    sprite('ca620_01', 6)
    loopRest()
    uponSendToLabel(32, 1)
    label(0)
    sprite('ca620_02', 2)
    sprite('ca620_03', 2)
    sprite('ca620_04', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca620_05', 6)
    sprite('ca620_06', 6)
    sprite('ca620_07', 6)
    sprite('ca620_08', 6)
    sprite('ca620_09', 8)
    sprite('ca620_10', 8)
    sprite('ca620_11', 8)
    sprite('ca620_12', 8)
    Voiceline('ca411')
    sprite('ca620_13', 8)
    sprite('ca620_14', 8)
    sprite('ca620_15', 8)
    sprite('ca620_16', 32767)
    DemoTimer(90)


@State
def EventDefEntryWait():
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryStand():
    enterState('CmnActStand')


@State
def EventArmorWait():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1280, 0)
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventArmorOpenStand():
    sprite('keep', 2)
    ObjectUpon2(11, 1281, 0)
    loopRest()
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventMegane():
    sprite('ca001_00', 8)
    sprite('ca001_01', 8)
    sprite('ca001_02', 8)
    sprite('ca001_03', 8)
    sprite('ca001_04', 8)
    sprite('ca001_05', 8)
    sprite('ca001_06', 8)
    sprite('ca001_07', 8)
    enterState('CmnActStand')


@State
def EventBoushi():
    sprite('ca001_08', 8)
    sprite('ca001_09', 8)
    sprite('ca001_10', 8)
    sprite('ca001_11', 8)
    sprite('ca001_12', 8)
    sprite('ca001_13', 8)
    sprite('ca001_14', 8)
    sprite('ca001_15', 8)
    sprite('ca001_16', 8)
    sprite('ca001_17', 8)
    enterState('CmnActStand')


@State
def EventLose():
    sprite('ca070_03', 32767)
    ObjectUpon2(11, 1536, 0)


@State
def EventLose2():
    sprite('ca063_11', 32767)
    ObjectUpon2(11, 1536, 0)


@State
def EventVSAM1():
    sprite('ca031_00', 6)
    physicsXImpulse(-2000)
    sprite('ca031_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_02', 6)
    sprite('ca031_03', 6)
    sprite('ca031_04', 6)
    sprite('ca031_05', 6)
    sprite('ca031_06', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_07', 6)
    EndMomentum(1)
    sprite('ca000_00', 6)
    ObjectUpon2(11, 1282, 0)
    sprite('ca600_12', 6)
    sprite('ca600_11', 6)
    sprite('ca600_10', 6)
    sprite('ca600_09', 6)
    sprite('ca600_08', 6)
    sprite('ca600_07', 6)
    sprite('ca600_06', 6)
    sprite('ca600_05', 6)
    sprite('ca600_04', 6)
    sprite('ca600_03', 6)
    sprite('ca600_02', 6)
    sprite('ca600_01', 6)
    sprite('ca600_00', 32767)


@State
def EventVSAM2():
    sprite('ca600_00', 6)
    sprite('ca600_01', 6)
    sprite('ca600_02', 6)
    sprite('ca600_03', 6)
    sprite('ca600_04', 6)
    sprite('ca600_05', 6)
    sprite('ca600_06', 6)
    sprite('ca600_07', 6)
    sprite('ca600_08', 6)
    sprite('ca600_09', 6)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    sprite('ca030_00', 6)
    physicsXImpulse(2000)
    sprite('ca030_01', 6)
    sprite('ca030_02', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 6)
    sprite('ca030_04', 6)
    sprite('ca030_05', 6)
    sprite('ca030_06', 6)
    sprite('ca030_07', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    ObjectUpon2(11, 1281, 0)
    enterState('CmnActStand')


@State
def EventVSAM3():
    sprite('ca001_00', 7)
    sprite('ca001_01', 7)
    sprite('ca001_02', 7)
    sprite('ca001_03', 32767)


@State
def EventVSAM4():
    sprite('ca001_04', 7)
    sprite('ca001_05', 7)
    sprite('ca001_06', 7)
    sprite('ca001_07', 7)
    enterState('CmnActStand')


@State
def EventVSAM5():
    sprite('ca033_00', 2)
    ScreenCollision(0)
    uponSendToLabel(LANDING, 1)
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    setGravity(1000)
    JumpSoundEffects()
    sprite('ca033_01', 2)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    ObjectUpon2(11, 512, 0)
    loopRest()
    label(0)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca033_04', 3)
    physicsXImpulse(-800000)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(LANDING)
    sprite('ca033_05', 3)


@State
def EventCAVsTK_Tobitsukare():
    XPositionRelativeFacing(-50000)
    uponSendToLabel(32, 1)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('ca050_00', 2)
    SetInertia(-30000)
    sprite('ca050_01', 1)
    sprite('ca050_02', 1)
    sprite('ca050_03', 1)
    sprite('ca050_04', 1)
    sprite('ca071_12', 1)
    sprite('ca060_14', 32767)
    EndMomentum(1)
    loopRest()


@State
def EventCAVsTK_Okiagaru():
    sprite('ca061_00', 4)
    sprite('ca061_01', 4)
    sprite('ca061_02', 3)
    sprite('ca061_03', 3)
    sprite('ca061_04', 3)
    sprite('ca061_05', 4)
    sprite('ca061_06', 4)
    sprite('ca061_07', 4)
    sprite('ca061_08', 5)
    sprite('ca061_09', 5)
    sprite('ca061_10', 5)
    loopRest()
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    if SLOT_IsFacingRight:
        if SLOT_XDistanceFromCenterOfStage < 260000:
            gotoLabel(1)
    elif SLOT_XDistanceFromCenterOfStage > -260000:
        gotoLabel(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 265000:
                sendToLabel(3)
        elif SLOT_XDistanceFromCenterOfStage > -265000:
            sendToLabel(3)
    sprite('ca030_00', 5)
    sprite('ca030_01', 1)
    physicsXImpulse(5000)
    loopRest()
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)
    label(1)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage > 255000:
                sendToLabel(3)
        elif SLOT_XDistanceFromCenterOfStage < -255000:
            sendToLabel(3)
    sprite('ca031_00', 6)
    sprite('ca031_01', 1)
    physicsXImpulse(-5000)
    loopRest()
    label(2)
    sprite('ca031_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_02', 6)
    sprite('ca031_03', 6)
    sprite('ca031_04', 6)
    sprite('ca031_05', 6)
    sprite('ca031_06', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_07', 6)
    sprite('ca031_08', 6)
    sprite('ca031_09', 6)
    sprite('ca031_10', 6)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(EVERY_FRAME)
    sprite('ca001_08', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('ca001_09', 6)
    sprite('ca001_10', 6)
    sprite('ca001_11', 6)
    sprite('ca001_12', 6)
    sprite('ca001_13', 6)
    sprite('ca001_14', 6)
    sprite('ca001_15', 6)
    sprite('ca001_16', 6)
    sprite('ca001_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSRL1():
    sprite('ca001_00', 7)
    ObjectUpon2(11, 273, 0)
    sprite('ca001_01', 7)
    sprite('ca001_02', 7)
    sprite('ca001_03', 32767)


@State
def EventNoDisp():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Visibility(1)
    sprite('null', 32767)
    ObjectUpon2(11, 2048, 0)


@State
def EventVSCEWarpIn():

    def upon_IMMEDIATE():
        SetZVal(-500)
        BlendMode_Normal()
    sprite('ca000_00', 6)
    ObjectUpon2(11, 2049, 0)
    AlphaValue(0)
    sprite('ca000_01', 6)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(10)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    loopRest()
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsTbWinner():
    sprite('ca000_00', 5)
    ObjectUpon2(11, 1282, 0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventCAVsLC_Entry():
    sprite('ca612_02', 32767)
    loopRest()


@State
def EventCAVsLC_Prepare():
    sprite('ca612_01', 6)
    sprite('ca612_00', 6)
    loopRest()
    sprite('ca001_00', 7)
    sprite('ca001_01', 7)
    sprite('ca001_02', 7)
    sprite('ca001_03', 7)
    sprite('ca001_04', 7)
    sprite('ca001_05', 7)
    sprite('ca001_06', 7)
    sprite('ca001_07', 7)
    enterState('CmnActStand')


@State
def EventCAVsLCWin():
    sprite('ca601_00', 32767)
    loopRest()


@State
def EventVsRCEntryWait0():
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1290, 0)
    sprite('ca600_00', 32767)
    loopRest()


@State
def EventVsRCEntryWait1():
    sprite('ca600_00', 240)
    sprite('ca600_00', 60)
    ObjectUpon2(11, 1291, 0)
    sprite('ca600_01', 32767)
    loopRest()


@State
def EventVsRCEntry():
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    loopRest()
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsHZEntryWait0():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1540, 0)
    loopRest()
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsHZEntryWait1():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1541, 0)
    loopRest()
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventARVsCA_TurnToNirvana():
    sprite('ca003_00', 4)
    ForceFaceSprite()
    Flip()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    sprite('ca030_00', 5)
    physicsXImpulse(2000)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_05', 5)
    sprite('ca612_00', 5)
    EndMomentum(1)
    sprite('ca612_01', 32767)
    loopRest()


@State
def EventARVsCA_Doubt():
    sprite('ca612_02', 5)
    sprite('ca612_03', 32767)
    loopRest()


@State
def EventARVsCA_ReturnToEnemy():
    sprite('ca003_00', 4)
    ForceFaceSprite()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 265000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -265000:
            sendToLabel(1)
    sprite('ca030_00', 5)
    sprite('ca030_01', 1)
    physicsXImpulse(2000)
    loopRest()
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    sprite('ca001_08', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('ca001_09', 6)
    sprite('ca001_10', 6)
    sprite('ca001_11', 6)
    sprite('ca001_12', 6)
    sprite('ca001_13', 6)
    sprite('ca001_14', 6)
    sprite('ca001_15', 6)
    sprite('ca001_16', 6)
    sprite('ca001_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventARVsCA_Loser():
    sprite('ca070_00', 7)
    ObjectUpon2(11, 1536, 0)
    sprite('ca070_01', 7)
    sprite('ca070_02', 7)
    label(0)
    sprite('ca070_03', 1)
    loopRest()
    gotoLabel(0)


@State
def EventTBVsCA_EntryWait():
    sprite('ca601_00', 1)
    ObjectUpon2(11, 1280, 0)
    loopRest()
    label(0)
    sprite('ca601_00', 1)
    loopRest()
    gotoLabel(0)


@State
def EventTBVsCA_Entry():
    sprite('ca601_00', 16)
    sprite('ca601_01', 8)
    sprite('ca601_02', 8)
    sprite('ca601_03', 8)
    sprite('ca601_04', 40)
    sprite('ca601_05', 8)
    sprite('ca601_06', 8)
    sprite('ca601_07', 8)
    sprite('ca601_08', 8)
    sprite('ca601_09', 8)
    sprite('ca601_10', 8)
    sprite('ca601_11', 8)
    ObjectUpon2(11, 1281, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventTBVsCA_Loser():
    uponSendToLabel(32, 1)
    uponSendToLabel(LANDING, 3)
    ObjectUpon2(11, 1538, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 4)
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(2)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 6)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    ObjectUpon2(11, 1539, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    label(4)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(4)


@State
def EventVsTkEntryWait():
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1293, 0)
    label(0)
    sprite('ca600_00', 1)
    loopRest()
    gotoLabel(0)


@State
def EventVsTkEntry():
    sprite('ca600_00', 6)
    ObjectUpon2(11, 1294, 0)
    sprite('ca600_01', 6)
    sprite('ca600_02', 6)
    sprite('ca600_03', 6)
    sprite('ca600_04', 6)
    sprite('ca600_05', 6)
    sprite('ca600_06', 6)
    sprite('ca600_07', 6)
    sprite('ca600_08', 6)
    sprite('ca600_09', 6)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    loopRest()
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventRlVsCaEntry00():
    sprite('null', 1)
    ObjectUpon2(11, 1792, 0)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 1)
    AddX(-770000)
    sprite('null', 32767)
    loopRest()


@State
def EventRlVsCaEntry01():
    sprite('null', 1)
    ObjectUpon2(11, 1793, 0)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 32767)
    loopRest()


@State
def EventRlVsCaEntry02():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('ca030_00', 5)
    physicsXImpulse(4000)
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventRlVsCaEntry03():
    sprite('ca001_00', 8)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    sprite('ca001_01', 8)
    sprite('ca001_02', 8)
    sprite('ca001_03', 8)


@State
def EventRlVsCaEntry04():
    sprite('ca001_04', 8)
    sprite('ca001_05', 8)
    sprite('ca001_06', 8)
    sprite('ca001_07', 8)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventRlVsCaEntry05():
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca203_00', 4)
    ObjectUpon2(11, 1794, 0)
    sprite('ca203_01', 4)
    sprite('ca203_02', 4)
    sprite('ca203_03', 4)
    sprite('ca203_04', 4)
    sprite('ca203_05', 4)
    sprite('ca203_06', 4)
    sprite('ca203_07', 4)
    sprite('ca203_08', 4)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventRlVsCaEntry06():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1795, 0)
    enterState('CmnActStand')


@State
def EventRlVsCaEntry07():
    sprite('ca033_06', 5)
    sprite('ca033_05', 5)


@State
def EventRlVsCaEntry08():
    sprite('ca033_05', 6)
    sprite('ca033_06', 6)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventRlVsCaLoser01():
    sprite('ca110_06', 15)


@State
def EventRlVsCaLoser02():
    sprite('ca110_06', 30)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ca110_06', 30)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ca110_06', 30)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ca110_06', 30)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('ca110_06', 4)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-20)
    ObjectUpon2(11, 1796, 0)
    sprite('ca110_06', 120)
    sprite('ca110_06', 6)
    XPositionRelativeFacing(-900000)


@State
def EventVsHaEntryWait():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1284, 0)
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsHaEntryStand():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1285, 0)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsHaWinner():
    sprite('ca000_00', 1)
    ObjectUpon2(11, 1283, 0)
    label(0)
    sprite('ca000_00', 5)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsNyEntryWait():
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1293, 0)
    label(0)
    sprite('ca600_00', 1)
    loopRest()
    gotoLabel(0)


@State
def EventVsNyEntryStand():
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1294, 0)
    sprite('ca600_01', 8)
    sprite('ca600_02', 8)
    sprite('ca600_03', 8)
    sprite('ca600_04', 8)
    sprite('ca600_05', 8)
    sprite('ca600_06', 8)
    sprite('ca600_07', 8)
    sprite('ca600_08', 8)
    sprite('ca600_09', 8)
    sprite('ca600_10', 8)
    sprite('ca600_11', 7)
    sprite('ca600_12', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsNyWinner():
    sprite('ca620_16', 1)
    ObjectUpon2(11, 1286, 0)


@State
def EventVsNoLose00():
    ObjectUpon2(11, 1283, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsNoLose01():
    uponSendToLabel(32, 1)
    uponSendToLabel(LANDING, 3)
    ObjectUpon2(11, 1287, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 4)
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(2)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 6)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    ObjectUpon2(11, 1288, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    label(4)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(4)


@State
def EventVsRcLose00():
    ObjectUpon2(11, 1283, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsRcLose01():
    uponSendToLabel(32, 1)
    uponSendToLabel(LANDING, 3)
    ObjectUpon2(11, 1287, 0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 4)
    sprite('ca610_00', 4)
    sprite('ca610_01', 4)
    sprite('ca610_02', 4)
    physicsXImpulse(-12000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(2)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)

    def upon_EVERY_FRAME():
        MoveToCollision(11, 2, 0)
    sprite('ca610_05', 6)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CameraControlEnable(0)
    ObjectUpon2(11, 1288, 1)
    sprite('ca610_06', 6)
    sprite('ca610_07', 6)
    label(4)
    sprite('ca610_08', 2)
    sprite('ca610_09', 2)
    loopRest()
    gotoLabel(4)


@State
def EventPause1():
    sprite('ca450_00', 6)
    sprite('ca450_01', 6)
    sprite('ca450_02', 6)
    label(0)
    sprite('ca450_03', 6)
    sprite('ca450_04', 6)
    sprite('ca450_05', 6)
    gotoLabel(0)


@State
def EventPause1End():
    sprite('ca450_16', 6)
    sprite('ca450_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventNOVSCA():
    sprite('ca000_00', 6)
    ObjectUpon2(11, 1284, 0)
    XPositionRelativeFacing(-100000)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    gotoLabel(0)


@State
def EventPause1NoLoop():
    sprite('ca450_00', 6)
    sprite('ca450_01', 6)
    sprite('ca450_02', 6)
    sprite('ca450_03', 6)
    CommonSE('019_cloth_a')
    sprite('ca450_04', 6)
    sprite('ca450_05', 6)
    sprite('ca450_03', 6)
    CommonSE('019_cloth_a')
    sprite('ca450_04', 6)
    sprite('ca450_05', 6)
    sprite('ca450_06', 6)
    sprite('ca450_07', 6)
    Flip()
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca030_00', 6)
    physicsXImpulse(1500)
    sprite('ca030_01', 6)
    sprite('ca030_02', 6)
    sprite('ca030_03', 6)
    sprite('ca030_04', 6)
    sprite('ca030_05', 6)
    sprite('ca030_06', 6)
    sprite('ca030_07', 6)
    RunLoopUpon(17, 375)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('ca000_00', 6)
    physicsXImpulse(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    gotoLabel(0)
    label(1)
    sprite('ca003_00', 3)
    Flip()
    sprite('ca003_01', 3)
    sprite('ca003_02', 3)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca064_10', 8)
    sprite('ca064_09', 8)
    sprite('ca064_08', 32767)


@State
def EventPause2():
    sprite('ca203_00', 8)
    sprite('ca203_01', 8)
    sprite('ca203_02', 8)
    sprite('ca203_03', 8)
    label(0)
    sprite('ca203_04', 8)
    sprite('ca203_05', 8)
    sprite('ca203_06', 8)
    gotoLabel(0)


@State
def EventPause2End():
    sprite('ca203_07', 8)
    sprite('ca203_08', 8)
    enterState('CmnActStand')


@State
def EventPause2_Re():
    sprite('ca203_00', 7)
    sprite('ca203_01', 7)
    sprite('ca203_02', 7)
    sprite('ca203_03', 7)
    sprite('ca203_04', 7)
    sprite('ca203_05', 7)
    sprite('ca203_06', 7)
    sprite('ca203_07', 7)
    sprite('ca203_08', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventPause3Wait():
    sprite('ca000_00', 6)
    Flip()
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventPause3():
    sprite('ca003_00', 4)
    ForceFaceSprite()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventPause4Wait():
    sprite('ca003_00', 4)
    ForceFaceSprite()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventYoroke2():
    sprite('ca070_03', 32767)
    loopRest()


@State
def EventYorokeToStand():
    sprite('ca070_02', 6)
    sprite('ca070_01', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventBDashOut():
    sprite('ca033_00', 2)
    ScreenCollision(0)
    WallCollisionDetection(0)
    EnableCollision(0)
    sprite('ca033_01', 2)
    AddX(-20000)
    physicsXImpulse(-61000)
    physicsYImpulse(32000)
    setGravity(1550)
    JumpSoundEffects()
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)


@State
def EventVsCEStandWait():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
    sprite('rg460_00', 6)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageMask_1(0, 255, 0, 127)
    AfterimageMask_2(0, 127, 0, 255)
    AfterimageSize_1(1010)
    AfterimageSize_2(1100)
    StayAfterMovement(1, 1)
    label(0)
    sprite('rg460_01', 6)
    sprite('rg460_02', 6)
    sprite('rg460_03', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsRMBDash():
    label(10)
    sprite('ca033_00', 2)
    sprite('ca033_01', 2)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('ca033_02', 2)
    uponSendToLabel(LANDING, 1)
    sprite('ca033_02', 1)
    sprite('ca033_03', 3)
    loopRest()
    label(0)
    sprite('ca033_02', 3)
    sprite('ca033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca033_04', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('ca033_05', 2)
    XPositionRelativeFacing(-260000)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsRMWalk():
    RunLoopUpon(17, 70)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('ca030_00', 5)
    physicsXImpulse(4000)
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    EndMomentum(1)
    loopRest()
    enterState('EventKubikashige')


@State
def EventKubikashige():
    sprite('ca612_00', 5)
    sprite('ca612_01', 5)
    sprite('ca612_02', 5)
    sprite('ca612_03', 32767)
    loopRest()


@State
def EventVsRMEntryWait():
    sprite('keep', 2)
    XPositionRelativeFacing(10000)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsRMGuardBreakAir():
    sprite('ca092_00', 2)
    E0EAEffect('GuardCrushWind', 65535)
    CreateParticle('caef_guardcrash', 0)
    uponSendToLabel(LANDING, 1)
    physicsXImpulse(-8000)
    physicsYImpulse(15000)
    setGravity(1200)
    sprite('ca092_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('ca092_02', 20)
    sprite('ca092_03', 6)
    sprite('ca092_04', 32767)
    loopRest()
    label(1)
    sprite('ca024_00', 6)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('ca024_01', 6)
    sprite('ca010_02', 6)
    sprite('ca010_03', 6)
    sprite('ca010_04', 6)
    sprite('ca010_05', 6)
    sprite('ca010_06', 6)
    sprite('ca010_07', 6)
    sprite('ca010_08', 6)
    sprite('ca010_09', 6)
    sprite('ca010_01', 6)
    sprite('ca010_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_yorokeStart():
    sprite('ca070_00', 7)
    sprite('ca070_01', 7)
    sprite('ca070_02', 7)
    label(0)
    sprite('ca070_03', 1)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_yorokeEnd():
    sprite('ca070_02', 7)
    sprite('ca070_01', 7)
    sprite('ca070_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Kashige():
    sprite('ca612_00', 6)
    sprite('ca612_01', 6)
    sprite('ca612_02', 6)
    sprite('ca612_03', 32767)
    loopRest()


@State
def Act2Event_KashigeEnd():
    sprite('ca612_03', 6)
    sprite('ca612_02', 6)
    sprite('ca612_01', 6)
    sprite('ca612_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Megane():
    sprite('ca001_00', 8)
    sprite('ca001_01', 8)
    sprite('ca001_02', 8)
    sprite('ca001_03', 8)
    sprite('ca001_02', 32767)
    loopRest()


@State
def Act2Event_MeganeEnd():
    sprite('ca001_04', 8)
    sprite('ca001_05', 8)
    sprite('ca001_06', 8)
    sprite('ca001_07', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cavsmi_00():
    sprite('keep', 32767)
    CreateObject('Act2Event_Fade', -1)
    CommonSE('022_magiccircle_c')
    ConstantAlphaModifier(-4)

    def RunOnObject_11():
        ConstantAlphaModifier(-4)

    def RunOnObject_22():
        ConstantAlphaModifier(-4)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    loopRest()


@State
def Act2Event_Reverse():
    sprite('ca003_00', 4)
    Flip()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2EventARvsCA01():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1536, 0)
        RunLoopUpon(17, 40)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        XPositionRelativeFacing(100000)
        uponSendToLabel(32, 2)
    sprite('ca070_00', 7)
    AddInertia(-50000)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    sprite('ca070_01', 7)
    KnockdownEffects(100, 1, 1)
    CommonSE('208_brake_normal')
    sprite('ca070_02', 7)
    label(0)
    sprite('ca070_03', 7)
    CommonSE('208_brake_normal')
    sprite('ca070_02', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca070_04', 6)
    EndMomentum(1)
    sprite('ca070_05', 6)
    sprite('ca070_06', 4)
    sprite('ca070_07', 4)
    sprite('ca070_08', 4)
    sprite('ca070_09', 4)
    sprite('ca063_11', 32767)
    LandingEffects(100, 1, 0)
    CommonSE('209_down_normal_0')
    label(2)
    sprite('ca063_11', 32767)
    ObjectUpon2(11, 1792, 0)
    loopRest()


@State
def Act2EventARvsCA02():
    sprite('ca064_00', 32767)


@State
def Act2EventARvsCA03():
    sprite('ca064_00', 5)
    sprite('ca063_11', 32767)
    LandingEffects(100, 1, 0)
    CommonSE('209_down_normal_0')


@State
def Act2EventNYvsCA00():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 3)
        uponSendToLabel(34, 5)
        uponSendToLabel(35, 7)
        TriggerUponForState('Act2EventNirvanaAtk6D', 32)
    sprite('ca000_00', 2)
    CreateObject('Act2EventNirvanaAtk6D', 0)
    label(0)
    sprite('ca000_00', 4)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 2)
    loopRest()
    gotoLabel(0)
    label(5)
    sprite('ca003_00', 4)
    ForceFaceSprite()
    Flip()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    sprite('ca030_00', 5)
    physicsXImpulse(2000)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_05', 5)
    sprite('ca612_00', 5)
    EndMomentum(1)
    sprite('ca612_01', 5)
    sprite('ca612_02', 5)
    sprite('ca612_03', 32767)
    loopRest()
    label(6)
    sprite('ca000_00', 4)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 2)
    loopRest()
    gotoLabel(6)
    label(7)
    sprite('ca003_00', 4)
    EndMomentum(1)
    ForceFaceSprite()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 265000:
                sendToLabel(8)
        elif SLOT_XDistanceFromCenterOfStage > -265000:
            sendToLabel(8)
    sprite('ca030_00', 5)
    sprite('ca030_01', 1)
    physicsXImpulse(2000)
    loopRest()
    label(9)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(9)
    label(8)
    clearUponHandler(EVERY_FRAME)
    sprite('ca001_08', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('ca001_09', 6)
    sprite('ca001_10', 6)
    sprite('ca001_11', 6)
    sprite('ca001_12', 6)
    sprite('ca001_13', 6)
    sprite('ca001_14', 6)
    sprite('ca001_15', 6)
    sprite('ca001_16', 6)
    sprite('ca001_17', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca450_00', 6)
    TriggerUponForState('Act2EventNirvanaAtk6D', 33)
    sprite('ca450_01', 6)
    sprite('ca450_02', 6)
    label(2)
    sprite('ca450_03', 6)
    sprite('ca450_04', 6)
    sprite('ca450_05', 6)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ca450_16', 6)
    ObjectUpon2(11, 273, 0)
    sprite('ca450_17', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_CrouchToStand():
    sprite('ca010_01', 6)
    sprite('ca010_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_CrouchLoop():
    label(0)
    sprite('ca010_02', 6)
    sprite('ca010_03', 6)
    sprite('ca010_04', 6)
    sprite('ca010_05', 6)
    sprite('ca010_06', 6)
    sprite('ca010_07', 6)
    sprite('ca010_08', 6)
    sprite('ca010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_tgvsca_00():
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1293, 0)
    sprite('ca600_00', 32767)


@State
def Act3Event_tgvsca_01():
    sprite('ca600_00', 6)
    ObjectUpon2(11, 1294, 0)
    sprite('ca600_01', 6)
    sprite('ca600_02', 6)
    sprite('ca600_03', 6)
    sprite('ca600_04', 6)
    sprite('ca600_05', 6)
    sprite('ca600_06', 6)
    sprite('ca600_07', 6)
    sprite('ca600_08', 6)
    sprite('ca600_09', 6)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tgvsca_02():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        CreateObject('Act3Event_tgvsca_00', 0)
        RegisterObject(4, 1)
        XPositionRelativeFacing(-160000)
    sprite('ca000_00', 6)
    sprite('ca070_00', 17)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('ca070_00', 4)
    AddInertia(-11000)
    sprite('ca070_01', 4)
    sprite('ca070_02', 4)
    sprite('ca070_03', 32767)
    loopRest()


@State
def Act3Event_tgvsca_03():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
    sprite('ca070_10', 4)
    sprite('ca070_11', 4)
    sprite('ca070_12', 4)
    sprite('ca070_13', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tgvsca_04():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        ObjectUpon(FALLING, 32)
        uponSendToLabel(32, 1)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(2)

            def upon_EVERY_FRAME():
                MoveToCollision(4, 2, 0)
        CameraControlEnable(0)
    sprite('ca204_00', 4)
    sprite('ca204_01', 4)
    sprite('ca204_02', 4)
    sprite('ca204_03', 4)
    sprite('ca204_04', 4)
    sprite('ca204_05', 4)
    sprite('ca204_06', 4)
    sprite('ca204_07', 4)
    sprite('ca204_08', 4)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 3)
    sprite('ca610_01', 3)
    sprite('ca610_02', 3)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(9)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('ca610_05', 3)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    ObjectUpon(FALLING, 33)
    sprite('ca610_06', 3)
    sprite('ca610_07', 3)
    label(3)
    sprite('ca610_08', 3)
    sprite('ca610_09', 3)
    loopRest()
    gotoLabel(3)


@State
def Act3Event_BNvsCA00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-260000)
    sprite('ca000_00', 6)
    XPositionRelativeFacing(-300000)
    Flip()
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_BNvsCA01():
    RunLoopUpon(17, 10)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('ca030_00', 5)
    physicsXImpulse(4000)
    label(0)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_bnvsca_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(100000)
    sprite('ca010_06', 8)
    CommonSE('104_guard_grap_1')
    ScreenShake(3000, 18000)
    AddInertia(-40000)
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_1')
    CommonSE('006_swing_blade_2')
    CommonSE('006_swing_blade_1')
    sprite('ca010_07', 8)
    sprite('ca010_08', 8)
    sprite('ca010_09', 8)
    EndMomentum(1)
    label(0)
    sprite('ca010_02', 8)
    sprite('ca010_03', 8)
    sprite('ca010_04', 8)
    sprite('ca010_05', 8)
    sprite('ca010_06', 8)
    sprite('ca010_07', 8)
    sprite('ca010_08', 8)
    sprite('ca010_09', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CAvsRL00():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
        ObjectUpon2(11, 1792, 0)
        SLOT_51 = 0
        uponSendToLabel(32, 5)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 4)
    sprite('ca001_02', 32767)
    CreateObject('Act3Event_Nirvana22D', 0)
    label(5)
    sprite('ca001_04', 6)
    sprite('ca001_05', 6)
    sprite('ca001_06', 6)
    sprite('ca001_07', 6)
    label(0)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    sprite('ca000_00', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca031_00', 6)
    physicsXImpulse(-2000)
    sprite('ca031_01', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_02', 6)
    sprite('ca031_03', 6)
    sprite('ca031_04', 6)
    sprite('ca031_05', 6)
    sprite('ca031_06', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca031_07', 6)
    EndMomentum(1)
    sprite('ca003_00', 4)
    Flip()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('ca030_00', 7)
    physicsXImpulse(4200)
    TriggerUponForState('Act3Event_Nirvana22D', 32)
    label(3)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    if SLOT_51 <= 4:
        DashEffects(100, 0, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    if SLOT_51 <= 4:
        DashEffects(100, 0, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    SLOT_51 = SLOT_51 + 1
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ca003_00', 3)
    Flip()
    sprite('ca003_01', 3)
    sprite('ca003_02', 3)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CAvsLC00Loop():
    sprite('ca620_00', 6)
    sprite('ca620_01', 6)
    loopRest()
    label(0)
    sprite('ca620_02', 7)
    sprite('ca620_03', 7)
    sprite('ca620_04', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CAvsLC00LoopEnd():
    sprite('ca620_01', 6)
    sprite('ca620_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_CAvsLC01():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
        ObjectUpon2(11, 1792, 0)

        def upon_32():
            ObjectUpon(22, 32)
        uponSendToLabel(33, 1)
    sprite('ca001_00', 8)
    CreateObject('Act3Event_CAvsLC01', 0)
    sprite('ca001_01', 8)
    sprite('ca001_02', 8)
    sprite('ca001_03', 8)
    sprite('ca001_02', 32767)
    loopRest()
    label(1)
    sprite('ca001_04', 8)
    sprite('ca001_05', 8)
    sprite('ca001_06', 8)
    sprite('ca001_07', 8)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca003_00', 4)
    Flip()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    loopRest()
    sprite('ca030_00', 7)
    physicsXImpulse(4200)
    TriggerUponForState('Act3Event_CAvsLC01', 32)
    label(2)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    if SLOT_51 <= 4:
        DashEffects(100, 0, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    if SLOT_51 <= 4:
        DashEffects(100, 0, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    SLOT_51 = SLOT_51 + 1
    loopRest()
    gotoLabel(2)


@State
def Act3Event_CAvsNO00():
    sprite('ca003_00', 4)
    ForceFaceSprite()
    sprite('ca003_01', 4)
    sprite('ca003_02', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_tbvsca_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-220000)
    sprite('ca111_00', 3)
    SetInertia(-20000)
    XPositionRelativeFacing(0)
    ScreenShake(3000, 18000)
    sprite('ca111_01', 6)
    LandingEffects(100, 1, 1)
    CommonSE('208_brake_normal')
    sprite('ca111_02', 6)
    CommonSE('208_brake_normal')
    sprite('ca111_03', 6)
    CommonSE('208_brake_normal')
    sprite('ca111_04', 6)
    CommonSE('208_brake_normal')
    sprite('ca111_06', 5)
    sprite('ca111_07', 20)
    sprite('ca111_09', 5)
    sprite('ca111_10', 5)
    loopRest()
    enterState('Act2Event_CrouchLoop')


@State
def Act3Event_tbvsca_01():
    sprite('ca402_00', 4)
    sprite('ca402_01', 4)
    sprite('ca402_02', 4)
    sprite('ca402_03', 4)
    sprite('ca402_04', 4)
    sprite('ca402_05', 4)
    sprite('ca402_06', 4)
    sprite('ca402_07', 4)
    sprite('ca402_08', 4)
    sprite('ca402_09', 4)
    sprite('ca402_10', 4)
    sprite('ca402_11', 4)
    sprite('ca402_12', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsca_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        AddX(-1200000)

        def RunOnObject_11():
            AddX(-1200000)
    sprite('ca600_00', 1)
    ObjectUpon2(11, 1293, 0)
    sprite('ca600_00', 32767)


@State
def Act3Event_phvsca_01():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('ca600_00', 30)
    sprite('ca600_00', 6)
    ObjectUpon2(11, 1294, 0)
    sprite('ca600_01', 6)
    sprite('ca600_02', 6)
    sprite('ca600_03', 6)
    sprite('ca600_04', 6)
    sprite('ca600_05', 6)
    sprite('ca600_06', 6)
    sprite('ca600_07', 6)
    sprite('ca600_08', 6)
    sprite('ca600_09', 6)
    sprite('ca600_10', 6)
    sprite('ca600_11', 6)
    sprite('ca600_12', 6)
    loopRest()
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsca_02():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('ca001_00', 8)
    sprite('ca001_01', 8)
    sprite('ca001_02', 8)
    sprite('ca001_03', 8)
    sprite('ca001_02', 30)
    sprite('ca001_02', 32767)
    CameraControlEnable(0)
    loopRest()


@State
def Act3Event_phvsca_03():
    sprite('ca064_10', 7)
    sprite('ca064_09', 7)
    sprite('ca064_08', 7)
    sprite('ca064_07', 32767)
    loopRest()


@State
def Act3Event_phvsca_04():
    sprite('ca064_07', 7)
    sprite('ca064_08', 7)
    sprite('ca064_09', 7)
    sprite('ca064_10', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsca_05():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        CreateObject('Act3Event_phvsca_00', 0)
        RegisterObject(4, 1)
        ScreenCollision(0)
        CameraControlEnable(1)
    sprite('ca001_02', 60)
    loopRest()
    sprite('ca001_02', 160)
    ObjectUpon(FALLING, 33)
    sprite('ca001_02', 32767)
    CameraControlEnable(0)
    loopRest()


@State
def Act3Event_phvsca_06():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        CreateObject('Act3Event_phvsca_01', 0)
        RegisterObject(4, 1)
        XPositionRelativeFacing(-160000)
    sprite('ca064_00', 32767)
    loopRest()


@State
def Act3Event_phvsca_07():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)

        def upon_STATE_END():
            clearUponHandler(EVERY_FRAME)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 3:
            if SLOT_52 % 2:
                AddX(1000)
            else:
                AddX(-1000)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1
    sprite('ca064_00', 4)
    sprite('ca064_01', 10)
    sprite('ca064_02', 10)
    sprite('ca064_03', 9)
    sprite('ca064_04', 8)
    sprite('ca064_05', 8)
    sprite('ca064_06', 8)
    clearUponHandler(EVERY_FRAME)
    sprite('ca064_07', 6)
    sprite('ca064_08', 6)
    sprite('ca064_09', 6)
    sprite('ca064_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsca_08():

    def upon_IMMEDIATE():
        ObjectUpon2(11, 1792, 0)
        ObjectUpon(FALLING, 32)
        uponSendToLabel(32, 1)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(2)

            def upon_EVERY_FRAME():
                MoveToCollision(4, 2, 0)
        CameraControlEnable(0)
    label(0)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ca610_00', 3)
    sprite('ca610_01', 3)
    sprite('ca610_02', 3)
    physicsXImpulse(-4000)
    physicsYImpulse(6000)
    setGravity(1000)
    label(9)
    sprite('ca610_03', 2)
    sprite('ca610_04', 2)
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('ca610_05', 3)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    ObjectUpon(FALLING, 33)
    sprite('ca610_06', 3)
    sprite('ca610_07', 3)
    label(3)
    sprite('ca610_08', 3)
    sprite('ca610_09', 3)
    loopRest()
    gotoLabel(3)


@State
def Act3Event_phvsca_09():

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
    sprite('ca030_00', 5)
    physicsXImpulse(4000)
    label(9)
    sprite('ca030_01', 5)
    sprite('ca030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_03', 5)
    sprite('ca030_04', 5)
    sprite('ca030_05', 5)
    sprite('ca030_06', 5)
    sprite('ca030_07', 5)
    sprite('ca030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ca030_09', 5)
    sprite('ca030_10', 5)
    sprite('ca030_11', 5)
    sprite('ca030_12', 5)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ca000_00', 4)
    ObjectUpon2(11, 273, 0)
    loopRest()
    enterState('Act2Event_Megane')
