@Subroutine
def PreInit():
    CharacterID('bl')
    EnableDashBuffer(1)


@Subroutine
def AdditionalThrowInit():
    SLOT_64 = 0
    SLOT_65 = 0
    SLOT_52 = 1


@Subroutine
def DriveThrowInit():
    AttackDefaults_StandingNormal()
    AttackLevel_(3)
    Damage(450)
    AttackP1(90)
    AttackP2(69)
    Blockstun(20)
    Hitstop(9)
    OppPositionOnHit(1, 150000, 25000)
    PushbackX(30400)
    EnemyHitstopAddition(3, 3, 11)
    AttackOff()
    RunLoopUpon(17, 3)

    def upon_17():
        clearUponHandler(17)
        RefreshMultihit()
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            AttackLevel_(5)
        else:
            AttackLevel_(4)
            if SLOT_IsGrounded:
                pass
    DefeatOpponentBehavior(1)
    MoveAttributes(1, 0, 0, 0, 0)
    HitAirUnblockable(0)
    IgnoreBurst(1)
    SpecialCancel(0)
    IgnoreComboTime(1)

    def upon_OPPONENT_HIT():
        SetActionMark(1)
        SLOT_64 = 0
        EnableRapidCancel(0)
        SpecificInvincibility(1, 1, 1, 1, 1)
        DollInvincibility(1)
        BurstInvincibility(1)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SLOT_54 = 1
        XImpulseAcceleration(25)
        YAccel(25)
        sendToLabel(0)

    def upon_STATE_END():
        EndYPhysicsImpulse()
    setInvincible(1)
    GuardPoint_(0)
    SpecificInvincibility(0, 0, 0, 1, 1)
    StrikeProjectilesBypass(0)
    DollInvincibility(0)
    BurstInvincibility(0)
    callSubroutine('DriveLockOnTimeCheck')
    if SLOT_53:
        SpecificInvincibility(1, 1, 1, 1, 1)
        StrikeProjectilesBypass(1)
        DollInvincibility(1)
    callSubroutine('DriveThrowPowerUpCheck')


@Subroutine
def DriveThrowHitCheck():
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    clearUponHandler(OPPONENT_HIT)
    if SLOT_2 == 1:
        XImpulseAcceleration(25)
        YAccel(25)
        setGravity(3600)
        sendToLabel(1)
    else:
        if SLOT_54:
            if SLOT_6 == 2:
                enterState('DriveAttackMiss')
            else:
                enterState('DriveAttackMiss')
        else:
            XImpulseAcceleration(50)
            setGravity(3000)
        setInvincible(0)


@Subroutine
def DriveLockOnTimeCheck():
    if SLOT_60 > 0:
        SLOT_6 = 1
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            PrivateFunction(12, 2, 60, 0, 1, 2, 53)
            if SLOT_53:
                SLOT_6 = 2
        else:
            PrivateFunction(12, 2, 60, 0, 1, 2, 53)
            if SLOT_53:
                SLOT_6 = 2
    else:
        PrivateFunction(12, 2, 60, 0, 9999, 2, 53)
        if SLOT_53:
            SLOT_6 = 2


@Subroutine
def DriveThrowPowerUpCheck():
    callSubroutine('DriveLockOnTimeCheck')
    if SLOT_53:
        Damage(600)


@Subroutine
def DriveMidLowPowerUpCheck():
    AddActionMark(0)
    Damage(800)
    AttackLevel_(3)
    Blockstun(20)
    PushbackX(19800)
    SpecialCancel(0)
    SpecialCancelOnHit(1)
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            AttackLevel_(5)
        else:
            AttackLevel_(4)
    callSubroutine('DriveLockOnTimeCheck')
    if SLOT_53:
        Damage(1000)
        Blockstun(24)


@Subroutine
def DriveThrowLockOnZoneCtrl():
    SetActionMark(0)
    SLOT_60 = 0
    SLOT_51 = 0
    SLOT_6 = 0

    def upon_EVERY_FRAME():
        if CheckInput(0x5f):
            SLOT_55 = 1
            SLOT_60 = 0
        if SLOT_2:
            if SLOT_55:
                if SLOT_StateDuration >= 24:
                    ObjectUpon(5, 32)
                    if SLOT_IsAirborne:
                        enterState('DriveAttackCancelAir')
                    else:
                        enterState('DriveAttackCancelLand')
            elif SLOT_60:
                sendToLabel(1)
            CallPrivateFunction('BlDriveRangeCheck', 2, 4, 0, 0, 0, 0, 0, 0)
    uponSendToLabel(17, 1)


@Subroutine
def HeatUpStart():
    SLOT_64 = 0
    SLOT_5 = SLOT_5 + 1
    if SLOT_5 >= 2:
        SLOT_5 = 2
    SLOT_31 = 900
    CreateObject('HeatUpEff', 103)


@Subroutine
def HeatDownStart():
    SLOT_64 = 0
    if not SLOT_OverdriveTimer:
        SLOT_5 = SLOT_5 + -1
        if SLOT_5 <= 0:
            SLOT_5 = 0
            SLOT_31 = 0


@Subroutine
def HeatUpActionInit():
    SLOT_52 = 1
    IgnoreComboTime(0)
    PassByArmor(1)
    setInvincible(1)
    BurstInvincibility(0)

    def upon_STATE_END():
        SLOT_52 = 0
        if not SLOT_OverdriveTimer:
            SLOT_5 = 0
            SLOT_31 = 0


@Subroutine
def MatchInit():
    Health(11500)
    WalkFSpeed(5500)
    WalkBSpeed(4500)
    AirDashFSpeed(27500)
    AirFDashDuration(15)
    AirDashBSpeed(22000)
    AirBDashDuration(12)
    JumpYVelocity(31000)
    SuperJumpYVelocity(42000)
    Gravity(1800)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(5)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(1)
    CreateDecalOn(1)
    ResourceGauge(0, 0, 0, 1, 900, 0, -65536, -65536)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    AirborneOpponentPriority(2000)
    DamageStunPriority(1500)
    SkillEstimateRange(0, 350000, 0, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    DamageStunPriority(0)
    OpponentAttackPriority(250)
    SkillEstimateRange(0, 300000, -200000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 350000, -100000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(-10000, 400000, 0, 350000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    AirborneOpponentPriority(1500)
    SkillEstimateRange(-10000, 450000, 50000, 450000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    AirborneOpponentPriority(0)
    DamageStunPriority(2500)
    SkillEstimateRange(-25000, 400000, -150000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    MoveMaxChainRepeat(2)
    AirborneOpponentPriority(0)
    SkillEstimateRange(100000, 450000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    SkillEstimateRange(150000, 450000, -100000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk5C')
    MoveLow()
    AirborneOpponentPriority(0)
    MoveCancellableFrames(43, 45)
    GuardStunPriority(0)
    SkillEstimateRange(50000, 450000, -100000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(500)
    OpponentAttackPriority(1500)
    SkillEstimateRange(50000, 400000, -150000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    OpponentAttackPriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1)
    MoveButtonHoldTime(3, 2, 15)
    SkillEstimateRange(500000, 750000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    MoveMid()
    OpponentAttackPriority(1)
    AirborneOpponentPriority(500)
    DamageStunPriority(500)
    GuardStunPriority(1500)
    MoveButtonHoldTime(3, 2, 8)
    SkillEstimateRange(100000, 350000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    MoveLow()
    OpponentAttackPriority(1)
    AirborneOpponentPriority(500)
    DamageStunPriority(500)
    GuardStunPriority(1500)
    MoveButtonHoldTime(3, 2, 8)
    SkillEstimateRange(100000, 350000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    DamageStunPriority(500)
    SkillEstimateRange(50000, 350000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    DamageStunPriority(2000)
    SkillEstimateRange(-100000, 350000, -50000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SkillEstimateRange(-50000, 400000, -250000, 300000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    PlayerUsable(0)
    CPUUsable(0)
    SkillEstimateRange(-50000, 300000, -300000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x3037)
    CallSkillConditions('CheckJumpDActive')
    OpponentAttackPriority(1050)
    GuardStunPriority(0)
    SkillEstimateRange(-250000, 250000, -250000, 250000, 750, 0)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_Input_(INPUT_66)
    FollowupOnly(1)
    CallSkillConditions('CheckHeatUp')
    AddChain(1)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)
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
    SkillEstimateRange(100000, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('DriveAddAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    MovePriority(800)
    Unknown15027(2500)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    CallSkillConditions('CheckShotAvailable')
    MoveButtonHoldTime(0, 2, 20)
    JumpAvoidPriority(5000)
    AirborneOpponentPriority(0)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(300000, 700000, -200000, 600000, 0, 400)
    Move_EndRegister()
    Move_Register('InterrUpThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(4000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(-50000, 350000, -200000, 200000, 400, 0)
    Move_EndRegister()
    Move_Register('InterrUpAddAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    MovePriority(2000)
    DamageStunPriority(2000)
    Unknown15027(50)
    Move_EndRegister()
    Move_Register('AntiAirThrowLand', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    AirborneOpponentPriority(2000)
    MoveComboPriority(1)
    SkillEstimateRange(-100000, 450000, 250000, 600000, 200, 0)
    Move_EndRegister()
    Move_Register('AntiAirThrowCancel', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    Unknown15027(0)
    SkillEstimateRange(-50000, 300000, -200000, 250000, 500, 0)
    Move_EndRegister()
    Move_Register('AntiAirThrowAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_C)
    CallSkillConditions('CheckAntiAirThrowActive')
    DamageStunPriority(2000)
    TempPriorityMultiplierInterval(0, 0, 100, 0, 1000)
    SkillEstimateRange(-100000, 350000, 200000, 600000, 200, 0)
    Move_EndRegister()
    Move_Register('AntiAirAddAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_623)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    MovePriority(2000)
    DamageStunPriority(2000)
    Move_EndRegister()
    Move_Register('DashThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_C)
    MoveThrow()
    AirborneOpponentPriority(1)
    OpponentAttackPriority(0)
    GuardStunPriority(500)
    SkillEstimateRange(150000, 350000, -50000, 250000, 750, 0)
    Move_EndRegister()
    Move_Register('DashAddAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    Unknown15027(250)
    SkillEstimateRange(0, 700000, -200000, 800000, 3000, 0)
    Move_EndRegister()
    Move_Register('CommandThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(0xca)
    Move_Input_(INPUT_PRESS_B)
    NeutralOnly(1)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('CommandThrowAddAttack', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(INPUT_63214)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    DamageStunPriority(1)
    SkillEstimateRange(0, 350000, -200000, 200000, 3000, 0)
    Move_EndRegister()
    Move_Register('CompulsionHeatUp', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(0)
    DamageStunPriority(1500)
    GuardStunPriority(1500)
    MoveComboPriority(0)
    TempPriorityMultiplierInterval(0, 0, 250, 1000, 0)
    SkillEstimateRange(900000, 1300000, -200000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('CompulsionHeatUpCancel', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(0)
    DamageStunPriority(1500)
    GuardStunPriority(1500)
    MoveComboPriority(0)
    TempPriorityMultiplierInterval(0, 0, 250, 1000, 0)
    SkillEstimateRange(900000, 1300000, -200000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_2363214)
    Move_Input_(INPUT_PRESS_C)
    GuardStunPriority(0)
    DamageStunPriority(4000)
    SkillEstimateRange(200000, 450000, -200000, 300000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_2363214)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    GuardStunPriority(0)
    DamageStunPriority(4000)
    SkillEstimateRange(200000, 450000, -200000, 300000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_A)
    NeutralOnly(1)
    MoveThrow()
    AirborneOpponentPriority(0)
    DamageStunPriority(0)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 400000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateThrowOD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3081)
    NeutralOnly(1)
    MoveThrow()
    AirborneOpponentPriority(0)
    DamageStunPriority(0)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 400000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAddAttack', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Input_(0xcb)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUp')
    MovePriority(2000)
    DamageStunPriority(2000)
    Move_EndRegister()
    Move_Register('UltimateFinishAttack', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Input_(0xf6)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckHeatUpLv2')
    MovePriority(10000)
    DamageStunPriority(2000)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_D)
    MoveComboPriority(0)
    OpponentAttackPriority(2000)
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
    SkillEstimateRange(0, 400000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 400000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 400000, -200000, 300000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'AntiAirThrowLand', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'AntiAirThrowAir', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'Shot', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'InterrUpThrow', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Shot', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'DashThrow', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AntiAirThrowAir', 10000000)
    StylishModeSpecialButton('InterrUpThrow', 0x4, 0xea)
    StylishModeSpecialButton('Shot', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssaultOD', 0x4, 0x5f)
    StylishModeSpecialButton('CommandThrow', 0x4, 0x45)
    StylishModeSpecialButton('AntiAirThrowAir', 0x4, 0xea)
    StylishModeSpecialButton('DriveAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('InterrUpAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('DashAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('AntiAirAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('CommandThrowAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('UltimateAddAttack', 0x4, 0xea)
    StylishModeSpecialButton('UltimateFinishAttack', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 1, 180000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'DashThrow', 1, 180000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 8, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2C', 13, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk2C', 0, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk3C', 8, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk6C', 12, 0)
    StylishModeCancels('NmlAtk6B', 'FHighJump', 0, 0)
    StylishModeCancels('NmlAtk6B', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk6C', 'AntiAirThrowAir', 0, 0)
    StylishModeCancels('NmlAtk6C', 'BJump', 13, 0)
    StylishModeCancels('NmlAtk3C', 'InterrUpThrow', 0, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'DashThrow', 10, 1000000)
    StylishModeCancels('NmlAtk3C', 'Shot', 13, 0)
    StylishModeCancels('DriveAttackMid', 'AntiAirThrowCancel', 0, 0)
    StylishModeCancels('DriveAttackMid', 'DashThrow', 10, 1000000)
    StylishModeCancels('DriveAttackMid', 'Shot', 13, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk6B', 1, 180000)
    StylishModeCancels('NmlAtk2C', 'CompulsionHeatUp', 0, 0)
    StylishModeCancels('NmlAtk2C', 'UltimateAssault', 6, 0)
    StylishModeCancels('NmlAtk2C', 'UltimateAssaultOD', 6, 0)
    StylishModeCancels('NmlAtk2C', 'Shot', 13, 0)
    StylishModeCancels('DriveAttackLow', 'AntiAirThrowCancel', 0, 0)
    StylishModeCancels('DriveAttackLow', 'DashThrow', 10, 1000000)
    StylishModeCancels('DriveAttackLow', 'Shot', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AntiAirThrowAir', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 2, 200000)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5C', 13, 0)
    StylishModeCancels('DriveThrowExe', 'InterrUpThrow', 0, 0)
    StylishModeCancels('DriveThrowExe', 'DashThrow', 10, 1000000)
    StylishModeCancels('DashThrowExe', 'DashAddAttack', 0, 0)
    StylishModeCancels('InterrUpThrowExe', 'InterrUpAddAttack', 0, 0)
    StylishModeCancels('AntiAirThrowExe', 'AntiAirAddAttack', 0, 0)
    StylishModeCancels('UltimateThrow2ndExe', 'UltimateAddAttack', 0, 0)
    StylishModeCancels('UltimateAddAttackExe', 'UltimateFinishAttack', 0, 0)
    StylishModeCancels('CommandThrowExe', 'CommandThrowAddAttack', 0, 0)
    StylishModeCancels('BackThrowExe', 'Shot', 0, 0)
    StylishModeCancels('BackThrowExe', 'AstralHeat', 6, 0)
    StylishModeCancels('ThrowExe', 'CompulsionHeatUp', 0, 0)
    HitSprites(0, 'bl062_01')
    HitSprites(1, 'bl062_03')
    HitSprites(2, 'bl062_04')
    HitSprites(3, 'bl062_05')
    HitSprites(4, 'bl062_05')
    HitSprites(5, 'bl062_06')
    HitSprites(6, 'bl062_07')
    HitSprites(7, 'bl041_02')
    HitSprites(8, 'bl040_02')
    HitSprites(9, 'bl045_02')
    HitSprites(10, 'bl060_00')
    HitSprites(11, 'bl060_01')
    HitSprites(12, 'bl060_03')
    HitSprites(13, 'bl060_05')
    HitSprites(14, 'bl060_07')
    HitSprites(15, 'bl060_14')
    HitSprites(16, 'bl050_00')
    HitSprites(17, 'bl052_00')
    HitSprites(18, 'bl054_00')
    HitSprites(19, 'bl000_00')
    HitSprites(20, 'bl000_00')
    HitSprites(25, 'bl063_00')
    HitSprites(26, 'bl063_01')
    HitSprites(27, 'bl063_02')
    HitSprites(28, 'bl063_04')
    HitSprites(29, 'bl063_11')
    HitSprites(30, 'bl077_00')
    HitSprites(31, 'bl077_01')
    HitSprites(32, 'bl077_00ex01')
    HitSprites(33, 'bl077_01ex01')
    HitSprites(34, 'bl077_00ex02')
    HitSprites(35, 'bl077_01ex02')
    HitSprites(36, 'bl077_00ex03')
    HitSprites(37, 'bl077_01ex03')
    HitSprites(24, 'bl073_01')
    CommonVoicelines(0, 'bl000')
    CommonVoicelines(1, 'bl001')
    CommonVoicelines(2, 'bl002')
    CommonVoicelines(3, 'bl003')
    CommonVoicelines(4, 'bl004')
    CommonVoicelines(5, 'bl005')
    CommonVoicelines(6, 'bl006')
    CommonVoicelines(7, 'bl007')
    CommonVoicelines(8, 'bl008')
    CommonVoicelines(9, 'bl009')
    CommonVoicelines(10, 'bl010')
    CommonVoicelines(11, 'bl011')
    CommonVoicelines(12, 'bl012')
    CommonVoicelines(13, 'bl013')
    CommonVoicelines(14, 'bl014')
    CommonVoicelines(15, 'bl015')
    CommonVoicelines(16, 'bl016')
    CommonVoicelines(17, 'bl017')
    CommonVoicelines(18, 'bl018')
    CommonVoicelines(19, 'bl019')
    CommonVoicelines(20, 'bl020')
    CommonVoicelines(21, 'bl021')
    CommonVoicelines(22, 'bl022')
    CommonVoicelines(23, 'bl023')
    CommonVoicelines(24, 'bl024')
    CommonVoicelines(25, 'bl025')
    CommonVoicelines(26, 'bl026')
    CommonVoicelines(27, 'bl027')
    CommonVoicelines(28, 'bl028')
    CommonVoicelines(29, 'bl029')
    CommonVoicelines(30, 'bl030')
    CommonVoicelines(31, 'bl031')
    CommonVoicelines(32, 'bl032')
    CommonVoicelines(33, 'bl033')
    CommonVoicelines(34, 'bl034')
    CommonVoicelines(35, 'bl035')
    CommonVoicelines(36, 'bl036')
    CommonVoicelines(37, 'bl037')
    CommonVoicelines(38, 'bl038')
    CommonVoicelines(39, 'bl039')
    CommonVoicelines(40, 'bl040')
    CommonVoicelines(41, 'bl041')
    CommonVoicelines(42, 'bl042')
    CommonVoicelines(43, 'bl043')
    CommonVoicelines(44, 'bl044')
    CommonVoicelines(45, 'bl045')
    CommonVoicelines(46, 'bl046')
    CommonVoicelines(47, 'bl047')
    CommonVoicelines(48, 'bl048')
    CommonVoicelines(49, 'bl049')
    CommonVoicelines(50, 'bl050')
    CommonVoicelines(51, 'bl051')
    CommonVoicelines(52, 'bl052')
    CommonVoicelines(53, 'bl053')
    CommonVoicelines(54, 'bl100')
    CommonVoicelines(55, 'bl101')
    CommonVoicelines(56, 'bl102')
    CommonVoicelines(57, 'bl103')
    CommonVoicelines(58, 'bl104')
    CommonVoicelines(59, 'bl105')
    CommonVoicelines(60, 'bl106')
    CommonVoicelines(61, 'bl107')
    CommonVoicelines(62, 'bl108')
    CommonVoicelines(63, 'bl109')
    CommonVoicelines(64, 'bl150')
    CommonVoicelines(65, 'bl151')
    CommonVoicelines(66, 'bl152')
    CommonVoicelines(67, 'bl153')
    CommonVoicelines(68, 'bl154')
    CommonVoicelines(69, 'bl155')
    CommonVoicelines(70, 'bl156')
    CommonVoicelines(71, 'bl157')
    CommonVoicelines(72, 'bl158')
    CommonVoicelines(75, 'bl160')
    CommonVoicelines(73, 'bl402')
    CommonVoicelines(74, 'bl403')


@Subroutine
def MatchInit2():
    SLOT_59 = 90000
    SLOT_61 = 1
    SLOT_62 = 1


@Subroutine
def CheckHeatUp():
    SLOT_5 >= 1
    SLOT_47 = SLOT_0


@Subroutine
def CheckHeatUpLv2():
    SLOT_5 >= 2
    SLOT_47 = SLOT_0


@Subroutine
def CheckJumpDActive():
    SLOT_61 == 1
    SLOT_47 = SLOT_0


@Subroutine
def CheckAntiAirThrowActive():
    SLOT_62 == 1
    SLOT_47 = SLOT_0


@Subroutine
def CheckShotAvailable():
    if not CheckObjectPresence(7):
        SLOT_47 = 1
    else:
        SLOT_47 = 0


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnActionBegin():
    if not SLOT_65:
        if SLOT_64 == 1:
            callSubroutine('HeatUpStart')


@Subroutine
def OnFinalize():
    if not SLOT_65:
        if SLOT_64 == 2:
            callSubroutine('HeatDownStart')


@Subroutine
def OnFrameStep():
    if CheckObjectPresence(5):
        if SLOT_60:
            if not CheckObjectPresence(6):
                CreateObject('BLEF_LockOnMarker', -1)
                RegisterObject(6, 1)
            else:
                callSubroutine('DriveLockOnTimeCheck')
                if SLOT_53:
                    ObjectUpon(6, 32)
        elif CheckObjectPresence(6):
            ObjectUpon(6, 33)
    elif CheckObjectPresence(6):
        ObjectUpon(6, 33)
    if not SLOT_21:
        SLOT_5 = 0
        SLOT_31 = 0
    if SLOT_31:
        if SLOT_21:
            EnableAfterimage(1)
            AfterimageInterval(1)
            AfterimageCount(4)
            if SLOT_5 == 1:
                AfterimageBlendMode(2)
                AfterimageColor_1(160, 0, 0, 0)
                AfterimageColor_2(96, 0, 0, 0)
                AfterimageMask_1(0, 192, 48, 8)
                AfterimageMask_2(0, 255, 48, 8)
                AfterimageSize_1(1000)
                AfterimageSize_2(850)
            if SLOT_5 == 2:
                AfterimageBlendMode(1)
                AfterimageColor_1(200, 100, 32, 32)
                AfterimageColor_2(50, 200, 32, 32)
                AfterimageSize_1(1000)
                AfterimageSize_2(1050)
            if not SLOT_81:
                if not SLOT_52:
                    SLOT_31 = SLOT_31 + -1
                if SLOT_OverdriveTimer:
                    if not SLOT_31:
                        SLOT_31 = 1
                if not SLOT_31:
                    EnableAfterimage(0)
                    SLOT_5 = 0
    TrainingModeSLOT('TRI_BulletHeatUp', 2, 67)
    if SLOT_67 == 1:
        if SLOT_InNeutral:
            SLOT_5 = 1
            SLOT_31 = 900
    TrainingModeSLOT('TRI_BulletHeatUp', 2, 67)
    if SLOT_67 == 2:
        if SLOT_InNeutral:
            SLOT_5 = 2
            SLOT_31 = 900
    if CurrentStateCheck('RlAstralDamage'):
        EnableAfterimage(0)
        SLOT_5 = 0
        SLOT_31 = 0


@Subroutine
def OnLanding():
    if not SLOT_61:
        SLOT_61 = 1
    if not SLOT_62:
        SLOT_62 = 1


@State
def CmnActStand():
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(0)
    sprite('bl000_00', 6)
    SLOT_88 = 960
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    sprite('bl001_03', 6)
    SmartVoiceline('bl000')
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_11', 6)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('bl003_00', 3)
    SmartVoiceline('bl001')
    sprite('bl003_01', 3)
    sprite('bl003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('bl010_00', 4)
    sprite('bl010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('bl010_02', 6)
    sprite('bl010_03', 6)
    sprite('bl010_04', 6)
    sprite('bl010_05', 6)
    sprite('bl010_06', 6)
    sprite('bl010_07', 6)
    sprite('bl010_08', 6)
    sprite('bl010_09', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('bl013_00', 3)
    sprite('bl013_01', 3)
    sprite('bl013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('bl010_01', 4)
    sprite('bl010_00', 4)


@State
def CmnActJumpPre():
    sprite('bl023_00', 2)
    sprite('bl023_01', 2)


@State
def CmnActJumpUpper():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('bl020_00', 3)
    sprite('bl020_01', 3)
    SmartVoiceline('bl002')
    label(0)
    sprite('bl020_00', 3)
    sprite('bl020_01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl021_00', 3)
    sprite('bl021_01', 3)
    SmartVoiceline('bl002')
    label(10)
    sprite('bl021_00', 3)
    sprite('bl021_01', 3)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('bl022_00', 3)
    sprite('bl022_01', 3)
    SmartVoiceline('bl003')
    label(20)
    sprite('bl022_00', 3)
    sprite('bl022_01', 3)
    loopRest()
    gotoLabel(20)


@State
def CmnActJumpUpperEnd():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('bl020_02', 3)
    sprite('bl020_03', 3)
    sprite('bl020_04', 3)
    loopRest()
    ExitState()
    label(1)
    sprite('bl021_02', 3)
    sprite('bl021_03', 3)
    sprite('bl021_04', 2)
    sprite('bl021_05', 2)
    loopRest()
    ExitState()
    label(2)
    sprite('bl022_02', 3)
    sprite('bl022_03', 3)
    sprite('bl022_04', 2)
    sprite('bl022_05', 2)
    loopRest()
    ExitState()


@State
def CmnActJumpDown():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('bl020_05', 2)
    sprite('bl020_06', 2)
    label(0)
    sprite('bl020_07', 3)
    sprite('bl020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl021_06', 3)
    label(10)
    sprite('bl021_07', 3)
    sprite('bl021_08', 3)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('bl022_06', 3)
    label(20)
    sprite('bl022_07', 3)
    sprite('bl022_08', 3)
    loopRest()
    gotoLabel(20)


@State
def CmnActJumpLanding():
    sprite('bl024_00', 3)
    ObjectUpon(5, 32)
    sprite('bl024_01', 3)
    sprite('bl024_02', 3)
    sprite('bl024_03', 3)
    sprite('bl024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('bl024_00', 2)
    sprite('bl024_01', 2)
    sprite('bl024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('bl024_03', 3)
    sprite('bl024_04', 3)


@State
def CmnActFWalk():
    sprite('bl030_00', 4)
    label(0)
    sprite('bl030_01', 4)
    sprite('bl030_02', 4)
    sprite('bl030_03', 4)
    sprite('bl030_04', 4)
    sprite('bl030_05', 4)
    sprite('bl030_06', 4)
    sprite('bl030_07', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl030_08', 4)
    sprite('bl030_09', 4)
    sprite('bl030_10', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('bl031_00', 5)
    label(0)
    sprite('bl031_01', 5)
    sprite('bl031_02', 5)
    sprite('bl031_03', 5)
    sprite('bl031_04', 5)
    sprite('bl031_05', 5)
    sprite('bl031_06', 5)
    sprite('bl031_07', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl031_08', 5)
    sprite('bl031_09', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl031_10', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        EndMomentum(1)
        WhiffNormalCancel(1)
        WhiffSpecialCancel(1)
        WhiffBarrierCancel2(1)
        WhiffJumpCancel(1)
        WhiffOverdriveCancel(1)
        SetXCollisionFromOrigin(200)
        if SLOT_OverdriveTimer:
            SLOT_52 = 1
        SLOT_51 = 19500
        if SLOT_52:
            SLOT_51 = 27500
    sprite('bl032_00', 3)
    if SLOT_52:
        SetInertia(20000)
    else:
        SetInertia(15000)
    sprite('bl032_01', 3)
    SLOT_XVelocity = SLOT_51
    DashEffects(100, 1, 1)
    sprite('bl032_02', 3)
    WhiffBarrierCancel2(0)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    WhiffJumpCancel(0)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)
    ExitState()


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
    sprite('bl033_00', 1)
    sprite('bl033_00', 2)
    physicsXImpulse(-18000)
    physicsYImpulse(6300)
    setGravity(1550)
    JumpSoundEffects()
    sprite('bl033_01', 2)
    SmartVoiceline('bl005')
    sprite('bl033_02', 2)
    sprite('bl033_01', 2)
    setInvincible(0)
    sprite('bl033_02', 2)
    loopRest()
    label(0)
    sprite('bl033_01', 2)
    sprite('bl033_02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl033_03', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('bl033_04', 2)
    sprite('bl033_05', 2)
    sprite('bl033_06', 2)
    sprite('bl033_07', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('bl035_00', 3)
    sprite('bl035_01', 3)
    SmartVoiceline('bl004')
    sprite('bl035_02', 3)
    label(0)
    sprite('bl035_01', 3)
    sprite('bl035_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('bl036_00', 3)
    sprite('bl036_01', 3)
    SmartVoiceline('bl006')
    sprite('bl036_02', 3)
    label(0)
    sprite('bl036_01', 3)
    sprite('bl036_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('bl050_00', 1)
    sprite('bl050_01', 1)
    sprite('bl050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('bl050_01', 1)
    sprite('bl050_02', 1)
    sprite('bl050_01', 2)
    sprite('bl050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('bl050_02', 1)
    sprite('bl050_03', 1)
    sprite('bl050_02', 2)
    sprite('bl050_01', 2)
    sprite('bl050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('bl050_03', 1)
    sprite('bl050_04', 1)
    sprite('bl050_03', 2)
    sprite('bl050_02', 2)
    sprite('bl050_01', 2)
    sprite('bl050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('bl050_04', 1)
    sprite('bl050_04', 1)
    sprite('bl050_04', 2)
    sprite('bl050_03', 2)
    sprite('bl050_02', 2)
    sprite('bl050_01', 2)
    sprite('bl050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('bl052_00', 1)
    sprite('bl052_01', 1)
    sprite('bl052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('bl052_01', 1)
    sprite('bl052_02', 1)
    sprite('bl052_01', 2)
    sprite('bl052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('bl052_02', 1)
    sprite('bl052_03', 1)
    sprite('bl052_02', 2)
    sprite('bl052_01', 2)
    sprite('bl052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('bl052_03', 1)
    sprite('bl052_04', 1)
    sprite('bl052_03', 2)
    sprite('bl052_02', 2)
    sprite('bl052_01', 2)
    sprite('bl052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('bl052_04', 1)
    sprite('bl052_04', 1)
    sprite('bl052_04', 2)
    sprite('bl052_03', 2)
    sprite('bl052_02', 2)
    sprite('bl052_01', 2)
    sprite('bl052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('bl054_00', 1)
    sprite('bl054_01', 1)
    sprite('bl054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('bl054_01', 1)
    sprite('bl054_02', 1)
    sprite('bl054_01', 2)
    sprite('bl054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('bl054_02', 1)
    sprite('bl054_03', 1)
    sprite('bl054_02', 2)
    sprite('bl054_01', 2)
    sprite('bl054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('bl054_03', 1)
    sprite('bl054_04', 1)
    sprite('bl054_03', 2)
    sprite('bl054_02', 2)
    sprite('bl054_01', 2)
    sprite('bl054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('bl054_04', 1)
    sprite('bl054_04', 1)
    sprite('bl054_04', 2)
    sprite('bl054_03', 2)
    sprite('bl054_02', 2)
    sprite('bl054_01', 2)
    sprite('bl054_00', 2)


@State
def CmnActBDownUpper():
    sprite('bl060_00', 4)
    label(0)
    sprite('bl060_01', 4)
    sprite('bl060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('bl060_03', 4)


@State
def CmnActBDownDown():
    sprite('bl060_04', 4)
    label(0)
    sprite('bl060_05', 4)
    sprite('bl060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('bl060_07', 2)
    sprite('bl060_08', 2)


@State
def CmnActBDownBound():
    sprite('bl060_09', 3)
    sprite('bl060_10', 3)
    sprite('bl060_11', 3)
    sprite('bl060_12', 3)
    sprite('bl060_13', 3)


@State
def CmnActBDownLoop():
    sprite('bl060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('bl061_00', 3)
    sprite('bl061_01', 3)
    sprite('bl061_02', 3)
    sprite('bl061_03', 2)
    sprite('bl061_04', 2)
    sprite('bl061_05', 3)
    sprite('bl061_06', 3)
    sprite('bl061_07', 3)


@State
def CmnActFDownUpper():
    sprite('bl063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('bl063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('bl063_02', 3)
    sprite('bl063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('bl063_04', 3)
    sprite('bl063_05', 3)


@State
def CmnActFDownBound():
    sprite('bl063_06', 2)
    sprite('bl063_07', 2)
    sprite('bl063_08', 3)
    sprite('bl063_09', 3)
    sprite('bl063_10', 3)


@State
def CmnActFDownLoop():
    sprite('bl063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('bl064_00', 3)
    sprite('bl064_01', 3)
    sprite('bl064_02', 3)
    sprite('bl064_03', 2)
    sprite('bl064_04', 2)
    sprite('bl064_05', 3)
    sprite('bl064_06', 3)
    sprite('bl064_07', 3)


@State
def CmnActVDownUpper():
    sprite('bl062_00', 3)
    label(0)
    sprite('bl062_01', 3)
    sprite('bl062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('bl062_03', 3)
    sprite('bl062_04', 3)


@State
def CmnActVDownDown():
    sprite('bl062_05', 3)
    sprite('bl062_06', 3)
    label(0)
    sprite('bl062_07', 3)
    sprite('bl062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('bl062_09', 2)
    sprite('bl062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('bl062_09', 2)
    sprite('bl062_10', 2)


@State
def CmnActBlowoff():
    sprite('bl072_00', 3)
    sprite('bl072_01', 3)
    sprite('bl072_02', 3)
    label(0)
    sprite('bl072_01', 3)
    sprite('bl072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('bl074_00', 3)
    sprite('bl074_01', 3)
    sprite('bl074_02', 3)
    sprite('bl074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('bl082_00', 2)
    sprite('bl082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('bl071_04', 1)


@State
def CmnActWallBound():
    sprite('bl073_00', 3)
    sprite('bl073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('bl073_02', 3)
    label(0)
    sprite('bl073_03', 3)
    sprite('bl073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('bl070_00', 3)
    sprite('bl070_01', 3)
    sprite('bl070_02', 4)
    sprite('bl070_03', 4)


@State
def CmnActStaggerDown():
    sprite('bl070_04', 4)
    sprite('bl070_05', 4)
    sprite('bl070_06', 4)
    sprite('bl070_07', 4)
    sprite('bl070_08', 4)
    sprite('bl070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('bl070_10', 2)
    sprite('bl070_11', 2)
    sprite('bl070_12', 2)
    sprite('bl070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('bl113_00', 3)
    sprite('bl113_01', 3)
    sprite('bl113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('bl113_00', 3)
    sprite('bl113_01', 3)
    sprite('bl113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('bl113_00', 3)
    sprite('bl113_01', 3)
    sprite('bl113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('bl110_00', 3)
    sprite('bl110_01', 3)
    sprite('bl110_02', 2)
    sprite('bl110_03', 2)
    sprite('bl110_04', 2)
    sprite('bl110_05', 2)
    sprite('bl110_06', 200)
    sprite('bl110_07', 2)
    sprite('bl110_08', 2)
    sprite('bl110_09', 2)


@State
def CmnActUkemiLandB():
    sprite('bl111_00', 3)
    sprite('bl111_01', 3)
    sprite('bl111_02', 2)
    sprite('bl111_03', 2)
    sprite('bl111_04', 2)
    sprite('bl111_05', 2)
    sprite('bl111_06', 200)
    sprite('bl111_07', 2)
    sprite('bl111_08', 2)
    sprite('bl111_09', 2)


@State
def CmnActUkemiLandN():
    sprite('bl112_00', 2)
    sprite('bl112_01', 2)
    sprite('bl112_02', 2)
    sprite('bl112_03', 2)
    sprite('bl112_04', 2)
    sprite('bl112_05', 2)
    sprite('bl112_06', 2)
    sprite('bl112_07', 3)
    sprite('bl112_08', 3)


@State
def CmnActUkemiLandNLanding():
    sprite('bl024_00', 3)
    sprite('bl024_01', 3)
    sprite('bl024_02', 3)
    sprite('bl024_03', 3)
    sprite('bl024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('bl040_00', 3)
    sprite('bl040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('bl040_02', 3)
    sprite('bl040_03', 3)
    sprite('bl040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('bl040_01', 3)
    sprite('bl040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('bl040_05', 3)
    label(0)
    sprite('bl040_02', 3)
    sprite('bl040_03', 3)
    sprite('bl040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('bl040_01', 3)
    sprite('bl040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('bl041_00', 3)
    sprite('bl041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('bl041_02', 3)
    sprite('bl041_03', 3)
    sprite('bl041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('bl041_01', 3)
    sprite('bl041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('bl041_05', 3)
    label(0)
    sprite('bl041_02', 3)
    sprite('bl041_03', 3)
    sprite('bl041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('bl041_01', 3)
    sprite('bl041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('bl043_00', 3)
    sprite('bl043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('bl043_02', 3)
    sprite('bl043_03', 3)
    sprite('bl043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('bl043_01', 3)
    sprite('bl043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('bl043_05', 3)
    label(0)
    sprite('bl043_02', 3)
    sprite('bl043_03', 3)
    sprite('bl043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('bl043_01', 3)
    sprite('bl043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('bl045_00', 3)
    sprite('bl045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('bl045_02', 3)
    sprite('bl045_03', 3)
    sprite('bl045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('bl045_01', 3)
    sprite('bl045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('bl045_05', 3)
    label(0)
    sprite('bl045_02', 3)
    sprite('bl045_03', 3)
    sprite('bl045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('bl045_01', 3)
    sprite('bl045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('bl090_00', 2)
    sprite('bl090_01', 2)
    sprite('bl090_02', 1)
    SetCommonActionMark(1)
    sprite('bl090_03', 6)
    sprite('bl090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('bl091_00', 2)
    sprite('bl091_01', 2)
    sprite('bl091_02', 1)
    SetCommonActionMark(1)
    sprite('bl091_03', 6)
    sprite('bl091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('bl092_00', 2)
    sprite('bl092_01', 2)
    sprite('bl092_02', 1)
    SetCommonActionMark(1)
    sprite('bl092_03', 6)
    sprite('bl092_04', 6)


@State
def CmnActAirTurn():
    sprite('bl025_00', 4)
    sprite('bl025_01', 4)
    sprite('bl025_02', 4)


@State
def CmnActLockWait():
    sprite('bl040_02', 1)
    sprite('bl040_01', 3)
    sprite('bl040_00', 3)


@State
def CmnActLockReject():
    sprite('bl312_00', 3)
    sprite('bl312_01', 8)
    sprite('bl312_02', 3)
    sprite('bl312_03', 3)
    sprite('bl312_04', 4)
    sprite('bl312_05', 3)
    sprite('bl312_06', 2)
    sprite('bl312_07', 2)


@State
def CmnActAirLockWait():
    sprite('bl045_02', 1)
    sprite('bl045_01', 3)
    sprite('bl045_00', 3)


@State
def CmnActAirLockReject():
    sprite('bl322_00', 2)
    sprite('bl322_01', 2)
    sprite('bl322_02', 8)
    sprite('bl322_03', 2)
    sprite('bl322_04', 3)
    sprite('bl322_05', 3)
    sprite('bl322_06', 3)
    sprite('bl322_07', 3)
    sprite('bl322_08', 3)


@State
def CmnActLandSpin():
    sprite('bl071_00', 4)
    sprite('bl071_01', 4)
    label(0)
    sprite('bl071_02', 2)
    sprite('bl071_03', 2)
    sprite('bl071_04', 2)
    sprite('bl071_05', 2)
    sprite('bl071_06', 2)
    sprite('bl071_07', 2)
    sprite('bl071_08', 2)
    sprite('bl071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('bl071_10', 6)
    sprite('bl071_11', 5)
    sprite('bl071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('bl071_02', 2)
    sprite('bl071_03', 2)
    sprite('bl071_04', 2)
    sprite('bl071_05', 2)
    sprite('bl071_06', 2)
    sprite('bl071_07', 2)
    sprite('bl071_08', 2)
    sprite('bl071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('bl077_00', 2)
    sprite('bl077_01', 2)
    sprite('bl077_00ex01', 2)
    sprite('bl077_01ex01', 2)
    sprite('bl077_00ex02', 2)
    sprite('bl077_01ex02', 2)
    sprite('bl077_00ex03', 2)
    sprite('bl077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('bl077_02', 4)
    label(0)
    sprite('bl077_03', 3)
    sprite('bl077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('bl077_05', 5)
    sprite('bl077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('bl060_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('bl060_11', 4)
    sprite('bl060_13', 5)


@State
def CmnActBurstBegin():
    sprite('bl331_00', 2)
    sprite('bl331_01', 2)
    label(0)
    sprite('bl331_02', 3)
    sprite('bl331_03', 3)
    sprite('bl331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('bl331_05', 2)
    sprite('bl331_06', 3)
    sprite('bl331_07', 3)
    sprite('bl331_08', 3)
    label(0)
    sprite('bl331_06ex', 3)
    sprite('bl331_07ex', 3)
    sprite('bl331_08ex', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('bl331_09', 3)
    sprite('bl331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('bl331_11', 2)
    sprite('bl331_12', 2)
    label(0)
    sprite('bl331_02', 3)
    sprite('bl331_03', 3)
    sprite('bl331_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('bl331_05', 2)
    sprite('bl331_06', 3)
    sprite('bl331_07', 3)
    sprite('bl331_08', 3)
    label(0)
    sprite('bl331_06ex', 3)
    sprite('bl331_07ex', 3)
    sprite('bl331_08ex', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('bl331_13', 3)
    sprite('bl331_14', 3)
    label(0)
    sprite('bl020_07', 4)
    sprite('bl020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('bl333_00', 3)
    sprite('bl333_01', 3)
    sprite('bl333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('bl333_03', 32767)
    CreateObject('EMB_BL_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('bl333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('bl333_05', 3)
    callSubroutine('HeatUpStart')
    CreateObject('408_Kaiho', -1)
    sprite('bl333_06', 3)
    sprite('bl333_07', 3)
    label(0)
    sprite('bl333_05', 3)
    sprite('bl333_06', 3)
    sprite('bl333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('bl333_08', 3)
    sprite('bl333_09', 3)
    sprite('bl333_10', 3)
    sprite('bl333_11', 3)


@State
def CmnActAirOverDriveBegin():
    sprite('bl333_12', 3)
    sprite('bl333_13', 3)
    sprite('bl333_14', 3)
    CharacterFlash(16639, 20, 1)
    sprite('bl333_15', 32767)
    CreateObject('EMB_BL_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('bl333_16', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('bl333_05', 3)
    callSubroutine('HeatUpStart')
    CreateObject('408_Kaiho', -1)
    sprite('bl333_06', 3)
    sprite('bl333_07', 3)
    label(0)
    sprite('bl333_05', 3)
    sprite('bl333_06', 3)
    sprite('bl333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('bl333_08', 3)
    sprite('bl333_09', 3)
    sprite('bl333_17', 3)
    sprite('bl333_18', 3)


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
    sprite('bl200_00', 2)
    PerInertia(60)
    sprite('bl200_01', 2)
    sprite('bl200_02', 1)
    RandomCommonVoiceline(0)
    CommonSE('004_swing_grap_1_0')
    sprite('bl200_03', 3)
    sprite('bl200_04', 2)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('bl200_02', 2)
    sprite('bl200_01', 3)
    sprite('bl200_00', 3)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(550)
        HitOrBlockCancel('NmlAtk6A')
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
        HitOrBlockCancel('ShortDash')
        StayAfterMovement(1, 0)
        SetXCollisionFromOrigin(150)
    sprite('bl201_00', 3)
    sprite('bl201_01', 2)
    sprite('bl201_02', 2)
    sprite('bl201_03', 2)
    CommonSE('004_swing_grap_1_1')
    RandomCommonVoiceline(1)
    sprite('bl201_04', 3)
    sprite('bl201_05', 4)
    Recovery()
    Unknown2063()
    sprite('bl201_06', 3)
    sprite('bl201_07', 3)
    sprite('bl201_08', 3)
    sprite('bl201_09', 2)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        ProjectileLevel(1)
        Damage(800)
        AirUntechableTime(23)
        Hitstun(20)
        Hitstop(6)
        AirPushbackX(25000)
        AirPushbackY(1000)
        Floorslide(30)
        PushbackX(8000)
        UseFireHitspark(1)
        FatalCounter(1)
        CHGroundedHitstunAnimation(2)
        CHStagger(52)
        CHCrumple(42)
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('bl202_00', 2)
    sprite('bl202_01', 2)
    sprite('bl202_02', 3)
    DashEffects(100, 1, 1)
    physicsXImpulse(55000)
    sprite('bl202_02', 2)
    XImpulseAcceleration(15)
    DashEffects(100, 1, 1)
    sprite('bl202_02', 2)
    XImpulseAcceleration(40)
    sprite('bl202_03', 3)
    AddX(20000)
    XImpulseAcceleration(0)
    CommonSE('004_swing_grap_1_1')
    RandomCommonVoiceline(2)
    DespawnEAEffect('shot_charge')
    CreateObject('202_Blast00', 0)
    sprite('bl202_04', 1)
    StartMultihit()
    PrivateSE('blse_04')
    ScreenShake(5000, 2000)
    CreateObject('202_Blast01', 0)
    sprite('bl202_05', 5)
    AddInertia(-5000)
    sprite('bl202_05', 1)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('bl202_06', 4)
    sprite('bl202_07', 4)
    sprite('bl202_08', 4)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('DriveThrowLockOnZoneCtrl')
    sprite('bl203_00', 2)
    sprite('bl203_01', 1)
    sprite('bl203_01', 1)
    CreateObject('BLEF_LockOnZone', -1)
    RegisterObject(5, 1)
    RandomCommonVoiceline(3)
    sprite('bl203_02', 2)
    sprite('bl203_03', 1)
    SetActionMark(1)
    RunLoopUpon(17, 70)
    sprite('bl203_03', 1)
    uponSendToLabel(RELEASE_D, 1)
    sprite('bl203_04', 2)
    label(0)
    sprite('bl203_02', 3)
    sprite('bl203_03', 3)
    sprite('bl203_04', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    SetActionMark(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(17)
    CallPrivateFunction('BlDriveCancelCheck', 2, 60, 0, 0, 0, 0, 0, 0)
    sprite('bl203_05', 3)
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            sendToLabel(200)
        else:
            sendToLabel(100)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 11)
    gotoLabel(900)
    label(100)
    sprite('bl203_05', 5)
    ObjectUpon(5, 32)
    sprite('bl203_06', 11)
    gotoLabel(900)
    label(200)
    sprite('bl203_05', 5)
    ObjectUpon(5, 32)
    sprite('bl203_06', 11)
    label(900)
    sprite('keep', 1)
    CallPrivateFunction('BlDriveAngleSet', 0, 0, 0, 0, 0, 0, 0, 0)


@State
def DriveAttackCancelLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
    sprite('bl203_01', 5)
    ObjectUpon(5, 32)
    sprite('bl203_00', 5)
    loopRest()


@State
def DriveAttackMid():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackOff()
        AttackLevel_(4)
        AttackP1(80)
        BonusProration(110)
        AirUntechableTime(60)
        AirPushbackX(2500)
        AirPushbackY(-90000)
        GroundBounce(1)
        BouncePercentage(25)
        HitOverhead(2)
        HitAirUnblockable(0)
        MoveAttributes(1, 0, 0, 0, 0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        StarterRating(2)
        callSubroutine('DriveMidLowPowerUpCheck')

        def upon_OPPONENT_HIT():
            SetActionMark(1)
            SLOT_64 = 1
        uponSendToLabel(LANDING, 3)
    sprite('bl213_02', 2)
    SLOT_XVelocity = SLOT_19
    XImpulseAcceleration(5)
    physicsYImpulse(18000)
    EndYPhysicsImpulse()
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    JumpEffects(100, 1)
    sprite('bl213_03', 2)
    sprite('bl213_04', 2)
    sprite('bl213_05', 2)
    SLOT_XVelocity = SLOT_19
    XImpulseAcceleration(5)
    sprite('bl213_06', 2)
    sprite('bl213_07', 4)
    SmartVoiceline('bl108')
    sprite('bl213_08', 2)
    CommonSE('004_swing_grap_1_2')
    BeginBuffer('DriveAddAttack')
    sprite('bl213_09', 2)
    RefreshMultihit()
    label(2)
    sprite('bl213_10', 3)
    sprite('bl213_11', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('bl213_12', 4)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('bl213_13', 4)
    sprite('bl213_14', 2)
    if SLOT_2:
        BufferedOrPressedGoto('DriveAddAttack')
    sprite('bl213_15', 2)
    DisallowGoto('DriveAddAttack')
    sprite('bl213_16', 2)


@State
def DriveAttackLow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackOff()
        AttackLevel_(4)
        AttackP1(80)
        BonusProration(110)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(18000)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        callSubroutine('DriveMidLowPowerUpCheck')

        def upon_OPPONENT_HIT():
            SetActionMark(1)
            SLOT_64 = 1
        uponSendToLabel(LANDING, 3)
    sprite('bl213_02', 2)
    SLOT_XVelocity = SLOT_19
    XImpulseAcceleration(5)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    JumpEffects(100, 1)
    sprite('bl213_03', 2)
    sprite('bl213_04', 2)
    sprite('bl233_00', 2)
    SLOT_XVelocity = SLOT_19
    XImpulseAcceleration(5)
    label(2)
    sprite('bl233_01', 2)
    sprite('bl233_02', 2)
    sprite('bl233_03', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('bl233_04', 1)
    SmartVoiceline('bl109')
    sprite('bl233_05', 1)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('bl233_06', 1)
    CommonSE('004_swing_grap_1_2')
    BeginBuffer('DriveAddAttack')
    sprite('bl233_07', 3)
    RefreshMultihit()
    sprite('bl233_08', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('bl233_09', 3)
    sprite('bl233_10', 3)
    sprite('bl233_11', 3)
    sprite('bl213_14', 2)
    if SLOT_2:
        BufferedOrPressedGoto('DriveAddAttack')
    sprite('bl213_15', 2)
    DisallowGoto('DriveAddAttack')
    sprite('bl213_16', 2)


@State
def DriveAttackMiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
        EnterStateIfEventID(2, 'CmnActJumpLanding')
        PreviousStateCheck('DriveAttack6Land')
        SLOT_2 = SLOT_0

        def upon_EVERY_FRAME():
            if PreviousStateCheck('DriveAttack6Air'):
                SLOT_61 = 0
            if PreviousStateCheck('DriveAttack2'):
                SLOT_61 = 0
            if PreviousStateCheck('DriveAttack3'):
                SLOT_61 = 0
    sprite('bl431_06', 3)
    if SLOT_IsAirborne:
        AddX(-30000)
        AddY(-80000)
    sprite('bl022_00', 3)
    XImpulseAcceleration(0)
    AddX(100000)
    AddY(100000)
    physicsXImpulse(-1000)
    physicsYImpulse(9500)
    GravityDefault()
    sprite('bl022_01', 2)
    sprite('bl022_02', 2)
    XImpulseAcceleration(75)
    sprite('bl022_03', 2)
    if not SLOT_2:
        notConditionalSendToLabel(9)
    sprite('bl022_06', 3)
    XImpulseAcceleration(50)
    ForcedLandingRecovery(8, 1)
    label(0)
    sprite('bl022_07', 3)
    sprite('bl022_08', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('bl022_03', 1)


@State
def DriveAttackMiss_RockOn():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
        clearUponHandler(LANDING)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('bl431_13', 6)
    CrouchState(1)
    AddX(80000)
    physicsXImpulse(-5000)
    physicsYImpulse(5000)
    GravityDefault()
    if SLOT_IsAirborne:
        AddX(-80000)
    sprite('bl431_14', 32767)
    setGravity(3000)
    label(1)
    sprite('bl431_15', 5)
    LandingEffects(100, 1, 1)
    XImpulseAcceleration(90)
    sprite('bl431_16', 5)
    XImpulseAcceleration(75)


@State
def DriveAttack6Land():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(12500)
    sprite('bl203_07', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl203_08', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('bl203_07', 3)
    XImpulseAcceleration(50)
    sprite('bl203_37', 1)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl203_37', 2)
    XImpulseAcceleration(50)
    Recovery()
    sprite('bl203_38', 2)
    sprite('bl203_39', 2)
    sprite('bl203_40', 2)
    XImpulseAcceleration(50)
    sprite('bl203_55', 2)
    XImpulseAcceleration(25)
    sprite('bl203_56', 2)
    ExitState()
    label(1)
    sprite('bl203_18', 2)
    sprite('keep', 1)
    enterState('DriveThrowLand')


@State
def DriveAttack6Air():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
    sprite('bl203_07ex01', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl203_08ex01', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('bl203_07ex01', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bl203_37ex01', 1)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl203_37ex01', 2)
    ForcedLandingRecovery(11, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    Recovery()
    sprite('bl203_38ex01', 2)
    sprite('bl203_39ex01', 2)
    sprite('bl203_40ex01', 2)
    sprite('bl203_41', 2)
    sprite('bl203_42', 2)
    ExitState()
    label(1)
    sprite('bl203_09ex01', 1)
    sprite('keep', 1)
    enterState('DriveThrowAir')


@State
def DriveAttack2():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
    sprite('bl253_10', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl253_11', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('bl253_10', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bl253_19', 1)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl253_19', 2)
    ForcedLandingRecovery(6, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    Recovery()
    sprite('bl253_20', 2)
    sprite('bl253_21', 2)
    sprite('bl253_22', 2)
    sprite('bl253_23', 2)
    sprite('bl253_24', 2)
    ExitState()
    label(1)
    sprite('bl253_12', 1)
    sprite('keep', 1)
    enterState('DriveThrowAir')


@State
def DriveAttack3():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
    sprite('bl253_07', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl253_08', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('bl253_07', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bl253_13', 1)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl253_13', 2)
    ForcedLandingRecovery(6, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    Recovery()
    sprite('bl253_14', 2)
    sprite('bl253_15', 2)
    sprite('bl253_16', 2)
    sprite('bl253_17', 2)
    sprite('bl253_18', 2)
    ExitState()
    label(1)
    sprite('bl253_09', 1)
    sprite('keep', 1)
    enterState('DriveThrowAir')


@State
def DriveAttack8():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
    sprite('bl203_13', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl203_14', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    sprite('bl203_13', 3)
    XImpulseAcceleration(50)
    YAccel(50)
    setGravity(1800)
    sprite('bl203_49', 1)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl203_49', 2)
    ForcedLandingRecovery(6, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    Recovery()
    sprite('bl203_50', 2)
    sprite('bl203_51', 2)
    sprite('bl203_52', 2)
    sprite('bl203_53', 2)
    sprite('bl203_54', 2)
    ExitState()
    label(1)
    sprite('bl203_15', 1)
    sprite('keep', 1)
    enterState('DriveThrowAir')


@State
def DriveAttack9():

    def upon_IMMEDIATE():
        callSubroutine('DriveThrowInit')
    sprite('bl203_10', 3)
    AirDashEffects(1)
    PopSpeedX()
    PopSpeedY()
    sprite('bl203_11', 3)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('bl203_10', 3)
    XImpulseAcceleration(75)
    YAccel(75)
    setGravity(1800)
    sprite('bl203_43', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    label(0)
    sprite('keep', 1)
    callSubroutine('DriveThrowHitCheck')
    sprite('bl203_43', 2)
    ForcedLandingRecovery(6, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    Recovery()
    sprite('bl203_44', 2)
    sprite('bl203_45', 2)
    sprite('bl203_46', 2)
    sprite('bl203_47', 2)
    sprite('bl203_48', 2)
    ExitState()
    label(1)
    sprite('bl203_12', 1)
    sprite('keep', 1)
    enterState('DriveThrowAir')


@State
def DriveThrowLand():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('DriveThrowLandCatch', 1, 1, 0)
        clearUponHandler(LANDING)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        DamageFromStateOnly('DriveThrowExe')
        CHStateIfCHStart(3)
        SetZLine(1, 50)
        setInvincible(1)
        BurstInvincibility(0)
    sprite('keep', 1)
    ForceFaceSprite()
    sprite('bl203_19', 2)
    sprite('bl203_38', 2)
    sprite('bl203_39', 2)
    sprite('bl203_40', 2)
    sprite('bl203_55', 3)
    sprite('bl203_56', 3)


@State
def DriveThrowLandCatch():

    def upon_IMMEDIATE():
        CHStateIfCHStart(3)
        SpecialCancel(0)
        setInvincible(1)
    sprite('keep', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_20', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_20', 1)
    enterState('DriveThrowExe')


@State
def DriveThrowAir():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('DriveThrowAirCatch', 1, 1, 0)
        SetZLine(1, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        DamageFromStateOnly('DriveThrowExe')
        CHStateIfCHStart(3)
        EndMomentum(1)
        SpecialCancel(0)
        setInvincible(1)
        BurstInvincibility(0)
    sprite('keep', 1)
    ForceFaceSprite()
    AddY(20000)
    sprite('bl203_16', 2)
    sprite('bl203_38ex01', 2)
    sprite('bl203_39ex01', 2)
    sprite('bl203_40ex01', 2)
    sprite('bl203_41', 3)
    sprite('bl203_42', 3)


@State
def DriveThrowAirCatch():

    def upon_IMMEDIATE():
        CHStateIfCHStart(3)
        SLOT_52 = 1
        SpecialCancel(0)
        setInvincible(1)
    sprite('keep', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_17', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_17', 1)
    enterState('DriveThrowExe')


@Subroutine
def DriveThrowCancelInput():
    BeginBuffer('Shot')
    BeginBuffer('DriveAddAttack')
    BeginBuffer('InterrUpThrow')
    BeginBuffer('DashThrow')
    BeginBuffer('AntiAirThrowCancel')
    BeginBuffer('CompulsionHeatUpCancel')


@Subroutine
def DriveThrowCancelStart():
    BufferedOrPressedGoto('Shot')
    BufferedOrPressedGoto('InterrUpThrow')
    BufferedOrPressedGoto('DashThrow')
    BufferedOrPressedGoto('AntiAirThrowCancel')
    BufferedOrPressedGoto('CompulsionHeatUpCancel')


@Subroutine
def DriveThrowCancelClear():
    DisallowGoto('Shot')
    DisallowGoto('DriveAddAttack')
    DisallowGoto('InterrUpThrow')
    DisallowGoto('DashThrow')
    DisallowGoto('AntiAirThrowCancel')
    DisallowGoto('CompulsionHeatUpCancel')


@State
def DriveThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        SetZLine(1, 50)
        MinimumDamage(0)
        CHStateIfCHStart(3)
        SpecialCancel(0)
        setInvincible(1)
        SLOT_52 = 1
        CameraFast(1)
        uponSendToLabel(LANDING, 1)

        def upon_STATE_END():
            YAccel(50)
            EndYPhysicsImpulse()
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            if SLOT_2:
                clearUponHandler(OPPONENT_HIT)
                SLOT_64 = 1
    sprite('bl203_21', 2)
    physicsXImpulse(20000)
    physicsYImpulse(40000)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_22', 2)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl203_23', 2)
    RefreshMultihit()
    Damage(0)
    Hitstop(0)
    AirUntechableTime(50)
    AirPushbackX(0)
    AirPushbackY(10000)
    YImpulseBeforeWallbounce(300)
    AttackP2(100)
    SingleProration(1)
    OppPositionOnHit(1, 100000, -100000)
    XImpulseAcceleration(40)
    YAccel(85)
    sprite('bl203_24', 3)
    SetActionMark(1)
    BeginBuffer('DriveAddAttack')
    sprite('bl203_25', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bl203_26', 5)
    XImpulseAcceleration(50)
    GravityDefault()
    sprite('bl203_27', 5)
    XImpulseAcceleration(0)
    sprite('bl203_28', 1)
    physicsYImpulse(-80000)
    StartMultihit()
    sprite('bl203_29', 1)
    StartMultihit()
    sprite('bl203_30', 1)
    StartMultihit()
    RandomCommonVoiceline(1)
    sprite('bl203_29', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(900)
    AirUntechableTime(60)
    Hitstop(6)
    AirPushbackX(3000)
    AirPushbackY(-120000)
    YImpulseBeforeWallbounce(3300)
    GroundBounce(1)
    BouncePercentage(20)
    OppPositionOnHit(0, 0, 0)
    KeepBounceGravity(1)
    sprite('bl203_30', 1)
    sprite('bl203_31', 2)
    sprite('bl203_32', 2)
    sprite('bl203_33', 2)
    label(0)
    sprite('bl203_34', 3)
    sprite('bl203_35', 3)
    gotoLabel(0)
    label(1)
    sprite('bl203_36', 3)
    LandingEffects(100, 1, 1)
    sprite('bl213_12', 6)
    SpecialCancel(1)
    sprite('bl213_13', 6)
    sprite('bl213_14', 6)
    BufferedOrPressedGoto('DriveAddAttack')
    sprite('bl213_15', 6)
    DisallowGoto('DriveAddAttack')
    sprite('bl213_16', 3)
    sprite('bl213_16', 2)
    sprite('keep', 1)


@State
def DriveAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('DriveAddAttackExe', 1, 1, 0)
        clearUponHandler(LANDING)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SetZLine(1, 50)
        setInvincible(1)
        BurstInvincibility(0)
        callSubroutine('AdditionalThrowInit')
    sprite('bl203_19', 6)


@State
def DriveAddAttackExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        SetZLine(1, 50)
        callSubroutine('HeatUpActionInit')
        AttackLevel_(4)
        UseFireHitspark(1)
        MinimumDamage(0)
        OppPositionOnHit(1, 150000, 0)
        DamageEffect(5, '')
        if SLOT_5 == 1:
            AttackLevel_(4)
            Damage(800)
            Hitstop(10)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            AirPushbackX(60000)
            AirPushbackY(22000)
            AirHitstunAfterWallbounce(50)
            Wallbounce(1)
            WallbounceReboundTime(25)

            def upon_OPPONENT_HIT():
                ScreenShake(15000, 15000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_05')
        if SLOT_5 == 2:
            AttackLevel_(5)
            Damage(2400)
            Hitstop(15)
            AirHitstunAnimation(12)
            GroundedHitstunAnimation(12)
            AirPushbackX(60000)
            AirPushbackY(40000)
            AirHitstunAfterWallbounce(50)
            Wallbounce(1)
            WallbounceReboundTime(20)
            EnemyHitstopAddition(0, 3, 5)

            def upon_OPPONENT_HIT():
                ScreenShake(30000, 30000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_06')
    sprite('bl203_19', 3)
    CharacterFlash(16711680, 20, 2)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl400_00', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl400_01', 5)
    AddX(100000)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('shot_charge', 1)

    def RunOnObject_1():
        Size(1250)
    PrivateSE('blse_03')
    sprite('bl400_02', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 1)

    def RunOnObject_1():
        Size(1250)
    sprite('bl400_03', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 1)

    def RunOnObject_1():
        Size(1250)
    sprite('bl400_04', 6)
    Voiceline('bl200')
    AddX(60000)
    physicsXImpulse(5000)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 1)

    def RunOnObject_1():
        Size(1250)
    sprite('bl400_05', 1)
    AddX(40000)
    XImpulseAcceleration(50)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 1)

    def RunOnObject_1():
        Size(1250)
    sprite('bl400_06', 2)
    physicsXImpulse(-500)
    DespawnEAEffect('shot_charge')
    IgnoreBurst(0)
    DamageEffect(5, '')
    CreateObject('400_mazzle', 0)
    CreateObject('400_mazzle2', 0)
    sprite('bl400_07', 2)
    XImpulseAcceleration(50)
    sprite('bl400_08', 2)
    XImpulseAcceleration(50)
    sprite('bl400_09', 2)
    XImpulseAcceleration(0)
    sprite('bl400_10', 2)
    sprite('bl400_11', 2)
    sprite('bl400_12', 3)
    AddX(20000)
    sprite('bl400_13', 3)
    AddX(40000)
    sprite('bl400_14', 3)
    AddX(40000)
    sprite('bl400_15', 3)
    AddX(40000)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
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
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('bl230_00', 2)
    PerInertia(60)
    sprite('bl230_01', 3)
    RandomCommonVoiceline(0)
    sprite('bl230_02', 3)
    CommonSE('004_swing_grap_1_0')
    sprite('bl230_03', 4)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('bl230_04', 3)
    sprite('bl230_05', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(520)
        AttackP1(90)
        HitLow(2)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('bl231_00', 4)
    sprite('bl231_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('003_swing_grap_0_2')
    sprite('bl231_02', 1)
    sprite('bl231_03', 5)
    sprite('bl231_04', 3)
    Recovery()
    Unknown2063()
    sprite('bl231_05', 3)
    sprite('bl231_06', 3)
    sprite('bl231_07', 3)
    sprite('bl231_08', 3)
    sprite('bl231_09', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(500)
        AttackP1(90)
        AirPushbackX(3000)
        AirPushbackY(-60000)
        AirUntechableTime(30)
        Hitstun(20)
        HitLow(2)
        Hitstop(7)
        HardKnockdown(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')

        def upon_EVERY_FRAME():
            if SLOT_94:
                ChainCancel(0)
                SpecialCancel(0)
                if SLOT_StateDuration > 26:
                    SpecialCancel(1)
                    ChainCancel(1)
    sprite('bl232_00', 2)
    sprite('bl232_01', 2)
    sprite('bl232_02', 3)
    AddX(45000)
    physicsXImpulse(25000)
    DashEffects(100, 1, 1)
    sprite('bl232_03', 3)
    XImpulseAcceleration(50)
    sprite('bl232_04', 3)
    RandomCommonVoiceline(2)
    XImpulseAcceleration(25)
    CommonSE('004_swing_grap_1_0')
    sprite('bl232_05', 3)
    sprite('bl232_06', 2)
    sprite('bl232_07', 1)
    sprite('bl232_08', 1)
    sprite('bl232_09', 3)
    SetActionMark(1)
    sprite('bl232_10', 2)
    physicsXImpulse(45000)
    CommonSE('004_swing_grap_1_2')
    sprite('bl232_11', 1)
    RefreshMultihit()
    Damage(600)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(3000)
    AirPushbackY(18000)
    Hitstop(10)
    PushbackX(40000)
    HardKnockdown(-1)
    CHHardKnockdown(1)
    sprite('bl232_11', 2)
    XImpulseAcceleration(50)
    sprite('bl232_12', 1)
    Recovery()
    Unknown2063()
    sprite('bl232_13', 2)
    XImpulseAcceleration(25)
    sprite('bl232_14', 2)
    sprite('bl232_15', 2)
    sprite('bl232_16', 2)
    XImpulseAcceleration(0)
    sprite('bl232_17', 2)
    sprite('bl232_18', 2)
    sprite('bl232_19', 3)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(860)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-1000)
        AirPushbackY(20000)
        AirUntechableTime(40)
        AttackP1(90)
        CHHardKnockdown(1)
        FatalCounter(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('bl235_00', 3)
    sprite('bl235_01', 3)
    physicsXImpulse(50000)
    sprite('bl235_02', 3)
    XImpulseAcceleration(50)
    sprite('bl235_03', 2)
    setInvincible(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    sprite('bl235_04', 2)
    sprite('bl235_05', 2)
    sprite('bl235_06', 5)
    RandomCommonVoiceline(2)
    XImpulseAcceleration(25)
    sprite('bl235_07', 3)
    setInvincible(0)
    XImpulseAcceleration(25)
    CommonSE('004_swing_grap_1_2')
    sprite('bl235_08', 2)
    Recovery()
    Unknown2063()
    sprite('bl235_09', 2)
    sprite('bl235_10', 5)
    XImpulseAcceleration(0)
    sprite('bl235_11', 4)
    sprite('bl235_12', 4)
    sprite('bl235_13', 4)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('DriveThrowLockOnZoneCtrl')
    sprite('bl203_00', 2)
    sprite('bl203_01', 1)
    sprite('bl203_01', 1)
    CreateObject('BLEF_LockOnZone', -1)
    RegisterObject(5, 1)
    RandomCommonVoiceline(3)
    sprite('bl203_02', 2)
    sprite('bl203_03', 1)
    SetActionMark(1)
    RunLoopUpon(17, 70)
    sprite('bl203_03', 1)
    uponSendToLabel(RELEASE_D, 1)
    sprite('bl203_04', 2)
    label(0)
    sprite('bl203_02', 3)
    sprite('bl203_03', 3)
    sprite('bl203_04', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 3)
    SetActionMark(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(17)
    CallPrivateFunction('BlDriveCancelCheck', 2, 60, 0, 0, 0, 0, 0, 0)
    sprite('bl203_05', 1)
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            sendToLabel(200)
        else:
            sendToLabel(100)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    gotoLabel(900)
    label(100)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    gotoLabel(900)
    label(200)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    label(900)
    sprite('keep', 1)
    enterState('DriveAttackLow')


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        AttackP1(80)
        AirUntechableTime(14)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('bl250_00', 2)
    sprite('bl250_01', 2)
    RandomCommonVoiceline(0)
    sprite('bl250_02', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('bl250_03', 3)
    sprite('bl250_04', 5)
    Recovery()
    Unknown2063()
    sprite('bl250_02', 4)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(540)
        AttackP1(80)
        AirUntechableTime(17)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
    sprite('bl251_00', 2)
    sprite('bl251_01', 1)
    sprite('bl251_02', 2)
    sprite('bl251_03', 3)
    RandomCommonVoiceline(1)
    sprite('bl251_03', 1)
    CommonSE('004_swing_grap_1_1')
    sprite('bl251_04', 3)
    sprite('bl251_05', 3)
    Recovery()
    Unknown2063()
    sprite('bl251_06', 3)
    sprite('bl251_07', 3)
    sprite('bl251_08', 2)
    sprite('bl251_09', 2)
    sprite('bl251_10', 2)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(810)
        AttackP1(80)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(22)
        CHAirUntechableTime(60)
        CHAirPushbackY(-40000)
        CHHardKnockdown(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitJumpCancel(1)
    sprite('bl252_00', 3)
    sprite('bl252_01', 4)
    sprite('bl252_02', 4)
    CommonSE('004_swing_grap_1_2')
    RandomCommonVoiceline(2)
    sprite('bl252_03', 3)
    sprite('bl252_04', 5)
    Recovery()
    Unknown2063()
    sprite('bl252_05', 5)
    sprite('bl252_06', 5)
    sprite('bl252_07', 3)
    sprite('bl252_08', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AirPushbackX(12000)
        AirPushbackY(-30000)
        AirUntechableTime(32)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        CHAirUntechableTime(60)
        CHAirPushbackY(-100000)
        CHGroundBounce(1)
        CHBouncePercentage(25)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockJumpCancel(1)
        clearUponHandler(LANDING)
    sprite('bl022_02', 2)
    EndMomentum(1)
    setGravity(0)
    physicsXImpulse(-10000)
    physicsYImpulse(10000)
    sprite('bl022_03', 2)
    sprite('bl022_04', 2)
    sprite('bl431_07ex', 6)
    StartMultihit()
    physicsXImpulse(-4000)
    physicsYImpulse(4000)
    sprite('bl431_07ex', 6)
    StartMultihit()
    physicsXImpulse(-2000)
    physicsYImpulse(2000)
    sprite('bl431_08ex', 4)
    physicsXImpulse(1000)
    physicsYImpulse(-1000)
    sprite('bl431_09ex', 4)
    sprite('bl431_10', 2)
    StartMultihit()
    AddX(-30000)
    AddY(-20000)
    physicsXImpulse(40000)
    physicsYImpulse(-80000)
    setGravity(0)
    sprite('bl431_11', 2)
    AddY(80000)
    uponSendToLabel(LANDING, 100)
    label(0)
    sprite('bl431_12', 2)
    sprite('bl431_11', 2)
    gotoLabel(0)
    label(100)
    sprite('bl431_11', 2)
    StartMultihit()
    LandingEffects(100, 1, 1)
    AltKnockdownEffects(100, 1, 1)
    CrouchState(1)
    XImpulseAcceleration(10)
    sprite('bl431_13', 4)
    physicsXImpulse(-10000)
    physicsYImpulse(5000)
    setGravity(1800)
    sprite('bl431_14', 4)
    XImpulseAcceleration(50)
    sprite('bl431_15', 4)
    XImpulseAcceleration(50)
    sprite('bl431_16', 5)
    XImpulseAcceleration(50)
    sprite('bl431_16', 5)
    XImpulseAcceleration(0)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('DriveThrowLockOnZoneCtrl')
    sprite('bl253_00', 2)
    sprite('bl253_01', 1)
    sprite('bl253_01', 1)
    EndMomentum(1)
    CreateObject('BLEF_LockOnZone', -1)
    RegisterObject(5, 1)
    SLOT_61 = 0
    RandomCommonVoiceline(3)
    AddAirJumpCount(-1)
    AddAirDashCount(-1)
    sprite('bl253_02', 2)
    XImpulseAcceleration(25)
    YAccel(25)
    setGravity(100)
    sprite('bl253_03', 1)
    SetActionMark(1)
    RunLoopUpon(17, 70)
    sprite('bl253_03', 1)
    uponSendToLabel(RELEASE_D, 1)
    sprite('bl253_04', 2)
    label(0)
    sprite('bl253_02', 3)
    sprite('bl253_03', 3)
    sprite('bl253_04', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    SetActionMark(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(17)
    ObjectUpon(5, 32)
    CallPrivateFunction('BlDriveCancelCheck', 2, 60, 0, 0, 0, 0, 0, 0)
    sprite('bl253_05', 3)
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            sendToLabel(200)
        else:
            sendToLabel(100)
    sprite('bl253_05', 1)
    sprite('bl253_06', 3)
    gotoLabel(900)
    label(100)
    sprite('bl253_05', 3)
    sprite('bl253_06', 3)
    gotoLabel(900)
    label(200)
    sprite('bl253_05', 3)
    sprite('bl253_06', 3)
    label(900)
    sprite('keep', 1)
    CallPrivateFunction('BlDriveAngleSet', 0, 0, 0, 0, 0, 0, 0, 0)


@State
def DriveAttackCancelAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Recovery()
        EndYPhysicsImpulse()
    sprite('bl253_01', 5)
    sprite('bl253_00', 5)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(750)
        AttackP1(90)
        HitOverhead(2)
        GroundedHitstunAnimation(3)
        AirPushbackY(-150000)
        GroundBounce(1)
        BouncePercentage(15)
        AirUntechableTime(34)
        PushbackX(12000)
        StarterRating(2)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('bl210_00', 3)
    sprite('bl210_01', 3)
    sprite('bl210_02', 3)
    sprite('bl210_03', 5)
    sprite('bl210_04', 5)
    sprite('bl210_05', 2)
    RandomCommonVoiceline(1)
    sprite('bl210_06', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('bl210_07', 3)
    sprite('bl210_08', 3)
    Recovery()
    Unknown2063()
    sprite('bl210_09', 3)
    sprite('bl210_10', 3)
    sprite('bl210_11', 2)
    sprite('bl210_12', 2)
    sprite('bl210_13', 2)
    sprite('bl210_14', 2)
    sprite('bl210_15', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(90)
        AttackP2(79)
        AirUntechableTime(24)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        CHGroundedHitstunAnimation(10)
        AirPushbackY(35000)
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('ShortDash')
    sprite('bl211_00', 3)
    sprite('bl211_01', 1)
    sprite('bl211_01', 2)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('bl211_02', 3)
    RandomCommonVoiceline(1)
    sprite('bl211_03', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('bl211_04', 3)
    sprite('bl211_05', 4)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('bl211_06', 5)
    sprite('bl211_07', 4)
    sprite('bl211_08', 4)
    sprite('bl211_09', 2)
    sprite('bl211_10', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(90)
        AttackP2(82)
        MoveAttributes(1, 0, 0, 0, 0)
        AirUntechableTime(37)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(6500)
        AirPushbackY(42000)
        FatalCounter(1)
        HitAirUnblockable(0)
        Wallbounce(1)
        NonCornerWallbounce(1)
        AirHitstunAfterWallbounce(60)
        WallbounceReboundTime(15)
        HitOrBlockJumpCancel(1)
    sprite('bl212_00', 4)
    sprite('bl212_01', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('bl212_02', 4)
    AddX(45000)
    sprite('bl212_03', 4)
    physicsXImpulse(3000)
    sprite('bl212_04', 3)
    sprite('bl212_05', 3)
    RandomCommonVoiceline(2)
    sprite('bl212_06', 3)
    AddX(50000)
    physicsXImpulse(16500)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    sprite('bl212_07', 3)
    sprite('bl212_08', 3)
    Recovery()
    Unknown2063()
    sprite('bl212_09', 3)
    sprite('bl212_10', 3)
    sprite('bl212_11', 32767)
    ForcedLandingRecovery(9, 1)
    EnterStateIfEventID(2, 'CmnActJumpLanding')


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('DriveThrowLockOnZoneCtrl')
    sprite('bl203_00', 2)
    sprite('bl203_01', 1)
    sprite('bl203_01', 1)
    CreateObject('BLEF_LockOnZone', -1)
    RegisterObject(5, 1)
    RandomCommonVoiceline(3)
    sprite('bl203_02', 2)
    sprite('bl203_03', 1)
    SetActionMark(1)
    RunLoopUpon(17, 70)
    sprite('bl203_03', 1)
    uponSendToLabel(RELEASE_D, 1)
    sprite('bl203_04', 2)
    label(0)
    sprite('bl203_02', 3)
    sprite('bl203_03', 3)
    sprite('bl203_04', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 3)
    SetActionMark(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    clearUponHandler(17)
    CallPrivateFunction('BlDriveCancelCheck', 2, 60, 0, 0, 0, 0, 0, 0)
    sprite('bl203_05', 1)
    if SLOT_5 >= 1:
        if SLOT_5 == 2:
            sendToLabel(200)
        else:
            sendToLabel(100)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    gotoLabel(900)
    label(100)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    gotoLabel(900)
    label(200)
    sprite('bl203_05', 3)
    ObjectUpon(5, 32)
    sprite('bl203_06', 6)
    label(900)
    sprite('keep', 1)
    enterState('DriveAttackMid')


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('bl300_00', 6)
    sprite('bl300_01', 6)
    if random_(2, 0, 50):
        Voiceline('bl404')
    else:
        Voiceline('bl405')
    sprite('bl300_02', 8)
    sprite('bl300_03', 10)
    sprite('bl300_04', 8)
    sprite('bl300_05', 8)
    sprite('bl300_06', 8)
    sprite('bl300_07', 10)
    sprite('bl300_08', 8)
    sprite('bl300_09', 5)
    sprite('bl300_10', 5)
    sprite('bl300_11', 5)
    sprite('bl300_12', 5)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
    sprite('bl211_00', 4)
    sprite('bl211_01', 3)
    sprite('bl211_02', 3)
    sprite('bl211_03', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('bl211_04ex01', 3)
    sprite('bl211_04ex01', 8)
    AttackOff()
    sprite('bl211_05', 4)
    sprite('bl211_06', 4)
    sprite('bl211_07', 4)
    sprite('bl211_08', 4)
    sprite('bl211_09', 3)
    sprite('bl211_10', 3)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        ProjectileLevel(1)
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
    sprite('bl405_00', 3)
    sprite('bl405_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    Voiceline('bl159')
    HeatChange(-2500)
    sprite('bl405_01', 3)
    CharacterFlash(16763080, 8, 2)
    sprite('bl405_02', 2)
    sprite('bl405_03', 3)
    CreateObject('shot_charge', 0)

    def RunOnObject_1():
        Size(1100)
    PrivateSE('blse_03')
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    label(100)
    sprite('bl405_03', 3)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('bl405_05', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('bl405_05', 2)
    sprite('bl405_03', 3)
    sprite('bl405_04', 2)
    sprite('bl405_04', 1)
    PrivateSE('blse_05')
    ScreenShake(10000, 15000)
    sprite('bl405_06', 1)
    AddInertia(-5000)
    DespawnEAEffect('shot_charge')
    CreateObject('405_mazzle', 0)
    sprite('bl405_06', 2)
    StartMultihit()
    EnableAfterimage(0)
    sprite('bl405_07', 3)
    sprite('bl405_08', 4)
    sprite('bl405_09', 4)
    sprite('bl405_10', 4)
    sprite('bl405_11', 4)
    sprite('bl405_12', 2)
    sprite('bl405_13', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('bl310_00', 3)
    sprite('bl310_01', 2)
    sprite('bl310_01', 1)
    CommonSE('010_swing_sword_0')
    sprite('bl310_02', 3)
    sprite('bl310_03', 4)
    sprite('bl310_04', 4)
    sprite('bl310_05', 7)
    SmartVoiceline('bl155')
    sprite('bl310_06', 4)
    sprite('bl310_07', 4)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        Hitstop(0)
        AirUntechableTime(30)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirPushbackX(60000)
        AirPushbackY(20000)
        AirHitstunAfterWallbounce(50)
        Wallbounce(1)
        WallbounceReboundTime(10)
        Wallstick(1)
        WallstickDuration(33)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        EnableCollision(0)
    sprite('bl310_02', 6)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('bl311_00', 6)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl311_01', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl311_02', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_03', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_04', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_05', 3)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_06', 3)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_07', 3)
    AbsoluteY(120000)
    physicsXImpulse(5000)
    physicsYImpulse(5000)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl311_08', 3)
    SmartVoiceline('bl153')
    setGravity(500)
    AddX(60000)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl311_09', 3)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl311_10', 1)
    StartMultihit()
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl311_10', 4)
    sprite('bl311_11', 6)
    EndYPhysicsImpulse()
    uponSendToLabel(LANDING, 1)
    sprite('bl311_12', 32767)
    label(1)
    sprite('bl311_13', 3)
    physicsXImpulse(0)
    sprite('bl311_14', 4)
    sprite('bl311_15', 4)
    sprite('bl311_16', 4)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('bl310_00', 3)
    sprite('bl310_01', 2)
    sprite('bl310_01', 1)
    CommonSE('010_swing_sword_0')
    sprite('bl310_02', 3)
    sprite('bl310_03', 4)
    sprite('bl310_04', 4)
    sprite('bl310_05', 7)
    SmartVoiceline('bl155')
    sprite('bl310_06', 4)
    sprite('bl310_07', 4)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        AirPushbackY(-30000)
        AirPushbackX(1200)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HardKnockdown(20)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
    sprite('bl310_02', 6)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('bl311_00', 6)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl311_01', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl311_02', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl311_03', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl313_00', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl313_01', 4)
    OppThrowAnimation(16, 0)
    OppThrowPosition(0, 0, 0, 0, 6)
    sprite('bl313_02', 4)
    physicsXImpulse(-5000)
    physicsYImpulse(12500)
    EndYPhysicsImpulse()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl313_03', 4)
    AddX(-20000)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl313_04', 4)
    SmartVoiceline('bl153')
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    uponSendToLabel(LANDING, 1)
    label(0)
    sprite('bl313_05', 4)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl313_06', 4)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl313_05', 4)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl313_06', 4)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    gotoLabel(0)
    label(1)
    sprite('bl313_07', 1)
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    StartMultihit()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('bl313_07', 3)
    sprite('bl313_08', 6)
    physicsXImpulse(5000)
    sprite('bl313_09', 6)
    XImpulseAcceleration(50)
    sprite('bl313_10', 6)
    XImpulseAcceleration(50)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('bl320_00', 3)
    sprite('bl320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('bl320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('bl320_03', 4)
    sprite('bl320_04', 4)
    sprite('bl320_05', 7)
    SmartVoiceline('bl155')
    sprite('bl320_06', 4)
    sprite('bl320_07', 4)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        StarterRating(2)
        Hitstop(0)
        AirUntechableTime(60)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirPushbackX(60000)
        AirPushbackY(25000)
        Wallbounce(1)
        WallbounceReboundTime(25)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        ForcedLandingRecovery(0, 0)
    sprite('bl320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('bl321_00', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_02', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_03', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_04', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_05', 6)
    SmartVoiceline('bl154')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_06', 1)
    CommonSE('004_swing_grap_1_2')
    StartMultihit()
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl321_06', 3)
    sprite('bl321_07', 3)
    sprite('bl321_08', 3)
    EndYPhysicsImpulse()
    sprite('bl321_09', 3)
    sprite('bl321_10', 3)


@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('bl032_00', 3)
    sprite('bl032_01', 3)
    AirDashEffects(0)
    physicsXImpulse(19500)
    sprite('bl032_02', 3)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)


@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0

        def upon_17():
            clearUponHandler(17)
            AltKnockdownEffects(100, 1, 0)
            SetActionMark(1)
            sendToLabel(1)

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('bl401_00', 2)
    Voiceline('bl201')
    sprite('bl401_01', 2)
    sprite('bl401_02', 2)
    sprite('bl401_03', 1)
    RunLoopUpon(17, 19)
    uponSendToLabel(RELEASE_A, 1)
    sprite('bl401_03', 3)
    sprite('bl401_04', 3)
    CreateObject('shot_charge', 0)

    def RunOnObject_1():
        Size(1125)
    PrivateSE('blse_03')
    sprite('bl401_05', 3)
    label(0)
    sprite('bl401_03', 3)
    sprite('bl401_04', 3)
    sprite('bl401_05', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    clearUponHandler(RELEASE_A)
    clearUponHandler(17)
    sprite('bl401_06', 2)
    DespawnEAEffect('shot_charge')
    sprite('bl401_06', 1)
    if SLOT_2:
        CreateObject('shot_geyser', -1)
        RegisterObject(7, 1)
        if SLOT_5 == 1:
            ObjectUpon(CORNERED, 32)
        if SLOT_5 == 2:
            ObjectUpon(CORNERED, 33)
    else:
        CreateObject('shot', -1)
        RegisterObject(7, 1)
        if SLOT_5 == 1:
            ObjectUpon(CORNERED, 32)
        if SLOT_5 == 2:
            ObjectUpon(CORNERED, 33)
    sprite('bl401_07', 2)
    CreateObject('shot_fire', -1)
    CreateObject('shot_mazzle', 0)
    CommonSE('016_explode_1')
    AddInertia(-2500)
    sprite('bl401_08', 2)
    sprite('bl401_09', 6)
    sprite('bl401_10', 6)
    sprite('bl401_11', 6)
    sprite('bl401_12', 6)
    Recovery()
    sprite('bl401_13', 5)
    sprite('keep', 1)
    SLOT_65 = 0


@State
def InterrUpThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Damage(400)
        Hitstop(12)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Blockstun(16)
        Stagger(30)
        Crumple(20)
        PushbackX(-15000)
        OppPositionOnHit(1, 250000, 0)
        IgnoreComboTime(1)
        StarterRating(0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(350000)
        AttackP1(70)
        AttackP2(100)
        IgnoreBurst(1)

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0

        def upon_OPPONENT_HIT():
            Hitstop(6)
            EnableRapidCancel(0)
            enterState('InterrUpThrowCatch')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl402_00', 5)
    setInvincible(1)
    sprite('bl402_01', 6)
    Voiceline('bl202')
    sprite('bl402_02', 2)
    CommonSE('006_swing_blade_2')
    sprite('bl402_03', 2)
    sprite('bl402_04', 2)
    setInvincible(0)
    sprite('bl402_05', 10)
    sprite('bl402_06', 10)
    sprite('bl402_07', 5)
    sprite('bl402_08', 5)
    sprite('bl402_09', 5)
    sprite('keep', 1)
    SLOT_65 = 0


@State
def InterrUpThrowCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('InterrUpThrowExe', 2, 0, 0)
        SetZLine(1, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        AttackP2(100)
        SameMoveProration(-1)
        CHStateIfCHStart(3)
        if SLOT_5 == 2:
            SLOT_66 = 1
        setInvincible(1)
        PreventAirborneHit(0)

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0
    sprite('bl402_03', 2)
    sprite('bl402_04', 2)
    setInvincible(0)
    sprite('bl402_05', 5)
    sprite('bl402_06', 5)
    sprite('bl402_07', 5)
    sprite('bl402_08', 5)
    sprite('bl402_09', 4)
    sprite('keep', 1)
    SLOT_65 = 0


@State
def InterrUpThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(52)
        AirUntechableTime(100)
        MinimumDamage(0)
        OppPositionOnHit(1, 150000, 50000)
        CHStateIfCHStart(3)
        IgnoreComboTime(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3500)
        AirPushbackY(45000)
        YImpulseBeforeWallbounce(2500)
        StarterRating(0)
        uponSendToLabel(LANDING, 1)
        setInvincible(1)
        if SLOT_66:
            AirHitstunAnimation(17)
            GroundedHitstunAnimation(17)
            AirPushbackX(2500)
            AirPushbackY(38000)
            ResetGravity()
        SLOT_52 = 1

        def upon_STATE_END():
            SLOT_65 = 0
            SLOT_66 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl402_03', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl402_10', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl402_11', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl402_12', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    BeginBuffer('InterrUpAddAttack')
    sprite('bl402_13', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(8000)
    physicsYImpulse(13000)
    EndYPhysicsImpulse()
    JumpEffects(100, 1)
    sprite('bl402_14', 3)
    setGravity(2000)
    sprite('bl402_15', 3)
    Recovery()
    sprite('bl402_16', 32767)
    label(1)
    sprite('bl402_17', 5)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl402_18', 5)
    sprite('bl402_19', 5)
    BufferedOrPressedGoto('InterrUpAddAttack')
    sprite('bl402_20', 9)
    DisallowGoto('InterrUpAddAttack')


@State
def InterrUpAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('InterrUpAddAttackExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        AttackP2(100)
        SameMoveProration(-1)
        OnlyHitIfHitstun(1)
        setInvincible(1)
        callSubroutine('AdditionalThrowInit')
    sprite('bl403_00', 3)
    CreateObject('shot_charge', 0)
    PrivateSE('blse_03')
    sprite('bl403_01', 3)
    CommonSE('010_swing_sword_0')
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_02', 3)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_01', 3)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_02', 3)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_00', 3)
    DespawnEAEffect('shot_charge')


@State
def InterrUpAddAttackExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        SingleProration(1)
        AirPushbackY(-30000)
        AirPushbackX(1200)
        MinimumDamage(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HardKnockdown(27)
        UseFireHitspark(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        callSubroutine('HeatUpActionInit')
        IgnoreComboTime(1)
        if SLOT_5 == 1:
            AttackLevel_(4)
            Damage(1800)
            AttackP2(82)
            Hitstop(10)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                ScreenShake(0, 30000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_05')
        if SLOT_5 == 2:
            AttackLevel_(5)
            Damage(3500)
            AttackP2(84)
            Hitstop(20)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                ScreenShake(0, 50000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_06')
    sprite('bl403_01', 4)
    CharacterFlash(16711680, 20, 2)
    StartMultihit()
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_03', 6)
    Voiceline('bl203')
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_04', 1)
    StartMultihit()
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    DamageEffect(5, '')
    CreateObject('403_mazzle', 0)
    sprite('bl403_04', 2)
    IgnoreBurst(0)
    sprite('bl403_05', 2)
    sprite('bl403_06', 2)
    sprite('bl403_07', 7)
    sprite('bl403_08', 4)
    if not SLOT_94:
        if CheckInput(INPUT_HOLD_D):
            sendToLabel(0)
    sprite('bl403_09', 4)
    sprite('bl403_10', 2)
    sprite('bl403_11', 10)
    RefreshMultihit()
    AttackLevel_(2)
    Damage(50)
    MinimumDamage(100)
    Hitstop(0)
    UseFireHitspark(0)
    AirPushbackX(50000)
    AirPushbackY(19000)
    YImpulseBeforeWallbounce(1500)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(40)
    HardKnockdownReset()
    FlipOnHit(1)
    EnableCollision(0)
    IgnoreComboTime(0)
    Wallbounce(1)
    AirHitstunAfterWallbounce(50)
    WallbounceReboundTime(15)
    if SLOT_5 == 2:
        AirPushbackX(50000)
        AirPushbackY(25000)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(35)
        Wallstick(1)
        WallstickDuration(35)
    DamageEffect(0, '')
    sprite('bl403_12', 6)
    Recovery()
    sprite('bl403_13', 6)
    sprite('bl403_14', 6)
    sprite('bl403_15', 6)
    EnableCollision(1)
    ExitState()
    label(0)
    sprite('bl407_17', 5)
    Flip()
    sprite('bl407_18', 5)
    sprite('bl407_19', 5)
    sprite('bl407_20', 5)
    sprite('bl000_00', 1)
    Flip()
    ExitState()


@State
def DashThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('DashThrowExe', 2, 0, 0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(180000)
        ThrowTechWindow(-1)
        PreventAirborneHit(0)
        LockOpponentState(1)
        CrouchWhiff(1)
        SameMoveProration(-1)

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if not SLOT_94:
                    if CheckInput(INPUT_HOLD_B):
                        SLOT_51 = 1
                        clearUponHandler(EVERY_FRAME)
                        sendToLabel(100)
                    elif SLOT_19 < 250000:
                        clearUponHandler(EVERY_FRAME)
                        sendToLabel(1)
                elif SLOT_19 < 250000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(1)
    sprite('bl404_00', 4)
    sprite('bl404_00', 3)
    physicsXImpulse(8500)
    setInvincible(1)
    GuardPoint_(0)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('bl404_01', 3)
    Voiceline('bl204')
    XImpulseAcceleration(200)
    JumpEffects(100, 1)
    AirDashEffects(1)
    sprite('bl404_02', 3)
    sprite('bl404_03', 3)
    DashEffects(100, 1, 1)
    SetActionMark(1)
    sprite('bl404_04', 3)
    XImpulseAcceleration(150)
    sprite('bl404_05', 3)
    sprite('bl404_06', 3)
    sprite('bl404_07', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_08', 3)
    label(1)
    sprite('bl404_09', 2)
    clearUponHandler(EVERY_FRAME)
    XImpulseAcceleration(50)
    sprite('bl404_09', 2)
    sprite('bl404_10', 1)
    WhiffCancelEnable(0)
    XImpulseAcceleration(50)
    CommonSE('006_swing_blade_2')
    sprite('bl404_11', 3)
    XImpulseAcceleration(0)
    sprite('bl404_12', 3)
    setInvincible(0)
    physicsXImpulse(10000)
    AddX(40000)
    sprite('bl404_13', 4)
    XImpulseAcceleration(50)
    AddX(40000)
    sprite('bl404_14', 4)
    XImpulseAcceleration(50)
    sprite('bl404_15', 4)
    XImpulseAcceleration(0)
    sprite('bl404_16', 4)
    sprite('bl404_17', 3)
    sprite('keep', 1)
    SLOT_65 = 0
    ExitState()
    label(100)
    sprite('bl032_03', 3)
    Recovery()
    XImpulseAcceleration(50)
    sprite('bl032_04', 3)
    sprite('bl032_05', 5)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 5)
    setInvincible(0)
    sprite('bl032_07', 4)
    sprite('keep', 1)
    SLOT_65 = 0
    ExitState()


@State
def DashThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(1700)
        AttackP2(82)
        AirUntechableTime(44)
        Hitstop(0)
        MinimumDamage(0)
        OppPositionOnHit(1, 50000, 200000)
        CHStateIfCHStart(3)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(19000)
        AirPushbackY(23000)
        YImpulseBeforeWallbounce(1600)
        IgnoreComboTime(0)
        uponSendToLabel(LANDING, 1)
        SetZLine(1, 50)
        if SLOT_19 < 250000:
            AirPushbackX(9500)
            AirPushbackY(27000)
            AirUntechableTime(60)
        setInvincible(1)
        SLOT_52 = 1

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('bl404_11', 1)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('bl404_18', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    physicsXImpulse(12000)
    sprite('bl404_19', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl404_20', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    XImpulseAcceleration(200)
    AirDashEffects(1)
    sprite('bl404_21', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl404_22', 4)
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SkidEffects(100, 1, 1)
    XImpulseAcceleration(75)
    sprite('bl404_23', 4)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    XImpulseAcceleration(50)
    sprite('bl404_24', 6)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    SetZLine(0, 50)
    physicsYImpulse(12000)
    setGravity(1000)
    JumpEffects(100, 1)
    sprite('bl404_25', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    SetZLine(1, 50)
    sprite('bl404_26', 4)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 0, 0, 0, 8)
    BeginBuffer('DashAddAttack')
    sprite('bl404_27', 1)
    StartMultihit()
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl404_27', 3)
    sprite('bl404_28', 3)
    Recovery()
    sprite('bl404_29', 32767)
    label(1)
    sprite('bl404_30', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl404_31', 3)
    sprite('bl404_31', 1)
    sprite('bl404_31', 2)
    sprite('bl404_32', 3)
    BufferedOrPressedGoto('DashAddAttack')
    sprite('bl404_33', 3)
    DisallowGoto('DashAddAttack')


@State
def DashAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        NoAttackDuringAction(1)
        SetYCollisionFromOrigin(100)
        callSubroutine('HeatUpActionInit')
        callSubroutine('AdditionalThrowInit')
    sprite('bl405_00', 1)
    CharacterFlash(16711680, 20, 2)
    sprite('bl405_01', 2)
    sprite('bl405_02', 2)
    sprite('bl405_03', 2)
    CreateObject('shot_charge', 0)

    def RunOnObject_1():
        Size(1600)
    PrivateSE('blse_03')
    sprite('bl405_04', 2)
    sprite('bl405_05', 2)
    sprite('bl405_03', 2)
    sprite('bl405_04', 2)
    Voiceline('bl205')
    sprite('bl405_05', 2)
    sprite('bl405_06', 3)
    CreateObject('blef405Atk', -1)
    ObjectUpon(STATE_END, 32)
    AddInertia(-5000)
    DespawnEAEffect('shot_charge')
    CreateObject('404_mazzle', 0)
    CreateObject('404_mazzle2', 0)
    sprite('bl405_07', 5)
    Recovery()
    sprite('bl405_08', 5)
    sprite('bl405_09', 5)
    sprite('bl405_10', 5)
    sprite('bl405_11', 3)
    sprite('bl405_12', 3)
    sprite('bl405_13', 3)


@State
def AntiAirThrowLand():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AntiAirThrowExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, 1000000, -40000)
        RangeCheck(250000)
        ThrowTechWindow(-1)
        AttackP1(90)
        AttackP2(90)
        SameMoveProration(-1)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        EndMomentum(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
    sprite('bl023_00', 3)
    sprite('bl023_01', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('bl406_02', 2)
    JumpEffects(100, 1)
    physicsXImpulse(28000)
    physicsYImpulse(28000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    SetYCollisionFromOrigin(250)
    sprite('bl406_03', 2)
    sprite('bl406_04', 2)
    sprite('bl406_05ex01', 4)
    XImpulseAcceleration(25)
    sprite('bl406_06', 3)
    setInvincible(0)
    setGravity(800)
    sprite('bl406_07', 3)
    Voiceline('bl155')
    sprite('bl406_08', 6)
    EndYPhysicsImpulse()
    sprite('bl406_09', 6)
    sprite('bl406_10', 6)
    sprite('bl406_11', 6)
    label(0)
    sprite('bl020_07', 3)
    sprite('bl020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl024_00', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl024_01', 2)
    sprite('bl024_02', 2)
    sprite('bl024_03', 2)
    sprite('bl024_04', 2)


@State
def AntiAirThrowCancel():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AntiAirThrowExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(250000)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        EndMomentum(1)

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
    sprite('bl023_00', 1)
    sprite('bl023_01', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('bl406_02', 1)
    JumpEffects(100, 1)
    physicsXImpulse(5000)
    physicsYImpulse(18000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    SetYCollisionFromOrigin(250)
    sprite('bl406_03', 1)
    sprite('bl406_04', 1)
    sprite('bl406_05', 4)
    XImpulseAcceleration(25)
    sprite('bl406_06', 3)
    setInvincible(0)
    setGravity(300)
    sprite('bl406_07', 3)
    Voiceline('bl155')
    sprite('bl406_08', 6)
    sprite('bl406_09', 6)
    EndYPhysicsImpulse()
    sprite('bl406_10', 6)
    sprite('bl406_11', 6)
    label(0)
    sprite('bl020_07', 3)
    sprite('bl020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl024_00', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl024_01', 2)
    sprite('bl024_02', 2)
    sprite('bl024_03', 2)
    sprite('bl024_04', 1)
    sprite('keep', 1)
    SLOT_65 = 0


@State
def AntiAirThrowAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        Damage(0)
        Hitstop(6)
        OppPositionOnHit(1, 100000, 50000)
        IgnoreBurst(1)
        IgnoreComboTime(1)
        EnableRapidCancel(0)
        AttackP2(100)
        SameMoveProration(-1)
        HitAirUnblockable(0)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        EndMomentum(1)
        AddAirJumpCount(-1)
        AddAirDashCount(-1)
        Unknown2061(1)

        def upon_OPPONENT_HIT():
            enterState('AntiAirThrowCatch')
    sprite('bl406_00', 2)
    sprite('bl406_01', 2)
    sprite('bl406_02', 3)
    physicsXImpulse(12000)
    physicsYImpulse(32000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    SLOT_62 = 0
    sprite('bl406_03', 2)
    sprite('bl406_04', 2)
    sprite('bl406_05', 2)
    sprite('bl406_06', 3)
    EnableRapidCancel(1)
    XImpulseAcceleration(80)
    setGravity(800)
    sprite('bl406_07', 3)
    Voiceline('bl155')
    sprite('bl406_08', 6)
    EndYPhysicsImpulse()
    sprite('bl406_09', 6)
    sprite('bl406_10', 6)
    sprite('bl406_11', 6)


@State
def AntiAirThrowCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AntiAirThrowExe', 2, 1, 0)
        SetZLine(1, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        CHStateIfCHStart(3)
    sprite('bl406_05', 2)
    sprite('bl406_06', 3)
    Recovery()
    sprite('bl406_07', 3)
    sprite('bl406_08', 3)
    sprite('bl406_09', 3)
    sprite('bl406_10', 3)
    sprite('bl406_11', 3)


@State
def AntiAirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(2200)
        AttackP2(82)
        AirUntechableTime(62)
        Hitstop(0)
        MinimumDamage(0)
        IgnoreComboTime(0)
        CHStateIfCHStart(3)
        AttackDirection(3)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(13500)
        AirPushbackY(50000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        AirHitstunAfterWallbounce(60)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickDuration(13)
        OppPositionOnHit(1, -50000, 50000)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        EnterStateIfEventID(2, 'CmnActJumpLanding')
        if SLOT_19 < 250000:
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
            AirPushbackX(5000)
            AirPushbackY(50000)
            AirUntechableTime(60)
        SLOT_52 = 1

        def upon_STATE_END():
            SLOT_65 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl406_05', 5)
    Voiceline('bl206')
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_12', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_13', 5)
    BeginBuffer('AntiAirAddAttack')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl406_14', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_15', 3)
    physicsXImpulse(7500)
    physicsYImpulse(19000)
    EndYPhysicsImpulse()
    sprite('bl406_16', 4)
    Recovery()
    sprite('bl406_17', 5)
    sprite('bl406_18', 5)
    BufferedOrPressedGoto('AntiAirAddAttack')
    sprite('bl406_19', 3)
    DisallowGoto('AntiAirAddAttack')
    sprite('bl406_20', 3)
    sprite('bl406_21', 3)
    sprite('bl022_06', 3)
    Flip()
    label(0)
    sprite('bl022_07', 3)
    sprite('bl022_08', 3)
    gotoLabel(0)


@State
def AntiAirThrowAirCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AntiAirThrowAirExe', 2, 1, 0)
        SetZLine(1, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        CHStateIfCHStart(3)
    sprite('bl406_05', 2)
    sprite('bl406_06', 3)
    Recovery()
    sprite('bl406_07', 3)
    sprite('bl406_08', 3)
    sprite('bl406_09', 3)
    sprite('bl406_10', 3)
    sprite('bl406_11', 3)


@State
def AntiAirThrowAirExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(4)
        Damage(2200)
        AttackP2(82)
        AirUntechableTime(62)
        Hitstop(0)
        MinimumDamage(0)
        IgnoreComboTime(0)
        CHStateIfCHStart(3)
        AttackDirection(3)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(13500)
        AirPushbackY(50000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        AirHitstunAfterWallbounce(60)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickDuration(13)
        OppPositionOnHit(1, -50000, 50000)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        EnterStateIfEventID(2, 'CmnActJumpLanding')
        if SLOT_19 < 250000:
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
            AirPushbackX(5000)
            AirPushbackY(50000)
            AirUntechableTime(60)
        SLOT_52 = 1

        def upon_STATE_END():
            SLOT_65 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl406_05', 5)
    Voiceline('bl206')
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_12', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_13', 5)
    BeginBuffer('AntiAirAddAttack')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl406_14', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl406_15', 3)
    physicsXImpulse(7500)
    physicsYImpulse(19000)
    EndYPhysicsImpulse()
    sprite('bl406_16', 4)
    Recovery()
    sprite('bl406_17', 5)
    sprite('bl406_18', 5)
    BufferedOrPressedGoto('AntiAirAddAttack')
    sprite('bl406_19', 3)
    DisallowGoto('AntiAirAddAttack')
    sprite('bl406_20', 3)
    sprite('bl406_21', 3)
    sprite('bl022_06', 3)
    Flip()
    label(0)
    sprite('bl022_07', 3)
    sprite('bl022_08', 3)
    gotoLabel(0)


@State
def AntiAirAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AntiAirAddAttackExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        OnlyHitIfHitstun(1)
        EndMomentum(1)
        setInvincible(1)
        callSubroutine('AdditionalThrowInit')
    sprite('bl406_00', 3)
    sprite('bl406_01', 3)
    sprite('bl407_01', 3)
    Flip()
    physicsXImpulse(-35000)
    PrivateFunction(3, 2, 20, 0, 10, 2, 13)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    sprite('bl407_02', 3)
    sprite('bl407_03', 3)
    sprite('bl407_04', 3)
    Voiceline('bl155')
    XImpulseAcceleration(50)
    WhiffCrouchBlockCancel(1)
    sprite('bl407_05', 3)
    sprite('bl407_06', 3)
    sprite('bl407_07', 3)
    sprite('bl407_08', 3)
    sprite('bl407_09', 3)


@State
def AntiAirAddAttackExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        MinimumDamage(0)
        UseFireHitspark(1)
        AirPushbackX(-350)
        YImpulseBeforeWallbounce(1800)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)

        def upon_FALLING():
            clearUponHandler(FALLING)
            sendToLabel(100)
        callSubroutine('HeatUpActionInit')
        if SLOT_5 == 1:
            AttackLevel_(4)
            Damage(1900)
            AttackP2(82)
            Hitstop(10)
            AirUntechableTime(60)
            GroundedHitstunAnimation(9)
            AirHitstunAnimation(9)
            AirPushbackY(30000)

            def upon_OPPONENT_HIT():
                ScreenShake(15000, 15000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_05')
        if SLOT_5 == 2:
            AttackLevel_(5)
            Damage(4200)
            AttackP2(84)
            Hitstop(15)
            AirUntechableTime(60)
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirPushbackY(45000)

            def upon_OPPONENT_HIT():
                ScreenShake(30000, 30000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_06')
    sprite('bl407_03', 3)
    CharacterFlash(16711680, 20, 2)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(-15000)
    physicsYImpulse(60000)
    setGravity(2000)
    sprite('bl407_10', 5)
    OppThrowAnimation(1, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl407_11', 5)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl407_12', 32767)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    setGravity(5000)
    CreateObject('shot_charge', 0)
    PrivateSE('blse_03')
    label(100)
    sprite('bl407_13', 5)
    XImpulseAcceleration(40)
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    label(0)
    sprite('bl407_14', 3)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl407_15', 3)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    gotoLabel(0)
    label(1)
    sprite('bl407_16', 3)
    Voiceline('bl207')
    EndMomentum(1)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    sprite('bl403_04', 1)
    Flip()
    StartMultihit()
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    DespawnEAEffect('shot_charge')
    DamageEffect(5, '')
    CreateObject('403_mazzle', 0)
    sprite('bl403_04', 3)
    IgnoreBurst(0)
    sprite('bl403_05', 3)
    Recovery()
    sprite('bl403_06', 3)
    sprite('bl403_07', 3)
    sprite('bl403_08', 3)
    sprite('bl407_17', 3)
    Flip()
    sprite('bl407_18', 3)
    sprite('bl407_19', 3)
    sprite('bl407_20', 3)
    sprite('bl000_00', 1)
    Flip()


@State
def CommandThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('CommandThrowExe', 2, 0, 0)
        AttackP1(80)
        RangeCheck(100000)
        DistanceCheck(250000, 1, -1, -1)
        SetZLine(0, 50)
    sprite('bl431_00', 3)
    sprite('bl431_01', 3)
    sprite('bl431_02', 3)
    sprite('bl431_03', 3)
    CommonSE('006_swing_blade_2')
    sprite('bl310_04', 4)
    sprite('bl310_05', 9)
    Voiceline('bl155')
    sprite('bl310_05', 9)
    sprite('bl310_06', 8)
    sprite('bl310_07', 8)


@State
def CommandThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(3)
        Damage(0)
        Hitstop(1)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        PushbackX(9800)
        StarterRating(2)
        setInvincible(1)
        SLOT_52 = 1

        def upon_LANDING():
            clearUponHandler(LANDING)
            EndMomentum(1)
            sendToLabel(1)
        BeginBuffer('CommandThrowAddAttack')
    sprite('bl431_03', 1)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('bl409_00', 3)
    sprite('bl409_01', 2)
    Voiceline('bl209')
    sprite('bl409_02', 3)
    physicsXImpulse(3000)
    physicsYImpulse(30000)
    setGravity(2000)
    sprite('bl409_03', 5)
    sprite('bl409_04', 5)
    sprite('bl409_05', 5)
    sprite('bl409_06', 5)
    sprite('bl409_07', 5)
    sprite('bl409_08', 2)
    StartMultihit()
    sprite('bl409_08', 32767)
    RefreshMultihit()
    Damage(300)
    ResetAttackP2()
    Hitstop(6)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    if SLOT_137:
        DamageMultiplier(80)
    label(1)
    sprite('bl409_09', 6)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(700)
    YImpulseBeforeWallbounce(50000)
    KeepBounceGravity(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(500)
    AirPushbackY(-40000)
    Hitstop(6)
    HardKnockdown(25)
    ScreenShake(0, 30000)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('bl409_10', 6)
    sprite('bl409_11', 4)
    BufferedOrPressedGoto('CommandThrowAddAttack')
    sprite('bl409_12', 4)
    DisallowGoto('CommandThrowAddAttack')
    sprite('bl409_13', 4)
    sprite('bl409_14', 4)


@State
def CommandThrowAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('CommandThrowAddAttackExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        DoNotHitKnockedDownOpp(0)
        EndMomentum(1)
        setInvincible(1)
        callSubroutine('AdditionalThrowInit')
    sprite('bl409_11', 3)
    sprite('bl410_00', 3)
    sprite('bl410_01', 3)
    sprite('bl410_02', 3)
    sprite('bl410_03', 3)
    RefreshMultihit()
    WhiffCrouchBlockCancel(1)


@State
def CommandThrowAddAttackExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        MinimumDamage(0)
        EnableRapidCancel(0)
        setInvincible(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
    sprite('bl410_03', 3)
    CharacterFlash(16711680, 20, 2)
    StartMultihit()
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_04', 3)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_05', 3)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_06', 3)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_07', 3)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(300)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(500)
    AirPushbackY(-40000)
    HardKnockdown(1)
    OppPositionOnHit(1, 100000, 0)
    sprite('keep', 1)
    enterState('CommandThrowAddAttack2nd')


@State
def CommandThrowAddAttack2nd():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('CommandThrowAddAttack2ndExe', 2, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        DoNotHitKnockedDownOpp(0)
        EnableRapidCancel(0)
        EndMomentum(1)
        setInvincible(1)
        callSubroutine('AdditionalThrowInit')
    sprite('bl410_07', 3)
    Voiceline('bl210')
    RefreshMultihit()
    sprite('bl410_08', 3)
    sprite('bl410_09', 3)
    sprite('bl410_10', 3)
    sprite('bl410_11', 3)
    sprite('bl410_12', 3)
    sprite('bl410_13', 3)
    RefreshMultihit()
    AttackLevel_(5)
    sprite('bl410_14', 3)
    sprite('bl410_15', 3)
    sprite('bl410_16', 3)
    sprite('bl410_17', 3)
    sprite('bl410_18', 3)


@State
def CommandThrowAddAttack2ndExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        MinimumDamage(0)
        setInvincible(1)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        SLOT_52 = 1
        UseFireHitspark(1)
        callSubroutine('HeatUpActionInit')
    sprite('bl410_07', 1)
    StartMultihit()
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_08', 8)
    CreateObject('shot_charge', 0)
    PrivateSE('blse_03')
    CreateObject('blef_410_fire', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_09', 8)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    CreateObject('blef_410_fire', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_10', 8)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    CreateObject('blef_410_fire', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_11', 8)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    CreateObject('blef_410_fire', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_12', 8)
    DespawnEAEffect('shot_charge')
    CreateObject('shot_charge', 0)
    CreateObject('blef_410_fire', 0)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl410_13', 1)
    DespawnEAEffect('shot_charge')
    StartMultihit()
    OppThrowAnimation(10, 0)
    OppThrowPosition(0, 4, 4, 0, 1)
    sprite('bl410_13', 3)
    RefreshMultihit()
    CreateObject('blef_410_finish', 1)
    IgnoreBurst(0)
    if SLOT_5 == 1:
        AttackLevel_(4)
        Damage(1700)
        AirUntechableTime(30)
        AttackP2(82)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(45000)
        AirPushbackY(20000)
        Wallbounce(1)
        WallbounceReboundTime(50)
        AirHitstunAfterWallbounce(40)
        Wallstick(1)
        WallstickDuration(40)

        def upon_OPPONENT_HIT():
            ScreenShake(15000, 15000)
            PrivateSE('blse_05')
    if SLOT_5 == 2:
        AttackLevel_(5)
        Damage(2700)
        AirUntechableTime(30)
        AttackP2(84)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(30000)
        Wallbounce(1)
        WallbounceReboundTime(60)
        AirHitstunAfterWallbounce(40)
        Wallstick(1)
        WallstickDuration(45)

        def upon_OPPONENT_HIT():
            ScreenShake(30000, 30000)
            CommonSE('016_explode_2')
            PrivateSE('blse_06')
    sprite('bl410_14', 5)
    sprite('bl410_15', 5)
    sprite('bl410_16', 5)
    sprite('bl410_17', 5)
    sprite('bl410_18', 5)


@State
def CompulsionHeatUp():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EndMomentum(1)
        PreventBlocking(1)
        SetActionMark(0)
        RunLoopUpon(17, 30)

        def upon_17():
            AddActionMark(1)
            sendToLabel(1)
    sprite('bl408_00', 2)
    sprite('bl408_01', 2)
    Voiceline('bl208')
    sprite('bl408_02', 3)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    CreateObject('408_Fireroop', 0)
    CreateObject('408_BodyFire', -1)
    sprite('bl408_03', 3)
    uponSendToLabel(RELEASE_D, 1)
    label(0)
    sprite('bl408_02', 3)
    sprite('bl408_03', 3)
    gotoLabel(0)
    label(1)
    sprite('bl408_02', 3)
    clearUponHandler(RELEASE_D)
    clearUponHandler(17)
    TriggerUponForState('408_Fireroop', 32)
    sprite('bl408_03', 3)
    sprite('bl408_04', 2)
    sprite('bl408_05', 2)
    setInvincible(0)
    PrivateSE('blse_09')
    AltKnockdownEffects(100, 1, 0)
    ScreenShake(10000, 20000)
    sprite('bl408_06', 2)
    CreateObject('408_Kaiho', -1)
    sprite('bl408_07', 2)
    callSubroutine('HeatUpStart')
    if SLOT_2:
        callSubroutine('HeatUpStart')
        ScreenShake(30000, 50000)
    sprite('bl408_08', 2)
    sprite('bl408_06', 2)
    sprite('bl408_07', 2)
    sprite('bl408_08', 2)
    sprite('bl408_09', 3)
    sprite('bl408_10', 3)
    sprite('bl408_11', 3)


@State
def CompulsionHeatUpCancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        EndMomentum(1)
        PreventBlocking(1)

        def upon_PLAYER_DAMAGED():
            if SLOT_65:
                SLOT_64 = 0
                SLOT_65 = 0
    sprite('bl408_00', 4)
    sprite('bl408_01', 4)
    Voiceline('bl208')
    sprite('bl408_02', 3)
    setInvincible(1)
    GuardPoint_(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    CreateObject('408_Fireroop', 0)
    CreateObject('408_BodyFire', -1)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    TriggerUponForState('408_Fireroop', 32)
    sprite('bl408_03', 3)
    sprite('bl408_04', 3)
    sprite('bl408_05', 3)
    setInvincible(0)
    PrivateSE('blse_09')
    AltKnockdownEffects(100, 1, 0)
    ScreenShake(10000, 20000)
    sprite('bl408_06', 3)
    CreateObject('408_Kaiho', -1)
    sprite('bl408_07', 3)
    SLOT_5 = SLOT_5 + 1
    if SLOT_5 >= 2:
        SLOT_5 = 2
    SLOT_31 = 900
    CreateObject('HeatUpEff', 103)
    sprite('bl408_08', 3)
    sprite('bl408_06', 3)
    sprite('bl408_07', 3)
    sprite('bl408_08', 3)
    sprite('bl408_09', 3)
    sprite('bl408_10', 3)
    sprite('bl408_11', 2)
    sprite('keep', 1)
    SLOT_65 = 0


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(400)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        Hitstop(3)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(20000)
        CHAirPushbackX(5000)
        CHAirPushbackY(20000)
        EndMomentum(1)
        StayAfterMovement(1, 0)
        AttackDirection(2)
        StarterRating(2)
        OppPositionOnHit(1, 25000, 70000)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            SetActionMark(1)
        SLOT_63 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl430_00', 3)
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', 100)
    setInvincible(1)
    sprite('bl430_01', 3)
    Voiceline('bl250')
    sprite('bl430_02', 3)
    CreateObject('430_handaura', 0)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_05', 3)
    DespawnEAEffect('430_handaura')
    setInvincible(0)
    sprite('bl430_06', 3)
    sprite('bl404_00', 2)
    AirDashEffects(1)
    sprite('bl404_01', 2)
    physicsXImpulse(35000)
    sprite('bl404_02', 2)
    sprite('bl404_03', 2)

    def upon_EVERY_FRAME():
        if SLOT_19 < 300000:
            sendToLabel(1)
    sprite('bl404_04', 2)
    XImpulseAcceleration(110)
    sprite('bl404_05', 2)
    XImpulseAcceleration(110)
    sprite('bl404_06', 2)
    XImpulseAcceleration(110)
    sprite('bl404_07', 2)
    DashEffects(100, 1, 1)
    sprite('bl404_08', 2)
    label(1)
    sprite('bl430_07', 4)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(LANDING, 2)
    XImpulseAcceleration(25)
    SetXCollisionFromOrigin(100)
    SetYCollisionFromOrigin(250)
    sprite('bl402_10', 3)
    XImpulseAcceleration(50)
    sprite('bl402_12', 1)
    sprite('bl402_13', 1)
    JumpEffects(100, 1)
    sprite('bl402_14', 1)
    EnableCollision(0)
    CommonSE('003_swing_grap_0_2')
    sprite('bl402_14', 2)
    physicsXImpulse(2500)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    sprite('bl402_14', 3)
    RefreshMultihit()
    sprite('bl402_14', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(-11000)
    AirPushbackY(35000)
    CHAirPushbackX(-11000)
    CHAirPushbackY(35000)
    sprite('bl402_15', 5)
    sprite('bl402_16', 32767)
    label(2)
    sprite('bl402_17', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl402_18', 3)
    sprite('bl402_19', 6)
    sprite('bl402_20', 8)
    if SLOT_2:
        enterState('UltimateAssaultExe')


@State
def UltimateAssaultExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(3)
        Damage(800)
        MinimumDamage(15)
        AttackP2(100)
        AirPushbackX(5000)
        AirPushbackY(31250)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(40)
        Hitstop(6)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        EndMomentum(1)
        EnableCollision(0)
        ForceFaceSprite()
        SetActionMark(0)

        def upon_STATE_END():
            XImpulseAcceleration(25)
            YAccel(25)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl212_00', 2)
    sprite('bl212_01', 2)
    sprite('bl212_02', 2)
    AddX(30000)
    sprite('bl212_03', 2)
    sprite('bl212_04', 2)
    Voiceline('bl251')
    sprite('bl212_05', 2)
    sprite('bl212_06', 2)
    AddX(60000)
    physicsXImpulse(70000)
    physicsYImpulse(31000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    sprite('bl212_07', 3)
    XImpulseAcceleration(25)
    sprite('bl212_08', 3)
    sprite('bl213_04', 1)
    XImpulseAcceleration(50)
    ForceFaceSprite()

    def upon_OPPONENT_HIT():
        SetActionMark(1)
    sprite('bl213_05', 1)
    sprite('bl213_06', 4)
    sprite('bl213_07', 5)
    sprite('bl213_07', 3)
    setGravity(2500)
    sprite('bl213_08', 1)
    CommonSE('004_swing_grap_1_2')
    sprite('bl213_09', 2)
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(-100000)
    GroundBounce(1)
    BouncePercentage(20)
    uponSendToLabel(LANDING, 1)
    label(0)
    sprite('bl213_10', 3)
    sprite('bl213_11', 3)
    gotoLabel(0)
    label(1)
    sprite('bl213_12', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    sprite('bl213_13', 3)
    sprite('bl213_14', 3)
    sprite('bl213_15', 5)
    sprite('bl213_16', 1)
    if SLOT_2:
        clearUponHandler(OPPONENT_HIT)
        enterState('UltimateAssaultFinish')
    loopRest()
    sprite('bl213_16', 5)
    ExitState()


@State
def UltimateAssaultFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(3)
        Damage(300)
        MinimumDamage(15)
        AttackP2(100)
        DefeatOpponentBehavior(1)
        Hitstop(2)
        UseFireHitspark(1)
        AirPushbackX(5000)
        AirPushbackY(18750)
        CHStateIfCHStart(3)
        if CharacterIDCheck('tg'):
            if not SLOT_140:
                SLOT_53 = 1
        if SLOT_86:
            SLOT_53 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl213_16', 5)
    sprite('bl430_08', 6)
    EnableRapidCancel(0)
    ForceFaceSprite()
    EnableCollision(1)
    DistortionSettings(32, -1, 0)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CreateObject('430_handaura2', 0)
    sprite('bl430_09', 6)
    sprite('bl430_10', 20)
    if SLOT_53:
        Voiceline('bl252')
    sprite('bl430_11', 3)
    if not SLOT_53:
        Voiceline('bl252')
    DespawnEAEffect('430_handaura2')
    DamageEffect(5, '')
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_12', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_13', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_14', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_15', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_16', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_17', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_18', 1)
    if SLOT_63:
        sendToLabel(100)
    sprite('bl430_18', 10)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    AttackLevel_(5)
    Damage(1200)
    AirPushbackX(2000)
    AirPushbackY(50000)
    YImpulseBeforeWallbounce(2100)
    AirUntechableTime(90)
    GroundBounceReset()
    HardKnockdown(1)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    ScreenShake(30000, 30000)
    CreateObject('430_mazzlelast', 0)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('bl430_19', 6)
    CreateParticle('blef_433_smkaf', 0)
    sprite('bl430_20', 6)
    sprite('bl430_21', 6)
    sprite('bl430_22', 6)
    sprite('bl430_23', 6)
    sprite('bl430_24', 6)
    sprite('bl430_25', 6)
    sprite('bl430_26', 6)
    EnableRapidCancel(1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    sprite('bl430_27', 11)
    sprite('bl430_28', 6)
    ExitState()
    label(100)
    sprite('bl430_18', 8)
    RefreshMultihit()
    AirPushbackX(1000)
    AirPushbackY(25000)
    YImpulseBeforeWallbounce(1000)
    AirUntechableTime(90)
    GroundBounceReset()
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    ScreenShake(30000, 30000)
    CreateObject('430_mazzlelast', 0)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('bl430_19', 4)
    CreateParticle('blef_433_smkaf', 0)
    sprite('bl430_20', 4)
    sprite('bl430_21', 4)
    sprite('bl430_22', 4)
    sprite('bl430_23', 4)
    enterState('UltimateAssaultOverDrive')
    ExitState()


@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(400)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        Hitstop(3)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(20000)
        CHAirPushbackX(5000)
        CHAirPushbackY(20000)
        EndMomentum(1)
        StayAfterMovement(1, 0)
        AttackDirection(2)
        StarterRating(2)
        OppPositionOnHit(1, 25000, 70000)

        def upon_STATE_END():
            BlendMode_Off()
            ConstantAlphaModifier(0)
            AlphaValue(255)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            SetActionMark(1)
        SLOT_63 = 1
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl430_00', 3)
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', 100)
    setInvincible(1)
    sprite('bl430_01', 3)
    Voiceline('bl250')
    sprite('bl430_02', 3)
    CreateObject('430_handaura', 0)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_02', 3)
    sprite('bl430_03', 3)
    sprite('bl430_04', 3)
    sprite('bl430_05', 3)
    DespawnEAEffect('430_handaura')
    setInvincible(0)
    sprite('bl430_06', 3)
    sprite('bl404_00', 2)
    AirDashEffects(1)
    sprite('bl404_01', 2)
    physicsXImpulse(35000)
    sprite('bl404_02', 2)
    sprite('bl404_03', 2)

    def upon_EVERY_FRAME():
        if SLOT_19 < 300000:
            sendToLabel(1)
    sprite('bl404_04', 2)
    XImpulseAcceleration(110)
    sprite('bl404_05', 2)
    XImpulseAcceleration(110)
    sprite('bl404_06', 2)
    XImpulseAcceleration(110)
    sprite('bl404_07', 2)
    DashEffects(100, 1, 1)
    sprite('bl404_08', 2)
    label(1)
    sprite('bl430_07', 4)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(LANDING, 2)
    XImpulseAcceleration(25)
    SetXCollisionFromOrigin(100)
    SetYCollisionFromOrigin(250)
    sprite('bl402_10', 3)
    XImpulseAcceleration(50)
    sprite('bl402_12', 1)
    sprite('bl402_13', 1)
    JumpEffects(100, 1)
    sprite('bl402_14', 1)
    EnableCollision(0)
    CommonSE('003_swing_grap_0_2')
    sprite('bl402_14', 2)
    physicsXImpulse(2500)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    sprite('bl402_14', 3)
    RefreshMultihit()
    sprite('bl402_14', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(-11000)
    AirPushbackY(35000)
    CHAirPushbackX(-11000)
    CHAirPushbackY(35000)
    sprite('bl402_15', 5)
    sprite('bl402_16', 32767)
    label(2)
    sprite('bl402_17', 2)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl402_18', 3)
    sprite('bl402_19', 6)
    sprite('bl402_20', 8)
    if SLOT_2:
        enterState('UltimateAssaultExeOD')


@State
def UltimateAssaultExeOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(3)
        Damage(800)
        MinimumDamage(15)
        AttackP2(100)
        AirPushbackX(5000)
        AirPushbackY(31250)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(40)
        Hitstop(6)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        EndMomentum(1)
        EnableCollision(0)
        ForceFaceSprite()
        SetActionMark(0)

        def upon_STATE_END():
            XImpulseAcceleration(25)
            YAccel(25)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl212_00', 2)
    sprite('bl212_01', 2)
    sprite('bl212_02', 2)
    AddX(30000)
    sprite('bl212_03', 2)
    sprite('bl212_04', 2)
    Voiceline('bl251')
    sprite('bl212_05', 2)
    sprite('bl212_06', 2)
    AddX(60000)
    physicsXImpulse(70000)
    physicsYImpulse(31000)
    EndYPhysicsImpulse()
    CommonSE('006_swing_blade_2')
    sprite('bl212_07', 3)
    XImpulseAcceleration(25)
    sprite('bl212_08', 3)
    sprite('bl213_04', 1)
    XImpulseAcceleration(50)
    ForceFaceSprite()

    def upon_OPPONENT_HIT():
        SetActionMark(1)
    sprite('bl213_05', 1)
    sprite('bl213_06', 4)
    sprite('bl213_07', 5)
    sprite('bl213_07', 3)
    setGravity(2500)
    sprite('bl213_08', 1)
    CommonSE('004_swing_grap_1_2')
    sprite('bl213_09', 2)
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(-100000)
    GroundBounce(1)
    BouncePercentage(20)
    uponSendToLabel(LANDING, 1)
    label(0)
    sprite('bl213_10', 3)
    sprite('bl213_11', 3)
    gotoLabel(0)
    label(1)
    sprite('bl213_12', 3)
    EndMomentum(1)
    clearUponHandler(LANDING)
    sprite('bl213_13', 3)
    sprite('bl213_14', 3)
    sprite('bl213_15', 5)
    sprite('bl213_16', 1)
    if SLOT_2:
        clearUponHandler(OPPONENT_HIT)
        enterState('UltimateAssaultFinishOD')
    loopRest()
    sprite('bl213_16', 5)
    ExitState()


@State
def UltimateAssaultFinishOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(3)
        Damage(300)
        MinimumDamage(15)
        AttackP2(100)
        DefeatOpponentBehavior(1)
        Hitstop(2)
        UseFireHitspark(1)
        AirPushbackX(5000)
        AirPushbackY(18750)
        CHStateIfCHStart(3)
        if CharacterIDCheck('tg'):
            if not SLOT_140:
                SLOT_53 = 1
        if SLOT_86:
            SLOT_53 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl213_16', 5)
    sprite('bl430_08', 6)
    EnableRapidCancel(0)
    ForceFaceSprite()
    EnableCollision(1)
    DistortionSettings(32, -1, 0)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CreateObject('430_handaura2', 0)
    sprite('bl430_09', 6)
    sprite('bl430_10', 20)
    if SLOT_53:
        Voiceline('bl252')
    sprite('bl430_11', 3)
    if not SLOT_53:
        Voiceline('bl252')
    DespawnEAEffect('430_handaura2')
    DamageEffect(5, '')
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_12', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_13', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_14', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_15', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_16', 3)
    RefreshMultihit()
    CreateObject('430_mazzle2', 0)
    sprite('bl430_17', 3)
    RefreshMultihit()
    CreateObject('430_mazzle', 0)
    sprite('bl430_18', 1)
    if SLOT_63:
        sendToLabel(100)
    sprite('bl430_18', 10)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    AttackLevel_(5)
    Damage(1200)
    AirPushbackX(2000)
    AirPushbackY(50000)
    YImpulseBeforeWallbounce(2100)
    AirUntechableTime(90)
    GroundBounceReset()
    HardKnockdown(1)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    ScreenShake(30000, 30000)
    CreateObject('430_mazzlelast', 0)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('bl430_19', 6)
    CreateParticle('blef_433_smkaf', 0)
    sprite('bl430_20', 6)
    sprite('bl430_21', 6)
    sprite('bl430_22', 6)
    sprite('bl430_23', 6)
    sprite('bl430_24', 6)
    sprite('bl430_25', 6)
    sprite('bl430_26', 6)
    EnableRapidCancel(1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    sprite('bl430_27', 11)
    sprite('bl430_28', 6)
    ExitState()
    label(100)
    sprite('bl430_18', 8)
    RefreshMultihit()
    AirPushbackX(1000)
    AirPushbackY(25000)
    YImpulseBeforeWallbounce(1000)
    AirUntechableTime(90)
    GroundBounceReset()
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    ScreenShake(30000, 30000)
    CreateObject('430_mazzlelast', 0)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('bl430_19', 4)
    CreateParticle('blef_433_smkaf', 0)
    sprite('bl430_20', 4)
    sprite('bl430_21', 4)
    sprite('bl430_22', 4)
    sprite('bl430_23', 4)
    enterState('UltimateAssaultOverDrive')
    ExitState()


@State
def UltimateAssaultOverDrive():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(550)
        AttackType(4)
        MinimumDamage(15)
        AttackP2(100)
        Hitstop(3)
        UseFireHitspark(1)
        AirPushbackX(50000)
        AirPushbackY(30000)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirUntechableTime(60)
        HardKnockdown(30)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        EnableRapidCancel(0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('bl405_00', 4)
    AddX(40000)
    sprite('bl405_01', 4)
    sprite('bl405_02', 4)
    sprite('bl405_03', 3)
    E0EAEffect('GuardCrushWind', 65535)
    CreateObject('shot_charge', 0)
    PrivateSE('blse_03')
    ScreenShake(0, 10000)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    Voiceline('bl253')
    sprite('bl405_03', 3)
    ScreenShake(0, 20000)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl405_03', 3)
    ScreenShake(0, 30000)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl431_26', 1)
    DespawnEAEffect('shot_charge')
    CreateObject('431_bigmazzleShockmatome', 0)
    AddX(-100000)
    CameraControlEnable(0)
    sprite('bl431_26', 1)
    RefreshMultihit()
    sprite('bl431_26', 1)
    RefreshMultihit()
    sprite('bl431_26', 1)
    RefreshMultihit()
    sprite('bl431_26', 10)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    Hitstop(20)
    ScreenShake(100000, 100000)
    AddInertia(-15000)
    CommonSE('025_cleanhit_grap')
    CommonSE('016_explode_2')
    sprite('bl431_27', 3)
    sprite('bl431_28', 3)
    sprite('bl431_29', 6)
    CameraNoScreenCollision(0)
    EnableRapidCancel(1)
    sprite('bl431_30', 6)
    sprite('bl431_31', 6)
    sprite('bl431_32', 6)
    sprite('bl431_33', 6)
    sprite('bl431_34', 15)
    sprite('bl431_35', 6)


@State
def UltimateThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateThrowExe', 3, 0, 0)
        AttackP1(80)
        RangeCheck(150000)
        DistanceCheck(300000, 1, -1, -1)
        SetZLine(0, 50)
        setInvincible(1)
        SLOT_63 = 0
    sprite('bl431_00', 4)
    sprite('bl431_01', 4)
    DistortionSettings(34, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', 100)
    sprite('bl431_02', 30)
    sprite('bl431_03', 1)
    CommonSE('006_swing_blade_2')
    sprite('bl431_03', 1)
    physicsXImpulse(40000)
    DashEffects(100, 1, 1)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl310_04', 6)
    XImpulseAcceleration(50)
    setInvincible(0)
    sprite('bl310_05', 10)
    XImpulseAcceleration(0)
    sprite('bl310_05', 10)
    Voiceline('bl155')
    sprite('bl310_06', 8)
    sprite('bl310_07', 8)


@State
def UltimateThrowOD():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateThrowExe', 3, 0, 0)
        AttackP1(80)
        RangeCheck(150000)
        DistanceCheck(300000, 1, -1, -1)
        SetZLine(0, 50)
        setInvincible(1)
        SLOT_63 = 1
        AttackType(4)
    sprite('bl431_00', 4)
    sprite('bl431_01', 4)
    DistortionSettings(34, -1, 0)
    HeatChange(-5000)
    CreateObject('EMB', 100)
    sprite('bl431_02', 30)
    sprite('bl431_03', 1)
    CommonSE('006_swing_blade_2')
    sprite('bl431_03', 1)
    physicsXImpulse(40000)
    DashEffects(100, 1, 1)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl431_03', 1)
    XImpulseAcceleration(50)
    sprite('bl310_04', 6)
    XImpulseAcceleration(50)
    setInvincible(0)
    sprite('bl310_05', 10)
    XImpulseAcceleration(0)
    sprite('bl310_05', 10)
    Voiceline('bl155')
    sprite('bl310_06', 8)
    sprite('bl310_07', 8)


@State
def UltimateThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(3)
        Damage(0)
        Hitstop(1)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        setInvincible(1)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            if SLOT_2:
                if SLOT_XDistanceFromFowardCorner < 250000:
                    clearUponHandler(OPPONENT_HIT)
                    sendToLabel(1)
        SLOT_52 = 1
    sprite('bl431_03', 1)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('bl431_04', 3)
    Voiceline('bl254')
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl431_05', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl431_06', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl431_07', 8)
    RefreshMultihit()
    physicsXImpulse(-5000)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    sprite('bl431_08', 8)
    XImpulseAcceleration(50)
    sprite('bl431_09', 8)
    XImpulseAcceleration(50)
    sprite('bl431_10', 5)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(-200000)
    AirPushbackX(30000)
    HardKnockdown(10)
    SetActionMark(1)
    physicsXImpulse(75000)
    physicsYImpulse(-20000)
    sprite('bl431_11', 4)
    OppPositionOnHit(1, 300000, 0)
    RefreshMultihit()
    physicsYImpulse(0)
    AirPushbackY(-5000)
    sprite('bl431_12', 4)
    RefreshMultihit()
    label(0)
    sprite('bl431_11', 4)
    CreateParticle('blef_433smoke_smk03', -1)
    RefreshMultihit()
    sprite('bl431_12', 4)
    CreateParticle('blef_433smoke_smk03', -1)
    RefreshMultihit()
    gotoLabel(0)
    label(1)
    sprite('bl431_11', 3)
    RefreshMultihit()
    AirPushbackX(20000)
    AirPushbackY(40000)
    AirHitstunAnimation(19)
    GroundedHitstunAnimation(19)
    Wallbounce(1)
    NonCornerWallbounce(1)
    AirHitstunAfterWallbounce(40)
    WallbounceReboundTime(5)
    sprite('bl431_13', 6)
    physicsXImpulse(-15000)
    sprite('bl431_14', 6)
    XImpulseAcceleration(50)
    sprite('bl431_15', 10)
    XImpulseAcceleration(50)
    sprite('bl431_16', 5)
    XImpulseAcceleration(50)
    sprite('bl431_16', 5)
    XImpulseAcceleration(0)
    sprite('keep', 1)
    enterState('UltimateThrow2nd')


@State
def UltimateThrow2nd():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateThrow2ndExe', 3, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        EndMomentum(1)
        setInvincible(1)
        SLOT_52 = 1
    sprite('bl431_16', 1)
    sprite('bl431_17', 3)


@State
def UltimateThrow2ndExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(4)
        Damage(320)
        AirPushbackX(30000)
        AirPushbackY(15000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Wallbounce(1)
        NonCornerWallbounce(1)
        DefeatOpponentBehavior(1)
        AirHitstunAfterWallbounce(40)
        WallbounceReboundTime(5)
        EnemyHitstopAddition(0, 25, 25)
        setInvincible(1)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            ScreenShake(10000, 5000)
        SLOT_52 = 1
        if CharacterIDCheck('tg'):
            if not SLOT_140:
                SLOT_53 = 1
        if SLOT_86:
            SLOT_53 = 0
    sprite('bl431_17', 3)
    if SLOT_53:
        Voiceline('bl255')
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    label(0)
    sprite('bl431_18', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('bl431_19', 2)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('bl431_20', 3)
    RefreshMultihit()
    sprite('bl431_21', 5)
    sprite('bl431_22', 5)
    sprite('keep', 1)
    AddActionMark(1)
    if SLOT_2 >= 2:
        sendToLabel(1)
    else:
        sendToLabel(0)
    label(1)
    clearUponHandler(OPPONENT_HIT)
    sprite('bl431_22', 3)
    if not SLOT_53:
        Voiceline('bl255')
    sprite('bl431_23', 3)
    sprite('bl431_24', 3)
    CreateObject('shot_charge', 0)

    def RunOnObject_1():
        SetScaleSpeed(80)
    PrivateSE('blse_03')
    sprite('bl431_25', 3)
    sprite('bl431_24', 3)
    sprite('bl431_25', 3)
    sprite('bl431_24', 3)
    sprite('bl431_25', 3)
    sprite('bl431_24', 3)
    sprite('bl431_25', 3)
    sprite('bl431_24', 3)
    BeginBuffer('UltimateAddAttack')
    sprite('bl431_25', 3)
    sprite('bl431_24', 3)
    sprite('bl431_25', 3)
    sprite('bl431_26', 3)
    DespawnEAEffect('shot_charge')
    CreateObject('431_bigmazzleShockmatome', 0)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1420)
    Hitstop(20)
    AttackP2(60)
    UseFireHitspark(1)
    AirPushbackX(10000)
    AirPushbackY(6250)
    AirHitstunAnimation(19)
    GroundedHitstunAnimation(19)
    Wallbounce(1)
    NonCornerWallbounce(1)
    HardKnockdown(25)
    AirHitstunAfterWallbounce(40)
    WallbounceReboundTime(5)
    EnemyHitstopAddition(0, 0, 2)
    DefeatOpponentBehavior(0)
    PrivateSE('blse_06')
    ScreenShake(25000, 25000)
    AddInertia(-15000)
    sprite('bl431_27', 3)
    sprite('bl431_28', 3)
    sprite('bl431_27', 3)
    sprite('bl431_28', 3)
    sprite('bl431_27', 3)
    sprite('bl431_28', 3)
    BufferedOrPressedGoto('UltimateAddAttack')
    sprite('bl431_29', 6)
    sprite('bl431_30', 6)
    DisallowGoto('UltimateAddAttack')
    sprite('bl431_31', 6)
    sprite('bl431_32', 6)
    sprite('bl431_33', 6)
    sprite('bl431_34', 15)
    sprite('bl431_35', 6)


@State
def UltimateAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateAddAttackExe', 3, 1, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        EndMomentum(1)
        callSubroutine('AdditionalThrowInit')
    sprite('bl431_18', 20)
    DistortionSettings(20, -1, 0)
    sprite('bl432_00', 3)


@State
def UltimateAddAttackExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(4)
        Damage(250)
        AirPushbackX(4000)
        AirPushbackY(70000)
        AirUntechableTime(100)
        BonusProration(125)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        FlipOnHit(1)
        DefeatOpponentBehavior(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        EnableRapidCancel(0)
        setInvincible(1)
        if SLOT_5 == 2:
            BonusProration(175)
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
        callSubroutine('HeatUpActionInit')
        if CharacterIDCheck('tg'):
            if not SLOT_140:
                SLOT_53 = 1
        if SLOT_86:
            SLOT_53 = 0
    sprite('bl432_00', 6)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('bl432_01', 8)
    if SLOT_53:
        Voiceline('bl256')
    StartMultihit()
    physicsXImpulse(-2000)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl404_20', 3)
    BeginBuffer('UltimateFinishAttack')
    Flip()
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    physicsXImpulse(20000)
    AirDashEffects(1)
    CreateParticle('blef_433smoke_smk03', -1)
    sprite('bl404_21', 3)
    XImpulseAcceleration(200)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl404_20', 3)
    XImpulseAcceleration(200)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateParticle('blef_433smoke_smk03', -1)
    sprite('bl404_21', 3)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_02', 6)
    if not SLOT_53:
        Voiceline('bl256')
    XImpulseAcceleration(50)
    Flip()
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_03', 6)
    XImpulseAcceleration(50)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_04', 8)
    XImpulseAcceleration(50)
    OppThrowAnimation(3, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_05', 3)
    XImpulseAcceleration(0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_06', 1)
    CreateObject('431_bigmazzleShockmatomeDown', 0)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl432_06', 3)
    ScreenShake(0, 50000)
    sprite('bl432_07', 10)
    sprite('bl432_08', 6)
    sprite('bl432_09', 6)
    AddX(-175000)
    sprite('bl432_10', 6)
    BufferedOrPressedGoto('UltimateFinishAttack')


@State
def UltimateFinishAttack():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        AttackLevel_(5)
        Damage(100)
        Hitstop(3)
        UseFireHitspark(1)
        AirPushbackX(5000)
        AirPushbackY(-50000)
        AirUntechableTime(100)
        HardKnockdown(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        EnableRapidCancel(0)
        setInvincible(1)
        CameraControlEnable(1)
        callSubroutine('HeatUpActionInit')
        AttackOff()
        if SLOT_63:
            AttackType(4)
    sprite('bl433_00', 3)
    Flip()
    DistortionSettings(26, -1, 0)
    sprite('bl433_01', 20)
    Voiceline('bl257')

    def RunOnObject_22():
        physicsXImpulse(10)
        physicsYImpulse(5000)
        setGravity(5)
    sprite('bl433_02', 3)
    sprite('bl433_02', 8)
    Visibility(1)
    CameraControlEnable(0)
    CameraLookAtEnemy(1)
    CameraNoScreenCollision(1)
    CameraNoCeiling(1)
    sprite('bl203_13', 3)
    Visibility(0)
    physicsYImpulse(200000)
    sprite('bl203_14', 3)
    sprite('bl203_13', 3)
    sprite('bl203_14', 3)
    YAccel(25)
    CameraControlEnable(1)
    CameraLookAtEnemy(0)
    sprite('bl203_13', 3)
    sprite('bl433_03', 3)
    TeleportToObject(22)
    AddY(300000)
    physicsXImpulse(0)
    physicsYImpulse(10000)
    setGravity(300)
    sprite('bl433_04', 3)
    sprite('bl433_05', 3)
    sprite('bl433_04', 3)
    sprite('bl433_05', 3)
    sprite('bl433_04', 3)
    sprite('bl433_05', 3)
    sprite('bl433_06', 3)
    Voiceline('bl258')
    CreateObject('431_bigmazzleShockmatomeUp', -1)
    sprite('bl433_07', 1)
    ScreenShake(40000, 40000)
    PrivateSE('blse_07')
    RefreshMultihit()
    if not SLOT_63:
        sendToLabel(100)
    sprite('bl433_07', 1)
    Hitstop(2)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    label(100)
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    sprite('bl433_07', 1)
    RefreshMultihit()
    Damage(1910)
    Hitstop(20)
    ScreenShake(50000, 50000)
    CommonSE('025_cleanhit_grap')
    CommonSE('016_explode_2')
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    sprite('bl433_08', 5)
    CameraControlEnable(0)
    CameraLookAtEnemy(1)
    sprite('bl433_09', 5)
    sprite('bl433_10', 5)
    sprite('bl433_11', 5)
    uponSendToLabel(LANDING, 1)
    sprite('bl020_06', 4)
    Flip()
    label(0)
    sprite('bl020_07', 4)
    sprite('bl020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bl024_00', 3)
    CameraLookAtEnemy(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('bl024_01', 6)
    sprite('bl024_02', 6)
    sprite('bl024_03', 6)
    sprite('bl024_04', 3)


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
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(0)
        MoveAttributes(0, 1, 0, 0, 0)
        OppPositionOnHit(1, 200000, 0)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('AstralHeatCatch')
        EnterStateIfEventID(12, 'AstralHeatCatch')
        IgnoreScreenfreeze(1)
        EndMomentum(1)
        setInvincible(1)
    sprite('bl450_00', 3)
    sprite('bl450_01', 3)
    Voiceline('bl290')
    CreateObject('450_gandredfireroop', 0)
    DistortionSettings(60, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_BL_AH', -1)
    sprite('bl450_02', 3)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    CreateObject('450_tamesmokeroop', -1)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_02', 4)
    sprite('bl450_01', 4)
    sprite('bl450_03', 4)
    TriggerUponForState('450_tamesmokeroop', 32)
    sprite('bl450_04', 5)
    TriggerUponForState('450_gandredfireroop', 32)
    sprite('bl450_05', 5)
    sprite('bl450_05', 1)
    CommonSE('004_swing_grap_1_2')
    sprite('bl450_06', 3)
    CreateObject('450_Zanzo', -1)
    sprite('bl450_07', 15)
    setInvincible(0)
    sprite('bl450_42', 8)
    sprite('bl450_43', 8)


@State
def AstralHeatCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AstralHeatShot', 5, 0, 0)
        setInvincible(1)
        DamageFromStateOnly('AstralHeatShot')
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        AttackLevel_(4)
        Damage(0)
        PassByArmor(1)
        AstralHeatCleanup(1, 1)
        HitAnywhere(1)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SetZVal(-500)
        EnableRapidCancel(0)
    sprite('bl450_06', 6)
    StartMultihit()
    sprite('bl450_07', 40)
    sprite('bl450_08', 6)
    PlayPlayAstralBGM(1)
    HUDVisibillity(1)
    sprite('bl450_09', 6)
    sprite('bl450_10', 6)
    sprite('bl450_11', 6)


@State
def AstralHeatShot():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(0)
        MinimumDamage(100)
        DefeatOpponentBehavior(1)
        Hitstop(3)
        HardKnockdown(60)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        EnemyHitstopAddition(0, 120, 0)
        OppPositionOnHit(1, -45000, 85000)
        EnableCollision(0)
        UseFireHitspark(1)
        IgnoreComboTime(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('bl450_11', 5)
    Voiceline('bl291')
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_12', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_13', 5)
    CreateObject('450_ryuhai', -1)
    EnableCollision(1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl450_14', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_15', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_16', 5)
    PrivateSE('blse_06')
    ParticleColorFromPalette(49, 49, 49)
    CallCustomizableParticle('blef_450hahen_parts1', 0)
    CreateObject('450_bigmazzle00', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_17', 1)
    Damage(1000)
    ScreenShake(10000, 10000)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_18', 3)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_19', 10)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_13', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl450_14', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_15', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_16', 5)
    PrivateSE('blse_06')
    ParticleColorFromPalette(49, 49, 49)
    CallCustomizableParticle('blef_450hahen_parts1', 0)
    CreateObject('450_bigmazzle01', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_17', 2)
    RefreshMultihit()
    Damage(1500)
    ScreenShake(25000, 25000)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_18', 3)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_19', 10)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_13', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('bl450_14', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_15', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_16', 5)
    PrivateSE('blse_06')
    ParticleColorFromPalette(49, 49, 49)
    CallCustomizableParticle('blef_450hahen_parts1', 0)
    CreateObject('450_bigmazzle02', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_17', 2)
    Damage(3500)
    RefreshMultihit()
    ScreenShake(50000, 50000)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_18', 3)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_19', 20)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_19', 3)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    TriggerUponForState('450_ryuhai', 32)
    enterState('AstralHeatCatch2')


@State
def AstralHeatCatch2():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AstralHeatMountShot', 5, 1, 0)
        setInvincible(1)
        DamageFromStateOnly('AstralHeatMountShot')
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        AttackLevel_(3)
        Damage(0)
        PassByArmor(1)
        OppPositionOnHit(1, -150000, 100000)
        IgnoreComboTime(1)
        DefeatOpponentBehavior(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('bl450_19', 21)
    CallCustomizableParticle('blef_450atk1_sub', 1)
    sprite('bl450_20', 6)
    CallCustomizableParticle('blef_450atk1_sub', 1)


@State
def AstralHeatMountShot():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(0)
        IgnoreComboTime(1)
        Hitstop(0)
        DefeatOpponentBehavior(1)
        AirPushbackX(1000)
        AirPushbackY(-50000)
        HardKnockdown(150)
        PassByArmor(1)
        OppPositionOnHit(1, 50000, 100000)
        EnableCollision(0)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('bl450_20', 6)
    CreateObject('450nageBG', -1)
    Voiceline('bl292')
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_21', 6)
    OppThrowAnimation(2, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_22', 1)
    StartMultihit()
    OppThrowAnimation(4, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl450_22', 20)
    sprite('bl450_23', 6)
    AddX(50000)
    sprite('bl450_24', 6)
    AddX(30000)
    sprite('bl450_25', 6)
    AddX(30000)
    sprite('bl450_26ex04', 5)
    PrivateSE('blse_03')
    PrivateSE('blse_10')
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    CameraForAstralHeat(210, 140)
    ScreenShake(1000, 1000)
    CreateObject('450_lastTame', 0)
    sprite('bl450_27ex04', 5)
    ScreenShake(1000, 2000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 3000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 4000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 3000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 4000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 3000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 4000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 3000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 4000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 5000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 6000)
    sprite('bl450_26', 5)
    ScreenShake(1000, 7000)
    sprite('bl450_27', 5)
    ScreenShake(1000, 8000)
    sprite('bl450_26ex00', 5)
    ScreenShake(1000, 9000)
    sprite('bl450_27ex00', 5)
    ScreenShake(1000, 10000)
    sprite('bl450_26ex01', 5)
    ScreenShake(1000, 11000)
    sprite('bl450_27ex01', 5)
    ScreenShake(1000, 12000)
    sprite('bl450_26ex02', 5)
    ScreenShake(1000, 13000)
    sprite('bl450_27ex02', 5)
    ScreenShake(1000, 14000)
    sprite('bl450_26ex03', 5)
    ScreenShake(1000, 15000)
    sprite('bl450_27ex03', 2)
    sprite('bl450_27ex03', 1)
    TriggerUponForState('450_lastTame', 32)
    sprite('bl450_28', 6)
    PrivateSE('blse_07')
    CommonSE('016_explode_2')
    StartMultihit()
    ScreenShake(50000, 50000)
    CreateObject('450_lastAtk00', 0)
    CreateObject('450_rock', -1)
    TriggerUponForState('450nageBG', 32)
    sprite('bl450_29', 4)
    sprite('bl450_30', 3)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(5000)
    MinimumDamage(100)
    Hitstop(15)
    DefeatOpponentBehavior(3)
    UseFireHitspark(1)
    IgnoreComboTime(1)
    OppPositionOnHit(1, 0, 0)
    AirPushbackX(1000)
    AirPushbackY(-10000)
    AttackDirection(2)
    CreateParticle('blef_450flash_black', -1)
    SetBackground(3)
    sprite('bl450_29', 3)
    sprite('bl450_30', 3)
    sprite('bl450_29', 4)
    sprite('bl450_30', 4)
    sprite('bl450_29', 4)
    sprite('bl450_30', 4)
    sprite('bl450_29', 5)
    sprite('bl450_30', 5)
    sprite('bl450_29', 5)
    sprite('bl450_30', 5)
    sprite('bl450_29', 6)
    sprite('bl450_30', 6)
    sprite('bl450_29', 6)
    sprite('bl450_30', 6)
    sprite('bl450_30', 3)
    sprite('bl450_29', 3)
    sprite('bl450_30', 3)
    sprite('bl450_29', 4)
    sprite('bl450_30', 4)
    sprite('bl450_29', 4)
    sprite('bl450_30', 4)

    def RunOnObject_22():
        ColorForTransition(4282137660)
    CreateParticle('blef_450smoke01', -1)
    sprite('bl450_31', 6)
    sprite('bl450_32', 6)
    sprite('bl450_33', 6)
    sprite('bl450_34', 6)
    sprite('bl450_35', 6)
    sprite('bl450_36', 6)
    sprite('bl450_37', 6)
    CameraFast(1)
    CameraWinnerControlStop(1)
    CameraControlInfinity(1)
    sprite('bl450_38', 6)
    EnableAfterimage(0)
    WinAction()
    Voiceline('bl293')
    sprite('bl450_39', 20)
    sprite('bl450_40', 6)
    sprite('bl450_41', 6)
    WinAction()
    DemoTimer(120)
    label(100)
    sprite('bl450_38', 6)
    sprite('bl450_39', 40)
    sprite('bl450_40', 8)
    sprite('bl450_41', 8)
    gotoLabel(100)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('bl054')
    sprite('bl900_00', 32767)
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
    sprite('bl901_00', 50)
    physicsYImpulse(-150)
    sprite('bl901_00', 50)
    physicsYImpulse(150)
    Voiceline('bl055')
    label(0)
    sprite('bl901_00', 50)
    physicsYImpulse(-150)
    sprite('bl901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 150000, 100000)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        DamageFromStateOnly('BurstDDCatch')

        def upon_OPPONENT_HIT():
            enterState('BurstDDCatch')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('bl430_08ex01', 5)
    E0EAEffect('BurstDDeff', 103)
    sprite('bl430_09ex01', 5)
    Voiceline('bl280')
    sprite('bl430_10ex01', 5)
    sprite('bl430_11ex01', 2)
    sprite('bl430_12ex01', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('bl440_00', 3)
    sprite('bl440_01', 5)
    setInvincible(0)
    sprite('bl440_02', 5)
    sprite('bl440_01', 5)
    sprite('bl440_02', 5)
    sprite('bl440_01', 5)
    sprite('bl440_02', 5)
    sprite('bl403_00ex01', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 150000, 100000)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        DamageFromStateOnly('BurstDDCatch')

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
    sprite('bl430_08ex01', 2)
    E0EAEffect('BurstDDeff', 103)
    sprite('bl430_09ex01', 2)
    Voiceline('bl280')
    sprite('bl430_10ex01', 2)
    sprite('bl430_11ex01', 1)
    sprite('bl430_12ex01', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('bl440_00', 3)
    sprite('bl440_01', 5)
    setInvincible(0)
    sprite('bl440_02', 5)
    sprite('bl440_01', 5)
    sprite('bl440_02', 5)
    sprite('bl440_01', 5)
    sprite('bl440_02', 5)
    sprite('bl403_00ex01', 4)


@State
def BurstDDCatch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BurstDDAdd', 3, 1, 0)
        SetZLine(1, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SameMoveProration(-1)
        AttackP2(100)
        DamageFromStateOnly('BurstDDAdd')
        CHStateIfCHStart(3)
        MinimumDamage(10)
        setInvincible(1)
        Unknown2066(1)
    sprite('bl440_00', 8)
    RefreshMultihit()
    sprite('bl440_01', 8)
    sprite('bl440_02', 8)
    sprite('bl403_00ex01', 8)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        Damage(300)
        AirPushbackX(1200)
        AirPushbackY(-40000)
        MinimumDamage(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HardKnockdown(30)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        MinimumDamage(10)
        SetBackground(1)
        DamageFromStateOnly('BurstDDAdd')
    sprite('bl440_00', 3)
    StartMultihit()
    sprite('bl403_03ex01', 6)
    OppThrowAnimation(6, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl403_04ex01', 1)
    Voiceline('bl281')
    StartMultihit()
    OppThrowAnimation(29, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('bl403_04ex01', 2)
    OppPositionOnHit(1, 300000, 0)
    sprite('bl403_05ex01', 2)
    OppPositionOnHit(0, 0, 0)
    sprite('bl403_06ex01', 2)
    sprite('bl403_07ex01', 8)
    sprite('bl403_08ex01', 4)
    sprite('bl403_09ex01', 4)
    sprite('keep', 1)
    if SLOT_51:
        sendToLabel(100)
    sprite('bl440_03', 3)
    RefreshMultihit()
    AttackLevel_(2)
    Damage(120)
    OppPositionOnHit(1, 100000, 0)
    AirPushbackX(-40000)
    AirPushbackY(-5000)
    Hitstop(2)
    HitsparkSize(200)
    AddX(30000)
    physicsXImpulse(-15000)
    sprite('bl440_04', 3)
    RefreshMultihit()
    XImpulseAcceleration(200)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_05', 12)
    XImpulseAcceleration(50)
    sprite('bl440_06', 6)
    XImpulseAcceleration(50)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    DefeatOpponentBehavior(0)
    AirPushbackX(60000)
    AirPushbackY(37000)
    AirUntechableTime(60)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    UseFireHitspark(1)
    HitsparkSize(1000)
    Hitstop(12)
    HardKnockdownReset()
    FlipOnHit(1)
    OppPositionOnHit(1, -200000, 0)
    CreateObject('440_frameEff', -1)
    SetXCollisionFromOrigin(250)
    CommonSE('016_explode_2')
    Voiceline('bl282')
    sprite('bl440_07', 6)
    XImpulseAcceleration(50)
    sprite('bl440_08', 6)
    XImpulseAcceleration(0)
    sprite('bl401_10ex01', 6)
    sprite('bl401_11ex01', 6)
    sprite('bl401_12ex01', 6)
    sprite('bl401_13ex01', 6)
    loopRest()
    ExitState()
    label(100)
    sprite('bl440_03', 3)
    RefreshMultihit()
    AttackLevel_(2)
    Damage(180)
    OppPositionOnHit(1, 100000, 0)
    AirPushbackX(-40000)
    AirPushbackY(-5000)
    Hitstop(2)
    HitsparkSize(200)
    AddX(30000)
    physicsXImpulse(-20000)
    sprite('bl440_04', 3)
    RefreshMultihit()
    XImpulseAcceleration(200)
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_03', 3)
    RefreshMultihit()
    sprite('bl440_04', 3)
    RefreshMultihit()
    ParticleSize(1500)
    CallCustomizableParticle('blef_440_fireroad', -1)
    sprite('bl440_05', 12)
    XImpulseAcceleration(50)
    sprite('bl440_06', 6)
    CreateObject('440_frameEffEX', -1)
    XImpulseAcceleration(50)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2600)
    DefeatOpponentBehavior(0)
    AirPushbackX(60000)
    AirPushbackY(37000)
    AirUntechableTime(60)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    UseFireHitspark(1)
    HitsparkSize(1000)
    Hitstop(12)
    HardKnockdownReset()
    FlipOnHit(1)
    OppPositionOnHit(1, -200000, 0)
    SetXCollisionFromOrigin(250)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    Voiceline('bl282')
    sprite('bl440_07', 6)
    XImpulseAcceleration(50)
    sprite('bl440_08', 6)
    XImpulseAcceleration(0)
    sprite('bl401_10ex01', 6)
    sprite('bl401_11ex01', 6)
    sprite('bl401_12ex01', 6)
    sprite('bl401_13ex01', 6)
    loopRest()
    ExitState()


@Subroutine
def MouthTableInit():
    Unknown18011('bl055', 13921, 13155, 24886, 25397, 24885, 25397, 24885, 
        25397, 24885, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl400', 13921, 13923, 14433, 14435, 12641, 25392, 56, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl401', 14433, 14435, 14433, 12899, 24883, 25398, 24886, 
        25398, 24886, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl404', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl406', 14177, 14179, 14177, 14179, 14177, 14435, 14433, 
        14179, 24886, 25400, 24886, 25400, 24886, 25400, 56, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl407', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
        14435, 24880, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl408', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('bl412', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl413', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl414', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl415', 13921, 13923, 13921, 13923, 13921, 13923, 14433, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl416', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 99, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bl417', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('bl000', 14177, 14179, 14177, 12643, 24888, 25399, 
            24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl400', 13921, 13923, 13921, 13923, 12641, 25392, 54,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl401', 14433, 14435, 14433, 13667, 24882, 12337, 
            14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl404', 14177, 14179, 13921, 13923, 13921, 13923, 
            14433, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl405', 14177, 14179, 14177, 14179, 14689, 14179, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl406', 13921, 13923, 13921, 13923, 14433, 13411, 
            24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
            25398, 24886, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl407', 13411, 12641, 25394, 12854, 14433, 14435, 
            13921, 13923, 13921, 13923, 14433, 14435, 12641, 25392, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('bl408', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl412', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl413', 13921, 13923, 13921, 13923, 13921, 13923, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl414', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('bl415', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bl416', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('bl417', 13921, 13923, 13921, 13923, 13921, 13923, 
            12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('tg'):
            Unknown18011('bl000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('bl400', 12641, 25394, 24888, 25400, 13618, 14433,
                14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('bl401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            if SLOT_140:
                Unknown18011('bl000', 14177, 14179, 14177, 14179, 14177, 
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('bl400', 14177, 14179, 14177, 14179, 14177, 
                    14691, 24880, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('bl401', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tg'):
            Unknown18011('bl510', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13155, 24880, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('bl511', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('bl510', 13921, 12643, 13367, 13921, 13923, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13667, 24882, 25398, 24886, 25398, 24886, 25398,
                    54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
                Unknown18011('bl511', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    14435, 24880, 25398, 24886, 25398, 12342, 13921, 13923,
                    13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('bl546', 13921, 13923, 13921, 13923, 12641, 25400,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 12342, 13921, 13923, 12641, 
                25400, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('bl547', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13667, 
                24882, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('bl548', 13921, 13411, 24885, 25398, 24886, 25398,
                24886, 25397, 24885, 25397, 24888, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('bl549', 14177, 14179, 14177, 14179, 13921, 13923,
                13921, 13155, 24880, 12337, 14435, 12641, 25392, 24888, 
                12337, 14435, 12641, 25392, 24888, 12337, 14435, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('bl548', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 14435, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('bl549', 13921, 13923, 13921, 13923, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2150)
        else:
            gotoLabel(150)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('kk'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(340)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('bl600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('bl600_00', 60)
    Voiceline('bl412')
    sprite('bl600_01', 4)
    sprite('bl600_02', 4)
    sprite('bl600_03', 4)
    sprite('bl600_04', 8)
    sprite('bl600_05', 3)
    sprite('bl600_06', 4)
    CommonSE('003_swing_grap_0_1')
    sprite('bl600_07', 4)
    sprite('bl600_08', 6)
    sprite('bl600_09', 6)
    Voiceline('bl413')
    DemoEndOnVoiceEnd(1)
    sprite('bl600_10', 4)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    ExitState()
    label(10)
    sprite('bl601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('bl601_00', 100)
    Voiceline('bl414')
    sprite('bl601_01', 4)
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 10)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 6)
    sprite('bl601_08', 6)
    sprite('bl601_09', 8)
    Voiceline('bl415')
    DemoEndOnVoiceEnd(1)
    sprite('bl601_10', 8)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    ExitState()
    label(20)
    sprite('bl601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('bl601_00', 100)
    Voiceline('bl416')
    sprite('bl601_01', 4)
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 10)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 6)
    sprite('bl601_08', 6)
    sprite('bl601_09', 8)
    Voiceline('bl417')
    DemoEndOnVoiceEnd(1)
    sprite('bl601_10', 8)
    sprite('bl601_10', 8)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    ExitState()
    label(150)
    sprite('bl611_08', 6)
    sprite('bl611_09', 8)
    sprite('bl611_10', 8)
    sprite('bl611_11', 30)
    sprite('bl611_10', 8)
    sprite('bl611_09', 8)
    sprite('bl611_08', 6)
    sprite('bl611_07', 10)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(150)
    sprite('bl611_08', 6)
    sprite('bl611_09', 8)
    sprite('bl611_10', 8)
    sprite('bl611_11', 30)
    sprite('bl611_10', 8)
    sprite('bl611_09', 8)
    sprite('bl611_08', 6)
    sprite('bl611_07', 10)
    sprite('bl611_08', 6)
    sprite('bl611_09', 8)
    sprite('bl611_10', 8)
    sprite('bl611_11', 30)
    sprite('bl611_10', 8)
    sprite('bl611_09', 8)
    sprite('bl611_08', 6)
    sprite('bl611_07', 10)
    sprite('bl611_06', 5)
    CommonSE('019_cloth_b')
    sprite('bl611_05', 5)
    sprite('bl611_04', 5)
    sprite('bl611_03', 5)
    sprite('bl611_02', 5)
    sprite('bl611_01', 5)
    sprite('bl611_00', 5)

    def upon_32():
        SetActionMark(1)
    label(151)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(151)
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 6)
    sprite('bl615_03', 6)
    sprite('bl615_04', 6)
    Voiceline('bl510')
    sprite('bl615_05', 130)
    sprite('bl615_04', 6)
    sprite('bl615_03', 6)
    sprite('bl615_02', 6)
    sprite('bl615_01', 6)
    sprite('bl615_00', 6)
    DemoTimer(20)
    loopRest()
    ExitState()
    label(2150)
    sprite('bl601_00', 2)
    uponSendToLabel(32, 2151)
    sprite('bl601_00', 32767)
    loopRest()
    label(2151)
    sprite('bl601_00', 45)
    sprite('bl601_01', 5)
    Voiceline('bl510')
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 20)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 5)
    sprite('bl601_08', 5)
    sprite('bl601_09', 5)
    sprite('bl601_10', 5)
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    SetActionMark(4)
    label(2152)
    sprite('bl001_03', 6)
    AddActionMark(-1)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2152)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_11', 6)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(330)
    sprite('null', 1)
    uponSendToLabel(32, 332)
    label(331)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    sprite('bl001_03', 5)
    Voiceline('bl546')
    sprite('bl001_03', 240)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    ObjectUpon(22, 32)
    sprite('bl001_10', 6)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_11', 6)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(340)
    uponSendToLabel(32, 342)
    label(341)
    sprite('bl600_00', 6)
    loopRest()
    gotoLabel(341)
    label(342)
    sprite('bl600_00', 60)
    clearUponHandler(32)
    Voiceline('bl548')
    DemoTimer(150)
    sprite('bl600_01', 4)
    sprite('bl600_02', 4)
    sprite('bl600_03', 4)
    sprite('bl600_04', 8)
    sprite('bl600_05', 3)
    sprite('bl600_06', 4)
    CommonSE('003_swing_grap_0_1')
    sprite('bl600_07', 4)
    sprite('bl600_08', 6)
    sprite('bl600_09', 6)
    sprite('bl600_10', 4)
    loopRest()
    ExitState()
    label(2340)
    sprite('bl601_00', 2)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2340)
    sprite('bl601_00', 20)
    sprite('bl601_00', 60)
    Voiceline('bl548')
    sprite('bl601_01', 5)
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 20)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 5)
    sprite('bl601_08', 5)
    sprite('bl601_09', 5)
    sprite('bl601_10', 5)
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    SetActionMark(2)
    label(2341)
    sprite('bl001_03', 6)
    AddActionMark(-1)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2341)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_11', 6)
    ObjectUpon(22, 32)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    DemoTimer(60)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 6)
    sprite('bl615_03', 6)
    sprite('bl615_04', 6)
    if random_(2, 0, 50):
        Voiceline('bl400')
    else:
        Voiceline('bl401')
    DemoEndOnVoiceEnd(1)
    sprite('bl615_05', 8)
    sprite('bl615_06', 10)
    sprite('bl615_07', 10)
    sprite('bl615_08', 8)
    label(0)
    sprite('bl615_05', 8)
    sprite('bl615_06', 10)
    sprite('bl615_07', 10)
    sprite('bl615_08', 8)
    loopRest()
    gotoLabel(0)


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('tg'):
        if SLOT_140:
            gotoLabel(2150)
        else:
            gotoLabel(150)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('kk'):
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(340)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('bl610_00', 4)
    sprite('bl610_01', 4)
    sprite('bl610_02', 4)
    sprite('bl610_03', 4)
    sprite('bl610_04', 4)
    sprite('bl610_05', 4)
    sprite('bl610_06', 4)
    CommonSE('019_cloth_b')
    sprite('bl610_07', 4)
    sprite('bl610_08', 4)
    sprite('bl610_09', 4)
    sprite('bl610_10', 4)
    Voiceline('bl406')
    DemoEndOnVoiceEnd(1)
    sprite('bl610_11', 4)
    sprite('bl610_12', 4)
    sprite('bl610_13', 6)
    sprite('bl610_14', 6)
    sprite('bl610_15', 32767)
    loopRest()
    label(10)
    sprite('bl610_00', 4)
    sprite('bl610_01', 4)
    sprite('bl610_02', 4)
    sprite('bl610_03', 4)
    sprite('bl610_04', 4)
    sprite('bl610_05', 4)
    sprite('bl610_06', 4)
    CommonSE('019_cloth_b')
    sprite('bl610_07', 4)
    sprite('bl610_08', 4)
    sprite('bl610_09', 4)
    sprite('bl610_10', 4)
    Voiceline('bl407')
    DemoEndOnVoiceEnd(1)
    sprite('bl610_11', 4)
    sprite('bl610_12', 4)
    sprite('bl610_13', 6)
    sprite('bl610_14', 6)
    sprite('bl610_15', 32767)
    loopRest()
    label(20)
    sprite('bl611_00', 6)
    sprite('bl611_01', 6)
    sprite('bl611_02', 6)
    sprite('bl611_03', 6)
    sprite('bl611_04', 6)
    sprite('bl611_05', 6)
    sprite('bl611_06', 6)
    sprite('bl611_07', 6)
    sprite('bl611_08', 6)
    Voiceline('bl408')
    DemoEndOnVoiceEnd(1)
    sprite('bl611_09', 8)
    sprite('bl611_10', 8)
    sprite('bl611_11', 60)
    sprite('bl611_10', 8)
    sprite('bl611_09', 8)
    sprite('bl611_08', 6)
    sprite('bl611_07', 10)
    sprite('bl611_08', 6)
    label(21)
    sprite('bl611_09', 8)
    sprite('bl611_10', 8)
    sprite('bl611_11', 60)
    sprite('bl611_10', 8)
    sprite('bl611_09', 8)
    sprite('bl611_08', 6)
    sprite('bl611_07', 10)
    sprite('bl611_08', 6)
    loopRest()
    gotoLabel(21)
    label(150)
    sprite('bl610_00', 4)
    sprite('bl610_01', 4)
    sprite('bl610_02', 4)
    sprite('bl610_03', 4)
    sprite('bl610_04', 4)
    sprite('bl610_05', 4)
    sprite('bl610_06', 4)
    CommonSE('019_cloth_b')
    sprite('bl610_07', 4)
    sprite('bl610_08', 4)
    sprite('bl610_09', 4)
    sprite('bl610_10', 4)
    Voiceline('bl511')
    DemoEndOnVoiceEnd(1)
    sprite('bl610_11', 4)
    sprite('bl610_12', 4)
    sprite('bl610_13', 6)
    sprite('bl610_14', 6)
    sprite('bl610_15', 32767)
    loopRest()
    label(2150)
    sprite('bl450_36', 6)
    AddX(-30000)
    sprite('bl450_37', 6)
    sprite('bl450_38', 6)
    Voiceline('bl511')
    DemoEndOnVoiceEnd(1)
    sprite('bl450_39', 60)
    sprite('bl450_40', 7)
    sprite('bl450_41', 7)
    sprite('bl450_38', 6)
    sprite('bl450_39', 60)
    sprite('bl450_40', 7)
    sprite('bl450_41', 7)
    sprite('bl450_38', 6)
    sprite('bl450_39', 32767)
    label(330)
    sprite('bl610_00', 4)
    sprite('bl610_01', 4)
    sprite('bl610_02', 4)
    sprite('bl610_03', 4)
    sprite('bl610_04', 4)
    sprite('bl610_05', 4)
    sprite('bl610_06', 4)
    CommonSE('019_cloth_b')
    sprite('bl610_07', 4)
    sprite('bl610_08', 4)
    sprite('bl610_09', 4)
    sprite('bl610_10', 4)
    Voiceline('bl547')
    DemoEndOnVoiceEnd(1)
    sprite('bl610_11', 4)
    sprite('bl610_12', 4)
    sprite('bl610_13', 6)
    sprite('bl610_14', 6)
    sprite('bl610_15', 32767)
    loopRest()
    label(340)
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 6)
    sprite('bl615_03', 6)
    sprite('bl615_04', 6)
    Voiceline('bl549')
    DemoEndOnVoiceEnd(1)
    sprite('bl615_05', 8)
    sprite('bl615_06', 10)
    sprite('bl615_07', 10)
    sprite('bl615_08', 8)
    sprite('bl615_05', 8)
    sprite('bl615_06', 10)
    sprite('bl615_07', 32767)
    loopRest()
    label(2340)
    sprite('bl450_36', 6)
    AddX(-30000)
    sprite('bl450_37', 6)
    sprite('bl450_38', 6)
    Voiceline('bl549')
    DemoEndOnVoiceEnd(1)
    sprite('bl450_39', 60)
    sprite('bl450_40', 7)
    sprite('bl450_41', 7)
    sprite('bl450_38', 6)
    sprite('bl450_39', 60)
    sprite('bl450_40', 7)
    sprite('bl450_41', 7)
    sprite('bl450_38', 6)
    sprite('bl450_39', 32767)
    label(666)
    sprite('bl610_00', 4)
    sprite('bl610_01', 4)
    sprite('bl610_02', 4)
    sprite('bl610_03', 4)
    sprite('bl610_04', 4)
    sprite('bl610_05', 4)
    sprite('bl610_06', 4)
    CommonSE('019_cloth_b')
    sprite('bl610_07', 4)
    sprite('bl610_08', 4)
    sprite('bl610_09', 4)
    sprite('bl610_10', 4)
    if random_(2, 0, 50):
        Voiceline('bl406')
    else:
        Voiceline('bl407')
    DemoEndOnVoiceEnd(1)
    sprite('bl610_11', 4)
    sprite('bl610_12', 4)
    sprite('bl610_13', 6)
    sprite('bl610_14', 6)
    sprite('bl610_15', 32767)
    loopRest()


@State
def CmnActLose():
    sprite('bl620_00', 6)
    Voiceline('bl411')
    sprite('bl620_01', 6)
    sprite('bl620_02', 6)
    sprite('bl620_03', 6)
    sprite('bl620_04', 6)
    sprite('bl620_05', 6)
    sprite('bl620_06', 6)
    sprite('bl620_07', 6)
    sprite('bl620_08', 6)
    ScreenShake(0, 5000)
    sprite('bl620_09', 32767)
    DemoTimer(90)


@State
def EventDefEntryWait():
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
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
    sprite('bl620_04', 32767)


@State
def EventDefLose2():
    label(0)
    sprite('bl070_02', 5)
    gotoLabel(0)


@State
def EventDefLose3():
    sprite('bl070_03', 6)
    sprite('bl070_04', 6)
    sprite('bl070_05', 6)
    sprite('bl070_06', 6)
    sprite('bl070_07', 6)
    sprite('bl070_08', 6)
    sprite('bl070_09', 6)
    sprite('bl063_11', 32767)


@State
def EventEntryWithBag():
    sprite('bl600_00', 32767)
    loopRest()


@State
def EventEntryWithBagToStand():
    sprite('bl600_01', 4)
    sprite('bl600_02', 4)
    sprite('bl600_03', 4)
    sprite('bl600_04', 8)
    sprite('bl600_05', 3)
    sprite('bl600_06', 4)
    sprite('bl600_07', 4)
    sprite('bl600_08', 6)
    sprite('bl600_09', 6)
    sprite('bl600_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def EventDefEntryFDashIn():
    EnableCollision(0)
    ScreenCollision(0)
    XPositionRelativeFacing(-1280000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 400000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -400000:
            sendToLabel(1)
    sprite('bl032_01', 1)
    DashEffects(100, 1, 1)
    CommonSE('000_airdash_0')
    physicsXImpulse(21000)
    SetAcceleration(200)
    label(0)
    sprite('bl032_01', 3)
    sprite('bl032_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    sprite('bl032_03', 3)
    AddX(20000)
    XImpulseAcceleration(70)
    sprite('bl032_03', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_05', 8)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('bl032_06', 6)
    sprite('bl032_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventGauntletFire():
    sprite('bl601_10', 4)
    sprite('bl601_08', 4)
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 10)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 6)
    sprite('bl601_08', 6)
    sprite('bl601_09', 8)
    sprite('bl601_10', 8)
    loopRest()
    enterState('CmnActStand')


@State
def EventChouhatsuStart():
    sprite('bl300_00', 6)
    sprite('bl300_01', 6)
    sprite('bl300_02', 8)
    sprite('bl300_03', 10)
    sprite('bl300_04', 8)
    sprite('bl300_05', 8)
    sprite('bl300_06', 8)
    sprite('bl300_07', 32767)
    loopRest()


@State
def EventChouhatsuEnd():
    sprite('bl300_08', 8)
    sprite('bl300_09', 5)
    sprite('bl300_10', 5)
    sprite('bl300_11', 5)
    sprite('bl300_12', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventRequestShake():
    sprite('keep', 12)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('keep', 12)
    ScreenShake(3000, 8000)
    sprite('keep', 12)
    ScreenShake(4000, 9000)
    sprite('keep', 12)
    ScreenShake(4000, 10000)
    label(0)
    sprite('keep', 12)
    ScreenShake(4000, 12000)
    CommonSE('019_quake_1')
    sprite('keep', 12)
    ScreenShake(4000, 12000)
    sprite('keep', 12)
    ScreenShake(4000, 12000)
    CommonSE('019_quake_0')
    sprite('keep', 12)
    ScreenShake(4000, 12000)
    gotoLabel(0)


@State
def EventBackStep():
    sprite('bl033_00', 1)
    EnableCollision(0)
    ScreenCollision(0)
    sprite('bl033_00', 2)
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    setGravity(750)
    CommonSE('001_airbackdash_2')
    sprite('bl033_01', 2)
    sprite('bl033_01', 1)
    sprite('bl033_02', 3)
    sprite('bl033_01', 3)
    sprite('bl033_02', 3)
    sprite('bl033_01', 3)
    sprite('bl033_02', 3)
    sprite('bl033_01', 3)
    sprite('bl033_02', 3)
    sprite('bl033_01', 3)
    sprite('bl033_02', 3)
    sprite('bl033_01', 3)
    sprite('bl033_03', 2)
    sprite('bl033_04', 2)
    sprite('bl033_05', 2)
    sprite('bl033_06', 2)
    sprite('bl033_07', 2)
    sprite('bl033_07', 2)
    sprite('null', 32767)


@State
def EventBLVsVH_YorokeToYoroke():
    sprite('bl070_01', 5)
    sprite('bl070_00', 5)
    sprite('bl000_00', 120)
    sprite('bl620_00', 6)
    sprite('bl620_01', 6)
    sprite('bl620_00', 6)
    sprite('bl620_01', 6)
    sprite('bl620_02', 6)
    sprite('bl620_01', 6)
    sprite('bl620_02', 6)
    sprite('bl620_01', 6)
    sprite('bl620_00', 18)
    sprite('bl620_01', 3)
    sprite('bl620_02', 3)
    sprite('bl620_03', 3)
    sprite('bl620_04', 120)
    sprite('bl620_05', 6)
    sprite('bl620_06', 6)
    sprite('bl620_07', 6)
    sprite('bl620_08', 6)
    ScreenShake(0, 5000)
    sprite('bl620_09', 32767)
    loopRest()


@State
def EventDefReverseEntryWait():
    sprite('bl000_00', 6)
    Flip()
    label(0)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDefReverseEntryWaitEnd():
    sprite('bl003_00', 6)
    Flip()
    sprite('bl003_01', 6)
    sprite('bl003_02', 6)
    enterState('CmnActStand')


@State
def EventAtk5D():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 40)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('bl203_00', 2)
    sprite('bl203_01', 1)
    sprite('bl203_01', 1)
    CreateObject('BLEF_LockOnZone', -1)
    RegisterObject(5, 1)
    sprite('bl203_02', 2)
    sprite('bl203_03', 1)
    sprite('bl203_03', 1)
    sprite('bl203_04', 2)
    ObjectUpon(22, 32)
    label(0)
    sprite('bl203_02', 3)
    sprite('bl203_03', 3)
    sprite('bl203_04', 3)
    gotoLabel(0)
    label(1)
    sprite('bl203_01', 3)
    ObjectUpon(5, 32)
    sprite('bl203_00', 2)
    enterState('CmnActStand')


@State
def EventBLWinLoop():
    label(0)
    sprite('bl615_05', 8)
    sprite('bl615_06', 10)
    sprite('bl615_07', 10)
    sprite('bl615_08', 8)
    loopRest()
    gotoLabel(0)


@State
def EventBLWinLoopEnd():
    sprite('bl615_04', 6)
    sprite('bl615_03', 6)
    sprite('bl615_02', 6)
    sprite('bl615_01', 6)
    sprite('bl615_00', 6)
    loopRest()
    enterState('EventDefEntryWait')


@State
def EventWalkFrameIn():
    ScreenCollision(0)
    EnableCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -260000:
            sendToLabel(1)
    sprite('bl030_00', 4)
    physicsXImpulse(3250)
    label(0)
    sprite('bl030_01', 4)
    sprite('bl030_02', 4)
    sprite('bl030_03', 4)
    sprite('bl030_04', 4)
    sprite('bl030_05', 4)
    sprite('bl030_06', 4)
    sprite('bl030_07', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl030_08', 4)
    sprite('bl030_09', 4)
    sprite('bl030_10', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefYorokeToStand():
    sprite('bl070_10', 5)
    sprite('bl070_11', 5)
    sprite('bl070_12', 5)
    sprite('bl070_13', 5)
    enterState('CmnActStand')


@State
def EventWalkScreenOut():
    sprite('bl030_01', 4)
    Flip()
    ScreenCollision(0)
    EnableCollision(0)
    sprite('bl030_02', 4)
    physicsXImpulse(4300)
    RunLoopUpon(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('bl030_03', 4)
    sprite('bl030_04', 4)
    sprite('bl030_05', 4)
    sprite('bl030_06', 4)
    sprite('bl030_07', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl030_08', 4)
    sprite('bl030_09', 4)
    sprite('bl030_10', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bl030_01', 4)
    sprite('bl030_02', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 20)


@State
def EventCKRunAction():
    sprite('keep', 32767)
    Visibility(1)
    XPositionRelativeFacing(-900000)
    CreateObject('EventCKRun', -1)

    def RunOnObject_1():
        XPositionRelativeFacing(900000)


@State
def EventBLvsAREntry01():
    EnableCollision(0)
    ScreenCollision(0)
    XPositionRelativeFacing(-1280000)
    RunLoopUpon(17, 25)

    def upon_17():
        clearUponHandler(17)
        ObjectUpon(22, 32)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 400000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -400000:
            sendToLabel(1)
    sprite('bl032_01', 1)
    DashEffects(100, 1, 1)
    CommonSE('000_airdash_0')
    physicsXImpulse(21000)
    SetAcceleration(200)
    label(0)
    sprite('bl032_01', 3)
    sprite('bl032_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    sprite('bl032_03', 3)
    AddX(20000)
    XImpulseAcceleration(70)
    sprite('bl032_03', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_05', 8)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('bl032_06', 6)
    sprite('bl032_07', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventTGCreate():
    sprite('keep', 32767)
    Visibility(1)
    XPositionRelativeFacing(-900000)
    CreateObject('EventTG', -1)


@State
def EventBLvsAZDashEntry():
    uponSendToLabel(32, 10)
    EnableCollision(0)
    ScreenCollision(0)
    XPositionRelativeFacing(-1280000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage < 400000:
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage > -400000:
            sendToLabel(1)
    sprite('bl032_01', 1)
    DashEffects(100, 1, 1)
    CommonSE('000_airdash_0')
    physicsXImpulse(21000)
    SetAcceleration(200)
    label(0)
    sprite('bl032_01', 3)
    sprite('bl032_02', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    sprite('bl032_03', 3)
    AddX(20000)
    XImpulseAcceleration(70)
    sprite('bl032_03', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_04', 3)
    XImpulseAcceleration(70)
    sprite('bl032_05', 8)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('bl032_06', 6)
    sprite('bl032_07', 6)
    loopRest()
    label(2)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('keep', 22)
    TriggerUponForState('EventTG', 32)
    ScreenShake(7500, 20000)
    loopRest()
    enterState('EventDefReverseEntryWait')


@State
def EventDefLose2End():
    sprite('bl070_01', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RoundWin():
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 6)
    sprite('bl615_03', 6)
    sprite('bl615_04', 6)
    sprite('bl615_05', 32767)
    loopRest()


@State
def Act2Event_RoundWinEnd():
    sprite('bl615_04', 6)
    sprite('bl615_03', 6)
    sprite('bl615_02', 6)
    sprite('bl615_01', 6)
    sprite('bl615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Ikaku():
    sprite('bl611_00', 4)
    sprite('bl611_01', 4)
    sprite('bl611_02', 4)
    sprite('bl611_03', 4)
    sprite('bl611_04', 4)
    sprite('bl611_05', 4)
    sprite('bl611_06', 4)
    sprite('bl601_01', 5)
    sprite('bl601_02', 5)
    sprite('bl601_03', 5)
    sprite('bl601_04', 20)
    sprite('bl601_05', 4)
    CreateParticle('blef_entry', 0)
    CommonSE('016_explode_1')
    sprite('bl601_06', 5)
    sprite('bl601_07', 5)
    sprite('bl601_08', 5)
    sprite('bl601_09', 5)
    sprite('bl601_10', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoroke():
    sprite('bl070_03', 32767)
    loopRest()


@State
def Act2Event_YorokeEnd():
    sprite('bl070_10', 4)
    sprite('bl070_11', 4)
    sprite('bl070_12', 4)
    sprite('bl070_13', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvstb_00():

    def upon_IMMEDIATE():
        SetZVal(-500)
    sprite('bl032_00', 3)
    SetInertia(30000)
    sprite('bl032_01', 3)
    DashEffects(100, 1, 1)
    sprite('bl032_02', 3)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)
    sprite('bl402_00', 6)
    sprite('bl402_01', 4)
    sprite('bl402_02', 3)
    EndMomentum(1)
    CommonSE('006_swing_blade_2')
    sprite('bl402_03', 3)
    CommonSE('107_throw_catch')
    ObjectUpon(22, 32)
    sprite('bl402_10', 3)
    sprite('bl402_11', 32767)
    loopRest()


@State
def Act2Event_blvstb_01():
    sprite('keep', 2)
    sprite('bl402_08', 6)
    ObjectUpon(22, 33)
    sprite('bl402_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvstk_00():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        EnableCollision(0)
    label(9)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('bl060_00', 2)
    CommonSE('107_throw_catch')
    ScreenShake(1000, 20000)
    sprite('bl060_07', 6)
    sprite('bl060_14', 30)
    sprite('bl061_00', 5)
    sprite('bl061_01', 32767)


@State
def Act2Event_blvstk_01():

    def upon_IMMEDIATE():
        EnableCollision(0)

        def upon_STATE_END():
            SetZVal(0)
            XPositionRelativeFacing(-260000)
    sprite('bl061_02', 3)
    sprite('bl061_03', 2)
    sprite('bl061_04', 2)
    sprite('bl061_05', 3)
    sprite('bl061_06', 3)
    sprite('bl061_07', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvstk_02():
    sprite('bl032_00', 3)
    SetInertia(20000)
    sprite('bl032_01', 3)
    DashEffects(100, 1, 1)
    sprite('bl032_02', 3)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvstk_03():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
    sprite('bl404_00', 3)
    sprite('bl404_00', 3)
    physicsXImpulse(8500)
    sprite('bl404_01', 3)
    XImpulseAcceleration(200)
    JumpEffects(100, 1)
    AirDashEffects(1)
    sprite('bl404_02', 3)
    sprite('bl404_03', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_04', 3)
    XImpulseAcceleration(200)
    sprite('bl404_05', 3)
    sprite('bl404_06', 3)
    sprite('bl404_07', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_08', 3)


@State
def Act2Event_blvstk_04():
    sprite('bl300_00', 6)
    sprite('bl300_01', 6)
    sprite('bl300_02', 8)
    sprite('bl300_03', 10)
    sprite('bl300_04', 8)
    sprite('bl300_05', 8)
    sprite('bl300_06', 8)
    sprite('bl300_07', 10)
    sprite('bl300_08', 8)
    sprite('bl300_09', 5)
    sprite('bl300_10', 5)
    sprite('bl300_11', 5)
    sprite('bl300_12', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvstk_05():
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_11', 6)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvskk_00():
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 6)
    sprite('bl615_03', 6)
    sprite('bl615_04', 6)
    sprite('bl615_05', 32767)
    loopRest()


@State
def Act2Event_blvskk_01():
    sprite('bl615_04', 6)
    sprite('bl615_03', 6)
    sprite('bl615_02', 32767)
    loopRest()


@State
def Act2Event_blvskk_02():
    sprite('bl615_01', 6)
    sprite('bl615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_blvskk_03():
    sprite('bl615_00', 6)
    sprite('bl615_01', 6)
    sprite('bl615_02', 32767)
    loopRest()


@State
def Act3Event_blvsmk_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)
        XPositionRelativeFacing(-1250000)
    label(0)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    sprite('bl000_00', 6)
    loopRest()
    gotoLabel(0)
    loopRest()


@State
def Act3Event_blvsmk_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        CameraControlEnable(1)

        def upon_32():
            CameraControlEnable(0)
    sprite('bl200_00', 6)
    sprite('bl200_01', 6)
    sprite('bl200_02', 15)
    sprite('bl200_02', 15)
    CommonSE('blse_02')
    sprite('bl200_02', 15)
    CommonSE('014_electric_sl')
    sprite('bl200_02', 15)
    sprite('bl200_01', 6)
    sprite('bl200_00', 6)
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_blvsmk_02():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        AddX(430000)
    sprite('bl032_00', 3)
    SetInertia(62000)
    sprite('bl032_01', 3)
    DashEffects(100, 1, 1)
    sprite('bl032_02', 3)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    WhiffJumpCancel(0)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)
    loopRest()
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvshb_00():
    sprite('keep', 2)
    AddX(90000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvshb_01():
    sprite('bl405_00', 3)
    sprite('bl405_01', 1)
    sprite('bl405_01', 3)
    sprite('bl405_02', 2)
    label(0)
    sprite('bl405_03', 3)
    if SLOT_2:
        DespawnEAEffect('shot_charge')
        SLOT_2 = 0
    CreateObject('shot_charge', 0)

    def RunOnObject_1():
        Size(1100)
    PrivateSE('blse_03')
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl405_03', 3)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl405_03', 3)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl405_03', 3)
    sprite('bl405_04', 3)
    sprite('bl405_05', 3)
    sprite('bl405_03', 3)
    sprite('bl405_04', 3)
    sprite('bl405_05', 2)
    sprite('bl405_05', 1)
    AddActionMark(1)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_blvshb_02():
    sprite('bl405_05', 1)
    sprite('bl405_05', 2)
    sprite('bl405_03', 3)
    sprite('bl405_04', 2)
    ObjectUpon(22, 32)
    sprite('bl405_04', 1)
    PrivateSE('blse_05')
    ScreenShake(10000, 15000)
    sprite('bl405_06', 1)
    AddInertia(-5000)
    DespawnEAEffect('shot_charge')
    CreateObject('405_mazzle', 0)
    sprite('bl405_06', 2)
    sprite('bl405_07', 3)
    sprite('bl405_08', 4)
    sprite('bl405_09', 4)
    sprite('bl405_10', 4)
    sprite('bl405_11', 4)
    sprite('bl405_12', 2)
    sprite('bl405_13', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvshb_03():
    sprite('bl032_00', 3)
    EnableCollision(0)
    SetInertia(25000)
    sprite('bl032_01', 3)
    DashEffects(100, 1, 1)
    sprite('bl032_02', 3)
    XImpulseAcceleration(200)
    sprite('bl032_03', 3)
    WhiffJumpCancel(0)
    sprite('bl032_04', 2)
    sprite('bl032_05', 2)
    XImpulseAcceleration(10)
    SkidEffects(100, 1, 1)
    sprite('bl032_06', 2)
    sprite('bl032_07', 2)
    loopRest()
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvsrm_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        AddX(-350000)
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def Act3Event_blvsrm_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)

        def upon_EVERY_FRAME():
            if SLOT_19 < 350000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(22, 32)
                sendToLabel(1)
    sprite('bl203_06', 3)
    AirDashEffects(1)
    physicsXImpulse(48000)
    label(0)
    sprite('bl203_07', 3)
    sprite('bl203_08', 3)
    sprite('bl203_07', 3)
    sprite('bl203_08', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    EndMomentum(1)
    setGravity(0)
    sprite('bl431_06', 3)
    if SLOT_IsAirborne:
        AddX(-30000)
        AddY(-80000)
    sprite('bl022_00', 3)
    XImpulseAcceleration(0)
    AddX(100000)
    AddY(100000)
    physicsXImpulse(-15000)
    physicsYImpulse(9500)
    GravityDefault()
    if SLOT_IsOppAirborne:
        physicsYImpulse(10000)
    sprite('bl022_01', 3)
    sprite('bl022_02', 3)
    XImpulseAcceleration(75)
    sprite('bl022_03', 3)
    sprite('bl022_06', 3)
    XImpulseAcceleration(50)
    sprite('bl022_07', 3)
    sprite('bl022_08', 32767)

    def upon_LANDING():
        EndMomentum(1)
        XPositionRelativeFacing(-260000)
        sendToLabel(2)
    label(2)
    sprite('bl024_00', 2)
    LandingEffects(100, 1, 1)
    sprite('bl024_01', 3)
    sprite('bl024_02', 1)
    sprite('bl024_03', 3)
    sprite('bl024_04', 3)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvsrm_02():
    sprite('bl405_05', 1)
    sprite('bl405_05', 2)
    sprite('bl405_03', 3)
    sprite('bl405_04', 2)
    sprite('bl405_04', 1)
    PrivateSE('blse_05')
    ScreenShake(10000, 15000)
    sprite('bl405_06', 1)
    AddInertia(-5000)
    DespawnEAEffect('shot_charge')
    CreateObject('405_mazzle', 0)
    sprite('bl405_06', 2)
    sprite('bl405_07', 3)
    ObjectUpon(22, 32)
    sprite('bl405_08', 4)
    sprite('bl405_09', 4)
    sprite('bl405_10', 4)
    sprite('bl405_11', 4)
    sprite('bl405_12', 2)
    sprite('bl405_13', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_blvsrm_03():
    sprite('bl000_00', 6)
    CommonSE('401_nesica_pass')
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl200_00', 6)
    sprite('bl200_01', 6)
    sprite('bl200_02', 32767)
    loopRest()


@State
def Act3Event_blvsrm_04():
    sprite('bl200_02', 15)
    CommonSE('blse_02')
    sprite('bl200_02', 15)
    CommonSE('014_electric_sl')
    sprite('bl200_02', 15)
    sprite('bl200_01', 6)
    sprite('bl200_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Turn():
    sprite('bl003_00', 3)
    Flip()
    sprite('bl003_01', 3)
    sprite('bl003_02', 3)
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_RunAway():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
        SetZVal(-500)
    sprite('bl404_00', 3)
    sprite('bl404_00', 3)
    physicsXImpulse(12500)
    sprite('bl404_01', 3)
    XImpulseAcceleration(200)
    JumpEffects(100, 1)
    sprite('bl404_02', 3)
    sprite('bl404_03', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_04', 3)
    sprite('bl404_05', 3)
    sprite('bl404_06', 3)
    sprite('bl404_07', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_08', 3)
    sprite('bl404_01', 3)
    sprite('bl404_02', 3)
    sprite('bl404_03', 3)
    DashEffects(100, 1, 1)
    sprite('bl404_04', 3)
    loopRest()
    label(0)
    sprite('bl404_05', 3)
    sprite('bl404_06', 3)
    sprite('bl404_07', 3)
    sprite('bl404_08', 3)
    sprite('bl404_01', 3)
    sprite('bl404_02', 3)
    sprite('bl404_03', 3)
    sprite('bl404_04', 3)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_AfterBurner():
    sprite('bl408_00', 2)
    sprite('bl408_01', 2)
    sprite('bl408_02', 3)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    CreateObject('408_Fireroop', 0)
    CreateObject('408_BodyFire', -1)
    sprite('bl408_03', 3)
    label(0)
    sprite('bl408_02', 3)
    CreateObject('408_BodyFire', -1)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    sprite('bl408_03', 3)
    sprite('bl408_02', 3)
    sprite('bl408_03', 3)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_AfterBurnerEnd():
    sprite('bl408_02', 5)
    TriggerUponForState('408_Fireroop', 32)
    sprite('bl408_03', 5)
    sprite('bl408_04', 4)
    sprite('bl408_05', 4)
    PrivateSE('blse_09')
    AltKnockdownEffects(100, 1, 0)
    ScreenShake(10000, 20000)
    sprite('bl408_06', 3)
    CreateObject('408_Kaiho', -1)
    sprite('bl408_07', 3)
    ScreenShake(30000, 50000)
    sprite('bl408_08', 3)
    sprite('bl408_06', 3)
    sprite('bl408_07', 3)
    sprite('bl408_08', 3)
    sprite('bl408_06', 3)
    sprite('bl408_07', 3)
    sprite('bl408_08', 3)
    sprite('bl408_06', 3)
    sprite('bl408_07', 3)
    sprite('bl408_08', 3)
    sprite('bl408_09', 5)
    sprite('bl408_10', 5)
    sprite('bl408_11', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Reaction():
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl001_00', 6)
    sprite('bl001_01', 6)
    sprite('bl001_02', 6)
    label(0)
    sprite('bl001_03', 6)
    sprite('bl001_04', 6)
    sprite('bl001_05', 6)
    sprite('bl001_06', 6)
    sprite('bl001_07', 6)
    sprite('bl001_08', 6)
    sprite('bl001_09', 6)
    sprite('bl001_10', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ReactionEnd():
    sprite('bl001_11', 6)
    sprite('bl001_12', 6)
    sprite('bl001_13', 6)
    loopRest()
    enterState('CmnActStand')
