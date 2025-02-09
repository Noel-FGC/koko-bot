@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_ma.DIG', '')
        RenderLayer(5)
        AddY(280000)
        Size(1500)
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
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_ma.DIG', '')
        RenderLayer(5)
        AddY(280000)
        Size(1500)
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
def EMB_MA_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_ma.DIG', '')
        RenderLayer(5)
        AddY(280000)
        Size(1500)
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

@State
def DIST_RG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(5000)
        RandRotationAngle()
        AlphaValue(255)
        ParticleTransparency(1)
        PlayerTransparency(16000)
        Unknown3059(-40)
        SetScaleSpeed(50)
        ConstantAlphaModifier(-4)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)
    sprite('vrdist00', 3)
    DeviationX(-10000, 10000)
    DeviationY(-10000, 10000)
    RandAddScale(-500, 500)

@State
def rgef_drains():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('rgef_draina', -1)

@State
def rgef_drain():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('rgef_drainb', -1)

@State
def ThrowMazzle():
    sprite('null', 120)
    CreateParticle('rgef_muzzle00', -1)
    CreateParticle('rgef_muzzle00', -1)

@State
def rgef431_Start():
    sprite('null', 120)
    ParticleColor(4278190080, 4278190080, 16711680)
    CallCustomizableParticle('rgef_bloodkineR', -1)
    ParticleColor(4278190080, 4278190080, 16711680)
    CallCustomizableParticle('rgef_bloodkineL', -1)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('rgef_bloodkineR2', -1)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('rgef_bloodkineL2', -1)
    CallCustomizableParticle('rgef_bkburst', -1)
    ParticleLayer(2)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('rgef_bloodkineback', -1)

@State
def rgef203atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(500)
        Size(900)
        AddX(50000)
        AlphaValue(212)
    sprite('vrrgef203atk_00', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    sprite('vrrgef203atk_01', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef203atk_02', 5)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_03', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_04', 1)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    SetZVal(-500)
    sprite('vrrgef203atk_05', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_06', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef203atk_07', 4)
    AlphaValue(212)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_08', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_09', 3)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    sprite('vrrgef203atk_10', 3)
    CreateParticle('rgef02', 0)

@State
def rgef203atkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1100)
        Size(1100)
        AlphaValue(212)
    sprite('vrrgef203atk_00', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    sprite('vrrgef203atk_01', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef203atk_02', 5)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_03', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_04', 1)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    SetZVal(-500)
    sprite('vrrgef203atk_05', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_06', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef203atk_07', 4)
    AlphaValue(212)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_08', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_09', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    sprite('vrrgef203atk_10', 3)
    CreateParticle('rgef02', 0)

@State
def rgef213atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        AlphaValue(255)
    sprite('vrrgef213atk_00', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    sprite('vrrgef213atk_01', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    sprite('vrrgef213atk_02', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef213atk_03', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    sprite('vrrgef213atk_04', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef213atk_05', 2)
    CreateParticle('rgef03', 0)
    ConstantAlphaModifier(-10)

@State
def rgef213atkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1100)
        Size(1200)
        AlphaValue(212)
    sprite('vrrgef213atk_00', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    sprite('vrrgef213atk_01', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    sprite('vrrgef213atk_02', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    sprite('vrrgef213atk_03', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    sprite('vrrgef213atk_04', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    sprite('vrrgef213atk_05', 2)
    CreateParticle('rgef03', 0)
    ConstantAlphaModifier(-10)

@State
def rgef233atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
        AlphaValue(212)
    sprite('vrrgef233atk_00', 3)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef233atk_01', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef233atk_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef233atk_03', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef233atk_04', 2)
    E0EAEffectPosition(0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef233atk_05', 5)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateParticle('rgef03', 5)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateObject('rgef_drains', 5)
    sprite('vrrgef233atk_06', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    sprite('vrrgef233atk_07', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef233atk_08', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef233atk_09', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    ConstantAlphaModifier(-10)

@State
def rgef233atkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
        AlphaValue(212)
        Size(1200)
    sprite('vrrgef233atk_00', 3)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 0)
    AddY(-100000)
    sprite('vrrgef233atk_01', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef233atk_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef233atk_03', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef233atk_04', 2)
    E0EAEffectPosition(0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef233atk_05', 5)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateParticle('rgef03', 5)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    AddY(100000)
    sprite('vrrgef233atk_06', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 4)
    sprite('vrrgef233atk_07', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef233atk_08', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef233atk_09', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    ConstantAlphaModifier(-10)

@State
def rgef253atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AlphaValue(212)
    sprite('vrrgef253atk_00', 3)
    sprite('vrrgef253atk_01', 3)
    sprite('vrrgef253atk_02', 2)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef253atk_03', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 3)
    sprite('vrrgef253atk_04', 2)
    ConstantAlphaModifier(-10)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    sprite('vrrgef253atk_05', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)

@State
def rgef253atkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AlphaValue(212)
    sprite('vrrgef253atk_00', 3)
    sprite('vrrgef253atk_01', 3)
    sprite('vrrgef253atk_02ex01', 2)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 4)
    sprite('vrrgef253atk_03ex01', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 3)
    sprite('vrrgef253atk_04', 2)
    ConstantAlphaModifier(-10)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    sprite('vrrgef253atk_05', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)

@State
def rgef400loop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(900)
        AlphaValue(255)
        SetScaleY(1100)
        AddY(-60000)
    sprite('vrrgef400atk_02', 3)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    sprite('vrrgef400atk_03', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    label(0)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1000)
    ConstantAlphaModifier(-10)
    AddX(200000)
    AddY(-5000)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1100)
    AddY(5000)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1200)
    AddY(-10000)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1100)
    AddY(-5000)
    ConstantAlphaModifier(10)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1200)
    AddY(2000)
    sprite('vrrgef400atk_04', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    Size(1100)
    AddY(-3000)
    loopRest()
    gotoLabel(0)
    sprite('null', 20)

@State
def rgef400end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AlphaValue(255)
        SetScaleY(1100)
        AddY(-70000)
        AddX(120000)
    sprite('vrrgef400atk_05', 2)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    ConstantAlphaModifier(-10)
    sprite('vrrgef400atk_06', 4)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    E0EAEffectPosition(0)
    sprite('vrrgef400atk_07', 4)
    CreateParticle('rgef00', 0)
    CreateParticle('rgef00', 1)
    CreateParticle('rgef00', 2)
    sprite('vrrgef400atk_08', 4)
    sprite('null', 20)

@State
def rgef400nokori():

    def upon_IMMEDIATE():
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AlphaValue(255)
    sprite('vrrgef400b_00', 5)
    ConstantAlphaModifier(-2)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    sprite('vrrgef400b_01', 2)
    sprite('vrrgef400b_02', 3)
    sprite('vrrgef400b_03', 3)
    sprite('vrrgef400b_04', 3)
    sprite('vrrgef400b_05', 3)
    sprite('vrrgef400b_06', 3)
    sprite('vrrgef400b_07', 3)
    sprite('vrrgef400b_08', 3)
    sprite('vrrgef400b_09', 3)
    sprite('null', 9)
    ConstantAlphaModifier(-6)

@State
def rgef401atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(-500)
        BlendMode_Normal()
        AlphaValue(224)
    sprite('vrrgef401atk_00', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef401atk_01', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateObject('rgef_drains', 5)
    CreateObject('rgef_drains', 6)
    sprite('vrrgef401atk_02', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef401atk_03', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateObject('rgef_drains', 5)
    CreateObject('rgef_drains', 6)
    CreateObject('rgef_drains', 7)
    CreateObject('rgef_drains', 8)
    sprite('vrrgef401atk_04', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef401atk_05', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef401atk_06', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef401atk_07', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef401atk_08', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)

@State
def rgef402atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(-500)
        AlphaValue(240)
    sprite('vrrgef402atk_00', 1)
    sprite('vrrgef402atk_01', 1)
    sprite('vrrgef402atk_02', 1)
    sprite('vrrgef402atk_03', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef402atk_04', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef402atk_05', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef402atk_06', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef402atk_07', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef402atk_08', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)

@State
def rgef406atk():

    def upon_IMMEDIATE():
        AlphaValue(255)
        ConstantAlphaModifier(-20)
    sprite('vrrgef406atk_00', 3)
    CreateParticle('rgef02', 1)
    sprite('vrrgef406atk_01', 3)
    CreateParticle('rgef02', 2)
    sprite('vrrgef406atk_02', 3)
    CreateParticle('rgef02', 1)
    sprite('vrrgef406atk_03', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef406atk_00', 3)
    CreateParticle('rgef02', 1)
    sprite('vrrgef406atk_01', 3)
    CreateParticle('rgef02', 2)
    sprite('vrrgef406atk_02', 3)
    sprite('vrrgef406atk_03', 3)

@State
def rgef406batk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(-500)
        AddY(300000)
        AddX(120000)
        BlendMode_Normal()
        AlphaValue(224)
    sprite('vrrgef406batk_00', 4)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef406batk_01', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef406batk_02', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateParticle('rgef03', 5)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    CreateObject('rgef_drains', 5)
    sprite('vrrgef406batk_03', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef406batk_04', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    sprite('vrrgef406batk_05', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    ConstantAlphaModifier(-20)

@State
def rgef406batkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1100)
        AddY(300000)
        AddX(120000)
        BlendMode_Normal()
        AlphaValue(224)
    sprite('vrrgef406batk_00', 4)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 0)
    sprite('vrrgef406batk_01', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef406batk_02', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    sprite('vrrgef406batk_03', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    sprite('vrrgef406batk_04', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    sprite('vrrgef406batk_05', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 0)
    ConstantAlphaModifier(-20)

@State
def rgef408nokori():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-500)
        AfterimageBlendMode(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AddX(-128000)
        AlphaValue(255)
    sprite('vrrgef408b_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrrgef408b_01', 2)
    sprite('vrrgef408b_02', 2)
    sprite('vrrgef408b_03', 2)
    sprite('vrrgef408b_04', 2)
    sprite('vrrgef408b_05', 2)
    sprite('vrrgef408b_06', 2)

@State
def rgef408Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AttackP1(90)
        Damage(1000)
        PushbackX(39900)
        AirUntechableTime(36)
        MoveAttributes(0, 0, 0, 1, 0)
        AirPushbackX(30000)
        AirPushbackY(30000)
        SameMoveProration(60)
        AirHitstunAnimation(13)
        Lifesteal(100, 100)
        ChipPercentage(0)
        GuardCrush(1, 1)
        PaletteIndex(1)
        SetZVal(-500)
        BlendMode_Normal()
        AddX(250000)
        Size(1000)

        def upon_44():
            AttackOff()

        def upon_ON_HIT_OR_BLOCK():
            AttackOff()
            NoAttackDuringAction(1)
            sendToLabel(0)
    Visibility(1)
    CreateObject('408_dog', -1)
    sprite('vrrgef408_shot00', 1)
    sprite('vrrgef408_shot01', 1)
    AttackOff()
    physicsXImpulse(4000)
    Size(600)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(120)
    Size(700)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(140)
    Size(900)
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    XImpulseAcceleration(160)
    Size(1000)
    sprite('vrrgef408_shot01', 2)
    XImpulseAcceleration(180)
    sprite('vrrgef408_shot01', 4)
    XImpulseAcceleration(200)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(60)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(60)
    label(0)
    clearUponHandler(10)
    sprite('vrrgef408_shot02', 2)
    XImpulseAcceleration(60)
    sprite('vrrgef408_shot02', 2)
    XImpulseAcceleration(60)
    sprite('vrrgef408_shot03', 4)
    AttackOff()
    physicsXImpulse(0)
    sprite('vrrgef408_shot04', 3)
    sprite('vrrgef408_shot05', 3)
    sprite('vrrgef408_shot06', 3)
    ConstantAlphaModifier(-20)
    sprite('vrrgef408_shot07', 3)
    sprite('vrrgef408_shot06', 3)
    Visibility(1)
    sprite('vrrgef408_shot07', 3)

@State
def rgef408ShotD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Hitstop(6)
        AttackLevel_(4)
        AttackP1(90)
        Damage(600)
        PushbackX(23000)
        AirUntechableTime(36)
        MoveAttributes(0, 0, 0, 1, 0)
        AirPushbackX(30000)
        AirPushbackY(30000)
        SameMoveProration(60)
        SingleProration(1)
        AirHitstunAnimation(13)
        Lifesteal(100, 100)
        ChipPercentage(0)
        GuardCrush(1, 1)
        PaletteIndex(1)
        SetZVal(-500)
        BlendMode_Normal()
        AddX(250000)
        Size(1000)

        def upon_44():
            AttackOff()

        def upon_ON_HIT_OR_BLOCK():
            XImpulseAcceleration(80)
            AddActionMark(1)
            if (SLOT_2 == 3):
                XImpulseAcceleration(50)
                AttackOff()
                NoAttackDuringAction(1)
    Visibility(1)
    CreateObject('408_dog', -1)
    ApplyFunctionsToObjects(1)
    AddScale(175)
    ApplyFunctionsToSelf()
    sprite('vrrgef408_shot00', 1)
    sprite('vrrgef408_shot01', 1)
    AttackOff()
    physicsXImpulse(4000)
    Size(600)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(120)
    Size(800)
    sprite('vrrgef408_shot01', 1)
    XImpulseAcceleration(140)
    Size(1000)
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    XImpulseAcceleration(160)
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    XImpulseAcceleration(180)
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    XImpulseAcceleration(200)
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    sprite('vrrgef408_shot01', 2)
    RefreshMultihit()
    sprite('vrrgef408_shot01', 2)
    sprite('vrrgef408_shot02', 2)
    RefreshMultihit()
    sprite('vrrgef408_shot02', 2)
    RefreshMultihit()
    XImpulseAcceleration(60)
    sprite('vrrgef408_shot03', 4)
    AttackOff()
    physicsXImpulse(0)
    sprite('vrrgef408_shot04', 3)
    sprite('vrrgef408_shot05', 3)
    sprite('vrrgef408_shot06', 3)
    ConstantAlphaModifier(-20)
    sprite('vrrgef408_shot07', 3)
    sprite('vrrgef408_shot06', 3)
    Visibility(1)
    sprite('vrrgef408_shot07', 3)

@State
def __408_dog():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AttackP2(82)
        SameMoveProration(60)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(33)
        AirPushbackX(28000)
        AirPushbackY(28000)
        PushbackX(39900)
        Lifesteal(100, 100)
        ChipPercentage(0)
        StarterRating(2)

        def upon_44():
            AttackOff()

        def upon_ON_HIT_OR_BLOCK():
            AttackOff()
            NoAttackDuringAction(1)
            sendToLabel(0)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(800)
        AddY(8000)
        AddX(250000)
        SetZVal(-500)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrgef408_00', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef408_01', 1)
    physicsXImpulse(6000)
    AddScale(-500)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef408_01', 1)
    AddScale(200)
    XImpulseAcceleration(150)
    sprite('vrrgef408_01', 1)
    AddScale(200)
    XImpulseAcceleration(150)
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    XImpulseAcceleration(200)
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    AddScale(100)
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef408_02', 1)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    XImpulseAcceleration(90)
    sprite('vrrgef408_02', 1)
    XImpulseAcceleration(90)
    sprite('vrrgef408_02', 1)
    XImpulseAcceleration(90)
    label(0)
    clearUponHandler(10)
    sprite('vrrgef408_03', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    XImpulseAcceleration(80)
    sprite('vrrgef408_03', 2)
    XImpulseAcceleration(80)
    sprite('vrrgef408_04', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef408_04', 2)
    XImpulseAcceleration(50)
    sprite('vrrgef408_05', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    XImpulseAcceleration(50)
    sprite('vrrgef408_06', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    physicsXImpulse(0)
    sprite('vrrgef408_07', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef408_08', 4)

@State
def __408_dogD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        SameMoveProration(60)
        AirHitstunAnimation(13)
        AirUntechableTime(36)
        AirPushbackX(30000)
        AirPushbackY(30000)
        PushbackX(23000)
        Hitstop(6)
        Lifesteal(50, 100)
        ChipPercentage(0)
        StarterRating(2)

        def upon_44():
            AttackOff()

        def upon_OPPONENT_HIT():
            if SLOT_51:
                clearUponHandler(12)
                Damage(300)
            SLOT_51 = 1

        def upon_ON_HIT_OR_BLOCK():
            XImpulseAcceleration(80)
            AddActionMark(1)
            if (SLOT_2 == 3):
                XImpulseAcceleration(50)
                AttackOff()
                NoAttackDuringAction(1)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(800)
        AddY(8000)
        AddX(250000)
        SetZVal(-500)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrrgef408_00', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef408_01', 1)
    physicsXImpulse(8000)
    AddScale(-500)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef408_01', 1)
    AddScale(200)
    XImpulseAcceleration(150)
    sprite('vrrgef408_01', 1)
    AddScale(200)
    XImpulseAcceleration(150)
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    XImpulseAcceleration(200)
    RefreshMultihit()
    WallCollisionDetection(1)
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    AddScale(100)
    RefreshMultihit()
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    AddScale(100)
    RefreshMultihit()
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    RefreshMultihit()
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    RefreshMultihit()
    sprite('vrrgef408_02', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    RefreshMultihit()
    sprite('vrrgef408_02', 1)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    XImpulseAcceleration(90)
    sprite('vrrgef408_02', 1)
    XImpulseAcceleration(90)
    sprite('vrrgef408_02', 1)
    XImpulseAcceleration(90)
    label(0)
    clearUponHandler(10)
    sprite('vrrgef408_03', 2)
    WallCollisionDetection(0)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    XImpulseAcceleration(80)
    sprite('vrrgef408_03', 2)
    XImpulseAcceleration(80)
    sprite('vrrgef408_04', 2)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    sprite('vrrgef408_04', 2)
    XImpulseAcceleration(50)
    sprite('vrrgef408_05', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    XImpulseAcceleration(50)
    sprite('vrrgef408_06', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    physicsXImpulse(0)
    sprite('vrrgef408_07', 4)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    sprite('vrrgef408_08', 4)

@State
def rgef412effpos():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('vrrgef412effpos_00', 3)
    CreateParticle('rgef03', 0)
    CreateParticle('rgef03', 1)
    CreateParticle('rgef03', 2)
    CreateParticle('rgef03', 3)
    CreateParticle('rgef03', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateObject('rgef_drains', 3)
    CreateObject('rgef_drains', 4)
    sprite('vrrgef412effpos_00', 3)
    CreateParticle('rgef03', 5)
    CreateParticle('rgef03', 6)
    CreateParticle('rgef03', 7)
    CreateParticle('rgef03', 8)
    CreateParticle('rgef03', 9)
    CreateObject('rgef_drains', 5)
    CreateObject('rgef_drains', 6)
    CreateObject('rgef_drains', 7)
    CreateObject('rgef_drains', 8)
    CreateObject('rgef_drains', 9)
    sprite('vrrgef412effpos_00', 3)
    CreateParticle('rgef03', 10)
    CreateParticle('rgef03', 11)
    CreateParticle('rgef03', 12)
    CreateParticle('rgef03', 13)
    CreateObject('rgef_drains', 10)
    CreateObject('rgef_drains', 11)
    CreateObject('rgef_drains', 12)
    CreateObject('rgef_drains', 13)
    sprite('vrrgef412effpos_00', 3)
    CreateParticle('rgef03', 14)
    CreateParticle('rgef03', 15)
    CreateParticle('rgef03', 16)
    CreateParticle('rgef03', 17)
    CreateParticle('rgef03', 18)
    CreateParticle('rgef03', 19)
    CreateParticle('rgef03', 20)
    CreateParticle('rgef03', 21)
    CreateParticle('rgef03', 22)
    CreateParticle('rgef03', 23)
    CreateParticle('rgef03', 24)
    CreateParticle('rgef03', 25)
    CreateParticle('rgef03', 26)
    CreateObject('rgef_drains', 14)
    CreateObject('rgef_drains', 15)
    CreateObject('rgef_drains', 16)
    CreateObject('rgef_drains', 17)
    CreateObject('rgef_drains', 18)
    CreateObject('rgef_drains', 19)
    CreateObject('rgef_drains', 20)
    CreateObject('rgef_drains', 21)
    CreateObject('rgef_drains', 22)
    CreateObject('rgef_drains', 23)
    CreateObject('rgef_drains', 24)
    CreateObject('rgef_drains', 25)
    CreateObject('rgef_drains', 26)
    sprite('vrrgef412effpos_00', 3)
    CreateParticle('rgef03', 27)
    CreateParticle('rgef03', 28)
    CreateParticle('rgef03', 29)
    CreateObject('rgef_drains', 27)
    CreateObject('rgef_drains', 28)
    CreateObject('rgef_drains', 29)

@State
def rgef_414():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        AddX(-32000)
    sprite('vrrgef414_10', 3)
    sprite('vrrgef414_11', 3)
    sprite('vrrgef414_12', 3)

@State
def rgef_414_fall():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    label(0)
    sprite('vrrgef414_01', 5)
    sprite('vrrgef414_02', 5)
    gotoLabel(0)

@State
def rgef432lock():

    def upon_IMMEDIATE():
        SetZVal(-100)
        BlendMode_Normal()
        AlphaValue(224)
    sprite('vrrgef432lock_00', 4)
    sprite('vrrgef432lock_01', 4)
    sprite('vrrgef432lock_02', 4)
    sprite('vrrgef432lock_03', 4)
    sprite('vrrgef432lock_04', 4)
    sprite('vrrgef432lock_05', 4)
sprite('null', 1)

@State
def rgef432loop():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        LinkParticle('rgef432_drainhit')
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(10)
        AfterimageSize_1(1000)
        AfterimageSize_2(1200)
        BlendMode_Normal()
        AlphaValue(192)
        Size(1000)
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    ConstantAlphaModifier(-15)
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')

@State
def rgef432loop_SP():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(10)
        AfterimageSize_1(1000)
        AfterimageSize_2(1200)
        BlendMode_Normal()
        AlphaValue(192)
        Size(1500)
    sprite('null', 2)
    CreateParticle('rgef432loopptc', -1)
    CreateParticle('rgef432_drainhit', -1)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    ConstantAlphaModifier(-15)
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')
    sprite('null', 2)
    CommonSE('007_swing_knife_1')

@State
def rgef440():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        IgnorePauses(2)
        AddX(500000)
        AddScale(200)
    sprite('vrrgef440_00', 6)
    ScreenShake(20000, 20000)
    sprite('vrrgef440_01', 5)
    sprite('vrrgef440_02', 4)
    sprite('vrrgef440_03', 3)
    sprite('vrrgef440_04', 3)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)
    CreateParticle('rgef02', 1)
    CreateObject('rgef_drains', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 3)
    CreateObject('rgef_drains', 3)
    CreateParticle('rgef02', 4)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 5)
    CreateObject('rgef_drains', 5)
    CreateParticle('rgef02', 6)
    CreateObject('rgef_drains', 6)
    CreateParticle('rgef02', 7)
    CreateObject('rgef_drains', 7)
    CreateParticle('rgef02', 8)
    CreateObject('rgef_drains', 8)
    CreateParticle('rgef02', 9)
    CreateObject('rgef_drains', 9)
    sprite('vrrgef440_05', 3)

@State
def rgef440Ex():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        IgnorePauses(2)
        AddX(500000)
        AddScale(400)
    sprite('vrrgef440_00', 6)
    ScreenShake(20000, 20000)
    sprite('vrrgef440_01', 5)
    sprite('vrrgef440_02', 4)
    sprite('vrrgef440_03', 3)
    sprite('vrrgef440_04', 3)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)
    CreateParticle('rgef02', 1)
    CreateObject('rgef_drains', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 3)
    CreateObject('rgef_drains', 3)
    CreateParticle('rgef02', 4)
    CreateObject('rgef_drains', 4)
    CreateParticle('rgef02', 5)
    CreateObject('rgef_drains', 5)
    CreateParticle('rgef02', 6)
    CreateObject('rgef_drains', 6)
    CreateParticle('rgef02', 7)
    CreateObject('rgef_drains', 7)
    CreateParticle('rgef02', 8)
    CreateObject('rgef_drains', 8)
    CreateParticle('rgef02', 9)
    CreateObject('rgef_drains', 9)
    sprite('vrrgef440_05', 3)

@State
def rgef440StartEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        AlphaValue(245)
        Size(1450)
        AddY(-25000)
        AddX(75000)
        RenderLayer(6)
    sprite('vrrgef440_10', 6)
    sprite('vrrgef440_11', 5)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    sprite('vrrgef440_12', 5)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef440_13', 5)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef440_14', 4)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)
    sprite('vrrgef440_15', 4)
    CreateParticle('rgef02', 0)
    CreateObject('rgef_drains', 0)

@State
def rgef450():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        SetZVal(-500)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrrgef450atk_00', 2)
    sprite('vrrgef450atk_01', 2)
    sprite('vrrgef450atk_02', 3)
    sprite('vrrgef450atk_03', 5)
    sprite('vrrgef450atk_04', 5)
    sprite('vrrgef450atk_05', 5)
    sprite('vrrgef450atk_06', 5)
    ConstantAlphaModifier(-10)

@State
def rgef451atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(3)
        EnableAfterimage(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AddX(100000)
        Size(1500)
    sprite('vrrgef451atk_01', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef451atk_02', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    sprite('vrrgef451atk_03', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    sprite('vrrgef451atk_04', 4)
    Size(750)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateParticle('rgef02', 10)
    CreateParticle('rgef02', 11)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    CreateObject('rgef_drain', 8)
    CreateObject('rgef_drain', 9)
    CreateObject('rgef_drain', 10)
    CreateObject('rgef_drain', 11)
    sprite('vrrgef451atk_05', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    E0EAEffectPosition(0)
    sprite('vrrgef451atk_06', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    sprite('vrrgef451atk_07', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef451atk_08', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    sprite('vrrgef451atk_09', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef451atk_10', 3)
    sprite('null', 12)

@State
def rgef451atkOD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(3)
        EnableAfterimage(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AddX(100000)
        Size(1500)
    sprite('vrrgef451atk_01', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    sprite('vrrgef451atk_02', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    sprite('vrrgef451atk_03', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateObject('rgef_drain', 5)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    sprite('vrrgef451atk_04', 2)
    Size(750)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateParticle('rgef02', 10)
    CreateParticle('rgef02', 11)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    CreateObject('rgef_drain', 8)
    CreateObject('rgef_drain', 9)
    CreateObject('rgef_drain', 10)
    CreateObject('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)
    AddScale(150)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateParticle('rgef02', 10)
    CreateParticle('rgef02', 11)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    CreateObject('rgef_drain', 8)
    CreateObject('rgef_drain', 9)
    CreateObject('rgef_drain', 10)
    CreateObject('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)
    AddScale(150)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateParticle('rgef02', 10)
    CreateParticle('rgef02', 11)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    CreateObject('rgef_drain', 8)
    CreateObject('rgef_drain', 9)
    CreateObject('rgef_drain', 10)
    CreateObject('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)
    AddScale(150)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateParticle('rgef02', 10)
    CreateParticle('rgef02', 11)
    CreateObject('rgef_drain', 6)
    CreateObject('rgef_drain', 7)
    CreateObject('rgef_drain', 8)
    CreateObject('rgef_drain', 9)
    CreateObject('rgef_drain', 10)
    CreateObject('rgef_drain', 11)
    sprite('vrrgef451atk_05', 4)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    E0EAEffectPosition(0)
    sprite('vrrgef451atk_06', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    CreateParticle('rgef02', 9)
    sprite('vrrgef451atk_07', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef451atk_08', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    sprite('vrrgef451atk_09', 3)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef451atk_10', 3)
    sprite('null', 12)

@State
def rgef610wingmake():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('rgef610_02', 3)
    sprite('rgef610_03', 3)
    sprite('rgef610_04', 3)
    sprite('rgef610_05', 3)
    sprite('rgef610_06', 3)
    sprite('rgef610_06ex01', 3)

@State
def rgef610wingbreak():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(4)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('rgef610_07', 2)
    ConstantAlphaModifier(-5)
    SetScaleSpeedY(5)
    SetScaleXPerFrame(10)
    sprite('rgef610_08', 2)
    sprite('rgef610_09', 2)
    CreateParticle('rgef610', 4)
    CreateParticle('rgef610', 5)
    CreateParticle('rgef610', 6)
    CreateParticle('rgef610', 7)
    sprite('rgef610_10', 2)
    CreateParticle('rgef610', 0)
    CreateParticle('rgef610', 1)
    CreateParticle('rgef610', 2)
    CreateParticle('rgef610', 3)
    sprite('rgef610_11', 2)
    CreateParticle('rgef610', 0)
    CreateParticle('rgef610', 1)
    CreateParticle('rgef610', 2)
    CreateParticle('rgef610', 3)
    CreateParticle('rgef610', 4)
    CreateParticle('rgef610', 5)
    CreateParticle('rgef610', 6)
    CreateParticle('rgef610', 7)
    sprite('rgef610_12', 2)
    CreateParticle('rgef610', 0)
    CreateParticle('rgef610', 1)
    CreateParticle('rgef610', 2)
    CreateParticle('rgef610', 3)
    CreateParticle('rgef610', 4)
    CreateParticle('rgef610', 5)
    CreateParticle('rgef610', 6)
    CreateParticle('rgef610', 7)
    sprite('rgef610_13', 3)
    CreateParticle('rgef610', 0)
    CreateParticle('rgef610', 1)
    CreateParticle('rgef610', 2)
    CreateParticle('rgef610', 3)
    sprite('rgef610_14', 3)
    CreateParticle('rgef610', 4)
    CreateParticle('rgef610', 5)
    CreateParticle('rgef610', 6)
    CreateParticle('rgef610', 7)
    sprite('rgef610_15', 4)
    CreateParticle('rgef610', 1)
    CreateParticle('rgef610', 2)
    CreateParticle('rgef610', 3)
    CreateParticle('rgef610', 4)
    sprite('rgef610_16', 4)
    sprite('null', 30)

@State
def AstralMoveSword():

    def upon_IMMEDIATE():
        SetScaleX(-1000)
    sprite('rg460_swd00', 4)
    physicsYImpulse(-34000)
    sprite('rg460_swd01', 4)
    sprite('rg460_swd02', 4)
    physicsYImpulse(2000)

@State
def ChangeToDeathscythe():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1050)
        BlendMode_Normal()
        AlphaValue(255)
        SetScaleX(-1000)
    sprite('rg460_kama00', 1)
    PrivateSE('rgse_05')
    sprite('rg460_kama00ex01', 2)
    sprite('rg460_kama00ex02', 2)
    sprite('rg460_kama00ex03', 2)
    sprite('rg460_kama00ex04', 2)
    sprite('rg460_kama00ex05', 2)
    CommonSE('105_guard_slash_2')
    PrivateSE('rgse_21')
    sprite('rg460_kama01', 14)
    sprite('rg460_kama02', 2)
    sprite('rg460_kama03', 2)
    sprite('rg460_kama04', 2)
    sprite('rg460_kama05', 2)
    sprite('rg460_kama06', 2)
    sprite('rg460_kama07', 2)
    PrivateSE('rgse_25')
    PrivateSE('rgse_25')
    sprite('rg460_kama07ex01', 2)
    sprite('rg460_kama07ex02', 2)
    sprite('rg460_kama07', 2)
    sprite('rg460_kama07ex01', 2)
    sprite('rg460_kama07ex02', 2)
    loopRest()

@State
def nyPhantom():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Hitstop(6)
        AttackLevel_(4)
        AttackP1(80)
        Damage(700)
        PushbackX(18000)
        Blockstun(25)
        Hitstun(25)
        AirUntechableTime(27)
        PaletteIndex(2)
        SetZVal(-500)
        Flip()
        AlphaValue(0)
        BlendMode_Normal()
        AddX(-600000)
        AddY(10000)
        Size(1000)
    sprite('ny600_11', 6)
    ConstantAlphaModifier(10)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    AlphaValue(128)
    ConstantAlphaModifier(0)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    ConstantAlphaModifier(-2)
    physicsXImpulse(1000)
    sprite('ny600_12', 6)
    physicsXImpulse(400)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)
    sprite('ny600_11', 6)
    sprite('ny600_12', 6)
    sprite('ny600_13', 6)
    sprite('ny600_14', 6)

@State
def rgef203atkD3rd():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(85)
        AttackP2(82)
        MoveAttributes(0, 1, 0, 0, 0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Stagger(60)
        Crumple(42)
        PushbackX(12000)
        AirPushbackY(-60000)
        AirPushbackX(12000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(90)
        HardKnockdown(1)
        Lifesteal(100, 100)
        ChipPercentage(0)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        GuardCrushOld(800)
        GuardCrush(1, 1)
        PaletteIndex(1)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1100)
        Size(1500)
        AlphaValue(212)
        AddX(-150000)
    sprite('vrrgef203atk_00', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    sprite('vrrgef203atk_01', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef203atk_02', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_03', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_04ex', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 4)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef203atk_07', 4)
    AlphaValue(212)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_08', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_09', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    sprite('vrrgef203atk_10', 4)
    CreateParticle('rgef02', 0)

@State
def EventEffectRGVsTB_Hakumen():
    sprite('ha041_03', 32767)
    PaletteIndex(7)
    ForceFaceSprite()
    Flip()
    AddX(-520000)
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
    sprite('null', 60)
    loopRest()

@State
def rgef414atk():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)
        SetZVal(-500)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1100)
        Size(1000)
        AlphaValue(212)
        AddX(-50000)
    sprite('vrrgef203atk_00', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    sprite('vrrgef203atk_01', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 0)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    sprite('vrrgef203atk_02', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_03', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_04ex', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 2)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateObject('rgef_drain', 4)
    CreateParticle('rgef02', 6)
    CreateParticle('rgef02', 7)
    CreateParticle('rgef02', 8)
    sprite('vrrgef203atk_07', 4)
    AlphaValue(212)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateObject('rgef_drain', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    CreateParticle('rgef02', 6)
    sprite('vrrgef203atk_08', 3)
    CreateObject('rgef_drain', 0)
    CreateObject('rgef_drain', 1)
    CreateObject('rgef_drain', 2)
    CreateParticle('rgef02', 3)
    CreateParticle('rgef02', 4)
    CreateParticle('rgef02', 5)
    sprite('vrrgef203atk_09', 4)
    CreateObject('rgef_drains', 0)
    CreateObject('rgef_drains', 1)
    CreateObject('rgef_drains', 2)
    CreateParticle('rgef02', 1)
    CreateParticle('rgef02', 2)
    CreateParticle('rgef02', 3)
    sprite('vrrgef203atk_10', 4)
    CreateParticle('rgef02', 0)

@State
def DS_Niku_Head():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(1, 0, 0, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Niku_Body():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(0, 1, 0, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Niku_Leg():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(0, 0, 1, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Niku_Approach():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(0, 0, 0, 1, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Niku_Throw():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(0, 0, 0, 0, 1)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Shot_Head():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(1, 0, 0, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Shot_Body():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 1, 0, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Shot_Leg():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 0, 1, 0, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Shot_Approach():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 0, 0, 1, 0)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def DS_Shot_Throw():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(10000)
        DefeatOpponentBehavior(1)
        StrikeProjectileLevel(0)
        ProjectileLevel(1)
        MoveAttributes(0, 0, 0, 0, 1)
        PaletteIndex(1)
        TeleportToObject(22)
    sprite('vrrgef408_shot03', 60)

@State
def Eventrgef_drains():
    sprite('null', 200)
    ParticleColorFromPalette(224, 224, 224)
    CallPrivateEffect('rgef_draina')
    Size(2000)
    Visibility(1)

@State
def Eventrgef_drains2():
    sprite('null', 6)
    AddY(200000)
    ParticleSize(1500)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('rgef00', 0)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('rgef02', 0)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('rgef02', 1)
    ParticleSize(1500)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('rgef00', 2)

@State
def Eventrgef_drains3():

    def upon_IMMEDIATE():
        pass
    sprite('null', 100)
    AddY(200000)
    ParticleSize(3000)
    CallCustomizableParticle('rgef_drainstart', 0)
    ParticleColorFromPalette(215, 215, 209)
    CallCustomizableParticle('rgef432break', 0)

@State
def HAKUMEN_NOUNAI():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ScreenPosition(1)
        XPositionRelativeFacing(-640000)
        AbsoluteY(0)
        Size(20000)
        sendToLabelUpon(32, 0)
    sprite('vr_screen_black', 30)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('vr_screen_black', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(120)
    label(0)
    sprite('vr_screen_black', 30)
    ConstantAlphaModifier(-4)
    sprite('vr_screen_black', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)

@Subroutine
def Zanzou_Color():
    BlendMode_Add()
    PaletteIndex(1)
    TurnParticleColorable1(1)
    PaletteEffType(2)
    PaletteColor2(1)
    PaletteColor3(128)
    PaletteColor1(128)
    PaletteColor4(1)

@Subroutine
def maef_color():
    PaletteIndex(1)
    ParticleColorFromPalette(128, 128, 128)
    ColorFromPaletteIndex(128)

@Subroutine
def maef_color2():
    PaletteIndex(1)
    ParticleColorFromPalette(64, 64, 64)
    ColorFromPaletteIndex(64)

@Subroutine
def maef_color3():
    PaletteIndex(1)
    ParticleColorFromPalette(1, 1, 1)
    ColorFromPaletteIndex(1)

@Subroutine
def __3d_color():
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    ColorFromPaletteIndex(1)

@State
def maef_001_zanzou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrmaef001_00', 20)
    callSubroutine('Zanzou_Color')

@State
def maef_001_zanzou2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(197)
    sprite('vrmaef001_10', 4)
    sprite('vrmaef001_11', 20)
    callSubroutine('Zanzou_Color')

@State
def maef_231():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Visibility(1)
        NoDamageAction(1)
    sprite('ma231_03', 3)
    CreateObject('maef_231_3d', -1)
    sprite('keep', 3)
    sprite('keep', 3)
    sprite('keep', 3)
    sprite('keep', 3)

@State
def maef_231_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Size(1450)
        AlphaValue(200)
        BlendMode_Normal()
        AddX(60000)
        Eff3DEffect('maef_231slash', '')
    sprite('null', 15)

@State
def maef_231_3d2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Size(1450)
        BlendMode_Add()
        callSubroutine('maef_color3')
        AddX(60000)
        Eff3DEffect('maef_231slash', '')
        AlphaValue(128)
    sprite('null', 15)

@State
def maef_202():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmaef202_01', 3)
    sprite('vrmaef202_02', 3)
    sprite('vrmaef202_03', 3)
    AddX(-23000)

@State
def maef_202_2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef202_04', 4)
    AddX(-64000)
    sprite('vrmaef202_05', 12)

@State
def maef_232():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef232_04', 4)
    sprite('vrmaef232_05', 12)

@State
def maef_252():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef252_04', 4)
    ConstantAlphaModifier(-16)
    sprite('vrmaef252_05', 3)
    sprite('vrmaef252_06', 3)

@State
def maef_311():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef311_08', 16)

@State
def maef_321():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef321_09', 16)

@State
def maef_340():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef340_00', 3)
    sprite('vrmaef340_01', 3)

@State
def maef_500():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef500_03', 3)
    CreateObject('maef_500_Particle', 0)

@State
def maef_500_Particle():
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_500dust', -1)

@State
def maef_501_zanzou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef501_00', 5)
    callSubroutine('Zanzou_Color')
    sprite('vrmaef501_01', 16)
    callSubroutine('Zanzou_Color')

@State
def maef_502_zanzou():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef502_00', 20)

@State
def maef_501_atk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        Hitstop(5)
        AirUntechableTime(17)
        Hitstun(17)
        AirPushbackX(20000)
        AirPushbackY(10000)
        PushbackX(30400)
        StarterRating(2)
        physicsXImpulse(0)

        def upon_32():
            SLOT_51 = 1

        def upon_33():
            HitLow(2)
        CollideWithWall(1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
    sprite('vrmaef501atk', 3)
    StartMultihit()
    AddX(50000)
    CreateObject('maef_501', -1)
    RegisterObject(4, 1)
    PrivateSE('mase_00')
    sprite('vrmaef501atk', 20)
    physicsXImpulse(60000)
    if SLOT_51:
        physicsXImpulse(30000)
    sprite('vrmaef501atk', 5)
    XImpulseAcceleration(60)
    sprite('vrmaef501atk', 5)
    XImpulseAcceleration(60)
    sprite('vrmaef501atk', 5)
    XImpulseAcceleration(60)
    ObjectUpon(4, 32)
    AttackOff()
    sprite('vrmaef501atk', 10)
    XImpulseAcceleration(20)
    label(580)
    sprite('vrmaef501atk', 10)
    clearUponHandler(54)
    DeleteObject(4)
    EndMomentum(1)
    AttackOff()

@State
def maef_501():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleY(600)
        SetScaleX(950)
        LinkParticle('maef_shot_sub')

        def upon_32():
            ConstantAlphaModifier(-10)
            AlphaValue(128)
            ObjectUpon(4, 32)
    sprite('vrmaef_shot00', 2)
    CreateObject('maef_501_Shot', -1)
    RegisterObject(4, 1)
    sprite('vrmaef_shot01', 2)
    sprite('vrmaef_shot02', 2)
    CreateObject('maef_501_Shot_aura', -1)
    label(0)
    sprite('vrmaef_shot00', 2)
    sprite('vrmaef_shot01', 2)
    sprite('vrmaef_shot02', 2)
    gotoLabel(0)

@State
def maef_501_Shot():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)

        def upon_32():
            ConstantAlphaModifier(-10)
            AlphaValue(128)
    sprite('null', 32767)
    CallPrivateEffect('maef_shot')

@State
def maef_501_Shot_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_shot_aura', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_shot_aura2', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_shot_dust', -1)
    gotoLabel(0)

@State
def maef_muzzle():
    sprite('null', 1)
    AddX(60000)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_muzzle_blm', -1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_muzzle_add', -1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_muzzle', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_muzzle_ring', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_muzzle_dust', -1)
    CreateParticle('maef_muzzle_sub', -1)

@State
def maef_503():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmaef503_00', 3)
    sprite('vrmaef503_01', 4)
    CreateObject('maef_503_particle', 0)
    sprite('vrmaef503_02', 4)

@State
def maef_503_particle():
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_503dust', -1)

@State
def maef_503_wind():

    def upon_IMMEDIATE():
        Eff3DEffect('maef_503wind.DIG', '')
        BlendMode_Normal()
        SetScaleXPerFrame(5)
        AddX(600000)
    sprite('null', 20)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def maef_520_slash():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        Eff3DEffect('maef_520slash.DIG', '')
        BlendMode_Add()
        AlphaValue(150)
        AddX(4000)
        Visibility(1)
    sprite('vrmaef520_00', 2)
    ParticleLayer(11)
    CallCustomizableParticle('maef_520smoke', 0)
    ParticleLayer(11)
    CallCustomizableParticle('maef_520smoke', 1)
    CreateParticle('maef_520smoke', 2)
    sprite('vrmaef520_00', 4)
    CreateParticle('maef_520smoke', 3)
    CreateParticle('maef_520smoke', 4)
    sprite('null', 10)
    E0EAEffectPosition(0)

@State
def maef_521_kick():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        AddX(256000)
        AddY(64000)
        AlphaValue(220)
    sprite('null', 3)
    Eff3DEffect('maef_521kick.DIG', '')
    sprite('null', 10)
    Eff3DEffect('maef_521kick2.DIG', '')
    E0EAEffectPosition(0)

@State
def maef_522():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        AddX(100000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    CreateObject('maef_522_a', -1)
    CreateObject('maef_522_b', -1)
    CreateObject('maef_522_c', -1)
    CreateObject('maef_522_dust', -1)
    label(0)
    sprite('null', 4)
    DespawnEAEffect('maef_522_c')
    DespawnEAEffect('maef_522_dust')
    SetScaleSpeed(-250)

@State
def maef_522_a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectScale(2)
    sprite('null', 32767)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_522a')

@State
def maef_522_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectScale(2)
    sprite('null', 32767)
    CallPrivateEffect('maef_522b')

@State
def maef_522_c():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AddX(-30000)
    label(0)
    sprite('null', 3)
    CreateObject('maef_522_c2', -1)
    gotoLabel(0)

@State
def maef_522_c2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 30)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_522c')

@State
def maef_522_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        AddX(-100000)
    label(0)
    sprite('null', 10)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_522dust', -1)
    gotoLabel(0)

@State
def maef_522_ribon():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef522_03', 16)

@State
def maef_530():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef530_00', 3)
    CreateObject('maef_530_Particle', 0)
    sprite('vrmaef530_01', 4)
    sprite('vrmaef530_02', 12)

@State
def maef_530_Particle():
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_530slash', -1)
    CallCustomizableParticle('maef_530slash_add', -1)

@State
def maef_531():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        callSubroutine('Zanzou_Color')
        AddX(64000)
    sprite('vrmaef531_00', 4)
    CreateObject('maef_531_smash', 0)
    sprite('vrmaef531_01', 20)

@State
def maef_531_smash():
    sprite('null', 1)
    AddX(-32000)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_531smash', -1)

@State
def maef_533():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddX(600000)
        AddX(150000)
    label(0)
    sprite('null', 2)
    CreateObject('maef_533_slash', -1)
    sprite('null', 2)
    CreateObject('maef_533_slash2', -1)
    sprite('null', 2)
    CreateObject('maef_533_slash3', -1)
    sprite('null', 2)
    CreateObject('maef_533_slash4', -1)
    sprite('null', 2)
    CreateObject('maef_533_slash5', -1)
    sprite('null', 2)
    CreateObject('maef_533_slash6', -1)
    gotoLabel(0)

@State
def maef_533_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_slash2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash2.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash2_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash2_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash2_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_slash3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash3.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash3_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash3_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash3_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_slash4():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash4.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash4_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash4_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash4_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_slash5():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash5.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash5_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash5_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash5_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_slash6():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash6.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 9)
    CreateObject('maef_533_slash6_add', -1)
    CreateObject('maef_533_particle', -1)

@State
def maef_533_slash6_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_533slash6_add.DIG', '')
        BlendMode_Add()
    sprite('null', 6)
    sprite('null', 3)
    AlphaValue(128)

@State
def maef_533_particle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        E0EAEffectPosition(3)
        DeviationY(350000, 0)
        DeviationX(-500000, -300000)
        RandAddRotation(30000, -30000)
    sprite('null', 6)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_533slash')
    CreateObject('maef_533_particle_add', -1)

@State
def maef_533_particle_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
    sprite('null', 6)
    CallPrivateEffect('maef_533slash_add')

@State
def maef_540():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef540_03', 2)
    AddX(-64000)
    sprite('vrmaef540_04', 16)
    AddX(64000)
    AddX(-128000)
    CreateObject('maef_540_Particle', 0)
    CreateObject('maef_540_Particle', 1)

@State
def maef_540_Particle():
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_540dust', -1)

@State
def ma203Shot():

    def upon_IMMEDIATE():
        Visibility(1)
        CreateObject('ma203_Shot_poly', -1)
        CreateObject('ma203_Shot_poly_add', -1)
        CreateObject('ma203_Shot_poly2', -1)
        CreateObject('ma203_Shot_particle', -1)
        SLOT_6 = 1
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(800)
        StarterRating(2)
        AttackP1(70)
        AttackP2(79)
        SingleProration(1)
        AirUntechableTime(35)
        Hitstun(19)
        Stagger(30)
        Crumple(25)
        CHStagger(40)
        CHCrumple(35)
        Hitstop(2)
        EnemyHitstopAddition(1, 11, 13)
        UseSlashHitspark(1)
        ContinueState(300)

        def upon_43():
            if (SLOT_48 == 0):
                RotationAngle(0)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(18000)
                callSubroutine('maef_color3')
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 1):
                RotationAngle(15000)
                AirHitstunAnimation(11)
                AirPushbackX(10000)
                AirPushbackY(13000)
                callSubroutine('maef_color3')
                ParticleRotationAngle(15000)
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                ParticleRotationAngle(15000)
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 2):
                RotationAngle(-15000)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(30000)
                callSubroutine('maef_color3')
                ParticleRotationAngle(-15000)
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                ParticleRotationAngle(-15000)
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 3):
                RotationAngle(20000)
                GroundedHitstunAnimation(19)
                AirHitstunAnimation(19)
                AirPushbackX(37000)
                AirPushbackY(5000)
                HardKnockdown(1)
                EnableEmergencyTechAirHit(1)
                SLOT_57 = 1
                callSubroutine('maef_color3')
                ParticleRotationAngle(20000)
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                ParticleRotationAngle(20000)
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 4):
                RotationAngle(0)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(18000)
                HardKnockdown(1)
                EnableEmergencyTechAirHit(1)
                SLOT_57 = 1
                callSubroutine('maef_color3')
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            if (SLOT_48 == 5):
                RotationAngle(40000)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(34000)
                AirPushbackY(-15000)
                HardKnockdown(1)
                SLOT_56 = 1
                SLOT_57 = 1
                callSubroutine('maef_color3')
                ParticleRotationAngle(40000)
                CallCustomizableParticle('maef_D_mazzle', -1)
                callSubroutine('maef_color2')
                ParticleRotationAngle(40000)
                CallCustomizableParticle('maef_D_mazzle_ring', -1)
            XSpeed2(70000, 0)
        if SLOT_7:
            AttackLevel_(4)
            Damage(900)
            AttackP2(82)
            EnemyHitstopAddition(11, 11, 13)
            if (not SLOT_57):
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
            Size(1500)
            HitOverhead(4)
            HitLow(4)
            HitAirUnblockable(4)

        def upon_39():
            clearUponHandler(39)
            SLOT_53 = 1

            def upon_OPPONENT_HIT_OR_BLOCK():
                clearUponHandler(11)
                sendToLabel(3)

        def upon_40():
            clearUponHandler(40)
            HitOverhead(0)
            HitLow(0)
            HitAirUnblockable(0)
            CrouchWhiff(0)
            Unknown23042()
            AttackDirection(0)
            sendToLabel(1)

        def upon_FRAME_STEP():
            if (SLOT_23 < 60000):
                PassbackAddActionMarkToFunction('NmlAtk5D', 33)
                PassbackAddActionMarkToFunction('NmlAtkAIR5D', 33)
            if SLOT_56:
                if (SLOT_23 < 180000):
                    PassbackAddActionMarkToFunction('NmlAtk5D', 33)
                    PassbackAddActionMarkToFunction('NmlAtkAIR5D', 33)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            AttackOff()
            PassbackAddActionMarkToFunction('NmlAtk5D', 32)
            PassbackAddActionMarkToFunction('NmlAtkAIR5D', 32)
            CreateObject('ma203_Shot_hit', -1)

        def upon_56():
            CopyFromRightToLeft(23, 2, 58, 3, 2, 58)
            if (not SLOT_58):
                sendToLabel(580)
        HitsPerCall(1, 0, 0, 0, 1, 0, 1, 1)

        def upon_54():
            clearUponHandler(39)
            clearUponHandler(40)
            sendToLabel(580)
        sendToLabelUpon(32, 580)
    sprite('ma203atk_dummy', 1)
    sprite('ma203atk_dummy', 1)
    if SLOT_7:
        XImpulseAcceleration(150)
        YAccel(150)
    label(0)
    sprite('ma203atk_dummy', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    EndMomentum(1)
    ForceFaceSprite()
    CreateObject('maef_D_turn', -1)
    PrivateSE('mase_03')
    sprite('ma203atk_dummy', 1)
    Unknown1111(70000, 22)
    RefreshMultihit()
    AirHitstunAnimation(17)
    EnemyHitstopAddition(11, 11, 13)
    AirPushbackX(1000)
    AirPushbackY(28000)
    HardKnockdownReset()
    if SLOT_7:
        XImpulseAcceleration(150)
        YAccel(150)
    elif SLOT_53:
        XImpulseAcceleration(150)
        YAccel(150)
    if SLOT_57:
        GroundedHitstunAnimation(17)
    label(2)
    sprite('ma203atk_dummy', 1)
    XImpulseAcceleration(105)
    YAccel(105)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ma203atk_dummy', 3)
    loopRest()
    gotoLabel(1)
    label(580)
    sprite('ma203atk_dummy', 1)
    clearUponHandler(43)
    clearUponHandler(39)
    clearUponHandler(40)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(11)
    clearUponHandler(54)
    clearUponHandler(32)
    SLOT_7 = 0
    PassbackAddActionMarkToFunction('NmlAtk5D', 33)
    PassbackAddActionMarkToFunction('NmlAtkAIR5D', 33)
    EndMomentum(1)
    AttackOff()

@State
def ma203_Shot_poly():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        E0EAEffectDirection(2)
        if SLOT_7:
            Size(1500)
    sprite('null', 32767)
    callSubroutine('maef_color3')
    CallPrivateEffect('maef_lance3')
    BlendMode_Add()
    PaletteIndex(1)
    ColorFromPaletteIndex(1)
    Unknown23048(1)
    Unknown23051('vrmaef_lancelay.hip', '')
    Unknown23050(20, 0)
    Unknown23052(40)
    Unknown23049(-1, 16777215)

@State
def ma203_Shot_poly_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        E0EAEffectDirection(2)
    sprite('null', 32767)
    LinkParticle('maef_lance')

@State
def ma203_Shot_poly2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        E0EAEffectDirection(2)
        if SLOT_7:
            Size(1500)
    sprite('null', 32767)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_lance2')
    BlendMode_Add()
    callSubroutine('maef_color')
    Unknown23048(1)
    Unknown23051('vrmaef_lancelay.hip', '')
    Unknown23050(20, 0)
    Unknown23052(60)
    Unknown23049(-1, -1)

@State
def ma203_Shot_particle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_lance_smoke', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_lance_dust', -1)
    gotoLabel(0)

@State
def ma203_Shot_hit():
    sprite('null', 1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_D_hit', -1)

@State
def maef_D_turn():
    sprite('null', 1)
    CreateParticle('maef_D_turn_add', -1)
    callSubroutine('maef_color2')
    ParticleSize(1500)
    CallCustomizableParticle('maef_D_turn00', -1)
    callSubroutine('maef_color2')
    ParticleSize(1500)
    CallCustomizableParticle('maef_D_turn_ring', -1)

@State
def maef_D_hold():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_203_up():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(-10000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_203_up2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(-20000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_203_down():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(10000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_203_down2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(20000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_AirD_hold():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(20000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_253_up():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(10000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_253_up2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_253_down():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(30000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_253_down2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RotationAngle(40000)
        DespawnEAEffect('maef_D')
    sprite('null', 32767)
    CreateObject('maef_D', -1)

@State
def maef_D():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 32767)
    CreateObject('maef_D_particle_a', -1)
    CreateObject('maef_D_particle_b', -1)
    CreateObject('maef_D_particle_c', -1)
    CreateObject('maef_D_particle_d', -1)
    CreateObject('maef_D_particle_e', -1)
    CreateObject('maef_D_particle_f', -1)
    CreateObject('maef_D_3d', -1)

@State
def maef_D_particle_a():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)

        def upon_32():
            Size(2000)
        if SLOT_7:
            Size(2000)
    sprite('null', 32767)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_D_hold_a')

@State
def maef_D_particle_b():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)

        def upon_32():
            Size(2000)
        if SLOT_7:
            Size(2000)
    sprite('null', 32767)
    CallPrivateEffect('maef_D_hold_b')

@State
def maef_D_particle_c():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)

        def upon_32():
            Size(2000)
        if SLOT_7:
            Size(2000)
    sprite('null', 32767)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_D_hold_c')

@State
def maef_D_particle_d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 32767)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_D_hold_d')

@State
def maef_D_particle_e():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 32767)
    CallPrivateEffect('maef_D_hold_e')

@State
def maef_D_particle_f():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 32767)
    callSubroutine('maef_color3')
    CallPrivateEffect('maef_D_hold_f')

@State
def maef_D_3d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
        Eff3DEffect('maef_203wind.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
        Size(600)
    sprite('null', 32767)

@State
def maef_catch():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        E0EAEffectRotation(2)
        IgnorePauses(3)
        SLOT_6 = 0
    sprite('vrmaef_catch', 1)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_catch')
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_catch_ring', 0)
    sprite('vrmaef_catch', 3)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_catch_dust', 0)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_catch_dust', 1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_catch_dust', 2)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_catch_dust', 3)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_catch_dust', 4)
    sprite('vrmaef_catch', 60)
    E0EAEffectPosition(0)

@State
def maef_401():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    CreateObject('maef_401_dust', 0)
    CreateObject('maef_401_ring', 0)
    CreateObject('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    loopRest()

@State
def maef_401C():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        RotationAngle(-30000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    CreateObject('maef_401_dust', 0)
    CreateObject('maef_401_ring', 0)
    CreateObject('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    loopRest()

@State
def maef_403():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        RotationAngle(90000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    CreateObject('maef_401_dust', 0)
    CreateObject('maef_401_ring', 0)
    CreateObject('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    ConstantAlphaModifier(-128)
    loopRest()

@State
def maef_403B():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        RotationAngle(60000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    CreateObject('maef_401_dust', 0)
    CreateObject('maef_401_ring', 0)
    CreateObject('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    ConstantAlphaModifier(-128)
    loopRest()

@State
def maef_403C():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        RotationAngle(30000)
        sendToLabelUpon(32, 1)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    CreateObject('maef_401_dust', 0)
    CreateObject('maef_401_ring', 0)
    CreateObject('maef_401_ring2', 0)
    label(0)
    sprite('vrmaef401_01', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    sprite('vrmaef401_00', 3)
    CreateObject('maef_401_aura', 0)
    CreateObject('maef_401_aura2', 0)
    CreateObject('maef_401_aura3', 0)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    ConstantAlphaModifier(-128)
    loopRest()

@State
def maef_401_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 60)
    LinkParticle('maef_401aura')

@State
def maef_401_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_401aura2')

@State
def maef_401_aura3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectRotation(2)
    sprite('null', 60)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_401aura3')

@State
def maef_401_dust():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_401dust')

@State
def maef_401_ring():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_401ring')

@State
def maef_401_ring2():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
    sprite('null', 60)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_401ring2')

@State
def maef_403_landing():

    def upon_IMMEDIATE():
        IgnorePauses(3)
    sprite('null', 60)
    CreateParticle('maef_403smoke', -1)
    callSubroutine('maef_color2')
    ParticleSize(1500)
    CallCustomizableParticle('maef_403dust', -1)
    callSubroutine('maef_color')
    ParticleSize(1500)
    CallCustomizableParticle('maef_403aura', -1)

@State
def maef_401_impact():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    LinkParticle('maef_401impact')
    sprite('null', 60)
    E0EAEffectPosition(0)

@State
def maef_401_impact_C():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RotationAngle(-45000)
    sprite('null', 1)
    LinkParticle('maef_401impact')
    sprite('null', 60)
    E0EAEffectPosition(0)

@State
def maef_401_hit():
    sprite('null', 1)
    CreateParticle('maef_401hit', -1)

@State
def maef430_test():

    def upon_IMMEDIATE():
        AddX(400000)
    sprite('null', 1)
    CreateObject('maef430_strike', -1)
    CreateObject('maef430_bg', -1)

@State
def maef430_hold():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        sendToLabelUpon(32, 0)
        AddX(240000)
        AddY(-16000)
    sprite('null', 60)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_430hold')
    label(0)
    sprite('null', 60)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-17)

@State
def maef430_hold_yari():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('null', 60)
    RotationAngle(-57000)
    callSubroutine('maef_color3')
    CallPrivateEffect('maef_430yari')

@State
def maef430_hold_yari_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('null', 60)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_430yari_aura')

@State
def maef430_hold_yari_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('null', 75)
    ParticleLayer(6)
    callSubroutine('maef_color3')
    CallPrivateEffect('maef_430yari_flower')

@State
def maef430_ex():
    sprite('null', 1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_430ex_dust', -1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_430ex_flower', -1)

@State
def maef430():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('null', 32767)
    CreateObject('maef430_bloom', -1)
    CreateObject('maef430_aura', -1)
    CreateObject('maef430_dust', -1)

@State
def maef430_aura():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_430aura.DIG', '')
        callSubroutine('maef_color2')
        BlendMode_Add()
        AddX(200000)
        AddY(-40000)
    sprite('null', 16)
    AlphaValue(0)
    ConstantAlphaModifier(64)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef430_bloom():

    def upon_IMMEDIATE():
        callSubroutine('maef_color')
        CallPrivateEffect('maef_430bloom')
        AddX(25000)
        AddY(-20000)
        IgnoreScreenfreeze(1)
    sprite('null', 8)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('null', 24)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef430_dust():
    sprite('null', 1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_430bloom00', -1)

@State
def maef430_lance():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmaef430_00', 2)
    sprite('vrmaef430_02', 3)
    sprite('vrmaef430_03', 3)
    sprite('vrmaef430_10', 2)
    sprite('vrmaef430_11', 2)

@State
def maef430_strike():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        AddY(168000)
        AddX(600000)
    sprite('null', 1)
    CreateObject('maef430_strike_aura', -1)
    CreateObject('maef430_strike_anm', -1)
    CreateObject('maef430_strike_3d', -1)
    CreateObject('maef430_strike_bg', -1)
    CreateObject('maef430_flower', -1)

@State
def maef430_strike_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 1)
    CreateParticle('maef_430strike_add', -1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_430strike_blm', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_430strike_ring00', -1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_430strike_aura', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_430strike_dust', -1)

@State
def maef430_strike_anm():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmaef430_50', 6)
    sprite('vrmaef430_51', 20)
    ConstantAlphaModifier(-12)
    SetScaleXPerFrame(20)

@State
def maef430_strike_3d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_430lance.DIG', '')
        BlendMode_Add()
        SetScaleY(2000)
        SetScaleX(1750)
    sprite('null', 25)
    ConstantAlphaModifier(-10)

@State
def maef430_strike_bg():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_430bg.DIG', '')
        callSubroutine('maef_color3')
        BlendMode_Add()
    sprite('null', 25)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-10)

@State
def maef430_bg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 1)
    CreateParticle('maef_430smoke', -1)
    CreateObject('maef430_bg_aura', -1)

@State
def maef430_bg_aura():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_430aura2.DIG', '')
        BlendMode_Add()
    sprite('null', 32)
    Size(1500)
    AlphaValue(175)
    ConstantAlphaModifier(-6)

@State
def maef430_flower():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrmaef430_60', 16)
    CreateObject('maef430_flower_particle', -1)
    SetScaleSpeed(10)
    sprite('vrmaef430_61', 8)
    sprite('vrmaef430_62', 8)
    E0EAEffectPosition(0)
    sprite('vrmaef430_63', 10)
    ConstantAlphaModifier(-25)

@State
def maef430_flower_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_430flower_dust', -1)

@State
def maef430_flower_particle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        AddX(-130000)
    sprite('null', -1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_430flower', -1)

@State
def maef430_od():
    sprite('null', -1)
    AddY(164000)
    AddX(64000)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_430_od', -1)

@State
def maef431():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(700)
        AttackP2(75)
        AirPushbackX(-3000)
        AirPushbackY(24000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        UsePunchHitspark(1)
        Hitstop(1)
        SameMoveProration(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        Visibility(1)
        ContinueState(15)
    sprite('vrmaef431_00', 30)
    CreateObject('maef431_aura', 0)
    CreateObject('maef431_aura2', 0)
    CreateObject('maef431_aura_add', 0)
    CreateObject('maef431_aura_add2', 0)
    CreateObject('maef431_aura_screw', 0)
    CreateObject('maef431_hold_dust', 0)
    CreateObject('maef431_bloom', -1)

@State
def maef431_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        Rotation(-204000)
    sprite('null', 25)
    CallPrivateEffect('maef_431aura')

@State
def maef431_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        Rotation(-204000)
    sprite('null', 25)
    ParticleLayer(11)
    CallPrivateEffect('maef_431aura01')

@State
def maef431_aura_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Rotation(-204000)
        AlphaValue(191)
    sprite('null', 25)
    CallPrivateEffect('maef_431add')

@State
def maef431_aura_add2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Rotation(-204000)
        callSubroutine('maef_color2')
    sprite('null', 25)
    CallPrivateEffect('maef_431add00')

@State
def maef431_aura_screw():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
        Flip()
        Eff3DEffect('maef_431aura.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
        Rotation(24000)
    sprite('null', 32767)

@State
def maef431_hold_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        AddX(100000)
        AddY(50000)
    sprite('null', 25)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_431hold_flower', -1)

@State
def maef431_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
    sprite('null', 25)
    CallPrivateEffect('maef_431bloom')

@State
def maef431_jump():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(100)
    sprite('vrmaef431_10', 3)
    CreateObject('maef431_jump1', 0)
    CreateObject('maef431_jump1add', 0)
    sprite('vrmaef431_11', 3)
    DespawnEAEffect('maef431_jump1')
    DespawnEAEffect('maef431_jump1add')
    CreateObject('maef431_jump2', 0)
    CreateObject('maef431_jump2add', 0)
    sprite('vrmaef431_12', 2)
    DespawnEAEffect('maef431_jump2')
    DespawnEAEffect('maef431_jump2add')
    CreateObject('maef431_jump3', 0)
    CreateObject('maef431_jump3add', 0)
    CreateObject('maef431_tornade', -1)
    CreateObject('maef431_dust', -1)
    label(0)
    sprite('vrmaef431_13', 2)
    sprite('vrmaef431_12', 2)
    gotoLabel(0)

@State
def maef431_jump_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(100)
    sprite('vrmaef431_10', 3)
    CreateObject('maef431_jump1', 0)
    CreateObject('maef431_jump1add', 0)
    sprite('vrmaef431_11', 3)
    DespawnEAEffect('maef431_jump1')
    DespawnEAEffect('maef431_jump1add')
    CreateObject('maef431_jump2', 0)
    CreateObject('maef431_jump2add', 0)
    sprite('vrmaef431_12', 2)
    DespawnEAEffect('maef431_jump2')
    DespawnEAEffect('maef431_jump2add')
    CreateObject('maef431_jump3', 0)
    CreateObject('maef431_jump3add', 0)
    CreateObject('maef431_tornade', -1)
    CreateObject('maef431_dust_od', -1)
    label(0)
    sprite('vrmaef431_13', 2)
    sprite('vrmaef431_12', 2)
    gotoLabel(0)

@State
def maef431_jump1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        RotationAngle(33000)
        Size(800)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance')

@State
def maef431_jump1add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RotationAngle(33000)
        Size(800)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance_add')

@State
def maef431_jump2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        RotationAngle(-3000)
        Size(950)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance')

@State
def maef431_jump2add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RotationAngle(-3000)
        Size(950)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance_add')

@State
def maef431_jump3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        RotationAngle(180000)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance')

@State
def maef431_jump3add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RotationAngle(180000)
    sprite('null', 32767)
    CallPrivateEffect('maef_431lance_add')

@State
def maef431_tornade():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        SetScaleSpeed(7)
    sprite('vrmaef431_30', 6)
    sprite('vrmaef431_31', 6)
    sprite('null', 1)
    CreateObject('maef431_tornade2', -1)

@State
def maef431_tornade2():

    def upon_IMMEDIATE():
        callSubroutine('Zanzou_Color')
        AddScale(84)
        SetScaleSpeed(7)
    sprite('vrmaef431_32', 10)

@State
def maef431_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_431dust', -1)
    gotoLabel(0)

@State
def maef431_dust_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    label(0)
    sprite('null', 3)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_431dust', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_431flower', -1)
    gotoLabel(0)

@State
def maef431_fall():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrmaef431_20', 2)
    CreateObject('maef431_fall_lance', 0)
    CreateObject('maef431_fall_lance_add', 0)
    CreateObject('maef431_fall_bloom', 0)
    CreateObject('maef431_fall_ribon', 0)
    CreateObject('maef431_fall_dust', 0)
    label(0)
    sprite('vrmaef431_21', 2)
    sprite('vrmaef431_20', 2)
    gotoLabel(0)

@State
def maef431_fall_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrmaef431_20', 2)
    CreateObject('maef431_fall_lance', 0)
    CreateObject('maef431_fall_lance_add', 0)
    CreateObject('maef431_fall_bloom', 0)
    CreateObject('maef431_fall_ribon', 0)
    CreateObject('maef431_fall_dust', 0)
    label(0)
    sprite('vrmaef431_21', 2)
    sprite('vrmaef431_20', 2)
    gotoLabel(0)

@State
def maef431_fall_lance():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color3')
    sprite('null', 32767)
    CallPrivateEffect('maef_431fall')

@State
def maef431_fall_lance_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 32767)
    CallPrivateEffect('maef_431fall_add')

@State
def maef431_fall_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('maef_color')
        AddY(300000)
        AlphaValue(128)
    sprite('null', 32767)
    CallPrivateEffect('maef_431fall_blm')

@State
def maef431_fall_ribon():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('maef_431ribon.DIG', '')
        callSubroutine('maef_color2')
        AddY(18000)
    sprite('null', 32767)

@State
def maef431_fall_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        AddY(305000)
    label(0)
    sprite('null', 2)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_431fall_dust', -1)
    gotoLabel(0)

@State
def maef431_crash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 100)
    ScreenShake(48000, 48000)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_431crash_wave', -1)
    CreateObject('maef431_crash_aura', -1)
    CreateObject('maef431_crash_yari', -1)
    CreateObject('maef431_crash_particle', -1)
    CreateObject('maef431_flower_3d', -1)
    CreateObject('maef431_flower_particle', -1)
    CreateObject('maef431_storm', -1)
    CreateObject('maef431_storm2', -1)
    CreateObject('maef431_rock', -1)

@State
def maef431_crash_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 100)
    ScreenShake(64000, 64000)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_431crash_wave_od', -1)
    CreateObject('maef431_crash_aura', -1)
    CreateObject('maef431_crash_yari_od', -1)
    CreateObject('maef431_crash_particle', -1)
    CreateObject('maef431_flower_3d', -1)
    CreateObject('maef431_flower_particle', -1)
    CreateObject('maef431_storm', -1)
    CreateObject('maef431_storm2', -1)
    CreateObject('maef431_rock', -1)

@State
def maef431_crash_particle():
    sprite('null', 1)
    callSubroutine('3d_color')
    CallCustomizableParticle('maef_431crash_blm', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_431crash_dust', -1)

@State
def maef431_crash_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrmaef431_40', 6)
    sprite('vrmaef431_41', 6)
    sprite('vrmaef431_42', 6)
    sprite('vrmaef431_43', 6)

@State
def maef431_flower_3d():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 5)
    CreateObject('maef431_flower3', -1)
    CreateObject('maef431_flower4', -1)
    CreateObject('maef431_flower', -1)
    sprite('null', 5)
    CreateObject('maef431_flower2', -1)
    sprite('null', 5)
    CreateObject('maef431_flower', -1)
    sprite('null', 5)
    CreateObject('maef431_flower2', -1)
    sprite('null', 5)
    CreateObject('maef431_flower', -1)
    sprite('null', 5)
    CreateObject('maef431_flower2', -1)
    sprite('null', 100)

@State
def maef431_flower():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431flower.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color')
        BlendMode_Add()
        RandAddScale(-500, 250)
        SetScaleSpeed(10)
        CreateObject('maef431_flower_b', -1)
    sprite('null', 6)
    sprite('null', 10)
    E0EAEffectPosition(0)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef431_flower_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431flower.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color3')
        BlendMode_Add()
        E0EAEffectScale(2)
    sprite('null', 32)
    ConstantAlphaModifier(-8)

@State
def maef431_flower2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431flower2.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color')
        BlendMode_Add()
        RandAddScaleY(-250, -500)
        RandAddScaleX(1000, 800)
        RandAddScaleZ(1000, 800)
        SetScaleSpeed(10)
        AlphaValue(128)
        DeviationY(160000, 80000)
        DeviationX(-32000, 32000)
        CreateObject('maef431_flower2b', -1)
    sprite('null', 6)
    sprite('null', 10)
    E0EAEffectPosition(0)
    sprite('null', 16)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-8)

@State
def maef431_flower2b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431flower2.DIG', '')
        FaceSpawnLocation()
        E0EAEffectScale(2)
        callSubroutine('maef_color3')
        BlendMode_Add()
    sprite('null', 16)
    ConstantAlphaModifier(-8)
    sprite('null', 16)

@State
def maef431_flower3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431flower3.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color')
        BlendMode_Add()
        CreateObject('maef431_flower3b', -1)
    sprite('null', 60)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-10)

@State
def maef431_flower3b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431flower3.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color3')
        BlendMode_Add()
        E0EAEffectScale(2)
    sprite('null', 60)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-10)

@State
def maef431_flower4():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431flower4.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color')
        BlendMode_Add()
        SetScaleY(800)
        SetScaleX(1600)
        SetScaleZ(1600)
        SetScaleSpeed(10)
        AlphaValue(128)
        AddY(50000)
        CreateObject('maef431_flower4b', -1)
    sprite('null', 16)
    sprite('null', 16)
    ConstantAlphaModifier(-8)

@State
def maef431_flower4b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431flower4.DIG', '')
        FaceSpawnLocation()
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        callSubroutine('maef_color3')
        BlendMode_Add()
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef431_storm():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431storm.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color2')
        BlendMode_Add()
        Size(1100)
    sprite('null', 6)
    CreateObject('maef431_storm_add', -1)
    sprite('null', 26)
    E0EAEffectPosition(0)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef431_storm_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431storm.DIG', '')
        FaceSpawnLocation()
        E0EAEffectScale(2)
        callSubroutine('maef_color3')
        BlendMode_Add()
    sprite('null', 32)
    AlphaValue(128)
    ConstantAlphaModifier(-4)

@State
def maef431_storm2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('maef_431storm2.DIG', '')
        FaceSpawnLocation()
        callSubroutine('maef_color2')
        BlendMode_Add()
    sprite('null', 6)
    CreateObject('maef431_storm2_add', -1)
    sprite('null', 10)
    E0EAEffectPosition(0)
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def maef431_storm2_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('maef_431storm2.DIG', '')
        FaceSpawnLocation()
        E0EAEffectScale(2)
        callSubroutine('maef_color3')
        BlendMode_Add()
    sprite('null', 16)
    AlphaValue(128)
    ConstantAlphaModifier(-8)

@State
def maef431_flower_particle():
    sprite('null', 1)
    callSubroutine('maef_color3')
    CallCustomizableParticle('maef_431crash_flower', -1)

@State
def maef431_crash_yari():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('null', 20)
    AddX(17000)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_431crash')
    CreateObject('maef431_crash_yari_add', -1)

@State
def maef431_crash_yari_add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('null', 20)
    AddX(17000)
    LinkParticle('maef_431crash_add')

@State
def maef431_crash_yari_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        SetScaleX(1750)
        SetScaleY(1250)
    sprite('null', 20)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_431crash')
    CreateObject('maef431_crash_yari_add_od', -1)

@State
def maef431_crash_yari_add_od():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        E0EAEffectScale(2)
    sprite('null', 20)
    LinkParticle('maef_431crash_add')

@State
def maef431_rock():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        Eff3DEffect('maef_431crack.DIG', '')
        BlendMode_Normal()
        RenderLayer(2)
        SetScaleX(1750)
    sprite('null', 20)
    CreateObject('maef431_rock_bloom', -1)
    CreateParticle('maef_431rock', -1)
    sprite('null', 40)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-6)

@State
def maef431_rock_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
    sprite('null', 20)
    Size(1255)
    callSubroutine('maef_color')
    ParticleLayer(2)
    CallPrivateEffect('maef_431rock_blm')
    sprite('null', 40)
    E0EAEffectPosition(0)

@State
def AstralCamera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
        sendToLabelUpon(37, 5)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    label(1)
    sprite('null', 20)
    physicsYImpulse(90000)
    sprite('null', 32767)
    EndMomentum(1)
    label(2)
    sprite('null', 5)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    EndMomentum(1)
    CameraFast(1)
    sprite('null', 10)
    SetBackground(3)
    CameraFast(0)
    TeleportToObject(3)
    AddY(250000)
    EndMomentum(1)
    sprite('null', 32767)
    CreateObject('maef_ah_Ryuhai', -1)
    CommonSE('000_airdash_0')
    label(3)
    sprite('null', 10)
    sprite('null', 5)
    SetBackground(2)
    sprite('null', 10)
    SetBackground(3)
    sprite('null', 32767)
    AbsoluteY(3000000)
    CameraFast(1)
    label(4)
    sprite('null', 50)
    physicsYImpulse(-50000)
    CreateObject('maef450_yari', -1)
    PrivateSE('mase_10')
    PrivateSE('mase_10')
    sprite('null', 10)
    physicsYImpulse(-4000)
    sprite('null', 10)
    physicsYImpulse(-2000)
    sprite('null', 40)
    physicsYImpulse(-1000)
    sprite('null', 40)
    EndMomentum(1)
    sprite('null', 30)
    SLOT_11 = 1
    sprite('null', 40)
    CreateObject('maef450_bomb', -1)
    sprite('null', 5)
    CreateObject('maef450_bomb2', -1)
    PrivateSE('mase_11')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 32767)
    CreateObject('maef450_cloud2', -1)
    CreateObject('maef450_cloud', -1)
    label(5)
    sprite('null', 30)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    CreateObject('maef_ah_killwhite', -1)
    FloorCollision(0)
    clearUponHandler(2)
    sprite('null', 32767)
    Unknown20010(0, 700, 0)

@State
def maef450():
    sprite('null', 1)
    IgnoreScreenfreeze(1)
    CreateObject('maef450_circle', -1)
    CreateObject('maef450_lance', -1)
    CreateObject('maef450_aura', -1)
    CreateObject('maef450_wind', -1)

@State
def maef450_circle():
    sprite('null', 1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_450circle', -1)
    CreateParticle('maef_450circle_add', -1)

@State
def maef450_lance():
    sprite('null', 1)
    AddX(5000)
    AddY(-10000)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_450lance', -1)
    CreateParticle('maef_450lance_add', -1)

@State
def maef450_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_450aura.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
    sprite('null', 30)
    SetScaleX(500)
    SetScaleXPerFrame(25)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 15)
    SetScaleXPerFrame(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)

@State
def maef450_wind():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_450wind.DIG', '')
        RenderLayer(11)
        BlendMode_Normal()
    sprite('null', 30)
    Size(500)
    AddScaleY(250)
    SetScaleSpeed(16)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 30)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)

@State
def maef450_slash():
    sprite('null', 1)
    CreateObject('maef450_zanzou', -1)
    CreateObject('maef450_aura2', -1)
    CreateObject('maef450_wind2', -1)
    CreateObject('maef450_dust', -1)
    CreateObject('maef450_smoke', -1)

@State
def maef450_zanzou():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef450_00', 3)
    sprite('vrmaef450_01', 16)

@State
def maef450_aura2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        Eff3DEffect('maef_450slash.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
        AddY(256000)
        SetScaleSpeed(15)
    sprite('null', 15)

@State
def maef450_wind2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('maef_450wind2.DIG', '')
        RenderLayer(2)
        AddScaleY(1250)
        BlendMode_Normal()
    sprite('null', 32)
    SetScaleSpeed(25)
    ConstantAlphaModifier(-8)

@State
def maef450_dust():
    sprite('null', 1)
    callSubroutine('maef_color')
    CallCustomizableParticle('maef_450dust2', -1)

@State
def maef450_smoke():
    sprite('null', 1)
    AddX(90000)
    CallCustomizableParticle('maef_450smoke', -1)

@State
def maef450_upper():
    sprite('null', 1)
    AddX(-128000)
    CreateObject('maef450_zanzou2', -1)
    CreateObject('maef450_particle', -1)
    CreateObject('maef450_aura3', -1)

@State
def maef450_zanzou2():
    sprite('vrmaef450_10', 20)
    callSubroutine('Zanzou_Color')

@State
def maef450_particle():
    sprite('null', 1)
    callSubroutine('maef_color')
    ParticleRotationAngle(40000)
    CallCustomizableParticle('maef_450upper', -1)

@State
def maef450_aura3():

    def upon_IMMEDIATE():
        Eff3DEffect('maef_450upper.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Add()
        RotationAngle(40000)
    sprite('null', 30)
    SetScaleXPerFrame(-33)
    ConstantAlphaModifier(-8)

@State
def maef450_charge():
    sprite('null', 32767)
    E0EAEffectScale(2)
    CreateObject('maef450_charge_lance', -1)
    CreateObject('maef450_charge_lance_add', -1)
    CreateObject('maef450_charge_lance_sub', -1)
    CreateObject('maef450_charge_aura', -1)
    CreateObject('maef450_charge_aura2', -1)
    CreateObject('maef450_charge_bloom', -1)
    CreateObject('maef450_charge_flower', -1)

@State
def maef450_charge_flower():
    sprite('null', 32767)
    RemoveOnCallStateEnd(2)
    ParticleSize(2)
    callSubroutine('maef_color2')
    CallPrivateEffect('maef_450charge_flower')

@State
def maef450_charge_lance():
    sprite('null', 32767)
    RemoveOnCallStateEnd(2)
    callSubroutine('3d_color')
    ParticleSize(2)
    CallPrivateEffect('maef_450charge')

@State
def maef450_charge_lance_add():
    sprite('null', 32767)
    RemoveOnCallStateEnd(2)
    ParticleSize(2)
    LinkParticle('maef_450charge_add')

@State
def maef450_charge_lance_sub():
    sprite('null', 32767)
    RemoveOnCallStateEnd(2)
    AddY(200000)
    ParticleSize(2)
    LinkParticle('maef_450charge_sub')

@State
def maef450_charge_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        FaceLeft()
        callSubroutine('maef_color2')
        Eff3DEffect('maef_450charge.DIG', '')
        BlendMode_Add()
        AddY(-25000)
        SetScaleX(750)
        SetScaleY(1250)
    sprite('null', 32767)

@State
def maef450_charge_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        FaceLeft()
        callSubroutine('3d_color')
        Eff3DEffect('maef_450charge2.DIG', '')
        BlendMode_Normal()
        AlphaValue(128)
        AddY(-100000)
        SetScaleY(1000)
        SetScaleX(1500)
    sprite('null', 32767)

@State
def maef450_charge_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        callSubroutine('maef_color')
        Eff3DEffect('maef_450bloom.DIG', '')
        BlendMode_Add()
        AlphaValue(64)
        AddY(-25000)
        SetScaleX(1000)
    sprite('null', 32767)

@State
def maef450_throw():
    sprite('null', 3)
    LinkParticle('maef_450throw_sub')
    CreateParticle('maef_450throw_speed', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450throw_dust', -1)
    CreateObject('maef_450_throw_flower', -1)
    callSubroutine('3d_color')
    CallCustomizableParticle('maef_450throw', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450throw_add', -1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450throw_yari', -1)
    sprite('null', 32767)
    CreateParticle('maef_450throw_yari2', -1)

@State
def maef_450_throw_flower():
    sprite('null', 1)
    AddY(60000)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450throw_flower', -1)

@State
def maef450_yari():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(0)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        TeleportToObject(2)
        AddY(98000)
        E0EAEffectPosition(2)
    sprite('maef450_90', 6)
    sprite('maef450_91', 6)
    sprite('maef450_92', 6)
    CreateObject('maef450_yari_dust', -1)
    sprite('maef450_93', 7)
    sprite('maef450_94', 8)
    sprite('maef450_95', 6)
    CreateObject('maef450_yari2_dust', -1)
    sprite('maef450_96', 4)
    sprite('maef450_97', 3)
    sprite('maef450_98', 3)
    sprite('null', 20)
    physicsYImpulse(-4000)
    sprite('null', 10)
    physicsYImpulse(-1000)
    sprite('null', 70)
    CreateObject('maef450_yari2', -1)
    sprite('null', 60)

@State
def maef450_yari2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CreateObject('maef450_yari2_add', -1)
    sprite('null', 60)
    callSubroutine('maef_color')
    CallPrivateEffect('maef_450kira')
    Size(1100)
    SetScaleSpeed(-18)

@State
def maef450_yari2_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 60)
    CallPrivateEffect('maef_450kira')
    Size(775)
    SetScaleSpeed(-12)

@State
def maef450_yari_dust():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddY(-128000)
    sprite('null', 8)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450yari_dust', -1)
    CreateObject('maef450_yari_speed', -1)
    sprite('null', 9)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450yari_dust', -1)
    sprite('null', 10)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450yari_dust', -1)
    sprite('null', 1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_450yari_dust', -1)

@State
def maef450_yari2_dust():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(1000)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    CreateObject('maef450_yari2_speed', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(800)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(600)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(400)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    CreateObject('maef450_yari2_speed2', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(200)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    sprite('null', 3)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(150)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    sprite('null', 6)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(120)
    CallCustomizableParticle('maef_450yari2_dust', -1)
    sprite('null', 6)
    callSubroutine('maef_color2')
    ParticleSize(90)
    CallCustomizableParticle('maef_450yari2_dust', -1)

@State
def maef450_yari_speed():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed', -1)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed', -1)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed', -1)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed', -1)

@State
def maef450_yari2_speed():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddY(-192000)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed2', -1)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed2', -1)
    sprite('null', 6)
    CreateParticle('maef_450yari_speed2', -1)

@State
def maef450_yari2_speed2():

    def upon_IMMEDIATE():
        AddY(-110000)
    sprite('null', 30)
    LinkParticle('maef_450yari_speed3')
    sprite('null', 5)
    AddY(-50000)
    sprite('null', 60)
    ConstantAlphaModifier(-4)

@State
def maef450_bomb():

    def upon_IMMEDIATE():
        FaceLeft()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        TeleportToObject(2)
        AddY(-32000)
    sprite('null', 1)
    CreateParticle('maef_450bomb_ring', -1)

@State
def maef450_bomb2():

    def upon_IMMEDIATE():
        FaceLeft()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        Eff3DEffect('maef_450bomb.DIG', '')
        BlendMode_Add()
        TeleportToObject(2)
        AddY(-32000)
        ContinueState(120)
    sprite('null', 6)
    SetScaleSpeed(100)
    CreateParticle('maef_450bomb', -1)
    sprite('null', 10)
    SetScaleSpeed(10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    label(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    SetScaleSpeed(4)
    gotoLabel(0)

@State
def maef450_cloud():

    def upon_IMMEDIATE():
        RenderLayer(2)
        FaceLeft()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        Eff3DEffect('maef_astral_whirl.DIG', '')
        BlendMode_Normal()
        TeleportToObject(2)
        AddY(-150000)
        ContinueState(120)
    sprite('null', 32767)

@State
def maef450_cloud2():

    def upon_IMMEDIATE():
        RenderLayer(2)
        FaceLeft()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        Eff3DEffect('maef_astral_black.DIG', '')
        TeleportToObject(2)
        AddY(-225000)
        ContinueState(120)
        BlendMode_Normal()
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(128)

@State
def maef_ah_Ryuhai():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('maef_450kirikae', '')
        SetScaleY(-1000)
    sprite('null', 20)

@State
def maef_ah_killwhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        E0EAEffectPosition(2)
        SetPosXByScreenPer(50)
        Size(10000)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vr_white', 5)
    ConstantAlphaModifier(51)
    sprite('vr_white', 120)
    sprite('vr_white', 5)
    ConstantAlphaModifier(-51)

@State
def ma450yari_dummy():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('ma450yari_dummy', 32767)

@State
def maef_440():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef312_00', 3)
    sprite('vrmaef312_01', 15)

@State
def maef_440_slash_3d():

    def upon_IMMEDIATE():
        Eff3DEffect('maef_440slash.DIG', '')
        callSubroutine('3d_color')
        BlendMode_Normal()
        AddScale(500)
        RandRotationAngle()
        AddX(256000)
        AddY(256000)
    sprite('null', 15)
    CreateObject('maef_440_slash_3d_add', -1)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-16)

@State
def maef_440_slash_3d_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        E0EAEffectScale(2)
        Eff3DEffect('maef_440slash.DIG', '')
        BlendMode_Add()
    sprite('null', 15)

@State
def maef_440_slash1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_00', 4)
    sprite('vrmaef440_01', 10)

@State
def maef_440_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_10', 4)
    sprite('vrmaef440_11', 10)

@State
def maef_440_slash3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_20', 4)
    sprite('vrmaef440_21', 4)
    sprite('vrmaef440_22', 10)

@State
def maef_440_slash4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_30', 4)
    sprite('vrmaef440_31', 4)

@State
def maef_440_slash5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        callSubroutine('Zanzou_Color')
    sprite('vrmaef440_40', 4)
    sprite('vrmaef440_41', 10)

@State
def maef_440_finish():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou_Color')
        AddScaleX(250)
        AddX(-192000)
    sprite('vrmaef440_90', 20)

@State
def maef_440_finish2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        callSubroutine('Zanzou_Color')
        AddScaleX(250)
    sprite('vrmaef440_80', 20)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        AddX(280000)
    sprite('null', 32767)

@State
def maef_311_shadow2():

    def upon_IMMEDIATE():
        AddX(200000)
    sprite('null', 20)
    CreateParticle('maef_311shadow2', -1)
    sprite('null', 14)
    sprite('null', 1)
    ApplyFunctionsToObjects(22)
    ForceShadowOff(0)
    ApplyFunctionsToSelf()

@State
def maef_311_shadow2_b():

    def upon_IMMEDIATE():
        AddX(160000)
    sprite('null', 20)
    CreateParticle('maef_311shadow2', -1)
    sprite('null', 14)
    sprite('null', 1)
    ApplyFunctionsToObjects(22)
    ForceShadowOff(0)
    ApplyFunctionsToSelf()

@State
def maef_601():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        AddY(704000)
    sprite('null', 30)
    sprite('maef601_00', 2)
    physicsYImpulse(-64000)
    CreateObject('maef_601_dust', -1)
    sprite('maef601_00', 2)
    CreateObject('maef_601_dust', -1)
    sprite('maef601_00', 2)
    CreateObject('maef_601_dust', -1)
    sprite('maef601_00', 2)
    CreateObject('maef_601_dust', -1)
    sprite('maef601_00', 2)
    CreateObject('maef_601_dust', -1)

@State
def maef_601_dust():
    sprite('null', 1)
    callSubroutine('maef_color2')
    CallCustomizableParticle('maef_601dust', -1)

@State
def maef_600():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        AddY(250000)
    sprite('vrmaef600m_00', 30)
    physicsXImpulse(-35000)
    physicsYImpulse(18000)
    setGravity(500)
    SetAcceleration(500)