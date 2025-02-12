@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_VH.DIG', 'ef_emb_VH_motion_000.mmot')
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
    sprite('null', 20)


@State
def EMB_VH_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_VH.DIG', 'ef_emb_VH_motion_000.mmot')
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
    sprite('null', 20)


@State
def EMB_VH_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_VH.DIG', 'ef_emb_VH_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 20)


@State
def WolfDamage():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        CallPrivateFunction('VH_Copy', 0, 0, 0, 0, 0, 0, 0, 0)
        IgnoreScreenfreeze(1)
    sprite('keep', 5)
    sprite('keep', 30)
    ConstantAlphaModifier(-15)
    BlendMode_Normal()


@State
def Camera():

    def upon_IMMEDIATE():
        E0EAEffectDirection(3)

        def upon_45():
            if CheckInput(0x79):
                XSpeed(4000)
            if CheckInput(0x93):
                YSpeed(4000)
            if CheckInput(0x5f):
                XSpeed(-4000)
            if CheckInput(0x45):
                YSpeed(-4000)
            if CheckInput(0xb):
                DeviationX(3800000, -3800000)
                DeviationY(200000, -200000)
                SLOT_106 = 500
            if CheckInput(INPUT_HOLD_C):
                SLOT_106 = SLOT_106 + 40
            if CheckInput(INPUT_HOLD_D):
                SLOT_106 = SLOT_106 + -40
            XImpulseAcceleration(80)
            YAccel(80)
            CameraNoScreenCollision(1)
            CameraNoCeiling(1)
            Unknown20008(1)
            EnableAfterimage(1)
            AfterimageBlendMode(2)
            AfterimageColor_1(200, 0, 0, 0)
            AfterimageColor_1(100, 0, 0, 0)
            AfterimageMask_1(0, 0, 255, 0)
            AfterimageMask_2(0, 0, 255, 0)
            AfterimageSize_1(1100)
            HUDVisibillity(1)
        CameraControlEnable(1)
        CameraFast(1)
    sprite('camera', 1200)
    NoDamageAction(1)
    Size(500)


@State
def Yugami():
    sprite('vr_yugami', 24)
    E0EAEffectPosition(22)
    Size(4000)
    SetScaleSpeed(-25)
    AddRotationPerFrame(200)
    ParticleTransparency(1)
    PlayerTransparency(800)
    Unknown3059(30)
    sprite('vr_yugami', 20)
    AddRotationPerFrame(700)
    Unknown3059(40)
    sprite('vr_yugami', 60)
    AddRotationPerFrame(1200)
    Unknown3059(50)
    sprite('vr_yugami', 60)
    SetScaleSpeed(-12)
    AddRotationPerFrame(100)
    Unknown3059(30)


@State
def DummyA():
    sprite('null', 1)
    CreateObject('AstralHeatBunshin9', -1)


@State
def AstralHeatBunshin1stJump():
    sprite('vh450_51', 3)
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    physicsYImpulse(10000)
    setGravity(-4000)
    EnableAfterimage(1)
    CommonSE('001_airbackdash_0')
    CommonSE('001_airbackdash_0')
    sprite('vh450_51add01', 2)
    sprite('vh450_51add01', 2)
    sprite('vh450_51add01', 2)
    sprite('vh450_51add02', 2)
    sprite('vh450_51add02', 2)
    sprite('vh450_51add02', 2)
    sprite('vh450_51add02', 2)
    sprite('vh450_51add02', 2)


@State
def AstralHeatBunshinBlackUpper():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(4)
        Damage(800)
        MinimumDamage(100)
        UseSlashHitspark(1)
        AirPushbackX(0)
        AirPushbackY(21000)
        YImpulseBeforeWallbounce(700)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        Hitstop(0)
        PushbackX(0)
        AirUntechableTime(300)
        DefeatOpponentBehavior(1)
    sprite('vh450_51add01', 6)
    EnableAfterimage(1)
    AfterimageColor_1(150, 70, 70, 70)
    AfterimageColor_2(60, 70, 70, 70)
    ColorForTransition(4283453520)
    TeleportToObject(22)
    AddY(-1000000)
    physicsYImpulse(180000)
    SetZVal(500)
    AttackOff()
    sprite('vh450_51add01', 80)
    RefreshMultihit()
    HitAnywhere(1)


@State
def AstralHeatMultiHitObj():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(4)
        Damage(900)
        MinimumDamage(100)
        DamageEffect(6, 'AstralHeatHitEffect')
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        Hitstop(0)
        PushbackX(0)
        AirUntechableTime(300)
        EnemyHitstopAddition(6, 6, 6)
        GroundedHitstunAnimation(17)
        DefeatOpponentBehavior(1)
        Visibility(1)
        Size(4000)
    sprite('camera', 4)
    AttackOff()
    sprite('camera', 8)
    TeleportToObject(22)
    AddY(230000)
    RefreshMultihit()
    AirHitstunAnimation(17)
    FlipOnHit(0)
    sprite('camera', 10)
    RefreshMultihit()
    AirHitstunAnimation(18)
    FlipOnHit(0)
    sprite('camera', 8)
    RefreshMultihit()
    AirHitstunAnimation(10)
    FlipOnHit(1)
    sprite('camera', 8)
    RefreshMultihit()
    AirHitstunAnimation(9)
    FlipOnHit(1)
    sprite('camera', 7)
    RefreshMultihit()
    AirHitstunAnimation(10)
    sprite('camera', 7)
    RefreshMultihit()
    AirHitstunAnimation(17)
    FlipOnHit(0)
    sprite('camera', 6)
    RefreshMultihit()
    AirHitstunAnimation(10)
    FlipOnHit(1)
    sprite('camera', 6)
    RefreshMultihit()
    AirHitstunAnimation(18)
    FlipOnHit(1)
    sprite('camera', 6)
    RefreshMultihit()
    AirHitstunAnimation(9)
    FlipOnHit(1)
    sprite('camera', 5)
    RefreshMultihit()
    AirHitstunAnimation(10)
    sprite('camera', 5)
    RefreshMultihit()
    AirHitstunAnimation(17)
    FlipOnHit(0)
    sprite('camera', 4)
    RefreshMultihit()
    AirHitstunAnimation(18)
    FlipOnHit(0)
    sprite('camera', 4)
    RefreshMultihit()
    AirHitstunAnimation(10)
    FlipOnHit(1)
    sprite('camera', 4)
    RefreshMultihit()
    AirHitstunAnimation(9)
    FlipOnHit(0)
    sprite('camera', 4)
    RefreshMultihit()
    AirHitstunAnimation(12)
    FlipOnHit(1)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(10)
    FlipOnHit(0)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(18)
    FlipOnHit(0)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(17)
    FlipOnHit(1)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(12)
    FlipOnHit(1)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(9)
    FlipOnHit(1)
    sprite('camera', 3)
    RefreshMultihit()
    AirHitstunAnimation(9)
    FlipOnHit(1)
    Hitstop(100)


@State
def AstralDummyKillObj():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        HitAnywhere(1)
        AttackLevel_(4)
        Damage(6000)
        MinimumDamage(100)
        AirPushbackY(0)
        Hitstop(0)
        DefeatOpponentBehavior(3)
        PushbackX(0)
        AirPushbackX(0)
        YImpulseBeforeWallbounce(0)
        DamageEffect(5, 'AstralHeatHitEffect')
        DefeatOpponentBehavior(3)
        Visibility(1)
    sprite('camera', 200)


@State
def AstralCamera():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_35():
            sendToLabel(3)

        def upon_36():
            sendToLabel(4)

        def upon_37():
            sendToLabel(5)

        def upon_38():
            SLOT_51 = 2

        def upon_39():
            sendToLabel(7)

        def upon_40():
            sendToLabel(8)

        def upon_45():
            if SLOT_51 == 1:

                def RunOnObject_22():
                    ColorForTransition(4282400832)
            if SLOT_51 == 2:

                def RunOnObject_22():
                    ColorForTransition(4278190080)
    label(1)
    sprite('camera', 50)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    HUDVisibillity(1)

    def upon_EVERY_FRAME():
        TeleportToObject(22)
        AbsoluteY(200000)
    sprite('camera', 32767)
    loopRest()
    label(2)
    clearUponHandler(EVERY_FRAME)
    sprite('camera', 32767)

    def RunOnObject_22():
        setGravity(0)
        physicsXImpulse(-50)
        physicsYImpulse(400)
        AddY(100)
        EnableAfterimage(1)
    loopRest()
    label(3)
    clearUponHandler(EVERY_FRAME)
    sprite('camera', 10)
    CameraFast(1)

    def RunOnObject_22():
        physicsXImpulse(0)
        physicsYImpulse(100000)
        Unknown23178(0)
    physicsYImpulse(70000)
    setGravity(0)
    sprite('camera', 6)
    sprite('camera', 1)
    YAccel(90)
    setGravity(0)
    sprite('camera', 1)
    YAccel(90)
    sprite('camera', 1)
    YAccel(80)
    sprite('camera', 1)
    YAccel(80)
    sprite('camera', 1)
    YAccel(75)
    sprite('camera', 1)
    YAccel(70)
    sprite('camera', 1)
    sprite('camera', 10)
    CreateObject('Fade2', -1)
    EndMomentum(1)
    sprite('camera', 20)
    TeleportToObject(3)
    AbsoluteY(200000)
    sprite('camera', 10)
    AbsoluteY(200000)
    EndMomentum(1)
    sprite('camera', 32767)
    loopRest()
    label(4)
    clearUponHandler(EVERY_FRAME)
    sprite('camera', 7)
    E0EAEffectPosition(0)
    physicsYImpulse(80000)
    setGravity(-4500)
    CameraFast(1)
    CameraPosition(1000)
    clearUponHandler(EVERY_FRAME)

    def RunOnObject_22():
        EndMomentum(1)
        AbsoluteY(38000000)
        AddY(-600000)
        Unknown23178(0)
    SLOT_51 = 1
    loopRest()
    sprite('camera', 11)
    sprite('camera', 30)
    setGravity(-7500)
    sprite('camera', 32767)
    label(8)
    sprite('camera', 8)
    CreateObject('Fade5', -1)
    sprite('camera', 32767)
    EndMomentum(1)

    def RunOnObject_22():
        AbsoluteY(38000000)
        AddY(-300000)
        physicsYImpulse(7000)
        setGravity(0)
        XPositionRelativeFacing(0)

    def RunOnObject_3():
        XPositionRelativeFacing(0)
    TeleportToObject(22)
    AddY(200000)
    E0EAEffectPosition(22)
    CameraPosition(4000)
    label(7)
    sprite('camera', 4)
    CreateObject('Fade5', -1)
    sprite('camera', 80)
    CameraPosition(1000)
    E0EAEffectPosition(0)
    EndMomentum(1)
    AbsoluteY(39000000)
    AddY(-250000)
    physicsYImpulse(10000)
    setGravity(125)

    def RunOnObject_22():
        AbsoluteY(39000000)
        AddY(-700000)
        physicsYImpulse(12000)
        setGravity(125)
    sprite('camera', 4)
    EndMomentum(1)
    sprite('camera', 10)
    sprite('camera', 4)
    sprite('camera', 32767)
    label(5)
    clearUponHandler(EVERY_FRAME)
    sprite('camera', 3)
    E0EAEffectPosition(0)
    TeleportToObject(3)
    AddY(200000)
    E0EAEffectPosition(3)
    CameraNoCeiling(0)
    sprite('camera', 32767)
    CameraFast(0)


@State
def Fade1():
    sprite('vr_fade', 8)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(1)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('vr_fade', 2)
    sprite('vr_fade', 8)
    ConstantAlphaModifier(-32)


@State
def Fade2():
    sprite('vr_fade', 10)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(1)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('vr_fade', 10)
    sprite('vr_fade', 10)
    ConstantAlphaModifier(-32)


@State
def Fade3():
    sprite('vr_fade', 4)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(1)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4280287296)
    AlphaValue(0)
    ConstantAlphaModifier(65)
    sprite('vr_fade', 4)
    sprite('vr_fade', 4)
    ConstantAlphaModifier(-65)


@State
def Fade4():
    sprite('vr_fade', 4)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(2)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4294901760)
    AlphaValue(0)
    ConstantAlphaModifier(65)
    sprite('vr_fade', 200)
    sprite('vr_fade', 4)
    ConstantAlphaModifier(-65)


@State
def Fade5():
    sprite('null', 10)
    CreateObject('Fade5Sub', -1)
    CreateObject('Fade5Sub', -1)
    ObjectUpon(STATE_END, 32)
    CreateObject('Fade5Sub', -1)
    ObjectUpon(STATE_END, 33)


@State
def Fade5Sub():

    def upon_IMMEDIATE():
        FaceRight()
        BlendMode_Normal()
        RenderLayer(1)
        XPositionRelativeFacing(640000)
        AbsoluteY(1768000)
        ScreenPosition(1)
        ColorForTransition(4278190080)
        Size(2500)
        SetScaleY(5500)
        physicsYImpulse(-250000)

        def upon_32():
            AddX(426666)

        def upon_33():
            AddX(-426666)
    sprite('vr_shadow', 100)


@State
def WolfHairColorA():
    sprite('null', 1)
    ParticleColorFromPalette(48, 48, 48)
    CallCustomizableParticle('vhef_form_ex_off_dust', -1)


@State
def WolfHairColorB():
    sprite('null', 1)
    ParticleColorFromPalette(52, 52, 52)
    CallCustomizableParticle('vhef_form_ex_off_dust', -1)


@State
def vhef_attack_c():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(50, 50, 50)
    CallCustomizableParticle('vhef_attack_c', -1)


@State
def vhef_hit():
    sprite('null', 1)
    ParticleDeviation(15000, 75000)
    CallCustomizableParticle('vhef_hit', -1)
    CommonSE('020_blood_1')


@State
def vhef_hit_mini():
    sprite('null', 1)
    ParticleDeviation(15000, 75000)
    ParticleSize(500)
    CallCustomizableParticle('vhef_hit', -1)
    CommonSE('101_hit_slash_0')
    CommonSE('020_blood_1')


@State
def vh202LegEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef202_04', 2)
    AddX(-120000)
    AlphaValue(255)
    sprite('vrvhef202_04', 2)
    ConstantAlphaModifier(-20)
    sprite('vrvhef202_05', 4)


@State
def vh211ArmEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef211_08', 3)
    AddX(-70000)
    AlphaValue(255)
    sprite('vrvhef211_09', 3)
    ConstantAlphaModifier(-30)
    sprite('vrvhef211_10', 5)
    CreateObject('vhef_form_dust', 0)
    CreateObject('vhef_form_dust', 1)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)


@State
def vh212LegEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef212_06', 2)
    E0EAEffectPosition(3)
    AlphaValue(255)
    sprite('vrvhef212_07', 3)
    sprite('vrvhef212_08', 2)
    E0EAEffectPosition(0)
    sprite('vrvhef212_13', 3)
    CreateObject('vhef_form_dust', 0)
    CreateObject('vhef_form_dust', 1)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)
    ConstantAlphaModifier(-25)


@State
def vhef_213():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(128000)
    sprite('vrvhef213_00', 3)
    AlphaValue(96)
    CreateParticle('vh213', -1)
    sprite('vrvhef213_01', 3)
    sprite('vrvhef213_02', 3)
    ConstantAlphaModifier(-32)


@State
def vh232LegEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef232_05', 3)
    AddX(40000)
    AlphaValue(255)
    sprite('vrvhef232_06', 3)
    ConstantAlphaModifier(-25)
    sprite('vrvhef232_07', 5)
    CreateObject('vhef_form_dust', 0)
    CreateObject('vhef_form_dust', 1)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)


@State
def vh234LegEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef234_05', 3)
    AlphaValue(255)
    sprite('vrvhef234_06', 3)
    ConstantAlphaModifier(-25)
    sprite('vrvhef234_06', 4)
    AddX(-20000)
    CreateObject('vhef_form_dust', 0)
    CreateObject('vhef_form_dust', 1)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)


@State
def vh252LegEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
    sprite('vrvhef252_04', 3)
    E0EAEffectPosition(3)
    AlphaValue(255)
    sprite('vrvhef252_04', 1)
    E0EAEffectPosition(0)
    sprite('vrvhef252_05', 2)
    ConstantAlphaModifier(-30)
    sprite('vrvhef252_05', 3)
    CreateObject('vhef_form_dust', 0)
    CreateObject('vhef_form_dust', 1)
    CreateObject('vhef_form_dust', 2)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)
    CreateObject('vhef_form_dustlight', 2)


@State
def vw252LegEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(100)
    sprite('vrvwef252_00', 3)
    E0EAEffectPosition(3)
    AlphaValue(255)
    sprite('vrvwef252_01', 1)
    E0EAEffectPosition(0)
    sprite('vrvwef252_01', 3)
    ConstantAlphaModifier(-30)
    CreateObject('vhef_form_dustlight', 0)
    CreateObject('vhef_form_dustlight', 1)
    CreateObject('vhef_form_dustlight', 2)


@State
def vhef_form_dust():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(52, 52, 53)
    CallCustomizableParticle('vhef_form_dust', -1)


@State
def vhef_form_dustlight():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(241, 240, 241)
    CallCustomizableParticle('vhef_form_off', -1)


@State
def DriveForm():

    def upon_IMMEDIATE():
        LinkParticle('vhef_form_ex_a')
        BlendMode_Add()
        Size(1200)
    sprite('null', 45)
    CreateObject('FormDust', -1)
    CreateObject('FormDust_b', -1)
    CreateObject('FormCircle', -1)
    CreateObject('FormOffMoya_front', -1)
    CreateParticle('vhef_form_ex02', -1)


@State
def FormDust():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(48, 48, 48)
    CallCustomizableParticle('vhef_form_ex_dust', -1)


@State
def FormDust_b():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(50, 50, 50)
    CallCustomizableParticle('vhef_form_ex_dust', -1)


@State
def FormCircle():
    sprite('null', 1)
    Visibility(1)
    PaletteIndex(1)
    ParticleColorFromPalette(241, 240, 241)
    CallCustomizableParticle('vhef_form_ex', -1)


@State
def vhef_form_ex():
    sprite('null', 1)
    Visibility(1)
    PaletteIndex(1)
    ParticleColorFromPalette(241, 240, 241)
    CallCustomizableParticle('vhef_form_ex01', -1)


@State
def vhef_form_ex_dust():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(48, 48, 48)
    CallCustomizableParticle('vhef_form_ex_dust', -1)


@State
def vhef_form_ex_dust_b():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(50, 50, 50)
    CallCustomizableParticle('vhef_form_ex_dust', -1)


@State
def vhef_form_ex_round():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(52, 52, 52)
    CallCustomizableParticle('vhef_form_ex_round', -1)


@State
def DriveFormOff():

    def upon_IMMEDIATE():
        LinkParticle('vhef_form_ex_a')
        BlendMode_Add()
    sprite('null', 45)
    CreateObject('FormOffMoya_back', -1)
    CreateObject('FormOffMoya_front', -1)
    CreateObject('FormOffCircle', -1)
    CreateParticle('vhef_form_ex02', -1)


@State
def FormOffCircle():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        ParticleColorFromPalette(241, 240, 241)
        CallPrivateEffect('vhef_form_ex01')
        BlendMode_Add()
        Size(850)
    sprite('null', 45)
    Visibility(1)


@State
def FormOffMoya():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(1200)
    sprite('null', 15)
    ParticleLayer(1)
    CallPrivateEffect('vhef_driveform_moya')
    sprite('null', 5)
    ConstantAlphaModifier(-50)
    sprite('null', 1)
    AlphaValue(0)


@State
def FormOffMoya_front():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AddY(85000)
    sprite('null', 15)
    AlphaValue(200)
    ParticleLayer(1)
    CallPrivateEffect('vhef_driveform_moyafront')
    sprite('null', 8)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def FormOffMoya_back():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AddY(120000)
        Size(600)
    sprite('null', 30)
    ParticleLayer(2)
    CallPrivateEffect('vhef_driveform_moyaback')
    AlphaValue(120)
    sprite('null', 6)
    ConstantAlphaModifier(-20)
    sprite('null', 1)
    AlphaValue(0)


@State
def Form_Air():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdrivelform')
    sprite('null', 60)
    AddY(90000)
    Visibility(1)


@State
def FormOff_Air():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        ParticleColorFromPalette(241, 240, 241)
        CallPrivateEffect('vhef_airform_ex00')
        AddY(90000)
    sprite('null', 40)
    Visibility(1)


@State
def vhef431_form_ex_dust():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        ParticleColorFromPalette(48, 48, 48)
        CallPrivateEffect('vhef_form_ex_off_dust')
        BlendMode_Normal()
    sprite('null', 5)
    AlphaValue(30)
    ConstantAlphaModifier(40)
    physicsYImpulse(8000)
    sprite('null', 12)
    physicsYImpulse(12000)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def vh400_tossin():

    def upon_IMMEDIATE():
        LinkParticle('vhef_400attack')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        Size(1400)
        uponSendToLabel(32, 60)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    AlphaValue(255)
    sprite('null', 7)
    sprite('null', 10)
    ConstantAlphaModifier(-20)
    loopRest()
    ExitState()
    label(60)
    sprite('null', 1)
    CreateObject('vh400_kakusan', -1)


@State
def vh400_kakusan():

    def upon_IMMEDIATE():
        LinkParticle('vh400_kakusan')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(1300)
    sprite('null', 20)


@State
def vh400_step():

    def upon_IMMEDIATE():
        LinkParticle('vhef_400step')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(800)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 10)
    AlphaValue(255)
    sprite('null', 5)
    ConstantAlphaModifier(-35)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh403_syogeki():

    def upon_IMMEDIATE():
        LinkParticle('vh403_syogeki')
        BlendMode_Add()
        Size(1000)
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('vh403_ring2', 1)
    sprite('null', 4)
    CreateObject('vh403_ring1', 0)
    sprite('null', 12)


@State
def vh403_ring1():

    def upon_IMMEDIATE():
        LinkParticle('vh403_ring')
        BlendMode_Add()
        Size(500)
    sprite('null', 40)
    AddX(80000)
    AddY(80000)


@State
def vh403_ring2():

    def upon_IMMEDIATE():
        LinkParticle('vh403_ring')
        BlendMode_Add()
        Size(800)
    sprite('null', 40)


@State
def ef_airdashf6C4C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
    sprite('null', 20)


@State
def ef_airdashf8C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
        RotationAngle(270000)
    sprite('null', 20)


@State
def ef_airdashf2C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
        RotationAngle(90000)
    sprite('null', 20)


@State
def ef_airdashf9C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
        RotationAngle(320000)
    sprite('null', 20)


@State
def ef_airdashf3C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
        RotationAngle(50000)
    sprite('null', 20)


@State
def ef_airdashf1C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_airdashf')
        BlendMode_Add()
        RotationAngle(120000)
    sprite('null', 20)


@State
def vw202_tossin():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw202_tossin8C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
        RotationAngle(270000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw202_tossin2C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
        RotationAngle(90000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw202_tossin9C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
        RotationAngle(320000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw202_tossin3C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
        RotationAngle(50000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw202_tossin1C():

    def upon_IMMEDIATE():
        LinkParticle('vhef_vw202tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(800)
        RotationAngle(120000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw400_tame():

    def upon_IMMEDIATE():
        LinkParticle('vw400_tame')
        BlendMode_Add()
    sprite('null', 30)


@State
def vw400_tossin_dust():

    def upon_IMMEDIATE():
        LinkParticle('vw400_tossin_dust')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AddX(-50000)
        AlphaValue(0)
        uponSendToLabel(32, 80)

        def upon_33():
            RotationAngle(320000)

        def upon_34():
            RotationAngle(45000)

        def upon_35():
            RotationAngle(60000)

        def upon_36():
            RotationAngle(270000)

        def upon_37():
            RotationAngle(90000)
    sprite('null', 4)
    ConstantAlphaModifier(30)
    sprite('null', 24)
    ConstantAlphaModifier(0)
    AlphaValue(120)
    label(80)
    sprite('null', 14)
    clearUponHandler(32)
    ConstantAlphaModifier(-35)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw400_tossin_line():

    def upon_IMMEDIATE():
        LinkParticle('vw400_tossin_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AlphaValue(0)
        uponSendToLabel(32, 80)

        def upon_33():
            RotationAngle(320000)

        def upon_34():
            RotationAngle(45000)

        def upon_35():
            RotationAngle(60000)

        def upon_36():
            RotationAngle(270000)

        def upon_37():
            RotationAngle(90000)
    sprite('null', 4)
    ConstantAlphaModifier(30)
    sprite('null', 28)
    ConstantAlphaModifier(0)
    AlphaValue(160)
    label(80)
    sprite('null', 18)
    clearUponHandler(32)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw401_tossin():

    def upon_IMMEDIATE():
        LinkParticle('vw400_2tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AlphaValue(0)
        uponSendToLabel(32, 80)

        def upon_33():
            RotationAngle(320000)

        def upon_34():
            RotationAngle(45000)

        def upon_35():
            RotationAngle(60000)
            AddX(-10000)

        def upon_36():
            RotationAngle(270000)

        def upon_37():
            RotationAngle(90000)
    sprite('null', 2)
    ConstantAlphaModifier(50)
    sprite('null', 8)
    AlphaValue(255)
    label(80)
    sprite('null', 20)
    clearUponHandler(32)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw401_Rasen():

    def upon_IMMEDIATE():
        Eff3DEffect('vhef_screw.DIG', 'vhef_screw_motion_000.mmot')
        E0EAEffectPosition(3)
        FaceSpawnLocation()
        BlendMode_Add()
        Size(600)
        AddX(-180000)
        AlphaValue(0)
        uponSendToLabel(32, 80)

        def upon_33():
            RotationAngle(320000)
            AddX(30000)
            AddY(-140000)

        def upon_34():
            AddX(120000)
            AddY(80000)
            RotationAngle(45000)

        def upon_35():
            RotationAngle(60000)
            AddX(50000)
            AddY(160000)

        def upon_36():
            RotationAngle(270000)
            AddX(200000)
            AddY(-150000)

        def upon_37():
            RotationAngle(90000)
            AddX(200000)
            AddY(150000)
    sprite('null', 4)
    ConstantAlphaModifier(30)
    sprite('null', 10)
    ConstantAlphaModifier(0)
    AlphaValue(160)
    label(80)
    sprite('null', 8)
    clearUponHandler(32)
    ConstantAlphaModifier(-45)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw401_line():

    def upon_IMMEDIATE():
        LinkParticle('vw400_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AlphaValue(0)
        uponSendToLabel(32, 81)

        def upon_33():
            RotationAngle(320000)

        def upon_34():
            RotationAngle(45000)

        def upon_35():
            RotationAngle(60000)
            AddX(-50000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 4)
    AlphaValue(255)
    label(81)
    sprite('null', 10)
    clearUponHandler(32)
    ConstantAlphaModifier(-35)
    sprite('null', 1)
    AlphaValue(0)


@State
def Sukuryu():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)

        def upon_32():
            RotationAngle(0)
            AddX(200000)
            AddY(200000)

        def upon_33():
            RotationAngle(320000)
            AddX(72000)
            AddY(283000)

        def upon_34():
            RotationAngle(45000)
            AddX(81000)
            AddY(167000)

        def upon_35():
            RotationAngle(60000)
            AddX(43000)
            AddY(127000)

        def upon_37():
            RotationAngle(340000)
            AddX(72000)
            AddY(263000)

        def upon_38():
            RotationAngle(0)
            AddX(200000)
            AddY(50000)

        def upon_39():
            RotationAngle(270000)
            AddY(300000)

        def upon_40():
            RotationAngle(90000)
            AddY(100000)

        def upon_36():
            EndObject()
    label(81)
    sprite('vw204_00', 1)
    sprite('vw204_01', 1)
    sprite('vw204_02', 1)
    loopRest()
    gotoLabel(81)


@State
def vwef_hit_kiba():

    def upon_IMMEDIATE():
        LinkParticle('vwef_hit_kiba')
        BlendMode_Add()
        Size(800)
        CommonSE('101_hit_slash_2')
        CommonSE('020_blood_1')
    sprite('null', 40)


@State
def vwef_hit_kiba_mini():

    def upon_IMMEDIATE():
        LinkParticle('vwef_hit_kiba')
        BlendMode_Add()
        Size(600)
        CommonSE('101_hit_slash_0')
        CommonSE('020_blood_1')
    sprite('null', 40)


@State
def vw402_kamituki():

    def upon_IMMEDIATE():
        LinkParticle('vw402_kamituki')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1100)
    sprite('null', 40)


@State
def vw402_keri():

    def upon_IMMEDIATE():
        LinkParticle('vw402_keri')
        BlendMode_Add()
        Size(1000)
    sprite('null', 30)


@State
def vh431_jumpkick():

    def upon_IMMEDIATE():
        LinkParticle('vh431_jumpkick')
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        uponSendToLabel(32, 70)
        Size(1000)
    sprite('null', 3)
    E0EAEffectPosition(3)
    ConstantAlphaModifier(100)
    sprite('null', 20)
    AlphaValue(255)
    label(70)
    sprite('null', 3)
    E0EAEffectPosition(0)
    AddX(-140000)
    ConstantAlphaModifier(-90)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw431_tossin():

    def upon_IMMEDIATE():
        LinkParticle('vw431_tossin')
        BlendMode_Add()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(1400)
        AlphaValue(0)
        RotationAngle(320000)
        uponSendToLabel(32, 71)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 26)
    AlphaValue(255)
    label(71)
    sprite('null', 14)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw431_tame():

    def upon_IMMEDIATE():
        LinkParticle('vw431_tame')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1100)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 37)
    AlphaValue(255)
    sprite('null', 8)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def vw431_line9():

    def upon_IMMEDIATE():
        LinkParticle('vw400_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1200)
        AlphaValue(0)
        RotationAngle(320000)
        uponSendToLabel(32, 72)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 26)
    AlphaValue(255)
    label(72)
    sprite('null', 14)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh431_syougeki():

    def upon_IMMEDIATE():
        BlendMode_Add()
    sprite('null', 30)


@State
def vh431_hit_kiba1():

    def upon_IMMEDIATE():
        LinkParticle('vh431_hit_kiba1')
        BlendMode_Add()
        AddX(420000)
        AddY(240000)
        RotationAngle(-55000)
        Size(1500)
    sprite('null', 40)


@State
def vh431_hit_kiba2():

    def upon_IMMEDIATE():
        LinkParticle('vh431_hit_kiba2')
        BlendMode_Add()
        AddX(420000)
        AddY(240000)
        RotationAngle(-35000)
        Size(1500)
    sprite('null', 40)


@State
def vh431_hit():

    def upon_IMMEDIATE():
        LinkParticle('vh431_hit')
        BlendMode_Add()
        AddX(420000)
        AddY(240000)
        RotationAngle(-55000)
        Size(1500)
    sprite('null', 50)


@State
def vh430Hit():

    def upon_IMMEDIATE():
        LinkParticle('vhef_430hit')
    sprite('null', 60)
    Size(2400)
    AddY(50000)
    AddX(50000)
    CommonSE('101_hit_slash_1')
    RotationAngle(-105000)


@State
def vhef_hit_vh430():
    sprite('null', 3)
    CommonSE('101_hit_slash_1')
    sprite('null', 60)
    CreateObject('vh430Hit', -1)


@State
def vh450_kakato_kick2():

    def upon_IMMEDIATE():
        LinkParticle('vh450_kakato_kick2')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1500)
        RotationAngle(-25000)
    sprite('null', 30)


@State
def vh450_kakato_kickef1():

    def upon_IMMEDIATE():
        LinkParticle('vh450_kakato_kickef')
        BlendMode_Add()
        Size(700)
    sprite('null', 30)


@State
def vh450_kakato_kickef2():

    def upon_IMMEDIATE():
        LinkParticle('vh450_kakato_kickef')
        BlendMode_Add()
        Size(850)
    sprite('null', 30)


@State
def vh450_kakato_kickef3():

    def upon_IMMEDIATE():
        LinkParticle('vh450_kakato_kickef')
        BlendMode_Add()
        Size(900)
    sprite('null', 30)


@State
def vh450_tame():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('vh450_tame')
        BlendMode_Add()
        Size(900)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 38)
    AlphaValue(255)
    sprite('null', 6)
    ConstantAlphaModifier(-45)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh450_moya1():

    def upon_IMMEDIATE():
        LinkParticle('vh450_moya1')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1500)
        uponSendToLabel(32, 82)
    sprite('null', 75)
    label(82)
    sprite('null', 5)
    ConstantAlphaModifier(-50)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh450_moya2():

    def upon_IMMEDIATE():
        LinkParticle('vh450_moya2')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(850)
    sprite('null', 95)


@State
def vh450_moya3():

    def upon_IMMEDIATE():
        LinkParticle('vh450_moya3')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1200)
    sprite('null', 40)


@State
def vh450_moya5():

    def upon_IMMEDIATE():
        LinkParticle('vh450_moya1')
        BlendMode_Add()
        E0EAEffectPosition(2)
        Size(1500)
        uponSendToLabel(32, 82)
    sprite('null', 75)
    label(82)
    sprite('null', 5)
    ConstantAlphaModifier(-50)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh450_moya4():

    def upon_IMMEDIATE():
        LinkParticle('vh450_moya4')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
    sprite('null', 40)


@State
def vh450_howling1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('vh450_howling1')
        BlendMode_Add()
        Size(560)
    sprite('null', 30)


@State
def vh450_howling2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('vh450_howling2')
        BlendMode_Add()
        Size(1000)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 37)
    AlphaValue(255)
    sprite('null', 6)
    ConstantAlphaModifier(-45)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh450_jump():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('vh450_jump')
        BlendMode_Add()
        Size(900)
    sprite('null', 30)
    sprite('null', 60)
    Size(2400)
    AddY(50000)
    AddX(50000)
    CommonSE('101_hit_slash_1')
    RotationAngle(-105000)


@State
def AstralHeatBunshin9():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        RenderLayer(2)
        physicsXImpulse(-40000)
        physicsYImpulse(10000)
        AddX(120000)
        AddY(-30000)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add01', 1)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_37', 1)
    sprite('vh450_37', 1)
    sprite('vh450_37', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_37', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add02', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)


@State
def AstralHeatBunshin3():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        physicsXImpulse(-18000)
        physicsYImpulse(-48000)
        AddX(30000)
        AddY(120000)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add01', 1)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_39', 1)
    sprite('vh450_39', 1)
    sprite('vh450_39', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_39', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add02', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)


@State
def AstralHeatBunshin1():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        physicsXImpulse(50000)
        physicsYImpulse(-18000)
        AddX(-90000)
        AddY(22500)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add01', 1)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_40', 1)
    sprite('vh450_40', 1)
    sprite('vh450_40', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_40', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add02', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)


@State
def AstralHeatBunshin7():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        RenderLayer(2)
        physicsXImpulse(14000)
        physicsYImpulse(40000)
        AddX(-30000)
        AddY(-120000)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add01', 1)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_38', 1)
    sprite('vh450_38', 1)
    sprite('vh450_38', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_38', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add02', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)


@State
def AstralHeatBunshin9short():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        RenderLayer(2)
        physicsXImpulse(-60000)
        physicsYImpulse(20000)
        AddX(135000)
        AddY(-45000)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_37', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_37', 1)
    sprite('vh450_37', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_37', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_37add02', 1)
    sprite('vh450_37add02', 1)


@State
def AstralHeatBunshin3short():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        RenderLayer(2)
        physicsXImpulse(-18000)
        physicsYImpulse(-72000)
        AddX(40500)
        AddY(135000)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_39', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_39', 1)
    sprite('vh450_39', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_39', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_39add02', 1)
    sprite('vh450_39add02', 1)


@State
def AstralHeatBunshin1short():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        ColorForTransition(3369259730)
        AlphaValue(0)
        physicsXImpulse(54000)
        physicsYImpulse(-18000)
        AddX(-90000)
        AddY(22500)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_40', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_40', 1)
    sprite('vh450_40', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_40', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_40add02', 1)
    sprite('vh450_40add02', 1)


@State
def AstralHeatBunshin7short():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AfterimageColor_1(100, 255, 255, 255)
        AfterimageColor_1(50, 255, 255, 255)
        BlendMode_Normal()
        ConstantAlphaModifier(30)
        AlphaValue(0)
        ColorForTransition(3369259730)
        RenderLayer(2)
        physicsXImpulse(14000)
        physicsYImpulse(40000)
        AddX(-30000)
        AddY(-120000)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add01', 1)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vh450_38', 1)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('vh450_38', 1)
    sprite('vh450_38', 1)
    sprite('vh450_38', 1)
    XImpulseAcceleration(230)
    YAccel(230)
    sprite('vh450_38', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    ConstantAlphaModifier(-40)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add01', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add02', 1)
    XImpulseAcceleration(140)
    YAccel(140)
    sprite('vh450_38add02', 1)
    sprite('vh450_38add02', 1)


@State
def AstralHeatHitEffect():
    sprite('null', 1)
    CommonSE('101_hit_slash_2')
    CreateObject('AstralHeatHitEffect_Blood', -1)
    ParticleDeviation(15000, 270000)
    ParticleLayer(2)
    CallCustomizableParticle('vhef_430hit_rip1b', 0)


@State
def AstralHeatHitEffect_Blood():
    sprite('null', 1)
    CommonSE('020_blood_1')
    ParticleDeviation(15000, 75000)
    ParticleLayer(1)
    CallCustomizableParticle('vhef_astralhit_flash', 0)


@State
def vh_AH_ray():

    def upon_IMMEDIATE():
        ParticleLayer(1)
        CallPrivateEffect('vhef_astralspeedline_bk')
    sprite('null', 120)


@State
def vh450_tsume():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(255)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageCount(2)
        AfterimageMask_1(0, 255, 255, 255)
        AfterimageMask_2(0, 255, 255, 255)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
        AddY(900000)
        SetScaleX(900)
        SetScaleY(1200)
        FaceRight()
    sprite('vrvhef450_00', 10)
    physicsYImpulse(-2000)
    sprite('vrvhef450_00', 16)
    physicsYImpulse(-5000)
    sprite('vrvhef450_00', 1)
    CommonSE('101_hit_slash_3')
    CommonSE('101_hit_slash_3')
    PrivateSE('vhse_11')
    PrivateSE('vhse_10')
    CreateObject('vh450_claw', 0)
    CreateObject('vh450_claw', 1)
    CreateObject('vh450_claw', 2)
    CreateObject('vh450_claw', 3)
    physicsYImpulse(-280000)
    sprite('vrvhef450_00', 2)
    ScreenShake(0, 75000)
    YAccel(75)
    sprite('vrvhef450_00', 2)
    CreateObject('vh450_claw', 4)
    CreateObject('vh450_claw', 5)
    CreateObject('vh450_claw', 6)
    CreateObject('vh450_claw', 7)
    YAccel(40)
    sprite('vrvhef450_00', 2)
    YAccel(10)
    sprite('vrvhef450_00', 32)
    YAccel(5)
    sprite('vrvhef450_00', 12)
    CreateObject('vh450_tsume01', -1)
    sprite('vrvhef450_00', 12)
    CreateObject('vh450_tsume02', -1)
    sprite('vrvhef450_00', 12)
    CreateObject('vh450_tsume03', -1)
    sprite('vrvhef450_00', 12)
    CreateObject('vh450_tsume04', -1)
    sprite('vrvhef450_00', 1)
    CreateObject('WhiteBlood', -1)
    CreateObject('WhiteBlood3D1', -1)
    CreateObject('WhiteBlood3D2', -1)


@State
def vh450_tsume01():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(255)
        PaletteIndex(1)
        AddY(450000)
        AddX(600000)
        SetScaleX(1200)
        SetScaleY(1200)
        RotationAngle(60000)
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageCount(2)
        AfterimageMask_1(0, 255, 255, 255)
        AfterimageMask_2(0, 255, 255, 255)
        AfterimageSize_1(1060)
        AfterimageSize_2(10000)
    sprite('vrvhef450_01', 2)
    CommonSE('101_hit_slash_3')
    CommonSE('101_hit_slash_3')
    PrivateSE('vhse_11')
    PrivateSE('vhse_10')
    CreateObject('vh450_claw02', 0)
    CreateObject('vh450_claw02', 1)
    CreateObject('vh450_claw02', 2)
    CreateObject('vh450_claw02', 3)
    physicsXImpulse(-90000)
    physicsYImpulse(-60000)
    sprite('vrvhef450_01', 6)
    ScreenShake(50000, 50000)
    CreateObject('vh450_claw02', 4)
    CreateObject('vh450_claw02', 5)
    CreateObject('vh450_claw02', 6)
    CreateObject('vh450_claw02', 7)
    sprite('vrvhef450_01', 1)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('vrvhef450_01', 2)
    YAccel(30)
    XImpulseAcceleration(30)
    sprite('vrvhef450_01', 2)
    YAccel(15)
    XImpulseAcceleration(15)
    sprite('vrvhef450_01', 10)
    YAccel(5)
    XImpulseAcceleration(5)
    sprite('vrvhef450_01', 32767)


@State
def vh450_tsume02():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(255)
        PaletteIndex(1)
        AddY(450000)
        AddX(-600000)
        SetScaleX(1200)
        SetScaleY(1200)
        RotationAngle(300000)
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageCount(2)
        AfterimageMask_1(0, 255, 255, 255)
        AfterimageMask_2(0, 255, 255, 255)
        AfterimageSize_1(1060)
        AfterimageSize_2(10000)
    sprite('vrvhef450_02', 2)
    CommonSE('101_hit_slash_3')
    CommonSE('101_hit_slash_3')
    PrivateSE('vhse_11')
    PrivateSE('vhse_10')
    CreateObject('vh450_claw03', 0)
    CreateObject('vh450_claw03', 1)
    CreateObject('vh450_claw03', 2)
    CreateObject('vh450_claw03', 3)
    physicsXImpulse(90000)
    physicsYImpulse(-60000)
    sprite('vrvhef450_02', 6)
    ScreenShake(50000, 50000)
    CreateObject('vh450_claw03', 4)
    CreateObject('vh450_claw03', 5)
    CreateObject('vh450_claw03', 6)
    CreateObject('vh450_claw03', 7)
    sprite('vrvhef450_02', 1)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('vrvhef450_02', 2)
    YAccel(30)
    XImpulseAcceleration(30)
    sprite('vrvhef450_02', 2)
    YAccel(15)
    XImpulseAcceleration(15)
    sprite('vrvhef450_02', 10)
    YAccel(5)
    XImpulseAcceleration(5)
    sprite('vrvhef450_02', 32767)


@State
def vh450_tsume03():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(255)
        PaletteIndex(1)
        SetScaleX(1500)
        SetScaleY(1500)
        RotationAngle(90000)
    sprite('vrvhef450_01', 25)
    CommonSE('101_hit_slash_3')
    CommonSE('101_hit_slash_3')
    PrivateSE('vhse_11')
    PrivateSE('vhse_10')
    ScreenShake(50000, 50000)
    CreateObject('vh450_claw04', 4)
    CreateObject('vh450_claw04', 5)
    CreateObject('vh450_claw04', 6)
    CreateObject('vh450_claw04', 7)
    sprite('vrvhef450_01', 32767)


@State
def vh450_tsume04():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(255)
        PaletteIndex(1)
        AddY(100000)
        AddX(0)
        SetScaleX(1500)
        SetScaleY(1500)
        RotationAngle(45000)
    sprite('vrvhef450_02', 25)
    CommonSE('101_hit_slash_3')
    CommonSE('101_hit_slash_3')
    PrivateSE('vhse_11')
    PrivateSE('vhse_10')
    sprite('vrvhef450_02', 32767)


@State
def vh450_claw():

    def upon_IMMEDIATE():
        LinkParticle('vhef_astralcrow')
        E0EAEffectPosition(2)
        Size(1200)
    sprite('null', 80)


@State
def vh450_claw02():

    def upon_IMMEDIATE():
        LinkParticle('vhef_astralcrow')
        E0EAEffectPosition(2)
        Size(1200)
        RotationAngle(55000)
    sprite('null', 80)


@State
def vh450_claw03():

    def upon_IMMEDIATE():
        LinkParticle('vhef_astralcrow')
        E0EAEffectPosition(2)
        Size(1200)
        RotationAngle(300000)
    sprite('null', 80)


@State
def vh450_claw04():

    def upon_IMMEDIATE():
        LinkParticle('vhef_astralcrow')
        E0EAEffectPosition(2)
        Size(1200)
        RotationAngle(300000)
    sprite('null', 80)


@State
def Fade_Backout():
    sprite('vr_fade', 8)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(0)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(65)
    sprite('vr_fade', 4)
    sprite('vr_fade', 120)
    sprite('vr_fade', 8)
    ConstantAlphaModifier(-32)


@State
def WhiteBlood():

    def upon_IMMEDIATE():
        LinkParticle('vh450_astralblood')
        AddY(350000)
        AddX(490000)
        Size(1500)
        FaceLeft()
    sprite('null', 140)
    BlendMode_Add()
    RenderLayer(4)


@State
def WhiteBlood3D1():

    def upon_IMMEDIATE():
        Eff3DEffect('vhef_shibuki.DIG', 'vhef_shibuki_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(1000)
        AddY(150000)
        AddX(280000)
        RotationAngle(90000)
        AlphaValue(0)
    sprite('null', 4)
    ConstantAlphaModifier(80)
    sprite('null', 115)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-15)


@State
def WhiteBlood3D2():

    def upon_IMMEDIATE():
        Eff3DEffect('vhef_shibuki.DIG', 'vhef_shibuki_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(600)
        AddY(270000)
        AddX(-40000)
        RotationAngle(-110000)
        AlphaValue(0)
    sprite('null', 4)
    ConstantAlphaModifier(80)
    sprite('null', 115)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-15)


@State
def vh440_crow():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('vhef_440hikkaki00', '')
        AddX(350000)
        AddY(250000)
        SetScaleX(-1200)
        SetScaleY(1200)
        Rotation(35000)
    sprite('null', 12)
    sprite('null', 5)
    physicsXImpulse(10000)
    ConstantAlphaModifier(-51)


@State
def vh440_crow2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddX(200000)
        AddY(250000)
        Eff3DEffect('vhef_440hikkaki01', '')
        SetScaleX(-1800)
        SetScaleY(1800)
    sprite('null', 12)
    sprite('null', 5)
    SetScaleSpeed(-15)
    physicsXImpulse(10000)
    ConstantAlphaModifier(-51)


@State
def vh440_hikkaki():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddX(350000)
        Size(1200)
        IgnorePauses(2)
    sprite('vrvhef430_00', 8)
    CreateObject('vh440_hikkakiSub', -1)
    ScreenShake(20000, 20000)
    sprite('vrvhef430_01', 3)
    sprite('vrvhef430_02', 3)
    ParticleSize(1500)
    ParticleRotationAngle(-7500)
    CallCustomizableParticle('vhef440_end', 0)
    CreateParticle('vhef440_end', 1)
    ParticleSize(800)
    CallCustomizableParticle('vhef440_end', 2)
    sprite('vrvhef430_03', 3)


@State
def vh440_hikkakiSub():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddX(-600000)
        SetScaleX(800)
        SetScaleY(800)
        Flip()
        IgnorePauses(2)
    sprite('vrvhef430_00', 8)
    sprite('vrvhef430_01', 2)
    sprite('vrvhef430_02', 2)
    ParticleSize(1200)
    ParticleRotationAngle(-7500)
    CallCustomizableParticle('vhef440_end', 0)
    ParticleSize(800)
    CreateParticle('vhef440_end', 1)
    ParticleSize(600)
    CallCustomizableParticle('vhef440_end', 2)
    sprite('vrvhef430_03', 2)


@State
def vh440_hikkakiEX():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddX(400000)
        Size(1600)
        IgnorePauses(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrvhef430_00', 4)
    ScreenShake(20000, 20000)
    CreateObject('vh440_hikkakiSubEX', -1)
    sprite('vrvhef430_00', 10)
    ScreenShake(10000, 10000)
    sprite('vrvhef430_01', 3)
    sprite('vrvhef430_02', 3)
    ParticleSize(1700)
    ParticleRotationAngle(-7500)
    CallCustomizableParticle('vhef440_end', 0)
    ParticleSize(1400)
    CallCustomizableParticle('vhef440_end', 1)
    ParticleSize(1000)
    CallCustomizableParticle('vhef440_end', 2)
    sprite('vrvhef430_03', 3)


@State
def vh440_hikkakiSubEX():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddX(-600000)
        SetScaleX(1200)
        SetScaleY(1200)
        Flip()
        IgnorePauses(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrvhef430_00', 12)
    sprite('vrvhef430_01', 2)
    sprite('vrvhef430_02', 2)
    ParticleSize(1200)
    ParticleRotationAngle(-7500)
    CallCustomizableParticle('vhef440_end', 0)
    ParticleSize(800)
    CreateParticle('vhef440_end', 1)
    ParticleSize(600)
    CallCustomizableParticle('vhef440_end', 2)
    sprite('vrvhef430_03', 2)


@State
def vh440_hikkakiShock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('vhef_440shock00', '')
    sprite('null', 17)
    sprite('null', 5)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(-100)
    SetScaleSpeedZ(200)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def vh600_tojo_kick1():

    def upon_IMMEDIATE():
        LinkParticle('vh600_tojo_kick1')
        BlendMode_Add()
        Size(1200)
        RotationAngle(-20000)
    sprite('null', 20)


@State
def vh600_tojo_kick2():

    def upon_IMMEDIATE():
        LinkParticle('vh600_tojo_kick2')
        BlendMode_Add()
        Size(1200)
    sprite('null', 20)


@State
def vh600_tojo_kick3():

    def upon_IMMEDIATE():
        LinkParticle('vh600_tojo_kick3')
        Size(700)
        BlendMode_Add()
    sprite('null', 30)


@State
def vh601_line():

    def upon_IMMEDIATE():
        LinkParticle('vh600_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AlphaValue(0)
        AddX(-250000)
        AddY(-35000)
        uponSendToLabel(32, 73)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 4)
    AlphaValue(255)
    label(73)
    sprite('null', 14)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh601_line_masita():

    def upon_IMMEDIATE():
        LinkParticle('vh600_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1000)
        AlphaValue(0)
        RotationAngle(90000)
        uponSendToLabel(32, 74)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 4)
    AlphaValue(255)
    label(74)
    sprite('null', 14)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vh601_line_nanameue():

    def upon_IMMEDIATE():
        LinkParticle('vh600_line')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(1200)
        AlphaValue(0)
        RotationAngle(320000)
        AddX(-480000)
        AddY(-400000)
        uponSendToLabel(32, 75)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 4)
    AlphaValue(255)
    label(75)
    sprite('null', 14)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def vhef_entry():

    def upon_IMMEDIATE():
        LinkParticle('vh610_entry')
        BlendMode_Add()
        Size(840)
        AlphaValue(0)
        uponSendToLabel(32, 76)
    sprite('null', 8)
    ConstantAlphaModifier(32)
    sprite('null', 160)
    AlphaValue(255)
    label(76)
    sprite('null', 20)
    sprite('null', 26)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    AlphaValue(0)


@State
def vhef_entry1_2D():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ForceShadowOn(1)
        ForceShadowOff(1)
        ForceBloomMaskOn(1)
        AddX(-20000)
        SetScaleX(1100)
        SetScaleY(3300)
    sprite('vrvhef_env', 110)


@State
def vhef_entry2_2D():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ForceShadowOn(1)
        ForceShadowOff(1)
        ForceBloomMaskOn(1)
        AddX(-20000)
        SetScaleX(1250)
        SetScaleY(4800)
    sprite('vrvhef_env', 90)


@State
def vh610_entry_moya():

    def upon_IMMEDIATE():
        LinkParticle('vh610_entry_moya')
        BlendMode_Add()
        E0EAEffectPosition(3)
        Size(900)
        AlphaValue(0)
        uponSendToLabel(32, 78)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 200)
    AlphaValue(255)
    label(78)
    sprite('null', 10)
    sprite('null', 26)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    AlphaValue(0)


@State
def EventEffectRCFallWait():
    sprite('rc602_00', 6)
    AbsoluteY(720000)
    XPositionRelativeFacing(-50000)
    PaletteIndex(7)
    loopRest()


@State
def EventEffectRCFall():
    AbsoluteY(720000)
    XPositionRelativeFacing(-100000)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    sprite('rc602_00', 6)
    PaletteIndex(7)
    setGravity(25)
    physicsYImpulse(-1200)
    CommonSE('019_cloth_a')
    sprite('rc602_01', 6)
    sprite('rc602_02', 6)
    sprite('rc602_03', 6)
    sprite('rc602_04', 6)
    sprite('rc602_00', 6)
    CommonSE('019_cloth_a')
    sprite('rc602_01', 6)
    sprite('rc602_02', 6)
    sprite('rc602_03', 6)
    sprite('rc602_04', 6)
    sprite('rc602_00', 6)
    CommonSE('019_cloth_a')
    sprite('rc602_01', 6)
    sprite('rc602_02', 6)
    sprite('rc602_03', 6)
    sprite('rc602_04', 6)
    sprite('rc602_00', 6)
    CommonSE('019_cloth_a')
    sprite('rc602_01', 6)
    sprite('rc602_02', 6)
    sprite('rc602_03', 6)
    sprite('rc602_04', 6)
    sprite('rc602_05', 6)
    sprite('rc602_06', 6)
    setGravity(-46)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(0)
    sprite('rc602_07', 5)
    CommonSE('019_cloth_a')
    sprite('rc602_08', 5)
    sprite('rc602_09', 5)
    sprite('rc602_10', 5)
    sprite('rc602_11', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc602_12', 5)
    EndYPhysicsImpulse()
    physicsYImpulse(0)
    EndMomentum(1)
    CommonSE('202_walk_steal_0')
    LandingEffects(100, 1, 0)
    sprite('rc602_13', 5)
    sprite('rc602_14', 5)
    sprite('rc602_15', 5)
    sprite('rc602_16', 5)
    sprite('rc602_18', 7)
    sprite('rc602_19', 5)
    sprite('rc602_20', 5)
    sprite('rc602_21', 5)
    label(2)
    sprite('rc000_00', 7)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    loopRest()
    gotoLabel(2)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Eventoffset_Sosai():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(300000)
        DeviationX(-30000, 100000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
