@State
def EMB_TM():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TM.DIG', '')
        RenderLayer(5)
        Size(1800)
        AddY(36000)
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
def EMB_TM_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TM.DIG', '')
        RenderLayer(5)
        Size(1800)
        AddY(36000)
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
def EMB_TM_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TM.DIG', '')
        Size(1800)
        AddY(18000)
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
def AntiAirWindSmokeOpt():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        RotationAngle(-180000)
        Size(1250)
        AddScaleY(-500)
        AlphaValue(120)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(10)
    loopRest()
    label(99)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def tmef_Aura():

    def upon_IMMEDIATE():
        IgnorePauses(3)
    sprite('null', 1)
    CreateParticle('tmef_envaura', -1)


@State
def tmef_AuraDelete():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        ParticleLayer(2)
        ParticleSize(600)
        CallCustomizableParticle('tmef_deleteaura', -1)
        Size(600)
        ContinueState(1)
    sprite('null', 1)


@State
def EffKamae():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        LinkParticle('tmef_kamaeaura')
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 32767)
    loopRest()
    label(99)
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def EffKamaeLand():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        ParticleLayer(5)
        CallPrivateEffect('tmef_landaura')
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 10)
    SetScaleSpeed(50)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(99)
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def EffLandAura():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        CallPrivateEffect('tmef_landaura')
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    Size(1500)
    SetScaleSpeed(200)


@State
def EffAirAura():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    sprite('null', 10)
    ParticleLayer(5)
    CallPrivateEffect('tmef_airaura')
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    Size(1500)
    SetScaleSpeed(200)


@State
def EffCommandThrowAura():

    def upon_IMMEDIATE():
        LinkParticle('tmef_spaura')
    sprite('null', 60)


@State
def EffCommandThrowWind():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        CallPrivateEffect('tmef_comthrowwind')
        Size(1200)
        RandAddScale(-200, 250)
        AlphaValue(150)
    sprite('null', 30)


@State
def ExBodyAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(0)
        ColorForTransition(3355473940)
        AddX(20000)
        AddY(200000)
        uponSendToLabel(32, 99)
        uponSendToLabel(PLAYER_DAMAGED, 99)
        ContinueState(160)
    sprite('vref_env', 10)
    SetScaleSpeed(600)
    sprite('vref_env', 40)
    SetScaleSpeed(0)
    label(99)
    sprite('vref_env', 14)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def EffKnifeSignal():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    Visibility(1)
    LinkParticle('tmef_knifesignal')
    CreateParticle('tmef_knifesignalopt', -1)
    Size(900)
    RandAddRotation(-90000, 90000)


@State
def HZEF_GuardLoop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(-16000)
        uponSendToLabel(32, 99)
    sprite('null', 20)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(32000)
        AddY(-97500)
        physicsYImpulse(20000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(16000)
        AddY(110000)
        physicsYImpulse(-40000)
        SetScaleX(-1000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(-16000)
        AddY(-100000)
        physicsYImpulse(40000)
        SetScaleX(-1000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(-40000)
        AddY(95000)
        physicsYImpulse(-15000)
        Unknown1082(4)
    loopRest()
    ExitState()
    label(99)
    TriggerUponForState('HZEF_GuardLoopParts', 32)


@State
def HZEF_GuardLoopParts():

    def upon_IMMEDIATE():
        SetZVal(-100)
        BlendMode_Normal()
        uponSendToLabel(32, 99)
    sprite('vrtmef_guard00', 4)
    AlphaValue(100)
    sprite('vrtmef_guard00', 2)
    IgnorePauses(3)
    AlphaValue(200)
    sprite('vrtmef_guard00', 12)
    IgnorePauses(0)
    AlphaValue(120)
    ConstantAlphaModifier(-15)
    loopRest()
    ExitState()
    label(99)
    EndObject()


@State
def HZEF_HeavyGuardLoop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        TriggerUponForState('HZEF_GuardLoop', 32)
    sprite('null', 20)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(48000)
        AddY(32000)
        physicsYImpulse(10000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(16000)
        AddY(-16000)
        physicsYImpulse(-15000)
        SetScaleX(-1000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(-16000)
        AddY(16000)
        physicsYImpulse(15000)
        SetScaleX(-1000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(-48000)
        AddY(-32000)
        physicsYImpulse(-10000)


@State
def HZEF_HeavyGuardLoopObj():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        SetZVal(-100)
        BlendMode_Normal()
        AddX(-64000)
    sprite('vrtmef_guard00', 2)
    AlphaValue(250)
    sprite('vrtmef_guard00', 10)
    AlphaValue(150)
    ConstantAlphaModifier(-15)


@State
def Eff6AZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef210_00', 2)
    sprite('vrtmef210_01', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff5CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef202_00', 2)
    E0EAEffectPosition(0)
    sprite('vrtmef202_01', 6)
    AddAlpha(-100)


@State
def Eff8CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef252_00', 2)
    sprite('vrtmef252_01', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef252_02', 2)
    sprite('vrtmef252_03', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef252_04', 2)
    sprite('vrtmef252_05', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef252_06', 2)
    sprite('vrtmef252_07', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff2CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef232_00', 3)
    sprite('vrtmef232_01', 2)
    sprite('vrtmef232_02', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff6CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef213_00', 2)
    sprite('vrtmef213_01', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff6CZanzo2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrtmef213_11', 2)
    sprite('vrtmef213_12', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def tmef203():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(220000)
        AddY(210000)
    sprite('vrtmef203_00', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrtmef203_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    sprite('vrtmef203_02', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_03', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_04', 4)
    E0EAEffectPosition(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_05', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef203_06', 4)
    ConstantAlphaModifier(-30)


@State
def tmef203_OD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(260000)
        AddY(210000)
        Size(1300)
    sprite('vrtmef203_00', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrtmef203_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    sprite('vrtmef203_02', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_03', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_04', 4)
    E0EAEffectPosition(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef203_05', 4)
    ConstantAlphaModifier(-20)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef203_06', 4)


@State
def tmef_233_snoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Size(550)
    sprite('null', 30)
    LinkParticle('tmef_400_hand')


@State
def tmef_233_arm_a():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_a', '')
        BlendMode_Normal()
    sprite('null', 60)


@State
def tmef_233_arm_b():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_b', '')
        BlendMode_Normal()
    sprite('null', 60)


@State
def tmef_233_arm_c():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_c', '')
        BlendMode_Normal()
    sprite('null', 60)


@State
def tmef_233_arm_d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_d', '')
        BlendMode_Normal()
    sprite('null', 60)


@State
def tmef_233_arm_e():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_e', '')
        BlendMode_Normal()
    sprite('null', 60)


@State
def tmef_233_arm_f():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_f', '')
        BlendMode_Normal()
        Size(2000)
        Rotation(-60000)
        PerAngleSpeed(15000)
    sprite('null', 60)


@State
def tmef_233_arm_g():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_arm_g', '')
        BlendMode_Normal()
        Size(2000)
        Rotation(-35000)
        PerAngleSpeed(5000)
    sprite('null', 60)


@State
def tmef_233_magiccircle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('null', 4)
    SetScaleSpeed(100)
    LinkParticle('tmef_233_exportalparts')
    sprite('null', 19)
    SetScaleSpeed(0)
    sprite('null', 120)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-32)


@State
def tmef_233_exportal_tm():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AddY(-10000)
        AddX(-5000)
        Size(1000)
    sprite('null', 35)
    LinkParticle('tmef_233_exportal2')
    CreateParticle('tmef_233_splash', -1)


@State
def tmef_233_chain():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_chain', '')
        BlendMode_Normal()
        AddX(448000)
    sprite('null', 19)
    Size(275)
    SetScaleSpeed(110)
    CreateObject('tmef_233_exportal', -1)
    CreateObject('tmef_233_exportal_b', -1)
    sprite('null', 3)
    SetScaleSpeed(0)
    sprite('null', 30)
    CreateObject('tmef_233_snake', -1)


@State
def tmef_233_snake():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_snake', '')
        BlendMode_Normal()
        FaceSpawnLocation()
    sprite('null', 22)
    Size(2475)
    CreateObject('tmef_233_snake_end', -1)


@State
def tmef_233_snake_end():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(666)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef233_00', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_02', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)


@State
def tmef_233_exportal():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        AddX(35200)
        Size(1100)
    sprite('null', 19)
    physicsXImpulse(12650)
    LinkParticle('tmef_233_exportal')
    sprite('null', 60)
    physicsXImpulse(0)


@State
def tmef_233_exportal_b():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        AddX(-35200)
        Size(1125)
    sprite('null', 19)
    physicsXImpulse(-12650)
    LinkParticle('tmef_233_exportal')
    sprite('null', 60)
    physicsXImpulse(0)


@State
def tmef_233_chain_DD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_chain', '')
        BlendMode_Normal()
        AddX(448000)
    sprite('null', 19)
    Size(375)
    SetScaleSpeed(150)
    CreateObject('tmef_233_exportal_DD', -1)
    CreateObject('tmef_233_exportal_b_DD', -1)
    sprite('null', 3)
    SetScaleSpeed(0)
    sprite('null', 30)
    CreateObject('tmef_233_snake_DD', -1)


@State
def tmef_233_snake_DD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_233_snake', '')
        BlendMode_Normal()
        Size(1500)
    sprite('null', 22)
    Size(3375)
    CreateObject('tmef_233_snake_end_DD', -1)


@State
def tmef_233_snake_end_DD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1000)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    sprite('vrtmef233_dummy', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_Aura', 10)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    CreateObject('tmef_AuraDelete', 10)
    sprite('vrtmef233_00', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    sprite('vrtmef233_02', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)


@State
def tmef_233_exportal_DD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        AddX(48000)
        Size(1500)
    sprite('null', 19)
    physicsXImpulse(17250)
    LinkParticle('tmef_233_exportal')
    sprite('null', 60)
    physicsXImpulse(0)


@State
def tmef_233_exportal_b_DD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        AddX(-48000)
        Size(1500)
    sprite('null', 19)
    physicsXImpulse(-17250)
    LinkParticle('tmef_233_exportal')
    sprite('null', 60)
    physicsXImpulse(0)


@State
def tm233_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(680)
        AttackP1(90)
        AttackP2(82)
        BonusProration(110)
        Hitstop(0)
        EnemyHitstopAddition(8, 8, 10)
        Hitstun(19)
        AirUntechableTime(36)
        Blockstun(18)
        PushbackX(-60000)
        AirPushbackX(-12000)
        AirPushbackY(30000)
        HeatGainMultiplier(400)
        OppHeatGainMultiplier(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            HeatChange(500)
            CreateObject('HeatDrainEff', 103)

            def RunOnObject_1():
                EffectPosition(3, 103)
    sprite('null', 27)
    sprite('tm233_AtkCol00', 3)
    sprite('tm233_AtkCol01', 3)
    sprite('tm233_AtkCol02', 3)
    sprite('tm233_AtkCol03', 3)
    sprite('tm233_AtkCol04', 3)


@State
def tm233_AtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(350)
        AttackP1(90)
        AttackP2(82)
        SingleProration(1)
        BonusProration(110)
        Hitstop(0)
        EnemyHitstopAddition(8, 8, 10)
        Hitstun(19)
        AirUntechableTime(36)
        Blockstun(18)
        PushbackX(-60000)
        AirPushbackX(-16000)
        AirPushbackY(30000)
        HeatGainMultiplier(400)
        OppHeatGainMultiplier(0)
        CopyFromRightToLeft(23, 2, 56, 22, 2, 122)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            HeatChange(500)

            def RunOnObject_22():
                HeatChange(-200)
            CopyFromRightToLeft(23, 2, 57, 22, 2, 122)
            PrivateFunction(1, 2, 56, 2, 57, 2, 58)
            SLOT_Meter = SLOT_Meter + SLOT_58
            CopyFromRightToLeft(23, 2, 56, 22, 2, 122)
            AddActionMark(-1)
            if not SLOT_2:
                NoAttackDuringAction(1)
            CreateObject('HeatDrainEff', 103)

            def RunOnObject_1():
                EffectPosition(3, 103)
        SetActionMark(3)
        Size(1200)
    sprite('null', 27)
    sprite('tm233_AtkColSP00', 3)
    RefreshMultihit()
    sprite('tm233_AtkColSP01', 3)
    RefreshMultihit()
    sprite('tm233_AtkColSP02', 3)
    RefreshMultihit()
    sprite('tm233_AtkColSP03', 3)
    RefreshMultihit()
    sprite('tm233_AtkColSP04', 3)
    RefreshMultihit()


@State
def tmef214():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1300)
        AddY(-160000)
        AddX(-80000)
        AlphaValue(220)
    sprite('vrtmef214_00', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef214_01', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef214_02', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef214_03', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    ConstantAlphaModifier(-30)
    sprite('vrtmef214_04', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)


@State
def tmef214_2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1400)
        AddY(-60000)
        AddX(-70000)
        AlphaValue(220)
    sprite('vrtmef214_10', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef214_11', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef214_12', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef214_13', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef214_14', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    ConstantAlphaModifier(-30)


@State
def tmef214sp():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1300)
        AddY(-160000)
        AddX(-80000)
        AlphaValue(207)
    sprite('vrtmef214_00', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef214_01', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef214_02', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef214_03', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef214_04', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)


@State
def tmef214_2sp():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1400)
        AddY(-60000)
        AddX(-70000)
        AlphaValue(207)
    sprite('vrtmef214_10', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef214_11', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef214_12', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef214_13', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef214_14', 1)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 2)


@State
def tmef253():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(152000)
        AddY(16000)
    sprite('vrtmef253_00', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    sprite('vrtmef253_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef253_02', 3)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef253_03', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef253_04', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    ConstantAlphaModifier(-30)


@State
def tmef253SP():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(152000)
        AddY(26000)
        Size(1300)
    sprite('vrtmef253_00', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    sprite('vrtmef253_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef253_02', 3)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef253_03', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef253_04', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)


@State
def tmef254():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(40000)
        AddY(280000)
    sprite('vrtmef254_00', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrtmef254_01', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef254_02', 4)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef254_03', 8)
    IgnorePauses(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrtmef254_04', 4)
    E0EAEffectPosition(0)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrtmef254_05', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrtmef254_06', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)


@State
def tmef340():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(0)
    sprite('vrtmef340_00z', 2)


@State
def Atk2DChain():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        FloorCollision(1)
        SetXCollisionFromOrigin(10)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 3, 0, 0, 0, 0, 0, 0)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        RenderLayer(8)
        CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)
        uponSendToLabel(32, 0)
        AttackOff()
    sprite('null', 1)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariSpeed', 0, 5000, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationSomething(0)
    CallPrivateFunction('KusariMochite', 0, 109, 0, 0, 0, 0, 0, 0)
    sprite('null', 12)
    Unknown23143(-7000, -20000, 100)
    RotationSomething(0)
    sprite('null', 11)
    Unknown23143(0, 0, 100)
    sprite('null', 10)
    Unknown23143(-15000, 60000, 70)
    sprite('null', 4)
    Unknown23143(0, 0, 100)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 80, 0, 40)
    label(0)
    sprite('null', 1)
    Unknown23143(0, 0, 100)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 100, 0, 50)
    EndObject()
    loopRest()


@State
def tmef_400_hand():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        LinkParticle('tmef_400_hand')
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 10)
    sprite('null', 10)
    E0EAEffectPosition(0)
    loopRest()


@State
def AssaultChain():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        AddX(60000)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        BlendMode_Normal()

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_51:
                CallPrivateFunction('KusariAngleByChain', 0, 0, 0, 0, 0, 0,
                    0, 0)
                RotationSomething(-180000)
            if SLOT_2:
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                DeleteObject(23)
        uponSendToLabel(32, 0)
    sprite('vr_chain_tip03aa', 1)
    RenderLayer(1)
    Unknown23143(40000, 55000, 70)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationAngle(-30000)
    sprite('vr_chain_tip03aa', 30)
    SetActionMark(1)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 10)
    SetActionMark(0)
    SLOT_51 = 1
    EnableAfterimage(0)
    TriggerUponForState('ExPortalSp', 32)
    Unknown23143(-60000, -45000, 20)
    AddRotationPerFrame(-1000)
    BlendMode_Normal()
    ConstantAlphaModifier(-5)
    sprite('vr_chain_tip04', 10)
    RenderLayer(5)
    sprite('vr_chain_tip04', 6)
    Unknown23143(100000, -50000, 25)
    sprite('vr_chain_tip04', 8)
    RenderLayer(0)
    Unknown23143(-100000, 60000, 25)
    SetZVal(-500)
    AddRotationPerFrame(0)
    RotationAngle(30000)
    ConstantAlphaModifier(-10)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    label(0)
    sprite('vr_chain_tip04ex01', 10)
    SetActionMark(0)
    Unknown23143(-5000, 10000, 20)
    PrivateSE('hzse_02')
    sprite('vr_chain_tip04ex01', 6)
    SLOT_51 = 1
    Unknown23143(-20000, 35000, 20)
    sprite('vr_chain_tip04ex01', 10)
    Unknown23143(-50000, -122500, 20)
    ConstantAlphaModifier(-6)
    sprite('vr_chain_tip04ex01', 29)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 80, 0, 3)


@State
def tmef_400_Aura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddX(30000)
        AddY(30000)
        physicsXImpulse(15000)
    sprite('null', 5)
    label(0)
    sprite('null', 1)
    CreateParticle('tmef_400_tossinaura00', -1)
    gotoLabel(0)


@State
def tmef_400_Sneak():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Flip()
        RenderLayer(1)
        BlendMode_Normal()
        AlphaValue(240)
    sprite('null', 16)
    sprite('vrtmef400_10', 4)
    CreateObject('tmef_Aura400', 0)
    CreateObject('tmef_Aura400', 1)
    CreateObject('tmef_Aura400', 2)
    CreateObject('tmef_Aura400', 3)
    CreateObject('tmef_Aura400', 4)
    CreateObject('tmef_Aura400', 5)
    CreateObject('tmef_AuraDelete400', 0)
    CreateObject('tmef_AuraDelete400', 1)
    CreateObject('tmef_AuraDelete400', 2)
    CreateObject('tmef_AuraDelete400', 3)
    CreateObject('tmef_AuraDelete400', 4)
    CreateObject('tmef_AuraDelete400', 5)
    sprite('vrtmef400_11', 4)
    CreateObject('tmef_Aura400', 0)
    CreateObject('tmef_Aura400', 1)
    CreateObject('tmef_Aura400', 2)
    CreateObject('tmef_Aura400', 3)
    CreateObject('tmef_Aura400', 4)
    CreateObject('tmef_Aura400', 5)
    CreateObject('tmef_Aura400', 6)
    CreateObject('tmef_Aura400', 7)
    CreateObject('tmef_AuraDelete400', 0)
    CreateObject('tmef_AuraDelete400', 1)
    CreateObject('tmef_AuraDelete400', 2)
    CreateObject('tmef_AuraDelete400', 3)
    CreateObject('tmef_AuraDelete400', 4)
    CreateObject('tmef_AuraDelete400', 5)
    CreateObject('tmef_AuraDelete400', 6)
    CreateObject('tmef_AuraDelete400', 7)
    sprite('vrtmef400_12', 4)
    CreateObject('tmef_Aura400', 0)
    CreateObject('tmef_Aura400', 2)
    CreateObject('tmef_Aura400', 4)
    CreateObject('tmef_Aura400', 6)
    CreateObject('tmef_Aura400', 8)
    CreateObject('tmef_Aura400', 10)
    CreateObject('tmef_Aura400', 12)
    CreateObject('tmef_AuraDelete400', 0)
    CreateObject('tmef_AuraDelete400', 2)
    CreateObject('tmef_AuraDelete400', 4)
    CreateObject('tmef_AuraDelete400', 6)
    CreateObject('tmef_AuraDelete400', 8)
    CreateObject('tmef_AuraDelete400', 10)
    CreateObject('tmef_AuraDelete400', 12)
    sprite('vrtmef400_13', 4)
    CreateObject('tmef_Aura400', 0)
    CreateObject('tmef_Aura400', 1)
    CreateObject('tmef_Aura400', 2)
    CreateObject('tmef_Aura400', 3)
    CreateObject('tmef_Aura400', 4)
    CreateObject('tmef_Aura400', 5)
    CreateObject('tmef_Aura400', 6)
    CreateObject('tmef_Aura400', 7)
    CreateObject('tmef_Aura400', 8)
    CreateObject('tmef_AuraDelete400', 0)
    CreateObject('tmef_AuraDelete400', 1)
    CreateObject('tmef_AuraDelete400', 2)
    CreateObject('tmef_AuraDelete400', 3)
    CreateObject('tmef_AuraDelete400', 4)
    CreateObject('tmef_AuraDelete400', 5)
    CreateObject('tmef_AuraDelete400', 6)
    CreateObject('tmef_AuraDelete400', 7)
    CreateObject('tmef_AuraDelete400', 8)
    sprite('vrtmef400_14', 4)
    sprite('vrtmef400_15', 4)
    sprite('vrtmef400_16', 4)
    ConstantAlphaModifier(-20)


@State
def tmef_Aura400():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('tmef_envaura_400', -1)


@State
def tmef_AuraDelete400():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        ParticleLayer(2)
        ParticleSize(1000)
        CallCustomizableParticle('tmef_deleteaura', -1)
        Size(1000)
        ContinueState(1)
    sprite('null', 1)


@State
def tmef_401_hand():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        LinkParticle('tmef_401_hand')
    sprite('null', 7)
    sprite('null', 60)
    E0EAEffectPosition(0)
    loopRest()


@State
def tmef_401_enemy():

    def upon_IMMEDIATE():
        pass
    sprite('null', 5)
    sprite('null', 10)
    EffectPosition(22, 103)
    LinkParticle('tmef_401_bind')
    Size(850)
    CreateObject('tmef_401_magiccircle', -1)
    CreateObject('tmef_401_bind', -1)

    def RunOnObject_1():
        AddY(138000)
        Rotation(175000)
        SetScaleZ(1000)
        SetScaleX(1000)
    CreateObject('tmef_401_bind', -1)

    def RunOnObject_1():
        AddY(40000)
        Rotation(3000)
        SetScaleZ(1200)
        SetScaleX(1200)
    CreateObject('tmef_401_bind', -1)

    def RunOnObject_1():
        AddY(-24000)
        Rotation(-3000)
        SetScaleZ(1075)
        SetScaleX(1075)
    CreateObject('tmef_401_bind', -1)

    def RunOnObject_1():
        AddY(-88000)
        Rotation(2000)
        SetScaleZ(1150)
        SetScaleX(1150)
    CreateObject('tmef_401_bind', -1)

    def RunOnObject_1():
        AddY(-154000)
        Rotation(175000)
        SetScaleZ(950)
        SetScaleX(950)
    sprite('null', 15)
    sprite('null', 60)
    sprite('null', 1)
    DespawnEAEffect('tmef_401_bind')
    CreateParticle('tmef_401_finish', -1)


@State
def tmef_401_bind():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_401_bind', '')
        BlendMode_Normal()
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 9)
    ConstantAlphaModifier(50)
    SetScaleSpeed(-50)
    sprite('null', 30)
    SetScaleSpeed(0)
    sprite('null', 32767)
    Eff3DEffect('tmef_401_bind_anm', '')
    SetScaleXPerFrame(-4)
    SetScaleSpeedZ(-4)


@State
def tmef_401_magiccircle():

    def upon_IMMEDIATE():
        AbsoluteY(0)
    sprite('null', 10)
    LinkParticle('tmef_401_exportalparts')
    Size(0)
    SetScaleSpeed(230)
    sprite('null', 80)
    SetScaleSpeed(0)
    sprite('null', 5)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-50)


@State
def CommandThrow_HitEff():

    def upon_IMMEDIATE():
        EffectPosition(22, 105)
    sprite('null', 1)
    ParticleRandomRotation()
    ParticleSize(900)
    CallCustomizableParticle('ef_hitmz', 0)
    CommonSE('101_hit_slash_1')
    CommonSE('021_bonecleak_0')
    PrivateSE('tmse_08')


@State
def CommandThrowChain():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 5, 0, 0, 0, 0, 0, 0)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        Size(500)
        WallCollisionDetection(1)
        FloorCollision(1)

        def upon_EVERY_FRAME():
            CallPrivateFunction('KusariAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_2:
                pass
        uponSendToLabel(32, 0)
    sprite('null', 1)
    RenderLayer(1)
    Unknown23143(-10000, -70000, 100)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 20, 0, 0, 0, 100)
    CallPrivateFunction('KusariParam', 0, 2, 0, 40, 0, 0, 0, 100)
    CallPrivateFunction('KusariParam', 0, 3, 0, 60, 0, 0, 0, 100)
    CallPrivateFunction('KusariParam', 0, 4, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariSpeed', 0, 5000, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationAngle(90000)
    sprite('null', 4)
    sprite('null', 4)
    Unknown23143(0, 0, 100)
    EndMomentum(1)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 50, 0, 35)
    sprite('null', 4)
    SetActionMark(1)
    sprite('null', 4)
    sprite('null', 4)
    sprite('null', 32767)
    label(0)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 3)
    SetActionMark(0)
    FloorCollision(1)
    sprite('null', 3)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()


@State
def tmef_403():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    sprite('null', 2)
    sprite('null', 3)
    sprite('vrtmef403_02', 3)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef403_03', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_AuraDelete', 0)
    sprite('vrtmef403_04', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrtmef403_05', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    sprite('vrtmef403_06', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrtmef403_07', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    sprite('vrtmef403_08', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrtmef403_09', 3)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)


@State
def UltimateAssault_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Damage(2400)
        MinimumDamage(15)
        AttackP2(70)
        AirUntechableTime(60)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(0)
        AirPushbackX(10000)
        AirPushbackY(30000)
        Hitstop(0)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        EnemyHitstopAddition(7, 7, 15)
        StarterRating(0)
        SetScaleX(2000)

        def upon_32():
            TeleportToObject(22)
            sendToLabel(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            AddCombo(3)
    sprite('null', 32767)
    label(0)
    sprite('tm430_AtkCol', 3)


@State
def eftm430_snake00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        Flip()
        Size(1100)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('vrhzef430_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 0)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 1)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 2)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 3)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 4)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 5)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 6)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 7)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 8)
    sprite('vrhzef430_00', 6)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 0)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 1)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 2)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 3)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 4)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 5)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 6)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 7)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 8)
    sprite('vrhzef430_01', 4)
    sprite('vrhzef430_02', 32767)
    AddX(80000)
    label(0)
    sprite('vrhzef430_03', 32767)
    AddX(80000)
    E0EAEffectPosition(3)
    IgnorePauses(3)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    label(1)
    sprite('vrhzef430_03', 1)
    EnableAfterimage(0)
    physicsXImpulse(0)
    sprite('vrhzef430_04', 2)
    sprite('null', 4)
    CreateObject('eftm430_snake01', -1)


@State
def eftm430_snakeOD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        Flip()
        Size(1000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('vrhzef430_03', 6)
    sprite('vrhzef430_03', 32767)
    AddX(80000)
    label(0)
    sprite('vrhzef430_03', 32767)
    AddX(80000)
    E0EAEffectPosition(3)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    physicsXImpulse(30000)
    label(1)
    sprite('vrhzef430_04', 4)
    EnableAfterimage(0)
    physicsXImpulse(0)
    sprite('null', 4)
    CreateObject('eftm430_snake01', -1)


@State
def eftm430_snake01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('tmef_430_nokori00', '')
    sprite('null', 6)
    sprite('null', 5)
    ConstantAlphaModifier(-17)


@State
def UltimateAssault_OD_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Damage(1000)
        MinimumDamage(20)
        AttackP2(100)
        AirUntechableTime(60)
        PushbackX(0)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(12000)
        YImpulseBeforeWallbounce(1600)
        Hitstop(0)
        UseSlashHitspark(1)
        AttackType(4)
        CHStateIfCHStart(3)
        StarterRating(0)
        SetScaleX(2000)

        def upon_32():
            TeleportToObject(22)
            sendToLabel(0)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                AddCombo(3)

        def upon_33():
            TeleportToObject(22)
            sendToLabel(1)
            FlipOnHit(1)
            Damage(2400)
            MinimumDamage(15)
            AttackP2(70)
            Hitstop(5)
            ResetVerticalDrag()

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                AddCombo(5)
    sprite('null', 32767)
    label(0)
    sprite('tm430_AtkCol', 3)
    RefreshMultihit()
    sprite('null', 32767)
    loopRest()
    ExitState()
    label(1)
    sprite('tm430_AtkCol', 3)
    RefreshMultihit()


@State
def UltimateAirAssault_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Damage(2400)
        MinimumDamage(15)
        AttackP1(90)
        AttackP2(70)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        PushbackX(0)
        AirPushbackX(-3000)
        AirPushbackY(40000)
        YImpulseBeforeWallbounce(2600)
        Hitstop(0)
        CHStateIfCHStart(3)
        UseSlashHitspark(1)
        EnemyHitstopAddition(7, 7, 15)
        StarterRating(0)
        SetScaleX(2000)
        TeleportToObject(22)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            AddCombo(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('tm430_AtkCol', 3)


@State
def eftm430_snake02():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        Flip()
        E0EAEffectPosition(2)
        Size(1200)
        AddX(80000)
        AlphaValue(0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
    label(0)
    sprite('vrhzef430_05', 5)
    ConstantAlphaModifier(26)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 0)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 1)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 2)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 3)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 4)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 5)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 6)
    ParticleSize(1400)
    CallCustomizableParticle('tmef_400_hand02', 7)
    gotoLabel(0)
    label(1)
    sprite('null', 6)
    CreateObject('eftm430_snake01test', -1)
    sprite('null', 32767)
    Size(1200)
    AddX(-80000)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    label(2)
    sprite('null', 11)
    DespawnEAEffect('eftm430_snake01test')
    EnableAfterimage(0)
    Size(1200)
    CreateObject('eftm430_snake02air', -1)


@State
def eftm430_snake01air():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Eff3DEffect('tmef_430_nokori01', '')
        Flip()
        TeleportToObject(22)
        Size(1500)
        AddY(150000)
    sprite('null', 15)


@State
def eftm430_snake02air():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Eff3DEffect('tmef_430_nokori01', '')
        TeleportToObject(3)
        SetScaleX(600)
    sprite('null', 5)
    sprite('null', 6)
    ConstantAlphaModifier(-51)


@State
def eftm430_snake01test():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('tmef_430_test00', '')
    sprite('null', 32767)


@State
def UltimateAirAssault_OD_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        Damage(1000)
        AttackP1(90)
        AttackP2(100)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        PushbackX(0)
        AirPushbackX(-1000)
        AirPushbackY(18000)
        YImpulseBeforeWallbounce(2800)
        HardKnockdown(1)
        UseSlashHitspark(1)
        AttackType(4)
        CHStateIfCHStart(3)
        StarterRating(0)
        SetScaleX(2000)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            AddCombo(3)

        def upon_32():
            TeleportToObject(22)
            sendToLabel(0)
            FlipOnHit(1)
            Damage(2400)
            MinimumDamage(15)
            AttackP2(70)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirPushbackX(8000)
            ResetVerticalDrag()
            YImpulseBeforeWallbounce(1600)
            HardKnockdown(0)
            Hitstop(5)

            def upon_OPPONENT_HIT():
                clearUponHandler(OPPONENT_HIT)
                AddCombo(5)
            if SLOT_137:
                DamageMultiplier(80)
        TeleportToObject(22)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('tm430_AtkCol', 3)
    RefreshMultihit()
    sprite('null', 32767)
    loopRest()
    ExitState()
    label(0)
    sprite('tm430_AtkCol', 3)
    RefreshMultihit()


@State
def eftm432():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(64000)
        AddY(64000)
    sprite('vrtmef432_00', 5)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_01', 5)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_02', 4)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrtmef432_03', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_04', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_05', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_06', 3)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_07', 2)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_08', 2)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_09', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_09', 2)
    CreateParticle('tmef_432backaura_01', 0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrtmef432_10', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_11', 4)
    CreateParticle('tmef_432backaura_01', 0)


@State
def eftm432_air():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(64000)
        AddY(64000)
    sprite('vrtmef432_00', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_01', 5)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_02', 4)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrtmef432_03', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_04', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_05', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_06', 3)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_07', 2)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_08', 2)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_09', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_09', 2)
    CreateParticle('tmef_432backaura_01', 0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrtmef432_10', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_11', 4)
    CreateParticle('tmef_432backaura_01', 0)


@State
def tmef433():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrhzef432_00', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrhzef432_01', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    CreateParticle('tmef_432backaura_01', 2)
    sprite('vrhzef432_02', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    CreateParticle('tmef_432backaura_01', 2)
    sprite('vrhzef432_03', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrhzef432_04', 6)
    RenderLayer(2)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    CreateParticle('tmef_432backaura_01', 2)
    sprite('vrhzef432_05', 6)
    sprite('vrhzef432_06', 3)
    Size(1100)
    ConstantAlphaModifier(-30)
    sprite('vrhzef432_06', 3)


@State
def tmef434_hand():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        LinkParticle('tmef_434_hand')
    label(0)
    sprite('null', 4)
    CreateParticle('tmef_434_hand_add', -1)
    gotoLabel(0)


@State
def tmef434_hand_2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        LinkParticle('tmef_434_hand')
    label(0)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    gotoLabel(0)


@State
def tmef434_hand_3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
    CreateParticle('tmef_434_hand2_add', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    CreateParticle('tmef_434_hand2_ryushi', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)
    sprite('null', 4)
    CreateParticle('tmef_434_hand2', -1)


@State
def eftm434_slashRed():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(3)
        TeleportToObject(22)
        AddY(300000)
        Size(1200)
    sprite('vrtmef434_00', 4)
    CreateParticle('tmef_434_shockcircle', -1)
    sprite('vrtmef434_01', 5)
    ScreenShake(40000, 40000)
    CreateParticle('tmef_434_shock00', -1)
    sprite('vrtmef434_01', 5)
    ScreenShake(40000, 40000)
    sprite('vrtmef434_02', 3)
    CreateObject('eftm434_slashBlack', -1)
    sprite('vrtmef434_03', 4)
    sprite('vrtmef434_04', 4)


@State
def eftm434_slashBlack():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('tmef_434slash', '')
        FaceSpawnLocation()
        AlphaValue(150)
        E0EAEffectPosition(2)
    sprite('null', 19)


@State
def eftm434_YotyouMoya():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        TeleportToObject(22)
        E0EAEffectPosition(22)
        AddY(150000)
    sprite('null', 5)
    sprite('null', 50)
    LinkParticle('tmef_434_chainmoya02')


@State
def eftm434_Chain00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('tmef_434chain00', '')
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    AddY(-50000)
    label(1)
    sprite('null', 10)
    sprite('null', 9)
    AlphaValue(0)
    CreateObject('eftm434_Chain00a', -1)


@State
def eftm434_Chain00a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('tmef_434chain00a', '')
        FaceSpawnLocation()
    sprite('null', 5)


@State
def eftm434_Chain01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        Eff3DEffect('tmef_434chain01', '')
    sprite('null', 19)
    sprite('null', 10)
    ConstantAlphaModifier(-20)


@State
def eftm_436_snake():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        FaceLeft()
        IgnoreScreenfreeze(1)
        AbsoluteY(0)

        def upon_EVERY_FRAME():
            if not SLOT_2:
                ScreenPosition(1)
                XPositionRelativeFacing(-640000)
            else:
                ScreenPosition(0)
                EffectPosition(22, 103)
                Unknown4022(22)
    sprite('null', 35)
    Visibility(1)
    sprite('vrtmef436_00', 5)
    Visibility(0)
    AddY(64000)
    CreateObject('eftm_436_snake_pt', -1)
    sprite('null', 1)
    CreateObject('eftm_436_snake_atk', -1)


@State
def eftm_436_snake_atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        FaceLeft()
        TeleportToObject(3)
        AddY(200000)
        FloorCollision(1)
        ScreenCollision(1)
        IgnoreFinishStop(1)
    sprite('vrtmef436_01', 5)
    AddY(96000)
    physicsYImpulse(-20000)
    sprite('vrtmef436_02', 5)
    AddY(-96000)
    sprite('vrtmef436_03', 6)
    CreateObject('eftm_436_snake_wind', -1)
    YAccel(1000)
    LinkParticle('tmef_436_finish')
    sprite('vrtmef436_04', 4)
    TeleportToObject(3)
    sprite('vrtmef436_05', 6)
    sprite('vrtmef436_06', 6)
    sprite('null', 30)


@State
def eftm_436_snake_pt():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        TeleportToObject(22)
        AbsoluteY(1000000)
    sprite('null', 1)
    CreateParticle('tmef_436_assault2', -1)


@State
def eftm_436_snake_wind():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', '')
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        BlendMode_Add()
        AlphaValue(255)
        RedColorValue(63)
        AddY(230000)
        AddScale(1000)
    sprite('null', 20)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    ConstantAlphaModifier(-20)


@State
def eftm_436_assault():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddY(160000)
    sprite('null', 1)
    CreateObject('eftm_436_assault_3d', -1)
    CreateObject('eftm_436_assault_3d2', -1)
    ParticleRotationAngle(60000)
    CallCustomizableParticle('tmef_436_assault', -1)
    sprite('null', 1)
    CreateObject('eftm_436_assault_3d', -1)


@State
def eftm_436_assault2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddY(160000)
        Flip()
    sprite('null', 1)
    CreateObject('eftm_436_assault_3d', -1)
    CreateObject('eftm_436_assault_3d2', -1)
    ParticleRotationAngle(60000)
    CallCustomizableParticle('tmef_436_assault', -1)
    sprite('null', 1)
    CreateObject('eftm_436_assault_3d', -1)


@State
def eftm_436_assault_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('tmef_436_assault', '')
        FaceSpawnLocation()
        SetScaleY(1100)
        SetScaleX(2000)
        RotationAngle(-30000)
        RedColorValue(127)
        GreenColorValue(255)
        BlueColorValue(255)
        ConstantRedModifier(-10)
        ConstantGreenModifier(-10)
        ConstantBlueModifier(-10)
    sprite('null', 20)
    SetScaleSpeedY(-45)
    ConstantAlphaModifier(-10)


@State
def eftm_436_assault_3d2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('tmef_436_assault_b', '')
        FaceSpawnLocation()
        SetScaleY(1100)
        SetScaleX(2000)
        RotationAngle(-30000)
    sprite('null', 10)
    SetScaleSpeedY(-45)
    sprite('null', 10)
    ConstantAlphaModifier(-20)


@State
def UltimateChainLand():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        BlendMode_Normal()
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('UltimateKusariAtkVectorX', 0, 80, 0, 0, 0, 0, 0, 0
            )
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_2:
                RotationSomething(0)
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                DeleteObject(23)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        AttackOff()
    sprite('vr_chain_tip03', 1)
    SetActionMark(1)
    SetZVal(-500)
    Unknown23143(80000, -2000, 70)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 80)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    loopRest()
    ExitState()
    label(0)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip04', 32767)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    loopRest()
    ExitState()
    label(1)
    SetActionMark(0)
    AddX(120000)
    EndAttack()
    sprite('vr_chain_tip04', 28)
    RenderLayer(2)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 5)
    ConstantAlphaModifier(-5)
    sprite('vr_chain_tip04', 10)
    RenderLayer(0)
    sprite('vr_chain_tip04', 3)
    SetZVal(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    sprite('vr_chain_tip04', 7)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 45, 0, 55)
    sprite('vr_chain_tip04', 10)
    loopRest()
    ExitState()
    label(2)
    AddX(60000)
    sprite('vr_chain_tip04', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip04', 3)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 27)
    SetZVal(500)
    sprite('vr_chain_tip04', 30)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    ExitState()
    label(3)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip04', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip04', 30)
    ConstantAlphaModifier(-31)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    ExitState()


@State
def UltimateChainLand2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        BlendMode_Normal()
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        CallPrivateFunction('KusariKansetsu', 0, 3, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('UltimateKusariAtkVectorX', 0, 80, 0, 0, 0, 0, 0, 0
            )

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_2:
                RotationSomething(0)
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                DeleteObject(23)
        uponSendToLabel(32, 0)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        AttackOff()
    sprite('vr_chain_tip05', 1)
    SetActionMark(1)
    SetZVal(-500)
    Unknown23143(70000, 0, 70)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariMochite', 0, 110, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip05', 4)
    sprite('vr_chain_tip05', 60)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    loopRest()
    ExitState()
    label(0)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip05', 32767)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    loopRest()
    ExitState()
    label(1)
    SetActionMark(0)
    AddX(120000)
    EndAttack()
    sprite('vr_chain_tip05', 28)
    EndMomentum(1)
    Unknown23143(-80000, -5000, 70)
    sprite('vr_chain_tip05', 5)
    Unknown23143(0, 0, 70)
    sprite('vr_chain_tip05', 10)
    Unknown23143(60000, 50000, 70)
    sprite('vr_chain_tip05', 10)
    Unknown23143(0, 0, 70)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 85, 0, 55)
    SetZVal(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    sprite('vr_chain_tip04', 10)
    loopRest()
    ExitState()
    label(2)
    AddX(60000)
    sprite('vr_chain_tip05', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip05', 3)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip05', 27)
    SetZVal(500)
    sprite('vr_chain_tip05', 30)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    ExitState()
    label(3)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip05', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip05', 30)
    ConstantAlphaModifier(-31)
    Unknown23144(3, 0, 110, 0, 0, 0, 0, 0, 75, 0, 4)
    loopRest()
    sprite('vr_chain_tip05', 1)
    EndObject()
    loopRest()
    ExitState()


@State
def UltimateChainAir():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        BlendMode_Normal()
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('UltimateKusariAtkVectorX', 0, 80, 0, 0, 0, 0, 0, 0
            )
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_2:
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                DeleteObject(23)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        AttackOff()
    sprite('vr_chain_tip03aa', 1)
    SetActionMark(1)
    SetZVal(-500)
    Unknown23143(80000, 36000, 70)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariMochite', 0, 110, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationAngle(-30000)
    sprite('vr_chain_tip03aa', 80)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    loopRest()
    ExitState()
    label(0)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip04', 32767)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    loopRest()
    ExitState()
    label(1)
    sprite('vr_chain_tip04', 10)
    SetActionMark(0)
    SLOT_51 = 1
    EnableAfterimage(0)
    Unknown23143(-80000, -35000, 40)
    AddRotationPerFrame(-1000)
    sprite('vr_chain_tip04', 12)
    sprite('vr_chain_tip04', 10)
    BlendMode_Normal()
    ConstantAlphaModifier(-5)
    RenderLayer(5)
    sprite('vr_chain_tip04', 6)
    Unknown23143(180000, -25000, 25)
    sprite('vr_chain_tip04', 10)
    RenderLayer(0)
    Unknown23143(-150000, 80000, 25)
    SetZVal(-500)
    AddRotationPerFrame(0)
    RotationAngle(30000)
    ConstantAlphaModifier(-10)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    label(2)
    AddX(60000)
    sprite('vr_chain_tip04', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip04', 3)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 27)
    SetZVal(500)
    sprite('vr_chain_tip04', 30)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    ExitState()
    label(3)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip04', 10)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip04', 20)
    ConstantAlphaModifier(-12)
    Unknown23144(3, 0, 110, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    ExitState()


@State
def UltimateChainAir2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        BlendMode_Normal()
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        CallPrivateFunction('KusariKansetsu', 0, 3, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('UltimateKusariAtkVectorX', 0, 80, 0, 0, 0, 0, 0, 0
            )

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_2:
                RotationSomething(0)
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                DeleteObject(23)
        uponSendToLabel(32, 0)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        AttackOff()
    sprite('vr_chain_tip05', 1)
    SetActionMark(1)
    SetZVal(-500)
    Unknown23143(60000, 30000, 30)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariMochite', 0, 109, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationAngle(-30000)
    sprite('vr_chain_tip05', 4)
    sprite('vr_chain_tip05', 60)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    loopRest()
    ExitState()
    label(0)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip05', 32767)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    loopRest()
    ExitState()
    label(1)
    SetActionMark(0)
    AddX(120000)
    EndAttack()
    sprite('vr_chain_tip05', 28)
    EndMomentum(1)
    Unknown23143(-80000, -5000, 70)
    sprite('vr_chain_tip05', 5)
    Unknown23143(0, 0, 70)
    sprite('vr_chain_tip05', 10)
    Unknown23143(60000, 50000, 70)
    sprite('vr_chain_tip05', 10)
    Unknown23143(0, 0, 70)
    Unknown23144(3, 0, 110, 0, 0, 0, 0, 0, 85, 0, 55)
    SetZVal(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    sprite('vr_chain_tip04', 10)
    loopRest()
    ExitState()
    label(2)
    AddX(60000)
    sprite('vr_chain_tip05', 3)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip05', 3)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip05', 27)
    SetZVal(500)
    sprite('vr_chain_tip05', 30)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    ExitState()
    label(3)
    SetActionMark(0)
    AddX(60000)
    sprite('vr_chain_tip05', 10)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip05', 20)
    ConstantAlphaModifier(-12)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 75, 0, 4)
    loopRest()
    sprite('vr_chain_tip05', 1)
    EndObject()
    loopRest()
    ExitState()


@State
def UltimateChain3rd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        Flip()
        BlendMode_Normal()
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('tmef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('tmef_exheadmoveopt', -1)
        uponSendToLabel(32, 0)
        AttackOff()
    sprite('vr_chain_tip03aa', 1)
    SetActionMark(1)
    Unknown23143(140000, 120000, 90)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    RotationAngle(-30000)
    sprite('vr_chain_tip03aa', 15)
    SetActionMark(1)
    CallPrivateFunction('KusariSpeed', 0, 5000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 32767)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    label(0)
    sprite('vr_chain_tip04', 9)
    SetActionMark(0)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    sprite('vr_chain_tip04', 3)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 80, 0, 10)
    sprite('vr_chain_tip04', 3)
    SetZVal(500)
    sprite('vr_chain_tip04', 3)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 100, 0, 75)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    ExitState()


@State
def UltimateShot_FinishAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(2000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(100)
        HardKnockdown(20)
        PushbackX(0)
        AirPushbackX(3000)
        AirPushbackY(-80000)
        YImpulseBeforeWallbounce(0)
        Hitstop(5)
        FlipOnHit(1)
        DefeatOpponentBehavior(1)
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        TeleportToObject(22)
    sprite('tm436_AtkCol', 3)


@State
def UltimateShot_FinishAtk2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(3500)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackY(70000)
        YImpulseBeforeWallbounce(3000)
        HardKnockdown(1)
        Hitstop(0)
        FlipOnHit(1)
        DamageEffect(9, '')
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        HitAnywhere(1)
        TeleportToObject(22)
    sprite('tm436_AtkCol', 3)


@State
def UltimateShotAtk_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(800)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(100)
        AirPushbackX(10000)
        AirPushbackY(8000)
        YImpulseBeforeWallbounce(0)
        Hitstop(6)
        DisableOppPushCollision(1)
        DefeatOpponentBehavior(1)
        AttackDirection(1)
        HitAnywhere(1)
        AttackType(4)
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
    sprite('null', 10)
    AddX(-600000)
    AddY(-1300000)
    sprite('tm436_19', 2)
    physicsXImpulse(78000)
    physicsYImpulse(48000)
    sprite('tm436_20', 2)
    sprite('tm436_21', 3)
    RefreshMultihit()
    CreateObject('eftm_436_assault', -1)
    sprite('tm436_22', 3)
    sprite('tm436_23', 3)
    sprite('null', 10)
    TeleportToObject(22)
    EndMomentum(1)
    AddX(1000000)
    AddY(-600000)
    sprite('tm436_33', 3)
    physicsXImpulse(-80000)
    physicsYImpulse(60000)
    sprite('tm436_34', 3)
    sprite('tm436_35', 3)
    sprite('tm436_36', 3)
    RefreshMultihit()
    FlipOnHit(1)
    UseSlashHitspark(1)
    CreateObject('eftm_436_assault2', -1)
    sprite('tm436_37', 3)
    sprite('tm436_38', 3)
    sprite('tm436_39', 3)
    sprite('null', 5)
    TeleportToObject(22)
    EndMomentum(1)
    AddX(-500000)
    AddY(-400000)
    sprite('tm436_19', 1)
    physicsXImpulse(104000)
    physicsYImpulse(64000)
    sprite('tm436_20', 2)
    sprite('tm436_21', 3)
    RefreshMultihit()
    UseSlashHitspark(0)
    FlipOnHit(1)
    CreateObject('eftm_436_assault', -1)
    sprite('tm436_22', 3)
    sprite('tm436_23', 3)
    sprite('null', 5)
    TeleportToObject(22)
    EndMomentum(1)
    AddX(1000000)
    AddY(-600000)
    sprite('tm436_33', 2)
    physicsXImpulse(-128000)
    physicsYImpulse(96000)
    sprite('tm436_34', 2)
    sprite('tm436_35', 3)
    sprite('tm436_36', 3)
    RefreshMultihit()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackY(10000)
    YImpulseBeforeWallbounce(1000)
    UseSlashHitspark(1)
    CreateObject('eftm_436_assault2', -1)
    sprite('tm436_37', 3)
    sprite('tm436_38', 3)
    sprite('tm436_39', 3)


@State
def UltimateShot_FinishAtk_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(3000)
        MinimumDamage(15)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(100)
        HardKnockdown(20)
        PushbackX(0)
        AirPushbackX(3000)
        AirPushbackY(-80000)
        YImpulseBeforeWallbounce(0)
        Hitstop(5)
        FlipOnHit(1)
        DefeatOpponentBehavior(1)
        AttackType(4)
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        TeleportToObject(22)
    sprite('tm436_AtkCol', 3)


@State
def UltimateShot_FinishAtk2_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(4000)
        MinimumDamage(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackY(70000)
        YImpulseBeforeWallbounce(3000)
        HardKnockdown(1)
        Hitstop(0)
        FlipOnHit(1)
        DamageEffect(9, '')
        AttackType(4)
        OnlyHitPlayer(1)
        PassByArmor(1)
        CHStateIfCHStart(3)
        HitAnywhere(1)
        TeleportToObject(22)
    sprite('tm436_AtkCol', 3)


@State
def tmef_435_weapon():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(0)
        AddY(144000)
    sprite('vrtmef435_weapon', 16)
    AlphaValue(0)
    ConstantAlphaModifier(16)
    Unknown23123(-1, 32)
    sprite('vrtmef435_weapon', 32767)
    physicsYImpulse(-3000)


@State
def tmef_435_weapon_pt():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        AddY(144000)
    sprite('null', 32767)
    LinkParticle('tmef_435_weapon')


@State
def tmef_435_slash():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(2)
        AddY(10000)
        AddX(10000)
        RedColorValue(127)
        BlueColorValue(127)
    sprite('vrtmef435_00', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef435_01', 3)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrtmef435_02', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef435_03', 3)


@State
def tmef_435_slash2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(2)
        RedColorValue(127)
        BlueColorValue(127)
    sprite('vrtmef435_10', 2)
    sprite('vrtmef435_11', 2)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrtmef435_12', 4)


@State
def tmef_435_snake():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(64000)
        AddY(64000)
        AlphaValue(191)
    label(0)
    sprite('vrtmef435_30', 40)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    CreateParticle('tmef_432backaura_01', 2)
    gotoLabel(0)


@State
def tmef_435_snake_b():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(64000)
        AddY(64000)
        SetZVal(100)
        AlphaValue(191)
    label(0)
    sprite('vrtmef435_30b', 40)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    gotoLabel(0)


@State
def tmef_435_snakemesh():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        AddX(64000)
        AddY(64000)
    sprite('vrtmef435_30z', 4)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    RedColorValue(191)
    BlueColorValue(191)
    sprite('vrtmef435_30z', 16)
    ConstantAlphaModifier(-16)


@State
def tmef_435_wavelight():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_435_wavelight', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AlphaValue(127)
        RedColorValue(0)
        BlueColorValue(0)
        Size(1750)
        AddX(53000)
        AddY(273000)
    sprite('null', 24)
    loopRest()


@State
def tmef_435_damege():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AddY(256000)
        AddX(64000)
    sprite('null', 1)
    CreateParticle('tmef_435_damege', -1)


@State
def tmef_435_magiccircle():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        TeleportToObject(22)
        AddY(256000)
        AddX(64000)
    sprite('null', 32767)
    LinkParticle('tmef_435_magiccircle')
    CreateObject('tmef_435_smallcircle', -1)
    CreateObject('tmef_435_smallcircle2', -1)


@State
def tmef_435_magiccircle_end():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        TeleportToObject(22)
        AddY(384000)
        AddX(64000)
    sprite('null', 32767)
    CreateParticle('tmef_435_magiccircle_end', -1)


@State
def tmef_435_smallcircle():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        AddX(132000)
    sprite('null', 32767)
    LinkParticle('tmef_435_smallcircle')


@State
def tmef_435_smallcircle2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        AddX(-144000)
    sprite('null', 32767)
    LinkParticle('tmef_435_smallcircle')


@State
def tmef_435_finish():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(64000)
        AddY(64000)
        AlphaValue(223)
    sprite('null', 6)
    sprite('vrtmef435_32', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_435_finish', -1)
    sprite('vrtmef435_33', 4)
    CreateParticle('tmef_432backaura_01', 0)
    ConstantAlphaModifier(-50)


@State
def tmef_435_finish_b():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(64000)
        AddY(64000)
        SetZVal(100)
        AlphaValue(223)
    sprite('vrtmef435_31', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrtmef435_32b', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef435_33b', 4)
    CreateParticle('tmef_432backaura_01', 0)
    ConstantAlphaModifier(-50)


@State
def tmef_435_Samaso():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(80000)
    sprite('vrhzef401_00', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrhzef401_01', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    sprite('vrhzef401_02', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    sprite('vrhzef401_03', 2)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    sprite('vrhzef401_04', 8)
    CreateObject('tmef_Aura', 0)
    CreateObject('tmef_Aura', 1)
    CreateObject('tmef_Aura', 2)
    CreateObject('tmef_Aura', 3)
    CreateObject('tmef_Aura', 4)
    CreateObject('tmef_Aura', 5)
    CreateObject('tmef_Aura', 6)
    CreateObject('tmef_Aura', 7)
    CreateObject('tmef_Aura', 8)
    CreateObject('tmef_Aura', 9)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    CreateObject('tmef_AuraDelete', 6)
    CreateObject('tmef_AuraDelete', 7)
    CreateObject('tmef_AuraDelete', 8)
    CreateObject('tmef_AuraDelete', 9)
    sprite('vrhzef401_05', 4)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)
    sprite('vrhzef401_06', 6)
    CreateObject('tmef_AuraDelete', 0)
    CreateObject('tmef_AuraDelete', 1)
    CreateObject('tmef_AuraDelete', 2)
    CreateObject('tmef_AuraDelete', 3)
    CreateObject('tmef_AuraDelete', 4)
    CreateObject('tmef_AuraDelete', 5)


@State
def tmef_435_ODaura():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 32767)
    LinkParticle('tmef_401_aura')


@State
def tmef_440_magiccircle():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-35000)
        uponSendToLabel(32, 0)
    sprite('null', 8)
    AlphaValue(0)
    ConstantAlphaModifier(15)
    Size(2000)
    SetScaleSpeed(60)
    LinkParticle('tmef_440circle')
    sprite('null', 3)
    SetScaleSpeed(0)
    label(1)
    sprite('null', 3)
    gotoLabel(1)
    label(0)
    sprite('null', 120)
    ConstantAlphaModifier(-32)


@State
def tmef_440_snakes():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-100000)
    sprite('null', 9)
    CreateObject('tmef_440_snake', -1)

    def RunOnObject_1():
        AddX(100000)
    PrivateSE('tmse_10')
    sprite('null', 9)
    CreateObject('tmef_440_snake', -1)

    def RunOnObject_1():
        AddX(-100000)
    PrivateSE('tmse_02')
    sprite('null', 9)
    CreateObject('tmef_440_snake', -1)

    def RunOnObject_1():
        AddX(100000)
    PrivateSE('tmse_02')
    sprite('null', 9)
    CreateObject('tmef_440_snake', -1)

    def RunOnObject_1():
        AddX(-100000)
    PrivateSE('tmse_02')


@State
def tmef_440_snake():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        AddX(64000)
    sprite('vrtmef440_00', 4)
    CreateObject('tmef_440_snake_pt', -1)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrtmef440_01', 3)
    sprite('vrtmef440_02', 3)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrtmef440_03', 3)
    sprite('vrtmef440_04', 3)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrtmef440_05', 3)
    sprite('vrtmef440_06', 3)


@State
def tmef_440_snake_pt():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        AddX(-70000)
    label(0)
    sprite('null', 7)
    CreateParticle('tmef_440aura3', -1)
    gotoLabel(0)


@State
def tmef_440_snake_large():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(60000)
    sprite('vrtmef440_50', 10)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    CreateObject('tmef_440_snake_large_pt', -1)
    PrivateSE('tmse_10')
    sprite('vrtmef440_51', 5)
    sprite('vrtmef440_52', 5)
    sprite('vrtmef440_53', 5)
    CreateParticle('tmef_440aura2', 0)
    CreateParticle('tmef_440aura2', 1)
    CreateParticle('tmef_440aura2', 2)
    PrivateSE('tmse_10')
    sprite('vrtmef440_54', 5)
    CreateParticle('tmef_440aura2', 0)
    CreateParticle('tmef_440aura2', 1)
    CreateParticle('tmef_440aura2', 2)
    sprite('vrtmef440_55', 5)
    sprite('vrtmef440_56', 5)
    sprite('vrtmef440_57', 1)
    sprite('vrtmef440_57', 8)
    ConstantAlphaModifier(-45)


@State
def tmef_440_snake_large_pt():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        AddX(-150000)
    label(0)
    sprite('null', 7)
    CreateParticle('tmef_440aura', -1)
    gotoLabel(0)


@State
def tmef_215():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrtmef215_00', 3)
    AlphaValue(64)
    ConstantAlphaModifier(32)
    sprite('vrtmef215_01', 5)
    AlphaValue(255)
    ConstantAlphaModifier(-8)
    LinkParticle('tmef_215splash')
    sprite('vrtmef215_02', 3)
    CreateParticle('tmef_215splash2', -1)
    sprite('null', 30)


@State
def ASTcamera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        AddX(300000)
    sprite('null', 32767)


@State
def tmef_450_knife():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Normal()
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
    sprite('vrtmef450_knife00', 3)
    ParticleRotationAngle(-40000)
    CallCustomizableParticle('tmef_450_knife', 0)
    sprite('vrtmef450_knife01', 3)


@State
def tmef_450_knife2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Normal()
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
    sprite('vrtmef450_knife10', 4)
    ParticleRotationAngle(-55000)
    CallCustomizableParticle('tmef_450_knife', 0)
    sprite('vrtmef450_knife11', 4)


@State
def tmef_aststartcircle():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
    sprite('null', 16)
    LinkParticle('tmef_aststartcircle')
    SetScaleSpeed(25)
    PrivateSE('tmse_12')
    sprite('null', 230)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 32)
    clearUponHandler(32)
    ConstantAlphaModifier(-8)


@State
def AstralHeat_1st():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(0)
        MinimumDamage(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(500)
        Crumple(9999)
        PushbackX(0)
        OppPositionOnHit(1, 0, 0)
        DefeatOpponentBehavior(1)
        DisableOppPushCollision(1)
        AddX(600000)

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)
            NoAttackDuringAction(1)
    sprite('tm450_AtkCol', 16)
    CreateObject('tmef_aststartcircle', -1)


@State
def AstralHeat_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(5)
        Damage(100)
        MinimumDamage(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(1000)
        AirPushbackX(0)
        AirPushbackY(10)
        YImpulseBeforeWallbounce(0)
        OppPositionOnHit(1, 0, 50000)
        DefeatOpponentBehavior(1)
        TeleportToObject(22)
    sprite('tm450_AtkCol', 8)
    CreateObject('tmef_450_chain', -1)
    CreateObject('tmef_450_chain2', -1)
    sprite('tm450_AtkCol', 8)


@State
def tmef_450_chain():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_450_chain', '')
        BlendMode_Normal()
    sprite('null', 520)
    sprite('null', 60)
    ConstantAlphaModifier(-20)


@State
def tmef_450_chain2():

    def upon_IMMEDIATE():
        Flip()
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('tmef_450_chain2', '')
        BlendMode_Normal()
        Rotation(3000)
        AddY(40000)
    sprite('null', 520)
    sprite('null', 60)
    ConstantAlphaModifier(-20)


@State
def AstralHeat_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(3)
        Damage(400)
        MinimumDamage(100)
        AttackP2(99)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(1000)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(0)
        Hitstop(0)
        DefeatOpponentBehavior(1)
        uponSendToLabel(32, 1)
    label(0)
    sprite('tm450_AtkCol2', 5)
    RefreshMultihit()
    EffectPosition(22, 105)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 3)


@State
def tmef_450_hole():

    def upon_IMMEDIATE():
        AddX(-192000)
        AddY(320000)
        uponSendToLabel(32, 1)
    sprite('null', 30)
    LinkParticle('tmef_450_hole')
    CreateParticle('tmef_450_hole2', -1)
    CommonSE('022_magiccircle_b')
    label(0)
    sprite('null', 5)
    CreateObject('tmef_450_snake_a', -1)
    CreateObject('tmef_450_linework', -1)
    PrivateSE('tmse_03')
    sprite('null', 5)
    CreateObject('tmef_450_snake_b', -1)
    CreateObject('tmef_450_linework', -1)
    sprite('null', 5)
    CreateObject('tmef_450_snake_c', -1)
    CreateObject('tmef_450_linework', -1)
    sprite('null', 5)
    CreateObject('tmef_450_snake_d', -1)
    CreateObject('tmef_450_linework', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32)
    SetScaleSpeed(-25)
    ConstantAlphaModifier(-4)


@State
def tmef_450_linework():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 1)
    CreateParticle('tmef_450_bg6', -1)


@State
def tmef_450_snake_a():

    def upon_IMMEDIATE():
        Eff3DEffect('tmef_450_snake_a', '')
        BlendMode_Normal()
        Size(2000)
        AddY(-64000)
    sprite('null', 20)
    CreateParticle('tmef_450_snakesplash', -1)


@State
def tmef_450_snake_b():

    def upon_IMMEDIATE():
        Eff3DEffect('tmef_450_snake_b', '')
        BlendMode_Normal()
        Size(2000)
        AddY(-96000)
    sprite('null', 20)
    CreateParticle('tmef_450_snakesplash', -1)


@State
def tmef_450_snake_c():

    def upon_IMMEDIATE():
        Eff3DEffect('tmef_450_snake_b', '')
        BlendMode_Normal()
        FaceSpawnLocation()
        Size(2000)
        AddY(128000)
    sprite('null', 20)
    CreateParticle('tmef_450_snakesplash', -1)


@State
def tmef_450_snake_d():

    def upon_IMMEDIATE():
        Eff3DEffect('tmef_450_snake_a', '')
        BlendMode_Normal()
        FaceSpawnLocation()
        Size(2000)
        AddY(64000)
    sprite('null', 20)
    CreateParticle('tmef_450_snakesplash', -1)


@State
def tmef_450_aura():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('tmef_450_aura', -1)


@State
def tmef_450_aura2():

    def upon_IMMEDIATE():
        pass
    label(0)
    sprite('null', 1)
    CreateParticle('tmef_450_aura2', 103)
    gotoLabel(0)


@State
def tmef_450_bg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    label(0)
    sprite('null', 2)
    CreateParticle('tmef_450_bg', -1)
    gotoLabel(0)


@State
def tmef_450_bg2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    label(0)
    sprite('null', 6)
    CreateParticle('tmef_450_bg2', -1)
    gotoLabel(0)


@State
def tmef_450_henshinshock():

    def upon_IMMEDIATE():
        AddY(256000)
    sprite('null', 1)
    CreateParticle('tmef_450_henshinshock', -1)


@State
def tmef_450_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        PaletteIndex(0)
    sprite('vrtmef450_90', 6)
    CreateObject('tmef_450_slash_3D', 0)
    CreateObject('tmef_450_slash_b_3D', 0)
    sprite('vrtmef450_91', 6)


@State
def tmef_450_slash_3D():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        E0EAEffectPosition(3)
        Eff3DEffect('tmef_450_slash', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        XPositionRelativeFacing(576000)
        RotationAngle(110000)
        SetScaleX(5000)
        SetScaleY(2000)
    sprite('null', 15)
    CreateParticle('tmef_450_finish', -1)
    SetScaleSpeedY(-40)
    sprite('null', 16)
    ConstantAlphaModifier(-21)


@State
def tmef_450_slash_b_3D():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        E0EAEffectPosition(3)
        Eff3DEffect('tmef_450_slash_b', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        XPositionRelativeFacing(576000)
        RotationAngle(110000)
        SetScaleX(4000)
        SetScaleY(2000)
    sprite('null', 15)
    SetScaleSpeedY(-40)
    sprite('null', 16)
    ConstantAlphaModifier(-21)


@State
def tmef_450_end():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Sub()
    sprite('vrtmef450_37z', 30)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    CreateParticle('tmef_450_aura4', 0)
    CreateParticle('tmef_450_aura4', 1)
    CreateParticle('tmef_450_aura4', 2)
    CreateParticle('tmef_450_aura4', 3)
    CreateParticle('tmef_450_aura4', 4)
    CreateParticle('tmef_450_aura4', 0)
    sprite('vrtmef450_37z', 25)
    ConstantAlphaModifier(-10)
    sprite('vrtmef450_37z', 17)
    ConstantAlphaModifier(-12)


@State
def tmef611S():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    label(0)
    sprite('vrtmef611_expos00', 15)
    CreateParticle('tmef_611_aura2_hinoko', 0)
    CreateParticle('tmef_611_aura2_hinoko', 1)
    CreateParticle('tmef_611_aura2_hinoko', 2)
    CreateParticle('tmef_611_aura2_hinoko', 3)
    CreateParticle('tmef_611_aura2_hinoko', 4)
    CreateParticle('tmef_611_aura2_hinoko', 5)
    CreateParticle('tmef_611_aura2_hinoko', 6)
    CreateParticle('tmef_611_aura2_hinoko', 7)
    CreateParticle('tmef_611_aura2_hinoko', 8)
    gotoLabel(0)


@State
def tmef611M():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    label(0)
    sprite('vrtmef611_expos01', 15)
    CreateParticle('tmef_611_aura3_sub', 0)
    CreateParticle('tmef_611_aura3_sub', 1)
    CreateParticle('tmef_611_aura3_sub', 2)
    CreateParticle('tmef_611_aura3_sub', 3)
    CreateParticle('tmef_611_aura3_sub', 4)
    CreateParticle('tmef_611_aura3_sub', 5)
    CreateParticle('tmef_611_aura3_sub', 6)
    CreateParticle('tmef_611_aura3_sub', 7)
    CreateParticle('tmef_611_aura3_sub', 8)
    CreateParticle('tmef_611_aura3_sub', 8)
    CreateParticle('tmef_611_aura3_sub', 9)
    CreateParticle('tmef_611_aura3_sub', 10)
    CreateParticle('tmef_611_aura3_sub', 11)
    CreateParticle('tmef_611_aura3_sub', 12)
    CreateParticle('tmef_611_aura3_sub', 13)
    gotoLabel(0)


@State
def tmef611():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('vrtmef611_expos', 32767)
    CreateParticle('tmef_611_firstshock00', -1)
    CreateObject('tmef611solo', 1)
    CreateObject('tmef611solo', 2)
    CreateObject('tmef611solo', 3)
    CreateObject('tmef611solo', 4)
    CreateObject('tmef611solo', 5)
    CreateObject('tmef611solo', 6)
    CreateObject('tmef611solo', 7)
    CreateObject('tmef611solo', 8)
    CreateObject('tmef611solo', 9)
    CreateObject('tmef611solo', 10)
    CreateObject('tmef611solo', 11)
    CreateObject('tmef611solo', 12)
    CreateObject('tmef611solo', 13)
    CreateObject('tmef611solo', 14)
    CreateObject('tmef611solo', 15)
    CreateObject('tmef611solo', 16)
    CreateObject('tmef611solo', 17)
    CreateObject('tmef611solo', 18)
    CreateObject('tmef611solo', 19)
    CreateObject('tmef611solo', 20)


@State
def tmef611solo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 32767)
    LinkParticle('tmef_611_aura01')


@State
def SummonHZ():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def TakeBowHZ():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('hz601_00', 5)
    sprite('hz601_01', 5)
    sprite('hz601_02', 5)
    sprite('hz601_03', 5)
    sprite('hz601_04', 5)
    sprite('hz601_05', 5)
    sprite('hz601_06', 5)
    sprite('hz601_07', 5)
    sprite('hz601_08', 5)
    sprite('hz601_09', 5)
    sprite('hz601_10', 5)
    sprite('hz601_11', 5)
    sprite('hz601_12', 32767)


@State
def TakeBowHZEnd():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('hz601_13', 6)
    sprite('hz601_14', 6)
    sprite('hz601_15', 6)
    sprite('hz601_16', 6)
    sprite('hz601_17', 7)
    sprite('hz601_18', 5)
    sprite('hz601_19', 5)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def ThinkingHZ():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('hz610_00', 6)
    sprite('hz610_01', 6)
    sprite('hz610_02', 6)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    label(0)
    sprite('hz610_03', 6)
    sprite('hz610_04', 6)
    sprite('hz610_05', 6)
    loopRest()
    gotoLabel(0)


@State
def ThinkingHZEnd():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('hz610_02', 6)
    sprite('hz610_01', 6)
    sprite('hz610_00', 6)
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def LaughingHZ():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('hz301_00', 6)
    sprite('hz301_01', 6)
    label(0)
    sprite('hz301_02', 6)
    sprite('hz301_03', 6)
    loopRest()
    gotoLabel(0)


@State
def HeatDrainEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        LinkParticle('tmef_heatup')
    sprite('null', 36)


@State
def tmef433_event():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrhzef432_00', 3)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrhzef432_00', 3)
    physicsXImpulse(40000)
    sprite('vrhzef432_01', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrhzef432_02', 6)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrhzef432_03', 6)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrhzef432_04', 2)
    RenderLayer(2)
    CreateParticle('tmef_432backaura_01', 0)
    CreateParticle('tmef_432backaura_01', 1)
    sprite('vrhzef432_04', 4)
    EndMomentum(1)
    sprite('vrhzef432_05', 6)
    sprite('vrhzef432_06', 3)
    Size(1100)
    ConstantAlphaModifier(-30)
    sprite('vrhzef432_06', 3)


@State
def eftm432_event():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(64000)
        AddY(64000)
    sprite('vrtmef432_00', 3)
    sprite('vrtmef432_01', 5)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_02', 4)
    CreateParticle('tmef_432backaura_01', 0)
    sprite('vrtmef432_03', 4)
    sprite('vrtmef432_04', 4)
    sprite('vrtmef432_05', 4)
    sprite('vrtmef432_06', 4)


@State
def eftm434_slashRed_event():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(3)
        AddY(300000)
        Size(1200)
    sprite('vrtmef434_00', 4)
    CreateParticle('tmef_434_shockcircle', -1)
    sprite('vrtmef434_01', 5)
    ScreenShake(40000, 40000)
    CreateParticle('tmef_434_shock00', -1)
    sprite('vrtmef434_01', 5)
    ScreenShake(40000, 40000)
    sprite('vrtmef434_02', 3)
    CreateObject('eftm434_slashBlack', -1)
    sprite('vrtmef434_03', 4)
    sprite('vrtmef434_04', 4)


@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)

        def upon_EVERY_FRAME():
            TeleportToObject(3)
            SLOT_51 = SLOT_19
            SLOT_51 = SLOT_51 / 4
            CopyFromRightToLeft(23, 2, 52, 3, 2, 22)
            CopyFromRightToLeft(23, 2, 53, 22, 2, 22)
            if SLOT_52 < SLOT_53:
                SLOT_XDistanceFromCenterOfStage = (
                    SLOT_XDistanceFromCenterOfStage + SLOT_51)
            elif SLOT_52 > SLOT_53:
                SLOT_XDistanceFromCenterOfStage = (
                    SLOT_XDistanceFromCenterOfStage - SLOT_51)
            else:
                pass
            SLOT_XDistanceFromCenterOfStage = (
                SLOT_XDistanceFromCenterOfStage + 100000)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 120)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)
