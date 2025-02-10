@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        Size(1550)
        AddY(270000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_su.DIG', '')
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
        Size(1550)
        AddY(270000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_su.DIG', '')
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
def EMB_SU_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        Size(1550)
        AddY(270000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_su.DIG', '')
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
def suef_test():

    def upon_IMMEDIATE():
        pass


@State
def suef_unlock_center__at__():
    sprite('null', 1)
    CreateParticle('suef_unlock', -1)
    PaletteIndex(1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_unlock_color', -1)


@State
def suef_unlock1st__at__():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        AddY(40000)
    sprite('vrsuef_font01', 20)
    CreateObject('suef_unlock_center', -1)
    sprite('vrsuef_font01', 5)
    ConstantAlphaModifier(-51)


@State
def suef_unlock_center():
    CallCustomizableParticle('suef_unlock', -1)
    PaletteIndex(1)
    ParticleSize(1500)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_unlock_color', -1)
    ParticleSize(1400)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_unlock_square', -1)


@State
def suef_unlock_particle():
    pass


@State
def suef_unlock_tama():
    pass


@State
def suef_unlock1st():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1300)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font01', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)


@State
def suef_unlock2nd():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font02', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)


@State
def suef_unlock3rd():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font03', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)


@State
def suef_unlock4th():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font04', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)
    CreateObject('suef_unlock_tama', 3)


@State
def suef_unlock5th():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font05', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)
    CreateObject('suef_unlock_tama', 3)
    CreateObject('suef_unlock_tama', 4)


@State
def suef_unlock6th():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font06', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)
    CreateObject('suef_unlock_tama', 3)
    CreateObject('suef_unlock_tama', 4)
    CreateObject('suef_unlock_tama', 5)


@State
def suef_unlock7th():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font07', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)
    CreateObject('suef_unlock_tama', 3)
    CreateObject('suef_unlock_tama', 4)
    CreateObject('suef_unlock_tama', 5)
    CreateObject('suef_unlock_tama', 6)


@State
def suef_unlock8th():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(40000)
        Size(1100)
    sprite('suef_unlock', 1)
    CreateObject('suef_unlock_font08', -1)
    CreateObject('suef_unlock_center', -1)
    CreateObject('suef_unlock_particle', 0)
    CreateObject('suef_unlock_particle', 1)
    CreateObject('suef_unlock_particle', 2)
    CreateObject('suef_unlock_particle', 3)
    CreateObject('suef_unlock_particle', 4)
    CreateObject('suef_unlock_particle', 5)
    CreateObject('suef_unlock_particle', 6)
    CreateObject('suef_unlock_particle', 7)
    CreateObject('suef_unlock_tama', 0)
    CreateObject('suef_unlock_tama', 1)
    CreateObject('suef_unlock_tama', 2)
    CreateObject('suef_unlock_tama', 3)
    CreateObject('suef_unlock_tama', 4)
    CreateObject('suef_unlock_tama', 5)
    CreateObject('suef_unlock_tama', 6)
    CreateObject('suef_unlock_tama', 7)


@State
def suef_unlock_font01():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font01', 10)
    sprite('vrsuef_font01', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font02():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font02', 10)
    sprite('vrsuef_font02', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font03():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font03', 10)
    sprite('vrsuef_font03', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font04():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font04', 10)
    sprite('vrsuef_font04', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font05():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font05', 10)
    sprite('vrsuef_font05', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font06():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font06', 10)
    sprite('vrsuef_font06', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font07():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font07', 10)
    sprite('vrsuef_font07', 20)
    ConstantAlphaModifier(-12)


@State
def suef_unlock_font08():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Sub()
        RenderLayer(1)
        Size(1100)
        SetScaleSpeed(6)
    sprite('vrsuef_font08', 10)
    sprite('vrsuef_font08', 20)
    ConstantAlphaModifier(-12)


@State
def suef_aura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('null', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_aura', -1)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_aura_add', -1)
    sprite('null', 8)
    ParticleColorFromPalette(241, 241, 241)
    CallCustomizableParticle('suef_aura', -1)


@State
def suef_dust():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleLayer(11)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_dust00', -1)
    CreateParticle('suef_dust', -1)


@State
def suef_dust_front():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_dust00', -1)
    CreateParticle('suef_dust', -1)


@State
def suef_dust_large():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleLayer(11)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_dust_c2', -1)
    CreateParticle('suef_dust_large', -1)


@State
def suef_200():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(-8000)
        AddY(10000)
    sprite('vrsuef200_00', 4)
    CreateObject('suef_dust', 0)
    sprite('vrsuef200_01', 5)


@State
def suef_230():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(-30000)
        AddY(10000)
    sprite('vrsuef230_00', 5)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef230_01', 4)


@State
def suef_250():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        SetZVal(-500)
    sprite('vrsuef250_00', 5)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef250_01', 4)


@State
def suef_210_shot():
    sprite('null', 1)
    CreateParticle('suef_210shot_b', -1)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_210shot', -1)
    if SLOT_19 >= 200000:
        CreateObject('suef_210_shot_add', -1)
    else:
        CopyFromRightToLeft(23, 2, 0, 22, 2, 23)
        if SLOT_0 >= 100000:
            CreateObject('suef_210_shot_add', -1)


@State
def suef_210_shot_add():
    sprite('null', 1)
    AddX(150000)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_210shot_add', -1)


@State
def suef_210_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        Hitstop(8)
        GroundedHitstunAnimation(19)
        AirHitstunAnimation(19)
        AirPushbackX(40000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(2400)
        PushbackX(12000)
        Floorslide(12)
        StarterRating(2)
        CancelIfPlayerHit(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('suef_210_hit', 101)
            AttackOff()
        GuardPoint_(1)
        setInvincible(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        GuardpointHitstop(0, 0)
        PretendNoGuardPointIfFail(1)

        def upon_GUARDPOINT_ACTIVATION():
            NoAttackDuringAction(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk6A', 33)
    sprite('null', 1)
    sprite('su210_def', 1)
    sprite('su210_atk', 3)


@State
def suef_210_hit():
    sprite('null', 1)
    AddX(-50000)
    CreateParticle('suef_210hit_b', -1)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_210hit', -1)


@State
def suef_211():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('vrsuef211_00', 3)
    CreateObject('suef_dust_large', 0)
    AddX(-104000)
    sprite('vrsuef211_01', 4)
    AddX(104000)
    AddX(-124000)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef211_02', 6)
    E0EAEffectPosition(0)


@State
def suef_211_2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
    sprite('vrsuef211_10', 5)
    AddX(-128000)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    sprite('vrsuef211_11', 5)
    sprite('vrsuef211_12', 2)


@State
def suef_211_foot():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RenderLayer(11)
        Eff3DEffect('suef_211rock.DIG', '')
        Size(600)
    sprite('null', 5)
    ParticleSize(1200)
    CallCustomizableParticle('suef_211foot', -1)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_211_foot2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RenderLayer(11)
        Eff3DEffect('suef_211rock.DIG', '')
        Size(900)
    sprite('null', 5)
    ParticleSize(1600)
    CallCustomizableParticle('suef_211foot', -1)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_231():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(-45000)
        AddY(5000)
    sprite('vrsuef231_00', 4)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef231_01', 4)
    sprite('vrsuef231_02', 4)


@State
def suef_251():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        SetZVal(-500)
    sprite('vrsuef251_00', 2)
    sprite('vrsuef251_01', 2)
    sprite('vrsuef251_particle', 1)
    Visibility(1)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)


@State
def suef_251_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_251claw.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(80000)
        AddY(180000)
        RotationAngle(17500)
        Size(750)
    sprite('null', 15)


@State
def suef_232():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        SetZVal(-500)
        AddX(72000)
        AddY(4000)
    sprite('vrsuef232_00', 5)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef232_01', 5)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    sprite('vrsuef232_02', 5)
    sprite('vrsuef232_03', 4)
    sprite('vrsuef232_04', 16)
    ConstantAlphaModifier(-16)
    E0EAEffectPosition(0)


@State
def suef_252():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('vrsuef252_00', 3)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef252_01', 5)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef252_02', 4)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    sprite('vrsuef252_03', 3)
    E0EAEffectPosition(0)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    sprite('vrsuef252_04', 3)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef252_05', 8)
    ConstantAlphaModifier(-32)


@State
def suef_212():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Normal()
        SetZVal(-500)
    sprite('vrsuef212_00', 3)
    sprite('vrsuef212_01', 3)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef212_02', 3)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef212_03', 3)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef212_04', 3)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    CreateObject('suef_dust_large', 2)
    sprite('vrsuef212_05', 3)
    sprite('vrsuef212_06', 3)
    sprite('vrsuef212_07', 3)


@State
def suef_235():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('null', 3)
    sprite('vrsuef235_01', 2)
    AddX(-88000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    sprite('vrsuef235_02', 2)
    CreateObject('suef_dust', 0)
    sprite('vrsuef235_03', 4)


@State
def suef_235_2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('null', 2)
    sprite('vrsuef235_11', 4)
    AddX(-100000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef235_12', 4)
    sprite('vrsuef235_13', 4)


@State
def suef_203():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        PaletteIndex(1)
    sprite('vrsuef203_00', 2)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef203_01', 4)
    sprite('vrsuef203_02', 3)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrsuef203_03', 8)
    ConstantAlphaModifier(-32)


@State
def suef_203_atk():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(-80000)
    sprite('vrsuef203_10', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    sprite('vrsuef203_11', 6)
    sprite('vrsuef203_12', 6)
    sprite('vrsuef203_13', 6)
    E0EAEffectPosition(0)
    IgnorePauses(0)


@State
def suef_233_claw_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_233claw.DIG', '')
        FaceSpawnLocation()
        AddX(-7000)
    sprite('vrsuef233_particle', 4)
    Visibility(1)
    CreateParticle('suef_233', 0)
    CreateParticle('suef_233b', 1)
    CreateParticle('suef_233b', 2)
    sprite('vrsuef233_particle', 1)
    CreateParticle('suef_233_2b', 3)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_233_2', 3)
    CreateParticle('suef_233', 0)
    CreateParticle('suef_233b', 1)
    CreateParticle('suef_233b', 2)
    sprite('vrsuef233_particle', 19)
    E0EAEffectPosition(0)
    CreateParticle('suef_233_2b', 4)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_233_2', 4)
    CreateParticle('suef_233_2b', 5)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_233_2', 5)


@State
def suef_233_claw2_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_233claw2.DIG', '')
        FaceSpawnLocation()
        AddX(35000)
    sprite('null', 8)
    sprite('null', 8)
    E0EAEffectPosition(0)


@State
def suef_253_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_253.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(90000)
        Size(1125)
    sprite('null', 8)
    AddRotationPerFrame(15000)
    SetScaleSpeed(25)
    CreateObject('suef_253_particle', -1)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_253_particle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
    sprite('null', 60)
    LinkParticle('suef_253dust')


@State
def suef_213():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        RenderLayer(7)
    sprite('vrsuef213_00', 3)
    AddX(-51000)
    AddX(10000)
    CreateObject('suef_dust', 0)
    sprite('vrsuef213_01', 2)
    AddX(51000)
    AddX(-97000)
    sprite('vrsuef213_01', 2)
    AddX(97000)
    AddX(-144000)
    CreateObject('suef_dust', 0)


@State
def suef_213_2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        RenderLayer(7)
    sprite('vrsuef213_10', 2)
    AddX(-160000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef213_11', 5)
    AddX(160000)
    AddX(-160000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)


@State
def suef_213_3d():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        Eff3DEffect('suef_213.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(-32000)
    sprite('vrsuef213_particle', 14)
    CreateParticle('suef_213stump_b', 0)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_213stump', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef213_particle', 6)
    E0EAEffectPosition(0)


@State
def suef_214():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('suef_214', -1)


@State
def suef_214ground():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        ParticleColorFromPalette(240, 240, 240)
        CallPrivateEffect('suef_214ground')
    sprite('null', 20)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_214ground_dust', -1)
    AlphaValue(0)
    ConstantAlphaModifier(64)
    sprite('null', 60)
    ConstantAlphaModifier(-16)


@State
def suef_214ground2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        ParticleColorFromPalette(242, 242, 242)
        CallPrivateEffect('suef_214aura')
        RandAddScale(-200, 100)
    if random_(2, 0, 50):
        gotoLabel(1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Flip()
    AlphaValue(0)
    ConstantAlphaModifier(25)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def suef_311():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
    sprite('vrsuef311', 6)
    AddX(-40000)
    Visibility(1)
    CreateObject('suef_311_3d', -1)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    sprite('vrsuef311', 6)
    CreateObject('suef_dust', 4)
    CreateObject('suef_dust', 5)
    CreateObject('suef_dust', 6)
    CreateObject('suef_dust', 7)


@State
def suef_311_3d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        Eff3DEffect('suef_311', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-42)


@State
def suef_312():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddY(-16000)
    sprite('vrsuef312_00', 6)
    sprite('vrsuef312_01', 6)


@State
def suef_313():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        PaletteIndex(1)
    sprite('null', 1)
    ParticleSize(950)
    CallCustomizableParticle('suef_313_b', -1)
    ParticleSize(950)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_313', -1)


@State
def suef_313_smoke():
    sprite('null', 3)
    CreateParticle('suef_313smoke', -1)
    CreateObject('suef_313_smoke1', -1)
    sprite('null', 3)
    CreateObject('suef_313_smoke2', -1)


@State
def suef_313_smoke1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(128)
        ContinueState(60)
        Eff3DEffect('suef_313smoke.DIG', '')
        AddX(-300000)
        SetScaleX(600)
        Flip()
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-4)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 32767)


@State
def suef_313_smoke2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(128)
        ContinueState(60)
        Eff3DEffect('suef_313smoke.DIG', '')
        AddX(-250000)
        SetScaleX(900)
        Flip()
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-4)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 32767)


@State
def suef_321():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
    sprite('vrsuef321', 8)
    Visibility(1)
    CreateObject('suef_321_3d', -1)
    CreateObject('suef_321_3d_r', -1)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    CreateObject('suef_dust', 4)
    CreateObject('suef_dust', 5)
    CreateObject('suef_dust', 6)
    CreateObject('suef_dust', 7)
    sprite('vrsuef321', 8)
    CreateObject('suef_dust', 8)
    CreateObject('suef_dust', 9)
    CreateObject('suef_dust', 10)
    CreateObject('suef_dust', 11)
    CreateObject('suef_dust', 12)
    CreateObject('suef_dust', 13)


@State
def suef_321_3d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        Eff3DEffect('suef_321', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(352000)
    sprite('null', 15)


@State
def suef_321_3d_r():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        E0EAEffectPosition(2)
        Eff3DEffect('suef_321', '')
        Flip()
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(352000)
    sprite('null', 15)


@State
def suef_331():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        AddY(64000)
    sprite('null', 1)
    CreateObject('suef_331_a', -1)
    CreateObject('suef_331_b', -1)


@State
def suef_331_a():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
    sprite('null', 3)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_331', -1)
    sprite('null', 3)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_331', -1)
    sprite('null', 3)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_331', -1)
    sprite('null', 3)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_331', -1)


@State
def suef_331_b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    sprite('null', 5)
    CreateParticle('suef_331b', -1)
    sprite('null', 5)
    CreateParticle('suef_331b', -1)
    sprite('null', 5)
    CreateParticle('suef_331b', -1)


@State
def suef_340_hold():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(2)
        PaletteIndex(1)
    label(0)
    sprite('vrsuef340_00', 3)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_dust340', 0)
    sprite('vrsuef340_01', 3)
    sprite('vrsuef340_02', 3)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_dust340', 0)
    sprite('vrsuef340_03', 3)
    gotoLabel(0)


@State
def suef_340():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(2)
        PaletteIndex(1)
    sprite('vrsuef340_10', 2)
    CreateObject('suef_dust_large', 0)
    sprite('vrsuef340_11', 4)
    AddX(-32000)
    sprite('vrsuef340_12', 3)
    AddX(0)
    CreateObject('suef_dust_large', 0)
    CreateObject('suef_dust_large', 1)
    sprite('vrsuef340_13', 3)
    AddX(-12000)
    CreateObject('suef_dust_large', 0)
    ParticleColorFromPalette(15, 15, 15)
    CallCustomizableParticle('suef_340ground', 1)
    CreateParticle('suef_340ground00', 1)
    sprite('vrsuef340_14', 3)
    AddX(-28000)


@State
def suef_340_rock():

    def upon_IMMEDIATE():
        Flip()
        Eff3DEffect('suef_406rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(11)
    sprite('null', 16)
    Size(500)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_400():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('vrsuef400_05', 3)
    CreateObject('suef_400_aura', 0)
    CreateObject('suef_400_particle', 0)
    label(0)
    sprite('vrsuef400_05', 3)
    gotoLabel(0)


@State
def suef_400_aura():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 32767)
    Eff3DEffect('suef_400aura.DIG', '')
    BlendMode_Normal()
    PaletteIndex(1)
    ColorFromPaletteIndex(240)


@State
def suef_400_aura3():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('suef_400aura3.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 2)


@State
def suef_400_aura2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        Eff3DEffect('suef_400aura2.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 4)
    ConstantAlphaModifier(-8)


@State
def suef_400_particle():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)

        def upon_56():
            DeleteObject(23)
    label(0)
    sprite('null', 2)
    CreateObject('suef_dust_front', -1)
    gotoLabel(0)


@State
def suef_400_particle2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Visibility(1)
    label(0)
    sprite('vrsuef400_05', 2)
    CallCustomizableParticle('suef_400dust', 0)
    CallCustomizableParticle('suef_400dash', -1)
    gotoLabel(0)


@State
def suef_400_claw():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_400claw', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        AddY(-64000)
        AddX(64000)
    sprite('null', 16)


@State
def suef_400_claw2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_400claw2', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Size(1250)
        AddX(-64000)
        AddY(-25000)
    sprite('null', 1)
    sprite('null', 3)
    sprite('null', 8)
    AddScaleSpeed(25)
    ConstantAlphaModifier(-32)


@State
def suef_401handaura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrsuef401_00', 2)
    CreateObject('suef_dust', 0)
    sprite('vrsuef401_01', 2)
    CreateObject('suef_dust', 0)
    sprite('vrsuef401_02', 2)
    CreateObject('suef_dust', 0)
    sprite('vrsuef401_03', 2)
    CreateObject('suef_dust', 0)
    sprite('vrsuef401_03_2', 2)
    sprite('vrsuef401_04', 1)
    CreateObject('suef_dust', 0)
    sprite('vrsuef401_particle', 1)
    Visibility(1)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)


@State
def suef_401():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1400)
        AttackP1(60)
        AttackP2(92)
        SameMoveProration(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackY(40000)
        HitAirUnblockable(3)
        AttackDirection(3)
        StarterRating(0)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('AntiAir', 32)

        def upon_56():
            E0EAEffectPosition(0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('su401_Atk', 4)
    ParticleLayer(6)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_401smoke', -1)
    CreateParticle('suef_401stone', -1)
    CreateObject('suef_401_swordaura', -1)
    CreateObject('suef_401_swordaura2', -1)
    CreateObject('suef_401_crack', -1)
    sprite('su401_AtkEx0', 4)
    sprite('su401_AtkEx1', 4)
    sprite('null', 20)


@State
def suef_401_SP():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
    sprite('null', 4)
    ParticleLayer(6)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_401smoke', -1)
    CreateParticle('suef_401stone', -1)
    CreateObject('suef_401_swordaura', -1)
    CreateObject('suef_401_swordaura2', -1)
    CreateObject('suef_401_crack', -1)
    sprite('null', 4)
    Size(1200)
    sprite('null', 4)
    Size(1500)
    sprite('null', 20)


@State
def suef_401_crack():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_406rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(13)
        Size(1250)
        AddX(48000)
    sprite('null', 16)
    sprite('null', 16)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-16)


@State
def suef_401_swordaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_401swordaura.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(7)
    sprite('null', 15)
    Size(1250)
    SetScaleSpeed(10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def suef_401_swordaura2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_401swordaura2.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(11)
    sprite('null', 15)
    Size(1250)
    SetScaleSpeed(10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def suef_402():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        uponSendToLabel(33, 1)
    sprite('vrsuef402_00', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef402_01', 3)
    AddX(-29000)
    CreateObject('suef_dust', 0)
    sprite('vrsuef402_02', 3)
    AddX(29000)
    AddX(-49000)
    sprite('vrsuef402_03', 2)
    AddX(49000)
    AddX(-92000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef402_04', 2)
    AddX(92000)
    AddX(-128000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    CreateObject('suef_dust', 4)
    sprite('vrsuef402_05', 2)
    AddX(128000)
    AddX(-148000)
    sprite('vrsuef402_06', 3)
    AddX(148000)
    AddX(-187000)
    CreateObject('suef_402_b', -1)
    sprite('vrsuef402_07', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    sprite('vrsuef402_08', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef402_09', 6)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef402_10', 6)
    CreateObject('suef_dust', 0)
    sprite('vrsuef402_11', 4)
    AddX(187000)
    AddX(-119000)
    ExitState()
    label(1)
    sprite('vrsuef402_00', 2)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef402_01', 4)
    AddX(-29000)
    CreateObject('suef_dust', 0)
    sprite('vrsuef402_02', 6)
    AddX(29000)
    AddX(-49000)
    sprite('vrsuef402_03', 2)
    AddX(49000)
    AddX(-92000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef402_04', 2)
    AddX(92000)
    AddX(-128000)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    CreateObject('suef_dust', 4)
    sprite('vrsuef402_05', 2)
    AddX(128000)
    AddX(-148000)
    sprite('vrsuef402_06', 3)
    AddX(148000)
    AddX(-187000)
    CreateObject('suef_402_b', -1)
    sprite('vrsuef402_07', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    sprite('vrsuef402_08', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef402_09', 6)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    sprite('vrsuef402_10', 6)
    CreateObject('suef_dust', 0)
    sprite('vrsuef402_11', 4)
    AddX(187000)
    AddX(-119000)


@State
def suef_402_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        SetZVal(-1000)
    sprite('vrsuef402_20', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)
    CreateObject('suef_dust', 4)
    CreateObject('suef_dust', 5)
    sprite('vrsuef402_21', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    CreateObject('suef_dust', 2)
    CreateObject('suef_dust', 3)


@State
def suef_403_camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)

        def upon_32():
            CameraControlEnable(0)
            DeleteObject(23)
    sprite('null', 30)


@State
def suef_403_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddX(25000)
        AddY(-15000)
    label(0)
    sprite('null', 4)
    DashEffects(104, 1, 0)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_403aura', -1)
    gotoLabel(0)


@State
def suef_403_hand():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(7)
    label(0)
    sprite('vrsuef403_00', 4)
    CreateObject('suef_dust_front', 0)
    sprite('vrsuef403_01', 4)
    sprite('vrsuef403_02', 4)
    gotoLabel(0)


@State
def suef_403_smash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(7)
        uponSendToLabel(33, 1)
    sprite('vrsuef403_10', 5)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    sprite('vrsuef403_20', 5)
    ParticleLayer(10)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_403smash', -1)
    sprite('vrsuef403_21', 5)
    ExitState()
    label(1)
    sprite('vrsuef403_10', 3)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    sprite('vrsuef403_20', 3)
    sprite('vrsuef403_21', 3)


@State
def suef_403_smoke():

    def upon_IMMEDIATE():
        AddX(768000)
        AddY(-32000)
    sprite('null', 6)
    CreateObject('suef_403_smoke1', -1)
    CreateObject('suef_403_smoke_b', -1)
    CreateObject('suef_403_smoke_b2', -1)
    CreateObject('suef_403_smoke_b3', -1)
    sprite('null', 6)
    CreateObject('suef_403_smoke2', -1)
    CreateObject('suef_403_smoke3', -1)
    sprite('null', 3)
    sprite('null', 6)
    CreateObject('suef_403_smoke4', -1)
    sprite('null', 6)
    CreateObject('suef_403_smoke5', -1)


@State
def suef_403_smoke1():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(6)
    sprite('null', 6)
    SetScaleSpeed(2)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke2():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(7)
    sprite('null', 6)
    SetScaleSpeed(2)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke3():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(700)
        SetScaleY(500)
        RenderLayer(8)
    sprite('null', 6)
    physicsXImpulse(-8000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    physicsXImpulse(-2000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke4():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(750)
        SetScaleY(280)
        AddX(-150000)
        RenderLayer(0)
    sprite('null', 6)
    physicsXImpulse(-5000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    physicsXImpulse(-2000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke5():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(425)
        SetScaleY(150)
        AddY(4000)
        AddX(-140000)
        RenderLayer(10)
    sprite('null', 6)
    physicsXImpulse(-4000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    physicsXImpulse(-2000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke_b():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke2.DIG', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(4000)
        AddX(-100000)
        RenderLayer(9)
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    physicsXImpulse(-8000)
    SetScaleXPerFrame(5)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke_b2():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke2.DIG', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(4000)
        AddX(-700000)
        RenderLayer(9)
        SetScaleX(500)
        SetScaleY(400)
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    physicsXImpulse(-2000)
    SetScaleXPerFrame(5)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_403_smoke_b3():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_403smoke2.DIG', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddY(4000)
        AddX(-45000)
        RenderLayer(9)
        SetScaleX(350)
        SetScaleY(700)
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    physicsXImpulse(-5000)
    SetScaleXPerFrame(5)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)


@State
def suef_404():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    label(0)
    sprite('null', 3)
    CreateObject('suef_404a', -1)
    CreateObject('suef_404b', -1)
    CommonSE('014_electric_ml')
    gotoLabel(0)


@State
def suef_404a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 3)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_404a')


@State
def suef_404b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 3)
    LinkParticle('suef_404b')


@State
def suef_405():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('null', 4)
    CreateObject('suef_405_ground', -1)
    CreateObject('suef_405_aura', -1)
    sprite('null', 4)
    CreateObject('suef_405_aura', -1)
    sprite('null', 4)
    CreateObject('suef_405_aura', -1)
    label(0)
    sprite('null', 4)
    CreateObject('suef_405_ground', -1)
    CreateObject('suef_405_aura', -1)
    sprite('null', 4)
    CreateObject('suef_405_aura', -1)
    sprite('null', 4)
    CreateObject('suef_405_aura', -1)
    gotoLabel(0)


@State
def suef_405_ground():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
    sprite('null', 60)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_405jimen')


@State
def suef_405_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
    sprite('null', 30)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_405aura')


@State
def suef_405_crack():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        Eff3DEffect('suef_405crack.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(11)
        AddX(50000)
    sprite('null', 32767)


@State
def suef_405kick():

    def upon_IMMEDIATE():
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)
        uponSendToLabel(54, 999)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AttackDefaults_SpecialProjectile()
        AttackP1(80)
        SameMoveProration(80)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        PushbackX(24800)
        Unknown9219(1)
        FatalCounter(1)

        def upon_33():
            AttackLevel_(3)
            Damage(900)
            AttackP2(89)
            Hitstop(7)
            AirUntechableTime(27)
            if SLOT_137:
                DamageMultiplier(80)

        def upon_34():
            AttackLevel_(4)
            Damage(1000)
            AttackP2(92)
            AirUntechableTime(29)
            GotoState('suef_405kick_Lv2')
            if SLOT_137:
                DamageMultiplier(80)

        def upon_35():
            AttackLevel_(5)
            Damage(1100)
            AttackP2(94)
            AirUntechableTime(31)
            GroundedHitstunAnimation(2)
            AirHitstunAnimation(13)
            CHStagger(51)
            CHCrumple(41)
            GuardCrush(100, 1)
            SetActionMark(481)
            GuardCrushHitstun(30)
            GotoState('suef_405kick_Lv3')
            if SLOT_137:
                DamageMultiplier(80)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AttackOff()
            if SLOT_2:
                if SLOT_IsOppAirborne:
                    GuardCrushHitstun(42)
            TriggerUponForState('Shot', 32)
    sprite('vrsuef405_10', 3)
    CreateObject('suef_405_rock', -1)
    sprite('vrsuef405_11', 3)
    CreateObject('suef_dust_front', 0)
    sprite('vrsuef405_12', 4)
    E0EAEffectPosition(0)
    DespawnEAEffect('suef_405_crack')
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    CreateObject('suef_dust_front', 3)
    CreateObject('suef_dust_front', 4)
    CreateObject('suef_dust_front', 5)
    sprite('vrsuef405_13', 3)
    ConstantAlphaModifier(-28)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    sprite('vrsuef405_14', 3)
    AddScaleSpeed(10)
    sprite('vrsuef405_15', 3)
    ExitState()
    label(999)
    sprite('null', 1)


@State
def suef_405kick_SP():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AddScaleY(300)
        AddScaleX(45)
    sprite('vrsuef405_10', 3)
    CreateObject('suef_405_rock', -1)
    sprite('vrsuef405_11', 3)
    CreateObject('suef_dust_front', 0)
    sprite('vrsuef405_12', 4)
    E0EAEffectPosition(0)
    DespawnEAEffect('suef_405_crack')
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    CreateObject('suef_dust_front', 3)
    CreateObject('suef_dust_front', 4)
    CreateObject('suef_dust_front', 5)
    sprite('vrsuef405_13', 3)
    ConstantAlphaModifier(-28)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    CreateObject('suef_dust_front', 2)
    sprite('vrsuef405_14', 3)
    AddScaleSpeed(10)
    sprite('vrsuef405_15', 3)


@State
def suef_405_rock():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        BlendMode_Normal()
        AddX(-100000)
    sprite('null', 3)
    CreateParticle('suef_405rock', -1)
    Eff3DEffect('suef_405rock.DIG', '')
    sprite('null', 3)
    CreateParticle('suef_405rock', -1)
    Eff3DEffect('suef_405rock2.DIG', '')
    sprite('null', 5)
    CreateParticle('suef_405rock2', -1)
    Eff3DEffect('suef_405rock3.DIG', '')
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_406_roll_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        Eff3DEffect('suef_406rolling.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AlphaValue(192)
        AddY(64000)
        AddRotationPerFrame(30000)
    label(0)
    sprite('null', 2)
    gotoLabel(0)


@State
def suef_406():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('null', 1)
    CreateObject('suef_406_3d', -1)
    CreateObject('suef_406_rock', -1)
    CreateObject('suef_406_crack', -1)


@State
def suef_406_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        Eff3DEffect('suef_406splash', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(7)
    sprite('null', 12)
    CreateParticle('suef_406', -1)
    AlphaValue(192)
    Size(500)
    SetScaleSpeedY(20)
    SetScaleXPerFrame(10)
    sprite('null', 3)
    ConstantAlphaModifier(-64)


@State
def suef_406_OD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)

        def upon_32():
            SetActionMark(1)
    sprite('null', 3)
    CreateObject('suef_406_OD_pt', -1)
    CreateObject('suef_406_OD_rock', -1)
    CreateObject('suef_406_crack', -1)
    sprite('null', 1)
    CreateObject('suef_406_OD_3d', -1)
    PrivateSE('suse_00')
    if SLOT_2:
        CreateObject('suef_406_Atk_Air', -1)
    else:
        CreateObject('suef_406_Atk', -1)


@State
def suef_406_SP():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)
    sprite('null', 3)
    CreateObject('suef_406_OD_pt', -1)
    CreateObject('suef_406_OD_rock', -1)
    CreateObject('suef_406_crack', -1)
    sprite('null', 1)
    CreateObject('suef_406_OD_3d', -1)


@State
def suef_406_Atk():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(840)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        AirUntechableTime(45)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(38000)
        Hitstop(8)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(3)
        CHStateIfCHStart(3)
        Visibility(1)
        TeleportToObject(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('MidAssault', 32)
        if SLOT_137:
            DamageMultiplier(80)
        NoDamageAction(1)
    sprite('su406_10ex00', 8)


@State
def suef_406_Atk_Air():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(660)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        AirUntechableTime(45)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Hitstop(8)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(3)
        CHStateIfCHStart(3)
        Visibility(1)
        TeleportToObject(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('AirMidAssault', 32)
        if SLOT_137:
            DamageMultiplier(80)
        NoDamageAction(1)
    sprite('su406_10ex00', 8)


@State
def suef_406_OD_3d():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_406splash_od', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(6)
        Size(500)
        AddX(-64000)
    sprite('null', 16)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_406_OD_pt():

    def upon_IMMEDIATE():
        CallPrivateEffect('suef_406dust_od')
        AddX(25000)
    sprite('null', 16)
    sprite('null', 8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_406_rock():

    def upon_IMMEDIATE():
        Flip()
        BlendMode_Normal()
        RenderLayer(11)
        Size(750)
    sprite('null', 8)
    Eff3DEffect('suef_406rock.DIG', '')
    sprite('null', 8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_406_OD_rock():

    def upon_IMMEDIATE():
        Flip()
        BlendMode_Normal()
        RenderLayer(11)
        Size(1250)
    sprite('null', 8)
    Eff3DEffect('suef_406rock.DIG', '')
    sprite('null', 8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_406_crack():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleLayer(12)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_406jimen', -1)
    CreateParticle('suef_406smoke', -1)


@State
def suef_407_jiware():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 3)
    CreateObject('suef_407_rock', -1)
    CreateObject('suef_407_aura', -1)
    CommonSE('019_quake_0')
    sprite('null', 3)
    CreateObject('suef_407_aura3', -1)
    gotoLabel(0)


@State
def suef_407_rock():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_407rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(11)
        AddX(100000)
    sprite('null', 8)
    CreateParticle('suef_407stone', -1)
    RandAddScale(-400, 400)
    sprite('null', 8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_407_aura():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_407aura.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RandAddScale(-500, 0)
        SetScaleSpeedY(15)
        SetScaleXPerFrame(10)
        DeviationX(384000, 128000)
        DeviationY(-50000, 0)
        IgnoreFinishStop(1)
    sprite('null', 12)
    sprite('null', 4)
    ConstantAlphaModifier(-64)
    CreateObject('suef_407_aura2', -1)


@State
def suef_407_aura2():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        Eff3DEffect('suef_407aura.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RandAddScale(-750, -500)
        SetScaleSpeedY(15)
        SetScaleXPerFrame(10)
        AbsoluteY(0)
        AddX(-320000)
    sprite('null', 12)
    sprite('null', 4)
    ConstantAlphaModifier(-64)


@State
def suef_407_aura3():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_407aura.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddScale(100)
        RandAddScale(0, -250)
        SetScaleSpeedY(15)
        SetScaleXPerFrame(10)
        AddX(384000)
        RenderLayer(11)
    sprite('null', 12)
    sprite('null', 4)
    ConstantAlphaModifier(-64)


@State
def suef_407_kick():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
    sprite('null', 5)
    CreateObject('suef_407_kick1', -1)
    CreateObject('suef_407_kick2', -1)
    CreateObject('suef_407_kick_rock', -1)
    sprite('null', 5)
    CreateObject('suef_407_kick2', -1)
    sprite('null', 5)
    CreateObject('suef_407_kick2', -1)


@State
def suef_407_kick1():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_407kick.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(128000)
        RenderLayer(11)
        SetScaleX(1250)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def suef_407_kick2():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_407kick2.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        DeviationX(256000, 0)
        DeviationY(-64000, -32000)
        RenderLayer(7)
        RandAddScale(-250, 0)
    sprite('null', 20)
    SetScaleSpeed(10)


@State
def suef_407_kick_rock():

    def upon_IMMEDIATE():
        Flip()
        Eff3DEffect('suef_407rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(6)
        AddX(0)
        AddY(16000)
        Size(1250)
    sprite('null', 8)
    sprite('null', 24)
    ConstantAlphaModifier(-10)


@State
def suef_430_sword():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        uponSendToLabel(32, 10)
    sprite('vrsuef430_00', 3)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)
    sprite('vrsuef430_01', 3)
    sprite('vrsuef430_02', 3)
    CreateObject('suef_dust_front', 0)
    sprite('suef430_03', 3)
    AddX(-69000)
    sprite('suef430_04', 3)
    sprite('suef430_05', 6)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_430sword', 0)
    sprite('suef430_06', 6)
    sprite('suef430_07', 6)
    label(1)
    sprite('suef430_05', 6)
    sprite('suef430_06', 6)
    sprite('suef430_07', 6)
    gotoLabel(1)
    label(10)
    sprite('suef430_08', 6)
    sprite('suef430_09', 6)
    sprite('suef430_10', 6)
    AddX(69000)
    AddX(-97000)
    sprite('suef430_11', 6)
    AddX(97000)
    AddX(-148000)
    sprite('suef430_12', 6)
    AddX(148000)
    AddX(-180000)
    sprite('vrsuef430_13', 6)
    sprite('vrsuef430_14', 1)
    sprite('vrsuef430_15', 1)
    sprite('vrsuef430_16', 6)
    sprite('vrsuef430_17', 6)
    RenderLayer(11)
    sprite('vrsuef430_18', 6)
    sprite('vrsuef430_19', 6)
    sprite('vrsuef430_20', 6)


@State
def suef_430_slash():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_430slash.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(1000)
        AddX(430000)
        AbsoluteY(200000)
    sprite('null', 29)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_430bg', -1)
    CreateParticle('suef_430bg', -1)


@State
def suef_430_bg():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_430bg.DIG', '')
        PaletteIndex(1)
        BlendMode_Sub()
        RenderLayer(1)
        SetScaleX(1000)
        SetPosXByScreenPer(50)
        AbsoluteY(200000)
    sprite('null', 20)
    SetScaleSpeedY(-50)
    AlphaValue(204)


@State
def suef_431_punch():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        SetZVal(10)
    sprite('vrsuef431_00', 3)
    AddX(21000)
    sprite('vrsuef431_01', 3)
    AddX(-21000)
    AddX(-98000)
    CreateObject('suef_dust', 0)
    sprite('vrsuef431_02', 3)
    AddX(98000)
    AddX(-188000)
    sprite('vrsuef431_03', 3)
    AddX(188000)
    AddX(-236000)
    CreateObject('suef_dust', 0)
    sprite('vrsuef431_04', 3)
    AddX(236000)
    AddX(-261000)
    sprite('vrsuef431_05', 3)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('vrsuef431_06', 3)
    CreateObject('suef_dust', 0)


@State
def suef_431_punch2():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
    sprite('null', 16)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_431punch')


@State
def suef_431_charge():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_431charge.DIG', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Size(1200)
    sprite('null', 16)
    AlphaValue(0)
    ConstantAlphaModifier(16)
    SetScaleSpeed(5)
    sprite('null', 8)
    sprite('null', 8)
    ConstantAlphaModifier(-32)


@State
def suef_431_ring():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('suef431_90', 6)
    AddX(-60000)
    sprite('suef431_91', 6)
    AddX(60000)
    AddX(-72000)


@State
def suef_431_beam():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ContinueState(100)
        AddY(150000)
        AddX(150000)
    sprite('null', 10)
    CreateObject('suef_431_beam0', -1)
    CreateObject('suef_431_beam1', -1)
    CreateObject('suef_431_beam2', -1)
    CreateObject('suef_431_ring2', -1)
    CreateObject('suef_431_ring3', -1)
    CreateObject('suef_431_wave', -1)
    CreateObject('suef_431_dome', -1)
    CreateObject('suef_431_rock', -1)
    CreateObject('suef_431_dome2', -1)
    label(0)
    sprite('null', 10)
    CreateObject('suef_431_dome', -1)
    CreateObject('suef_431_dome2', -1)
    CreateObject('suef_431_rock', -1)
    gotoLabel(0)


@State
def suef_431_beam0():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddX(55000)
        ContinueState(100)
    label(0)
    sprite('null', 6)
    PaletteIndex(1)
    ParticleLayer(8)
    CallCustomizableParticle('suef_431mouth_b', -1)
    ParticleLayer(7)
    CallCustomizableParticle('suef_431mouth_a', -1)
    ParticleLayer(6)
    CallCustomizableParticle('suef_431mouth_c', -1)
    ParticleLayer(11)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_431mouth_clr', -1)
    gotoLabel(0)


@State
def suef_431_beam1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_431beam1.DIG', '')
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        BlendMode_Normal()
        RenderLayer(12)
        AddX(-70000)
    sprite('null', 90)


@State
def suef_431_beam2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('suef_431beam2.DIG', '')
        RenderLayer(12)
        AddX(-70000)
        BlendMode_Add()
    sprite('null', 90)


@State
def suef_431_ring2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Add()
        Size(1100)
        AddX(350000)
        RenderLayer(10)
        CreateObject('suef_431_ring2b', -1)
    sprite('suef431_80', 20)
    SetScaleSpeedY(10)
    sprite('suef431_80', 30)
    ConstantAlphaModifier(-8)


@State
def suef_431_ring2b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnContact(2)
        PaletteIndex(1)
        BlendMode_Add()
        RenderLayer(12)
    sprite('suef431_80b', 50)


@State
def suef_431_ring3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Add()
        Size(2200)
        AddX(225000)
        RenderLayer(10)
        CreateObject('suef_431_ring3b', -1)
    sprite('suef431_80', 20)
    SetScaleSpeedY(10)
    sprite('suef431_80', 30)
    ConstantAlphaModifier(-8)


@State
def suef_431_ring3b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnContact(2)
        PaletteIndex(1)
        BlendMode_Add()
        RenderLayer(11)
    sprite('suef431_80b', 50)


@State
def suef_431_wave():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('suef_431wave.DIG', '')
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        BlendMode_Normal()
        AddX(100000)
        Size(650)
    sprite('null', 90)


@State
def suef_431_dome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('suef_431dome.DIG', '')
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        BlendMode_Normal()
        AbsoluteY(-50000)
        AddX(16000)
        AlphaValue(128)
    sprite('null', 30)
    physicsXImpulse(-16000)


@State
def suef_431_dome2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(-50000)
        AddX(64000)
    sprite('suef431_70', 30)
    physicsXImpulse(-16000)
    ConstantAlphaModifier(-8)


@State
def suef_431_rock():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
    sprite('null', 1)
    CreateParticle('suef_431rock00', -1)
    CreateParticle('suef_431rock01', -1)


@State
def suef_432_aura():

    def upon_IMMEDIATE():
        Flip()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('suef_432aura.DIG', '')
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        BlendMode_Normal()
    sprite('null', 20)
    Size(750)
    SetScaleY(500)
    SetScaleSpeed(10)
    SetScaleSpeedY(15)
    sprite('null', 10)


@State
def suef_432_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('suef_432aura2.DIG', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AbsoluteY(-20000)
    sprite('null', 5)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_432aura_smoke', -1)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    Size(250)
    SetScaleSpeed(100)
    SetScaleSpeedY(300)
    sprite('null', 5)
    SetScaleSpeed(25)
    SetScaleSpeedY(-60)
    sprite('null', 5)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_432_auradust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        ContinueState(20)
    label(0)
    sprite('null', 3)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_432aura_dust', -1)
    gotoLabel(0)


@State
def suef_440():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        PaletteIndex(1)
        Flip()
        AddX(48000)
    sprite('null', 1)
    ParticleSize(600)
    CallCustomizableParticle('suef_313_b', -1)
    ParticleSize(600)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_313', -1)


@State
def suef_440_smoke():
    sprite('null', 3)
    CreateParticle('suef_313smoke', -1)
    CreateObject('suef_440_smoke1', -1)
    sprite('null', 3)
    CreateObject('suef_440_smoke2', -1)


@State
def suef_440_smoke1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(128)
        ContinueState(60)
        Eff3DEffect('suef_313smoke.DIG', '')
        AddX(250000)
        SetScaleX(500)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-4)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 32767)


@State
def suef_440_smoke2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(128)
        ContinueState(60)
        Eff3DEffect('suef_313smoke.DIG', '')
        AddX(200000)
        SetScaleX(750)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 6)
    ConstantAlphaModifier(-4)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 32767)


@State
def suef_440_kick():
    sprite('null', 5)
    CreateObject('suef_440_kick_rock', -1)
    CreateObject('suef_440_kick1', -1)
    CreateObject('suef_440_kick2', -1)
    sprite('null', 5)
    CreateObject('suef_440_kick2', -1)
    sprite('null', 5)
    CreateObject('suef_440_kick2', -1)


@State
def suef_440_kick1():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_440kick.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(128000)
        RenderLayer(11)
        Size(500)
    sprite('null', 50)
    sprite('null', 32)
    ConstantAlphaModifier(-8)


@State
def suef_440_kick2():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_407kick2.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        DeviationX(256000, 0)
        DeviationY(-64000, -32000)
        RenderLayer(7)
        RandAddScale(-250, 0)
    sprite('null', 20)
    SetScaleSpeed(10)


@State
def suef_440_kick_rock():

    def upon_IMMEDIATE():
        Flip()
        Eff3DEffect('suef_407rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(6)
        AddX(50000)
        AddY(16000)
        SetScaleX(1600)
        SetScaleY(1200)
    sprite('null', 8)
    CreateParticle('suef_407stone', -1)
    sprite('null', 24)
    ConstantAlphaModifier(-10)


@State
def suef_440_rolling():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(2)
        Eff3DEffect('suef_406rolling.DIG', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AlphaValue(192)
        AddY(64000)
        AddRotationPerFrame(30000)
        PaletteIndex(1)
        ParticleColorFromPalette(240, 240, 240)
        ParticleLayer(11)
        CallPrivateEffect('suef_440rolling')
        uponSendToLabel(32, 1)
    sprite('null', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('null', 32767)
    AlphaValue(191)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 30)
    ConstantAlphaModifier(-9)


@State
def suef_440_fireaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    label(0)
    sprite('null', 3)
    CreateObject('suef_440_fireaura_pt', -1)
    gotoLabel(0)


@State
def suef_440_fireaura_pt():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
    sprite('null', 24)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_440aura', -1)


@State
def suef_440_finish():
    sprite('null', 30)
    CreateObject('suef_440_crack', -1)
    CreateObject('suef_440_shock', -1)
    CreateObject('suef_440_tornado', -1)
    sprite('null', 1)
    DespawnEAEffect('suef_440_fireaura')


@State
def suef_440_finish_sp():
    sprite('null', 30)
    CreateObject('suef_440_crack_sp', -1)
    CreateObject('suef_440_shock', -1)
    CreateObject('suef_440_wave', -1)
    CreateObject('suef_440_tornado', -1)
    CreateObject('suef_440_tornado2', -1)
    sprite('null', 1)
    DespawnEAEffect('suef_440_fireaura')


@State
def suef_440_crack():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('suef_406rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(11)
        SetScaleX(1500)
        SetScaleY(1250)
        AddX(48000)
        PaletteIndex(1)
    sprite('null', 40)
    CreateObject('suef_440_rock', -1)
    CreateObject('suef_440_aurasmoke', -1)
    sprite('null', 24)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-10)


@State
def suef_440_crack_sp():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('suef_406rock.DIG', '')
        BlendMode_Normal()
        RenderLayer(11)
        SetScaleX(1500)
        SetScaleY(1250)
        AddX(48000)
        PaletteIndex(1)
    sprite('null', 60)
    CreateObject('suef_440_rock', -1)
    CreateObject('suef_440_aurasmoke', -1)
    sprite('null', 40)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-6)


@State
def suef_440_rock():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 90)
    LinkParticle('suef_440rock')


@State
def suef_440_aurasmoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        AddX(-25000)
    sprite('null', 90)
    ParticleColorFromPalette(240, 240, 240)
    ParticleLayer(10)
    CallPrivateEffect('suef_440smoke')
    CreateParticle('suef_401stone', -1)


@State
def suef_440_shock():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(25000)
    sprite('null', 1)
    CreateObject('suef_440_shock1', -1)
    CreateObject('suef_440_shock2', -1)


@State
def suef_440_shock1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
    sprite('null', 60)
    ParticleLayer(12)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('suef_440finish')


@State
def suef_440_shock2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 60)
    ParticleLayer(12)
    CallPrivateEffect('suef_440finish2')


@State
def suef_440_tornado():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Eff3DEffect('suef_432aura.DIG', '')
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        BlendMode_Normal()
    sprite('null', 20)
    Size(1000)
    SetScaleY(750)
    SetScaleSpeed(10)
    SetScaleSpeedY(15)
    sprite('null', 10)


@State
def suef_440_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('suef_432aura2.DIG', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AbsoluteY(-20000)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    Size(400)
    SetScaleSpeed(100)
    sprite('null', 40)
    SetScaleSpeed(0)
    SetScaleSpeedY(-35)
    ConstantAlphaModifier(-6)


@State
def suef_440_wave():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(25000)
    sprite('null', 1)
    CreateObject('suef_440_wave1', -1)
    CreateObject('suef_440_wave2', -1)
    CreateObject('suef_440_wave3', -1)


@State
def suef_440_wave1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('suef_440wave', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(750)
        RenderLayer(14)
    sprite('null', 60)
    sprite('null', 40)
    ConstantAlphaModifier(-6)


@State
def suef_440_wave2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('suef_440wave2', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        SetScaleX(750)
        RenderLayer(6)
    sprite('null', 60)
    sprite('null', 40)
    ConstantAlphaModifier(-6)


@State
def suef_440_wave3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('suef_440wave3', '')
        BlendMode_Normal()
        SetScaleX(750)
        RenderLayer(13)
        AlphaValue(192)
    sprite('null', 60)
    sprite('null', 40)
    ConstantAlphaModifier(-4)


@State
def AstralHeat_Camera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        uponSendToLabel(33, 1)
        uponSendToLabel(41, 9)
    sprite('null', 32767)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    sprite('null', 15)
    AddY(100000)
    AddX(50000)
    sprite('null', 15)
    AddY(-50000)
    AddX(-50000)
    sprite('null', 15)
    AddY(50000)
    AddX(50000)
    sprite('null', 15)
    AddY(-50000)
    AddX(-50000)
    sprite('null', 1)
    Unknown20008(1)
    CameraPosition(1150)
    AbsoluteY(400000)
    sprite('null', 10)
    AddY(-200000)
    AddX(-200000)
    sprite('null', 10)
    AddY(200000)
    AddX(200000)
    sprite('null', 10)
    AddY(-200000)
    AddX(-200000)
    sprite('null', 10)
    AddY(200000)
    AddX(200000)
    sprite('null', 10)
    AddY(-200000)
    AddX(-200000)
    sprite('null', 1)
    CameraPosition(1300)
    Unknown20008(1)
    AbsoluteY(300000)
    AddX(200000)
    label(100)
    sprite('null', 5)
    AddY(-200000)
    AddX(-100000)
    sprite('null', 5)
    AddY(200000)
    AddX(-100000)
    sprite('null', 5)
    AddY(-200000)
    AddX(100000)
    sprite('null', 5)
    AddY(200000)
    AddX(100000)
    loopRest()
    gotoLabel(100)
    sprite('null', 32767)
    label(9)
    sprite('null', 1)
    CameraPosition(1000)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    Unknown20008(0)


@State
def suef_450_hand():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        RenderLayer(1)
    sprite('suef450_00', 3)
    AddX(-64000)
    sprite('suef450_01', 3)
    AddX(64000)
    AddX(-108000)
    label(0)
    sprite('suef450_02', 3)
    CreateParticle('suef_450hand_b', 0)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 0)
    sprite('suef450_03', 3)
    CreateParticle('suef_450handaura_b', 0)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 0)
    sprite('suef450_04', 3)
    CreateParticle('suef_450handaura_b', 0)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 0)
    gotoLabel(0)


@State
def suef_450_atk1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        BlendMode_Normal()
        RenderLayer(7)
    sprite('suef450_05', 3)
    AddX(-108000)
    sprite('suef450_06', 3)
    ParticleLayer(6)
    CallCustomizableParticle('suef_450handaura_b', 1)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 1)
    ParticleLayer(6)
    CallCustomizableParticle('suef_450handaura_b', 2)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 2)
    ParticleLayer(6)
    CallCustomizableParticle('suef_450handaura_b', 3)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450hand', 3)
    ParticleLayer(6)
    CallCustomizableParticle('suef_450splash_b', 0)
    ParticleLayer(6)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450splash', 0)
    CreateObject('suef_450_atk1_3d', -1)
    sprite('suef450_07', 6)
    sprite('suef450_08', 3)


@State
def suef_450_atk1_3d():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Eff3DEffect('suef_450splash.DIG', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        RenderLayer(7)
        AddX(128000)
    sprite('null', 12)
    SetScaleSpeed(20)
    sprite('null', 8)
    ConstantAlphaModifier(-32)


@State
def suef_450_atk2():
    sprite('null', 1)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450splash2', -1)
    BlendMode_Normal()
    ColorFromPaletteIndex(240)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        XSpeed2(4000, 0)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        Flip()
        XSpeed2(4000, 0)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        RotationAngle(-50000)
        XSpeed2(4000, 0)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        Flip()
        RotationAngle(-50000)
        XSpeed2(4000, 0)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        RotationAngle(50000)
        XSpeed2(4000, 0)
    CreateObject('suef_450_atk2_3d', -1)

    def RunOnObject_1():
        Flip()
        RotationAngle(50000)
        XSpeed2(4000, 0)


@State
def suef_450_atk2_3d():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_450splash2.DIG', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        AddScaleSpeedY(-50)
        AddScaleSpeedX(50)
        AddScale(500)
    sprite('null', 32)


@State
def suef_450_sword():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        AddX(32000)
        AddY(19000)
        uponSendToLabel(32, 10)
        RenderLayer(7)
    sprite('suef450_15', 6)
    AddX(-100000)
    sprite('suef450_16', 8)
    AddX(192000)
    sprite('suef450_17', 8)
    sprite('suef450_18', 8)
    sprite('suef450_19', 8)
    sprite('suef450_20', 6)
    sprite('suef450_21', 6)
    AddX(-192000)
    AddX(256000)
    AddY(-80000)
    sprite('suef450_22', 6)
    AddX(-256000)
    AddY(80000)
    AddX(64000)
    AddY(-80000)
    sprite('suef450_23', 6)
    AddX(-64000)
    AddY(80000)
    AddX(-192000)
    AddY(-80000)
    sprite('suef450_24add', 3)
    AddX(192000)
    sprite('suef450_25', 3)
    AddY(80000)
    sprite('suef450_26', 3)
    label(1)
    sprite('suef450_24', 3)
    sprite('suef450_25', 3)
    sprite('suef450_26', 3)
    gotoLabel(1)
    label(10)
    sprite('suef450_27', 3)
    sprite('suef450_28', 3)
    sprite('suef450_29', 3)
    AddX(272000)
    AddY(-64000)
    sprite('suef450_30', 3)
    RenderLayer(6)
    AddY(64000)
    AddY(-128000)
    sprite('suef450_31', 3)
    sprite('suef450_32', 3)
    label(0)
    sprite('suef450_30', 3)
    sprite('suef450_31', 3)
    sprite('suef450_32', 3)
    gotoLabel(0)


@State
def suef_450_swordaura():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450swordaura.DIG', '')
        AddX(95000)
        AddY(400000)
        RotationAngle(-44000)
        RenderLayer(6)
        uponSendToLabel(32, 0)
    sprite('null', 15)
    AlphaValue(0)
    ConstantAlphaModifier(14)
    sprite('null', 32767)
    AlphaValue(220)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 3)
    AddY(75000)
    AddX(-75000)
    Size(2000)
    RotationAngle(-20000)


@State
def suef_450_bg():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(100)
        PaletteIndex(1)
        ParticleLayer(0)
        ParticleColorFromPalette(242, 242, 242)
        CallPrivateEffect('suef_450bg')
    sprite('null', 90)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('null', 32767)
    AlphaValue(255)
    ConstantAlphaModifier(0)


@State
def suef_450_shake():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 10)
        uponSendToLabel(33, 20)
        uponSendToLabel(34, 30)
    label(0)
    sprite('null', 5)
    ScreenShake(2000, 2000)
    gotoLabel(0)
    label(10)
    sprite('null', 5)
    ScreenShake(5500, 5500)
    gotoLabel(10)
    label(20)
    sprite('null', 5)
    ScreenShake(15000, 15000)
    gotoLabel(20)
    label(30)
    sprite('null', 5)
    ScreenShake(25000, 25000)
    gotoLabel(30)


@State
def suef_450_storm_group():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            TriggerUponForState('suef_450_storm', 32)
            TriggerUponForState('suef_450_storm_b', 32)
    sprite('null', 4)
    CreateObject('suef_450_stormdust', -1)
    sprite('null', 32767)
    CreateObject('suef_450_storm', -1)
    CreateObject('suef_450_storm_b', -1)


@State
def suef_450_stormdust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 50)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_450stormdust', -1)
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    gotoLabel(0)


@State
def suef_450_storm():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450storm.DIG', '')
        uponSendToLabel(32, 0)
    sprite('null', 30)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('null', 32767)
    AlphaValue(128)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 4)
    ConstantAlphaModifier(-32)


@State
def suef_450_storm_b():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450storm2.DIG', '')
        RenderLayer(2)
        uponSendToLabel(32, 0)
    sprite('null', 30)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('null', 32767)
    AlphaValue(128)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 4)
    ConstantAlphaModifier(-32)


@State
def suef_450_swordaura2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450swordaura2.DIG', '')
        RenderLayer(6)
        AddX(500000)
        AddY(-115000)
    sprite('null', 32767)


@State
def suef_450_storm2_group():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 10)
        uponSendToLabel(33, 20)
        CreateObject('suef_450_stormdust2', -1)
    label(0)
    sprite('null', 5)
    CreateObject('suef_450_storm2', -1)
    CreateObject('suef_450_storm2_b', -1)
    CommonSE('019_quake_0')
    gotoLabel(0)
    label(10)
    sprite('null', 4)
    CreateObject('suef_450_storm2', -1)
    CreateObject('suef_450_storm2_b', -1)
    CommonSE('019_quake_0')
    gotoLabel(10)
    label(20)
    sprite('null', 3)
    CreateObject('suef_450_storm2', -1)
    CreateObject('suef_450_storm2_b', -1)
    gotoLabel(20)


@State
def suef_450_stormdust2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 30)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_450stormdust2', -1)
    gotoLabel(0)


@State
def suef_450_storm2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450storm3.DIG', '')
        DeviationX(-256000, 256000)
        DeviationY(-128000, 128000)
        RandRotationAngle()
        RenderLayer(7)
    sprite('null', 15)
    SetScaleX(200)
    SetScaleY(1600)
    SetScaleSpeed(100)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_450_storm2_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450storm3.DIG', '')
        DeviationX(-256000, 256000)
        DeviationY(-128000, 128000)
        RandRotationAngle()
        RenderLayer(15)
    sprite('null', 15)
    SetScaleX(200)
    SetScaleY(1600)
    SetScaleSpeed(100)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def suef_450_storm3_group():
    sprite('null', 10)
    CreateObject('suef_450_storm3_a', -1)
    sprite('null', 10)
    CreateObject('suef_450_storm3_b', -1)
    sprite('null', 10)
    CreateObject('suef_450_storm3_c', -1)
    sprite('null', 5)
    CreateObject('suef_450_storm3_d', -1)
    sprite('null', 5)
    CreateObject('suef_450_storm3_e', -1)


@State
def suef_450_storm3_a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        Eff3DEffect('suef_450storm4.DIG', '')
        AddX(0)
        RotationAngle(-15000)
        SetScaleX(4000)
        SetScaleY(5000)
        RenderLayer(8)
        SetScaleSpeed(100)
    sprite('null', 32767)


@State
def suef_450_storm3_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(0)
        AddY(150000)
        RotationAngle(80000)
        SetScaleX(3000)
        SetScaleY(5000)
        Eff3DEffect('suef_450storm4.DIG', '')
        RenderLayer(8)
        SetScaleSpeed(100)
    sprite('null', 32767)


@State
def suef_450_storm3_c():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(500000)
        AddY(0)
        RotationAngle(10000)
        SetScaleX(5000)
        SetScaleY(5000)
        Eff3DEffect('suef_450storm4.DIG', '')
        RenderLayer(9)
        SetScaleSpeed(100)
    sprite('null', 32767)


@State
def suef_450_storm3_d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(-400000)
        AddY(0)
        SetScaleX(6000)
        SetScaleY(6000)
        RotationAngle(-10000)
        Eff3DEffect('suef_450storm4.DIG', '')
        RenderLayer(10)
        SetScaleSpeed(100)
    sprite('null', 32767)


@State
def suef_450_storm3_e():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        AddX(0)
        AddY(0)
        SetScaleX(10000)
        SetScaleY(10000)
        RotationAngle(0)
        Eff3DEffect('suef_450storm4.DIG', '')
        RenderLayer(1)
    sprite('null', 9)
    sprite('null', 1)


@State
def suef_450_end():
    sprite('null', 32767)
    CreateObject('suef_450_end_bg', -1)
    CreateObject('suef_450_end_perticle', -1)


@State
def suef_450_end_bg():

    def upon_IMMEDIATE():
        FaceLeft()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('suef_astralmoya', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(2)
    sprite('null', 32767)


@State
def suef_450_end_perticle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        SetPosXByScreenPer(-15)
        SetPosYByScreenPer(100)
    sprite('null', 32767)
    PaletteIndex(1)
    ParticleLayer(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450end_pt', -1)


@State
def suef_450_HitEff():

    def upon_IMMEDIATE():
        DeviationX(-600000, 600000)
        DeviationY(-50000, 500000)
        ScreenShake(5000, 5000)
    sprite('null', 1)
    ParticleRandomRotation()
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmz', 0)


@State
def su600_ha():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(4)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RenderLayer(14)
        uponSendToLabel(32, 0)
    sprite('su600_ha', 32767)
    label(0)
    sprite('su600_ha', 90)
    ColorTransition(4278190080, 30)
    CreateObject('suef_600_ground', -1)
    CreateObject('suef_600_smoke_ha', -1)
    CreateObject('suef_60_denki_ha', -1)
    sprite('su600_ha', 90)
    ConstantAlphaModifier(-2)


@State
def suef_60_denki_ha():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddX(-48000)
        AddY(256000)
    sprite('null', 60)
    PaletteIndex(1)
    ParticleLayer(13)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('suef_600denki')
    CommonSE('022_magiccircle_c')
    sprite('null', 60)
    ConstantAlphaModifier(-10)


@State
def suef_600_smoke_ha():
    label(0)
    sprite('null', 3)
    ParticleLayer(15)
    CallCustomizableParticle('suef_600smoke', -1)
    gotoLabel(0)


@State
def suef_600_ground():
    label(0)
    sprite('null', 12)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_600dust', -1)
    CreateParticle('suef_600ground', -1)
    gotoLabel(0)


@State
def su600_tm():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(5)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RenderLayer(11)
        uponSendToLabel(32, 0)
    sprite('su600_tm610', 32767)
    label(0)
    sprite('su600_tm00', 8)
    CreateObject('suef_600_aura', -1)
    CreateObject('suef_600_dust_tm', -1)
    CommonSE('014_electric_sl')
    sprite('su600_tm01', 8)
    CommonSE('014_electric_ll')
    sprite('su600_tm02', 8)
    sprite('su600_tm03', 4)
    CreateObject('suef_600_denki_tm', -1)
    CreateObject('suef_600_smoke_tm', -1)
    CommonSE('014_electric_l')
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    CommonSE('014_electric_m')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    CommonSE('014_electric_ml')
    ColorTransition(4278190080, 30)
    ForceBloomMaskOn(0)
    sprite('su600_tm05', 4)
    sprite('su600_tm03', 4)
    CommonSE('014_electric_s')
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    CommonSE('014_electric_sl')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    CommonSE('014_electric_ll')
    sprite('su600_tm05', 4)
    sprite('su600_tm03', 4)
    CommonSE('014_electric_l')
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    CommonSE('014_electric_ml')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    CommonSE('014_electric_m')
    sprite('su600_tm05', 4)
    sprite('su600_tm03', 4)
    CommonSE('014_electric_sl')
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    ConstantAlphaModifier(-4)
    CommonSE('014_electric_s')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    CommonSE('014_electric_m')
    sprite('su600_tm05', 4)
    sprite('su600_tm03', 4)
    CommonSE('014_electric_ml')
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    CommonSE('014_electric_s')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    CommonSE('014_electric_ll')
    CommonSE('015_blaze_2')
    sprite('su600_tm05', 4)
    CommonSE('016_explode_0')
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    sprite('su600_tm03', 4)
    sprite('su600_tm04', 4)
    sprite('su600_tm05', 4)
    DespawnEAEffect('suef_600_smoke_ha')
    DespawnEAEffect('suef_600_smoke_tm')
    DespawnEAEffect('suef_600_ground')


@State
def suef_600_denki_tm():

    def upon_IMMEDIATE():
        AddX(30000)
        AddY(256000)
    sprite('null', 90)
    PaletteIndex(1)
    ParticleLayer(10)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('suef_600denki')
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def suef_600_smoke_tm():

    def upon_IMMEDIATE():
        AddX(100000)
    label(0)
    sprite('null', 3)
    ParticleLayer(14)
    CallCustomizableParticle('suef_600smoke2', -1)
    gotoLabel(0)


@State
def suef_600_aura():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_600aura.DIG', '')
        BlendMode_Sub()
    sprite('null', 32)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 60)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 90)
    ConstantAlphaModifier(-3)


@State
def suef_600_dust_tm():
    sprite('null', 32)
    AddY(125000)
    AddX(125000)
    ParticleLayer(8)
    CallCustomizableParticle('suef_600dust_tm', -1)


@State
def suef_600():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RenderLayer(13)
    sprite('suef600_10', 24)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    sprite('suef600_11', 8)
    sprite('suef600_12', 8)


@State
def suef_600_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        uponSendToLabel(32, 1)
    sprite('suef600_50', 6)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('suef600_51', 6)
    sprite('suef600_52', 6)
    label(0)
    sprite('suef600_50', 6)
    sprite('suef600_51', 6)
    sprite('suef600_52', 6)
    gotoLabel(0)
    label(1)
    sprite('suef600_53', 10)


@State
def suef_600_splash():

    def upon_IMMEDIATE():
        AddY(128000)
    sprite('null', 16)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_600splash', -1)
    CreateParticle('suef_600splash2', -1)


@State
def suef_601():
    CreateObject('suef_601_aura', -1)
    CreateObject('suef_601_dust', -1)
    CreateObject('suef_601_stone', -1)
    CreateObject('suef_601_crack', -1)
    CreateObject('suef_601_wave', -1)
    CreateObject('suef_601_wave2', -1)
    CreateObject('suef_601_screen', -1)


@State
def suef_601_aura():

    def upon_IMMEDIATE():
        ContinueState(60)
        PaletteIndex(1)
    label(0)
    sprite('null', 2)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_601aura', -1)
    gotoLabel(0)


@State
def suef_601_stone():

    def upon_IMMEDIATE():
        ContinueState(25)
    label(0)
    sprite('null', 1)
    CreateParticle('suef_601stone2', -1)
    gotoLabel(0)


@State
def suef_601_dust():

    def upon_IMMEDIATE():
        ContinueState(90)
    label(0)
    sprite('null', 1)
    CallCustomizableParticle('suef_601dust', -1)
    gotoLabel(0)


@State
def suef_601_bloom():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        Unknown23122(241)
    label(0)
    sprite('suef020_00', 4)
    sprite('suef020_01', 4)
    gotoLabel(0)


@State
def suef_601_bloom2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        Unknown23122(242)
    label(0)
    sprite('suef020_07', 5)
    sprite('suef020_08', 5)
    gotoLabel(0)


@State
def suef_601_bloom_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Add()
        PaletteIndex(1)
        ParticleLayer(12)
        ParticleColorFromPalette(242, 242, 242)
        CallPrivateEffect('suef_601bloom')
        AlphaValue(128)
        AddY(290000)
        Size(1250)
    sprite('null', 60)
    sprite('null', 10)
    sprite('null', 60)
    ConstantAlphaModifier(-4)


@State
def suef_601_wave():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_601wave', '')
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
        RenderLayer(14)
    sprite('null', 60)
    sprite('null', 60)
    ConstantAlphaModifier(-4)


@State
def suef_601_wave2():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_601wave2', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 30)
    sprite('null', 60)
    ConstantAlphaModifier(-4)


@State
def suef_601_screen():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        RenderLayer(15)
        AlphaValue(0)
    sprite('suef601_screen', 60)
    sprite('suef601_screen', 60)
    ConstantAlphaModifier(-4)


@State
def suef_601_crack():

    def upon_IMMEDIATE():
        Eff3DEffect('suef_601rock.DIG', '')
        BlendMode_Normal()
        Size(1500)
        AddX(50000)
    sprite('null', 15)
    CreateParticle('suef_601stone', -1)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallCustomizableParticle('suef_450flash', -1)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def suef_610_soul():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        PaletteIndex(2)
        EffectPosition(22, 100)
        RenderLayer(1)
        uponSendToLabel(32, 0)
    sprite('suef610_00', 12)
    AbsoluteY(64000)
    sprite('suef610_01', 6)
    sprite('suef610_02', 6)
    CreateParticle('suef_610c', -1)
    PrivateSE('suse_09')
    sprite('suef610_03', 4)
    AbsoluteY(320000)
    sprite('suef610_04', 4)
    sprite('suef610_05', 4)
    label(1)
    sprite('suef610_03', 4)
    sprite('suef610_04', 4)
    sprite('suef610_05', 4)
    gotoLabel(1)
    label(0)
    sprite('suef610_06', 8)


@State
def suef_610_soul2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        PaletteIndex(2)
        uponSendToLabel(32, 1)
    sprite('suef610_07', 6)
    AddX(256000)
    CommonSE('015_blaze_0')
    sprite('suef610_08', 7)
    AddX(-256000)
    sprite('suef610_09', 7)
    CreateParticle('suef_610b', 0)
    sprite('suef610_10', 8)
    sprite('null', 12)
    sprite('null', 6)
    sprite('null', 6)
    sprite('suef610_13', 6)
    label(0)
    sprite('suef610_14', 6)
    sprite('suef610_15', 6)
    sprite('suef610_16', 6)
    gotoLabel(0)
    label(1)
    sprite('suef610_17', 6)
    sprite('suef610_18', 6)
    sprite('suef610_19', 6)
    sprite('suef610_20', 4)
    CreateParticle('suef_610', 0)
    sprite('suef610_21', 4)
    sprite('suef610_22', 4)


@State
def suef_611():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('suef611_01', 6)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_02', 6)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_03', 6)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_04', 7)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_05', 7)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_06', 7)
    CreateObject('suef_dust', 0)
    CreateObject('suef_dust', 1)
    sprite('suef611_07', 5)
    CreateObject('suef_dust_front', 0)
    CreateObject('suef_dust_front', 1)


@State
def suef_611_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        RenderLayer(9)
    sprite('suef611_08', 6)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_611', 0)
    CreateParticle('suef_611_b', 0)
    label(0)
    sprite('suef611_09', 6)
    CreateObject('suef_611_dust', 0)
    CreateObject('suef_611_dust', 1)
    CreateObject('suef_611_dust', 2)
    sprite('suef611_10', 6)
    sprite('suef611_11', 6)
    gotoLabel(0)


@State
def suef_611_dust():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
    sprite('null', 1)
    ParticleColorFromPalette(240, 240, 240)
    CallCustomizableParticle('suef_611sword', -1)


@State
def suef_611_ah():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        RenderLayer(9)
    label(0)
    sprite('suef611_09', 6)
    CreateObject('suef_611_dust', 0)
    CreateObject('suef_611_dust', 1)
    CreateObject('suef_611_dust', 2)
    sprite('suef611_10', 6)
    sprite('suef611_11', 6)
    gotoLabel(0)


@State
def suef_001():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 100)
    CreateObject('suef_001_dummy', -1)
    CallPrivateEffect('suef_001dust@')


@State
def suef_001_dummy():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
    sprite('vrsuef001_dummy', 4)
    CreateObject('suef_001_aura', 0)
    sprite('vrsuef001_dummy', 4)
    CreateObject('suef_001_aura2', 1)

    def RunOnObject_1():
        Flip()
    sprite('vrsuef001_dummy', 4)
    CreateObject('suef_001_aura', 2)

    def RunOnObject_1():
        Flip()
    sprite('vrsuef001_dummy', 4)
    CreateObject('suef_001_aura', 3)
    sprite('vrsuef001_dummy', 4)
    CreateObject('suef_001_aura2', 4)

    def RunOnObject_1():
        Flip()
    CreateObject('suef_001_aura2', 5)


@State
def suef_001_aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        Eff3DEffect('suef_001aura.DIG', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(241)
        RenderLayer(7)
    sprite('null', 45)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_001_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        Eff3DEffect('suef_001aura2.DIG', '')
        PaletteIndex(1)
        BlendMode_Normal()
        ColorFromPaletteIndex(241)
        RenderLayer(7)
    sprite('null', 45)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 16)
    ConstantAlphaModifier(-16)


@State
def suef_001_blm():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 30)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_001body')
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 30)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def suef_001_blm_2d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(1)
    sprite('vrsuef001_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('vrsuef001_01', 6)
    sprite('vrsuef001_02', 7)
    sprite('vrsuef001_03', 8)
    sprite('vrsuef001_04', 9)
    sprite('vrsuef001_05', 9)
    sprite('vrsuef001_06', 9)
    ConstantAlphaModifier(-8)
    sprite('vrsuef001_07', 8)
    sprite('vrsuef001_08', 7)
    sprite('vrsuef001_09', 6)
    sprite('vrsuef001_10', 6)


@State
def suef_300():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 100)
    CreateObject('suef_300_dummy', -1)
    CallPrivateEffect('suef_001dust@')


@State
def suef_300_blm_2d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(1)
    sprite('vrsuef300_00', 7)
    AlphaValue(0)
    sprite('vrsuef300_01', 7)
    ConstantAlphaModifier(12)
    sprite('vrsuef300_02', 7)
    sprite('vrsuef300_03', 10)
    sprite('vrsuef300_03', 30)
    ConstantAlphaModifier(-6)
    sprite('vrsuef300_03', 20)
    sprite('vrsuef300_04', 7)
    sprite('vrsuef300_05', 7)
    sprite('vrsuef300_06', 7)


@State
def suef_300_dummy():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
    sprite('vrsuef300_dummy', 1)
    CreateObject('suef_001_aura', 0)
    CreateObject('suef_001_aura', 1)

    def RunOnObject_1():
        Flip()
    CreateObject('suef_001_aura', 2)
    CreateObject('suef_001_aura', 3)

    def RunOnObject_1():
        Flip()


@State
def suef_300_blm():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 15)
    PaletteIndex(1)
    ParticleColorFromPalette(242, 242, 242)
    CallPrivateEffect('suef_001body')
    AlphaValue(0)
    ConstantAlphaModifier(17)
    sprite('null', 15)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def suef_900_circle():

    def upon_IMMEDIATE():
        pass
    sprite('null', 32767)
    ParticleLayer(11)
    CallCustomizableParticle('rlef_ashlock_mc', -1)
    CreateParticle('rlef_ashlock_aura', -1)
