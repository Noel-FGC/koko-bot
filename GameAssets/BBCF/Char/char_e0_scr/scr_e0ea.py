@State
def drain_base():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('null', 1)
    CreateParticle('rgef_drainstart', -1)
    label(0)
    sprite('null', 2)
    CallPrivateFunction('CreateDrainTsubu', 0, 0, 0, 0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(0)


@State
def drain_num8():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('null', 4)
    CreateParticle('rgef_drainstart', -1)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)
    sprite('null', 4)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)
    sprite('null', 4)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)
    sprite('null', 4)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)


@State
def drain_num4():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('null', 1)
    ParticleSize(300)
    CallCustomizableParticle('rgef_drainstart', -1)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)
    CreateObject('drain_tsubu', -1)


@State
def drain_tsubu():

    def upon_IMMEDIATE():
        Visibility(1)
        SetSpeedZ(0)
        SetAccelerationZ(0)
        SetPositionZ(0)
        DeviationX(-70000, 70000)
        DeviationY(-70000, 70000)
        RandAddSpeedSphere(100000, 120000)
        RandSpeedY(50000, 60000)
        CallObject('DrainLine')
        SetActionMark(0)
        LinkParticle('rgef_drainroop')

        def upon_32():
            Size(3000)

        def upon_33():
            ConstantAlphaModifier(-6)
    sprite('null', 1)
    CommonPolyline('vrdraintex_test.hip', 3000)
    sprite('null', 15)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(80)
        YAccel(80)
        PerSpeedZ(80)
        Unknown2070(3, 0, 1, 0)
    sprite('null', 7)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 1, 0)
    sprite('null', 5)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 2, 0)
    sprite('null', 3)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 4, 0)
    sprite('null', 3)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 8, 0)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 16, 0)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 24, 0)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 36, 0)
    label(0)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 48, 0)
    uponSendToLabel(29, 1)
    RunLoopUpon(29, 200000)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    CallPrivateFunction('DrainTubuKaihuku', 0, 0, 0, 0, 0, 0, 0, 0)
    AddActionMark(1)
    clearUponHandler(29)

    def upon_EVERY_FRAME():
        XImpulseAcceleration(90)
        YAccel(90)
        PerSpeedZ(90)
        Unknown2070(3, 0, 96, 0)


@State
def EffBarrier():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_gird_f.DIG', 'ef_gird_f_motion_000.mmot')
        FaceSpawnLocation()
        AbsoluteY(0)
        XPositionRelativeFacing(0)
        E0EAEffectPositionCenter(3)
        E0EAEffectDirection(3)
        Visibility(1)
        BlendMode_Add()

        def upon_32():
            if not SLOT_2:
                SetActionMark(1)
                sendToLabel(1)
        CreateObject('EffBarrierParts', -1)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    Size(1000)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    AlphaValue(150)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(30)


@State
def EffBarrierJust():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_gird_f.DIG', 'ef_gird_f_motion_000.mmot')
        FaceSpawnLocation()
        AbsoluteY(0)
        XPositionRelativeFacing(0)
        E0EAEffectPositionCenter(3)
        E0EAEffectDirection(3)
        Visibility(1)
        BlendMode_Add()
    sprite('null', 30)


@State
def EffBarrierParts():

    def upon_IMMEDIATE():
        LinkParticle('ef_gird_f')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
    sprite('null', 32767)


@State
def EffBarrierPartsTraining():

    def upon_IMMEDIATE():
        LinkParticle('ef_gird_f')
        E0EAEffectPosition(2)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-30)


@State
def FLORE_BURST():
    sprite('null', 240)
    Visibility(1)
    FloorSprite('vr_burnt.hip')
    RandAddScale(-100, 100)
    AlphaValue(240)
    RandRotationAngle()
    sprite('null', 48)
    ConstantAlphaModifier(-5)


@State
def e0_burst():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(32000)
        AirPushbackY(25000)
        Hitstop(0)
        AttackP2(10)
        BurstAttribute(1)
        DefeatOpponentBehavior(2)
        AttackDirection(3)
        E0EAEffectPositionCenter(3)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('vrdmy_burst', 16)
    Visibility(1)
    StartMultihit()
    LinkParticle('ef_burst')
    sprite('vrdmy_burst', 10)
    sprite('vrdmy_burst', 10)
    StartMultihit()


@State
def BurstLv0First():
    sprite('null', 30)
    LinkParticle('ef_bbb_A')
    E0EAEffectPositionCenter(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)


@State
def BurstLv1First():
    sprite('null', 30)
    LinkParticle('ef_bbg_A')
    E0EAEffectPositionCenter(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)


@State
def BurstLv2First():
    sprite('null', 30)
    LinkParticle('ef_bbo_A')
    E0EAEffectPositionCenter(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)


@State
def BurstObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        E0EAEffectPositionCenter(3)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        Visibility(1)
        IgnoreBurst(1)
        YImpulseBeforeWallbounce(1600)

        def upon_32():
            LinkParticle('ef_bbg_B')
            AttackLevel_(3)
            Damage(0)
            BurstAttribute(1)
            Hitstop(0)
            AttackDirection(3)
            StrikeProjectileLevel(1)
            PassByArmor(1)
            MoveAttributes(0, 0, 0, 0, 0)
            StarterRating(0)
            Unknown12055(1)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            AirPushbackX(32000)
            AirPushbackY(30000)
            AttackP1(10)
            AirUntechableTime(300)
            Blockstun(24)

        def upon_33():
            LinkParticle('ef_bbo_B')
            AttackLevel_(3)
            Damage(0)
            BurstAttribute(1)
            Hitstop(0)
            AttackDirection(3)
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
            AirPushbackX(3200)
            AirPushbackY(50000)
            YImpulseBeforeWallbounce(1600)
            AttackP1(80)
            AirUntechableTime(300)
            Blockstun(36)
            AttackP1(65)
            AttackP2(110)
            RemoveOnCallStateEnd(3)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            pass
    uponSendToLabel(32, 1)
    sprite('vrdmy_burst', 4)
    AttackOff()
    sprite('vrdmy_burst', 4)
    RefreshMultihit()
    sprite('vrdmy_burst', 23)
    AttackOff()
    sendToLabel(2)
    label(1)
    sprite('vrdmy_burst', 3)
    AttackOff()
    sprite('vrdmy_burst', 6)
    RefreshMultihit()
    sprite('vrdmy_burst', 23)
    AttackOff()
    loopRest()
    label(2)
    loopRest()


@State
def aura():

    def upon_IMMEDIATE():
        Eff3DEffect('dd_eff.DIG', 'dd_eff_motion_000.mmot')
        ColorForTransition(4278190335)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Size(1000)
    sprite('null', 120)


@State
def yugami_ring():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('vr_yugami', 5)
    SetScaleSpeed(800)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami', 10)
    SetScaleSpeed(200)
    Unknown3059(-3200)


@State
def yugami_ring2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('vr_yugami2', 5)
    SetScaleSpeed(800)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami2', 10)
    SetScaleSpeed(200)
    Unknown3059(-3200)


@State
def FLORE_FROST():
    sprite('null', 240)
    Visibility(1)
    FloorSprite('vr_frost.hip')
    RandAddScale(-200, 200)
    AlphaValue(240)
    RandRotationAngle()
    sprite('null', 48)
    ConstantAlphaModifier(-5)


@State
def FreezeDamage():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_ice_a.DIG', 'jnef_ice_a_motion_000.mmot')
        ColorParent(22)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        PaletteMapping(1, 175, 111, 63, 32, 8)
        CommonSE('ice_fast')

        def upon_32():
            CommonSE('ice_break_slow')
            CreateObject('FreezeDamageRendaParts', -1)
            CreateObject('FreezeDamageRendaParts', -1)
            CreateObject('FreezeDamageRendaParts', -1)
            CreateObject('FreezeDamageRendaParts', -1)

        def upon_33():
            CommonSE('ice_break_fast')
            CreateObject('FreezeDamageBreakParts', -1)

        def upon_34():
            SLOT_51 = SLOT_51 + 1
            if not SLOT_51 % 10:
                CreateObject('FreezeDamageLandParts', -1)
                CreateObject('FREEZE_FLORE_FROST', -1)
    label(0)
    sprite('null', 1)
    loopRest()
    gotoLabel(0)


@State
def FreezeDamageParts():

    def upon_IMMEDIATE():
        Visibility(1)
        ColorParent(22)
        CommonSE('ice_break_fast')
        PaletteIndex(1)
    sprite('null', 1)
    DeviationX(-100000, 100000)
    DeviationY(0, 400000)
    ParticleColorFromPalette(175, 111, 111)
    CallCustomizableParticle('ef_freezebreak', -1)


@State
def FreezeDamageBreakParts():

    def upon_IMMEDIATE():
        Visibility(1)
        ColorParent(22)
        PaletteIndex(1)
        AbsoluteY(256000)
    sprite('null', 200)
    ParticleColorFromPalette(175, 111, 111)
    CallPrivateEffect('ef_freezebreak')


@State
def FreezeDamageLandParts():

    def upon_IMMEDIATE():
        Visibility(1)
        ColorParent(22)
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        AbsoluteY(256000)
    sprite('null', 32767)
    ParticleColorFromPalette(175, 111, 111)
    CallPrivateEffect('ef_freezeland')


@State
def FREEZE_FLORE_FROST():
    sprite('null', 10)
    Visibility(1)
    FloorSprite('vr_frost.hip')
    RandAddScale(-200, 200)
    AlphaValue(0)
    ConstantAlphaModifier(18)
    RandRotationAngle()
    sprite('null', 40)
    ConstantAlphaModifier(0)
    sprite('null', 30)
    ConstantAlphaModifier(-6)


@State
def FreezeDamageRendaParts():

    def upon_IMMEDIATE():
        Visibility(1)
        ColorParent(22)
        PaletteIndex(1)
    sprite('null', 1)
    DeviationX(-100000, 100000)
    DeviationY(0, 400000)
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef_icebrl', -1)


@State
def ef_danger():

    def upon_IMMEDIATE():
        Visibility(1)
        E0EAEffectPosition(3)
        LinkParticle('ef_danger')
    sprite('null', 40)


@State
def ef_danger_re():

    def upon_IMMEDIATE():
        Visibility(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        E0EAEffectPositionCenter(3)
        LinkParticle('ef_danger_re')
    sprite('null', 40)


@State
def FreezeDamageTest():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_ice_a.DIG', 'jnef_ice_a_motion_000.mmot')
        CommonSE('ice_slow')
    label(0)
    sprite('null', 1)
    loopRest()
    gotoLabel(0)


@State
def PushAndDamage():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        EnableCollision(1)
        NoAttackDuringAction(1)
    sprite('vr_debug_dmg', 2400)


@State
def Banana():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(0)
        Damage(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(20)
        HardKnockdown(3)
        AirPushbackX(0)
        AirPushbackY(10000)
        MaxHP(1000)
        CurrentHP(1000)
        SetActionMark(1)

        def upon_19():
            if SLOT_2:
                sendToLabel(0)
            SetActionMark(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_2:
                sendToLabel(0)
            SetActionMark(0)
    sprite('vr_banana', 2400)
    label(0)
    sprite('vr_banana2', 30)
    BlendMode_Normal()
    ConstantAlphaModifier(-8)


@State
def RandomAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        setInvincible(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
    sprite('vr_debug_dmg', 40)
    physicsXImpulse(10000)
    AttackOff()
    AirPushbackX(100000)
    loopRest()
    gotoLabel(4)
    label(0)
    sprite('vr_debug_dmg', 20)
    ColorForTransition(4278190335)
    NoAttackDuringAction(1)
    loopRest()
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    if random_(2, 0, 10):
        conditionalSendToLabel(1)
    label(4)
    sprite('vr_debug_dmg', 20)
    physicsXImpulse(0)
    NoAttackDuringAction(0)
    RefreshMultihit()
    ColorForTransition(4294901760)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_debug_dmg', 1)


@State
def PushFix():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        EnableCollision(1)
        NoAttackDuringAction(1)
        ColorForTransition(4278255360)
        PreventSelfPush(1)
    sprite('vr_debug_dmg', 2400)


@State
def HitStopObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        EnemyHitstopAddition(30, 30, 30)
        Damage(20000)
        TeleportToObject(22)
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()
    sprite('vr_debug_dmg', 10)
    RefreshMultihit()


@State
def Aura():
    sprite('vr_aura00', 7)
    IgnoreScreenfreeze(1)
    BlendMode_Add()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    ColorTransition(16776960, 30)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def AuraDark():
    sprite('vr_aura00', 7)
    BlendMode_Normal()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    RedColorValue(255)
    GreenColorValue(0)
    BlueColorValue(0)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def cmn_tekitou_w():
    sprite('null', 10)
    CreateParticle('ef_kaihi', -1)


@State
def cmn_tekitou():
    sprite('null', 10)
    CreateParticle('ef_ukemi', -1)


@State
def cmn_tekitou_r():
    sprite('null', 10)
    CreateParticle('ef_rapidcancel', -1)


@State
def cmn_digitalcrush():
    sprite('null', 10)
    CreateParticle('ef_digitalcrush', -1)


@State
def cmn_shotsousai():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(2000)
    sprite('vr_yugami', 5)
    CreateParticle('ef_shotsousai', -1)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami', 10)
    SetScaleSpeed(100)
    Unknown3059(-3200)


@State
def cmn_judgment():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RenderLayer(1)
    DeleteObject(23)
    if SLOT_96:
        conditionalSendToLabel(1)
    label(0)
    sprite('vr_judge_arrow', 8)
    physicsYImpulse(1000)
    sprite('vr_judge_arrow', 6)
    YAccel(50)
    sprite('vr_judge_arrow', 2)
    YAccel(50)
    sprite('vr_judge_arrow', 8)
    physicsYImpulse(-1000)
    sprite('vr_judge_arrow', 6)
    YAccel(50)
    sprite('vr_judge_arrow', 2)
    YAccel(50)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_judge_arrow2p', 8)
    physicsYImpulse(1000)
    sprite('vr_judge_arrow2p', 6)
    YAccel(50)
    sprite('vr_judge_arrow2p', 2)
    YAccel(50)
    sprite('vr_judge_arrow2p', 8)
    physicsYImpulse(-1000)
    sprite('vr_judge_arrow2p', 6)
    YAccel(50)
    sprite('vr_judge_arrow2p', 2)
    YAccel(50)
    loopRest()
    gotoLabel(1)


@State
def EffOverDrive():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
    sprite('vr_aura00', 4)
    CreateParticle('ef_overdriveptc', -1)
    BlendMode_Add()
    AlphaValue(180)
    SetScaleX(800)
    SetScaleY(1000)
    SetScaleSpeedY(10)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RedColorValue(0)
    GreenColorValue(64)
    BlueColorValue(255)
    sprite('vr_aura01', 5)
    sprite('vr_aura02', 5)
    SetScaleSpeedY(10)
    physicsYImpulse(-100)
    sprite('vr_aura03', 7)
    physicsYImpulse(-400)
    SetScaleSpeedY(20)
    sprite('vr_aura04', 7)
    AddY(-8000)
    ConstantAlphaModifier(-5)
    sprite('vr_aura05', 7)


@State
def AuraRed():
    sprite('vr_aura00', 7)
    BlendMode_Normal()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RemoveOnContact(2)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    RedColorValue(255)
    GreenColorValue(20)
    BlueColorValue(20)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def AuraBlack():
    sprite('vr_aura00', 7)
    BlendMode_Sub()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RemoveOnContact(2)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    RedColorValue(240)
    GreenColorValue(240)
    BlueColorValue(240)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def AuraSilver():
    sprite('vr_aura00', 7)
    BlendMode_Normal()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RemoveOnContact(2)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    RedColorValue(240)
    GreenColorValue(240)
    BlueColorValue(240)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def AuraGold():
    sprite('vr_aura00', 7)
    BlendMode_Normal()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RemoveOnContact(2)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(-6)
    RedColorValue(255)
    GreenColorValue(255)
    BlueColorValue(20)
    sprite('vr_aura01', 7)
    sprite('vr_aura02', 7)
    sprite('vr_aura03', 30)
    ConstantAlphaModifier(-20)


@State
def AuraRainbow():
    sprite('vr_aura00', 7)
    BlendMode_Normal()
    AddY(-40000)
    SetScaleX(700)
    physicsYImpulse(70)
    SetScaleXPerFrame(12)
    SetScaleSpeedY(12)
    SetZVal(500)
    if random_(2, 0, 50):
        Flip()
    RemoveOnContact(2)
    E0EAEffectPosition(2)
    ConstantRedModifier(-30)
    ConstantGreenModifier(30)
    ConstantBlueModifier(30)
    ConstantAlphaModifier(-6)
    sprite('vr_aura01', 7)
    ConstantRedModifier(30)
    ConstantGreenModifier(30)
    ConstantBlueModifier(-30)
    ConstantAlphaModifier(-6)
    sprite('vr_aura02', 7)
    ConstantRedModifier(30)
    ConstantGreenModifier(-30)
    ConstantBlueModifier(30)
    ConstantAlphaModifier(-6)


@State
def GuardCrushptc():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('ef_mcGuardcrush_ptc')
        RemoveOnCallStateEnd(3)
    sprite('null', 40)


@State
def GuardCrushWind():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_girdcrashwind00.DIG', '')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(56, 99)
        SetScaleX(900)
        SetScaleY(700)
        AddY(70000)
        AddPositionZ(70000)
    sprite('null', 2)
    AlphaValue(0)
    ParticleLayer(5)
    CallCustomizableParticle('ef_mcGuardcrush', -1)
    CreateObject('GuardCrushptc', -1)
    sprite('null', 2)
    CreateObject('GuardCrushWind01', -1)
    sprite('null', 16)
    AlphaValue(200)
    loopRest()
    label(99)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    ConstantAlphaModifier(-20)


@State
def GuardCrushWind01():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_girdcrashwind01.DIG', '')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(56, 99)
        SetScaleX(1000)
        SetScaleY(700)
        AddY(-100000)
        AddPositionZ(70000)
    sprite('null', 4)
    AlphaValue(0)
    sprite('null', 8)
    AlphaValue(200)
    loopRest()
    label(99)
    sprite('null', 5)
    SetScaleXPerFrame(90)
    ConstantAlphaModifier(-40)


@State
def GuardCrushWind_tg():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_girdcrashwind00.DIG', '')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(56, 99)
        SetScaleX(1100)
        SetScaleY(750)
        AddY(70000)
        AddPositionZ(70000)
    sprite('null', 2)
    AlphaValue(0)
    ParticleSize(1100)
    ParticleLayer(5)
    CallCustomizableParticle('ef_mcGuardcrush', -1)
    sprite('null', 2)
    CreateObject('GuardCrushWind_tg01', -1)
    sprite('null', 16)
    AlphaValue(200)
    loopRest()
    label(99)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    ConstantAlphaModifier(-20)


@State
def GuardCrushWind_tg01():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_girdcrashwind01.DIG', '')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(56, 99)
        SetScaleX(1300)
        SetScaleY(1000)
        AddY(-100000)
        AddPositionZ(70000)
    sprite('null', 4)
    AlphaValue(0)
    sprite('null', 8)
    AlphaValue(200)
    loopRest()
    label(99)
    sprite('null', 5)
    SetScaleXPerFrame(90)
    ConstantAlphaModifier(-40)


@State
def BurstDDeff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        PaletteIndex(3)
        Size(1800)
        AlphaValue(120)
        RandAddRotation(-60000, 60000)
        RenderLayer(2)
        EnableAfterimage(1)
        AfterimageInterval(3)
        AfterimageCount(2)
    sprite('vr_bstdd00', 4)
    CreateParticle('ef_burstdd_00', -1)
    sprite('vr_bstdd01', 4)
    sprite('vr_bstdd02', 4)
    sprite('vr_bstdd03', 4)
    sprite('vr_bstdd04', 4)
    ConstantAlphaModifier(-26)
    sprite('vr_bstdd05', 4)


@State
def BurstDDeff_OFF():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 60)
    LinkParticle('ef_burstdd_Off')


@State
def Positive_ON():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 60)
    CreateParticle('ef_Positive', -1)


@State
def Positive_OFF():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 60)
    CreateParticle('ef_Positive_Off', -1)
