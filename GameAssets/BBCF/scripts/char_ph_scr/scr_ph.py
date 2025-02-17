@Subroutine
def BGN_Delete():
    SLOT_8 = 0
    ObjectUpon(CORNERED, 32)
    setInvincible(0)


@Subroutine
def BGN_Break():
    SLOT_8 = 0
    ObjectUpon(CORNERED, 35)
    setInvincible(0)


@Subroutine
def ActiveMagicAllDelete():
    ObjectUpon(CORNERED, 32)
    ObjectUpon(8, 32)
    TriggerUponForState('DriveAtk_BRN', 32)
    TriggerUponForState('DriveAtk_RRB', 32)
    TriggerUponForState('DriveAtk_RRG', 32)
    TriggerUponForState('DriveAtk_GGR', 32)
    TriggerUponForState('DriveAtk_GGR_C', 32)
    TriggerUponForState('DriveAtk_GGR_L', 32)
    TriggerUponForState('DriveAtk_GGR_LL', 32)
    TriggerUponForState('DriveAtk_GGR_R', 32)
    TriggerUponForState('DriveAtk_GGR_RR', 32)
    TriggerUponForState('DriveAtk_GGB', 32)
    TriggerUponForState('DriveAtk_GGB_ATKMaster', 32)
    TriggerUponForState('DriveAtk_BBR', 32)
    TriggerUponForState('DriveAtk_BBG', 32)
    TriggerUponForState('DriveAtk_BGR', 32)


@Subroutine
def MagicReset():
    SLOT_4 = 0
    SLOT_31 = 0
    SLOT_59 = 0
    SLOT_60 = 0
    SLOT_61 = 0
    callSubroutine('MagicEffectDelete')


@Subroutine
def MagicFastReset():
    SLOT_4 = 0
    SLOT_31 = 0
    SLOT_59 = 0
    SLOT_60 = 0
    SLOT_61 = 0
    callSubroutine('MagicEffectFastDelete')


@Subroutine
def StockMagicReset():
    SLOT_5 = 0
    SLOT_32 = 0
    SLOT_62 = 0
    SLOT_63 = 0
    SLOT_64 = 0


@Subroutine
def MagicEffectDelete():
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)


@Subroutine
def MagicEffectFastDelete():
    ObjectUpon(FALLING, 41)
    ObjectUpon(5, 41)
    ObjectUpon(6, 41)


@Subroutine
def MagicReductionClear():
    SLOT_33 = 0
    TriggerUponForState('pheff_BufWindMato', 32)
    TriggerUponForState('pheff_BufWaterMato', 32)
    TriggerUponForState('pheff_BufFireMato', 32)


@Subroutine
def MagicReductionOD():
    if SLOT_OverdriveTimer:
        if SLOT_4:
            PrivateSE('phse_09')
            if SLOT_59 == 4:
                CreateParticle('phef_buf_red', 103)
                SLOT_6 = 4
                callSubroutine('MagicReductionClear')
                CreateObject('pheff_BufFireMato', 103)
            if SLOT_59 == 2:
                CreateParticle('phef_buf_green', 103)
                SLOT_6 = 2
                callSubroutine('MagicReductionClear')
                CreateObject('pheff_BufWindMato', 103)
            if SLOT_59 == 1:
                CreateParticle('phef_buf_blue', 103)
                SLOT_6 = 1
                callSubroutine('MagicReductionClear')
                CreateObject('pheff_BufWaterMato', 103)
            if SLOT_4 >= 1:
                SLOT_33 = 180
            if SLOT_4 >= 16:
                SLOT_33 = 360
            if SLOT_4 >= 256:
                SLOT_33 = 540


@Subroutine
def MagicTableUpDate():
    SLOT_4 = SLOT_4 * 16
    ModifyVar_(7, 2, 4, 0, 4095)
    SLOT_4 = SLOT_4 + SLOT_55
    callSubroutine('MagicEffectDelete')
    callSubroutine('MagicIDUpDate')
    callSubroutine('StockMagicIDUpDate')


@Subroutine
def MagicReplace():
    SLOT_0 = SLOT_5
    SLOT_5 = SLOT_4
    SLOT_4 = SLOT_0
    callSubroutine('MagicEffectDelete')
    callSubroutine('MagicIDUpDate')
    callSubroutine('StockMagicIDUpDate')


@Subroutine
def MagicCompose():
    SLOT_4 = SLOT_4 + SLOT_59
    SLOT_60 = SLOT_60 * 16
    SLOT_4 = SLOT_4 + SLOT_60
    SLOT_61 = SLOT_61 * 256
    SLOT_4 = SLOT_4 + SLOT_61


@Subroutine
def MagicIDUpDate():
    PrivateFunction(7, 2, 4, 0, 15, 2, 59)
    PrivateFunction(7, 2, 4, 0, 240, 2, 60)
    SLOT_60 = SLOT_60 / 16
    PrivateFunction(7, 2, 4, 0, 3840, 2, 61)
    SLOT_61 = SLOT_61 / 256
    SLOT_56 = 0
    SLOT_57 = 0
    SLOT_58 = 0
    SLOT_31 = 0
    if SLOT_59 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_59 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_59 == 1:
        SLOT_58 = SLOT_58 + 1
    if SLOT_60 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_60 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_60 == 1:
        SLOT_58 = SLOT_58 + 1
    if SLOT_61 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_61 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_61 == 1:
        SLOT_58 = SLOT_58 + 1
    SLOT_56 = SLOT_56 * 256
    SLOT_57 = SLOT_57 * 16
    SLOT_31 = SLOT_31 + SLOT_56
    SLOT_31 = SLOT_31 + SLOT_57
    SLOT_31 = SLOT_31 + SLOT_58


@Subroutine
def MagicIconUpDate():
    if SLOT_31 == 0:
        ResourceBarIcon(0, 0)
    if SLOT_31 == 1:
        ResourceBarIcon(0, 55)
    if SLOT_31 == 16:
        ResourceBarIcon(0, 56)
    if SLOT_31 == 256:
        ResourceBarIcon(0, 54)
    if SLOT_31 == 2:
        ResourceBarIcon(0, 58)
    if SLOT_31 == 32:
        ResourceBarIcon(0, 59)
    if SLOT_31 == 512:
        ResourceBarIcon(0, 57)
    if SLOT_31 == 17:
        ResourceBarIcon(0, 62)
    if SLOT_31 == 257:
        ResourceBarIcon(0, 60)
    if SLOT_31 == 272:
        ResourceBarIcon(0, 61)
    if SLOT_31 == 3:
        ResourceBarIcon(0, 64)
    if SLOT_31 == 48:
        ResourceBarIcon(0, 65)
    if SLOT_31 == 768:
        ResourceBarIcon(0, 63)
    if SLOT_31 == 513:
        ResourceBarIcon(0, 66)
    if SLOT_31 == 528:
        ResourceBarIcon(0, 67)
    if SLOT_31 == 288:
        ResourceBarIcon(0, 70)
    if SLOT_31 == 33:
        ResourceBarIcon(0, 71)
    if SLOT_31 == 258:
        ResourceBarIcon(0, 68)
    if SLOT_31 == 18:
        ResourceBarIcon(0, 69)
    if SLOT_31 == 273:
        ResourceBarIcon(0, 72)


@Subroutine
def StockMagicIDUpDate():
    PrivateFunction(7, 2, 5, 0, 15, 2, 62)
    PrivateFunction(7, 2, 5, 0, 240, 2, 63)
    SLOT_63 = SLOT_63 / 16
    PrivateFunction(7, 2, 5, 0, 3840, 2, 64)
    SLOT_64 = SLOT_64 / 256
    SLOT_56 = 0
    SLOT_57 = 0
    SLOT_58 = 0
    SLOT_32 = 0
    if SLOT_62 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_62 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_62 == 1:
        SLOT_58 = SLOT_58 + 1
    if SLOT_63 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_63 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_63 == 1:
        SLOT_58 = SLOT_58 + 1
    if SLOT_64 == 4:
        SLOT_56 = SLOT_56 + 1
    if SLOT_64 == 2:
        SLOT_57 = SLOT_57 + 1
    if SLOT_64 == 1:
        SLOT_58 = SLOT_58 + 1
    SLOT_56 = SLOT_56 * 256
    SLOT_57 = SLOT_57 * 16
    SLOT_32 = SLOT_32 + SLOT_56
    SLOT_32 = SLOT_32 + SLOT_57
    SLOT_32 = SLOT_32 + SLOT_58


@Subroutine
def StockMagicIconUpDate():
    if SLOT_32 == 0:
        ResourceBarIcon(1, 0)
    if SLOT_32 == 1:
        ResourceBarIcon(1, 55)
    if SLOT_32 == 16:
        ResourceBarIcon(1, 56)
    if SLOT_32 == 256:
        ResourceBarIcon(1, 54)
    if SLOT_32 == 2:
        ResourceBarIcon(1, 58)
    if SLOT_32 == 32:
        ResourceBarIcon(1, 59)
    if SLOT_32 == 512:
        ResourceBarIcon(1, 57)
    if SLOT_32 == 17:
        ResourceBarIcon(1, 62)
    if SLOT_32 == 257:
        ResourceBarIcon(1, 60)
    if SLOT_32 == 272:
        ResourceBarIcon(1, 61)
    if SLOT_32 == 3:
        ResourceBarIcon(1, 64)
    if SLOT_32 == 48:
        ResourceBarIcon(1, 65)
    if SLOT_32 == 768:
        ResourceBarIcon(1, 63)
    if SLOT_32 == 513:
        ResourceBarIcon(1, 66)
    if SLOT_32 == 528:
        ResourceBarIcon(1, 67)
    if SLOT_32 == 288:
        ResourceBarIcon(1, 70)
    if SLOT_32 == 33:
        ResourceBarIcon(1, 71)
    if SLOT_32 == 258:
        ResourceBarIcon(1, 68)
    if SLOT_32 == 18:
        ResourceBarIcon(1, 69)
    if SLOT_32 == 273:
        ResourceBarIcon(1, 72)


@Subroutine
def MagicEffectUpDate():
    if SLOT_59:
        if not CheckObjectPresence(4):
            CreateObject('phStocEff_Master1', -1)
            RegisterObject(4, 1)
            if SLOT_59 == 1:
                ObjectUpon(FALLING, 33)
            if SLOT_59 == 2:
                ObjectUpon(FALLING, 34)
            if SLOT_59 == 4:
                ObjectUpon(FALLING, 35)
            if SLOT_60:
                if not CheckObjectPresence(5):
                    CreateObject('phStocEff_Master2', -1)
                    RegisterObject(5, 1)
                    if SLOT_60 == 1:
                        ObjectUpon(5, 33)
                    if SLOT_60 == 2:
                        ObjectUpon(5, 34)
                    if SLOT_60 == 4:
                        ObjectUpon(5, 35)
                    if SLOT_61:
                        if not CheckObjectPresence(6):
                            CreateObject('phStocEff_Master3', -1)
                            RegisterObject(6, 1)
                            if SLOT_61 == 1:
                                ObjectUpon(6, 33)
                            if SLOT_61 == 2:
                                ObjectUpon(6, 34)
                            if SLOT_61 == 4:
                                ObjectUpon(6, 35)
    if not SLOT_59:
        if CheckObjectPresence(4):
            ObjectUpon(FALLING, 32)
    if not SLOT_60:
        if CheckObjectPresence(5):
            ObjectUpon(5, 32)
    if not SLOT_61:
        if CheckObjectPresence(6):
            ObjectUpon(6, 32)


@Subroutine
def TrainingMagicIDUpDate():
    if SLOT_67 == 1:
        SLOT_4 = 0
    if SLOT_67 == 2:
        SLOT_4 = 1
    if SLOT_67 == 3:
        SLOT_4 = 16
    if SLOT_67 == 4:
        SLOT_4 = 256
    if SLOT_67 == 5:
        SLOT_4 = 2
    if SLOT_67 == 6:
        SLOT_4 = 32
    if SLOT_67 == 7:
        SLOT_4 = 512
    if SLOT_67 == 8:
        SLOT_4 = 17
    if SLOT_67 == 9:
        SLOT_4 = 257
    if SLOT_67 == 10:
        SLOT_4 = 272
    if SLOT_67 == 11:
        SLOT_4 = 3
    if SLOT_67 == 12:
        SLOT_4 = 48
    if SLOT_67 == 13:
        SLOT_4 = 768
    if SLOT_67 == 14:
        SLOT_4 = 513
    if SLOT_67 == 15:
        SLOT_4 = 528
    if SLOT_67 == 16:
        SLOT_4 = 288
    if SLOT_67 == 17:
        SLOT_4 = 33
    if SLOT_67 == 18:
        SLOT_4 = 258
    if SLOT_67 == 19:
        SLOT_4 = 18
    if SLOT_67 == 20:
        SLOT_4 = 273


@Subroutine
def PreInit():
    CharacterID('ph')
    EnableDashBuffer(1)


@Subroutine
def MatchInit():
    Health(10500)
    WalkFSpeed(6800)
    WalkBSpeed(5300)
    JumpYVelocity(28000)
    SuperJumpYVelocity(30000)
    ForwardJumpVelocity(12500)
    BackwardJumpVelocity(7500)
    ForwardSuperJumpVelocity(20000)
    BackwardSuperJumpVelocity(12000)
    Gravity(1200)
    AirDashCount(0)
    ComboRate(60)
    HeatGainFactor(20)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(1)
    FootstepSE(2)
    CreateDecalOn(1)
    ResourceGauge(0, 1, 0, 1, 999, 0, 0, 0)
    ResourceGaugeFlash(0, 1)
    HideResourceGauge(1, 1)
    DisableResourceGaugeBar(0, 1)
    ResourceGauge(1, 1, 0, 1, 999, 0, 0, 0)
    DisableResourceGaugeBar(1, 1)
    ResourceGauge(2, 1, 0, 1, 540, 0, -1, -1)
    DisableResourceGaugeBar(2, 1)
    CPUJumpPriority(10000)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('2ndDash66', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(0xe2)
    DamageStunPriority(4000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 1500000, -400000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('2ndDash44', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(0xe1)
    GuardStunPriority(4000)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 400000, -400000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('2ndDash88', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(0xe4)
    OpponentAttackPriority(4000)
    SkillEstimateRange(0, 400000, -400000, 400000, 1500, 0)
    Move_EndRegister()
    Move_Register('2ndDash22', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Input_(0xdf)
    SkillEstimateRange(0, 400000, -400000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('SpDashF_Air', INPUT_SPECIALMOVE)
    NeutralOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_66)
    Move_Condition(0x3037)
    CallSkillConditions('CheckEnableAirDash')
    DamageStunPriority(5000)
    SkillEstimateRange(400000, 1000000, -400000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('SpDashB_Air', INPUT_SPECIALMOVE)
    NeutralOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_44)
    Move_Condition(0x3037)
    CallSkillConditions('CheckEnableAirDash')
    OpponentAttackPriority(4000)
    SkillEstimateRange(400000, 1000000, -400000, 200000, 375, 50)
    Move_EndRegister()
    Move_Register('Swoop', INPUT_SPECIALMOVE)
    NeutralOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0xdf)
    Move_Condition(0x3037)
    CallSkillConditions('CheckEnableAirDash')
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(2)
    DamageStunPriority(1500)
    SkillEstimateRange(200000, 600000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMaxChainRepeat(1)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 500000, 200000, 600000, 750, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4A', INPUT_4A)
    MoveMaxChainRepeat(1)
    SkillEstimateRange(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(2)
    MoveLow()
    DamageStunPriority(2000)
    SkillEstimateRange(100000, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    SharedGatling('NmlAtk5A')
    DamageStunPriority(1500)
    SkillEstimateRange(300000, 800000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    SharedGatling('NmlAtk6A')
    AirborneOpponentPriority(2000)
    SkillEstimateRange(100000, 600000, 150000, 550000, 750, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4B', INPUT_4B)
    SharedGatling('NmlAtk4A')
    SkillEstimateRange(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk2A')
    MoveLow()
    AirborneOpponentPriority(2000)
    SkillEstimateRange(300000, 550000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    SharedGatling('NmlAtk5A')
    DamageStunPriority(1500)
    SkillEstimateRange(300000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    SharedGatling('NmlAtk6A')
    AirborneOpponentPriority(2000)
    SkillEstimateRange(200000, 700000, 100000, 500000, 750, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4C', INPUT_4C)
    SharedGatling('NmlAtk4A')
    SkillEstimateRange(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    SharedGatling('NmlAtk2A')
    MoveLow()
    AirborneOpponentPriority(2000)
    SkillEstimateRange(200000, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    SharedGatling('NmlAtk6A')
    MoveLow()
    AirborneOpponentPriority(250)
    SkillEstimateRange(200000, 550000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 500000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2A', INPUT_J2A)
    MoveMaxChainRepeat(1)
    SkillEstimateRange(-100000, 300000, -450000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SharedGatling('NmlAtkAIR5A')
    SkillEstimateRange(0, 600000, -50000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B', INPUT_J2B)
    SharedGatling('NmlAtkAIR2A')
    SkillEstimateRange(0, 400000, -400000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    SharedGatling('NmlAtkAIR5A')
    SkillEstimateRange(0, 550000, -50000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    SharedGatling('NmlAtkAIR2A')
    SkillEstimateRange(100000, 500000, -350000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', 0x1)
    MoveMaxChainRepeat(2)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 400000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5D_Lv2', 0x1)
    SharedGatling('NmlAtk5D')
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMagicLv2')
    DamageStunPriority(4000)
    SkillEstimateRange(500000, 800000, -200000, 600000, 250, 750)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5D_Lv3', 0x1)
    SharedGatling('NmlAtk5D')
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMagicLv3')
    DamageStunPriority(4000)
    MoveComboPriority(2000)
    SkillEstimateRange(500000, 800000, -200000, 600000, 250, 750)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    MoveMaxChainRepeat(2)
    SkillEstimateRange(0, 400000, -200000, 150000, 750, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5D_Lv2', 0x1)
    SharedGatling('NmlAtkAIR5D')
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMagicLv2')
    SkillEstimateRange(0, 650000, -500000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5D_Lv3', 0x1)
    SharedGatling('NmlAtkAIR5D')
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMagicLv3')
    SkillEstimateRange(0, 650000, -500000, 150000, 1000, 50)
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
    Move_Register('AssaultLand', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(500)
    SkillEstimateRange(0, 650000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('AssaultAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    CallSkillConditions('CheckEnableAssaultAir')
    OpponentAttackPriority(500)
    SkillEstimateRange(0, 400000, -150000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    AirborneOpponentPriority(2000)
    OpponentAttackPriority(2000)
    SkillEstimateRange(0, 500000, 200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    MoveMid()
    OpponentAttackPriority(0)
    DamageStunPriority(0)
    GuardStunPriority(0)
    SkillEstimateRange(500000, 1500000, -200000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('MagicConversion', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckEnableMagicConversion')
    MovePriority(0)
    DamageStunPriority(0)
    GuardStunPriority(0)
    Move_EndRegister()
    Move_Register('MagicReduction', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckEnableMagicReduction')
    DamageStunPriority(0)
    GuardStunPriority(0)
    OpponentAttackPriority(5000)
    TempPriorityMultiplierInterval(0, 0, 1, 0, 1000)
    SkillEstimateRange(-200000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(5000)
    DamageStunPriority(2000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 1500000, 50000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateShotOD', INPUT_DISTORTION)
    Move_Condition(0x3081)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_A)
    OpponentAttackPriority(5000)
    DamageStunPriority(2000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 1500000, 50000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateCharge', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(3000)
    SkillEstimateRange(0, 500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateChargeOD', INPUT_DISTORTION)
    Move_Condition(0x3081)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_B)
    DamageStunPriority(3000)
    SkillEstimateRange(0, 500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateLock', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(6000)
    DamageStunPriority(2500)
    SkillEstimateRange(0, 550000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateLockOD', INPUT_DISTORTION)
    Move_Condition(0x3081)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(6000)
    DamageStunPriority(2500)
    SkillEstimateRange(0, 550000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(8000)
    DamageStunPriority(2000)
    SkillEstimateRange(400000, 1500000, -200000, 200000, 250, 0)
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
    TempPriorityMultiplier('NmlAtk3C', 'AssaultLand', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'AN_NmlAtk5D_Lv2', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'AN_NmlAtk5D_Lv3', 10000000)
    TempPriorityMultiplier('NmlAtk4A', 'NmlAtk5A', 10000000)
    TempPriorityMultiplier('NmlAtk4B', 'NmlAtk5B', 10000000)
    TempPriorityMultiplier('NmlAtk4C', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk6A', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6C', 10000000)
    TempPriorityMultiplier('NmlAtk5A', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'MidAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'MidAssault', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'FJump', 10000000)
    TempPriorityMultiplier('NmlAtkDrive_GNN', 'UltimateShot', 10000000)
    TempPriorityMultiplier('NmlAtkDrive_GGN', 'UltimateShot', 10000000)
    TempPriorityMultiplier('NmlAtkDrive_GGG', 'UltimateShot', 10000000)
    StylishModeSpecialButton('MagicReduction', 0x4, 0xea)
    StylishModeSpecialButton('AntiAir', 0x4, 0xea)
    StylishModeSpecialButton('AssaultLand', 0x4, 0x79)
    StylishModeSpecialButton('AssaultAir', 0x4, 0x79)
    StylishModeSpecialButton('UltimateLock', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateLockOD', 0x4, 0x5f)
    StylishModeSpecialButton('MagicConversion', 0x4, 0x45)
    StylishModeSpecialButton('MidAssault', 0x4, 0x45)
    StylishModeCancels('NmlAtk4A', 'NmlAtk5A', 0, 0)
    StylishModeCancels('NmlAtk4B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk4C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk4A', 'NmlAtk6A', 3, 0)
    StylishModeCancels('NmlAtk4B', 'NmlAtk6A', 3, 0)
    StylishModeCancels('NmlAtk4C', 'NmlAtk6A', 3, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk5C', 'AssaultLand', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5A', 1, 500000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5B', 1, 600000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5C', 1, 550000)
    StylishModeCancels('NmlAtk5A', 'NmlAtk3C', 1, 400000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk3C', 1, 400000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 1, 400000)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 3, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk5A', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk3C', 'AssaultLand', 0, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateShot', 6, 0)
    StylishModeCancels('NmlAtk3C', 'UltimateShotOD', 6, 0)
    StylishModeCancels('NmlAtk3C', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtk5D', 0, 0)
    StylishModeCancels('NmlAtk6A', 'FHighJump', 3, 0)
    StylishModeCancels('NmlAtk6B', 'FHighJump', 3, 0)
    StylishModeCancels('NmlAtk6C', 'FHighJump', 3, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5A', 13, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5B', 13, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5C', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR2A', 12, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR2B', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR2C', 12, 0)
    StylishModeCancels('NmlAtkAIR2A', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR2B', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR2C', 'NmlAtkAIR5D', 0, 0)
    StylishModeCancels('NmlAtkAIR2A', 'FJump', 3, 0)
    StylishModeCancels('NmlAtkAIR2B', 'FJump', 3, 0)
    StylishModeCancels('NmlAtkAIR2C', 'FJump', 3, 0)
    HitSprites(0, 'ph062_01')
    HitSprites(1, 'ph062_03')
    HitSprites(2, 'ph062_04')
    HitSprites(3, 'ph062_05')
    HitSprites(4, 'ph062_05')
    HitSprites(5, 'ph062_06')
    HitSprites(6, 'ph062_07')
    HitSprites(7, 'ph041_02')
    HitSprites(8, 'ph040_02')
    HitSprites(9, 'ph045_02')
    HitSprites(10, 'ph060_00')
    HitSprites(11, 'ph060_01')
    HitSprites(12, 'ph060_03')
    HitSprites(13, 'ph060_05')
    HitSprites(14, 'ph060_07')
    HitSprites(15, 'ph060_14')
    HitSprites(16, 'ph050_00')
    HitSprites(17, 'ph052_00')
    HitSprites(18, 'ph054_00')
    HitSprites(19, 'ph000_00')
    HitSprites(20, 'ph000_00')
    HitSprites(25, 'ph063_00')
    HitSprites(26, 'ph063_01')
    HitSprites(27, 'ph063_02')
    HitSprites(28, 'ph063_04')
    HitSprites(29, 'ph063_11')
    HitSprites(30, 'ph077_00')
    HitSprites(31, 'ph077_01')
    HitSprites(32, 'ph077_00ex01')
    HitSprites(33, 'ph077_01ex01')
    HitSprites(34, 'ph077_00ex02')
    HitSprites(35, 'ph077_01ex02')
    HitSprites(36, 'ph077_00ex03')
    HitSprites(37, 'ph077_01ex03')
    HitSprites(24, 'ph073_01')
    CommonVoicelines(0, 'ph000')
    CommonVoicelines(1, 'ph001')
    CommonVoicelines(2, 'ph002')
    CommonVoicelines(3, 'ph003')
    CommonVoicelines(4, 'ph004')
    CommonVoicelines(5, 'ph005')
    CommonVoicelines(6, 'ph006')
    CommonVoicelines(7, 'ph007')
    CommonVoicelines(8, 'ph008')
    CommonVoicelines(9, 'ph009')
    CommonVoicelines(10, 'ph010')
    CommonVoicelines(11, 'ph011')
    CommonVoicelines(12, 'ph012')
    CommonVoicelines(13, 'ph013')
    CommonVoicelines(14, 'ph014')
    CommonVoicelines(15, 'ph015')
    CommonVoicelines(16, 'ph016')
    CommonVoicelines(17, 'ph017')
    CommonVoicelines(18, 'ph018')
    CommonVoicelines(19, 'ph019')
    CommonVoicelines(20, 'ph020')
    CommonVoicelines(21, 'ph021')
    CommonVoicelines(22, 'ph022')
    CommonVoicelines(23, 'ph023')
    CommonVoicelines(24, 'ph024')
    CommonVoicelines(25, 'ph025')
    CommonVoicelines(26, 'ph026')
    CommonVoicelines(27, 'ph027')
    CommonVoicelines(28, 'ph028')
    CommonVoicelines(29, 'ph029')
    CommonVoicelines(30, 'ph030')
    CommonVoicelines(31, 'ph031')
    CommonVoicelines(32, 'ph032')
    CommonVoicelines(33, 'ph033')
    CommonVoicelines(34, 'ph034')
    CommonVoicelines(35, 'ph035')
    CommonVoicelines(36, 'ph036')
    CommonVoicelines(37, 'ph037')
    CommonVoicelines(38, 'ph038')
    CommonVoicelines(39, 'ph039')
    CommonVoicelines(40, 'ph040')
    CommonVoicelines(41, 'ph041')
    CommonVoicelines(42, 'ph042')
    CommonVoicelines(43, 'ph043')
    CommonVoicelines(44, 'ph044')
    CommonVoicelines(45, 'ph045')
    CommonVoicelines(46, 'ph046')
    CommonVoicelines(47, 'ph047')
    CommonVoicelines(48, 'ph048')
    CommonVoicelines(49, 'ph049')
    CommonVoicelines(50, 'ph050')
    CommonVoicelines(51, 'ph051')
    CommonVoicelines(52, 'ph052')
    CommonVoicelines(53, 'ph053')
    CommonVoicelines(54, 'ph100')
    CommonVoicelines(55, 'ph101')
    CommonVoicelines(56, 'ph102')
    CommonVoicelines(57, 'ph103')
    CommonVoicelines(58, 'ph104')
    CommonVoicelines(59, 'ph105')
    CommonVoicelines(60, 'ph106')
    CommonVoicelines(61, 'ph107')
    CommonVoicelines(62, 'ph108')
    CommonVoicelines(63, 'ph109')
    CommonVoicelines(64, 'ph150')
    CommonVoicelines(65, 'ph151')
    CommonVoicelines(66, 'ph152')
    CommonVoicelines(67, 'ph153')
    CommonVoicelines(68, 'ph154')
    CommonVoicelines(69, 'ph155')
    CommonVoicelines(70, 'ph156')
    CommonVoicelines(71, 'ph157')
    CommonVoicelines(72, 'ph158')
    CommonVoicelines(75, 'ph160')
    CommonVoicelines(73, 'ph402')
    CommonVoicelines(74, 'ph403')


@Subroutine
def CheckStockMagic():
    SLOT_47 = 0
    SLOT_47 = 1


@Subroutine
def CheckStockMagicLv2():
    SLOT_47 = 0
    if SLOT_5:
        if SLOT_5 >= 256:
            SLOT_47 = 1


@Subroutine
def CheckStockMagicLv3():
    SLOT_47 = 0
    if SLOT_5:
        if SLOT_5 >= 256:
            SLOT_47 = 1


@Subroutine
def CheckActivateMagicLv2():
    SLOT_47 = 0
    if SLOT_4 >= 16:
        SLOT_47 = 1


@Subroutine
def CheckActivateMagicLv3():
    SLOT_47 = 0
    if SLOT_4 >= 256:
        SLOT_47 = 1


@Subroutine
def CheckEnableAirDash():
    SLOT_47 = 0
    SLOT_7 and 1
    if op(15, 2, 0, 0, 1):
        SLOT_47 = 1


@Subroutine
def CheckEnableAssaultAir():
    SLOT_47 = 0
    SLOT_7 and 2
    if op(15, 2, 0, 0, 2):
        SLOT_47 = 1


@Subroutine
def CheckEnableMagicConversion():
    SLOT_47 = 0
    if not CurrentStateCheck('MagicConversion'):
        SLOT_47 = 1


@Subroutine
def CheckEnableMagicReduction():
    SLOT_47 = 0
    SLOT_7 and 8
    if op(15, 2, 0, 0, 8):
        SLOT_47 = 1


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def OnFrameStep():
    if not SLOT_81:
        if SLOT_InNeutral:
            TrainingModeSLOT('TRI_PhantomMagic1', 2, 67)
            if SLOT_67:
                SLOT_4 = 0
                if SLOT_67 == 4:
                    SLOT_59 = 0
                    SLOT_60 = 0
                    SLOT_61 = 0
                else:
                    if SLOT_67 == 3:
                        SLOT_67 = 4
                    if SLOT_67 == 2:
                        SLOT_67 = 2
                    if SLOT_67 == 1:
                        SLOT_67 = 1
                    if op(15, 2, 59, 2, 67):
                        callSubroutine('MagicEffectDelete')
                    SLOT_59 = SLOT_67
                    TrainingModeSLOT('TRI_PhantomMagic2', 2, 68)
                    if SLOT_68 == 0:
                        SLOT_60 = 0
                        SLOT_61 = 0
                    else:
                        if SLOT_68 == 3:
                            SLOT_68 = 4
                        if SLOT_68 == 2:
                            SLOT_68 = 2
                        if SLOT_68 == 1:
                            SLOT_68 = 1
                        if op(15, 2, 60, 2, 68):
                            callSubroutine('MagicEffectDelete')
                        SLOT_60 = SLOT_68
                        TrainingModeSLOT('TRI_PhantomMagic3', 2, 69)
                        if SLOT_69 == 0:
                            SLOT_61 = 0
                        else:
                            if SLOT_69 == 3:
                                SLOT_69 = 4
                            if SLOT_69 == 2:
                                SLOT_69 = 2
                            if SLOT_69 == 1:
                                SLOT_69 = 1
                            if op(15, 2, 61, 2, 69):
                                callSubroutine('MagicEffectDelete')
                            SLOT_61 = SLOT_69
                callSubroutine('MagicCompose')
                callSubroutine('MagicIDUpDate')
        if SLOT_IsInHitstun:
            callSubroutine('MagicEffectDelete')
        else:
            callSubroutine('MagicEffectUpDate')
        if SLOT_33:
            TrainingModeSLOT('TRI_PhantomPowerUp', 2, 70)
            if SLOT_70:
                SLOT_33 = 540
            SLOT_33 = SLOT_33 + -1
            if not SLOT_33:
                SLOT_6 = 0
                callSubroutine('MagicReductionClear')
    if SLOT_IsInHitstun:
        callSubroutine('MagicIconUpDate')
        callSubroutine('StockMagicIconUpDate')
    else:
        callSubroutine('MagicIconUpDate')
        callSubroutine('StockMagicIconUpDate')
    CallPrivateFunction('PH_Cloak', 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_IsGrounded:
        if SLOT_7:
            SLOT_7 = 0
    if not SLOT_21:
        SLOT_6 = 0
        callSubroutine('MagicReset')
        callSubroutine('StockMagicReset')
        callSubroutine('MagicReductionClear')
        callSubroutine('ActiveMagicAllDelete')


@Subroutine
def OnPreDraw():
    CallPrivateFunction('PH_Light', 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActStand():
    label(0)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(0, 2, 123):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('ph001_00', 7)
    SLOT_88 = 960
    Voiceline('ph000')
    sprite('ph001_01', 7)
    sprite('ph001_02', 7)
    CreateObject('ph001Eff', -1)
    CommonSE('015_blaze_2')
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    label(1)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_02', 7)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    loopRest()
    gotoLabel(1)


@State
def CmnActStandTurn():
    sprite('ph003_00', 3)
    sprite('ph003_01', 3)
    sprite('ph003_00ex01', 3)


@State
def CmnActStand2Crouch():
    sprite('ph010_00', 4)
    sprite('ph010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('ph010_02', 6)
    sprite('ph010_03', 6)
    sprite('ph010_04', 6)
    sprite('ph010_05', 6)
    sprite('ph010_06', 6)
    sprite('ph010_07', 6)
    sprite('ph010_08', 6)
    sprite('ph010_09', 6)
    sprite('ph010_10', 6)
    sprite('ph010_11', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('ph013_00', 3)
    sprite('ph013_01', 3)
    sprite('ph013_00ex01', 3)


@State
def CmnActCrouch2Stand():
    sprite('ph010_01', 4)
    sprite('ph010_00', 4)


@State
def CmnActJumpPre():
    sprite('ph023_00', 2)
    sprite('ph023_01', 2)


@State
def CmnActJumpUpper():
    label(0)
    sprite('ph020_00', 4)
    sprite('ph020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('ph020_02', 3)
    sprite('ph020_03', 3)
    sprite('ph020_04', 3)


@State
def CmnActJumpDown():
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('ph024_00', 2)
    sprite('ph024_01', 2)
    sprite('ph024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def CmnActFWalk():
    sprite('ph030_00', 7)
    label(0)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('ph031_00', 7)
    label(0)
    sprite('ph031_01', 7)
    sprite('ph031_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_03', 7)
    sprite('ph031_04', 7)
    sprite('ph031_05', 7)
    sprite('ph031_06', 7)
    sprite('ph031_07', 7)
    sprite('ph031_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_09', 7)
    sprite('ph031_10', 7)
    sprite('ph031_11', 7)
    sprite('ph031_12', 7)
    loopRest()
    gotoLabel(0)


@Subroutine
def DashEndFunc():
    AlphaValue(0)
    ConstantAlphaModifier(42)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    EndMomentum(1)


@Subroutine
def __2ndDashInputFB():
    BeginBuffer('2ndDash66')
    BeginBuffer('2ndDash44')


@Subroutine
def __2ndDashInputUD():
    BeginBuffer('2ndDash22')
    BeginBuffer('2ndDash88')


@Subroutine
def __2ndDashBegin():
    if not SLOT_51:
        BufferedOrPressedGoto('2ndDash66')
        BufferedOrPressedGoto('2ndDash44')
        BufferedOrPressedGoto('2ndDash22')
        BufferedOrPressedGoto('2ndDash88')


@Subroutine
def __2ndDashClear():
    setInvincible(0)
    DisallowGoto('2ndDash66')
    DisallowGoto('2ndDash44')
    DisallowGoto('2ndDash22')
    DisallowGoto('2ndDash88')


@State
def CmnActFDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')

        def upon_EVERY_FRAME():
            if CheckInput(INPUT_PRESS_A):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_B):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_C):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_D):
                SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph032_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    callSubroutine('2ndDashInputUD')
    sprite('ph032_01', 2)
    sprite('ph032_02', 3)
    SpecificInvincibility(1, 1, 1, 1, 1)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    callSubroutine('2ndDashInputFB')
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(60000)
    sprite('ph032_04', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph032FireEff2', -1)
    sprite('ph032_02', 3)
    sprite('ph032_03', 3)
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    callSubroutine('2ndDashClear')
    sprite('ph032_05', 3)
    sprite('ph032_06', 2)


@State
def CmnActFDashStop():
    pass


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        NegativeForBackDash()
        EnterStateIfEventID(8, '_NEUTRAL')

        def upon_EVERY_FRAME():
            if CheckInput(INPUT_PRESS_A):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_B):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_C):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_D):
                SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph032_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    callSubroutine('2ndDashInputUD')
    sprite('ph032_01', 2)
    sprite('ph032_02', 3)
    SpecificInvincibility(1, 1, 1, 1, 1)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    callSubroutine('2ndDashInputFB')
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(-50000)
    sprite('ph032_04', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph032FireEff2', -1)
    sprite('ph032_02', 3)
    sprite('ph032_03', 3)
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    callSubroutine('2ndDashClear')
    sprite('ph032_05', 3)
    sprite('ph032_06', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    pass


@State
def SpDashF_Air():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        ModifyVar_(8, 2, 7, 0, 1)
        Unknown2061(1)

        def upon_EVERY_FRAME():
            if CheckInput(INPUT_PRESS_A):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_B):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_C):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_D):
                SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph035_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    EndMomentum(1)
    callSubroutine('2ndDashInputUD')
    sprite('ph035_01', 2)
    sprite('ph035_01', 1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('ph035_02', 3)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    sprite('null', 5)
    callSubroutine('2ndDashInputFB')
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(80000)
    sprite('ph035_03', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    sprite('ph035_04', 3)
    callSubroutine('2ndDashBegin')
    sprite('ph035_05', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    callSubroutine('2ndDashClear')
    EndYPhysicsImpulse()
    sprite('ph035_06', 2)


@State
def CmnActAirBDash():
    pass


@State
def SpDashB_Air():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        ModifyVar_(8, 2, 7, 0, 1)
        Unknown2061(1)

        def upon_EVERY_FRAME():
            if CheckInput(INPUT_PRESS_A):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_B):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_C):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_D):
                SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph035_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    EndMomentum(1)
    callSubroutine('2ndDashInputUD')
    sprite('ph035_01', 2)
    sprite('ph035_01', 1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('ph035_02', 3)
    SpecificInvincibility(1, 1, 1, 1, 1)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    sprite('null', 5)
    callSubroutine('2ndDashInputFB')
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(-80000)
    sprite('ph035_03', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    sprite('ph035_04', 3)
    callSubroutine('2ndDashBegin')
    sprite('ph035_05', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    callSubroutine('2ndDashClear')
    EndYPhysicsImpulse()
    sprite('ph035_06', 2)


@State
def Swoop():

    def upon_IMMEDIATE():
        EnterStateIfEventID(8, '_NEUTRAL')
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        ModifyVar_(8, 2, 7, 0, 1)
        Unknown2061(1)

        def upon_EVERY_FRAME():
            if CheckInput(INPUT_PRESS_A):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_B):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_C):
                SLOT_51 = 1
            if CheckInput(INPUT_PRESS_D):
                SLOT_51 = 1

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph035_00', 3)
    sprite('ph035_01', 1)
    sprite('ph035_01', 2)
    sprite('ph035_02', 4)
    EndMomentum(1)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    sprite('ph035_03', 4)
    callSubroutine('2ndDashInputUD')
    sprite('null', 2)
    physicsYImpulse(-20000)
    EnableCollision(0)
    sprite('null', 3)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    YAccel(600)
    callSubroutine('2ndDashInputFB')
    sprite('null', 4)
    PushSpeedX()
    PushSpeedY()
    XImpulseAcceleration(0)
    sprite('null', 1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(101)
    label(1)
    sprite('ph032_03', 4)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 4)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    physicsXImpulse(0)
    EndYPhysicsImpulse()
    sprite('ph032_05', 4)
    SmartVoiceline('ph005')
    callSubroutine('2ndDashClear')
    sprite('ph032_06', 4)
    ExitState()
    label(101)
    sprite('ph035_03', 4)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    callSubroutine('2ndDashBegin')
    sprite('ph035_04', 4)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    physicsXImpulse(0)
    EndYPhysicsImpulse()
    sprite('ph035_05', 4)
    SmartVoiceline('ph005')
    callSubroutine('2ndDashClear')
    sprite('ph035_06', 4)
    ExitState()


@State
def __2ndDash66():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        EndMomentum(1)
        Unknown2061(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        setInvincible(1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(100)
    sprite('ph032_02', 3)
    DespawnEAEffect('ph032FireEff2')
    CreateObject('ph032FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    if PreviousStateCheck('CmnActFDash'):
        physicsXImpulse(60000)
        XImpulseAcceleration(75)
    else:
        physicsXImpulse(50000)
    sprite('ph032_04', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_02', 3)
    sprite('ph032_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('ph032_05', 3)
    sprite('ph032_06', 3)
    ExitState()
    label(100)
    sprite('ph035_02', 3)
    DespawnEAEffect('ph035FireEff2')
    CreateObject('ph035FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph035_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(40000)
    sprite('ph035_02', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndYPhysicsImpulse()
    sprite('ph035_05', 3)
    sprite('ph035_06', 3)


@State
def __2ndDash44():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        EndMomentum(1)
        Unknown2061(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        setInvincible(1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(100)
    sprite('ph032_02', 3)
    DespawnEAEffect('ph032FireEff2')
    CreateObject('ph032FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    if PreviousStateCheck('CmnActBDash'):
        physicsXImpulse(-50000)
        XImpulseAcceleration(75)
    else:
        physicsXImpulse(-60000)
    sprite('ph032_04', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_02', 3)
    sprite('ph032_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('ph032_05', 3)
    sprite('ph032_06', 3)
    ExitState()
    label(100)
    sprite('ph035_02', 3)
    DespawnEAEffect('ph035FireEff2')
    CreateObject('ph035FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph035_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsXImpulse(-40000)
    sprite('ph035_02', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndYPhysicsImpulse()
    sprite('ph035_05', 3)
    sprite('ph035_06', 3)


@State
def __2ndDash22():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        EndMomentum(1)
        Unknown2061(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
        setInvincible(1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(100)
    sprite('ph032_02', 3)
    DespawnEAEffect('ph032FireEff2')
    CreateObject('ph032FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph032_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    label(1)
    sprite('ph032_02', 3)
    callSubroutine('DashEndFunc')
    CreateObject('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    physicsXImpulse(0)
    sprite('ph032_05', 3)
    sprite('ph032_06', 3)
    ExitState()
    label(100)
    sprite('ph035_02', 3)
    DespawnEAEffect('ph035FireEff2')
    CreateObject('ph035FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    clearUponHandler(LANDING)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph035_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('null', 4)
    physicsYImpulse(-80000)
    sprite('null', 1)
    EndMomentum(1)
    AddY(-80000)
    if SLOT_IsGrounded:
        conditionalSendToLabel(1)
    sprite('ph035_02', 3)
    ForceFaceSprite()
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('ph035_05', 3)
    EndYPhysicsImpulse()
    sprite('ph035_06', 3)


@State
def __2ndDash88():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        NegativeForBackDash()
        AddAirDashCount(-1)
        AddAirJumpCount(-1)
        ModifyVar_(8, 2, 7, 0, 1)
        EndMomentum(1)
        Unknown2061(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            AddAirDashCount(-1)
            AddAirJumpCount(-1)
            ModifyVar_(8, 2, 7, 0, 1)
        setInvincible(1)
    if SLOT_IsAirborne:
        conditionalSendToLabel(100)
    sprite('ph032_02', 3)
    DespawnEAEffect('ph032FireEff2')
    CreateObject('ph032FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph032_03', 3)
    sprite('ph032_04', 3)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph032_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph032_03', 3)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsYImpulse(75200)
    loopRest()
    gotoLabel(101)
    label(100)
    sprite('ph035_02', 3)
    DespawnEAEffect('ph035FireEff2')
    CreateObject('ph035FireEff2', -1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    EndMomentum(1)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    CreateObject('ph035FireEff', -1)
    CommonSE('000_airdash_0')
    sprite('ph035_02', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    sprite('ph035_03', 3)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    SetXCollisionFromOrigin(40)
    physicsYImpulse(40000)
    label(101)
    sprite('ph035_02', 3)
    ForceFaceSprite()
    callSubroutine('DashEndFunc')
    CreateObject('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)
    sprite('ph035_04', 3)
    SmartVoiceline('ph005')
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('ph035_05', 3)
    EndYPhysicsImpulse()
    sprite('ph035_06', 3)


@State
def CmnActHitStandLv1():
    sprite('ph050_00', 1)
    sprite('ph050_01', 1)
    sprite('ph050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('ph050_01', 1)
    sprite('ph050_02', 1)
    sprite('ph050_01', 2)
    sprite('ph050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('ph050_02', 1)
    sprite('ph050_03', 1)
    sprite('ph050_02', 2)
    sprite('ph050_01', 2)
    sprite('ph050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('ph050_03', 1)
    sprite('ph050_04', 1)
    sprite('ph050_03', 2)
    sprite('ph050_02', 2)
    sprite('ph050_01', 2)
    sprite('ph050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('ph050_04', 1)
    sprite('ph050_04', 1)
    sprite('ph050_04', 2)
    sprite('ph050_03', 2)
    sprite('ph050_02', 2)
    sprite('ph050_01', 2)
    sprite('ph050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('ph052_00', 1)
    sprite('ph052_01', 1)
    sprite('ph052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('ph052_01', 1)
    sprite('ph052_02', 1)
    sprite('ph052_01', 2)
    sprite('ph052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('ph052_02', 1)
    sprite('ph052_03', 1)
    sprite('ph052_02', 2)
    sprite('ph052_01', 2)
    sprite('ph052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('ph052_03', 1)
    sprite('ph052_04', 1)
    sprite('ph052_03', 2)
    sprite('ph052_02', 2)
    sprite('ph052_01', 2)
    sprite('ph052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('ph052_04', 1)
    sprite('ph052_04', 1)
    sprite('ph052_04', 2)
    sprite('ph052_03', 2)
    sprite('ph052_02', 2)
    sprite('ph052_01', 2)
    sprite('ph052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('ph054_00', 1)
    sprite('ph054_01', 1)
    sprite('ph054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('ph054_01', 1)
    sprite('ph054_02', 1)
    sprite('ph054_01', 2)
    sprite('ph054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('ph054_02', 1)
    sprite('ph054_03', 1)
    sprite('ph054_02', 2)
    sprite('ph054_01', 2)
    sprite('ph054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('ph054_03', 1)
    sprite('ph054_04', 1)
    sprite('ph054_03', 2)
    sprite('ph054_02', 2)
    sprite('ph054_01', 2)
    sprite('ph054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('ph054_04', 1)
    sprite('ph054_04', 1)
    sprite('ph054_04', 2)
    sprite('ph054_03', 2)
    sprite('ph054_02', 2)
    sprite('ph054_01', 2)
    sprite('ph054_00', 2)


@State
def CmnActBDownUpper():
    sprite('ph060_00', 4)
    label(0)
    sprite('ph060_01', 4)
    sprite('ph060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('ph060_03', 4)


@State
def CmnActBDownDown():
    sprite('ph060_04', 4)
    label(0)
    sprite('ph060_05', 4)
    sprite('ph060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('ph060_07', 2)
    sprite('ph060_08', 2)


@State
def CmnActBDownBound():
    sprite('ph060_09', 3)
    sprite('ph060_10', 3)
    sprite('ph060_11', 3)
    sprite('ph060_12', 3)
    sprite('ph060_13', 3)


@State
def CmnActBDownLoop():
    sprite('ph060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('ph061_00', 3)
    sprite('ph061_01', 3)
    sprite('ph061_02', 3)
    sprite('ph061_03', 3)
    sprite('ph061_04', 3)
    sprite('ph061_05', 3)
    sprite('ph061_06', 2)
    sprite('ph061_07', 2)
    sprite('ph061_08', 2)
    sprite('ph061_09', 2)


@State
def CmnActFDownUpper():
    sprite('ph063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('ph063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('ph063_02', 3)
    sprite('ph063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('ph063_04', 3)
    sprite('ph063_05', 3)


@State
def CmnActFDownBound():
    sprite('ph063_06', 2)
    sprite('ph063_07', 2)
    sprite('ph063_08', 3)
    sprite('ph063_09', 3)
    sprite('ph063_10', 3)


@State
def CmnActFDownLoop():
    sprite('ph063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('ph064_00', 2)
    sprite('ph064_01', 2)
    sprite('ph064_02', 2)
    sprite('ph061_02', 2)
    sprite('ph061_03', 2)
    sprite('ph061_04', 2)
    sprite('ph061_05', 2)
    sprite('ph061_06', 2)
    sprite('ph061_07', 2)
    sprite('ph061_08', 2)
    sprite('ph061_09', 2)


@State
def CmnActVDownUpper():
    sprite('ph062_00', 3)
    label(0)
    sprite('ph062_01', 3)
    sprite('ph062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('ph062_03', 3)
    sprite('ph062_04', 3)


@State
def CmnActVDownDown():
    sprite('ph062_05', 3)
    sprite('ph062_06', 3)
    label(0)
    sprite('ph062_07', 3)
    sprite('ph062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('ph062_09', 2)
    sprite('ph062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('ph062_09', 2)
    sprite('ph062_10', 2)


@State
def CmnActBlowoff():
    sprite('ph072_00', 3)
    sprite('ph072_01', 3)
    sprite('ph072_02', 3)
    label(0)
    sprite('ph072_01', 3)
    sprite('ph072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ph074_00', 3)
    sprite('ph074_01', 3)
    sprite('ph074_02', 3)
    sprite('ph074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('ph082_00', 2)
    sprite('ph082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('ph071_04', 1)


@State
def CmnActWallBound():
    sprite('ph073_00', 3)
    sprite('ph073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('ph073_02', 3)
    label(0)
    sprite('ph073_03', 3)
    sprite('ph073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('ph070_00', 3)
    sprite('ph070_01', 3)
    label(0)
    sprite('ph070_02', 4)
    sprite('ph070_03', 4)
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('ph070_04', 4)
    sprite('ph070_05', 4)
    sprite('ph070_06', 4)
    sprite('ph070_07', 4)
    sprite('ph070_08', 4)
    sprite('ph070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('ph070_10', 2)
    sprite('ph070_11', 2)
    sprite('ph070_12', 2)
    sprite('ph070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('ph113_00', 3)
    sprite('ph113_01', 3)
    sprite('ph113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('ph113_00', 3)
    sprite('ph113_01', 3)
    sprite('ph113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('ph113_00', 3)
    sprite('ph113_01', 3)
    sprite('ph113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('ph110_00', 2)
    sprite('ph110_01', 2)
    sprite('ph110_02', 2)
    sprite('ph110_03', 2)
    sprite('ph110_04', 2)
    sprite('ph110_05', 2)
    sprite('ph110_06', 2)
    sprite('ph110_07', 200)
    sprite('ph110_08', 3)
    sprite('ph110_09', 3)


@State
def CmnActUkemiLandB():
    sprite('ph111_00', 2)
    sprite('ph111_01', 2)
    sprite('ph111_02', 2)
    sprite('ph111_03', 2)
    sprite('ph111_04', 2)
    sprite('ph111_05', 2)
    sprite('ph111_06', 2)
    sprite('ph111_07', 200)
    sprite('ph111_08', 3)
    sprite('ph111_09', 3)


@State
def CmnActUkemiLandN():
    sprite('ph112_00', 2)
    sprite('ph112_01', 2)
    sprite('ph112_02', 3)
    sprite('ph112_03', 3)
    sprite('ph112_04', 3)
    sprite('ph112_05', 3)
    sprite('ph112_06', 3)
    sprite('ph112_07', 3)
    sprite('ph112_08', 3)
    sprite('ph112_09', 3)


@State
def CmnActUkemiLandNLanding():
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('ph040_00', 3)
    sprite('ph040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ph040_02', 3)
    sprite('ph040_03', 3)
    sprite('ph040_04', 3)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('ph040_01', 3)
    sprite('ph040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('ph040_05', 3)
    label(0)
    sprite('ph040_02', 3)
    sprite('ph040_03', 3)
    sprite('ph040_04', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('ph040_01', 3)
    sprite('ph040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('ph041_00', 3)
    sprite('ph041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ph041_02', 3)
    sprite('ph041_03', 3)
    sprite('ph041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('ph041_01', 3)
    sprite('ph041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('ph041_05', 3)
    label(0)
    sprite('ph041_02', 3)
    sprite('ph041_03', 3)
    sprite('ph041_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('ph041_01', 3)
    sprite('ph041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('ph043_00', 3)
    sprite('ph043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ph043_02', 3)
    sprite('ph043_03', 3)
    sprite('ph043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('ph043_01', 3)
    sprite('ph043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ph043_05', 3)
    label(0)
    sprite('ph043_02', 3)
    sprite('ph043_03', 3)
    sprite('ph043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ph043_01', 3)
    sprite('ph043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('ph045_00', 3)
    sprite('ph045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ph045_02', 3)
    sprite('ph045_03', 3)
    sprite('ph045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('ph045_01', 3)
    sprite('ph045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('ph045_05', 3)
    label(0)
    sprite('ph045_02', 3)
    sprite('ph045_03', 3)
    sprite('ph045_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('ph045_01', 3)
    sprite('ph045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('ph090_00', 2)
    sprite('ph090_01', 2)
    sprite('ph090_02', 1)
    SetCommonActionMark(1)
    sprite('ph090_03', 6)
    sprite('ph090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('ph091_00', 2)
    sprite('ph091_01', 2)
    sprite('ph091_02', 1)
    SetCommonActionMark(1)
    sprite('ph091_03', 6)
    sprite('ph091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('ph092_00', 2)
    sprite('ph092_01', 2)
    sprite('ph092_02', 1)
    SetCommonActionMark(1)
    sprite('ph092_03', 6)
    sprite('ph092_04', 6)


@State
def CmnActAirTurn():
    sprite('ph025_00', 4)
    sprite('ph025_01', 4)
    sprite('ph025_00ex01', 4)


@State
def CmnActLockWait():
    sprite('ph040_02', 1)
    sprite('ph040_01', 3)
    sprite('ph040_00', 3)


@State
def CmnActLockReject():
    sprite('ph312_00', 3)
    sprite('ph312_01', 5)
    sprite('ph312_02', 5)
    sprite('ph312_03', 3)
    sprite('ph312_04', 3)
    sprite('ph312_05', 3)
    sprite('ph312_06', 2)
    sprite('ph312_07', 2)
    sprite('ph312_08', 2)
    sprite('ph312_09', 2)


@State
def CmnActAirLockWait():
    sprite('ph045_02', 1)
    sprite('ph045_01', 3)
    sprite('ph045_00', 3)


@State
def CmnActAirLockReject():
    sprite('ph322_00', 4)
    sprite('ph322_01', 4)
    sprite('ph322_02', 4)
    sprite('ph322_03', 3)
    sprite('ph322_04', 3)
    sprite('ph322_05', 3)
    sprite('ph322_06', 2)
    sprite('ph322_07', 2)
    sprite('ph322_08', 2)
    sprite('ph322_09', 3)


@State
def CmnActLandSpin():
    sprite('ph071_00', 4)
    sprite('ph071_01', 4)
    label(0)
    sprite('ph071_02', 2)
    sprite('ph071_03', 2)
    sprite('ph071_04', 2)
    sprite('ph071_05', 2)
    sprite('ph071_06', 2)
    sprite('ph071_07', 2)
    sprite('ph071_08', 2)
    sprite('ph071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('ph071_10', 6)
    sprite('ph071_11', 5)
    sprite('ph071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('ph071_02', 2)
    sprite('ph071_03', 2)
    sprite('ph071_04', 2)
    sprite('ph071_05', 2)
    sprite('ph071_06', 2)
    sprite('ph071_07', 2)
    sprite('ph071_08', 2)
    sprite('ph071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('ph077_00', 2)
    sprite('ph077_01', 2)
    sprite('ph077_00ex01', 2)
    sprite('ph077_01ex01', 2)
    sprite('ph077_00ex02', 2)
    sprite('ph077_01ex02', 2)
    sprite('ph077_00ex03', 2)
    sprite('ph077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('ph077_02', 4)
    label(0)
    sprite('ph077_03', 3)
    sprite('ph077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('ph077_05', 5)
    sprite('ph077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ph060_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('ph060_12', 4)
    sprite('ph060_13', 5)


@State
def CmnActBurstBegin():
    sprite('ph331_00', 2)
    sprite('ph331_01', 2)
    label(0)
    sprite('ph331_02', 3)
    sprite('ph331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('ph331_04', 2)
    sprite('ph331_05', 2)
    label(0)
    sprite('ph331_06', 3)
    sprite('ph331_07', 3)
    sprite('ph331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('ph331_09', 3)
    sprite('ph331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('ph331_11', 2)
    sprite('ph331_12', 2)
    label(0)
    sprite('ph331_02', 3)
    sprite('ph331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('ph331_04', 2)
    sprite('ph331_05', 2)
    label(0)
    sprite('ph331_06', 3)
    sprite('ph331_07', 3)
    sprite('ph331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('ph331_13', 3)
    sprite('ph331_14', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('ph333_00', 3)
    sprite('ph333_01', 3)
    sprite('ph333_02', 3)
    CharacterFlash(16639, 20, 1)
    CreateObject('ph333_arm', 100)
    sprite('ph333_03', 32767)
    CreateObject('EMB_PH_OD', 0)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('ph333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('ph333_05', 3)
    sprite('ph333_06', 3)
    sprite('ph333_07', 3)
    label(0)
    sprite('ph333_05', 3)
    sprite('ph333_06', 3)
    sprite('ph333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('ph333_08', 6)
    DespawnEAEffect('ph333_arm')
    sprite('ph333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('ph333_10', 3)
    sprite('ph333_11', 3)
    sprite('ph333_12', 3)
    CharacterFlash(16639, 20, 1)
    CreateObject('ph333_arm', 100)
    sprite('ph333_13', 32767)
    CreateObject('EMB_PH_OD', 0)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('ph333_14', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('ph333_05', 3)
    sprite('ph333_06', 3)
    sprite('ph333_07', 3)
    label(0)
    sprite('ph333_05', 3)
    sprite('ph333_06', 3)
    sprite('ph333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('ph333_15', 6)
    DespawnEAEffect('ph333_arm')
    sprite('ph333_16', 6)


@Subroutine
def ChainRoute5_A():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute5_B():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute5_C():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute2_A():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute2_B():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute2_C():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute3():
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    callSubroutine('MagicChainLand')


@Subroutine
def ChainRoute4_A():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')


@Subroutine
def ChainRoute4_B():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')


@Subroutine
def ChainRoute4_C():
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk4B')
    HitOrBlockCancel('NmlAtk4C')
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk5C')
    HitOrBlockCancel('NmlAtk6A')
    HitOrBlockCancel('NmlAtk6B')
    HitOrBlockCancel('NmlAtk6C')
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    HitOrBlockCancel('NmlAtk3C')
    callSubroutine('MagicChainLand')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')


@Subroutine
def ChainRoute6_A():
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    callSubroutine('MagicChainLand')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRoute6_B():
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    callSubroutine('MagicChainLand')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRoute6_C():
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    callSubroutine('MagicChainLand')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR5_A():
    HitOrBlockCancel('NmlAtkAIR5A')
    HitOrBlockCancel('NmlAtkAIR5B')
    HitOrBlockCancel('NmlAtkAIR5C')
    HitOrBlockCancel('NmlAtkAIR2A')
    HitOrBlockCancel('NmlAtkAIR2B')
    HitOrBlockCancel('NmlAtkAIR2C')
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR5_B():
    HitOrBlockCancel('NmlAtkAIR5A')
    HitOrBlockCancel('NmlAtkAIR5B')
    HitOrBlockCancel('NmlAtkAIR5C')
    HitOrBlockCancel('NmlAtkAIR2A')
    HitOrBlockCancel('NmlAtkAIR2B')
    HitOrBlockCancel('NmlAtkAIR2C')
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR5_C():
    HitOrBlockCancel('NmlAtkAIR5A')
    HitOrBlockCancel('NmlAtkAIR5B')
    HitOrBlockCancel('NmlAtkAIR5C')
    HitOrBlockCancel('NmlAtkAIR2A')
    HitOrBlockCancel('NmlAtkAIR2B')
    HitOrBlockCancel('NmlAtkAIR2C')
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR2_A():
    PrivateFunction(9, 2, 6, 0, 1, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR2_B():
    PrivateFunction(9, 2, 6, 0, 2, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def ChainRouteAIR2_C():
    PrivateFunction(9, 2, 6, 0, 4, 2, 52)
    callSubroutine('MagicChainAir')
    HitOrBlockJumpCancel(1)


@Subroutine
def MagicNormalAtkInit():
    HitAirUnblockable(0)
    ProjectileLevel(1)
    PassByArmor(1)
    SLOT_54 = 0
    if SLOT_OverdriveTimer:
        SLOT_54 = 1

    def upon_14():
        clearUponHandler(14)
        SLOT_54 = 0

    def upon_OPPONENT_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_HIT_OR_BLOCK)
        if not SLOT_2:
            callSubroutine('MagicTableUpDate')

    def upon_16():
        if SLOT_2:
            clearUponHandler(16)
            callSubroutine('MagicTableUpDate')


@Subroutine
def PowerUpFlashBlue():
    if SLOT_52:
        CharacterFlash(2105599, 5, 2)


@Subroutine
def PowerUpFlashGreen():
    if SLOT_52:
        CharacterFlash(2146336, 5, 2)


@Subroutine
def PowerUpFlashRed():
    if SLOT_52:
        CharacterFlash(16719904, 5, 2)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        UseSlashHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute5_A')
        SLOT_55 = 1
        HitOrBlockJumpCancel(1)
        if SLOT_52:
            Damage(720)
            ChipPercentage(5)
    sprite('ph200_00', 3)
    sprite('ph200_01', 3)
    callSubroutine('PowerUpFlashBlue')
    sprite('ph200_02', 2)
    RandomCommonVoiceline(1)
    sprite('ph200_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph200_eff', -1)
    PrivateSE('phse_00')
    sprite('ph200_03', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ph200_04', 5)
    sprite('ph200_05', 5)
    sprite('ph200_06', 5)
    sprite('ph200_07', 5)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        UseSlashHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute5_B')
        SLOT_55 = 2
        HitOrBlockJumpCancel(1)
        if SLOT_52:
            Damage(720)
            ChipPercentage(5)
    sprite('ph201_00', 3)
    sprite('ph201_01', 3)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph201_02', 3)
    sprite('ph201_03', 2)
    SmartVoiceline('ph109')
    sprite('ph201_04', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph201_eff', -1)
    PrivateSE('phse_01')
    sprite('ph201_05', 3)
    sprite('ph201_06', 6)
    Recovery()
    Unknown2063()
    sprite('ph201_07', 5)
    sprite('ph201_08', 5)
    sprite('ph201_09', 5)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        UseFireHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute5_C')
        SLOT_55 = 4
        HitOrBlockJumpCancel(1)
        if SLOT_52:
            Damage(720)
            ChipPercentage(5)
    sprite('ph202_00', 3)
    sprite('ph202_01', 4)
    callSubroutine('PowerUpFlashRed')
    sprite('ph202_02', 4)
    RandomCommonVoiceline(1)
    sprite('ph202_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph202_eff', -1)
    PrivateSE('phse_02')
    sprite('ph202_03', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ph202_04', 6)
    sprite('ph202_05', 6)
    sprite('ph202_06', 5)
    sprite('ph202_07', 5)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('ph203_00', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@State
def AN_NmlAtk5D_Lv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('ph204_00', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@State
def AN_NmlAtk5D_Lv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('ph205_00', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@Subroutine
def ActivateMagicSelect():
    if SLOT_31 == 0:
        enterState('NmlAtkDrive_NNN')
    if SLOT_31 == 1:
        enterState('NmlAtkDrive_BNN')
    if SLOT_31 == 16:
        enterState('NmlAtkDrive_GNN')
    if SLOT_31 == 256:
        enterState('NmlAtkDrive_RNN')
    if SLOT_31 == 2:
        enterState('NmlAtkDrive_BBN')
    if SLOT_31 == 32:
        enterState('NmlAtkDrive_GGN')
    if SLOT_31 == 512:
        enterState('NmlAtkDrive_RRN')
    if SLOT_31 == 17:
        enterState('NmlAtkDrive_BGN')
    if SLOT_31 == 257:
        enterState('NmlAtkDrive_BRN')
    if SLOT_31 == 272:
        enterState('NmlAtkDrive_GRN')
    if SLOT_31 == 3:
        enterState('NmlAtkDrive_BBB')
    if SLOT_31 == 48:
        enterState('NmlAtkDrive_GGG')
    if SLOT_31 == 768:
        enterState('NmlAtkDrive_RRR')
    if SLOT_31 == 513:
        enterState('NmlAtkDrive_RRB')
    if SLOT_31 == 528:
        enterState('NmlAtkDrive_RRG')
    if SLOT_31 == 288:
        enterState('NmlAtkDrive_GGR')
    if SLOT_31 == 33:
        enterState('NmlAtkDrive_GGB')
    if SLOT_31 == 258:
        enterState('NmlAtkDrive_BBR')
    if SLOT_31 == 18:
        enterState('NmlAtkDrive_BBG')
    if SLOT_31 == 273:
        enterState('NmlAtkDrive_BGR')


@Subroutine
def MagicInitialize():
    if SLOT_IsAirborne:
        AttackDefaults_AirNormal()
        EndMomentum(1)
        CreateObject('Eff_DriveMagicCircle', -1)
    else:
        AttackDefaults_StandingNormal()
    SpecialCancel(0)


@State
def NmlAtkDrive_NNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 0
        SpecialCancel(1)
    sprite('ph203_05', 2)
    SmartVoiceline('ph300')
    sprite('ph203_06', 2)
    sprite('ph203_07', 5)
    CreateObject('DriveAtk_NNN', -1)
    callSubroutine('MagicReset')
    sprite('ph203_08', 5)
    EndYPhysicsImpulse()
    sprite('ph203_09', 5)
    sprite('ph203_10', 5)
    sprite('ph203_11', 5)
    EndYPhysicsImpulse()
    sprite('ph203_12', 5)
    SpriteCall('ph203_15', 5, 2, 36)
    sprite('ph203_13', 5)
    SpriteCall('ph203_16', 5, 2, 36)


@State
def NmlAtkDrive_RNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 4, 2, 52)
        SLOT_53 = 256
        SpecialCancel(1)
    sprite('ph203_04', 2)
    SmartVoiceline('ph301')
    callSubroutine('PowerUpFlashRed')
    sprite('ph203_05', 2)
    sprite('ph203_06', 2)
    sprite('ph203_07', 2)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_RNN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph203_08', 3)
    sprite('ph203_09', 3)
    sprite('ph203_10', 3)
    sprite('ph203_08', 3)
    sprite('ph203_11', 3)
    sprite('ph203_12', 3)
    SpriteCall('ph203_15', 3, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph203_13', 3)
    SpriteCall('ph203_16', 3, 2, 36)


@State
def NmlAtkDrive_GNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 2, 2, 52)
        SLOT_53 = 16
        SpecialCancel(1)
    sprite('ph203_01', 2)
    SmartVoiceline('ph303')
    callSubroutine('PowerUpFlashGreen')
    CreateObject('Wind_Herald', -1)
    sprite('ph203_04', 3)
    sprite('ph203_05', 3)
    sprite('ph203_06', 2)
    sprite('ph203_07', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_GNN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph203_08', 3)
    sprite('ph203_09', 3)
    sprite('ph203_10', 3)
    sprite('ph203_08', 3)
    sprite('ph203_11', 4)
    sprite('ph203_12', 4)
    SpriteCall('ph203_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph203_13', 4)
    SpriteCall('ph203_16', 4, 2, 36)


@State
def NmlAtkDrive_BNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 1, 2, 52)
        SLOT_53 = 1
        SpecialCancel(1)
    sprite('ph203_04', 2)
    SmartVoiceline('ph302')
    callSubroutine('PowerUpFlashBlue')
    sprite('ph203_05', 2)
    sprite('ph203_06', 2)
    sprite('ph203_07', 4)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_BNN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph203_08', 5)
    sprite('ph203_09', 5)
    sprite('ph203_11', 4)
    sprite('ph203_12', 4)
    SpriteCall('ph203_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph203_13', 4)
    SpriteCall('ph203_16', 4, 2, 36)


@State
def NmlAtkDrive_RRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 4, 2, 52)
        SLOT_53 = 512
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph204_01', 2)
    SpriteCall('ph204_14', 2, 2, 36)
    SmartVoiceline('ph304')
    callSubroutine('PowerUpFlashRed')
    sprite('ph204_02', 2)
    sprite('ph204_05', 1)
    sprite('ph204_06', 1)
    sprite('ph204_07', 2)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_RRN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 3)
    XImpulseAcceleration(50)
    sprite('ph204_09', 3)
    XImpulseAcceleration(50)
    sprite('ph204_10', 3)
    sprite('ph204_11', 3)
    XImpulseAcceleration(50)
    sprite('ph204_12', 3)
    XImpulseAcceleration(0)
    sprite('ph212_11', 3)
    SpriteCall('ph204_15', 3, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 3)
    SpriteCall('ph204_16', 3, 2, 36)


@State
def NmlAtkDrive_GGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 2, 2, 52)
        SLOT_53 = 32
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph204_01', 3)
    SpriteCall('ph204_14', 3, 2, 36)
    SmartVoiceline('ph306')
    callSubroutine('PowerUpFlashGreen')
    CreateObject('Wind_Herald', -1)
    sprite('ph204_02', 2)
    sprite('ph204_05', 3)
    sprite('ph204_06', 2)
    sprite('ph204_07', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_GGN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 3)
    XImpulseAcceleration(50)
    sprite('ph204_09', 3)
    XImpulseAcceleration(50)
    sprite('ph204_10', 3)
    XImpulseAcceleration(50)
    sprite('ph204_11', 3)
    XImpulseAcceleration(50)
    sprite('ph204_12', 4)
    XImpulseAcceleration(0)
    sprite('ph212_11', 4)
    SpriteCall('ph204_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 4)
    SpriteCall('ph204_16', 4, 2, 36)


@State
def NmlAtkDrive_BBN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 1, 2, 52)
        SLOT_53 = 2
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph204_01', 2)
    SpriteCall('ph204_14', 2, 2, 36)
    SmartVoiceline('ph305')
    callSubroutine('PowerUpFlashBlue')
    sprite('ph204_02', 2)
    sprite('ph204_05', 1)
    sprite('ph204_06', 1)
    sprite('ph204_07', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_BBN', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 3)
    XImpulseAcceleration(50)
    sprite('ph204_09', 3)
    XImpulseAcceleration(50)
    sprite('ph204_11', 3)
    XImpulseAcceleration(50)
    sprite('ph204_12', 4)
    XImpulseAcceleration(0)
    sprite('ph212_11', 5)
    SpriteCall('ph204_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 5)
    SpriteCall('ph204_16', 5, 2, 36)


@State
def NmlAtkDrive_BGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 17
        PreventBlocking(1)
    sprite('ph204_01', 3)
    SpriteCall('ph204_14', 3, 2, 36)
    SmartVoiceline('ph309')
    callSubroutine('BGN_Delete')
    sprite('ph204_05', 3)
    sprite('ph204_06', 3)
    sprite('ph204_07', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_BGN', -1)
    RegisterObject(7, 1)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 4)
    XImpulseAcceleration(50)
    sprite('ph204_09', 4)
    XImpulseAcceleration(50)
    sprite('ph204_10', 4)
    XImpulseAcceleration(50)
    sprite('ph204_11', 4)
    XImpulseAcceleration(50)
    sprite('ph204_12', 4)
    XImpulseAcceleration(0)
    sprite('ph212_11', 4)
    SpriteCall('ph204_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 4)
    SpriteCall('ph204_16', 4, 2, 36)


@State
def NmlAtkDrive_BRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 257
        PreventBlocking(1)
    sprite('ph204_01', 3)
    SpriteCall('ph204_14', 3, 2, 36)
    SmartVoiceline('ph308')
    sprite('ph204_02', 3)
    sprite('ph204_03', 3)
    sprite('ph204_04', 3)
    sprite('ph204_05', 3)
    sprite('ph204_06', 3)
    sprite('ph204_07', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_BRN', 32)
    CreateObject('DriveAtk_BRN', -1)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 3)
    XImpulseAcceleration(50)
    sprite('ph204_09', 3)
    XImpulseAcceleration(50)
    sprite('ph204_11', 3)
    XImpulseAcceleration(50)
    sprite('ph204_12', 4)
    XImpulseAcceleration(0)
    sprite('ph212_11', 3)
    SpriteCall('ph204_15', 3, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 3)
    SpriteCall('ph204_16', 3, 2, 36)


@State
def NmlAtkDrive_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 272
        PreventBlocking(1)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

        def upon_40():
            if SLOT_2:
                setInvincible(1)
                SpecificInvincibility(1, 1, 1, 1, 1)
                SLOT_54 = 1
    sprite('ph204_01', 3)
    SpriteCall('ph204_14', 3, 2, 36)
    SmartVoiceline('ph307')
    sprite('ph204_05', 3)
    sprite('ph204_06', 3)
    sprite('ph204_07', 3)
    callSubroutine('MagicReductionOD')
    SetActionMark(1)
    ObjectUpon(8, 32)
    CreateObject('DriveDef_GRN', -1)
    RegisterObject(8, 1)
    callSubroutine('MagicReset')
    physicsXImpulse(-7500)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph204_08', 4)
    SetActionMark(0)
    if not SLOT_54:
        setInvincible(0)
    XImpulseAcceleration(50)
    sprite('ph204_09', 4)
    XImpulseAcceleration(50)
    sprite('ph204_10', 4)
    sprite('ph204_11', 4)
    XImpulseAcceleration(50)
    sprite('ph204_12', 4)
    XImpulseAcceleration(0)
    sprite('ph212_11', 4)
    SpriteCall('ph204_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph212_12', 4)
    SpriteCall('ph204_16', 4, 2, 36)


@State
def NmlAtkDrive_RRR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 4, 2, 52)
        SLOT_53 = 768
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph205_01', 2)
    SmartVoiceline('ph310')
    callSubroutine('PowerUpFlashRed')
    sprite('ph205_02', 2)
    sprite('ph205_05', 2)
    sprite('ph205_06', 2)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_RRR', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-10000)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph205_07', 3)
    XImpulseAcceleration(50)
    sprite('ph205_08', 3)
    XImpulseAcceleration(50)
    sprite('ph205_09', 3)
    XImpulseAcceleration(50)
    sprite('ph205_10', 3)
    XImpulseAcceleration(50)
    sprite('ph205_11', 3)
    XImpulseAcceleration(0)
    sprite('ph205_12', 3)
    SpriteCall('ph205_15', 3, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 3)
    SpriteCall('ph205_16', 3, 2, 36)


@State
def NmlAtkDrive_GGG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 2, 2, 52)
        SLOT_53 = 48
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph205_01', 3)
    SmartVoiceline('ph312')
    callSubroutine('PowerUpFlashGreen')
    CreateObject('Wind_Herald', -1)
    sprite('ph205_02', 2)
    sprite('ph205_04', 3)
    sprite('ph205_05', 2)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_GGG', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-10000)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph205_07', 3)
    XImpulseAcceleration(50)
    sprite('ph205_08', 3)
    XImpulseAcceleration(50)
    sprite('ph205_09', 3)
    XImpulseAcceleration(50)
    sprite('ph205_10', 3)
    XImpulseAcceleration(50)
    sprite('ph205_11', 4)
    XImpulseAcceleration(0)
    sprite('ph205_12', 4)
    SpriteCall('ph205_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 4)
    SpriteCall('ph205_16', 4, 2, 36)


@State
def NmlAtkDrive_BBB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        PrivateFunction(9, 2, 6, 0, 1, 2, 52)
        SLOT_53 = 3
        SpecialCancel(1)

        def upon_STATE_END():
            XImpulseAcceleration(0)
    sprite('ph205_01', 2)
    SmartVoiceline('ph311')
    callSubroutine('PowerUpFlashBlue')
    sprite('ph205_04', 2)
    sprite('ph205_05', 2)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    CreateObject('DriveAtk_BBB', -1)
    if SLOT_IsAirborne:
        ObjectUpon(STATE_END, 33)
    if SLOT_52:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    physicsXImpulse(-10000)
    if SLOT_IsGrounded:
        LandingEffects(100, 1, 0)
    sprite('ph205_07', 3)
    XImpulseAcceleration(50)
    sprite('ph205_08', 3)
    sprite('ph205_10', 3)
    XImpulseAcceleration(50)
    sprite('ph205_11', 4)
    XImpulseAcceleration(0)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_RRB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 513
        PreventBlocking(1)
    sprite('ph205_01', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_RRB', 32)
    CreateParticle('phef_rrn_mc', 103)
    SmartVoiceline('ph313')
    CreateObject('DriveAtk_RRB', -1)
    callSubroutine('MagicReset')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_RRG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 528
        PreventBlocking(1)
    sprite('ph205_01', 3)
    SmartVoiceline('ph314')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_RRG', 32)
    CreateObject('DriveAtk_RRG', -1)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_GGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 288
        PreventBlocking(1)
    sprite('ph205_01', 3)
    SmartVoiceline('ph317')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_GGR', 32)
    CreateObject('DriveAtk_GGR', -1)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_GGB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 33
        PreventBlocking(1)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if CheckInput(0x20):
                SLOT_54 = 1
            if SLOT_2:
                if SLOT_StateDuration >= 35:
                    if SLOT_54:
                        clearUponHandler(EVERY_FRAME)
                        TriggerUponForState('DriveAtk_GGB', 34)
                        sendToLabel(9)
                if SLOT_StateDuration >= 65:
                    clearUponHandler(EVERY_FRAME)
                    TriggerUponForState('DriveAtk_GGB', 34)
                    sendToLabel(9)
    sprite('ph205_01', 3)
    SmartVoiceline('ph318')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_GGB_ATKMaster', 32)
    TriggerUponForState('DriveAtk_GGB', 32)
    CreateParticle('phef_ggb_mc', 103)
    CreateObject('DriveAtk_GGB', -1)
    callSubroutine('MagicReset')
    sprite('ph205_07', 4)
    if SLOT_54:
        clearUponHandler(EVERY_FRAME)
        TriggerUponForState('DriveAtk_GGB', 33)
        sendToLabel(1)
    else:
        SetActionMark(1)
    sprite('ph205_08', 4)
    sprite('ph205_09', 4)
    label(0)
    sprite('ph205_07', 4)
    sprite('ph205_08', 4)
    sprite('ph205_09', 4)
    gotoLabel(0)
    label(1)
    sprite('ph205_07', 3)
    sprite('ph205_08', 3)
    sprite('ph205_09', 3)
    sprite('ph205_07', 3)
    sprite('ph205_08', 3)
    sprite('ph205_09', 3)
    sprite('ph205_07', 3)
    sprite('ph205_08', 3)
    sprite('ph205_09', 3)
    sprite('ph205_07', 3)
    sprite('ph205_08', 3)
    sprite('ph205_09', 3)
    sprite('ph205_07', 3)
    sprite('ph205_08', 3)
    sprite('ph205_09', 3)
    label(9)
    sprite('ph205_10', 4)
    sprite('ph205_11', 4)
    sprite('ph205_12', 4)
    SpriteCall('ph205_15', 4, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 4)
    SpriteCall('ph205_16', 4, 2, 36)


@State
def NmlAtkDrive_BBR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 258
        PreventBlocking(1)
    sprite('ph205_01', 3)
    CreateParticle('phef_rrn_mc', 103)
    SmartVoiceline('ph315')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_BBR', 32)
    CreateObject('DriveAtk_BBR', -1)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_BBG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 18
        PreventBlocking(1)
    sprite('ph205_01', 3)
    SmartVoiceline('ph316')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_BBG', 32)
    CreateObject('DriveAtk_BBG', -1)
    if CheckInput(0x5f):
        ObjectUpon(STATE_END, 33)
    CreateParticle('phef_ggb_mc', 103)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtkDrive_BGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInitialize')
        SLOT_53 = 273
        PreventBlocking(1)
    sprite('ph205_01', 3)
    CreateParticle('phef_rgb_mc', 103)
    SmartVoiceline('ph319')
    sprite('ph205_04', 3)
    sprite('ph205_05', 3)
    sprite('ph205_06', 3)
    callSubroutine('MagicReductionOD')
    TriggerUponForState('DriveAtk_BGR', 32)
    CreateObject('DriveAtk_BGR', -1)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    SpriteCall('ph205_15', 5, 2, 36)
    EndYPhysicsImpulse()
    sprite('ph205_13', 5)
    SpriteCall('ph205_16', 5, 2, 36)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(550)
        AttackP1(90)
        UseSlashHitspark(1)
        HitLow(2)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute2_A')
        SLOT_55 = 1
        if SLOT_52:
            Damage(660)
            ChipPercentage(5)
    sprite('ph230_00', 3)
    sprite('ph230_01', 3)
    callSubroutine('PowerUpFlashBlue')
    sprite('ph230_02', 3)
    RandomCommonVoiceline(0)
    sprite('ph230_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph230_eff', -1)
    PrivateSE('phse_00')
    sprite('ph230_04', 5)
    Recovery()
    Unknown2063()
    sprite('ph230_05', 5)
    sprite('ph230_06', 5)
    sprite('ph230_07', 4)
    sprite('ph230_08', 4)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(550)
        AttackP1(90)
        UseSlashHitspark(1)
        HitLow(2)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute2_B')
        SLOT_55 = 2
        if SLOT_52:
            Damage(660)
            ChipPercentage(5)
    sprite('ph231_00', 3)
    sprite('ph231_00', 1)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph231_01', 3)
    sprite('ph231_02', 3)
    SmartVoiceline('ph108')
    sprite('ph231_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph231_eff', -1)
    PrivateSE('phse_01')
    sprite('ph231_04', 3)
    sprite('ph231_05', 6)
    Recovery()
    Unknown2063()
    sprite('ph231_06', 5)
    sprite('ph231_07', 5)
    sprite('ph231_08', 5)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(550)
        AttackP1(90)
        HitLow(2)
        UseFireHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute2_C')
        SLOT_55 = 4
        if SLOT_52:
            Damage(660)
            ChipPercentage(5)
    sprite('ph232_00', 3)
    sprite('ph232_00', 2)
    callSubroutine('PowerUpFlashRed')
    sprite('ph232_01', 5)
    RandomCommonVoiceline(0)
    sprite('ph232_02', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph232_eff', -1)
    PrivateSE('phse_02')
    sprite('ph232_02', 3)
    AttackOff()
    Recovery()
    Unknown2063()
    sprite('ph232_03', 6)
    sprite('ph232_04', 6)
    sprite('ph232_05', 5)
    sprite('ph232_06', 5)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(750)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(1500)
        AirPushbackY(18000)
        AirUntechableTime(40)
        CHHardKnockdown(3)
        UseFireHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute3')
        SLOT_55 = 4
        if SLOT_52:
            Damage(900)
            ChipPercentage(5)
    sprite('ph235_00', 3)
    sprite('ph235_01', 3)
    callSubroutine('PowerUpFlashRed')
    sprite('ph235_02', 3)
    RandomCommonVoiceline(1)
    sprite('ph235_03', 5)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph235_eff', -1)
    PrivateSE('phse_02')
    sprite('ph235_04', 5)
    Recovery()
    Unknown2063()
    sprite('ph235_05', 5)
    sprite('ph235_06', 5)
    sprite('ph235_07', 5)
    sprite('ph235_08', 5)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        UseSlashHitspark(1)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR5_A')
        SLOT_55 = 1
        if SLOT_52:
            Damage(840)
            ChipPercentage(5)
    sprite('ph250_00', 3)
    sprite('ph250_01', 2)
    callSubroutine('PowerUpFlashBlue')
    sprite('ph250_02', 2)
    RandomCommonVoiceline(1)
    sprite('ph250_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph250_eff', -1)
    PrivateSE('phse_00')
    sprite('ph250_04', 5)
    Recovery()
    Unknown2063()
    sprite('ph250_05', 5)
    sprite('ph250_06', 5)
    sprite('ph250_07', 5)
    sprite('ph250_08', 5)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        AirHitstunAnimation(10)
        UseSlashHitspark(1)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR5_B')
        SLOT_55 = 2
        if SLOT_52:
            Damage(840)
            ChipPercentage(5)
    sprite('ph251_00', 3)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph251_01', 3)
    sprite('ph251_02', 3)
    SmartVoiceline('ph108')
    sprite('ph251_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph251_eff', -1)
    PrivateSE('phse_01')
    sprite('ph251_04', 3)
    sprite('ph251_04', 3)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ph251_05', 6)
    sprite('ph251_06', 6)
    sprite('ph251_07', 6)
    sprite('ph251_08', 6)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        AirHitstunAnimation(10)
        UseFireHitspark(1)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR5_C')
        SLOT_55 = 4
        if SLOT_52:
            Damage(840)
            ChipPercentage(5)
    sprite('ph252_00', 3)
    sprite('ph252_00', 1)
    callSubroutine('PowerUpFlashRed')
    sprite('ph252_01', 4)
    sprite('ph252_02', 2)
    RandomCommonVoiceline(1)
    sprite('ph252_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph252_eff', -1)
    PrivateSE('phse_02')
    sprite('ph252_04', 5)
    Recovery()
    Unknown2063()
    sprite('ph252_05', 5)
    sprite('ph252_06', 5)
    sprite('ph252_07', 5)
    sprite('ph252_08', 5)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR2A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        UseSlashHitspark(1)
        AirPushbackY(22000)
        AirUntechableTime(22)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR2_A')
        SLOT_55 = 1
        if SLOT_52:
            Damage(960)
            ChipPercentage(5)
    sprite('ph253_00', 3)
    sprite('ph253_00', 3)
    callSubroutine('PowerUpFlashBlue')
    sprite('ph253_01', 3)
    sprite('ph253_02', 3)
    RandomCommonVoiceline(1)
    sprite('ph253_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph253_eff', -1)
    PrivateSE('phse_00')
    sprite('ph253_04', 7)
    Recovery()
    Unknown2063()
    sprite('ph253_05', 7)
    sprite('ph253_06', 7)
    sprite('ph253_07', 7)
    sprite('ph253_08', 7)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR2B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        UseSlashHitspark(1)
        AirPushbackY(22000)
        AirUntechableTime(22)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR2_B')
        SLOT_55 = 2
        if SLOT_52:
            Damage(960)
            ChipPercentage(5)
    sprite('ph254_00', 3)
    sprite('ph254_00', 3)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph254_01', 7)
    sprite('ph254_02', 3)
    SmartVoiceline('ph108')
    sprite('ph254_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph254_eff', -1)
    PrivateSE('phse_01')
    sprite('ph254_04', 3)
    sprite('ph254_04', 4)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ph254_05', 7)
    sprite('ph254_06', 7)
    sprite('ph254_07', 7)
    sprite('ph254_08', 7)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        UseFireHitspark(1)
        AirPushbackY(22000)
        AirUntechableTime(22)
        EndYPhysicsImpulse()
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRouteAIR2_C')
        SLOT_55 = 4
        if SLOT_52:
            Damage(960)
            ChipPercentage(5)
    sprite('ph255_00', 3)
    sprite('ph255_00', 3)
    callSubroutine('PowerUpFlashRed')
    sprite('ph255_01', 7)
    sprite('ph255_02', 3)
    RandomCommonVoiceline(1)
    sprite('ph255_03', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph255_eff', -1)
    PrivateSE('phse_02')
    sprite('ph255_04', 7)
    Recovery()
    Unknown2063()
    sprite('ph255_05', 7)
    sprite('ph255_06', 7)
    sprite('ph255_07', 7)
    sprite('ph255_08', 7)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(0)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        ForceFaceSprite()
    sprite('ph203_14', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@State
def AN_NmlAtkAIR5D_Lv2():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        ForceFaceSprite()
    sprite('ph204_13', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@State
def AN_NmlAtkAIR5D_Lv3():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
        ForceFaceSprite()
    sprite('ph205_14', 3)
    sprite('keep', 1)
    callSubroutine('ActivateMagicSelect')


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AirPushbackX(2700)
        AirPushbackY(27000)
        AirUntechableTime(29)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AttackP2(82)
        UseSlashHitspark(1)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute6_A')
        SLOT_55 = 1
        HitAirUnblockable(3)
        if SLOT_52:
            Damage(1080)
            ChipPercentage(5)
    sprite('ph210_00', 2)
    sprite('ph210_01', 1)
    sprite('ph210_01', 1)
    callSubroutine('PowerUpFlashBlue')
    sprite('ph210_02', 2)
    sprite('ph210_03', 2)
    sprite('ph210_04', 2)
    RandomCommonVoiceline(2)
    sprite('ph210_05', 4)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph210_eff', -1)
    PrivateSE('phse_00')
    sprite('ph210_06', 4)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ph210_07', 4)
    sprite('ph210_08', 3)
    sprite('ph210_09', 3)
    sprite('ph210_10', 3)
    sprite('ph210_11', 3)
    sprite('ph210_12', 3)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AirPushbackX(4050)
        AirPushbackY(27000)
        AirUntechableTime(29)
        UseSlashHitspark(1)
        GroundedHitstunAnimation(10)
        AttackP2(82)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute6_B')
        SLOT_55 = 2
        HitAirUnblockable(3)
        if SLOT_52:
            Damage(1080)
            ChipPercentage(5)
    sprite('ph211_00', 2)
    sprite('ph211_01', 1)
    sprite('ph211_01', 1)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph211_02', 3)
    sprite('ph211_03', 2)
    sprite('ph211_04', 2)
    SmartVoiceline('ph109')
    sprite('ph211_05', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph211_eff', -1)
    PrivateSE('phse_01')
    sprite('ph211_06', 3)
    sprite('ph211_07', 4)
    Recovery()
    Unknown2063()
    sprite('ph211_08', 4)
    sprite('ph211_09', 4)
    sprite('ph211_10', 3)
    sprite('ph211_11', 3)
    sprite('ph211_12', 3)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AirPushbackY(27000)
        AirUntechableTime(29)
        UseFireHitspark(1)
        GroundedHitstunAnimation(10)
        AttackP2(82)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute6_C')
        SLOT_55 = 4
        HitAirUnblockable(3)
        if SLOT_52:
            Damage(1080)
            ChipPercentage(5)
    sprite('ph212_00', 3)
    sprite('ph212_01', 3)
    callSubroutine('PowerUpFlashRed')
    sprite('ph212_02', 2)
    sprite('ph212_03', 2)
    sprite('ph212_04', 2)
    RandomCommonVoiceline(2)
    sprite('ph212_05', 4)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph212_eff', -1)
    PrivateSE('phse_02')
    sprite('ph212_06', 4)
    Recovery()
    Unknown2063()
    sprite('ph212_07', 4)
    sprite('ph212_08', 4)
    sprite('ph212_09', 4)
    sprite('ph212_10', 3)
    sprite('ph212_11', 3)
    sprite('ph212_12', 3)


@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(300)
        UseSlashHitspark(1)
        PushbackX(12000)
        StarterRating(2)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute4_A')
        SLOT_55 = 1

        def upon_32():
            if not SLOT_2:
                clearUponHandler(32)
                callSubroutine('MagicTableUpDate')
                SLOT_54 = 0
                EndAttack()
        if SLOT_52:
            Damage(360)
            ChipPercentage(5)
    sprite('ph214_00', 3)
    PerInertia(60)
    CreateObject('ShotDefCol', -1)
    sprite('ph214_01', 2)
    callSubroutine('PowerUpFlashBlue')
    RandomCommonVoiceline(0)
    sprite('ph214_02', 3)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph214_eff', -1)
    PrivateSE('phse_00')
    sprite('ph214_03', 3)
    sprite('ph214_04', 5)
    Recovery()
    Unknown2063()
    sprite('ph214_05', 5)


@State
def NmlAtk4B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(300)
        UseSlashHitspark(1)
        PushbackX(12000)
        StarterRating(2)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute4_B')
        SLOT_55 = 2

        def upon_32():
            if not SLOT_2:
                clearUponHandler(32)
                callSubroutine('MagicTableUpDate')
                SLOT_54 = 0
                EndAttack()
        if SLOT_52:
            Damage(360)
            ChipPercentage(5)
    sprite('ph215_00', 2)
    PerInertia(60)
    CreateObject('ShotDefCol', -1)
    sprite('ph215_01', 1)
    sprite('ph215_01', 1)
    callSubroutine('PowerUpFlashGreen')
    sprite('ph215_02', 1)
    SmartVoiceline('ph108')
    sprite('ph215_03', 4)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph215_eff', -1)
    PrivateSE('phse_01')
    sprite('ph215_04', 4)
    sprite('ph215_05', 5)
    Recovery()
    Unknown2063()
    sprite('ph215_06', 5)


@State
def NmlAtk4C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(300)
        UseFireHitspark(1)
        PushbackX(12000)
        StarterRating(2)
        callSubroutine('MagicNormalAtkInit')
        callSubroutine('ChainRoute4_C')
        SLOT_55 = 4

        def upon_32():
            if not SLOT_2:
                clearUponHandler(32)
                callSubroutine('MagicTableUpDate')
                SLOT_54 = 0
                EndAttack()
        if SLOT_52:
            Damage(360)
            ChipPercentage(5)
    sprite('ph216_00', 2)
    PerInertia(60)
    CreateObject('ShotDefCol', -1)
    sprite('ph216_01', 1)
    sprite('ph216_01', 1)
    callSubroutine('PowerUpFlashRed')
    sprite('ph216_02', 1)
    RandomCommonVoiceline(0)
    sprite('ph216_03', 4)
    if SLOT_54:
        SetActionMark(1)
    CreateObject('ph216_eff', -1)
    PrivateSE('phse_02')
    sprite('ph216_04', 4)
    sprite('ph216_05', 6)
    Recovery()
    Unknown2063()
    sprite('ph216_06', 6)


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('ph300_00', 6)
    sprite('ph300_01', 6)
    if random_(2, 0, 50):
        Voiceline('ph404')
    else:
        Voiceline('ph405')
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_01', 6)
    sprite('ph300_00', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        StayAfterMovement(1, 0)
        AirUntechableTime(30)
        CHAirUntechableTime(30)
        Floorslide(40)
        AirPushbackX(30000)
        AirPushbackY(10000)
    sprite('ph311_01', 3)
    sprite('ph311_05', 3)
    sprite('ph311_06', 3)
    sprite('ph311_08', 3)
    sprite('ph311_09ex01', 3)
    RefreshMultihit()
    sprite('ph311_10', 6)
    sprite('ph311_11', 6)
    sprite('ph311_12', 6)
    sprite('ph311_13', 6)
    sprite('ph311_14', 6)
    sprite('ph311_15', 6)


@Subroutine
def CheckMirrerKick():
    if CheckObjectPresence(8):
        CopyFromRightToLeft(23, 2, 0, 8, 2, 50)
        if SLOT_0 <= 350000:
            CopyFromRightToLeft(23, 2, 0, 8, 2, 23)
            if SLOT_0 <= 300000:
                CopyFromRightToLeft(23, 2, 0, 8, 2, 19)
                if SLOT_0 <= SLOT_19:
                    ObjectUpon(8, 40)
                else:
                    pass


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
    sprite('ph340_00', 3)
    sprite('ph340_00', 1)
    Voiceline('ph159')
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    StayAfterMovement(1, 0)
    sprite('ph340_01', 4)
    CharacterFlash(16763080, 8, 2)
    sprite('ph340_02', 3)
    sprite('ph340_03', 3)
    label(100)
    sprite('ph340_01', 3)
    sprite('ph340_02', 3)
    sprite('ph340_03', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('ph340_04', 2)
    clearUponHandler(EVERY_FRAME)
    sprite('ph340_05', 3)
    sprite('ph340_06', 2)
    sprite('ph340_07', 2)
    CreateObject('phef_340_fire', 100)
    CommonSE('004_swing_grap_1_2')
    PrivateSE('phse_02')
    sprite('ph340_08', 1)
    callSubroutine('CheckMirrerKick')
    sprite('ph340_08', 1)
    StartMultihit()
    EnableAfterimage(0)
    sprite('ph340_09', 2)
    sprite('ph340_10', 2)
    sprite('ph340_11', 2)
    sprite('ph340_12', 2)
    sprite('ph340_13', 3)
    sprite('ph340_14', 3)
    sprite('ph340_15', 3)
    sprite('ph340_16', 3)
    sprite('ph340_17', 2)
    sprite('ph340_18', 2)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('ph310_00', 3)
    sprite('ph310_01', 3)
    sprite('ph310_02', 3)
    CommonSE('007_swing_knife_0')
    SLOT_65 = 1
    sprite('ph310_03', 3)
    SLOT_65 = 0
    sprite('ph310_04', 5)
    Voiceline('ph155')
    sprite('ph310_05', 5)
    sprite('ph310_06', 5)
    sprite('ph310_07', 5)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(2)
        Damage(600)
        AttackP2(100)
        PushbackX(35000)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(40)
        Crumple(60)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        SpecialCancel(0)
        EnableRapidCancel(0)
        DamageFromStateOnly('ThrowExeFinish')
        SetActionMark(0)
        if CharacterIDCheck('ce'):
            SetActionMark(1)
        if SLOT_44:
            SetActionMark(1)
        TriggerUponForState('DriveAtk_BGN', 32)
    sprite('ph310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ph311_00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    if SLOT_2:
        Voiceline('ph153')
    sprite('ph311_01', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph311_02', 3)
    RefreshMultihit()
    if not SLOT_2:
        Voiceline('ph153')
    sprite('keep', 10)
    enterState('ThrowExeFinish')


@State
def ThrowExeFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AirUntechableTime(30)
        AirHitstunAfterWallbounce(40)
        Wallstick(1)
        WallstickDuration(42)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(55000)
        AirPushbackY(18000)
        Wallbounce(1)
        WallbounceReboundTime(45)
        MinimumDamage(100)
        IgnoreBurst(1)
        callSubroutine('MagicChainLand')
        setInvincible(1)
    sprite('ph311_03', 5)
    sprite('ph311_04', 5)
    sprite('ph311_05', 5)
    sprite('ph311_06', 8)
    sprite('ph311_07', 8)
    sprite('ph311_08', 15)
    sprite('ph311_09', 3)
    RefreshMultihit()
    sprite('ph311_10', 4)
    sprite('ph311_11', 4)
    sprite('ph311_12', 4)
    sprite('ph311_13', 4)
    sprite('ph311_14', 4)
    sprite('ph311_15', 4)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('ph310_00', 3)
    sprite('ph310_01', 3)
    sprite('ph310_02', 3)
    SLOT_65 = 1
    CommonSE('007_swing_knife_0')
    sprite('ph310_03', 3)
    SLOT_65 = 0
    sprite('ph310_04', 5)
    Voiceline('ph155')
    sprite('ph310_05', 5)
    sprite('ph310_06', 5)
    sprite('ph310_07', 5)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(2)
        Damage(600)
        AttackP2(100)
        PushbackX(35000)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(40)
        Crumple(60)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        WhiffCrouchBlockCancel(1)
        SpecialCancel(0)
        EnableRapidCancel(0)
        IgnoreTurn(1)
        DamageFromStateOnly('ThrowExeFinish')
        SetActionMark(0)
        if CharacterIDCheck('ce'):
            SetActionMark(1)
        if SLOT_44:
            SetActionMark(1)
        TriggerUponForState('DriveAtk_BGN', 32)
    sprite('ph310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('ph313_00', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph313_01', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph313_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph313_03', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 1)
    sprite('ph313_04', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph313_05', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph313_06', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph311_00', 3)
    Flip()
    if SLOT_2:
        Voiceline('ph153')
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph311_01', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('ph311_02', 3)
    RefreshMultihit()
    if not SLOT_2:
        Voiceline('ph153')
    sprite('keep', 10)
    enterState('ThrowExeFinish')


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
        EndYPhysicsImpulse()

        def upon_STATE_END():
            SLOT_65 = 0
    sprite('ph320_00', 3)
    sprite('ph320_01', 3)
    sprite('ph320_02', 3)
    SLOT_65 = 1
    CommonSE('007_swing_knife_0')
    sprite('ph320_03', 5)
    SLOT_65 = 0
    Voiceline('ph155')
    ForcedLandingRecovery(4, 1)
    sprite('ph320_04', 6)
    sprite('ph320_05', 6)
    sprite('ph320_06', 6)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(1)
        Damage(50)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(10000)
        AirUntechableTime(60)
        Hitstop(0)
        EnemyHitstopAddition(0, 20, 20)
        UseFireHitspark(1)
        DamageFromStateOnly('AirThrowExe')
        StarterRating(2)
        DefeatOpponentBehavior(1)
        DamageEffect(5, '')
        SetZLine(0, 50)
        EndMomentum(1)
        ForcedLandingRecovery(0, 0)
        SpecialCancel(0)
        EnableRapidCancel(0)
        TriggerUponForState('DriveAtk_BGN', 32)
    sprite('ph320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    StartMultihit()
    sprite('ph321_00', 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    StartMultihit()
    sprite('ph321_01', 3)
    Voiceline('ph154')
    RefreshMultihit()
    NoAttackOffset(1)
    CreateObject('ph320SmokeEff', 1)

    def RunOnObject_1():
        RotationAngle(30000)
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_2')
    CreateObject('ph320SmokeEff2', 2)

    def RunOnObject_1():
        RotationAngle(100000)
    CreateObject('ph320SmokeEff', 3)

    def RunOnObject_1():
        RotationAngle(150000)
        AddScale(-300)
    CreateObject('ph320SmokeEff2', 4)

    def RunOnObject_1():
        RotationAngle(-30000)
    CreateObject('ph320SmokeEff', 5)

    def RunOnObject_1():
        RotationAngle(-85000)
    CreateObject('ph320SmokeEff2', 6)

    def RunOnObject_1():
        RotationAngle(-160000)
        AddScale(-300)
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 3)
    RefreshMultihit()
    CreateObject('ph320SmokeEff', 1)

    def RunOnObject_1():
        RotationAngle(60000)
    CreateObject('ph320SmokeEff', 3)

    def RunOnObject_1():
        RotationAngle(120000)
        AddScale(-300)
    CreateObject('ph320SmokeEff', 4)

    def RunOnObject_1():
        RotationAngle(-60000)
        AddY(25000)
    CreateObject('ph320SmokeEff', 6)

    def RunOnObject_1():
        RotationAngle(-120000)
        AddScale(-300)
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 3)
    RefreshMultihit()
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 3)
    RefreshMultihit()
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 10)
    StartMultihit()
    sprite('ph321_02', 8)
    sprite('ph321_03', 1)
    RefreshMultihit()
    NoAttackOffset(0)
    AttackLevel_(4)
    Damage(1100)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(1500)
    AirPushbackY(45000)
    AttackP2(50)
    Hitstop(13)
    EnemyHitstopAddition(0, 0, 0)
    DamageEffect(0, '')
    DamageFromStateOnly('')
    DefeatOpponentBehavior(0)
    CreateObject('ph320BombEff', 0)
    CommonSE('016_explode_2')
    sprite('ph321_03', 2)
    SpecialCancel(1)
    EnableRapidCancel(1)
    callSubroutine('MagicChainAir')
    sprite('ph321_04', 3)
    EndYPhysicsImpulse()
    sprite('ph321_05', 3)
    sprite('ph321_06', 3)
    sprite('ph321_07', 5)
    sprite('ph321_08', 5)


@Subroutine
def MagicChainLand():
    HitOrBlockCancel('NmlAtk5D')
    HitOrBlockCancel('AN_NmlAtk5D_Lv2')
    HitOrBlockCancel('AN_NmlAtk5D_Lv3')


@Subroutine
def MagicChainAir():
    HitOrBlockCancel('NmlAtkAIR5D')
    HitOrBlockCancel('AN_NmlAtkAIR5D_Lv2')
    HitOrBlockCancel('AN_NmlAtkAIR5D_Lv3')


@Subroutine
def MagicCancel():
    SetActionMark(0)


@Subroutine
def MagicCancelBegin():
    SetActionMark(1)


@State
def AssaultLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        AirUntechableTime(70)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(10000)
        PushbackX(8000)
        DistanceCheck(200000, -200000, 200000, -200000)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
        SLOT_54 = 0

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            SLOT_54 = SLOT_54 + 1
            physicsXImpulse(80000)
            sendToLabel(1)
        callSubroutine('MagicCancel')

        def upon_STATE_END():
            XImpulseAcceleration(25)
    sprite('ph400_00', 3)
    Voiceline('ph200')
    physicsXImpulse(2050)
    sprite('ph400_01', 3)
    XImpulseAcceleration(150)
    sprite('ph400_02', 2)
    XImpulseAcceleration(150)
    CommonSE('000_airdash_0')
    sprite('ph400_03', 2)
    XImpulseAcceleration(400)
    CreateObject('pheff_400', -1)
    CommonSE('015_blaze_0')
    sprite('ph400_04', 2)
    XImpulseAcceleration(800)
    sprite('ph400_02', 3)
    XImpulseAcceleration(50)
    Visibility(1)
    RefreshMultihit()
    TriggerUponForState('pheff_400', 32)
    sprite('ph400_03', 3)
    XImpulseAcceleration(25)
    sprite('ph400_04', 3)
    XImpulseAcceleration(25)
    label(1)
    sprite('ph400_05', 6)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    ForceFaceSprite()
    XImpulseAcceleration(25)
    sprite('ph400_05', 1)
    Visibility(0)
    physicsXImpulse(-15000)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(950)
    ResetPushback()
    AirPushbackY(18000)
    PushbackX(12000)
    AirUntechableTime(40)
    UseFireHitspark(1)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    DistanceCheck(250000, -250000, 300000, -300000)
    if SLOT_54:
        DistanceCheck(-1, -1, -1, -1)
    if SLOT_137:
        DamageMultiplier(80)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
        SLOT_54 = SLOT_54 + 1
    CommonSE('016_explode_1')
    CommonSE('016_explode_0')
    sprite('ph400_05', 3)
    StartMultihit()
    sprite('ph400_06', 4)
    SpriteCall('ph400_06', 3, 2, 54)
    Recovery()
    XImpulseAcceleration(25)
    sprite('ph400_07', 5)
    SpriteCall('ph400_07', 4, 2, 54)
    callSubroutine('MagicCancelBegin')
    XImpulseAcceleration(25)
    sprite('ph400_08', 5)
    SpriteCall('ph400_08', 4, 2, 54)
    XImpulseAcceleration(25)
    sprite('ph400_09', 5)
    SpriteCall('ph400_09', 4, 2, 54)
    XImpulseAcceleration(25)
    sprite('ph400_10', 5)
    SpriteCall('ph400_10', 4, 2, 54)
    XImpulseAcceleration(0)


@State
def AssaultAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        EndMomentum(1)
        AttackLevel_(3)
        Damage(500)
        AttackP1(90)
        AirUntechableTime(70)
        AirPushbackX(15000)
        AirPushbackY(7500)
        PushbackX(8000)
        GroundedHitstunAnimation(9)
        DistanceCheck(250000, -200000, 300000, -200000)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
        callSubroutine('MagicCancel')
        SLOT_54 = 0

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            SLOT_54 = SLOT_54 + 1
            physicsXImpulse(80000)
            physicsYImpulse(0)
            sendToLabel(1)

        def upon_EVERY_FRAME():
            SLOT_51 = 0
            SLOT_YVelocity = 0
            if SLOT_2:
                CopyFromRightToLeft(3, 2, 51, 22, 2, 23)
                PrivateFunction(1, 2, 23, 2, 51, 2, 51)
                PrivateFunction(3, 2, 51, 0, -10, 2, 13)
                if SLOT_YVelocity <= 0:
                    SLOT_YVelocity = 0
                PrivateFunction(3, 2, 19, 0, 50, 2, 52)
                SLOT_XVelocity = SLOT_XVelocity + SLOT_52

        def upon_STATE_END():
            XImpulseAcceleration(25)
    sprite('ph400_11', 3)
    Voiceline('ph200')
    physicsXImpulse(1100)
    ModifyVar_(8, 2, 7, 0, 2)
    sprite('ph400_01', 3)
    XImpulseAcceleration(150)
    sprite('ph400_02', 2)
    XImpulseAcceleration(150)
    CommonSE('000_airdash_0')
    sprite('ph400_03', 2)
    CreateObject('pheff_400Air', -1)
    CommonSE('015_blaze_0')
    XImpulseAcceleration(400)
    sprite('ph400_04', 1)
    SetActionMark(1)
    XImpulseAcceleration(800)
    sprite('ph400_04', 1)
    if SLOT_YVelocity < 0:
        TriggerUponForState('pheff_400Air', 33)
    if SLOT_YVelocity > 0:
        TriggerUponForState('pheff_400Air', 34)
    sprite('ph400_02', 3)
    XImpulseAcceleration(50)
    Visibility(1)
    RefreshMultihit()
    TriggerUponForState('pheff_400Air', 32)
    sprite('ph400_03', 3)
    SetActionMark(0)
    XImpulseAcceleration(25)
    sprite('ph400_04', 3)
    XImpulseAcceleration(25)
    label(1)
    sprite('ph400_05', 3)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    clearUponHandler(EVERY_FRAME)
    ForceFaceSprite()
    SetYCollisionFromOrigin(-1)
    XImpulseAcceleration(25)
    sprite('ph400_05', 3)
    TriggerUponForState('pheff_400Air', 35)
    sprite('ph400_05', 1)
    Visibility(0)
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    RefreshMultihit()
    AttackLevel_(5)
    Damage(950)
    AirPushbackX(30000)
    AirPushbackY(-30000)
    PushbackX(12000)
    HardKnockdown(10)
    AirUntechableTime(40)
    UseFireHitspark(1)
    GroundedHitstunAnimation(9)
    DistanceCheck(300000, -300000, 300000, -300000)
    if SLOT_54:
        DistanceCheck(-1, -1, -1, -1)
    if SLOT_137:
        DamageMultiplier(80)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
        SLOT_54 = SLOT_54 + 1
    CommonSE('016_explode_1')
    CommonSE('016_explode_0')
    sprite('ph400_05', 2)
    StartMultihit()
    sprite('ph400_06', 6)
    Recovery()
    XImpulseAcceleration(50)
    sprite('ph400_12', 4)
    callSubroutine('MagicCancelBegin')
    XImpulseAcceleration(50)
    sprite('ph400_13', 4)
    XImpulseAcceleration(50)
    sprite('ph400_14', 4)
    XImpulseAcceleration(50)
    sprite('ph400_15', 1)
    XImpulseAcceleration(50)
    if not SLOT_54:
        sendToLabel(2)
    sprite('ph400_15', 3)
    ExitState()
    label(2)
    sprite('ph400_15', 3)
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(3)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    gotoLabel(3)
    ExitState()


@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackOff()
        StayAfterMovement(1, 0)

        def upon_32():
            SetActionMark(1)
        callSubroutine('MagicCancel')
    sprite('ph401_00', 3)
    sprite('ph401_01', 3)
    Voiceline('ph201')
    CrouchState(1)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('ph401_02', 6)
    CreateObject('Eff_401', -1)
    CommonSE('016_explode_1')
    PrivateSE('phse_02')
    sprite('ph401_03', 3)
    physicsXImpulse(10000)
    CommonSE('004_swing_grap_1_2')
    sprite('ph401_04', 3)
    XImpulseAcceleration(25)
    sprite('ph401_05', 5)
    Recovery()
    setInvincible(0)
    XImpulseAcceleration(25)
    sprite('ph401_06', 5)
    XImpulseAcceleration(0)
    sprite('ph401_07', 5)
    physicsXImpulse(-2000)
    sprite('ph401_08', 5)
    XImpulseAcceleration(50)
    sprite('ph401_09', 5)
    callSubroutine('MagicCancelBegin')
    CrouchState(0)
    XImpulseAcceleration(50)
    sprite('ph401_10', 5)
    XImpulseAcceleration(50)
    sprite('ph401_11', 5)
    XImpulseAcceleration(50)


@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_32():
            SetActionMark(1)
        callSubroutine('MagicCancel')
    sprite('ph402_00', 3)
    Voiceline('ph202')
    sprite('ph402_01', 3)
    sprite('ph402_02', 3)
    sprite('ph402_03', 3)
    sprite('ph402_04', 3)
    CreateObject('MidAssault_Atk', -1)
    sprite('ph402_02', 3)
    sprite('ph402_03', 3)
    sprite('ph402_05', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('ph402_06', 2)
    sprite('ph402_07', 2)
    CreateObject('Eff_402Fire_PL', -1)
    sprite('ph402_08', 5)
    sprite('ph402_09', 5)
    ScreenShake(5000, 20000)
    sprite('ph402_10', 5)
    sprite('ph402_11', 4)
    sprite('ph402_12', 4)
    sprite('ph204_12', 4)
    callSubroutine('MagicCancelBegin')
    sprite('ph212_11', 4)
    sprite('ph212_12', 4)


@State
def MagicConversion():

    def upon_IMMEDIATE():
        if SLOT_IsAirborne:
            AttackDefaults_AirSpecial()
        else:
            AttackDefaults_StandingSpecial()
        WhiffCancel('NmlAtk5D')
        WhiffCancel('NmlAtkAIR5D')
    sprite('ph403_00', 2)
    sprite('ph403_01', 2)
    SpriteCall('ph403_01ex01', 2, 2, 36)
    sprite('ph403_02', 2)
    SpriteCall('ph403_02ex01', 2, 2, 36)
    sprite('ph403_03', 3)
    SpriteCall('ph403_03ex01', 3, 2, 36)
    CreateObject('Eff_MagicConv', 0)
    callSubroutine('MagicReplace')
    PrivateSE('phse_08')
    sprite('ph403_04', 3)
    SpriteCall('ph403_04ex01', 3, 2, 36)
    WhiffCancelEnable(1)
    WhiffSpecialCancel(1)
    sprite('ph403_05', 3)
    SpriteCall('ph403_05ex01', 3, 2, 36)
    sprite('ph403_03', 3)
    SpriteCall('ph403_03ex01', 3, 2, 36)
    sprite('ph403_02', 1)
    SpriteCall('ph403_02ex01', 1, 2, 36)
    if SLOT_IsAirborne:
        EndYPhysicsImpulse()
    sprite('ph403_01', 1)
    SpriteCall('ph403_01ex01', 1, 2, 36)
    sprite('keep', 1)
    if SLOT_IsAirborne:
        sendToLabel(1)
    sprite('ph403_00', 2)
    ExitState()
    label(1)
    sprite('ph020_04', 2)
    ExitState()


@State
def MagicReduction():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        if SLOT_IsAirborne:
            AttackDefaults_AirSpecial()
            EndMomentum(1)
        else:
            AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP1(60)
        MoveAttributes(0, 0, 0, 1, 0)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(24000)
        AirPushbackY(28000)
        AirUntechableTime(30)
        EnemyHitstopAddition(9, 0, 2)
        PushbackX(12000)
        StarterRating(0)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
        if SLOT_4:
            setInvincible(1)
    sprite('ph404_00', 3)
    sprite('ph404_01', 3)
    SpriteCall('ph404_01ex01', 3, 2, 36)
    sprite('ph404_03', 3)
    SpriteCall('ph404_03ex01', 3, 2, 36)
    sprite('ph404_04', 3)
    SpriteCall('ph404_04ex01', 3, 2, 36)
    sprite('ph404_02', 3)
    SpriteCall('ph404_02ex01', 3, 2, 36)
    if SLOT_4:
        if SLOT_59 == 4:
            CreateParticle('phef_buf_red', 103)
            CreateObject('Eff_BuffAtkR', -1)
        if SLOT_59 == 2:
            CreateParticle('phef_buf_green', 103)
            CreateObject('Eff_BuffAtkG', -1)
        if SLOT_59 == 1:
            CreateParticle('phef_buf_blue', 103)
            CreateObject('Eff_BuffAtkB', -1)
    sprite('ph404_03', 3)
    SpriteCall('ph404_03ex01', 3, 2, 36)
    sprite('ph404_04', 3)
    SpriteCall('ph404_04ex01', 3, 2, 36)
    sprite('ph404_02', 1)
    SpriteCall('ph404_02ex01', 1, 2, 36)
    if SLOT_4:
        RefreshMultihit()
        ScreenShake(5000, 30000)
        PrivateSE('phse_09')
        if SLOT_59 == 4:
            SLOT_6 = 4
            callSubroutine('MagicReductionClear')
            CreateObject('pheff_BufFireMato', 103)
        if SLOT_59 == 2:
            SLOT_6 = 2
            callSubroutine('MagicReductionClear')
            CreateObject('pheff_BufWindMato', 103)
        if SLOT_59 == 1:
            SLOT_6 = 1
            callSubroutine('MagicReductionClear')
            CreateObject('pheff_BufWaterMato', 103)
        if SLOT_4 >= 1:
            SLOT_33 = 180
        if SLOT_4 >= 16:
            SLOT_33 = 360
        if SLOT_4 >= 256:
            SLOT_33 = 540
        callSubroutine('MagicReset')
    sprite('ph404_02', 2)
    SpriteCall('ph404_02ex01', 2, 2, 36)
    AttackOff()
    sprite('ph404_03', 3)
    SpriteCall('ph404_03ex01', 3, 2, 36)
    setInvincible(0)
    sprite('ph404_04', 3)
    SpriteCall('ph404_04ex01', 3, 2, 36)
    sprite('ph404_02', 3)
    SpriteCall('ph404_02ex01', 2, 2, 36)
    sprite('ph404_03', 3)
    SpriteCall('ph404_03ex01', 3, 2, 36)
    sprite('ph404_04', 3)
    SpriteCall('ph404_04ex01', 3, 2, 36)
    sprite('ph404_01', 5)
    SpriteCall('ph404_01ex01', 5, 2, 36)
    sprite('keep', 1)
    if SLOT_IsAirborne:
        sendToLabel(1)
    sprite('ph404_00', 6)
    ExitState()
    label(1)
    sprite('keep', 1)
    EndYPhysicsImpulse()
    sprite('ph020_03', 6)
    sprite('ph020_04', 6)
    sprite('ph020_05', 6)
    ExitState()


@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
        SetActionMark(0)
        if CharacterIDCheck('ha'):
            SetActionMark(1)
    sprite('ph430_00', 4)
    DistortionSettings(56, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    setInvincible(1)
    sprite('ph430_01', 4)
    sprite('ph430_02', 20)
    CreateObject('Eff_430_cap', 0)
    if SLOT_2:
        Voiceline('ph250')
    sprite('ph430_03', 8)
    sprite('ph430_04', 8)
    sprite('ph430_05', 13)
    sprite('ph430_06', 6)
    SpecificInvincibility(0, 0, 0, 1, 0)
    if not SLOT_2:
        Voiceline('ph250')
    sprite('ph430_07', 6)
    sprite('ph430_08', 2)
    sprite('ph430_09', 2)
    CreateObject('UltimateShotAtk1st', -1)
    SetInertia(-20000)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_13', 4)
    setInvincible(0)
    sprite('ph430_14', 4)
    sprite('ph430_15', 4)
    sprite('ph430_16', 4)
    sprite('ph430_17', 4)
    sprite('ph430_18', 3)
    CreateObject('UltimateShotAtk2nd', -1)
    SetInertia(-40000)
    sprite('ph430_19', 3)
    Voiceline('ph251')
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_22', 6)
    sprite('ph430_23', 6)
    sprite('ph430_24', 6)
    sprite('ph430_25', 6)
    CreateObject('Eff_430_capFire', -1)
    sprite('ph430_26', 6)
    sprite('ph430_27', 6)


@State
def UltimateShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()

        def upon_32():
            SLOT_51 = 1
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
        SetActionMark(0)
        if CharacterIDCheck('ha'):
            SetActionMark(1)
    sprite('ph430_00', 4)
    DistortionSettings(56, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    setInvincible(1)
    sprite('ph430_01', 4)
    sprite('ph430_02', 20)
    CreateObject('Eff_430_cap', 0)
    if SLOT_2:
        Voiceline('ph250')
    sprite('ph430_03', 8)
    sprite('ph430_04', 8)
    sprite('ph430_05', 13)
    sprite('ph430_06', 6)
    SpecificInvincibility(0, 0, 0, 1, 0)
    if not SLOT_2:
        Voiceline('ph250')
    sprite('ph430_07', 6)
    sprite('ph430_08', 2)
    sprite('ph430_09', 2)
    CreateObject('UltimateShotAtk1stOD', -1)
    SetInertia(-20000)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_10', 3)
    sprite('ph430_11', 3)
    sprite('ph430_12', 3)
    sprite('ph430_13', 4)
    setInvincible(0)
    sprite('ph430_14', 4)
    sprite('ph430_15', 4)
    sprite('ph430_16', 4)
    sprite('ph430_17', 4)
    sprite('ph430_18', 3)
    CreateObject('UltimateShotAtk2ndOD', -1)
    SetInertia(-40000)
    sprite('ph430_19', 3)
    Voiceline('ph251')
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_21', 3)
    sprite('ph430_19', 3)
    sprite('ph430_20', 3)
    sprite('ph430_28', 5)
    sprite('ph430_29', 5)
    sprite('ph430_30', 5)
    DistortionSettings(50, -1, 0)
    E0EAEffect('aura', 65535)
    if SLOT_51:
        CreateObject('UltimateShotODCamera', -1)
    EnableRapidCancel(0)
    sprite('ph430_31', 5)
    CreateObject('UltimateShotHinokagutsuchi', -1)
    sprite('ph430_32', 5)
    sprite('ph430_33', 5)
    sprite('ph430_31', 5)
    sprite('ph430_32', 5)
    sprite('ph430_33', 5)
    sprite('ph430_31', 5)
    sprite('ph430_32', 5)
    sprite('ph430_33', 5)
    sprite('ph430_34', 3)
    sprite('ph430_35', 3)
    SetInertia(-10000)
    Voiceline('ph252')
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_36', 3)
    sprite('ph430_37', 3)
    sprite('ph430_38', 3)
    sprite('ph430_39', 6)
    if SLOT_51:
        TriggerUponForState('UltimateShotODCamera', 33)
    sprite('ph430_40', 6)
    sprite('ph430_41', 6)
    sprite('ph430_25', 6)
    CreateObject('Eff_430_capFire', -1)
    sprite('ph430_26', 6)
    sprite('ph430_27', 6)


@State
def UltimateCharge():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
    sprite('ph431_00', 6)
    Voiceline('ph253')
    sprite('ph431_01', 6)
    DistortionSettings(94, -1, 0)
    HeatChange(-5000)
    setInvincible(1)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    CreateObject('Eff_431_obi', -1)
    callSubroutine('MagicEffectFastDelete')
    sprite('ph431_02', 6)
    sprite('ph431_03', 6)
    sprite('ph431_04', 8)
    AddX(-90000)
    sprite('ph431_05', 6)
    sprite('ph431_06', 6)
    sprite('ph431_07', 6)
    physicsXImpulse(5000)
    sprite('ph431_08', 8)
    XImpulseAcceleration(50)
    CreateObject('Eff_431_mc', -1)
    sprite('ph431_09', 8)
    XImpulseAcceleration(50)
    sprite('ph431_10', 8)
    CreateObject('Eff_431_mc_sub1', -1)
    CreateObject('Eff_431_BomBall', -1)
    XImpulseAcceleration(0)
    PrivateSE('phse_02')
    sprite('ph431_11', 8)
    TriggerUponForState('Eff_431_BomBall', 32)
    sprite('ph431_12', 8)
    sprite('ph431_13', 4)
    TriggerUponForState('Eff_431_mc', 32)
    TriggerUponForState('Eff_431_mc_sub1', 32)
    TriggerUponForState('Eff_431_BomBall', 33)
    sprite('ph431_14', 4)
    TriggerUponForState('Eff_431_BomBall', 34)
    callSubroutine('MagicReset')
    Voiceline('ph254')
    CreateObject('Eff_431_bomb', -1)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    callSubroutine('MagicReplace')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    sprite('ph431_15', 3)
    AttackOff()
    sprite('ph431_16', 2)
    sprite('ph431_17', 2)
    CreateObject('UltimateChargeATK', -1)
    sprite('ph431_18', 2)
    setInvincible(0)
    sprite('ph431_19', 3)
    sprite('ph431_20', 3)
    sprite('ph431_21', 3)
    sprite('ph431_22', 6)
    sprite('ph431_23', 6)
    sprite('ph431_24', 4)


@State
def UltimateChargeOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackType(4)

        def upon_32():
            CreateObject('UltimateChargeODAddAtk', 100)
            sendToLabel(0)
    sprite('ph431_00', 6)
    Voiceline('ph253')
    sprite('ph431_01', 6)
    DistortionSettings(94, -1, 0)
    HeatChange(-5000)
    setInvincible(1)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    CreateObject('Eff_431_obi', -1)
    callSubroutine('MagicEffectFastDelete')
    sprite('ph431_02', 6)
    sprite('ph431_03', 6)
    sprite('ph431_04', 8)
    AddX(-90000)
    sprite('ph431_05', 6)
    sprite('ph431_06', 6)
    sprite('ph431_07', 6)
    physicsXImpulse(5000)
    sprite('ph431_08', 8)
    XImpulseAcceleration(50)
    CreateObject('Eff_431_mc', -1)
    sprite('ph431_09', 8)
    XImpulseAcceleration(50)
    sprite('ph431_10', 8)
    CreateObject('Eff_431_mc_sub1', -1)
    CreateObject('Eff_431_BomBall', -1)
    XImpulseAcceleration(0)
    PrivateSE('phse_02')
    sprite('ph431_11', 8)
    TriggerUponForState('Eff_431_BomBall', 32)
    sprite('ph431_12', 8)
    sprite('ph431_13', 4)
    TriggerUponForState('Eff_431_mc', 32)
    TriggerUponForState('Eff_431_mc_sub1', 32)
    TriggerUponForState('Eff_431_BomBall', 33)
    sprite('ph431_14', 4)
    TriggerUponForState('Eff_431_BomBall', 34)
    callSubroutine('MagicReset')
    Voiceline('ph254')
    CreateObject('Eff_431_bomb', -1)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    callSubroutine('MagicReplace')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    Unknown61(0, 1, 0, 4, 0, 0, 0, 3, 0, 9999, 0, 9999)
    SLOT_55 = SLOT_0
    callSubroutine('MagicTableUpDate')
    sprite('ph431_15', 3)
    AttackOff()
    sprite('ph431_16', 2)
    sprite('ph431_17', 2)
    CreateObject('UltimateChargeODATK', -1)
    sprite('ph431_18', 2)
    setInvincible(0)
    sprite('ph431_19', 3)
    sprite('ph431_20', 3)
    sprite('ph431_21', 3)
    sprite('ph431_22', 6)
    sprite('ph431_23', 6)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_17', 4)
    sprite('ph431_18', 4)
    sprite('ph431_16', 4)
    sprite('ph431_19', 4)
    sprite('ph431_20', 4)
    sprite('ph431_21', 4)
    sprite('ph431_22', 8)
    sprite('ph431_23', 8)
    label(9)
    sprite('ph431_24', 4)


@State
def UltimateLock():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(2)
        Damage(100)
        MinimumDamage(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(70)
        Crumple(60)
        DefeatOpponentBehavior(1)
        UseFireHitspark(1)
        MoveAttributes(0, 0, 1, 0, 0)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SetActionMark(1)
            PushbackX(0)
            Hitstop(0)
            callSubroutine('ActiveMagicAllDelete')
        SLOT_66 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ph432_00', 4)
    DistortionSettings(24, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    Voiceline('ph255')
    setInvincible(1)
    sprite('ph432_01', 4)
    sprite('ph432_02', 4)
    sprite('ph432_03', 4)
    sprite('ph432_04', 3)
    sprite('ph432_05', 3)
    sprite('ph432_06', 3)
    sprite('ph432_04', 3)
    sprite('ph432_05', 3)
    sprite('ph432_06', 3)
    sprite('ph432_07', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('ph432_08', 5)
    ScreenShake(0, 10000)
    CreateObject('Eff_432_AtkFire', -1)
    CommonSE('016_explode_0')
    sprite('ph432_09', 2)
    SpriteCall('ph432_08', 2, 2, 2)
    RefreshMultihit()
    Damage(0)
    Hitstop(10)
    AttackP2(100)
    ResetPushbackX()
    HitAnywhere(1)
    DamageEffect(5, '')
    if not SLOT_2:
        setInvincible(0)
    DamageFromStateOnly('UltimateLock_Atk1stLv1')
    if SLOT_4 >= 16:
        DamageFromStateOnly('UltimateLock_Atk1stLv2')
    if SLOT_4 >= 256:
        DamageFromStateOnly('UltimateLock_Atk1stLv3')

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        EnableRapidCancel(0)
    sprite('ph432_09', 3)
    sprite('ph432_10', 3)
    sprite('ph432_11', 3)
    sprite('ph432_09', 3)
    sprite('ph432_10', 3)
    sprite('ph432_11', 3)
    sprite('ph432_12', 6)
    sprite('ph432_13', 6)
    sprite('ph432_14', 5)
    sprite('keep', 1)
    if SLOT_2:
        enterState('UltimateLock_1stSelect')


@State
def UltimateLockOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(2)
        Damage(100)
        MinimumDamage(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(70)
        Crumple(60)
        DefeatOpponentBehavior(1)
        UseFireHitspark(1)
        MoveAttributes(0, 0, 1, 0, 0)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SetActionMark(1)
            PushbackX(0)
            Hitstop(0)
            callSubroutine('ActiveMagicAllDelete')
        SLOT_66 = 1
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ph432_00', 4)
    Voiceline('ph255')
    DistortionSettings(24, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH', -1)
    setInvincible(1)
    sprite('ph432_01', 4)
    sprite('ph432_02', 4)
    sprite('ph432_03', 4)
    sprite('ph432_04', 3)
    sprite('ph432_05', 3)
    sprite('ph432_06', 3)
    sprite('ph432_04', 3)
    sprite('ph432_05', 3)
    sprite('ph432_06', 3)
    sprite('ph432_07', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('ph432_08', 5)
    ScreenShake(0, 10000)
    CreateObject('Eff_432_AtkFire', -1)
    CommonSE('016_explode_0')
    sprite('ph432_09', 2)
    SpriteCall('ph432_08', 2, 2, 2)
    RefreshMultihit()
    Damage(0)
    Hitstop(10)
    AttackP2(100)
    ResetPushbackX()
    HitAnywhere(1)
    DamageEffect(5, '')
    if not SLOT_2:
        setInvincible(0)
    DamageFromStateOnly('UltimateLock_Atk1stLv1')
    if SLOT_4 >= 16:
        DamageFromStateOnly('UltimateLock_Atk1stLv2')
    if SLOT_4 >= 256:
        DamageFromStateOnly('UltimateLock_Atk1stLv3')

    def upon_OPPONENT_HIT():
        clearUponHandler(OPPONENT_HIT)
        EnableRapidCancel(0)
    sprite('ph432_09', 3)
    sprite('ph432_10', 3)
    sprite('ph432_11', 3)
    sprite('ph432_09', 3)
    sprite('ph432_10', 3)
    sprite('ph432_11', 3)
    sprite('ph432_12', 6)
    sprite('ph432_13', 6)
    sprite('ph432_14', 5)
    sprite('keep', 1)
    if SLOT_2:
        enterState('UltimateLock_1stSelect')


@State
def UltimateLock_1stSelect():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
    sprite('ph000_00', 10)
    if SLOT_4 >= 1:
        if SLOT_4 >= 16:
            if SLOT_4 >= 256:
                enterState('UltimateLock_1stLv3')
            else:
                enterState('UltimateLock_1stLv2')
        else:
            enterState('UltimateLock_1stLv1')
    else:
        enterState('UltimateLock_1stLv1')


@State
def UltimateLock_1stLv1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        ForceFaceSprite()
        EnableRapidCancel(0)
    sprite('ph214_00', 4)
    sprite('ph214_01', 4)
    sprite('ph214_02', 4)
    CreateObject('UltimateLock_Atk1stLv1', -1)
    callSubroutine('MagicReset')
    CommonSE('024_getset_b')
    sprite('ph214_03', 6)
    sprite('ph214_04', 6)
    sprite('ph214_05', 6)
    sprite('keep', 1)
    enterState('UltimateLock_2ndSelect')


@State
def UltimateLock_1stLv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        ForceFaceSprite()
        EnableRapidCancel(0)
    sprite('ph202_00', 5)
    sprite('ph202_01', 5)
    sprite('ph202_02', 5)
    sprite('ph202_03', 3)
    CreateObject('UltimateLock_Atk1stLv2', -1)
    callSubroutine('MagicReset')
    CommonSE('024_getset_b')
    CommonSE('016_explode_0')
    CommonSE('016_explode_1')
    sprite('ph202_04', 6)
    sprite('ph202_05', 6)
    sprite('ph202_06', 6)
    sprite('ph202_07', 6)
    sprite('keep', 1)
    enterState('UltimateLock_2ndSelect')


@State
def UltimateLock_1stLv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        ForceFaceSprite()
        EnableRapidCancel(0)
    sprite('ph216_00', 3)
    sprite('ph216_01', 8)
    sprite('ph216_02', 3)
    sprite('ph216_03', 7)
    CreateObject('UltimateLock_Atk1stLv3', -1)
    callSubroutine('MagicReset')
    CommonSE('024_getset_b')
    PrivateSE('phse_02')
    PrivateSE('phse_02')
    sprite('ph216_04', 7)
    sprite('ph216_05', 5)
    sprite('ph216_06', 5)
    sprite('keep', 1)
    enterState('UltimateLock_2ndSelect')


@State
def UltimateLock_2ndSelect():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
    sprite('ph000_00', 10)
    Voiceline('ph256')
    callSubroutine('MagicReplace')
    if SLOT_4 >= 1:
        if SLOT_4 >= 16:
            if SLOT_4 >= 256:
                enterState('UltimateLock_2ndLv4')
            else:
                enterState('UltimateLock_2ndLv3')
        else:
            enterState('UltimateLock_2ndLv2')
    else:
        enterState('UltimateLock_2ndLv1')


@State
def UltimateLock_2ndLv1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ph211_00', 4)
    sprite('ph211_01', 4)
    sprite('ph211_02', 4)
    sprite('ph432_15', 4)
    physicsYImpulse(10000)
    sprite('ph432_16', 4)
    YAccel(50)
    sprite('ph432_17', 4)
    YAccel(50)
    sprite('ph432_18', 3)
    YAccel(0)
    sprite('ph432_19', 3)
    sprite('ph251_00', 3)
    sprite('ph251_01', 3)
    sprite('ph251_02', 4)
    sprite('ph251_03', 4)
    physicsXImpulse(-10000)
    CreateObject('UltimateLock_Atk2ndLv1', -1)
    if SLOT_66:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph251_04', 4)
    XImpulseAcceleration(50)
    sprite('ph251_05', 4)
    XImpulseAcceleration(50)
    sprite('ph432_20', 4)
    XImpulseAcceleration(50)
    sprite('ph432_21', 4)
    XImpulseAcceleration(0)
    sprite('ph251_06', 3)
    sprite('ph251_07', 3)
    sprite('ph251_08', 3)
    sprite('keep', 1)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    if SLOT_66:
        enterState('UltimateLock_ODAttack')
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def UltimateLock_2ndLv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ph203_00', 4)
    sprite('ph203_01', 4)
    physicsYImpulse(10000)
    sprite('ph203_02', 4)
    YAccel(50)
    sprite('ph203_03', 4)
    YAccel(50)
    sprite('ph203_01', 4)
    YAccel(0)
    sprite('ph203_02', 4)
    sprite('ph203_04', 5)
    sprite('ph203_05', 5)
    sprite('ph203_06', 5)
    sprite('ph203_07', 5)
    physicsXImpulse(-12500)
    CreateObject('UltimateLock_Atk2ndLv2', -1)
    if SLOT_66:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph203_08', 5)
    XImpulseAcceleration(50)
    sprite('ph203_09', 6)
    XImpulseAcceleration(50)
    sprite('ph203_10', 6)
    XImpulseAcceleration(50)
    sprite('ph203_08', 6)
    XImpulseAcceleration(0)
    sprite('ph203_09', 6)
    sprite('ph203_10', 4)
    sprite('ph203_11', 3)
    sprite('ph203_15', 3)
    sprite('ph203_16', 3)
    sprite('keep', 1)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    if SLOT_66:
        enterState('UltimateLock_ODAttack')
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def UltimateLock_2ndLv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ph204_00', 4)
    sprite('ph204_01', 4)
    sprite('ph204_02', 4)
    physicsYImpulse(10000)
    sprite('ph204_03', 4)
    YAccel(50)
    sprite('ph204_04', 4)
    YAccel(50)
    sprite('ph204_02', 4)
    YAccel(0)
    sprite('ph204_03', 4)
    sprite('ph204_04', 4)
    sprite('ph204_05', 4)
    sprite('ph204_06', 4)
    sprite('ph204_07', 4)
    physicsXImpulse(-15000)
    CreateObject('UltimateLock_Atk2ndLv3', -1)
    if SLOT_66:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph204_08', 5)
    XImpulseAcceleration(50)
    sprite('ph204_09', 6)
    XImpulseAcceleration(50)
    sprite('ph204_10', 6)
    XImpulseAcceleration(50)
    sprite('ph204_08', 6)
    XImpulseAcceleration(0)
    sprite('ph204_08', 6)
    sprite('ph204_09', 6)
    sprite('ph204_10', 6)
    sprite('ph204_08', 6)
    sprite('ph204_09', 6)
    sprite('ph204_10', 6)
    sprite('ph204_08', 2)
    sprite('ph204_11', 3)
    sprite('ph204_12', 3)
    sprite('ph204_15', 3)
    sprite('ph204_16', 3)
    sprite('keep', 1)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    if SLOT_66:
        enterState('UltimateLock_ODAttack')
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def UltimateLock_2ndLv4():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)
        EnableRapidCancel(0)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ph205_00', 5)
    sprite('ph205_01', 5)
    sprite('ph205_02', 4)
    physicsYImpulse(10000)
    sprite('ph205_03', 4)
    YAccel(50)
    sprite('ph205_04', 4)
    YAccel(50)
    sprite('ph205_02', 4)
    YAccel(0)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    sprite('ph205_05', 5)
    sprite('ph205_06', 5)
    physicsXImpulse(-20000)
    CreateObject('UltimateLock_Atk2ndLv4', -1)
    if SLOT_66:
        ObjectUpon(STATE_END, 32)
    callSubroutine('MagicReset')
    sprite('ph205_07', 5)
    XImpulseAcceleration(50)
    sprite('ph205_08', 6)
    XImpulseAcceleration(50)
    sprite('ph205_09', 6)
    XImpulseAcceleration(50)
    sprite('ph205_07', 6)
    XImpulseAcceleration(0)
    sprite('ph205_08', 6)
    sprite('ph205_09', 6)
    sprite('ph205_07', 6)
    sprite('ph205_08', 6)
    sprite('ph205_09', 6)
    sprite('ph205_07', 6)
    sprite('ph205_08', 6)
    sprite('ph205_09', 6)
    sprite('ph205_07', 6)
    sprite('ph205_08', 6)
    sprite('ph205_09', 4)
    sprite('ph205_10', 3)
    sprite('ph205_11', 3)
    sprite('ph205_15', 3)
    sprite('ph205_16', 3)
    sprite('keep', 1)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()
    if SLOT_66:
        enterState('UltimateLock_ODAttack')
    sprite('ph020_05', 3)
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def UltimateLock_ODAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        NoAttackDuringAction(1)
        setInvincible(1)

        def upon_LANDING():
            clearUponHandler(LANDING)
            sendToLabel(1)
    sprite('ph320_00', 6)
    sprite('ph320_01', 6)
    DistortionSettings(40, -1, 0)
    sprite('ph320_02', 6)
    sprite('ph321_01', 3)
    RefreshMultihit()
    sprite('ph320_02', 3)
    RefreshMultihit()
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 3)
    RefreshMultihit()
    sprite('ph320_02', 3)
    RefreshMultihit()
    sprite('ph321_00', 3)
    RefreshMultihit()
    sprite('ph321_01', 3)
    RefreshMultihit()
    sprite('ph320_02', 3)
    RefreshMultihit()
    sprite('ph321_00', 10)
    Voiceline('ph257')
    sprite('ph321_02', 8)
    sprite('ph321_03', 6)
    CreateObject('UltimateLock_AtkODAdd', -1)
    sprite('ph321_04', 6)
    sprite('ph321_05', 20)
    sprite('ph321_06', 8)
    sprite('ph321_07', 8)
    sprite('ph321_08', 8)
    sprite('ph020_05', 3)
    EndYPhysicsImpulse()
    sprite('ph020_06', 3)
    label(0)
    sprite('ph020_07', 4)
    sprite('ph020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)
    sprite('ph024_01', 3)
    sprite('ph024_02', 3)
    sprite('ph024_03', 3)
    sprite('ph024_04', 3)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()

        def upon_32():
            enterState('AstralHeatExe')
        setInvincible(1)
    sprite('ph450_00', 3)
    sprite('ph450_01', 3)
    Voiceline('ph290')
    sprite('ph450_02', 3)
    DistortionSettings(52, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PH_AH', -1)
    sprite('ph450_02', 5)
    sprite('ph450_03', 5)
    sprite('ph450_04', 5)
    sprite('ph450_02', 5)
    sprite('ph450_03', 5)
    sprite('ph450_04', 5)
    sprite('ph450_02', 5)
    sprite('ph450_03', 5)
    sprite('ph450_04', 5)
    sprite('ph450_05', 5)
    sprite('ph450_06', 5)
    sprite('ph450_07', 5)
    sprite('ph450_08', 5)
    sprite('ph450_09', 3)
    CreateObject('AstralHeatAtk', -1)
    CreateObject('Eff_450_EyeBurning', 0)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_12', 6)
    DespawnEAEffect('Eff_450_EyeBurning')
    setInvincible(0)
    sprite('ph450_13', 6)
    sprite('ph450_14', 6)
    Voiceline('ph294')
    sprite('ph450_15', 6)
    sprite('ph450_16', 6)
    sprite('ph450_17', 6)
    sprite('ph450_18', 6)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)

        def RunOnObject_22():
            Unknown23169(1)
    sprite('ph450_09', 3)
    HUDVisibillity(1)
    AstralHeatCleanup(1, 1)
    PlayPlayAstralBGM(1)
    CreateObject('Eff_450_EyeBurning', 0)
    callSubroutine('ActiveMagicAllDelete')
    callSubroutine('MagicReset')
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    CreateObject('AstralHeat_Hinokagutsuchi', -1)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    Voiceline('ph291')
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    CreateObject('AstralHeatAtk2nd', -1)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 3)
    sprite('ph450_09', 3)
    sprite('ph450_10', 3)
    sprite('ph450_11', 20)
    CreateObject('Eff_450_Terepo', -1)
    CommonSE('000_airdash_0')
    DespawnEAEffect('Eff_450_EyeBurning')
    Visibility(1)
    sprite('ph450_11', 20)
    Visibility(1)
    CreateObject('phAst_ShaSha00', -1)
    sprite('null', 4)
    SetBackground(3)
    Unknown20010(0, -10000000, 10000000)
    AbsoluteY(800000)
    XPositionRelativeFacing(800000)
    Size(500)
    FaceLeft()

    def RunOnObject_22():
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        Visibility(1)
    CreateObject('AstralHeat_Camera', -1)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    Voiceline('ph292')
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    Visibility(0)
    CreateParticle('phef450_terepo', -1)
    CreateObject('Eff_450_circle', -1)

    def RunOnObject_1():
        AddY(-150000)
        AddScale(-600)
    CommonSE('000_airdash_0')
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    CommonSE('022_magiccircle_b')
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    PrivateSE('phse_04')
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_19', 3)
    sprite('ph450_20', 3)
    sprite('ph450_21', 3)
    sprite('ph450_22', 3)
    Voiceline('ph293')
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    PrivateSE('phse_10')
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    SetBackground(2)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    Visibility(1)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 130)
    CreateObject('AstralHeatEff_MeteoMato', -1)
    sprite('ph450_23', 3)
    CreateObject('AstralHeatLastAtk', -1)

    def RunOnObject_22():
        AlphaValue(0)
    sprite('ph450_24', 3)
    sprite('ph450_25', 3)
    sprite('ph450_23', 3)
    sprite('ph450_24', 3)
    sprite('ph450_25', 150)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    sprite('ph450_23', 3)
    WinAction()
    DemoTimer(120)
    sprite('ph450_24', 3)
    sprite('ph450_25', 32767)
    EndDemo()


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('ph054')
    sprite('ph900_00', 1)
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
    sprite('ph900_00', 32767)
    CreateObject('ph900Eff', 0)
    CreateObject('ph900Eff', 1)
    CreateObject('ph900Eff', 2)
    CreateObject('ph900Eff3', 3)
    CreateObject('ph900Eff2', 4)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(200000)
    sprite('ph901_00', 54)
    physicsYImpulse(-150)
    sprite('ph901_00', 54)
    physicsYImpulse(150)
    Voiceline('ph055')
    label(0)
    sprite('ph901_00', 54)
    physicsYImpulse(-150)
    sprite('ph901_00', 54)
    physicsYImpulse(150)
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5500)
        AirPushbackY(63000)
        AirUntechableTime(90)
        Hitstop(20)
        Blockstun(26)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDRevEff')
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
    sprite('ph440_00', 5)
    E0EAEffect('BurstDDeff', 103)
    sprite('ph440_01', 5)
    physicsXImpulse(2500)
    sprite('ph440_02', 9)
    XImpulseAcceleration(200)
    Voiceline('ph280')
    sprite('ph440_03', 3)
    XImpulseAcceleration(800)
    CommonSE('004_swing_grap_1_2')
    callSubroutine('CheckMirrerKick')
    sprite('ph440_04', 3)
    setInvincible(0)
    XImpulseAcceleration(25)
    sprite('ph440_04', 2)
    XImpulseAcceleration(50)
    sprite('ph440_07', 2)
    sprite('ph440_07', 4)
    XImpulseAcceleration(50)
    sprite('ph440_08', 4)
    XImpulseAcceleration(50)
    sprite('ph440_08', 2)
    XImpulseAcceleration(0)
    sprite('ph440_09', 6)
    sprite('ph440_10', 6)
    sprite('ph440_11', 5)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5500)
        AirPushbackY(63000)
        AirUntechableTime(90)
        Hitstop(20)
        Blockstun(26)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDRevEff')
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
    sprite('ph440_00', 3)
    E0EAEffect('BurstDDeff', 103)
    sprite('ph440_01', 3)
    physicsXImpulse(2500)
    sprite('ph440_02', 3)
    XImpulseAcceleration(200)
    Voiceline('ph280')
    sprite('ph440_03', 3)
    XImpulseAcceleration(800)
    CommonSE('004_swing_grap_1_2')
    callSubroutine('CheckMirrerKick')
    sprite('ph440_04', 3)
    setInvincible(0)
    XImpulseAcceleration(25)
    sprite('ph440_04', 2)
    XImpulseAcceleration(50)
    sprite('ph440_07', 2)
    sprite('ph440_07', 4)
    XImpulseAcceleration(50)
    sprite('ph440_08', 4)
    XImpulseAcceleration(50)
    sprite('ph440_08', 2)
    XImpulseAcceleration(0)
    sprite('ph440_09', 6)
    sprite('ph440_10', 6)
    sprite('ph440_11', 5)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        SetBackground(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('ph440_03', 6)
    StartMultihit()
    CreateObject('BurstDDCamera', -1)
    sprite('ph440_04', 6)
    sprite('ph440_05', 6)
    sprite('ph440_06', 6)
    sprite('ph440_07', 6)
    sprite('ph440_12', 6)
    sprite('ph440_13', 6)
    sprite('ph440_14', 6)
    sprite('ph440_15', 6)
    sprite('ph440_16', 6)
    sprite('ph440_17', 2)
    Voiceline('ph281')
    CreateObject('BurstDDEff', -1)
    CreateObject('BurstDDRevEff', -1)
    if SLOT_51:
        ObjectUpon(STATE_END, 32)
    sprite('ph440_18', 2)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    label(1)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    TriggerUponForState('BurstDDCamera', 33)
    sprite('ph440_19', 3)
    sprite('ph440_20', 3)
    sprite('ph440_21', 3)
    sprite('ph440_22', 6)
    sprite('ph440_23', 6)
    sprite('ph440_24', 6)


@Subroutine
def MouthTableInit():
    Unknown18011('ph000', 12643, 24880, 25398, 24886, 25398, 54, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph055', 13921, 13923, 12897, 25392, 12340, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('ph400', 12641, 25397, 24886, 12338, 13923, 13921, 13923, 
        13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph401', 12641, 25397, 24886, 12337, 13411, 24880, 25398, 
        24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph404', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13155, 24880, 25398, 24886, 25398, 
        24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('ph405', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph406', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13155, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
        24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph407', 13921, 13923, 13921, 13155, 24880, 25398, 24886, 
        25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph408', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 12643, 24885, 25398, 24886, 25398, 
        24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('ph411', 13921, 13923, 13921, 13155, 24880, 25398, 24886, 
        25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph412', 13921, 25392, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('ph413', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph414', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph415', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph416', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ph417', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph400', 13921, 13923, 13153, 25392, 12338, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph401', 13665, 13667, 13665, 13667, 13665, 13667, 
            13921, 13155, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 
            25398, 24886, 25398, 24886, 25398, 12337, 13153, 25392, 54, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph404', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13153, 
            25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph405', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13155, 24880, 25398, 24886, 
            25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph406', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13155, 24880, 25398, 24886, 25398, 24886, 
            25398, 24886, 25398, 24886, 25395, 54, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph407', 12897, 25392, 12340, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph408', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13155, 24880, 25398, 24886, 
            25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
            24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ph411', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ph412', 13921, 25392, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph413', 13153, 25397, 13619, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('ph414', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('ph415', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
            13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ph416', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('ph417', 13921, 13923, 13921, 13923, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('ha'):
            Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 13155, 25392, 24888, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14433, 14435, 14433, 14435, 14433, 13923,
                24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 13411, 24885, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14433, 14435, 14433, 12643, 24885, 25400,
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('ph000', 13921, 13923, 13921, 13155, 24880, 25398,
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 14435, 14433, 13923,
                24880, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14433, 14435, 14433, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 14435, 14433, 13923,
                25392, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 
                25400, 24888, 25400, 24888, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14177, 14179, 14177, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('es'):
            Unknown18011('ph000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 12641, 25397, 12343, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 12641, 25394, 12342, 14177, 14179, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('ph000', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14433, 14435, 14433, 13923, 24880, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rg'):
            if SLOT_138:
                Unknown18011('ph500', 14433, 14435, 14433, 14435, 14433, 
                    14435, 14433, 13667, 24880, 14385, 14435, 14433, 13411,
                    24885, 25400, 24888, 25400, 13620, 14433, 14435, 14433,
                    14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ph501', 13921, 13923, 13921, 13923, 13921, 
                    14435, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0)
            else:
                Unknown18011('ph500', 14177, 14179, 14177, 13923, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('ph501', 14179, 12641, 25392, 24887, 12337, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 12641, 25392, 12341, 14433, 14435,
                    14433, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('ph502', 14689, 14691, 14689, 14691, 14689, 14691,
                14689, 13923, 24880, 25401, 24889, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph503', 12641, 25394, 24886, 25398, 12341, 13921,
                13923, 13921, 13923, 14433, 14435, 14433, 14435, 14433, 
                14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('ph504', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 13620, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph505', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13667, 24880, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            Unknown18011('ph506', 12641, 25397, 13617, 14433, 13923, 14433,
                13923, 14433, 14179, 24880, 25400, 24886, 25400, 24886, 
                25400, 24886, 25400, 24886, 25400, 24886, 25400, 13620, 
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('ph507', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 14179, 24880, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 12342, 14433, 13923, 14433, 13923, 14433, 
                13923, 14433, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ha'):
            Unknown18011('ph520', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                14433, 13923, 14433, 13923, 24880, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 24886, 25400, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph521', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 13667, 24880, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ny'):
            Unknown18011('ph522', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13411, 24885, 25400, 24886, 25400, 
                24886, 25400, 12340, 14433, 13923, 14433, 13923, 14433, 
                13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('ph523', 14433, 14691, 24880, 25400, 24886, 25400,
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                12342, 14433, 13667, 24885, 25400, 24886, 25400, 24886, 
                25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
        if CharacterIDCheck('hz'):
            Unknown18011('ph526', 14433, 13923, 14433, 13923, 14433, 13411,
                24885, 25400, 24886, 25400, 24886, 25400, 13620, 14433, 
                13923, 14433, 13923, 14433, 13923, 14433, 13923, 14433, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('ph527', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13411, 24885, 25400, 24886, 25400, 24886, 25400, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('vh'):
            Unknown18011('ph532', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 
                14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph533', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 24880, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('pt'):
            Unknown18011('ph534', 14433, 13923, 14433, 13923, 14433, 14179,
                24880, 25400, 24886, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph535', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 24880, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('rl'):
            Unknown18011('ph536', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 14433, 13923, 14433, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph537', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 24880, 25400, 24886, 25400, 24886, 25400, 
                24886, 25400, 24886, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('am'):
            Unknown18011('ph540', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13923, 14433, 13923, 24880, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('ph541', 14433, 13923, 14433, 13923, 14433, 13923,
                14433, 13667, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('ph540', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('ph546', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 24880, 25400, 13620, 14433, 14435, 14433, 
                14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph547', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 13411, 24880, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('ph548', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 24880, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph549', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 13411, 24885, 25400, 24888, 25400, 24888, 25400, 
                24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('ph550', 14433, 14435, 14433, 14435, 14433, 13923,
                24880, 25400, 24888, 25400, 24888, 25400, 12342, 14433, 
                14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
                14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('ph551', 14433, 14435, 14433, 14435, 14433, 13923,
                24880, 25400, 12337, 14433, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('ph552', 12641, 25392, 13617, 13921, 13923, 13921,
                13923, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph553', 13921, 13923, 24880, 25398, 24886, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 12339, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mi'):
            Unknown18011('ph562', 12641, 25392, 24886, 12337, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph563', 12641, 25394, 24886, 25400, 24888, 25400,
                24886, 25397, 24885, 12849, 13923, 13921, 13923, 14177, 
                14179, 13921, 13923, 12641, 25392, 24885, 25397, 24885, 
                14385, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
        if CharacterIDCheck('su'):
            Unknown18011('ph564', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph565', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13667, 24885, 25399, 24885, 25399, 
                24885, 25399, 24885, 25399, 12340, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('es'):
            Unknown18011('ph566', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13411, 24885, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph567', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13411, 24885, 25399, 24885, 25399, 
                24885, 25399, 24885, 25399, 12341, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('ph000', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13411, 24880, 25399, 24885, 25399, 24885, 25399, 53,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph400', 14177, 14179, 14177, 14179, 14177, 13923,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph401', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 
                24885, 25399, 24885, 25399, 24885, 25399, 53, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph570', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13923, 24885, 25399, 24887, 25399, 
                24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ph571', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13667, 24880, 25399, 24885, 25399, 
                24885, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


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
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(120)
    if CharacterIDCheck('rc'):
        SyncEntry()
        gotoLabel(130)
    if CharacterIDCheck('ha'):
        SyncEntry()
        gotoLabel(200)
    if CharacterIDCheck('ny'):
        SyncEntry()
        gotoLabel(210)
    if CharacterIDCheck('hz'):
        SyncEntry()
        gotoLabel(230)
    if CharacterIDCheck('vh'):
        SyncEntry()
        gotoLabel(260)
    if CharacterIDCheck('pt'):
        SyncEntry()
        gotoLabel(270)
    if CharacterIDCheck('rl'):
        SyncEntry()
        gotoLabel(280)
    if CharacterIDCheck('am'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2300)
        else:
            gotoLabel(300)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('kk'):
        SyncEntry()
        gotoLabel(340)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ce'):
        SyncEntry()
        gotoLabel(360)
    if CharacterIDCheck('mi'):
        SyncEntry()
        gotoLabel(410)
    if CharacterIDCheck('su'):
        SyncEntry()
        gotoLabel(420)
    if CharacterIDCheck('es'):
        SyncEntry()
        gotoLabel(430)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if random_(2, 0, 33):
        conditionalSendToLabel(20)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(0)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    Voiceline('ph412')
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    Voiceline('ph413')
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(10)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(11)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(11)
    sprite('ph601_00ex01', 6)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph414')
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 13)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(12)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(12)
    label(13)
    sprite('ph601_04', 8)
    Voiceline('ph415')
    if SLOT_44:
        DemoTimer(170)
    else:
        DemoTimer(60)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    ExitState()
    label(20)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(21)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(21)
    sprite('ph601_00ex01', 6)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph416')
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 23)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(22)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(22)
    label(23)
    sprite('ph601_04', 8)
    Voiceline('ph417')
    if SLOT_44:
        DemoTimer(90)
    else:
        DemoTimer(90)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    ExitState()
    label(100)

    def upon_32():
        SLOT_52 = 1
    label(101)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(101)
    label(102)
    sprite('ph600_00', 6)
    clearUponHandler(32)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    Voiceline('ph500')
    DemoTimer(360)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    loopRest()
    ExitState()
    label(1100)
    sprite('ph600_15', 1)

    def upon_32():
        SLOT_52 = 1
        Voiceline('ph500')
        DemoTimer(210)
    label(1101)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(1101)
    SetActionMark(10)
    label(1102)
    sprite('ph600_15', 6)
    AddActionMark(-1)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1102)
    sprite('ph600_18', 6)
    loopRest()
    ExitState()
    label(110)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)

    def upon_32():
        SLOT_52 = 1
    label(111)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(111)
    sprite('ph601_00ex01', 6)
    clearUponHandler(32)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph502')
    DemoTimer(250)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 113)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(112)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(112)
    label(113)
    sprite('ph601_04', 8)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    ExitState()
    label(120)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(120)
    sprite('ph600_00', 6)
    Voiceline('ph504')
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    DemoTimer(360)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    ObjectUpon(22, 32)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(130)
    sprite('ph601_00ex01', 1)
    CreateObject('Entry_HinoEff', -1)

    def upon_32():
        SLOT_52 = 1

    def upon_EVERY_FRAME():
        if not SLOT_17:
            clearUponHandler(EVERY_FRAME)
            TriggerUponForState('Entry_HinoEff', 33)
    label(131)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(131)
    label(132)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(132)
    sprite('ph601_00ex01', 6)
    clearUponHandler(32)
    Voiceline('ph506')
    DemoTimer(400)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 134)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(133)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(133)
    label(134)
    sprite('ph601_04', 8)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    ExitState()
    label(200)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(200)
    sprite('ph600_00', 6)
    clearUponHandler(32)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    Voiceline('ph520')
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(210)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(210)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    Voiceline('ph522')
    DemoTimer(360)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(230)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(230)
    sprite('ph600_00', 6)
    Voiceline('ph526')
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    DemoTimer(360)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    ObjectUpon(22, 32)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    loopRest()
    ExitState()
    label(260)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(261)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(261)
    sprite('ph601_00ex01', 6)
    clearUponHandler(32)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph532')
    DemoTimer(400)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 263)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(262)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(262)
    label(263)
    sprite('ph601_04', 8)
    clearUponHandler(32)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    ObjectUpon(22, 32)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    ExitState()
    label(270)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(270)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    Voiceline('ph534')
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(280)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(280)
    sprite('ph600_00', 6)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_00', 6)
    CreateObject('phef_600_FireWall', -1)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_00', 6)
    ConstantAlphaModifier(-8)
    sprite('ph600_01', 6)
    sprite('ph600_02', 6)
    sprite('ph600_03', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    ColorTransition(4294967295, 20)
    sprite('ph600_03', 6)
    sprite('ph600_04', 6)
    sprite('ph600_05', 6)
    Voiceline('ph536')
    DemoTimer(360)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_06', 6)
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_07', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_08', 6)
    CreateParticle('phef_340mant', 0)
    CreateParticle('phef_340mant', 1)
    sprite('ph600_09', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_10', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_11', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_12', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_13', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_14', 6)
    CreateParticle('phef_340mant', 0)
    CreateObject('phef_600_Hat', -1)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_15', 6)
    CreateParticle('phef_340mant', 0)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(300)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(301)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(301)
    sprite('ph601_00ex01', 6)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph540')
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 303)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(302)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(302)
    label(303)
    sprite('ph601_04', 8)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2300)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(2301)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2301)
    sprite('ph601_00ex01', 6)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph540')
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 2303)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(2302)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(2302)
    label(2303)
    sprite('ph601_04', 8)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    ObjectUpon(22, 32)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    ExitState()
    label(330)

    def upon_32():
        SLOT_52 = 1
    label(331)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    if not SLOT_52:
        notConditionalSendToLabel(331)
    sprite('ph300_00', 6)
    clearUponHandler(32)
    Voiceline('ph546')
    DemoTimer(300)
    sprite('ph300_01', 6)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_01', 6)
    sprite('ph300_00', 6)
    ExitState()
    label(340)
    label(341)
    sprite('ph602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(341)
    sprite('ph602_00', 100)
    Voiceline('ph548')
    loopRest()
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph602_00', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph602_01', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    ColorTransition(4291310130, 18)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph602_05', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph331_10', 7)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    EnableAfterimage(0)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(350)
    sprite('ph601_00ex01', 6)
    CreateObject('Entry_HinoEff', -1)
    label(351)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(351)
    sprite('ph601_00ex01', 6)
    TriggerUponForState('Entry_HinoEff', 33)
    Voiceline('ph550')
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00ex01', 6)
    sprite('ph601_00ex02', 6)
    sprite('ph601_00ex03', 6)
    sprite('ph601_00ex04', 6)
    sprite('ph601_00ex05', 6)
    sprite('ph601_00ex06', 6)
    sprite('ph601_00ex07', 6)
    sprite('ph601_00ex08', 6)
    sprite('ph601_00ex09', 6)
    sprite('ph601_00ex10', 6)
    sprite('ph601_00', 15)
    uponSendToLabel(LANDING, 353)
    CreateObject('Entry_Hinokagutsuchi', -1)
    TriggerUponForState('Entry_HinoEff', 32)
    physicsYImpulse(4000)
    setGravity(250)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    label(352)
    sprite('ph601_01', 6)
    sprite('ph601_02', 6)
    sprite('ph601_03', 6)
    gotoLabel(352)
    label(353)
    sprite('ph601_04', 8)
    sprite('ph601_05', 8)
    sprite('ph601_06', 8)
    loopRest()
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(360)
    uponSendToLabel(32, 362)
    label(361)
    sprite('ph602_00', 6)
    loopRest()
    gotoLabel(361)
    label(362)
    sprite('ph602_00', 100)
    Voiceline('ph552')
    loopRest()
    sprite('ph602_00', 6)
    clearUponHandler(32)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph602_00', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph602_01', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    ColorTransition(4291310130, 18)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph602_05', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph331_10', 7)
    EnableAfterimage(0)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(410)
    sprite('ph602_00', 32767)
    uponSendToLabel(32, 411)
    loopRest()
    label(411)
    sprite('ph602_00', 30)
    sprite('ph602_00', 65)
    Voiceline('ph562')
    loopRest()
    sprite('ph602_00', 6)
    clearUponHandler(32)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph602_00', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph602_01', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    ColorTransition(4291310130, 18)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph602_05', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph331_10', 7)
    EnableAfterimage(0)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(420)
    sprite('keep', 2)

    def upon_32():
        SetActionMark(1)
    label(421)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(421)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    sprite('ph600_15', 7)
    Voiceline('ph564')
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    SetActionMark(7)
    label(422)
    sprite('ph600_15', 7)
    AddActionMark(-1)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(422)
    sprite('ph600_18', 7)
    sprite('ph333_00', 6)
    sprite('ph333_01', 6)
    sprite('ph333_02', 6)
    sprite('ph333_03', 30)
    SetActionMark(6)
    label(423)
    sprite('ph333_03', 10)
    AddActionMark(-1)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(423)
    sprite('ph333_04', 4)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(5000, 100000)
    CreateObject('Event_phef_600_Fire', -1)
    CreateObject('Event_phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    CreateObject('Event_phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph333_07', 5)
    CreateObject('Event_phef_600_FireWall', -1)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    ColorTransition(4294967295, 20)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_08', 6)
    sprite('ph333_09', 6)
    loopRest()
    DemoTimer(45)
    loopRest()
    ExitState()
    label(430)
    sprite('keep', 2)

    def upon_32():
        SetActionMark(1)
    label(431)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(431)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    sprite('ph600_15', 7)
    Voiceline('ph566')
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    SetActionMark(7)
    label(432)
    sprite('ph600_15', 7)
    AddActionMark(-1)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(432)
    sprite('ph600_18', 7)
    DemoTimer(120)
    loopRest()
    ExitState()
    label(440)
    sprite('ph602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(440)
    sprite('ph602_00', 100)
    Voiceline('ph570')
    loopRest()
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph602_00', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph602_00', 6)
    sprite('ph602_00', 6)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph602_01', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    ColorTransition(4291310130, 18)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    sprite('ph602_02', 6)
    sprite('ph602_03', 6)
    sprite('ph602_04', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph602_05', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph331_10', 7)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    EnableAfterimage(0)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    if CharacterIDCheck('ce'):
        conditionalSendToLabel(360)
    sprite('ph615_00', 5)
    sprite('ph615_01', 5)
    sprite('ph615_02', 5)
    if random_(2, 0, 50):
        Voiceline('ph400')
    else:
        Voiceline('ph401')
    DemoEndOnVoiceEnd(1)
    sprite('ph615_03', 5)
    sprite('ph615_04', 5)
    label(0)
    sprite('ph615_05', 5)
    sprite('ph615_06', 5)
    sprite('ph615_07', 5)
    sprite('ph615_08', 5)
    sprite('ph615_09', 5)
    sprite('ph615_10', 5)
    gotoLabel(0)
    label(360)
    sprite('ph001_00', 7)
    if random_(2, 0, 50):
        Voiceline('ph400')
    else:
        Voiceline('ph401')
    DemoEndOnVoiceEnd(1)
    sprite('ph001_01', 7)
    sprite('ph001_02', 7)
    CreateObject('ph001Eff', -1)
    CommonSE('015_blaze_2')
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    label(361)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_02', 7)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    loopRest()
    gotoLabel(361)


@State
def CmnActMatchWin():
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
    if CharacterIDCheck('rc'):
        conditionalSendToLabel(130)
    if CharacterIDCheck('ha'):
        conditionalSendToLabel(200)
    if CharacterIDCheck('ny'):
        conditionalSendToLabel(210)
    if CharacterIDCheck('hz'):
        conditionalSendToLabel(230)
    if CharacterIDCheck('vh'):
        conditionalSendToLabel(260)
    if CharacterIDCheck('pt'):
        conditionalSendToLabel(270)
    if CharacterIDCheck('rl'):
        conditionalSendToLabel(280)
    if CharacterIDCheck('am'):
        conditionalSendToLabel(300)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('kk'):
        conditionalSendToLabel(340)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ce'):
        conditionalSendToLabel(360)
    if CharacterIDCheck('mi'):
        if SLOT_138:
            gotoLabel(410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('su'):
        conditionalSendToLabel(420)
    if CharacterIDCheck('es'):
        conditionalSendToLabel(430)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    label(482)
    if SLOT_123:
        conditionalSendToLabel(10)
    if SLOT_124:
        conditionalSendToLabel(10)
    if SLOT_109:
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(20)
    AttackDefaults_StandingSpecial()
    AttackLevel_(3)
    Damage(0)
    AirPushbackX(0)
    AirPushbackY(-30000)
    Floorslide(1)
    AttackDirection(0)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    DisableOppPushCollision(1)
    HitBackReturnIgnore(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            sendToLabel(22)
    sprite('ph030_00', 7)
    physicsXImpulse(6000)
    CameraControlEnable(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    label(21)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(21)
    label(22)
    sprite('ph610_00', 5)
    sprite('ph610_01', 5)
    sprite('ph610_02', 5)
    sprite('ph610_03', 5)
    sprite('ph610_04', 5)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    if random_(2, 0, 50):
        Voiceline('ph406')
    else:
        Voiceline('ph407')
    DemoEndOnVoiceEnd(1)
    label(23)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    gotoLabel(23)
    label(10)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph408')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(11)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(11)
    label(100)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph501')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(101)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(101)
    label(1100)
    sprite('ph615_00', 7)
    sprite('ph615_01', 7)
    sprite('ph615_02', 7)
    sprite('ph615_03', 7)
    sprite('ph615_04', 7)
    Voiceline('ph501')
    DemoEndOnVoiceEnd(1)
    label(1101)
    sprite('ph615_05', 6)
    sprite('ph615_06', 6)
    sprite('ph615_07', 6)
    sprite('ph615_08', 6)
    sprite('ph615_09', 6)
    sprite('ph615_10', 6)
    loopRest()
    gotoLabel(1101)
    label(110)
    if SLOT_109:
        conditionalSendToLabel(482)
    AttackDefaults_StandingSpecial()
    AttackLevel_(3)
    Damage(0)
    AirPushbackX(0)
    AirPushbackY(-30000)
    Floorslide(1)
    AttackDirection(0)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    DisableOppPushCollision(1)
    HitBackReturnIgnore(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            sendToLabel(112)
    sprite('ph030_00', 7)
    physicsXImpulse(6000)
    CameraControlEnable(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    label(111)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('ph610_00', 5)
    sprite('ph610_01', 5)
    sprite('ph610_02', 5)
    sprite('ph610_03', 5)
    sprite('ph610_04', 5)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    Voiceline('ph503')
    DemoEndOnVoiceEnd(1)
    label(113)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    gotoLabel(113)
    label(120)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph505')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(121)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(121)
    label(130)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph507')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(131)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(131)
    label(200)
    if SLOT_109:
        conditionalSendToLabel(482)
    AttackDefaults_StandingSpecial()
    AttackLevel_(3)
    Damage(0)
    AirPushbackX(0)
    AirPushbackY(-30000)
    Floorslide(1)
    AttackDirection(0)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    DisableOppPushCollision(1)
    HitBackReturnIgnore(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            sendToLabel(202)
    sprite('ph030_00', 7)
    physicsXImpulse(6000)
    CameraControlEnable(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    label(201)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('ph610_00', 5)
    sprite('ph610_01', 5)
    sprite('ph610_02', 5)
    sprite('ph610_03', 5)
    sprite('ph610_04', 5)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    Voiceline('ph521')
    DemoEndOnVoiceEnd(1)
    label(203)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    gotoLabel(203)
    label(210)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph523')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(211)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(211)
    label(230)
    if SLOT_109:
        conditionalSendToLabel(482)
    AttackDefaults_StandingSpecial()
    AttackLevel_(3)
    Damage(0)
    AirPushbackX(0)
    AirPushbackY(-30000)
    Floorslide(1)
    AttackDirection(0)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    DisableOppPushCollision(1)
    HitBackReturnIgnore(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            sendToLabel(232)
    sprite('ph030_00', 7)
    physicsXImpulse(6000)
    CameraControlEnable(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    label(231)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(231)
    label(232)
    sprite('ph610_00', 5)
    sprite('ph610_01', 5)
    sprite('ph610_02', 5)
    sprite('ph610_03', 5)
    sprite('ph610_04', 5)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    Voiceline('ph527')
    DemoEndOnVoiceEnd(1)
    label(233)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    gotoLabel(233)
    label(260)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph533')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(261)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(261)
    label(270)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph535')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(271)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(271)
    label(280)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph537')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(281)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(281)
    label(300)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph541')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(301)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(301)
    label(330)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph547')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(331)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(331)
    label(340)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph549')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(341)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(341)
    label(350)
    if SLOT_109:
        conditionalSendToLabel(482)
    AttackDefaults_StandingSpecial()
    AttackLevel_(3)
    Damage(0)
    AirPushbackX(0)
    AirPushbackY(-30000)
    Floorslide(1)
    AttackDirection(0)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    DisableOppPushCollision(1)
    HitBackReturnIgnore(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            physicsXImpulse(0)
            sendToLabel(352)
    sprite('ph030_00', 7)
    physicsXImpulse(6000)
    CameraControlEnable(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    label(351)
    sprite('ph030_01', 7)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    gotoLabel(351)
    label(352)
    sprite('ph610_00', 5)
    sprite('ph610_01', 5)
    sprite('ph610_02', 5)
    sprite('ph610_03', 5)
    sprite('ph610_04', 5)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    Voiceline('ph551')
    DemoEndOnVoiceEnd(1)
    label(353)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    gotoLabel(353)
    label(360)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph553')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(301)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(301)
    label(410)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    Voiceline('ph563')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(411)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(411)
    label(1410)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    Voiceline('ph563')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    sprite('ph611_15', 8)
    label(1411)
    sprite('ph611_16', 8)
    sprite('ph611_17', 8)
    sprite('ph611_18', 8)
    gotoLabel(1411)
    label(420)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph565')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    label(421)
    sprite('ph611_15', 7)
    sprite('ph611_16', 7)
    sprite('ph611_17', 7)
    sprite('ph611_18', 7)
    loopRest()
    gotoLabel(421)
    label(430)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph567')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    label(431)
    sprite('ph611_15', 7)
    sprite('ph611_16', 7)
    sprite('ph611_17', 7)
    sprite('ph611_18', 7)
    loopRest()
    gotoLabel(431)
    label(440)
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 6)
    sprite('ph611_03', 15)
    sprite('ph611_04', 6)
    sprite('ph611_05', 6)
    Voiceline('ph571')
    DemoEndOnVoiceEnd(1)
    sprite('ph611_06', 6)
    sprite('ph611_07', 6)
    sprite('ph611_08', 15)
    sprite('ph611_09', 5)
    CommonSE('019_cloth_c')
    sprite('ph611_10', 5)
    sprite('ph611_11', 5)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph611_12', 5)
    sprite('ph611_13', 5)
    sprite('ph611_14', 5)
    label(441)
    sprite('ph611_15', 7)
    sprite('ph611_16', 7)
    sprite('ph611_17', 7)
    sprite('ph611_18', 7)
    loopRest()
    gotoLabel(441)


@State
def CmnActLose():
    sprite('ph620_00', 30)
    Voiceline('ph411')
    sprite('ph620_01', 6)
    sprite('ph620_02', 6)
    sprite('ph620_03', 6)
    sprite('ph620_04', 6)
    sprite('ph620_05', 6)
    sprite('ph620_06', 5)
    sprite('ph620_07', 5)
    sprite('ph620_08', 8)
    DemoTimer(90)
    label(0)
    sprite('ph620_09', 8)
    sprite('ph620_10', 8)
    sprite('ph620_11', 8)
    gotoLabel(0)


@State
def EventDefEntryWait():
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
def EventWarpIn():
    SetZVal(-500)
    BlendMode_Normal()
    ScreenCollision(0)
    sprite('ph216_00', 6)
    AlphaValue(0)
    sprite('ph216_01', 6)
    CreateParticle('haef_event_lose', 103)
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(10)
    sprite('ph216_02', 6)
    sprite('ph216_03', 6)
    sprite('ph216_04', 6)
    sprite('ph216_05', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    sprite('ph216_06', 6)
    enterState('CmnActStand')


@State
def EventNoDisp():
    sprite('null', 32767)
    Visibility(1)


@State
def EventReaction():
    sprite('ph001_00', 7)
    sprite('ph001_01', 7)
    sprite('ph001_02', 7)
    CreateObject('ph001Eff', -1)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    sprite('ph001_02', 7)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_02', 7)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_01', 7)
    sprite('ph001_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventReactionLoop():
    sprite('ph001_00', 7)
    sprite('ph001_01', 7)
    sprite('ph001_02', 7)
    CreateObject('ph001Eff', -1)
    label(0)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_02', 7)
    loopRest()
    gotoLabel(0)


@State
def EventReactionLoopEnd():
    sprite('ph001_01', 7)
    sprite('ph001_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefChouhatsu():
    sprite('ph300_00', 6)
    sprite('ph300_01', 6)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_02', 5)
    sprite('ph300_03', 5)
    sprite('ph300_04', 5)
    sprite('ph300_05', 5)
    sprite('ph300_06', 5)
    sprite('ph300_07', 5)
    sprite('ph300_01', 4)
    sprite('ph300_00', 4)
    enterState('CmnActStand')


@State
def EventDefChouhatsu2():
    sprite('ph331_10', 6)
    sprite('ph331_09', 6)
    sprite('ph331_08', 8)
    sprite('ph331_07', 8)
    sprite('ph331_06', 8)
    sprite('ph331_08', 8)
    sprite('ph331_07', 8)
    sprite('ph331_06', 8)
    sprite('ph331_08', 8)
    sprite('ph331_07', 8)
    sprite('ph331_06', 8)
    sprite('ph331_09', 6)
    sprite('ph331_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefChouhatsu2Loop():
    sprite('ph331_10', 6)
    sprite('ph331_09', 6)
    label(0)
    sprite('ph331_08', 8)
    sprite('ph331_07', 8)
    sprite('ph331_06', 8)
    loopRest()
    gotoLabel(0)


@State
def EventDefChouhatsu2LoopEnd():
    sprite('ph331_09', 6)
    sprite('ph331_10', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventStand2():
    sprite('ph450_00', 6)
    sprite('ph450_01', 6)
    label(0)
    sprite('ph450_02', 6)
    sprite('ph450_03', 6)
    sprite('ph450_04', 6)
    loopRest()
    gotoLabel(0)


@State
def EventStand2End():
    sprite('ph450_01', 6)
    sprite('ph450_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventAction5B():
    sprite('ph201_00', 8)
    sprite('ph201_01', 8)
    sprite('ph201_02', 8)
    sprite('ph201_03', 8)
    sprite('ph201_04', 8)
    sprite('ph201_05', 8)
    sprite('ph201_06', 8)
    sprite('ph201_07', 8)
    sprite('ph201_08', 8)
    sprite('ph201_09', 8)
    loopRest()
    enterState('CmnActStand')


@State
def EventAction6B():
    sprite('ph211_00', 6)
    sprite('ph211_01', 6)
    sprite('ph211_02', 6)
    sprite('ph211_03', 6)
    sprite('ph211_04', 6)
    sprite('ph211_05', 6)
    sprite('ph211_06', 6)
    sprite('ph211_07', 6)
    sprite('ph211_08', 6)
    sprite('ph211_09', 6)
    sprite('ph211_10', 6)
    sprite('ph211_11', 6)
    sprite('ph211_12', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventAction4A():
    sprite('ph214_00', 8)
    sprite('ph214_01', 8)
    sprite('ph214_02', 8)
    sprite('ph214_03', 8)
    sprite('ph214_04', 8)
    sprite('ph214_05', 8)
    loopRest()
    enterState('CmnActStand')


@State
def EventWinLoop():
    label(0)
    sprite('ph615_06', 6)
    sprite('ph615_07', 6)
    sprite('ph615_08', 6)
    sprite('ph615_09', 6)
    sprite('ph615_10', 6)
    loopRest()
    gotoLabel(0)


@State
def EventWinLoopEnd():
    sprite('ph615_05', 6)
    sprite('ph615_04', 6)
    sprite('ph615_03', 6)
    sprite('ph615_02', 6)
    sprite('ph615_01', 6)
    sprite('ph615_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDriveLoop():
    sprite('ph203_00', 6)
    sprite('ph203_04', 4)
    sprite('ph203_05', 4)
    sprite('ph203_06', 4)
    sprite('ph203_07', 4)
    loopRest()
    label(0)
    sprite('ph203_08', 6)
    sprite('ph203_09', 6)
    sprite('ph203_10', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDriveLoopEnd():
    sprite('ph203_08', 6)
    sprite('ph203_11', 6)
    sprite('ph203_12', 6)
    sprite('ph203_13', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsTM01():
    sprite('ph600_18', 6)
    CreateObject('phef_600_Fire', -1)
    CreateObject('EventBGBlack', -1)
    label(0)
    sprite('ph600_15', 6)
    ScreenShake(5000, 2000)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    CreateParticle('phef_340mant2', 0)
    CreateParticle('phef_340mant2', 1)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    ScreenShake(5000, 2000)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    gotoLabel(0)


@State
def EventVsTM02():
    RunLoopUpon(17, 300)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('ph600_16', 6)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    ScreenShake(5000, 4000)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    ScreenShake(5000, 5000)
    ColorTransition(4282318848, 30)
    CreateObject('phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph600_16', 6)
    CreateObject('phef_600_FireWall', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        XPositionRelativeFacing(0)
        SetZVal(-500)
    CreateObject('phef_600_FireWall', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        XPositionRelativeFacing(-80000)
        SetZVal(-500)
    CreateObject('phef_600_FireWall', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        XPositionRelativeFacing(80000)
        SetZVal(-500)
    sprite('ph333_00', 4)
    ColorTransition(4294967295, 20)
    sprite('ph333_01', 4)
    sprite('ph333_02', 4)
    ScreenShake(6000, 6000)
    sprite('ph333_03', 4)
    sprite('ph333_04', 4)
    sprite('ph333_05', 4)
    ScreenShake(6000, 6000)
    sprite('ph333_06', 4)
    sprite('ph333_07', 4)
    sprite('ph333_05', 6)
    ScreenShake(7000, 6000)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    ScreenShake(7000, 6000)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    ScreenShake(8000, 6000)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    ScreenShake(8000, 6000)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    ScreenShake(9000, 6000)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    ScreenShake(9000, 6000)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_08', 6)
    TriggerUponForState('EventBGBlack', 32)
    sprite('ph333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventVsTMEnd():
    sprite('ph333_08', 6)
    sprite('ph333_09', 6)
    TriggerUponForState('EventBGBlack', 32)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():
    sprite('null', 32767)
    Visibility(1)


@State
def Act2Event_WarpIn():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('null', 4)
    CommonSE('000_airdash_0')
    sprite('null', 14)
    sprite('ph032_02', 4)
    Visibility(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Stand():
    label(0)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Udekumi():
    sprite('ph611_00', 6)
    sprite('ph611_01', 6)
    sprite('ph611_02', 32767)
    loopRest()


@State
def Act2Event_UdekumiEnd():
    sprite('ph611_02', 6)
    sprite('ph611_01', 6)
    sprite('ph611_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_phvskk_00():
    sprite('ph202_00', 6)
    ObjectUpon(22, 32)
    sprite('ph202_01', 5)
    sprite('ph202_02', 4)
    sprite('ph202_03', 19)
    CreateObject('ph202_eff', -1)
    PrivateSE('phse_02')
    sprite('ph202_04', 6)
    sprite('ph202_05', 5)
    sprite('ph202_06', 5)
    sprite('ph202_07', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_phvsrg_00():
    SLOT_51 = 3
    label(0)
    Unknown61(0, 2, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0)
    SLOT_2 = SLOT_0

    def upon_EVERY_FRAME():
        if not SLOT_2:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(2)
    label(1)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    AddActionMark(-1)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    AddActionMark(-1)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ph402_00', 3)
    SLOT_51 = SLOT_51 - 1
    sprite('ph402_01', 3)
    sprite('ph402_02', 3)
    sprite('ph402_03', 3)
    sprite('ph402_04', 3)
    CreateObject('Event_MidAssault_Atk', -1)
    sprite('ph402_02', 3)
    sprite('ph402_03', 3)
    sprite('ph402_05', 3)
    CommonSE('004_swing_grap_1_1')
    sprite('ph402_06', 2)
    sprite('ph402_07', 2)
    CreateObject('Eff_402Fire_PL', -1)
    sprite('ph402_08', 5)
    ObjectUpon(22, 32)
    sprite('ph402_09', 5)
    ScreenShake(5000, 20000)
    sprite('ph402_10', 5)
    sprite('ph402_11', 4)
    sprite('ph402_12', 4)
    sprite('ph204_12', 4)
    sprite('ph212_11', 4)
    sprite('ph212_12', 4)
    loopRest()
    if SLOT_51:
        gotoLabel(0)
    else:
        enterState('CmnActStand')


@State
def Act2Event_phvsrg_01():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_29 < 280000:
                ObjectUpon(22, 33)
                clearUponHandler(EVERY_FRAME)
                EndMomentum(1)
                sendToLabel(1)
    sprite('ph030_00', 8)
    physicsXImpulse(3000)
    label(0)
    sprite('ph030_01', 8)
    sprite('ph030_02', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 8)
    sprite('ph030_04', 8)
    sprite('ph030_05', 8)
    sprite('ph030_06', 8)
    sprite('ph030_07', 8)
    sprite('ph030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 8)
    sprite('ph030_10', 8)
    sprite('ph030_11', 8)
    sprite('ph030_12', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph610_00', 5)
    sprite('ph610_01', 6)
    sprite('ph610_02', 7)
    sprite('ph610_03', 4)
    sprite('ph610_04', 12)
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    label(2)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    loopRest()
    gotoLabel(2)


@State
def Act2Event_Doya():
    sprite('ph432_14', 6)
    sprite('ph432_13', 6)
    sprite('ph432_12', 6)
    label(0)
    sprite('ph432_09', 6)
    sprite('ph432_10', 6)
    sprite('ph432_11', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_DoyaEnd():
    sprite('keep', 2)
    sprite('ph432_12', 6)
    sprite('ph432_13', 6)
    sprite('ph432_14', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_OverDrive():
    sprite('ph333_00', 6)
    sprite('ph333_01', 6)
    sprite('ph333_02', 6)
    sprite('ph333_03', 30)
    SetActionMark(6)
    label(0)
    sprite('ph333_03', 10)
    AddActionMark(-1)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    label(1)
    sprite('ph333_03', 5)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(1)


@State
def Act2Event_OverDriveEnd():
    sprite('keep', 10)
    sprite('ph333_04', 4)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(100000, 100000)
    CreateObject('Event_phef_600_Fire', -1)
    CreateObject('Event_phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    CreateObject('Event_phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph333_07', 5)
    CreateObject('Event_phef_600_FireWall', -1)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    ColorTransition(4294967295, 20)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_08', 6)
    sprite('ph333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoin():
    sprite('ph205_05', 10)
    sprite('ph205_06', 4)
    CreateObject('Event_DriveAtk_RRR', -1)
    LandingEffects(100, 1, 0)
    sprite('ph205_07', 4)
    sprite('ph205_08', 4)
    sprite('ph205_09', 4)
    sprite('ph205_07', 4)
    sprite('ph205_08', 4)
    sprite('ph205_09', 4)
    sprite('ph205_07', 4)
    sprite('ph205_08', 4)
    sprite('ph205_09', 4)
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_12', 5)
    sprite('ph205_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoin2():
    sprite('ph311_08', 3)
    sprite('ph311_09', 16)
    sprite('ph311_10', 5)
    sprite('ph311_11', 5)
    sprite('ph311_12', 5)
    sprite('ph311_13', 5)
    sprite('ph311_14', 5)
    sprite('ph311_15', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_FaceHide():
    sprite('ph333_00', 7)
    sprite('ph333_01', 7)
    sprite('ph333_02', 7)
    sprite('ph333_03', 32767)
    loopRest()


@State
def Act2Event_FaceHideEnd():
    sprite('ph333_02', 7)
    sprite('ph333_01', 7)
    sprite('ph333_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_EntryReverse():
    sprite('ph600_18', 6)
    label(0)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvsph_00():
    sprite('ph040_00', 3)
    ObjectUpon(22, 32)
    sprite('ph040_01', 3)
    label(0)
    sprite('ph040_02', 3)
    sprite('ph040_03', 3)
    sprite('ph040_04', 3)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvsph_01():
    sprite('keep', 1)
    ObjectUpon(22, 33)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsph_02():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('ph030_00', 8)
    physicsXImpulse(3000)
    label(0)
    sprite('ph030_01', 8)
    sprite('ph030_02', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 8)
    sprite('ph030_04', 8)
    sprite('ph030_05', 8)
    sprite('ph030_06', 8)
    sprite('ph030_07', 8)
    sprite('ph030_08', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 8)
    sprite('ph030_10', 8)
    sprite('ph030_11', 8)
    sprite('ph030_12', 8)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act3Event_amvsph_00():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph032_02', 4)
    CommonSE('000_airdash_0')
    ConstantAlphaModifier(-12)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    sprite('null', 32767)
    AlphaValue(0)
    Visibility(1)


@State
def Act3Event_amvsph_01():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    label(0)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph032_02', 4)
    CommonSE('000_airdash_0')
    ConstantAlphaModifier(-12)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    Visibility(1)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    sprite('null', 20)
    sprite('null', 4)
    CommonSE('000_airdash_0')
    Flip()
    sprite('null', 14)
    sprite('ph600_18', 6)
    Visibility(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    CreateObject('Event_ph032FireEff2', -1)
    label(2)
    sprite('ph600_15', 7)
    sprite('ph600_16', 7)
    sprite('ph600_17', 7)
    loopRest()
    gotoLabel(2)


@State
def Act3Event_amvsph_02():
    sprite('ph600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevsph_00():
    sprite('keep', 1)
    Flip()
    label(0)
    sprite('ph000_00', 7)
    sprite('ph000_01', 7)
    sprite('ph000_02', 7)
    sprite('ph000_03', 7)
    sprite('ph000_04', 7)
    sprite('ph000_05', 7)
    sprite('ph000_06', 7)
    sprite('ph000_07', 7)
    sprite('ph000_08', 7)
    sprite('ph000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_cevsph_01():
    sprite('ph003_00', 6)
    Flip()
    sprite('ph003_01', 6)
    sprite('ph003_00ex01', 3)
    sprite('ph000_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_cevsph_02():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph032_02', 4)
    CommonSE('000_airdash_0')
    ConstantAlphaModifier(-12)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    sprite('null', 20)
    AlphaValue(0)
    sprite('ph032_02', 4)
    CommonSE('000_airdash_0')
    Visibility(0)
    AlphaValue(0)
    XPositionRelativeFacing(100000)
    ConstantAlphaModifier(8)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsno_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        AlphaValue(0)
        uponSendToLabel(32, 1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    label(0)
    sprite('ph602_00', 32767)
    loopRest()
    label(1)
    sprite('ph333_00', 6)
    clearUponHandler(32)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph333_01', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph333_02', 6)
    sprite('ph333_03', 6)
    ConstantAlphaModifier(5)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    ScreenShake(0, 20000)
    sprite('ph333_04', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    ColorTransition(4291310130, 18)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph333_08', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph333_09', 7)
    EnableAfterimage(0)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsno_01():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            EndMomentum(1)
            XPositionRelativeFacing(-260000)

    def upon_EVERY_FRAME():
        if SLOT_IsFacingRight:
            if SLOT_XDistanceFromCenterOfStage > 260000:
                SetActionMark(0)
                sendToLabel(1)
        elif SLOT_XDistanceFromCenterOfStage < -260000:
            sendToLabel(1)
    sprite('ph031_00', 7)
    physicsXImpulse(-2000)
    label(0)
    sprite('ph031_01', 7)
    sprite('ph031_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_03', 7)
    sprite('ph031_04', 7)
    sprite('ph031_05', 7)
    sprite('ph031_06', 7)
    sprite('ph031_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_08', 7)
    sprite('ph031_09', 7)
    sprite('ph031_10', 7)
    sprite('ph031_11', 7)
    sprite('ph031_12', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph003_00', 6)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    sprite('ph003_01', 6)
    sprite('ph003_00ex01', 3)
    sprite('ph000_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsno_02():
    sprite('ph001_00', 7)
    sprite('ph001_01', 7)
    sprite('ph001_02', 7)
    CreateObject('ph001Eff', -1)
    label(0)
    sprite('ph001_03', 7)
    sprite('ph001_04', 7)
    sprite('ph001_05', 7)
    sprite('ph001_06', 7)
    sprite('ph001_02ex01', 7)
    sprite('ph001_03ex01', 7)
    sprite('ph001_04ex01', 7)
    sprite('ph001_05ex01', 7)
    sprite('ph001_06ex01', 7)
    sprite('ph001_02', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsno_03():
    sprite('ph001_01', 7)
    sprite('ph001_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsno_04():
    sprite('ph203_00', 7)
    label(0)
    sprite('ph203_01', 7)
    sprite('ph203_02', 7)
    sprite('ph203_03', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsno_05():
    sprite('ph203_04', 6)
    sprite('ph203_05', 6)
    CommonSE('019_cloth_c')
    sprite('ph203_06', 6)
    sprite('ph203_07', 6)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    label(0)
    sprite('ph203_08', 6)
    sprite('ph203_09', 6)
    sprite('ph203_10', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsno_06():
    sprite('ph203_11', 6)
    sprite('ph203_12', 6)
    sprite('ph203_13', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsno_07():
    EndAttack()
    SetZVal(-500)
    AddX(285000)
    sprite('ph610_04', 12)
    ScreenShake(0, 20000)
    CommonSE('100_hit_grap_2')
    sprite('ph610_05', 5)
    sprite('ph610_06', 5)
    sprite('ph610_07', 5)
    sprite('ph610_08', 5)
    sprite('ph610_09', 5)
    label(2)
    sprite('ph610_10', 6)
    sprite('ph610_11', 6)
    sprite('ph610_12', 6)
    sprite('ph610_13', 6)
    loopRest()
    gotoLabel(2)


@State
def Act3Event_phvsno_08():

    def upon_IMMEDIATE():
        SetZVal(500)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageInterval(12)
        AfterimageCount(6)

        def upon_STATE_END():
            EndMomentum(1)
            clearUponHandler(EVERY_FRAME)
            EnableAfterimage(0)
    sprite('ph032_00', 6)
    CommonSE('019_cloth_c')
    physicsXImpulse(-4000)
    physicsYImpulse(3000)
    sprite('ph032_01', 6)
    CommonSE('001_airbackdash_0')
    sprite('ph032_02', 6)
    sprite('ph032_03', 6)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('ph032_04', 6)
    sprite('ph032_02', 6)
    XImpulseAcceleration(20)
    YAccel(20)
    sprite('ph032_03', 6)
    sprite('ph032_04', 6)
    XImpulseAcceleration(15)
    YAccel(15)
    sprite('ph032_02', 6)
    XImpulseAcceleration(10)
    YAccel(10)
    sprite('ph032_03', 6)
    ObjectUpon(22, 32)
    EndMomentum(1)
    sprite('ph032_04', 6)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 60:
            if SLOT_52 % 2:
                physicsYImpulse(200)
            else:
                physicsYImpulse(-200)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1
    label(0)
    sprite('ph032_02', 6)
    sprite('ph032_03', 6)
    sprite('ph032_04', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsno_09():

    def upon_IMMEDIATE():
        setGravity(0)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('ph032_02', 4)
    CreateObject('ph032FireEff', -1)
    CommonSE('000_airdash_0')
    ConstantAlphaModifier(-12)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    sprite('null', 32767)
    AlphaValue(0)
    Visibility(1)


@State
def Act3Event_phvsca_00():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        AddY(1650000)
        AddX(-6800000)
        CameraNoScreenCollision(1)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_phvsca_01():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        AddY(1550000)
        AddX(-600000)
        CameraNoScreenCollision(1)
        EnableAfterimage(1)
        AfterimageInterval(12)
        AfterimageCount(6)

        def upon_STATE_END():
            EndMomentum(1)
            clearUponHandler(EVERY_FRAME)
            EnableAfterimage(0)
    sprite('ph340_00', 7)
    CameraControlEnable(1)
    sprite('ph340_01', 7)
    sprite('ph340_02', 7)
    sprite('ph340_03', 7)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        if SLOT_51 == 60:
            if SLOT_52 % 2:
                physicsYImpulse(200)
            else:
                physicsYImpulse(-200)
            SLOT_51 = 0
            SLOT_52 = SLOT_52 + 1
    label(0)
    sprite('ph340_01', 7)
    sprite('ph340_02', 7)
    sprite('ph340_03', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsca_02():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        ScreenCollision(0)
        WallCollisionDetection(0)
        CameraNoScreenCollision(1)
        EnableAfterimage(1)
        AfterimageInterval(12)
        AfterimageCount(6)

        def upon_STATE_END():
            EnableAfterimage(0)
            WallCollisionDetection(1)
            ScreenCollision(1)
            CameraNoScreenCollision(0)
    sprite('ph340_01', 7)
    sprite('ph340_00', 7)
    sprite('ph205_00', 6)
    CameraPosition(1800)
    sprite('ph205_01', 6)
    CreateParticle('phef_rrn_mc', 103)
    CommonSE('022_magiccircle_c')
    sprite('ph205_02', 4)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    CreateObject('Act3Event_phEff_RRB', -1)
    RegisterObject(9, 1)

    def RunOnObject_9():
        AddX(400000)
        AddY(600000)
        Size(2500)
        RotationAngle(-45000)
    sprite('ph205_02', 4)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    CreateObject('Act3Event_phEff_RRB', -1)
    RegisterObject(10, 1)

    def RunOnObject_10():
        AddX(600000)
        AddY(-300000)
        Size(2000)
        RotationAngle(-45000)
    sprite('ph205_02', 4)
    ObjectUpon(9, 33)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    CreateObject('Act3Event_phEff_RRB', -1)
    RegisterObject(11, 1)

    def RunOnObject_11():
        AddX(-400000)
        AddY(-100000)
        Size(3000)
        RotationAngle(-45000)
    sprite('ph205_02', 4)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    sprite('ph205_02', 4)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    sprite('ph205_02', 4)
    sprite('ph205_03', 4)
    sprite('ph205_04', 4)
    sprite('ph205_05', 6)
    sprite('ph205_06', 6)
    sprite('ph205_07', 5)
    sprite('ph205_08', 5)
    sprite('ph205_09', 5)
    loopRest()
    sprite('ph205_07', 5)
    ObjectUpon(9, 32)
    PrivateSE('phse_10')
    sprite('ph205_08', 5)
    sprite('ph205_09', 5)
    ObjectUpon(OPPONENT_HIT_OR_BLOCK, 32)
    sprite('ph205_07', 5)
    CameraControlEnable(0)
    sprite('ph205_08', 5)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    sprite('ph205_09', 5)
    loopRest()
    sprite('ph205_07', 5)
    sprite('ph205_08', 5)
    sprite('ph205_09', 5)
    loopRest()
    sprite('ph205_07', 5)
    sprite('ph205_08', 5)
    sprite('ph205_09', 5)
    loopRest()
    sprite('ph205_07', 5)
    sprite('ph205_08', 5)
    sprite('ph205_09', 5)
    loopRest()
    sprite('ph205_10', 5)
    sprite('ph205_11', 5)
    sprite('ph205_15', 5)
    sprite('ph205_16', 32767)
    loopRest()


@State
def Act3Event_phvsca_03():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('null', 4)
    XPositionRelativeFacing(-260000)
    AbsoluteY(0)
    CommonSE('000_airdash_0')
    sprite('null', 14)
    sprite('ph032_02', 4)
    Visibility(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    CreateObject('Event_ph032FireEff2', -1)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_02', 4)
    sprite('ph032_03', 4)
    sprite('ph032_04', 4)
    sprite('ph032_05', 5)
    sprite('ph032_06', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsca_04():
    sprite('ph600_18', 6)
    CameraControlEnable(1)
    sprite('ph600_17', 6)
    CommonSE('200_walk_normal_0')
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    CreateObject('phef_600_HatFire', -1)
    CommonSE('015_blaze_0')
    sprite('ph600_14', 6)
    sprite('ph600_13', 6)
    sprite('ph600_12', 250)
    sprite('ph600_11', 7)
    sprite('ph600_10', 7)
    sprite('ph600_09', 32767)
    CommonSE('200_walk_normal_0')
    loopRest()


@State
def Act3Event_phvsjn_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)

        def upon_STATE_END():
            AlphaValue(255)
            ConstantAlphaModifier(0)
    label(1)
    sprite('ph333_00', 6)
    AddX(-260000)
    CreateParticle('phef_602hinoko', 100)
    sprite('ph333_01', 6)
    CreateObject('phef_600_bg', -1)
    CreateObject('phef_602_Fire', -1)
    sprite('ph333_02', 6)
    sprite('ph333_03', 6)
    ConstantAlphaModifier(5)
    CreateObject('phef_602_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph333_04', 6)
    CreateObject('phef_602_FireWall', -1)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    ColorTransition(4291310130, 18)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    sprite('ph333_05', 6)
    sprite('ph333_06', 6)
    sprite('ph333_07', 6)
    EnableAfterimage(1)
    AfterimageInterval(2)
    AfterimageCount(4)
    sprite('ph333_08', 7)
    ColorTransition(4294967295, 24)
    CreateParticle('phef_602add', 100)
    sprite('ph333_09', 7)
    LandingEffects(100, 1, 1)
    EnableAfterimage(0)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsjn_01():

    def upon_IMMEDIATE():
        EnableCollision(0)
        ScreenCollision(0)
    sprite('ph003_00', 6)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    sprite('ph003_01', 6)
    sprite('ph003_00ex01', 3)
    Flip()
    sprite('ph000_00', 6)
    physicsXImpulse(2000)
    SetActionMark(4)
    label(0)
    sprite('ph030_01', 7)
    AddActionMark(-1)
    sprite('ph030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 7)
    sprite('ph030_04', 7)
    sprite('ph030_05', 7)
    sprite('ph030_06', 7)
    sprite('ph030_07', 7)
    sprite('ph030_08', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 7)
    sprite('ph030_10', 7)
    sprite('ph030_11', 7)
    sprite('ph030_12', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_phvsjn_02():
    sprite('ph214_00', 8)
    sprite('ph214_01', 8)
    sprite('ph214_02', 8)
    sprite('ph214_03', 8)
    sprite('ph214_04', 8)
    sprite('ph214_05', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsjn_03():
    sprite('ph210_00', 6)
    sprite('ph210_01', 6)
    sprite('ph210_02', 6)
    sprite('ph210_03', 6)
    sprite('ph210_04', 7)
    sprite('ph210_05', 7)
    CommonSE('019_cloth_c')
    sprite('ph210_06', 30)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph210_06', 7)
    sprite('ph210_07', 7)
    sprite('ph210_08', 7)
    sprite('ph210_09', 7)
    sprite('ph210_10', 7)
    sprite('ph210_11', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsjn_04():
    sprite('ph211_00', 6)
    sprite('ph211_01', 6)
    sprite('ph211_02', 6)
    sprite('ph211_03', 6)
    sprite('ph211_04', 6)
    CommonSE('019_cloth_c')
    sprite('ph211_05', 6)
    CreateParticle('phef_611fire', 0)
    CreateParticle('phef_611fire', 1)
    sprite('ph211_06', 6)
    sprite('ph211_07', 6)
    sprite('ph211_08', 6)
    sprite('ph211_09', 6)
    sprite('ph211_10', 6)
    sprite('ph211_11', 6)
    sprite('ph211_12', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_phvsrl_00():
    sprite('ph600_18', 6)
    sprite('ph600_17', 6)
    CommonSE('200_walk_normal_0')
    SetActionMark(5)
    label(0)
    sprite('ph600_15', 6)
    AddActionMark(-1)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_phvsrl_02():
    sprite('ph600_18', 6)
    loopRest()
    sprite('ph333_00', 8)
    CommonSE('200_walk_normal_0')
    sprite('ph333_01', 8)
    sprite('ph333_02', 8)
    SetActionMark(6)
    label(0)
    sprite('ph333_03', 10)
    AddActionMark(-1)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    label(1)
    sprite('ph333_03', 5)
    ScreenShake(0, 6000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(1)


@State
def Act3Event_suvsph_00():
    sprite('null', 32767)
    CommonSE('400_menu_cursor_a')
    loopRest()


@State
def Act3Event_suvsph_01():
    sprite('null', 32767)
    CommonSE('400_menu_ok')
    loopRest()


@State
def Act3Event_suvsph_02():

    def upon_IMMEDIATE():
        AlphaValue(0)

        def upon_STATE_END():
            AlphaValue(255)
    sprite('ph600_18', 5)
    CreateParticle('story_teni', 103)
    CommonSE('000_airdash_2')
    CommonSE('022_magiccircle_b')
    ConstantAlphaModifier(4)
    sprite('ph600_17', 5)
    sprite('ph600_15', 5)
    sprite('ph600_16', 5)
    sprite('ph600_17', 5)
    sprite('ph600_15', 5)
    sprite('ph600_16', 5)
    sprite('ph600_17', 5)
    sprite('ph600_15', 5)
    sprite('ph600_16', 5)
    sprite('ph600_17', 5)
    sprite('ph600_15', 5)
    sprite('ph600_16', 5)
    sprite('ph600_17', 5)
    CreateParticle('haef_event_lose_end', 103)
    label(0)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_suvsph_03():
    sprite('ph600_17', 6)
    sprite('ph600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_suvsph_04():
    sprite('ph214_00', 8)
    sprite('ph214_01', 8)
    ObjectUpon(22, 32)
    sprite('ph214_02', 8)
    sprite('ph214_03', 8)
    sprite('ph214_04', 8)
    sprite('ph214_05', 8)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_suvsph_05():
    sprite('ph600_16', 6)
    CommonSE('022_magiccircle_b')
    sprite('ph600_17', 6)
    ConstantAlphaModifier(-4)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_jbvsph_00():
    label(0)
    sprite('ph600_15', 6)
    sprite('ph600_16', 6)
    sprite('ph600_17', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_jbvsph_01():
    sprite('ph620_01', 6)
    sprite('ph620_02', 6)
    sprite('ph620_03', 6)
    sprite('ph620_04', 7)
    sprite('ph620_05', 7)
    sprite('ph620_06', 7)
    sprite('ph620_07', 7)
    sprite('ph620_08', 8)
    DemoTimer(90)
    label(0)
    sprite('ph620_09', 8)
    sprite('ph620_10', 8)
    sprite('ph620_11', 8)
    gotoLabel(0)


@State
def Act3Event_jbvsph_02():
    sprite('ph620_05', 7)
    sprite('ph620_04', 7)
    sprite('ph620_03', 7)
    sprite('ph620_02', 7)
    sprite('ph620_01', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsph_03():
    sprite('ph333_00', 6)
    sprite('ph333_01', 6)
    sprite('ph333_02', 6)
    sprite('ph333_03', 30)
    SetActionMark(24)
    label(0)
    sprite('ph333_03', 10)
    AddActionMark(-1)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('ph333_04', 4)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(5000, 100000)
    CreateObject('Event_phef_600_Fire', -1)
    CreateObject('Event_phef_600_bg', -1)
    ColorTransition(4282318848, 30)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    CreateObject('Event_phef_600_Fire2', -1)
    PrivateSE('phse_02')
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('ph333_07', 5)
    CreateObject('Event_phef_600_FireWall', -1)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    ColorTransition(4294967295, 20)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_05', 5)
    sprite('ph333_06', 5)
    sprite('ph333_07', 5)
    sprite('ph333_08', 6)
    sprite('ph333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jbvsph_04():
    sprite('ph600_18', 7)
    loopRest()
    enterState('CmnActStand')
