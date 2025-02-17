@State
def EMB_BASE():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_NO.DIG', 'ef_emb_NO_motion_000.mmot')
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
def EMB_NO_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_NO.DIG', 'ef_emb_NO_motion_000.mmot')
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
def EMB_NO_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_NO.DIG', 'ef_emb_NO_motion_000.mmot')
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
    sprite('null', 80)


@State
def DIST_NO():
    sprite('vrdist00', 2)
    BlendMode_Normal()
    ParticleTransparency(1)
    PlayerTransparency(16000)
    Unknown3059(-40)
    Size(2000)
    SetScaleSpeed(50)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-4)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)
    sprite('vrdist00', 2)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-100, 100)


@State
def DIST_NO2():
    sprite('vrdist00', 2)
    BlendMode_Normal()
    ParticleTransparency(1)
    PlayerTransparency(10000)
    Unknown3059(-50)
    SetScaleX(1200)
    SetScaleY(1600)
    SetScaleSpeed(10)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-8)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)
    sprite('vrdist00', 2)
    DeviationX(-5000, 5000)
    DeviationY(-10000, 10000)
    RandAddScale(-50, 50)


@State
def noef229gtlptc_make():
    sprite('null', 4)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef_292henkei_tubu', 0)


@State
def noef_smoke():
    sprite('null', 4)
    CreateParticle('noef00', -1)


@State
def noef431gtlptc_make():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 143)
    CallCustomizableParticle('noef431_mc00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef431_mc01', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_mc02', -1)
    ParticleColorFromPalette(239, 239, 223)
    CallCustomizableParticle('noef431_mc03', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_circle00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef431_light00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600', -1)


@State
def noef431gunptc_make():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 143)
    CallCustomizableParticle('noef431up_mc00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_mc01', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_mc02', -1)
    ParticleColorFromPalette(223, 223, 143)
    CallCustomizableParticle('noef431up_mc03', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_circle00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_light00', -1)


@State
def noef600ptc_R():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 143)
    CallCustomizableParticle('noef600_mc00R', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_mc02', -1)
    ParticleColorFromPalette(223, 223, 143)
    CallCustomizableParticle('noef600_mc03', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_circle00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_light00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600', -1)


@State
def noef600ptc_L():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 143)
    CallCustomizableParticle('noef600_mc00L', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_mc02', -1)
    ParticleColorFromPalette(223, 223, 143)
    CallCustomizableParticle('noef600_mc03', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_circle00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_light00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600', -1)


@State
def noef430bzk_make():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 143)
    ParticleSize(2000)
    CallCustomizableParticle('noef430_mc00', -1)
    ParticleColorFromPalette(254, 254, 254)
    CallCustomizableParticle('noef430_mc01', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef430_mc02', -1)
    ParticleColorFromPalette(223, 223, 143)
    ParticleSize(2000)
    CallCustomizableParticle('noef430_mc03', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600_circle00', -1)
    ParticleColorFromPalette(239, 239, 239)
    ParticleSize(2000)
    CallCustomizableParticle('noef430_light00', -1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('noef600', -1)


@State
def noef_MagicShot():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef202_kakusan00', 2)
    ParticleColorFromPalette(254, 223, 234)
    CallCustomizableParticle('noef202_light00', 2)
    ParticleColorFromPalette(223, 254, 223)
    CallCustomizableParticle('noef202_2', 2)


@State
def BLT():

    def upon_IMMEDIATE():

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            PrivateSE('nose_02')
    sprite('vr_blt', 40)
    AddRotationPerFrame(10000)
    RandAddRotation(0, 360000)
    PrivateSE('nose_02')
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    RandSpeedX(-1000, 1000)
    RandSpeedY(-1000, 1000)


@State
def EFF_SakuretsuFar():

    def upon_IMMEDIATE():
        SetZVal(500)
    sprite('null', 1)
    CreateObject('noef_envlight', -1)
    CreateObject('noef_gfA', -1)
    CreateObject('noef_smoke', -1)


@State
def EFF_SakuretsuNear():

    def upon_IMMEDIATE():
        SetZVal(-500)
    sprite('null', 1)
    CreateObject('noef_envlight', -1)
    CreateObject('noef_gfA', -1)
    CreateObject('noef_smoke', -1)


@State
def EFF_LongFireTypeA():

    def upon_IMMEDIATE():
        SetZVal(-500)
    sprite('null', 1)
    CreateObject('noef_envlight', 2)
    CreateObject('noef_gfsideA', 2)
    CreateObject('noef_smoke', 2)


@State
def EFF_LongFireTypeB():

    def upon_IMMEDIATE():
        SetZVal(-500)
    sprite('null', 1)
    CreateObject('noef_envlight', 2)
    CreateObject('noef_gfsideB', 2)
    CreateObject('noef_smoke', 2)


@State
def EFF_LongFireTypeC():

    def upon_IMMEDIATE():
        SetZVal(-500)
    sprite('null', 1)
    CreateObject('noef_envlight', 2)
    CreateObject('noef_gfsideC', 2)
    CreateObject('noef_smoke', 2)


@State
def EFF_LongFireTypeD():

    def upon_IMMEDIATE():
        SetZVal(-500)
        RotationAngle(-8000)
    sprite('null', 1)
    CreateObject('noef_envlight', 2)
    CreateObject('noef_gfB', 2)
    CreateObject('noef_gfsideD', 2)
    CreateObject('noef_smoke', 2)


@State
def EFF_Spark():
    sprite('null', 1)
    CreateObject('noef_envlight', 2)
    CreateObject('noef_gfB', 2)
    CreateObject('noef_smoke', 2)


@State
def noef_envlight():

    def upon_IMMEDIATE():
        SetScaleX(1000)
        SetScaleY(1000)
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        PaletteIndex(2)
    sprite('vref_pallight', 12)
    BlendMode_Add()
    AlphaValue(255)
    ConstantAlphaModifier(-12)


@State
def noef_gfA():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfire00', 2)
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)


@State
def noef_gfB():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfired00', 2)
    sprite('vrnoef_gunfired01', 3)
    sprite('vrnoef_gunfired02', 2)
    sprite('vrnoef_gunfired03', 2)
    sprite('vrnoef_gunfired04', 2)
    sprite('vrnoef_gunfired05', 2)


@State
def noef_gfsideA():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfireb00', 1)
    sprite('vrnoef_gunfireb01', 2)
    sprite('vrnoef_gunfireb02', 2)
    sprite('vrnoef_gunfireb03', 2)
    sprite('vrnoef_gunfireb04', 2)
    sprite('vrnoef_gunfireb05', 2)


@State
def noef_gfsideB():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
        SetScaleX(1200)
        SetScaleY(1600)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfirec00', 1)
    sprite('vrnoef_gunfirec01', 2)
    sprite('vrnoef_gunfirec02', 2)
    sprite('vrnoef_gunfirec03', 2)
    sprite('vrnoef_gunfirec04', 2)
    sprite('vrnoef_gunfirec05', 2)


@State
def noef_gfsideC():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
        SetScaleX(1200)
        SetScaleY(1600)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfiree00', 1)
    sprite('vrnoef_gunfiree01', 2)
    sprite('vrnoef_gunfiree02', 2)
    sprite('vrnoef_gunfiree03', 2)
    sprite('vrnoef_gunfiree04', 2)
    sprite('vrnoef_gunfiree05', 2)
    sprite('vrnoef_gunfiree06', 2)
    sprite('vrnoef_gunfiree07', 2)


@State
def noef_gfsideD():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
        SetScaleY(1200)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_gunfireh00', 4)
    sprite('vrnoef_gunfireh01', 3)
    sprite('vrnoef_gunfireh02', 3)
    sprite('vrnoef_gunfireh03', 6)
    SetScaleXPerFrame(10)
    AlphaValue(255)
    ConstantAlphaModifier(-40)


@State
def noef_gfground():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        AlphaValue(255)
        PaletteIndex(1)
    sprite('vrnoef_gunfireg00', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 500, 500)
    sprite('vrnoef_gunfireg01', 2)
    sprite('vrnoef_gunfireg02', 2)
    sprite('vrnoef_gunfireg03', 2)
    sprite('vrnoef_gunfireg04', 2)
    sprite('vrnoef_gunfireg05', 2)
    sprite('vrnoef_gunfireg06', 2)
    ConstantAlphaModifier(-30)
    sprite('vrnoef_gunfireg07', 2)
    sprite('vrnoef_gunfireg08', 1)
    sprite('vrnoef_gunfireg08', 1)
    sprite('vrnoef_gunfireg08', 1)
    sprite('vrnoef_gunfireg08', 1)


@State
def noef_OIUCHI():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        PaletteIndex(1)
    sprite('vrnoef_gunfiref00', 2)
    BlendMode_Add()
    CreateDecal(0, 'FLORE_BURST', -1, 500, 500)
    CreateObject('DIST_NO', -1)
    sprite('vrnoef_gunfiref01', 2)
    sprite('vrnoef_gunfiref02', 2)
    sprite('vrnoef_gunfiref03', 2)
    sprite('vrnoef_gunfiref04', 2)
    sprite('vrnoef_gunfiref05', 2)


@State
def EFF_TargetA():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Visibility(1)
        NoAttackDuringAction(1)
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirUntechableTime(38)
        Hitstop(8)
        Damage(650)
        AttackP1(90)
        SameMoveProration(10)
        AirPushbackY(18000)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnoef_202tgt00', 2)
    PrivateSE('nose_22')
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        AlphaValue(64)
    sprite('vrnoef_202tgt00', 2)
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        Size(750)
    sprite('vrnoef_202tgt00', 4)
    sprite('vrnoef_202tgt00', 4)
    CommonSE('016_explode_1')
    CreateObject('noef_envlight', -1)
    CreateObject('Target_Mainfire', -1)
    CreateObject('noef_smoke', -1)
    CreateObject('EFF_Spark', 0)

    def RunOnObject_1():
        Size(1500)
    NoAttackDuringAction(0)
    CancelIfPlayerHit(0)


@State
def EFF_TargetB():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Visibility(1)
        NoAttackDuringAction(1)
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirUntechableTime(38)
        Hitstop(8)
        Damage(650)
        AttackP1(90)
        SameMoveProration(10)
        AirPushbackY(18000)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnoef_202tgt00', 2)
    PrivateSE('nose_22')
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        AlphaValue(64)
    sprite('vrnoef_202tgt00', 2)
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        Size(750)
    sprite('vrnoef_202tgt00', 4)
    sprite('vrnoef_202tgt00', 4)
    CommonSE('016_explode_1')
    CreateObject('noef_envlight', -1)
    CreateObject('Target_Mainfire', -1)
    CreateObject('noef_smoke', -1)
    CreateObject('EFF_Spark', 0)

    def RunOnObject_1():
        Size(1500)
    NoAttackDuringAction(0)
    CancelIfPlayerHit(0)


@State
def EFF_TargetInclude():
    sprite('vrnoef_202tgt00', 6)
    PaletteIndex(1)
    BlendMode_Add()
    AlphaValue(0)
    ConstantAlphaModifier(25)
    Size(800)
    SetScaleSpeed(10)
    sprite('vrnoef_202tgt00', 8)
    ConstantAlphaModifier(-15)
    SetScaleSpeed(-5)


@State
def Target_Mainfire():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        BlendMode_Add()
        Size(1200)
        PaletteIndex(1)
    sprite('vrnoef_gunfire00', 3)
    AddRotationPerFrame(50)
    sprite('vrnoef_gunfire01', 3)
    CreateObject('Target_Subfire', -1)
    sprite('vrnoef_gunfire02', 3)
    sprite('vrnoef_gunfire03', 3)
    sprite('vrnoef_gunfire04', 3)
    sprite('vrnoef_gunfire05', 3)
    AddRotationPerFrame(500)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-40)
    sprite('vrnoef_gunfire06', 3)


@State
def Target_Subfire():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        BlendMode_Add()
        Size(650)
        PaletteIndex(1)
    sprite('vrnoef_gunfirei00', 2)
    AddRotationPerFrame(50)
    ConstantAlphaModifier(-5)
    sprite('vrnoef_gunfirei01', 2)
    sprite('vrnoef_gunfirei02', 2)
    sprite('vrnoef_gunfirei03', 2)
    sprite('vrnoef_gunfirei04', 2)
    sprite('vrnoef_gunfirei05', 2)
    sprite('vrnoef_gunfirei06', 6)
    AddRotationPerFrame(500)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-40)


@State
def MajuShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Blockstun(20)
        Hitstun(21)
        AirUntechableTime(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(100)
        AttackP1(80)
        AttackP2(100)
        MinimumDamage(10)
        MoveAttributes(0, 0, 0, 1, 0)
        StarterRating(2)
        VoodooDamageMultiplier(3)
        AirPushbackY(10000)
        AirPushbackX(1400)
        YImpulseBeforeWallbounce(500)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        ContinueState(30)
        BlendMode_Add()
        PrivateSE('nose_04')
        PaletteIndex(1)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 62)
        if not SLOT_51:
            Damage(300)
            ResetAttackP2()
            AirPushbackY(16000)
            YImpulseBeforeWallbounce(1600)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)


@State
def MajuShotObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        AttackLevel_(4)
        Blockstun(20)
        Hitstun(21)
        AirUntechableTime(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(100)
        AttackP1(80)
        AttackP2(100)
        MinimumDamage(10)
        MoveAttributes(0, 0, 0, 1, 0)
        StarterRating(2)
        VoodooDamageMultiplier(3)
        AirPushbackY(10000)
        AirPushbackX(1400)
        YImpulseBeforeWallbounce(500)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        ContinueState(30)
        BlendMode_Add()
        PrivateSE('nose_04')
        PaletteIndex(1)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 62)
        if not SLOT_51:
            Damage(300)
            ResetAttackP2()
            AirPushbackY(16000)
            YImpulseBeforeWallbounce(1600)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)


@State
def MajuShotObj_Tsuika():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        AttackLevel_(4)
        AirUntechableTime(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        HeatGainMultiplier(0)
        Damage(100)
        AttackP1(80)
        AttackP2(100)
        MoveAttributes(0, 0, 0, 1, 0)
        AirPushbackY(6000)
        AirPushbackX(2800)
        YImpulseBeforeWallbounce(300)
        MinimumDamage(20)
        VoodooDamageMultiplier(3)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        ContinueState(30)
        BlendMode_Add()
        PrivateSE('nose_04')
        PaletteIndex(1)
        RotationAngle(-35000)
        physicsXImpulse(90000)
        physicsYImpulse(90000)
        IgnoreScreenfreeze(1)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)


@State
def no431_gun():
    sprite('no431_gun', 20)
    BlendMode_Normal()
    IgnoreScreenfreeze(1)
    ConstantAlphaModifier(-12)
    physicsXImpulse(-4000)
    physicsYImpulse(4000)
    GravityDefault()


@State
def noef431gun_del():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
    sprite('vrnoef431_00', 4)
    BlendMode_Add()
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    ParticleColorFromPalette(205, 205, 205)
    CallCustomizableParticle('noef600', 0)
    ParticleColorFromPalette(205, 205, 205)
    CallCustomizableParticle('noef600', 1)
    sprite('vrnoef431_01', 8)


@State
def noef431gtl_make():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
    sprite('vrnoef431_02', 4)
    BlendMode_Add()
    AlphaValue(128)
    ConstantAlphaModifier(30)
    sprite('vrnoef431_03', 8)


@State
def noef431gun_make():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
    sprite('vrnoef431_04', 4)
    BlendMode_Add()
    AlphaValue(64)
    ConstantAlphaModifier(10)
    AddX(70000)
    ParticleColorFromPalette(205, 205, 205)
    CallCustomizableParticle('noef431up', 0)
    ParticleColorFromPalette(205, 205, 205)
    CallCustomizableParticle('noef431up', 1)
    CreateObject('noef431gunptc_make', 2)
    sprite('vrnoef431_05', 6)
    sprite('vrnoef431_06', 20)
    sprite('vrnoef431_04', 10)
    ConstantAlphaModifier(-25)


@State
def noef431gun_turn():

    def upon_IMMEDIATE():
        SetZVal(-100)
    sprite('vrnoef285_00', 2)
    BlendMode_Normal()
    AlphaValue(250)
    RandRotationAngle()
    sprite('vrnoef285_00', 2)
    RandRotationAngle()
    AlphaValue(220)
    sprite('vrnoef285_00', 1)
    RandRotationAngle()
    AlphaValue(128)


@State
def RanshaShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Blockstun(20)
        AirUntechableTime(100)
        HardKnockdown(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(3000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(50)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(330)
        AttackP1(80)
        AttackP2(97)
        MoveAttributes(0, 0, 0, 1, 0)
        VoodooDamageMultiplier(3)
        StarterRating(2)
        MinimumDamage(10)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 50)
        ContinueState(30)
        HitboxMovement(175000, -45000)
        RotationAngle(45000)
        BlendMode_Add()
        PrivateSE('nose_27')
        PaletteIndex(1)

        def upon_EVERY_FRAME():
            Unknown2065(23)
            if SLOT_0:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    gotoLabel(3)
    label(50)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 2)
    ParticleSize(3000)
    CallCustomizableParticle('noef_explB', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 1000)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    label(3)


@State
def RanshaShotObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Blockstun(20)
        AirUntechableTime(100)
        HardKnockdown(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(3000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(50)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(330)
        AttackP1(80)
        AttackP2(97)
        MoveAttributes(0, 0, 0, 1, 0)
        MinimumDamage(10)
        AttackType(4)
        VoodooDamageMultiplier(3)
        StarterRating(2)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 50)
        ContinueState(30)
        HitboxMovement(175000, -45000)
        RotationAngle(45000)
        BlendMode_Add()
        PrivateSE('nose_27')
        PaletteIndex(1)

        def upon_EVERY_FRAME():
            Unknown2065(23)
            if SLOT_0:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    gotoLabel(3)
    label(50)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 2)
    ParticleSize(3000)
    CallCustomizableParticle('noef_explB', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 1000)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    label(3)


@State
def noef430bzk_rocket():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Blockstun(20)
        AirUntechableTime(120)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(50000)
        YImpulseBeforeWallbounce(1600)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(1900)
        GuardCrush(2, 1)
        MoveAttributes(0, 0, 0, 1, 0)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 1)
        ContinueState(120)
        SetZVal(-500)
        PaletteIndex(0)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnoef430_16r', 3)
    CreateObject('noef430rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef430rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef430rkf', 2)
    RegisterObject(6, 1)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    setGravity(0)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 2)
    CreateObject('noef430rkp', -1)
    RegisterObject(7, 1)
    SetActionMark(1)
    label(0)
    sprite('vrnoef430_16r', 2)
    physicsXImpulse(56000)
    physicsYImpulse(-40000)
    setGravity(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    PaletteIndex(1)
    BlendMode_Add()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(4000)
    RandRotationAngle()
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    if SLOT_2:
        DeleteObject(7)
    ParticleSize(6000)
    CallCustomizableParticle('noef_explA', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 2000)
    PrivateSE('nose_24')
    PrivateSE('nose_24')
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    ExitState()


@State
def noef430bzk_rocket_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        AttackLevel_(4)
        Blockstun(20)
        AirUntechableTime(120)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(50000)
        YImpulseBeforeWallbounce(1600)
        Hitstop(0)
        HeatGainMultiplier(0)
        PushbackX(5000)
        Damage(2000)
        GuardCrush(2, 1)
        MoveAttributes(0, 0, 0, 1, 0)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 1)
        ContinueState(120)
        SetZVal(-500)
        PaletteIndex(0)
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnoef430_16rOver', 3)
    CreateObject('noef430rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef430rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef430rkf', 2)
    RegisterObject(6, 1)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    setGravity(0)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 2)
    CreateObject('noef430rkp', -1)
    RegisterObject(7, 1)
    SetActionMark(1)
    label(0)
    sprite('vrnoef430_16rOver', 2)
    physicsXImpulse(56000)
    physicsYImpulse(-40000)
    setGravity(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    PaletteIndex(1)
    BlendMode_Add()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(4000)
    RandRotationAngle()
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    if SLOT_2:
        DeleteObject(7)
    ParticleSize(6000)
    CallCustomizableParticle('noef_explA', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 2000)
    PrivateSE('nose_24')
    PrivateSE('nose_24')
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    ExitState()


@State
def noef430bzk_fire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        SetZVal(-100)
        PaletteIndex(2)
    sprite('vrnoef430_00', 3)
    ParticleSize(3000)
    CallCustomizableParticle('noef_explA', -1)
    ConstantAlphaModifier(5)
    sprite('vrnoef430_01', 3)
    sprite('vrnoef430_02', 3)
    sprite('vrnoef430_03', 3)
    sprite('vrnoef430_04', 3)
    sprite('vrnoef430_05', 3)
    sprite('vrnoef430_06', 3)
    sprite('vrnoef430_07', 3)


@State
def noef430rkf():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        RotationAngle(34000)
        ContinueState(120)
        SetZVal(100)
        PaletteIndex(1)
    sprite('vrnoef430rkf_00', 2)
    SetScaleX(400)
    SetScaleY(200)
    SetScaleXPerFrame(5)
    SetScaleSpeedY(10)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 2)
    sprite('vrnoef430rkf_00', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 2)
    sprite('vrnoef430rkf_00', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    Size(1500)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430charge', -1)
    SetScaleX(750)
    SetScaleY(2500)
    SetScaleSpeed(-20)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430charge', -1)
    CommonSE('015_blaze_0')
    SetScaleSpeed(0)
    SetScaleX(2500)
    SetScaleY(4000)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    label(0)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_05', 1)
    loopRest()
    gotoLabel(0)


@State
def noef430rkp():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        RotationAngle(34000)
        ContinueState(120)
        PaletteIndex(1)
    label(0)
    sprite('vrnoef430rkp_00', 1)
    SetScaleY(2000)
    sprite('vrnoef430rkp_01', 1)
    sprite('vrnoef430rkp_02', 1)
    loopRest()
    gotoLabel(0)


@State
def GunThrowShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Hitstop(2)
        AttackLevel_(4)
        Damage(150)
        AttackP1(80)
        AttackP2(99)
        Hitstun(29)
        AirUntechableTime(30)
        Blockstun(28)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(1600)
        HitsparkSize(700)
        GuardCrush(1, 1)
        AirHitstunAnimation(10)
        MoveAttributes(0, 0, 0, 1, 0)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Off()
        SetZVal(100)
        AddRotationPerFrame(45000)
        SetAcceleration(-1900)
        physicsXImpulse(38500)
        AddX(50000)
        AddY(30000)
        physicsYImpulse(5000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('con6C', 32)
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    PushbackX(30000)
    AirPushbackX(24000)
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    PushbackX(5000)
    AirPushbackX(2000)
    AirPushbackY(16000)
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    SetAcceleration(-4000)
    PushbackX(-39900)
    AirPushbackX(-4000)
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')
    sprite('vrnoef285_00', 4)
    RefreshMultihit()
    CommonSE('003_swing_grap_0_0')


@State
def noef251z00():
    sprite('vrnoef251z00', 3)
    PaletteIndex(1)
    BlendMode_Add()
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(254)
    PaletteColor3(95)
    PaletteColor4(255)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)


@State
def noef251z01():
    sprite('vrnoef251z01', 3)
    PaletteIndex(1)
    BlendMode_Add()
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(254)
    PaletteColor3(95)
    PaletteColor4(255)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)


@State
def noef251z02():
    sprite('vrnoef251z02', 20)
    PaletteIndex(1)
    BlendMode_Add()
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(254)
    PaletteColor3(95)
    PaletteColor4(255)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)


@State
def noef_samaso():

    def upon_IMMEDIATE():
        AddX(150000)
        AddY(250000)
        PaletteIndex(1)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
    sprite('vrnoef289_00', 3)
    sprite('vrnoef289_01', 4)
    sprite('vrnoef289_02', 2)
    sprite('vrnoef289_03', 2)
    sprite('vrnoef289_04', 2)
    sprite('vrnoef289_05', 2)


@State
def noef_292():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        SetScaleX(950)
        AddX(80000)
    sprite('vrnoef_292_00', 4)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef_292fire_smoke', 1)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef_shotgun_tub00', 2)
    CreateObject('BLT', 0)
    sprite('vrnoef_292_01', 4)
    sprite('vrnoef_292_02', 4)
    AlphaValue(200)
    CreateObject('noef_gfB', -1)

    def RunOnObject_1():
        AddY(180000)
        AddX(200000)
        AddScale(500)
    sprite('vrnoef_292_03', 2)
    AlphaValue(150)


@State
def noef_234():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        Size(625)
    sprite('vrnoef_gunfirec00', 2)
    CreateObject('noef_234add', -1)
    sprite('vrnoef_gunfirec01', 2)
    sprite('vrnoef_gunfirec02', 2)
    sprite('vrnoef_gunfirec03', 2)
    sprite('vrnoef_gunfirec04', 2)
    sprite('vrnoef_gunfirec05', 2)


@State
def noef_234add():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        BlendMode_Add()
        PaletteIndex(1)
        Size(900)
        RandRotationAngle()
    sprite('vrnoef_gunfired00', 2)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef_293fire_add3', -1)
    sprite('vrnoef_gunfired01', 2)
    sprite('vrnoef_gunfired02', 2)
    sprite('vrnoef_gunfired03', 2)
    sprite('vrnoef_gunfired04', 2)
    sprite('vrnoef_gunfired05', 2)


@State
def noef_293():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        E0EAEffectPosition(2)
        AddY(150000)
        AddX(160000)
        RotationAngle(-12000)
        Size(1100)
    sprite('vrnoef_293_00', 2)
    sprite('vrnoef_293_01', 2)
    sprite('vrnoef_293_02', 2)
    E0EAEffectPosition(0)
    sprite('vrnoef_293_03', 2)
    CreateObject('noef_293sml', 0)
    CreateObject('noef_293sml', 1)
    AlphaValue(150)
    AddScale(-200)
    sprite('vrnoef_293_04', 2)
    sprite('vrnoef_293_05', 2)


@State
def noef_293sml():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        PaletteIndex(1)
        Size(600)
    sprite('vrnoef_gunfired00', 2)
    PaletteIndex(1)
    ParticleColorFromPalette(239, 223, 234)
    CallCustomizableParticle('noef_293fire_add3', -1)
    sprite('vrnoef_gunfired01', 3)
    sprite('vrnoef_gunfired02', 2)
    sprite('vrnoef_gunfired03', 2)
    sprite('vrnoef_gunfired04', 2)
    sprite('vrnoef_gunfired05', 2)


@State
def noef_406():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrnoef_406_00', 1)
    ParticleRotationAngle(-8000)
    CallCustomizableParticle('noef_406ground_ground', 0)
    sprite('vrnoef_406_01', 1)
    CreateParticle('noef_406hibana_tubu', 0)
    CreateParticle('noef_406hibana_tubu', 1)
    sprite('vrnoef_406_02', 1)
    sprite('vrnoef_406_03', 2)
    sprite('vrnoef_406_04', 2)
    sprite('vrnoef_406_05', 2)


@State
def noef601manto():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('vrnoef601m_00', 4)
    setGravity(500)
    physicsYImpulse(10000)
    physicsXImpulse(-20000)
    sprite('vrnoef601m_01', 4)
    sprite('vrnoef601m_02', 4)
    physicsYImpulse(-1000)
    setGravity(1200)
    sprite('vrnoef601m_03', 5)


@State
def MajuMagicCircle():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('noef_neme1.DIG', 'noef_neme1_motion_000.mmot')
        IgnoreScreenfreeze(1)
    sprite('null', 60)


@State
def ModelBeam():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('noef_neme2.DIG', 'noef_neme2_motion_000.mmot')
        IgnoreScreenfreeze(1)
    sprite('null', 50)


@State
def LookAtMe():

    def upon_IMMEDIATE():
        AddX(280000)
        AbsoluteY(0)
    sprite('null', 32767)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)


@State
def LastLookAtMe():

    def upon_IMMEDIATE():
        AddX(-64000)
        AbsoluteY(0)
    sprite('null', 32767)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)


@State
def AstWhiteOut():
    sprite('vr_white', 60)
    SetZVal(-1000)
    BlendMode_Normal()
    AlphaValue(0)
    ConstantAlphaModifier(10)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    Size(4000)
    sprite('vr_white', 90)


@State
def AstDando():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('null', 500)
    ParticleSize(1000)
    CallCustomizableParticle('noef_AH_flash', -1)
    CreateObject('DIST_NO2', -1)


@State
def AstLaserAll():

    def upon_IMMEDIATE():
        AddX(330000)
    sprite('null', 43)
    sprite('null', 30)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 8)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 29)
    CreateObject('AstLaser', -1)
    sprite('null', 29)
    CreateObject('AstLaser', -1)
    sprite('null', 15)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    sprite('null', 5)
    CreateObject('AstLaser', -1)
    CreateObject('AstLaser', -1)
    CreateObject('AstCharge', -1)
    sprite('null', 16)
    CommonSE('015_blaze_2')
    CommonSE('002_highjump_0')
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 8)
    CommonSE('002_highjump_0')
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 8)
    CommonSE('002_highjump_0')
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 8)
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 4)
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 4)
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 4)
    CommonSE('002_highjump_1')
    CommonSE('019_quake_1')
    sprite('null', 4)
    CommonSE('000_airdash_1')
    sprite('null', 2)
    CommonSE('000_airdash_1')
    sprite('null', 2)
    sprite('null', 2)
    sprite('null', 60)
    sprite('null', 10)
    CreateObject('AstLaserLast', -1)


@State
def AstCharge():

    def upon_IMMEDIATE():
        AbsoluteY(256000)
    sprite('null', 200)
    ParticleSize(1000)
    CallCustomizableParticle('noef_AH_charge', -1)
    CommonSE('022_magiccircle_d')


@State
def DIST_NO_Ast():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(20000)
        SetScaleX(5000)
        SetScaleY(5000)
    label(0)
    sprite('vrdist00', 2)
    RandAddRotation(-90000, 90000)
    loopRest()
    gotoLabel(0)


@State
def EFF_AstTarget():

    def upon_IMMEDIATE():
        AddX(280000)
        AbsoluteY(256000)
        RandAddScaleX(-500, 500)
        PaletteIndex(1)
    sprite('vrnoef_202tgt00', 10)
    BlendMode_Add()
    AlphaValue(32)
    ConstantAlphaModifier(10)
    Size(5000)
    SetScaleSpeed(-350)
    CreateObject('DIST_NO_Ast', -1)
    sprite('vrnoef_202tgt00', 30)
    SetScaleSpeed(2)
    sprite('vrnoef_202tgt00', 340)
    SetScaleSpeed(0)
    sprite('vrnoef_202tgt00', 40)
    ConstantAlphaModifier(-5)
    SetScaleSpeed(5)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(3)
    AfterimageCount(5)
    AfterimageSize_1(1000)
    AfterimageSize_2(2000)
    CreateParticle('noef_AH_finishflash', -1)
    CommonSE('022_magiccircle_b')


@State
def AstLockLaser():

    def upon_IMMEDIATE():
        AddX(330000)
        AbsoluteY(256000)
    sprite('null', 32767)
    ParticleSize(1200)
    CallCustomizableParticle('noef_AH_farstattack', -1)
    CommonSE('024_getset_b')


@State
def AstFarstFlash():

    def upon_IMMEDIATE():
        pass
    sprite('null', 32767)
    CreateParticle('noef_AH_farstflash', -1)
    CreateObject('DIST_NO', -1)
    CommonSE('022_magiccircle_d')


@State
def AstLaser():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(3)
        HitsparkSize(700)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(220)
        Crumple(200)
        Hitstop(0)
        PushbackX(0)
        HitAnywhere(1)
        DisableOppPushCollision(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        RemoveOnCallStateEnd(2)
        LinkParticle('noef_AH_attack')
        Visibility(1)
        SetZVal(100)
        AbsoluteY(128000)
        DeviationX(-150000, 150000)
        DeviationY(0, 230000)
    sprite('vrnoef_astatk00', 5)
    CreateParticle('noef_AH_splash', -1)
    PrivateSE('nose_23')
    sprite('vrnoef_astatk00', 5)
    sprite('vrnoef_astatk00', 32767)


@State
def AstLaserLast():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(4)
        DefeatOpponentBehavior(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(100000)
        AirPushbackX(2000)
        AirUntechableTime(270)
        Hitstop(0)
        PushbackX(0)
        HitAnywhere(1)
        DisableOppPushCollision(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(255)
        TeleportToObject(22)
        AbsoluteY(0)
        SetZVal(100)
        SetScaleX(3000)
        SetScaleY(1000)
    sprite('null', 5)
    CreateParticle('noef_AH_lastattack', -1)
    CreateObject('AstExplPtc', -1)
    sprite('vrnoef_astatk01', 5)
    SetScaleXPerFrame(5)
    sprite('vrnoef_astatk01', 30)
    ConstantAlphaModifier(-10)
    SetScaleXPerFrame(-50)


@State
def AstExplPtc():

    def upon_IMMEDIATE():
        pass
    sprite('null', 3)
    ParticleSize(4000)
    CallCustomizableParticle('noef_AH_expl', -1)
    CommonSE('016_explode_2')
    ScreenShake(15000, 0)
    sprite('null', 3)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    ScreenShake(15000, 0)
    sprite('null', 3)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    ScreenShake(15000, 0)


@State
def RLAstSmoke():

    def upon_IMMEDIATE():
        LinkParticle('noef_rlAHsmoke')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 65)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def AHatemiEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('noef_hantei00', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 1)
        uponSendToLabel(STATE_END, 1)
        uponSendToLabel(33, 0)
        Size(1800)
        AddY(180000)
        AddX(150000)
    sprite('null', 10)
    CreateParticle('noef_450atemi_subc', -1)
    sprite('null', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 30)
    CreateParticle('noef_450atebrake_tub', -1)
    CharacterFlash2(-65536, 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    gotoLabel(2)
    label(2)
    sprite('null', 1)


@State
def SphereMagiMatome():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(2)
        uponSendToLabel(33, 0)
        uponSendToLabel(32, 1)
    sprite('null', 30)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(300000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(700000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(-700000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(800000)
        AddX(-400000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(800000)
        AddX(400000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(-150000)
        AddX(300000)
    CreateObject('Bakuhapos', -1)

    def RunOnObject_1():
        AddY(-150000)
        AddX(-300000)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    CreateObject('SphereMagi00', -1)

    def RunOnObject_1():
        AddY(300000)
    sprite('null', 5)
    CreateObject('SphereMagi01', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(700000)
    sprite('null', 5)
    CreateObject('SphereMagi01a', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(-700000)
    sprite('null', 5)
    CreateObject('SphereMagi02', -1)

    def RunOnObject_1():
        AddY(800000)
        AddX(-400000)
    sprite('null', 5)
    CreateObject('SphereMagi03', -1)

    def RunOnObject_1():
        AddY(800000)
        AddX(400000)
    sprite('null', 5)
    CreateObject('SphereMagi04', -1)

    def RunOnObject_1():
        AddY(-150000)
        AddX(300000)
    sprite('null', 5)
    CreateObject('SphereMagi05', -1)

    def RunOnObject_1():
        AddY(-150000)
        AddX(-300000)
    sprite('null', 25)
    sprite('null', 32767)
    label(1)
    sprite('null', 2)
    TriggerUponForState('SphereMagi00', 32)
    sprite('null', 2)
    TriggerUponForState('SphereMagi01', 32)
    TriggerUponForState('SphereMagi01a', 32)
    sprite('null', 2)
    TriggerUponForState('SphereMagi02', 32)
    sprite('null', 2)
    TriggerUponForState('SphereMagi03', 32)
    sprite('null', 2)
    TriggerUponForState('SphereMagi04', 32)
    sprite('null', 2)
    TriggerUponForState('SphereMagi05', 32)
    CreateParticle('noef_whiteout_03', -1)


@State
def Bakuhapos():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('noef_450_bakuhapos')
        Size(3000)
    sprite('null', 100)


@State
def SphereMagi00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(150000)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(-150000)
    sprite('null', 10)
    CreateObject('AHboom', -1)


@State
def SphereMagi01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsXImpulse(1500)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(-150000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(-150000)


@State
def SphereMagi01a():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsXImpulse(-1500)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(150000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddX(150000)


@State
def SphereMagi02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsYImpulse(750)
    physicsXImpulse(-750)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(-300000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(-300000)


@State
def SphereMagi03():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsYImpulse(750)
    physicsXImpulse(750)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(-300000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(-300000)


@State
def SphereMagi04():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsYImpulse(-750)
    physicsXImpulse(750)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(300000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(300000)


@State
def SphereMagi05():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_emb_sphereemb', '')
        IgnoreScreenfreeze(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    CreateParticle('noef_450_magistart', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    physicsYImpulse(-750)
    physicsXImpulse(-750)
    sprite('null', 10)
    LinkParticle('noef_450_jizoku_aura')
    sprite('null', 30)
    CharacterFlash2(1694466112, 90)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(300000)
    sprite('null', 10)
    CreateObject('AHboom', -1)

    def RunOnObject_1():
        AddY(300000)


@State
def AHboom():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteID(0)
        PaletteIndex(1)
        E0EAEffectPosition(2)
        Size(2000)
        RandAddRotation(0, 360000)
        RenderLayer(1)
    sprite('vrnoef_gunfire00', 4)
    ScreenShake(5000, 5000)
    CreateObject('bommhojo', -1)
    sprite('vrnoef_gunfire01', 4)
    sprite('vrnoef_gunfire02', 4)
    sprite('vrnoef_gunfire03', 4)
    sprite('vrnoef_gunfire04', 4)
    sprite('vrnoef_gunfire05', 4)
    sprite('vrnoef_gunfire06', 4)
    sprite('null', 8)


@State
def bommhojo():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteID(0)
        PaletteIndex(1)
        E0EAEffectPosition(2)
        RandAddScale(500, 1000)
        RandAddRotation(0, 360000)
        RenderLayer(1)
    sprite('vrnoef_gunfirei00', 4)
    sprite('vrnoef_gunfirei01', 4)
    sprite('vrnoef_gunfirei02', 4)
    sprite('vrnoef_gunfirei03', 4)
    sprite('vrnoef_gunfirei04', 4)
    sprite('vrnoef_gunfirei05', 4)
    sprite('vrnoef_gunfirei06', 4)


@State
def AHmazle():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        RandAddScale(500, 1000)
        RandAddRotation(0, 360000)
        RenderLayer(1)
        ParticleColorFromPalette(239, 223, 143)
        CallPrivateEffect('noef_450_mazzle_circle')
    sprite('vrnoef_gunfire00', 3)
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 3)
    sprite('vrnoef_gunfire03', 3)
    sprite('vrnoef_gunfire04', 3)
    sprite('vrnoef_gunfire05', 3)
    sprite('vrnoef_gunfire06', 3)


@State
def AHanten():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        LinkParticle('noef_anten')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def AHDaburi():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('no450cutin_00', 10)
    CharacterFlash2(255, 10)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-26)
    physicsYImpulse(-28000)


@State
def AHatemiAnten():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(3)
        SetPosXByScreenPer(50)
        ColorForTransition(4278190080)
        Size(10000)
        BlendMode_Normal()
        AlphaValue(0)
    sprite('vr_white', 60)
    ConstantAlphaModifier(17)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-20)


@State
def AHantenSlow():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        SetPosXByScreenPer(50)
        ColorForTransition(4278190080)
        RenderLayer(4)
        uponSendToLabel(32, 0)
    sprite('vr_white', 17)
    ConstantAlphaModifier(15)
    AlphaValue(0)
    sprite('vr_white', 32767)
    AlphaValue(255)
    label(0)
    sprite('vr_white', 25)
    ConstantAlphaModifier(-10)


@State
def AHcamera():

    def upon_IMMEDIATE():
        E0EAEffectDirection(3)
        DisableOppPushCollision(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraControlEnable(1)
        CameraFast(1)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    XPositionRelativeFacing(-200000)
    label(1)
    sprite('null', 32767)
    XPositionRelativeFacing(0)
    CreateObject('SphereMagiMatome', -1)
    label(2)
    sprite('null', 1)


@State
def EFF_TargetA_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Visibility(1)
        NoAttackDuringAction(1)
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirUntechableTime(33)
        Damage(650)
        AttackP1(90)
        SameMoveProration(10)
        MoveAttributes(0, 0, 0, 1, 0)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
    sprite('vrnoef_202tgt00', 2)
    PrivateSE('nose_22')
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        AlphaValue(64)
    sprite('vrnoef_202tgt00', 2)
    CreateObject('EFF_TargetInclude', -1)

    def RunOnObject_1():
        Size(750)
    sprite('vrnoef_202tgt00', 4)
    sprite('vrnoef_202tgt00', 4)
    CommonSE('016_explode_1')
    CreateObject('noef_envlight', -1)
    CreateObject('Target_Mainfire', -1)
    CreateObject('noef_smoke', -1)
    CreateObject('EFF_Spark', 0)

    def RunOnObject_1():
        Size(1500)
    NoAttackDuringAction(0)
    CancelIfPlayerHit(0)


@State
def Target_Mainfire_Event():

    def upon_IMMEDIATE():
        RandRotationAngle()
        E0EAEffectDirection(2)
        BlendMode_Add()
        Size(1200)
        PaletteIndex(1)
    sprite('vrnoef_gunfire00', 3)
    AddRotationPerFrame(50)
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 3)
    sprite('vrnoef_gunfire03', 3)
    sprite('vrnoef_gunfire04', 3)
    sprite('vrnoef_gunfire05', 3)
    AddRotationPerFrame(500)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-40)
    sprite('vrnoef_gunfire06', 3)


@State
def noef440bzk_rocket():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(660)
        AirUntechableTime(999)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(55000)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        Hitstop(0)
        CHStateIfCHStart(3)
        MinimumDamage(10)
        AttackType(4)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        OnlyHitPlayer(1)
        EnableRapidCancel(0)
        DisableOppPushCollision(1)
        IgnoreComboTime(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 1)
        uponSendToLabel(32, 2)
        SetZVal(-500)
        PaletteIndex(0)
    sprite('vrnoef430_16r', 3)
    CreateObject('noef440rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf', 2)
    RegisterObject(6, 1)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    setGravity(0)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16r', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16r', 2)
    CreateObject('noef430rkp', -1)
    RegisterObject(7, 1)
    SetActionMark(1)
    sprite('vrnoef430_16r', 2)
    physicsXImpulse(56000)
    physicsYImpulse(-20000)
    setGravity(0)
    loopRest()
    sprite('vrnoef430_16r', 2)
    RotationAngle(-10000)
    sprite('vrnoef430_16r', 2)
    RotationAngle(-20000)
    sprite('vrnoef430_16r', 2)
    RotationAngle(-30000)
    sprite('vrnoef430_16r', 2)
    RotationAngle(-34000)
    label(1)
    sprite('vrnoef440_06r', 2)
    RotationAngle(0)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf', 2)
    RegisterObject(6, 1)

    def upon_45():
        PrivateFunction3(22, 150000, 10000, 50, 1)
    sprite('vrnoef440_06r', 2)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf_3', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf_3', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf_3', 2)
    RegisterObject(6, 1)
    sprite('vrnoef440_06r', 3)
    if SLOT_2:
        DeleteObject(7)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf_3', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf_3', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf_3', 2)
    RegisterObject(6, 1)
    sprite('vrnoef440_06r', 32767)
    loopRest()
    label(2)
    sprite('vrnoef440_06r', 1)
    sprite('vrnoef440_06r', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1700)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(30000)
    AirPushbackY(30000)
    AirUntechableTime(120)
    Floorslide(70)
    HardKnockdown(30)
    YImpulseBeforeWallbounce(2000)
    DefeatOpponentBehavior(0)
    HitAnywhere(1)
    CreateObject('no440WhiteOut', 0)
    sprite('vrnoef_gunfire00', 2)
    PaletteIndex(1)
    BlendMode_Add()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(4000)
    RandRotationAngle()
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    if SLOT_2:
        DeleteObject(7)
    ParticleSize(6000)
    CallCustomizableParticle('noef_explA', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 2000)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    HitAnywhere(0)
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    ExitState()


@State
def noef440bzk_rocket_Over():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(660)
        AirUntechableTime(999)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(55000)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        Hitstop(0)
        CHStateIfCHStart(3)
        MinimumDamage(10)
        AttackType(4)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        OnlyHitPlayer(1)
        EnableRapidCancel(0)
        DisableOppPushCollision(1)
        IgnoreComboTime(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 1)
        uponSendToLabel(32, 2)

        def upon_OPPONENT_HIT_OR_BLOCK():

            def RunOnObject_22():
                AbsoluteY(0)
        SetZVal(-500)
        PaletteIndex(0)
    sprite('vrnoef430_16rOver', 3)
    CreateObject('noef440rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf', 2)
    RegisterObject(6, 1)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    setGravity(0)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(-1400)
    AddY(-1000)
    sprite('vrnoef430_16rOver', 3)
    AddX(1400)
    AddY(1000)
    sprite('vrnoef430_16rOver', 2)
    CreateObject('noef430rkp', -1)
    RegisterObject(7, 1)
    SetActionMark(1)
    sprite('vrnoef430_16rOver', 2)
    physicsXImpulse(56000)
    physicsYImpulse(-20000)
    setGravity(0)
    loopRest()
    sprite('vrnoef430_16rOver', 2)
    RotationAngle(-10000)
    sprite('vrnoef430_16rOver', 2)
    RotationAngle(-20000)
    sprite('vrnoef430_16rOver', 2)
    RotationAngle(-30000)
    sprite('vrnoef430_16rOver', 2)
    RotationAngle(-34000)
    label(1)
    sprite('vrnoef440_06rOver', 2)
    RotationAngle(0)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf', 2)
    RegisterObject(6, 1)

    def upon_45():
        PrivateFunction3(22, 150000, 10000, 50, 1)
    sprite('vrnoef440_06rOver', 2)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf_3', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf_3', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf_3', 2)
    RegisterObject(6, 1)
    sprite('vrnoef440_06rOver', 3)
    if SLOT_2:
        DeleteObject(7)
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    CreateObject('noef440rkf_3', 0)
    RegisterObject(4, 1)
    CreateObject('noef440rkf_3', 1)
    RegisterObject(5, 1)
    CreateObject('noef440rkf_3', 2)
    RegisterObject(6, 1)
    sprite('vrnoef440_06rOver', 32767)
    loopRest()
    label(2)
    sprite('vrnoef440_06rOver', 1)
    CreateObject('no440BombMato', -1)
    sprite('vrnoef440_06rOver', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1700)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(40000)
    AirPushbackY(40000)
    AirUntechableTime(120)
    Floorslide(70)
    HardKnockdown(30)
    YImpulseBeforeWallbounce(2000)
    DefeatOpponentBehavior(0)
    CreateObject('no440WhiteOut_2', 0)
    sprite('vrnoef_gunfire00', 2)
    PaletteIndex(1)
    BlendMode_Add()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(4000)
    RandRotationAngle()
    DeleteObject(4)
    DeleteObject(5)
    DeleteObject(6)
    if SLOT_2:
        DeleteObject(7)
    ParticleSize(6000)
    CallCustomizableParticle('noef_explA', 2)
    CreateDecal(0, 'FLORE_BURST', -1, 2000, 2000)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('vrnoef_gunfire01', 2)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)
    loopRest()
    ExitState()


@State
def noef440rkf():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        BlendMode_Add()
        RotationAngle(34000)
        SetZVal(100)
        PaletteIndex(1)
        EnableCollision(0)
    sprite('vrnoef430rkf_00', 2)
    SetScaleX(400)
    SetScaleY(200)
    SetScaleXPerFrame(5)
    SetScaleSpeedY(10)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 2)
    sprite('vrnoef430rkf_00', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 2)
    sprite('vrnoef430rkf_00', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_01', 2)
    sprite('vrnoef430rkf_02', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_03', 2)
    sprite('vrnoef430rkf_04', 2)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    Size(1500)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430charge', -1)
    SetScaleX(750)
    SetScaleY(2500)
    SetScaleSpeed(-20)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430charge', -1)
    CommonSE('015_blaze_0')
    SetScaleSpeed(0)
    SetScaleX(2500)
    SetScaleY(4000)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    label(0)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_05', 1)
    loopRest()
    gotoLabel(0)


@State
def noef440rkf_2():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        BlendMode_Add()
        RotationAngle(34000)
        SetZVal(100)
        PaletteIndex(1)
    sprite('vrnoef430rkf_05', 1)
    Size(1500)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430charge', -1)
    SetScaleX(750)
    SetScaleY(2500)
    SetScaleSpeed(-20)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430charge', -1)
    SetScaleSpeed(0)
    SetScaleX(2500)
    SetScaleY(4000)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    label(0)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_05', 1)
    loopRest()
    gotoLabel(0)


@State
def noef440rkf_3():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        IgnorePauses(2)
        BlendMode_Add()
        SetZVal(100)
        PaletteIndex(1)
        AddY(50000)
    sprite('vrnoef430rkf_05', 1)
    Size(1500)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430charge', -1)
    SetScaleX(750)
    SetScaleY(2500)
    SetScaleSpeed(-20)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430charge', -1)
    SetScaleSpeed(0)
    SetScaleX(2500)
    SetScaleY(4000)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430charge', -1)
    sprite('vrnoef430rkf_05', 1)
    label(0)
    sprite('vrnoef430rkf_00', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_01', 1)
    sprite('vrnoef430rkf_02', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_03', 1)
    sprite('vrnoef430rkf_04', 1)
    CreateParticle('noef430fire', -1)
    sprite('vrnoef430rkf_05', 1)
    loopRest()
    gotoLabel(0)


@State
def no440RailGun():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        setGravity(0)
        Size(2000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
    sprite('null', 32767)
    physicsXImpulse(70000)
    CreateObject('no440RailGunMitame', -1)
    CreateObject('no440TamaSmoke', -1)
    label(0)
    sprite('null', 32767)
    physicsXImpulse(1000)
    label(1)
    sprite('null', 32767)
    physicsXImpulse(150000)
    label(2)
    sprite('null', 10)
    TriggerUponForState('no440TamaSmoke', 32)
    loopRest()


@State
def no440RailGunMitame():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('noef_440tama')
        CreateObject('no440ThunderTama', -1)
        Size(1800)
        AddX(20000)
    label(0)
    sprite('null', 2)
    AddScaleX(100)
    AddScaleY(-200)
    AddY(15000)
    AddX(-15000)
    sprite('null', 2)
    AddScaleX(-100)
    AddScaleY(200)
    AddY(-15000)
    AddX(15000)
    gotoLabel(0)


@State
def no440ThunderTama():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        FaceSpawnLocation()
        Eff3DEffect('noef_thunder00', '')
        SetScaleY(1800)
        SetScaleX(3500)
        AddX(-300000)
        AlphaValue(100)
    sprite('null', 32767)


@State
def no440TamaSmoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('noef_440shot_smoke00')
        AddY(-250000)
        AddX(-200000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('noef_440shot_smoke_nokosi', -1)
    gotoLabel(0)


@State
def no440Shake():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(2)
    label(0)
    sprite('null', 3)
    ScreenShake(1000, 3000)
    sprite('null', 3)
    ScreenShake(1000, 3000)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    ScreenShake(1000, 5000)
    sprite('null', 3)
    ScreenShake(1000, 5000)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('null', 10)
    ScreenShake(75000, 75000)
    loopRest()


@State
def no440Camera():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
        uponSendToLabel(41, 9)
        IgnoreScreenfreeze(1)
        Visibility(1)
        RemoveOnCallStateEnd(3)
    sprite('null', 32767)
    label(0)
    sprite('vrnoef440railguntest', 30)
    TeleportToObject(22)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    sprite('keep', 32767)
    physicsXImpulse(60000)
    label(1)
    sprite('vrnoef440railguntest', 20)
    CameraPosition(1000)
    physicsXImpulse(0)
    TeleportToObject(3)
    sprite('keep', 32767)
    CreateObject('no440ShaSha', -1)
    label(2)
    sprite('vrnoef440railguntest', 32767)
    CameraFast(1)
    TeleportToObject(3)
    AddX(-1000000)
    loopRest()
    label(3)
    sprite('vrnoef440railguntest', 5)
    CameraFast(1)
    TeleportToObject(3)
    CameraPosition(1000)
    sprite('vrnoef440railguntest', 40)
    CameraFast(0)
    physicsXImpulse(53000)
    sprite('vrnoef440railguntest', 32767)
    label(4)
    sprite('vrnoef440railguntest', 40)
    TeleportToObject(22)
    physicsXImpulse(15000)
    sprite('vrnoef440railguntest', 32767)
    physicsXImpulse(0)
    label(5)
    sprite('vrnoef440railguntest', 32767)
    EndMomentum(1)
    TeleportToObject(3)
    CameraFast(1)
    label(9)
    sprite('vrnoef440railguntest', 40)

    def upon_EVERY_FRAME():
        PrivateFunction3(22, 300000, 0, 100, 0)


@State
def no440Camera_2():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
        uponSendToLabel(41, 9)
        IgnoreScreenfreeze(1)
        Visibility(1)
        RemoveOnCallStateEnd(3)
    sprite('null', 32767)
    label(0)
    sprite('vrnoef440railguntest', 30)
    TeleportToObject(22)
    AbsoluteY(0)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    sprite('keep', 32767)
    physicsXImpulse(60000)
    label(1)
    sprite('vrnoef440railguntest', 20)
    CameraPosition(1000)
    physicsXImpulse(0)
    TeleportToObject(3)
    sprite('keep', 32767)
    CreateObject('no440ShaSha', -1)
    label(2)
    sprite('vrnoef440railguntest', 32767)
    CameraFast(1)
    TeleportToObject(3)
    AddX(-1000000)
    loopRest()
    label(3)
    sprite('vrnoef440railguntest', 5)
    CameraFast(1)
    TeleportToObject(3)
    CameraPosition(1000)
    sprite('vrnoef440railguntest', 40)
    CameraFast(0)
    physicsXImpulse(53000)
    sprite('vrnoef440railguntest', 32767)
    label(4)
    sprite('vrnoef440railguntest', 40)
    physicsXImpulse(15000)
    sprite('vrnoef440railguntest', 32767)
    physicsXImpulse(0)
    label(5)
    sprite('vrnoef440railguntest', 32767)
    EndMomentum(1)
    TeleportToObject(3)
    CameraFast(1)
    label(9)
    sprite('vrnoef440railguntest', 40)

    def upon_EVERY_FRAME():
        PrivateFunction3(22, 300000, 0, 100, 0)


@State
def no440Tame():

    def upon_IMMEDIATE():
        Visibility(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(200000)
        BlendMode_Normal()
        Eff3DEffect('noef_thunder00', '')
    label(0)
    sprite('vrnoef440_tamepos', 20)
    CreateParticle('noef_440tame', 0)
    CreateParticle('noef_440tame', 1)
    gotoLabel(0)


@State
def no440TameMato2():

    def upon_IMMEDIATE():
        Visibility(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(200000)
        AddX(200000)
        BlendMode_Normal()
    label(0)
    sprite('null', 4)
    CreateObject('no440Tame2', -1)
    CreateObject('no440TameBloom', -1)
    sprite('null', 4)
    CreateObject('no440Tame3', -1)
    CreateObject('no440TameBloom', -1)
    gotoLabel(0)


@State
def no440Tame2():

    def upon_IMMEDIATE():
        Visibility(1)
        AddScaleX(1400)
        RandAddScaleY(0, 1000)
        SetScaleSpeedY(100)
        DeviationY(-50000, 12500)
        AlphaValue(160)
        BlendMode_Normal()
        Eff3DEffect('noef_thunder00', '')
    sprite('null', 6)


@State
def no440Tame3():

    def upon_IMMEDIATE():
        Visibility(1)
        AddScaleX(700)
        AddX(150000)
        RandAddScaleY(250, 500)
        SetScaleSpeedY(100)
        AlphaValue(255)
        BlendMode_Normal()
        Eff3DEffect('noef_thunder01', '')
    sprite('null', 6)


@State
def no440TameBloom():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddX(100000)
        Eff3DEffect('noef_bloomblue00', '')
        LinkParticle('noef_440tame_zentai')
        SetScaleX(750)
        RandAddScaleY(-500, 500)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def no440ShaSha():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(300000)
    sprite('null', 175)
    sprite('null', 39)
    CreateObject('no440ShaSha2', -1)


@State
def no440ShaSha2():

    def upon_IMMEDIATE():
        Visibility(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        SetScaleX(3000)
        SetScaleY(1450)
        BlendMode_Normal()
        RenderLayer(1)
    sprite('null', 39)
    Eff3DEffect('noef_shasha00', '')


@State
def no440Ring():

    def upon_IMMEDIATE():
        Visibility(1)
        RemoveOnCallStateEnd(2)
        Size(50)
        AddX(150000)
        AddY(200000)
        BlendMode_Normal()
        Eff3DEffect('noef_addcircle.DIG', '')
    sprite('null', 20)
    SetScaleSpeed(25)
    ConstantAlphaModifier(-13)


@State
def no440BombMato():

    def upon_IMMEDIATE():
        Visibility(1)
        BlendMode_Normal()
        LinkParticle('noef_440tame_beam')
    sprite('null', 3)
    sprite('null', 2)
    CreateObject('no440Bomb2', -1)

    def RunOnObject_1():
        AddX(-270000)
    sprite('null', 3)
    CreateObject('no440Bomb', -1)

    def RunOnObject_1():
        AddX(-540000)
    sprite('null', 3)
    CreateObject('no440Bomb2', -1)

    def RunOnObject_1():
        AddX(-810000)
    sprite('null', 3)
    CreateObject('no440Bomb', -1)

    def RunOnObject_1():
        AddX(-1080000)
    sprite('null', 3)
    CreateObject('no440Bomb2', -1)

    def RunOnObject_1():
        AddX(-1350000)
    sprite('null', 60)


@State
def no440BombMatoEX():

    def upon_IMMEDIATE():
        Visibility(1)
        BlendMode_Normal()
        LinkParticle('noef_440tame_beam')
    sprite('null', 3)
    sprite('null', 2)
    CreateObject('no440Bomb2', -1)

    def RunOnObject_1():
        AddX(-270000)
    sprite('null', 3)
    CreateObject('no440Bomb', -1)

    def RunOnObject_1():
        AddX(-540000)
    sprite('null', 3)
    CreateObject('no440Bomb2', -1)

    def RunOnObject_1():
        AddX(-810000)
    sprite('null', 60)


@State
def no440Bomb():

    def upon_IMMEDIATE():
        Visibility(1)
        Flip()
        BlendMode_Add()
        Size(1800)
        AddScaleY(-250)
        RandAddScaleX(-100, 100)
        AbsoluteY(0)
    sprite('null', 11)
    Eff3DEffect('noef_bomb00.DIG', '')
    CreateObject('no440RingBomb', -1)
    sprite('null', 3)
    BlendMode_Normal()
    sprite('null', 18)
    Eff3DEffect('noef_bomb01.DIG', '')
    sprite('null', 15)
    CreateParticle('noef_440bomb_smoke', -1)
    ConstantAlphaModifier(-20)


@State
def no440Bomb2():

    def upon_IMMEDIATE():
        Visibility(1)
        Flip()
        BlendMode_Add()
        Size(1800)
        AddScaleY(200)
        RandAddScaleX(-100, 100)
        AbsoluteY(0)
    sprite('null', 11)
    ScreenShake(5000, 5000)
    Eff3DEffect('noef_bomb00.DIG', '')
    CreateObject('no440RingBomb', -1)
    sprite('null', 3)
    BlendMode_Normal()
    AlphaValue(180)
    sprite('null', 18)
    Eff3DEffect('noef_bomb01.DIG', '')
    sprite('null', 15)
    ConstantAlphaModifier(-20)


@State
def no440RingBomb():

    def upon_IMMEDIATE():
        Visibility(1)
        Size(50)
        AddX(150000)
        AddY(200000)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        RotationAngle(35000)
        Eff3DEffect('noef_addcircle01.DIG', '')
    sprite('null', 5)
    SetScaleSpeed(25)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def MajuShotObj_EA():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(80)
        AirPushbackX(1400)
        AirPushbackY(16000)
        YImpulseBeforeWallbounce(500)
        AirUntechableTime(200)
        HardKnockdown(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        CHStateIfCHStart(3)
        SameMoveProration(-1)
        MinimumDamage(10)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        OnlyHitPlayer(1)
        EnableRapidCancel(0)
        IgnoreComboTime(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        ContinueState(30)
        BlendMode_Add()
        PaletteIndex(1)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 62)
        if not SLOT_51:
            Damage(140)
            AirPushbackY(16000)
            YImpulseBeforeWallbounce(1600)
    label(0)
    sprite('vrnoef430blt_00', 2)
    CreateParticle('noef430fire', -1)
    SetScaleX(1000)
    SetScaleY(750)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnoef_gunfire00', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Size(2000)
    RandRotationAngle()
    sprite('vrnoef_gunfire01', 3)
    sprite('vrnoef_gunfire02', 2)
    sprite('vrnoef_gunfire03', 2)
    sprite('vrnoef_gunfire04', 2)
    sprite('vrnoef_gunfire05', 2)
    sprite('vrnoef_gunfire06', 2)


@State
def no440WhiteOut():

    def upon_IMMEDIATE():
        RenderLayer(4)
        IgnoreScreenfreeze(1)
        AbsoluteY(900000)
        BlendMode_Normal()
        Size(20000)
        AlphaValue(0)
    sprite('vr_white', 20)
    ConstantAlphaModifier(12)
    sprite('vr_white', 30)
    sprite('vr_white', 20)
    ConstantAlphaModifier(-15)


@State
def no440WhiteOut_2():

    def upon_IMMEDIATE():
        RenderLayer(4)
        IgnoreScreenfreeze(1)
        AbsoluteY(900000)
        BlendMode_Normal()
        Size(20000)
        AlphaValue(0)
    sprite('vr_white', 20)
    ConstantAlphaModifier(12)
    sprite('vr_white', 40)
    sprite('vr_white', 20)
    ConstantAlphaModifier(-15)


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


@State
def Act2Event_Fade():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AlphaValue(0)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('null', 60)
    Size(20000)
    ColorForTransition(4278190080)
    ConstantAlphaModifier(4)
    SetBackground(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)


@State
def Act3Event_Image():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ScreenPosition(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        Size(20000)
        uponSendToLabel(32, 0)
        ColorForTransition(4278190080)
    sprite('vr_white', 30)
    AlphaValue(0)
    ConstantAlphaModifier(5)
    sprite('vr_white', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(150)
    label(0)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-5)
    sprite('vr_white', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)


@State
def Act3Event_Nagenuke():

    def upon_IMMEDIATE():
        TeleportToObject(3)
        AddX(150000)
        AddY(200000)
    sprite('null', 10)
    CreateParticle('ef_nagenuke', 103)
    CommonSE('107_throw_comeout')


@State
def Act3Event_Makoto():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        SetZVal(-750)
        TeleportToObject(22)
        AddX(-100000)
        Flip()
    label(0)
    sprite('mk000_00', 5)
    sprite('mk000_01', 5)
    sprite('mk000_02', 6)
    sprite('mk000_03', 6)
    sprite('mk000_04', 5)
    sprite('mk000_05', 5)
    sprite('mk000_06', 6)
    sprite('mk000_07', 6)
    sprite('mk000_08', 5)
    sprite('mk000_09', 5)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_RCCreate():

    def upon_IMMEDIATE():
        AddX(200000)
        LoadSpritePalette(0)
    label(0)
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
    gotoLabel(0)


@State
def Act3Event_ExclamationControl():

    def upon_IMMEDIATE():
        TeleportToObject(3)
        AddX(10000)
        AddY(430000)
    sprite('null', 2)
    CreateParticle('ef_girdmiss_m', 0)


@State
def Act3Event_HACreate():

    def upon_IMMEDIATE():
        AddX(-900000)
        LoadSpritePalette(0)
        CameraControlEnable(1)
    label(0)
    sprite('ha601_00', 6)
    sprite('ha601_01', 6)
    sprite('ha601_02', 6)
    loopRest()
    gotoLabel(0)
