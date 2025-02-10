@State
def dmy():
    sprite('vrdmy', 120)


@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_RC.DIG', 'ef_emb_RC_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 80)


@State
def EMB_RC_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_RC.DIG', 'ef_emb_RC_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 80)


@State
def EMB_RC_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_RC.DIG', 'ef_emb_RC_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Normal()
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 80)


@State
def Gi():

    def upon_IMMEDIATE():
        CallObject('GiControl')
        TeleportToObject(3)
        AddX(-120000)
        AddY(360000)
        IgnorePauses(3)
    sprite('vrgi000_00', 100)
    enterState('GiNeutral')


@State
def GiNeutral():
    label(0)
    sprite('vrgi000_00', 2)
    FlagDelActionMark(1)
    sprite('vrgi000_01', 2)
    sprite('vrgi000_02', 2)
    sprite('vrgi000_03', 2)
    sprite('vrgi000_04', 2)
    sprite('vrgi000_05', 2)
    sprite('vrgi000_06', 2)
    sprite('vrgi000_07', 2)
    sprite('vrgi000_08', 2)
    sprite('vrgi000_09', 2)
    sprite('vrgi000_00', 3)
    FlagAddActionMark(1)
    sprite('vrgi000_01', 3)
    sprite('vrgi000_02', 3)
    sprite('vrgi000_03', 3)
    sprite('vrgi000_04', 3)
    sprite('vrgi000_05', 3)
    sprite('vrgi000_06', 3)
    sprite('vrgi000_07', 3)
    sprite('vrgi000_08', 3)
    sprite('vrgi000_09', 3)
    loopRest()
    gotoLabel(0)


@State
def GiPlayerDamage():
    sprite('vrgi060_00', 3)
    sprite('vrgi060_01', 3)
    label(0)
    sprite('vrgi060_02', 3)
    sprite('vrgi060_03', 3)
    sprite('vrgi060_04', 3)
    sprite('vrgi060_05', 3)
    sprite('vrgi060_06', 3)
    sprite('vrgi060_04', 3)
    sprite('vrgi060_03', 3)
    loopRest()
    gotoLabel(0)


@State
def GiTurn():
    sprite('vrgi000_10', 2)
    sprite('vrgi000_10', 2)
    Flip()
    sprite('vrgi000_10', 1)
    sprite('keep', 100)
    enterState('GiNeutral')


@State
def GiDash():
    sprite('vrgi030_00', 3)
    label(0)
    sprite('vrgi030_01', 3)
    sprite('vrgi030_02', 3)
    sprite('vrgi030_03', 3)
    loopRest()
    gotoLabel(0)


@State
def GiDashDown():
    sprite('vrgi032_00', 3)
    label(0)
    sprite('vrgi032_01', 3)
    sprite('vrgi032_02', 3)
    sprite('vrgi032_03', 3)
    loopRest()
    gotoLabel(0)


@State
def GiDashUp():
    sprite('vrgi033_00', 3)
    label(0)
    sprite('vrgi033_01', 3)
    sprite('vrgi033_02', 3)
    sprite('vrgi033_03', 3)
    loopRest()
    gotoLabel(0)


@State
def gi_GirdBreak():

    def upon_IMMEDIATE():
        SetZVal(-500)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('vrgi090_02', 4)
    sprite('vrgi090_03', 3)
    sprite('vrgi090_04', 3)
    ConstantAlphaModifier(-20)


@State
def GiStorm():

    def upon_IMMEDIATE():

        def upon_33():
            sendToLabel(0)

        def upon_34():
            sendToLabel(1)

        def upon_35():
            sendToLabel(99)
        E0EAEffectDirection(3)

        def upon_STATE_END():
            E0EAEffectDirection(0)
    sprite('vrgi060_00', 3)
    sprite('vrgi060_01', 5)
    sprite('vrgi060_02', 3)
    sprite('vrgi432_00', 4)
    sprite('vrgi432_01', 4)
    sprite('vrgi432_01ex01', 5)
    sprite('vrgi432_02', 5)
    sprite('vrgi432_03', 5)
    label(0)
    sprite('vrgi432_04', 10)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrgi432_05', 4)
    sprite('vrgi432_06', 4)
    sprite('vrgi432_07', 4)
    loopRest()
    label(2)
    sprite('vrgi432_08', 2)
    sprite('vrgi432_09', 2)
    sprite('vrgi432_10', 2)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('vrgi432_11', 4)
    sprite('vrgi432_12', 4)
    sprite('vrgi432_13', 4)
    sprite('vrgi432_14', 4)
    enterState('GiNeutral')


@State
def GiHide():
    label(0)
    sprite('null', 1)
    Visibility(1)
    loopRest()
    gotoLabel(0)


@State
def nago_medama():

    def upon_IMMEDIATE():
        SetZVal(-500)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('rc063_11n', 5)
    sprite('rc063_11nex00', 5)
    sprite('rc063_11nex01', 8)
    sprite('rc063_11nex02', 5)
    sprite('rc063_11nex03', 5)
    sprite('rc063_11nex04', 5)
    sprite('rc063_11nex05', 5)
    sprite('rc063_11nex06', 5)
    sprite('rc063_11nex07', 5)
    sprite('rc063_11nex08', 5)
    sprite('rc063_11nex09', 20)
    ConstantAlphaModifier(-20)


@Subroutine
def FlogDie():
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(LANDING)
    clearUponHandler(19)
    clearUponHandler(PLAYER_DAMAGED)
    SLOT_59 = 0
    SetActionMark(0)
    NoAttackDuringAction(1)
    NoDamageAction(1)
    sendToLabel(324)


@Subroutine
def FlogReset():
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ExternalForcesRate(0, 0)
    SLOT_52 = 0


@State
def Flog():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        NoAttackDuringAction(1)
        callSubroutine('FlogReset')
        AttackLevel_(3)
        PushbackX(5000)
        Hitstop(4)
        Damage(250)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        HitsparkSize(300)
        AirUntechableTime(35)
        AttackP1(80)
        SingleProration(1)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        Unknown12052(1)
        SetZVal(-500)
        PaletteIndex(1)
        SLOT_56 = 540
        SLOT_59 = 1

        def upon_33():
            physicsXImpulse(10000)
            physicsYImpulse(6000)
            setGravity(1300)

        def upon_34():
            physicsXImpulse(15000)
            physicsYImpulse(20000)
            setGravity(1300)
        WallCollisionDetection(1)
        MaxHP(750)
        CurrentHP(750)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        GuardpointHitstop(-2, -1)
        if SLOT_IsUnlimited:
            MaxHP(1600)
            CurrentHP(1600)
            EnableAfterimage(1)
            AfterimageBlendMode(2)
            AfterimageCount(5)
            AfterimageColor_1(100, 128, 128, 128)
            AfterimageColor_2(10, 100, 100, 100)
            AfterimageMask_1(0, 255, 255, 0)
            AfterimageMask_2(0, 255, 255, 0)
            AfterimageSize_1(1040)
            AfterimageSize_2(1300)

        def upon_19():
            if SLOT_59:
                callSubroutine('FlogDie')

        def upon_PLAYER_DAMAGED():
            if not SLOT_IsUnlimited:
                if SLOT_59:
                    callSubroutine('FlogDie')

        def upon_53():
            if SLOT_59:
                callSubroutine('FlogDie')

        def upon_45():
            if SLOT_53:
                SLOT_9 = 1

        def upon_EVERY_FRAME():
            if not SLOT_IsUnlimited:
                SLOT_56 = SLOT_56 + -1
                if SLOT_56 < 0:
                    if SLOT_59:
                        callSubroutine('FlogDie')
            if SLOT_IsUnlimited:
                if not SLOT_21:
                    if SLOT_59:
                        callSubroutine('FlogDie')
            if SLOT_2:
                if SLOT_29 < 280000:
                    SetActionMark(0)
                    sendToLabel(661)
            if SLOT_2:
                CallPrivateFunction('RC_FlogWindCheck', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_2:
                if SLOT_40 < 0:
                    if SLOT_IsFacingRight == 0:
                        SetActionMark(0)
                        sendToLabel(322)
                if SLOT_40 > 0:
                    if SLOT_IsFacingRight == 1:
                        SetActionMark(0)
                        sendToLabel(322)

        def upon_32():
            if SLOT_59:
                callSubroutine('FlogDie')

        def upon_STATE_END():
            SLOT_9 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_fgjp03', 3)
    PrivateSE('rcse_24')
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(100000)
    Size(500)
    SetScaleSpeed(50)

    def upon_LANDING():
        if SLOT_59:
            sendToLabel(50)
    sprite('vrrcef_fgjp04', 3)
    label(55)
    sprite('vrrcef_fgjp05', 4)
    Size(900)
    SetScaleSpeed(0)
    gotoLabel(55)
    loopRest()
    label(50)
    clearUponHandler(LANDING)
    uponSendToLabel(GUARDPOINT_ACTIVATION, 136)
    callSubroutine('FlogReset')
    AbsoluteY(0)
    sprite('vrrcef_fgjp06', 2)
    Size(1000)
    SetScaleSpeed(0)
    sprite('vrrcef_fgjp07', 2)
    sprite('vrrcef_fgjp02', 2)
    sprite('vrrcef_fgjp01', 2)
    sprite('vrrcef_fgjp00', 2)
    label(338)
    sprite('vrrcef_fggr00', 2)
    loopRest()
    label(132)
    callSubroutine('FlogReset')
    SetActionMark(1)
    physicsXImpulse(2000)
    sprite('vrrcef_fgwk00', 5)
    sprite('vrrcef_fgwk01', 5)
    PrivateSE('rcse_06')
    sprite('vrrcef_fgwk02', 5)
    sprite('vrrcef_fgwk03', 5)
    sprite('vrrcef_fgwk04', 5)
    sprite('vrrcef_fgwk05', 5)
    sprite('vrrcef_fgwk06', 5)
    sprite('vrrcef_fgwk07', 5)
    PrivateSE('rcse_06')
    sprite('vrrcef_fgwk08', 5)
    sprite('vrrcef_fgwk09', 5)
    sprite('vrrcef_fgwk10', 5)
    sprite('vrrcef_fgwk11', 5)
    sprite('vrrcef_fgwk01', 5)
    loopRest()
    label(133)
    sprite('vrrcef_fgwk02', 5)
    sprite('vrrcef_fgwk03', 5)
    sprite('vrrcef_fgwk04', 5)
    sprite('vrrcef_fgwk05', 5)
    sprite('vrrcef_fgwk06', 5)
    sprite('vrrcef_fgwk07', 5)
    PrivateSE('rcse_06')
    sprite('vrrcef_fgwk08', 5)
    sprite('vrrcef_fgwk09', 5)
    sprite('vrrcef_fgwk10', 5)
    sprite('vrrcef_fgwk11', 5)
    sprite('vrrcef_fgwk01', 5)
    loopRest()
    gotoLabel(133)
    label(134)
    sprite('vrrcef_fgsl00', 6)
    callSubroutine('FlogReset')
    SetActionMark(1)
    ExternalForcesRate(150, 0)
    SelfWind(150, 0, 0)
    SLOT_52 = 1
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgsl00', 6)
    sprite('vrrcef_fgjp06', 4)
    sprite('vrrcef_fgjp07', 4)
    loopRest()
    gotoLabel(132)
    label(135)
    sprite('vrrcef_fgwk00', 2)
    callSubroutine('FlogReset')
    SetActionMark(1)
    ExternalForcesRate(35, 0)
    SelfWind(35, 0, 0)
    SLOT_52 = 2
    sprite('vrrcef_fgwk01', 2)
    AddX(2000)
    sprite('vrrcef_fgwk02', 2)
    AddX(-2000)
    sprite('vrrcef_fgwk03', 2)
    AddX(2000)
    sprite('vrrcef_fgwk04', 2)
    AddX(-2000)
    sprite('vrrcef_fgwk05', 2)
    AddX(2000)
    sprite('vrrcef_fgwk06', 2)
    AddX(-2000)
    sprite('vrrcef_fgwk07', 2)
    AddX(2000)
    loopRest()
    gotoLabel(132)
    label(136)
    sprite('vrrcef_fgwk00', 3)
    callSubroutine('FlogReset')
    SetActionMark(1)
    ExternalForcesRate(35, 0)
    SelfWind(35, 0, 0)
    SLOT_52 = 2
    SetInertia(-16000)
    sprite('vrrcef_fgwk01', 3)
    AddX(2000)
    sprite('vrrcef_fgwk02', 3)
    AddX(-2000)
    sprite('vrrcef_fgwk03', 3)
    AddX(2000)
    sprite('vrrcef_fgwk04', 3)
    AddX(-2000)
    sprite('vrrcef_fgwk05', 3)
    AddX(2000)
    sprite('vrrcef_fgwk06', 3)
    AddX(-2000)
    sprite('vrrcef_fgwk07', 3)
    AddX(2000)
    SetInertia(0)
    loopRest()
    gotoLabel(132)
    label(251)
    callSubroutine('FlogReset')
    SetActionMark(1)
    physicsXImpulse(0)
    sprite('vrrcef_fgjp00', 4)
    sprite('vrrcef_fgjp01', 4)
    sprite('vrrcef_fgjp02', 3)
    SetActionMark(0)
    sprite('vrrcef_fgjp03', 3)
    PrivateSE('rcse_24')
    physicsXImpulse(12000)
    physicsYImpulse(13000)
    setGravity(1300)
    uponSendToLabel(LANDING, 100)
    sprite('vrrcef_fgjp04', 3)
    label(101)
    sprite('vrrcef_fgjp05', 3)
    loopRest()
    gotoLabel(101)
    label(100)
    callSubroutine('FlogReset')
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    sprite('vrrcef_fgjp06', 2)
    SetActionMark(1)
    PrivateSE('rcse_06')
    sprite('vrrcef_fgjp07', 3)
    sprite('vrrcef_fgjp02', 6)
    sprite('vrrcef_fgjp01', 6)
    sprite('vrrcef_fgjp00', 10)
    loopRest()
    gotoLabel(132)
    label(322)
    callSubroutine('FlogReset')
    sprite('vrrcef_fggr80', 6)
    Flip()
    SetActionMark(0)
    sprite('vrrcef_fggr00', 6)
    loopRest()
    gotoLabel(132)
    label(661)
    callSubroutine('FlogReset')
    SetActionMark(0)
    physicsXImpulse(0)
    NoAttackDuringAction(1)
    clearUponHandler(GUARDPOINT_ACTIVATION)
    sprite('vrrcef_fggr00', 2)
    SLOT_53 = 1
    PerExternalForces(80)
    SLOT_56 = 9999
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(2000)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr01', 2)
    PerExternalForces(80)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(-2000)
    sprite('vrrcef_fggr02', 2)
    PerExternalForces(80)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(2000)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr03', 2)
    PerExternalForces(80)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(-2000)
    sprite('vrrcef_fggr01', 2)
    PerExternalForces(80)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(2000)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr00', 2)
    PerExternalForces(0)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(-2000)
    sprite('vrrcef_fggr01', 2)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(2000)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr02', 2)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(-2000)
    sprite('vrrcef_fggr03', 2)
    CreateObject('StayThunder', 0)
    CreateObject('StayThunder', 0)
    AddX(2000)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr00', 2)
    NoAttackDuringAction(0)
    RefreshMultihit()
    CreateObject('LightningFrog', -1)
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr01', 2)
    RefreshMultihit()
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr02', 2)
    RefreshMultihit()
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr03', 2)
    RefreshMultihit()
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr02', 2)
    RefreshMultihit()
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr01', 2)
    RefreshMultihit()
    CommonSE('014_electric_ll')
    sprite('vrrcef_fggr00', 6)
    NoAttackDuringAction(1)
    NoDamageAction(1)
    DespawnEAEffect('LightningFrog')
    CreateObject('LightningFrogDelete', -1)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr03', 6)
    sprite('vrrcef_fggr02', 6)
    PrivateSE('rcse_06')
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr00', 6)
    loopRest()
    if SLOT_IsUnlimited:
        conditionalSendToLabel(337)
    sprite('vrrcef_fggr00', 6)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr03', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr01', 6)
    gotoLabel(324)
    label(337)
    sprite('vrrcef_fggr00', 6)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr03', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr00', 6)
    sprite('vrrcef_fggr00', 6)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr03', 6)
    sprite('vrrcef_fggr02', 6)
    sprite('vrrcef_fggr01', 6)
    sprite('vrrcef_fggr00', 6)
    loopRest()
    gotoLabel(338)
    label(324)
    SLOT_59 = 0
    NoAttackDuringAction(1)
    sprite('vrrcef_fggr03', 1)
    BlendMode_Normal()
    ConstantAlphaModifier(-14)
    CreateObject('FrogDelete', 0)


@State
def LightningFrog():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        RemoveOnCallStateEnd(2)
        Size(2700)
        AlphaValue(180)
        ContinueState(90)
    label(0)
    sprite('vrrcef_lightning03', 2)
    SetScaleSpeed(-200)
    RandAddRotation(-180000, 180000)
    sprite('vrrcef_lightning03', 2)
    SetScaleSpeed(200)
    RandAddRotation(-180000, 180000)
    loopRest()
    gotoLabel(0)


@State
def LightningFrogDelete():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        RemoveOnCallStateEnd(2)
        Size(2200)
        AlphaValue(255)
        AlphaValue(180)
    sprite('vrrcef_lightning03', 2)
    SetScaleSpeed(-200)
    ConstantAlphaModifier(-20)
    physicsYImpulse(4000)
    RandAddRotation(-180000, 180000)
    sprite('vrrcef_lightning03', 2)
    RandAddRotation(-180000, 180000)
    sprite('vrrcef_lightning03', 2)
    RandAddRotation(-180000, 180000)
    sprite('vrrcef_lightning03', 2)
    RandAddRotation(-180000, 180000)


@State
def StayThunder():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrrcef_stlt00', 1)
    Size(1000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrrcef_stlt01', 1)
    sprite('null', 1)
    sprite('vrrcef_stlt02', 1)
    sprite('null', 1)
    sprite('vrrcef_stlt03', 1)


@State
def ExWindRight():
    sprite('null', 100)
    CreateParticle('rcef_exwindR', -1)


@State
def rcef_212Rose():
    sprite('null', 100)
    E0EAEffectPosition(2)
    ParticleColorFromPalette(225, 226, 226)
    CallCustomizableParticle('rcef_212rose00', -1)
    CreateParticle('rcef_212light00', -1)


@State
def rcef_252Wind():
    sprite('null', 100)
    E0EAEffectPosition(2)
    CreateParticle('rcef_252up_mc02', -1)


@State
def rc201_Wind():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)

        def upon_56():
            E0EAEffectPosition(0)
    sprite('null', 19)
    BlendMode_Add()
    CommonSE('006_swing_blade_0')
    Eff3DEffect('rcef_windA.DIG', 'rcef_windA_mot_000.mmot')


@State
def rcef_201rose():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)

        def upon_56():
            E0EAEffectPosition(0)
    sprite('null', 100)
    CreateParticle('rcef_201rose01', 0)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_201rose02', 0)
    ParticleColorFromPalette(225, 224, 224)
    CallCustomizableParticle('rcef_201rose03', 0)
    CreateParticle('rcef_201rose04', 0)


@State
def rcef_202rose():
    sprite('null', 120)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_202rose00', -1)


@State
def rcef_202wind():
    sprite('null', 120)
    CreateParticle('rcef_202wind00', -1)
    CreateParticle('rcef_202wind01', -1)


@State
def rcef_202tsuki():
    sprite('null', 120)
    PaletteIndex(2)
    ParticleColorFromPalette(233, 127, 127)
    CallCustomizableParticle('rcef_202tsuki', -1)


@State
def rc231_Wind():
    sprite('null', 19)
    BlendMode_Add()
    CommonSE('006_swing_blade_0')
    Eff3DEffect('rcef_windB.DIG', 'rcef_windB_mot_000.mmot')


@State
def rcef_231rose():
    sprite('null', 100)
    CreateParticle('rcef_231rose01', 0)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_231rose02', 0)
    ParticleColorFromPalette(225, 224, 224)
    CallCustomizableParticle('rcef_231rose03', 0)
    CreateParticle('rcef_231rose04', 0)


@State
def rcef232ChairMc():
    sprite('null', 120)
    CreateParticle('rcef_elchair_mc00', 0)
    CreateParticle('rcef_elchair_mc01', 0)


@State
def rcef_602EntryPtc():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 100)
    LinkParticle('rcef_602entryptc')
    CreateObject('rcef_602EntryLight', -1)
    CreateObject('rcef_602EntryRose', -1)
    CreateObject('rcef_602EntryWind', -1)


@State
def rcef_602EntryRose():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 100)
    ParticleColorFromPalette(225, 226, 227)
    CallPrivateEffect('rcef_602entryrose00')


@State
def rcef_602EntryLight():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 100)
    LinkParticle('rcef_602entrylight00')


@State
def rcef_602EntryWind():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 100)
    LinkParticle('rcef_602entrywind00')


@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        SetZVal(10)
        Eff3DEffect('rcef_mc.DIG', 'rcef_mc_mot_000.mmot')
        FaceSpawnLocation()
        RenderLayer(2)
        ColorFromPaletteIndex(225)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    E0EAEffectPosition(3)
    sprite('null', 49)
    E0EAEffectPosition(0)


@State
def ModelMagicCircleAST():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
    sprite('null', 300)
    CreateObject('AstralMagicCircleA', -1)
    CreateObject('AstralMagicCircleB', -1)


@State
def AstralMagicCircleA():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('rcef_mc2.DIG', 'rcef_mc2_mot_000.mmot')
        FaceSpawnLocation()
        RenderLayer(2)
        BlendMode_Add()
        AlphaValue(0)
        Size(800)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    SetScaleSpeed(50)
    CommonSE('022_magiccircle_b')
    ColorForTransition(4294901760)
    ColorTransition(4294901760, 20)
    sprite('null', 120)
    SetScaleSpeed(0)
    sprite('null', 20)
    ColorTransition(4278190080, 20)
    ConstantAlphaModifier(-12)


@State
def AstralMagicCircleB():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('rcef_mc3.DIG', 'rcef_mc3_mot_000.mmot')
        FaceSpawnLocation()
        RenderLayer(2)
        BlendMode_Add()
        AlphaValue(0)
        Size(600)
    sprite('null', 60)
    sprite('null', 40)
    SetScaleSpeed(5)
    ConstantAlphaModifier(4)
    CommonSE('022_magiccircle_b')
    ColorForTransition(4278190080)
    ColorTransition(1090453504, 40)
    sprite('null', 10)
    AlphaValue(255)
    SetScaleSpeed(0)
    sprite('null', 20)
    ColorTransition(4278190080, 20)
    ConstantAlphaModifier(-12)
    SetScaleSpeed(2)


@State
def rcef_mc():
    sprite('null', 100)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_mc', -1)


@State
def rcef_600rose():
    sprite('null', 100)
    ParticleColorFromPalette(265, 266, 266)
    CallCustomizableParticle('rcef_600rose', 0)


@State
def rcef_404flog():
    sprite('null', 100)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_404flog', 0)


@State
def LightningRodStart():
    sprite('null', 100)
    E0EAEffectPosition(2)
    PaletteIndex(1)
    ParticleColorFromPalette(230, 230, 230)
    CallCustomizableParticle('rcef_lightrod_make', -1)


@State
def LightningRodRoop():
    sprite('null', 100)
    RemoveOnCallStateEnd(2)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('rcef_lightrod00', -1)
    ParticleColorFromPalette(230, 230, 230)
    CallCustomizableParticle('rcef_lightrod_roop', -1)


@State
def LightningRodDelete():
    sprite('null', 100)
    E0EAEffectPosition(2)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('rcef_lightrod_del00', -1)
    ParticleColorFromPalette(233, 233, 233)
    CallCustomizableParticle('rcef_lightrod_del01', -1)
    ParticleColorFromPalette(230, 230, 230)
    CallCustomizableParticle('rcef_lightrod_del', -1)


@State
def BatSummons():
    sprite('null', 100)
    E0EAEffectPosition(2)
    ParticleColorFromPalette(29, 29, 29)
    CallCustomizableParticle('rcef_gi_act00', -1)
    ParticleColorFromPalette(28, 28, 28)
    CallCustomizableParticle('rcef_gi_actb', -1)


@State
def BatDelete():
    sprite('null', 100)
    E0EAEffectPosition(2)
    ParticleColorFromPalette(29, 29, 29)
    CallCustomizableParticle('rcef_gi_act00', -1)
    ParticleColorFromPalette(28, 28, 28)
    CallCustomizableParticle('rcef_gi_act01', -1)
    CreateParticle('rcef_gi_act', -1)


@State
def BirdSummons():
    sprite('null', 120)
    PaletteIndex(2)
    CreateParticle('rcef_birdkirakira00', 0)
    ParticleColorFromPalette(239, 175, 127)
    CallCustomizableParticle('rcef_birdsummons', 0)


@State
def FrogDelete():
    sprite('null', 100)
    E0EAEffectPosition(2)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('rcef_gi_act00', -1)
    ParticleColorFromPalette(236, 236, 236)
    CallCustomizableParticle('rcef_gi_act01', -1)
    CreateParticle('rcef_gi_act', -1)


@State
def rcef212windA():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_212wind00')
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 120)


@State
def rcef212windB():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_212wind01')
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 120)


@State
def rcef252windA():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_252wind00')
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 120)


@State
def rcef252windB():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_252wind00')
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 120)


@State
def AstralFinishRose():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddY(-256000)
    sprite('null', 100)
    ParticleColorFromPalette(226, 226, 225)
    CallCustomizableParticle('rcef_astwinrose', -1)


@State
def BirdFire():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_birdfire')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 3)
    CreateParticle('rcef_birdfire', -1)


@State
def DownFallMcA():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_falldown_mc00')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 30)


@State
def DownFallMcB():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('rcef_falldown_mc01')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 30)


@State
def ReichelStormLv0():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_wind.DIG', 'rcef_storm_wind_motion_000.mmot')
        CreateObject('ReichelStormBG_Air_Lv1', -1)
        RegisterObject(4, 1)
        CreateObject('ReichelStormBG_Rain_Lv1', -1)
        RegisterObject(5, 1)
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 1)
        uponSendToLabel(56, 1)
    sprite('null', 30)
    ConstantAlphaModifier(3)
    if CharacterIDCheck('ta'):
        ConstantAlphaModifier(0)
        ObjectUpon(FALLING, 32)
        ObjectUpon(5, 32)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    clearUponHandler(33)
    clearUponHandler(56)
    sprite('null', 60)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ConstantAlphaModifier(-5)


@State
def ReichelStormLv1():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_wind.DIG', 'rcef_storm_wind_motion_000.mmot')
        CreateObject('ReichelStormBG_Air_Lv1', -1)
        RegisterObject(4, 1)
        CreateObject('ReichelStormBG_Rain_Lv1', -1)
        RegisterObject(5, 1)
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 1)
        uponSendToLabel(56, 1)
    sprite('null', 30)
    ConstantAlphaModifier(3)
    if CharacterIDCheck('ta'):
        ConstantAlphaModifier(0)
        ObjectUpon(FALLING, 32)
        ObjectUpon(5, 32)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    clearUponHandler(33)
    clearUponHandler(56)
    sprite('null', 60)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ConstantAlphaModifier(-5)


@State
def ReichelStormLv2():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_wind.DIG', 'rcef_storm_wind_motion_000.mmot')
        CreateObject('ReichelStormBG_Air_Lv2', -1)
        RegisterObject(4, 1)
        CreateObject('ReichelStormBG_Rain_Lv2', -1)
        RegisterObject(5, 1)
        BlendMode_Add()
        Size(1500)
        XPositionRelativeFacing(0)
        AbsoluteY(32000)
        AlphaValue(0)
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 1)
        uponSendToLabel(56, 1)
    sprite('null', 30)
    ConstantAlphaModifier(4)
    if CharacterIDCheck('ta'):
        ConstantAlphaModifier(0)
        ObjectUpon(FALLING, 32)
        ObjectUpon(5, 32)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    clearUponHandler(33)
    clearUponHandler(56)
    sprite('null', 60)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ConstantAlphaModifier(-5)


@State
def ReichelStormLv3():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_wind.DIG', 'rcef_storm_wind_motion_000.mmot')
        CreateObject('ReichelStormBG_Air_Lv3', -1)
        RegisterObject(4, 1)
        CreateObject('ReichelStormBG_Rain_Lv1', -1)
        RegisterObject(5, 1)
        CreateObject('ReichelStormBG_Rain_Lv3', -1)
        RegisterObject(6, 1)
        BlendMode_Add()
        Size(2000)
        XPositionRelativeFacing(0)
        AbsoluteY(64000)
        AlphaValue(0)
        uponSendToLabel(33, 1)
        uponSendToLabel(56, 1)
    IgnoreScreenfreeze(1)
    sprite('null', 30)
    ConstantAlphaModifier(5)
    if CharacterIDCheck('ta'):
        ConstantAlphaModifier(0)
        ObjectUpon(FALLING, 32)
        ObjectUpon(5, 32)
        ObjectUpon(6, 32)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    clearUponHandler(33)
    clearUponHandler(56)
    sprite('null', 60)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)
    ConstantAlphaModifier(-5)


@State
def ReichelStormLv4():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_wind.DIG', 'rcef_storm_wind_motion_000.mmot')
        CreateObject('ReichelStormBG_Air_Lv4', -1)
        RegisterObject(4, 1)
        CreateObject('ReichelStormBG_Rain_Lv2', -1)
        RegisterObject(5, 1)
        CreateObject('ReichelStormBG_Rain_Lv4', -1)
        RegisterObject(6, 1)
        BlendMode_Add()
        Size(3000)
        XPositionRelativeFacing(0)
        AbsoluteY(160000)
        AlphaValue(0)
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 1)
        uponSendToLabel(56, 1)
    sprite('null', 30)
    ConstantAlphaModifier(6)
    if CharacterIDCheck('ta'):
        ConstantAlphaModifier(0)
        ObjectUpon(FALLING, 32)
        ObjectUpon(5, 32)
        ObjectUpon(6, 32)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    clearUponHandler(33)
    clearUponHandler(56)
    sprite('null', 60)
    ObjectUpon(FALLING, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)
    ConstantAlphaModifier(-5)


@State
def GeneratorLv0():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 12)
    CreateObject('ReichelStormA', -1)
    sprite('null', 10)
    CreateObject('ReichelStormA', -1)


@State
def GeneratorLv0_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 12)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 10)
    CreateObject('ReichelStormA_ODFinish', -1)


@State
def GeneratorLv1():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 12)
    CreateObject('ReichelStormA', -1)
    sprite('null', 10)
    CreateObject('ReichelStormA', -1)
    ObjectUpon(STATE_END, 41)


@State
def GeneratorLv1_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 12)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 10)
    CreateObject('ReichelStormA_ODFinish', -1)
    ObjectUpon(STATE_END, 41)


@State
def GeneratorLv2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 7)
    CreateObject('ReichelStormA', -1)
    sprite('null', 11)
    CreateObject('ReichelStormA', -1)
    sprite('null', 10)
    CreateObject('ReichelStormB', -1)
    ObjectUpon(STATE_END, 41)


@State
def GeneratorLv2_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA_OD', -1)
    ObjectUpon(STATE_END, 41)
    sprite('null', 10)
    CreateObject('ReichelStormA_OD', -1)
    ObjectUpon(STATE_END, 41)
    sprite('null', 13)
    CreateObject('ReichelStormA_OD', -1)
    ObjectUpon(STATE_END, 41)
    sprite('null', 13)
    CreateObject('ReichelStormB_OD', -1)


@State
def GeneratorLv3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormB', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 6)
    CreateObject('ReichelStormA', -1)
    sprite('null', 15)
    CreateObject('ReichelStormB', -1)
    sprite('null', 10)
    CreateObject('ReichelStormC', -1)


@State
def GeneratorLv3_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 3)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 4)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormA_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 8)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 8)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 15)
    CreateObject('ReichelStormB_OD', -1)
    ObjectUpon(STATE_END, 40)
    sprite('null', 10)
    CreateObject('ReichelStormC_OD', -1)


@State
def GeneratorLv4():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB', -1)
    sprite('null', 15)
    CreateObject('ReichelStormC', -1)
    sprite('null', 10)
    CreateObject('ReichelStormD', -1)


@State
def GeneratorLv4_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 16)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 5)
    CreateObject('ReichelStormB_OD', -1)
    sprite('null', 6)
    CreateObject('ReichelStormC_OD', -1)
    sprite('null', 12)
    CreateObject('ReichelStormC_OD', -1)
    sprite('null', 15)
    CreateObject('ReichelStormD_OD', -1)
    sprite('null', 10)
    CreateObject('ReichelStormD_ODFinish', -1)


@Subroutine
def ReichelStorm_Matome():
    TeleportToObject(3)
    SetPosYByScreenPer(50)
    SetPosXByScreenPer(-4)
    ExternalForcesRate(50, 50)
    SelfWind(100, 100, 0)
    PaletteIndex(3)
    SetZVal(-100)
    BlendMode_Normal()
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageInterval(1)
    AfterimageCount(2)
    FloorCollision(1)
    CollideWithWall(1)
    IgnoreScreenfreeze(0)
    ContinueState(480)

    def upon_OPPONENT_HIT_OR_BLOCK():
        clearUponHandler(OPPONENT_HIT_OR_BLOCK)
        PerExternalForces(0)
        ExternalForcesRate(0, 0)
        XImpulseAcceleration(20)
        if random_(2, 0, 50):
            XImpulseAcceleration(150)
        if random_(2, 0, 50):
            XImpulseAcceleration(150)
        if random_(2, 0, 50):
            XImpulseAcceleration(200)
        YAccel(60)
        if random_(2, 0, 50):
            YAccel(130)
        if random_(2, 0, 50):
            YAccel(130)
        if random_(2, 0, 50):
            YAccel(150)
        sendToLabel(1)

    def upon_5():
        clearUponHandler(5)
        FloorCollision(0)
        SetAcceleration(0)
        XImpulseAcceleration(30)
        if random_(2, 0, 50):
            XImpulseAcceleration(130)
        if random_(2, 0, 50):
            XImpulseAcceleration(130)
        if random_(2, 0, 50):
            XImpulseAcceleration(200)
        YAccel(-60)
        if random_(2, 0, 50):
            YAccel(120)
        if random_(2, 0, 50):
            YAccel(120)
        if random_(2, 0, 50):
            YAccel(150)
        setGravity(1000)

    def upon_PLAYER_DAMAGED():
        ExternalForcesRate(0, 0)


@Subroutine
def ReichelStorm_Koumori():
    AttackDefaults_SuperProjectile()
    AttackLevel_(3)
    Damage(300)
    ChipPercentage(15)
    MinimumDamage(10)
    AttackP2(94)
    Hitstun(25)
    AirUntechableTime(40)
    AirPushbackX(3000)
    AirPushbackY(35000)
    StarterRating(0)
    VoodooDamageMultiplier(2)
    AddRotationPerFrame(3000)
    physicsXImpulse(18000)
    physicsYImpulse(12000)
    SetAcceleration(300)
    setGravity(1500)
    RandSpeedY(-3000, 3000)
    RandSpeedX(-2000, 6000)
    DeviationY(50000, 130000)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

    def upon_54():
        clearUponHandler(54)
        sendToLabel(1)
    AttackOff()


@Subroutine
def ReichelStorm_Ushi():
    AttackDefaults_SuperProjectile()
    AttackLevel_(3)
    Damage(400)
    ChipPercentage(15)
    MinimumDamage(10)
    AttackP2(94)
    AirUntechableTime(50)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(3000)
    AirPushbackY(35000)
    StarterRating(0)
    VoodooDamageMultiplier(2)
    AddRotationPerFrame(2500)
    physicsXImpulse(18000)
    physicsYImpulse(12000)
    SetAcceleration(300)
    setGravity(1500)
    RandSpeedY(-3000, 3000)
    RandSpeedX(-2000, 6000)
    DeviationY(50000, 130000)
    RandAddRotation(30000, 160000)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

    def upon_54():
        clearUponHandler(54)
        sendToLabel(1)
    LandingHeight(120000)
    AttackOff()

    def upon_41():
        AddY(100000)
        Damage(600)
        Size(1300)


@Subroutine
def ReichelStorm_Pumpkin():
    AttackDefaults_SuperProjectile()
    AttackLevel_(4)
    Damage(500)
    ChipPercentage(15)
    MinimumDamage(10)
    AttackP2(94)
    AirUntechableTime(90)
    Hitstop(3)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackX(3000)
    AirPushbackY(35000)
    StarterRating(0)
    VoodooDamageMultiplier(2)
    AddRotationPerFrame(7500)
    physicsXImpulse(18000)
    physicsYImpulse(20000)
    SetAcceleration(300)
    setGravity(1500)
    RandSpeedY(-3000, 3000)
    RandSpeedX(-2000, 6000)
    DeviationY(50000, 100000)
    LandingHeight(120000)
    AttackOff()

    def upon_41():
        AddY(100000)
        Damage(800)
        Size(1500)


@Subroutine
def ReichelStorm_KingFlog():
    AttackDefaults_SuperProjectile()
    AttackLevel_(5)
    ChipPercentage(15)
    MinimumDamage(10)
    AttackP2(94)
    AirUntechableTime(90)
    Hitstop(3)
    GroundedHitstunAnimation(14)
    AirHitstunAnimation(14)
    AirPushbackX(3000)
    AirPushbackY(35000)
    StarterRating(0)
    VoodooDamageMultiplier(2)
    AddRotationPerFrame(7500)
    physicsXImpulse(18000)
    physicsYImpulse(20000)
    SetAcceleration(300)
    setGravity(1500)
    LandingHeight(120000)
    AttackOff()


@State
def ReichelStormA():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Koumori')

        def upon_41():
            Damage(400)
            Size(2000)
    sprite('vrrcef_stmA', 5)
    sprite('vrrcef_stmA', 1)
    RefreshMultihit()
    sprite('vrrcef_stmA', 32767)
    label(1)
    sprite('vrrcef_stmA', 200)
    NoAttackDuringAction(1)


@State
def ReichelStormA_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Koumori')
        AttackType(4)

        def upon_41():
            Damage(400)
            Size(2000)
    sprite('vrrcef_stmA', 5)
    sprite('vrrcef_stmA', 1)
    RefreshMultihit()
    sprite('vrrcef_stmA', 32767)
    label(1)
    sprite('vrrcef_stmA', 200)
    NoAttackDuringAction(1)


@State
def ReichelStormA_ODFinish():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Koumori')
        AttackType(4)

        def upon_41():
            Damage(400)
            Size(2000)
    sprite('vrrcef_stmA', 5)
    sprite('vrrcef_stmA', 1)
    RefreshMultihit()
    sprite('vrrcef_stmA', 32767)
    label(1)
    sprite('vrrcef_stmA', 200)
    NoAttackDuringAction(1)


@State
def ReichelStormB():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Ushi')
    sprite('vrrcef_stmB00', 5)
    sprite('vrrcef_stmB00', 1)
    RefreshMultihit()
    label(99)
    sprite('vrrcef_stmB00', 2)
    sprite('vrrcef_stmB01', 2)
    sprite('vrrcef_stmB02', 2)
    sprite('vrrcef_stmB03', 2)
    gotoLabel(99)
    label(1)
    sprite('vrrcef_stmB00', 200)
    PrivateSE('rcse_20')
    NoAttackDuringAction(1)


@State
def ReichelStormB_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Ushi')
        AttackType(4)

        def upon_40():
            Size(1300)
    sprite('vrrcef_stmB00', 5)
    sprite('vrrcef_stmB00', 1)
    RefreshMultihit()
    label(99)
    sprite('vrrcef_stmB00', 2)
    sprite('vrrcef_stmB01', 2)
    sprite('vrrcef_stmB02', 2)
    sprite('vrrcef_stmB03', 2)
    gotoLabel(99)
    label(1)
    sprite('vrrcef_stmB00', 200)
    PrivateSE('rcse_20')
    NoAttackDuringAction(1)


@State
def ReichelStormC():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Pumpkin')
        CreateObject('ReichelStormCoption', -1)
        Size(1200)
    sprite('vrrcef_stmC', 5)
    sprite('vrrcef_stmC', 1)
    RefreshMultihit()
    sprite('vrrcef_stmC', 32767)
    label(1)
    sprite('vrrcef_stmC', 10)
    RefreshMultihit()
    sprite('vrrcef_stmC', 10)
    RefreshMultihit()
    Hitstop(11)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
    uponSendToLabel(54, 580)
    label(580)
    sprite('vrrcef_stmC', 180)
    clearUponHandler(54)
    PrivateSE('rcse_22')
    NoAttackDuringAction(1)


@State
def ReichelStormC_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Pumpkin')
        AttackType(4)
        CreateObject('ReichelStormCoption', -1)
        ObjectUpon(STATE_END, 32)
        Size(1400)
    sprite('vrrcef_stmC', 5)
    sprite('vrrcef_stmC', 1)
    RefreshMultihit()
    sprite('vrrcef_stmC', 32767)
    label(1)
    sprite('vrrcef_stmC', 10)
    RefreshMultihit()
    sprite('vrrcef_stmC', 10)
    RefreshMultihit()
    Hitstop(11)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
    uponSendToLabel(54, 580)
    label(580)
    sprite('vrrcef_stmC', 180)
    clearUponHandler(54)
    PrivateSE('rcse_22')
    NoAttackDuringAction(1)


@State
def ReichelStormCoption():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        SetZVal(501)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        IgnoreScreenfreeze(1)
        Size(1000)

        def upon_32():
            Size(1200)
    label(0)
    AddRotationPerFrame(7500)
    sprite('vrrcef_stmCopt00', 6)
    Rotation(30000)
    sprite('vrrcef_stmCopt01', 6)
    Rotation(30000)
    sprite('vrrcef_stmCopt02', 6)
    Rotation(30000)
    loopRest()
    gotoLabel(0)


@State
def ReichelStormD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        Damage(600)
        CreateObject('ReichelStormDoption', -1)
    sprite('vrrcef_stmD', 5)
    sprite('vrrcef_stmD', 1)
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)
    E0EAEffectPosition(0)
    label(1)
    sprite('vrrcef_stmD', 20)
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)
    RefreshMultihit()
    Hitstop(20)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
    uponSendToLabel(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)
    clearUponHandler(54)
    PrivateSE('rcse_21')
    NoAttackDuringAction(1)


@State
def ReichelStormD_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        Damage(600)
        AttackType(4)
        CreateObject('ReichelStormDoption', -1)
    sprite('vrrcef_stmD', 5)
    sprite('vrrcef_stmD', 1)
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)
    E0EAEffectPosition(0)
    label(1)
    sprite('vrrcef_stmD', 20)
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)
    RefreshMultihit()
    Hitstop(20)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
    uponSendToLabel(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)
    clearUponHandler(54)
    PrivateSE('rcse_21')
    NoAttackDuringAction(1)


@State
def ReichelStormD_ODFinish():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        Damage(600)
        AttackType(4)
        CreateObject('ReichelStormDoptionOver', -1)
        Size(1300)
    sprite('vrrcef_stmD', 5)
    sprite('vrrcef_stmD', 1)
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)
    E0EAEffectPosition(0)
    label(1)
    sprite('vrrcef_stmD', 20)
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)
    RefreshMultihit()
    Hitstop(20)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
    uponSendToLabel(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)
    clearUponHandler(54)
    PrivateSE('rcse_21')
    NoAttackDuringAction(1)


@State
def ReichelStormDoption():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        SetZVal(501)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AddRotationPerFrame(5500)
        IgnoreScreenfreeze(1)
    label(0)
    sprite('vrrcef_stmDopt00', 4)
    Rotation(10000)
    sprite('vrrcef_stmDopt01', 4)
    Rotation(10000)
    sprite('vrrcef_stmDopt02', 4)
    Rotation(10000)
    loopRest()
    gotoLabel(0)


@State
def ReichelStormDoptionOver():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        SetZVal(501)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageInterval(1)
        AfterimageCount(4)
        AddRotationPerFrame(5500)
        Size(1300)
        IgnoreScreenfreeze(1)
    label(0)
    sprite('vrrcef_stmDopt00', 4)
    Rotation(10000)
    sprite('vrrcef_stmDopt01', 4)
    Rotation(10000)
    sprite('vrrcef_stmDopt02', 4)
    Rotation(10000)
    loopRest()
    gotoLabel(0)


@State
def ReichelStormBG_Air_Lv1():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_air.DIG', 'rcef_storm_air_motion_000.mmot')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
    sprite('null', 30)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def ReichelStormBG_Air_Lv2():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_air.DIG', 'rcef_storm_air_motion_000.mmot')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
    sprite('null', 30)
    ConstantAlphaModifier(4)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def ReichelStormBG_Air_Lv3():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_air.DIG', 'rcef_storm_air_motion_000.mmot')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
    sprite('null', 30)
    ConstantAlphaModifier(7)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def ReichelStormBG_Air_Lv4():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_air.DIG', 'rcef_storm_air_motion_000.mmot')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
    sprite('null', 30)
    ConstantAlphaModifier(10)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def ReichelStormBG_Rain_Lv1():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_rain_Lv1.DIG',
            'rcef_storm_rain_Lv1_motion_000.')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
        CancelIfPlayerHit(3)
    sprite('null', 30)
    ConstantAlphaModifier(4)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 15)
    ConstantAlphaModifier(-20)


@State
def ReichelStormBG_Rain_Lv2():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_rain_Lv2.DIG',
            'rcef_storm_rain_Lv2_motion_000.')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
        CancelIfPlayerHit(3)
    sprite('null', 30)
    ConstantAlphaModifier(6)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 15)
    ConstantAlphaModifier(-20)


@State
def ReichelStormBG_Rain_Lv3():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_rain_Lv3.DIG',
            'rcef_storm_rain_Lv3_motion_000.')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
        CancelIfPlayerHit(3)
    sprite('null', 30)
    ConstantAlphaModifier(10)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 15)
    ConstantAlphaModifier(-20)


@State
def ReichelStormBG_Rain_Lv4():

    def upon_IMMEDIATE():
        Eff3DEffect('rcef_storm_rain_Lv4.DIG',
            'rcef_storm_rain_Lv4_motion_000.')
        BlendMode_Add()
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)
        CancelIfPlayerHit(3)
    sprite('null', 30)
    ConstantAlphaModifier(10)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 15)
    ConstantAlphaModifier(-20)


@State
def rc202SwordLight():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    sprite('vrrcef202_11', 4)
    AlphaValue(255)
    sprite('vrrcef202_12', 8)
    ConstantAlphaModifier(-30)


@State
def rc232ElectlicChair():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        ContinueState(13)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    label(0)
    sprite('vrrcef_232_07', 1)
    sprite('vrrcef_232_08', 1)
    sprite('vrrcef_232_08add01', 1)
    sprite('vrrcef_232_08add02', 1)
    loopRest()
    gotoLabel(0)


@State
def Bird():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        AttackP2(92)
        Hitstop(9)
        Hitstun(20)
        AirUntechableTime(20)
        StarterRating(2)
        AttackOff()
        BlendMode_Normal()
        PaletteIndex(1)
        FloorCollision(1)
        E0EAEffect('cmn_judgment', 65535)

        def RunOnObject_1():
            AbsoluteY(80000)
        SetActionMark(4)
        SLOT_51 = 300

        def upon_32():
            if SLOT_2:
                sendToLabel(99)

        def upon_33():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(1)

        def upon_34():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(2)

        def upon_35():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(3)

        def upon_36():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(4)

        def upon_38():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(6)

        def upon_39():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(7)

        def upon_40():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(8)

        def upon_41():
            if SLOT_2:
                SLOT_51 = 180
                AddActionMark(-1)
                sendToLabel(9)

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    SLOT_2 = 0
        uponSendToLabel(LANDING, 129)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)

        def upon_54():
            SetActionMark(0)
    label(0)
    if not SLOT_2:
        sendToLabel(99)
    sprite('vrrcef_pump00', 2)
    CreateObject('BirdFire', -1)
    AttackOff()
    physicsXImpulse(1500)
    physicsYImpulse(1000)
    Size(1000)
    SetScaleSpeed(0)
    uponSendToLabel(LANDING, 0)
    sprite('vrrcef_pump01', 2)
    sprite('vrrcef_pump02', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pump03', 2)
    sprite('vrrcef_pump02', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pump01', 2)
    loopRest()
    gotoLabel(0)
    label(129)
    sprite('vrrcef_pump00', 2)
    CreateObject('BirdFire', -1)
    AttackOff()
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    Size(1000)
    SetScaleSpeed(0)
    uponSendToLabel(LANDING, 129)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    FaceLeft()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(13)
    label(2)
    sprite('vrrcef_pumpdown00', 2)
    CreateObject('BirdFire', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)
    physicsXImpulse(0)
    physicsYImpulse(-45000)
    RefreshMultihit()
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(2000)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)
    CreateObject('BirdFire', -1)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(3)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    FaceRight()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(13)
    label(13)
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)
    physicsXImpulse(31815)
    physicsYImpulse(-31815)
    RefreshMultihit()
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(2000)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)
    CreateObject('BirdFire', -1)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpsidedown01', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(4)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    FaceLeft()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(46)
    label(6)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    FaceRight()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(46)
    label(46)
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)
    physicsXImpulse(45000)
    physicsYImpulse(0)
    RefreshMultihit()
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(2000)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)
    CreateObject('BirdFire', -1)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(7)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    FaceLeft()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(79)
    label(8)
    sprite('vrrcef_pumpup00', 2)
    CreateObject('BirdFire', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)
    physicsXImpulse(0)
    physicsYImpulse(45000)
    RefreshMultihit()
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(2000)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)
    CreateObject('BirdFire', -1)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    FaceRight()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(1000)
    SetScaleSpeed(100)
    CommonSE('001_airbackdash_0')
    CommonSE('006_swing_blade_1')
    CommonSE('015_blaze_0')
    loopRest()
    gotoLabel(79)
    label(79)
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)
    physicsXImpulse(31815)
    physicsYImpulse(31815)
    RefreshMultihit()
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(2000)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)
    CreateObject('BirdFire', -1)
    CommonSE('015_blaze_0')
    sprite('vrrcef_pumpsideup01', 2)
    CreateObject('BirdFire', -1)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(99)
    clearUponHandler(EVERY_FRAME)
    NoAttackDuringAction(1)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    SetScaleSpeed(0)
    Size(1000)
    SLOT_2 = 0
    clearUponHandler(LANDING)
    sprite('vrrcef_sbbreak00', 2)
    sprite('vrrcef_sbbreak01', 2)
    sprite('vrrcef_sbbreak02', 2)
    sprite('vrrcef_sbbreak03', 2)


@Subroutine
def LightningRod_Initialize():
    AttackDefaults_SpecialProjectile()
    PaletteIndex(1)
    BlendMode_Normal()
    AlphaValue(255)
    WallCollisionDetection(1)

    def upon_CORNERED():
        if SLOT_54:
            clearUponHandler(CORNERED)
            XImpulseAcceleration(-60)
            SLOT_55 = 40
    ExternalForcesRate(100, 100)
    SelfWind(100, 100, 0)

    def upon_32():
        sendToLabel(35)

    def upon_53():
        sendToLabel(35)

    def upon_33():
        if SLOT_2:
            clearUponHandler(LANDING)
            SLOT_58 = 0
            AttackOff()
            sendToLabel(47)

    def upon_41():
        if SLOT_2:
            clearUponHandler(LANDING)
            SLOT_54 = 0
            AttackOff()
            sendToLabel(49)

    def upon_40():
        if SLOT_2:
            clearUponHandler(LANDING)
            SLOT_54 = 0
            AttackOff()
            sendToLabel(48)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_66:
                SLOT_55 = SLOT_55 + -1
                if not SLOT_55:
                    RefreshMultihit()
    AttackLevel_(3)
    Damage(850)
    AttackP1(80)
    AttackP2(89)
    SameMoveProration(10)
    SingleProration(1)
    AirPushbackY(12000)
    AirUntechableTime(30)

    def upon_34():
        AirPushbackX(7000)
        AirPushbackY(7000)
        physicsXImpulse(7000)
        physicsYImpulse(8500)
        setGravity(1200)

    def upon_35():
        AirPushbackX(9500)
        physicsXImpulse(9500)
        physicsYImpulse(27000)
        setGravity(1200)

    def upon_36():
        AirPushbackX(12000)
        physicsXImpulse(15000)
        physicsYImpulse(36000)
        setGravity(1200)

    def upon_37():
        AirPushbackX(21000)
        physicsXImpulse(21000)
        physicsYImpulse(25000)
        setGravity(1500)

    def upon_38():
        AirPushbackX(27000)
        physicsXImpulse(27000)
        physicsYImpulse(-9000)
        setGravity(1500)

    def upon_39():
        AirPushbackX(13000)
        physicsXImpulse(13000)
        physicsYImpulse(-30000)
        setGravity(1000)
    uponSendToLabel(LANDING, 70)
    HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)

    def upon_54():
        AttackOff()
        EnableAfterimage(0)
        StopCharacterFlash1(0)
        XImpulseAcceleration(-30)
        physicsYImpulse(20000)
        ExternalForcesRate(0, 0)
        ResetExternalForces()
        AddRotationPerFrame(-10000)

    def upon_PLAYER_DAMAGED():
        CreateObject('StayThunder', 100)
        CreateObject('StayThunder', 100)
        CreateObject('StayThunder', 100)
        CreateObject('StayThunder', 100)
        ColorForTransition(4288716960)
        EnableAfterimage(1)
        AfterimageCount(6)
        EndAttack()
        clearUponHandler(PLAYER_DAMAGED)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SLOT_66 = 1
        AttackOff()

    def upon_58():
        if EnteredState('ShotCatch'):
            if SLOT_2 == 1:
                if SLOT_66:
                    sendToLabel(50)
        if EnteredState('SummonWindRateUpGhost'):
            if SLOT_2:
                clearUponHandler(LANDING)
                AttackOff()
                sendToLabel(51)
        if EnteredState('SummonWindSuctionGhost'):
            if SLOT_2:
                clearUponHandler(LANDING)
                AttackOff()
                sendToLabel(52)


@State
def LightningRodA():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_lightrod00', 2)
    Size(500)
    AddRotationPerFrame(30000)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRodB():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)
    Size(500)
    AddRotationPerFrame(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(9500)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRodC():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)
    Size(500)
    AddRotationPerFrame(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(12000)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRodA_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_lightrod00', 2)
    Size(500)
    AddRotationPerFrame(30000)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRodB_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)
    Size(500)
    AddRotationPerFrame(30000)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRodC_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)
    Size(500)
    AddRotationPerFrame(30000)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 5)
    Size(1000)
    SetActionMark(1)
    sprite('vrrcef_lightrod00', 32767)
    SLOT_54 = 1
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(49)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkSubOD', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def LightningRod_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        BlendMode_Normal()
        AlphaValue(255)
        IgnoreScreenfreeze(1)
        WallCollisionDetection(1)

        def upon_CORNERED():
            XImpulseAcceleration(-30)
        ExternalForcesRate(100, 100)
        SelfWind(100, 100, 0)

        def upon_32():
            sendToLabel(35)

        def upon_53():
            sendToLabel(35)

        def upon_33():
            if SLOT_2:
                clearUponHandler(LANDING)
                sendToLabel(47)

        def upon_40():
            if SLOT_2:
                clearUponHandler(LANDING)
                sendToLabel(48)
        AttackLevel_(4)
        AttackP1(80)

        def upon_34():
            setGravity(1500)
            physicsXImpulse(7000)
            physicsYImpulse(9000)
            AttackP1(80)
            AttackP2(89)
            Damage(600)
            SameMoveProration(80)
            AirPushbackX(7000)
            AirPushbackY(12000)
            AirUntechableTime(30)

        def upon_35():
            setGravity(1500)
            physicsXImpulse(9500)
            physicsYImpulse(27000)
            AttackP2(89)
            Damage(600)
            AirPushbackX(9500)
            AirUntechableTime(30)

        def upon_36():
            setGravity(1500)
            physicsXImpulse(12000)
            physicsYImpulse(36000)
            AttackP2(89)
            Damage(600)
            AirUntechableTime(30)
            AirPushbackX(13000)

        def upon_37():
            Damage(600)
            setGravity(1500)
            physicsXImpulse(21000)
            physicsYImpulse(25000)
            AirPushbackX(22500)
            AirUntechableTime(30)

        def upon_38():
            Damage(600)
            setGravity(1500)
            physicsXImpulse(27000)
            physicsYImpulse(-9000)
            AirPushbackX(29000)
            AirPushbackY(-27000)
            AirUntechableTime(30)

        def upon_39():
            Damage(600)
            setGravity(1000)
            physicsXImpulse(13000)
            physicsYImpulse(-30000)
            AirPushbackX(13000)
            AirPushbackY(-27000)
            Hitstun(23)
            AirUntechableTime(30)
        uponSendToLabel(LANDING, 70)
        HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)

        def upon_PLAYER_DAMAGED():
            CreateObject('StayThunder', 100)
            CreateObject('StayThunder', 100)
            CreateObject('StayThunder', 100)
            CreateObject('StayThunder', 100)
            ColorForTransition(4288716960)
            EnableAfterimage(1)
            AfterimageCount(6)
            EndAttack()
            clearUponHandler(PLAYER_DAMAGED)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_66 = 1

        def upon_58():
            if EnteredState('ShotCatch'):
                if SLOT_2 == 1:
                    if SLOT_66:
                        sendToLabel(50)
            if EnteredState('SummonWindRateUpGhost'):
                if SLOT_2:
                    clearUponHandler(LANDING)
                    sendToLabel(51)
            if EnteredState('SummonWindSuctionGhost'):
                if SLOT_2:
                    clearUponHandler(LANDING)
                    sendToLabel(52)
    sprite('vrrcef_lightrod00', 2)
    Size(500)
    AddRotationPerFrame(30000)
    sprite('vrrcef_lightrod00', 2)
    Size(750)
    sprite('vrrcef_lightrod00', 32767)
    Size(1000)
    SetActionMark(1)
    loopRest()
    label(70)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    StopCharacterFlash1(0)
    EnableAfterimage(0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    SetActionMark(2)
    SLOT_66 = 0
    clearUponHandler(LANDING)
    EndMomentum(1)
    AbsoluteY(0)
    RotationAngle(0)
    AddRotationPerFrame(0)
    SetZVal(500)
    sprite('vrrcef_lightrod01', 3)
    CreateObject('LightningRodStart', -1)
    CommonSE('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)
    sprite('vrrcef_lightrod03', 3)
    sprite('vrrcef_lightrod04', 3)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(512000)
    label(77)
    sprite('vrrcef_lightrod05', 5)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    SetZVal(500)
    CreateObject('LightningRodRoop', -1)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    CreateObject('StayThunder', 106)
    physicsYImpulse(500)
    YSpeed(-50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(250)
    YSpeed(-25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(100)
    YSpeed(-10)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-500)
    YSpeed(50)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-250)
    YSpeed(25)
    sprite('vrrcef_lightrod05', 5)
    physicsYImpulse(-100)
    YSpeed(10)
    loopRest()
    gotoLabel(77)
    label(35)
    SetActionMark(0)
    sprite('keep', 20)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    ConstantAlphaModifier(-12)
    CreateObject('LightningRodDelete', -1)
    EndMomentum(1)
    clearUponHandler(LANDING)
    EndAttack()
    loopRest()
    ExitState()
    label(47)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    if SLOT_OverdriveTimer:
        SLOT_52 = 1
    if SLOT_52:
        CreateObject('LightningObjAtkSubOD', 104)
    else:
        CreateObject('LightningObjAtkSub', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(48)
    SetActionMark(0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('LightningObjAtkMini_Event', 104)
    CreateObject('LightningRodDelete', 104)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(50)
    SetActionMark(0)
    AttackOff()
    sprite('keep', 15)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-31)
    loopRest()
    ExitState()
    label(51)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindRateUpGhost', 0)
    ObjectUpon(STATE_END, 38)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()
    label(52)
    SetActionMark(0)
    CreateParticle('rcef_412_wind', 0)
    CreateObject('rcef_412rose', 0)
    sprite('keep', 30)
    HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(58)
    ColorForTransition(4294967295)
    EnableAfterimage(0)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    AddRotationPerFrame(0)
    CreateObject('WindSuctionGhost', 0)
    ObjectUpon(STATE_END, 38)
    ConstantAlphaModifier(-12)
    loopRest()
    ExitState()


@State
def rcef_412rose():
    sprite('null', 120)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_412_rose', -1)


@State
def LightningObjAtk():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SuperProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(450)
        MinimumDamage(15)
        AttackP2(75)
        SingleProration(1)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(100)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        HitsparkSize(500)
        StarterRating(2)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_lightning01', 2)
    RotationAngle(15000)
    AddX(150000)
    SetScaleX(2000)
    SetScaleY(1000)
    StartMultihit()
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning01', 2)
    RotationAngle(-15000)
    AddX(-300000)
    SetScaleX(-2000)
    SetScaleY(1000)
    StartMultihit()
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    AddX(150000)
    SetScaleX(1200)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(1500)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1500)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def LightningObjAtk_Matome():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(350)
        MinimumDamage(15)
        AttackP2(75)
        SingleProration(1)
        AirUntechableTime(100)
        Hitstop(4)
        GroundedHitstunAnimation(14)
        AirHitstunAnimation(14)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        HitsparkSize(500)
        StarterRating(2)
        AttackType(4)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 6)
    CreateObject('LightningObjAtk_OD', 100)
    CreateObject('LightningObjAtk_OD', 100)
    ObjectUpon(STATE_END, 32)
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)
    RefreshMultihit()
    sprite('null', 4)


@State
def LightningObjAtk_OD():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        RotationAngle(15000)
        AddX(125000)

        def upon_32():
            AddX(-310000)
        NoAttackDuringAction(1)
    sprite('vrrcef_lightning01', 2)
    SetScaleX(2000)
    SetScaleY(1000)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning01', 2)
    RotationAngle(-15000)
    AddX(200000)
    SetScaleX(-2000)
    SetScaleY(1000)
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    AddX(-170000)
    SetScaleX(1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(1500)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1500)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(1500)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1500)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)
    SetScaleX(-1200)
    SetScaleY(2000)
    CreateObject('LightningLand', -1)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def LightningObjAtkSub_Matome():
    sprite('null', 2)
    TriggerUponForState('LightningLandB', 32)
    TriggerUponForState('LightningAirB', 32)
    sprite('null', 2)
    TriggerUponForState('LightningLandB', 35)
    TriggerUponForState('LightningAirB', 35)
    sprite('null', 2)
    TriggerUponForState('LightningLandB', 33)
    TriggerUponForState('LightningAirB', 33)
    sprite('null', 2)
    TriggerUponForState('LightningLandB', 36)
    TriggerUponForState('LightningAirB', 36)
    sprite('null', 60)
    TriggerUponForState('LightningLandB', 34)
    TriggerUponForState('LightningAirB', 34)


@State
def LightningObjAtkSub():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SuperProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(250)
        MinimumDamage(15)
        AttackP1(75)
        AttackP2(100)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(100)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        HitsparkSize(500)
        AttackDirection(3)
        StarterRating(2)
        SameMoveProration(-1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('null', 2)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    if SLOT_52:
        SetScaleX(1050)
        SetScaleY(2000)
    else:
        SetScaleX(750)
        SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    if SLOT_52:
        SetScaleX(750)
        SetScaleY(2000)
    else:
        SetScaleX(-750)
        SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    if SLOT_52:
        SetScaleX(1250)
        SetScaleY(2000)
    else:
        SetScaleX(1000)
        SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1000)
    SetScaleY(1000)
    if SLOT_52:
        SetScaleX(1250)
        SetScaleY(2000)
    else:
        SetScaleX(-1000)
        SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def LightningObjAtkSubOD_Matome():
    sprite('null', 2)
    TriggerUponForState('LightningLandB_OD', 32)
    TriggerUponForState('LightningAirB_OD', 32)
    sprite('null', 2)
    TriggerUponForState('LightningLandB_OD', 35)
    TriggerUponForState('LightningAirB_OD', 35)
    sprite('null', 2)
    TriggerUponForState('LightningLandB_OD', 33)
    TriggerUponForState('LightningAirB_OD', 33)
    sprite('null', 2)
    TriggerUponForState('LightningLandB_OD', 36)
    TriggerUponForState('LightningAirB_OD', 36)
    sprite('null', 60)
    TriggerUponForState('LightningLandB_OD', 34)
    TriggerUponForState('LightningAirB_OD', 34)


@State
def LightningObjAtkSubOD():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SuperProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(250)
        MinimumDamage(15)
        AttackP1(75)
        AttackP2(100)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(100)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        HitsparkSize(500)
        AttackDirection(3)
        StarterRating(2)
        AttackType(4)
        SameMoveProration(-1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2 == 4:
                AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('null', 2)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(1050)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(750)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(1050)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(750)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(1050)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(750)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1250)
    SetScaleY(2000)
    RefreshMultihit()
    CreateObject('LightningLandSub', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def EffLightningMiniBoss():
    if random_(2, 0, 33):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('null', 30)
    SetPosXByScreenPer(40)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    ExitState()
    label(0)
    sprite('null', 30)
    SetPosXByScreenPer(90)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(-200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(-200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(-200000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    ExitState()
    label(1)
    sprite('null', 60)
    sprite('null', 20)
    TeleportToObject(3)
    AbsoluteY(0)
    sprite('null', 40)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 20)
    TeleportToObject(22)
    AbsoluteY(0)
    sprite('null', 40)
    CreateObject('LightningObjAtkMini', -1)
    ExitState()


@State
def EffLightningMiniEntryHZ():
    sprite('null', 30)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(-250000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)
    AddX(250000)
    CreateObject('LightningObjAtkMini', -1)
    sprite('null', 30)


@State
def LightningObjAtkMini():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SpecialProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(900)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        Hitstop(12)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        HitsparkSize(500)
        AirUntechableTime(46)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(3)
        Unknown12052(1)
        VoodooDamageMultiplier(3)
        Unknown23042()
        SetScaleX(500)
        AlphaValue(200)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_0')
    sprite('null', 2)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)


@State
def LightningObjAtkMini_Event():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SpecialProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(600)
        Hitstop(12)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        HitsparkSize(500)
        AirUntechableTime(42)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackP1(80)
        AttackDirection(3)
        SetScaleX(500)
        AlphaValue(200)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_0')
    sprite('null', 2)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)


@State
def LightningOption():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AlphaValue(200)
    sprite('null', 3)
    sprite('vrrcef_lightning01', 2)
    DeviationX(-100000, 100000)
    RandAddScaleX(-2000, 2000)
    RandSpeedX(-50000, 50000)
    SetScaleY(1000)


@State
def LightningLand():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnorePauses(2)
        if SLOT_OverdriveTimer:
            SLOT_52 = 1
        if SLOT_52:
            SetScaleX(3900)
            SetScaleY(2900)
        else:
            SetScaleX(3400)
            SetScaleY(2400)
        AlphaValue(255)
    sprite('vrrcef_lightning02', 2)
    SetScaleSpeed(-200)
    sprite('vrrcef_lightning02', 3)
    ConstantAlphaModifier(-85)


@State
def LightningLandSub():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnorePauses(2)
        SetScaleX(2800)
        SetScaleY(2000)
        AlphaValue(255)
        AlphaValue(200)
    sprite('vrrcef_lightning02', 2)
    SetScaleSpeed(-200)
    sprite('vrrcef_lightning02', 3)
    ConstantAlphaModifier(-85)


@State
def rc600giPot():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        SetZVal(-500)
        RemoveOnCallStateEnd(3)
    label(0)
    sprite('rc600_00ex01', 6)
    sprite('rc600_01ex01', 6)
    sprite('rc600_02ex01', 6)
    sprite('rc600_03ex01', 6)
    sprite('rc600_04ex01', 6)
    sprite('rc600_05ex01', 6)
    sprite('rc600_06ex01', 6)
    sprite('rc600_07ex01', 6)
    loopRest()
    gotoLabel(0)


@State
def rc620nago():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        SetZVal(-100)
        RemoveOnCallStateEnd(3)
    sprite('rc620_07n', 4)
    sprite('rc620_07nex01', 4)
    sprite('rc620_07nex02', 4)
    LandingEffects(0, 1, 0)
    sprite('rc620_07nex03', 4)
    label(0)
    sprite('rc620_07nex04', 4)
    loopRest()
    gotoLabel(0)


@State
def dengeki():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('rc082_00', 1)
    PaletteIndex(6)
    RandAddScale(-150, 150)
    DeviationX(-1000, 1000)
    DeviationY(-5000, 5000)
    sprite('rc082_00', 1)
    Size(1000)
    sprite('rc082_01', 1)
    PaletteIndex(7)
    RandAddScale(-150, 150)
    DeviationX(-1000, 1000)
    DeviationY(-5000, 5000)
    sprite('rc082_01', 1)
    Size(1000)
    loopRest()


@State
def dengeki_ng():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectObjectZ(2)
        SetZVal(100)

        def upon_16():
            SkeletonPaletteEffectOnNoStopIdling()
    sprite('rc082_00n', 32767)


@State
def AstralNago():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        physicsYImpulse(-5000)
        AbsoluteY(720000)
        AddX(8000)
        SetScaleX(-1000)
    sprite('rc450_n08', 6)
    sprite('rc450_n08ex01', 6)
    sprite('rc450_n08', 6)
    sprite('rc450_n08ex02', 6)
    sprite('rc450_n08', 6)
    sprite('rc450_n08ex01', 6)
    sprite('rc450_n08', 6)
    sprite('rc450_n08ex02', 6)
    sprite('rc450_n08', 6)
    sprite('rc450_n08ex01', 3)
    sprite('rc450_n08ex01', 1)
    CreateObject('BatDelete', 0)


@State
def LightningObjAST():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SuperProjectile()
        BlendMode_Add()
        SetZVal(100)
        NoAttackDuringAction(1)
    sprite('vrrcef_lightning01', 1)
    RotationAngle(15000)
    AddX(150000)
    SetScaleX(2000)
    SetScaleY(1000)
    StartMultihit()
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning01', 1)
    RotationAngle(-15000)
    AddX(-300000)
    SetScaleX(-2000)
    SetScaleY(1000)
    StartMultihit()
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    AddX(150000)
    SetScaleX(2400)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-2400)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(3000)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-3000)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    AddX(100000)
    SetScaleX(2400)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-2400)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(3000)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    AddX(-200000)
    SetScaleX(-3000)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    AddX(200000)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    AddX(-150000)
    SetScaleX(-1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def light():
    sprite('vr_light', 40)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)
    SetZVal(-500)
    IgnoreScreenfreeze(1)
    BlendMode_Add()
    SetScaleX(100)
    SetScaleXPerFrame(35)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 40)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('vr_light', 40)
    SetScaleXPerFrame(0)
    SetScaleX(1500)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('vr_light', 10)
    ColorForTransition(4294901760)
    ColorTransition(4278190080, 10)
    SetScaleXPerFrame(5)
    CommonSE('019_quake_0')


@State
def haka():
    sprite('vr_haka', 10)
    SetZVal(500)
    SetScaleY(0)
    SetScaleX(3000)
    SetScaleSpeedY(300)
    sprite('vr_haka', 1000)
    SetScaleSpeedY(0)


@State
def TestAstLightning():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        AttackLevel_(2)
        Damage(800)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(100)
        HitsparkSize(500)
    sprite('null', 200)
    sprite('vrrcef_lightning01', 2)
    RotationAngle(15000)
    AddX(150000)
    SetScaleX(2000)
    SetScaleY(1000)
    StartMultihit()
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning01', 2)
    RotationAngle(-15000)
    AddX(-300000)
    SetScaleX(-2000)
    SetScaleY(1000)
    StartMultihit()
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    AddX(150000)
    SetScaleX(1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1500)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1500)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleX(1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1200)
    SetScaleY(1000)
    RefreshMultihit()
    CreateObject('LightningLand', -1)
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_1')
    CommonSE('013_thunder_0')
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)


@State
def WindRateUpGhost():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(600)
        AttackP1(70)
        AttackP2(92)
        AttackDirection(3)
        StarterRating(2)
        FloorCollision(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetZVal(-100)
        CreateObject('WindRateUpGhost_fin', -1)

        def upon_41():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkSubOD', 104)
            SLOT_5 = 0

        def upon_39():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkSub', 104)
            SLOT_5 = 0

        def upon_40():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkMini', 104)
            SLOT_5 = 0

        def upon_53():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_32():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_33():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            clearUponHandler(54)
            TriggerUponForState('WindRateUpGhost', 33)
            SLOT_5 = 360
            SetActionMark(2)
            EndAttack()
            ExternalForcesRate(0, 0)
            SelfWind(0, 0, 0)
            sendToLabel(1)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 0)

        def upon_54():
            sendToLabel(99)

        def upon_EVERY_FRAME():
            if SLOT_2 == 1:
                ForceFaceSprite()
                ObjectUpon26(22, 0, -200000, 4000, 1)
            if SLOT_2 == 2:
                ForceFaceSprite()
                PrivateFunction3(22, -100000, 25000, 5, 1)
                physicsXImpulse(0)
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 26:
                SLOT_51 = 0
                PrivateSE('rcse_27')
    sprite('vrrcef412_00', 4)
    AttackOff()
    sprite('vrrcef412_01', 4)
    sprite('vrrcef412_02', 4)
    SetActionMark(1)
    sprite('vrrcef412_00', 3)
    RefreshMultihit()
    ExternalForcesRate(120, 120)
    SelfWind(120, 120, 0)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    loopRest()
    gotoLabel(99)
    label(1)
    HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    physicsXImpulse(-100000)
    physicsYImpulse(1000)
    IgnoreScreenfreeze(1)
    RemoveOnContact(22)
    label(51)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    if not SLOT_21:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(51)
    label(99)
    AttackOff()
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    EndMomentum(1)
    sprite('keep', 1)
    enterState('WindRateUpGhostEnd')
    label(100)
    sprite('keep', 1)


@State
def WindRateUpGhostEnd():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        FloorCollision(1)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetZVal(-100)
        AttackOff()
    sprite('vrrcef412_00', 6)
    CreateObject('WindRateUpGhost_fin_end', -1)
    ConstantAlphaModifier(-10)
    sprite('vrrcef412_01', 6)
    sprite('vrrcef412_02', 13)


@State
def WindRateUpGhost_fin():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    sprite('vrrcef412_10', 32767)
    AddRotationPerFrame(30000)


@State
def WindRateUpGhost_fin_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    sprite('vrrcef412_10', 32767)
    AddRotationPerFrame(30000)
    ConstantAlphaModifier(-25)


@State
def WindSuctionGhost():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(600)
        AttackP1(70)
        AirUntechableTime(20)
        AttackP2(92)
        AttackDirection(3)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(3)
        FloorCollision(1)
        Unknown23042()
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetZVal(-100)
        CreateObject('WindSuctionGhost_fin', -1)

        def upon_41():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkSubOD', 104)
            SLOT_6 = 0

        def upon_39():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkSub', 104)
            SLOT_6 = 0

        def upon_40():
            AttackOff()
            sendToLabel(100)
            CreateObject('LightningObjAtkMini', 104)
            SLOT_6 = 0

        def upon_53():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_32():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_33():
            if SLOT_2 == 2:
                sendToLabel(99)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            clearUponHandler(54)
            TriggerUponForState('WindSuctionGhost', 33)
            SLOT_6 = 360
            SetActionMark(2)
            EndAttack()
            ExternalForcesRate(0, 0)
            SelfWind(0, 0, 0)
            sendToLabel(1)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)

        def upon_54():
            sendToLabel(99)

        def upon_EVERY_FRAME():
            if SLOT_2 == 1:
                ForceFaceSprite()
                ObjectUpon26(22, 0, -200000, 4000, 1)
            if SLOT_2 == 2:
                ForceFaceSprite()
                PrivateFunction3(22, 0, 5000, 8, 1)
                physicsXImpulse(0)
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 26:
                SLOT_51 = 0
                PrivateSE('rcse_27')
    sprite('vrrcef412_00', 4)
    AttackOff()
    sprite('vrrcef412_01', 4)
    sprite('vrrcef412_02', 4)
    SetActionMark(1)
    sprite('vrrcef412_00', 3)
    RefreshMultihit()
    ExternalForcesRate(120, 120)
    SelfWind(120, 120, 0)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    loopRest()
    gotoLabel(99)
    label(1)
    HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    physicsXImpulse(-100000)
    physicsYImpulse(1000)
    IgnoreScreenfreeze(1)
    RemoveOnContact(22)
    label(51)
    sprite('vrrcef412_00', 3)
    sprite('vrrcef412_01', 3)
    sprite('vrrcef412_02', 3)
    if not SLOT_21:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(51)
    label(99)
    AttackOff()
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    ResetExternalForces()
    EndMomentum(1)
    sprite('keep', 1)
    enterState('WindSuctionGhostEnd')
    label(100)
    sprite('keep', 1)


@State
def WindSuctionGhostEnd():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        FloorCollision(1)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetZVal(-100)
        AttackOff()
    sprite('vrrcef412_00', 6)
    CreateObject('WindSuctionGhost_fin_end', -1)
    ConstantAlphaModifier(-10)
    sprite('vrrcef412_01', 6)
    sprite('vrrcef412_02', 13)


@State
def WindSuctionGhost_fin():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RemoveOnContact(22)
    sprite('vrrcef412_10', 32767)
    AddRotationPerFrame(30000)


@State
def WindSuctionGhost_fin_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RemoveOnContact(22)
    sprite('vrrcef412_10', 32767)
    AddRotationPerFrame(30000)
    ConstantAlphaModifier(-25)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        AddX(50000)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    physicsYImpulse(600000)
    sprite('null', 32767)
    physicsYImpulse(0)
    label(4)
    sprite('null', 100)
    physicsYImpulse(60000)
    sprite('null', 32767)
    physicsYImpulse(0)
    label(2)
    sprite('null', 10)
    physicsYImpulse(-600000)
    sprite('null', 3)
    physicsYImpulse(0)
    sprite('null', 32767)
    label(3)
    sprite('null', 1)


@State
def BurstDD_WindEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('rcef_430core')
        Eff3DEffect('rcef_440_trnado', '')
        SetScaleY(1600)
        SetScaleX(100)
        SetScaleZ(100)
        AddX(300000)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(18)
    SetScaleXPerFrame(105)
    SetScaleSpeedZ(105)
    PrivateSE('rcse_08')
    PrivateSE('rcse_09')
    PrivateSE('rcse_10')
    sprite('null', 10)
    ConstantAlphaModifier(0)
    PrivateSE('rcse_09')
    sprite('null', 40)
    physicsYImpulse(25000)
    SetScaleXPerFrame(-8)
    SetScaleSpeedZ(-8)
    SetScaleSpeedY(1)
    PrivateSE('rcse_10')
    sprite('null', 10)
    CreateObject('BurstDD_Shasha', -1)
    sprite('null', 20)
    ConstantAlphaModifier(-13)
    SetScaleXPerFrame(-80)
    SetScaleSpeedZ(-80)


@State
def BurstDD_WindEffEx():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('rcef_430core')
        Eff3DEffect('rcef_440_trnado', '')
        SetScaleY(1600)
        SetScaleX(100)
        SetScaleZ(100)
        AddX(300000)
        AlphaValue(0)
    sprite('null', 10)
    CreateObject('BurstDD_WindThunderEff', -1)
    CreateObject('ModelMagicCircle1', -1)

    def RunOnObject_1():
        AddScale(1500)
        AddY(400000)
    ConstantAlphaModifier(18)
    SetScaleXPerFrame(115)
    SetScaleSpeedZ(115)
    PrivateSE('rcse_08')
    PrivateSE('rcse_09')
    PrivateSE('rcse_10')
    sprite('null', 10)
    ConstantAlphaModifier(0)
    PrivateSE('rcse_09')
    sprite('null', 40)
    physicsYImpulse(25000)
    SetScaleXPerFrame(-8)
    SetScaleSpeedZ(-8)
    SetScaleSpeedY(1)
    PrivateSE('rcse_10')
    sprite('null', 30)
    physicsYImpulse(0)
    sprite('null', 10)
    CreateObject('BurstDD_Shasha', -1)
    sprite('null', 20)
    ConstantAlphaModifier(-13)
    SetScaleXPerFrame(-80)
    SetScaleSpeedZ(-80)


@State
def BurstDD_WindThunderEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rcef_440_trnadothunder', '')
        SetScaleY(1600)
        SetScaleX(100)
        SetScaleZ(100)
    label(0)
    sprite('null', 2)
    AlphaValue(255)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)
    sprite('null', 3)
    AlphaValue(0)
    gotoLabel(0)


@State
def BurstDD_Shasha():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('rcef_440_shasha', '')
        RenderLayer(1)
        SetScaleX(2000)
    sprite('null', 35)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@Subroutine
def IvyBlossom_WindRate():
    ExternalForcesRate(100, 100)
    if SLOT_53 == 0:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 1:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 2:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 3:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 4:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 5:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 6:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 7:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 8:
        callSubroutine('IvyBlossom_WindRandom')
    if SLOT_53 == 9:
        callSubroutine('IvyBlossom_WindRandom')


@Subroutine
def IvyBlossom_WindRandom():
    if random_(2, 0, 33):
        SelfWind(80, 80, 80)
    elif random_(2, 0, 50):
        SelfWind(60, 60, 60)
    else:
        SelfWind(120, 120, 120)


@Subroutine
def IvyBlossom_Homing():
    if SLOT_53 == 0:
        Unknown23144(2, 0, 1, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 1:
        Unknown23144(2, 0, 2, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 2:
        Unknown23144(2, 0, 3, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 3:
        Unknown23144(2, 0, 4, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 4:
        Unknown23144(2, 0, 5, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 5:
        Unknown23144(2, 0, 6, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 6:
        Unknown23144(2, 0, 7, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 7:
        Unknown23144(2, 0, 8, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 8:
        Unknown23144(2, 0, 9, 0, 0, 0, 0, 0, 80, 0, 1)
    if SLOT_53 == 9:
        Unknown23144(2, 0, 10, 0, 0, 0, 0, 0, 80, 0, 1)


@Subroutine
def IvyBlossom_Homing2():
    if SLOT_53 == 0:
        Unknown23144(2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 1:
        Unknown23144(2, 0, 2, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 2:
        Unknown23144(2, 0, 3, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 3:
        Unknown23144(2, 0, 4, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 4:
        Unknown23144(2, 0, 5, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 5:
        Unknown23144(2, 0, 6, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 6:
        Unknown23144(2, 0, 7, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 7:
        Unknown23144(2, 0, 8, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 8:
        Unknown23144(2, 0, 9, 0, 0, 0, 0, 0, 1, 0, 1)
    if SLOT_53 == 9:
        Unknown23144(2, 0, 10, 0, 0, 0, 0, 0, 1, 0, 1)


@State
def rcef_414():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        WallCollisionDetection(1)
        NoDamageAction(1)
        BlendMode_Normal()
        PaletteIndex(0)
        SetZVal(-500)

        def upon_33():
            physicsXImpulse(2000)
            physicsYImpulse(16000)
            setGravity(1600)

        def upon_34():
            physicsXImpulse(2000)
            physicsYImpulse(16000)
            setGravity(1600)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_32():
            Unknown23090(23)

        def upon_36():
            AddActionMark(-1)
            if not SLOT_2:
                Unknown23090(23)

        def upon_35():
            IgnorePauses(3)
            Unknown23090(23)

        def upon_53():
            Unknown23090(23)

        def upon_54():
            if SLOT_51:
                sendToLabel(10)
            else:
                SLOT_51 = 1
        ExternalForcesRate(100, 100)
        SelfWind(100, 100, 0)
    sprite('vrrcef414_00', 32767)
    E0EAEffect('cmn_judgment', 65535)

    def RunOnObject_1():
        AbsoluteY(100000)
    CreateParticle('rcef_414', 0)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_414b', 0)

    def upon_LANDING():
        sendToLabel(2)
    label(2)
    sprite('vrrcef414_10', 5)
    EndMomentum(1)
    PerExternalForces(40)
    ExternalForcesRate(0, 0)
    SelfWind(0, 0, 0)
    AbsoluteY(0)
    CreateParticle('rcef_414box', 0)
    ParticleColorFromPalette(225, 226, 227)
    CallCustomizableParticle('rcef_414rose', 0)
    CommonSE('012_stab_fast')
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(9)
    if random_(2, 0, 10):
        conditionalSendToLabel(5)
    if random_(2, 0, 10):
        conditionalSendToLabel(6)
    sprite('vrrcef414_10b', 2)
    CreateParticle('rcef_414open', 0)
    SLOT_51 = 1
    sprite('vrrcef414_10c', 2)
    sprite('vrrcef414_11', 2)
    CreateObject('IvyBlossom_SE', 0)
    CreateObject('rcef_414_bat', 0)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 33)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 40)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 35)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 37)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 36)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 38)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 39)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 34)
    AddActionMark(1)
    sprite('vrrcef414_11', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 41)
    AddActionMark(1)
    sprite('vrrcef414_11', 32767)
    SetZVal(500)
    ExitState()
    label(5)
    sprite('vrrcef414_10b', 2)
    CreateParticle('rcef_414open', 0)
    SLOT_51 = 1
    sprite('vrrcef414_10c', 2)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('IvyBlossom_SE', 0)
    CreateObject('rcef_414_bat', 0)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 33)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 40)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 35)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 37)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 36)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 38)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 39)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 34)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 41)
    AddActionMark(1)
    sprite('vrrcef414_11ex00', 32767)
    SetZVal(500)
    ExitState()
    label(6)
    sprite('vrrcef414_10b', 2)
    CreateParticle('rcef_414open', 0)
    SLOT_51 = 1
    sprite('vrrcef414_10c', 2)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('IvyBlossom_SE', 0)
    CreateObject('rcef_414_bat', 0)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 33)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 40)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 34)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 37)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 36)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 38)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 39)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 34)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 2)
    CreateObject('rcef_414_bat', 0)
    ObjectUpon(STATE_END, 41)
    AddActionMark(1)
    sprite('vrrcef414_11ex01', 32767)
    SetZVal(500)
    ExitState()
    label(9)
    sprite('vrrcef414_10', 10)
    clearUponHandler(32)
    clearUponHandler(54)
    SLOT_11 = 0
    ConstantAlphaModifier(-25)
    ExitState()
    label(10)
    sprite('vrrcef414_11', 4)
    clearUponHandler(32)
    clearUponHandler(54)
    SLOT_11 = 0
    DespawnEAEffect('IvyBlossom_SE')
    sprite('vrrcef414_10c', 4)
    sprite('vrrcef414_10b', 4)
    sprite('vrrcef414_10', 38)
    sprite('vrrcef414_10', 20)
    ConstantAlphaModifier(-12)


@State
def rcef_414_test():
    sprite('vrrcef414_10', 20)
    AddX(200000)
    sprite('vrrcef414_10b', 4)
    sprite('vrrcef414_10c', 4)
    sprite('vrrcef414_11', 60)


@State
def rcef_414_bat():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        if SLOT_95:
            CreateObject('rcef_414_anm_2p', -1)
        else:
            CreateObject('rcef_414_anm', -1)
        SLOT_52 = 240
        SLOT_53 = 0
        Size(1200)

        def upon_33():
            Size(1200)
            SLOT_53 = 1

        def upon_34():
            Size(1200)
            SLOT_53 = 2

        def upon_35():
            Size(1200)
            SLOT_53 = 3

        def upon_36():
            Size(1200)
            SLOT_53 = 4

        def upon_37():
            Size(1025)
            SLOT_53 = 5

        def upon_38():
            Size(1025)
            SLOT_53 = 6

        def upon_39():
            Size(1025)
            SLOT_53 = 7

        def upon_40():
            Size(1025)
            SLOT_53 = 8

        def upon_41():
            Size(1025)
            SLOT_53 = 9

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_YDistanceFromFloor > 40000:
                    ObjectUpon24(23, 0, 22, 103)
                    if SLOT_0 < 150000:
                        if not SLOT_56:
                            SLOT_56 = 1
                            SLOT_11 = SLOT_11 + 1
                    elif SLOT_56:
                        SLOT_56 = 0
                        SLOT_11 = SLOT_11 + -1
                elif SLOT_56:
                    SLOT_56 = 0
                    SLOT_11 = SLOT_11 + -1
            if SLOT_56:
                PerExternalForces(92)
            CopyFromRightToLeft(23, 2, 54, 3, 2, 62)
            if SLOT_54:
                SLOT_51 = 1
                SLOT_57 = 40
                SLOT_52 = 240
                Unknown23144(0, 0, 103, 0, 0, 0, 0, 0, 0, 0, 0)
                XImpulseAcceleration(0)
                if SLOT_54 <= 15:
                    if SLOT_54 >= 1:
                        PerExternalForces(80)
                        YAccel(80)
                if SLOT_54 <= 1:
                    sendToLabel(0)
            elif SLOT_51:
                SLOT_57 = SLOT_57 + -1
                if not SLOT_57:
                    callSubroutine('IvyBlossom_Homing2')
            else:
                callSubroutine('IvyBlossom_Homing')
            if SLOT_YDistanceFromFloor < 30000:
                AbsoluteY(30000)
            SLOT_52 = SLOT_52 + -1
            if SLOT_52 <= 0:
                Unknown23090(23)

        def upon_14():
            NoAttackDuringAction(1)

        def upon_32():
            Unknown23090(23)

        def upon_53():
            Unknown23090(23)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            clearUponHandler(54)
            clearUponHandler(EVERY_FRAME)
            NoDamageAction(1)
            PerExternalForces(15)
            YAccel(15)
            XImpulseAcceleration(15)
            sendToLabel(9)
    label(0)
    sprite('vrrcef414_atk', 9)
    callSubroutine('IvyBlossom_WindRate')
    SLOT_55 = 120
    RefreshMultihit()
    label(1)
    sprite('vrrcef414_atk', 3)
    SLOT_2 = 1
    SLOT_55 = SLOT_55 + -1
    loopRest()
    if SLOT_55:
        conditionalSendToLabel(1)
    label(9)
    sprite('keep', 16)
    clearUponHandler(54)
    Unknown23144(0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_56:
        SLOT_11 = SLOT_11 + -1
    TriggerUponForState('rcef_414', 36)
    ConstantAlphaModifier(-15)
    AttackOff()


@State
def rcef_414_anm():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        BlendMode_Normal()
        PaletteIndex(5)
        RenderLayer(7)
        RemoveOnContact(2)

        def upon_33():
            if not SLOT_2:
                SLOT_2 = 1
                CharacterFlash(16711680, 30, 100)

        def upon_34():
            if SLOT_2:
                SLOT_2 = 0
                CharacterFlash(0, 20, 1)
    label(0)
    sprite('vrrcef414_20', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt', -1)
    sprite('vrrcef414_21', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt', -1)
    sprite('vrrcef414_22', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt', -1)
    sprite('vrrcef414_23', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt', -1)
    gotoLabel(0)


@State
def rcef_414_anm_2p():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        BlendMode_Normal()
        PaletteIndex(5)
        RenderLayer(7)
        RemoveOnContact(2)

        def upon_33():
            if not SLOT_2:
                SLOT_2 = 1
                CharacterFlash(9830600, 30, 100)

        def upon_34():
            if SLOT_2:
                SLOT_2 = 0
                CharacterFlash(0, 20, 1)
    label(0)
    sprite('vrrcef414_20_2p', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt_2p', -1)
    sprite('vrrcef414_21_2p', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt_2p', -1)
    sprite('vrrcef414_22_2p', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt_2p', -1)
    sprite('vrrcef414_23_2p', 4)
    ParticleLayer(6)
    CallCustomizableParticle('rcef_414bat_pt_2p', -1)
    gotoLabel(0)


@State
def IvyBlossom_EnergyDrain():

    def upon_IMMEDIATE():
        EffectPosition(22, 103)

        def upon_16():
            PrivateFunction3(22, 0, 0, 100, 1)
        E0EAEffectPosition(22)
        AddY(50000)
    label(1)
    sprite('null', 5)
    CreateParticle('rcef_414drain', -1)
    gotoLabel(1)


@State
def IvyBlossom_SE():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    label(1)
    sprite('null', 26)
    PrivateSE('rcse_27')
    gotoLabel(1)


@State
def Fade1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(0)
        AlphaValue(160)
        AbsoluteY(3000)
        SetZVal(-500)
        BlendMode_Normal()
    sprite('rc000_00', 15)
    ConstantAlphaModifier(-9)
    SetScaleSpeed(50)
    physicsYImpulse(-12000)
    sprite('rc000_00', 20)
    SetScaleSpeed(-130)
    physicsYImpulse(12000)
    sprite('rc000_00', 2)
    Size(0)


@State
def LightningObjAtkMini_Event2():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AttackDefaults_SpecialProjectile()
        BlendMode_Add()
        SetZVal(100)
        IgnoreScreenfreeze(1)
        HitsparkSize(500)
        SetScaleX(500)
        AlphaValue(200)
        TeleportToObject(22)
        AddX(-50000)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CommonSE('013_thunder_0')
    sprite('null', 2)
    sprite('vrrcef_lightning01', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)
    RotationAngle(0)
    SetScaleXPerFrame(-100)
    SetScaleX(750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-750)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)
    SetScaleX(-1000)
    SetScaleY(1000)
    CreateObject('LightningLandSub', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)
    CreateObject('LightningOption', -1)
    sprite('null', 2)
    CreateObject('LightningOption', -1)


@State
def EventShakeObj():
    sprite('null', 40)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    label(0)
    sprite('null', 8)
    ScreenShake(0, 5000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    loopRest()
    gotoLabel(0)
