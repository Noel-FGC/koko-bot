@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        BlendMode_Add()
        Size(1500)
        AddY(273000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_es.DIG', '')
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
def EMB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        BlendMode_Add()
        Size(1500)
        AddY(273000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_es.DIG', '')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 80)

@State
def EMB_ES_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        BlendMode_Add()
        Size(1500)
        AddY(273000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_es.DIG', '')
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
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        FaceSpawnLocation()
        ColorFromPaletteIndex(224)
        IgnoreScreenfreeze(1)
    sprite('null', 74)

@Subroutine
def Zanzou():
    BlendMode_Add()
    PaletteIndex(4)
    TurnParticleColorable1(1)
    PaletteEffType(2)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor1(240)
    PaletteColor4(1)

@State
def esef_kira():
    pass

@State
def esef_CmnMg():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        AlphaValue(255)
        RandAddScaleY(-200, 200)
        Eff3DEffect('esef_cmneff00', '')
    sprite('null', 60)
    SetScaleSpeedY(20)
    ConstantAlphaModifier(-4)

@State
def esef_BuffMg():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        AlphaValue(255)
        DeviationX(-50000, 50000)
        DeviationY(0, 200000)
        RandAddScaleY(-100, 100)
        Eff3DEffect('esef_cmneff00', '')
        Size(400)
        RenderLayer(11)
    sprite('null', 10)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', -1)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    physicsYImpulse(4000)
    sprite('null', 20)
    ConstantAlphaModifier(-12)

@State
def esef_201():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(194)
        callSubroutine('Zanzou')
    sprite('vresef201_00', 16)

@State
def esef_211():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(194)
        callSubroutine('Zanzou')
    sprite('vresef211_00', 16)

@State
def esef_231():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(194)
        callSubroutine('Zanzou')
    sprite('vresef231_00', 16)

@State
def esef_251():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(194)
        callSubroutine('Zanzou')
    sprite('vresef251_00', 3)
    sprite('vresef251_00', 14)
    E0EAEffectPosition(0)

@State
def esef_251_2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(194)
        callSubroutine('Zanzou')
    sprite('vresef251_10', 3)
    sprite('vresef251_10', 14)
    E0EAEffectPosition(0)

@State
def esef_202():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(170)
        callSubroutine('Zanzou')
    sprite('vresef202_00', 4)
    sprite('vresef202_01', 30)
    E0EAEffectPosition(0)

@State
def esef_232():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        IgnorePauses(3)
        AlphaValue(170)
        callSubroutine('Zanzou')
    sprite('vresef232_00', 3)
    sprite('vresef232_01', 3)
    E0EAEffectPosition(0)

@State
def esef_252():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(170)
        callSubroutine('Zanzou')
    sprite('vresef252_00', 16)

@State
def esef_235():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(11)
        callSubroutine('Zanzou')
    sprite('vresef235_00', 3)
    sprite('vresef235_01', 3)
    sprite('vresef235_02', 3)
    sprite('vresef235_03', 3)
    sprite('vresef235_04', 16)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-25)
    AddY(5000)

@State
def esef_001():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(4)
    sprite('null', 56)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('eseff_001tame_bloom')
    sprite('null', 20)
    ConstantAlphaModifier(-32)
    DespawnEAEffect('esef_001_tame_add')

@State
def esef_001_tame_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(4)
    sprite('null', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_001tame_add', -1)
    label(1)
    sprite('null', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_001tame_add2', -1)
    gotoLabel(1)

@State
def esef_212():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    LinkParticle('esef_212')
    CreateParticle('esef_212add', -1)
    sprite('null', 30)
    IgnorePauses(0)
    CreateParticle('esef_212add', -1)

@State
def esef_331():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        RotationAngle(30000)
    sprite('null', 1)
    CreateObject('esef_331_1', -1)
    CreateObject('esef_331_2', -1)
    CreateObject('esef_331_3', -1)
    CreateObject('esef_331_4', -1)
    CreateObject('esef_331_5', -1)

@State
def esef_331_add():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        E0EAEffectRotation(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_331circle_add.DIG', '')
    sprite('null', 49)

@State
def esef_331_add2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        E0EAEffectRotation(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_331circle2_add.DIG', '')
    sprite('null', 49)

@State
def esef_331_1():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_331circle2.DIG', '')
    sprite('null', 15)
    CreateObject('esef_331_add2', -1)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    Size(400)
    AddScaleSpeed(53)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(1200)
    SetScaleSpeed(0)
    sprite('null', 10)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-25)

@State
def esef_331_2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_331circle.DIG', '')
    sprite('null', 15)
    CreateObject('esef_331_add', -1)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    Size(900)
    physicsXImpulse(4000)
    physicsYImpulse(8000)
    sprite('null', 10)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-25)
    physicsXImpulse(2000)
    physicsYImpulse(4000)

@State
def esef_331_3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_331circle.DIG', '')
        RenderLayer(11)
    sprite('null', 15)
    CreateObject('esef_331_add', -1)
    AlphaValue(0)
    Size(900)
    ConstantAlphaModifier(8)
    physicsXImpulse(-4000)
    physicsYImpulse(-8000)
    sprite('null', 10)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-2000)
    physicsYImpulse(-4000)

@State
def esef_331_4():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_331circle2.DIG', '')
    sprite('null', 15)
    CreateObject('esef_331_add2', -1)
    AlphaValue(0)
    Size(300)
    ConstantAlphaModifier(17)
    AddX(50000)
    AddY(100000)
    physicsXImpulse(3000)
    physicsYImpulse(6000)
    sprite('null', 10)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-25)
    physicsXImpulse(4000)
    physicsYImpulse(8000)

@State
def esef_331_5():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_331circle2.DIG', '')
        RenderLayer(11)
    sprite('null', 15)
    CreateObject('esef_331_add2', -1)
    AlphaValue(0)
    Size(300)
    ConstantAlphaModifier(17)
    AddX(-50000)
    AddY(-100000)
    physicsXImpulse(-3000)
    physicsYImpulse(-6000)
    sprite('null', 10)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-25)
    physicsXImpulse(-4000)
    physicsYImpulse(-8000)

@State
def esef_333Eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        Visibility(1)
        Eff3DEffect('esef_333_brust00', '')
        ParticleColorFromPalette(241, 241, 241)
        CallPrivateEffect('eseff_333_tobitiri')
        Size(600)
        Rotation(-29000)
        AddY(200000)
        AddX(-200000)
        IgnoreScreenfreeze(1)
    sprite('null', 3)
    AlphaValue(0)
    sprite('null', 25)
    AlphaValue(255)
    CreateObject('esef_333EffAdd', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_333EffAdd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Visibility(1)
        Eff3DEffect('esef_333_brust00', '')
        Size(300)
        Rotation(-29000)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def esef_340():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RotationAngle(-30000)
        AddX(-6000)
        PaletteIndex(4)
    sprite('esef340_circle', 3)
    CreateObject('esef_340_circle1', -1)
    CreateObject('esef_340_circle2', -1)
    ParticleLayer(12)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 106)
    label(0)
    sprite('esef340_circle', 3)
    ParticleLayer(12)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)

@State
def esef_340_circle1():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_340circle.DIG', '')
        sendToLabelUpon(32, 0)
    sprite('null', 12)
    AlphaValue(0)
    ConstantAlphaModifier(21)
    Size(437)
    AddScaleSpeed(36)
    sprite('null', 32767)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(875)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(875)
    SetScaleSpeed(0)
    ConstantAlphaModifier(-25)
    SetScaleSpeed(50)

@State
def esef_340_circle2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_340circle2.DIG', '')
        sendToLabelUpon(32, 0)
    sprite('null', 12)
    CreateObject('esef_340_circle2Add', -1)
    AlphaValue(0)
    ConstantAlphaModifier(21)
    Size(375)
    AddScaleSpeed(31)
    AddX(27000)
    AddY(9000)
    sprite('null', 32767)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(750)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('esef_340_circle2Add', 32)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(750)
    SetScaleSpeed(0)
    ConstantAlphaModifier(-25)
    SetScaleSpeed(50)

@State
def esef_340_circle2Add():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_340circle2add.DIG', '')
        sendToLabelUpon(32, 0)
    sprite('null', 12)
    AlphaValue(0)
    ConstantAlphaModifier(21)
    Size(375)
    AddScaleSpeed(31)
    AddX(27000)
    AddY(9000)
    sprite('null', 32767)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(750)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 5)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    Size(750)
    SetScaleSpeed(0)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(50)

@State
def esef_340_blade():

    def upon_IMMEDIATE():
        AddY(200000)
        AddX(50000)
        IgnorePauses(3)
    sprite('null', 10)
    CreateObject('esef_340_blade_color', -1)
    CreateObject('esef_340_blade_add', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 240)
    CallCustomizableParticle('esef_340crash', -1)
    sprite('null', 15)

@State
def esef_340_blade_color():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        FaceSpawnLocation()
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        RotationAngle(75000)
        Size(1400)
        AddScaleX(650)
        Visibility(1)
    sprite('null', 2)
    Eff3DEffect('esef_340blade_start.DIG', '')
    sprite('null', 4)
    Eff3DEffect('esef_340blade.DIG', '')
    sprite('vresef340_ParitclePos', 10)
    ConstantAlphaModifier(-25)
    SetScaleXPerFrame(7)
    SetScaleSpeedY(14)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)

@State
def esef_340_blade_add():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Size(1400)
        CancelIfPlayerHit(3)
        FaceSpawnLocation()
        RotationAngle(75000)
        AddScaleX(650)
    sprite('null', 2)
    Eff3DEffect('esef_340blade_start.DIG', '')
    sprite('null', 4)
    Eff3DEffect('esef_340blade.DIG', '')
    IgnorePauses(2)
    sprite('null', 9)
    Eff3DEffect('esef_340blade_end.DIG', '')
    ConstantAlphaModifier(-51)
    SetScaleXPerFrame(-7)
    SetScaleSpeedY(14)

@State
def esef_340_zanzou():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        callSubroutine('Zanzou')
    sprite('vresef340_00', 1)
    sprite('vresef340_00', 16)
    ConstantAlphaModifier(-25)

@State
def eseff_DTame():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        ParticleColorFromPalette(240, 240, 240)
        CallPrivateEffect('eseff_203tame')
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@Subroutine
def Monsho_AtkData():
    AttackLevel_(1)
    Damage(740)
    AttackP1(80)
    AttackP2(89)
    Hitstop(9)
    Hitstun(17)
    AirUntechableTime(21)
    Blockstun(11)
    UseSlashHitspark(1)
    StarterRating(2)

@State
def esef_203Add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_203slash_02Add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def esef_203():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectObjectZ(2)
        Visibility(1)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        SetScaleX(1250)
        SetScaleY(1200)
    sprite('vresef203_ParitclePos', 1)
    IgnoreFinishStop(1)
    Eff3DEffect('esef_203slash_00.DIG', '')
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 0)
    sprite('vresef203_ParitclePos', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 1)
    sprite('vresef203_ParitclePos', 1)
    Eff3DEffect('esef_203slash_01.DIG', '')
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 2)
    sprite('vresef203_ParitclePos', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('vresef203_ParitclePos', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 4)
    sprite('vresef203_ParitclePos', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('null', 10)
    Eff3DEffect('esef_203slash_02.DIG', '')
    CreateObject('esef_203Add', -1)
    IgnorePauses(2)
    IgnoreFinishStop(0)
    sprite('null', 12)
    Eff3DEffect('esef_203slash_03.DIG', '')
    DespawnEAEffect('esef_203Add')
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    IgnoreScreenfreeze(1)

@State
def es203_effAtk_Yotyou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_203slash_yotyou00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        RenderLayer(15)
        SetScaleX(1250)
        SetScaleY(1200)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    label(0)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-13)
    sprite('null', 10)
    ConstantAlphaModifier(13)
    gotoLabel(0)

@State
def esef_203Monsho():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_203slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        AddY(40000)
        AddX(45000)
        RotationAngle(7500)
    sprite('null', 5)
    CreateObject('esef_203MonshoAdd', 100)
    ScreenShake(5000, 5000)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnoreFinishStop(0)
    IgnorePauses(2)
    sprite('vresef203_ParitclePos', 10)
    DespawnEAEffect('esef_203MonshoAdd')
    Eff3DEffect('esef_203slashAddAtk_01.DIG', '')
    ConstantAlphaModifier(-25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    IgnoreScreenfreeze(1)

@State
def esef_203MonshoAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        Eff3DEffect('esef_203slashAddAtk_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def es203_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
    sprite('null', 15)
    sprite('null', 5)
    CreateObject('es203_effAtk_Yotyou', -1)
    RegisterObject(11, 1)
    label(0)
    sprite('null', 4)
    clearUponHandler(32)
    clearUponHandler(33)
    DeleteObject(11)
    CreateObject('esef_203Monsho', 100)
    PrivateSE('esse_01')
    sprite('es203_effatk', 3)
    sprite('null', 50)

@State
def es203_effAtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
        PerScale(120)
    sprite('null', 15)
    sprite('null', 5)
    label(0)
    sprite('null', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 4)
    CreateObject('esef_203Monsho', 100)
    ApplyFunctionsToObjects(1)
    PerScale(120)
    ApplyFunctionsToSelf()
    sprite('es203_effatk', 3)
    sprite('null', 50)

@State
def esef_213Add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_213slash_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def esef_213():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_213slash_00.DIG', '')
        Visibility(1)
        Size(950)
        AbsoluteY(12000)
    sprite('vresef213_ParitclePos', 15)
    CreateObject('esef_213Add', -1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('null', 15)
    Eff3DEffect('esef_213slashEnd.DIG', '')
    DespawnEAEffect('esef_213Add')
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    IgnoreScreenfreeze(1)

@State
def es213_effAtk_Yotyou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_213slash_yotyou00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        RenderLayer(15)
        Size(850)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    label(0)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-13)
    sprite('null', 10)
    ConstantAlphaModifier(13)
    gotoLabel(0)

@State
def esef_213Monsho():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_213slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(950)
        AbsoluteY(12000)
    sprite('null', 5)
    ScreenShake(5000, 5000)
    CreateObject('esef_213MonshoAdd', 100)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnorePauses(2)
    IgnoreFinishStop(0)
    sprite('vresef213_ParitclePos', 10)
    Eff3DEffect('esef_213slashAddAtk_01.DIG', '')
    DespawnEAEffect('esef_213MonshoAdd')
    ConstantAlphaModifier(-25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    IgnoreScreenfreeze(1)

@State
def esef_213MonshoAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_213slashAddAtk_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def es213_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    sprite('null', 30)
    CreateObject('es213_effAtk_Yotyou', -1)
    RegisterObject(11, 1)
    label(0)
    sprite('null', 3)
    clearUponHandler(32)
    clearUponHandler(33)
    DeleteObject(11)
    CreateObject('esef_213Monsho', -1)
    PrivateSE('esse_01')
    sprite('es213_effatk', 3)
    sprite('null', 50)

@State
def es213_effAtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
        PerScale(120)
    sprite('null', 20)
    sprite('null', 30)
    label(0)
    sprite('null', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 3)
    CreateObject('esef_213Monsho', -1)
    ApplyFunctionsToObjects(1)
    PerScale(120)
    ApplyFunctionsToSelf()
    sprite('es213_effatk', 3)
    sprite('null', 50)

@State
def esef_233Add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_233slash_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def esef_233():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_233slash_00.DIG', '')
        Visibility(1)
        Size(950)
        AbsoluteY(12000)
    sprite('vresef233_ParitclePos', 15)
    CreateObject('esef_233Add', -1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('null', 15)
    Eff3DEffect('esef_233slash_01.DIG', '')
    DespawnEAEffect('esef_233Add')
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    IgnoreScreenfreeze(1)

@State
def es233_effAtk_Yotyou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_233slash_yotyou00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        RenderLayer(15)
        Size(850)
        AddScaleX(200)
        AddX(-200000)
        AddY(25000)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    label(0)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-13)
    sprite('null', 10)
    ConstantAlphaModifier(13)
    gotoLabel(0)

@State
def esef_233Monsho():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_233slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(950)
        AbsoluteY(12000)
        AddX(-50000)
    sprite('null', 5)
    ScreenShake(5000, 5000)
    CreateObject('esef_233MonshoAdd', 100)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnoreFinishStop(0)
    IgnorePauses(2)
    sprite('vresef213_ParitclePos', 10)
    Eff3DEffect('esef_233slashAddAtk_01.DIG', '')
    DespawnEAEffect('esef_233MonshoAdd')
    ConstantAlphaModifier(-25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    IgnoreScreenfreeze(1)

@State
def esef_233MonshoAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_233slashAddAtk_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def es233_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    sprite('null', 60)
    CreateObject('es233_effAtk_Yotyou', -1)
    RegisterObject(11, 1)
    label(0)
    sprite('null', 3)
    clearUponHandler(32)
    clearUponHandler(33)
    DeleteObject(11)
    CreateObject('esef_233Monsho', -1)
    PrivateSE('esse_01')
    sprite('es233_effatk', 3)
    sprite('null', 50)

@State
def es233_effAtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
        PerScale(120)
    sprite('null', 20)
    sprite('null', 60)
    label(0)
    sprite('null', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 3)
    CreateObject('esef_233Monsho', -1)
    ApplyFunctionsToObjects(1)
    PerScale(120)
    ApplyFunctionsToSelf()
    sprite('es233_effatk', 3)
    sprite('null', 50)

@State
def esef_253_wari():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_253slash_00.DIG', '')
        Visibility(1)
        RenderLayer(1)
        AddY(250000)
        Size(750)
    sprite('null', 32767)

@State
def esef_253_wari2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_253slash_01.DIG', '')
        Visibility(1)
        RenderLayer(1)
        AddY(250000)
        Size(750)
    sprite('null', 32767)

@State
def esef_253Add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_253slash_02add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def esef_253():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_253slash_02.DIG', '')
        Visibility(1)
        RenderLayer(15)
        AddY(250000)
        Size(750)
    sprite('vresef253_ParitclePos', 10)
    IgnoreScreenfreeze(1)
    CreateObject('esef_253Add', -1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 9)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 10)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('eseff_cmngarass', 11)
    sprite('null', 15)
    Eff3DEffect('esef_253slash_03.DIG', '')
    DespawnEAEffect('esef_253Add')
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)

@State
def es253_effAtk_Yotyou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_253slash_yotyou00.DIG', '')
        E0EAEffectPosition(2)
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        RenderLayer(15)
        Size(1200)
        AddY(250000)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    label(0)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-13)
    sprite('null', 10)
    ConstantAlphaModifier(13)
    gotoLabel(0)

@State
def esef_253Monsho():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_253slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        AddY(250000)
        Size(1100)
    sprite('null', 5)
    IgnoreFinishStop(1)
    ScreenShake(5000, 5000)
    CreateObject('esef_253MonshoAdd', 100)
    sprite('null', 10)
    IgnoreFinishStop(0)
    IgnorePauses(2)
    sprite('vresef213_ParitclePos', 10)
    DespawnEAEffect('esef_253MonshoAdd')
    ConstantAlphaModifier(-25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    IgnoreScreenfreeze(1)

@State
def esef_253MonshoAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_253slashAddAtk_00add.DIG', '')
        BlendMode_Add()
    sprite('null', 32767)

@State
def es253_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        AttackDirection(1)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    sprite('null', 95)
    CreateObject('es253_effAtk_Yotyou', -1)
    RegisterObject(11, 1)
    label(0)
    sprite('null', 3)
    clearUponHandler(32)
    clearUponHandler(33)
    DeleteObject(11)
    CreateObject('esef_253Monsho', -1)
    PrivateSE('esse_01')
    sprite('es253_effatk', 3)
    sprite('null', 50)

@State
def es253_effAtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        AttackDirection(1)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            DeleteObject(23)

        def upon_33():
            DeleteObject(23)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    sprite('null', 95)
    label(0)
    sprite('null', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 3)
    CreateObject('esef_253Monsho', -1)
    ApplyFunctionsToObjects(1)
    PerScale(120)
    ApplyFunctionsToSelf()
    sprite('es253_effatk', 3)
    sprite('null', 50)

@State
def esef_ThrowEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_311_mc00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        RenderLayer(15)
        TeleportToObject(22)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Size(50)
    SetScaleSpeed(95)
    sprite('null', 32767)
    SetScaleSpeed(1)
    label(0)
    sprite('null', 25)
    RemoveOnCallStateEnd(0)
    CreateObject('esef_ThrowEffAtk', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)

@State
def esef_ThrowEffAtk():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_311_mc01.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        TeleportToObject(22)
        Size(500)
        AddScaleY(200)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    CreateObject('esef_ThrowEffImpact', -1)
    CreateObject('esef_ThrowEffAtkAdd', -1)
    sprite('vresef311_ParticlePos', 10)
    ConstantAlphaModifier(-26)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)

@State
def esef_ThrowEffAtkAdd():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_311_mc01add.DIG', '')
        BlendMode_Add()
        Visibility(1)
        TeleportToObject(22)
        Size(500)
        AddScaleY(200)
        IgnoreScreenfreeze(1)
    sprite('null', 15)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_ThrowEffImpact():

    def upon_IMMEDIATE():
        IgnoreFinishStop(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('esef_cmnbigimpact00.DIG', '')
        BlendMode_Add()
        Size(250)
        AddY(10000)
    sprite('null', 5)
    Size(300)
    SetScaleSpeed(95)
    sprite('null', 5)
    SetScaleSpeed(10)
    IgnoreFinishStop(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def esef_BackThrowEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_311_mc00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        RenderLayer(15)
        TeleportToObject(22)
        AddY(200000)
        RotationAngle(-65000)
        IgnoreScreenfreeze(1)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    SetScaleX(200)
    SetScaleY(800)
    SetScaleSpeed(95)
    sprite('null', 32767)
    SetScaleSpeed(1)
    label(0)
    sprite('null', 25)
    AlphaValue(150)
    RemoveOnCallStateEnd(0)
    CreateObject('esef_BackThrowEffAtk', -1)
    CreateObject('esef_BackThrowEffAtkAdd', -1)
    CreateObject('esef_BackThrowEffAtkSub', -1)
    CreateObject('esef_BackThrowEffAtk2', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)

@State
def esef_BackThrowEffAtk():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_313_mc00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(1000)
        AddX(-100000)
        AddScaleX(400)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    ScreenShake(10000, 10000)
    sprite('vresef313_ParticlePos', 10)
    ConstantAlphaModifier(-26)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 9)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 10)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 11)

@State
def esef_BackThrowEffAtkAdd():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_313_mc00add.DIG', '')
        BlendMode_Add()
        Visibility(1)
        Size(1000)
        AddScaleX(400)
        AddX(-100000)
        IgnoreScreenfreeze(1)
    sprite('null', 19)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_BackThrowEffAtkSub():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_313_mc00.DIG', '')
        BlendMode_Sub()
        Visibility(1)
        Size(1000)
        AddScaleX(400)
        AddX(-100000)
        IgnoreScreenfreeze(1)
        RenderLayer(15)
        AlphaValue(100)
    sprite('null', 19)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_BackThrowEffAtk2():

    def upon_IMMEDIATE():
        Eff3DEffect('esef_313_mc00back.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(1000)
        AddScaleX(400)
        RenderLayer(15)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    AlphaValue(100)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_402EffKidou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_402kidou01.DIG', '')
        BlendMode_Add()
        Visibility(1)
        sendToLabelUpon(33, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 15)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-17)
    loopRest()

@State
def esef_402EffAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        Eff3DEffect('esef_402slash_00add.DIG', '')
        BlendMode_Add()
        Visibility(1)
        E0EAEffectPosition(2)
        sendToLabelUpon(33, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)
    loopRest()

@State
def esef_402Eff():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        CancelIfPlayerHit(2)
        Eff3DEffect('esef_402slash_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        AddX(100000)
        SetScaleY(700)
        SetScaleX(1000)
        Visibility(1)
    sprite('es402_effatk1', 24)
    CreateObject('esef_402EffAdd', -1)
    CreateObject('esef_402EffKidou', -1)
    CreateObject('esef_402EffParticle', -1)
    sprite('null', 2)
    Eff3DEffect('esef_402slash_01.DIG', '')
    PassbackAddActionMarkToFunction('esef_402EffAdd', 33)
    PassbackAddActionMarkToFunction('esef_402EffKidou', 33)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-8)
    sprite('null', 2)
    Eff3DEffect('esef_402slash_02.DIG', '')
    sprite('null', 2)
    Eff3DEffect('esef_402slash_03.DIG', '')
    sprite('null', 2)
    Eff3DEffect('esef_402slash_04.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_05.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_06.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_07.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_08.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_09.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_10.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_11.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_12.DIG', '')
    sprite('null', 1)
    Eff3DEffect('esef_402slash_13.DIG', '')

@State
def esef_402EffParticle():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(4)
        AddX(100000)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 9)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 10)
    sprite('vresef402_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 11)

@State
def esef_402EffAddAtk():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_402slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        AddX(100000)
        SetScaleY(700)
        SetScaleX(1000)
        Visibility(1)
    sprite('null', 15)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_402EffAddAtkadd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_402slashAddAtk_00add.DIG', '')
        BlendMode_Add()
        AddX(100000)
        SetScaleY(700)
        SetScaleX(1000)
        Visibility(1)
    sprite('null', 15)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_402Eff2C():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_402_2Ceff.DIG', '')
        AddY(300000)
        AddScaleX(300)
    sprite('null', 15)
    IgnoreFinishStop(1)
    CreateObject('esef_402Eff2CAdd', 100)
    sprite('vresef402_2CParitclePos', 2)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-13)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    sprite('vresef402_2CParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    sprite('vresef402_2CParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    sprite('vresef402_2CParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('vresef402_2CParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    sprite('vresef402_2CParitclePos', 10)

@State
def esef_402Eff2CAdd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
        Eff3DEffect('esef_402_2Ceffadd.DIG', '')
        AddScaleX(300)
    sprite('null', 15)
    IgnoreFinishStop(1)
    sprite('null', 19)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-13)

@State
def es402_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('Monsho_AtkData')
        Damage(800)
        AttackP1(60)
        AttackP2(100)
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        AirPushbackY(18000)
        PushbackX(19800)
        Unknown12052(1)
        CancelIfPlayerHit(3)
        AddX(150000)
        AddY(400000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 21)
    sprite('null', 5)
    CreateObject('esef_402EffAddAtk', -1)
    CreateObject('esef_402EffAddAtkadd', -1)
    ScreenShake(5000, 5000)
    PrivateSE('esse_01')
    sprite('es402_effatk', 6)
    sprite('null', 10)

@State
def esef_402_zanzou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        callSubroutine('Zanzou')
    sprite('vresef402_00', 3)
    sprite('vresef402_01', 2)
    ConstantAlphaModifier(-16)

@State
def esef_405EffAdd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        Visibility(1)
        Eff3DEffect('esef_405slash_00add.DIG', '')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 15)
    Eff3DEffect('esef_405slash_01.DIG', '')
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    loopRest()

@State
def esef_405Eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_405slash_00.DIG', '')
        Size(4600)
        SetScaleZ(500)
        AddY(200000)
    sprite('null', 5)
    CreateObject('esef_405EffAdd', -1)
    sprite('null', 10)
    E0EAEffectPosition(0)
    sprite('null', 20)
    CreateObject('esef_405EffSlaskParticle', -1)
    PassbackAddActionMarkToFunction('esef_405EffAdd', 32)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_405EffSlaskParticle():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(4)
        Size(800)
    sprite('vresef405_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)

@State
def esef_405EffEX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_405slash_00.DIG', '')
        Size(4600)
        SetScaleZ(500)
        AddY(200000)
    sprite('null', 5)
    CreateObject('esef_405EffAdd', -1)
    sprite('null', 5)
    E0EAEffectPosition(0)
    CreateObject('esef_405EffAddAtk', -1)
    CreateObject('es405_effAtk', -1)
    ScreenShake(5000, 5000)
    PrivateSE('esse_01')
    sprite('null', 10)
    DespawnEAEffect('esef_405EffAdd')
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_405EffAddAtk():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_405slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Size(3400)
        SetScaleZ(500)
        Visibility(1)
        RenderLayer(12)
        AddX(50000)
    sprite('null', 25)
    CreateObject('esef_405EffAddAtkadd', -1)
    ScreenShake(10000, 10000)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('esef_405EffAddAtkadd', 32)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_405EffAddAtkadd():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('esef_405slashAddAtk_00add.DIG', '')
        E0EAEffectScale(2)
        BlendMode_Add()
        Visibility(1)
        RenderLayer(12)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    label(0)
    sprite('null', 10)
    CreateObject('esef_405EffAddAtkParticle', -1)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_405EffAddAtkParticle():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(4)
    sprite('vresef405_ParitclePos', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 9)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 10)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 11)

@State
def es405_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('Monsho_AtkData')
        Damage(800)
        AttackP1(70)
        AttackP2(100)
        AirUntechableTime(40)
        Unknown12052(1)
        AddX(70000)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 12)
    sprite('es405_effatk', 6)
    sprite('null', 10)

@State
def esef_406Eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_406slash_00.DIG', '')
        AddY(200000)
        Size(800)
        sendToLabelUpon(32, 0)

        def upon_33():
            SetActionMark(1)

        def upon_56():
            IgnorePauses(0)
    sprite('null', 20)
    CreateObject('esef_406Effadd', -1)
    loopRest()
    SpriteCall('null', 40, 2, 2)
    label(0)
    sprite('null', 20)
    clearUponHandler(32)
    CreateObject('esef_406EffAddAtkParticle', -1)
    Eff3DEffect('esef_406slash_00end.DIG', '')
    DespawnEAEffect('esef_406Effadd')
    ConstantAlphaModifier(-12)

@State
def esef_406Effadd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        Visibility(1)
        Eff3DEffect('esef_406slash_00end.DIG', '')
        Size(800)

        def upon_33():
            SetActionMark(1)

        def upon_56():
            IgnorePauses(0)
    sprite('null', 20)
    loopRest()
    SpriteCall('null', 40, 2, 2)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_406Eff2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_406slash_01.DIG', '')
        AddY(200000)
        AddX(-50000)
        Size(800)
    sprite('null', 25)
    CreateObject('esef_406Effadd2', -1)
    sprite('null', 20)
    PassbackAddActionMarkToFunction('esef_406Eff', 32)
    Eff3DEffect('esef_406slash_01end.DIG', '')
    CreateObject('esef_406EffAddAtkParticle2', -1)
    ApplyFunctionsToObjects(1)
    AddX(-150000)
    AddY(-200000)
    ApplyFunctionsToSelf()
    DespawnEAEffect('esef_406Effadd2')
    ConstantAlphaModifier(-12)

@State
def esef_406Effadd2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Visibility(1)
        Eff3DEffect('esef_406slash_01end.DIG', '')
        Size(800)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def esef_406EffEX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_406slash_00.DIG', '')
        AddY(200000)
        Size(800)
        sendToLabelUpon(32, 0)

        def upon_33():
            SetActionMark(1)

        def upon_56():
            IgnorePauses(0)
    sprite('null', 20)
    CreateObject('esef_406Effadd', -1)
    loopRest()
    SpriteCall('null', 40, 2, 2)
    label(0)
    sprite('null', 10)
    clearUponHandler(32)
    CreateObject('esef_406EffAddAtk', 100)
    if (not SLOT_2):
        CreateObject('es406_effAtk', -1)
    PrivateSE('esse_01')
    sprite('null', 20)
    Eff3DEffect('esef_406slash_00end.DIG', '')
    CreateObject('esef_406EffAddAtkParticle', -1)
    ConstantAlphaModifier(-12)

@State
def esef_406Eff2EX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        Visibility(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_406slash_01.DIG', '')
        AddY(200000)
        AddX(-50000)
        Size(800)
    sprite('null', 15)
    CreateObject('esef_406Effadd2', -1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('esef_406EffEX', 32)
    CreateObject('esef_406EffAddAtk2', 100)
    CreateObject('es407_effAtk', -1)
    sprite('null', 20)
    Eff3DEffect('esef_406slash_01end.DIG', '')
    CreateObject('esef_406EffAddAtkParticle2', -1)
    ConstantAlphaModifier(-12)

@State
def esef_406EffAddAtk():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_406slashAddAtk_00.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(800)
    sprite('null', 25)
    CreateObject('esef_406EffAddAtkadd', -1)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('esef_406EffAddAtkadd', 32)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_406EffAddAtkadd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_406slashAddAtk_00add.DIG', '')
        BlendMode_Add()
        Visibility(1)
        Size(800)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    label(0)
    sprite('null', 10)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_406EffAddAtk2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_406slashAddAtk_01.DIG', '')
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Visibility(1)
        Size(800)
    sprite('null', 25)
    CreateObject('esef_406EffAddAtkadd2', -1)
    ScreenShake(10000, 10000)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    DespawnEAEffect('esef_406Effadd')
    sprite('null', 10)
    PassbackAddActionMarkToFunction('esef_406EffAddAtkadd2', 32)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_406EffAddAtkadd2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('esef_406slashAddAtk_01add.DIG', '')
        BlendMode_Add()
        Visibility(1)
        Size(800)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    RemoveOnCallStateEnd(0)
    IgnoreFinishStop(1)
    label(0)
    sprite('null', 10)
    IgnoreFinishStop(0)
    RemoveOnCallStateEnd(0)
    ConstantAlphaModifier(-25)

@State
def esef_406EffAddAtkParticle():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(4)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('vresef406_ParitclePos', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)

@State
def esef_406EffAddAtkParticle2():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(4)
        AddX(150000)
    sprite('vresef406_ParitclePos2', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    sprite('vresef406_ParitclePos2', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    sprite('vresef406_ParitclePos2', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('vresef406_ParitclePos2', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    sprite('vresef406_ParitclePos2', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    sprite('vresef406_ParitclePos2', 2)

@State
def es406_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('Monsho_AtkData')
        Damage(800)
        AttackP1(70)
        AttackP2(100)
        AirPushbackX(8000)
        AirPushbackY(22000)
        AirUntechableTime(40)
        PushbackX(19800)
        Unknown12052(1)
        CancelIfPlayerHit(3)
        ScreenShake(5000, 5000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('es406_effatk', 6)
    sprite('null', 15)

@State
def es407_effAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('Monsho_AtkData')
        Damage(800)
        AttackP1(70)
        AttackP2(100)
        GroundedHitstunAnimation(2)
        Crumple(36)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(24000)
        AirUntechableTime(55)
        PushbackX(19800)
        Unknown12052(1)
        CancelIfPlayerHit(3)
        ScreenShake(5000, 5000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 7)
    sprite('es407_effatk', 6)
    sprite('null', 15)

@State
def esef_408Eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ParticleColorFromPalette(241, 241, 241)
        CallPrivateEffect('eseff_4083tame_jizoku')
        Eff3DEffect('esef_408_MCircle00.DIG', '')
        Visibility(1)
        AddY(25000)
        AddPositionZ(25000)
    sprite('null', 18)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleXPerFrame(20)
    SetScaleSpeedZ(20)

@Subroutine
def es400_Init():
    AttackDefaults_SpecialProjectile()
    AttackLevel_(2)
    Damage(800)
    AttackP1(80)
    AirPushbackX(12000)
    AirPushbackY(12000)
    AirUntechableTime(20)
    Hitstun(17)
    Hitstop(8)
    PushbackX(8000)
    Unknown12052(1)
    UseSlashHitspark(1)
    CancelIfPlayerHit(3)
    HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

    def upon_54():
        clearUponHandler(33)
        DeleteObject(23)
        ObjectUpon(4, 32)
    if SLOT_137:
        DamageMultiplier(80)
    callSubroutine('es400_Delete')

@Subroutine
def es400_Delete():

    def upon_FRAME_STEP():
        if SLOT_38:
            PrivateFunction5(125)
            if (SLOT_22 < SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                DeleteObject(23)
                DeleteObject(4)
        else:
            PrivateFunction5(125)
            if (SLOT_22 > SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                DeleteObject(23)
                DeleteObject(4)

@State
def es400_A():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        AddY(128000)
        AddX(100000)
    sprite('es400eff_atk1', 3)
    CreateObject('esef_400eff_MatomeA', -1)
    RegisterObject(4, 1)
    physicsXImpulse(45000)
    SetAcceleration(-1300)
    PrivateSE('esse_03')
    sprite('es400eff_atk2', 27)
    PassbackAddActionMarkToFunction('shot', 32)
    sprite('null', 1)
    ObjectUpon(4, 33)

@State
def es400_B():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        AddY(128000)
        AddX(100000)

        def upon_32():
            NoAttackDuringAction(1)
    sprite('null', 3)
    CreateObject('esef_400eff_MatomeB', -1)
    RegisterObject(4, 1)
    physicsXImpulse(2500)
    PrivateSE('esse_03')
    sprite('es400eff_atk1', 22)
    clearUponHandler(32)
    sprite('es400eff_atk2', 100)
    PassbackAddActionMarkToFunction('shot', 32)
    physicsXImpulse(70000)

@State
def es400_A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddY(128000)
        AddX(110000)
    sprite('es400eff_atk1', 3)
    CreateObject('esef_400eff2nd_MatomeA', -1)
    RegisterObject(4, 1)
    physicsXImpulse(45000)
    SetAcceleration(-1300)
    sprite('es400eff_atk2', 27)
    PassbackAddActionMarkToFunction('shot2', 32)
    sprite('null', 1)
    ObjectUpon(4, 33)

@State
def es400_A_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddY(128000)
        AddX(110000)
    sprite('es400eff_atk1', 3)
    CreateObject('esef_400eff2nd_MatomeA', -1)
    RegisterObject(4, 1)
    physicsXImpulse(45000)
    SetAcceleration(-1300)
    sprite('es400eff_atk2', 27)
    PassbackAddActionMarkToFunction('shot2', 32)
    sprite('null', 1)
    ObjectUpon(4, 33)

@State
def es400_B_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddY(128000)
        AddX(110000)

        def upon_33():
            CreateObject('es400_B_2ndEX', -1)
            DespawnEAEffect('es400_A')
            DespawnEAEffect('esef_400eff_MatomeA')
            DeleteObject(23)
            DespawnEAEffect('esef_400eff2nd_MatomeB')
            DespawnEAEffect('esef_400eff2nd_MatomeB2')
    CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)
    CreateObject('esef_400eff2nd_MatomeB', -1)
    RegisterObject(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)
    CreateObject('esef_400eff2nd_MatomeB2', -1)
    RegisterObject(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)

@State
def es400_B_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddY(128000)
        AddX(110000)

        def upon_33():
            CreateObject('es400_B_2ndEX', -1)
            DespawnEAEffect('es400_A')
            DespawnEAEffect('esef_400eff_MatomeA')
            DeleteObject(23)
            DespawnEAEffect('esef_400eff2nd_MatomeB')
            DespawnEAEffect('esef_400eff2nd_MatomeB2')
    CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)
    CreateObject('esef_400eff2nd_MatomeB', -1)
    RegisterObject(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)
    CreateObject('esef_400eff2nd_MatomeB2', -1)
    RegisterObject(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)

@State
def es400_A_2ndEX():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        ProjectileLevel(2)
        Damage(1200)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(36000)
        AirPushbackY(12000)
        AirUntechableTime(36)
        Floorslide(10)
        Hitstop(11)
        ResetPushbackX()
        Unknown12052(1)
        UseSlashHitspark(1)
        AddY(128000)
        AddX(50000)
        CancelIfPlayerHit(3)
        HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            DeleteObject(23)
            ObjectUpon(4, 32)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
        DespawnEAEffect('es400_B')
        DespawnEAEffect('esef_400eff_MatomeB')
    sprite('es400eff_largeatk1', 3)
    CreateObject('esef_400eff_EX', -1)
    RegisterObject(4, 1)
    physicsXImpulse(70000)
    PrivateSE('esse_03')
    sprite('es400eff_largeatk2', 100)

@State
def es400_B_2ndEX():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        ProjectileLevel(2)
        Damage(1200)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(36000)
        AirPushbackY(12000)
        AirUntechableTime(36)
        Floorslide(10)
        Hitstop(11)
        ResetPushbackX()
        Unknown12052(1)
        UseSlashHitspark(1)
        AddX(-50000)
        CancelIfPlayerHit(3)
        HitsPerCall(1, 0, 0, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            DeleteObject(23)
            ObjectUpon(4, 32)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('es400eff_largeatk2', 103)
    CreateObject('esef_400eff_EX', -1)
    RegisterObject(4, 1)
    physicsXImpulse(70000)

@State
def es401_A():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        AddX(100000)
        AddY(80000)
        RotationAngle(42000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            clearUponHandler(2)
            DeleteObject(23)
            ObjectUpon(4, 33)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff_MatomeA', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot', 32)

@State
def es401_B():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        AddX(100000)
        AddY(140000)
        RotationAngle(5000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            Unknown23090(23)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff_MatomeB', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot', 32)

@State
def es401_A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddX(60000)
        AddY(70000)
        RotationAngle(42000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            Unknown23090(23)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff2nd_MatomeA', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)

@State
def es401_B_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddX(100000)
        AddY(140000)
        RotationAngle(5000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            Unknown23090(23)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff2nd_MatomeB', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)

@State
def es401_A_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddX(60000)
        AddY(70000)
        RotationAngle(42000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            Unknown23090(23)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff2nd_MatomeA', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)

@State
def es401_B_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        ResetPushbackX()
        AddX(100000)
        AddY(140000)
        RotationAngle(5000)
        XSpeed2(35000, 0)
        LandingHeight(20000)

        def upon_LANDING():
            Unknown23090(23)
    sprite('es400eff_airatk1', 3)
    CreateObject('esef_400Aireff2nd_MatomeB', -1)
    RegisterObject(4, 1)
    sprite('es400eff_airatk2', 100)
    PassbackAddActionMarkToFunction('shot2', 32)

@State
def esef_400Aura():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_cmneff01.DIG', '')
        Visibility(1)
        AddPositionZ(25000)
        RandAddRotation(-10000, 10000)
        DeviationX(-50000, 50000)
        DeviationY(-50000, 50000)
        Size(2500)
        AddScaleX(1000)
        IgnoreScreenfreeze(1)
    sprite('null', 45)
    AlphaValue(128)
    SetScaleSpeed(20)
    ConstantAlphaModifier(-2)

@State
def esef_400eff_MatomeA():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot', -1)
    CreateObject('shot_add', -1)
    CreateObject('esef_400_zanzo', -1)
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)
    ExitState()
    label(2)
    sprite('keep', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    physicsXImpulse(4500)
    ConstantAlphaModifier(-42)
    SetScaleSpeed(-50)

@State
def esef_400eff_MatomeB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 105)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 25)
    CreateObject('shot', -1)
    CreateObject('shot_add', -1)
    CreateObject('esef_400_zanzo', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)

@State
def esef_400eff2nd_MatomeA():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot2', -1)
    CreateObject('shot2_add', -1)
    CreateObject('esef_400_zan2', -1)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    PaletteIndex(4)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)
    ExitState()
    label(2)
    sprite('keep', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    physicsXImpulse(4500)
    ConstantAlphaModifier(-42)
    SetScaleSpeed(-50)

@State
def esef_400eff2nd_MatomeB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 105)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 25)
    CreateObject('shot2', -1)
    CreateObject('shot2_add', -1)
    CreateObject('esef_400_zan2', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)

@State
def esef_400eff2nd_MatomeB2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot2', -1)
    CreateObject('shot2_add', -1)
    CreateObject('esef_400_zan2', -1)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)

@State
def esef_400eff_EX():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 103)

        def upon_17():
            DeleteObject(23)
    sprite('esef400_Expoint3', 3)
    CreateObject('largeshot', -1)
    CreateObject('largeshot_add', -1)
    CreateObject('esef_400large_zan', -1)
    label(0)
    sprite('esef400_Expoint4', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_Expoint4', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_Expoint4', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_Expoint4', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('keep', 12)
    clearUponHandler(32)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    SetScaleSpeed(-50)

@State
def esef_400Aireff_MatomeA():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot', -1)
    CreateObject('shot_add', -1)
    CreateObject('esef_400_zanzo', -1)
    ObjectUpon(1, 32)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    ApplyFunctionsToObjects(1)
    Rotation(35000)
    ApplyFunctionsToSelf()
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-405000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-405000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-405000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-405000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-21)
    ExitState()
    label(2)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-42)

@State
def esef_400Aireff_MatomeB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot', -1)
    CreateObject('shot_add', -1)
    CreateObject('esef_400_zanzo', -1)
    ObjectUpon(1, 33)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    ApplyFunctionsToObjects(1)
    Rotation(5000)
    ApplyFunctionsToSelf()
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-80000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-80000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-80000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-80000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('null', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    ExitState()
    label(2)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-42)

@State
def esef_400Aireff2nd_MatomeA():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot2', -1)
    CreateObject('shot2_add', -1)
    CreateObject('esef_400_zan2', -1)
    ObjectUpon(1, 32)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)
    CreateObject('esef_400Aura', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    sprite('esef400_EXpoint2', 5)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('null', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-21)
    ExitState()
    label(2)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-42)

@State
def esef_400Aireff2nd_MatomeB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        NoAttackDuringAction(1)
        RunLoopUpon(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)
    CreateObject('shot2', -1)
    CreateObject('shot2_add', -1)
    CreateObject('esef_400_zan2', -1)
    ObjectUpon(1, 33)
    PrivateSE('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 4)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    ParticleRotationAngle(-80000)
    CallCustomizableParticle('eseff_cmngarass', 106)
    gotoLabel(0)
    label(1)
    sprite('null', 12)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end', -1)
    ConstantAlphaModifier(-21)
    ExitState()
    label(2)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(17)
    CreateObject('shot_end2', -1)
    ConstantAlphaModifier(-42)

@State
def shot():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_400shot_NoJet.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)
    label(0)
    sprite('null', 32767)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_400shot.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)

@State
def shot_add():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400shot_add.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)

@State
def shot_sub():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400shot_sub.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)

@State
def shot_end():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        Visibility(1)
        Size(700)
        E0EAEffectRotation(2)
    sprite('vresef400_ParitclePos00', 1)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleRotationAngle(-90000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 10)
    ParticleRotationAngle(-90000)

@State
def shot_end2():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        Visibility(1)
        Size(700)
        E0EAEffectRotation(2)
    sprite('vresef400_ParitclePos00', 1)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleRotationAngle(-45000)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 10)

@State
def shot_test():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 60)
    Eff3DEffect('esef_400shot_test.DIG', '')
    FaceSpawnLocation()

@State
def shot2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_400shot2_NoJet.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)
    label(0)
    sprite('null', 32767)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_400shot2.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)

@State
def shot2_add():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400shot2_add.DIG', '')
    FaceSpawnLocation()

@State
def shot2_sub():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400shot2_sub.DIG', '')
    FaceSpawnLocation()
    AlphaValue(0)
    ConstantAlphaModifier(32)

@State
def largeshot():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_400largeshot.DIG', '')
    FaceSpawnLocation()

@State
def largeshot_add():

    def upon_IMMEDIATE():
        BlendMode_Add()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400largeshot_add.DIG', '')
    FaceSpawnLocation()

@State
def largeshot_sub():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
    sprite('null', 32767)
    Eff3DEffect('esef_400largeshot_sub.DIG', '')
    FaceSpawnLocation()

@State
def esef_400_zanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)

        def upon_32():
            RotationAngle(42000)
            SLOT_51 = 1

        def upon_33():
            RotationAngle(5000)
            SLOT_52 = 1
    label(1)
    sprite('null', 2)
    CreateObject('esef_400_zan_a', -1)
    if SLOT_51:
        ObjectUpon(1, 32)
    elif SLOT_52:
        ObjectUpon(1, 33)
    gotoLabel(1)

@State
def esef_400_zan_a():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)

        def upon_32():
            RotationAngle(42000)

        def upon_33():
            RotationAngle(5000)
    sprite('null', 7)
    PaletteIndex(4)
    ColorFromPaletteIndex(240)
    Eff3DEffect('esef_400shot_NoJet.DIG', '')
    FaceSpawnLocation()
    AlphaValue(90)
    ConstantAlphaModifier(-12)

@State
def esef_400_zan2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)

        def upon_32():
            RotationAngle(42000)
            SLOT_51 = 1

        def upon_33():
            RotationAngle(5000)
            SLOT_52 = 1
    label(1)
    sprite('null', 2)
    CreateObject('esef_400_zan2_a', -1)
    if SLOT_51:
        ObjectUpon(1, 32)
    elif SLOT_52:
        ObjectUpon(1, 33)
    gotoLabel(1)

@State
def esef_400_zan2_a():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)

        def upon_32():
            RotationAngle(42000)

        def upon_33():
            RotationAngle(5000)
    sprite('null', 5)
    PaletteIndex(4)
    ColorFromPaletteIndex(240)
    Eff3DEffect('esef_400shot2_NoJet.DIG', '')
    FaceSpawnLocation()
    AlphaValue(90)
    ConstantAlphaModifier(-15)
    SetScaleSpeed(20)

@State
def esef_400large_zan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
    label(1)
    sprite('null', 2)
    CreateObject('esef_400large_zan_a', -1)
    gotoLabel(1)

@State
def esef_400large_zan_a():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectRotation(2)
    sprite('null', 5)
    PaletteIndex(4)
    ColorFromPaletteIndex(240)
    Eff3DEffect('esef_400largeshot.DIG', '')
    FaceSpawnLocation()
    AlphaValue(90)
    ConstantAlphaModifier(-15)
    SetScaleSpeed(20)

@State
def esef_400_zanzou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        callSubroutine('Zanzou')
    sprite('vresef400_00', 20)

@State
def esef_400_zanzou2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        callSubroutine('Zanzou')
    sprite('vresef400_10', 20)

@State
def esef_401_zanzou():

    def upon_IMMEDIATE():
        callSubroutine('Zanzou')
    sprite('vresef401_00', 20)

@State
def esef_401_zanzou2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        callSubroutine('Zanzou')
    sprite('vresef401_10', 30)

@State
def esef_404_kick():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou')
        AddY(45000)
    sprite('vresef404_00', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    sprite('vresef404_01', 5)
    sprite('vresef404_01', 12)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)

@State
def esef_404_kick_BDD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou')
        AddY(-40000)
    sprite('vresef404_00', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    sprite('vresef404_01', 4)
    E0EAEffectPosition(0)
    sprite('vresef404_02', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)

@State
def esef_409():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
    sprite('esef409', 1)
    CreateObject('esef_409_kick', -1)
    CreateObject('esef_409_kick_add', -1)
    CreateObject('esef_409_circle', -1)
    CreateObject('esef_409_dust', -1)

@State
def esef_409_kick():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        Size(1100)
    sprite('null', 5)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_409kick.DIG', '')
    FaceSpawnLocation()
    sprite('null', 10)
    ConstantAlphaModifier(-25)

@State
def esef_409_kick_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        Size(1100)
    sprite('null', 5)
    Eff3DEffect('esef_409kick_add.DIG', '')
    FaceSpawnLocation()
    sprite('null', 10)
    ConstantAlphaModifier(-25)

@State
def esef_409_circle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(4)
        Size(1050)
    sprite('null', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallPrivateEffect('esef_409circle')
    sprite('null', 10)
    ConstantAlphaModifier(-25)

@State
def esef_409_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(4)
        AddY(-65000)
    sprite('null', 7)
    sprite('null', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('esef_409dust', -1)

@State
def esef_409_3rd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('esef409_3rd', 10)
    Visibility(1)
    CreateObject('esef_409_3rd_kick', -1)
    CreateObject('esef_409_3rd_kick_add', -1)
    PaletteIndex(4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    sprite('esef409_3rd', 20)
    E0EAEffectPosition(0)

@State
def esef_409_3rd_kick():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Size(1500)
        AddY(225000)
    sprite('null', 10)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_409kick2.DIG', '')
    FaceSpawnLocation()
    sprite('null', 10)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-25)

@State
def esef_409_3rd_kick_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Size(1500)
        AddY(225000)
    sprite('null', 10)
    Eff3DEffect('esef_409kick2_add.DIG', '')
    FaceSpawnLocation()
    sprite('null', 10)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-25)

@State
def esef_440EffAsiba():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        IgnoreScreenfreeze(1)
        Eff3DEffect('esef_311_mc00.DIG', '')
        Size(200)
        RenderLayer(11)
    sprite('null', 3)
    SetScaleSpeed(50)
    AlphaValue(128)
    sprite('null', 10)
    SetScaleSpeed(1)
    sprite('null', 10)
    ConstantAlphaModifier(-13)

@State
def esef_440():
    sprite('esef440', 6)
    Size(1250)
    Visibility(1)
    CreateObject('esef_440_sword', -1)
    CreateObject('esef_440_sword_add', -1)
    PaletteIndex(4)
    ParticleSize(1250)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('esef_440circle', -1)
    ParticleColorFromPalette(242, 241, 241)
    CallCustomizableParticle('esef_440circle_b', -1)
    sprite('esef440', 1)
    CreateObject('esef_440_sword_aura', -1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 9)

@State
def esef_440_sp():
    sprite('esef440', 6)
    Visibility(1)
    Size(1500)
    CreateObject('esef_440_sword', -1)
    CreateObject('esef_440_sword_add', -1)
    PaletteIndex(4)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('esef_440circle', -1)
    ParticleColorFromPalette(242, 241, 241)
    CallCustomizableParticle('esef_440circle_b', -1)
    sprite('esef440', 1)
    CreateObject('esef_440_sword_aura', -1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 7)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 9)

@State
def esef_440_sword():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        AddY(-75000)
        RenderLayer(15)
        sendToLabelUpon(32, 0)
    sprite('null', 100)
    PaletteIndex(4)
    ColorFromPaletteIndex(241)
    Eff3DEffect('esef_440sword.DIG', '')
    FaceSpawnLocation()
    label(0)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def esef_440_sword_add():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        AddY(-75000)
        RenderLayer(15)
        sendToLabelUpon(32, 0)
    sprite('null', 100)
    Eff3DEffect('esef_440sword_add.DIG', '')
    FaceSpawnLocation()
    label(0)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def esef_440_sword_aura():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Size(800)
        AddScaleX(200)
        BlendMode_Add()
        AddY(-75000)
        RenderLayer(15)
    sprite('null', 45)
    ConstantAlphaModifier(-5)
    Eff3DEffect('esef_440sword_aura.DIG.DIG', '')
    FaceSpawnLocation()

@State
def es403_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(600)
        AttackP1(60)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(1000)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(50)
        AirHitstunAfterWallbounce(60)
        Unknown12052(1)
        UseSlashHitspark(1)
        WallCollisionDetection(1)
        AddX(200000)
        AddY(150000)
        CancelIfPlayerHit(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 5)
    CreateObject('esef_402Eff2C', -1)
    ApplyFunctionsToObjects(1)
    AddX(10000)
    ApplyFunctionsToSelf()
    sprite('es403_effatk', 8)
    sprite('null', 60)

@State
def esef_430EffStartOD():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        AddY(310000)
        AddX(288000)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        SetScaleX(1500)
        SetScaleY(2200)
        Visibility(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 32767)
    CreateObject('esef_430EffStartODhikari', -1)
    Eff3DEffect('esef_430eff00', '')
    label(0)
    sprite('vresef430_ParitclePos', 32767)
    PassbackAddActionMarkToFunction('esef_430EffStartODhikari', 32)
    Eff3DEffect('esef_430eff01', '')
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 0)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 1)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 2)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 3)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 4)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 5)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('eseff_cmngarass', 6)
    label(1)
    sprite('null', 4)
    DespawnEAEffect('esef_430EffStartODhikari')
    ScreenShake(10000, 10000)
    CreateObject('esef_430EffStartAdd', -1)
    Eff3DEffect('esef_430eff02', '')
    sprite('null', 6)
    Eff3DEffect('esef_430eff03', '')
    DespawnEAEffect('esef_430EffStartAdd')
    sprite('null', 20)
    ConstantAlphaModifier(-12)

@State
def esef_430EffStartODhikari():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        PaletteIndex(4)
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        Visibility(1)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Eff3DEffect('esef_430eff00', '')
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)
    ConstantAlphaModifier(-26)
    label(0)
    sprite('null', 5)
    Eff3DEffect('esef_430eff01', '')
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)
    ConstantAlphaModifier(-26)

    @State
    def esef_430EffStart():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(310000)
            AddX(288000)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            AlphaValue(255)
            SetScaleX(1500)
            SetScaleY(2200)
            Visibility(1)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
        sprite('null', 32767)
        Eff3DEffect('esef_430eff00', '')
        label(0)
        sprite('vresef430_ParitclePos', 32767)
        Eff3DEffect('esef_430eff01', '')
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 5)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 6)
        label(1)
        sprite('null', 4)
        ScreenShake(10000, 10000)
        CreateObject('esef_430EffStartAdd', -1)
        Eff3DEffect('esef_430eff02', '')
        sprite('null', 6)
        Eff3DEffect('esef_430eff03', '')
        DespawnEAEffect('esef_430EffStartAdd')
        sprite('null', 20)
        ConstantAlphaModifier(-12)

    @State
    def esef_430EffStartAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            IgnoreScreenfreeze(1)
            E0EAEffectScale(2)
            RemoveOnCallStateEnd(2)
            E0EAEffectRotation(2)
            AlphaValue(255)
        sprite('null', 4)
        ScreenShake(10000, 10000)
        Eff3DEffect('esef_430eff02add', '')
        sprite('null', 25)
        SetScaleSpeed(10)

    @State
    def esef_430Eff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(230000)
            AddX(350000)
            Size(1300)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
        sprite('null', 4)
        AlphaValue(0)
        Eff3DEffect('esef_430eff00shot', '')
        label(0)
        sprite('null', 5)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_430_grass', -1)
        AlphaValue(255)
        gotoLabel(0)

    @State
    def esef_430EffAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            AddY(230000)
            AddX(350000)
            Size(1300)
        sprite('null', 4)
        AlphaValue(0)
        Eff3DEffect('esef_430eff00shot', '')
        sprite('null', 32767)
        AlphaValue(255)
        Eff3DEffect('esef_430eff00shotAdd', '')

    @Subroutine
    def es430_Init():
        CancelIfPlayerHit(3)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(2200)
        MinimumDamage(30)
        AttackP1(70)
        AttackP2(72)
        Hitstop(6)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(45000)
        PushbackX(50000)
        AirUntechableTime(40)
        Unknown12052(1)
        UseSlashHitspark(1)
        StarterRating(0)
        ContinueState(60)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(125)
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    DeleteObject(23)
            else:
                PrivateFunction5(125)
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    DeleteObject(23)
        if SLOT_137:
            DamageMultiplier(80)

    @Subroutine
    def es430OD_Init():
        CancelIfPlayerHit(3)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(2200)
        MinimumDamage(30)
        AttackP1(70)
        AttackP2(72)
        SingleProration(1)
        Hitstop(1)
        EnemyHitstopAddition(-1, -1, -1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(90000)
        AirPushbackY(10000)
        PushbackX(70000)
        AirUntechableTime(40)
        Unknown12052(1)
        UseSlashHitspark(1)
        HitsparkSize(500)
        StarterRating(0)
        AttackType(4)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SetActionMark(1)

        def upon_45():
            if SLOT_2:
                Damage(220)
                if SLOT_137:
                    DamageMultiplier(80)
        ContinueState(60)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(125)
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    DeleteObject(23)
            else:
                PrivateFunction5(125)
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    DeleteObject(23)
        HitsPerCall(10, 1, 1, 1, 1, 0, 10, 10)
        sendToLabelUpon(54, 580)
        if SLOT_137:
            DamageMultiplier(80)

    @State
    def es430LandA():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
            sendToLabelUpon(54, 580)
        sprite('null', 4)
        CreateObject('esef_430Eff', -1)
        CreateObject('esef_430EffAdd', -1)
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk1', 3)
        physicsXImpulse(70000)
        sprite('es430_LandAtk2', 60)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def es430LandB():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            AirPushbackX(40000)
            AirPushbackY(40000)
            AddX(-50000)
            AddY(50000)
            RotationAngle(345000)
            HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
            sendToLabelUpon(54, 580)
        sprite('null', 4)
        CreateObject('esef_430Eff', -1)
        ApplyFunctionsToObjects(1)
        RotationAngle(346000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAdd', -1)
        ApplyFunctionsToObjects(1)
        RotationAngle(346000)
        ApplyFunctionsToSelf()
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk3', 3)
        XSpeed2(70000, 0)
        sprite('es430_LandAtk4', 60)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def esef_430EffOD():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(230000)
            AddX(350000)
            Size(1300)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
        sprite('null', 4)
        AlphaValue(0)
        Eff3DEffect('esef_430eff00shot', '')
        label(0)
        sprite('null', 6)
        CreateObject('esef_430EffODnokosi', -1)
        CreateObject('esef_430EffAddNokosi', -1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_430_grass', -1)
        AlphaValue(255)
        gotoLabel(0)

    @State
    def esef_430EffODnokosi():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(240)
            Size(1300)
            AlphaValue(160)
            RemoveOnCallStateEnd(2)
            RenderLayer(15)
        sprite('null', 1)
        E0EAEffectRotation(2)
        sprite('null', 20)
        ConstantAlphaModifier(-8)
        Eff3DEffect('esef_430eff00shotAddnokosi', '')

    @State
    def esef_430EffAddNokosi():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            Size(800)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(-300000)
        sprite('null', 3)
        CreateParticle('eseff_430_odparticle', -1)
        Eff3DEffect('esef_430eff_od00', '')
        sprite('null', 20)
        ConstantAlphaModifier(-12)
        SetScaleSpeedY(-20)

    @State
    def es430LandAOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
        sprite('null', 4)
        CreateObject('esef_430EffOD', -1)
        CreateObject('esef_430EffAdd', -1)
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk1', 2)
        physicsXImpulse(70000)
        label(0)
        sprite('es430_LandAtk1', 2)
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def es430LandBOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            AirPushbackX(60000)
            AirPushbackY(30000)
            AddX(-50000)
            AddY(50000)
            RotationAngle(345000)
        sprite('null', 4)
        CreateObject('esef_430EffAddNokosiAir', -1)
        ApplyFunctionsToObjects(1)
        RotationAngle(346000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAirOD', -1)
        ApplyFunctionsToObjects(1)
        RotationAngle(346000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAdd', -1)
        ApplyFunctionsToObjects(1)
        RotationAngle(346000)
        ApplyFunctionsToSelf()
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk3', 2)
        XSpeed2(70000, 0)
        label(0)
        sprite('es430_LandAtk3', 2)
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def esef_430EffAsiba():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_311_mc00.DIG', '')
            Size(200)
            RenderLayer(11)
            sendToLabelUpon(32, 0)
        sprite('null', 5)
        SetScaleSpeed(100)
        AlphaValue(128)
        sprite('null', 32767)
        SetScaleSpeed(1)
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-13)

    @State
    def esef_430EffStartAir():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(310000)
            AddX(360000)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            AlphaValue(255)
            SetScaleX(1500)
            SetScaleY(2200)
            Visibility(1)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
        sprite('null', 32767)
        Eff3DEffect('esef_430eff00', '')
        label(0)
        sprite('vresef430_ParitclePos', 32767)
        Eff3DEffect('esef_430eff01', '')
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 5)
        ParticleSize(1500)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 6)
        label(1)
        sprite('null', 4)
        ScreenShake(10000, 10000)
        CreateObject('esef_430EffStartAddAir', -1)
        Eff3DEffect('esef_430eff02', '')
        sprite('null', 25)
        SetScaleSpeed(10)

    @State
    def esef_430EffStartAddAir():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            IgnoreScreenfreeze(1)
            E0EAEffectScale(2)
            RemoveOnCallStateEnd(2)
            AlphaValue(255)
        sprite('null', 4)
        ScreenShake(10000, 10000)
        Eff3DEffect('esef_430eff02add', '')
        sprite('null', 25)
        SetScaleSpeed(10)

    @State
    def es430AirA():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
            sendToLabelUpon(54, 580)
        sprite('null', 4)
        CreateObject('esef_430Eff', -1)
        CreateObject('esef_430EffAdd', -1)
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk1', 3)
        physicsXImpulse(70000)
        sprite('es430_LandAtk2', 60)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def es430AirB():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            RotationAngle(10000)
            HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
            sendToLabelUpon(54, 580)
        sprite('null', 4)
        CreateObject('esef_430Eff', -1)
        ApplyFunctionsToObjects(1)
        Rotation(11000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAdd', -1)
        ApplyFunctionsToObjects(1)
        Rotation(11000)
        ApplyFunctionsToSelf()
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_AirAtk1', 3)
        XSpeed2(70000, 0)
        sprite('es430_AirAtk2', 60)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def esef_430EffAirOD():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(230000)
            AddX(350000)
            Size(1300)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
        sprite('null', 4)
        AlphaValue(0)
        Eff3DEffect('esef_430eff00shot', '')
        label(0)
        sprite('null', 6)
        CreateObject('esef_430EffODnokosi', -1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_430_grass', -1)
        AlphaValue(255)
        gotoLabel(0)

    @State
    def esef_430EffAddNokosiAir():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            Size(800)
            AddScaleX(200)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            Eff3DEffect('esef_431eff01od2', '')
            AddY(250000)
            AddX(290000)
            E0EAEffectPosition(2)
            RemoveOnCallStateEnd(2)
        label(0)
        sprite('null', 4)
        ParticleRotationAngle(11000)
        ParticleSize(1400)
        CallCustomizableParticle('eseff_430_odparticleAir', -1)
        gotoLabel(0)

    @State
    def es430AirAOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            AirPushbackY(20000)
        sprite('null', 4)
        CreateObject('esef_430EffAddNokosiAir', -1)
        CreateObject('esef_430EffAirOD', -1)
        CreateObject('esef_430EffAdd', -1)
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_LandAtk1', 2)
        physicsXImpulse(70000)
        label(0)
        sprite('es430_LandAtk1', 2)
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def es430AirBOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            RotationAngle(10000)
        sprite('null', 4)
        CreateObject('esef_430EffAddNokosiAir', -1)
        ApplyFunctionsToObjects(1)
        Rotation(11000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAirOD', -1)
        ApplyFunctionsToObjects(1)
        Rotation(11000)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffAdd', -1)
        ApplyFunctionsToObjects(1)
        Rotation(11000)
        ApplyFunctionsToSelf()
        PrivateSE('esse_04')
        PrivateSE('esse_04')
        sprite('es430_AirAtk1', 2)
        XSpeed2(70000, 0)
        label(0)
        sprite('es430_LandAtk3', 2)
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)
        clearUponHandler(54)

    @State
    def esef_431Eff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            IgnorePauses(2)
            RemoveOnCallStateEnd(3)
            Unknown4022(2)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 2)
            AddY(200000)
            AddX(200000)
        sprite('null', 32767)
        CreateObject('esef_431Emb', -1)
        CreateObject('esef_431EffSub', -1)
        label(0)
        sprite('esef431_03', 1)
        CreateObject('esef_431Tossin', -1)
        Visibility(1)
        Size(1200)
        PassbackAddActionMarkToFunction('esef_431Emb', 32)
        PassbackAddActionMarkToFunction('esef_431EffSub', 32)
        IgnoreScreenfreeze(1)
        SetScaleXPerFrame(15)
        EnableAfterimage(1)
        label(1)
        sprite('esef431_03', 2)
        CreateObject('esef_431EmbNokosi', -1)
        gotoLabel(1)
        label(2)
        sprite('esef431_04', 10)
        PassbackAddActionMarkToFunction('esef_431Tossin', 32)
        ConstantAlphaModifier(-31)

    @State
    def esef_431Emb():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            RemoveOnCallStateEnd(3)
            sendToLabelUpon(32, 0)
            AddX(70000)
        sprite('null', 10)
        Size(50)
        SetScaleSpeed(75)
        Eff3DEffect('esef_431eff_emb00', '')
        CreateObject('esef_431EmbAdd', -1)
        sprite('null', 32767)
        SetScaleSpeed(1)
        label(0)
        sprite('null', 5)
        SetScaleSpeed(50)
        sprite('null', 20)
        RenderLayer(15)
        PassbackAddActionMarkToFunction('esef_431EmbAdd', 32)
        ConstantAlphaModifier(-12)
        SetScaleSpeed(5)
        Unknown4022(0)
        RemoveOnCallStateEnd(0)

    @State
    def esef_431EmbAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(3)
            E0EAEffectScale(2)
            sendToLabelUpon(32, 0)
        sprite('null', 32767)
        Eff3DEffect('esef_431eff_emb00', '')
        label(0)
        sprite('null', 20)
        RenderLayer(15)
        ConstantAlphaModifier(-12)
        SetScaleSpeed(5)
        RemoveOnCallStateEnd(0)

    @State
    def esef_431EffSub():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(2)
            sendToLabelUpon(32, 0)
            Size(2000)
        sprite('null', 32767)
        LinkParticle('eseff_431gen')
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-25)

    @State
    def esef_431EmbNokosi():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            RenderLayer(15)
        sprite('null', 10)
        Eff3DEffect('esef_431eff_emb01', '')
        ConstantAlphaModifier(-25)
        SetScaleSpeed(20)

    @State
    def esef_431Tossin():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(2)
            Eff3DEffect('esef_431_tossin00', '')
            sendToLabelUpon(32, 0)
            Size(800)
            AddScaleY(200)
        sprite('null', 5)
        CreateObject('esef_431TossinAdd', -1)
        SetScaleSpeedY(-5)
        sprite('null', 32767)
        ConstantAlphaModifier(13)
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-25)

    @State
    def esef_431TossinAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            E0EAEffectScale(2)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            Eff3DEffect('esef_431_tossin00add', '')
            sendToLabelUpon(32, 0)
        sprite('null', 5)
        sprite('null', 10)
        ConstantAlphaModifier(26)

    @State
    def esef_431Camera():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            IgnoreScreenfreeze(1)
            CameraControlEnable(1)
            CameraPosition(900)
            sendToLabelUpon(32, 0)
        sprite('null', 300)

    @State
    def esef_431Eff2():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
        sprite('esef431_20', 5)
        sprite('esef431_11', 3)
        AddX(-300000)
        ScreenShake(10000, 10000)
        E0EAEffectPosition(0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        sprite('esef431_11', 3)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        sprite('esef431_12', 6)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('esef431_13', 6)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('esef431_14', 5)
        sprite('esef431_15', 5)

    @State
    def esef_431EffSlash():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            AddY(180000)
        sprite('null', 60)
        ParticleColorFromPalette(241, 241, 241)
        CallPrivateEffect('eseff_431_slash')

    @State
    def esef_431EffSlashOD():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            AddY(180000)
        sprite('null', 80)
        CreateObject('esef_431EffSlashODCorol', -1)
        CallPrivateEffect('eseff_431_slashOD')

    @State
    def esef_431EffSlashODCorol():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            SetScaleY(2000)
        sprite('null', 60)
        ParticleColorFromPalette(241, 241, 241)
        CallPrivateEffect('eseff_431_slash01')

    @State
    def esef_431EffScrew():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            Eff3DEffect('esef_431eff01', '')
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(200000)
            AddX(200000)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            AddScaleY(1100)
            AddScaleZ(1100)
        sprite('null', 14)
        sprite('null', 5)
        ConstantAlphaModifier(-51)

    @State
    def esef_431EffScrewOD():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Eff3DEffect('esef_431eff01od', '')
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            AddY(200000)
            AddX(300000)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            AddScaleY(1080)
            AddScaleZ(1320)
            AlphaValue(128)
        sprite('null', 6)
        CreateObject('esef_431EffMcOD', -1)
        SetScaleSpeedY(-20)
        SetScaleSpeedZ(-20)
        sprite('null', 6)
        CreateObject('esef_431EffMcOD', -1)
        sprite('null', 6)
        CreateObject('esef_431EffMcOD', -1)
        sprite('null', 6)
        CreateObject('esef_431EffMcOD', -1)
        sprite('null', 9)
        CreateObject('esef_431EffMcOD', -1)
        sprite('null', 19)
        ConstantAlphaModifier(-6)

    @State
    def esef_431EffMcOD():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Eff3DEffect('esef_431eff01od_circle', '')
            IgnoreScreenfreeze(1)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            AlphaValue(0)
            RotationAngle(-20000)
        sprite('null', 5)
        ConstantAlphaModifier(40)
        physicsXImpulse(-12500)
        sprite('null', 5)
        ConstantAlphaModifier(0)
        physicsXImpulse(-35000)
        SetScaleSpeed(50)
        sprite('null', 10)
        ConstantAlphaModifier(-25)

    @State
    def esef_431EffEsRay():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Eff3DEffect('esef_431esRay00', '')
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            Size(2435)
            AlphaValue(200)
            AddY(15000)
        sprite('null', 19)
        CreateObject('esef_431EffEsRayColor', -1)
        sprite('null', 10)
        sprite('null', 10)
        ConstantAlphaModifier(-20)

    @State
    def esef_431EffEsRayColor():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Eff3DEffect('esef_431esRay00', '')
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            E0EAEffectScale(2)
            PaletteIndex(4)
            ColorFromPaletteIndex(240)
        sprite('null', 24)
        sprite('null', 15)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_431_rayend', -1)

    @State
    def esef_432Camera():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            IgnoreScreenfreeze(1)
            CameraControlEnable(1)
            CameraPosition(860)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
        sprite('null', 32767)
        label(0)
        sprite('null', 20)
        physicsYImpulse(10000)
        sprite('null', 10)
        physicsYImpulse(0)
        sprite('null', 32767)
        CameraPosition(1000)
        label(1)
        sprite('null', 1)
        CameraPosition(1000)
        CameraNoScreenCollision(0)
        CameraControlEnable(0)

    @State
    def esef_408Eff2():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            E0EAEffectPosition(2)
            RemoveOnCallStateEnd(2)
            ParticleColorFromPalette(241, 241, 241)
            CallPrivateEffect('eseff_4083tame_jizoku')
            Eff3DEffect('esef_408_MCircle00.DIG', '')
            Visibility(1)
            AddY(20000)
            AddPositionZ(25000)
            IgnoreScreenfreeze(1)
        sprite('null', 30)
        sprite('null', 5)
        ConstantAlphaModifier(-51)

    @State
    def esef_432Eff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            RemoveOnCallStateEnd(2)
            IgnoreScreenfreeze(1)
            AlphaValue(255)
            EnableAfterimage(1)
            AfterimageCount(2)
        sprite('vresef432_00', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        sprite('vresef432_01', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        sprite('vresef432_02', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        sprite('vresef432_03', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_04', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_05', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_06', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_07', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_08', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_09', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        sprite('vresef432_10', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef432_11', 4)
        sprite('vresef432_12', 6)
        AddY(-50000)
        sprite('vresef432_12', 2)
        AddY(-25000)
        sprite('vresef432_12', 2)
        AddY(-25000)
        PrivateSE('esse_10')
        sprite('vresef432_13', 4)
        sprite('vresef432_14', 4)
        sprite('vresef432_15', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_432shock00', 0)
        AlphaValue(255)
        ScreenShake(5000, 5000)
        sprite('vresef432_15ex01', 5)
        AddY(500000)
        AddX(-5000)
        AddRotationPerFrame(-2500)
        sprite('vresef432_15ex01', 10)
        AddRotationPerFrame(-7800)
        sprite('vresef432_15ex01', 5)
        physicsYImpulse(24000)
        AddRotationPerFrame(0)
        sprite('vresef432_15ex01', 3)
        physicsYImpulse(0)

    @State
    def esef_43EsRayEff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
        sprite('vresef432_16', 5)
        sprite('vresef432_16', 5)
        ConstantAlphaModifier(-51)

    @State
    def esef_432RayEff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ParticleColorFromPalette(241, 241, 241)
            CallPrivateEffect('eseff_432shockRay')
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            Size(900)
        sprite('null', 5)
        sprite('null', 25)
        CreateObject('esef_432RayEffSub', -1)
        sprite('null', 5)
        ConstantAlphaModifier(-51)

    @State
    def esef_432RayEffSub():

        def upon_IMMEDIATE():
            CallPrivateEffect('eseff_432sordsub')
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            Size(900)
        sprite('null', 15)
        sprite('null', 5)
        ConstantAlphaModifier(-51)

    @State
    def es_ChageAuraGenerator():

        def upon_IMMEDIATE():

            def upon_FRAME_STEP():
                SLOT_51 = (SLOT_51 + 1)
                if (not op(4, 2, 51, 0, 20)):
                    SLOT_52 = 0
                    CopyFromRightToLeft(23, 2, 52, 2, 2, 30)
                    if (not SLOT_52):
                        ApplyFunctionsToObjects(3)
                        CreateObject('esef_BuffMg', -1)
                        ApplyFunctionsToSelf()
        sprite('null', 32767)

    @State
    def es432_ChageEff():

        def upon_IMMEDIATE():
            E0EAEffectPosition(3)
            CancelIfPlayerHit(3)
            Size(600)
            IgnoreScreenfreeze(1)
        sprite('null', 30)
        LinkParticle('ef_ukemi')

    @State
    def BurstDD_Camera():

        def upon_IMMEDIATE():
            CameraControlEnable(1)
            CameraNoScreenCollision(1)
            CancelIfPlayerHit(3)
            E0EAEffectDirection(3)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
            sendToLabelUpon(34, 2)
            sendToLabelUpon(35, 3)
            sendToLabelUpon(36, 4)
            sendToLabelUpon(37, 5)
        sprite('null', 600)
        loopRest()
        gotoLabel(5)
        label(0)
        sprite('null', 18)
        RemoveOnCallStateEnd(3)
        AddY(630000)
        physicsYImpulse(30000)
        sprite('null', 1000)
        EndMomentum(1)
        loopRest()
        gotoLabel(5)
        label(1)
        sprite('null', 1000)
        TeleportToObject(3)
        AddY(200000)
        AddX(130000)
        loopRest()
        gotoLabel(5)
        label(2)
        sprite('null', 1)
        sprite('null', 35)
        physicsYImpulse(-70000)
        sprite('null', 1000)
        EndMomentum(1)
        loopRest()
        gotoLabel(5)
        label(3)
        sprite('null', 5)
        physicsYImpulse(40000)
        physicsXImpulse(20000)
        sprite('null', 8)
        physicsXImpulse(0)
        sprite('null', 1000)
        EndMomentum(1)
        loopRest()
        gotoLabel(5)
        label(4)
        sprite('null', 4)
        sprite('null', 15)
        physicsYImpulse(-120000)
        sprite('null', 1000)
        EndMomentum(1)
        loopRest()
        gotoLabel(5)
        label(5)
        sprite('null', 1)
        CameraNoScreenCollision(0)
        CameraControlEnable(0)

    @State
    def AstralHeat_Camera():

        def upon_IMMEDIATE():
            CameraControlEnable(1)
            CameraNoScreenCollision(1)
            CancelIfPlayerHit(3)
            RemoveOnCallStateEnd(3)
            E0EAEffectDirection(3)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
            sendToLabelUpon(34, 2)
            sendToLabelUpon(35, 3)
            sendToLabelUpon(36, 4)
        sprite('null', 32767)
        label(0)
        sprite('null', 2)
        CameraPosition(950)
        sprite('null', 2)
        CameraPosition(900)
        sprite('null', 2)
        CameraPosition(850)
        sprite('null', 2)
        CameraPosition(800)
        sprite('null', 2)
        CameraPosition(750)
        sprite('null', 32767)
        CameraPosition(700)
        label(1)
        sprite('null', 2)
        CameraPosition(750)
        AddX(30000)
        sprite('null', 2)
        CameraPosition(800)
        AddX(30000)
        sprite('null', 2)
        CameraPosition(850)
        AddX(30000)
        AddY(300000)
        sprite('null', 2)
        CameraPosition(900)
        AddX(30000)
        AddY(50000)
        sprite('null', 2)
        CameraPosition(950)
        AddX(30000)
        AddY(50000)
        sprite('null', 2)
        CameraPosition(1000)
        AddX(30000)
        AddY(50000)
        sprite('null', 2)
        CameraPosition(1100)
        AddX(30000)
        AddY(50000)
        sprite('null', 2)
        CameraPosition(1200)
        AddX(30000)
        AddY(50000)
        sprite('null', 44)
        CameraPosition(1300)
        AddX(30000)
        AddY(50000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 10)
        AddY(100000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 2)
        AddY(100000)
        sprite('null', 1000)
        AddY(100000)
        loopRest()
        gotoLabel(4)
        label(2)
        sprite('null', 1000)
        CameraFast(1)
        XPositionRelativeFacing(-880000)
        AbsoluteY(1500000)
        loopRest()
        gotoLabel(4)
        label(3)
        sprite('null', 2)
        sprite('null', 6)
        IgnorePauses(2)
        CameraFast(0)
        physicsXImpulse(170000)
        physicsYImpulse(-220000)
        sprite('null', 1000)
        IgnorePauses(0)
        EndMomentum(1)
        label(4)
        sprite('null', 1)
        CameraControlEnable(0)
        CameraNoScreenCollision(0)
        CameraPosition(1000)

    @State
    def esef_430EffSlashAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            E0EAEffectScale(2)
        sprite('null', 4)
        AlphaValue(0)
        ConstantAlphaModifier(8)
        Eff3DEffect('esef_450_slm00', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm01', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm02', '')
        sprite('null', 4)
        Eff3DEffect('esef_450_slm03', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm04', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm05', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm06', '')
        sprite('null', 10)
        Eff3DEffect('esef_450_slm07', '')
        sprite('null', 10)
        ConstantAlphaModifier(-25)

    @State
    def esef_430EffSlash():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            Size(2500)
        sprite('null', 4)
        AlphaValue(0)
        ConstantAlphaModifier(63)
        CreateObject('esef_430EffSlashAdd', -1)
        Eff3DEffect('esef_450_slm00', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm01', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm02', '')
        sprite('null', 4)
        Eff3DEffect('esef_450_slm03', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm04', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm05', '')
        sprite('null', 3)
        Eff3DEffect('esef_450_slm06', '')
        sprite('null', 10)
        Eff3DEffect('esef_450_slm07', '')
        sprite('null', 30)
        ConstantAlphaModifier(-8)
        CreateObject('esef_430EffNokosi', -1)

    @State
    def esef_430EffNokosi():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            IgnoreScreenfreeze(1)
            E0EAEffectPosition(2)
            Visibility(1)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 1)
        CreateObject('esef_CmnMg', 1)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 2)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 3)
        CreateObject('esef_CmnMg', 3)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 4)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 5)
        CreateObject('esef_CmnMg', 5)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 6)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 7)
        CreateObject('esef_CmnMg', 7)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 8)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 9)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 10)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 11)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 12)
        sprite('vresef450_ParitclePos', 1)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', 13)

    @State
    def esef_450ChangeSordEff():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            SetScaleY(1000)
            SetScaleX(1500)
            Rotation(30000)
            Eff3DEffect('esef_450_parge00', '')
            AddY(60000)
            AddX(30000)
        sprite('null', 10)
        CreateObject('esef_450ChangeSordEffC', -1)
        sprite('null', 29)
        ConstantAlphaModifier(-9)

    @State
    def esef_450ChangeSordEffC():

        def upon_IMMEDIATE():
            BlendMode_Add()
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            E0EAEffectRotation(2)
            SetScaleY(1000)
            Eff3DEffect('esef_450_parge00', '')
        sprite('null', 5)
        sprite('null', 5)
        ConstantAlphaModifier(-51)

    @State
    def esef_430EffBG():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Unknown4023(3)
            Eff3DEffect('esef_450_BG00', '')
            SetScaleX(3000)
            SetScaleY(3200)
            SetScaleZ(3000)
            AddY(-10000)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
        sprite('null', 30)
        AlphaValue(0)
        ConstantAlphaModifier(8)
        sprite('null', 32767)
        ConstantAlphaModifier(0)
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-14)
        sprite('null', 32767)
        ConstantAlphaModifier(0)
        label(1)
        sprite('null', 1)

    @State
    def esef_430EffBGAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Unknown4023(3)
            Eff3DEffect('esef_450_BG00add', '')
            SetScaleX(3000)
            SetScaleY(3200)
            SetScaleZ(3000)
            AddY(-10000)
            sendToLabelUpon(32, 0)
        sprite('null', 30)
        AlphaValue(0)
        ConstantAlphaModifier(8)
        sprite('null', 32767)
        ConstantAlphaModifier(0)
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-25)

    @State
    def esef_430EffAasiba():

        def upon_IMMEDIATE():
            BlendMode_Add()
            RenderLayer(15)
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_asiba00', '')
            Size(2000)
        sprite('null', 15)
        CreateObject('esef_430EffAasibaAdd', -1)
        sprite('null', 4)
        SetScaleSpeed(300)
        ConstantAlphaModifier(-13)
        ParticleColorFromPalette(241, 241, 240)
        CallCustomizableParticle('eseff_cmngarass', -1)
        sprite('null', 15)
        SetScaleSpeed(100)

    @State
    def esef_430EffAasibaAdd():

        def upon_IMMEDIATE():
            BlendMode_Add()
            RenderLayer(15)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_asiba00', '')
            E0EAEffectPosition(2)
            E0EAEffectScale(2)
            E0EAEffectRotation(2)
        sprite('null', 15)
        ConstantAlphaModifier(-12)
        sprite('null', 5)
        SetScaleSpeed(300)

    @State
    def esef_430EffAtkSlash():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_431_slash')
            AddY(200000)
        sprite('null', 60)
        CreateObject('esef_430EffAtkSlashC', -1)
        ScreenShake(10000, 10000)

    @State
    def esef_430EffAtkSlashC():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_slash00', '')
            SetScaleY(1200)
        sprite('null', 10)
        sprite('null', 20)
        ConstantAlphaModifier(-12)

    @State
    def esef_430EffCutIn():

        def upon_IMMEDIATE():
            PaletteIndex(0)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            AddX(200000)
            AddY(140000)
            RenderLayer(1)
            EnableAfterimage(1)
        sprite('es450cutin_00', 4)
        CreateObject('esef_430EffBG2', -1)
        ScreenShake(10000, 10000)
        physicsXImpulse(60000)
        physicsYImpulse(-30000)
        CreateObject('esef_430EffCutInSpeed', 0)
        ApplyFunctionsToObjects(1)
        AddY(500000)
        AddScale(300)
        ApplyFunctionsToSelf()
        CreateObject('esef_430EffCutInSpeed', 1)
        ApplyFunctionsToObjects(1)
        AddY(-400000)
        ApplyFunctionsToSelf()
        CommonSE('000_airdash_0')
        sprite('es450cutin_00', 32767)
        physicsXImpulse(1000)
        physicsYImpulse(-500)

    @State
    def esef_430EffCutInSpeed():

        def upon_IMMEDIATE():
            PaletteIndex(0)
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            ParticleLayer(4)
            CallPrivateEffect('eseff_450_cutin_speed')
            RotationAngle(33000)
            Size(1500)
        sprite('null', 32767)

    @State
    def esef_430EffBG2():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_BG01', '')
            Size(2000)
            AddScaleY(300)
            AddY(10000)
            AddX(100000)
            Rotation(35000)
        sprite('null', 6)
        AlphaValue(0)
        sprite('null', 8)
        ConstantAlphaModifier(31)
        sprite('null', 32767)
        ConstantAlphaModifier(0)

    @State
    def esef_450SlashLast():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_lastslash00', '')
            Rotation(35000)
            Size(900)
            XPositionRelativeFacing(-1269000)
            AbsoluteY(1490000)
            IgnorePauses(2)
        sprite('null', 7)
        PaletteIndex(4)
        ParticleColorFromPalette(241, 241, 241)
        ParticleRotationAngle(35000)
        CallCustomizableParticle('eseff_450_flash', -1)
        CreateObject('esef_450EffLastSlashNigiyakasi', -1)
        sprite('null', 8)
        physicsXImpulse(130000)
        physicsYImpulse(-90000)
        sprite('null', 20)
        EndMomentum(1)
        sprite('null', 60)
        ScreenShake(20000, 20000)
        AlphaValue(0)

    @State
    def esef_450EffLastSlashNigiyakasi():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            Eff3DEffect('esef_450_slash00', '')
            SetScaleY(1200)
        sprite('null', 5)
        AlphaValue(0)
        sprite('null', 10)
        ConstantAlphaModifier(26)
        sprite('null', 10)
        sprite('null', 20)
        ConstantAlphaModifier(-12)

    @State
    def esef_450EffEmb():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_emb00', '')
            AddX(-200000)
            AddY(200000)
            Flip()
        sprite('null', 1)
        CallCustomizableParticle('eseff_450_flash2', -1)
        label(0)
        sprite('null', 5)
        ScreenShake(800, 800)
        gotoLabel(0)

    @State
    def esef_450EffWing():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_wing00', '')
            RenderLayer(2)
            Size(1000)
            CreateObject('esef_450EffWingSub', -1)
            Visibility(1)
            PrivateSE('esse_12')
        label(0)
        sprite('vresef450_ParitclePos2', 5)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 0)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 1)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 2)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 3)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 4)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 5)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 6)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 7)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 8)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 9)
        ParticleLayer(13)
        CallCustomizableParticle('eseff_450_gotya00', 10)
        AddScale(2)
        sprite('vresef450_ParitclePos2', 5)
        AddScale(2)
        sprite('vresef450_ParitclePos2', 5)
        AddScale(2)
        sprite('vresef450_ParitclePos2', 5)
        AddScale(2)
        gotoLabel(0)

    @State
    def esef_450EffWingAdd():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_wing00', '')
            RenderLayer(2)
            Size(1000)
            Visibility(1)
            sendToLabelUpon(32, 1)
        label(0)
        sprite('null', 5)
        AlphaValue(0)
        AddScale(2)
        gotoLabel(0)
        label(1)
        sprite('null', 5)
        ConstantAlphaModifier(4)
        gotoLabel(1)

    @State
    def esef_450EffWingSub():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_wing00sub', '')
            RenderLayer(6)
            Size(1000)
        label(0)
        sprite('null', 10)
        AlphaValue(75)
        Size(1000)
        sprite('null', 10)
        AlphaValue(0)
        sprite('null', 5)
        AlphaValue(75)
        sprite('null', 5)
        AlphaValue(0)
        gotoLabel(0)

    @State
    def esef_450EffBGClash():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            Eff3DEffect('esef_450_BG02', '')
            RenderLayer(2)
            SetScaleY(1300)
            SetScaleX(3000)
            AlphaValue(200)
            AddY(-115000)
            PrivateSE('esse_13')
        sprite('null', 32767)

    @State
    def esef_450EffBGLast():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            IgnoreScreenfreeze(1)
            Eff3DEffect('esef_450_BG03', '')
            SetScaleY(850)
            AlphaValue(255)
            AddY(-15000)
        sprite('null', 32767)

    @State
    def esef_450EffClashA():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00')
            RenderLayer(2)
            Size(800)
            RotationAngle(-65000)
        sprite('null', 150)
        SetScaleSpeed(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashB():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00')
            RenderLayer(2)
            Size(500)
            RotationAngle(-100000)
        sprite('null', 150)
        SetScaleSpeed(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashC():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00')
            RenderLayer(2)
            Size(600)
            RotationAngle(-25000)
        sprite('null', 150)
        SetScaleSpeed(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashAmove():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00m')
            RenderLayer(2)
            Size(800)
            RotationAngle(-65000)
        sprite('null', 130)
        DespawnEAEffect('esef_450EffClashA')

    @State
    def esef_450EffClashBmove():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00m')
            RenderLayer(2)
            Size(500)
            RotationAngle(-100000)
        sprite('null', 130)
        DespawnEAEffect('esef_450EffClashB')

    @State
    def esef_450EffClashCmove():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00m')
            RenderLayer(2)
            Size(800)
            RotationAngle(-25000)
        sprite('null', 130)
        DespawnEAEffect('esef_450EffClashC')

    @State
    def esef_450EffClash01():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00')
            RenderLayer(2)
            Size(800)
            AddY(180000)
            AddX(-400000)
        sprite('null', 149)

    @State
    def esef_450EffClash01m():

        def upon_IMMEDIATE():
            BlendMode_Add()
            IgnoreScreenfreeze(1)
            E0EAEffectRotation(2)
            RemoveOnCallStateEnd(2)
            RemoveOnCallStateEnd(2)
            LinkParticle('eseff_450_clash00m')
            RenderLayer(2)
            Size(800)
            AddY(180000)
            AddX(-400000)
        sprite('null', 100)

    @State
    def esef_450WhiteOut():

        def upon_IMMEDIATE():
            XPositionRelativeFacing(260000)
            RemoveOnCallStateEnd(2)
        sprite('null', 10)
        sprite('null', 200)
        ParticleLayer(4)
        CallPrivateEffect('eseff_450_flash3')

    @State
    def esef_450PaticleInf():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
        sprite('null', 32767)
        LinkParticle('eseff_450_infwin')

    @State
    def esef_450SordLostMaso():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(3)
            PaletteIndex(4)
        sprite('vresef615_whitesord', 100)
        AlphaValue(0)
        sprite('vresef615_whitesord', 40)
        ConstantAlphaModifier(6)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 3)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_450_masolost', 5)
        sprite('vresef615_whitesord', 32767)

    @State
    def suef_600_screen():

        def upon_IMMEDIATE():
            SetPosXByScreenPer(50)
            SetPosYByScreenPer(50)
            PaletteIndex(3)
            BlendMode_Sub()
            RenderLayer(15)
        sprite('esef600_screen', 32)
        AlphaValue(0)
        ConstantAlphaModifier(2)
        ApplyFunctionsToObjects(22)
        ColorTransition(4288059030, 32)
        ApplyFunctionsToSelf()
        sprite('esef600_screen', 60)
        ConstantAlphaModifier(0)
        AlphaValue(64)
        sprite('esef600_screen', 32)
        ConstantAlphaModifier(-2)
        ApplyFunctionsToObjects(22)
        ColorTransition(4294967295, 32)
        ApplyFunctionsToSelf()

    @State
    def suef_600_es():

        def upon_IMMEDIATE():
            PaletteIndex(4)
            BlendMode_Add()
        sprite('esef600_00', 16)
        AlphaValue(0)
        ConstantAlphaModifier(16)
        sprite('esef600_00', 16)
        ConstantAlphaModifier(-16)

    @State
    def suef_600_light_core():
        sprite('null', 32)
        PaletteIndex(4)
        ParticleLayer(11)
        ParticleColorFromPalette(241, 241, 241)
        CallPrivateEffect('esef_600core')
        Size(0)
        SetScaleSpeed(100)
        ConstantAlphaModifier(-8)

    @State
    def suef_600_light():
        sprite('null', 1)
        PaletteIndex(4)
        ParticleLayer(11)
        ParticleColorFromPalette(240, 240, 240)
        CallCustomizableParticle('esef_600light', -1)
        ParticleLayer(11)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('esef_600amida', -1)
        CreateParticle('esef_600dust', -1)

    @State
    def esef_600light_end():
        sprite('null', 9)
        sprite('null', 1)
        PaletteIndex(4)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('esef_600end', -1)
        CreateParticle('esef_600end2', -1)

    @State
    def esef_600_particle():

        def upon_IMMEDIATE():
            E0EAEffectPosition(2)
            PaletteIndex(4)
            Visibility(1)
        label(0)
        sprite('es600_09', 5)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 106)
        gotoLabel(0)

    @State
    def esef_601():

        def upon_IMMEDIATE():
            AddX(180000)
            AddY(256000)
        sprite('null', 1)
        CreateObject('esef_601_sword', -1)
        CreateObject('esef_601_sword_add', -1)
        CreateObject('esef_601_bloom', -1)
        CreateObject('esef_601_sub', -1)
        CreateObject('esef_601_sword_particle', -1)

    @State
    def esef_601_bloom():

        def upon_IMMEDIATE():
            PaletteIndex(4)
            ParticleColorFromPalette(240, 240, 240)
            CallPrivateEffect('esef_601bloom')
            sendToLabelUpon(32, 0)
        sprite('null', 32767)
        AlphaValue(0)
        ConstantAlphaModifier(4)
        label(0)
        sprite('null', 60)
        ConstantAlphaModifier(-4)

    @State
    def esef_601_sub():

        def upon_IMMEDIATE():
            LinkParticle('esef_601sub')
            sendToLabelUpon(32, 0)
        sprite('null', 32767)
        AlphaValue(0)
        ConstantAlphaModifier(4)
        label(0)
        sprite('null', 60)
        ConstantAlphaModifier(-4)

    @State
    def esef_601_sword_particle():

        def upon_IMMEDIATE():
            PaletteIndex(4)
        label(0)
        sprite('esef601_sword', 16)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 106)
        gotoLabel(0)

    @State
    def esef_601_sword():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Size(860)

            def upon_32():
                SLOT_51 = 1
        sprite('null', 10)
        sprite('null', 100)
        PaletteIndex(4)
        ColorFromPaletteIndex(241)
        Eff3DEffect('esef_601sword.DIG', '')
        AlphaValue(0)
        ConstantAlphaModifier(6)
        label(0)
        sprite('null', 3)
        Eff3DEffect('esef_601sword3.DIG', '')
        loopRest()
        GotoIf0(0, 2, 51)
        sprite('null', 34)
        sprite('null', 15)
        ObjectUpon(3, 32)
        sprite('null', 7)
        Eff3DEffect('esef_601sword2.DIG', '')
        CreateObject('esef_601_sword_zanzou1', -1)
        sprite('null', 7)
        CreateObject('esef_601_sword_zanzou2', -1)
        sprite('null', 7)
        CreateObject('esef_601_sword_zanzou3', -1)

    @State
    def esef_601_sword_add():

        def upon_IMMEDIATE():
            BlendMode_Add()
            Size(860)

            def upon_32():
                SLOT_51 = 1
        sprite('null', 10)
        sprite('null', 100)
        PaletteIndex(4)
        ColorFromPaletteIndex(242)
        Eff3DEffect('esef_601sword_add.DIG', '')
        AlphaValue(0)
        ConstantAlphaModifier(6)
        label(0)
        sprite('null', 3)
        Eff3DEffect('esef_601sword3_add.DIG', '')
        loopRest()
        GotoIf0(0, 2, 51)
        sprite('null', 34)
        sprite('null', 15)
        sprite('null', 7)
        Eff3DEffect('esef_601sword2_add.DIG', '')
        sprite('null', 7)
        sprite('null', 7)

    @State
    def esef_601_sword_zanzou1():
        sprite('null', 28)
        Size(860)
        RenderLayer(11)
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_601sword2_zanzou1.DIG', '')
        ConstantAlphaModifier(-5)

    @State
    def esef_601_sword_zanzou2():
        sprite('null', 21)
        Size(860)
        RenderLayer(11)
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_601sword2_zanzou2.DIG', '')
        ConstantAlphaModifier(-10)

    @State
    def esef_601_sword_zanzou3():
        sprite('null', 7)
        Size(860)
        RenderLayer(11)
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_601sword2_zanzou3.DIG', '')
        ConstantAlphaModifier(-15)
        sprite('null', 14)
        CreateObject('esef_601_sword_zanzou4', -1)

    @State
    def esef_601_sword_zanzou4():
        sprite('null', 21)
        Size(860)
        RenderLayer(11)
        PaletteIndex(4)
        ColorFromPaletteIndex(240)
        Eff3DEffect('esef_601sword2_zanzou4.DIG', '')
        ConstantAlphaModifier(-20)

    @State
    def esef_601_zanzou():

        def upon_IMMEDIATE():
            PaletteIndex(4)
            BlendMode_Add()
        sprite('esef601_00', 7)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)
        sprite('esef601_01', 7)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        sprite('esef601_02', 7)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)

    @State
    def esef_610_emblem():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(3)
            BlendMode_Add()
            PaletteIndex(3)
            AlphaValue(0)
            ConstantAlphaModifier(4)
            FaceLeft()
        sprite('null', 10)
        CreateObject('esef_610_particle', -1)
        loopRest()
        Size(625)
        if CharacterIDCheck('rg'):
            sendToLabel(1)
        if CharacterIDCheck('jn'):
            sendToLabel(2)
        if CharacterIDCheck('no'):
            sendToLabel(3)
        if CharacterIDCheck('rc'):
            sendToLabel(4)
        if CharacterIDCheck('tk'):
            sendToLabel(5)
        if CharacterIDCheck('tg'):
            sendToLabel(6)
        if CharacterIDCheck('lc'):
            sendToLabel(7)
        if CharacterIDCheck('ar'):
            sendToLabel(8)
        if CharacterIDCheck('bn'):
            sendToLabel(9)
        if CharacterIDCheck('ca'):
            sendToLabel(10)
        if CharacterIDCheck('ha'):
            sendToLabel(11)
        if CharacterIDCheck('ny'):
            sendToLabel(12)
        if CharacterIDCheck('tb'):
            sendToLabel(13)
        if CharacterIDCheck('hz'):
            sendToLabel(14)
        if CharacterIDCheck('mu'):
            sendToLabel(15)
        if CharacterIDCheck('mk'):
            sendToLabel(16)
        if CharacterIDCheck('vh'):
            sendToLabel(17)
        if CharacterIDCheck('pt'):
            sendToLabel(18)
        if CharacterIDCheck('rl'):
            sendToLabel(19)
        if CharacterIDCheck('iz'):
            sendToLabel(20)
        if CharacterIDCheck('am'):
            sendToLabel(21)
        if CharacterIDCheck('bl'):
            sendToLabel(22)
        if CharacterIDCheck('az'):
            sendToLabel(23)
        if CharacterIDCheck('kg'):
            sendToLabel(24)
        if CharacterIDCheck('kk'):
            sendToLabel(25)
        if CharacterIDCheck('tm'):
            sendToLabel(26)
        if CharacterIDCheck('ce'):
            sendToLabel(27)
        if CharacterIDCheck('rm'):
            sendToLabel(28)
        if CharacterIDCheck('hb'):
            sendToLabel(29)
        if CharacterIDCheck('nt'):
            sendToLabel(30)
        if CharacterIDCheck('ph'):
            sendToLabel(31)
        if CharacterIDCheck('mi'):
            sendToLabel(32)
        if CharacterIDCheck('su'):
            sendToLabel(33)
        if CharacterIDCheck('es'):
            sendToLabel(34)
        if CharacterIDCheck('ma'):
            sendToLabel(35)
        if CharacterIDCheck('jb'):
            sendToLabel(36)
        label(1)
        sprite('esef_emb_rg', 32767)
        label(2)
        sprite('esef_emb_jn', 32767)
        label(3)
        sprite('esef_emb_no', 32767)
        label(4)
        sprite('esef_emb_rc', 32767)
        label(5)
        sprite('esef_emb_tk', 32767)
        label(6)
        sprite('esef_emb_tg', 32767)
        label(7)
        sprite('esef_emb_lc', 32767)
        label(8)
        sprite('esef_emb_ar', 32767)
        label(9)
        sprite('esef_emb_bn', 32767)
        label(10)
        sprite('esef_emb_ca', 32767)
        label(11)
        sprite('esef_emb_ha', 32767)
        label(12)
        sprite('esef_emb_ny', 32767)
        label(13)
        sprite('esef_emb_tb', 32767)
        label(14)
        sprite('esef_emb_hz', 32767)
        label(15)
        sprite('esef_emb_mu', 32767)
        label(16)
        sprite('esef_emb_mk', 32767)
        label(17)
        sprite('esef_emb_vh', 32767)
        label(18)
        sprite('esef_emb_pt', 32767)
        label(19)
        sprite('esef_emb_rl', 32767)
        label(20)
        sprite('esef_emb_iz', 32767)
        label(21)
        sprite('esef_emb_am', 32767)
        label(22)
        sprite('esef_emb_bl', 32767)
        label(23)
        sprite('esef_emb_az', 32767)
        label(24)
        sprite('esef_emb_kg', 32767)
        label(25)
        sprite('esef_emb_kk', 32767)
        label(26)
        sprite('esef_emb_tm', 32767)
        label(27)
        sprite('esef_emb_ce', 32767)
        label(28)
        sprite('esef_emb_rm', 32767)
        label(29)
        sprite('esef_emb_hb', 32767)
        label(30)
        sprite('esef_emb_nt', 32767)
        label(31)
        sprite('esef_emb_ph', 32767)
        label(32)
        sprite('esef_emb_mi', 32767)
        label(33)
        sprite('esef_emb_su', 32767)
        label(34)
        sprite('esef_emb_es', 32767)
        label(35)
        sprite('esef_emb_ma', 32767)
        label(36)
        sprite('esef_emb_jb', 32767)

    @State
    def esef_610_particle():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(3)
        sprite('null', 1)
        CreateObject('esef_610_particle_color', -1)
        CreateObject('esef_610_particle_sub', -1)

    @State
    def esef_610_particle_color():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(3)
            PaletteIndex(4)
            ParticleColorFromPalette(240, 240, 240)
            CallPrivateEffect('esef_610light')
            AlphaValue(0)
            ConstantAlphaModifier(8)
        sprite('null', 30)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('esef_610smoke', -1)
        CreateParticle('esef_610dust', -1)
        CreateParticle('esef_610circle', -1)
        label(0)
        sprite('null', 30)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('esef_610smoke', -1)
        CreateParticle('esef_610dust', -1)
        gotoLabel(0)

    @State
    def esef_610_particle_sub():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(3)
            E0EAEffectPosition(3)
            LinkParticle('esef_610sub')
            AlphaValue(0)
            ConstantAlphaModifier(8)
        sprite('null', 32767)

    @State
    def esef_611():
        CreateObject('esef_611_sword', -1)
        CreateObject('esef_611_sword_add', -1)
        CreateObject('esef_611_particle', -1)

    @State
    def esef_611_sword():

        def upon_IMMEDIATE():
            PaletteIndex(0)
            BlendMode_Normal()
        sprite('esef611_sword00', 7)

    @State
    def esef_611_sword_add():

        def upon_IMMEDIATE():
            PaletteIndex(4)
            BlendMode_Add()
            SetZVal(-1000)
        sprite('esef611_sword01', 7)
        AlphaValue(0)
        ConstantAlphaModifier(36)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        sprite('esef611_sword02', 7)
        sprite('esef611_sword03', 7)
        sprite('esef611_sword04', 7)
        sprite('null', 1)
        CreateObject('esef_611_henkei', -1)

    @State
    def esef_611_henkei():
        CreateObject('esef_611_sword2', -1)
        CreateObject('esef_611_sword2_add', -1)

    @State
    def esef_611_sword2():

        def upon_IMMEDIATE():
            BlendMode_Add()
            PaletteIndex(4)
            ColorFromPaletteIndex(241)
        sprite('null', 21)
        Eff3DEffect('esef_611sword2.DIG', '')
        sprite('null', 30)
        ConstantAlphaModifier(-16)

    @State
    def esef_611_sword2_add():

        def upon_IMMEDIATE():
            BlendMode_Add()
        sprite('null', 21)
        Eff3DEffect('esef_611sword2_add.DIG', '')
        sprite('null', 30)
        ConstantAlphaModifier(-16)

    @State
    def esef_611_particle():

        def upon_IMMEDIATE():
            PaletteIndex(4)
            Visibility(1)
        sprite('esef611_particle', 14)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        sprite('esef611_particle', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 4)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('esef611_particle', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 1)
        sprite('esef611_particle', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 2)
        sprite('esef611_particle', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 3)

    @State
    def esef_611_es_add():

        def upon_IMMEDIATE():
            E0EAEffectPosition(2)
            PaletteIndex(4)
            BlendMode_Add()
            RenderLayer(11)
        sprite('esef611_07', 7)
        AlphaValue(0)
        ConstantAlphaModifier(18)
        sprite('esef611_08', 7)
        sprite('esef611_09', 7)
        sprite('esef611_10', 7)
        sprite('esef611_11', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        ConstantAlphaModifier(-12)
        sprite('esef611_11', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)
        sprite('esef611_11', 7)
        ParticleLayer(12)
        ParticleColorFromPalette(241, 241, 241)
        CallCustomizableParticle('eseff_cmngarass', 0)

    @State
    def es901_Pudding1():

        def upon_IMMEDIATE():
            if random_(2, 0, 50):
                RandSpeedY(100, 200)
            else:
                RandSpeedY(-100, -200)
        label(0)
        sprite('es901_02', 60)
        YAccel(-100)
        loopRest()
        gotoLabel(0)

    @State
    def es901_Pudding2():

        def upon_IMMEDIATE():
            if random_(2, 0, 50):
                RandSpeedY(100, 200)
            else:
                RandSpeedY(-100, -200)
        label(0)
        sprite('es901_03', 60)
        YAccel(-100)
        loopRest()
        gotoLabel(0)

    @State
    def es901_Pudding3():

        def upon_IMMEDIATE():
            if random_(2, 0, 50):
                RandSpeedY(100, 200)
            else:
                RandSpeedY(-100, -200)
        label(0)
        sprite('es901_04', 60)
        YAccel(-100)
        loopRest()
        gotoLabel(0)

    @State
    def es901_Pudding4():

        def upon_IMMEDIATE():
            if random_(2, 0, 50):
                RandSpeedY(100, 200)
            else:
                RandSpeedY(-100, -200)
        label(0)
        sprite('es901_05', 60)
        YAccel(-100)
        loopRest()
        gotoLabel(0)

    @State
    def Act3Event_esvsiz_sousai():

        def upon_IMMEDIATE():
            AddX(100000)
            AbsoluteY(200000)
        sprite('null', 3)
        CreateParticle('ef_offset', 0)
        CommonSE('105_guard_slash_2')
        CommonSE('105_guard_slash_2')
        loopRest()

    @State
    def Act3Event_esvsiz_rg():

        def upon_IMMEDIATE():
            LoadSpritePalette(0)
            ScreenCollision(0)
            ForceFaceSprite()
            XPositionRelativeFacing(-920000)

            def upon_FRAME_STEP():
                if SLOT_38:
                    if (SLOT_22 < 260000):
                        clearUponHandler(3)
                        XPositionRelativeFacing(-260000)
                        EndMomentum(1)
                        sendToLabel(0)
                elif (SLOT_22 > (-260000)):
                    clearUponHandler(3)
                    XPositionRelativeFacing(-260000)
                    EndMomentum(1)
                    sendToLabel(0)
            sendToLabelUpon(32, 1)
        sprite('rg030_00', 7)
        physicsXImpulse(5000)
        label(9)
        sprite('rg030_01', 7)
        sprite('rg030_02', 7)
        SFX_FOOTSTEP_(100, 1, 1)
        sprite('rg030_03', 7)
        sprite('rg030_04', 7)
        sprite('rg030_05', 7)
        sprite('rg030_06', 7)
        SFX_FOOTSTEP_(100, 1, 1)
        sprite('rg030_07', 7)
        sprite('rg030_08', 7)
        loopRest()
        gotoLabel(9)
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
        label(1)
        sprite('rg040_00', 4)
        ObjectUpon(4, 32)
        CreateParticle('story_teni', 103)
        CommonSE('000_airdash_2')
        CommonSE('022_magiccircle_b')
        ConstantAlphaModifier(-4)
        sprite('rg040_01', 4)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        sprite('rg040_02', 5)
        sprite('rg040_02ex', 5)
        CreateParticle('haef_event_lose_end', 103)
        sprite('keep', 1)
        Visibility(1)
        ForceShadowOff(1)
        sprite('null', 99)
        sprite('null', 32767)
        loopRest()