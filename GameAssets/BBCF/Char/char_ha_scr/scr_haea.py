@State
def EMB_HA():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EMB_HA_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EMB_HA_AH():

    def upon_IMMEDIATE():
        FaceRight()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EventRCStand():

    def upon_43():
        if (SLOT_48 == 10):
            enterState('EventRCWarpOut')
    PaletteIndex(7)
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
    gotoLabel(0)

@State
def EventRCWarpIn():
    BlendMode_Normal()
    PaletteIndex(7)
    sprite('rc000_00', 7)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    AlphaValue(0)
    ConstantAlphaModifier(10)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 0)
    enterState('EventRCStand')

@State
def EventRCWarpOut():
    BlendMode_Normal()
    PaletteIndex(7)
    sprite('rc000_00', 7)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    ConstantAlphaModifier(-10)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    Visibility(1)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    sprite('rc000_08', 32767)

@State
def ha_D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
    sprite('null', 40)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    sprite('null', 21)
    E0EAEffectPosition(0)

@State
def ha_D_usui():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
    sprite('null', 10)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    AlphaValue(150)
    ConstantAlphaModifier(-5)
    sprite('null', 51)
    E0EAEffectPosition(0)

@State
def ha_D_no_link_pos():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
    sprite('null', 10)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    sprite('null', 51)
    AlphaValue(140)
    ConstantAlphaModifier(-20)
    E0EAEffectPosition(0)

@State
def ha_5D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        sendToLabelUpon(32, 0)

        def upon_33():
            E0EAEffectPosition(0)
    sprite('null', 32767)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    label(0)
    sprite('null', 10)
    AddToAlphaModifier(-20)

@State
def ha_2D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)

        def upon_32():
            E0EAEffectPosition(0)
    sprite('null', 8)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    sprite('null', 20)
    AddToAlphaModifier(-15)

@State
def ha_6D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        sendToLabelUpon(32, 0)

        def upon_33():
            E0EAEffectPosition(0)
    sprite('null', 32767)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    label(0)
    sprite('null', 7)
    AlphaValue(140)
    ConstantAlphaModifier(-20)

@State
def ha_202():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef202_00', 120)

@State
def ha_232():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef232_00', 2)
    sprite('vrhaef232_00', 2)
    ConstantAlphaModifier(-5)
    AlphaValue(160)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrhaef232_00', 14)
    AlphaValue(120)

@State
def ha_212():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef212_00', 3)
    sprite('vrhaef212_01', 2)
    ConstantAlphaModifier(-5)
    AlphaValue(160)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrhaef212_01', 14)
    AlphaValue(120)

@State
def ha_234():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef234_00', 3)
    sprite('vrhaef234_01', 16)

@State
def ha_252():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef252_00', 2)
    sprite('vrhaef252_01', 2)
    sprite('vrhaef252_02', 2)
    sprite('vrhaef252_03', 3)
    sprite('vrhaef252_04', 16)

@State
def ha_214():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef214_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrhaef214_00', 2)
    AlphaValue(160)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrhaef214_00', 16)
    AlphaValue(120)

@State
def ha_260():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(220)
    sprite('vrhaef260_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrhaef260_00', 2)
    AlphaValue(120)
    sprite('vrhaef260_00', 6)
    AlphaValue(80)
    sprite('vrhaef260_00', 6)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)

@State
def ha_406():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef406_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrhaef406_01', 2)
    AlphaValue(160)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrhaef406_01', 16)
    AlphaValue(120)

@State
def ha_power_circle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(-1000)
        AddY(256000)
    sprite('vrhaef_power_circle', 6)
    SetScaleSpeed(225)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_circle', 25)
    SetScaleSpeed(4)
    ConstantAlphaModifier(-10)

@State
def ha_power_light():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(501)
        AddY(256000)
    sprite('vrhaef_power_light', 6)
    SetScaleSpeed(250)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_light', 25)
    SetScaleSpeed(8)
    ConstantAlphaModifier(-10)

@State
def ha_power_bluelight():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(-999)
        AddY(256000)
    sprite('vrhaef_power_bluelight', 6)
    SetScaleSpeed(250)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_bluelight', 25)
    SetScaleSpeed(5)
    ConstantAlphaModifier(-10)

@State
def ha_power_1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(-1000)
        AddY(256000)
    sprite('vrhaef_power_1', 6)
    SetScaleSpeed(167)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_1', 15)
    SetScaleSpeed(4)
    ConstantAlphaModifier(0)
    sprite('vrhaef_power_1', 10)
    ConstantAlphaModifier(-26)

@State
def ha_power_2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(-1000)
        AddY(256000)
    sprite('vrhaef_power_2', 6)
    SetScaleSpeed(167)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_2', 15)
    SetScaleSpeed(4)
    ConstantAlphaModifier(0)
    sprite('vrhaef_power_2', 10)
    ConstantAlphaModifier(-26)

@State
def ha_power_3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(0)
        AlphaValue(0)
        FaceLeft()
        SetZVal(-1000)
        AddY(256000)
    sprite('vrhaef_power_3', 6)
    SetScaleSpeed(167)
    ConstantAlphaModifier(43)
    sprite('vrhaef_power_3', 15)
    SetScaleSpeed(4)
    ConstantAlphaModifier(0)
    sprite('vrhaef_power_3', 10)
    ConstantAlphaModifier(-26)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(37)
        PaletteColor3(38)
        PaletteColor4(1)
        AlphaValue(247)
    sprite('vrhaef408_00', 2)
    sprite('vrhaef408_01', 120)

@State
def ha_402a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteIndex(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef402_00', 16)
    AddX(-96000)

@State
def ha_402b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        TurnParticleColorable1(1)
        PaletteIndex(1)
        BlendMode_Add()
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef402_10', 16)
    AddX(-128000)

@State
def ha_409():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)

        def upon_32():
            E0EAEffectPosition(0)
    sprite('null', 8)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 241, 242)
    CallPrivateEffect('haef_D')
    sprite('null', 20)
    AddToAlphaModifier(-15)

@State
def ha_409_dash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 5)
    CreateParticle('haef_409dash', -1)
    gotoLabel(0)

@State
def ha_404():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        TurnParticleColorable1(1)
        PaletteIndex(1)
        BlendMode_Add()
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vrhaef404_00', 3)
    sprite('vrhaef404_01', 16)

@State
def haef410_kick():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(1)
        PaletteColor1(32)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483948)
        AddX(96000)
        AddY(32000)
    sprite('vrhaef410_00', 32)
    CreateParticle('haef_kick_splash', 0)
    ParticleSize(875)
    CallCustomizableParticle('haef_kick_drop', 1)
    CreateObject('haef410_kick_blm', -1)

@State
def haef410_kick_blm():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
    sprite('vrhaef410_01', 12)
    sprite('vrhaef410_01', 20)
    ConstantAlphaModifier(-12)

@State
def haef410_kick2():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483948)
        AddX(50000)
        AddY(44000)
    sprite('vrhaef410_10', 16)
    CreateParticle('haef_kick_splash', 0)
    ParticleSize(875)
    CallCustomizableParticle('haef_kick_drop', 1)
    CreateObject('haef410_kick2_blm', -1)

@State
def haef410_kick2_blm():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        E0EAEffectRotation(2)
        E0EAEffectScale(2)
        BlendMode_Normal()
    sprite('vrhaef410_11', 1)
    sprite('vrhaef410_11', 15)
    ConstantAlphaModifier(-17)

@State
def ha_kick():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_00', 16)
    CreateParticle('haef_kick_splash', 0)

@State
def ha_kick_b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_01', 16)
    ConstantAlphaModifier(-16)

@State
def ha_kick2():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(20)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_10', 18)

@State
def ha_kick2b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_11', 20)
    ConstantAlphaModifier(-13)

@State
def ha_kick3():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        PaletteIndex(1)
        BlendMode_Normal()
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_20', 16)

@State
def ha_kick3b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_21', 16)
    ConstantAlphaModifier(-16)

@State
def ha_kick4():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_30', 16)
    CreateParticle('haef_kick_splash', 0)

@State
def ha_kick4b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(50000)
        AddY(50000)
    sprite('vrhaef401_31', 16)
    ConstantAlphaModifier(-16)

@State
def ha_FastEnma():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        Size(1050)
        BlendMode_Normal()
    sprite('vrhaef403_00', 3)
    CreateObject('ha_FastEnmab', -1)
    sprite('vrhaef403_10', 5)
    CreateParticle('haef_kick_drop', 1)
    CreateParticle('haef_kick_drop', 2)
    sprite('vrhaef403_10', 5)
    ConstantAlphaModifier(-26)

@State
def ha_FastEnmab():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        Size(1050)
    sprite('vrhaef403_01', 3)
    sprite('vrhaef403_11', 10)
    ConstantAlphaModifier(-26)

@State
def ha_air_kick():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddY(150000)
    sprite('vrhaef405_00', 16)
    CreateParticle('haef_kick_splash', 0)

@State
def ha_air_kick_b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddY(150000)
    sprite('vrhaef405_01', 16)
    ConstantAlphaModifier(-16)

@State
def ha_407():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(950)
        AttackP1(70)
        AttackP2(92)
        SameMoveProration(-1)
        Hitstop(9)
        EnemyHitstopAddition(3, 3, 8)
        AirPushbackX(0)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(36)
        CHAirPushbackY(-50000)
        CHGroundBounce(1)
        CHBouncePercentage(50)
        AutoHitStopSending(1)
        HardKnockdown(1)
        CHHardKnockdown(-1)
        EnableEmergencyTechAirHit(1)
        if SLOT_110:
            HeatCooldown(0)
        SameMoveProration(1)
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(-50000)
        AddY(-100000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrhaef407_00', 4)
    CreateParticle('haef_kick_splash', 1)
    CreateParticle('haef_kick_splash', 0)
    sprite('vrhaef407_00', 12)
    StartMultihit()

@State
def ha_407_b():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(-50000)
        AddY(-100000)
    sprite('vrhaef407_01', 16)
    ConstantAlphaModifier(-16)

@State
def ha_407_hasei():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AttackP2(92)
        SameMoveProration(-1)
        Hitstop(7)
        EnemyHitstopAddition(5, 5, 8)
        AirPushbackX(0)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        GroundBounce(1)
        BouncePercentage(55)
        FatalCounter(1)
        AutoHitStopSending(1)
        if SLOT_110:
            HeatCooldown(0)
        if SLOT_80:
            AirUntechableTime(60)
            GroundBounce(1)
            BouncePercentage(55)

            def upon_OPPONENT_HIT():
                SLOT_4 = (SLOT_4 + 1)
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(246)
        PaletteColor3(246)
        PaletteColor4(2147483898)
        AddX(-50000)
        AddY(-100000)
    sprite('vrhaef407_00', 4)
    CreateParticle('haef_kick_splash', 1)
    CreateParticle('haef_kick_splash', 0)
    sprite('vrhaef407_00', 12)
    StartMultihit()

@State
def ha_407_b_hasei():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(-50000)
        AddY(-100000)
    sprite('vrhaef407_01', 16)
    ConstantAlphaModifier(-16)

@State
def ShotDelete():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(900)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)
        AttackP1(85)
        LinkParticle('haef_shotkiller')
        SetActionMark(90)

        def upon_FRAME_STEP():
            AddActionMark(-1)
            if (SLOT_2 < 0):
                Unknown23090(23)

        def upon_GUARDPOINT_ACTIVATION():
            SetActionMark(90)

        def upon_OPPONENT_HIT_OR_BLOCK():
            Unknown23090(23)

        def upon_53():
            CollidableInvincibility(0)
            Unknown23090(23)

        def upon_39():
            Unknown23090(23)
        HitsPerCall(1, 1, 1, 1, 0, 0, 0, 0)

        def upon_54():
            sendToLabel(1)
        GuardPoint_(1)
        StrikeProjectilesBypass(0)
        PretendNoGuardPointIfFail(1)
        Unknown23142(1)
        PassByArmor(1)
        SameMoveProration(1)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    Size(700)
    SetScaleSpeed(50)
    CreateObject('ShotDeleteMoji', -1)
    CreateObject('ShotDeleteMagicCircle', -1)
    CreateObject('ShotDeleteColorCircle', -1)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    SetScaleSpeed(0)
    RefreshMultihit()
    loopRest()
    label(0)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 30)
    RefreshMultihit()
    PrivateSE('hase_25')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    SetScaleSpeed(-100)
    CallCustomizableParticle('haef_shotkiller_del', -1)

@State
def ShotDeleteMoji():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('haef_shotkiller_m')
        FaceLeft()
    sprite('null', 32767)
    AddRotationPerFrame(1000)

@State
def ShotDeleteMagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        ParticleColorFromPalette(208, 208, 208)
        CallPrivateEffect('haef_shotkiller_mc')
    sprite('null', 32767)
    AddRotationPerFrame(500)

@State
def ShotDeleteColorCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        ColorFromPaletteIndex(239)
    sprite('vrhaef_shotkiller', 32767)
    AddRotationPerFrame(1000)

@State
def ha_DD_1_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('null', 1)
    ParticleFacing(0)
    CallCustomizableParticle('haef_DD_1', 0)

@State
def ha_DD_1_shot():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        UseSlashHitspark(1)
        AttackLevel_(4)
        ProjectileLevel(3)
        HeatGainMultiplier(0)
        Damage(2500)
        AttackP2(80)
        AirPushbackX(20000)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        StarterRating(2)
        PaletteIndex(1)

        def upon_32():
            NoAttackDuringAction(1)
            clearUponHandler(32)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 4)
    physicsXImpulse(64000)
    CreateObject('ha_DD_1_shot_a', -1)
    CreateObject('ha_DD_1_shot_b', -1)
    sprite('vrhaef430_dummy', 90)

@State
def ha_DD_1_shot_a():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Hitstop(0)
    label(0)
    sprite('null', 1)
    CreateParticle('haef_DD_1_shot', -1)
    loopRest()
    gotoLabel(0)

@State
def ha_DD_1_shot_b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Hitstop(0)
    label(0)
    sprite('null', 4)
    CreateParticle('haef_DD_1_shot_b', -1)
    loopRest()
    gotoLabel(0)

@State
def ha_DD_1_shotSP():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        AttackLevel_(5)
        ProjectileLevel(3)
        HeatGainMultiplier(0)
        Damage(3000)
        AttackP2(80)
        AirUntechableTime(50)
        Hitstop(0)
        EnemyHitstopAddition(13, 13, 13)
        AirPushbackX(80000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Stagger(60)
        Crumple(50)
        UseSlashHitspark(1)
        StarterRating(2)
        CollideWithWall(1)
        PaletteIndex(2)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(10)
        AfterimageSize_1(1000)
        AfterimageSize_2(500)
        BlendMode_Add()

        def upon_32():
            NoAttackDuringAction(1)
            clearUponHandler(32)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 4)
    CancelIfPlayerHit(0)
    physicsXImpulse(64000)
    SetAcceleration(800)
    ContinueState(120)
    label(0)
    sprite('vrjnef430_00', 2)
    AlphaValue(255)
    PrivateSE('jnse_01')
    sprite('vrjnef430_01', 2)
    PrivateSE('jnse_01')
    loopRest()
    gotoLabel(0)

@State
def ha_DD_2_ex():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
    sprite('null', 16)
    CallPrivateEffect('haef_DD_2_ex')
    sprite('null', 1)
    CreateObject('ha_DD_2_ex_usui', -1)
    sprite('null', 60)

@State
def ha_DD_2_ex_usui():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
    sprite('null', 70)
    CallPrivateEffect('haef_DD_2_ex')
    AlphaValue(150)
    ConstantAlphaModifier(-5)

@State
def ha_AH():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    sprite('null', 1)
    CreateParticle('haef_AH', -1)

@State
def ha_AH_fude():

    def upon_IMMEDIATE():
        ContinueState(220)
        E0EAEffectPosition(3)
    sprite('null', 60)
    CreateObject('ha_451_fude00', -1)
    sprite('null', 16)
    CreateObject('ha_451_fude01', -1)
    sprite('null', 16)
    CreateObject('ha_451_fude02', -1)
    sprite('null', 14)
    CreateObject('ha_451_fude03', -1)
    sprite('null', 14)
    CreateObject('ha_451_fude04', -1)
    sprite('null', 12)
    CreateObject('ha_451_fude05', -1)
    sprite('null', 12)
    CreateObject('ha_451_fude06', -1)
    sprite('null', 10)
    CreateObject('ha_451_fude07', -1)
    sprite('null', 10)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 8)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 8)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 6)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 6)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 4)
    CreateObject('ha_451_fude01', -1)
    sprite('null', 4)
    CreateObject('ha_451_fude08', -1)
    sprite('null', 4)
    CreateObject('ha_451_black00', -1)
    sprite('null', 4)
    CreateObject('ha_451_black01', -1)
    sprite('null', 4)
    CreateObject('ha_451_black02', -1)
    sprite('null', 8)
    CreateObject('ha_451_black03', -1)

@State
def haef_AH_RedBG():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        LinkParticle('haef_AH_slash')
    sprite('null', 450)

@State
def ha_451_fude00():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        AlphaValue(128)
        ConstantAlphaModifier(9)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-180000)
        AbsoluteY(224000)
        SetScaleX(1000)
        SetScaleY(1500)
        SetScaleXPerFrame(1)
        SetScaleSpeedY(2)
        RotationAngle(-14000)
        physicsXImpulse(-100)
        physicsYImpulse(-100)
    sprite('vrhaef451_fude', 32767)
    CreateParticle('haef_AH_2_hit', 1)
    CreateParticle('haef_AH_2_drop', 0)
    CreateObject('haef_AH_RedBG', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_2')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_fude01():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(320000)
        AbsoluteY(320000)
        RotationAngle(60000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude02():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-16000)
        AbsoluteY(288000)
        RotationAngle(150000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude03():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-256000)
        AbsoluteY(288000)
        RotationAngle(285000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude04():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(192000)
        AbsoluteY(288000)
        RotationAngle(30000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude05():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-32000)
        AbsoluteY(480000)
        RotationAngle(165000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude06():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(128000)
        AbsoluteY(224000)
        RotationAngle(20000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude07():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-512000)
        AbsoluteY(448000)
        RotationAngle(275000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_fude08():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        DeviationX(-128000, 128000)
        DeviationY(-128000, 512000)
        RandAddRotation(0, 364000)
        SetScaleXPerFrame(5)
        SetScaleSpeedY(2)
        LinkParticle('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    CreateParticle('haef_AH_2_hit_pos', 0)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    ConstantAlphaModifier(-2)

@State
def ha_451_black00():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(360000)
        AbsoluteY(288000)
        SetScaleX(4000)
        SetScaleY(320000)
        RotationAngle(10000)
        AlphaValue(64)
    sprite('vrhaef451_black', 32767)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black01():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(480000)
        AbsoluteY(288000)
        SetScaleX(5000)
        SetScaleY(320000)
        RotationAngle(-15000)
        AlphaValue(64)
    sprite('vrhaef451_black', 32767)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black02():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddX(-576000)
        AbsoluteY(288000)
        SetScaleX(10000)
        SetScaleY(320000)
        RotationAngle(-10000)
        AlphaValue(64)
    sprite('vrhaef451_black', 32767)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black03():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AbsoluteY(288000)
        SetScaleX(320000)
        SetScaleY(320000)
        RotationAngle(-10000)
        AlphaValue(255)
    sprite('vrhaef451_black', 32767)
    CommonSE('020_blood_1')
    CommonSE('015_blaze_1')
    CommonSE('101_hit_slash_3')

@State
def ha_451_finish():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        Damage(38000)
        MinimumDamage(100)
        AddCombo(18)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(70)
        Crumple(67)
        UseSlashHitspark(1)
        HitsparkSize(2000)
        HitAnywhere(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        E0EAEffectPosition(3)
        PaletteIndex(1)
        sendToLabelUpon(12, 0)

        def upon_ON_HIT_OR_BLOCK():
            CreateParticle('haef_AH_2_hit', 101)
    sprite('vrhaef451_dummy', 3)
    AbsoluteY(288000)
    Hitstop(25)
    CreateParticle('haef_AH_2_finish03', -1)
    CommonSE('025_cleanhit_slash')
    CommonSE('101_hit_slash_3')
    loopRest()
    label(0)
    sprite('null', 1)

@State
def HaAstBG_Start():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        AbsoluteY(200000)
        CreateParticle('haef_AH_ground', -1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        SetZVal(500)
        BlendMode_Add()
        AlphaValue(0)
        ConstantAlphaModifier(50)
        SetScaleX(10000)
        SetScaleY(2200)
    sprite('vr_white', 32767)

@State
def HaAstBG_Finish():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        AbsoluteY(200000)
        CreateParticle('haef_AH_ground00', -1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        SetZVal(500)
        BlendMode_Add()
        AlphaValue(0)
        ConstantAlphaModifier(4)
        SetScaleX(10000)
        SetScaleY(2200)
    sprite('vr_white', 32767)

@State
def EventEffectHAVsRG_TB():
    XPositionRelativeFacing(-460000)
    sendToLabelUpon(32, 1)
    PaletteIndex(6)
    label(0)
    sprite('tb070_03', 1)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('tb070_03', 6)
    sprite('tb070_02', 5)
    sprite('tb070_01', 4)
    sprite('tb070_00', 4)
    sprite('tb033_00', 2)
    sprite('tb033_01', 2)
    physicsXImpulse(-25000)
    physicsYImpulse(11000)
    setGravity(1550)
    CommonSE('205_runjump_garden_1')
    sprite('tb033_02', 2)
    sprite('tb033_02', 1)
    sprite('tb033_03', 3)
    loopRest()
    sendToLabelUpon(2, 3)
    label(2)
    sprite('tb033_02', 3)
    sprite('tb033_03', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('tb033_04', 2)
    EndMomentum(1)
    sprite('tb033_05', 2)
    sprite('null', 32767)
    loopRest()

@State
def NOISE():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_eventnoise.DIG', '')
        FaceSpawnLocation()
        RenderLayer(4)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 80)
    loopRest()

@State
def SummonTrinity():

    def upon_IMMEDIATE():
        PaletteIndex(5)
        AlphaValue(0)
        BlendMode_Normal()
        AddY(50000)
        AddX(40000)
    sprite('pt999_00', 75)
    ConstantAlphaModifier(3)
    sprite('pt999_00', 10)
    ConstantAlphaModifier(0)
    CharacterFlash(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)

@Subroutine
def ShotDelete_dmy():
    CancelIfPlayerHit(2)
    RemoveOnCallStateEnd(2)
    E0EAEffectPosition(2)
    IgnorePauses(2)
    GuardPoint_(1)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardpointHitstop(0, 0)
    PretendNoGuardPointIfFail(1)
    SetActionMark(1)

    def upon_FRAME_STEP():
        if (not SLOT_30):

            def upon_GUARDPOINT_ACTIVATION():
                if SLOT_2:
                    ObjectUpon(3, 32)
                    HeatChange(1250)
                    AddActionMark(-1)
                    PassbackAddActionMarkToFunction('ShotDelete', 39)
                    CreateObject('ShotDelete', 102)
                    PrivateSE('hase_23')

@State
def ha202_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha202_col_dmy_00', 1)
    sprite('ha202_col_dmy_01', 2)

@State
def ha212_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha212_col_dmy_00', 2)
    sprite('ha212_col_dmy_01', 3)

@State
def ha232_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha232_col_dmy_00', 3)
    sprite('ha232_col_dmy_03', 3)
    sprite('ha232_col_dmy_04', 3)

@State
def ha234_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha234_col_dmy_00', 1)
    sprite('ha234_col_dmy_01', 3)
    sprite('ha234_col_dmy_02', 4)

@State
def ha214_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha214_col_dmy_00', 1)
    sprite('ha214_col_dmy_01', 1)
    sprite('ha214_col_dmy_02', 1)

@State
def ha252_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha252_col_dmy_00', 2)
    sprite('ha252_col_dmy_01', 3)
    sprite('ha252_col_dmy_02', 1)

@State
def ha260_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha260_col_dmy_00', 6)
    sprite('ha260_col_dmy_01', 4)
    sprite('ha260_col_dmy_02', 4)
    sprite('ha260_col_dmy_03', 4)

@State
def ha406_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha406_col_dmy_00', 2)
    sprite('ha406_col_dmy_01', 2)
    sprite('ha406_col_dmy_02', 6)

@State
def ha402_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha402_col_dmy_00', 3)
    sprite('null', 14)
    sprite('ha402_col_dmy_01', 3)

@State
def ha404_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha404_col_dmy_00', 3)

@State
def ha430_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha430_col_dmy_00', 4)

@State
def ha430_col_dmy_OD():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha430_col_dmy_00', 4)

@State
def BurstDD_Camera_Super():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        AbsoluteY(0)
    sprite('null', 10)

@State
def BurstDD_Camera_Normal():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
    sprite('null', 300)

@State
def Act3Event_havsno_01():
    sprite('null', 32767)
    XPositionRelativeFacing(360000)
    CameraControlEnable(1)

@State
def Act3Event_ObjCol():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 50)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('null', 1)
    SLOT_52 = (SLOT_52 + 1)
    CopyFromRightToLeft(2, 2, 52, 23, 2, 52)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def Act3Event_ha_DD_1_shot():

    def upon_IMMEDIATE():
        PaletteIndex(1)
    sprite('null', 30)
    physicsXImpulse(64000)
    CreateObject('ha_DD_1_shot_a', -1)
    CreateObject('ha_DD_1_shot_b', -1)