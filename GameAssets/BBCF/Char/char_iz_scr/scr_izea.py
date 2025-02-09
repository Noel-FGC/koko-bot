@State
def EMB_IZ():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_IZ.DIG', '')
        RenderLayer(5)
        Size(900)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 18)

@State
def EMB_IZ_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_IZ.DIG', '')
        RenderLayer(5)
        Size(900)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 18)

@State
def EMB_IZ_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_IZ.DIG', '')
        RenderLayer(5)
        Size(900)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 8)
    ColorTransition(4294912040, 10)
    sprite('null', 8)
    ColorTransition(4294948020, 10)
    sprite('null', 8)
    ColorTransition(4294901760, 10)
    sprite('null', 18)

@Subroutine
def AdditionalExGage():
    if (not SLOT_4):

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_31 = (SLOT_31 + 1)

        def upon_OPPONENT_HIT():
            SLOT_31 = (SLOT_31 + 1)

@Subroutine
def LightSaverSwitch():
    BlendMode_Add()
    PaletteIndex(2)
    TurnParticleColorable1(1)
    AlphaValue(255)
    if SLOT_4:
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
    else:
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)

@Subroutine
def ShotColorSwitch():
    if SLOT_6:
        PaletteIndex(5)
    else:
        PaletteIndex(4)

@State
def KakuseiMagicCircle():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_magiccircle00.DIG', '')
        FaceSpawnLocation()
        RenderLayer(5)
        BlendMode_Add()
        Size(300)
        AddX(-20000)
        AddY(10000)
        AlphaValue(160)
        RotationAngle(0)
        sendToLabelUpon(56, 1)
    sprite('null', 8)
    ColorForTransition(4291328255)
    ColorTransition(4294967168, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 3)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(120)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(20)

@State
def Install():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_wind.DIG', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        Size(500)
        AddX(-20000)
        AlphaValue(255)
        sendToLabelUpon(56, 1)
    sprite('null', 10)
    ColorForTransition(4291328255)
    ColorTransition(4294967168, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 5)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(200)
    ConstantAlphaModifier(-50)

@State
def __5DLightsaber_on():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef204_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef204_00', 6)
    ConstantAlphaModifier(0)
    sprite('vrizef204_00', 6)
    ConstantAlphaModifier(-50)

@State
def __5DLightsaber_off():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef204_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef204_00', 4)
    ConstantAlphaModifier(-50)

@State
def KakuseiAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(300)
        SetScaleX(300)
        RotationAngle(-48000)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-40)
    ConstantAlphaModifier(-30)

@State
def KakuseiAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(280)
        SetScaleX(250)
        RotationAngle(-70000)
        RenderLayer(5)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def __2DLightsaber_on():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef234_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef234_00', 6)
    ConstantAlphaModifier(0)
    sprite('vrizef234_00', 6)
    ConstantAlphaModifier(-50)

@State
def __2DLightsaber_off():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef234_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef234_00', 4)
    ConstantAlphaModifier(-50)

@State
def __2DKakuseiAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(300)
        RotationAngle(18000)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def __2DKakuseiAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(300)
        SetScaleX(250)
        RotationAngle(28000)
        RenderLayer(5)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def AirLightsaber_on():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef254_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef254_00', 6)
    ConstantAlphaModifier(0)
    sprite('vrizef254_00', 6)
    ConstantAlphaModifier(-50)

@State
def AirLightsaber_off():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('vrizef254_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrizef254_00', 4)
    ConstantAlphaModifier(-50)

@State
def AirKakuseiAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(350)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def AirKakuseiAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(300)
        RenderLayer(5)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def OverDriveAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(300)
        RotationAngle(-20000)
    sprite('null', 32767)

@State
def OverDriveAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(300)
        SetScaleX(250)
        RotationAngle(-40000)
        RenderLayer(5)
    sprite('null', 32767)

@State
def __5CKakuseiAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        SetScaleY(400)
        SetScaleX(300)
        RotationAngle(-30000)
    sprite('null', 6)
    sprite('null', 2)
    RotationAngle(-80000)
    ConstantAlphaModifier(-30)
    SetScaleY(100)
    SetScaleX(200)
    AddX(130000)

@State
def __5CKakuseiAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        SetScaleY(300)
        SetScaleX(250)
        RotationAngle(-20000)
        RenderLayer(5)
    sprite('null', 6)
    sprite('null', 2)
    RotationAngle(-80000)
    ConstantAlphaModifier(-30)
    SetScaleY(100)
    SetScaleX(200)
    AddX(130000)

@State
def __2CKakuseiAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        Size(300)
    sprite('null', 5)
    RotationAngle(-15000)
    sprite('null', 5)
    AddX(15000)
    AddY(10000)
    RotationAngle(-10000)
    SetScaleY(350)
    sprite('null', 4)
    AddX(20000)
    AddY(10000)
    sprite('null', 3)
    RotationAngle(-20000)
    ConstantAlphaModifier(-30)

@State
def Kakusei3CAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(400)
        AlphaValue(200)
        sendToLabelUpon(32, 1)
    sprite('null', 3)
    RotationAngle(15000)
    sprite('null', 40)
    Size(400)
    RotationAngle(0)
    AddX(45000)
    AddY(-25000)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def Kakusei3CAuraFire():

    def upon_IMMEDIATE():
        CallPrivateEffect('izef_hoverdashaura')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RotationAngle(180000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def AirThrowAura1():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(400)
        AlphaValue(200)
        RotationAngle(30000)
    sprite('null', 40)

@State
def AirThrowAura2():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(400)
        AlphaValue(200)
        RotationAngle(30000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    AddX(-20000)
    AddY(-30000)
    RotationAngle(20000)

@State
def AirThrowAuraFire():

    def upon_IMMEDIATE():
        CallPrivateEffect('izef_hoverdashaura')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        Flip()
        RotationAngle(-30000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def HoverDashAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(350)
        SetScaleX(400)
        AlphaValue(255)
        RotationAngle(-20000)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    CreateObject('HoverDashFire', -1)
    label(1)
    sprite('null', 3)
    PassbackAddActionMarkToFunction('HoverDashFire', 32)
    AddY(5000)
    RotationAngle(-15000)
    SetScaleSpeedY(-70)
    ConstantAlphaModifier(-20)

@State
def HoverDashFire():

    def upon_IMMEDIATE():
        CallPrivateEffect('izef_hoverdashaura')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RotationAngle(170000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def HoverDashAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(300)
        SetScaleX(350)
        AlphaValue(200)
        RotationAngle(-25000)
        RenderLayer(5)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 3)
    SetScaleSpeedY(-70)
    ConstantAlphaModifier(-20)

@State
def BackHoverDashAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(350)
        AlphaValue(200)
        RotationAngle(-25000)
        Flip()
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    CreateObject('BackHoverDashFire', -1)
    label(1)
    sprite('null', 3)
    AlphaValue(0)

@State
def BackHoverDashFire():

    def upon_IMMEDIATE():
        CallPrivateEffect('izef_hoverdashaura')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RotationAngle(160000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def BackHoverDashAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Size(300)
        AlphaValue(200)
        RotationAngle(-20000)
        RenderLayer(5)
        Flip()
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 3)
    AlphaValue(0)

@State
def ShotD_Aura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(150)
        SetScaleX(250)
        RotationAngle(-60000)
    sprite('null', 3)
    sprite('null', 3)
    RotationAngle(-65000)
    AddX(40000)
    Size(300)
    sprite('null', 10)
    RotationAngle(-70000)
    AddX(30000)
    sprite('null', 2)
    AddX(-10000)
    SetScaleY(150)
    SetScaleX(250)

@State
def ShotD_Aura_back():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RotationAngle(-55000)
        Size(250)
        RenderLayer(5)
    sprite('null', 3)
    sprite('null', 12)
    RotationAngle(-45000)
    Size(300)
    sprite('null', 2)
    RotationAngle(-45000)
    SetScaleY(150)
    SetScaleX(250)

@State
def AirShotAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Flip()
        SetScaleY(290)
        SetScaleX(250)
        RotationAngle(18000)
    sprite('null', 12)
    sprite('null', 2)
    RotationAngle(-2500)
    AddX(-14000)
    AddY(-20000)
    SetScaleY(110)
    ConstantAlphaModifier(-30)

@State
def AirShotAura_oku():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        SetScaleY(280)
        SetScaleX(250)
        RotationAngle(-70000)
        RenderLayer(5)
    sprite('null', 17)
    sprite('null', 4)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-30)

@State
def ShieildBit():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackOff()
        SetActionMark(0)
        UseSlashHitspark(1)
        Hitstop(5)
        FloorCollision(1)
        BlendMode_Normal()

        def upon_33():
            clearUponHandler(33)
            clearUponHandler(34)
            SLOT_56 = 1
            SetZVal(-500)
            SetActionMark(1)

        def upon_34():
            clearUponHandler(33)
            clearUponHandler(34)
            SLOT_56 = 0
            SetZVal(500)
            Size(900)
            SetActionMark(1)

        def upon_38():
            sendToLabel(200)

        def upon_35():
            PassbackAddActionMarkToFunction('Bit_wing00', 33)
            PassbackAddActionMarkToFunction('Bit_wing01', 33)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(300)
        if (not SLOT_21):
            SLOT_32 = 0
            if SLOT_2:
                sendToLabel(300)

        def upon_53():
            SLOT_32 = 0

        def upon_44():
            AttackOff()

        def upon_FRAME_STEP():
            if SLOT_2:
                TurnAround()
                if SLOT_56:
                    PrivateFunction3(3, -125000, 150000, 15, 1)
                else:
                    PrivateFunction3(3, -45000, 180000, 15, 1)
            if (SLOT_32 <= 0):
                if SLOT_2:
                    sendToLabel(300)
    sprite('vrizef431_00', 10)
    RotationAngle(30000)
    CreateObject('Bit_particle', 100)
    CreateParticle('izef_bit_lost', 100)
    CreateObject('Bit_wing00', 0)
    CreateObject('Bit_wing01', 1)
    SetActionMark(1)
    sprite('keep', 1)
    PassbackAddActionMarkToFunction('Bit_wing00', 32)
    PassbackAddActionMarkToFunction('Bit_wing01', 32)
    label(0)
    sprite('vrizef431_00', 32767)
    label(100)
    sprite('vrizef431_01', 10)
    SetActionMark(0)
    physicsXImpulse(-3000)
    physicsYImpulse(-8000)
    CreateParticle('izef_bit_ready', 100)
    CreateObject('Bit_Particle_Attack', 100)
    CreateObject('Bit_particle_add', 103)
    sprite('vrizef431_01', 8)
    RefreshMultihit()
    AttackLevel_(2)
    Damage(200)
    Hitstun(17)
    AirUntechableTime(17)
    AttackP2(100)
    physicsXImpulse(60000)
    physicsYImpulse(-30000)
    AfterimageBlendMode(2)
    EnableAfterimage(1)
    sprite('vrizef431_01', 4)
    AttackOff()
    physicsXImpulse(6250)
    physicsYImpulse(-1250)
    EnableAfterimage(0)
    DespawnEAEffect('Bit_particle_add')
    sprite('vrizef431_01', 10)
    physicsXImpulse(2500)
    physicsYImpulse(5000)
    label(200)
    sprite('vrizef431_00', 20)
    SetActionMark(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrizef431_00', 1)
    gotoLabel(0)
    label(300)
    sprite('vrizef431_00', 2)
    CreateParticle('izef_bit_lost', 100)
    DeleteObject(23)

@State
def Bit_wing00():

    def upon_IMMEDIATE():
        E0EAEffectObjectZ(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        RotationAngle(30000)

        def upon_32():
            E0EAEffectPosition(0)
            sendToLabel(0)
        sendToLabelUpon(33, 100)
        SetActionMark(1)

        def upon_48():
            if SLOT_2:
                EffectPosition(2, 0)
    sprite('vrizef431_w00', 32767)
    label(0)
    sprite('vrizef431_w00', 20)
    AddRotationPerFrame(-500)
    sprite('vrizef431_w00', 20)
    AddRotationPerFrame(500)
    gotoLabel(0)
    label(100)
    sprite('vrizef431_w00', 10)
    E0EAEffectPosition(2)
    SetActionMark(0)
    RotationAngle(30000)
    AddRotationPerFrame(3000)
    sprite('vrizef431_w00', 12)
    RotationAngle(15000)
    AddRotationPerFrame(0)
    sprite('vrizef431_w00', 10)
    E0EAEffectPosition(0)
    SetActionMark(1)
    sprite('vrizef431_w00', 4)
    AddRotationPerFrame(1500)
    sprite('vrizef431_w00', 1)
    RotationAngle(30000)
    AddRotationPerFrame(0)
    gotoLabel(0)

@State
def Bit_wing01():

    def upon_IMMEDIATE():
        E0EAEffectObjectZ(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        E0EAEffectDirection(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        RotationAngle(30000)

        def upon_32():
            E0EAEffectPosition(0)
            sendToLabel(0)
        sendToLabelUpon(33, 100)
        SetActionMark(1)

        def upon_48():
            if SLOT_2:
                EffectPosition(2, 1)
    sprite('vrizef431_w01', 32767)
    label(0)
    sprite('vrizef431_w01', 20)
    AddRotationPerFrame(500)
    sprite('vrizef431_w01', 20)
    AddRotationPerFrame(-500)
    gotoLabel(0)
    label(100)
    sprite('vrizef431_w01', 10)
    E0EAEffectPosition(2)
    SetActionMark(0)
    RotationAngle(30000)
    AddRotationPerFrame(-3000)
    sprite('vrizef431_w01', 12)
    RotationAngle(45000)
    AddRotationPerFrame(0)
    sprite('vrizef431_w01', 10)
    E0EAEffectPosition(0)
    SetActionMark(1)
    sprite('vrizef431_w01', 4)
    AddRotationPerFrame(-1500)
    sprite('vrizef431_w01', 1)
    RotationAngle(30000)
    AddRotationPerFrame(0)
    gotoLabel(0)

@State
def Bit_particle():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 4)
    CreateParticle('izef_bit_dust', 103)
    gotoLabel(0)

@State
def Bit_Particle_Attack():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('izef_bit_attack')
    sprite('null', 35)

@State
def Bit_particle_add():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 2)
    CreateParticle('izef_bit_dust', 103)
    gotoLabel(0)

@State
def EffLightSaber():

    def upon_IMMEDIATE():
        Visibility(1)
        CallObject('IzEffLightSaber')
    sprite('null', 32767)

@State
def __6AZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(246)
        PaletteColor1(247)
        PaletteColor3(248)
        PaletteColor4(0)
        AlphaValue(200)
    sprite('vrizef210_f04', 5)
    CreateObject('6Afanel', -1)
    sprite('null', 10)

@State
def __6Afanel():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    sprite('iz210_f04', 3)
    AlphaValue(255)

@State
def __6BZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(246)
        PaletteColor1(247)
        PaletteColor3(248)
        PaletteColor4(0)
        AlphaValue(200)
    sprite('vrizef211_f09', 3)

@State
def __6CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(246)
        PaletteColor1(247)
        PaletteColor3(248)
        PaletteColor4(0)
        AlphaValue(200)
    sprite('vrizef212_f06', 2)
    sprite('vrizef212_f07', 3)

@State
def __5CZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef202_00', 2)
    sprite('vrizef202_01', 3)
    sprite('vrizef202_01', 7)
    ConstantAlphaModifier(-20)

@State
def Kaku5CZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef203_00', 3)
    sprite('vrizef203_00', 4)
    ConstantAlphaModifier(-20)

@State
def __2CZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef232_00', 3)
    sprite('vrizef232_01', 3)
    AddX(-10000)
    AddY(7000)
    sprite('vrizef232_02', 6)
    AlphaValue(100)

@State
def ParAtk2C():

    def upon_IMMEDIATE():
        LinkParticle('izef_atk2c')
        RemoveOnCallStateEnd(3)
        RenderLayer(1)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        SetScaleY(600)
    sprite('null', 10)
    sprite('null', 6)
    ConstantAlphaModifier(-40)

@State
def Kaku2CZanzo00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef233_00', 2)
    sprite('vrizef233_01', 10)
    CreateObject('ParAtk2C', 0)

@State
def Kaku2CZanzo01():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(243)
        PaletteColor1(244)
        PaletteColor3(245)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef233_02', 10)
    sprite('vrizef233_02', 10)
    ConstantAlphaModifier(-10)

@State
def __3CZanzo00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(0)
        RenderLayer(3)
    sprite('vrizef235_00', 2)
    sprite('vrizef235_01', 10)

@State
def AIR5CZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(0)
    sprite('vrizef252_00', 3)
    sprite('vrizef252_01', 3)
    sprite('vrizef252_01', 7)
    E0EAEffectPosition(0)

@State
def ParSpDash_6():

    def upon_IMMEDIATE():
        LinkParticle('copy00 izef__drivelight00')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 24)
    AlphaValue(255)
    sprite('null', 6)

@State
def GuardCrushZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        callSubroutine('LightSaverSwitch')
        RenderLayer(3)
    sprite('vrizef412_00', 10)

@State
def ThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('izef_lockmagic.DIG', 'izef_lockmagic_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        AddY(220000)
        ColorForTransition(4294967220)

        def upon_32():
            sendToLabel(99)
    sprite('null', 32767)
    ConstantAlphaModifier(-2)
    loopRest()
    label(99)
    sprite('null', 10)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)

@State
def ThrowFunnel():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(33, 99)
    sprite('iz311_f02', 32767)
    label(99)
    sprite('null', 1)

@State
def AirThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('izef_lockmagic.DIG', 'izef_lockmagic_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        AddY(220000)
        ColorForTransition(4294967220)

        def upon_32():
            sendToLabel(98)
    sprite('null', 32767)
    ConstantAlphaModifier(-2)
    loopRest()
    label(98)
    sprite('null', 5)
    E0EAEffectPosition(0)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)

@State
def Iaimcircle():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        ParticleColorFromPalette(48, 48, 48)
        CallPrivateEffect('izef_iaimcircle')
        sendToLabelUpon(33, 99)
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    Size(1600)
    SetScaleSpeed(-100)
    sprite('null', 32767)
    AlphaValue(255)
    Size(1000)
    SetScaleSpeed(0)
    label(99)
    sprite('null', 4)
    sprite('null', 8)
    SetScaleSpeed(200)
    ConstantAlphaModifier(-30)

@State
def Iaimcircle_EntryVsMu():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        RemoveOnCallStateEnd(3)
        ParticleColorFromPalette(48, 48, 48)
        CallPrivateEffect('izef_iaimcircle')
        sendToLabelUpon(33, 99)
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    Size(1500)
    sprite('null', 32767)
    AlphaValue(255)
    Size(1500)
    PerScaleX(120)
    PerScaleY(120)
    SetScaleSpeed(0)
    label(99)
    sprite('null', 4)
    sprite('null', 8)
    SetScaleSpeed(200)
    ConstantAlphaModifier(-15)

@State
def izef_413_a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(4)
        BlendMode_Add()
        callSubroutine('ShotColorSwitch')
        AddX(110000)
        AddY(410000)
    sprite('vrizef_413_00', 2)
    sprite('vrizef_413_01', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    sprite('vrizef_413_02', 3)
    sprite('vrizef_413_03', 3)
    sprite('vrizef_413_04', 8)
    ConstantAlphaModifier(-32)

@State
def izef_413_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(4)
        BlendMode_Add()
        callSubroutine('ShotColorSwitch')
        AddX(120000)
        AddY(270000)
    sprite('vrizef_413_11', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    sprite('vrizef_413_12', 3)
    sprite('vrizef_413_13', 3)
    sprite('vrizef_413_14', 3)
    sprite('vrizef_413_15', 8)
    ConstantAlphaModifier(-32)

@State
def izef_413_c():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        PaletteIndex(4)
        BlendMode_Add()
        callSubroutine('ShotColorSwitch')
        AddX(116000)
        AddY(132000)
    sprite('vrizef_413_21', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    sprite('vrizef_413_22', 3)
    sprite('vrizef_413_23', 3)
    sprite('vrizef_413_24', 3)
    ConstantAlphaModifier(-32)

@State
def Iai_SlashZanzo00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddX(128000)
        AddY(192000)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_402_00', 2)
    sprite('vrizef_402_01', 2)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    sprite('vrizef_402_02', 2)
    sprite('vrizef_402_03', 2)
    sprite('vrizef_402_04', 2)
    sprite('vrizef_402_05', 8)
    ConstantAlphaModifier(-32)

@State
def Iai_SlashZanzo_Gedan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddX(160000)
        AddY(160000)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_402_10', 3)
    sprite('vrizef_402_11', 2)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 2)
    sprite('vrizef_402_13', 2)
    sprite('vrizef_402_14', 2)
    sprite('vrizef_402_15', 8)
    ConstantAlphaModifier(-32)

@State
def Iai_SlashZanzo_AntiAirA():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddX(256000)
        AddY(380000)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_404_00', 2)
    sprite('vrizef_404_01', 2)
    SetZVal(100)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    CreateParticle('izef_Iai_feather', 9)
    sprite('vrizef_404_02', 2)
    sprite('vrizef_404_03', 2)
    sprite('vrizef_404_04', 2)
    sprite('vrizef_404_05', 8)
    ConstantAlphaModifier(-32)

@State
def Iai_SlashZanzo_AntiAirB():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddY(384000)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_405_01', 2)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    CreateParticle('izef_Iai_feather', 9)
    sprite('vrizef_405_02', 2)
    sprite('vrizef_405_03', 2)
    sprite('vrizef_405_04', 2)
    sprite('vrizef_405_05', 8)
    ConstantAlphaModifier(-32)

@State
def Iai_AntiAirNext_Zanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vrizef_406_00', 3)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    sprite('vrizef_406_00', 2)
    gotoLabel(0)
    label(1)
    sprite('vrizef_406_01', 3)
    AddY(-5000)
    sprite('vrizef_406_01', 5)
    ConstantAlphaModifier(-20)

@State
def IaiAntiAirNextAuraL():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        Flip()
        SetScaleX(600)
        SetScaleY(450)
        AlphaValue(255)
        RotationAngle(110000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    AddX(-5000)
    AddY(-130000)
    Size(350)
    Rotation(20000)
    sprite('null', 5)
    AddX(5000)
    AddY(-20000)
    Size(300)
    Rotation(5000)

@State
def IaiAntiAirNextAuraR():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        SetScaleX(600)
        SetScaleY(450)
        AlphaValue(255)
        RotationAngle(110000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    AddX(30000)
    AddY(-150000)
    Size(250)
    Rotation(30000)
    sprite('null', 5)
    AddX(5000)
    AddY(-10000)
    Rotation(5000)

@State
def Iai_AntiAir_Next_404F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz404_03', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(6000)
    SetAcceleration(2000)
    ConstantAlphaModifier(-20)
    sprite('iz404_04', 2)
    sprite('iz404_05', 6)

@State
def Iai_AntiAir_Next_404B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz404_03', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(-6000)
    SetAcceleration(-2000)
    ConstantAlphaModifier(-20)
    sprite('iz404_04', 2)
    sprite('iz404_05', 6)

@State
def Iai_AntiAir_Next_405F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz405_07', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(6000)
    SetAcceleration(2000)
    ConstantAlphaModifier(-20)
    sprite('iz405_08', 2)
    sprite('iz405_09', 6)

@State
def Iai_AntiAir_Next_405B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz405_07', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(-6000)
    SetAcceleration(-2000)
    ConstantAlphaModifier(-20)
    sprite('iz405_08', 2)
    sprite('iz405_09', 6)

@State
def Iai_AntiAir_Next_408F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz408_07', 3)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(6000)
    SetAcceleration(2000)
    ConstantAlphaModifier(-20)
    sprite('iz408_08', 7)

@State
def Iai_AntiAir_Next_408B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz408_07', 3)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(-6000)
    SetAcceleration(-2000)
    ConstantAlphaModifier(-20)
    sprite('iz408_08', 7)

@State
def Iai_AntiAir_Next_403F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        TeleportToObject(3)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz403_00', 5)
    CharacterFlash(51200, 6, 2)
    AddX(400000)
    physicsXImpulse(-80000)
    AlphaValue(128)

@State
def Iai_AntiAir_Next_403B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        TeleportToObject(3)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz403_00', 5)
    CharacterFlash(51200, 6, 2)
    AddX(-400000)
    physicsXImpulse(80000)
    AlphaValue(128)

@State
def Iai_AntiAir_Next_406F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        TeleportToObject(3)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz406_00', 3)
    CharacterFlash(51200, 6, 2)
    AddX(240000)
    physicsXImpulse(-20000)
    AlphaValue(128)
    sprite('iz406_01', 4)
    sprite('iz406_02', 3)

@State
def Iai_AntiAir_Next_406B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        TeleportToObject(3)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz406_00', 3)
    CharacterFlash(51200, 6, 2)
    AddX(-240000)
    physicsXImpulse(20000)
    AlphaValue(128)
    sprite('iz406_01', 4)
    sprite('iz406_02', 3)

@State
def Iai_AntiAir_Next_413F():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz413_15', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(6000)
    SetAcceleration(2000)
    ConstantAlphaModifier(-20)
    sprite('iz413_16', 2)
    sprite('iz413_17', 6)

@State
def Iai_AntiAir_Next_413B():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz413_15', 2)
    CharacterFlash(51200, 6, 2)
    physicsXImpulse(-6000)
    SetAcceleration(-2000)
    ConstantAlphaModifier(-20)
    sprite('iz413_16', 2)
    sprite('iz413_17', 6)

@State
def Iai_hold():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        callSubroutine('ShotColorSwitch')
    label(0)
    sprite('null', 2)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_Iai_hold', 0)
    gotoLabel(0)

@State
def Iai_hold_add():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
    label(0)
    sprite('null', 1)
    CreateParticle('izef_Iai_hold_add', 0)
    gotoLabel(0)

@State
def AirAssaultZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(2)
        AlphaValue(200)
        RenderLayer(3)
    sprite('vrizef_408_00', 2)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    sprite('vrizef_408_01', 3)
    ConstantAlphaModifier(-30)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    sprite('vrizef_408_02', 2)
    sprite('null', 5)

@State
def Ia_SlashNextZanzo():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddX(50000)
        AddY(160000)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_402_11', 2)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 2)
    sprite('vrizef_402_13', 2)
    sprite('vrizef_402_14', 2)
    sprite('vrizef_402_15', 8)
    ConstantAlphaModifier(-32)

@State
def Ia_SlashNextZanzo_EntryVsMu():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        AddX(50000)
        AddY(160000)
        RenderLayer(3)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef_402_11', 16)
    CreateParticle('izef_Iai_feather', 0)
    CreateParticle('izef_Iai_feather', 1)
    CreateParticle('izef_Iai_feather', 2)
    CreateParticle('izef_Iai_feather', 3)
    CreateParticle('izef_Iai_feather', 4)
    CreateParticle('izef_Iai_feather', 5)
    CreateParticle('izef_Iai_feather', 6)
    CreateParticle('izef_Iai_feather', 7)
    CreateParticle('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 4)
    sprite('vrizef_402_13', 4)
    sprite('vrizef_402_14', 4)
    sprite('vrizef_402_15', 8)
    ConstantAlphaModifier(-32)

@State
def IaiSlashNextAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        SetScaleX(600)
        SetScaleY(450)
        AlphaValue(255)
    sprite('null', 6)
    sprite('null', 3)
    SetScaleY(300)
    SetScaleX(400)
    AddX(40000)
    RotationAngle(-25000)

@State
def DIST_IZShot():

    def upon_FRAME_STEP():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
    sprite('vrdist_iz00', 6)
    AlphaValue(200)
    SetScaleX(750)
    SetScaleY(500)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_iz00', 10)
    SetScaleSpeedY(-100)
    SetScaleSpeedY(-100)

@State
def DIST_IZSpecial_Shot():

    def upon_FRAME_STEP():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
    sprite('vrdist_iz00', 6)
    AlphaValue(200)
    SetScaleX(1000)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_iz00', 10)
    SetScaleSpeedY(-100)
    SetScaleSpeedY(-100)

@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(800)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        Hitstop(7)
        EnemyHitstopAddition(0, 3, 4)
        HitsparkSize(600)
        Hitstun(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        ParticleColorFromPalette(240, 241, 241)
        CallCustomizableParticle('izef_shot_circle', 100)
    sprite('vrizef_shot00', 16)
    physicsXImpulse(1000)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 6)
    RefreshMultihit()
    physicsXImpulse(25000)
    physicsYImpulse(0)
    RotationSomething(0)
    sprite('vrizef_shot00', 32)
    XImpulseAcceleration(160)
    sprite('vrizef_shot00', 6)
    AttackOff()
    physicsXImpulse(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Air_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(800)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(10)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        ParticleRotationAngle(45000)
        ParticleColorFromPalette(240, 241, 241)
        CallCustomizableParticle('izef_shot_circle', 100)
    sprite('vrizef_shot00', 11)
    RotationAngle(45000)
    physicsXImpulse(1000)
    physicsYImpulse(-1000)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 2)
    RefreshMultihit()
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    SetAcceleration(900)
    setGravity(900)
    ContinueState(240)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 4)
    YAccel(140)
    sprite('vrizef_shot00', 40)
    label(1)
    sprite('vrizef_shot00', 6)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def shotD_Matome():
    sprite('iz400_expoint', 90)
    CreateObject('Shot_D', 0)
    CreateObject('Shot_D', 1)
    ObjectUpon(1, 32)
    CreateObject('Shot_D', 2)
    ObjectUpon(1, 33)
    CreateObject('Shot_D_circle', 1)

@State
def shotD_MatomeOD():
    sprite('iz400_expointOD', 90)
    CreateObject('Shot_D_OD', 0)
    ObjectUpon(1, 32)
    CreateObject('Shot_D_OD', 1)
    CreateObject('Shot_D_OD', 2)
    ObjectUpon(1, 33)
    CreateObject('Shot_D_OD', 3)
    ObjectUpon(1, 34)
    CreateObject('Shot_D_OD', 4)
    ObjectUpon(1, 35)
    CreateObject('Shot_D_OD_circle', 1)

@State
def AirshotD_Matome():
    sprite('iz401_expoint', 90)
    CreateObject('Air_Shot_D', 0)
    CreateObject('Air_Shot_D', 1)
    ObjectUpon(1, 32)
    CreateObject('Air_Shot_D', 2)
    ObjectUpon(1, 33)
    CreateObject('Air_Shot_D_circle', 0)

@State
def AirshotD_MatomeOD():
    sprite('iz401_expointOD', 90)
    CreateObject('Air_Shot_D_OD', 0)
    CreateObject('Air_Shot_D_OD', 1)
    ObjectUpon(1, 32)
    CreateObject('Air_Shot_D_OD', 2)
    ObjectUpon(1, 33)
    CreateObject('Air_Shot_D_OD', 3)
    ObjectUpon(1, 34)
    CreateObject('Air_Shot_D_OD', 4)
    ObjectUpon(1, 35)
    CreateObject('Air_Shot_D_OD_circle', 0)

@State
def Shot_D():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        Size(835)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(10)
        HitsparkSize(600)
        Hitstun(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')

        def upon_32():
            RotationAngle(-10000)

        def upon_33():
            RotationAngle(-20000)

        def upon_34():
            RotationAngle(20000)

        def upon_35():
            RotationAngle(-20000)
    sprite('vrizef_shot00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 15)
    XSpeed2(500, 0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    sprite('vrizef_shot00', 15)
    RefreshMultihit()
    XImpulseAcceleration(600)
    YAccel(600)
    sprite('vrizef_shot00', 20)
    XImpulseAcceleration(150)
    YAccel(150)
    RotationSomething(0)
    sprite('vrizef_shot00', 30)
    XImpulseAcceleration(1000)
    YAccel(1000)
    sprite('vrizef_shot00', 6)
    AttackOff()
    XImpulseAcceleration(0)
    YAccel(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Air_Shot_D():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        Size(835)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(10)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        RotationAngle(40000)

        def upon_32():
            RotationAngle(10000)

        def upon_33():
            RotationAngle(70000)

        def upon_34():
            RotationAngle(25000)

        def upon_35():
            RotationAngle(65000)
    sprite('vrizef_shot00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 10)
    XSpeed2(1000, 0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    sprite('vrizef_shot00', 5)
    RefreshMultihit()
    XImpulseAcceleration(500)
    YAccel(500)
    ContinueState(240)
    sprite('vrizef_shot00', 5)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 5)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 20)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 60)
    label(1)
    sprite('vrizef_shot00', 6)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Shot_D_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        Size(760)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(10)
        HitsparkSize(600)
        Hitstun(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')

        def upon_32():
            RotationAngle(10000)

        def upon_33():
            RotationAngle(-10000)

        def upon_34():
            RotationAngle(20000)

        def upon_35():
            RotationAngle(-20000)
    sprite('vrizef_shot00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 15)
    XSpeed2(500, 0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    sprite('vrizef_shot00', 15)
    RefreshMultihit()
    XImpulseAcceleration(600)
    YAccel(600)
    sprite('vrizef_shot00', 20)
    XImpulseAcceleration(150)
    YAccel(150)
    RotationSomething(0)
    sprite('vrizef_shot00', 30)
    XImpulseAcceleration(1000)
    YAccel(1000)
    sprite('vrizef_shot00', 6)
    AttackOff()
    XImpulseAcceleration(0)
    YAccel(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Air_Shot_D_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        Size(760)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = (SLOT_7 + 1)

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        ContinueState(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(10)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        StarterRating(2)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_FRAME_STEP():
            if SLOT_38:
                PrivateFunction5(105)
                if (SLOT_22 < SLOT_0):
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if (SLOT_22 > SLOT_0):
                    DeleteObject(23)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        RotationAngle(45000)

        def upon_32():
            RotationAngle(35000)

        def upon_33():
            RotationAngle(55000)

        def upon_34():
            RotationAngle(25000)

        def upon_35():
            RotationAngle(65000)
    sprite('vrizef_shot00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    StopCharacterFlash1(-1)
    CharacterFlash(0, 20, 1)
    sprite('vrizef_shot00', 10)
    XSpeed2(1000, 0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 100)
    sprite('vrizef_shot00', 5)
    RefreshMultihit()
    XImpulseAcceleration(500)
    YAccel(500)
    ContinueState(240)
    sprite('vrizef_shot00', 5)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 5)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 20)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 60)
    label(1)
    sprite('vrizef_shot00', 6)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Shot_D_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    ParticleSize(1250)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_circle', 100)

@State
def Shot_D_OD_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    ParticleSize(1750)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_circle', 100)

@State
def Air_Shot_D_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    ParticleSize(1250)
    ParticleRotationAngle(45000)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_circle', 100)

@State
def Air_Shot_D_OD_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    ParticleSize(1750)
    ParticleRotationAngle(45000)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_circle', 100)

@State
def Special_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = 1

        def upon_STATE_END():
            SLOT_7 = 0
        AttackLevel_(3)
        Damage(800)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(16)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        AttackP1(85)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        if SLOT_110:
            SLOT_52 = 1
        callSubroutine('ShotColorSwitch')
        ParticleColorFromPalette(240, 241, 241)
        CallCustomizableParticle('izef_SPshot_circle', 100)
        ParticleColorFromPalette(241, 240, 240)
        CallCustomizableParticle('izef_shot_dust', 100)

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 32)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 33)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 34)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 35)
        if SLOT_52:
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 36)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 37)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 38)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 39)
    sprite('vrizef_shot01a', 5)
    AlphaValue(0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    ConstantAlphaModifier(40)
    sprite('vrizef_shot01b', 1)
    AlphaValue(255)
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    RefreshMultihit()
    physicsXImpulse(28000)
    SetAcceleration(800)
    physicsYImpulse(0)
    RotationSomething(0)
    sprite('vrizef_shot01i', 1)
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 8)
    sprite('vrizef_shot01', 60)
    SetAcceleration(1600)
    sprite('vrizef_shot01', 12)
    AttackOff()
    physicsXImpulse(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    EndMomentum(1)
    sprite('keep', 12)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Special_Shot_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(16)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        AttackP1(85)
        AttackOff()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        callSubroutine('ShotColorSwitch')
        ParticleColorFromPalette(240, 241, 241)
        CallCustomizableParticle('izef_SPshot_circle', 100)
        ParticleColorFromPalette(241, 240, 240)
        CallCustomizableParticle('izef_shot_dust', 100)

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 32)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 33)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 34)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 35)
    sprite('vrizef_shot01a', 5)
    AlphaValue(0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    ConstantAlphaModifier(40)
    sprite('vrizef_shot01b', 1)
    AlphaValue(255)
    RefreshMultihit()
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    SetAcceleration(200)
    physicsYImpulse(0)
    RotationSomething(0)
    sprite('vrizef_shot01i', 1)
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 8)
    SetAcceleration(800)
    sprite('vrizef_shot01', 60)
    SetAcceleration(1600)
    sprite('vrizef_shot01', 12)
    AttackOff()
    physicsXImpulse(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    XImpulseAcceleration(30)
    YAccel(30)
    SetAcceleration(0)
    sprite('keep', 12)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Special_Shot_Air():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        SLOT_7 = 1

        def upon_STATE_END():
            SLOT_7 = 0
        AttackLevel_(3)
        UseSlashHitspark(1)
        PushbackX(20000)
        Hitstop(16)
        HitsparkSize(600)
        Hitstun(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(0)
        AttackP1(85)
        AttackOff()
        if SLOT_110:
            SLOT_52 = 1
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)
        callSubroutine('ShotColorSwitch')
        ParticleColorFromPalette(240, 241, 241)
        ParticleRotationAngle(45000)
        CallCustomizableParticle('izef_SPshot_circle', 100)
        ParticleColorFromPalette(241, 240, 240)
        CallCustomizableParticle('izef_shot_dust', 100)

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 32)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 33)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 34)
        CreateObject('Special_Shot_Next', -1)
        ObjectUpon(1, 35)
        if SLOT_52:
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 36)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 37)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 38)
            CreateObject('Special_Shot_Next', -1)
            ObjectUpon(1, 39)
    sprite('vrizef_shot01a', 5)
    RotationAngle(45000)
    physicsXImpulse(300)
    physicsYImpulse(-300)
    AlphaValue(0)
    CreateObject('Shot_particle', 100)
    CreateParticle('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    ConstantAlphaModifier(40)
    sprite('vrizef_shot01b', 1)
    AlphaValue(255)
    SetAcceleration(100)
    setGravity(100)
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    sprite('vrizef_shot01i', 1)
    RefreshMultihit()
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 4)
    SetAcceleration(800)
    setGravity(800)
    RotationSomething(0)
    ContinueState(240)
    sprite('vrizef_shot01', 50)
    SetAcceleration(1600)
    setGravity(1600)
    label(1)
    sprite('vrizef_shot01', 12)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    EndMomentum(1)
    sprite('keep', 12)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZSpecial_Shot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_shot_delete_circle', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Special_Shot_Next():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(150)
        UseSlashHitspark(1)
        Hitstop(0)
        EnemyHitstopAddition(4, 4, 5)
        HitsparkSize(600)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(70)
        AttackP2(97)
        AttackOff()
        Size(800)
        callSubroutine('ShotColorSwitch')

        def upon_32():
            TeleportToObject(22)
            AddX(-250000)
            AddY(400000)
            RotationAngle(45000)
            sendToLabel(0)
            SLOT_51 = 1
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(45000)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_33():
            TeleportToObject(22)
            AddX(250000)
            AddY(0)
            RotationAngle(-45000)
            ForceFaceSprite()
            SLOT_51 = 4
            sendToLabel(1)
            FlipOnHit(1)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(-45000)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_34():
            TeleportToObject(22)
            AddX(-250000)
            AddY(0)
            RotationAngle(-45000)
            SLOT_51 = 3
            sendToLabel(2)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(-45000)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_35():
            TeleportToObject(22)
            AddX(250000)
            AddY(400000)
            RotationAngle(45000)
            ForceFaceSprite()
            SLOT_51 = 2
            sendToLabel(3)
            FlipOnHit(1)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(45000)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_38():
            TeleportToObject(22)
            AddX(300000)
            AddY(200000)
            RotationAngle(0)
            ForceFaceSprite()
            SLOT_51 = 7
            sendToLabel(7)
            FlipOnHit(1)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(0)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_39():
            TeleportToObject(22)
            AddX(-300000)
            AddY(200000)
            RotationAngle(0)
            ForceFaceSprite()
            SLOT_51 = 8
            sendToLabel(6)
            FlipOnHit(0)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(0)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_36():
            TeleportToObject(22)
            AddX(0)
            AddY(450000)
            RotationAngle(90000)
            ForceFaceSprite()
            SLOT_51 = 5
            sendToLabel(4)
            FlipOnHit(0)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(90000)
            CallCustomizableParticle('izef_shot_circle_small', 1)

        def upon_37():
            TeleportToObject(22)
            AddX(0)
            AddY(-100000)
            RotationAngle(-90000)
            ForceFaceSprite()
            SLOT_51 = 6
            sendToLabel(5)
            FlipOnHit(0)
            ParticleColorFromPalette(240, 241, 241)
            ParticleRotationAngle(-90000)
            CallCustomizableParticle('izef_shot_circle_small', 1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 580)
    label(7)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 26)
    gotoLabel(10)
    label(6)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 23)
    gotoLabel(10)
    label(5)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 20)
    gotoLabel(10)
    label(4)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 17)
    gotoLabel(10)
    label(3)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 14)
    gotoLabel(10)
    label(2)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 11)
    gotoLabel(10)
    label(1)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 8)
    gotoLabel(10)
    label(0)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 1)
    label(10)
    sprite('vrizef_shot02', 4)
    XSpeed2(40000, 0)
    sprite('vrizef_shot02', 20)
    RefreshMultihit()
    sendToLabelUpon(10, 11)
    sendToLabelUpon(2, 11)
    label(11)
    sprite('vrizef_shot02', 12)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetAcceleration(0)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    ConstantAlphaModifier(-20)
    CreateObject('DIST_IZShot', 100)
    CreateParticle('izef_shot_delete_feather', 100)
    ParticleColorFromPalette(241, 240, 240)
    CallCustomizableParticle('izef_shot_dust', 100)

@State
def Shot_particle():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 1)
    CreateParticle('izef_shot_dust', 100)
    gotoLabel(0)

@State
def WarpHoverAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(5)
        Flip()
        BlendMode_Add()
        SetScaleX(700)
        SetScaleY(400)
        AlphaValue(232)
        ConstantAlphaModifier(50)
    sprite('null', 2)
    sprite('null', 2)
    ConstantAlphaModifier(0)
    SetScaleX(600)
    AddX(10000)
    sprite('null', 2)
    AlphaValue(200)
    SetScaleX(400)
    AddX(30000)
    AddY(-30000)
    sprite('null', 2)
    SetScaleY(300)
    AddY(30000)
    RotationAngle(-25000)

@State
def WarpHoverAura_Air():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', 'izef_hoveraura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(5)
        BlendMode_Add()
        SetScaleX(700)
        SetScaleY(400)
        AlphaValue(100)
        ConstantAlphaModifier(50)
    sprite('null', 2)
    sprite('null', 2)
    ConstantAlphaModifier(0)
    SetScaleX(600)
    AddX(10000)
    sprite('null', 2)
    AlphaValue(200)
    SetScaleX(400)
    AddX(-30000)
    AddY(-10000)
    sprite('null', 2)

@State
def WarpEff():

    def upon_IMMEDIATE():
        callSubroutine('ShotColorSwitch')
    sprite('null', 1)
    ParticleSize(800)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_warpair01', 100)
    ParticleSize(900)
    CallCustomizableParticle('izef_warpair00', 100)

@State
def WarpEff_D():

    def upon_IMMEDIATE():
        callSubroutine('ShotColorSwitch')
    sprite('null', 1)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_warpair00', 100)
    ParticleColorFromPalette(240, 241, 241)
    CallCustomizableParticle('izef_warpair01', 100)
    CreateParticle('izef_warpair', 100)

@State
def Warp_D_Land_Zanzo00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz409_02', 6)
    CharacterFlash(16777215, 6, 2)
    physicsXImpulse(16000)
    ConstantAlphaModifier(-30)

@State
def Warp_D_Land_Zanzo01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz409_02', 6)
    CharacterFlash(16777215, 6, 2)
    physicsXImpulse(-16000)
    ConstantAlphaModifier(-30)

@State
def Warp_A_Zanzo00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz409_04', 6)
    AddX(96000)
    physicsXImpulse(-16000)
    ConstantAlphaModifier(30)
    AlphaValue(0)

@State
def Warp_A_Zanzo01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz409_04', 6)
    AddX(-96000)
    physicsXImpulse(16000)
    ConstantAlphaModifier(30)
    AlphaValue(0)

@State
def firespark():

    def upon_IMMEDIATE():
        LinkParticle('izef_firespark')
    sprite('null', 45)
    Flip()

@State
def Warp_D_Air_Zanzo00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz410_02', 6)
    CharacterFlash(16777215, 6, 2)
    physicsXImpulse(16000)
    ConstantAlphaModifier(-30)

@State
def Warp_D_Air_Zanzo01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('iz410_02', 6)
    CharacterFlash(16777215, 6, 2)
    physicsXImpulse(-16000)
    ConstantAlphaModifier(-30)

@State
def DD_3d_zanzoh():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        AddX(168000)
        AddY(224000)
        Size(1500)
        Eff3DEffect('izef_430_slash.DIG', '')
        FaceSpawnLocation()
        RenderLayer(1)
    sprite('null', 16)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def DD_pt_edge():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(240000)
        AddY(224000)
        PaletteIndex(2)
    sprite('null', 60)
    ParticleColorFromPalette(246, 246, 246)
    CallCustomizableParticle('izef_DD_edge', 100)

@State
def DD_pt_circle():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(260000)
        AddY(224000)
        Size(1000)
    sprite('null', 15)
    sprite('null', 60)
    LinkParticle('izef_DD_circle')
    sprite('null', 30)
    ConstantAlphaModifier(-8)

@State
def DD_3Dcircle_out():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_DDring.DIG', '')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1320)
        AddX(260000)
        AddY(204000)
    sprite('null', 25)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 50)
    AlphaValue(200)
    ConstantAlphaModifier(0)
    sprite('null', 40)
    SetScaleSpeed(20)
    ConstantAlphaModifier(-12)

@State
def DD_3Dcircle_in():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_DDmahojin.DIG', '')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(0)
        AddX(190000)
        AbsoluteY(230000)
    sprite('null', 25)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    SetScaleSpeed(36)
    sprite('null', 50)
    Size(1080)
    SetScaleSpeed(0)
    AlphaValue(240)
    ConstantAlphaModifier(0)
    sprite('null', 40)
    SetScaleSpeed(20)
    ConstantAlphaModifier(-12)

@State
def DD_sword():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(226000)
        AddY(234000)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef430swd00', 20)
    CreateParticle('izef_DD_sword', -1)
    sprite('vrizef430swd00', 12)
    ConstantAlphaModifier(-20)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    CreateParticle('izef_dellight', 2)
    CreateParticle('izef_dellight', 3)
    CreateParticle('izef_dellight', 4)
    CreateParticle('izef_dellight', 5)
    CreateParticle('izef_dellight', 6)

@State
def DD_sword_env():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddX(226000)
        AddY(234000)
        PaletteIndex(1)
        AlphaValue(100)
    sprite('vrizef430swd_env', 20)
    sprite('vrizef430swd_env', 10)
    ConstantAlphaModifier(-10)

@State
def DD_3d_swordaura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddX(256000)
        AddY(224000)
        SetScaleX(875)
        SetScaleY(750)
        Eff3DEffect('izef_430_aura.DIG', '')
        FaceSpawnLocation()
        RenderLayer(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def DD_sword_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(226000)
        AddY(220000)
        PaletteIndex(6)
        BlendMode_Add()
    sprite('vrizef430swd01', 20)
    CreateParticle('izef_DD_sword', -1)
    sprite('vrizef430swd01', 12)
    ConstantAlphaModifier(-20)
    CreateParticle('izef_dellight', 0)
    CreateParticle('izef_dellight', 1)
    CreateParticle('izef_dellight', 2)
    CreateParticle('izef_dellight', 3)
    CreateParticle('izef_dellight', 4)
    CreateParticle('izef_dellight', 5)
    CreateParticle('izef_dellight', 6)
    CreateParticle('izef_dellight', 7)
    CreateParticle('izef_dellight', 8)
    CreateParticle('izef_dellight', 9)
    CreateParticle('izef_dellight', 10)
    CreateParticle('izef_dellight', 11)
    CreateParticle('izef_dellight', 12)

@State
def DD_sword_env_OD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddX(226000)
        AddY(234000)
        PaletteIndex(1)
        AlphaValue(100)
    sprite('vrizef430swd01_env', 20)
    sprite('vrizef430swd01_env', 10)
    ConstantAlphaModifier(-10)

@State
def UltimateAssaultAura():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        SetScaleX(600)
        SetScaleY(500)
        RotationAngle(18000)
    sprite('null', 27)
    sprite('null', 3)
    AddY(-12000)
    SetScaleX(400)
    SetScaleY(200)
    RotationAngle(-5000)

@State
def UltimateAssaultAura_back():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_aura.DIG', 'izef_aura_motion_000.mmot')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(500)
        RotationAngle(20000)
    sprite('null', 27)
    sprite('null', 3)
    AddY(-12000)
    SetScaleX(400)
    SetScaleY(200)
    RotationAngle(-5000)

@State
def iz431_mahojin():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_DD2mahojin.DIG', '')
        FaceSpawnLocation()
        RenderLayer(5)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        Size(900)
    sprite('null', 120)
    sprite('null', 10)
    SetScaleSpeed(5)
    sprite('null', 24)
    ConstantAlphaModifier(-10)

@State
def SummonFunnelAuraR():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_DD2aura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        SetScaleX(750)
        RotationAngle(-35000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Size(600)
    Rotation(-3000)

@State
def SummonFunnelAuraL():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_DD2aura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Flip()
        SetScaleX(750)
        RotationAngle(-35000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Size(600)
    Rotation(-3000)

@State
def SummonFunnelF():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        RenderLayer(2)
        BlendMode_Normal()
    sprite('iz431_f19', 4)
    CreateObject('SummonFunnelAuraL', 0)
    CreateObject('SummonFunnelAuraR', 1)
    CreateParticle('izef_GNptcR', 1)
    CreateParticle('izef_GNptcR', 2)
    CreateParticle('izef_GNptcR', 3)
    CreateParticle('izef_GNptcR', 6)
    CreateParticle('izef_GNptcL', 0)
    CreateParticle('izef_GNptcL', 4)
    CreateParticle('izef_GNptcL', 5)
    CreateParticle('izef_GNptcL', 7)
    sprite('iz431_f20', 16)
    sprite('iz431_f20', 16)
    sprite('iz431_f24', 4)
    PassbackAddActionMarkToFunction('SummonFunnelAuraL', 32)
    PassbackAddActionMarkToFunction('SummonFunnelAuraR', 32)
    sprite('iz431_f25', 4)

@State
def AST1st_mahojin():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_mahojin.DIG', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        Size(1000)
    sprite('null', 40)
    SetScaleSpeed(5)
    sprite('null', 70)
    SetScaleSpeed(0)
    sprite('null', 10)
    SetScaleSpeed(5)
    sprite('null', 24)
    ConstantAlphaModifier(-10)

@State
def AST_changelightC():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        LinkParticle('izef_AH_changelightC')
    sprite('null', 60)

@State
def AST_changeBG():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        LinkParticle('izef_AH_changeBG')
        sendToLabelUpon(32, 90)
    sprite('null', 60)
    loopRest()
    label(90)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(-25)

@State
def AstWhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        Size(10000)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vr_white', 10)
    ConstantAlphaModifier(25)
    sprite('vr_white', 20)
    sprite('vr_white', 30)
    AlphaValue(240)
    ConstantAlphaModifier(-8)

@State
def AST_1stAuraL():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        SetScaleX(1000)
        SetScaleY(1400)
        sendToLabelUpon(32, 1)
    sprite('null', 16)
    sprite('null', 6)
    AddX(-20000)
    SetScaleX(700)
    SetScaleY(1400)
    sprite('null', 6)
    SetScaleY(1100)
    AddX(-20000)
    AddY(-32000)
    RotationAngle(18000)
    sprite('null', 6)
    AddX(20000)
    SetScaleY(800)
    Rotation(2000)
    sprite('null', 6)
    AddY(20000)
    Rotation(1000)
    sprite('null', 20)
    SetScaleY(1000)
    label(1)

@State
def AST_1stAuraR():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Flip()
        SetScaleX(1000)
        SetScaleY(1400)
    sprite('null', 16)
    sprite('null', 6)
    AddY(-15000)
    AddX(-15000)
    SetScaleX(700)
    RotationAngle(5000)
    sprite('null', 6)
    SetScaleY(1300)
    RotationAngle(14000)
    AddX(25000)
    sprite('null', 6)
    AddY(20000)
    AddX(20000)
    RotationAngle(10000)
    SetScaleX(300)
    SetScaleY(700)
    sprite('null', 6)
    Flip()
    AddX(-48000)
    RotationAngle(28000)
    SetScaleX(200)
    SetScaleY(800)
    sprite('null', 20)
    SetScaleY(1000)
    SetScaleX(400)
    AddX(-20000)

@State
def AST_2ndAurafront():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(4)
        BlendMode_Add()
        Flip()
        RotationAngle(-12000)
    sprite('null', 5)
    sprite('null', 4)
    Rotation(-8000)
    AddY(7760000)
    AddX(180000)
    SetScaleX(900)
    SetScaleY(600)
    sprite('null', 4)
    SetScaleX(900)
    SetScaleY(450)
    AddY(-9000)
    AddX(150000)
    sprite('null', 4)
    AddX(70000)
    SetScaleX(700)
    sprite('null', 4)
    AddX(15000)
    AddY(-9000)
    SetScaleX(700)
    sprite('null', 4)
    RenderLayer(5)
    AddY(-9000)
    AddX(35000)
    SetScaleX(500)
    SetScaleY(300)
    sprite('null', 4)
    AddY(-9000)
    AddX(35000)
    Rotation(-24000)
    SetScaleX(400)
    sprite('null', 4)
    AddY(-9000)
    AddX(30000)
    sprite('null', 4)
    Rotation(-24000)
    sprite('null', 4)
    Rotation(-28000)
    AddX(30000)
    SetScaleY(500)
    SetScaleX(300)
    sprite('null', 4)
    Rotation(-28000)
    AddX(30000)

@State
def AST_2ndAuraback():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Flip()
        RotationAngle(-20000)
        Size(900)
    sprite('null', 5)
    sprite('null', 4)
    AddY(7760000)
    AddX(150000)
    Size(600)
    sprite('null', 4)
    Size(500)
    AddX(130000)
    sprite('null', 4)
    AddX(100000)
    sprite('null', 4)
    AddX(70000)
    Rotation(-25000)
    sprite('null', 4)
    AddX(60000)
    Rotation(-12000)
    sprite('null', 4)
    AddX(20000)
    Rotation(-20000)
    sprite('null', 4)
    Flip()
    AddX(-30000)
    Rotation(3000)
    SetScaleY(100)
    sprite('null', 4)
    Rotation(30000)
    Size(800)
    AddY(20000)
    sprite('null', 4)
    sprite('null', 4)

@State
def AST_2ndAura():

    def upon_IMMEDIATE():
        AbsoluteY(284000)
        Visibility(1)
    sprite('iz450cutin_15', 5)
    CreateObject('AST_2ndAurafront', 0)
    CreateObject('AST_2ndAuraback', 1)

@State
def AST_3rdAurafront():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RenderLayer(1)
        BlendMode_Add()
        SetScaleX(900)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    RotationAngle(-30000)
    label(1)
    sprite('null', 5)
    sprite('null', 5)
    Rotation(-3000)
    sprite('null', 214)
    Rotation(-3000)
    sprite('null', 5)
    Rotation(15000)
    sprite('null', 5)
    sprite('null', 5)
    AddY(-5000)
    sprite('null', 5)
    AddX(5000)
    SetScaleX(800)
    sprite('null', 40)
    RotationAngle(-15000)
    SetScaleY(1500)
    SetScaleX(800)
    AddY(15000)

@State
def AST_3rdAuraback():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_hoveraura.DIG', '')
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(900)
        AlphaValue(200)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    RotationAngle(-45000)
    label(1)
    sprite('null', 5)
    sprite('null', 5)
    Rotation(-3000)
    sprite('null', 214)
    Rotation(-3000)
    sprite('null', 5)
    Rotation(15000)
    sprite('null', 5)
    sprite('null', 5)
    AddY(15000)
    sprite('null', 5)
    AddX(35000)
    SetScaleX(700)
    sprite('null', 40)
    RotationAngle(-15000)
    SetScaleY(1400)
    SetScaleX(400)
    AddY(15000)

@State
def iz450cutin():

    def upon_IMMEDIATE():
        RenderLayer(1)
        IgnorePauses(3)
        PaletteIndex(0)
        BlendMode_Normal()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-384000)
        XPositionRelativeFacingAbsolute(640000)
    sprite('iz450cutin_00', 5)
    SmartVoiceline('iz291')
    AlphaValue(0)
    ConstantAlphaModifier(12)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    AlphaValue(255)
    sprite('iz450cutin_00', 5)
    CreateObject('izef_ah_cloud', -1)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    if SLOT_44:
        SmartVoiceline('iz292')
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    if SLOT_43:
        SmartVoiceline('iz292')
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_04', 5)
    sprite('iz450cutin_05', 5)
    sprite('iz450cutin_06', 5)
    sprite('iz450cutin_07', 5)
    sprite('iz450cutin_08', 5)
    sprite('iz450cutin_09', 5)
    sprite('iz450cutin_10', 5)
    sprite('iz450cutin_11', 5)
    sprite('iz450cutin_12', 5)
    sprite('iz450cutin_13', 5)
    sprite('iz450cutin_14', 5)
    sprite('iz450cutin_15', 5)
    CreateObject('AST_2ndAurafront', 0)
    CreateObject('AST_2ndAuraback', 1)
    sprite('iz450cutin_16', 4)
    sprite('iz450cutin_17', 4)
    sprite('iz450cutin_18', 4)
    sprite('iz450cutin_19', 4)
    sprite('iz450cutin_20', 4)
    sprite('iz450cutin_21', 4)
    sprite('iz450cutin_22', 4)
    sprite('iz450cutin_23', 4)
    sprite('iz450cutin_24', 4)
    sprite('iz450cutin_25', 4)
    physicsYImpulse(0)

@State
def iz450_shield():

    def upon_IMMEDIATE():
        RenderLayer(4)
        BlendMode_Normal()
    sprite('iz450_26ex', 45)

@State
def iz450_shieldlight():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('iz450_29ex', 20)
    CharacterFlash(16777215, 15, 1)
    sprite('iz450_29ex', 5)
    ConstantAlphaModifier(-50)
    ParticleSize(1500)
    CallCustomizableParticle('izef_shieldDel', 0)
    ParticleSize(1500)
    CallCustomizableParticle('izef_shieldDel', 1)

@State
def iz450dammy():

    def upon_IMMEDIATE():
        RenderLayer(0)
        BlendMode_Normal()
        AddX(-215000)
        AddY(-102000)
    sprite('iz450_26', 5)
    CreateObject('iz450_shield', -1)
    CreateObject('AST_3rdAurafront', 0)
    CreateObject('AST_3rdAuraback', 1)
    sprite('iz450_27', 5)
    SmartVoiceline('iz293')
    sprite('iz450_28', 5)
    sprite('iz450_26', 5)
    sprite('iz450_27', 5)
    sprite('iz450_28', 5)
    sprite('iz450_26', 5)
    sprite('iz450_27', 5)
    sprite('iz450_28', 5)
    sprite('iz450_29', 10)
    CreateObject('iz450_shieldlight', -1)
    sprite('iz450_30', 5)
    sprite('iz450_31', 5)
    PassbackAddActionMarkToFunction('AST_3rdAurafront', 32)
    PassbackAddActionMarkToFunction('AST_3rdAuraback', 32)
    sprite('iz450_32', 5)
    PrivateSE('izse_05')
    sprite('iz450_33', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    ParticleLayer(5)
    ParticleRotationAngle(-20000)
    CallCustomizableParticle('izef_ASTptcCharget', 0)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    CreateObject('izef_ah_javelinwind', -1)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    SmartVoiceline('iz294')
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    CreateObject('izef_ah_javelin', 0)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    SmartVoiceline('iz295')
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    ParticleRotationAngle(-55000)
    ParticleSize(1500)
    ParticleLayer(1)
    CallCustomizableParticle('izef_ASTcharge', 1)
    ParticleSize(1000)
    ParticleRotationAngle(-5000)
    ParticleLayer(1)
    CallCustomizableParticle('izef_ASTcharge', 2)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    CreateObject('izef_ah_javelin_backfire', 0)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_37', 5)
    sprite('iz450_38', 5)
    sprite('iz450_39', 5)
    sprite('iz450_40', 5)
    ParticleSize(1200)
    ParticleRotationAngle(-20000)
    ParticleLayer(5)
    CallCustomizableParticle('izef_ah_javelinbackfire', 0)
    sprite('iz450_41', 5)
    AddX(-3000)
    AddY(-2000)
    physicsXImpulse(-5000)
    physicsYImpulse(-2000)
    PassbackAddActionMarkToFunction('izef_ah_javelin_backfire', 32)
    sprite('iz450_42', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz450_43', 5)
    XImpulseAcceleration(40)
    YAccel(40)
    PassbackAddActionMarkToFunction('izef_ah_javelin_backfire', 33)
    sprite('iz450_41', 5)
    XImpulseAcceleration(30)
    YAccel(30)
    sprite('iz450_42', 5)
    XImpulseAcceleration(20)
    YAccel(20)
    sprite('iz450_43', 5)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('iz450_41', 5)
    sprite('iz450_42', 5)

@State
def izef_ah_javelinwind():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ASTwindA.DIG', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        RenderLayer(5)
        BlendMode_Add()
        XPositionRelativeFacing(-400000)
        AddY(400000)
        SetScaleX(200)
        SetScaleY(80)
        RotationAngle(70000)
    sprite('null', 11)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    SetScaleSpeed(100)
    sprite('null', 9)
    SetScaleSpeed(0)
    sprite('null', 40)
    AlphaValue(160)
    ConstantAlphaModifier(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)
    SetScaleSpeedY(30)
    SetScaleXPerFrame(100)

@State
def izef_ah_javelin():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin.DIG', '')
        RemoveOnCallStateEnd(3)
        RenderLayer(5)
        BlendMode_Normal()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(24)
    Size(1400)
    RotationAngle(-11000)
    AddY(60000)
    AddX(-90000)
    sprite('null', 20)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('null', 120)
    CreateParticle('izef_shot_haneopen', -1)
    sprite('null', 20)
    label(0)
    sprite('null', 32767)
    physicsYImpulse(60000)
    AlphaValue(0)
    physicsXImpulse(150000)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def izef_ah_cloud():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_cloud.DIG', '')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        AddY(7800000)
        RenderLayer(2)
        AlphaValue(80)
    sprite('null', 550)

@State
def izef_ah_javelin2():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin_01.DIG', '')
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        AddX(-100000)
        AddY(-50000)
        RenderLayer(2)
        Flip()
    sprite('null', 38)
    sprite('null', 10)
    ScreenShake(15000, 15000)
    sprite('null', 10)
    CreateObject('izef_ah_kirikaeWhite', -1)
    sprite('null', 1)
    AlphaValue(0)

@State
def izef_ah_javelin3():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin_02.DIG', '')
        BlendMode_Normal()
        IgnoreFinishStop(1)
        AddY(180000)
        Size(1200)
        SetZVal(-1000)
        RenderLayer(4)
    sprite('null', 30)
    sprite('null', 10)
    AlphaValue(0)
    CreateParticle('izef_ahfinalhit', -1)
    sprite('null', 60)
    CreateObject('izef_ah_killwhite', -1)

@State
def izef_ah_Ryuhai():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(3)
        SetPosXByScreenPer(50)
        BlendMode_Normal()
        Eff3DEffect('izef_ah_kirikae', '')
    sprite('null', 30)

@State
def izef_ah_kirikaeWhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(3)
        SetPosXByScreenPer(50)
        Size(10000)
        BlendMode_Normal()
        ColorForTransition(4278190080)
        AlphaValue(0)
    sprite('vr_white', 5)
    ConstantAlphaModifier(51)
    sprite('vr_white', 8)
    sprite('vr_white', 5)
    ConstantAlphaModifier(-51)

@State
def izef_ah_killwhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(3)
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
def izef_ah_javelin_backfire():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin_backfire.DIG', '')
        RemoveOnCallStateEnd(3)
        RenderLayer(5)
        BlendMode_Add()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    Size(1400)
    AlphaValue(0)
    ConstantAlphaModifier(24)
    RotationAngle(-21000)
    sprite('null', 140)
    RotationAngle(-21000)
    label(0)
    sprite('null', 32767)
    physicsYImpulse(60000)
    physicsXImpulse(150000)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def AstWhitefinish():

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
    sprite('vr_white', 15)
    sprite('vr_white', 30)
    ConstantAlphaModifier(51)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-20)

@State
def izef_ah_javelin00():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin.DIG', '')
        RenderLayer(0)
        RotationAngle(-30000)
        Size(2000)
        sendToLabelUpon(32, 1)
    sprite('null', 30)
    AddX(-1240000)
    AddY(-475000)
    sprite('null', 10)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    sprite('null', 65)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 5)
    physicsYImpulse(8000)
    physicsXImpulse(15000)
    sprite('null', 32767)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def izef_ah_javelin_backfire00():

    def upon_IMMEDIATE():
        Eff3DEffect('izef_ah_javelin_backfire.DIG', '')
        RenderLayer(0)
        RotationAngle(-30000)
        Size(2000)
        sendToLabelUpon(32, 1)
    sprite('null', 30)
    AddX(-1240000)
    AddY(-475000)
    sprite('null', 10)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    sprite('null', 65)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 5)
    physicsYImpulse(8000)
    physicsXImpulse(15000)
    sprite('null', 32767)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def ASTbg():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('izef_ah_javelin_sky.DIG', '')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(2)
        AbsoluteY(250000)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    LinkParticle('izef_shot_ahspeed')
    label(1)
    sprite('null', 1)
    AlphaValue(0)

@State
def AstralHeatNotKillObject():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        HitAnywhere(1)
        AttackLevel_(4)
        AirPushbackY(0)
        Hitstop(3)
        DefeatOpponentBehavior(1)
        PushbackX(0)
        AirPushbackX(0)
        YImpulseBeforeWallbounce(0)
        Unknown11101(10)
        Hitstun(1200)
        UsePunchHitspark(1)
        Visibility(1)
    sprite('vrASTact', 1)
    TeleportToObject(22)

@State
def AstralHeatKillObject():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        HitAnywhere(1)
        AttackLevel_(4)
        Damage(27000)
        MinimumDamage(100)
        AirPushbackY(0)
        Hitstop(0)
        DefeatOpponentBehavior(3)
        PushbackX(0)
        AirPushbackX(0)
        YImpulseBeforeWallbounce(100000)
        DefeatOpponentBehavior(3)
        UseSlashHitspark(1)
        Visibility(1)
    sprite('vrASTact', 1)
    TeleportToObject(22)

@State
def Twindrive0():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        CallObject('IzEffTwinDrive')
        SLOT_59 = 0
        PaletteIndex(1)
        ColorForTransition(4278255488)
    label(0)
    if (SLOT_60 == 1):
        CreateParticle('izef_twindrivePtc_f', 0)
    if (SLOT_60 == 2):
        CreateParticle('izef_twindrivePtc_b', 0)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def Twindrive1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        CallObject('IzEffTwinDrive')
        SLOT_59 = 1
        PaletteIndex(1)
        ColorForTransition(4278255488)
    label(0)
    if (SLOT_60 == 1):
        CreateParticle('izef_twindrivePtc_f', -1)
    if (SLOT_60 == 2):
        CreateParticle('izef_twindrivePtc_b', -1)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def TwindriveParts_Front0():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        ColorForTransition(4278255488)
        SetZVal(-500)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
    sprite('vr_light', 3)
    CreateParticle('izef_twindrivePtc_f', 0)

@State
def iz601amourlight():

    def upon_IMMEDIATE():
        RenderLayer(4)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrizef601_09', 7)
    sprite('vrizef601_10', 7)
    ConstantAlphaModifier(-20)
    sprite('vrizef601_11', 7)

@State
def iz601swdlight():

    def upon_IMMEDIATE():
        RenderLayer(4)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrizef601_18', 7)
    ConstantAlphaModifier(-20)
    sprite('vrizef601_19', 7)

@State
def EntryFallSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        SetZVal(500)
        BlendMode_Normal()
        AbsoluteY(760000)
        AddX(-140000)
    sprite('iz601_f00', 12)
    physicsYImpulse(-60000)
    sprite('iz601_f00', 5)
    physicsYImpulse(-2000)
    CallCustomizableParticle('izef_drivecircle', -1)
    sprite('iz601_f00', 5)
    physicsYImpulse(-1000)
    sprite('iz601_f00', 10)
    physicsYImpulse(-500)
    sprite('iz601_f00', 10)
    CreateParticle('izef_entrylightA', 0)
    sprite('iz601_f00', 5)
    sprite('iz601_f00', 12)
    sprite('iz601_f00', 6)
    CreateParticle('izef_entrylight01', 0)

@State
def EventJNVsRCDownLoop():
    PaletteIndex(7)
    XPositionRelativeFacing(140000)
    sendToLabelUpon(32, 1)
    label(0)
    sprite('jn063_09', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    SetZVal(-500)
    ScreenCollision(0)
    BlendMode_Normal()
    sprite('jn063_09', 26)
    CreateParticle('story_rc_teni', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('jn063_09', 1)
    XPositionRelativeFacing(-500000)
    sprite('null', 32767)
    loopRest()

@State
def EventTBYoroke():
    sendToLabelUpon(32, 1)
    PaletteIndex(3)
    label(0)
    sprite('tb070_02', 5)
    sprite('tb070_03', 5)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('null', 32767)
    loopRest()

@State
def BurstDDTwindrive0():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        CallObject('IzEffTwinDrive')
        SLOT_59 = 0
        PaletteIndex(1)
        ColorForTransition(4278255488)
    label(0)
    if (SLOT_60 == 1):
        CreateParticle('izef_twindrivePtc_f', 0)
    if (SLOT_60 == 2):
        CreateParticle('izef_twindrivePtc_b', 0)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def BurstDDTwindrive1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        CallObject('IzEffTwinDrive')
        SLOT_59 = 1
        PaletteIndex(1)
        ColorForTransition(4278255488)
    label(0)
    if (SLOT_60 == 1):
        CreateParticle('izef_twindrivePtc_f', -1)
    if (SLOT_60 == 2):
        CreateParticle('izef_twindrivePtc_b', -1)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def BurstDDFunnel():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(4)
        Damage(450)
        AirUntechableTime(100)
        Hitstun(100)
        Hitstop(3)
        PushbackX(4900)
        AttackP2(100)
        UseSlashHitspark(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        HitAnywhere(1)
        OnlyHitPlayer(1)
        DamageFromStateOnly('BurstDDFunnel')
        CHStateIfCHStart(3)

        def upon_32():
            sendToLabel(100)
    sprite('iz440_f05', 1)
    CreateObject('BurstDDTwindrive0', -1)
    CreateObject('BurstDDTwindrive1', -1)
    sprite('iz440_f05', 2)
    sprite('iz440_f06', 3)
    sprite('iz440_f07', 3)
    sprite('iz440_f08', 3)
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    CreateObject('BurstDDSlash', -1)
    CommonSE('006_swing_blade_1')
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    ObjectUpon(3, 32)
    sprite('iz440_f10', 2)
    sprite('iz440_f11', 2)
    sprite('iz440_f13', 2)
    sprite('iz440_f14', 2)
    sprite('iz440_f15', 2)
    sprite('iz440_f16', 2)
    sprite('iz440_f17', 2)
    sprite('iz440_f18', 2)
    sprite('iz440_f19', 2)
    sprite('iz440_f20', 3)
    CreateObject('BurstDDSlash2', -1)
    CommonSE('006_swing_blade_1')
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    DamageFromStateOnly('BurstDDFunnelLastAtk')
    sprite('iz440_f19', 5)
    sprite('iz440_f21', 5)
    sprite('iz440_f23', 5)
    ObjectUpon(3, 33)
    sprite('iz440_f24', 6)
    sprite('iz440_f25', 6)
    sprite('iz440_f26', 6)
    sprite('iz440_f27', 6)
    sprite('iz440_f28', 9)
    sprite('iz440_f28a', 3)
    sprite('iz440_f28b', 2)
    CreateParticle('izef_440fwarp00', 0)
    CreateParticle('izef_440fwarp00', 1)
    PrivateSE('izse_04')
    sprite('null', 300)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    CreateObject('BurstDDFunnelLastAtk', -1)
    ObjectUpon(1, 32)
    CreateObject('BurstDDFunnelLastAtk', -1)
    ObjectUpon(1, 33)
    ExitState()
    label(100)
    sprite('iz440_f05', 2)
    sprite('iz440_f06', 3)
    sprite('iz440_f07', 3)
    sprite('iz440_f08', 3)
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    CreateObject('BurstDDSlashEX', -1)
    CommonSE('006_swing_blade_2')
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    PassbackAddActionMarkToFunction('BurstDDSlashEX', 32)
    ObjectUpon(3, 32)
    sprite('iz440_f10', 2)
    sprite('iz440_f11', 2)
    sprite('iz440_f13', 2)
    sprite('iz440_f14', 2)
    sprite('iz440_f15', 2)
    sprite('iz440_f16', 2)
    sprite('iz440_f17', 2)
    sprite('iz440_f18', 2)
    sprite('iz440_f19', 2)
    sprite('iz440_f20', 3)
    CreateObject('BurstDDSlashEX2', -1)
    CommonSE('006_swing_blade_2')
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    sprite('iz440_f19', 3)
    sprite('iz440_f20', 3)
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    sprite('iz440_f19', 3)
    sprite('iz440_f20', 3)
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    DamageFromStateOnly('BurstDDFunnelLastAtk')
    sprite('iz440_f19', 5)
    PassbackAddActionMarkToFunction('BurstDDSlashEX2', 32)
    sprite('iz440_f21', 5)
    sprite('iz440_f23', 5)
    ObjectUpon(3, 33)
    sprite('iz440_f24', 6)
    sprite('iz440_f25', 6)
    sprite('iz440_f26', 6)
    sprite('iz440_f27', 6)
    sprite('iz440_f28', 15)
    sprite('iz440_f28a', 3)
    sprite('iz440_f28b', 2)
    CreateParticle('izef_440fwarp00', 0)
    CreateParticle('izef_440fwarp00', 1)
    PrivateSE('izse_04')
    sprite('null', 300)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    CreateObject('BurstDDFunnelLastAtk', -1)
    ObjectUpon(1, 34)
    CreateObject('BurstDDFunnelLastAtk', -1)
    ObjectUpon(1, 35)
    ExitState()

@State
def BurstDDFunnelLastAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1500)
        AttackType(4)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(35000)
        UseSlashHitspark(1)
        AttackP2(100)
        VoodooDamageMultiplier(2)
        TeleportToObject(22)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        CHStateIfCHStart(3)
        OnlyHitPlayer(1)
        AttackOff()

        def upon_32():
            AddX(-300000)
            EndAttack()

        def upon_33():
            AddX(300000)

        def upon_34():
            Damage(2400)
            AddX(-300000)
            EndAttack()
            sendToLabel(100)

        def upon_35():
            Damage(2400)
            AddX(300000)
            sendToLabel(100)

        def upon_OPPONENT_HIT():
            AddCombo(1)
    sprite('null', 1)
    AddY(400000)
    sprite('null', 4)
    sprite('iz440_f29warp01', 2)
    ForceFaceSprite()
    Flip()
    sprite('iz440_f29warp00', 2)
    sprite('iz440_f29ex01', 3)
    CreateObject('BurstDDSordEff', -1)
    CreateObject('BurstDDTwindrive0', -1)
    sprite('iz440_f29ex01', 5)
    CreateParticle('izef_440fwarp00', 0)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    sprite('iz440_f29ex01', 7)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex01', 7)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex01', 7)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 1)
    AlphaValue(255)
    physicsXImpulse(-150000)
    physicsYImpulse(-100000)
    PassbackAddActionMarkToFunction('BurstDD_MagicCircle', 32)
    sprite('iz440_f29ex02', 1)
    RefreshMultihit()
    sprite('iz440_f29ex02', 2)
    CreateObject('BurstDDLastAtk', -1)
    sprite('iz440_f29ex02', 4)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    PassbackAddActionMarkToFunction('BurstDDLastAtk', 32)
    ExitState()
    label(100)
    sprite('null', 4)
    PrivateSE('izse_12')
    sprite('iz440_f29warp01', 2)
    ForceFaceSprite()
    Flip()
    CreateParticle('izef_440fwarp00', 0)
    sprite('iz440_f29warp00', 2)
    sprite('iz440_f29ex01', 3)
    CreateObject('BurstDDSordEff', -1)
    CreateObject('BurstDDTwindrive0', -1)
    sprite('iz440_f29ex01', 5)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    sprite('iz440_f29ex01', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex01', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex01', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 1)
    AlphaValue(255)
    physicsXImpulse(-150000)
    physicsYImpulse(-100000)
    PassbackAddActionMarkToFunction('BurstDD_MagicCircle', 32)
    sprite('iz440_f29ex02', 1)
    RefreshMultihit()
    sprite('iz440_f29ex02', 2)
    CreateObject('BurstDDLastAtkEX', -1)
    sprite('iz440_f29ex02', 4)
    AlphaValue(0)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    PassbackAddActionMarkToFunction('BurstDDLastAtkEX', 32)
    ExitState()

@State
def BurstDD_MagicCircle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('izef_lockmagic2.DIG', '')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        ColorForTransition(4294967220)

        def upon_FRAME_STEP():
            TeleportToObject(22)
            AddX(-25000)
            AddY(200000)

        def upon_32():
            sendToLabel(98)
    sprite('null', 32767)
    loopRest()
    label(98)
    sprite('null', 1)
    E0EAEffectPosition(0)
    sprite('null', 4)
    ConstantAlphaModifier(-51)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)

@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)

        def upon_FRAME_STEP():
            TeleportToObject(3)
            ForceFaceSprite()
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 2)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 22)
            CopyFromRightToLeft(23, 2, 53, 22, 2, 22)
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 0)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 300)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)

@State
def BurstDDSlash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrizef440_00', 3)
    sprite('vrizef440_01', 3)
    sprite('vrizef440_02', 3)
    sprite('vrizef440_03', 3)
    sprite('vrizef440_00', 2)
    ConstantAlphaModifier(-48)
    sprite('vrizef440_01', 2)

@State
def BurstDDSlash2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrizef440_10', 3)
    sprite('vrizef440_11', 3)
    sprite('vrizef440_12', 3)
    sprite('vrizef440_13', 5)
    ConstantAlphaModifier(-31)
    sprite('vrizef440_12', 3)

@State
def BurstDDSlashEX():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vrizef440_00', 3)
    sprite('vrizef440_01', 3)
    sprite('vrizef440_02', 3)
    ScreenShake(10000, 10000)
    sprite('vrizef440_03', 3)
    gotoLabel(0)
    label(1)
    sprite('vrizef440_03', 3)
    ConstantAlphaModifier(-36)
    sprite('vrizef440_00', 2)
    sprite('vrizef440_01', 2)

@State
def BurstDDSlashEX2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vrizef440_10', 3)
    sprite('vrizef440_11', 3)
    sprite('vrizef440_12', 3)
    ScreenShake(10000, 10000)
    sprite('vrizef440_13', 3)
    gotoLabel(0)
    label(1)
    sprite('vrizef440_13', 5)
    ConstantAlphaModifier(-51)

@State
def BurstDDLastAtk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        Size(600)
        AddY(250000)
        Eff3DEffect('izef_440cross_00', '')
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 1)
    sprite('null', 6)
    SetScaleSpeed(150)
    ScreenShake(10000, 10000)
    CreateParticle('izef_440open', -1)
    label(0)
    sprite('null', 1)
    AddScale(200)
    SetScaleSpeed(0)
    sprite('null', 1)
    AddScale(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    CreateParticle('izef_440cross', -1)
    sprite('null', 2)
    CreateParticle('izef_440endkira_posL', -1)
    CreateParticle('izef_440endkira_posR', -1)

@State
def BurstDDLastAtkEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        Size(600)
        AddY(250000)
        Eff3DEffect('izef_440cross_01', '')
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 1)
    sprite('null', 6)
    SetScaleSpeed(200)
    ScreenShake(10000, 10000)
    ParticleSize(1300)
    CallCustomizableParticle('izef_440openEX', -1)
    label(0)
    sprite('null', 1)
    AddScale(200)
    SetScaleSpeed(0)
    sprite('null', 1)
    AddScale(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    CreateParticle('izef_440crossEX', -1)
    sprite('null', 2)
    ParticleSize(1300)
    CallCustomizableParticle('izef_440endkiraEX_posL', -1)
    ParticleSize(1300)
    CallCustomizableParticle('izef_440endkiraEX_posR', -1)

@State
def BurstDDRetrunEff():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrizef440_20', 4)
    sprite('vrizef440_21', 2)
    sprite('vrizef440_22', 2)
    sprite('vrizef440_23', 5)
    ConstantAlphaModifier(-51)

@State
def BurstDDSlashEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
    sprite('vrizef440_30', 2)
    sprite('vrizef440_31', 2)

@State
def BurstDDSlashEff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        callSubroutine('ShotColorSwitch')
        BlendMode_Add()
        RenderLayer(11)
    sprite('vrizef440_50', 6)
    sprite('vrizef440_51', 4)
    sprite('vrizef440_52', 4)

@State
def BurstDDSordEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        PaletteIndex(2)
    sprite('vrizef440_40', 7)
    sprite('vrizef440_41', 6)
    sprite('vrizef440_42', 6)
    sprite('vrizef440_43', 4)
    sprite('vrizef440_44', 4)
    sprite('vrizef440_45', 32767)

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_IZDummy():
    sprite('iz063_11', 32767)