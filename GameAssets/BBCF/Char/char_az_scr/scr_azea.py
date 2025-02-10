@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AZ.DIG', '')
        RenderLayer(5)
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
def EMB_AZ_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AZ.DIG', '')
        RenderLayer(5)
        Size(1500)
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
def EMB_AZ_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_AZ.DIG', '')
        RenderLayer(5)
        Size(1500)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(2533294080, 10)
    sprite('null', 10)
    ColorTransition(2533304360, 10)
    sprite('null', 10)
    ColorTransition(2533340340, 10)
    sprite('null', 10)
    ColorTransition(2533294080, 10)
    sprite('null', 80)


@State
def az406_dummy():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(1000)
        AirPushbackX(-3000)
        AirPushbackY(23000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        UsePunchHitspark(1)
        Hitstop(3)
        Visibility(1)
        SameMoveProration(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpulseBeforeWallbounce(20)
            NonCornerWallbounce(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickDuration(30)
            if SLOT_4 > 1:
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                PushSpeedX()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)


@State
def az406_dummy2():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(900)
        AirPushbackX(1000)
        AirPushbackY(26000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        UsePunchHitspark(1)
        Hitstop(3)
        Visibility(1)
        SameMoveProration(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpulseBeforeWallbounce(20)
            NonCornerWallbounce(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickDuration(30)
            if SLOT_4 > 1:
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                PushSpeedX()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)


@State
def rocktest():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(2000)
        AbsoluteY(0)
    sprite('null', 1)
    sprite('null', 0)
    CreateObject('hibiware', -1)
    ScreenShake(8000, 8000)
    sprite('null', 5)
    Eff3DEffect('azef_406jiware.DIG', '')
    CreateParticle('azef_406_stone', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-10)
    sprite('null', 14)


@State
def hibiware():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        AbsoluteY(0)
    sprite('null', 4)
    Eff3DEffect('azef_hibiware.DIG', '')
    sprite('null', 8)
    ConstantAlphaModifier(-26)


@State
def __203swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Size(900)
    sprite('null', 14)
    CreateObject('203yugami', -1)
    Eff3DEffect('azef_203swing00.DIG', '')
    FaceSpawnLocation()


@State
def __203yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddX(-25000)
        Size(900)
    sprite('vr_azef203_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(35000)
    Unknown3059(-2500)


@State
def __213swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        Size(900)
    sprite('null', 14)
    CreateObject('213yugami', -1)
    Eff3DEffect('azef_213swing00.DIG', '')
    FaceSpawnLocation()


@State
def __213yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddX(-25000)
        Size(900)
    sprite('vr_azef213_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(35000)
    Unknown3059(-2500)


@State
def __213rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_402rock.DIG', '')
        Size(1000)
        AddX(-20000)
        AddY(15000)
    sprite('null', 5)
    sprite('null', 10)
    ParticleSize(700)
    CallCustomizableParticle('azef_402rocksmoke_pos', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __253swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        Size(900)
    sprite('null', 6)
    Eff3DEffect('azef_253swing00.DIG', '')
    FaceSpawnLocation()


@State
def __253yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddX(-50000)
        AddY(30000)
        Size(900)
    sprite('vr_azef203_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(17500)
    Unknown3059(-2500)


@State
def __232rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        AddX(400000)
        Eff3DEffect('azef_232rock00.DIG', '')
    sprite('null', 1)
    AddY(-40000)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    AddY(40000)
    sprite('null', 2)
    AlphaValue(0)
    CreateObject('232rock01', -1)
    sprite('null', 4)
    CreateObject('232rock02', -1)
    sprite('null', 2)
    CreateObject('232rock03', -1)
    sprite('null', 20)
    CreateObject('232rock04', -1)


@State
def __232rock01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        Eff3DEffect('azef_232rock01.DIG', '')
        FaceSpawnLocation()
    sprite('null', 2)


@State
def __232rock02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        Eff3DEffect('azef_232rock02.DIG', '')
    sprite('null', 4)


@State
def __232rock03():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        AddX(-150000)
        AddY(-5000)
        Eff3DEffect('azef_232rock03.DIG', '')
        LinkParticle('azef_rockshadow_00')
    sprite('null', 2)


@State
def __232rock04():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1500)
        AddX(-150000)
        AddY(-5000)
        Eff3DEffect('azef_232rock04.DIG', '')
        LinkParticle('azef_rockshadow_00')
    sprite('null', 5)
    CreateParticle('azef_232brokerock_rock2', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __232rock_col():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(1100)
        ProjectileLevel(1)
        StrikeProjectileLevel(1)
        MoveAttributes(0, 1, 0, 0, 0)
        Hitstop(0)
        AttackP1(90)
        AttackP2(79)
        BonusProration(110)
        Hitstun(22)
        AirUntechableTime(50)
        EnemyHitstopAddition(12, 0, 5)
        GroundedHitstunAnimation(9)
        AirPushbackX(8800)
        AirPushbackY(43000)
        Visibility(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpulseBeforeWallbounce(20)
            NonCornerWallbounce(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickDuration(30)
            if SLOT_4 > 1:
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                PushSpeedX()
        HitsPerCall(1, 1, 1, 0, 1, 0, 1, 1)

        def upon_54():
            sendToLabel(580)
        SetActionMark(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk2C', 32)
    sprite('null', 5)
    sprite('vr_azef232_00col', 4)
    sprite('vr_azef232_01col', 2)
    label(580)
    sprite('null', 2)


@State
def __255swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(0)
        AddY(230000)
    sprite('null', 3)
    sprite('null', 3)
    AlphaValue(255)
    Eff3DEffect('azef_255swing00.DIG', '')
    FaceSpawnLocation()


@State
def __400impact():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_400impact00.DIG', '')
        FaceSpawnLocation()
        AddY(280000)
        AddX(200000)
        AlphaValue(255)
        Size(1700)
    sprite('null', 10)
    CreateParticle('azef_400impact_pos', -1)
    CreateObject('400yugami', -1)
    sprite('null', 5)


@State
def __400yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Size(1200)
        AddX(30000)
        AddY(15000)
    sprite('vr_azef400_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(50000)
    Unknown3059(-3000)


@State
def __401swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_401impact00.DIG', '')
        FaceSpawnLocation()
        Size(1700)
        AlphaValue(200)
    sprite('null', 10)
    sprite('null', 5)


@State
def azef_guardcrash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_401guardcrash00.DIG', '')
        FaceSpawnLocation()
        Size(1700)
        AlphaValue(200)
        RedColorValue(0)
    sprite('null', 10)
    sprite('null', 5)


@State
def azef_guardcrash_hold():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 4)
    CreateParticle('azef_guardcrash_hold', -1)
    gotoLabel(0)


@State
def azef_dustattack_hold():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 4)
    CreateParticle('azef_dustattack_hold', -1)
    gotoLabel(0)


@State
def __402rock1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_402rock.DIG', '')
        Size(1500)
        AddX(-20000)
        AddY(15000)
    sprite('null', 5)
    sprite('null', 10)
    CreateParticle('azef_402rocksmoke_pos', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __402swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('azef_402swing.DIG', '')
        FaceSpawnLocation()
        Size(1000)
        AlphaValue(255)
        AddY(300000)
        AddX(100000)
    sprite('null', 14)


@State
def __403swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('azef_403swing.DIG', '')
        FaceSpawnLocation()
        Size(700)
        AlphaValue(255)
    sprite('null', 14)
    CreateParticle('azef_403backadd_00', -1)
    CreateObject('403yugami', -1)


@State
def __403yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(230000)
        AddX(55000)
    sprite('vr_azef403_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(40000)
    Unknown3059(-2500)


@State
def __404tame():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('azef_404tame_addcircle')
        AddY(250000)
        AddX(-50000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __404swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_404swing.DIG', '')
        AddY(250000)
        AddX(250000)
        AlphaValue(0)
    sprite('null', 1)
    sprite('null', 1)
    AlphaValue(255)
    CreateParticle('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 8)
    CreateParticle('azef_blood_01', -1)


@State
def __404nigiyakasi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(250000)
        AddX(250000)
    sprite('null', 5)
    LinkParticle('azef_404impact_thunder')
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __405smoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
    CreateParticle('azef_405tossin_smoke', -1)
    label(0)
    sprite('null', 1)
    CreateParticle('azef_405tossin', -1)
    gotoLabel(0)


@State
def __405rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_405rock00.DIG', '')
        Size(1125)
        AddX(-15000)
        AddY(15000)
    sprite('null', 5)
    sprite('null', 10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __405punch():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        Size(800)
    sprite('null', 15)
    Eff3DEffect('azef_405punch00.DIG', '')
    FaceSpawnLocation()


@State
def __405yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(248000)
        AddX(-64000)
        Size(1200)
    sprite('vr_azef405_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(35000)
    Unknown3059(-2500)


@State
def __032rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_405rock00.DIG', '')
        Size(625)
        AddX(-20000)
        AddY(15000)
    sprite('null', 5)
    sprite('null', 10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def azef_rlah_circle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 30)
    AlphaValue(0)
    sprite('null', 32767)
    LinkParticle('rlef_ah_az_circle')
    ConstantAlphaModifier(16)


@State
def __407aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Visibility(1)
        Eff3DEffect('azef_aura00', '')
        FaceSpawnLocation()
    label(1)
    sprite('vr_azef407_efpos00', 1)
    CreateObject('407yugami', -1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 0)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 2)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 3)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 4)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya2', 2)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 3)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 4)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya2', 5)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 6)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 7)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CreateObject('407boya2', 8)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 9)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 10)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CreateObject('407boya2', 11)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 12)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 13)
    CreateObject('407boya2', 13)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 14)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 15)
    CreateObject('407boya2', 15)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 16)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 17)
    CreateObject('407boya2', 17)
    sprite('vr_azef407_efpos00', 5)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 18)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 19)
    CreateObject('407boya2', 19)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 0)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 2)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 3)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 4)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya', 1)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 3)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 4)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya', 2)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 6)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 7)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CreateObject('407boya', 7)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 9)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 10)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CreateObject('407boya', 8)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 12)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 13)
    CreateObject('407boya', 11)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 14)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 15)
    CreateObject('407boya', 14)
    sprite('vr_azef407_efpos00', 1)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 16)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 17)
    CreateObject('407boya', 16)
    sprite('vr_azef407_efpos00', 5)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 18)
    ParticleLayer(12)
    CallCustomizableParticle('azef_407backaura_02', 19)
    CreateObject('407boya', 18)
    gotoLabel(1)
    label(0)
    sprite('vr_azef407_efpos00', 5)
    ConstantAlphaModifier(-51)


@State
def __407boya():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(500)
        Eff3DEffect('azef_aura01', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        RenderLayer(11)
        AlphaValue(0)
    sprite('null', 19)
    ConstantAlphaModifier(26)
    SetScaleSpeedY(20)
    RandAddScaleY(-300, 500)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __407boya2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(500)
        Eff3DEffect('azef_aura01', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        RenderLayer(11)
        Flip()
        AlphaValue(0)
    sprite('null', 19)
    ConstantAlphaModifier(26)
    SetScaleSpeedY(20)
    RandAddScaleY(-300, 500)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __407yugami():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(180000)
        AddX(40000)
    sprite('vr_azef407_yugami', 60)
    SetScaleSpeed(10)
    physicsYImpulse(-2000)
    ConstantAlphaModifier(-9)
    ParticleTransparency(1)
    PlayerTransparency(10000)
    Unknown3059(-1500)


@State
def __407Kyushu():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(250000)
        AddX(140000)
        Size(1300)
    sprite('null', 25)
    LinkParticle('azef_407kyushu_tubusub')
    CommonSE('022_magiccircle_b')


@State
def __407Mutekicol():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Visibility(1)
        setInvincible(1)
        CollidableInvincibility(1)
        PretendNoGuardPointIfFail(1)
        StrikeProjectilesBypass(0)
        DollInvincibility(0)
        GuardPoint_(1)

        def upon_GUARDPOINT_ACTIVATION():
            ObjectUpon(EVERY_FRAME, 32)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(GUARDPOINT_ACTIVATION)
            setInvincible(0)
            sendToLabel(0)
    sprite('az407_03ex', 32767)
    label(0)
    sprite('null', 3)


@State
def azef_409_fall():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        LinkParticle('azef_409punch')
    label(0)
    sprite('null', 2)
    CreateParticle('azef_409punch_add', -1)
    gotoLabel(0)


@State
def azef_409_rock():

    def upon_IMMEDIATE():
        Eff3DEffect('azef_406jiware.DIG', '')
        BlendMode_Normal()
        Size(1750)
        AbsoluteY(50000)
        AddX(100000)
    sprite('null', 5)
    CreateObject('azef_409_hibiware', -1)
    ParticleSize(845)
    CallCustomizableParticle('azef_406_stone', -1)
    sprite('null', 20)
    ConstantAlphaModifier(-10)


@State
def azef_409_hibiware():

    def upon_IMMEDIATE():
        Eff3DEffect('azef_hibiware.DIG', '')
        BlendMode_Normal()
        Size(1500)
        AbsoluteY(100000)
        RenderLayer(2)
    sprite('null', 4)
    sprite('null', 8)
    ConstantAlphaModifier(-26)


@State
def weakhit00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        RemoveOnCallStateEnd(2)
        AddY(150000)
        Size(2400)
        RenderLayer(4)
        FaceLeft()
    sprite('null', 30)
    LinkParticle('azef_weakhit_red')


@State
def weakhit01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        RemoveOnCallStateEnd(2)
        AddY(150000)
        Size(2400)
        RenderLayer(4)
        FaceLeft()
    sprite('null', 30)
    LinkParticle('azef_weakhit_yellow')


@State
def weakpoint01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(255)
        Size(2300)
        PaletteIndex(1)
        ColorFromPaletteIndex(16)
        Eff3DEffect('azef_weakpoint00.DIG', '')
        FaceSpawnLocation()

        def upon_16():
            PrivateFunction3(22, 0, 60000, 100, 1)
        RemoveOnContact(22)
        uponSendToLabel(32, 0)
    sprite('null', 20)
    CreateObject('weakstart01', -1)
    SetScaleSpeed(-27)
    sprite('null', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(300)


@State
def weakpoint00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(255)
        RotationAngle(180000)
        Size(2300)
        PaletteIndex(1)
        ColorFromPaletteIndex(17)
        Eff3DEffect('azef_weakpoint00.DIG', '')
        FaceSpawnLocation()

        def upon_16():
            PrivateFunction3(22, 0, -80000, 100, 1)
        RemoveOnContact(22)
        uponSendToLabel(32, 0)
    sprite('null', 20)
    CreateObject('weakstart00', -1)
    SetScaleSpeed(-25)
    sprite('null', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-27)
    SetScaleSpeed(300)


@State
def weakstart00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    uponSendToLabel(32, 0)
    sprite('null', 5)
    sprite('null', 30)
    LinkParticle('azef_weakhit_02')


@State
def weakstart01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    uponSendToLabel(32, 0)
    sprite('null', 5)
    sprite('null', 30)
    LinkParticle('azef_weakhit_03')


@State
def __408sphere():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddY(230000)
        AddX(20000)
        Eff3DEffect('azef_408tama', '')
        FaceSpawnLocation()
        AlphaValue(0)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        AttackP1(80)
        ProjectileLevel(2)
        Damage(1400)
        AirUntechableTime(30)
        AirPushbackX(54000)
        AirPushbackY(18000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        StarterRating(2)
        UsePunchHitspark(1)
        Hitstop(3)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 580)
        CancelIfPlayerHit(3)
        Visibility(1)
        LinkParticle('azef_408_ambient00')
        SameMoveProration(1)

        def upon_32():
            AttackLevel_(3)
            ProjectileLevel(2)
            Damage(1000)
            AirUntechableTime(40)
            AirPushbackX(54000)
            AirPushbackY(18000)
            GroundedHitstunAnimation(19)
            AirHitstunAnimation(19)
            Wallbounce(1)
            WallbounceReboundTime(1)

        def upon_33():
            SetActionMark(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpulseBeforeWallbounce(20)
            NonCornerWallbounce(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickDuration(30)
            if SLOT_4 > 1:
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                PushSpeedX()
    label(0)
    sprite('vr_azef408_col', 1)
    StartMultihit()
    AddX(60000)
    sprite('vr_azef408_col', 1)
    if SLOT_2:
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        PretendNoGuardPointIfFail(1)
        Unknown23142(1)
    sprite('vr_azef408_col', 7)
    CollidableInvincibility(0)
    sprite('vr_azef408_col', 1)
    CreateObject('408JizokuSmoke', -1)
    ConstantAlphaModifier(51)
    RefreshMultihit()
    sprite('vr_azef408_col', 3)
    physicsXImpulse(80000)
    gotoLabel(9)
    label(9)
    sprite('vr_azef408_col', 4)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    CreateObject('408sphereJizoku', -1)
    RefreshMultihit()
    label(580)
    sprite('vr_azef408_col', 5)
    DespawnEAEffect('408JizokuSmoke')
    physicsXImpulse(0)
    CreateParticle('azef_408_brake_tubu', -1)
    sprite('vr_azef408_col', 5)
    ConstantAlphaModifier(-51)


@State
def __408sphereStart():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        AddY(230000)
        AddX(130000)
    sprite('null', 5)
    CreateParticle('azef_407kyushu_tubusub', -1)
    sprite('null', 8)
    LinkParticle('azef_408_sub')
    SetScaleSpeed(30)
    physicsXImpulse(1500)


@State
def __408JizokuSmoke():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 2)
    CreateParticle('azef_408_jizokuaura_tubu', -1)
    gotoLabel(0)


@State
def __408sphereJizoku():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_408tama2', '')
        FaceSpawnLocation()
        RandAddRotation(-5000, 5000)
        DeviationY(-15000, 15000)
        RandAddScale(0, 2500)
        SetScaleY(1500)
        SetScaleX(2000)
        AlphaValue(255)
    sprite('null', 7)
    SetScaleSpeedY(-30)
    ConstantAlphaModifier(-37)


@State
def __430Cam():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 5)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    physicsXImpulse(14800)
    sprite('null', 30)
    physicsXImpulse(0)
    sprite('null', 20)
    physicsXImpulse(-3700)


@State
def __430HandAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 0)
    CreateParticle('azef_408handaura_add', 1)
    CreateObject('430Hand01', 0)
    CreateObject('430Hand01', 1)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 2)
    CreateParticle('azef_408handaura_add', 3)
    CreateObject('430Hand01', 2)
    CreateObject('430Hand01', 3)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 4)
    CreateParticle('azef_408handaura_add', 5)
    CreateObject('430Hand01', 4)
    CreateObject('430Hand01', 5)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 6)
    CreateParticle('azef_408handaura_add', 7)
    CreateObject('430Hand01', 6)
    CreateObject('430Hand01', 7)
    sprite('vr_azef430_efpos00', 2)
    CreateParticle('azef_408handaura_add', 8)
    CreateParticle('azef_408handaura_add', 9)
    CreateObject('430Hand01', 8)
    CreateObject('430Hand01', 9)
    sprite('vr_azef430_efpos00', 2)
    CreateParticle('azef_408handaura_add', 10)
    CreateParticle('azef_408handaura_add', 11)
    CreateObject('430Hand01', 10)
    CreateObject('430Hand01', 11)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 12)
    CreateParticle('azef_408handaura_add', 13)
    CreateObject('430Hand01', 12)
    CreateObject('430Hand01', 13)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 14)
    CreateParticle('azef_408handaura_add', 15)
    CreateObject('430Hand01', 14)
    CreateObject('430Hand01', 15)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 16)
    CreateParticle('azef_408handaura_add', 17)
    CreateObject('430Hand01', 16)
    CreateObject('430Hand01', 17)
    sprite('vr_azef430_efpos00', 3)
    CreateParticle('azef_408handaura_add', 18)
    CreateParticle('azef_408handaura_add', 19)
    CreateObject('430Hand01', 18)
    CreateObject('430Hand01', 19)
    sprite('vr_azef430_efpos00', 6)
    CreateParticle('azef_408handaura_add', 20)
    CreateParticle('azef_408handaura_add', 21)
    sprite('vr_azef430_efpos00', 6)
    CreateParticle('azef_408handaura_add', 22)
    CreateParticle('azef_408handaura_add', 23)
    sprite('vr_azef430_efpos00', 6)
    CreateParticle('azef_408handaura_add', 24)
    sprite('vr_azef430_efpos00', 7)
    CreateParticle('azef_408handaura_add', 25)
    CreateParticle('azef_408handaura_add', 26)
    sprite('vr_azef430_efpos00', 6)
    CreateParticle('azef_408handaura_add', 27)
    CreateParticle('azef_408handaura_add', 28)


@State
def __430BodyAura():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(2)
    sprite('vr_azef430_efpos01', 3)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    ParticleLayer(12)
    CallCustomizableParticle('azef_408handaura_add', 106)
    sprite('vr_azef430_efpos01', 3)
    CreateObject('430Hand02', 0)
    CreateObject('430Hand02', 1)
    CreateObject('430Hand02', 2)
    CreateObject('430Hand02', 3)
    CreateObject('430Hand02', 4)
    CreateObject('430Hand02', 5)
    CreateObject('430Hand02', 6)
    CreateObject('430Hand02', 7)


@State
def __430Hand01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(400)
        Eff3DEffect('azef_aura01', '')
        FaceSpawnLocation()
    sprite('null', 19)
    SetScaleSpeed(10)
    RandAddRotation(-45000, 45000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __430Hand02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(400)
        Eff3DEffect('azef_aura01', '')
        FaceSpawnLocation()
        AlphaValue(0)
    sprite('null', 5)
    sprite('null', 14)
    ConstantAlphaModifier(26)
    SetScaleSpeed(10)
    RandAddRotation(-45000, 45000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __430aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Visibility(1)
        uponSendToLabel(32, 0)
    label(1)
    sprite('vr_azef430_efpos02', 2)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 0)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 1)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 2)
    CreateObject('407boya', 0)
    CreateObject('430boya', 1)
    CreateObject('407boya', 2)
    sprite('vr_azef430_efpos02', 2)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 3)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 4)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya', 3)
    CreateObject('430boya', 4)
    CreateObject('407boya', 5)
    sprite('vr_azef430_efpos02', 2)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 6)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 7)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CreateObject('430boya', 6)
    CreateObject('407boya', 7)
    CreateObject('407boya2', 8)
    sprite('vr_azef430_efpos02', 3)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 9)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 10)
    ParticleLayer(2)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CreateObject('407boya', 9)
    CreateObject('430boya', 10)
    CreateObject('407boya', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    ConstantAlphaModifier(-51)


@State
def __430boya():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(500)
        Eff3DEffect('azef_aura01', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        RenderLayer(12)
        AlphaValue(0)
    sprite('null', 19)
    ConstantAlphaModifier(26)
    SetScaleSpeedY(20)
    RandAddScaleY(500, 1000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __430Atk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_430shock01', '')
        AddY(200000)
        AddX(200000)
        Size(300)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    SetScaleSpeed(50)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    SetScaleSpeed(5)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(-90)


@State
def __430shock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('azef_430shock00', '')
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(200000)
        AddX(200000)
        RenderLayer(2)
    sprite('null', 5)
    ScreenShake(3000, 3000)
    CreateObject('430shock01', -1)
    CreateObject('430Speed', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-26)
    sprite('null', 10)
    TriggerUponForState('430Speed', 32)
    sprite('null', 15)


@State
def __430shock01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RenderLayer(2)
    sprite('null', 45)
    LinkParticle('azef_408_tukihit_add2')


@State
def __430Speed():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    LinkParticle('azef_408_speedline_down')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __431ODAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Visibility(1)
        uponSendToLabel(32, 0)
        Eff3DEffect('azef_431aura.DIG', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        AlphaValue(0)
        Size(950)
    sprite('null', 10)
    CreateObject('431Odaura', -1)
    ConstantAlphaModifier(17)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    ConstantAlphaModifier(0)
    CallCustomizableParticle('azef_407backaura_02', 0)
    CallCustomizableParticle('azef_407backaura_02', 1)
    CallCustomizableParticle('azef_407backaura_02', 2)
    CallCustomizableParticle('azef_407backaura_02', 3)
    CallCustomizableParticle('azef_407backaura_02', 4)
    CallCustomizableParticle('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 6)
    CallCustomizableParticle('azef_407backaura_02', 7)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CallCustomizableParticle('azef_407backaura_02', 9)
    CallCustomizableParticle('azef_407backaura_02', 10)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CallCustomizableParticle('azef_407backaura_02', 13)
    CallCustomizableParticle('azef_407backaura_02', 14)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    TriggerUponForState('431Odaura', 32)
    ConstantAlphaModifier(-51)


@State
def __431Odaura():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AlphaValue(170)
        uponSendToLabel(32, 0)
        SetZVal(100)
    sprite('null', 5)
    label(1)
    sprite('vr_azef431_00', 3)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)
    gotoLabel(1)
    label(0)
    sprite('vr_azef431_00', 3)
    ConstantAlphaModifier(-26)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)


@State
def __431swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_431swing00', '')
        AddY(160000)
        AddX(350000)
        Size(2000)
    sprite('null', 10)
    CreateObject('431yugami', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431yugami():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('vr_azef431_yugami', 15)
    SetScaleSpeed(10)
    physicsYImpulse(-2000)
    ConstantAlphaModifier(-9)
    ParticleTransparency(1)
    PlayerTransparency(30000)
    Unknown3059(-1500)


@State
def __450neppaMatome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(150000)
    sprite('null', 1)
    CreateObject('450neppa00', -1)
    CreateParticle('azef_450neppa_circle', -1)
    sprite('null', 7)
    CreateObject('450neppa01', -1)
    sprite('null', 7)
    CreateObject('450neppa01', -1)
    sprite('null', 7)


@State
def __450neppa00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('azef_450neppa00', '')
        RemoveOnCallStateEnd(2)
    sprite('null', 20)
    sprite('null', 7)
    ConstantAlphaModifier(-51)


@State
def __450neppa01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('azef_450neppa00', '')
        RemoveOnCallStateEnd(2)
    sprite('null', 7)
    sprite('null', 7)
    ConstantAlphaModifier(-51)
    endState()


@State
def nepparock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        IgnoreScreenfreeze(1)
        Size(2000)
        AddX(160000)
        Eff3DEffect('azef_406jiware.DIG', '')
    sprite('null', 10)
    CreateParticle('azef_406_stone', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450swing():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('azef_400impact00.DIG', '')
        FaceSpawnLocation()
        AddX(30000)
        AlphaValue(255)
        SetScaleY(3200)
        SetScaleX(2400)
        Flip()
        Rotation(100000)
    sprite('null', 10)


@State
def __450rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('azef_rock', '')
        AddX(280000)
    sprite('null', 6)
    CreateObject('450smoke', -1)

    def RunOnObject_22():
        AddY(15000)
        setGravity(0)
    Rotation(3250)
    AddY(70000)
    sprite('null', 50)
    Rotation(1625)
    AddY(35000)

    def RunOnObject_22():
        AddY(30000)
    sprite('null', 40)
    Rotation(812)
    AddY(40000)

    def RunOnObject_22():
        AddY(30000)
    sprite('null', 40)
    Rotation(406)
    AddY(20000)

    def RunOnObject_22():
        AddY(15000)
    sprite('null', 60)

    def RunOnObject_22():
        AddY(15000)
    Rotation(203)
    AddY(10000)
    sprite('null', 20)
    CreateObject('AHsection', -1)
    physicsYImpulse(60000)

    def RunOnObject_22():
        AddY(15000)
        physicsYImpulse(100000)
        RenderLayer(2)


@State
def __450smoke():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        AddY(-30000)
        AddX(-20000)
    sprite('null', 6)
    CreateObject('450smokeb', -1)
    ParticleLayer(4)
    CallCustomizableParticle('azef_450stonesmoke_brust', -1)
    sprite('null', 50)
    ParticleLayer(4)
    CallCustomizableParticle('azef_450stonesmoke_stone2', -1)
    sprite('null', 40)
    ParticleLayer(4)
    CallCustomizableParticle('azef_450stonesmoke_stone2', -1)
    sprite('null', 40)
    ParticleLayer(4)
    CallCustomizableParticle('azef_450stonesmoke_stone2', -1)
    sprite('null', 60)
    ParticleLayer(4)
    CallCustomizableParticle('azef_450stonesmoke_stone2', -1)


@State
def __450smokeb():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        AddY(-30000)
        AddX(-20000)
    sprite('null', 6)
    ParticleLayer(2)
    CallCustomizableParticle('azef_450stonesmoke_bbrust', -1)
    sprite('null', 50)
    ParticleLayer(2)
    CallCustomizableParticle('azef_450stonesmoke_b', -1)
    sprite('null', 40)
    ParticleLayer(2)
    CallCustomizableParticle('azef_450stonesmoke_b', -1)
    sprite('null', 40)
    ParticleLayer(2)
    CallCustomizableParticle('azef_450stonesmoke_b', -1)
    sprite('null', 60)
    ParticleLayer(2)
    CallCustomizableParticle('azef_450stonesmoke_b', -1)


@State
def __450smokec():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        AddY(-100000)
        AddX(300000)
        Size(1500)
        LinkParticle('azef_utiagesmoke_02')
    sprite('null', 50)


@State
def IrezumiRay():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AlphaValue(0)
        AddY(7000)
    sprite('vr_azef450_00', 20)
    ConstantAlphaModifier(26)
    CreateObject('IrezumiRayLine', -1)
    sprite('vr_azef450_00', 30)
    ConstantAlphaModifier(-26)


@State
def IrezumiRayLine():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        AlphaValue(0)
    sprite('vr_azef450_01', 20)
    ConstantAlphaModifier(26)
    sprite('vr_azef450_01', 20)
    ConstantAlphaModifier(-13)


@State
def az450_dummy():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        AttackLevel_(5)
        Damage(32000)
        MinimumDamage(100)
        AttackDirection(3)
        FinishBG(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(10000)
        HitAnywhere(1)
        TeleportToObject(22)
        Visibility(1)
        Size(3000)
    sprite('null', 7)
    sprite('vr_azef450_col', 10)
    HitAnywhere(1)
    sprite('az450cutin_01', 3000)


@State
def __450Cam():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        CameraControlEnable(1)
        AddY(300000)
    sprite('null', 6)
    CameraPosition(990)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(980)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(970)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(960)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(950)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(940)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(930)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(920)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(910)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(900)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(890)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(880)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(870)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(860)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(850)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(840)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(830)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(820)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(810)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(800)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(790)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(780)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(770)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    CameraPosition(760)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 4)
    CameraPosition(100)
    CreateParticle('azef_ahanten05', -1)
    ScreenShake(1275, 1275)
    sprite('null', 11)
    CameraPosition(1000)
    AddY(-800000)
    CameraControlEnable(0)


@State
def AHshadow():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_ahshadow_00')
        AddY(300000)
    sprite('null', 165)


@State
def AHanten00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_ahanten01')
        SetPosXByScreenPer(50)
    sprite('null', 90)


@State
def AHanten01():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_ahanten04')
    sprite('null', 90)


@State
def AHanten02():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_lastanten01')
        AddY(300000)
        SetPosXByScreenPer(50)
    sprite('null', 90)


@State
def AHsection():

    def upon_IMMEDIATE():
        Eff3DEffect('azef_section', '')
        FaceSpawnLocation()
    sprite('null', 60)


@State
def AHSmoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_ahfinishbg03')
    sprite('null', 32767)


@State
def AHaura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Visibility(1)
        uponSendToLabel(32, 0)
        Eff3DEffect('azef_aura02', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        AlphaValue(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 0)
    CallCustomizableParticle('azef_407backaura_02', 1)
    CallCustomizableParticle('azef_407backaura_02', 2)
    CallCustomizableParticle('azef_407backaura_02', 3)
    CallCustomizableParticle('azef_407backaura_02', 4)
    CallCustomizableParticle('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 6)
    CallCustomizableParticle('azef_407backaura_02', 7)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CallCustomizableParticle('azef_407backaura_02', 9)
    CallCustomizableParticle('azef_407backaura_02', 10)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CallCustomizableParticle('azef_407backaura_02', 13)
    CallCustomizableParticle('azef_407backaura_02', 14)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    ConstantAlphaModifier(-51)


@State
def __610aura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Visibility(1)
        uponSendToLabel(32, 0)
        Eff3DEffect('azef_610aura00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        AlphaValue(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 0)
    CallCustomizableParticle('azef_407backaura_02', 1)
    CallCustomizableParticle('azef_407backaura_02', 2)
    CallCustomizableParticle('azef_407backaura_02', 3)
    CallCustomizableParticle('azef_407backaura_02', 4)
    CallCustomizableParticle('azef_407backaura_02', 5)
    CreateObject('407boya', 1)
    CreateObject('407boya', 5)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 6)
    CallCustomizableParticle('azef_407backaura_02', 7)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CallCustomizableParticle('azef_407backaura_02', 9)
    CallCustomizableParticle('azef_407backaura_02', 10)
    CreateObject('407boya2', 6)
    CreateObject('407boya2', 9)
    CreateObject('407boya2', 10)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 11)
    CallCustomizableParticle('azef_407backaura_02', 13)
    CallCustomizableParticle('azef_407backaura_02', 14)
    CreateObject('407boya2', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    ConstantAlphaModifier(-51)


@State
def dashEff():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        IgnoreScreenfreeze(1)
        LinkParticle('azef_newdash2')
    sprite('null', 50)


@State
def dashEff2():

    def upon_IMMEDIATE():
        Flip()
        IgnoreScreenfreeze(1)
        LinkParticle('azef_newdash3')
    sprite('null', 50)


@State
def BrustDD_SlashEff():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        Flip()
        SetScaleX(900)
        SetScaleY(1100)
        AlphaValue(255)
        AddY(100000)
        AddX(-100000)
        BlendMode_Normal()
    sprite('vr_azef440_00', 4)
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    ConstantAlphaModifier(-51)


@State
def BrustDD_SlashEffEx():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        Flip()
        SetScaleX(1300)
        SetScaleY(1560)
        AlphaValue(255)
        AddY(10000)
        AddX(-100000)
        BlendMode_Normal()
    sprite('vr_azef440_00', 4)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(-10000)
        AddX(-125000)
        AddScale(500)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(-45000)
        AddX(-125000)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(-90000)
        AddX(-125000)
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    ConstantAlphaModifier(-51)


@State
def BrustDD_SlashEff2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        Flip()
        AddY(250000)
        AddX(-180000)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        IgnoreFinishStop(1)
    sprite('vr_azef440_10', 6)
    Size(1200)
    sprite('vr_azef440_11', 5)
    Size(1400)
    IgnoreFinishStop(0)
    sprite('vr_azef440_12', 12)
    Size(1500)
    SetScaleSpeed(20)
    sprite('vr_azef440_13', 4)
    CreateParticle('azef_440brust_00', -1)
    sprite('vr_azef440_14', 4)
    ConstantAlphaModifier(-51)


@State
def BrustDD_SlashEff2Ex():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        Flip()
        AddY(250000)
        AddX(-180000)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        IgnoreFinishStop(1)
    sprite('vr_azef440_10', 6)
    Size(1400)
    sprite('vr_azef440_11', 5)
    Size(1700)
    IgnoreFinishStop(0)
    sprite('vr_azef440_12', 12)
    Size(1800)
    SetScaleSpeed(40)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(450000)
        AddScale(250)
        RenderLayer(6)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(-450000)
        AddScale(500)
        RenderLayer(6)
    CreateObject('BrustDD_EXeff', -1)

    def RunOnObject_1():
        Rotation(1800000)
        AddScale(500)
        RenderLayer(6)
    sprite('vr_azef440_13', 4)
    CreateParticle('azef_440brust_01', -1)
    sprite('vr_azef440_14', 4)
    ConstantAlphaModifier(-51)


@State
def BrustDD_SlashEff3():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        Flip()
        AddY(290000)
        E0EAEffectPosition(2)
        IgnoreFinishStop(1)
        Size(1700)
    sprite('vr_azef440_20', 2)
    CreateObject('BrustDD_brust', -1)
    RenderLayer(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    AddX(35000)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(20000)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(150000)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(-45000)
        RenderLayer(11)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(-140000)
        RenderLayer(11)
    sprite('vr_azef440_22', 4)
    AddX(35000)
    sprite('vr_azef440_23', 4)
    AddX(35000)
    IgnoreFinishStop(0)
    sprite('vr_azef440_24', 4)
    AddX(35000)
    sprite('vr_azef440_25', 4)
    AddX(35000)
    ConstantAlphaModifier(-26)
    sprite('vr_azef440_26', 5)
    AddX(35000)


@State
def BrustDD_SlashEff3Ex():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        Flip()
        AddY(290000)
        E0EAEffectPosition(2)
        IgnoreFinishStop(1)
        Size(2000)
    sprite('vr_azef440_20', 2)
    CreateObject('BrustDD_brust', -1)
    RenderLayer(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    AddX(35000)
    sprite('vr_azef440_22', 4)
    AddX(35000)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(45000)
        AddScale(700)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(120000)
        AddScale(700)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(-45000)
        RenderLayer(11)
    CreateObject('BrustDD_EXeff2', -1)

    def RunOnObject_1():
        Rotation(-140000)
        RenderLayer(11)
    sprite('vr_azef440_23', 4)
    AddX(35000)
    IgnoreFinishStop(0)
    sprite('vr_azef440_24', 4)
    AddX(35000)
    sprite('vr_azef440_25', 4)
    AddX(35000)
    ConstantAlphaModifier(-26)
    sprite('vr_azef440_26', 5)
    AddX(35000)


@State
def BrustDD_brust():

    def upon_IMMEDIATE():
        LinkParticle('azef_440brust2_00')
        IgnoreFinishStop(1)
    sprite('null', 10)
    sprite('null', 50)
    IgnoreFinishStop(0)


@State
def BrustDD_EXeff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        Size(1500)
        BlendMode_Add()
    sprite('vr_azef440_30', 2)
    sprite('vr_azef440_31', 2)
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    ConstantAlphaModifier(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)


@State
def BrustDD_EXeff2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        Size(1500)
        BlendMode_Add()
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    ConstantAlphaModifier(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)


@State
def __440Aura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Visibility(1)
        uponSendToLabel(32, 0)
        Eff3DEffect('azef_aura02', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        AlphaValue(0)
        Size(950)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    ConstantAlphaModifier(0)
    CallCustomizableParticle('azef_407backaura_02', 0)
    CallCustomizableParticle('azef_407backaura_02', 1)
    CallCustomizableParticle('azef_407backaura_02', 2)
    CallCustomizableParticle('azef_407backaura_02', 3)
    CallCustomizableParticle('azef_407backaura_02', 4)
    CallCustomizableParticle('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    CallCustomizableParticle('azef_407backaura_02', 6)
    CallCustomizableParticle('azef_407backaura_02', 7)
    CallCustomizableParticle('azef_407backaura_02', 8)
    CallCustomizableParticle('azef_407backaura_02', 9)
    sprite('vr_azef610_efpos00', 2)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    ConstantAlphaModifier(-51)


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
        AbsoluteY(500000)
        DeviationX(-100000, 80000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)


@State
def Act2Event_Bang():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        ScreenCollision(0)
        LoadSpritePalette(0)
        XPositionRelativeFacing(360000)
        Flip()
        StayAfterMovement(1, 0)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(LANDING, 9)
    sprite('bn070_03', 32767)
    loopRest()
    label(0)
    sprite('bn070_03', 20)
    sprite('bn070_04', 4)
    sprite('bn070_05', 4)
    sprite('bn070_06', 4)
    sprite('bn070_07', 4)
    sprite('bn070_08', 4)
    sprite('bn070_09', 4)
    sprite('bn063_11', 4)
    AddX(130000)
    LandingEffects(0, 1, 1)
    CommonSE('209_down_normal_0')
    sprite('bn063_11', 32767)
    loopRest()
    label(1)
    sprite('bn064_00', 3)
    sprite('bn064_01', 3)
    sprite('bn064_03', 3)
    sprite('bn064_05', 3)
    sprite('bn064_07', 3)
    sprite('bn064_09', 3)
    sprite('bn064_11', 3)
    loopRest()
    label(100)
    sprite('bn000_00', 7)
    sprite('bn000_01', 7)
    sprite('bn000_02', 7)
    sprite('bn000_03', 7)
    sprite('bn000_04', 7)
    sprite('bn000_05', 7)
    sprite('bn000_06', 7)
    sprite('bn000_07', 7)
    sprite('bn000_08', 7)
    sprite('bn000_09', 7)
    sprite('bn000_11', 7)
    loopRest()
    gotoLabel(100)
    label(2)
    sprite('keep', 2)
    sprite('bn022_00', 5)
    physicsXImpulse(-30000)
    physicsYImpulse(36000)
    setGravity(1800)
    JumpEffects(0, 0)
    CommonSE('001_airbackdash_0')
    sprite('bn022_01', 5)
    sprite('bn022_02', 5)
    label(101)
    sprite('bn022_02', 5)
    loopRest()
    gotoLabel(101)
    label(9)
    sprite('null', 2)
    loopRest()


@State
def Act3Event_ar():

    def upon_IMMEDIATE():
        ArakuneSpriteOverlay('vraref000_00', 160, 0, 0, 500, 0, 2147483647,
            1000, 1000)
        LoadSpritePalette(0)
        AddX(-80000)
        SetZVal(-1000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('ar000_00', 5)
    sprite('ar000_01', 5)
    sprite('ar000_02', 5)
    sprite('ar000_03', 5)
    sprite('ar000_04', 5)
    sprite('ar000_05', 5)
    sprite('ar000_06', 5)
    sprite('ar000_07', 5)
    sprite('ar000_08', 5)
    sprite('ar000_09', 5)
    sprite('ar000_11', 5)
    sprite('ar000_12', 5)
    sprite('ar000_13', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ar060_01', 10)
    ParticleSize(1500)
    CallCustomizableParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('ar060_02', 4)
    physicsXImpulse(-45000)
    physicsYImpulse(27000)
    setGravity(2700)
    uponSendToLabel(LANDING, 4)
    sprite('ar060_03', 4)
    sprite('ar060_04', 32767)
    uponSendToLabel(LANDING, 2)
    loopRest()
    label(2)
    sprite('keep', 2)
    CommonSE('012_stab_deep')
    CommonSE('209_down_normal_0')


@State
def Act3Event_ar_01():

    def upon_IMMEDIATE():
        ArakuneSpriteOverlay('vraref000_00', 160, 0, 0, 500, 0, 2147483647,
            1000, 1000)
        LoadSpritePalette(0)
        ScreenCollision(0)
        EnableCollision(0)
        Flip()

        def upon_32():
            sendToLabel(2)

            def upon_EVERY_FRAME():
                if SLOT_50 < 350000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)

        def upon_33():
            sendToLabel(2)

            def upon_EVERY_FRAME():
                if SLOT_19 < 240000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(0)
        uponSendToLabel(36, 4)
    sprite('null', 32767)
    XPositionRelativeFacing(-920000)
    label(0)
    sprite('ar030_10', 4)
    EndMomentum(1)
    label(1)
    sprite('ar000_00', 5)
    sprite('ar000_01', 5)
    sprite('ar000_02', 5)
    sprite('ar000_03', 5)
    sprite('ar000_04', 5)
    sprite('ar000_05', 5)
    sprite('ar000_06', 5)
    sprite('ar000_07', 5)
    sprite('ar000_08', 5)
    sprite('ar000_09', 5)
    sprite('ar000_11', 5)
    sprite('ar000_12', 5)
    sprite('ar000_13', 5)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ar030_00', 7)
    SetXCollisionFromOrigin(200)
    physicsXImpulse(7200)
    sprite('ar030_01', 7)
    label(3)
    sprite('ar030_02', 7)
    sprite('ar030_03', 7)
    sprite('ar030_04', 7)
    sprite('ar030_05', 7)
    sprite('ar030_06', 7)
    sprite('ar030_07', 7)
    sprite('ar030_08', 7)
    sprite('ar030_09', 7)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ar610_09', 1)
    TeleportToObject(22)
    EndMomentum(1)
    clearUponHandler(EVERY_FRAME)
    sprite('ar610_09', 1)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    label(5)
    sprite('ar610_09', 2)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    gotoLabel(5)


@State
def Act3Event_ar_02():

    def upon_IMMEDIATE():
        ArakuneSpriteOverlay('vraref000_00', 160, 0, 0, 500, 0, 2147483647,
            1000, 1000)
        LoadSpritePalette(0)
        ScreenCollision(0)
        TeleportToObject(22)
        uponSendToLabel(36, 4)
    label(0)
    sprite('ar610_09', 2)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ar_03():

    def upon_IMMEDIATE():
        ArakuneSpriteOverlay('vraref000_00', 160, 0, 0, 500, 0, 2147483647,
            1000, 1000)
        LoadSpritePalette(0)
        ScreenCollision(0)
        EnableCollision(0)
        TeleportToObject(2)
        SetZVal(1000)
        uponSendToLabel(32, 0)
    sprite('ar060_15', 32767)
    AddX(-50000)
    loopRest()
    label(0)
    sprite('ar060_01', 10)
    ParticleSize(1500)
    CallCustomizableParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('ar060_02', 4)
    physicsXImpulse(-45000)
    physicsYImpulse(27000)
    setGravity(2700)
    uponSendToLabel(LANDING, 4)
    sprite('ar060_03', 4)
    sprite('ar060_04', 32767)
    uponSendToLabel(LANDING, 2)
    loopRest()
    label(2)
    sprite('keep', 2)
    CommonSE('012_stab_deep')
    CommonSE('209_down_normal_0')
