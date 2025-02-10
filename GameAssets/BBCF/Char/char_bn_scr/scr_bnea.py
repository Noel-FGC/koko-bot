@State
def EMB_BN():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
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
def EMB_BN_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
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
def EMB_BN_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
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
def bn_win():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AbsoluteY(488000)
    CallCustomizableParticle('bnef_win_smoke', -1)
    loopRest()


@State
def bn_bomber():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    ScreenShake(0, 16000)
    XPositionRelativeFacing(0)
    ParticleSize(1500)
    CallCustomizableParticle('bnef_bomber', -1)
    loopRest()


@State
def bn_perfect_ray():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        XPositionRelativeFacing(0)
        AbsoluteY(288000)
    label(0)
    sprite('null', 1)
    ParticleLayer(1)
    CallCustomizableParticle('ef_speed_center', -1)
    gotoLabel(0)


@State
def bn_perfect_font00():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Normal()
        XPositionRelativeFacing(-1040000)
        AbsoluteY(-208000)
        RenderLayer(4)
    sprite('bnef611_00', 32767)


@State
def bn_perfect_font01():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Normal()
        XPositionRelativeFacing(-1040000)
        AbsoluteY(-576000)
        RenderLayer(4)
    sprite('bnef611_01', 32767)


@State
def bn_perfect_font02():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Normal()
        XPositionRelativeFacing(-244000)
        AbsoluteY(-172000)
        RenderLayer(4)
    sprite('bnef611_02', 32767)


@State
def bn_perfect_font03():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Normal()
        XPositionRelativeFacing(-244000)
        AbsoluteY(-592000)
        RenderLayer(4)
    sprite('bnef611_03', 32767)


@State
def bn_perfect_font00b():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Add()
        XPositionRelativeFacing(-1040000)
        AbsoluteY(-208000)
        IgnoreScreenfreeze(1)
        RenderLayer(4)
    sprite('bnef611_10', 32767)


@State
def bn_perfect_font01b():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Add()
        XPositionRelativeFacing(-1040000)
        AbsoluteY(-576000)
        IgnoreScreenfreeze(1)
        RenderLayer(4)
    sprite('bnef611_11', 32767)


@State
def bn_perfect_font02b():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Add()
        XPositionRelativeFacing(-244000)
        AbsoluteY(-172000)
        IgnoreScreenfreeze(1)
        RenderLayer(4)
    sprite('bnef611_12', 32767)


@State
def bn_perfect_font03b():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        BlendMode_Add()
        XPositionRelativeFacing(-244000)
        AbsoluteY(-592000)
        IgnoreScreenfreeze(1)
        RenderLayer(4)
    sprite('bnef611_13', 32767)


@State
def bn_throw():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    AddY(150000)
    CreateParticle('bnef_throw_smoke', -1)
    CreateParticle('bnef_throw_leaf', -1)
    loopRest()


@State
def bn_throw_b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    AddY(150000)
    CreateParticle('bnef_throw_smoke', -1)
    loopRest()


@State
def bn_throw_air():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(288000)
    CreateParticle('bnef_throw_smoke', -1)
    CreateParticle('bnef_throw_leaf', -1)
    loopRest()


@State
def bn_throw_air_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(288000)
    ParticleLayer(4)
    CallCustomizableParticle('bnef_throw_smoke', -1)
    loopRest()


@State
def bn_sp_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(155000)
    CreateParticle('bnef_sp_throw_speed', -1)
    CreateParticle('bnef_sp_throw_leaf', -1)
    loopRest()


@State
def bn_sp_throw_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(280000)
    CreateParticle('bnef_sp_throw_speed', -1)
    loopRest()


@State
def bn_sp_throw_c():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(260000)
    CreateParticle('bnef_sp_throw_speed', -1)
    CreateParticle('bnef_sp_throw_leaf', -1)
    loopRest()


@State
def bn_sp_throw_d():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(245000)
    CreateParticle('bnef_sp_throw_speed', -1)
    loopRest()


@State
def bn_sp_air_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(295000)
    CreateParticle('bnef_sp_throw_speed', -1)
    CreateParticle('bnef_sp_throw_leaf', -1)
    loopRest()


@State
def bn_sp_air_throw_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(360000)
    CreateParticle('bnef_sp_throw_speed', -1)
    loopRest()


@State
def bn_sp_air_throw_c():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(365000)
    CreateParticle('bnef_sp_throw_speed', -1)
    CreateParticle('bnef_sp_throw_leaf', -1)
    loopRest()


@State
def bn_sp_air_throw_d():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    AddY(350000)
    CreateParticle('bnef_sp_throw_speed', -1)
    loopRest()


@State
def bn_strike():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef404_00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(192)
    sprite('vrbnef404_01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('vrbnef404_02', 2)
    sprite('vrbnef404_03', 4)
    CreateParticle('bnef_knuckle', 0)
    CreateParticle('bnef_knuckle', 1)
    CreateParticle('bnef_knuckle', 2)
    CreateParticle('bnef_knuckle', 3)
    CreateParticle('bnef_knuckle', 4)
    sprite('vrbnef404_04', 3)
    sprite('vrbnef404_05', 2)
    sprite('vrbnef404_06', 2)
    sprite('vrbnef404_07', 2)


@State
def bn_strike_air():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Size(1000)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef405_00', 3)
    AlphaValue(0)
    ConstantAlphaModifier(128)
    sprite('vrbnef405_01', 3)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('vrbnef405_02', 3)
    CreateParticle('bnef_knuckle_air', 0)
    CreateParticle('bnef_knuckle_air', 1)
    CreateParticle('bnef_knuckle_air', 2)
    CreateParticle('bnef_knuckle_air', 3)
    CreateParticle('bnef_knuckle_air', 4)
    CreateParticle('bnef_knuckle_air', 5)
    CreateParticle('bnef_knuckle_air', 6)
    sprite('vrbnef405_03', 3)
    sprite('vrbnef405_04', 2)
    sprite('vrbnef405_05', 2)


@State
def GuardCrash():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef410_00', 3)
    sprite('vrbnef410_01', 3)
    CreateParticle('bnef_guardcrash', 0)
    sprite('vrbnef410_02', 3)
    CreateParticle('bnef_guardcrash', 0)
    CreateParticle('bnef_guardcrash', 1)
    CreateParticle('bnef_guardcrash', 2)
    sprite('vrbnef410_03', 3)
    sprite('vrbnef410_04', 3)


@State
def shotAD_Matome():
    sprite('shot_expoint', 60)
    CreateObject('bn_shot_A', 0)
    ObjectUpon(STATE_END, 33)
    SLOT_31 = SLOT_31 + -1
    ParticleRotationAngle(45000)
    CallCustomizableParticle('bnef_kugi_pitch', 1)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_A', 0)
        ObjectUpon(STATE_END, 32)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(60000)
        CallCustomizableParticle('bnef_kugi_pitch', 2)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_A', 0)
        ObjectUpon(STATE_END, 34)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(30000)
        CallCustomizableParticle('bnef_kugi_pitch', 0)


@State
def bn_shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(74)
        AirUntechableTime(14)
        Hitstop(0)
        EnemyHitstopAddition(5, 5, 5)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        CollideWithWall(1)
        ContinueState(120)
        Size(1250)
        PaletteIndex(0)
        ForceShadowOff(1)
        StarterRating(2)
        HitsparkSize(500)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        Poison(300, 120)
        RotationAngle(30000)
        AirPushbackX(16000)
        AirPushbackY(5000)
        physicsXImpulse(32000)
        physicsYImpulse(-18000)

        def upon_32():
            RotationAngle(15000)
            physicsXImpulse(48000)
            physicsYImpulse(-9000)

        def upon_33():
            RotationAngle(30000)
            physicsXImpulse(32000)
            physicsYImpulse(-18000)

        def upon_34():
            RotationAngle(45000)
            physicsXImpulse(16000)
            physicsYImpulse(-27000)

        def upon_OPPONENT_HIT():
            CreateObject('bn_shot_A_hit', -1)
            clearUponHandler(OPPONENT_HIT)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 2)
        uponSendToLabel(LANDING, 2)

        def upon_39():
            NoAttackDuringAction(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_002', 4)
    sprite('vrbnef406_003', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    sprite('null', 1)
    CreateObject('bn_shot_reflect', -1)


@State
def bn_shot_A_hit():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        Size(1250)
        BlendMode_Normal()
    sprite('null', 2)
    ParticleFacing(0)
    CallCustomizableParticle('bnef_kugi_poison', -1)


@State
def bn_shot_reflect():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        Size(1250)
        BlendMode_Normal()
    sprite('vrbnef406_001', 60)
    AlphaValue(255)
    ConstantAlphaModifier(-4)
    AddRotationPerFrame(15000)
    physicsYImpulse(20000)
    physicsXImpulse(5000)
    setGravity(2000)
    CreateParticle('bnef_kugi_hit', -1)


@State
def shotBD_Matome():
    sprite('shot_expoint', 60)
    CreateObject('bn_shot_B', 0)
    ObjectUpon(STATE_END, 33)
    SLOT_31 = SLOT_31 + -1
    ParticleRotationAngle(45000)
    CallCustomizableParticle('bnef_kugi_pitch', 1)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_B', 0)
        ObjectUpon(STATE_END, 32)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(60000)
        CallCustomizableParticle('bnef_kugi_pitch', 2)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_B', 0)
        ObjectUpon(STATE_END, 34)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(30000)
        CallCustomizableParticle('bnef_kugi_pitch', 0)


@State
def bn_shot_B():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(94)
        SingleProration(1)
        AirUntechableTime(14)
        Hitstop(0)
        EnemyHitstopAddition(5, 5, 5)
        AirPushbackX(16000)
        AirPushbackY(7000)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        StarterRating(2)
        Unknown12052(1)
        HitsparkSize(500)

        def upon_EVERY_FRAME():
            if SLOT_51:
                clearUponHandler(EVERY_FRAME)
                AttackLevel_(3)
                AirUntechableTime(17)
                Hitstop(11)
                EnemyHitstopAddition(0, 0, 2)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(5400)
                AirPushbackY(24000)
                UseSlashHitspark(0)
                UseFireHitspark(1)
                HitsparkSize(1000)
                WallCollisionDetection(1)
                ForceShadowOff(1)
                BlendMode_Normal()
                Size(1250)
                AlphaValue(255)
                ConstantAlphaModifier(-4)
                AddRotationPerFrame(36000)
                CancelIfPlayerHit(3)
        WallCollisionDetection(1)
        ContinueState(120)
        Size(1250)
        PaletteIndex(0)
        ForceShadowOff(1)
        physicsXImpulse(38000)
        RotationAngle(65000)
        physicsXImpulse(21111)
        physicsYImpulse(-38000)

        def upon_32():
            RotationAngle(10000)
            physicsXImpulse(38000)
            physicsYImpulse(-8444)

        def upon_33():
            RotationAngle(20000)
            physicsXImpulse(38000)
            physicsYImpulse(-16888)

        def upon_34():
            RotationAngle(30000)
            physicsXImpulse(38000)
            physicsYImpulse(-25333)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 2)
        uponSendToLabel(CORNERED, 3)

        def upon_39():
            NoAttackDuringAction(1)
    label(0)
    sprite('vrbnef406_004', 4)
    sprite('vrbnef406_005', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(-33)
    YAccel(-50)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('bnef_kugi_hit', -1)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    AddRotationPerFrame(0)
    EndMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    Visibility(1)
    ExitState()
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(33)
    YAccel(-50)
    CreateParticle('bnef_kugi_hit', -1)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    AddRotationPerFrame(0)
    EndMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    Visibility(1)
    ExitState()
    label(3)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(-33)
    YAccel(75)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('bnef_kugi_hit', -1)
    uponSendToLabel(LANDING, 2)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    clearUponHandler(LANDING)
    AddRotationPerFrame(0)
    EndMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    Visibility(1)


@State
def bn_shot_B_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(300)
        AttackP1(70)
        AttackP2(90)
        Hitstop(5)
        AirPushbackX(16000)
        AirPushbackY(5000)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        StarterRating(2)

        def upon_EVERY_FRAME():
            if SLOT_51:
                DefaultAttack()
                AttackLevel_(3)
                StrikeProjectileLevel(0)
                ProjectileLevel(1)
                MoveAttributes(0, 0, 0, 1, 0)
                Damage(300)
                AttackP1(70)
                AttackP2(90)
                AirHitstunAnimation(9)
                GroundedHitstunAnimation(9)
                ForceShadowOff(1)
                StarterRating(2)
                PaletteIndex(0)
                Size(1250)
                BlendMode_Normal()
                WallCollisionDetection(1)
                CancelIfPlayerHit(3)
                AlphaValue(255)
                ConstantAlphaModifier(-4)
                AddRotationPerFrame(36000)
                clearUponHandler(EVERY_FRAME)
        WallCollisionDetection(1)
        ContinueState(120)
        Size(1250)
        PaletteIndex(0)
        ForceShadowOff(1)
        RotationAngle(45000)
        physicsXImpulse(28000)
        physicsYImpulse(-28000)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 2)
        uponSendToLabel(CORNERED, 3)
    label(0)
    sprite('vrbnef406_004', 4)
    sprite('vrbnef406_005', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(-33)
    YAccel(-150)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('bnef_kugi_hit', -1)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    sprite('vrbnef406_006_dummy', 3)
    Visibility(1)
    loopRest()
    ExitState()
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(33)
    YAccel(-100)
    CreateParticle('bnef_kugi_hit', -1)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    sprite('vrbnef406_006_dummy', 3)
    Visibility(1)
    loopRest()
    ExitState()
    label(3)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    clearUponHandler(CORNERED)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    XImpulseAcceleration(-33)
    YAccel(150)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('bnef_kugi_hit', -1)
    uponSendToLabel(LANDING, 2)
    sprite('null', 2)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_kugi_fire', -1)
    clearUponHandler(LANDING)
    sprite('vrbnef406_006_dummy', 3)
    Visibility(1)
    loopRest()


@State
def shotCD_Matome():
    sprite('shot_expoint', 60)
    CreateObject('bn_shot_C', 1)
    ObjectUpon(STATE_END, 33)
    SLOT_31 = SLOT_31 + -1
    ParticleRotationAngle(45000)
    CallCustomizableParticle('bnef_kugi_pitch', 1)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_C', 1)
        ObjectUpon(STATE_END, 32)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(60000)
        CallCustomizableParticle('bnef_kugi_pitch', 2)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_C', 1)
        ObjectUpon(STATE_END, 34)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(30000)
        CallCustomizableParticle('bnef_kugi_pitch', 0)


@State
def bn_shot_C():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(84)
        AirPushbackX(2500)
        AirPushbackY(10000)
        Hitstop(0)
        EnemyHitstopAddition(20, 40, 40)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        CollideWithWall(1)
        ContinueState(120)
        Size(1250)
        PaletteIndex(0)
        ForceShadowOff(1)
        StarterRating(2)
        HitsparkSize(500)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        PushbackX(1000)
        RotationAngle(45000)
        physicsXImpulse(18000)
        physicsYImpulse(-18000)
        RotationAngle(70000)
        physicsXImpulse(12000)
        physicsYImpulse(-48000)

        def upon_32():
            RotationAngle(60000)
            physicsXImpulse(14000)
            physicsYImpulse(-24248)

        def upon_33():
            RotationAngle(45000)
            physicsXImpulse(18000)
            physicsYImpulse(-18000)

        def upon_34():
            RotationAngle(30000)
            physicsXImpulse(24248)
            physicsYImpulse(-14000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            CreateObject('bn_shot_C_hit', -1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 2)
        uponSendToLabel(LANDING, 2)

        def upon_39():
            NoAttackDuringAction(1)
    label(0)
    sprite('vrbnef406_006', 4)
    sprite('vrbnef406_007', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    sprite('null', 1)
    CreateObject('bn_shot_reflect', -1)


@State
def bn_shot_C_hit():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        Size(1250)
        BlendMode_Normal()
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('null', 60)
    CreateParticle('bnef_kugi_web_bom', -1)
    CreateObject('bn_shot_C_web1', -1)
    CreateObject('bn_shot_C_web2', -1)
    CreateObject('bn_shot_C_web3', -1)
    CreateObject('bn_shot_C_web4', -1)
    CreateObject('bn_shot_C_web5', -1)
    CreateObject('bn_shot_C_web6', -1)


@State
def bn_shot_C_web1():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 15)
    XPositionRelativeFacing(128000)
    AbsoluteY(192000)
    DeviationX(0, 64000)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 30)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_shot_C_web2():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 10)
    XPositionRelativeFacing(-128000)
    AbsoluteY(192000)
    DeviationX(-64000, 0)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_shot_C_web3():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 15)
    XPositionRelativeFacing(64000)
    AbsoluteY(128000)
    DeviationX(0, 32000)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 30)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_shot_C_web4():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 10)
    XPositionRelativeFacing(-64000)
    AbsoluteY(128000)
    DeviationX(-32000, 0)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_shot_C_web5():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 10)
    XPositionRelativeFacing(64000)
    AbsoluteY(320000)
    DeviationX(32000, 0)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 25)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_shot_C_web6():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(22)
        FaceLeft()
        BlendMode_Add()
        ContinueState(60)
    sprite('vrbnef406_090', 10)
    XPositionRelativeFacing(-64000)
    AbsoluteY(256000)
    DeviationX(-32000, 0)
    DeviationY(-16000, 16000)
    RandRotationAngle()
    Size(0)
    SetScaleSpeed(50)
    CreateObject('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    SetScaleSpeed(0)
    sprite('vrbnef406_090', 15)
    ConstantAlphaModifier(-16)


@State
def bn_kugi_web_smoke():

    def upon_IMMEDIATE():
        ContinueState(60)
    sprite('null', 1)
    CreateParticle('bnef_kugi_web_smoke', -1)


@State
def shotD_Matome():
    sprite('shot_expoint', 60)
    CreateObject('bn_shot_D', 1)
    ObjectUpon(STATE_END, 33)
    SLOT_31 = SLOT_31 + -1
    ParticleRotationAngle(45000)
    CallCustomizableParticle('bnef_kugi_pitch', 1)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_D', 2)
        ObjectUpon(STATE_END, 32)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(60000)
        CallCustomizableParticle('bnef_kugi_pitch', 2)
    if SLOT_31 >= 1:
        CreateObject('bn_shot_D', 0)
        ObjectUpon(STATE_END, 34)
        SLOT_31 = SLOT_31 + -1
        ParticleRotationAngle(30000)
        CallCustomizableParticle('bnef_kugi_pitch', 0)


@State
def bn_shot_D():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(94)
        Hitstop(0)
        EnemyHitstopAddition(5, 5, 5)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        CollideWithWall(1)
        ContinueState(360)
        Size(1250)
        PaletteIndex(0)
        ForceShadowOff(1)
        StarterRating(2)
        HitsparkSize(500)
        Unknown12052(1)
        VoodooDamageMultiplier(2)
        Size(1250)
        AirPushbackX(14000)
        AirPushbackY(-10000)

        def upon_32():
            RotationAngle(60000)
            physicsXImpulse(14000)
            physicsYImpulse(-24248)

            def upon_LANDING():
                RotationAngle(-60000)
                PrivateFunction(2, 2, 13, 0, -1, 2, 13)
                CreateParticle('bnef_kugi_hit', -1)
                AirPushbackY(12000)

        def upon_33():
            RotationAngle(45000)
            physicsXImpulse(18000)
            physicsYImpulse(-18000)

            def upon_LANDING():
                RotationAngle(-45000)
                PrivateFunction(2, 2, 13, 0, -1, 2, 13)
                CreateParticle('bnef_kugi_hit', -1)
                AirPushbackY(12000)

        def upon_34():
            RotationAngle(30000)
            physicsXImpulse(24248)
            physicsYImpulse(-14000)

            def upon_LANDING():
                RotationAngle(-30000)
                PrivateFunction(2, 2, 13, 0, -1, 2, 13)
                CreateParticle('bnef_kugi_hit', -1)
                AirPushbackY(12000)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 2)

        def upon_39():
            NoAttackDuringAction(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_008', 4)
    sprite('vrbnef406_009', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    sprite('null', 1)
    CreateObject('bn_shot_reflect', -1)


@State
def bn_shot_E():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Hitstop(0)
        PaletteIndex(0)
        CollideWithWall(1)
        ContinueState(120)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 2)
    Size(1250)
    RotationAngle(30000)
    physicsXImpulse(24248)
    physicsYImpulse(-14000)
    label(0)
    sprite('vrbnef406_010', 4)
    sprite('vrbnef406_011', 4)
    gotoLabel(0)
    label(1)
    CreateObject('bn_shot_reflect', -1)
    gotoLabel(3)
    label(2)
    CreateObject('bn_shot_reflect', -1)
    label(3)


@State
def bn_stuck_wheel():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        ForceShadowOff(1)
        FaceLeft()
        PaletteIndex(4)
        BlendMode_Add()
        SetZVal(3999)
        XPositionRelativeFacing(13000)
        AbsoluteY(29000)
        E0EAEffect('cmn_judgment', 65535)

        def RunOnObject_1():
            AbsoluteY(100000)
        uponSendToLabel(32, 90)

        def upon_33():
            AddRotationPerFrame(1000)

        def upon_34():
            AddRotationPerFrame(200)

        def upon_53():
            Visibility(1)
    sprite('vrbnef407_90', 16)
    Size(0)
    SetScaleSpeed(31)
    AddRotationPerFrame(3000)
    sprite('vrbnef407_90', 2)
    Size(500)
    SetScaleSpeed(0)
    label(10)
    sprite('vrbnef407_90', 1)
    loopRest()
    gotoLabel(10)
    label(90)
    clearUponHandler(32)
    sprite('vrbnef407_90', 16)
    ConstantAlphaModifier(-16)
    SetScaleSpeed(31)


@State
def bn_stuck_Big():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        ForceShadowOff(1)
        FaceLeft()
        PaletteIndex(4)
        BlendMode_Add()
        SetZVal(3999)
        XPositionRelativeFacing(13000)
        AbsoluteY(29000)
    sprite('vrbnef407_90', 15)
    Size(500)
    SetScaleSpeed(80)
    AddRotationPerFrame(6000)
    ConstantAlphaModifier(-17)


@State
def bn_stuck():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        BlendMode_Normal()
        SetZVal(4000)
        WallCollisionDetection(1)
        uponSendToLabel(32, 90)

        def upon_34():
            AddX(-180000)
            AddY(450000)

        def upon_35():
            AddX(200000)
            AddY(450000)

        def upon_36():
            AddX(580000)
            AddY(450000)

        def upon_37():
            AddX(200000)
            AddY(200000)
            CopyFromRightToLeft(23, 2, 51, 3, 2, 25)
            if SLOT_51 < 370000:
                XPositionRelativeFacing(1750000)

        def upon_39():
            AddX(-380000)
            AddY(270000)
            CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
            if SLOT_51 < 350000:
                AbsoluteY(350000)

        def upon_40():
            AddY(270000)
            CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
            if SLOT_51 < 350000:
                AbsoluteY(350000)

        def upon_41():
            AddX(380000)
            AddY(270000)
            CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
            if SLOT_51 < 350000:
                AbsoluteY(350000)

        def upon_33():
            AddY(120000)
            CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
            if SLOT_51 < 350000:
                AbsoluteY(350000)

        def upon_38():
            CreateObject('bn_stuck_Big', -1)
            SLOT_2 = SLOT_2 + 5
            SLOT_52 = SLOT_52 + 1
            if SLOT_52 == 1:
                ObjectUpon(FALLING, 33)
                sendToLabel(1)
            if SLOT_52 == 2:
                ObjectUpon(FALLING, 34)
                sendToLabel(2)
            if SLOT_52 == 3:
                sendToLabel(90)

        def upon_45():
            if SLOT_2:
                ObjectUpon2(23, 38, 0)
                SLOT_2 = SLOT_2 + -1

        def upon_53():
            Visibility(1)
    sprite('null', 1)
    sprite('vrbnef407_001', 4)
    FaceLeft()
    Size(1000)
    AlphaValue(0)
    ConstantAlphaModifier(16)
    PrivateSE('bnse_00')
    LinkParticle('bnef_kugi_stuck')
    CreateObject('bn_stuck_wheel', -1)
    RegisterObject(4, 1)
    sprite('vrbnef407_002', 4)
    sprite('vrbnef407_003', 4)
    label(0)
    sprite('vrbnef407_001', 4)
    sprite('vrbnef407_002', 4)
    sprite('vrbnef407_003', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef407_004', 6)
    sprite('vrbnef407_005', 6)
    sprite('vrbnef407_006', 6)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('vrbnef407_007', 32767)
    label(90)
    sprite('vrbnef407_007', 12)
    ConstantAlphaModifier(-21)
    ObjectUpon(FALLING, 32)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)


@State
def bn_DD_1_ray_speed():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        XPositionRelativeFacing(0)
        AbsoluteY(288000)
        ContinueState(44)
    label(0)
    sprite('null', 1)
    ParticleFacing(2)
    CallCustomizableParticle('bnef_DD_1_ray', -1)
    gotoLabel(0)


@State
def bn_DD_1_ray_center():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        ContinueState(12)
    label(0)
    sprite('null', 1)
    CreateObject('bn_DD_1_ray_center_line', -1)
    gotoLabel(0)


@State
def bn_DD_1_ray_center2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        ContinueState(113)
    label(0)
    sprite('null', 1)
    CreateObject('bn_DD_1_ray_center_line', -1)
    gotoLabel(0)


@State
def bn_DD_1_ray_center_line():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        SetPosXByScreenPer(50)
        AbsoluteY(288000)
    ParticleLayer(1)
    CallCustomizableParticle('ef_speed_center', -1)


@State
def bn_DD_1_bomber():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    CommonSE('016_explode_2')
    CommonSE('015_blaze_2')
    ScreenShake(0, 128000)
    XPositionRelativeFacing(0)
    CreateParticle('bnef_DD_1_bomber', -1)


@State
def bn_DD_3_cutin():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(3)
        FaceLeft()
        RenderLayer(3)
        AbsoluteY(256000)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('vrbnef432_21', 4)
    SetScaleY(0)
    SetScaleSpeedY(250)
    AlphaValue(0)
    ConstantAlphaModifier(14)
    StopCharacterFlash1(16777215)
    CharacterFlash2(-16777216, 20)
    sprite('vrbnef432_21', 16)
    SetScaleSpeedY(0)
    sprite('vrbnef432_21', 57)
    StopCharacterFlash2()
    SetScaleY(1000)


@State
def bn_DD_3_face():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(3)
        FaceLeft()
        RenderLayer(3)
        PaletteIndex(0)
        AbsoluteY(256000)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 7)
    sprite('vrbnef432_20', 15)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrbnef432_20', 55)
    CreateObject('eyefire_l', 0)
    CreateObject('eyefire_r', 1)
    sprite('null', 1)


@State
def eyefire_l():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('null', 55)
    ParticleLayer(1)
    CallPrivateEffect('bnef_DD_3_eyefire')
    CommonSE('015_blaze_1')


@State
def eyefire_r():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('null', 55)
    ParticleLayer(1)
    CallPrivateEffect('bnef_DD_3_eyefire')


@State
def bn_DD_3_ray():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        ContinueState(150)
    label(0)
    sprite('null', 1)
    CreateObject('bn_DD_3_ray_line', -1)
    gotoLabel(0)


@State
def bn_DD_3_ray_line():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        AbsoluteY(320000)
    ParticleLayer(1)
    CallCustomizableParticle('ef_speed_center', -1)


@State
def bn_DD_3_rock():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
    sprite('null', 1)
    ParticleLayer(2)
    CallCustomizableParticle('bnef_DD_3_rock', -1)


@State
def bn_DD_3_fire():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        AbsoluteY(41000)
    sprite('null', 10)
    sprite('null', 1)
    ParticleLayer(2)
    CallCustomizableParticle('bnef_DD_3_fire', -1)


@State
def FuRinKaZan():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        IgnoreScreenfreeze(1)
        ContinueState(150)
        Size(1950)
    sprite('null', 2)
    sprite('null', 10)
    CreateObject('3DEFF_Fu', -1)
    CreateObject('3DEFF_Rin', -1)
    CreateObject('3DEFF_Ka', -1)
    CreateObject('3DEFF_Zan', -1)
    SetScaleSpeed(-2)
    sprite('null', 6)
    SetScaleSpeed(-120)
    sprite('null', 2)
    SetScaleSpeed(0)
    Size(900)
    sprite('null', 2)
    Size(1000)
    sprite('null', 2)
    Size(900)
    sprite('null', 90)
    sprite('null', 30)
    SetScaleSpeed(100)


@State
def __3DEFF_Fu():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        BlendMode_Normal()
        AddX(-360000)
        AbsoluteY(520000)
        RenderLayer(4)
        Eff3DEffect('ef_fu_BN.DIG', 'ef_fu_BN_motion_000.mmot')
    sprite('null', 15)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    StopCharacterFlash1(0)
    CharacterFlash(16777215, 30, 2)
    sprite('null', 15)
    CreateParticle('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    physicsXImpulse(-80000)
    physicsYImpulse(60000)


@State
def __3DEFF_Rin():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        BlendMode_Normal()
        AddX(-380000)
        AbsoluteY(150000)
        RenderLayer(4)
        Eff3DEffect('ef_rin_BN.DIG', 'ef_rin_BN_motion_000.mmot')
    sprite('null', 15)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    StopCharacterFlash1(0)
    CharacterFlash(16777215, 30, 2)
    sprite('null', 15)
    CreateParticle('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    physicsXImpulse(-80000)
    physicsYImpulse(-60000)


@State
def __3DEFF_Ka():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        BlendMode_Normal()
        AddX(360000)
        AbsoluteY(520000)
        RenderLayer(4)
        Eff3DEffect('ef_ka_BN.DIG', 'ef_ka_BN_motion_000.mmot')
    sprite('null', 15)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    StopCharacterFlash1(0)
    CharacterFlash(16777215, 30, 2)
    sprite('null', 15)
    CreateParticle('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    physicsXImpulse(80000)
    physicsYImpulse(60000)


@State
def __3DEFF_Zan():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        BlendMode_Normal()
        AddX(380000)
        AbsoluteY(160000)
        RenderLayer(4)
        Eff3DEffect('ef_zan_BN.DIG', 'ef_zan_BN_motion_000.mmot')
    sprite('null', 15)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    StopCharacterFlash1(0)
    CharacterFlash(16777215, 30, 2)
    sprite('null', 15)
    CreateParticle('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    physicsXImpulse(80000)
    physicsYImpulse(-60000)


@State
def bn_DD_2_hold():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(0)
        IgnoreScreenfreeze(1)
    sprite('vrbnef431_000', 3)
    RotationAngle(60000)


@State
def bn_DD_2():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        uponSendToLabel(PLAYER_DAMAGED, 99)
        physicsYImpulse(9629)
        CopyFromRightToLeft(23, 2, 51, 22, 2, 22)
        PrivateFunction(1, 2, 22, 2, 51, 2, 51)
        if SLOT_IsFacingRight:
            PrivateFunction(3, 2, 51, 0, 40, 2, 12)
        else:
            PrivateFunction(3, 2, 51, 0, -40, 2, 12)
    sprite('vrbnef431_000', 27)
    AddRotationPerFrame(-27000)
    sprite('null', 1)
    clearUponHandler(PLAYER_DAMAGED)
    ForceFaceSprite()
    AddRotationPerFrame(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CreateObject('bn_DD_2_open', -1)
    CommonSE('019_cloth_b')
    CommonSE('019_cloth_b')
    IgnoreScreenfreeze(0)
    loopRest()
    ExitState()
    label(99)
    clearUponHandler(PLAYER_DAMAGED)
    sprite('vrbnef431_005', 3)
    CommonSE('019_cloth_b')
    physicsYImpulse(0)
    sprite('vrbnef431_000', 3)
    sprite('vrbnef431_000', 10)
    RotationAngle(30000)
    AddRotationPerFrame(1000)
    physicsYImpulse(10000)
    setGravity(2000)
    sprite('vrbnef431_000', 30)
    ConstantAlphaModifier(-12)


@State
def bn_DD_2_open():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        BlendMode_Normal()
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
        if SLOT_31 == 0:
            SLOT_51 = 0
        if SLOT_31 >= 1:
            SLOT_31 = SLOT_31 + -1
            SLOT_51 = 6
        FaceLeft()

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(23, 2, 52, 22, 2, 22)
            PrivateFunction(1, 2, 22, 2, 52, 2, 52)
            PrivateFunction(3, 2, 52, 0, 50, 2, 12)

        def upon_14():
            Unknown23090(23)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(54)
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(39)
            SLOT_51 = 0
            XImpulseAcceleration(0)
            sendToLabel(580)

        def upon_53():
            sendToLabel(99)
        uponSendToLabel(39, 99)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 3)
    sprite('vrbnef431_004', 1)
    if not SLOT_51:
        notConditionalSendToLabel(99)
    label(1)
    sprite('vrbnef431_001', 2)
    CreateObject('bn_DD_2_kugi', -1)
    CommonSE('007_swing_knife_0')
    sprite('vrbnef431_002', 2)
    CreateObject('bn_DD_2_kugi', -1)
    sprite('vrbnef431_003', 2)
    CreateObject('bn_DD_2_kugi', -1)
    CommonSE('007_swing_knife_1')
    sprite('vrbnef431_004', 1)
    CreateObject('bn_DD_2_kugi', -1)
    sprite('vrbnef431_004', 1)
    SLOT_51 = SLOT_51 + -1
    if not SLOT_51:
        if SLOT_53 < 3:
            if SLOT_31 >= 1:
                SLOT_31 = SLOT_31 + -1
                SLOT_51 = SLOT_51 + 3
                SLOT_53 = SLOT_53 + 1
    if not SLOT_51:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(1)
    label(99)
    SLOT_51 = 0
    clearUponHandler(54)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(39)
    sprite('vrbnef431_001', 3)
    XImpulseAcceleration(90)
    sprite('vrbnef431_002', 3)
    XImpulseAcceleration(90)
    sprite('vrbnef431_003', 3)
    XImpulseAcceleration(90)
    sprite('vrbnef431_004', 3)
    XImpulseAcceleration(90)
    sprite('vrbnef431_001', 4)
    XImpulseAcceleration(60)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_005', 3)
    CommonSE('019_cloth_b')
    XImpulseAcceleration(0)
    physicsYImpulse(0)
    sprite('vrbnef431_000', 3)
    label(580)
    sprite('vrbnef431_000', 10)
    RotationAngle(30000)
    AddRotationPerFrame(1000)
    physicsYImpulse(10000)
    setGravity(2000)
    sprite('vrbnef431_000', 30)
    ConstantAlphaModifier(-12)


@State
def bn_DD_2_kugi():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        ForceShadowOff(1)
        PaletteIndex(0)
        BlendMode_Normal()
        UseSlashHitspark(1)
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(1)
        AttackP2(60)
        SingleProration(1)
        VoodooDamageMultiplier(2)
        EnemyHitstopAddition(1, 1, 1)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(1000)
        PushbackX(4000)
        AttackDirection(2)
        MoveAttributes(0, 0, 0, 1, 0)
        HitsparkSize(250)
        StarterRating(2)
        Unknown12052(1)
        AddY(80000)
        DeviationX(-160000, 160000)
        RotationAngle(90000)
        SetScaleX(875)
        SetScaleY(800)
        physicsYImpulse(-48000)
        ContinueState(180)
        SetZLine(0, 10)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        uponSendToLabel(LANDING, 2)

        def upon_39():
            NoAttackDuringAction(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_000', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef406_001', 1)
    AlphaValue(255)
    ConstantAlphaModifier(-4)
    AddRotationPerFrame(-15000)
    YSpeed(30000)
    XSpeed(-10000)
    setGravity(2400)
    sprite('vrbnef406_001', 32767)
    loopRest()
    label(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(LANDING)
    sprite('null', 1)
    CreateParticle('bnef_kugi_hit', -1)


@State
def bn_Warp():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    AddY(180000)
    CreateParticle('bnef_sp_throw_speed', -1)
    CreateParticle('bnef_sp_throw_leaf', -1)
    sprite('null', 1)
    CreateParticle('bnef_sp_throw_speed', -1)


@State
def bn_D_stand():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef203_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('vrbnef203_00', 6)
    AlphaValue(255)
    ConstantAlphaModifier(-42)


@State
def bn_D_stand2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef203_10', 2)
    sprite('vrbnef203_11', 2)
    sprite('vrbnef203_12', 3)
    sprite('vrbnef203_13', 3)


@State
def bn_D_front():

    def upon_IMMEDIATE():
        AddX(56000)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef213_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(42)
    sprite('vrbnef213_00', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-42)


@State
def bn_D_front2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef213_10', 2)
    sprite('vrbnef213_11', 2)
    sprite('vrbnef213_12', 2)
    sprite('vrbnef213_13', 2)
    sprite('vrbnef213_14', 1)


@State
def bn_D_crouch():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef233_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(42)
    sprite('vrbnef233_00', 6)
    AlphaValue(255)
    ConstantAlphaModifier(-42)


@State
def bn_D_crouch2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef233_10', 3)
    sprite('vrbnef233_11', 2)
    sprite('vrbnef233_12', 2)
    sprite('vrbnef233_13', 2)
    sprite('vrbnef233_14', 2)


@State
def bn_D_jump():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
        AddY(-13000)
    sprite('vrbnef253_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(42)
    sprite('vrbnef253_00', 3)
    AlphaValue(255)
    ConstantAlphaModifier(-42)


@State
def bn_D_jump2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrbnef253_10', 1)
    sprite('vrbnef253_11', 2)
    sprite('vrbnef253_12', 2)
    sprite('vrbnef253_13', 2)
    sprite('vrbnef253_14', 2)


@State
def bn_D_1():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
    sprite('vrbnef432_50', 16)
    BlendMode_Normal()
    FaceLeft()
    Size(1000)
    SetScaleSpeed(40)
    AlphaValue(255)
    ConstantAlphaModifier(-21)
    ParticleLayer(1)
    CallCustomizableParticle('bnef_D_flash', 0)


@State
def bn_D_2():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
    sprite('vrbnef432_51', 16)
    BlendMode_Normal()
    FaceLeft()
    Size(1000)
    SetScaleSpeed(40)
    AlphaValue(255)
    ConstantAlphaModifier(-21)
    ParticleLayer(1)
    CallCustomizableParticle('bnef_D_flash', 0)


@State
def bn_D_3():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
    sprite('vrbnef432_52', 16)
    BlendMode_Normal()
    FaceLeft()
    Size(1000)
    SetScaleSpeed(40)
    AlphaValue(255)
    ConstantAlphaModifier(-21)
    ParticleLayer(1)
    CallCustomizableParticle('bnef_D_flash', 0)


@State
def bn_D_4():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
    sprite('vrbnef432_53', 16)
    BlendMode_Normal()
    FaceLeft()
    Size(1000)
    SetScaleSpeed(40)
    AlphaValue(255)
    ConstantAlphaModifier(-21)
    ParticleLayer(1)
    CallCustomizableParticle('bnef_D_flash', 0)


@State
def bn_D_max():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
        if SLOT_YDistanceFromFloor <= 204000:
            AbsoluteY(205000)
    sprite('vrbnef432_90', 16)
    BlendMode_Normal()
    FaceLeft()
    Size(1000)
    AlphaValue(255)
    ParticleLayer(1)
    CallCustomizableParticle('bnef_D_flash2', 0)
    sprite('vrbnef432_90', 16)
    ConstantAlphaModifier(-16)


@State
def EventBN01_iblc():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        PaletteIndex(3)
    label(0)
    sprite('lc000_00', 5)
    sprite('lc000_01', 5)
    sprite('lc000_02', 5)
    sprite('lc000_03', 5)
    sprite('lc000_04', 5)
    sprite('lc000_05', 5)
    sprite('lc000_06', 5)
    sprite('lc000_07', 5)
    sprite('lc000_08', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc003_00', 2)
    Flip()
    sprite('lc003_01', 2)
    sprite('lc003_02', 2)
    sprite('lc032_00', 3)
    physicsXImpulse(20000)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    DashEffects(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)


@State
def BunshinAttackObject1():

    def upon_IMMEDIATE():
        SetZLine(0, 50)
        CreateObject('BunshinAttackObject2', -1)
        RenderLayer(4)
        EnableAfterimage(1)
    sprite('bn022_00', 2)
    physicsYImpulse(60000)
    physicsXImpulse(-30000)
    setGravity(0)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)


@State
def BunshinAttackObject2():

    def upon_IMMEDIATE():
        Flip()
        SetZLine(0, 50)
        RenderLayer(4)
        EnableAfterimage(1)
    sprite('bn022_00', 2)
    physicsYImpulse(60000)
    physicsXImpulse(-30000)
    setGravity(0)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)


@State
def BN433WhiteOut():

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
def BunshinX2():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-228000)
        AbsoluteY(880000)
        physicsYImpulse(22000)
    sprite('null', 30)
    CreateObject('BunshinAttackObject3', -1)
    CreateObject('BunshinAttackObject4', -1)
    sprite('null', 200)
    physicsYImpulse(0)


@State
def BunshinAttackObject3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(22)
        SetZVal(500)
        BlendMode_Normal()
        AddX(-320000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(12)
    sprite('bn022_01', 1)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    CommonSE('019_cloth_a')
    sprite('bn022_03', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_04', 4)
    YAccel(0)
    XImpulseAcceleration(50)
    sprite('bn022_05', 4)
    XImpulseAcceleration(0)
    sprite('bn022_06', 5)
    sprite('bn433_11', 5)
    sprite('bn433_12', 5)
    CommonSE('019_cloth_b')
    sprite('bn433_13', 5)
    sprite('bn433_14', 28)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)


@State
def BunshinAttackObject4():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(2)
        IgnorePauses(22)
        SetZVal(-500)
        BlendMode_Normal()
        AddX(-780000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(12)
    sprite('bn022_01', 1)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    CommonSE('019_cloth_c')
    sprite('bn022_03', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_04', 4)
    YAccel(0)
    XImpulseAcceleration(50)
    sprite('bn022_05', 4)
    XImpulseAcceleration(0)
    sprite('bn022_06', 5)
    sprite('bn433_11', 5)
    CommonSE('019_cloth_b')
    sprite('bn433_12', 5)
    sprite('bn433_13', 5)
    sprite('bn433_14', 28)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)


@State
def BunshinTodomeEff():

    def upon_IMMEDIATE():
        LinkParticle('bnef_xatk')
        AddY(160000)
    sprite('null', 8)
    CreateObject('BN433WhiteOut', -1)


@State
def BunshinTodome():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(3700)
        MinimumDamage(25)
        AirUntechableTime(300)
        HardKnockdown(65)
        Hitstop(15)
        AttackP2(40)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(1000)
        CHStateIfCHStart(3)
        StarterRating(2)
        TeleportToObject(22)
        Visibility(1)
    sprite('vrdmy_bunshin', 3)
    CreateObject('BunshinTodomeEff', -1)


@State
def BunshinX2OD():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-228000)
        AbsoluteY(880000)
        physicsYImpulse(22000)
    sprite('null', 30)
    CreateObject('BunshinAttackObject3OD', -1)
    CreateObject('BunshinAttackObject4OD', -1)
    sprite('null', 200)
    physicsYImpulse(0)


@State
def BunshinAttackObject3OD():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(22)
        SetZVal(500)
        BlendMode_Normal()
        AddX(-320000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(12)
        EnableCollision(0)
    sprite('bn352_00', 2)
    physicsXImpulse(72000)
    physicsYImpulse(64000)
    sprite('bn352_01', 2)
    CommonSE('000_airdash_2')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn355_00', 2)
    Flip()
    physicsXImpulse(120000)
    physicsYImpulse(-70000)
    sprite('bn355_01', 2)
    CommonSE('000_airdash_2')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn358_00', 2)
    Flip()
    physicsXImpulse(170000)
    physicsYImpulse(0)
    sprite('bn358_01', 2)
    CommonSE('000_airdash_2')
    sprite('bn358_02', 2)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn355_00', 2)
    Flip()
    physicsXImpulse(120000)
    physicsYImpulse(-40000)
    sprite('bn355_01', 2)
    CommonSE('000_airdash_2')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn352_00', 2)
    Flip()
    physicsXImpulse(52000)
    physicsYImpulse(35000)
    sprite('bn352_01', 2)
    CommonSE('000_airdash_2')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_00', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    PrivateSE('bnse_09')
    sprite('bn022_00', 2)
    Flip()
    physicsXImpulse(0)
    physicsYImpulse(22000)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_03', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_04', 4)
    YAccel(0)
    XImpulseAcceleration(50)
    sprite('bn022_05', 4)
    XImpulseAcceleration(0)
    sprite('bn022_06', 3)
    sprite('bn433_11', 3)
    sprite('bn433_12', 3)
    sprite('bn433_13', 3)
    sprite('bn433_14', 23)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)


@State
def BunshinAttackObject4OD():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(2)
        IgnorePauses(22)
        SetZVal(-500)
        BlendMode_Normal()
        AddX(-780000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(12)
    sprite('bn352_00', 2)
    physicsXImpulse(72000)
    physicsYImpulse(64000)
    sprite('bn352_01', 2)
    CommonSE('000_airdash_1')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn352_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn355_00', 2)
    Flip()
    physicsXImpulse(120000)
    physicsYImpulse(-70000)
    sprite('bn355_01', 2)
    CommonSE('000_airdash_1')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn358_00', 2)
    Flip()
    physicsXImpulse(170000)
    physicsYImpulse(0)
    sprite('bn358_01', 2)
    CommonSE('000_airdash_1')
    sprite('bn358_02', 2)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn358_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn355_00', 2)
    Flip()
    physicsXImpulse(120000)
    physicsYImpulse(-40000)
    sprite('bn355_01', 2)
    CommonSE('000_airdash_1')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('bn355_03', 2)
    XImpulseAcceleration(50)
    YAccel(50)
    PrivateSE('bnse_09')
    sprite('bn352_00', 2)
    Flip()
    physicsXImpulse(52000)
    physicsYImpulse(35000)
    sprite('bn352_01', 2)
    CommonSE('000_airdash_1')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_00', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    PrivateSE('bnse_09')
    sprite('bn022_00', 2)
    Flip()
    physicsXImpulse(0)
    physicsYImpulse(22000)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_03', 4)
    YAccel(50)
    XImpulseAcceleration(50)
    sprite('bn022_04', 4)
    YAccel(0)
    XImpulseAcceleration(50)
    sprite('bn022_05', 4)
    XImpulseAcceleration(0)
    sprite('bn022_06', 3)
    sprite('bn433_11', 3)
    sprite('bn433_12', 3)
    sprite('bn433_13', 3)
    sprite('bn433_14', 23)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)


@State
def BunshinTodomeOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(4167)
        MinimumDamage(25)
        AirUntechableTime(300)
        HardKnockdown(65)
        Hitstop(15)
        AttackP2(40)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(1000)
        CHStateIfCHStart(3)
        TeleportToObject(22)
        Visibility(1)
        AttackType(4)
        StarterRating(2)
    sprite('vrdmy_bunshin', 3)
    CreateObject('BunshinTodomeEff', -1)


@State
def Hibashira():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('bnef_hibashira')
        CreateObject('Hibashira_front', -1)
        RotationAngle(10000)
        AddX(64000)
        SetScaleY(1500)
        SetScaleX(1500)
    sprite('null', 3)
    SetScaleY(500)
    sprite('null', 200)
    SetScaleY(1500)
    CreateObject('Terikaeshi', -1)


@State
def Hibashira_front():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        IgnorePauses(2)
        E0EAEffectRotation(2)
        LinkParticle('bnef_hibashira_front')
        AlphaValue(200)
    sprite('null', 32767)


@State
def Hibashira_option():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        LinkParticle('bnef_hibashira_yuka')
        SetScaleX(1250)
    sprite('null', 300)


@State
def Terikaeshi():

    def upon_IMMEDIATE():
        Size(10000)
        AlphaValue(255)
        ConstantAlphaModifier(-10)
        AbsoluteY(64000)
    sprite('vref_env', 300)


@State
def LookAtPosBN433():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraFast(1)
        CameraControlEnable(1)
    sprite('null', 32767)


@State
def __434TRetrunKugi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        E0EAEffectPosition(22)
        IgnorePauses(2)
        AddY(340000)
        RotationAngle(-180000)
    sprite('vrbnef434_kugi00', 12)
    physicsYImpulse(-15000)
    AddRotationPerFrame(-28000)


@State
def __434ThrowKubi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        E0EAEffectPosition(22)
        IgnorePauses(2)
        AddY(-240000)
        SetZVal(500)
    sprite('vrbnef434_kugi00', 12)
    sprite('vrbnef434_kugi01', 29)
    AddY(-235000)
    sprite('vrbnef434_kugi01', 20)
    Visibility(1)
    sprite('vrbnef434_kugi01', 70)
    Visibility(0)
    sprite('vrbnef434_kugi01', 21)
    physicsYImpulse(30000)
    physicsXImpulse(-5000)
    AddRotationPerFrame(-10000)


@State
def __434PowNacEfff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('bnef_434pownac_add')
        uponSendToLabel(32, 0)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __434rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_rock', '')
        Size(1200)
        AddY(150000)
        TeleportToObject(22)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __434HitImpact():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_hitfire', '')
        Size(1200)
        AddY(-150000)
        AlphaValue(0)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(2)
    sprite('null', 5)
    ParticleRotationAngle(180000)
    CallCustomizableParticle('bnef_434atk00_smoke', -1)
    sprite('null', 5)
    CreateParticle('bnef_434lstatk_pos', -1)
    IgnorePauses(2)
    IgnoreScreenfreeze(0)
    AlphaValue(255)
    sprite('null', 35)
    sprite('null', 14)
    ConstantAlphaModifier(-26)


@State
def bn_AH_fusuma_r():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceRight()
        XPositionRelativeFacing(640000)
        AbsoluteY(640000)
        SetZVal(-100)
        PaletteIndex(4)
    sprite('vrbnef450_00', 8)
    SetScaleX(-2000)
    SetScaleY(2000)
    physicsYImpulse(-128000)
    sprite('vrbnef450_00', 30)
    ScreenShake(0, 16000)
    physicsYImpulse(0)
    sprite('vrbnef450_00', 16)
    SetScaleXPerFrame(-93)
    SetScaleSpeedY(93)
    physicsXImpulse(48000)


@State
def bn_AH_fusuma_l():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceRight()
        SetScaleX(-1000)
        XPositionRelativeFacing(640000)
        AbsoluteY(640000)
        SetZVal(-100)
        PaletteIndex(4)
    sprite('vrbnef450_00', 8)
    SetScaleX(2000)
    SetScaleY(2000)
    physicsYImpulse(-128000)
    sprite('vrbnef450_00', 30)
    physicsYImpulse(0)
    ScreenShake(0, 16000)
    sprite('vrbnef450_00', 16)
    SetScaleXPerFrame(93)
    SetScaleSpeedY(93)
    physicsXImpulse(-48000)


@State
def bn_AH_fusuma_r_open():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceRight()
        SetZVal(0)
        XPositionRelativeFacing(640000)
        AbsoluteY(-384000)
        PaletteIndex(4)
    sprite('vrbnef450_00', 16)
    SetScaleX(-1500)
    SetScaleY(1500)
    SetScaleXPerFrame(-93)
    SetScaleSpeedY(93)
    sprite('vrbnef450_00', 16)
    SetZVal(-100)
    physicsXImpulse(48000)


@State
def bn_AH_fusuma_l_open():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceRight()
        SetZVal(0)
        XPositionRelativeFacing(640000)
        AbsoluteY(-384000)
        PaletteIndex(4)
    sprite('vrbnef450_00', 16)
    SetScaleX(1500)
    SetScaleY(1500)
    SetScaleXPerFrame(93)
    SetScaleSpeedY(93)
    sprite('vrbnef450_00', 16)
    SetZVal(-100)
    physicsXImpulse(-48000)


@State
def bn_AH_faceup():

    def upon_IMMEDIATE():
        uponSendToLabel(17, 1)
        if SLOT_43:
            RunLoopUpon(17, 70)
            ContinueState(110)
        else:
            RunLoopUpon(17, 200)
            ContinueState(240)
        RenderLayer(11)
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(2)
        Size(1050)
        XPositionRelativeFacing(-640000)
        AbsoluteY(-384000)
    CreateObject('bn_AH_ray2', -1)
    label(0)
    sprite('vrbnef450_face00', 2)
    sprite('vrbnef450_face01', 2)
    sprite('vrbnef450_face02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    CreateObject('AstFaceCutinWhiteOut', -1)
    label(2)
    sprite('vrbnef450_face01', 2)
    sprite('vrbnef450_face02', 2)
    sprite('vrbnef450_face00', 2)
    loopRest()
    gotoLabel(2)


@State
def AstFaceCutinWhiteOut():

    def upon_IMMEDIATE():
        SetZVal(-1000)
        RemoveOnCallStateEnd(2)
        RenderLayer(4)
        BlendMode_Add()
        AlphaValue(0)
        Size(20000)
    sprite('vr_white', 25)
    ConstantAlphaModifier(10)
    sprite('vr_white', 32767)


@State
def bn_AH_kugi():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(0)
        AddX(-16000)
        AddY(216000)
    sprite('vrbnef450_kugi', 60)


@State
def bn_AH_kugi2():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    sprite('vrbnef450_kugi', 120)


@State
def bn_AH_Thunder():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ScreenPosition(1)
        FaceLeft()
        PaletteIndex(5)
        BlendMode_Add()
        SetZVal(4000)
        XPositionRelativeFacing(-1280000)
        AbsoluteY(-360000)
        Size(3000)
        SetScaleSpeedY(-100)
    sprite('vrbnef450_90', 2)
    CommonSE('015_blaze_2')
    CommonSE('006_swing_blade_2')
    CommonSE('010_swing_sword_2')
    CommonSE('006_swing_blade_1')
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    Size(0)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)


@State
def bn_AH_bomber():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(80)
    sprite('null', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_astbomber', -1)
    ScreenShake(0, 16000)
    CommonSE('016_explode_2')
    CommonSE('015_blaze_2')
    sprite('null', 1)
    ParticleSize(1500)
    CallCustomizableParticle('bnef_astbomber', -1)
    sprite('null', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_astbomber', -1)


@State
def bn_AH_UnderFire():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        AddY(240000)
        CallPrivateEffect('bnef_ast_groundfire')
    sprite('null', 32767)


@State
def bn_AH_ray():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        AbsoluteY(308000)
        ParticleLayer(4)
        CallPrivateEffect('ef_speedline_wt')
    sprite('null', 120)


@State
def bn_AH_ray2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        SetPosXByScreenPer(50)
        AddX(1790000)
        AbsoluteY(580000)
        Size(1250)
        ParticleLayer(4)
        CallPrivateEffect('ef_speedline_bk')
    sprite('null', 60)


@State
def bn_AH_HandFire():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        ContinueState(30)
        E0EAEffectPosition(2)
        CallPrivateEffect('bnef_ast_handfire')
    sprite('null', 1)


@State
def AstStartBlackOut():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        AbsoluteY(256000)
        SetZVal(500)
        BlendMode_Normal()
        AlphaValue(0)
        SetScaleX(5000)
        SetScaleY(1500)
        ColorForTransition(4278190080)
    sprite('vr_white', 10)
    sprite('vr_white', 20)
    ConstantAlphaModifier(13)
    sprite('vr_white', 128)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-9)


@State
def AstStartWhiteOut():

    def upon_IMMEDIATE():
        SetZVal(-1000)
        BlendMode_Add()
        AlphaValue(0)
        Size(20000)
    sprite('vr_white', 20)
    ConstantAlphaModifier(15)
    sprite('vr_white', 45)
    sprite('vr_white', 20)
    AlphaValue(200)
    ConstantAlphaModifier(-10)


@State
def AstWhiteOut():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        AbsoluteY(2048000)
        SetZVal(5)
        BlendMode_Add()
        AlphaValue(255)
        Size(20000)
    sprite('vr_white', 15)
    sprite('vr_white', 20)
    AlphaValue(200)
    ConstantAlphaModifier(-10)


@State
def AstFinishWhiteOut():

    def upon_IMMEDIATE():
        RenderLayer(1)
        SetPosXByScreenPer(50)
        AbsoluteY(256000)
        SetZVal(-1000)
        BlendMode_Add()
        AlphaValue(255)
        SetScaleX(5000)
        SetScaleY(1500)
    sprite('vr_white', 90)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-9)


@State
def AstFinishAtk():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        ContinueState(100)
        XPositionRelativeFacing(-6400000)
        StopCharacterFlash1(0)
        CharacterFlash2(16777215, 100)
        EnableAfterimage(0)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(8)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1100)
    sprite('bn450_13', 4)
    CreateObject('LookAtPosAtk', -1)
    sprite('bn450_14', 4)
    CommonSE('000_airdash_2')
    label(0)
    physicsXImpulse(64000)
    EnableAfterimage(1)
    sprite('bn450_17', 1)
    CreateObject('bn_AH_HandFire', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_ast_handfire', 2)
    ScreenShake(0, 5000)
    CommonSE('015_blaze_0')
    CommonSE('015_blaze_1')
    CommonSE('016_explode_0')
    sprite('bn450_17', 1)
    CreateObject('bn_AH_HandFire', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_ast_handfire', 2)
    sprite('bn450_16', 1)
    CreateObject('bn_AH_HandFire', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_ast_handfire', 2)
    sprite('bn450_16', 1)
    CreateObject('bn_AH_HandFire', 1)
    ParticleSize(2000)
    CallCustomizableParticle('bnef_ast_handfire', 2)
    loopRest()
    gotoLabel(0)


@State
def LookAtPosAtk():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraFast(1)
        CameraControlEnable(1)
        CameraForAstralHeat(40, 150)
        AddX(512000)
        AddY(220000)
    sprite('null', 40)


@State
def LookAtPos():

    def upon_IMMEDIATE():
        CameraFast(1)
        CameraControlEnable(1)
        CameraControlInfinity(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('null', 32767)


@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        Visibility(1)
        ParticleLayer(5)
        CallPrivateEffect('rlef_ashlock_mc')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        Visibility(1)
        CallPrivateEffect('rlef_ashlock_aura')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def BurstDD_Matome():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
        SetActionMark(2)
    if SLOT_51:
        conditionalSendToLabel(1)
    label(0)
    sprite('null', 5)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 32)
    sprite('null', 5)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 33)
    sprite('null', 5)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 34)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    SetActionMark(2)
    label(2)
    sprite('null', 5)
    AddActionMark(-1)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 32)
    sprite('null', 5)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 33)
    sprite('null', 5)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 34)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2)
    sprite('null', 1)
    SetActionMark(2)
    label(3)
    sprite('null', 3)
    AddActionMark(-1)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 32)
    sprite('null', 3)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 33)
    sprite('null', 3)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 34)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(3)
    label(4)
    sprite('null', 2)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 32)
    sprite('null', 2)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 33)
    sprite('null', 2)
    CreateObject('BurstDD_Shot', 0)
    ObjectUpon(STATE_END, 34)
    loopRest()
    gotoLabel(4)


@State
def BurstDD_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(50)
        MinimumDamage(10)
        AttackP2(100)
        ChipPercentage(0)
        HeatGainMultiplier(0)
        Hitstop(0)
        PushbackX(1000)
        Hitstun(60)
        Stagger(100)
        Crumple(100)
        HardKnockdown(100)
        UseSlashHitspark(1)
        HitsparkSize(400)
        PassByArmor(1)
        DefeatOpponentBehavior(1)
        VoodooDamageMultiplier(2)
        CHStateIfCHStart(3)
        DamageFromStateOnly('BurstDD_Shot')
        OnlyHitPlayer(1)
        ContinueState(120)
        ScreenShake(4000, 4000)
        RemoveOnCallStateEnd(3)
        if random_(2, 0, 16):
            DeviationY(70000, 90000)
            RotationAngle(356000)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 20):
            DeviationY(100000, 120000)
            RotationAngle(356000)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 25):
            DeviationY(150000, 170000)
            RotationAngle(0)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 33):
            DeviationY(200000, 220000)
            RotationAngle(0)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        elif random_(2, 0, 50):
            DeviationY(250000, 270000)
            RotationAngle(4000)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        else:
            DeviationY(300000, 320000)
            RotationAngle(4000)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        XSpeed2(50000, 0)
        RandSpeedX(10000, 20000)
        HitsPerCall(1, 1, 1, 0, 0, 0, 0, 0)
        uponSendToLabel(54, 9)

        def upon_32():
            EnableAfterimage(1)
            AfterimageCount(6)
            sendToLabel(0)

        def upon_33():
            EnableAfterimage(1)
            AfterimageCount(3)
            sendToLabel(1)

        def upon_34():
            EnableAfterimage(1)
            AfterimageCount(6)
            sendToLabel(2)

        def upon_36():
            clearUponHandler(54)
            clearUponHandler(OPPONENT_HIT)
            Damage(1500)
            AttackType(4)
            EnemyHitstopAddition(6, 6, 6)
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirUntechableTime(300)
            HardKnockdown(10)
            AirPushbackX(0)
            DefeatOpponentBehavior(0)
            UseSlashHitspark(0)
            UseFireHitspark(1)
            HitsparkSize(1000)
            Visibility(1)
            EndMomentum(1)
            TeleportToObject(22)
            AbsoluteY(0)
            sendToLabel(3)

        def upon_37():
            Damage(3300)
            HardKnockdown(30)
            AirPushbackY(80000)
            SetActionMark(1)

        def upon_OPPONENT_HIT():
            SLOT_8 = SLOT_8 + -1
            if SLOT_8 <= 0:
                clearUponHandler(OPPONENT_HIT)
                GroundedHitstunAnimation(2)
                AirHitstunAnimation(2)
                TriggerUponForState('BurstDDAdd', 34)

        def upon_EVERY_FRAME():
            if SLOT_8 <= -1:
                clearUponHandler(EVERY_FRAME)
                AttackOff()
    sprite('null', 1)
    label(0)
    sprite('vrbnef440_00', 2)
    sprite('vrbnef440_01', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef440_10', 32767)
    loopRest()
    label(2)
    sprite('vrbnef440_20', 32767)
    loopRest()
    label(3)
    sprite('vrbnef440_30', 3)
    CommonSE('016_explode_2')
    CommonSE('015_blaze_2')
    sprite('vrbnef440_30', 3)
    RefreshMultihit()
    CommonSE('016_explode_2')
    CommonSE('015_blaze_2')
    AddCombo(1)
    sprite('vrbnef440_30', 3)
    if SLOT_2:
        CommonSE('016_explode_2')
        CommonSE('015_blaze_2')
        AddCombo(1)
    sprite('vrbnef440_30', 3)
    if SLOT_2:
        CommonSE('016_explode_2')
        CommonSE('015_blaze_2')
        AddCombo(1)
    ExitState()
    label(9)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    sprite('keep', 12)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        AddX(230000)
    sprite('null', 15)
    sprite('null', 32767)
    E0EAEffectPosition(0)


@State
def BurstDD_syuriken():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        AfterimageCount(6)
    label(0)
    sprite('vrbnef440_00', 2)
    sprite('vrbnef440_01', 2)
    gotoLabel(0)


@State
def BurstDD_kunai():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        AfterimageCount(3)
    sprite('vrbnef440_10', 32767)


@State
def BurstDD_kugi():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        AfterimageCount(6)
    sprite('vrbnef440_20', 32767)


@State
def BurstDD_bomb():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        EnableAfterimage(1)
        AfterimageCount(6)
        PaletteIndex(4)
        AttackOff()

        def upon_32():
            RandSpeedX(8000, 9000)
            RandSpeedY(27000, 28000)
            RandAddGravity(1200, 1300)

        def upon_33():
            RotationAngle(315000)
            RandSpeedX(5000, 6000)
            RandSpeedY(24000, 25000)
            RandAddGravity(1100, 1200)

        def upon_34():
            RotationAngle(280000)
            RandSpeedX(5000, 6000)
            RandSpeedY(30000, 31000)
            RandAddGravity(1300, 1400)

        def upon_35():
            RotationAngle(30000)
            RandSpeedX(4000, 5000)
            RandSpeedY(33000, 35000)
            RandAddGravity(1400, 1500)

        def upon_EVERY_FRAME():
            if SLOT_YDistanceFromFloor <= 40000:
                clearUponHandler(EVERY_FRAME)
                EndMomentum(1)
                AbsoluteY(40000)
    sprite('vrbnef440_30', 1)
    sprite('vrbnef440_30', 32767)
    CreateObject('BurstDDSpark', 0)


@State
def BurstDDSpark():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('bnef_440spark00')
    sprite('null', 32767)


@State
def BurstDDKaton():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_440fire00_BN', '')
        TeleportToObject(22)
        SetScaleX(100)
        SetScaleZ(100)
        Visibility(1)
        uponSendToLabel(32, 0)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_434atk00_hasira00', -1)
    SetScaleXPerFrame(90)
    SetScaleSpeedZ(90)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 7)
    CreateObject('BurstDDKatonSubMato', -1)
    sprite('vrbnef440_firepos', 32767)
    SetScaleXPerFrame(0)
    SetScaleSpeedZ(0)
    label(0)
    sprite('vrbnef440_firepos', 10)
    ConstantAlphaModifier(-26)
    SetScaleXPerFrame(-45)
    SetScaleSpeedY(85)
    SetScaleSpeedZ(-45)
    TriggerUponForState('BurstDDKatonSubMato', 32)


@State
def BurstDDKatonSubMato():

    def upon_IMMEDIATE():
        Visibility(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        LinkParticle('bnef_440_gbloom')
    label(0)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 7)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 0)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 1)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 2)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 3)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 4)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 5)
    sprite('vrbnef440_firepos', 2)
    CreateParticle('bnef_440katon', 6)
    gotoLabel(0)
    label(1)
    sprite('vrbnef440_firepos', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(300)


@State
def BurstDDBomb():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        SetScaleSpeed(18)
        SetScaleX(1500)
        SetScaleY(1000)
    sprite('null', 4)
    CreateObject('BurstDDBombsub2', -1)
    ScreenShake(10000, 10000)
    sprite('null', 4)
    CreateObject('BurstDDBombsub', -1)
    ScreenShake(10000, 10000)


@State
def BurstDDBombEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        SetScaleX(2200)
        SetScaleY(1800)
    sprite('null', 4)
    CreateObject('BurstDDBombsub2', -1)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    CreateObject('BurstDDBombsub', -1)
    ScreenShake(20000, 20000)


@State
def BurstDDBombsub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_440bomb00_BN', '')
        IgnorePauses(2)
        E0EAEffectScale(2)
    sprite('null', 4)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def BurstDDBombsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_440bomb00_BN', '')
        IgnorePauses(2)
        E0EAEffectScale(2)
    sprite('null', 11)
    CreateParticle('bnef_434atk00_impact01', -1)
    CreateParticle('bnef_440_ray', -1)
    sprite('null', 10)
    CreateParticle('bnef_440bomb', -1)


@State
def bnef_411_atk():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(70)
        AirUntechableTime(80)
        Hitstop(2)
        EnemyHitstopAddition(13, 13, 21)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(35000)
        YImpulseBeforeWallbounce(1400)
        PushbackX(12000)
        UseFireHitspark(1)
        FatalCounter(1)
        StarterRating(2)
        Unknown12052(1)
        Size(1500)
        DamageEffect(4, '')
    sprite('vrbnef411_atk', 3)
    AttackOff()
    CreateObject('bnef_411_bomber', -1)
    CreateObject('bnef_411_cloth', -1)
    CommonSE('016_explode_2')
    ScreenShake(5000, 20000)
    sprite('vrbnef411_atk', 12)
    RefreshMultihit()


@State
def bnef_411_bomber():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        E0EAEffectScale(2)
        ParticleLayer(6)
        CallPrivateEffect('bnef_411bomber')
    sprite('null', 80)


@State
def bnef_411_cloth():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        ForceShadowOff(1)
        RenderLayer(7)
    sprite('vrbnef411_00', 4)
    sprite('vrbnef411_01', 4)
    sprite('vrbnef411_02', 2)
    sprite('vrbnef411_02', 2)
    ParticleColorFromPalette(12, 12, 12)
    CallCustomizableParticle('bnef_411_cloth_pos', -1)
    sprite('vrbnef411_03', 4)
    sprite('vrbnef411_04', 2)
    sprite('vrbnef411_04', 2)
    ParticleColorFromPalette(12, 12, 12)
    CallCustomizableParticle('bnef_411_cloth_pos', -1)


@State
def EventBNvsTBStandLC():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        PaletteIndex(3)
        SetZVal(500)
    sprite('lc000_00', 5)
    label(0)
    sprite('lc000_01', 5)
    sprite('lc000_02', 5)
    sprite('lc000_03', 5)
    sprite('lc000_04', 5)
    sprite('lc000_05', 5)
    sprite('lc000_06', 5)
    sprite('lc000_07', 5)
    sprite('lc000_08', 5)
    sprite('lc000_00', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc033_00', 1)
    sprite('lc033_00', 2)
    physicsXImpulse(-24000)
    physicsYImpulse(18000)
    JumpEffects(3, 0)
    sprite('lc033_01', 2)
    sprite('lc033_02', 3)
    setGravity(850)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    label(1)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Event_Headache():

    def upon_IMMEDIATE():
        TeleportToObject(3)
        AddY(360000)
    sprite('null', 1)
    CommonSE('014_electric_ll')
    ParticleSize(500)
    CallCustomizableParticle('ef_hits', -1)


@State
def Event_Kuginasi():
    sprite('null', 3)
    SetZVal(500)
    sprite('bn063_11ex', 32767)


@State
def Act2Event_CreatePT():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        uponSendToLabel(34, 3)
        AddX(-100000)
        LoadSpritePalette(0)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt200_00', 2)
    sprite('pt200_01', 3)
    CommonSE('003_swing_grap_0_0')
    sprite('pt200_02', 16)
    CreateParticle('ef_exhit_sub', 0)
    CommonSE('100_hit_grap_0')
    ScreenShake(4000, 6000)
    sprite('pt200_02', 2)
    ObjectUpon(LANDING, 35)
    sprite('pt200_03', 3)
    sprite('pt200_04', 4)
    sprite('pt200_05', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('pt003_00', 3)
    Flip()
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    loopRest()
    gotoLabel(0)
    label(3)
    sprite('pt032_02', 4)
    physicsXImpulse(-26200)
    Flip()
    CommonSE('000_airdash_1')
    sprite('pt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_04', 4)
    sprite('pt032_05', 4)
    sprite('pt032_06', 4)
    loopRest()


@State
def Act2Event_PTCamera():
    sprite('null', 32767)
    CameraControlEnable(1)
    uponSendToLabel(32, 1)
    AddX(-200000)
    loopRest()
    label(1)
    sprite('null', 20)


@State
def Act3Event_TeniObj():

    def upon_IMMEDIATE():
        AddY(100000)
    sprite('null', 80)
    CreateParticle('story_teni', 100)
    CommonSE('000_airdash_2')
    CommonSE('022_magiccircle_b')
    sprite('null', 3)
    CreateParticle('haef_event_lose_end', 103)
    loopRest()
